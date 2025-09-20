# varcross/gaia_query.py

from astroquery.gaia import Gaia
import pandas as pd

def query_gaia_dr3(source_ids):
    """
    Queries Gaia DR3 for a list of source_ids and returns selected columns.

    Parameters:
        source_ids (list of str): Gaia DR3 source_id values

    Returns:
        pandas.DataFrame: table with astrometry, photometry, RV, RUWE
    """
    if not source_ids:
        return pd.DataFrame()

    # Build comma-separated list for ADQL
    id_list = ",".join(source_ids)

    query = f"""
    SELECT
        source_id,
        ra, dec,
        parallax, parallax_error,
        pmra, pmdec,
        phot_g_mean_mag, phot_bp_mean_mag, phot_rp_mean_mag,
        radial_velocity, radial_velocity_error,
        ruwe
    FROM gaiadr3.gaia_source
    WHERE source_id IN ({id_list})
    """

    job = Gaia.launch_job_async(query)
    table = job.get_results()
    return table.to_pandas()
