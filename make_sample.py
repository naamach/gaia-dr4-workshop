"""Regenerate the Gaia DR3 nominal 100 pc sample used in the DR4 workshop tutorial.

Runs the same ADQL query the tutorial shows (all gaia_source columns, parallax > 10 mas,
parallax_over_error > 10, BP/RP flux_over_error > 10) as an asynchronous job on the ESA
Gaia archive and writes the result as FITS (fast to load in TOPCAT) and CSV.

Usage:
    python make_sample.py [outdir]
"""
import sys
from pathlib import Path

from astroquery.gaia import Gaia

QUERY = """
SELECT *
FROM gaiadr3.gaia_source
WHERE parallax_over_error > 10
AND phot_bp_mean_flux_over_error > 10
AND phot_rp_mean_flux_over_error > 10
AND parallax > 10
"""

def main(outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    Gaia.ROW_LIMIT = -1
    job = Gaia.launch_job_async(QUERY, dump_to_file=False)
    table = job.get_results()
    print(f"{len(table)} rows, {len(table.colnames)} columns")
    table.write(outdir / "GaiaDR3_100pc.fits", overwrite=True)
    table.write(outdir / "GaiaDR3_100pc.csv", overwrite=True)
    print("written to", outdir)

if __name__ == "__main__":
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else Path("."))
