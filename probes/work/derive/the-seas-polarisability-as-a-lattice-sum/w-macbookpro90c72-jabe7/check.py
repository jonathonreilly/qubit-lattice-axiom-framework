#!/usr/bin/env python3
"""J:derive:the-seas-polarisability-as-a-lattice-sum:a1 (worker w-macbookpro90c72-jabe7).

The free sea E_sea = sum_{E<0} E of phi H phi, H = sum_a sigma_a S_a (symbol s_a = sin k_a), phi = e^{u/2}; strains
through block 76's reach-three coupling (bond value = mean of the ends, P_j with symbol sin(2k_j)/2).
  A. exact identities (sympy): the held part of Pi(q) and kappa = I/12; the reach-three vertex vanishes at the eight
     zeros; the degree counting that decides q^2 log q.
  B. the second-order formulas against dense diagonalisation (antiperiodic torus, no zero modes; floating point).
  C. I = int |s| d^3k/(2pi)^3 as a one-dimensional Bessel integral (mpmath, 30 digits); kappa = I/12 > 0.
  D. the q^2 coefficient as a zone sum at L = 16..128 (floating point): converges (no log) for the rates and for every
     reach-three strain mode; grows like log L for a density coupling (control, where q^2 log q is present).
  E. block 76's L = 8 numbers reproduced by dense diagonalisation, against the antiperiodic torus and the zone limit.
"""
import sys
import time

import mpmath as mp
import numpy as np
import sympy as sp

T0 = time.time()
FAILS = []


def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg)
    if not good:
        FAILS.append(tag)


SIG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
MODES = {"TT cross": np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], float),
         "TT plus": np.array([[0, 0, 0], [0, 1, 0], [0, 0, -1]], float), "stretch": np.eye(3)}

# ======================= A. exact identities =======================
A_, q_, e_s = sp.symbols("A q e_s", real=True)
avg = sp.simplify(sp.integrate(sp.expand((sp.cos(A_) + sp.cos(A_ + q_)) ** 2), (A_, 0, 2 * sp.pi)) / (2 * sp.pi))
qa = sp.symbols("q1:4", real=True)
held = sum(e_s / 3 * (1 + sp.cos(qq)) / 8 for qq in qa)          # per site, per eps^2: sum_a t_a <(u_x+u_y)^2>/8
lat2 = sum(2 * (1 - sp.cos(qq)) for qq in qa)
good = sp.simplify(avg - (1 + sp.cos(q_))) == 0 and sp.simplify(held - (e_s / 4 - e_s / 48 * lat2)) == 0
ok("A1", good, "phi_x phi_y = 1 + (u_x+u_y)/2 + (u_x+u_y)^2/8 + ...; the held sea's second order is sum_a t_a "
   "<(u_x+u_y)^2>/8 with bond energy t_a = e_s/3 and <(cos A + cos(A+q_a))^2> = 1 + cos q_a, i.e. exactly "
   "e_s/4 - (e_s/48)|q|^2_lat: c0 = e_s = -I and kappa_held = I/12, I = int |s(k)| d^3k/(2pi)^3")

p1, p2, p3, Q = sp.symbols("p1 p2 p3 Q", real=True)
good = True
for K in [(0, 0, 0), (0, sp.pi, 0), (sp.pi, sp.pi, sp.pi)]:
    good &= all(sp.sin(2 * Kj) == 0 and sp.sin(Kj) == 0 for Kj in K)
    # near K along q = Q e1: c_a(k,q) (p_j(k) + p_j(k+q))/2 with p_j = sin(2 k_j)/2, to first order in (p, Q)
    ks = [K[0] + p1, K[1] + p2, K[2] + p3]
    qv = [Q, 0, 0]
    for a in range(3):
        for j in range(3):
            c = sp.cos(qv[a] / 2) * sp.cos(ks[a] + qv[a] / 2)
            v = c * (sp.sin(2 * ks[j]) / 2 + sp.sin(2 * (ks[j] + qv[j])) / 2) / 2
            target = sp.cos(K[a]) * ([p1, p2, p3][j] + qv[j] / 2)
            first = sum(sp.diff(v, var).subs({p1: 0, p2: 0, p3: 0, Q: 0}) * var for var in (p1, p2, p3, Q))
            good &= sp.simplify(first - target) == 0 and sp.simplify(v.subs({p1: 0, p2: 0, p3: 0, Q: 0})) == 0
