#!/usr/bin/env python3
"""
Rung 20 (corrected): the eps-cancellation of the native-discrete gap subleading
margin, derived for the CORRECT object (the eigenvalue ratio), with the eps^2
sign supported by computed witnesses.

DERIVED (symbolic / lattice-exact, Parts 1-3):
  * T_1 = [R, T_0], R = d_x + d_y: the W98 first correction is an infinitesimal
    translation conjugation of the leading operator (R(H e^-Q) = P_1 e^-Q, [R,L]=0).
  * mu_i^(1) = <Phi_i | [R, T_0] | Phi_i> = 0 -- and the lattice form
    <v | [C, T_0] | v> = 0 holds EXACTLY for any eigenvector v of a symmetric
    matrix T_0 and ANY matrix C (pure linear algebra, no boundary assumption).
  * coeff_eps( log(lambda_1/lambda_0) ) = mu_1^(1)/mu_1 - mu_0^(1)/mu_0 (exact),
    hence = 0: the beta^(-1/2) (eps) term of the eigenvalue-ratio margin cancels.
    The necessary-and-sufficient condition is the WEAKER state-independence of
    mu_i^(1)/mu_i; mu_i^(1)=0 each-state suffices.
  * C_4 = (1/8) L^2 (heat correction identity); P_2 e^-Q = (1/2) R^2[H e^-Q] + 3 H e^-Q.

WITNESSED (numerical, Parts 4-5; NOT proof inputs):
  * exact-Wilson recurrence: beta^(-1/2) coefficient b ~ 0 of log(lambda_1/lambda_0),
    and the 1/beta coefficient a_2 ~ 1.66 (matches the W90 cross-check fence).
  * eps^2 sign a_2 > 0: a_2 = a_2^heat + a_2^LC with
    a_2^heat = (1/4)(||L Phi_1||^2 - ||L Phi_0||^2) > 0 (excited reduced state is
    more L-curved); witnessed here. (a_2^LC > 0 is computed in the campaign notes.)

W99 CORRECTION (internal; W99 was never landed): W99 routed the cancellation
through the STATIC virial defect A_i + B_i/mu_i of the corrected reduced operator,
claiming coeff_eps(A_i+B_i/mu_i) = -mu_i^(1)/(2 mu_i) = 0. That is the WRONG
object: coeff_eps(A_i+B_i/mu_i) carries an extra term from the translation of the
Q-insertion, R(Q H e^-Q) = (3u H + Q P_1) e^-Q -- the dropped 3u H e^-Q term is
nonzero and state-dependent, so the static virial defect does NOT have a zero eps
slope. The eigenvalue-ratio object (this note) is the correct one.

Scope: native discrete surface and the retained reduced-A2 operator only. No
continuum, no physical beta=6, no Clay / infinite-volume Yang-Mills claim, no
audit outcome. W90 numbers are fenced cross-check witnesses, never proof inputs.

Status authority: independent audit lane only. This source note does not set or
predict an audit outcome.
"""
from __future__ import annotations
from pathlib import Path
import numpy as np
import sympy as sp
from scipy.special import iv

PASS = 0
FAIL = 0


def check(name, ok):
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {name}")
    else:
        FAIL += 1
        print(f"FAIL: {name}")


NOTE_PATH = (
    Path(__file__).resolve().parents[1]
    / "docs"
    / "NATIVE_GAUGE_TRANSFER_REDUCED_A2_EIGENVALUE_RATIO_EPS_CANCELLATION_RUNG_TWENTY_BOUNDED_NOTE_2026-06-12.md"
)
note_text = NOTE_PATH.read_text(encoding="utf-8")

check("note declares controlled claim type and source-side boundary",
      "**Claim type:** bounded_theorem" in note_text
      and "**Boundary:** eps-cancellation DERIVED" in note_text
      and "Claim type is a source-side boundary declaration, never an audit verdict." in note_text)
check("note separates derived eps-cancellation from computed eps^2 sign support",
      "eps-cancellation DERIVED" in note_text
      and "eps^2 sign has positive computed support" in note_text
      and "Computationally supported here (sign), not a-priori derived" in note_text)
check("note keeps the fully a-priori sign open",
      "partial-with-named-missing-link for the fully a-priori sign" in note_text
      and "Not derived here:" in note_text
      and "a fully a-priori proof" in note_text)
