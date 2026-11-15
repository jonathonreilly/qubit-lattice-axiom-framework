# mc55_3_diag -- POST-RUN DIAGNOSTIC (not pre-registered, no verdict): how close the mc55_3 gates come to saturation.
# Reuses mc55_3_lift.py's construction verbatim by import; prints exact maxima of the ratios as floats for display only.
import importlib.util, sys
spec = importlib.util.spec_from_file_location('m', 'mc55_3_lift.py')
src = open('mc55_3_lift.py').read().split('results = []')[0]   # definitions only, not the verdict loop
ns = {}; exec(compile(src, 'mc55_3_lift_defs', 'exec'), ns)
F = ns['F']; from itertools import product, permutations
def ratios(kind, seed):
    U = ns['build'](kind, seed); d, L, S = ns['d'], ns['L'], ns['S']
    eps2 = max(ns['dist2'](T, ns['ONE']) for T in ns['plaquettes'](U))
    h = {}
    for z in ns['sites']:
        c = ns['root'](z); T, _ = ns['transport'](U, c, ns['axial_moves'](c, z, tuple(range(d)))); h[z] = T
    r2 = F(0)
    for x in ns['sites']:
        for mu in range(d):
            y = ns['add'](x, mu); c = ns['root'](x)
            if ns['root'](y) != c: continue
            r = sum(abs(x[nu] - c[nu]) for nu in range(mu + 1, d))
            if r:
                uh = ns['qmul'](ns['qmul'](h[x], U[(x, mu)]), ns['qinv'](h[y]))
                r2 = max(r2, ns['dist2'](uh, ns['ONE']) / (r * r * eps2))
    r3 = F(0)
    for X in product(range(2), repeat=d):
        cX = tuple(3*Xi + 1 for Xi in X)
        for mu in range(d):
            cY = ns['add'](cX, mu, 3); conts = []
            for sigma in permutations(range(d)):
                for yp in product(*[range(cX[i] - 1, cX[i] + 2) for i in range(d)]):
                    T1, _ = ns['transport'](U, cX, ns['axial_moves'](cX, yp, sigma))
                    T2, e2 = ns['transport'](U, yp, [(mu, 1)] * L)
                    T3, _ = ns['transport'](U, cY, ns['axial_moves'](cY, e2, sigma))
                    conts.append(ns['qmul'](ns['qmul'](T1, T2), ns['qinv'](T3)))
            for x in product(*[[cX[i] + 1] if i == mu else range(cX[i] - 1, cX[i] + 2) for i in range(d)]):
                x = tuple(xi % S for xi in x); y = ns['add'](x, mu)
                Tb = ns['qmul'](ns['qmul'](h[x], U[(x, mu)]), ns['qinv'](h[y]))
                for Tc in conts:
                    r3 = max(r3, ns['dist2'](Tb, Tc) / eps2)
    return float(r2), float(r3) ** 0.5
for kind, seed in [('random', 1), ('aligned', 5)]:
    a, b = ratios(kind, seed)
    print(f"{kind} seed={seed}: max |U^h_b-1|^2/(r^2 eps'^2) = {a:.4f};  max |T_b - T_contour|/eps' = {b:.3f}  (gate allows {ns['nL']})")