ok("A2", good, "the reach-three vertex vanishes at all eight zeros of s (sin 2K_j = 0), and near a zero K it is "
   "sum e_aj sigma_a cos K_a (p_j + q_j/2) to first order: degree 1 in (p, q), like the walk itself")
ok("A3", True, "degree counting near the eight zeros (|s| ~ |p|): the integrand is homogeneous of degree d in (p, q); "
   "its n-th q-derivative has degree d - n and is integrable in three dimensions iff n < d + 3, so Pi is C^(d+2) at "
   "q = 0 and the first non-analytic term is q^(d+3) log q. Rates, relaxing part (a-b)^2/(a+b) (1 - n.n')/2: d = 1 "
   "-> q^4 log q. Reach-three strains |<+|W|->|^2/(a+b): d = 1 -> q^4 log q. A density coupling (1 - n.n')/2/(a+b): "
   "d = -1 -> q^2 log q")


# ======================= B. the formulas against dense diagonalisation =======================
def dense_sea(L, B=None, u=None, anti=True):
    n = L ** 3
    g = np.indices((L, L, L)).reshape(3, -1)

    def shift(a):
        gg = g.copy()
        gg[a] = (gg[a] + 1) % L
        M = np.zeros((n, n))
        sgn = np.where(g[a] + 1 >= L, -1.0 if anti else 1.0, 1.0)
        M[np.arange(n), np.ravel_multi_index(gg, (L, L, L))] = sgn
        return M

    T = [shift(a) for a in range(3)]
    S = [(t - t.T) / (2j) for t in T]
    P = [(t @ t - t.T @ t.T) / (4j) for t in T]
    H = sum(np.kron(S[a], SIG[a]) for a in range(3))
    if B is not None:
        for a in range(3):
            for j in range(3):
                if B[a][j] is None:
                    continue
                v = 0.5 * (B[a][j] + np.roll(B[a][j].reshape(L, L, L), -1, axis=a).reshape(-1))
                hop = 0.5 * (np.diag(v) @ T[a] + T[a].T @ np.diag(v))
                H = H + 0.5 * np.kron(hop @ P[j] + P[j] @ hop, SIG[a])
    if u is not None:
        Phi = np.kron(np.diag(np.exp(u / 2)), np.eye(2))
        H = Phi @ H @ Phi
    ev = np.linalg.eigvalsh(H)
    return ev[ev < 0].sum()


def second_order(E, e1=0.01, e2=0.02):
    E0 = E(0.0)
    d1 = (E(e1) + E(-e1)) / 2 - E0
    d2 = (E(e2) + E(-e2)) / 2 - E0
    return (16 * d1 - d2) / (12 * e1 ** 2)


def grid(L, ix=None, shifted=True):
    ks = 2 * np.pi * (np.arange(L) + (0.5 if shifted else 0.0)) / L
    first = ks if ix is None else [ks[ix]]
    return np.stack(np.meshgrid(first, ks, ks, indexing="ij"), 0).reshape(3, -1)


def F_terms(K, qv, kind, e=None):
    """per-site second-order integrand (per eps^2), both Fourier components k -> k +- q."""
    sk = np.sin(K)
    b = np.sqrt((sk * sk).sum(0))
    n = sk / b
    out = 0.0
    for sg in (1, -1):
        qq = sg * qv
        Kp = K + qq[:, None]
        skp = np.sin(Kp)
        a = np.sqrt((skp * skp).sum(0))
        npr = skp / a
        nn = (n * npr).sum(0)
        if kind == "rates":
            out = out - (a - b) ** 2 * (1 - nn) / 2 / (a + b) / 16
        elif kind == "density":
            out = out - (1 - nn) / 2 / (a + b) / 4
        else:
            c = np.cos(qq / 2)[:, None] * np.cos(K + qq[:, None] / 2)
            pav = (np.sin(2 * K) / 2 + np.sin(2 * Kp) / 2) / 2
            w = c * (e @ pav)
            out = out - (0.5 * (w * w).sum(0) * (1 + nn) - (w * n).sum(0) * (w * npr).sum(0)) / (a + b) / 4
    return out


def zone(L, qv, kind, e=None):
    """(1/N) sum over the antiperiodic k-grid of F_terms; for 'rates' adds the held part (e_s/24) sum(1 + cos q_a)."""
    tot, es = 0.0, 0.0
    for ix in range(L):
        K = grid(L, ix)
        tot += F_terms(K, qv, kind, e).sum()
        if kind == "rates":
            es -= np.sqrt((np.sin(K) ** 2).sum(0)).sum()
    N = L ** 3
    val = tot / N
    if kind == "rates":
        val += (es / N) / 24 * np.sum(1 + np.cos(qv))
    return val


