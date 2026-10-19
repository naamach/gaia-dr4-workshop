# Data for the tutorial

- `GaiaDR3_100pc.fits` (190 MB) is **not** in the repository (GitHub's 100 MB file limit). Download it from the
  release assets, https://github.com/naamach/gaia-dr4-workshop/releases/latest/download/GaiaDR3_100pc.fits, into this folder,
  or regenerate it with `python make_sample.py data` (asynchronous job on the ESA Gaia archive; log in, or use
  the ARI-Gaia mirror as shown in the notebook). Query: Gaia DR3 `gaia_source`, all columns, `parallax > 10`,
  `parallax_over_error > 10`, BP and RP `flux_over_error > 10` (306,517 rows).
- `table_20pc_WDs.csv`: the Gaia DR2 20 pc white dwarf sample of Hollands et al. (2018), MNRAS 480, 3942.
- `datalink/`, `datalink_rrlyr/`, `xp_continuous_20pc_wds.fits`, `xp_continuous_cvs.fits`: Gaia DR3 Datalink
  products (XP spectra, RVS spectrum, epoch photometry) cached by the notebook so it runs without live archive
  access. Delete them to force a fresh download.
