#!/usr/bin/env python3
"""Check c17 (session 6). Two parts.

(A) Lemma L4a-Pi (re-derivation of Balaban CMP 109 Sect. 5, eqs. (5.6)-(5.42)): if Pi_{mu nu}(x) is the second
    variation of a translation-, hypercubic- and gauge-invariant quadratic lattice functional (finite range here), then
    in the centred Fourier variable  Pt_{mu nu}(p) = sum_z exp(-i p.(z + (e_mu - e_nu)/2)) Pi_{mu nu}(z):
      (A1) Pt(0) = 0;  (A2) sum_nu Pt_{mu nu}(p) s_nu(p) = 0, s = 2 sin(p/2);
      (A3) beta := sum_z (z_1 + 1/2)(z_2 - 1/2) Pi_12(z) equals Balaban's (1.22) form sum_z z_1 z_2 Pi_12(z);
      (A4) Pt_11(t e_2) / t^2 -> beta (the diagonal coefficient equals the off-diagonal one);
      (A5) R = Pt - beta (delta s^2 - s s^T) is O(|p|^4): R(2t)/R(t) -> 16;
      (A6) known values: plaquettes (c0) -> beta = c0; plaquettes + 1x2 rectangles (c1) -> beta = c0 + 8 c1.
    Functionals: (i) plaquette, (ii) plaquette + rectangle, (iii)-(v) a random closed lattice loop symmetrised over the
    hypercubic group (384 elements in d = 4). Finite instances, not a proof; the proof is in PROOF.md (L4a-Pi).
(B) Balaban's link average CMP 109 eq. (0.4) vs our S4': with the SAME coordinate order at both ends ("diagonal pairing")
    exp(avg log(T S^-1)) S == S exp(avg log(S^-1 T)) exactly (conjugation identity); with Balaban's independent pairing
    of the two contour families the two maps differ, at second order in the field (difference ratio ~4 under t -> 2t).
"""
import os
os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1")
import time, itertools as it, numpy as np
AUDIT_TIMEOUT_SEC = 300
T0 = time.time(); NP = NF = 0
def check(n, ok, s=""):
    global NP, NF
    NP += bool(ok); NF += not ok; print(("PASS " if ok else "FAIL ") + n + (" | " + s if s else ""))

# ---------------- (A) ----------------
d = 4; E = np.eye(d, dtype=int)
def hyper_group(d):
    G = []
    for perm in it.permutations(range(d)):
        for sg in it.product((1, -1), repeat=d):
            G.append((perm, sg))
    return G
HG = hyper_group(d)
def act(g, link):  # link = (x0 tuple, mu, s): directed step from x0 to x0 + s e_mu, stored with base point of the bond
    perm, sg = g; x0, mu, s = link
    gx = np.zeros(d, int)
    for k in range(d): gx[perm[k]] = sg[k] * x0[k]
    nu = perm[mu]; ss = s * sg[mu]
    # bond base point: link stored as A_mu(x0) traversed with sign s, i.e. the bond (x0, x0+e_mu); image bond endpoints
    # g(x0) and g(x0 + e_mu) = g(x0) + sg[mu] e_nu
    base = gx if sg[mu] > 0 else gx - E[nu]
    return (tuple(base), nu, ss)
def loop_from_walk(steps):
    """steps: list of (mu, +-1); returns list of (bond base, mu, sign) for the closed walk from 0"""
    cur = np.zeros(d, int); out = []
    for mu, s in steps:
        if s > 0: out.append((tuple(cur), mu, 1)); cur = cur + E[mu]
        else: cur = cur - E[mu]; out.append((tuple(cur), mu, -1))
    assert not cur.any(); return out
def Pi_from_loops(loops_with_c):
    P = {}
    for loop, c in loops_with_c:
        for (x0, mu, s) in loop:
            for (y0, nu, t) in loop:
                z = tuple(np.array(x0) - np.array(y0)); P[(mu, nu, z)] = P.get((mu, nu, z), 0.0) + c * s * t
    return P
def plaquettes(c):
    out = []
    for mu, nu in it.permutations(range(d), 2):
        if mu < nu: out.append((loop_from_walk([(mu, 1), (nu, 1), (mu, -1), (nu, -1)]), c))
    return out
def rectangles(c):
    out = []
    for mu, nu in it.permutations(range(d), 2):  # long side along mu: both orientations appear as (mu,nu) and (nu,mu)
        out.append((loop_from_walk([(mu, 1), (mu, 1), (nu, 1), (mu, -1), (mu, -1), (nu, -1)]), c))
    return out
def symmetrised(steps, c):
    base = loop_from_walk(steps)
    return [([act(g, l) for l in base], c / len(HG)) for g in HG]
