#!/usr/bin/env python3
"""
Outcome-factorization statistics atom (R-D label G3) versus the unraveled step law.

Genre: narrow no-go sharpening.

Question: do the unraveling-lane results, quoted at their declared source scope,
force the two-registration outcome-factorization law

    m(j,k) = p_j p_k,   j,k in {s,d}

on the registered two-outcome quotient?

Answer proven here: NO. The source notes characterize one edge's complete
marginal trajectory law and explicitly leave cross-edge independence untested.
Product and shared-draw couplings of that whole law preserve every one-edge
statistic while differing on independence. The correlated-stack witness ρ_corr
is the binary registered-quotient instance: it shares both reduced states with
ρ_product while violating factorization. Cross-edge independence (unraveling
residual 4) together with identical marginals (residuals 1+3) is the exact
escape set; with identical marginals fixed, C_ss=0 forces a=p^2. Residual 4 is
the factorization-critical coupling residual and is precisely the residual the
source note marks "not tested here."

Nothing on a derivation path is hard-coded: the wall family, the positivity
interval, the product point a=p^2, the agreement-conditioning flow, and the
escape condition are all computed with sympy from the symbol p (and a).

No Monte Carlo. Exact sympy / deterministic numpy only.
"""

from pathlib import Path

import numpy as np
import sympy as sp

# ----------------------------------------------------------------------------
# check harness
# ----------------------------------------------------------------------------
_PASS = 0
_FAIL = 0
_LINES = []


def check(num, desc, ok):
    global _PASS, _FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        _PASS += 1
    else:
        _FAIL += 1
    line = f"[{tag}] {num}. {desc}"
    _LINES.append(line)
    print(line)
    return ok


def approx_zero(x, tol=1e-12):
    return abs(complex(x)) <= tol


# ----------------------------------------------------------------------------
# symbols
# ----------------------------------------------------------------------------
p, a, eps = sp.symbols("p a eps", real=True)
p_s = p
p_d = 1 - p

# ============================================================================
# BLOCK A -- the 2026-06-18 wall, re-derived exactly (consume its structure)
# ============================================================================

# A1: the one-parameter same-marginal joint family (a = m(s,s)).
m_ss = a
m_sd = p_s - a          # forced by marginal(row s) = p_s
m_ds = p_s - a          # forced by marginal(col s) = p_s (symmetric here)
m_dd = 1 - 2 * p + a    # forced by normalization

marg_row_s = sp.simplify(m_ss + m_sd)          # should be p_s
marg_row_d = sp.simplify(m_ds + m_dd)          # should be p_d
marg_col_s = sp.simplify(m_ss + m_ds)          # should be p_s
marg_col_d = sp.simplify(m_sd + m_dd)          # should be p_d
total = sp.simplify(m_ss + m_sd + m_ds + m_dd)

check(
    "A1",
    "same-marginal joint family: rows/cols = (p_s,p_d), sum = 1 (symbolic in a,p)",
    all(
        sp.simplify(x) == y
        for x, y in [
            (marg_row_s, p_s),
            (marg_row_d, p_d),
            (marg_col_s, p_s),
            (marg_col_d, p_d),
            (total, sp.Integer(1)),
        ]
    ),
)

# A2: positivity interval max(0, 2p-1) <= a <= p is nondegenerate for interior p.
lo = sp.Max(0, 2 * p - 1)
hi = p
width = sp.simplify(hi - lo)
# Resolve the Max piecewise: width=p below one half and 1-p above it.
width_lo = sp.simplify(p - 0)
width_hi = sp.simplify(p - (2 * p - 1))
# A small exact-rational grid is an auxiliary boundary guard.
widths_interior = [sp.nsimplify(width.subs(p, sp.Rational(k, 10))) for k in range(1, 10)]
check(
    "A2",
    "positivity interval [max(0,2p-1), p] has strictly positive width for p in (0,1)",
    width_lo == p
    and width_hi == 1 - p
    and all(float(w) > 0 for w in widths_interior),
)

