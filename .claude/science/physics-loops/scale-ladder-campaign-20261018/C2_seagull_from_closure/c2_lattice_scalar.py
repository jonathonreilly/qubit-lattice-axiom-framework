#!/usr/bin/env python3
"""C2 part 3 (lattice, numerical BZ quadrature): does the O(a^2) freedom of the lattice coupling reach the induced k^2 symbol?

Euclidean 4D hypercubic lattice (a = 1), real scalar of mass m, metric perturbation h_{mn} on sites, coupling = a lattice
transcription of the closure-forced covariant density sqrt g (g^{mn} d_m phi d_n phi + m^2 phi^2) / 2 (c2_closure.py S1;
zeta = 0).  All transcriptions agree with it to O(a^2) and with each other at h = 0 (D0 = phat^2 + m^2):
  S   site-local: W = sqrt g g^{-1} at x; diagonal (D+^2 + D-^2)/2, off-diagonal 1/4 sum_{s,t} D^s_m D^t_n
  M1  bond/plaquette: W evaluated on the corner-MEAN of h (bond mean for mm, plaquette 4-corner mean for mn, plaquette
      differences for the off-diagonal gradients)
  M2  as M1 but W replaced by the corner-mean of W(h) -- identical first-order vertex, seagull differs only by the O(a^2)
      placement of its two h legs (|avg(K)|^2 vs 1)
W[h] = 1/2 log det D[h];  Pi_AB(K) = <1/2 G D2_AB> - <1/2 G(p+K) D1_A G(p) D1_B>  (exact second variation, BZ mean).
The K^2 symbol along a unit direction n is M2(n) = d^2/dk^2 [Pi(k n) - Pi(0)] (even part, Richardson from k = 0.1, 0.05).
Ward test (symbol level, continuum k): max_nu |v_nu(n) . M2(n)| / max|M2(n)|, v_nu = components of n xi_nu + xi_nu n.
EH comparison: W_AB contains -c_EH FP_AB(k) with FP the Fierz-Pauli (= [sqrt g R]^(2)) cross kernel; c_EH by least squares.
Covariant reference (continuum proper time, c2_sakharov_continuum.py P2): c_EH = (1/6) <phi^2>/2 with <phi^2> = Lambda^2/16pi^2.

Pre-declared criteria: (L1) all three reduce to D0 = phat^2 + m^2 (exact); (L2) quadrature converged (N = 24 vs 32, rel <
1e-6); (L3) at least one transcription violates Ward at the symbol level by > 1e-2 relative; (L4) M1 and M2 (same
continuum seagull, O(a^2)-different leg placement) differ in the k^2 symbol by > 1e-2 relative; (L5) the M1 - M2
difference equals the analytic placement term -(1/4)... computed independently below.
Usage: python3 c2_lattice_scalar.py [m] [N]
"""
from __future__ import annotations
import sys, time, itertools
import numpy as np

T0 = time.time()
RES = {"pass": 0, "fail": 0}


def check(tag, ok, msg):
    RES["pass" if ok else "fail"] += 1
    print(("PASS" if ok else "FAIL") + f": {tag} [{time.time()-T0:.0f}s] {msg}", flush=True)


m = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
NG = int(sys.argv[2]) if len(sys.argv) > 2 else 24
d = 4
IDX = [(a, b) for a in range(d) for b in range(d) if a <= b]
E = []
for (a, b) in IDX:
    Mx = np.zeros((d, d))
    Mx[a, b] = 1
    Mx[b, a] = 1
    E.append(Mx)          # h = sum_A c_A E_A  (off-diagonal component c_ab = h_ab)


def W1(hm):
    return 0.5 * np.trace(hm) * np.eye(d) - hm


def W2(hm):
    t = np.trace(hm)
    return (t * t / 8 - np.trace(hm @ hm) / 4) * np.eye(d) - 0.5 * t * hm + hm @ hm


def S1(hm):
    return 0.5 * np.trace(hm)


def S2(hm):
    t = np.trace(hm)
    return t * t / 8 - np.trace(hm @ hm) / 4


def pol(f, A, B):
    return f(A + B) - f(A) - f(B)      # = 2 x symmetric bilinear part


# sanity of the expansion of sqrt g g^{-1}: compare with exact at small h
rng = np.random.default_rng(0)
hh = rng.normal(size=(d, d)); hh = (hh + hh.T) * 1e-3
g = np.eye(d) + hh
ex = np.sqrt(np.linalg.det(g)) * np.linalg.inv(g)
assert np.abs(ex - (np.eye(d) + W1(hh) + W2(hh))).max() < 1e-8


