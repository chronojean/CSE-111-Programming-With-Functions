#I created my own split-formula function using make_dict , A print_array function that works accordingly
#Validated some small answers to help the program work properly
#Created a dict for known formulas (make_known_molecules)
#Uncomment line 105 (compound using BYU formula) AND Comment lines 106 Compount and 110 to get normal output and use the given formula
import os, platform, formula

def clear_cls():
    """Use the clear terminal function for Linux or Windows"""
    sistema_operativo = platform.system()
    if sistema_operativo == "Windows":
        os.system('cls')
    elif sistema_operativo == "Linux":
        os.system('clear')
    else:
        print("Undetermined OS")
        
def make_periodic_table():
    return {"Ac": ["Actinum", 227],"Ag": ["Silver", 107.8682],"Al": ["Aluminum", 26.9815386],"Ar": ["Argon", 39.948],"As": ["Arsenic", 74.9216],"At": ["Astatine", 210],"Au": ["Gold", 196.966569],"B": ["Boron", 10.811],"Ba": ["Barium", 137.327],"Be": ["Beryllium", 9.012182],"Bi": ["Bismuth", 208.9804],"Br": ["Bromine", 79.904],"C": ["Carbon", 12.0107],"Ca": ["Calcium", 40.078],"Cd": ["Cadmium", 112.411],"Ce": ["Cerium", 140.116],"Cl": ["Chlorine", 35.453],"Co": ["Cobalt", 58.933195],"Cr": ["Chromium", 51.9961],"Cs": ["Cesium", 132.9054519],"Cu": ["Copper", 63.546],"Dy": ["Dysprosium", 162.5],"Er": ["Erbium", 167.259],"Eu": ["Europium", 151.964],"F": ["Fluorine", 18.9984032],"Fe": ["Iron", 55.845],"Fr": ["Francium", 223],"Ga": ["Gallium", 69.723],"Gd": ["Gadolinium", 157.25],"Ge": ["Germanium", 72.64],"H": ["Hydrogen", 1.00794],"He": ["Helium", 4.002602],"Hf": ["Hafnium", 178.49],"Hg": ["Mercury", 200.59],"Ho": ["Holmium", 164.93032],"I": ["Iodine", 126.90447],"In": ["Indium", 114.818],"Ir": ["Iridium", 192.217],"K": ["Potassium", 39.0983],"Kr": ["Krypton", 83.798],"La": ["Lanthanum", 138.90547],"Li": ["Lithium", 6.941],"Lu": ["Lutetium", 174.9668],"Mg": ["Magnesium", 24.305],"Mn": ["Manganese", 54.938045],"Mo": ["Molybdenum", 95.96],"N": ["Nitrogen", 14.0067],"Na": ["Sodium", 22.98976928],"Nb": ["Niobium", 92.90638],"Nd": ["Neodymium", 144.242],"Ne": ["Neon", 20.1797],"Ni": ["Nickel", 58.6934],"Np": ["Neptunium", 237],"O": ["Oxygen", 15.9994],"Os": ["Osmium", 190.23],"P": ["Phosphorus", 30.973762],"Pa": ["Protactinium", 231.03588],"Pb": ["Lead", 207.2],"Pd": ["Palladium", 106.42],"Pm": ["Promethium", 145],"Po": ["Polonium", 209],"Pr": ["Praseodymium", 140.90765],"Pt": ["Platinum", 195.084],"Pu": ["Plutonium", 244],"Ra": ["Radium", 226],"Rb": ["Rubidium", 85.4678],"Re": ["Rhenium", 186.207],"Rh": ["Rhodium", 102.9055],"Rn": ["Radon", 222],"Ru": ["Ruthenium", 101.07],"S": ["Sulfur", 32.065],"Sb": ["Antimony", 121.76],"Sc": ["Scandium", 44.955912],"Se": ["Selenium", 78.96],"Si": ["Silicon", 28.0855],"Sm": ["Samarium", 150.36],"Sn": ["Tin", 118.71],"Sr": ["Strontium", 87.62],"Ta": ["Tantalum", 180.94788],"Tb": ["Terbium", 158.92535],"Tc": ["Technetium", 98],"Te": ["Tellurium", 127.6],"Th": ["Thorium", 232.03806],"Ti": ["Titanium", 47.867],"Tl": ["Thallium", 204.3833],"Tm": ["Thulium", 168.93421],"U": ["Uranium", 238.02891],"V": ["Vanadium", 50.9415],"W": ["Tungsten", 183.84],"Xe": ["Xenon", 131.293],"Y": ["Yttrium", 88.90585],"Yb": ["Ytterbium", 173.054],"Zn": ["Zinc", 65.38],"Zr": ["Zirconium", 91.224]}

