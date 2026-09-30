# T65 results (outputs are in *_output.txt next to this file)

Deviations from PREREG.md, all disclosed in the report:
1. t65_test1: the first random-graph estimator took max/min over ~150 single-cone means and was
   noise-dominated (A 1.09-1.30). t65_test1b replaces it with a line-averaged estimator (13 lines,
   +/- pooled, 40 sources, bootstrap) and adds a Z^3 control run through the same estimator
   (1.33 at 20-degree cone resolution, exact ratio 1.73). The pre-registered threshold was kept.
2. Pre-registered expectation for 1c (integer alphabet ~10 reaches A<=1.05) was wrong: the 26-star
   floors at 1.128 even with real weights (1, sqrt2, sqrt3). 1.025 needs all vectors to max-norm 3 with Euclid weights.
3. 1b as first run capped vectors at max-norm 3, so its running minimum plateaued (1.118);
   t65_test1b uses ball-shaped unweighted sets instead (A=1.0345 at D=4168).
4. t65_test3: first run used p=2 sin(q/2), which is not periodic on the zone (jump at q=+-pi, tail
   exponent 2.60). t65_test3b uses p=sin(q): tail exponent 3.07; rho table unchanged to +-0.05.

Numbers: see the report's Test run section.
