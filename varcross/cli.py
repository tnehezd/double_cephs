import argparse
from varcross import simbad_lookup, gaia_query, amplitude_ratio

def main():
    parser = argparse.ArgumentParser(description="Run the Varcross pipeline")
    parser.add_argument("--input", required=True, help="Path to OGLE target list (txt)")
    parser.add_argument("--output", default="gaia_results.csv", help="Output CSV file")
    parser.add_argument("--candidates", default="candidates.csv", help="Filtered candidate output")
    parser.add_argument("--threshold", type=float, default=33.0, help="Amplitude ratio threshold")
    args = parser.parse_args()

    # Step 1: Simbad lookup
    print("Looking up Gaia DR3 IDs via Simbad...")
    gaia_map = simbad_lookup.get_gaia_ids_from_file(args.input)
    source_ids = [entry["id"] for entry in gaia_map.values() if entry]

    # Step 2: Gaia query
    print(f"Querying Gaia DR3 for {len(source_ids)} sources...")
    df = gaia_query.query_gaia_dr3(source_ids)

    # Step 3: Save full Gaia results
    df.to_csv(args.output, index=False)
    print(f"Full Gaia results saved to {args.output}")

    # Step 4: Compute amplitude ratio (A_vrad / A_G)
    print("⚖️ Computing amplitude ratios...")
    phot_df = df[["source_id", "phot_g_mean_mag"]].copy()
    phot_df = phot_df.rename(columns={"phot_g_mean_mag": "amp_G"})  # TEMP: proxy for amplitude

    rv_df = df[["source_id", "radial_velocity"]].copy()
    candidates = amplitude_ratio.compute_g_amplitude_ratio(rv_df, phot_df, threshold=args.threshold)

    # Step 5: Save filtered candidates
    candidates.to_csv(args.candidates, index=False)
    print(f"🎯 {len(candidates)} candidates saved to {args.candidates}")

if __name__ == "__main__":
    main()
