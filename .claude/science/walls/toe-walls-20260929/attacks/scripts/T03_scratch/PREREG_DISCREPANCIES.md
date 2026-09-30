# Where the pre-registered predictions were wrong (recorded after the first run; PREREGISTRATION.md unchanged)

Test 2, first run (out_test2_first_run.txt), tmax = 14:
- I predicted "H_orig: Delta*(1 + O(eps)) deposited per birth".  Observed exactly 2*Delta.  Cause: bookkeeping.  A birth raises
  N by 2 and, on the penalty-free sector, N_B by 2 (N_B - W = N - M_A is asserted in tree_model), so H_orig - H' = Delta*(N - M_A) moves by 2*Delta.
- I predicted "H': |Q|/delta >= 0.2 (hop-scale residual)".  Observed 0.0000 for the three stars; 0.60 for two_A_path at eps = 0.05 only
  because W = 1 states had not yet decayed at tmax = 14.  With tmax = 200 (probe_path.py) Q'/delta -> 0.0007.  So the HEAT in the H' convention
  is zero to numerical precision; the hop-scale term does not show up as heat.  It shows up as a change of the sector's ground-state energy
  (probe_gs.py: E_gs(N)/delta = -2, -3 -> -3, -4 -> -6 -> 0, -3 -> 0 for star_2, star_3, star_4, two_A_path), i.e. as binding lost, not heat.
The decision rule in PREREGISTRATION.md ("cost reappears as a supplied rest energy plus an O(hop) residual") is therefore met in a
different form than predicted; the report says so.
