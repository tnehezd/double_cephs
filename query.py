from astroquery.simbad import Simbad



# Lekérdezés
result = Simbad.query_object("OGLE LMC-CEP-227")
ids = Simbad.query_objectids("OGLE LMC-CEP-227")

# print(ids)



gaia_dr3_name = [row['id'] for row in ids if 'Gaia DR3' in row['id']][0]
print(gaia_dr3_name)