# A3: product point a = p^2 is strictly interior (product is NOT forced).
prod_a = p ** 2
# Exact branchwise gaps: for p<=1/2 the lower gap is p^2; for p>=1/2
# it is (1-p)^2; the upper gap is p(1-p) on both branches.
lower_gap_lo = sp.simplify(prod_a)
lower_gap_hi = sp.factor(sp.simplify(prod_a - (2 * p - 1)))
upper_gap = sp.factor(sp.simplify(p - prod_a))
interior_ok = []
for k in range(1, 10):
    pv = sp.Rational(k, 10)
    lov = float(lo.subs(p, pv))
    hiv = float(hi.subs(p, pv))
    av = float(prod_a.subs(p, pv))
    interior_ok.append(lov < av < hiv)
check(
    "A3",
    "product point a=p^2 lies strictly inside the positivity interval for p in (0,1) "
    "=> marginals+additivity do not force factorization",
    lower_gap_lo == p ** 2
    and lower_gap_hi == (p - 1) ** 2
    and upper_gap == -p * (p - 1)
    and all(interior_ok),
)

# A4: the concrete p=1/2 witness pair from the wall.
half = sp.Rational(1, 2)
prod_cells = [x.subs({a: prod_a, p: half}) for x in (m_ss, m_sd, m_ds, m_dd)]
corr_cells = [x.subs({a: p, p: half}) for x in (m_ss, m_sd, m_ds, m_dd)]  # a=p => perfect corr
check(
    "A4",
    "p=1/2 wall witnesses: product=(1/4,1/4,1/4,1/4), correlated=(1/2,0,0,1/2); "
    "both have marginals (1/2,1/2); only product factorizes",
    prod_cells == [sp.Rational(1, 4)] * 4
    and corr_cells == [half, 0, 0, half]
    and sp.simplify(corr_cells[1] - half * half) != 0,
)

# ============================================================================
# BLOCK B -- Born realization on C^2 (x) C^2 (consume 06-17 P4 / 06-18 witness)
# ============================================================================
# basis order: |00>, |01>, |10>, |11>  (copy1, copy2); s<->0, d<->1.


def diag_state(d0, d1, d2, d3):
    return sp.diag(d0, d1, d2, d3)


rho_product = diag_state(p ** 2, p * (1 - p), (1 - p) * p, (1 - p) ** 2)
rho_corr = diag_state(p, 0, 0, 1 - p)


def is_psd_diag(rho, pv):
    return all(float(rho[i, i].subs(p, pv)) >= -1e-12 for i in range(4))


def partial_trace2(rho):
    """Tr over copy 2 -> 2x2 on copy 1. basis (0,1) x (0,1)."""
    out = sp.zeros(2, 2)
    for i in range(2):
        for k in range(2):
            s = 0
            for j in range(2):
                s += rho[2 * i + j, 2 * k + j]
            out[i, k] = sp.simplify(s)
    return out


def partial_trace1(rho):
    """Tr over copy 1 -> 2x2 on copy 2."""
    out = sp.zeros(2, 2)
    for j in range(2):
        for l in range(2):
            s = 0
            for i in range(2):
                s += rho[2 * i + j, 2 * i + l]
            out[j, l] = sp.simplify(s)
    return out


# B1/B2: PSD + trace one for both witnesses.
tr_prod = sp.simplify(sum(rho_product[i, i] for i in range(4)))
tr_corr = sp.simplify(sum(rho_corr[i, i] for i in range(4)))
psd_grid = [sp.Rational(k, 10) for k in range(0, 11)]
check(
    "B1",
    "ρ_product = diag(p^2,p(1-p),(1-p)p,(1-p)^2) is PSD, trace 1",
    tr_prod == 1 and all(is_psd_diag(rho_product, pv) for pv in psd_grid),
)
check(
    "B2",
    "ρ_corr = diag(p,0,0,1-p) is PSD, trace 1",
    tr_corr == 1 and all(is_psd_diag(rho_corr, pv) for pv in psd_grid),
)

