#!/usr/bin/env python3
"""COROLLARY check, part 2 (independent model B7_check/chk_core.py).

Constructs symmetric steps W with a CERTIFIED quasi-energy gap E' (grid + Lipschitz + Bauer-Fike), takes every exactly 2-fold
level at k* with nonzero linear splitting (quasi-energy E), and tests the corollary's counting:
   n(k) = # eigenphases in the ccw arc (E', E)
   - even at the cube points where E is not attained,
   - odd at k* + q (|q| small),
   - and a point k != +-k* with E in spec W(k) is located by bisection along a segment (the corollary's conclusion).
Examples:
  A  O-symmetric quasi-local step W = exp(-i tau H), H a random O-symmetric range-1 Hamiltonian (W(k) analytic, not finite range);
  B  D2-symmetric FINITE-RANGE step W = V1 (cos a + i sin a R) V2 (cos b + i sin b R), R = H_link/sqrt2 (exact reflection),
     V1, V2 random D2-symmetric on-site unitaries;
  H  Hamiltonian version (n = # levels below mu) for the O-symmetric H itself.
"""
import itertools, sys
import numpy as np
from scipy.linalg import expm
sys.path.insert(0, '/home/user/qubit-lattice-axiom-framework/.claude/science/physics-loops/scale-ladder-campaign-20261018/B7_check')
from chk_core import OH, LAM, UF, PROPER, CORN, ETYPES, ELIST, u, fibre_image, same_k, wrap, find, torus_ops, Hk

PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

rng = np.random.default_rng(7)
CUBE = [np.array(s) * np.pi / 2 for s in itertools.product((1, -1), repeat=3)]
kst = np.array([1, -1, 1]) * np.pi / 2
I3 = find(np.eye(3, dtype=int))
c2x, c2y, c2z = (find(np.diag(d)) for d in ([1, -1, -1], [-1, 1, -1], [-1, -1, 1]))
D2 = [I3, c2x, c2y, c2z]
T4 = torus_ops(4)

def random_sym(idx, seed, r=1):
    rr = np.random.default_rng(seed)
    h = {d: rr.normal(size=(12, 12)) + 1j * rr.normal(size=(12, 12)) for d in itertools.product(range(-r, r + 1), repeat=3)}
    A = T4['from_blocks'](h); A = (A + A.conj().T) / 2
    Gs = [T4['G'](g) for g in idx]
    S = sum(G @ A @ G.T for G in Gs) / len(Gs)
    return T4['to_blocks'](S, r)
def dnorm(h):   # sup_u ||d/du H(k)|| <= sum_d |d| ||h_d||  (|u| = 1)
    return sum(np.linalg.norm(d) * np.linalg.norm(B, 2) for d, B in h.items())

# link hopping in the independent model: link edge types have nonzero shift
hl = {}
for (i1, i2, s) in ELIST:
    if s == (0, 0, 0): continue
    amp = (-1.0) ** int(u[ETYPES[(i1, i2, s)]])
    hl.setdefault(s, np.zeros((12, 12), complex))[i2, i1] += amp
    hl.setdefault(tuple(-x for x in s), np.zeros((12, 12), complex))[i1, i2] += amp
Rk = lambda k: Hk(hl, k)[0] / np.sqrt(2)
ks = rng.uniform(-np.pi, np.pi, size=(20, 3))
check("independent rebuild: H_link(k)^2 = 2 at random k (exact reflection R = H_link/sqrt2) and R is O-symmetric",
      all(np.allclose(Rk(k) @ Rk(k), np.eye(12)) for k in ks)
      and all(np.allclose(UF[g] @ Rk(k) @ UF[g].T, Rk(fibre_image(g, k))) for k in ks[:5] for g in PROPER))
LR = dnorm({d: B / np.sqrt(2) for d, B in hl.items()})

def eigph(W): return np.angle(np.linalg.eigvals(W))
def arcpos(x, a): return np.mod(x - a, 2 * np.pi)
def count(W, Ep, E):  # eigenphases in ccw open arc (Ep, E)
    return int(np.sum(arcpos(eigph(W), Ep) < arcpos(E, Ep) - 1e-12))
