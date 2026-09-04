"""
T240 - a sixth tempting coincidence, checked before it can be believed.

R152: the record field's 6 Goldstone modes give 1/G = 6/(12 pi tau0), G = 2 pi tau0.
R156: whether the Berry U(1) has a propagating photon is OPEN.
The tempting arithmetic: 6 Goldstones + 2 photon polarisations = 8 = exactly the
content R72 assumed, restoring G = (3/2) pi tau0 and ell_P = 0.45a.

Five such coincidences have already dissolved in this packet.  The question to
ask FIRST is whether a photon really counts as "+2 scalars".  It does not: the
induced-gravity weight is SPIN dependent, through the a1 heat-kernel coefficient

      for D = -(nabla* nabla + E) on a rank-k bundle:   tr a1 = tr E + k R/6

METHOD VALIDATION: the same computation must reproduce R76's stated -2 per Dirac.
"""
import numpy as np
from fractions import Fraction as F

d = 4
def weight(name, k, trE_over_R, extra_ghosts=0, statistics=1):
    """tr a1 / R  for a field, in units of a real scalar's 1/6"""
    tr_a1 = trE_over_R + F(k, 1)*F(1, 6)
    tr_a1 -= extra_ghosts*F(1, 6)          # ghosts are real scalars, subtracted
    return name, tr_a1, tr_a1/F(1, 6)*statistics

print(f"working in d = {d};  a real scalar has tr a1 = R/6\n")
print(f"{'field':34s} {'tr a1 / R':>10s}   {'weight vs real scalar':>22s}")

rows = [
    # real scalar: E = 0, k = 1
    weight("real scalar", 1, F(0), 0, 1),
    # Dirac: D^2 = nabla*nabla + R/4  (Lichnerowicz) -> E = -R/4 on a rank-4 bundle
    weight("Dirac fermion (Lichnerowicz)", 4, F(-1), 0, 1),
    # Maxwell: Hodge on 1-forms, Delta_1 = nabla*nabla + Ric -> E = -Ric, tr = -R,
    # rank d, minus 2 real scalar ghosts
    weight("Maxwell field (1-forms - 2 ghosts)", d, F(-1), 2, 1),
]
for name, a1, w in rows:
    print(f"{name:34s} {str(a1):>10s}   {str(w):>22s}")

print(f"""
METHOD CHECK: R76 states the induced 1/G weight is "-2 per Dirac".
   computed here: {rows[1][2]}   -> {'MATCHES R76' if rows[1][2] == -2 else 'DOES NOT MATCH'}
   so the same computation applied to a Maxwell field is trustworthy.

THE COINCIDENCE, TESTED:
   a photon does NOT count as +2 scalars; it counts as {rows[2][2]}.
   6 Goldstones + a propagating photon  =  6 + ({rows[2][2]}) = {6+rows[2][2]}
   G = 12 pi tau0 / N :
      N = 6  (no photon, R152)            -> G = {F(12,6)} pi tau0 = 2 pi tau0
      N = {6+rows[2][2]}  (with a photon)                -> G = {F(12,1)/(6+rows[2][2])} pi tau0
      R72's assumed N = 8                 -> G = 1.5 pi tau0
   the '6 + 2 = 8' arithmetic is wrong; the photon's weight is negative and
   four times a scalar's.  SIXTH COINCIDENCE, DISSOLVED.
""")