def grid(N):
    p = -np.pi + (np.arange(N) + 0.5) * 2 * np.pi / N
    return np.stack(np.meshgrid(p, p, p, p, indexing="ij"), -1).reshape(-1, 4)


def ef(q, mu):
    return np.exp(1j * q[..., mu])


# ----------------------------------------------------------------------------------------------------- discretisations
# each "term": (kind, mu, nu, alpha_hat(q), beta_hat(q), placement offsets)
def terms(disc):
    T = []
    for mu in range(d):
        if disc == "S":
            T.append(("d", mu, mu, lambda q, mu=mu: ef(q, mu) - 1, lambda q, mu=mu: ef(q, mu) - 1, [np.zeros(4)], 0.5))
            T.append(("d", mu, mu, lambda q, mu=mu: 1 - 1 / ef(q, mu), lambda q, mu=mu: 1 - 1 / ef(q, mu), [np.zeros(4)], 0.5))
        else:
            T.append(("d", mu, mu, lambda q, mu=mu: ef(q, mu) - 1, lambda q, mu=mu: ef(q, mu) - 1,
                      [np.zeros(4), np.eye(4)[mu]], 1.0))
    for mu in range(d):
        for nu in range(d):
            if mu == nu:
                continue
            if disc == "S":
                for sa in (+1, -1):
                    for sb in (+1, -1):
                        a_ = (lambda q, mu=mu, sa=sa: ef(q, mu) - 1) if sa > 0 else (lambda q, mu=mu: 1 - 1 / ef(q, mu))
                        b_ = (lambda q, nu=nu, sb=sb: ef(q, nu) - 1) if sb > 0 else (lambda q, nu=nu: 1 - 1 / ef(q, nu))
                        T.append(("o", mu, nu, a_, b_, [np.zeros(4)], 0.25))
            else:
                if mu > nu:
                    continue
                a_ = lambda q, mu=mu, nu=nu: 0.5 * (ef(q, mu) - 1) * (1 + ef(q, nu))
                b_ = lambda q, mu=mu, nu=nu: 0.5 * (ef(q, nu) - 1) * (1 + ef(q, mu))
                offs = [np.zeros(4), np.eye(4)[mu], np.eye(4)[nu], np.eye(4)[mu] + np.eye(4)[nu]]
                T.append(("o", mu, nu, a_, b_, offs, 2.0))      # W^{mn} + W^{nm}
    return T


def avg(offs, K):
    return np.mean([np.exp(1j * np.dot(K, o)) for o in offs])


def pair(al, be, qo, qi):
    """1/2 [alpha(-q_out) beta(q_in) + beta(-q_out) alpha(q_in)]"""
    return 0.5 * (al(-qo) * be(qi) + be(-qo) * al(qi))


def Pi(disc, K, P, seagull_mode):
    K = np.asarray(K, float)
    T = terms(disc)
    G0 = 1.0 / (np.sum((2 * np.sin(P / 2)) ** 2, -1) + m * m)
    PK = P + K
    G1 = 1.0 / (np.sum((2 * np.sin(PK / 2)) ** 2, -1) + m * m)
    nA = len(IDX)
    D1A = np.zeros((nA, len(P)), complex)
    D1B = np.zeros((nA, len(P)), complex)
    sea = np.zeros((nA, nA), complex)
    D0 = np.zeros(len(P), complex)
    for (kind, mu, nu, al, be, offs, w) in T:
        fA = pair(al, be, PK, P)          # <p+K| . |p>
        fB = pair(al, be, P, PK)          # <p| . |p+K>
        f0 = pair(al, be, P, P)
        D0 += w * f0 * (1.0 if mu == nu else 0.0)
        aK, amK = avg(offs, K), avg(offs, -K)
        c1 = np.array([W1(EA)[mu, nu] for EA in E])
        D1A += w * aK * c1[:, None] * fA[None, :]
        D1B += w * amK * c1[:, None] * fB[None, :]
        place = (aK * amK) if (disc == "M1") else 1.0
        c2 = np.array([[pol(W2, EA, EB)[mu, nu] for EB in E] for EA in E])
        sea += 0.5 * w * place * c2 * np.mean(G0 * f0)
    # mass term at sites: m^2 sqrt g
    s1v = np.array([S1(EA) for EA in E])
    D1A += m * m * s1v[:, None]
    D1B += m * m * s1v[:, None]
    sea += 0.5 * m * m * np.array([[pol(S2, EA, EB) for EB in E] for EA in E]) * np.mean(G0)
    bub = -0.5 * np.einsum("ip,p,jp->ij", D1A * G1, G0, D1B) / len(P)
    if seagull_mode == "none":
        sea = 0 * sea
    return sea + bub, D0, G0