def certify_gap(Wf, Lip, N=24):
    """largest empty arc on an N^3 grid; certified if every grid spectrum stays at chord distance > Lip*h*sqrt3/2 from e^{iE'}"""
    h = 2 * np.pi / N
    grid = np.array([np.array(t) * h - np.pi for t in itertools.product(range(N), repeat=3)])
    ph = np.concatenate([eigph(Wf(k)) for k in grid])
    s = np.sort(np.mod(ph, 2 * np.pi)); gaps = np.diff(np.concatenate([s, [s[0] + 2 * np.pi]]))
    j = int(np.argmax(gaps)); Ep = s[j] + gaps[j] / 2
    chord = 2 * np.sin(gaps[j] / 4)          # chord distance from e^{iE'} to the nearest grid eigenvalue
    need = Lip * h * np.sqrt(3) / 2
    return wrap(Ep), chord, need, chord > need

def doublets_at(Wf, k0, dW):
    W0 = Wf(k0); w, V = np.linalg.eig(W0); ph = np.angle(w); out = []
    used = set()
    for i in range(12):
        if i in used: continue
        grp = [j for j in range(12) if abs(wrap(ph[j] - ph[i])) < 1e-7]; used |= set(grp)
        if len(grp) != 2: continue
        Q, _ = np.linalg.qr(V[:, grp])
        hs = [(-1j) * Q.conj().T @ W0.conj().T @ dW(k0, i_) @ Q for i_ in range(3)]   # Hermitian first-order generators
        v = max(np.ptp(np.linalg.eigvalsh((x + x.conj().T) / 2)) / 2 for x in hs)
        tilt = max(abs(np.trace(x)) / 2 for x in hs)
        out.append((ph[i], v, tilt))
    return out

def locate(Wf, Ep, E, k1, k2, n1):
    """bisection on the segment k1 -> k2 for a point where the count changes, i.e. E (or E') is attained; E' is certified absent"""
    ts = np.linspace(0, 1, 401); prev = (0.0, n1)
    for t in ts[1:]:
        n = count(Wf(k1 + t * (k2 - k1)), Ep, E)
        if n != prev[1]:
            a, b = prev[0], t
            for _ in range(50):
                m = (a + b) / 2
                if count(Wf(k1 + m * (k2 - k1)), Ep, E) == prev[1]: a = m
                else: b = m
            kk = k1 + (a + b) / 2 * (k2 - k1)
            return kk, np.min(np.abs(wrap(eigph(Wf(kk)) - E)))
        prev = (t, n)
    return None, None

