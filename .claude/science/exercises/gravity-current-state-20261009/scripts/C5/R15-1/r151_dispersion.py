"""R15-1 (b), step 3: the single scalar's quadratic Lagrangian L = 1/2 A qdot^2 + Cx q qdot - 1/2 Mk q^2
(from r151_reduce.pkl). Integrating Cx q qdot by parts gives the effective mass  Meff = Mk + dCx/dt.
Checks:
 1. GR limit g = 0 (Hdot = -chidot^2/2): A = a^3/2 and Meff = a^3 [k^2/a^2 + V'' + 3chidot^2 + 2chidot V'/H + chidot^2 Hdot/H^2]
    (the Mukhanov-Sasaki flat-gauge field; GR comparator, RECALLED standard formula).
 2. With g != 0: sign of A(k) (ghost), high-k sound speed, and omega^2 = Meff/A at sample backgrounds.
"""
import sympy as sp, pickle
Lq = pickle.load(open('r151_reduce.pkl', 'rb'))['Lq']
fs = {s.name: s for s in Lq.free_symbols}
print('symbols:', sorted(fs))
H, Hd, cd, k, aa, qd, q = (fs[n] for n in ('H', 'Hdot', 'chidot', 'k', 'aa', 'qd', 'q'))
Vp, Vpp = fs['Vp'], fs['Vpp']
Hdd, Vppp = sp.symbols('Hddot Vppp')
def Dt(e):
    return (sp.diff(e, aa)*aa*H + sp.diff(e, H)*Hd + sp.diff(e, Hd)*Hdd + sp.diff(e, cd)*(-3*H*cd - Vp)
            + sp.diff(e, Vp)*Vpp*cd + sp.diff(e, Vpp)*Vppp*cd)
A = sp.simplify(sp.diff(Lq, qd, 2))
Cx = sp.simplify(sp.diff(Lq, q, qd))
Mk = sp.simplify(-sp.diff(Lq, q, 2))
Meff = sp.simplify(Mk + Dt(Cx))
g = sp.Symbol('g')
# GR check
grsub = {Hd: -cd**2/2, Hdd: -cd*(-3*H*cd - Vp)}
A_GR = sp.simplify(A.subs(grsub)); M_GR = sp.simplify(Meff.subs(grsub))
MS = aa**3*(k**2/aa**2 + Vpp + 3*cd**2 + 2*cd*Vp/H + cd**2*(-cd**2/2)/H**2)
print("GR limit: A =", A_GR, "; Meff - MukhanovSasaki =", sp.simplify(M_GR - MS))
# general g: express Hdot = -(g + chidot^2)/2
Ag = sp.factor(sp.simplify(A.subs(Hd, -(g + cd**2)/2)))
print("A(k) with g:", Ag)
# Hddot: keep g and gdot: Hdd = -(gdot + 2 chidot chiddot)/2
gd = sp.Symbol('gdot')
Mg = sp.simplify(Meff.subs(Hdd, -(gd + 2*cd*(-3*H*cd - Vp))/2).subs(Hd, -(g + cd**2)/2))
w2 = sp.simplify(Mg/Ag)
print("high-k expansion of omega^2 a^2/k^2:")
eps_ = sp.Symbol('e', positive=True)
ser = sp.series(sp.simplify((w2*aa**2/k**2).subs(k, 1/eps_)), eps_, 0, 3).removeO()
print("   ", sp.simplify(ser))
pickle.dump({'A': Ag, 'M': Mg}, open('r151_dispersion.pkl', 'wb'))
import numpy as np
fA = sp.lambdify((k, aa, H, cd, g), Ag, 'numpy')
fM = sp.lambdify((k, aa, H, cd, g, gd, Vp, Vpp), Mg, 'numpy')
print("\nNumerical scan (a = 1, H = 1, chidot^2 = 1 i.e. chi-dominated scale, V' = 0, V'' = 0, gdot = 0):")
ks = np.array([0.01, 0.1, 0.3, 1, 3, 10, 100])
for gv in [-100., -10., -1., 0., 1., 5.9, 6.1, 10., 100., 1000.]:
    Av = fA(ks, 1., 1., 1., gv); Mv = fM(ks, 1., 1., 1., gv, 0., 0., 0.)
    kg = np.sqrt(max(gv - 6, 0))/2
    print(f" g/H^2 = {gv:+8.1f}: ghost window k < {kg:.3f} H;  2A/a^3 = " + " ".join(f"{v:+.3e}" for v in 2*Av)
          + " | omega^2 = " + " ".join(f"{v:+.3e}" for v in Mv/Av))
