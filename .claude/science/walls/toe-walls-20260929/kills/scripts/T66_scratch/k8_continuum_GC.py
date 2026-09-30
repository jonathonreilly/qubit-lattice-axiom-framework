"""Validate the {G[xi],C[N]} = C[xi.dN] equations (signs, degrees) on the continuum ADM pieces of the attack (cont2d), in the 2D sector."""
import sympy as sp, random, pickle
from cont2d import *
pieces = pickle.load(open('cont2d_pieces.pkl', 'rb'))
V1, V2, T2, T3 = pieces['V1'], pieces['V2'], pieces['T2'], pieces['T3']
Ctot = K * V1 + T2 + K * V2 + T3
Glie = sp.expand(lie_G((XIx, XIy)))
lhs_full = PB(Glie, N * Ctot)
rhs_full = (XIx * sp.diff(N, x) + XIy * sp.diff(N, y)) * Ctot
random.seed(2)
def rp():
    return sum(sp.Rational(random.randint(-3, 3), random.randint(1, 3)) * x ** i * y ** j for i in range(3) for j in range(3) if i + j <= 3)
jets = {f: rp() for f in FIELDS_H + FIELDS_P + [N, XIx, XIy]}
pt = {x: sp.Rational(1, 3), y: sp.Rational(1, 5)}
for d in (0, 1, 2):
    diff = sp.expand(degpart(sp.expand(lhs_full), d) - degpart(sp.expand(rhs_full), d))
    vals = []
    for f in FIELDS_H + FIELDS_P:
        vals.append(sp.nsimplify(EL(diff, f).subs(jets).doit().subs(pt)))
    print("degree", d, "EL residual of ({G,C} - C[xi.dN]):", ['0' if v == 0 else 'NZ' for v in vals], flush=True)
# sign control: opposite sign
for d in (1, 2):
    diff = sp.expand(degpart(sp.expand(lhs_full), d) + degpart(sp.expand(rhs_full), d))
    vals = [sp.nsimplify(EL(diff, f).subs(jets).doit().subs(pt)) for f in FIELDS_H + FIELDS_P]
    print("degree", d, "opposite sign control:", ['0' if v == 0 else 'NZ' for v in vals], flush=True)