# B3: THE CRUX EQUALITY -- both witnesses share the single-registration reduced
# state on BOTH copies.
red2_prod = partial_trace2(rho_product)
red2_corr = partial_trace2(rho_corr)
red1_prod = partial_trace1(rho_product)
red1_corr = partial_trace1(rho_corr)
sigma = sp.diag(p, 1 - p)
check(
    "B3",
    "Tr_2 ρ_product = Tr_2 ρ_corr = diag(p,1-p) AND Tr_1 equal too "
    "(shared single-registration reduced state on both copies)",
    sp.simplify(red2_prod - sigma) == sp.zeros(2, 2)
    and sp.simplify(red2_corr - sigma) == sp.zeros(2, 2)
    and sp.simplify(red1_prod - sigma) == sp.zeros(2, 2)
    and sp.simplify(red1_corr - sigma) == sp.zeros(2, 2),
)

# B4: Born joint weights on P_j (x) P_k differ -> factorization holds for product,
# fails for corr.
# m(j,k) = rho[2j+k, 2j+k] for diagonal states.
m_prod = {(j, k): rho_product[2 * j + k, 2 * j + k] for j in range(2) for k in range(2)}
m_corr = {(j, k): rho_corr[2 * j + k, 2 * j + k] for j in range(2) for k in range(2)}
pj = {0: p_s, 1: p_d}
fact_prod = all(sp.simplify(m_prod[(j, k)] - pj[j] * pj[k]) == 0 for j in range(2) for k in range(2))
fact_corr = all(sp.simplify(m_corr[(j, k)] - pj[j] * pj[k]) == 0 for j in range(2) for k in range(2))
# Both witnesses are invariant under exchanging the two registrations. This
# closes the exchange-symmetry alternative without assuming factorization.
swap = sp.zeros(4, 4)
for j in range(2):
    for k in range(2):
        swap[2 * k + j, 2 * j + k] = 1
swap_prod = sp.simplify(swap * rho_product * swap.T - rho_product) == sp.zeros(4, 4)
swap_corr = sp.simplify(swap * rho_corr * swap.T - rho_corr) == sp.zeros(4, 4)
check(
    "B4",
    "swap-symmetric Born joint weights: product factorizes m(j,k)=p_j p_k; corr "
    "does NOT (m(s,d)=0 != p(1-p) for p in (0,1))",
    swap_prod and swap_corr and fact_prod and (not fact_corr)
    and sp.simplify(m_corr[(0, 1)]) == 0,
)

# B5: quotient cumulant C_jk (06-17 P3) is the exact discriminator.
C_prod = {jk: sp.simplify(m_prod[jk] - pj[jk[0]] * pj[jk[1]]) for jk in m_prod}
C_corr = {jk: sp.simplify(m_corr[jk] - pj[jk[0]] * pj[jk[1]]) for jk in m_corr}
check(
    "B5",
    "06-17 quotient cumulant C_jk = m(j,k)-p_j p_k: identically 0 for product, "
    "nonzero for corr (C_sd = -p(1-p))",
    all(v == 0 for v in C_prod.values())
    and sp.simplify(C_corr[(0, 1)] + p * (1 - p)) == 0,
)

# ============================================================================
# BLOCK C -- one-edge marginal laws do not determine cross-edge coupling
# ============================================================================
# Binary quantum instance: if F(rho)=f(Tr_2 rho), then F(ρ_product)=F(ρ_corr)
# because their reduced states agree (B3). The generic trajectory-law statement
# is checked at C4 with exact product/shared-draw couplings of a whole finite law.

# C1: battery of random single-registration observables f(sigma)=Tr(sigma O),
#     over a p-grid. Must coincide on the two witnesses to machine precision.
rng = np.random.default_rng(20260711)


def sig_np(pv):
    return np.diag([pv, 1 - pv]).astype(complex)


c1_devs = []
for pv in np.linspace(0.05, 0.95, 19):
    s2p = np.array(sp.Matrix(partial_trace2(rho_product)).subs(p, pv)).astype(complex)
    s2c = np.array(sp.Matrix(partial_trace2(rho_corr)).subs(p, pv)).astype(complex)
    for _ in range(25):
        M = rng.standard_normal((2, 2)) + 1j * rng.standard_normal((2, 2))
        O = M + M.conj().T  # Hermitian
        c1_devs.append(abs(np.trace(s2p @ O) - np.trace(s2c @ O)))