def corollary_test(label, Wf, dW, Lip, Ep_exact=None):
    if Ep_exact is None:
        Ep, chord, need, cert = certify_gap(Wf, Lip)
        check(f"{label}: quasi-energy gap certified at E' = {Ep:.4f}", cert, f"chord margin {chord:.3f} > Lipschitz radius {need:.3f}")
    else:
        Ep = Ep_exact
    dbl = [d for d in doublets_at(Wf, kst, dW) if d[1] > 1e-3]
    res = []
    for E, v, tilt in dbl:
        cube_n = [count(Wf(c), Ep, E) for c in CUBE if not same_k(c, kst) and np.min(np.abs(wrap(eigph(Wf(c)) - E))) > 1e-6]
        dirs = rng.normal(size=(20, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
        near = sorted(set(count(Wf(kst + 1e-4 * d), Ep, E) for d in dirs))
        nm = sorted(set(count(Wf(-kst + 1e-4 * d), Ep, E) for d in dirs))
        target = [c for c in CUBE if not same_k(c, kst) and not same_k(c, -kst)][0]
        kk, dist = locate(Wf, Ep, E, kst + 1e-4 * dirs[0], target, near[0])
        away = kk is not None and min(np.linalg.norm(wrap(kk - kst)), np.linalg.norm(wrap(kk + kst))) > 1e-2
        res.append(dict(E=E, v=v, tilt=tilt, cube_n=cube_n, near=near, nm=nm, kk=kk, dist=dist, away=away,
                        ncubeE=sum(np.min(np.abs(wrap(eigph(Wf(c)) - E))) < 1e-6 for c in CUBE)))
    ok = len(res) > 0 and all(all(n % 2 == 0 for n in r['cube_n']) and len(r['near']) == 1 and r['near'][0] % 2 == 1
                              and r['tilt'] < 1e-9 and r['away'] and r['dist'] < 1e-8 for r in res)
    det = "; ".join(f"E={r['E']:.3f} v={r['v']:.3f} tilt={r['tilt']:.0e} n(cube pts)={r['cube_n']} n(k*+q)={r['near']} n(-k*+q)={r['nm']} "
                    f"E reached at k={np.round(wrap(r['kk'])/np.pi, 4).tolist()}pi (resid {r['dist']:.0e}); cube pts at E: {r['ncubeE']}" for r in res)
    check(f"{label}: for every linearly split exactly-2-fold level at k*, n is even at the cube points off S_E, odd next to k*, zero tilt, "
          f"and E is attained at a located point other than +-k*", ok, f"{len(res)} doublets: " + det)
    return res

# ---- A: O-symmetric quasi-local step
hO = random_sym(PROPER, 101)
HO = lambda k: Hk(hO, k)[0]
spec = np.concatenate([np.linalg.eigvalsh(HO(k)) for k in rng.uniform(-np.pi, np.pi, size=(400, 3))])
Bnd = sum(np.linalg.norm(B, 2) for B in hO.values())   # rigorous: ||H(k)|| <= sum_d ||h_d|| for every k
tau = 0.95 * np.pi / Bnd                                   # => every eigenphase of exp(-i tau H(k)) lies in [-0.95 pi, 0.95 pi]
check("A: rigorous gap at E' = pi from ||tau H(k)|| <= 0.95 pi (triangle inequality on the hopping blocks)",
      tau * max(abs(spec.min()), abs(spec.max())) <= 0.95 * np.pi, f"sampled |tau E|max = {tau * np.abs(spec).max():.3f}, bound {0.95*np.pi:.3f}")
WA = lambda k: expm(-1j * tau * HO(k))
def dWA(k, i, eps=1e-6):
    e = np.zeros(3); e[i] = eps; return (WA(k + e) - WA(k - e)) / (2 * eps)
okA = all(np.allclose(UF[g] @ WA(k) @ UF[g].T, WA(fibre_image(g, k))) for k in ks[:4] for g in PROPER)
check("A: W = exp(-i tau H) commutes with the dressed O lifts (U_g W(k) U_g^T = W(R_g k + pi s_g))", okA, f"tau = {tau:.4f}")
corollary_test("A (O, quasi-local)", WA, dWA, None, Ep_exact=np.pi)

# ---- B: D2-symmetric finite-range step
def onsite_D2(seed):
    rr = np.random.default_rng(seed); A = rr.normal(size=(12, 12)) + 1j * rr.normal(size=(12, 12)); A = A + A.conj().T
    A = sum(UF[g].T @ A @ UF[g] for g in D2) / 4
    return expm(1j * A)
V1, V2 = onsite_D2(5), onsite_D2(6); al, be = 0.12, 0.09
WB = lambda k: V1 @ (np.cos(al) * np.eye(12) + 1j * np.sin(al) * Rk(k)) @ V2 @ (np.cos(be) * np.eye(12) + 1j * np.sin(be) * Rk(k))
def dWB(k, i, eps=1e-6):
    e = np.zeros(3); e[i] = eps; return (WB(k + e) - WB(k - e)) / (2 * eps)
okB = all(np.allclose(UF[g] @ WB(k) @ UF[g].T, WB(fibre_image(g, k))) for k in ks[:6] for g in D2) and \
      all(np.allclose(WB(k) @ WB(k).conj().T, np.eye(12)) for k in ks[:6])
check("B: finite-range step (range 2) is exactly unitary and commutes with the dressed D2 lifts", okB)
corollary_test("B (D2, finite range)", WB, dWB, (abs(np.sin(al)) + abs(np.sin(be))) * LR)

# ---- H: Hamiltonian version (n = number of levels below mu; no E' needed since H is bounded below)
w0, V0 = np.linalg.eigh(HO(kst)); res = []
lv = []
i = 0
while i < 12:
    j = i
    while j + 1 < 12 and w0[j + 1] - w0[i] < 1e-8: j += 1
    lv.append((w0[i], j - i + 1)); i = j + 1
for mu, m in lv:
    if m != 2: continue
    cube_n = [int(np.sum(np.linalg.eigvalsh(HO(c)) < mu)) for c in CUBE if not same_k(c, kst) and np.min(np.abs(np.linalg.eigvalsh(HO(c)) - mu)) > 1e-6]
    near = sorted(set(int(np.sum(np.linalg.eigvalsh(HO(kst + 1e-4 * d)) < mu)) for d in rng.normal(size=(20, 3))))
    res.append((mu, cube_n, near))
check("H: Hamiltonian version: for every 2-fold level mu at k*, # levels below mu is even at the cube points off S_mu and odd next to k*, "
      "so S_mu cannot be {+-k*} (it must separate k* from those cube points)",
      len(res) > 0 and all(all(n % 2 == 0 for n in r[1]) and len(r[2]) == 1 and r[2][0] % 2 == 1 for r in res),
      "; ".join(f"mu={r[0]:.3f}: cube {r[1]}, near k* {r[2]}" for r in res))
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
