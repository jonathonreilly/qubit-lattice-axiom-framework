"""Refuting pass, block 10 (supervisor, disjoint machinery): the recorded-set terms by the closed form of T3(b) instead of the
Möbius inversion — exp Phi_A = exp(-Delta_k log K_k(v_A)) — for the plaquette's {b, c} term and the star's leaf triple; and
the k-body ratios recomputed from Z_k with the vacuum at -x instead of +x (a different vacuum gives different values but the
same zero/nonzero verdict)."""
from fractions import Fraction as F
from itertools import product
import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[5] / "scripts"))
import importlib
r10 = importlib.import_module("admissibility_rule_recorded_set_gibbs_theorem_formation_laws_markov_graph_2026_09_15")
M = 6
rule = r10.Rule((3, 1, 2))

def closed_form_ratio(vals, vacuum=0):
    """exp(-Delta_k log K_k) at vals with the given vacuum: inverse of the mixed ratio of Z_k (the Z_1 powers cancel)."""
    k = len(vals); num, den = 1, 1
    for mask in range(1 << k):
        arg = tuple(vals[i] if (mask >> i) & 1 else vacuum for i in range(k))
        z = rule.Zk(arg)
        if (k - bin(mask).count("1")) % 2 == 0: num *= z
        else: den *= z
    return F(den, num)

# plaquette {b, c} term at the witness (b, c) = (+y, +z): T3(b) predicts exp Phi_bc = exp(-Delta_2 log K_2(b, c))
print("R1 plaquette {b,c} closed form:", closed_form_ratio((2, 4)), "== Möbius value 12/13:", closed_form_ratio((2, 4)) == F(12, 13))
# star leaves at (-x, -x, +y)
print("R2 star leaves closed form:", closed_form_ratio((1, 1, 2)), "== Möbius value 165/169:", closed_form_ratio((1, 1, 2)) == F(165, 169))
# k-body verdicts with the vacuum at -x (index 1) for k = 2..6 at witness assignments over {+x, +y}
verdicts = []
for k in range(2, 7):
    found = False
    for vals in product((0, 2), repeat=k):
        if closed_form_ratio(vals, vacuum=1) != 1:
            found = True; break
    verdicts.append((k, found))
print("R3 nonzero k-body term with vacuum -x, k=2..6:", verdicts)