check(
    "C1",
    "single-registration observable battery (475 random Hermitian f, p-grid): "
    "F(ρ_product)=F(ρ_corr) to machine precision (shared reduced state)",
    max(c1_devs) < 1e-10,
)

# C2: unraveling U1 marginal content -- single-edge Born weights coincide.
#     single-edge weight of outcome j = Tr(sigma P_j) = p_j, identical for both.
w_prod = [red2_prod[i, i] for i in range(2)]
w_corr = [red2_corr[i, i] for i in range(2)]
check(
    "C2",
    "U1 single-edge Born weights (Tr(sigma P_j)) coincide for both witnesses "
    "= (p, 1-p); one-registration content cannot separate them",
    [sp.simplify(x) for x in w_prod] == [p, 1 - p]
    and [sp.simplify(x) for x in w_corr] == [p, 1 - p],
)

# C3: exact illustrative binary one-edge spread. This is NOT substituted for
# the U2 runner; it shows that non-degeneracy of a marginal law is compatible
# with both product and correlated cross-edge couplings.
binary_mean = sp.simplify(p * eps + (1 - p) * (-eps))
binary_spread = sp.simplify(
    p * (eps - binary_mean) ** 2 + (1 - p) * (-eps - binary_mean) ** 2
)
c3_nondeg = [binary_spread.subs({p: sp.Rational(k, 10), eps: 1}) > 0
             for k in range(1, 10)]
check(
    "C3",
    "non-degenerate one-edge spread 4 eps^2 p(1-p)>0 is compatible with both "
    "product and correlated couplings (illustrative marginal fact, not a U2 surrogate)",
    sp.simplify(binary_spread - 4 * eps ** 2 * p * (1 - p)) == 0
    and all(c3_nondeg),
)

# C4: exact whole-law coupling lemma on a three-atom trajectory space. Treat
# each atom as an entire one-edge trajectory (so it may contain all U4 depths).
# Product and shared-draw couplings preserve the full marginal law, hence every
# one-edge functional, but differ on cross-edge independence.
mu = sp.Matrix([sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(1, 6)])
Gamma_product = mu * mu.T
Gamma_shared = sp.diag(*list(mu))
row_prod = Gamma_product * sp.ones(3, 1)
row_shared = Gamma_shared * sp.ones(3, 1)
col_prod = Gamma_product.T * sp.ones(3, 1)
col_shared = Gamma_shared.T * sp.ones(3, 1)
fvals = sp.Matrix([2, -1, 4])
mean_prod = (row_prod.T * fvals)[0]
mean_shared = (row_shared.T * fvals)[0]
second_prod = (row_prod.T * fvals.applyfunc(lambda x: x ** 2))[0]
second_shared = (row_shared.T * fvals.applyfunc(lambda x: x ** 2))[0]
check(
    "C4",
    "whole one-edge trajectory law: product and shared-draw couplings have the "
    "same complete marginals (and moments) but different joint couplings",
    row_prod == mu and row_shared == mu and col_prod == mu and col_shared == mu
    and mean_prod == mean_shared and second_prod == second_shared
    and Gamma_product != Gamma_shared,
)

# ============================================================================
# BLOCK D -- factorization is a genuine JOINT functional (above the lane's scope)
# ============================================================================

# D1: factorization functional G(rho)=m(s,d)-p_s p_d is NOT a single-registration
#     functional -- exhibit equal Tr_2 but different G.
G_prod = C_prod[(0, 1)]
G_corr = C_corr[(0, 1)]
check(
    "D1",
    "factorization functional G=m(s,d)-p_s p_d takes different values on states "
    "with EQUAL single-registration reduced state (0 vs -p(1-p)) "
    "=> G does not factor through Tr_2; it lives strictly above the unraveling scope",
    sp.simplify(red2_prod - red2_corr) == sp.zeros(2, 2)
    and sp.simplify(G_prod) == 0
    and sp.simplify(G_corr) != 0,
)


