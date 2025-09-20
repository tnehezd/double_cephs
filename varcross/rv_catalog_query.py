from astroquery.vizier import Vizier
import pandas as pd

Vizier.ROW_LIMIT = -1  # no row limit

def query_rv_from_vizier(source_ids, catalog="J/A+A/635/A6/table2"):
    """
    Queries VizieR for RV data for a list of Gaia DR3 source_ids.
    Default catalog: Ming Yang et al. (2020) LMC RV survey.

    Parameters:
        source_ids (list of str): Gaia DR3 source_id values
        catalog (str): VizieR catalog ID

    Returns:
        pandas.DataFrame: with source_id, rv_value, rv_error, epoch (if available)
    """
    if not source_ids:
        return pd.DataFrame()

    id_list = [str(sid) for sid in source_ids]

    result = Vizier.query_constraints(catalog=catalog, source_id=id_list)
    if not result:
        return pd.DataFrame()

    table = result[0].to_pandas()

    # Standardize column names
    rename_map = {
        "source_id": "source_id",
        "RV": "rv_value",
        "e_RV": "rv_error",
        "Epoch": "epoch"
    }
    for key in rename_map:
        if key in table.columns:
            table.rename(columns={key: rename_map[key]}, inplace=True)

    return table[["source_id", "rv_value", "rv_error", "epoch"]]
