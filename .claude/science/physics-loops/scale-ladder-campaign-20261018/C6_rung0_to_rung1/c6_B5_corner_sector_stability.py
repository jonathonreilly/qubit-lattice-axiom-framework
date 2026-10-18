#!/usr/bin/env python3
"""C6 part B5: where the corner flux pattern is the best UNIFORM sector (standard 1111 at nu = 7 for
|t2| = 1), is it also stable against period-2 (2^3-cell) single-edge flux changes?

Checks with independently justified expectations:
  - particle-hole identity: flipping every hop sign maps H -> -H and changes the standard flux of
    odd faces only (triangles), and Tr H = 0, so E(F, nu) = E(F with triangle flipped, 12 - nu).
Findings (no expected value): single-flip energy changes around the corner sector; greedy descent.
"""
import itertools, os, sys, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import importlib.util
spec = importlib.util.spec_from_file_location('c6b', os.path.join(HERE, 'c6_B_flux_energetics.py'))
# reuse the Model class without running the B script: exec only the class definition
src = open(os.path.join(HERE, 'c6_B_flux_energetics.py')).read()
cut = src.index('# ------------------------------------------------------------------ B0')
ns = {'__file__': os.path.join(HERE, 'c6_B_flux_energetics.py')}
exec(compile(src[:cut], 'c6_B_header', 'exec'), ns)
Model, TYPES = ns['Model'], ns['TYPES']

PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


T0 = time.time()
M = Model(2)
PATS = list(itertools.product((0, 1), repeat=4))
gauges = {F: M.gauge(dict(zip(TYPES, F))) for F in PATS}
lab = lambda F: ''.join(map(str, F))

# particle-hole identity
ok = True; dev = 0.0
for F in PATS:
    Ft = (F[0], 1 - F[1], F[2], F[3])
    for t2 in (0.2, 1.0):
        e1 = M.energies(M.spectrum(gauges[F], 4, 1.0, t2), range(1, 12))
        e2 = M.energies(M.spectrum(gauges[Ft], 4, 1.0, t2), range(1, 12))
        for nu in range(1, 12):
            dev = max(dev, abs(e1[nu] - e2[12 - nu]))
check("particle-hole identity E(F, nu) = E(F with triangle flipped, 12 - nu) for all 16 patterns, t2 = 0.2 and 1", dev < 1e-9, f"max dev {dev:.1e}")


def E(u, nu, t2, nk=4):
    return M.energies(M.spectrum(u, nk, 1.0, t2), [nu])[nu]


rng = np.random.default_rng(5)
for t2, nu in ((1.0, 7), (0.2, 7), (0.2, 8)):
    u0 = gauges[(1, 1, 1, 1)]
    e0 = E(u0, nu, t2)
    dE = np.empty(M.G.nE)
    for k in range(M.G.nE):
        u = u0.copy(); u[k] ^= 1
        dE[k] = E(u, nu, t2) - e0
    kmin = int(np.argmin(dE))
    u = u0.copy(); u[kmin] ^= 1
    dE6 = E(u, nu, t2, nk=6) - E(u0, nu, t2, nk=6)
    print(f"FINDING t2={t2} nu={nu}: corner sector E = {e0:.4f}; single period-2 edge flips: min dE = {dE.min():+.4f} "
          f"(edge {kmin}, {M.G.edges[kmin][2]}; recheck on 6^3 grid {dE6:+.4f}), #flips with dE<0: {int((dE < -1e-9).sum())}/{M.G.nE}; t={time.time()-T0:.0f}s")
    if dE.min() < -1e-9:
        # greedy descent from the corner sector (two sweeps)
        uu = u0.copy(); ee = e0
        for sweep in range(2):
            for k in rng.permutation(M.G.nE):
                uu[k] ^= 1; e2 = E(uu, nu, t2)
                if e2 < ee - 1e-9: ee = e2
                else: uu[k] ^= 1
        print(f"    greedy descent from the corner sector: E = {ee:.4f}, fluxes {M.fluxes(uu)}; t={time.time()-T0:.0f}s")

print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