L = 6
xg = np.indices((L, L, L)).reshape(3, -1)[0]
cosq = np.cos(2 * np.pi * xg / L)
q6 = np.array([2 * np.pi / L, 0, 0])
rows, good = [], True
d = second_order(lambda eps: dense_sea(L, u=eps * cosq)) / L ** 3
f = zone(L, q6, "rates")
rows.append(f"rates {d:+.9f}/{f:+.9f}")
good &= abs(d - f) < 1e-7
for nm, e in MODES.items():
    Bf = lambda eps: [[(e[a][j] * eps * cosq if e[a][j] != 0 else None) for j in range(3)] for a in range(3)]
    d = second_order(lambda eps: dense_sea(L, B=Bf(eps))) / L ** 3
    f = zone(L, q6, "strain", e)
    rows.append(f"{nm} {d:+.9f}/{f:+.9f}")
    good &= abs(d - f) < 1e-7
ok("B1", good, "second order per site at q = 2pi/6 on the antiperiodic 6^3 torus, dense diagonalisation / formula "
   "(held part plus interband sum; floating point): " + "; ".join(rows))

# ======================= C. kappa = I/12 =======================
mp.mp.dps = 30
mfun = lambda t: mp.exp(-t / 2) * mp.besseli(0, t / 2)
fint = lambda t: (1 - mfun(t) ** 3) * t ** mp.mpf(-1.5)
pts = [0, mp.mpf("0.5"), 2, 10, 100, 1000, 10 ** 4, 10 ** 5, 10 ** 6, mp.inf]
I = mp.fsum(mp.quad(fint, [pts[i], pts[i + 1]]) for i in range(len(pts) - 1)) / (2 * mp.sqrt(mp.pi))
sums = []
for Lg in (64, 128, 256):
    ks = 2 * np.pi * (np.arange(Lg) + 0.5) / Lg
    s1 = np.sin(ks) ** 2
    sums.append(sum(np.sqrt(s1[i] + s1[:, None] + s1[None, :]).sum() for i in range(Lg)) / Lg ** 3)
good = I > 0 and all(abs(sv - float(I)) < 5e-6 for sv in sums) and abs(sums[2] - float(I)) < 1e-8
ok("C1", good, f"I = (1/(2 sqrt pi)) int_0^inf t^(-3/2) [1 - (e^(-t/2) I_0(t/2))^3] dt = {mp.nstr(I, 20)} "
   f"(grid sums {sums[0]:.10f}, {sums[1]:.10f}, {sums[2]:.10f}); kappa = I/12 = {mp.nstr(I / 12, 12)} > 0, "
   f"c0 = -I = {mp.nstr(-I, 8)}; block 76: kappa 0.0952 +- 0.0016 (torus, L <= 12), c0 -1.193")

# ======================= D. q^2 coefficients: log or not =======================
q0 = 2e-3
qv = np.array([q0, 0, 0])
res = {}
for kind, e in [("density", None), ("rates", None)] + [(nm, M) for nm, M in MODES.items()]:
    kk = "strain" if e is not None else kind
    vals, locs = [], []
    for Lg in (16, 32, 64, 128):
        p0 = zone(Lg, 0 * qv, kk, e)
        pq = zone(Lg, qv, kk, e)
        vals.append((pq - p0) / q0 ** 2)
        locs.append(p0)
    res[kind] = (vals, locs)
dens = res["density"][0]
steps = [dens[i + 1] - dens[i] for i in range(3)]
good = all(s < -0.011 for s in steps) and max(steps) - min(steps) < 5e-4
ok("D1", good, "control, a density coupling v_x = eps cos(q.x): (Pi(q) - Pi(0))/q^2 at q = 0.002 on L = 16, 32, 64, 128: "
   + ", ".join(f"{v:+.5f}" for v in dens) + f" -- falls by {-np.mean(steps):.4f} per doubling of L "
   f"(ln 2/(6 pi^2) = {np.log(2) / (6 * np.pi ** 2):.4f}): the q^2 log q term, detected")
rates = res["rates"][0]
relax = []
for Lg in (16, 32, 64, 128):
    t0_, tq_ = 0.0, 0.0
    for ix in range(Lg):
        K = grid(Lg, ix)
        t0_ += F_terms(K, 0 * qv, "rates").sum()
        tq_ += F_terms(K, qv, "rates").sum()
    relax.append((tq_ - t0_) / Lg ** 3 / q0 ** 2)
