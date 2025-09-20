import argparse
from varcross import simbad_lookup, gaia_query

def main():
    parser = argparse.ArgumentParser(description="Run the Varcross pipeline")
    parser.add_argument("--input", required=True, help="Path to OGLE target list (txt)")
    parser.add_argument("--output", default="gaia_results.csv", help="Output CSV file")
    args = parser.parse_args()

    # Step 1: Simbad lookup
    print("Looking up Gaia DR3 IDs via Simbad...")
    gaia_map = simbad_lookup.get_gaia_ids_from_file(args.input)

    # Step 2: Extract valid source_ids
    source_ids = [entry["id"] for entry in gaia_map.values() if entry]

    # Step 3: Gaia query
    print(f"Querying Gaia DR3 for {len(source_ids)} sources...")
    df = gaia_query.query_gaia_dr3(source_ids)

    # Step 4: Save results
    df.to_csv(args.output, index=False)
    print(f"Results saved to {args.output}")

if __name__ == "__main__":
    main()