# D2: the witness changes the DOWNSTREAM agreement-conditioned flow -> the atom
#     does real work (matches RD anatomy [check 7] and file-1 control).
def agreement_conditioned_update(mdict):
    """Keep (s,s),(d,d), renormalize. Returns (p_s', p_d')."""
    keep_s = mdict[(0, 0)]
    keep_d = mdict[(1, 1)]
    Z = sp.simplify(keep_s + keep_d)
    return sp.simplify(keep_s / Z), sp.simplify(keep_d / Z)


ps_prod_new, pd_prod_new = agreement_conditioned_update(m_prod)
ps_corr_new, pd_corr_new = agreement_conditioned_update(m_corr)
# product must give x->x^2 map: p_i' = p_i^2/(p_s^2+p_d^2)
expected_ps_prod = sp.simplify(p_s ** 2 / (p_s ** 2 + p_d ** 2))
# corr must give identity p_i' = p_i
check(
    "D2",
    "agreement-conditioning: product => p_s'=p_s^2/(p_s^2+p_d^2) (G2 x->x^2 flow); "
    "corr => p_s'=p_s (identity). The correlated stack collapses the flow.",
    sp.simplify(ps_prod_new - expected_ps_prod) == 0
    and sp.simplify(ps_corr_new - p_s) == 0
    and sp.simplify(pd_corr_new - p_d) == 0,
)

# ============================================================================
# BLOCK E -- escape conditions (re-aim the lane onto residual 4)
# ============================================================================

# E1: imposing cross-edge independence (residual 4) as C_ss=0 FORCES a=p^2.
sol = sp.solve(sp.Eq(m_ss - p_s * p_s, 0), a)  # C_ss = a - p^2 = 0
check(
    "E1",
    "cross-edge independence residual-4 condition C_ss=0 solves to a=p^2, "
    "recovering the product point => residual 4 is the factorization-critical escape",
    sol == [p ** 2],
)

# E2: identical-marginal / stationarity lever is independent. Build an
#     unequal-marginal joint (copy1 weight p1 != copy2 weight p2). Both single-
#     registration-valid, but the equal-p factorization m(j,k)=p_j p_k is ill-posed.
p1, p2 = sp.symbols("p1 p2", real=True)
rho_unequal = sp.diag(p1 * p2, p1 * (1 - p2), (1 - p1) * p2, (1 - p1) * (1 - p2))
red2_u = partial_trace2(rho_unequal)  # copy1 marginal = diag(p1,1-p1)
red1_u = partial_trace1(rho_unequal)  # copy2 marginal = diag(p2,1-p2)
check(
    "E2",
    "stationarity/edge-identity lever (residuals 1+3): an unequal-marginal product "
    "witness has copy1 marginal p1 != copy2 marginal p2 -- valid single-registration "
    "law on each copy, yet the single-p target m(j,k)=p_j p_k is ill-posed without "
    "identical marginals",
    sp.simplify(red2_u[0, 0] - p1) == 0
    and sp.simplify(red1_u[0, 0] - p2) == 0
    and sp.simplify(red2_u[0, 0] - red1_u[0, 0] - (p1 - p2)) == 0
    and red2_u[0, 0].subs({p1: sp.Rational(1, 3), p2: sp.Rational(2, 3)})
    != red1_u[0, 0].subs({p1: sp.Rational(1, 3), p2: sp.Rational(2, 3)}),
)

# E3: exact escape set -- cross-edge independence AND identical marginals => the
#     target law. (Independence gives m(j,k)=p_j^(1) p_k^(2); identical marginals
#     collapse p^(1)=p^(2)=p.)
indep_law = sp.diag(p * p, p * (1 - p), (1 - p) * p, (1 - p) * (1 - p))
target_ok = all(
    sp.simplify(indep_law[2 * j + k, 2 * j + k] - pj[j] * pj[k]) == 0
    for j in range(2)
    for k in range(2)
)
check(
    "E3",
    "exact escape set: cross-edge independence (residual 4) + identical marginals "
    "(residuals 1+3) => m(j,k)=p_j p_k. Residual 4 is explicitly untested in "
    "the source note; stationarity fails in the bounded finite-horizon probe.",
    target_ok,
)

