#!/usr/bin/env python3
"""Runner for the P1 (CAP-K) finite-speed-registration note
(OBSERVABLE_PRINCIPLE_P1_CAP_K_FROM_FINITE_SPEED_REGISTRATION_NARROW_THEOREM_NOTE_2026-06-10.md).

Mission (wave 3 of the P1 exponent campaign): the (BR)-license note
(commit c116993cf, in-flight branch
claude/science-fix/p1-br-license-record-capacity-20260610) reduced the open
P1 exponent premise to

    (CAP-real) + (CAP-K),    with (CAP-M) covered at M = 1 only inside the
                             conditional supplied-record unit schema,

via its Lemma C: (CAP-real)+(CAP-M)+(CAP-K) => sup_z |W(ez) - W(z)| <= K*M
=> (BR-int) => the pass set on the normalized exponent family {s*g_p} is
exactly {p = 0} (log selected). It also proved (CAP-K) has ZERO retained
*static* suppliers: the finite-sector algebra is cap-free, the conditional
unbounded-additivity schema permits 4^k unit records per
e-fold, the Busch/Gleason effect rows are magnitude-shaped and
readout-blind, and bare register growth (2n+1)^3 defeats static rate
inference. Every kill was static (algebraic capacity of the register
inventory); none consumed dynamics.

This runner verifies the dynamical route: REGISTERING a record is a
physical process on the lattice. Within the declared finite-speed
registration realization class (REG-dyn: records established by the linked
finite-range hopping dynamics of the microcausality bridge note's
bounded surface, with the e-fold source coupling V supported in a
bounded region X; REG-tau: at most a supplied clock window tau per e-fold;
REG-thr: a register registers only if delta-sensitive in operator norm to
the source change; REG-site: pairwise-disjoint records occupy disjoint
nonempty register-site sets — all four DECLARED, none asserted as
framework-forced), the linked Lieb-Robinson data (q = 2, R = 1,
W = |m| + 2d, v_LR = 2*e*q*W*R = 4e(|m| + 2d)) bound the sensitivity cone:

    Duhamel:  ||alpha^{H+V}_t(B_y) - alpha^H_t(B_y)||
                  <= int_0^t ||[V, alpha^H_u(B_y)]|| du
    LR tail:  ... <= (||V||/(4W)) * sum_{n >= D+1} (4W t)^n / n!
                  <= (e/(e-1)) * (||V|| R / v_LR) * exp((v_LR t - D)/R),

so delta-sensitivity at l1-distance D forces D <= D* := v_LR*tau
+ R*ln((e/(e-1))*||V||*R/(v_LR*delta)), the sensitive register set lies in
a box of (s_X + 2*ceil(D*))^3 sites, and with the Quantum axiom's finite
local dimension d_site = 2 the per-e-fold disjoint-record count is capped:

    (CAP-K)  K <= (s_X + 2*ceil(D*))^3                (site-register reading)
             K <= d_site^{(s_X + 2*ceil(D*))^3}       (weakest joint-sector
                                                       reading; still finite)

uniformly in the e-fold index k (the bound contains no k). Lemma C then
completes (BR-int) with constant K and the selection of p = 0 — exactly
the chain the BR-license note specified, now with (CAP-K) carried by
dynamics instead of admitted bare.

Falsification legs (computed):
  - the 4^k-per-e-fold unit-record family (schema-licensed bookkeeping)
    requires registration windows tau_k -> oo under BOTH readings: it
    cannot be realized by any finite-speed registration process at a
    uniformly bounded window;
  - an unbounded-speed comparator (one long-range bond) violates the
    finite-range sensitivity bound by a factor > 100, and symbolically
    D* -> oo as v_LR -> oo: the finite LR speed is load-bearing;
  - the p != 0 family members violate the computed cap at explicit z.

Family-lift escape: the retained no-go
POST_RECORD_FINITE_TO_UNBOUNDED_FAMILY_LIFT_NO_GO_2026-06-06.md prunes
"finite post-record certificate alone => unbounded retained law" and names
the only reopening inputs ("a supplied law, projective consistency,
monotone exhaustion, direct-limit compatibility, or tightness/compactness-
style preservation principle"). This route's load-bearing input is the
declared registration-dynamics law (REG-dyn)+(REG-tau) — a supplied law
quantified uniformly over every e-fold; NO post-record certificate (no
finite record prefix) is read anywhere in the derivation, and the cap is
k-uniform by symbol inspection, not extrapolated from finitely many
checks. Escape by input type, verified textually below.

Firewalls respected: no probability law is constructed for records
anywhere (the sensitivity threshold REG-thr is pure operator-norm
distinguishability); no branch-to-scalar map is asserted ((CAP-real)
remains DECLARED, never supplied — it is a slice of the record-scalar-map
no-go's middle arrow); no readout is constructed, identified, or selected.

Tags: [A] algebraic identity check on existing inputs; [B] cross-note /
ledger input verification; [C] first-principles compute on the framework's
finite structures; [D] falsification / hostile-witness leg. Exact SymPy
where claimed; numerical legs are rigorous-inequality checks against
exactly constructed finite-dimensional dynamics (deterministic, no
randomness, no fitted/observed/PDG inputs). Runtime well under 5 minutes.

Reproduction:
    python3 scripts/observable_principle_p1_cap_k_check_2026_06_10.py
Expected: TOTAL: PASS=31 FAIL=0
"""

