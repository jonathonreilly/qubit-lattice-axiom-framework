#!/usr/bin/env python3
"""J:falsifier:PR9306 -- independent exact ground energies of the full 2^3-torus ring + single-link-hopping Hamiltonian (2^24 states).

Setting as supplied by the note: H = -g sum_p (U_p + U_p^dag) - t sum_l sigma^x_l + M sum_v Q_v^2, g = 1, M = 2, Q_v = div_v / 2, links carry arrows sigma = +-1 (sigma = +1: from v to v + e_a),
U_p flips the four arrows of a plaquette when they circulate the same way (circulation = +-4).  The note quotes Ritz references -9.631658548 (t = 0.35) and -10.430531975 (t = 0.5) from its own
matrix-free three-vector Lanczos.  Here: own site/link/plaquette construction, own numba matvec (different loop order and bit layout), scipy ARPACK (implicitly restarted Lanczos) with a random start,
plus extra checks beyond the note: the t = 0 ring-plus-charge limit, the exact bound E0 >= -t*24 - g*24, hermiticity, and the ice-sector projection of the ground state at t = 0.35.
"""
import sys, time
import numpy as np
import numba as nb
from scipy.sparse.linalg import LinearOperator, eigsh

PASS = FAIL = 0; HITS = []
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1; HITS.append(name)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}", flush=True)

L = 2
sites = [(x, y, z) for x in range(L) for y in range(L) for z in range(L)]
sid = {s: i for i, s in enumerate(sites)}
def link(s, a): return a * 8 + sid[s]                    # own layout: link index = axis*8 + site
def sh(s, a, d=1):
    t = list(s); t[a] = (t[a] + d) % L; return tuple(t)
NL = 24
# vertex incidence: div_v = sum_a [sigma(v, a) - sigma(v - e_a, a)]
vplus = np.zeros((8, 3), np.int64); vminus = np.zeros((8, 3), np.int64)
for s in sites:
    for a in range(3):
        vplus[sid[s], a] = link(s, a); vminus[sid[s], a] = link(sh(s, a, -1), a)
# plaquettes (s; a<b): circulation = sigma_a(s) + sigma_b(s+a) - sigma_a(s+b) - sigma_b(s)
plaq = []
for s in sites:
    for a in range(3):
        for b in range(a + 1, 3):
            plaq.append((link(s, a), link(sh(s, a), b), link(sh(s, b), a), link(s, b)))
plaq = np.array(plaq, np.int64)
assert len(plaq) == 24 and all(len(set(p)) == 4 for p in plaq)
pmask = np.array([sum(1 << int(l) for l in p) for p in plaq], np.int64)

@nb.njit(cache=False)
def diag_energy(n, vplus, vminus, M):
    d = np.zeros(n)
    for s in range(n):
        tot = 0
        for v in range(8):
            div = 0
            for a in range(3):
                div += 2 * ((s >> vplus[v, a]) & 1) - 1
                div -= 2 * ((s >> vminus[v, a]) & 1) - 1
            q = div // 2
            tot += q * q
        d[s] = M * tot
    return d

@nb.njit(cache=False, parallel=False)
def matvec(x, y, d, plaq, pmask, g, t):
    n = x.shape[0]
    for s in range(n):
        acc = d[s] * x[s]
        for l in range(24):
            acc -= t * x[s ^ (1 << l)]
        for p in range(24):
            c = (2 * ((s >> plaq[p, 0]) & 1) - 1) + (2 * ((s >> plaq[p, 1]) & 1) - 1) - (2 * ((s >> plaq[p, 2]) & 1) - 1) - (2 * ((s >> plaq[p, 3]) & 1) - 1)
            if c == 4 or c == -4:
                acc -= g * x[s ^ pmask[p]]
        y[s] = acc

n = 1 << NL
t0 = time.time()
d = diag_energy(n, vplus, vminus, 2.0)
print(f"   diagonal charge energy built in {time.time()-t0:.1f}s; charge-free states (all Q = 0): {int((d == 0).sum())} of {n} (9600 expected)")
check("the charge-free (ice) states number 9600 on the 2^3 torus", int((d == 0).sum()) == 9600)

