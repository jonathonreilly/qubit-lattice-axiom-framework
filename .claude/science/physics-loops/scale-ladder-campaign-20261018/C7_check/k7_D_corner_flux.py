#!/usr/bin/env python3
"""C7_check D: gauge-invariant Wilson loops of the repo corner-model family with the chiral term.

Hamiltonian as defined in the repo runners
(scripts/corner_fermion_projective_symmetry_group_class_and_site_shell_2026_10_17.py, cluster();
 scripts/corner_fermion_large_fermion_effective_theory_and_one_qubit_block_embedding_2026_10_17.py, bloch()/H_lattice()):
    H = -t1 sum_onsite u (c^dag_i c_j + h.c.) - t2 sum_links u (c^dag_i c_j + h.c.)
        + sum over the 8 octant triangles, traversed with det(x,y,z) > 0 (q -> r):  i lambda u_qr c^dag_r c_q + h.c.
with the u-pattern 1011 (prod u = -1 on squares, plaquettes, tubes; +1 on triangles).
I build it with my own geometry (k7_geom), apply a random U(1) gauge transformation, and measure the standard
flux arg prod(-amp) on every face of the L = 2 torus.  Predictions (derived by hand in the report, theta = arctan lambda,
t1 = -1): outward square pi - 4 theta, outward triangle pi + 3 theta, plaquette pi, tube (my orientation, whose two
on-site edges run against the triangle orientation) pi - 2 theta; any sign of t2.
Consequences checked: (i) no finite lambda reproduces 1c+11 (square pi forces theta in (pi/2)Z, i.e. lambda = 0,
then triangle = pi, not +-pi/2); (ii) the pure-chiral limit t1 = 0 has fluxes 1c+10 (square pi, triangle +pi/2,
plaquette pi, tube 0).
"""
import itertools, os, sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from k7_geom import Lat, gf2, det3, CORNERS

PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''), flush=True)


lat = Lat(2)
rng = np.random.default_rng(11)
# u-pattern 1011 in the u-convention (orientation-free products of real signs)
bits = {'square': 1, 'triangle': 0, 'plaquette': 1, 'tube': 1}
xu = gf2([[e for e, _ in w] for _, w, _ in lat.faces], [bits[k] for k, _, _ in lat.faces], lat.nE)
u = (-1.0) ** xu
# orientation of each on-site edge relative to the outward triangle containing it (repo rule: det(x,y,z) > 0)
sig = np.zeros(lat.nE)
for k, w, _ in lat.faces:
    if k == 'triangle':
        for e, s in w:
            sig[e] += s
okT = np.all(np.abs(sig[lat.onsite]) == 1) and np.all(sig[~lat.onsite] == 0)
check("each on-site edge lies in exactly one octant triangle (so the chiral term is one complex phase per on-site edge)", okT)


def amps(t1, t2, lam):
    a = np.where(lat.onsite, -t1 * u, -t2 * u).astype(complex)
    a = a + 1j * lam * u * sig          # outward traversal I->J adds i lam u to H[J,I]; backward adds its conjugate
    return a


def gauge(a):
    th = rng.uniform(0, 2 * np.pi, lat.n)
    return a * np.exp(1j * (th[lat.J] - th[lat.I]))


def wrap(x): return np.mod(x + np.pi, 2 * np.pi) - np.pi


okF = True
print("\nflux/pi per face type (t1 = -1), measured after a random U(1) gauge transformation:")
for lam in (0.0, -0.5, -1 / np.sqrt(3), 0.3, 1.7, -2.4):
    for t2 in (0.2, -0.3, 1.0):
        a = gauge(amps(-1.0, t2, lam))
        ph = lat.fluxes(a)
        th = np.arctan(lam)
        pred = {'square': np.pi - 4 * th, 'triangle': np.pi + 3 * th, 'plaquette': np.pi, 'tube': np.pi - 2 * th}
        dev = max(np.max(np.abs(wrap(ph[lat.fkind == i] - pred[k]))) for i, k in enumerate(('square', 'triangle', 'plaquette', 'tube')))
        okF &= dev < 1e-9
        if t2 == 0.2:
            vals = {k: sorted(set(np.round(np.mod(ph[lat.fkind == i], 2 * np.pi) / np.pi, 4)))
                    for i, k in enumerate(('square', 'triangle', 'plaquette', 'tube'))}
            print(f"   lambda = {lam:+.4f}: {vals}  max dev from formula over t2 in (0.2,-0.3,1): see check")
check("all 232 faces x 6 lambda x 3 t2: square pi - 4 arctan(lambda), triangle pi + 3 arctan(lambda), plaquette pi, "
      "tube pi - 2 arctan(lambda) (outward/my orientation), gauge invariant", okF)
# reversing orientation flips the sign of the shift (so 'pi -+ 4 arctan' in C7 = orientation ambiguity)
a = amps(-1.0, 0.2, -0.5)
k0, w0, _ = lat.faces[0]
rev = [(e, -s) for e, s in reversed(w0)]
check("reversed square orientation gives pi + 4 arctan(lambda)", abs(wrap(lat.flux(a, rev) - (np.pi + 4 * np.arctan(-0.5)))) < 1e-12)

# (i) no finite lambda reproduces 1c+11
lams = np.linspace(-20, 20, 400001)
th = np.arctan(lams)
sq_pi = np.abs(wrap(np.pi - 4 * th - np.pi)) < 1e-9
tri_q = np.abs(np.abs(wrap(np.pi + 3 * th)) - np.pi / 2) < 1e-9
tub_pi = np.abs(wrap(np.pi - 2 * th - np.pi)) < 1e-9
check("analytic: square = pi needs 4 arctan(lambda) in 2 pi Z, i.e. lambda = 0 for finite lambda; then triangle = pi != +-pi/2 "
      "(scan of 4e5 lambda in [-20, 20] finds no simultaneous square = tube = pi and triangle = +-pi/2)",
      not np.any(sq_pi & tri_q & tub_pi) and np.all(lams[sq_pi] == 0))
# (ii) pure chiral limit: t1 = 0
a = gauge(amps(0.0, 0.2, 1.0))
ph = lat.fluxes(a)
vals = {k: sorted(set(float(x) for x in np.round(np.mod(ph[lat.fkind == i] + 1e-9, 2 * np.pi) / np.pi, 6)))
        for i, k in enumerate(('square', 'triangle', 'plaquette', 'tube'))}
print("   t1 = 0 (pure chiral) fluxes/pi:", vals)
check("pure-chiral limit t1 = 0: square pi, outward triangle +pi/2, plaquette pi, tube 0 (= the Majorana pattern 1c+10, "
      "not 1c+11)", vals == {'square': [1.0], 'triangle': [0.5], 'plaquette': [1.0], 'tube': [0.0]})
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