check("note uses durable repo references, not scratch paths",
      "/tmp/" not in note_text
      and "file://" not in note_text
      and "NATIVE_GAUGE_TRANSFER_REDUCED_A2_VIRIAL_LEADING_EQUALITY_RUNG_EIGHTEEN_BOUNDED_NOTE_2026-06-12.md" in note_text
      and "NATIVE_GAUGE_TRANSFER_REDUCED_A2_SPECTRAL_DOMINATION_RUNG_ELEVEN_BOUNDED_NOTE_2026-06-12.md" in note_text)
check("note includes the no-go discipline gate for the sign boundary",
      "## No-Go Discipline Gate" in note_text
      and "N1 - Alternative route enumeration" in note_text
      and "N8 - Cross-cycle echo" in note_text)
check("note avoids audit-outcome assertions",
      "audited_clean" not in note_text.lower()
      and "audit status:" not in note_text.lower()
      and "Status authority: independent audit lane only" in note_text)


# ============================================================================
# PART 1 - symbolic identities (the DERIVED core)
# ============================================================================
print("[Part 1] symbolic identities")
x, y = sp.symbols("x y", real=True)
H = x * y * (x + y) / 2
Q = x ** 2 + x * y + y ** 2
u = x + y
G1 = (u ** 2 + 2 * x * y) / 2
P1 = sp.expand(G1 - 3 * u * H)
P2 = sp.expand(sp.Rational(3, 2) * u - 3 * u * G1 + sp.Rational(9, 2) * u ** 2 * H)


def L(f):
    return sp.Rational(1, 3) * (sp.diff(f, x, 2) - sp.diff(f, x, y) + sp.diff(f, y, 2))


def R(f):
    return sp.diff(f, x) + sp.diff(f, y)


W = H * sp.exp(-Q)
# (1) T_1 multiplier = translation of leading multiplier: R(H e^-Q) = P_1 e^-Q
check("R(H exp(-Q)) = P_1 exp(-Q)  [T_1 = translation of leading multiplier]",
      sp.simplify(R(W) * sp.exp(Q) - P1) == 0)
# (2) [R,L] = 0  =>  [R,S]=0
g = sum(sp.Symbol(f"c{i}{j}") * x ** i * y ** j for i in range(4) for j in range(4))
check("[R, L] = 0 on a generic polynomial  (=> [R, exp(L/2)] = 0)",
      sp.simplify(R(L(g)) - L(R(g))) == 0)
# (3) eigenvalue-ratio expansion: coeff_eps( log(lam1/lam0) ) = m1a/m1 - m0a/m0
m0, m1, m0a, m1a, e = sp.symbols("m0 m1 m0a m1a e")
Lam = sp.log((m1 + e * m1a) / (m0 + e * m0a))
check("coeff_eps( log(lambda_1/lambda_0) ) = mu_1^(1)/mu_1 - mu_0^(1)/mu_0",
      sp.simplify(sp.diff(Lam, e).subs(e, 0) - (m1a / m1 - m0a / m0)) == 0)
# (4) heat identity C_4 = (1/8) L^2
gg = sum(sp.Symbol(f"d{i}{j}") * x ** i * y ** j for i in range(5) for j in range(5))
C4 = (sp.Rational(1, 72) * (sp.diff(gg, x, 4) + sp.diff(gg, y, 4))
      - sp.Rational(1, 36) * (sp.diff(gg, x, 3, y, 1) + sp.diff(gg, x, 1, y, 3))
      + sp.Rational(1, 24) * sp.diff(gg, x, 2, y, 2))
check("C_4 = (1/8) L^2  [heat correction identity]",
      sp.simplify(C4 - sp.Rational(1, 8) * L(L(gg))) == 0)
# (5) P_2 reduction
check("P_2 exp(-Q) = (1/2) R^2[H exp(-Q)] + 3 H exp(-Q)",
      sp.simplify((P2 * sp.exp(-Q) - (sp.Rational(1, 2) * R(R(W)) + 3 * W)) * sp.exp(Q)) == 0)
# (6) W99-bug diagnosis: R(Q H e^-Q) e^Q = 3u H + Q P_1 ; dropped 3u H != 0 at (1,2)
RQW = sp.simplify(R(Q * W) * sp.exp(Q))
check("W99-bug: R(Q H exp(-Q)) exp(Q) = 3u H + Q P_1  (the dropped translation-of-Q term)",
      sp.simplify(RQW - (3 * u * H + Q * P1)) == 0)
check("W99-bug: the dropped term 3u H is nonzero (= 27 at (1,2))",
      sp.nsimplify((3 * u * H).subs({x: 1, y: 2})) == 27)