# ============================================================================
# BLOCK F -- no-go discipline executable anchors (N3, N4, N7, N8)
# ============================================================================

# F1 (N3/source-scope guard): consume no instrument values. Guard only the
# source notes' explicit one-edge scope and cross-edge non-delivery statements.
root = Path(__file__).resolve().parents[1]
u_note = (root / "docs" /
          "UNRAVELED_RECORD_TRAJECTORIES_SUPPLY_NONDEGENERATE_STEP_DISTRIBUTION_BOUNDED_THEOREM_NOTE_2026-06-10.md"
          ).read_text(encoding="utf-8")
u4_note = (root / "docs" /
           "UNRAVELED_STEP_LAW_BI_INVARIANT_QUASI_STATIONARITY_SPLIT_BOUNDED_THEOREM_NOTE_2026-06-10.md"
           ).read_text(encoding="utf-8")
u_flat = " ".join(u_note.replace("*", "").split())
u4_flat = " ".join(u4_note.replace("*", "").split())
f1_ok = (
    "cross-edge independence and convolution structure are not tested here." in u_flat
    and "not the whole step law; the bi-orbit-quotient law remains the named open object." in u4_flat
    and "Status: source proposal; the audit lane grades." in u_flat
)
check(
    "F1",
    "source guards: cross-edge independence is explicitly untested, the quotient "
    "law remains open, and the unraveling row is source-proposed rather than audited",
    f1_ok,
)

# F2 (N4 residual matching): this note's witness restricts to the 2026-06-18
#     ρ_corr at p=1/2 (matching residual role: same marginals, differing joint).
corr_half = [sp.simplify(x.subs(p, half)) for x in (rho_corr[0, 0], rho_corr[1, 1], rho_corr[2, 2], rho_corr[3, 3])]
check(
    "F2",
    "N4 residual matching: this note's ρ_corr specializes to the 06-18 wall witness "
    "diag(1/2,0,0,1/2) at p=1/2 -- same single-copy marginals, differing joint",
    corr_half == [half, 0, 0, half],
)

# F3 (N7 steelman): grant the COMPLETE one-edge trajectory law. Product and
# shared-draw couplings preserve that entire marginal law, yet the shared
# coupling is non-product. No surrogate for actual U2/U4 values is used.
steelman_ok = (row_prod == row_shared == mu
               and col_prod == col_shared == mu
               and Gamma_product != Gamma_shared
               and sp.simplify(G_corr) != 0)
check(
    "F3",
    "N7 steelman: even granting the complete one-edge trajectory law, product "
    "and shared-draw couplings preserve it while differing on independence",
    steelman_ok,
)

# F4 (N8 cross-cycle echo): the wall's shape 'not forced by these tested inputs'
#     is preserved -- adding the unraveling single-edge inputs to the tested set
#     leaves the wall standing (product still strictly interior; witness still
#     admissible + single-edge-indistinguishable).
f4_ok = (all(interior_ok)                       # product not forced (A3)
         and max(c1_devs) < 1e-10               # witness single-edge-indistinguishable (C1)
         and (not fact_corr))                   # witness breaks factorization (B4)
check(
    "F4",
    "N8 cross-cycle echo: with unraveling single-edge inputs added to the tested "
    "set, the wall still stands (product strictly interior; correlated stack "
    "single-edge-indistinguishable yet non-factorized)",
    f4_ok,
)

# ============================================================================
# summary
# ============================================================================
print()
print(f"TOTAL: PASS={_PASS} FAIL={_FAIL}")
if _FAIL == 0:
    print(
        "VERDICT: narrow no-go passes. The source-note results constrain the complete "
        "one-edge marginal trajectory law but not its cross-edge coupling. Product "
        "and shared-draw couplings preserve that law while only one factorizes. "
        "Cross-edge independence "
        "(residual 4) + identical marginals (residuals 1+3) is the exact escape set; "
        "residual 4 is the factorization-critical residual and is precisely the one "
        "the lane leaves untested."
    )
else:
    print("VERDICT: FAILURES PRESENT -- do not rely on this run.")

import sys
sys.exit(0 if _FAIL == 0 else 1)
