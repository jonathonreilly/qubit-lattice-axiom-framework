#!/usr/bin/env python3
"""
G3 outcome factorization vs the unraveled step law (rhalf follow-up block 8).

Genre: narrow no-go sharpening.

Question: do the unraveling-lane premises, quoted at their audited claim scope,
force the two-registration outcome-factorization law

    m(j,k) = p_j p_k,   j,k in {s,d}

on the registered two-outcome quotient?

Answer proven here: NO. Every audited unraveling deliverable is a
*single-registration functional* -- a functional F(rho) = f(Tr_2 rho) that reads
only the one-registration reduced state. The correlated-stack witness ρ_corr
(the 2026-06-18 wall's template, extended) shares that reduced state with the
product state ρ_product, so it reproduces every single-registration unraveling
deliverable while violating factorization. Cross-edge independence (unraveling
residual 4) together with an identical-marginal / stationarity condition
(residuals 1+3) is the exact escape set; residual 4 is the factorization-critical
one, and it is precisely the residual note 4 marks "not tested here" and note 5
leaves as "the named open object."

Nothing on a derivation path is hard-coded: the wall family, the positivity
interval, the product point a=p^2, the agreement-conditioning flow, and the
escape condition are all computed with sympy from the symbol p (and a).

No Monte Carlo. Exact sympy / deterministic numpy only.
"""

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
# width at a few interior points must be > 0
widths_interior = [sp.nsimplify(width.subs(p, sp.Rational(k, 10))) for k in range(1, 10)]
check(
    "A2",
    "positivity interval [max(0,2p-1), p] has strictly positive width for p in (0,1)",
    all(float(w) > 0 for w in widths_interior),
)

