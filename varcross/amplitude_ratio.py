import pandas as pd

def compute_g_amplitude_ratio(rv_df, phot_df, threshold=0.01):
    """
    Computes A_vrad / A_G ratio using Gaia DR3 radial velocity and G-band amplitude.

    Parameters:
        rv_df (DataFrame): must contain 'source_id' and 'radial_velocity'
        phot_df (DataFrame): must contain 'source_id' and 'amp_G'
        threshold (float): minimum ratio to select candidates

    Returns:
        DataFrame: filtered candidates with source_id and amplitude ratio
    """
    merged = pd.merge(rv_df, phot_df, on="source_id", how="inner")
    if "amp_G" not in merged.columns:
        raise ValueError("Photometric amplitude column 'amp_G' not found.")

    merged["amplitude_ratio"] = merged["radial_velocity"] / merged["amp_G"]
    selected = merged[merged["amplitude_ratio"] > threshold]
    return selected[["source_id", "amplitude_ratio"]]
