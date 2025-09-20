# varcross/simbad_lookup.py

from astroquery.simbad import Simbad

def get_gaia_ids_from_file(filepath):
    """
    Reads OGLE object names from a file and retrieves Gaia DR3 names and source_ids via Simbad.

    Parameters:
        filepath (str): Path to a text file containing OGLE names, one per line.

    Returns:
        dict: {
            "OGLE LMC-CEP-227": {"gaia_name": "Gaia DR3 4654937339840486528", "id": "4654937339840486528"},
            ...
        }
        If no Gaia DR3 match is found, value is None.
    """
    results = {}
    with open(filepath, 'r') as f:
        ogle_names = [line.strip() for line in f if line.strip()]
    
    for name in ogle_names:
        try:
            ids = Simbad.query_objectids(name)
            if ids is None:
                results[name] = None
                continue
            gaia_dr3 = [row['id'] for row in ids if 'Gaia DR3' in row['id']]
            if gaia_dr3:
                full_name = gaia_dr3[0]
                source_id = full_name.split()[-1]
                results[name] = {"gaia_name": full_name, "id": source_id}
            else:
                results[name] = None
        except Exception:
            results[name] = None
    return results
