# Header resolution before radial calculations

The frozen protocol follows the archive web page's displayed km/s units.
Opening the files showed BUNIT=METR/SEC for both moment1 and moment2, and
JY/B*M/S for moment0. The runner must divide these values by1000 before
using km/s. Moment2 is the rms line width, not a variance. The original
protocol and download bytes stay unchanged; this note records the resolved
metadata issue before any radial statistic. Multiplying by1000 in the wrong
direction would corrupt the squared-width pressure statistic by10^12.

The standard BMAJ/BMIN/BPA keywords are absent. Every product preserves an
AIPS CLEAN history entry. Natural beam: BMAJ=.0032049deg,
BMIN=.0029528deg, BPA=-68.22deg. Robust: .0017379deg, .0015028deg,
-80.10deg. These are respectively11.53764x10.63008 and6.25644x5.41008
arcsec. Use these history values, compare to Ott Table3 rounding, and do not
interpret map pixel size1.5arcsec as angular resolution.

All maps are1024x1024 with matching SIN projection sky coordinates. Natural
products have34766 finite pixels. Robust column density has32267 while
moment1/2 have31844; the robust untrimmed moment0 has34693 including484
negative values. Each annulus therefore needs its own recorded paired mask.
Robust moment headers have a legacy BLANK=-1 keyword on floating point data:
Astropy warns that it does not apply. Actual missing values are IEEE NaNs;
finite negative/zero counts remain explicit. No mask is silently repaired.

This note resolves file interpretation, not the physical conversion from
projected line width to intrinsic radial pressure. The new maps remain
exposed development evidence.
