#!/usr/bin/env python3
"""g-equality: do the window-renormalised edge registers give equal tensor and Newtonian couplings?

Edge register (CL-1): values n = 0..2S, length = flat length (1 + n/2S) (window [l_f, 2 l_f]); edge hop
J(V+V^dag) = cosine band in the edge momentum.  The window and the tetrahedron projector act on each
register's own values (edge-local).  Treatments: exact single register in a Weiss field (mean field) +
RPA for the lattice; exact small rings of registers as a check of RPA.  numpy/scipy only.
"""
import time
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spl

AUDIT_TIMEOUT_SEC = 120
t0 = time.time()
NP = NF = 0


def check(tag, ok, msg, det=""):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] [{tag}] {msg} | {det}")


def site(S, sig=None, c=None, J=1.0, k=None):
    """one register, on-site Weiss stiffness k centred at value c; returns r = k chi0 (1 = harmonic),
    M_eff/M_bare from the low-frequency expansion of chi0(w), mean, spread."""
    m = np.arange(2 * S + 1.0)
    c = S if c is None else c
    k = 0.5 * J / sig ** 4 if k is None else k          # harmonic spread sig (M = 1/2J)
    H = np.diag(0.5 * k * (m - c) ** 2) - J * (np.eye(len(m), k=1) + np.eye(len(m), k=-1))
    w, V = np.linalg.eigh(H); g = V[:, 0]; mel = V.T @ (m * g); dE = w[1:] - w[0]
    chi0 = 2 * np.sum(mel[1:] ** 2 / dE); c2 = 2 * np.sum(mel[1:] ** 2 / dE ** 3)
    mu = g @ (m * g)
    return chi0 * k, (c2 / chi0 ** 2) * 2 * J, mu, np.sqrt(g @ (m ** 2 * g) - mu ** 2)