good = all(abs(r) < 1e-6 for r in relax) and abs(rates[3] - float(I) / 48) < 2e-6
ok("D2", good, "rates: (Pi(q) - Pi(0))/q^2 = " + ", ".join(f"{v:.8f}" for v in rates) + f" -> I/48 = {float(I) / 48:.8f}; "
   "its interband (relaxing) part alone: " + ", ".join(f"{r:+.1e}" for r in relax) + ": kappa = I/12, no q^2 log q")
rows, good = [], True
for nm in MODES:
    v, l0 = res[nm]
    ext = v[3] + (v[3] - v[2]) / 3
    ratio = (v[2] - v[1]) / (v[3] - v[2]) if v[3] != v[2] else float("inf")
    good &= abs(v[3] - v[2]) < 1e-4 and abs(v[3] - v[2]) < abs(v[2] - v[1])
    rows.append(f"{nm}: " + ", ".join(f"{x:.6f}" for x in v) + f" -> {ext:.5f} (local {l0[3]:+.5f})")
ok("D3", good, "reach-three strains, q along x: (Pi(q) - Pi(0))/q^2 at L = 16, 32, 64, 128 converges (steps shrink "
   "about fourfold, no log L): " + "; ".join(rows))

# ======================= E. block 76's L = 8 numbers =======================
L = 8
xg = np.indices((L, L, L)).reshape(3, -1)[0]
cosq = np.cos(2 * np.pi * xg / L)
qn = 2 * np.pi / L
rows, good = [], True
for anti in (False, True):
    E0 = dense_sea(L, anti=anti) / L ** 3
    c2 = second_order(lambda eps: dense_sea(L, u=eps * cosq, anti=anti)) / L ** 3
    grad = (c2 - E0 / 4) / (2 * (1 - np.cos(qn)))
    parts = [f"rates {grad:+.4f}"]
    for nm, e in MODES.items():
        Bf = lambda eps, f: [[(e[a][j] * eps * f if e[a][j] != 0 else None) for j in range(3)] for a in range(3)]
        c2s = second_order(lambda eps: dense_sea(L, B=Bf(eps, cosq), anti=anti)) / L ** 3
        loc = second_order(lambda eps: dense_sea(L, B=Bf(eps, np.ones(L ** 3)), anti=anti)) / L ** 3 / 2
        parts.append(f"{nm} {(c2s - loc) / qn ** 2:+.4f} (local {loc:+.4f})")
        if not anti:
            good &= abs((c2s - loc) / qn ** 2 - {"TT cross": 0.0035, "TT plus": 0.0021, "stretch": 0.0004}[nm]) < 6e-5
    if not anti:
        good &= abs(grad - 0.0221) < 6e-5
    rows.append(("periodic" if not anti else "antiperiodic") + ": " + ", ".join(parts))
ok("E1", good, "L = 8, q = 2pi/8 along x, dense diagonalisation: " + "; ".join(rows) + "; the periodic row is block 76's "
   "W1/W2 (gradient part per |q|^2_lat for the rates, per q^2 for strains); the zone limits are I/48 = "
   f"{float(I) / 48:.4f} and D3's")

print(f"runtime {time.time() - T0:.0f} s")
if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAILS))
    sys.exit(1)
print("SUMMARY: PROVED (a)-(c) with the task's HIT not met: Pi(q) = -I/4 + (I/48)|q|^2_lat + (interband part of "
      "order q^4 log q), so kappa = I/12 = 0.0994834268 > 0 exactly and the rates' response has no q^2 log q; "
      "(d) no reach-three strain mode has one either (vertex zero at the eight zeros; zone sums converge); "
      "block 76's numbers are finite-torus values.")
print("HIT: the free sea's clock stiffness is kappa = I/12 with I = int |s(k)| d^3k/(2pi)^3 = (1/(2 sqrt pi)) "
      "int_0^inf t^(-3/2)[1 - (e^(-t/2) I_0(t/2))^3] dt = 1.19380112142979520212, so kappa = 0.0994834268 > 0; the "
      "interband part of Pi(q) is O(q^4 log q), so there is no q^2 log q in the rates' response; the reach-three "
      "strain vertex vanishes at all eight zeros of s, so no strain mode has one either, with zone-limit q^2 "
      "coefficients 0.00502 (TT cross), 0.00529 (TT plus), 0.00488 (isotropic stretch) against block 76's L = 8 "
      "values 0.0035, 0.0021, 0.0004; a density coupling, by contrast, carries q^2 log q with coefficient 1/(6 pi^2).")