def random_closed_walk(rng, n):
    while True:
        st = [(int(rng.integers(d)), int(rng.choice((1, -1)))) for _ in range(n // 2)]
        walk = st + [(mu, -s) for (mu, s) in rng.permutation(st).tolist()]
        # remove immediate backtracks
        red = []
        for w in walk:
            if red and red[-1][0] == w[0] and red[-1][1] == -w[1]: red.pop()
            else: red.append(tuple(w))
        if len(red) >= 6: return red
def Pt(P, p):
    M = np.zeros((d, d), complex)
    for (mu, nu, z), v in P.items():
        m = np.array(z) + (E[mu] - E[nu]) / 2.0; M[mu, nu] += v * np.exp(-1j * p @ m)
    return M
rng = np.random.default_rng(17)
cases = [("plaquette c0=1", Pi_from_loops(plaquettes(1.0)), 1.0),
         ("plaquette c0=1 + rectangle c1=-1/12", Pi_from_loops(plaquettes(1.0) + rectangles(-1 / 12)), 1.0 - 8 / 12)]
for k in range(3):
    steps = random_closed_walk(rng, 10)
    cases.append((f"random symmetrised loop #{k} (length {len(steps)})", Pi_from_loops(symmetrised(steps, 1.0)), None))
for name, P, expect in cases:
    e1 = np.abs(Pt(P, np.zeros(d))).max()
    tr = max(np.abs(Pt(P, p) @ (2 * np.sin(p / 2))).max() for p in rng.uniform(-np.pi, np.pi, size=(5, d)))
    bc = sum(v * (z[0] + .5) * (z[1] - .5) for (mu, nu, z), v in P.items() if (mu, nu) == (0, 1))
    bu = sum(v * z[0] * z[1] for (mu, nu, z), v in P.items() if (mu, nu) == (0, 1))
    t = 1e-3; bd = (Pt(P, t * E[1].astype(float))[0, 0]).real / t ** 2
    phat = rng.normal(size=d); phat /= np.linalg.norm(phat); rr = []
    for tt in (0.02, 0.04):
        p = tt * phat; s = 2 * np.sin(p / 2); R = Pt(P, p) - bc * (np.eye(d) * (s @ s) - np.outer(s, s)); rr.append(np.abs(R).max())
    ratio = rr[1] / rr[0] if rr[0] > 1e-14 else float('nan')
    ok = e1 < 1e-12 and tr < 1e-12 and abs(bc - bu) < 1e-12 and abs(bd - bc) < 1e-5 * max(1, abs(bc))
    ok = ok and (rr[0] < 1e-12 or abs(ratio - 16) < 0.5) and (expect is None or abs(bc - expect) < 1e-12)
    check(f"A {name}", ok, f"|Pt(0)|={e1:.1e} transv={tr:.1e} beta_c={bc:.6f} beta_(1.22)={bu:.6f} beta_diag={bd:.6f}"
          + (f" expect={expect:.6f}" if expect is not None else "") + f" R(2t)/R(t)={ratio:.2f} |R(t)|={rr[0]:.1e}")

# ---------------- (B) ----------------
dag = lambda M: np.conj(np.swapaxes(M, -1, -2))
def logu(Z):
    w, V = np.linalg.eig(Z); return V @ np.diag(np.log(w)) @ np.linalg.inv(V)
def expa(X):
    w, V = np.linalg.eigh(-1j * X); return V @ np.diag(np.exp(1j * w)) @ dag(V)
def gens2():
    s = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]])]
    return np.array(s, complex) / 2
def run_B(dd, Lb, Tc, amp, seed, independent):
    S = Lb * Tc; Ed = np.eye(dd, dtype=int); ORD = list(it.permutations(range(dd)))
    r = np.random.default_rng(seed); a = amp * r.normal(size=(dd,) + (S,) * dd + (3,))
    H = np.einsum("...a,aij->...ij", a, gens2()); w, V = np.linalg.eigh(H); U = V @ (np.exp(1j * w)[..., None] * dag(V))
    idx = lambda x: tuple(np.asarray(x) % S)
    def step(x, m, sg): return U[m][idx(x)] if sg > 0 else dag(U[m][idx(np.asarray(x) - Ed[m])])
    def path(a0, b, order):
        P = np.eye(2, dtype=complex); cur = np.array(a0)
        for m in order:
            while cur[m] != b[m]:
                sg = 1 if b[m] > cur[m] else -1; P = P @ step(cur, m, sg); cur[m] += sg
        return P
    def straight(y, m):
        P = np.eye(2, dtype=complex); cur = np.array(y)
        for _ in range(Lb): P = P @ step(cur, m, 1); cur[m] += 1
        return P
    X = (0,) * dd; m = 0; cX = np.array(X) * Lb + (Lb - 1) // 2; cY = cX + Lb * Ed[m]; Sc = straight(cX, m)
    accR = 0; accL = 0; n = 0
    for off in it.product(range(Lb), repeat=dd):
        y = np.array(X) * Lb + np.array(off); st = straight(y, m)
        legs1 = [path(cX, y, o) for o in ORD]; legs2 = [path(cY, y + Lb * Ed[m], o) for o in ORD]
        pairs = [(i, j) for i in range(len(ORD)) for j in range(len(ORD))] if independent else [(i, i) for i in range(len(ORD))]
        for i, j in pairs:
            T = legs1[i] @ st @ dag(legs2[j]); accR = accR + logu(dag(Sc) @ T); accL = accL + logu(T @ dag(Sc)); n += 1
    s4p = Sc @ expa(accR / n); bal = expa(accL / n) @ Sc
    return np.linalg.norm(s4p - bal), Sc, accR / n
for dd in (3, 4):
    e, _, _ = run_B(dd, 3, 2, 0.15, 5, independent=False)
    check(f"B d={dd} diagonal pairing: Balaban (0.4) form == S4' (conjugation identity)", e < 1e-12, f"err {e:.1e}")
diffs = []
for amp in (0.04, 0.08):
    _, _, Xd = run_B(3, 3, 2, amp, 9, independent=False); _, _, Xi = run_B(3, 3, 2, amp, 9, independent=True)
    diffs.append(np.linalg.norm(Xd - Xi))
ratio = diffs[1] / diffs[0]
check("B d=3 independent vs diagonal pairing differ at 2nd order (ratio under amp x2 in [3,5])", 3 < ratio < 5 and diffs[0] > 1e-8,
      f"diff(amp=.04)={diffs[0]:.2e} diff(amp=.08)={diffs[1]:.2e} ratio={ratio:.2f}")
print(f"runtime {time.time() - T0:.1f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