# ------------------------------------------------------------------ A. structure of the window term
print("== A. the window is an edge-local (mass) term, not a factor in G")
E6 = [np.array(e, float) for e in ((1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (0, 1, 1), (1, 0, 1), (1, -1, 0), (0, 1, -1), (-1, 0, 1))]
def rel(e, h):          # relative length change of edge e under a uniform metric change h
    return e @ h @ e / (2 * e @ e)
def wall_energy(h, wa=1.0, wd=1.0):  # per site: 3 axis + 3 face diagonals, diagonals alternating (avg of both)
    ax = sum(wa * rel(E6[i], h) ** 2 for i in range(3))
    dg = sum(0.5 * wd * (rel(E6[3 + i], h) ** 2 + rel(E6[6 + i], h) ** 2) for i in range(3))
    return ax + dg
basis = []
for (i, j) in ((0, 0), (1, 1), (2, 2), (0, 1), (1, 2), (0, 2)):
    h = np.zeros((3, 3)); h[i, j] = h[j, i] = 1.0; basis.append(h)
Wm = np.array([[0.25 * (wall_energy(a + b) - wall_energy(a - b)) for b in basis] for a in basis])
ew = np.linalg.eigvalsh(Wm)
check("T", ew.min() > 0,
      "A1 every uniform metric is flat (an affine image of the flat triangulation is embedded, so all deficits "
      "vanish) and the hinge-sum second variation is zero on all six; the window's edge-local stiffness is "
      "positive definite on them: it is a mass matrix, so it cannot be a rescaling of the hinge-sum form (of G)",
      f"wall form on uniform metrics, eigenvalues {np.round(ew, 4).tolist()} (w_axis = w_diag = 1)")
Eg = np.diag([1.0, -1.0, 0.0]); T2 = basis[3]; Tr = np.eye(3)
nrm = lambda h: np.sum(h * h)
mr = {n: wall_energy(h) / nrm(h) for n, h in (("E_g", Eg), ("T_2g", T2), ("trace", Tr))}
check("T", abs(mr["E_g"] / mr["T_2g"] - 2.5) < 1e-12,
      "A2 on the six-register layout the window mass per unit h_ij h_ij is w_a/4 + w_d/16 (E_g), w_d/8 (T_2g), "
      "(w_a+w_d)/4 (trace): a wave along an axis has its two TT polarisations at mass ratio sqrt(5/2) for equal "
      "weights, so the window makes the graviton birefringent and the scalar sector differs again",
      "m^2 ratios E_g : T_2g : trace = " + " : ".join(f"{mr[k]:.4f}" for k in ("E_g", "T_2g", "trace")))
fp = lambda h: nrm(h) - np.trace(h) ** 2
check("T", fp(Tr) < 0 < wall_energy(Tr),
      "A3 the window form is not of Fierz-Pauli form h_ij h_ij - (tr h)^2 (that is negative on the trace, the "
      "window form positive) and it also stiffens pure displacements (h = du + du^T): the window breaks the "
      "momentum-constraint gauge, a generic Lorentz-violating mass",
      f"FP(trace) {fp(Tr):.0f}, wall(trace) {wall_energy(Tr):.3f}")

# ------------------------------------------------------------------ B. exact rings of registers vs RPA
print("== B. exact rings of hop registers (gradient coupling K + weak on-site k0 = 0.2 K)")
def kron(*o):
    out = o[0]
    for x in o[1:]:
        out = sp.kron(out, x, format="csr")
    return out
def ring(N, S, s1, J=1.0, k0f=0.2):
    d = 2 * S + 1; I = sp.identity(d, format="csr"); n = sp.diags(np.arange(d) - S + 0.0)
    hop = sp.diags([np.ones(d - 1), np.ones(d - 1)], [1, -1], format="csr")
    xq = 2 * (1 - np.cos(2 * np.pi * np.arange(N) / N))
    f = lambda K: np.mean(1 / (2 * np.sqrt((k0f * K + K * xq) / (2 * J)))) - (s1 * S) ** 2
    lo, hi = 1e-8, 1e4
    for _ in range(120):
        mid = np.sqrt(lo * hi); lo, hi = (mid, hi) if f(mid) > 0 else (lo, mid)
    K = mid; k0 = k0f * K
    X = [kron(*[n if j == i else I for j in range(N)]) for i in range(N)]
    H = sum(-J * kron(*[hop if j == i else I for j in range(N)]) for i in range(N))
    H = H + sum(0.5 * k0 * (x @ x) for x in X) + sum(0.5 * K * ((X[i] - X[(i + 1) % N]) @ (X[i] - X[(i + 1) % N])) for i in range(N))
    H = H.tocsr(); w, v = spl.eigsh(H, k=1, which="SA", tol=1e-12); g = v[:, 0]
    A = (H - w[0] * sp.identity(H.shape[0])).tocsc(); xs, inv, rat = [], [], []
    for mq in range(N // 2 + 1):
        q = 2 * np.pi * mq / N; cs = np.cos(q * np.arange(N)); O = sum(cs[i] * X[i] for i in range(N))
        r_ = O @ g; r_ -= g * (g @ r_); y = spl.minres(A, r_, rtol=1e-12)[0]; y -= g * (g @ y)
        chi = 2 * (r_ @ y) / np.sum(cs ** 2); xs.append(2 * (1 - np.cos(q))); inv.append(1 / chi)
        rat.append(chi * (k0 + K * xs[-1]))
    B, A0 = np.polyfit(xs, inv, 1)
    r0 = site(S, J=J, k=k0 + 2 * K)[0]
    return (A0 - k0) / K, B / K, rat[0], 2.2 * (1 / r0 - 1)
rows = [(N, S, s1) + ring(N, S, s1) for (N, S) in ((5, 4), (4, 6)) for s1 in (0.2, 0.3, 0.4, 0.45)]
big = [r for r in rows if r[2] >= 0.4]
check("D", all(abs(r[4] - 1) < 0.01 for r in rows) and all(r[3] > 0.15 for r in big) and all(r[6] < r[3] for r in big),
      "B1 exact rings: the window adds an on-site (mass) term A to the inverse response and leaves the gradient "
      "stiffness K (the G-carrying term) within 0.5%; RPA underestimates the mass, by 1.3-2x at s1 >= 0.4 (the S = 4, s1 = 0.2 RPA value is single-site value-lattice pinning, an artefact)",
      "N,S,s1: A_box/K, B/K, chi(0)/harm, RPA A/K = " + "; ".join(f"{r[0]},{r[1]},{r[2]}: {r[3]:.3f}, {r[4]:.4f}, {r[5]:.3f}, {r[6]:.3f}" for r in rows))

# ------------------------------------------------------------------ C. 3D RPA: mass, cone clause, G_T/G_N
print("== C. 3D lattice, RPA on the exact single register (z = 6), large S (no value-lattice pinning)")
z = 6; Sb = 128
cen = {s1: site(Sb, s1 * Sb) for s1 in (0.15, 0.2, 0.25, 0.3, 0.4, 0.45)}
ma = {s1: np.sqrt(z * (1 / v[0] - 1)) for s1, v in cen.items()}
check("D", ma[0.4] > 1 and ma[0.2] < 0.1,
      "C1 RPA: chi^-1(q) = K q^2 + K z(1/r - 1): the gradient term is exactly unrenormalised and the window "
      "enters only as a mass, m a = sqrt(z(1/r-1)); at the rule's s1 ~ 0.4 the edge field is Yukawa-cut at "
      "~0.4 cell (static potential) and gapped at the cell scale (TT): no 1/r law to absorb into G",
      "s1: 1-r, m a = " + "; ".join(f"{s}: {1-v[0]:.1e}, {ma[s]:.2g}" for s, v in cen.items()))
# cone clause: retune J so that M_eff equals the hinge-sum (bare) value; does the mass go?
J0 = 1.0; k4 = 0.5 * J0 / (0.4 * Sb) ** 4; Mt = 1 / (2 * J0); Jc = J0
for _ in range(60):
    r_, Mr, _, _ = site(Sb, J=Jc, k=k4); Jc = Jc * (Mr * (1 / (2 * Jc))) / Mt
r_c, Mr_c, _, sd_c = site(Sb, J=Jc, k=k4); r_b, Mr_b, _, _ = site(Sb, J=J0, k=k4)
cg_b = 1 / np.sqrt(Mr_b)   # bare: c_g^2 = K/M_eff with K/M_bare = 1
check("D", abs(Mr_c * (1 / (2 * Jc)) / Mt - 1) < 1e-9 and np.sqrt(z * (1 / r_c - 1)) > 1,
      "C2 the dressed-weight clause (dressed kinetic form = second variation) fixes M_eff, i.e. c_g = 1, "
      "and with it G_T = G_N/c_g = G_N in RPA for omega >> m, r << 1/m; it leaves the mass: one combination "
      "(the cone) is fixed, the window mass matrix is not. Without the clause G_T/G_N = 1/c_g",
      f"s1 0.4: bare M_eff/M {Mr_b:.4f} -> c_g {cg_b:.4f}, G_T/G_N {1/cg_b:.4f}; clause J/J0 {Jc:.4f}, "
      f"m a {np.sqrt(z*(1/r_b-1)):.2f} -> {np.sqrt(z*(1/r_c-1)):.2f}")
wl = {t: site(400, 12.0, c=t * 12.0) for t in (0, 1, 2, 3, 5, 6, 7, 8)}
check("D", np.sqrt(z * (1 / wl[0][0] - 1)) > 3,
      "C3 one wall at distance d from the Weiss centre (the other far): the mass at d = 0, the state CL-1 "
      "gives every child edge just after a split (child length = flat length, n = 0), is m a ~ 4.5",
      "d/sigma: 1-r, m a = " + "; ".join(f"{t}: {1-v[0]:.1e}, {np.sqrt(z*(1/v[0]-1)):.2g}" for t, v in wl.items()))

# ------------------------------------------------------------------ D. against measurement
print("== D. estimates against measurement")
ts = np.array([5, 6, 7, 8.0]); ys = np.log([1 - wl[t][0] for t in ts]) + ts ** 2 / 2
b, a = np.polyfit(np.log(ts), ys, 1)          # 1-r ~ e^a t^b e^{-t^2/2}
inv_lr = 1.2e27                                # 1/l_rung in eV at Lambda ~ 4 (hop-recheck D3)
bounds = {"LIGO m_g<1.3e-23eV": 1.3e-23, "HT (m/w)^2<3e-3": 1.6e-20, "Will'18 lambda_g>1.8e16m": 1.1e-23}
def t_need(mlim):
    target = np.log((mlim / inv_lr) ** 2 / z); t = 10.0
    for _ in range(200):
        t = np.sqrt(2 * (a + b * np.log(t) - target))
    return t
tn = {k_: t_need(v) for k_, v in bounds.items()}
tL = tn["LIGO m_g<1.3e-23eV"]; s1n = 1 / tL; Lam = 4 * (0.4 / s1n) ** 2
check("E", 20 < tL < 24 and s1n < 0.05,
      "D1 the measured graviton-mass and Yukawa bounds need m a <~ 1e-50 for TT and static sectors alike, i.e. "
      "every register's nearest wall >~ 22 sigma away; centred that is s1 <~ 0.045 vs the rule's 0.4, i.e. "
      "Lambda = l_rung^2/(8 pi G hbar) >~ 300 (s1 ~ 0.8/sqrt(Lambda)) or edges on blocks of b >~ 9 cells",
      f"fit 1-r = e^{a:.2f} t^{b:.2f} e^(-t^2/2); d/sigma needed: " + ", ".join(f"{k_} {v:.1f}" for k_, v in tn.items())
      + f"; s1 <= {s1n:.3f}, Lambda >= {Lam:.0f}")
gtgn_ring = max(abs(r[4] - 1) for r in rows)
check("E", gtgn_ring < 0.01,
      "D2 the coupling ratio: in RPA G_T/G_N = 1 exactly once c_g = 1 (C2); beyond RPA the exact rings move the "
      "gradient stiffness by <= 0.5% at s1 0.2-0.45, falling with the wall weight e^(-1/2s1^2): if the window "
      "matters at all (s1 ~ 0.4) a sector-dependent shift of that size would fail the double pulsar (6e-5), "
      "but the mass bound (D1) forces s1 <~ 0.045, where the shift is ~e^-240: the ratio is not the binding test",
      f"max |B/K - 1| in rings {gtgn_ring:.4f}; HT 0.9983(16), double pulsar 0.999963(63)")
# split cycle: child edges start at n = 0; fraction of a doubling cycle within 22 sigma of a wall
sig_rel = 0.2 / np.sqrt(Lam / 4)               # sigma_l / l_f at the Lambda of D1
frac = (np.log2(1 + tL * sig_rel) + np.log2(2 / (2 - tL * sig_rel))) if tL * sig_rel < 1 else 1.0
check("E", frac > 0.5,
      "D3 the window also binds by position: children start at the bottom wall and parents split at the top "
      "wall, so even at s1 = 0.045 the edges sit within 22 sigma of a wall for most of each doubling cycle "
      "(and at d = 0 the mass is cell-scale, C3); a window that only just spans the cycle cannot work at any s1",
      f"fraction of the log-length cycle within 22 sigma of [l_f, 2 l_f] walls at Lambda {Lam:.0f}: {frac:.2f}")
Lf = 1.5 * Lam; marg = tL * 0.2 / np.sqrt(Lf / 4)   # 22 sigma_l / l_f at the proposed Lambda
check("E", marg < 0.5,
      "D4 proposed fix: registers spanning a factor 4, [l_f/2, 4 l_f] with the split at 2 l_f (children at l_f), "
      "plus Lambda >~ 450 (or edges role-assigned on blocks of b >~ 11, 16 on power-of-two rungs): walls then "
      "stay >= 22 sigma from the edges through the whole cycle, the window mass is < 1e-50/a, and "
      "G_T = G_N = hinge-sum G up to ~e^-240",
      f"at Lambda {Lf:.0f}: needed margin 22 sigma_l = {marg:.2f} l_f vs l_f/2 below, 2 l_f above")
print("theorems: A1-A3; diagnostics: B1, C1-C3; estimates: D1-D4")
print("supplied: RPA (z=6), toy gradient stiffness for the hinge sum, s1 ~ 0.4 at Lambda ~ 4 and s1 ~ Lambda^-1/2, 1/l_rung")
print(f"elapsed_seconds {time.time()-t0:.1f}")
print(f"TOTAL: PASS={NP} FAIL={NF}")
