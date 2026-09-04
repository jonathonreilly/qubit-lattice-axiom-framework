"""
T244 - the fermion gap, named; and the 1/G weight table made explicit.

Checking R159 against the packet surfaced two things.

(1) BOOKKEEPING.  R76's "-2 per Dirac" is the a1 WEIGHT.  The contribution to
    1/G carries an extra STATISTICS sign (a boson gives W = +1/2 logdet, a
    fermion W = -1/2 logdet).  T240 printed the a1 weights without that sign.
    The R159 arithmetic is unaffected -- all its fields are bosons -- but the
    table should show both columns.

(2) THE GAP.  R72's G rests on a FERMIONIC Kahler-Dirac field.  R152's G rests
    on the record field's SIX BOSONIC Goldstone modes.  Those are not the same
    kind of matter, and the framework has only ever DERIVED the bosonic one.
"""
from fractions import Fraction as F

rows = [
    ("real scalar",                    F(1),   +1, "boson"),
    ("Maxwell field",                  F(-4),  +1, "boson"),
    ("Dirac fermion",                  F(-2),  -1, "fermion"),
    ("Kahler-Dirac in 4D (4 tastes)",  F(-8),  -1, "fermion"),
]
print(f"{'field':32s} {'a1 weight':>10s} {'statistics':>11s} {'-> 1/G':>8s}")
for name, a1, st, kind in rows:
    print(f"{name:32s} {str(a1):>10s} {kind:>11s} {str(a1*st):>8s}")

print(f"""
CHECK against the packet's own line 5400-5402:
   "(-1)_statistics x (-8)_a1 = +8"      -> Kahler-Dirac gives {F(-8)*-1} : {'OK' if F(-8)*-1 == 8 else 'MISMATCH'}
   R72: 1/(16 pi G) = 8/(192 pi^2 tau0)  -> G = (3/2) pi tau0

R159 re-checked with the statistics column:
   six Goldstones  (bosons)   -> 6 x (+1) = +6
   plus a photon   (boson)    ->     (-4)
   total N = {6-4}   ->  G = 12 pi tau0 / {6-4} = {F(12,6-4)} pi tau0
   unchanged: every field in R159 is a boson, so no sign flips apply.

THE GAP:
   R72's  N = +8  comes from a FERMIONIC Kahler-Dirac field.
   R152's N = +6  comes from BOSONIC Goldstone modes of the record field.
   The framework derives the second and assumes the first.
""")