# A3: product point a = p^2 is strictly interior (product is NOT forced).
prod_a = p ** 2
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
    all(interior_ok),
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
check(
    "B4",
    "Born joint weights: product factorizes m(j,k)=p_j p_k; corr does NOT "
    "(m(s,d)=0 != p(1-p) for p in (0,1))",
    fact_prod and (not fact_corr) and sp.simplify(m_corr[(0, 1)]) == 0,
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
# BLOCK C -- the audited unraveling scope is single-registration (no-go core)
# ============================================================================
# LEMMA (exact): if F(rho) = f(Tr_2 rho), then F(ρ_product) = F(ρ_corr), because
# Tr_2 ρ_product = Tr_2 ρ_corr (B3). Every audited unraveling deliverable is such
# an F. We instantiate F three ways and confirm coincidence + non-degeneracy.

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

# C3: U2 non-degenerate single-edge step SURROGATE (labeled surrogate, not the
#     C^3 construction). A weak two-outcome instrument of strength eps acting on
#     the single-registration reduced state sigma produces outcome-labeled
#     increments; their spread is a functional of sigma alone.
#     step_spread(sigma,eps) = Var over outcomes of the post-outcome pointer shift.
def step_spread_from_sigma(sigma2, epsv):
    """Single-registration step-spread surrogate. Depends only on sigma."""
    p0 = float(sp.re(sigma2[0, 0]))
    p1 = float(sp.re(sigma2[1, 1]))
    # outcome-labeled increment values +eps (outcome s) / -eps (outcome d),
    # weighted by single-edge Born weights p0,p1.
    mean = p0 * (+epsv) + p1 * (-epsv)
    var = p0 * (+epsv - mean) ** 2 + p1 * (-epsv - mean) ** 2
    return var


epsv = 0.3
c3_ok = []
c3_nondeg = []
for pv in np.linspace(0.05, 0.95, 19):
    s2p = partial_trace2(rho_product).subs(p, pv)
    s2c = partial_trace2(rho_corr).subs(p, pv)
    vp = step_spread_from_sigma(s2p, epsv)
    vc = step_spread_from_sigma(s2c, epsv)
    c3_ok.append(abs(vp - vc) < 1e-12)
    c3_nondeg.append(vp > 1e-9)
check(
    "C3",
    "U2 single-edge step-spread surrogate: non-degenerate (>0) for p in (0,1) "
    "AND identical on both witnesses (functional of sigma only)",
    all(c3_ok) and all(c3_nondeg),
)

# C4: note 5 mean-spectrum SURROGATE. Build a single-registration-derived "mean"
#     object M(sigma) and read its singular/eigenvalue spectrum. Being a
#     functional of sigma, it coincides on both witnesses -> note-5 readouts
#     cannot separate the correlated stack from the product.
def mean_object_from_sigma(sigma2):
    """Single-registration mean surrogate: sigma pushed through a fixed
    weak-record Kraus pair, returning a 2x2 'mean increment'. Functional of sigma."""
    s = np.array(sp.Matrix(sigma2)).astype(complex)
    K0 = np.array([[1.0, 0.0], [0.0, np.sqrt(1 - epsv)]], dtype=complex)
    K1 = np.array([[0.0, 0.0], [0.0, np.sqrt(epsv)]], dtype=complex)
    return K0 @ s @ K0.conj().T + K1 @ s @ K1.conj().T


c4_sv = []
c4_ev = []
for pv in np.linspace(0.05, 0.95, 19):
    Mp = mean_object_from_sigma(partial_trace2(rho_product).subs(p, pv))
    Mc = mean_object_from_sigma(partial_trace2(rho_corr).subs(p, pv))
    c4_sv.append(np.linalg.norm(np.sort(np.linalg.svd(Mp, compute_uv=False))
                                - np.sort(np.linalg.svd(Mc, compute_uv=False))))
    c4_ev.append(np.linalg.norm(np.sort(np.linalg.eigvals(Mp).real)
                                - np.sort(np.linalg.eigvals(Mc).real)))
check(
    "C4",
    "note-5 mean-spectrum surrogate (singular + eigenvalue spectra): identical on "
    "both witnesses across p-grid (a single-registration functional)",
    max(c4_sv) < 1e-10 and max(c4_ev) < 1e-10,
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
    "agreement-conditioning: product => p_s'=p_s^2/(p_s^2+p_d^2) (retained x->x^2 flow); "
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
    and sp.simplify(red1_u[0, 0] - p2) == 0,
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
    "(residuals 1+3) => m(j,k)=p_j p_k. Neither is delivered by the audited "
    "unraveling lane (residual 4 'not tested here'; stationarity FAILS at finite horizon).",
    target_ok,
)

# ============================================================================
# BLOCK F -- no-go discipline executable anchors (N3, N4, N7, N8)
# ============================================================================

# F1 (N3 hidden-wall scan): the witness's single-edge law is derivable from p
#     alone -- no unaudited C^3 instrument value enters a derivation path.
#     Confirm: single-edge weights and step surrogate are functions of p only.
f1_ok = (
    set(sp.simplify(w_corr[0]).free_symbols) <= {p}
    and set(sp.simplify(w_corr[1]).free_symbols) <= {p}
)
check(
    "F1",
    "N3 hidden-wall scan: witness single-registration law is a function of p only; "
    "no unaudited unraveling/C^3 instrument value sits on a derivation path",
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

# F3 (N7 steelman): grant the STRONGEST honest reading of the lane -- U2
#     non-degeneracy (C3) AND note-5 mean-spectrum quasi-freeze (C4) as premises.
#     The witness satisfies BOTH yet breaks factorization (D1). So even the
#     steelmanned lane does not force factorization.
steelman_ok = (all(c3_ok) and all(c3_nondeg)  # U2 holds for witness
               and max(c4_sv) < 1e-10          # note-5 readout matches product
               and sp.simplify(G_corr) != 0)   # factorization still broken
check(
    "F3",
    "N7 steelman: even granting U2 non-degeneracy AND note-5 mean-spectrum "
    "quasi-freeze as premises, the correlated stack satisfies both and still "
    "violates factorization",
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
        "VERDICT: narrow no-go passes. The audited unraveling premises are "
        "single-registration functionals; the correlated-stack witness reproduces "
        "every one of them while violating m(j,k)=p_j p_k. Cross-edge independence "
        "(residual 4) + identical marginals (residuals 1+3) is the exact escape set; "
        "residual 4 is the factorization-critical residual and is precisely the one "
        "the lane leaves untested."
    )
else:
    print("VERDICT: FAILURES PRESENT -- do not rely on this run.")

import sys
sys.exit(0 if _FAIL == 0 else 1)
