import json
import numpy as np


def create_diatomic_molecule_geometry(species1, species2, bond_length):
    """Create a molecular geometry for a diatomic molecule.

    Args:
        species1 (str): Chemical symbol of the first atom, e.g. 'H'.
        species2 (str): Chemical symbol of the second atom.
        bond_length (float): bond distance.

    Returns:
        dict: a dictionary containing the coordinates of the atoms.
    """

    geometry = {
        "sites": [
            {"species": species1, "x": 0, "y": 0, "z": 0},
            {"species": species2, "x": 0, "y": 0, "z": bond_length},
        ]
    }

    return geometry


def create_diatomic_molecule(species1, species2, bond_length):
    geometry = create_diatomic_molecule_geometry(species1, species2, bond_length)
    geometry["schema"] = "molecular_geometry"
    with open("molecule.json", "w") as f:
        f.write(json.dumps(geometry))


def create_multiple_diatomic_molecules(species1, species2, bond_length, n_points, scale1, scale2):
    init_bond_length = scale1 * bond_length 
    final_bond_length = scale2 * bond_length 

    geometry = {}
    geometry["schema"] = "molecular_geometry_along_pes"
    geometry["n_points"] = n_points
    geometry["geometry_along_pes"] = {}
    

    for idx, r in enumerate(np.linspace(init_bond_length, final_bond_length, n_points)):
        single_point_geometry = create_diatomic_molecule_geometry(species1, species2, r)
        geometry["geometry_along_pes"][idx] = single_point_geometry
        
    with open("molecule_pes.json".format(str(idx)), "w") as f:
        f.write(json.dumps(geometry))
