from pyscript import document, display

non_metals = {
'H': {'symbol': 'H', 'name': 'Hydrogen', 'atomic_number': 1, 'atomic_mass': 1.008},
'C': {'symbol': 'C', 'name': 'Carbon', 'atomic_number': 6, 'atomic_mass': 12.011},
'N': {'symbol': 'N', 'name': 'Nitrogen', 'atomic_number': 7, 'atomic_mass': 14.007},
'O': {'symbol': 'O', 'name': 'Oxygen', 'atomic_number': 8, 'atomic_mass': 15.999},
'F': {'symbol': 'F', 'name': 'Fluorine', 'atomic_number': 9, 'atomic_mass': 18.998},
'Ne': {'symbol': 'Ne', 'name': 'Neon', 'atomic_number': 10, 'atomic_mass': 20.180},
'P': {'symbol': 'P', 'name': 'Phosphorus', 'atomic_number': 15, 'atomic_mass': 30.974},
'S': {'symbol': 'S', 'name': 'Sulfur', 'atomic_number': 16, 'atomic_mass': 32.06},
'Cl': {'symbol': 'Cl', 'name': 'Chlorine', 'atomic_number': 17, 'atomic_mass': 35.45},
'Ar': {'symbol': 'Ar', 'name': 'Argon', 'atomic_number': 18, 'atomic_mass': 39.95},
'Se': {'symbol': 'Se', 'name': 'Selenium', 'atomic_number': 34, 'atomic_mass': 78.971},
'Br': {'symbol': 'Br', 'name': 'Bromine', 'atomic_number': 35, 'atomic_mass': 79.904},
'Kr': {'symbol': 'Kr', 'name': 'Krypton', 'atomic_number': 36, 'atomic_mass': 83.80},
'I': {'symbol': 'I', 'name': 'Iodine', 'atomic_number': 53, 'atomic_mass': 126.90},
'Xe': {'symbol': 'Xe', 'name': 'Xenon', 'atomic_number': 54, 'atomic_mass': 131.29},
}

def search_element(event):
    symbol_input = document.querySelector("#symbol-input").value.strip().capitalize()

    fallback = {
        'symbol': symbol_input,
        'name': f"Error: The symbol '{symbol_input}' does not exist in the non-metals list.",
        'atomic_number': 'N/A',
        'atomic_mass': 'N/A'
    }
    
    element = non_metals.get(symbol_input, fallback)
    
    output_div = document.querySelector("#output")
    output_div.innerHTML = ""
    
    display(f"Symbol: {element['symbol']}", target="output")
    display(f"Name: {element['name']}", target="output")
    display(f"Atomic Number: {element['atomic_number']}", target="output")
    display(f"Atomic Mass: {element['atomic_mass']}", target="output")