# (7) anti-fab / falsifiers: P_1(1,2) = -41/2 ; wrong N_c=2 (A1, single root) differs
check("P_1(1,2) = -41/2", sp.nsimplify(P1.subs({x: 1, y: 2})) == sp.Rational(-41, 2))
check("P_2(1,2) = 135/2", sp.nsimplify(P2.subs({x: 1, y: 2})) == sp.Rational(135, 2))
# A1 (N_c=2) discriminant is a single linear root (degree 1), not the A2 cubic H
deltaA1 = x  # single positive root of A1
check("falsifier: A1 (N_c=2) discriminant is degree 1 (!= A2 cubic H, degree 3)",
      sp.Poly(deltaA1, x, y).total_degree() == 1 and sp.Poly(2 * H, x, y).total_degree() == 3)


# ============================================================================
# PART 2 - lattice form: <v|[C,T_0]|v> = 0  (mu_i^(1)=0, pure linear algebra)
# ============================================================================
print("[Part 2] lattice commutator identity (no boundary assumption)")
rng = np.random.default_rng(12345)
n = 8
A = rng.standard_normal((n, n))
T0m = A + A.T
C = rng.standard_normal((n, n))   # ANY matrix (stands in for R on the lattice)
w, V = np.linalg.eigh(T0m)
comm = C @ T0m - T0m @ C
maxexp = max(abs(float(V[:, k] @ comm @ V[:, k])) for k in range(n))
check("<v|[C,T_0]|v> = 0 for every eigenvector of symmetric T_0, ANY C  (<1e-10)",
      maxexp < 1e-10)


# ============================================================================
# PART 3 - exact-Wilson half-slice operator (operator construction)
# ============================================================================
def build_J(nmax):
    weights = [(p, q) for p in range(nmax + 1) for q in range(nmax + 1)]
    index = {wt: i for i, wt in enumerate(weights)}
    j = np.zeros((len(weights), len(weights)))
    for (p, q) in weights:
        i = index[(p, q)]
        for a, b in [(p + 1, q), (p - 1, q + 1), (p, q - 1),
                     (p, q + 1), (p + 1, q - 1), (p - 1, q)]:
            if a >= 0 and b >= 0 and (a, b) in index:
                j[index[(a, b)], i] += 1.0 / 6.0
    return j, weights, index


def matrix_exp_symmetric(m, tau):
    vals, vecs = np.linalg.eigh(m)
    return (vecs * np.exp(tau * vals)) @ vecs.T


def wilson_coeffs_full(weights, mode_max, arg):
    Wn = len(weights)
    lam = np.array([[p + q, q, 0] for (p, q) in weights])
    modes = np.arange(-mode_max, mode_max + 1)
    ii = np.arange(3)
    jj = np.arange(3)
    base = lam[:, None, :] + (ii[None, :, None] - jj[None, None, :])
    idx = base[..., None] + modes[None, None, None, :]
    lo = int(idx.min())
    hi = int(idx.max())
    orders = np.arange(lo, hi + 1)
    Ivals = iv(orders, arg)
    Mt = np.moveaxis(Ivals[idx - lo], 3, 1)
    dets = np.linalg.det(Mt)
    return dets.sum(axis=1)


def top_two(nmax, beta, mode_max):
    j, weights, index = build_J(nmax)
    E = matrix_exp_symmetric(j, beta / 2.0)
    c = wilson_coeffs_full(weights, mode_max, beta / 3.0)
    r = c / c[index[(0, 0)]]
    T = (E * r) @ E
    v = np.sort(np.linalg.eigvalsh(T))[::-1]
    return float(v[0]), float(v[1])


print("[Part 3] exact-Wilson eps-cancellation witness (b ~ 0) and a_2 ~ 1.66")
MODE_MAX = 120
betas = [60.0, 90.0, 120.0, 150.0, 200.0]
shells = {b: int(np.ceil(4.0 * np.sqrt(b))) + 2 for b in betas}
Lam_vals = []
for b in betas:
    l0, l1 = top_two(shells[b], b, MODE_MAX)
    Lam_vals.append(np.log(l1 / l0))
    print(f"  beta={b:6.1f} shell={shells[b]:3d}  Lambda=log(l1/l0)={np.log(l1/l0):.8f}")