def symbol(disc, n, P, mode="full"):
    n = np.asarray(n, float); n /= np.linalg.norm(n)
    P0 = Pi(disc, np.zeros(4), P, mode)[0]
    ev = lambda kap: 0.5 * (Pi(disc, kap * n, P, mode)[0] + Pi(disc, -kap * n, P, mode)[0]) - P0
    Ma = ev(0.1) / 0.01
    Mb = ev(0.05) / 0.0025
    return ((4 * Mb - Ma) / 3).real


def gauge_vecs(n):
    out = []
    for nu in range(d):
        xi = np.eye(d)[nu]
        hm = np.outer(n, xi) + np.outer(xi, n)
        out.append(np.array([hm[a, b] for (a, b) in IDX]))   # component c_ab = h_ab
    return out


def FP(n):
    """cross kernel of [sqrt g R]^(2) (Fierz-Pauli) for h = A e^{ikx} + B e^{-ikx}, in component basis."""
    k = np.asarray(n, float)
    k2 = k @ k
    Mx = np.zeros((10, 10))
    for i, EA in enumerate(E):
        for j, EB in enumerate(E):
            A, B = EA, EB
            v = (-0.25 * 2 * k2 * np.sum(A * B) + 0.5 * 2 * (k @ A) @ (k @ B)
                 - 0.5 * ((k @ A @ k) * np.trace(B) + (k @ B @ k) * np.trace(A)) + 0.25 * 2 * k2 * np.trace(A) * np.trace(B))
            Mx[i, j] = v
    return Mx


def ward_ratio(M2, n):
    n = np.asarray(n, float); n /= np.linalg.norm(n)
    return max(np.abs(v @ M2).max() for v in gauge_vecs(n)) / np.abs(M2).max()


DIRS = [np.array(v, float) for v in ([1, 0.37, 0.61, -0.23], [0.2, 1, -0.5, 0.8], [1, 1, 0, 0], [0.3, -0.1, 0.9, 0.4],
                                     [1, 0, 0, 0], [0.5, 0.5, 0.5, 0.5])]
DIRS = [v / np.linalg.norm(v) for v in DIRS]

print(f"   m = {m}, N = {NG}", flush=True)
P = grid(NG)
# L1
ok1 = True
for disc in ("S", "M1", "M2"):
    _, D0, G0 = Pi(disc, np.zeros(4), P, "full")
    ok1 &= np.abs(D0 - np.sum((2 * np.sin(P / 2)) ** 2, -1)).max() < 1e-12
check("L1", ok1, "S, M1, M2 all give D0 = sum phat^2 (+ m^2) at h = 0; positive control: FP kernel is Ward-transverse")
assert all(max(np.abs(v @ FP(n)).max() for v in gauge_vecs(n)) < 1e-12 for n in DIRS)

# L2 convergence
P2 = grid(NG + 8)
Ma = symbol("M1", DIRS[0], P); Mb = symbol("M1", DIRS[0], P2)
rel = np.abs(Ma - Mb).max() / np.abs(Mb).max()
check("L2", rel < 1e-6, f"quadrature convergence N={NG} vs {NG+8}: rel diff of the M1 k^2 symbol = {rel:.1e}")

phi2 = np.mean(1.0 / (np.sum((2 * np.sin(P / 2)) ** 2, -1) + m * m))
cov_cEH = (1 / 6) * phi2 / 2
print(f"   <phi^2>_lat = {phi2:.6f};  covariant (proper-time) reference matched on <phi^2>: c_EH = (1/6)<phi^2>/2 = {cov_cEH:.6f}")
res = {}
for disc in ("S", "M1", "M2"):
    Ms = [symbol(disc, n, P) for n in DIRS]
    wr = [ward_ratio(M2, n) for M2, n in zip(Ms, DIRS)]
    A = np.concatenate([FP(n).ravel() for n in DIRS])
    y = np.concatenate([M2.ravel() for M2 in Ms])
    cfit = -float(A @ y / (A @ A))
    nonEH = np.linalg.norm(y + cfit * A) / np.linalg.norm(y)
    res[disc] = (Ms, wr, cfit, nonEH)
    print(f"   {disc:2s}: Ward ratio over 6 directions {min(wr):.3f} .. {max(wr):.3f};  c_EH(LSQ) = {cfit:.6f} "
          f"({cfit/cov_cEH:.3f} x covariant ref);  non-EH fraction {nonEH:.3f}", flush=True)
check("L3", max(max(res[k_][1]) for k_ in res) > 1e-2,
      "the closure-forced coupling, transcribed to the lattice, does not give a Ward-transverse k^2 symbol "
      f"(max ratios S {max(res['S'][1]):.3f}, M1 {max(res['M1'][1]):.3f}, M2 {max(res['M2'][1]):.3f})")