def ground(t, g=1.0, k=1, seed=5):
    def mv(x):
        y = np.empty_like(x); matvec(np.ascontiguousarray(x, dtype=np.float64), y, d, plaq, pmask, g, t); return y
    op = LinearOperator((n, n), matvec=mv, dtype=np.float64)
    rng = np.random.default_rng(seed); v0 = rng.standard_normal(n)
    w, v = eigsh(op, k=k, which="SA", tol=1e-12, v0=v0, maxiter=4000, ncv=24)
    return w, v
# hermiticity on random vectors
rng = np.random.default_rng(1); a_ = rng.standard_normal(n); b_ = rng.standard_normal(n); ya = np.empty(n); yb = np.empty(n)
matvec(a_, ya, d, plaq, pmask, 1.0, 0.35); matvec(b_, yb, d, plaq, pmask, 1.0, 0.35)
check("the matvec is symmetric: <a, H b> = <H a, b> on random vectors", abs(a_ @ yb - ya @ b_) < 1e-6 * abs(a_ @ yb).max() + 1e-6, f"diff {abs(a_ @ yb - ya @ b_):.2e}")
refs = {0.35: -9.631658548, 0.5: -10.430531975}
res = {}
for tv in (0.35, 0.5):
    t0 = time.time(); w, v = ground(tv); res[tv] = (w[0], v[:, 0]); print(f"   t = {tv}: ARPACK ground energy {w[0]:.10f} ({time.time()-t0:.0f}s)")
    check(f"ground energy at t = {tv} equals the note's Ritz reference {refs[tv]} to 5e-9", abs(w[0] - refs[tv]) < 5e-9, f"mine {w[0]:.9f}, diff {w[0]-refs[tv]:+.2e}")
# beyond the note: other hopping values, the t -> 0 limit, and the sector structure of the ground state
for tv in (0.0, 0.2, 0.7):
    t0 = time.time(); w, v = ground(tv, seed=7); res[tv] = (w[0], v[:, 0]); print(f"   t = {tv}: {w[0]:.10f} ({time.time()-t0:.0f}s)")
check("the ground energy decreases monotonically with the hopping t on the grid 0, 0.2, 0.35, 0.5, 0.7", res[0.0][0] >= res[0.2][0] >= res[0.35][0] >= res[0.5][0] >= res[0.7][0])
e = [res[tv][0] for tv in (0.0, 0.2, 0.35, 0.5, 0.7)]
check("concavity of E0(t) (a minimum of linear functions of t): slopes on the grid 0, 0.2, 0.35, 0.5, 0.7 are non-increasing", all(((e[i + 1] - e[i]) / (tt[i + 1] - tt[i]) - (e[i] - e[i - 1]) / (tt[i] - tt[i - 1])) <= 1e-8 for i in range(1, 4) for tt in [(0.0, 0.2, 0.35, 0.5, 0.7)]))
check("the crude bound E0 >= -(24 t + 24 g) holds and E0(0.35) lies below E0(0)", -(24 * 0.35 + 24) <= res[0.35][0] <= res[0.0][0], f"E0(0) = {res[0.0][0]:.6f}")
psi = res[0.35][1]; ice_w = float((psi[d == 0] ** 2).sum())
print(f"   weight of the t = 0.35 ground state on charge-free configurations: {ice_w:.4f}; mean charge energy <M sum Q^2> = {float((d * psi**2).sum()):.4f}")
check("the ground state at t = 0.35 is normalized and carries a nonzero charged admixture (weight on the 9600 ice states below 1)", abs((psi ** 2).sum() - 1) < 1e-9 and 0.5 < ice_w < 1.0, f"ice weight {ice_w:.4f}")
if not HITS:
    print(f"SUMMARY: no falsifier fires: independent ARPACK/numba ground energies of the full 2^3 ring-plus-hopping Hamiltonian reproduce the note's Ritz references at t = 0.35 ({res[0.35][0]:.9f}) and t = 0.5 ({res[0.5][0]:.9f}) to better than 5e-9; the projector and 6^3 energies are stochastic diagnostics not testable from this exact side; {PASS} checks pass")
else:
    print("SUMMARY: failed: " + "; ".join(HITS))
    if any("Ritz reference" in h for h in HITS): print("HIT: 2^3 Ritz reference differs from an independent exact ground energy of the stated Hamiltonian: " + "; ".join(h for h in HITS if "Ritz reference" in h))
sys.exit(0)