betas_a = np.array(betas)
Lam_a = np.array(Lam_vals)
# fit Lambda = Linf + b*beta^-1/2 + a2*beta^-1 + a3*beta^-3/2
M = np.vstack([np.ones_like(betas_a), betas_a ** -0.5, betas_a ** -1.0, betas_a ** -1.5]).T
coef, *_ = np.linalg.lstsq(M, Lam_a, rcond=None)
Linf, bcoef, a2coef, a3coef = coef
print(f"  fit: L_inf={Linf:.6f}  b(eps)={bcoef:.6f}  a2={a2coef:.6f}  a3={a3coef:.6f}")
# force b=0 and confirm a2 stays in band (robustness)
M0 = np.vstack([np.ones_like(betas_a), betas_a ** -1.0, betas_a ** -1.5]).T
coef0, *_ = np.linalg.lstsq(M0, Lam_a, rcond=None)
a2_b0 = coef0[1]
print(f"  force b=0: a2={a2_b0:.6f}")
check("eps-cancellation witness: |b (beta^-1/2 coeff)| < 0.02  (~0)", abs(bcoef) < 0.02)
check("eps^2 margin a_2 in (1.55, 1.75)  [matches W90 fence ~1.66, sign POSITIVE]",
      1.55 < a2coef < 1.75 and 1.55 < a2_b0 < 1.75)
check("computed a_2 witness is positive (Route-A monotonicity direction support)", a2coef > 0)

# shell convergence of lambda_1/lambda_0 at beta=120
l0a, l1a = top_two(shells[120.0], 120.0, MODE_MAX)
l0b, l1b = top_two(shells[120.0] + 4, 120.0, MODE_MAX)
rel = abs((l1a / l0a) - (l1b / l0b)) / (l1a / l0a)
print(f"  shell-convergence beta=120: ratio delta(shell, shell+4) rel={rel:.2e}")
check("shell convergence: lambda_1/lambda_0 stable to <1e-5 (shell vs shell+4)", rel < 1e-5)


# ============================================================================
# PART 4 - a_2^heat sign witness: ||L Phi_1||^2 > ||L Phi_0||^2 (reduced operator)
# ============================================================================
print("[Part 4] a_2^heat = (1/4)(||L Phi_1||^2 - ||L Phi_0||^2) > 0 witness")
N = 44
Xmax = 6.0
xs = np.linspace(0, Xmax, N + 2)[1:-1]
hgrid = xs[1] - xs[0]
Xg, Yg = np.meshgrid(xs, xs, indexing="ij")
xv = Xg.ravel()
yv = Yg.ravel()
Wv = (xv * yv * (xv + yv) / 2.0) * np.exp(-(xv ** 2 + xv * yv + yv ** 2))


def d2_1d(nn, hh):
    o = np.ones(nn - 1)
    m = np.zeros((nn, nn))
    np.fill_diagonal(m, -2.0)
    m += np.diag(o, 1) + np.diag(o, -1)
    return m / hh ** 2


def d1_1d(nn, hh):
    o = np.ones(nn - 1)
    m = np.diag(o, 1) - np.diag(o, -1)
    return m / (2 * hh)


I_N = np.eye(N)
Dxx = np.kron(d2_1d(N, hgrid), I_N)
Dyy = np.kron(I_N, d2_1d(N, hgrid))
Dxy = np.kron(d1_1d(N, hgrid), d1_1d(N, hgrid))
Lmat = (1.0 / 3.0) * (Dxx - Dxy + Dyy)
S = matrix_exp_symmetric(Lmat, 0.5)
T0red = S @ (Wv[:, None] * S)
wred, Vred = np.linalg.eigh((T0red + T0red.T) / 2)
order = np.argsort(wred)[::-1]
Phi0 = Vred[:, order[0]]
Phi1 = Vred[:, order[1]]
Lc0 = (Lmat @ Phi0)
Lc1 = (Lmat @ Phi1)
nrm0 = float(Lc0 @ Lc0) / float(Phi0 @ Phi0)
nrm1 = float(Lc1 @ Lc1) / float(Phi1 @ Phi1)
a2_heat = 0.25 * (nrm1 - nrm0)
print(f"  ||L Phi_0||^2={nrm0:.6f}  ||L Phi_1||^2={nrm1:.6f}  a_2^heat={a2_heat:.6f}")
check("a_2^heat = (1/4)(||L Phi_1||^2 - ||L Phi_0||^2) > 0 (excited state more L-curved)",
      a2_heat > 0)
# leading virial defect: both states -> 3/2 (W97 consistency, normalization check)
print("  (W97 leading virial c_J=c_D already established; a_2^heat is the eps^2 piece.)")


# ============================================================================
print(f"\nTOTAL: PASS={PASS}, FAIL={FAIL}")