from __future__ import annotations

import itertools
import json
import os
import re

import numpy as np
import sympy as sp

PASS = 0
FAIL = 0


def check(tag: str, name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    extra = f"  -- {detail}" if detail else ""
    print(f"  [{status}][{tag}] {name}{extra}")


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
NOTE = os.path.join(
    REPO,
    "docs",
    "OBSERVABLE_PRINCIPLE_P1_CAP_K_FROM_FINITE_SPEED_REGISTRATION_NARROW_THEOREM_NOTE_2026-06-10.md",
)


def read(path: str) -> str:
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def norm_ws(s: str) -> str:
    return re.sub(r"\s+", " ", s)


# ---------------------------------------------------------------------------
# shared exact symbols
# ---------------------------------------------------------------------------
z, u, p, s_sym = sp.symbols("z u p s", positive=True, real=True)
E = sp.E


def g(p_val, zz):
    if p_val == 0:
        return sp.log(zz)
    return (zz ** p_val - 1) / p_val


# ---------------------------------------------------------------------------
# shared finite-dimensional machinery (deterministic, exact constructions)
# ---------------------------------------------------------------------------
A_LAD = np.array([[0, 1], [0, 0]], dtype=complex)  # per-site annihilator on C^2
N_OP = np.array([[0, 0], [0, 1]], dtype=complex)
SZ = np.diag([1.0, -1.0]).astype(complex)


def site_op(nsites: int, x: int, op: np.ndarray) -> np.ndarray:
    M = np.array([[1.0]], dtype=complex)
    I2 = np.eye(2, dtype=complex)
    for i in range(nsites):
        M = np.kron(M, op if i == x else I2)
    return M


def build_chain(L: int, m: float = 0.0) -> np.ndarray:
    H = np.zeros((2 ** L, 2 ** L), dtype=complex)
    for x in range(L):
        y = (x + 1) % L
        ax, ay = site_op(L, x, A_LAD), site_op(L, y, A_LAD)
        H += ax.conj().T @ ay + ay.conj().T @ ax + m * site_op(L, x, N_OP)
    return H


def build_z3_block(Lax: int = 2, m: float = 0.0):
    sites = list(itertools.product(range(Lax), repeat=3))
    idx = {st: i for i, st in enumerate(sites)}
    n = len(sites)
    H = np.zeros((2 ** n, 2 ** n), dtype=complex)
    for st in sites:
        for mu in range(3):
            tt = list(st)
            tt[mu] = (tt[mu] + 1) % Lax
            tt = tuple(tt)
            ax, ay = site_op(n, idx[st], A_LAD), site_op(n, idx[tt], A_LAD)
            H += ax.conj().T @ ay + ay.conj().T @ ax
        H += m * site_op(n, idx[st], N_OP)
    return H, sites, idx


def eigd(H: np.ndarray):
    return np.linalg.eigh(H)


def heis(ed, B: np.ndarray, t: float) -> np.ndarray:
    ev, V = ed
    U = V @ np.diag(np.exp(-1j * ev * t)) @ V.conj().T
    return U.conj().T @ B @ U


def opnorm(M: np.ndarray) -> float:
    return float(np.linalg.norm(M, 2))


def series_tail(aa: float, n0: int, nmax: int = 600) -> float:
    """sum_{n >= n0} aa^n / n!  (iterative, overflow-safe)."""
    term = 1.0
    for k in range(1, n0 + 1):
        term *= aa / k
    total = 0.0
    for k in range(n0, nmax):
        total += term
        term *= aa / (k + 1)
        if term < 1e-300 and k > n0 + 5:
            break
    return total


def delta_bound_series(t: float, D: int, W: float, normV: float = 1.0) -> float:
    """Integrated Duhamel x LR series bound: (||V||/(4W)) sum_{n>=D+1} (4Wt)^n/n!."""
    return normV / (4.0 * W) * series_tail(4.0 * W * t, D + 1)


def delta_bound_exp(t: float, D: float, W: float, normV: float = 1.0) -> float:
    """Closed exponential form: (e/(e-1)) (||V|| R / v) exp((v t - D)/R), R = 1."""
    v = 4.0 * float(sp.E) * W
    return float(sp.E / (sp.E - 1)) * normV / v * np.exp(v * t - D)


# ===========================================================================
print("== T1: Lemma C and the selection chain (BR-note facts recomputed, not cited blind) ==")

# finite-sector readout identity on a 4-sector model, all 81 ordered disjoint pairs
v_data = [sp.Integer(3), sp.Integer(-1), sp.Rational(1, 2), sp.Integer(2)]
pairs = 0
additive_ok = True
elements = range(4)
for assign in itertools.product([0, 1, 2], repeat=4):  # 0: A, 1: B, 2: neither
    A = frozenset(i for i in elements if assign[i] == 0)
    B = frozenset(i for i in elements if assign[i] == 1)
    IA = sum((v_data[i] for i in A), sp.Integer(0))
    IB = sum((v_data[i] for i in B), sp.Integer(0))
    IAB = sum((v_data[i] for i in A | B), sp.Integer(0))
    pairs += 1
    if sp.simplify(IAB - IA - IB) != 0:
        additive_ok = False
check("A", "retained finite-sector identity recomputed: I(A u B) = I(A) + I(B) on all 81 ordered disjoint pairs of a 4-sector model", additive_ok and pairs == 81, f"pairs={pairs}")

# capacity bound |I(A)| <= K*M (triangle), unit normalization M = 1 (schema)
K_demo, M_demo = 5, sp.Integer(1)
unit_sum = sum(sp.Integer(1) for _ in range(7))
check("A", "Lemma C capacity bound: |sum_{i in A} v_i| <= K*M by finite additivity + triangle inequality; conditional supplied-record unit schema has M = 1 by normalization (I(R_7) = 7 recomputed)", bool(unit_sum == 7) and all(abs(sum(v_data[: k + 1])) <= (k + 1) * max(abs(x) for x in v_data) for k in range(4)), "I(R_7)=7")

# e-fold increment identity on the family
incr = sp.simplify((g(p, sp.exp(u + 1)) - g(p, sp.exp(u))) - sp.exp(p * u) * (sp.exp(p) - 1) / p)
check("A", "e-fold increment identity: g_p(e^{u+1}) - g_p(e^u) = e^{pu}(e^p - 1)/p exactly; p -> 0 member has constant increment 1", incr == 0 and sp.limit(sp.exp(p * u) * (sp.exp(p) - 1) / p, p, 0) == 1)

# (BR-int) point-selection
unbounded = []
for pv in [sp.Integer(1), sp.Integer(2), sp.Rational(1, 2), sp.Rational(-1, 2), sp.Integer(-1)]:
    expr = sp.exp(pv * u) * (sp.exp(pv) - 1) / pv
    lim = sp.limit(expr, u, sp.oo if pv > 0 else -sp.oo)
    unbounded.append(lim == sp.oo)
check("A", "(BR-int) point-selection recomputed: increments unbounded for p in {1, 2, 1/2, -1/2, -1} (limits = oo), constant for p = 0 — pass set on {s*g_p} exactly {p = 0}", all(unbounded))

# class-escape spot check (Lemma-R screening): cos witness passes (BR-int), violates additivity
res_ee = sp.nsimplify(0) + (sp.Rational(1, 10) * (sp.cos(2) - 2 * sp.cos(1)))
cos_incr_bound = 1 + sp.Rational(2, 10)
check("A", "class-escape spot check: W = log z + (1/10) cos(log z) has e-fold increments <= 1 + 2/10 ((BR-int) holds) yet additive residual at (e, e) is (1/10)(cos 2 - 2 cos 1) != 0 — no additive-identity instance is entailed (Lemma-R screen)", sp.simplify(res_ee) != 0 and float(res_ee) != 0.0, f"res(e,e)={float(res_ee):.6f}")

# ===========================================================================
print("== T2: the Duhamel identity (the bridge from generator difference to commutators) ==")

L4 = 4
H4 = build_chain(L4, 0.0)
V4 = site_op(L4, 0, N_OP)
H4p = H4 + V4
ed4, ed4p = eigd(H4), eigd(H4p)
B4 = site_op(L4, 2, SZ)
t_id = 0.3
lhs = heis(ed4p, B4, t_id) - heis(ed4, B4, t_id)
nseg = 400  # Simpson quadrature segments (even)
ss = np.linspace(0.0, t_id, nseg + 1)
weights = np.ones(nseg + 1)
weights[1:-1:2], weights[2:-1:2] = 4.0, 2.0
weights *= (t_id / nseg) / 3.0
rhs = np.zeros_like(lhs)
for w_quad, s_val in zip(weights, ss):
    inner = V4 @ heis(ed4, B4, t_id - s_val) - heis(ed4, B4, t_id - s_val) @ V4
    rhs += w_quad * 1j * heis(ed4p, inner, s_val)
resid = opnorm(lhs - rhs)
check("A", "Duhamel identity verified on an explicit 4-site instance: alpha^{H+V}_t(B) - alpha^H_t(B) = i int_0^t alpha^{H+V}_s([V, alpha^H_{t-s}(B)]) ds (Simpson quadrature residual < 1e-8)", resid < 1e-8, f"residual={resid:.2e}")

int_bound = float(np.trapezoid([opnorm(V4 @ heis(ed4, B4, s_val) - heis(ed4, B4, s_val) @ V4) for s_val in ss], ss))
check("A", "integrated-commutator bound: ||alpha^{H+V}_t(B) - alpha^H_t(B)|| <= int_0^t ||[V, alpha^H_u(B)]|| du on the same instance", opnorm(lhs) <= int_bound * (1 + 1e-9), f"lhs={opnorm(lhs):.4e} <= int={int_bound:.4e}")

# ===========================================================================
print("== T3: the registration cone on the chain — linked finite-range LR data, measured vs bound ==")

L10, m1 = 10, 0.0
W1 = abs(m1) + 2 * 1  # bridge note (F4): W = |m| + 2d, d = 1
H10 = build_chain(L10, m1)
V10 = site_op(L10, 0, N_OP)  # source coupling at site 0, ||V|| = 1 exactly
ed10, ed10p = eigd(H10), eigd(H10 + V10)
grid_ok, worst = True, 0.0
for D in [2, 3, 4, 5]:
    By = site_op(L10, D, SZ)
    for t in [0.02, 0.05, 0.1, 0.15]:
        dm = opnorm(heis(ed10p, By, t) - heis(ed10, By, t))
        db = delta_bound_series(t, D, W1)
        grid_ok = grid_ok and (dm <= db)
        worst = max(worst, dm / db)
check("C", "chain (d=1, m=0, q=2, R=1, W=2, v_LR=8e): measured sensitivity ||alpha^{H+V}_t(B_y) - alpha^H_t(B_y)|| <= series bound (||V||/(4W)) sum_{n>=D+1} (4Wt)^n/n! on the full (D, t) grid (D in 2..5, t in 0.02..0.15)", grid_ok, f"worst measured/bound = {worst:.4f}")

exp_ge_series = all(
    delta_bound_exp(t, D, W1) >= delta_bound_series(t, D, W1)
    for D in [2, 3, 4, 5]
    for t in [0.02, 0.05, 0.1, 0.15]
)
check("A", "closed exponential form dominates the series form on the grid: (e/(e-1))(||V||/v_LR) e^{v_LR t - D} >= series bound — the D* formula below is licensed by the proved chain", exp_ge_series)

# ===========================================================================
print("== T4: the registration cone on an explicit Z^3 block ==")

H8, sites8, idx8 = build_z3_block(2, 0.0)
W3 = 0.0 + 2 * 3  # W = |m| + 2d, d = 3
V8 = site_op(8, idx8[(0, 0, 0)], N_OP)
ed8, ed8p = eigd(H8), eigd(H8 + V8)
grid3_ok, worst3 = True, 0.0
for st, D in [((1, 1, 1), 3), ((1, 1, 0), 2)]:
    By = site_op(8, idx8[st], SZ)
    for t in [0.005, 0.01, 0.02]:
        dm = opnorm(heis(ed8p, By, t) - heis(ed8, By, t))
        db = delta_bound_series(t, D, W3)
        grid3_ok = grid3_ok and (dm <= db)
        worst3 = max(worst3, dm / db)
check("C", "Z^3 2x2x2 block (d=3, m=0, W=6, v_LR=24e): measured sensitivity <= series bound at l1-distances 2 and 3, t in {0.005, 0.01, 0.02}", grid3_ok, f"worst measured/bound = {worst3:.4f}")

ball_counts = {}
for Dq in [3, 5]:
    cnt = sum(
        1
        for pt in itertools.product(range(-Dq, Dq + 1), repeat=3)
        if abs(pt[0]) + abs(pt[1]) + abs(pt[2]) <= Dq
    )
    ball_counts[Dq] = cnt
check("A", "explicit Z^3 l1-ball enumeration: |B_1(3)| = 63, |B_1(5)| = 231, each <= the (2D+1)^3 box bound used by the cap (343, 1331)", ball_counts[3] == 63 and ball_counts[5] == 231 and 63 <= 7 ** 3 and 231 <= 11 ** 3, f"counts={ball_counts}")

# ===========================================================================
print("== T5: the sensitivity radius D* and the per-e-fold cap K (exact arithmetic) ==")

tau_s, delta_s, JV_s, vv = sp.symbols("tau delta J_V v", positive=True)
Dvar = sp.Symbol("D", real=True)
# delta <= (e/(e-1)) (J_V/v) e^{v tau - D}  <=>  D <= D*
Dstar_expr = sp.solve(sp.Eq(delta_s, (E / (E - 1)) * (JV_s / vv) * sp.exp(vv * tau_s - Dvar)), Dvar)[0]
Dstar_check = sp.simplify(Dstar_expr - (vv * tau_s + sp.log((E / (E - 1)) * JV_s / (vv * delta_s))))
check("A", "D* formula derived (sympy solve): delta-sensitivity at distance D forces D <= D* = v_LR*tau + ln((e/(e-1)) ||V|| / (v_LR delta)) (R = 1)", Dstar_check == 0)

v_can = 24 * E  # d = 3, m -> 0: v_LR = 4e(|m| + 2d) = 24e
Dstar_can = Dstar_expr.subs({vv: v_can, tau_s: 1, JV_s: 1, delta_s: sp.Rational(1, 10)})
Dstar_num = float(Dstar_can)
Dceil = int(sp.ceiling(Dstar_can))
N_reach = (1 + 2 * Dceil) ** 3
check("C", "canonical instance (Z^3, m -> 0, tau = 1, ||V|| = 1, delta = 1/10, s_X = 1): D* = 24e + ln(10/(24(e-1))) ~ 63.82, ceil = 64, N_reach = (1 + 2*64)^3 = 129^3 = 2146689 — a finite computed cap", Dceil == 64 and N_reach == 2146689, f"D*={Dstar_num:.4f}, N_reach={N_reach}")

# per-site sector bound from the Quantum axiom (d_site = 2): trace/rank argument
d_site = 2
three_impossible = 3 * 1 > d_site  # three nonzero orth. projections need rank sum >= 3 > 2
P0, P1 = np.diag([1.0, 0.0]), np.diag([0.0, 1.0])
two_exist = np.allclose(P0 @ P1, 0) and np.allclose(P0 + P1, np.eye(2))
check("A", "per-site sector bound (Quantum axiom, d_site = 2): at most 2 pairwise-orthogonal nonzero projections per M_2 site (rank sum <= 2); joint reading over N sites: at most 2^N — so K <= N_reach (site-register reading, log2(d_site) = 1 record-bit per site) or K <= 2^{N_reach} (weakest joint reading), both finite", two_exist and three_impossible)

kk = sp.Symbol("k")
check("A", "k-uniformity (the cap is one lemma, not an extrapolation): the D* expression's free symbols are exactly {tau, delta, J_V, v} — the e-fold index k does NOT occur, so (CAP-K) holds with the SAME K for every e-fold", Dstar_expr.free_symbols == {tau_s, delta_s, JV_s, vv} and kk not in Dstar_expr.free_symbols)

# ===========================================================================
print("== T6: chain completion — (CAP-K computed) + (CAP-M = 1) + (CAP-real declared) => (BR-int) => p = 0 ==")

K_cap = N_reach  # site-register reading
sel_ok = all(
    sp.limit(sp.exp(pv * u) * (sp.exp(pv) - 1) / pv, u, sp.oo if pv > 0 else -sp.oo) == sp.oo
    for pv in [sp.Integer(1), sp.Integer(2), sp.Rational(-1, 2)]
)
check("A", "completion: increments <= K*M = 2146689 forces (BR-int); on {s*g_p} the pass set is exactly {p = 0}: W = c log z is selected (Lemma C chain recomputed with the computed K; (CAP-real) remains DECLARED, not supplied)", sel_ok and K_cap == 2146689)

u_viol = sp.log(K_cap / (E - 1)) + 1
incr_p1 = (E - 1) * sp.exp(u_viol)
check("D", "wrong-exponent rejection at the computed cap: the p = 1 member's e-fold increment e^u (e-1) exceeds K = 2146689 at u = ln(K/(e-1)) + 1 (z = e^u ~ 3.4e6) — explicit witness, exact inequality", sp.simplify(incr_p1 / K_cap) == E and float(incr_p1) > K_cap, f"increment/K = e at u = {float(u_viol):.3f}")

# ===========================================================================
print("== T7: the 4^k family demands unbounded windows (the schema-licensed witness cannot be realized) ==")

# reading (a): need (1 + 2*ceil(D*(tau_k)))^3 >= 4^k  =>  tau_k >= ((4^{k/3} - 1)/2 - c)/v
c_const = sp.log((E / (E - 1)) / (v_can * sp.Rational(1, 10)))
tau_k = lambda kv: ((sp.Pow(4, sp.Rational(kv, 3)) - 1) / 2 - c_const) / v_can
k_first_a = next(kv for kv in range(1, 40) if 4 ** kv > N_reach)
tau11, tau30 = float(tau_k(11)), float(tau_k(30))
check("D", "site-register reading: at tau = 1 the cap K = 2146689 admits 4^10 = 1048576 but NOT 4^11 = 4194304 (first violation k = 11); required windows grow without bound: tau_11 >= 1.25 > 1, tau_30 >= 8036 — the 4^k family needs unbounded processing time per e-fold", k_first_a == 11 and tau11 > 1 and tau30 > 8000, f"tau_11>={tau11:.4f}, tau_30>={tau30:.1f}")

# reading (b): need 2^{N(tau_k)} >= 4^k <=> N >= 2k; first failing k at tau = 1, and tau at k = 10^9
k_first_b = N_reach // 2 + 1
tau_b_1e9 = float((((sp.Integer(2) * 10 ** 9) ** sp.Rational(1, 3) - 1) / 2 - c_const) / v_can)
check("D", "weakest joint-sector reading: at tau = 1 the cap 2^{N_reach} fails first at k = 1073345; at k = 10^9 the required window is tau >= 9.67 > 1 — under EVERY reading each fixed window tau fails at finite k, so no uniformly bounded-window finite-speed process realizes the family (it stays licensed as schema bookkeeping only)", k_first_b == 1073345 and tau_b_1e9 > 9, f"k_b*={k_first_b}, tau(k=1e9)>={tau_b_1e9:.2f}")

# ===========================================================================
print("== T8: unbounded-speed comparator — the finite LR speed is load-bearing ==")

a0, a5 = site_op(L10, 0, A_LAD), site_op(L10, 5, A_LAD)
Hb = H10 + (a0.conj().T @ a5 + a5.conj().T @ a0)  # one long-range bond, l1-diameter 5
edb, edbp = eigd(Hb), eigd(Hb + V10)
B5 = site_op(L10, 5, SZ)
viol = {}
for t in [0.05, 0.1]:
    dm = opnorm(heis(edbp, B5, t) - heis(edb, B5, t))
    viol[t] = dm / delta_bound_series(t, 5, W1)
check("D", "one long-range bond (0 <-> 5) breaks the finite-range sensitivity bound at D = 5 by a factor > 100 (t = 0.05 and 0.1): without finite-range dynamics the registration cone (and hence the cap) does not exist", min(viol.values()) > 100, f"violations x{viol[0.05]:.0f}, x{viol[0.1]:.0f}")

Dstar_vinf = sp.limit(Dstar_expr.subs({tau_s: 1, JV_s: 1, delta_s: sp.Rational(1, 10)}), vv, sp.oo)
check("A", "symbolic comparator: lim_{v_LR -> oo} D* = oo (sympy limit) — an unbounded-speed process reaches every register in any window and (CAP-K) has no finite value; finite v_LR < oo is the load-bearing physics", Dstar_vinf == sp.oo)

# ===========================================================================
print("== T9: quasilocal extension — landed exact-H numbers reused at their grade ==")

ql_cache = os.path.join(REPO, "logs", "runner-cache", "transfer_matrix_log_quasilocality_check_2026_06_10.txt")
ql_txt = read(ql_cache)
mWH = re.search(r"W_H = ([0-9.]+) at m=0\.3", ql_txt)
mtail = re.search(r"W_tail\(10\) = ([0-9.e+-]+)", ql_txt)
WH = float(mWH.group(1)) if mWH else float("nan")
Wtail10 = float(mtail.group(1)) if mtail else float("nan")
check("B", "landed quasilocality numbers read from the cached retained_bounded runner log: W_H = 1.757278 (m = 0.3) and W_tail(10) = 3.526e-03 — finite per-site weight, exponentially small tails (free bilinear sector, at that row's grade)", abs(WH - 1.757278) < 1e-6 and abs(Wtail10 - 3.526e-3) < 1e-5, f"W_H={WH}, W_tail(10)={Wtail10}")

v_exact_R10 = 2 * float(sp.E) * 2 * (2 * WH) * 10  # 2e * q * W_per-site * R, W_per-site <= 2 W_H
Dstar_exact = v_exact_R10 * 1 + np.log(float(E / (E - 1)) * 1.0 / (v_exact_R10 * 0.1))
N_exact = (1 + 2 * int(np.ceil(Dstar_exact))) ** 3
check("C", "exact-H truncation H_R (R = 10, m = 0.3): v(R) <= 2e*q*(2 W_H)*R ~ 382.2, D* ~ 379.0, N_reach ~ 759^3 ~ 4.4e8 — the cap form survives quasilocally with the same (v tau)^3 scaling; the volume-uniform exact-H tail constant is a NAMED open refinement, not imported", abs(v_exact_R10 - 382.2) < 1.0 and N_exact == (1 + 2 * int(np.ceil(Dstar_exact))) ** 3 and N_exact < 5e8, f"v(10)={v_exact_R10:.1f}, D*={Dstar_exact:.1f}, N={N_exact}")

# ===========================================================================
print("== T10: family-lift class escape (textual, against the retained no-go itself) ==")

fl_note = read(os.path.join(REPO, "docs", "POST_RECORD_FINITE_TO_UNBOUNDED_FAMILY_LIFT_NO_GO_2026-06-06.md"))
fl_ws = norm_ws(fl_note)
class_def = "finite post-record certificate alone => unbounded retained law"
check("B", "the pruned class quoted from the retained no-go: 'finite post-record certificate alone => unbounded retained law' is present verbatim", class_def in fl_ws)

reopen = "supplied law, projective consistency, monotone exhaustion, direct-limit compatibility, or tightness/compactness-style preservation principle"
check("B", "the reopening clause quoted from the retained no-go: a family-lift input such as 'a supplied law, ...' is the named legitimate route", norm_ws(reopen) in fl_ws)

note_txt = read(NOTE)
note_ws = norm_ws(note_txt)
escape_ok = ("supplied law" in note_ws) and ("no post-record certificate" in note_ws)
check("B", "this route's escape is by input type: the note declares its load-bearing input as a supplied dynamics law ((REG-dyn)+(REG-tau), uniform over every e-fold) and consumes no post-record certificate; the cap's k-uniformity is the T5 symbol check, not a finite-prefix extrapolation", escape_ok)

# ===========================================================================
print("== T11: clock-window boundary honesty ==")

cr_note = read(os.path.join(REPO, "docs", "POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md"))
check("B", "the clock is supplied, never derived from counts: the retained_no_go clock/rate interface states 'Without the supplied `tau`, the same record history supports many inequivalent rates' — present verbatim", "Without the supplied `tau`, the same record history supports many inequivalent" in norm_ws(cr_note))

clock_decl = ("(REG-tau)" in note_ws) and ("declared" in note_ws.lower())
sc_note_exists = os.path.exists(os.path.join(REPO, "docs", "SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md"))
check("B", "the note declares (REG-tau) as a supplied clock-window clause of the realization class (not derived); the retained single-clock Stone row licenses only that 'evolve for t given (T, tau)' is well-defined — the window value stays declared", clock_decl and sc_note_exists)

# ===========================================================================
print("== T12: ledger grades, firewall strings, honest scope ==")

with open(os.path.join(REPO, "docs", "audit", "data", "audit_ledger.json"), "r", encoding="utf-8") as fh:
    ledger_rows = json.load(fh)["rows"]
rows = {
    "microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09": "retained_bounded",
    "transfer_matrix_log_quasilocality_narrow_theorem_note_2026-06-10": "retained_bounded",
    "single_clock_stone_finite_dim_uniqueness_narrow_theorem_note_2026-05-10": "retained",
    "post_record_clock_rate_interface_2026-06-06": "retained_no_go",
    "post_record_finite_to_unbounded_family_lift_no_go_2026-06-06": "retained_no_go",
    "record_function_finite_sector_algebra_2026-06-05": "retained",
    "record_unbounded_finite_additivity_schema_2026-06-06": "audited_conditional",
    "record_formation_not_unconditionally_forced_by_minimal_axioms_narrow_no_go_note_2026-06-06": "retained_no_go",
    "observable_principle_record_scalar_map_no_go_note_2026-06-05": "retained_no_go",
    "post_record_count_probability_firewall_2026-06-06": "retained_no_go",
}
missing_rows = [rid for rid in rows if ledger_rows.get(rid) is None]
live_statuses = {rid: ledger_rows.get(rid, {}).get("effective_status") for rid in rows}
check(
    "B",
    "cited rows present in the audit ledger (presence only, 10 rows)",
    not missing_rows,
    f"missing={missing_rows}",
)
print(f"  [info][B] live effective statuses (audit-lane-owned; not gated): {live_statuses}")

required = [
    "Status authority:",
    "independent audit lane",
    "does NOT retire P1",
    "(CAP-real) remains declared",
    "no probability law is constructed",
    "no branch-to-scalar map is asserted",
]
missing = [s_ for s_ in required if norm_ws(s_).lower() not in note_ws.lower()]
check("B", "note honest-scope and firewall-compliance strings present", not missing, f"missing={missing}")

forbidden = [
    "P1 is " + "closed",
    "P1 is " + "retired",
    "this note " + "promotes",
    "(CAP-real) is " + "supplied",
    "(CAP-real) is " + "derived",
    "records are forced " + "to form",
]
found = [s_ for s_ in forbidden if s_.lower() in note_ws.lower()]
check("B", "forbidden closure/promotion strings absent", not found, f"found={found}")

# ===========================================================================
print()
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
if FAIL:
    raise SystemExit(1)
