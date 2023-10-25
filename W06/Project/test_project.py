import pytest, os
from datetime import datetime, timedelta
from project import es_numero, validate_data, load_history, append_to_file, obtener_resolucion_monitor_actual, get_last_n_days_values,date_short_day

def test_es_numero():
    assert es_numero("123.45") is True
    assert es_numero("0") is True
    assert es_numero("abc") is False
    assert es_numero("1.2.3") is False

def test_validate_data():
    valid_date = datetime(2023, 10, 17).date()
    assert validate_data(None, "100.00", "Income", "Valid description", valid_date) is True
    assert validate_data(None, "abc", "Income", "Invalid amount", valid_date) is False
    future_date = datetime(2024, 12, 31).date()
    assert validate_data(None, "50.00", "Outcome", "Future date", future_date) is False
    assert validate_data(None, "75.50", "Income", "", valid_date) is False

def test_load_history():
    history_data = "2023/10/15, Transaction 1, 100.00\n2023/10/16, Transaction 2, -50.50"
    with open("test_history.txt", "w") as test_file:
        test_file.write(history_data)

    loaded_data = load_history("test_history.txt")

    assert len(loaded_data) == 2
    assert loaded_data[0] == ["2023/10/15", "Transaction 1", 100.00]
    assert loaded_data[1] == ["2023/10/16", "Transaction 2", -50.50]

    loaded_data = load_history("archivo_inexistente.txt")
    assert loaded_data == []

    with open("archivo_vacio.txt", "w") as empty_file:
        pass

    loaded_data = load_history("archivo_vacio.txt")
    assert loaded_data == []

    os.remove("test_history.txt")
    os.remove("archivo_vacio.txt")

def test_append_to_file():
    test_filename = "test_append_to_file.txt"
    initial_content = "2023/10/15, Transaction 1, 100.00\n2023/10/16, Transaction 2, -50.50"
    with open(test_filename, "w") as test_file:
        test_file.write(initial_content)

    appended_line = "2023/10/17, Transaction 3, 75.25"
    new_content = append_to_file(appended_line)

    assert appended_line in new_content

    test_filename = "test_append_to_file.txt"
    appended_line = "2023/10/18, Transaction 4, 30.00"
    new_content = append_to_file(appended_line, test_filename)

    assert appended_line in new_content
    os.remove(test_filename)

def test_obtener_resolucion_monitor_actual():
    monitor_resolution = [1920, 1080]
    actual_resolution = obtener_resolucion_monitor_actual()
    assert len(actual_resolution) == 2
    assert actual_resolution == monitor_resolution

def test_get_last_n_days_values():
    current_date = datetime.now().date()
    data = [
        [current_date.strftime("%Y/%m/%d"), "Transaction 1", 100.00],
        [(current_date - timedelta(days=1)).strftime("%Y/%m/%d"), "Transaction 2", -100.00],
        [(current_date - timedelta(days=2)).strftime("%Y/%m/%d"), "Transaction 3", 100.00],
        [(current_date - timedelta(days=3)).strftime("%Y/%m/%d"), "Transaction 4", -100.00],
        [(current_date - timedelta(days=4)).strftime("%Y/%m/%d"), "Transaction 5", 100.00],
        [(current_date - timedelta(days=5)).strftime("%Y/%m/%d"), "Transaction 6", -100.00],
        [(current_date - timedelta(days=6)).strftime("%Y/%m/%d"), "Transaction 7", 100.00],
    ]

    result = get_last_n_days_values(data, 7)
    assert result == {"income": 400, "outcome": -300}

    result = get_last_n_days_values(data, 3)
    assert result == {"income": 200.00, "outcome": -200.00}

    result = get_last_n_days_values(data, 1)
    assert result == {"income": 100.00, "outcome": -100.00}

    result = get_last_n_days_values(data, 0)
    assert result == {"income": 100.00, "outcome": 0.00}
    
def test_date_short_day():
    date = "2023/10/25"
    result = date_short_day(date)
    assert result == "2023/10/25 Wed"

    date = "2023/12/01"
    result = date_short_day(date)
    assert result == "2023/12/01 Fri"

    date = "2023/08/14"
    result = date_short_day(date)
    assert result == "2023/08/14 Mon"

pytest.main(["-v", "--tb=line", "-rN", __file__])