def make_known_molecules():
    return {"Al2O3": "aluminum oxide","CH3OH": "methanol","C2H6O": "ethanol","C2H5OH": "ethanol","C3H8O": "isopropyl alcohol","C3H8": "propane","C4H10": "butane","C6H6": "benzene","C6H14": "hexane","C8H18": "octane","CH3(CH2)6CH3": "octane","C13H18O2": "ibuprofen","C13H16N2O2": "melatonin","Fe2O3": "iron oxide","FeS2": "iron pyrite","H2O": "water"}

def get_element_data(element):
    elements = make_periodic_table()
    return elements[element]

def break_down_formula(str_formula):

    stripping_formula = str_formula

    arr_formula = []

    buff = ""
    element = ""
    n_atoms = ""

    while len(stripping_formula) != 0:
        buff = stripping_formula[0]
        stripping_formula = stripping_formula[1:]   

        if (element == "" and buff.isupper()) or (element != "" and buff.islower()):
            element += buff
        elif element != "" and buff.isnumeric():
            n_atoms += buff
        elif element != "" and buff.isupper():
            element_data = get_element_data(element)
            arr_formula.append([element,int(n_atoms) if n_atoms != "" else 1, element_data[0], element_data[1]])
            element = buff
            n_atoms = ""

    if element != "":
        element_data = get_element_data(element)
        arr_formula.append([element,int(n_atoms) if n_atoms != "" else 1, element_data[0], element_data[1]])
    return arr_formula

def print_elements(arr_compound,name="Unknown"):
    titles="Nº Atoms:\tElement:\tAtomic Mass:\tSymbol:"
    print("\t\tMolecule: "+name)
    print("-"*len(titles)*2)
    print(titles)
    print("-"*len(titles)*2)
    for _ in arr_compound:
        print(f"{_[1]}",end="\t" if len(str(_[1]))>=8 else "\t\t")
        print(f"{_[2]}",end="\t" if len(_[2])>=8 else "\t\t")
        print(f"{_[3]}",end="\t" if len(str(_[3]))>=8 else "\t\t")
        print(f"   {_[0]}")

def compute_molar_mass(compound,elements):
    molar_mass = 0
    for element in compound:
        molar_mass += element[1]*elements[element[0]][1]
    return molar_mass         

def get_formula_name(formula, known_molecules_dict):
    """Try to find formula in the known_molecules_dict.
    If formula is in the known_molecules_dict, return
    the name of the chemical formula; otherwise return
    "unknown compound".

    Parameters
        formula is a string that contains a chemical formula
        known_molecules_dict is a dictionary that contains
            known chemical formulas and their names
    Return: the name of a chemical formula
    """
    return known_molecules_dict[formula] if formula in known_molecules_dict else "Unknown"


def main():
    clear_cls()
    sample_formula = input("Type the formule of your molecule: ")
    if(sample_formula.islower()):
        print("Formulas are Case sensitive, this formula has no uppercase.")
        return
    elif("0" in sample_formula):
        ans = input("A Zero character (0) has been found. Maybe you wanted to type O for Oxygen. Y/N: ").upper()
        if ans == "Y":
            return
    sample_mass = float(input("Type the mass in grams of a sample of the substance (such as 3.71): ")) 
    if(sample_mass<0):
        print("A negative mass is not allowed")
        return
    
    elements = make_periodic_table()
    #compound = formula.parse_formula(sample_formula,elements)    
    compound = break_down_formula(sample_formula)    
    molar_mass = compute_molar_mass(compound,make_periodic_table())
    moles = sample_mass/molar_mass if sample_mass!= 0 and molar_mass != 0 else "Can't be determined"
    print()
    print_elements(compound,get_formula_name(sample_formula,make_known_molecules()).title())
    print(f"\nMolar mass: {molar_mass}")
    print(f"Moles: {moles}")
    print()    

if __name__ == "__main__":
    main()
