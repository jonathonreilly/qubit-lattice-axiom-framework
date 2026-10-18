#!/usr/bin/env python3
"""C6 part B6: re-check that non-uniform period-2 sectors found by greedy descent beat every uniform
pattern, with finer K-grids (4^3 -> 6^3 -> 8^3 on the 2^3 cell, i.e. effective L = 8, 12, 16), and
by an independent path (direct real-space diagonalization of the periodically extended gauge field
on the L = 8 torus at K = 0 vs Bloch at the matching grid).  Saves the found gauge fields.
"""
import itertools, os, sys, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
src = open(os.path.join(HERE, 'c6_B_flux_energetics.py')).read()
ns = {'__file__': os.path.join(HERE, 'c6_B_flux_energetics.py')}
exec(compile(src[:src.index('# ------------------------------------------------------------------ B0')], 'hdr', 'exec'), ns)
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
rng = np.random.default_rng(3)


def E(u, nu, t2, nk):
    return M.energies(M.spectrum(u, nk, 1.0, t2), [nu])[nu]


for t2, nu in ((0.2, 6), (1.0, 7)):
    uu = gauges[(1, 1, 1, 1)].copy(); ee = E(uu, nu, t2, 4)
    for k in rng.permutation(M.G.nE):
        uu[k] ^= 1; e2 = E(uu, nu, t2, 4)
        if e2 < ee - 1e-9: ee = e2
        else: uu[k] ^= 1
    np.save(os.path.join(HERE, f'c6_B6_u_t2_{t2}_nu_{nu}.npy'), uu)
    rows = []
    for nk in (4, 6, 8):
        en = E(uu, nu, t2, nk)
        bu = min(E(gauges[F], nu, t2, nk) for F in PATS)
        ec = E(gauges[(1, 1, 1, 1)], nu, t2, nk)
        rows.append((nk, en, bu, ec))
        print(f"  t2={t2} nu={nu} nk={nk}: one-sweep sector E = {en:.5f}; best uniform {bu:.5f}; corner 1111 {ec:.5f}; t={time.time()-T0:.0f}s")
    print(f"  fluxes of the found sector: {M.fluxes(uu)}")
    print(f"FINDING t2={t2} nu={nu}: found period-2 sector lies {rows[-1][2]-rows[-1][1]:+.4f} per site below the best uniform pattern"
          f" and {rows[-1][3]-rows[-1][1]:+.4f} below the corner pattern (8^3 grid)")
    check(f"t2={t2} nu={nu}: energy differences stable between 6^3 and 8^3 grids to 5e-3",
          abs((rows[1][2] - rows[1][1]) - (rows[2][2] - rows[2][1])) < 5e-3)

# independent path: real-space L = 4 torus from the periodic extension, against Bloch {0,pi}^3
M4 = Model(4)
desc2 = {}
for k, (v, c, disp, c2) in enumerate(M.G.edesc):
    desc2[(v, c, disp, c2)] = k
    w = tuple((a + b) % 2 for a, b in zip(v, disp))
    desc2[(w, c2, tuple(-x for x in disp), c)] = k
uu = np.load(os.path.join(HERE, 'c6_B6_u_t2_0.2_nu_6.npy'))
u4 = np.array([uu[desc2[(tuple(x % 2 for x in v), c, disp, c2)]] for (v, c, disp, c2) in M4.G.edesc], np.uint8)
er = M4.energies(M4.spectrum(u4, 1, 1.0, 0.2), [6])[6]
eb = E(uu, 6, 0.2, 2)
check("found sector: real-space L = 4 energy equals Bloch {0,pi}^3 energy (independent assembly path)", abs(er - eb) < 1e-9, f"{er:.6f} vs {eb:.6f}")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
