# Source and assumption ledger

Status: conditional-support; exposed development evidence.

- Official products: https://science.nrao.edu/science/surveys/vla-angst/data-products
  DDO125 row, natural/robust column density and moments 1/2. Original links
  use HTTP; normal TLS-verified HTTPS on the identical host is available.
- Ott et al. (2012), AJ 144,123: https://arxiv.org/html/1208.3737v1
  supplies observing/processing metadata, centers and moment definitions.
  Moment maps use masked, flux-rescaled, primary-beam-corrected products.
  The publicly offered cubes differ and cannot reproduce the maps by a
  naive channel sum. Noise/beam/flow contamination of moment 2 is explicit.
- Stil and Israel (2002): https://arxiv.org/html/astro-ph/0203133v1
  Table3 gives DDO125 PAkin=135 +/-2 and PAHI=118 +/-2 degrees; Table5
  gives globally averaged corrected Gaussian widths 6.2 and 7.3 +/-1.5
  km/s. The latter +/- is spatial scatter. This is neither a local sigma_R
  profile nor the same operation as the Ott second moment.
- Existing campaign source supplies distance2.59 Mpc, i=63 +/-3 degrees,
  the R=.94 kpc finite-matrix point, and the already checked necessary
  pressure correction. No new theory parameter is fitted here.
- New extraction choices: the finite geometry grid, annulus widths,
  paired mask and chord statistic are explicitly supplied. Different
  centers/angles are sensitivity cases, not posterior samples.
- Intrinsic pressure interpretation additionally needs steady circular
  motion, axisymmetry, isotropic radial velocity dispersion, vertical
  structure, tracer conversion and a forward beam/mask/noise model.

The new measurements constrain what the theory would need to explain;
they do not derive a matter coupling, a metric or a TOE.