dM = max(np.abs(a_ - b_).max() / np.abs(b_).max() for a_, b_ in zip(res["M1"][0], res["M2"][0]))
check("L4", dM > 1e-2, f"M1 vs M2 (identical continuum seagull, O(a^2)-different leg placement): k^2 symbols differ by "
      f"{dM:.3f} (relative max); c_EH {res['M1'][2]:.6f} vs {res['M2'][2]:.6f}")

# L5: independent analytic form of the M1 - M2 difference: only the seagull differs, by the factor
# |avg(K)|^2 - 1 = -(1/4) sum_{o,o'} |e^{iK.(o-o')} - 1|^2 / n^2 ...; its k^2 coefficient for a bond (offs 0, e_mu) is
# -(1/4) n_mu^2 and for a plaquette (mu,nu) -(1/4)(n_mu^2 + n_nu^2).  The difference symbol is thus
#   sum_terms w c2_AB coef * <1/2 G f0> computed with a separate loop below.
def placement_diff(n):
    n = np.asarray(n, float); n /= np.linalg.norm(n)
    G0 = 1.0 / (np.sum((2 * np.sin(P / 2)) ** 2, -1) + m * m)
    out = np.zeros((10, 10))
    for (kind, mu, nu, al, be, offs, w) in terms("M1"):
        coef = -0.25 * (n[mu] ** 2 + (n[nu] ** 2 if nu != mu else 0))   # k^2 coefficient of |avg|^2
        f0 = pair(al, be, P, P)
        tad = 0.5 * np.mean(G0 * f0).real
        for i, EA in enumerate(E):
            for j, EB in enumerate(E):
                out[i, j] += w * pol(W2, EA, EB)[mu, nu] * coef * tad
    return out


# (run-1 criterion bug, N = 16 run, not kept as a log: dividing by |M1 - M2| per direction fails on the diagonal direction
#  (1,1,1,1)/2, where M1 - M2 vanishes identically -- tr of the 4D second-order sqrt g g^{-1} is zero and off-diagonal
#  tadpoles vanish by reflection -- so the residual is now normalised by the largest difference over all directions)
scale = max(np.abs(a_ - b_).max() for a_, b_ in zip(res["M1"][0], res["M2"][0]))
l5 = max(np.abs((a_ - b_) - placement_diff(n)).max() / scale for a_, b_, n in zip(res["M1"][0], res["M2"][0], DIRS))
check("L5", l5 < 1e-4, f"the M1 - M2 k^2 difference is exactly the seagull-leg placement tadpole "
      f"(-1/4 per lattice difference x <G f0>), relative residual {l5:.1e}: an O(a^2) contact x Lambda^4 = O(Lambda^2) term")

# L6 (diagnostic, pre-declared as a report, threshold 1e-2): can the O(a^2) leg-placement freedom alone restore Ward?
# one-parameter family Pi_lam = M2 + lam (M1 - M2) (lam = 0: legs at one point, lam = 1: legs on the corner mean);
# minimise the summed squared Ward residual over lam (linear least squares) and report the best ratio.
num, den = 0.0, 0.0
for a_, b_, n in zip(res["M1"][0], res["M2"][0], DIRS):
    for v in gauge_vecs(n):
        r0, r1 = v @ b_, v @ (a_ - b_)
        num += r0 @ r1
        den += r1 @ r1
lam = -num / den
best = max(ward_ratio(b_ + lam * (a_ - b_), n) for a_, b_, n in zip(res["M1"][0], res["M2"][0], DIRS))
cl = -float(np.concatenate([FP(n).ravel() for n in DIRS]) @ np.concatenate([(b_ + lam * (a_ - b_)).ravel() for a_, b_ in
            zip(res["M1"][0], res["M2"][0])]) / sum(np.sum(FP(n) ** 2) for n in DIRS))
check("L6", best > 1e-2, f"placement freedom alone does not restore Ward: best lam = {lam:.3f} leaves max Ward ratio "
      f"{best:.3f} (c_EH there {cl:.6f}); restoring Ward needs further tuned non-covariant K^2 contact terms (B4b: 8 of 9 "
      f"B4 coefficients), which no examined lattice symmetry or closure condition supplies")
np.savez(f"c2_lattice_symbols_m{m}_N{NG}.npz", dirs=np.array(DIRS), **{k_: np.array(v_[0]) for k_, v_ in res.items()})
print(f"TOTAL: PASS={RES['pass']} FAIL={RES['fail']}  ({time.time()-T0:.0f}s)")
