import os, platform

def clear_cls():
    """Use the clear terminal function for Linux or Windows"""
    # Determine the operating system
    operating_system = platform.system()
    if operating_system == "Windows":
        os.system('cls')  # Clear the terminal for Windows
    elif operating_system == "Linux":
        os.system('clear')  # Clear the terminal for Linux
    else:
        print("Undetermined OS")  # Print a message for an undetermined OS

def make_periodic_table():
    return[["Ac","Actinium",227],["Ag","Silver",107.8682],["Al","Aluminum",26.9815386],["Ar","Argon",39.948],["As","Arsenic",74.9216],["At","Astatine",210],["Au","Gold",196.966569],["B","Boron",10.811],["Ba","Barium",137.327],["Be","Beryllium",9.012182],["Bi","Bismuth",208.9804],["Br","Bromine",79.904],["C","Carbon",12.0107],["Ca","Calcium",40.078],["Cd","Cadmium",112.411],["Ce","Cerium",140.116],["Cl","Chlorine",35.453],["Co","Cobalt",58.933195],["Cr","Chromium",51.9961],["Cs","Cesium",132.9054519],["Cu","Copper",63.546],["Dy","Dysprosium",162.5],["Er","Erbium",167.259],["Eu","Europium",151.964],["F","Fluorine",18.9984032],["Fe","Iron",55.845],["Fr","Francium",223],["Ga","Gallium",69.723],["Gd","Gadolinium",157.25],["Ge","Germanium",72.64],["H","Hydrogen",1.00794],["He","Helium",4.002602],["Hf","Hafnium",178.49],["Hg","Mercury",200.59],["Ho","Holmium",164.93032],["I","Iodine",126.90447],["In","Indium",114.818],["Ir","Iridium",192.217],["K","Potassium",39.0983],["Kr","Krypton",83.798],["La","Lanthanum",138.90547],["Li","Lithium",6.941],["Lu","Lutetium",174.9668],["Mg","Magnesium",24.305],["Mn","Manganese",54.938045],["Mo","Molybdenum",95.96],["N","Nitrogen",14.0067],["Na","Sodium",22.98976928],["Nb","Niobium",92.90638],["Nd","Neodymium",144.242],["Ne","Neon",20.1797],["Ni","Nickel",58.6934],["Np","Neptunium",237],["O","Oxygen",15.9994],["Os","Osmium",190.23],["P","Phosphorus",30.973762],["Pa","Protactinium",231.03588],["Pb","Lead",207.2],["Pd","Palladium",106.42],["Pm","Promethium",145],["Po","Polonium",209],["Pr","Praseodymium",140.90765],["Pt","Platinum",195.084],["Pu","Plutonium",244],["Ra","Radium",226],["Rb","Rubidium",85.4678],["Re","Rhenium",186.207],["Rh","Rhodium",102.9055],["Rn","Radon",222],["Ru","Ruthenium",101.07],["S","Sulfur",32.065],["Sb","Antimony",121.76],["Sc","Scandium",44.955912],["Se","Selenium",78.96],["Si","Silicon",28.0855],["Sm","Samarium",150.36],["Sn","Tin",118.71],["Sr","Strontium",87.62],["Ta","Tantalum",180.94788],["Tb","Terbium",158.92535],["Tc","Technetium",98],["Te","Tellurium",127.6],["Th","Thorium",232.03806],["Ti","Titanium",47.867],["Tl","Thallium",204.3833],["Tm","Thulium",168.93421],["U","Uranium",238.02891],["V","Vanadium",50.9415],["W","Tungsten",183.84],["Xe","Xenon",131.293],["Y","Yttrium",88.90585],["Yb","Ytterbium",173.054],["Zn","Zinc",65.38],["Zr","Zirconium",91.224]]

def get_element_data(element):
    elements = make_periodic_table()
    return [ele for ele in elements if ele[0] == element][0]

def break_down_formula(str_formula):
    # Initialize the variable to store the unprocessed formula
    stripping_formula = str_formula
    # Create an empty list to store the elements of the formula
    arr_formula = []
    # Initialize buffer variables for the element and the number of atoms
    buff = ""
    element = ""
    n_atoms = ""

    # Iterate through the formula until it's empty
    while len(stripping_formula) != 0:
        # Take the first character of the unprocessed formula
        buff = stripping_formula[0]
        stripping_formula = stripping_formula[1:]

        # Check the conditions to determine if the character belongs to an element
        if (element == "" and buff.isupper()) or (element != "" and buff.islower()):
            # If no element is being set or the character is lowercase (belongs to the element),
            # add the character to the element's name
            element += buff
        elif element != "" and buff.isnumeric():
            # If an element has been set and the character is numeric, add the character to the number of atoms
            n_atoms += buff
        elif element != "" and buff.isupper():
            # If another element is found, store the data of the current element in the list
            # and update the element's name and the number of atoms
            element_data = get_element_data(element)
            arr_formula.append([int(n_atoms) if n_atoms != "" else 1, element_data[1], element_data[2]])
            element = buff
            n_atoms = ""

    # After exiting the loop, check if there is an unprocessed element left
    if element != "":
        element_data = get_element_data(element)
        arr_formula.append([int(n_atoms) if n_atoms != "" else 1, element_data[1], element_data[2]])

    # Return the list of elements with their information
    return arr_formula


def print_elements(arr_compound):
    title = "\nNº Atoms:\tElement:\tAtomic Mass:"
    print(title)
    print("-" * len(title) * 2)
    for _ in arr_compound:
        print(f"{_[0]}", end="\t" if len(str(_[0])) >= 8 else "\t\t")
        print(f"{_[1]}", end="\t" if len(_[1]) >= 8 else "\t\t")
        print(f"{_[2]}")

def compute_molar_mass(compound):
    return sum([ele[0] * ele[2] for ele in compound])

def main():
    clear_cls()
    # Test formula
    sample_formula = input("Type the formula of your molecule: ")
    sample_mass = float(input("Type the mass in grams of a sample of the substance (e.g., 3.71): "))
    compound = break_down_formula(sample_formula)
    print_elements(compound)
    molar_mass = compute_molar_mass(compound)  # Fix the function call
    print(f"\nMolar mass: {molar_mass}")
    moles = sample_mass / molar_mass
    print(f"Moles: {moles}\n")

if __name__ == "__main__":
    main()
