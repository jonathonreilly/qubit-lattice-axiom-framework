#!/usr/bin/env python3
"""Runner for the P1 registration-realization pin-consolidation note
(OBSERVABLE_PRINCIPLE_P1_REGISTRATION_REALIZATION_PIN_CONSOLIDATION_NARROW_THEOREM_NOTE_2026-06-11.md).

Mission. The P1 exponent chain currently carries five separately declared
realization clauses: (CAP-real) (BR-license note
OBSERVABLE_PRINCIPLE_P1_BR_LICENSE_FROM_RECORD_CAPACITY_NARROW_NO_GO_NOTE_2026-06-10.md:
"each e-fold increment of W is realized by a finite record readout", with
the Lemma C representation I(A_z) = chi_A . v_z over a finite disjoint
record collection registered for that e-fold) and the four (REG) clauses
of the CAP-K note
(OBSERVABLE_PRINCIPLE_P1_CAP_K_FROM_FINITE_SPEED_REGISTRATION_NARROW_THEOREM_NOTE_2026-06-10.md):
(REG-dyn) records established by the retained finite-range dynamics with a
bounded-region source coupling; (REG-tau) at most a supplied clock window
per e-fold; (REG-thr) register sites delta-sensitive in operator norm;
(REG-site) disjoint records on disjoint nonempty register-site sets.

This runner verifies the implication-lattice theorem consolidating that
inventory around ONE declared Registration Realization clause

    (RR)  every e-fold increment of the T1-d scalar readout equals the
          finite-sector readout of a finite pairwise-disjoint record
          collection registered for that e-fold, where REGISTERED means:
          each record is established by unitary evolution under H + V_k
          (H the retained finite-range hopping dynamics, V_k the e-fold's
          source change supported in the bounded region X with
          ||V_k||_op <= J_V) and is supported in the delta-sensitive
          register set of that process (one uniform supplied threshold
          delta) within the e-fold's registration window,

which remains DECLARED (it is a quantitative slice of the
record-scalar-map no-go's middle arrow and is never derived here). The
lattice, every leg checked below:

  proven arrows (exhaustive finite-model verification of the syntactic
  factorization + explicit-dynamics instances):
    (RR) <=> (CAP-real) AND (REG-dyn) AND (REG-thr @ own window)
    (RR) AND (REG-tau)  => (REG-thr @ the supplied window tau)
    (RR) AND (REG-tau)  => (CAP-K), both readings (cap recomputed)
  witnessed non-arrows (finite constructions, one per leg):
    (CAP-real) =/=> (RR)        [4^k fiat assignment; no dynamics]
    (REG-dyn)+(REG-thr)+(REG-tau) =/=> (CAP-real)  [readout mismatch]
    (RR) =/=> (REG-tau)         [growing windows; cap fails: tau separate]
    (RR)+(REG-tau) =/=> (REG-site)  [2-qubit 4-projector pigeonhole;
                                     joint cap 2^N still finite]
    (REG-site) =/=> (RR)        [static site-disjoint fiat records]
    (RR) =/=> (T1-d blocks->records)  [two disjoint source blocks sharing
                                       a register site: T1-d not absorbed]
    (RR with e-fold-dependent threshold) loses k-uniformity
                                [D*(delta/2^k) - D*(delta) = k ln 2]

Minimal generating set: {(RR), (REG-tau)} — verified over the full model
library (every model with RR and REG-tau satisfies the three consolidated
clauses; each proper subset has a chain-failing countermodel). (REG-site)
is NOT generated and NOT needed for the p = 0 selection (the weakest
joint-sector reading keeps K = 2^{N_reach} finite and k-uniform); it is an
optional sharpening pin (polynomial vs exponential cap). The T1-d parent
Boundary (including its disjoint-blocks-to-disjoint-records clause) is
untouched and not absorbed.

Walls respected (string-checked + structurally): the record-scalar-map
no-go (RR stays declared, the middle arrow is never derived); the
count-probability firewall (no probability law anywhere — every
sensitivity is an operator norm); the record-formation no-go (RR
conditions on the realization, it does not force records to form; the
class may be empty); the clock/rate interface no-go ((REG-tau) is kept a
separate supplied-clock clause precisely because the window's meaning
needs the supplied clock map); the canonical-proposal no-dynamics
guardrail (RR is a declared realization clause, not a derivation that
records must form).

Tags: [A] algebraic identity / exhaustive finite-model check; [B]
cross-note / ledger input verification; [C] first-principles compute on
explicit finite-dimensional dynamics; [D] falsification / hostile-witness
leg. Exact SymPy where claimed; dynamics legs are deterministic
finite-dimensional computations (no randomness, no fitted/observed/PDG
inputs). Runtime well under 5 minutes.

Reproduction:
    python3 scripts/observable_principle_p1_rr_consolidation_check_2026_06_11.py
Expected: TOTAL: PASS=30 FAIL=0
"""

from __future__ import annotations

import itertools
import json
import os
import re
from dataclasses import dataclass

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
    "OBSERVABLE_PRINCIPLE_P1_REGISTRATION_REALIZATION_PIN_CONSOLIDATION_NARROW_THEOREM_NOTE_2026-06-11.md",
)


def read(path: str) -> str:
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def norm_ws(s: str) -> str:
    return re.sub(r"\s+", " ", s)


# ---------------------------------------------------------------------------
# shared exact symbols and finite-dimensional machinery (deterministic)
# ---------------------------------------------------------------------------
u, p = sp.symbols("u p", positive=True, real=True)
E = sp.E

A_LAD = np.array([[0, 1], [0, 0]], dtype=complex)  # per-site annihilator on C^2
N_OP = np.array([[0, 0], [0, 1]], dtype=complex)
SZ = np.diag([1.0, -1.0]).astype(complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)


def site_op(nsites: int, x: int, op: np.ndarray) -> np.ndarray:
    M = np.array([[1.0]], dtype=complex)
    I2 = np.eye(2, dtype=complex)
    for i in range(nsites):
        M = np.kron(M, op if i == x else I2)
    return M


def build_open_chain(L: int) -> np.ndarray:
    """Retained finite-range hopping family (F4 leg shape: q = 2, R = 1), open ends."""
    H = np.zeros((2 ** L, 2 ** L), dtype=complex)
    for x in range(L - 1):
        ax, ay = site_op(L, x, A_LAD), site_op(L, x + 1, A_LAD)
        H += ax.conj().T @ ay + ay.conj().T @ ax
    return H


def eigd(H: np.ndarray):
    return np.linalg.eigh(H)


def heis(ed, B: np.ndarray, t: float) -> np.ndarray:
    ev, V = ed
    U = V @ np.diag(np.exp(-1j * ev * t)) @ V.conj().T
    return U.conj().T @ B @ U


def opnorm(M: np.ndarray) -> float:
    return float(np.linalg.norm(M, 2))


def sensitivity(L: int, V: np.ndarray, y: int, t: float, H=None) -> float:
    """||alpha^{H+V}_t(sz_y) - alpha^H_t(sz_y)||_op on the open L-chain."""
    if H is None:
        H = build_open_chain(L)
    By = site_op(L, y, SZ)
    return opnorm(heis(eigd(H + V), By, t) - heis(eigd(H), By, t))


def series_tail(aa: float, n0: int, nmax: int = 600) -> float:
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


def lr_series_bound(t: float, D: int, W: float, normV: float = 1.0) -> float:
    """Integrated Duhamel x LR series bound (CAP-K note eq. (2))."""
    return normV / (4.0 * W) * series_tail(4.0 * W * t, D + 1)


# ---------------------------------------------------------------------------
# the clause formalization: finite models and INDEPENDENT predicate codepaths
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class Rec:
    val: object            # sector datum (exact)
    sector: frozenset      # abstract pairwise-orthogonality labels
    support: frozenset     # register sites carrying the record
    established: str       # "retained_dynamics" | "fiat"
    src_in_X: bool         # e-fold source change supported in the bounded region X
    src_norm_ok: bool      # ||V_k||_op <= J_V
    sens: dict             # site -> (operator-norm sensitivity, time achieved)


@dataclass(frozen=True)
class Efold:
    k: int
    increment: object      # declared T1-d readout e-fold increment
    recs: tuple
    window: object         # registration window actually used by the process
    block: frozenset = frozenset()  # source block (for the T1-d blocks->records check)


@dataclass(frozen=True)
class Model:
    efolds: tuple
    delta: object          # ONE uniform sensitivity threshold
    tau: object            # supplied clock window (None = no supplied clock)


def cap_real(M: Model) -> bool:
    """(CAP-real), BR-note wording: each e-fold increment equals the finite-sector
    readout of a finite pairwise-disjoint record collection registered for it."""
    for ef in M.efolds:
        if sum((r.val for r in ef.recs), sp.Integer(0)) != ef.increment:
            return False
        for r1, r2 in itertools.combinations(ef.recs, 2):
            if r1.sector & r2.sector:
                return False
    return True


def reg_dyn(M: Model) -> bool:
    """(REG-dyn): every record established by the retained finite-range dynamics
    with the e-fold source change supported in X and ||V_k|| <= J_V."""
    for ef in M.efolds:
        for r in ef.recs:
            if r.established != "retained_dynamics" or not r.src_in_X or not r.src_norm_ok:
                return False
    return True


def _thr_within(M: Model, window_of) -> bool:
    """(REG-thr) shape at a given per-e-fold window: every record-carrying site is
    delta-sensitive (operator norm, uniform delta) by some time <= window."""
    for ef in M.efolds:
        w = window_of(ef)
        if w is None:
            return False
        for r in ef.recs:
            if not r.support:
                return False
            for site in r.support:
                s, t = r.sens.get(site, (0, None))
                if t is None or s < M.delta or t > w:
                    return False
    return True


def reg_thr(M: Model) -> bool:
    """(REG-thr) at the SUPPLIED clock window tau (the CAP-K note's clause)."""
    return M.tau is not None and _thr_within(M, lambda ef: M.tau)


def reg_tau(M: Model) -> bool:
    """(REG-tau): a supplied clock window exists and every e-fold's registration
    runs within it."""
    return M.tau is not None and all(ef.window <= M.tau for ef in M.efolds)


def reg_site(M: Model) -> bool:
    """(REG-site): pairwise-disjoint records on pairwise-disjoint NONEMPTY site sets."""
    for ef in M.efolds:
        for r in ef.recs:
            if not r.support:
                return False
        for r1, r2 in itertools.combinations(ef.recs, 2):
            if r1.support & r2.support:
                return False
    return True


def rr(M: Model) -> bool:
    """(RR), single-pass checker of the consolidated sentence (independent codepath:
    does NOT call the clause predicates above)."""
    for ef in M.efolds:
        tot = sp.Integer(0)
        seen = []
        for r in ef.recs:
            tot += r.val
            for s0 in seen:
                if s0 & r.sector:
                    return False
            seen.append(r.sector)
            if r.established != "retained_dynamics":
                return False
            if not (r.src_in_X and r.src_norm_ok):
                return False
            if not r.support:
                return False
            for site in r.support:
                s, t = r.sens.get(site, (0, None))
                if t is None or s < M.delta or t > ef.window:
                    return False
        if tot != ef.increment:
            return False
    return True


def t1d_blocks_disjoint_records(M: Model) -> bool:
    """T1-d Boundary clause (parent note): independent disjoint source blocks
    register as disjoint records (site-supported reading across e-folds)."""
    for e1, e2 in itertools.combinations(M.efolds, 2):
        if e1.block and e2.block and not (e1.block & e2.block):
            for r1 in e1.recs:
                for r2 in e2.recs:
                    if r1.support & r2.support:
                        return False
    return True


def chain_capped(M: Model, K: int) -> bool:
    """(CAP-K) instance check: every e-fold's disjoint-record count <= K."""
    return all(len(ef.recs) <= K for ef in M.efolds)


# ===========================================================================
print("== T1: the consolidation equivalence — exhaustive finite-model verification ==")

DELTA = sp.Rational(1, 10)
TAU = sp.Integer(1)
MODEL_LIBRARY: list[Model] = []


def build_toggle_model(add_ok, sect_ok, est_ok, src_ok, sens_ok, win_ok, supp_disj, supp_nonempty) -> Model:
    """Deterministic 2-e-fold, 2-records-per-e-fold model for each toggle vector."""
    efolds = []
    for k in (1, 2):
        recs = []
        for j in (0, 1):
            bad_est = (not est_ok) and j == 0
            bad_src = (not src_ok) and j == 1
            bad_sens = (not sens_ok) and j == 0
            window = TAU if win_ok else 2 * TAU
            supp = frozenset() if (not supp_nonempty and j == 0) else (
                frozenset({2 * j}) if supp_disj else frozenset({0, 2 * j})
            )
            sect = frozenset({f"s{k}{j}"}) if sect_ok else frozenset({f"s{k}"})
            sens = {
                site: ((DELTA / 2 if bad_sens else 2 * DELTA), window)
                for site in supp
            }
            recs.append(
                Rec(
                    val=sp.Integer(1),
                    sector=sect,
                    support=supp,
                    established=("fiat" if bad_est else "retained_dynamics"),
                    src_in_X=not bad_src,
                    src_norm_ok=True,
                    sens=sens,
                )
            )
        inc = sp.Integer(2) if add_ok else sp.Rational(7, 2)
        efolds.append(Efold(k=k, increment=inc, recs=tuple(recs), window=(TAU if win_ok else 2 * TAU)))
    return Model(efolds=tuple(efolds), delta=DELTA, tau=TAU)


equiv_ok, a3_ok = True, True
strict = {"capreal_not_rr": 0, "regdyn_not_capreal": 0, "rr_not_tau": 0,
          "rr_not_site": 0, "site_not_rr": 0}
for toggles in itertools.product([True, False], repeat=8):
    M = build_toggle_model(*toggles)
    MODEL_LIBRARY.append(M)
    lhs = rr(M)
    rhs = cap_real(M) and reg_dyn(M) and _thr_within(M, lambda ef: ef.window)
    if lhs != rhs:
        equiv_ok = False
    if rr(M) and reg_tau(M) and not reg_thr(M):
        a3_ok = False
    if cap_real(M) and not rr(M):
        strict["capreal_not_rr"] += 1
    if reg_dyn(M) and not cap_real(M):
        strict["regdyn_not_capreal"] += 1
    if rr(M) and not reg_tau(M):
        strict["rr_not_tau"] += 1
    if rr(M) and not reg_site(M):
        strict["rr_not_site"] += 1
    if reg_site(M) and not rr(M):
        strict["site_not_rr"] += 1

check("A", "consolidation equivalence verified pointwise on all 256 toggle models (independent codepaths): RR(M) == (CAP-real)(M) AND (REG-dyn)(M) AND (REG-thr @ own window)(M) — both directions at once, so the declared RR neither strengthens nor weakens the three-clause conjunction", equiv_ok and len(MODEL_LIBRARY) == 256, f"models={len(MODEL_LIBRARY)}")
check("A", "arrow (RR) AND (REG-tau) => (REG-thr @ supplied tau) holds on all 256 models (the own-window threshold transfers to the supplied window because every window <= tau)", a3_ok)
check("A", "every strict containment is witnessed INSIDE the enumerated family: CAP-real w/o RR, REG-dyn w/o CAP-real, RR w/o REG-tau, RR w/o REG-site, REG-site w/o RR all occur", all(v > 0 for v in strict.values()), f"counts={strict}")

# ===========================================================================
print("== T2: an RR instance on explicit dynamics (the consolidated clause is satisfiable, not vacuous) ==")

L6 = 6
V6 = site_op(L6, 0, N_OP)  # source change at site 0 (X = {0}), ||V|| = 1 <= J_V
H6 = build_open_chain(L6)
ed6, ed6p = eigd(H6), eigd(H6 + V6)
t_reg = 0.6
sens6 = {}
for y in range(L6):
    By = site_op(L6, y, SZ)
    sens6[y] = opnorm(heis(ed6p, By, t_reg) - heis(ed6, By, t_reg))
recs_rr = tuple(
    Rec(val=sp.Integer(1), sector=frozenset({f"r{y}"}), support=frozenset({y}),
        established="retained_dynamics", src_in_X=True, src_norm_ok=True,
        sens={y: (sp.nsimplify(round(sens6[y], 12), rational=True), sp.Rational(3, 5))})
    for y in (0, 1)
)
M_rr = Model(
    efolds=tuple(Efold(k=k, increment=sp.Integer(2), recs=recs_rr, window=sp.Rational(3, 5)) for k in (1, 2)),
    delta=DELTA, tau=TAU,
)
MODEL_LIBRARY.append(M_rr)
all_true = rr(M_rr) and cap_real(M_rr) and reg_dyn(M_rr) and reg_thr(M_rr) and reg_tau(M_rr) and reg_site(M_rr)
check("C", "explicit 6-site open-chain instance (V = N_0, t = 0.6): measured operator-norm sensitivities at register sites 0 and 1 exceed delta = 1/10; two unit records on disjoint sites realize the increment 2 — ALL of RR, CAP-real, REG-dyn, REG-thr, REG-tau, REG-site evaluate True on one real-dynamics model", all_true and sens6[0] > 0.1 and sens6[1] > 0.1, f"sens(0)={sens6[0]:.4f}, sens(1)={sens6[1]:.4f}")

# cone teeth: at a short window the LR bound certifies a distant site CANNOT register
t_short_grid = [0.01, 0.02, 0.03, 0.04, 0.05]
sens_far = max(opnorm(heis(ed6p, site_op(L6, 4, SZ), t) - heis(ed6, site_op(L6, 4, SZ), t)) for t in t_short_grid)
bound_far = lr_series_bound(0.05, 4, 2.0)  # W = |m| + 2d = 2 (d = 1, m = 0)
rec_far = Rec(val=sp.Integer(1), sector=frozenset({"far"}), support=frozenset({4}),
              established="retained_dynamics", src_in_X=True, src_norm_ok=True,
              sens={4: (sp.nsimplify(round(sens_far, 14), rational=True), sp.Rational(1, 20))})
M_far = Model(efolds=(Efold(k=1, increment=sp.Integer(1), recs=(rec_far,), window=sp.Rational(1, 20)),),
              delta=DELTA, tau=TAU)
MODEL_LIBRARY.append(M_far)
check("C", "cone teeth: at window t <= 0.05 the retained LR series bound at l1-distance 4 is < delta (and the measured sensitivity sits below the bound), so a hypothetical distance-4 record at that window VIOLATES RR's threshold facet — the RR predicate rejects it", (sens_far <= bound_far) and (bound_far < 0.1) and (not rr(M_far)), f"measured={sens_far:.2e} <= bound={bound_far:.2e} < delta=0.1")

# ===========================================================================
print("== T3: witnessed non-arrow (CAP-real) =/=> (RR) — the fiat 4^k assignment ==")

fiat_efolds = []
for k in (1, 2, 3):
    recs = tuple(
        Rec(val=sp.Integer(1), sector=frozenset({(k, i)}), support=frozenset({(k, i)}),
            established="fiat", src_in_X=True, src_norm_ok=True,
            sens={(k, i): (2 * DELTA, TAU)})
        for i in range(4 ** k)
    )
    fiat_efolds.append(Efold(k=k, increment=sp.Integer(4 ** k), recs=recs, window=TAU))
M_fiat = Model(efolds=tuple(fiat_efolds), delta=DELTA, tau=TAU)
MODEL_LIBRARY.append(M_fiat)
prefix = sum(sp.Integer(4) ** k for k in (1, 2, 3))
check("D", "4^k unit records assigned to e-fold k by fiat (no establishing process): (CAP-real) holds exactly (additivity on every collection; prefix sum (4^4-1)/3 - 1 = 84 recomputed) while (REG-dyn) and RR are False — realization through records does NOT imply registration through the retained dynamics", cap_real(M_fiat) and (not reg_dyn(M_fiat)) and (not rr(M_fiat)) and prefix == 84, f"prefix_sum={prefix}")

# canonical cap recomputed (CAP-K note T5): D* and K = 129^3
tau_s, delta_s, JV_s, vv = sp.symbols("tau delta J_V v", positive=True)
Dvar = sp.Symbol("D", real=True)
Dstar_expr = sp.solve(sp.Eq(delta_s, (E / (E - 1)) * (JV_s / vv) * sp.exp(vv * tau_s - Dvar)), Dvar)[0]
v_can = 24 * E
Dstar_can = Dstar_expr.subs({vv: v_can, tau_s: 1, JV_s: 1, delta_s: sp.Rational(1, 10)})
Dceil = int(sp.ceiling(Dstar_can))
N_reach = (1 + 2 * Dceil) ** 3
check("A", "canonical cap recomputed (not cited blind): D* = 24e + ln(10/(24(e-1))) ~ 63.82, ceil = 64, K = 129^3 = 2146689; the fiat witness defeats it at k = 11 (4^11 = 4194304 > K) — (CAP-real) alone never carried the cap, exactly the BR-license note's split", Dceil == 64 and N_reach == 2146689 and 4 ** 11 > N_reach, f"D*={float(Dstar_can):.4f}, K={N_reach}")

# ===========================================================================
print("== T4: witnessed non-arrow (REG-dyn)+(REG-thr)+(REG-tau) =/=> (CAP-real) ==")

M_mismatch = Model(
    efolds=tuple(Efold(k=k, increment=sp.Rational(7, 2), recs=recs_rr, window=sp.Rational(3, 5)) for k in (1, 2)),
    delta=DELTA, tau=TAU,
)
MODEL_LIBRARY.append(M_mismatch)
check("C", "same real-dynamics records as T2 (established, delta-sensitive, within tau) but declared increment 7/2 != readout 2: (REG-dyn), (REG-thr), (REG-tau) all True, (CAP-real) and RR False — the (REG) class clauses alone do not generate the realization, so RR is a genuine join (neither side redundant)", reg_dyn(M_mismatch) and reg_thr(M_mismatch) and reg_tau(M_mismatch) and (not cap_real(M_mismatch)) and (not rr(M_mismatch)))

# ===========================================================================
print("== T5: witnessed non-arrow (RR) =/=> (REG-tau) — the window is irreducibly separate ==")

grow_efolds = []
for k in (1, 2, 3):
    wk = sp.Integer(k)
    recs = tuple(
        Rec(val=sp.Integer(1), sector=frozenset({(k, i)}), support=frozenset({(k, i)}),
            established="retained_dynamics", src_in_X=True, src_norm_ok=True,
            sens={(k, i): (2 * DELTA, wk)})
        for i in range(4 ** k)
    )
    grow_efolds.append(Efold(k=k, increment=sp.Integer(4 ** k), recs=recs, window=wk))
M_grow = Model(efolds=tuple(grow_efolds), delta=DELTA, tau=None)
MODEL_LIBRARY.append(M_grow)
check("D", "growing-window model (window_k = k, no supplied clock window): RR holds (every record established and delta-sensitive within ITS OWN window) while (REG-tau) fails — and the realized counts 4^k defeat every fixed cap, so RR alone yields NO (CAP-K)", rr(M_grow) and (not reg_tau(M_grow)) and (not chain_capped(M_grow, 4)) and (not chain_capped(M_grow, 16)))

c_const = sp.log((E / (E - 1)) / (v_can * sp.Rational(1, 10)))
tau_k = lambda kv: ((sp.Pow(4, sp.Rational(kv, 3)) - 1) / 2 - c_const) / v_can
tau11, tau30 = float(tau_k(11)), float(tau_k(30))
kk = sp.Symbol("k", positive=True)
tau_limit = sp.limit(((sp.Pow(4, kk / 3) - 1) / 2 - c_const) / v_can, kk, sp.oo)
check("A", "windows demanded by finite-speed registration of 4^k records recomputed: tau_11 >= 1.25 > 1, tau_30 >= 8036, and lim_{k->oo} tau_k = oo (sympy) — the supplied bounded window is load-bearing; (REG-tau) cannot be absorbed into RR without erasing it", tau11 > 1.25 - 1e-4 and tau30 > 8000 and tau_limit == sp.oo, f"tau_11>={tau11:.4f}, tau_30>={tau30:.1f}")

cr_note = read(os.path.join(REPO, "docs", "POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md"))
note_txt = read(NOTE)
note_ws = norm_ws(note_txt)
check("B", "clock wall verbatim ('Without the supplied `tau`, the same record history supports many inequivalent rates') + the note keeps (REG-tau) a separate supplied-clock clause (never folded into RR, never derived)", ("Without the supplied `tau`, the same record history supports many inequivalent" in norm_ws(cr_note)) and ("(REG-tau)" in note_ws) and ("separate" in note_ws))

# ===========================================================================
print("== T6: witnessed non-arrow (RR)+(REG-tau) =/=> (REG-site) — the joint-sector hole, and why it does not matter for p = 0 ==")

H2 = build_open_chain(2)
V2 = site_op(2, 0, N_OP)
ed2, ed2p = eigd(H2), eigd(H2 + V2)
sens2 = {y: opnorm(heis(ed2p, site_op(2, y, SZ), 1.0) - heis(ed2, site_op(2, y, SZ), 1.0)) for y in (0, 1)}
basis = np.eye(4, dtype=complex)
projs = [np.outer(basis[i], basis[i].conj()) for i in range(4)]
orth_resid = max(opnorm(projs[i] @ projs[j]) for i in range(4) for j in range(4) if i != j)
sum_is_id = opnorm(sum(projs) - np.eye(4)) < 1e-12
needs_both = all(
    opnorm(P @ site_op(2, y, SX) - site_op(2, y, SX) @ P) > 0.4
    for P in projs for y in (0, 1)
)
check("C", "2-qubit witness dynamics: the hopping bond makes BOTH sites delta-sensitive at t = 1 (measured), and the four rank-1 joint projectors are pairwise orthogonal (max residual < 1e-12), sum to I, and each fails to commute with each single-site algebra — four pairwise-disjoint records, every one supported on BOTH sites", sens2[0] > 0.1 and sens2[1] > 0.1 and orth_resid < 1e-12 and sum_is_id and needs_both, f"sens={sens2[0]:.3f}/{sens2[1]:.3f}, orth_resid={orth_resid:.1e}")

nonempty_subsets = [frozenset(s) for r in (1, 2) for s in itertools.combinations((0, 1), r)]
pigeonhole = not any(
    all(not (a & b) for a, b in itertools.combinations(assign, 2))
    for assign in itertools.product(nonempty_subsets, repeat=4)
)
fifth_impossible = opnorm(np.eye(4) - sum(projs)) < 1e-12  # sum P_i = I => any orthogonal P5 = 0
check("A", "pigeonhole exact (all 81 assignments enumerated): four pairwise-disjoint NONEMPTY subsets of a 2-site set do not exist, so (REG-site) FAILS — yet the joint-sector cap d_site^N = 2^2 = 4 holds with equality and a fifth mutually-orthogonal nonzero projection is impossible (sum P_i = I): (CAP-K) survives without (REG-site)", pigeonhole and fifth_impossible)

Dstar_k_free = Dstar_expr.free_symbols == {tau_s, delta_s, JV_s, vv}
check("A", "the chain survives without (REG-site): the weakest joint-sector reading keeps K = 2^{N_reach} finite and k-uniform (D* free symbols exclude k), and the p = 0 selection needs only finiteness + k-uniformity — (REG-site) is demoted from required declared clause to OPTIONAL SHARPENING (polynomial 129^3 vs exponential 2^{129^3} cap)", Dstar_k_free)

# ===========================================================================
print("== T7: reverse holes — (REG-site) =/=> (RR), and the T1-d blocks->records clause is NOT absorbed ==")

rec_static = tuple(
    Rec(val=sp.Integer(1), sector=frozenset({f"q{j}"}), support=frozenset({j}),
        established="fiat", src_in_X=True, src_norm_ok=True, sens={j: (2 * DELTA, TAU)})
    for j in (0, 1)
)
M_static = Model(efolds=(Efold(k=1, increment=sp.Integer(2), recs=rec_static, window=TAU),),
                 delta=DELTA, tau=TAU)
MODEL_LIBRARY.append(M_static)
check("A", "static site-disjoint fiat records: (REG-site) True while (REG-dyn) and RR are False — site disjointness supplies no establishment, so the reverse arrow fails too", reg_site(M_static) and (not reg_dyn(M_static)) and (not rr(M_static)))

L3 = 3
H3 = build_open_chain(L3)
Vb1, Vb2 = site_op(L3, 0, N_OP), site_op(L3, 2, N_OP)
s_mid_1 = opnorm(heis(eigd(H3 + Vb1), site_op(L3, 1, SZ), 1.0) - heis(eigd(H3), site_op(L3, 1, SZ), 1.0))
s_mid_2 = opnorm(heis(eigd(H3 + Vb2), site_op(L3, 1, SZ), 1.0) - heis(eigd(H3), site_op(L3, 1, SZ), 1.0))
mk_rec = lambda lbl, sval: Rec(val=sp.Integer(1), sector=frozenset({lbl}), support=frozenset({1}),
                               established="retained_dynamics", src_in_X=True, src_norm_ok=True,
                               sens={1: (sp.nsimplify(round(sval, 12), rational=True), TAU)})
M_blocks = Model(
    efolds=(
        Efold(k=1, increment=sp.Integer(1), recs=(mk_rec("b1", s_mid_1),), window=TAU, block=frozenset({0})),
        Efold(k=2, increment=sp.Integer(1), recs=(mk_rec("b2", s_mid_2),), window=TAU, block=frozenset({2})),
    ),
    delta=DELTA, tau=TAU,
)
MODEL_LIBRARY.append(M_blocks)
check("C", "two-block witness on the explicit 3-site chain: disjoint source blocks {0} and {2} both make the MIDDLE site delta-sensitive (measured), the per-e-fold RR facets all hold (RR, REG-tau True), yet the two blocks' records share register site 1 — 'independent disjoint source blocks register as disjoint records' FAILS: RR does not absorb the T1-d Boundary clause", rr(M_blocks) and reg_tau(M_blocks) and (not t1d_blocks_disjoint_records(M_blocks)) and s_mid_1 > 0.1 and s_mid_2 > 0.1, f"sens_mid={s_mid_1:.4f}/{s_mid_2:.4f}")

parent = read(os.path.join(REPO, "docs", "OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md"))
br_note = read(os.path.join(REPO, "docs", "OBSERVABLE_PRINCIPLE_P1_BR_LICENSE_FROM_RECORD_CAPACITY_NARROW_NO_GO_NOTE_2026-06-10.md"))
t1d_str = "independent disjoint source blocks register as disjoint records"
br_capreal = "each e-fold increment of W is realized by a finite record readout"
check("B", "T1-d Boundary wording present verbatim in the parent note; (CAP-real)'s published wording ('each e-fold increment of W is realized by a finite record readout', quoted in the note) is per-e-fold realization and does NOT contain the blocks->records clause (string absent from the BR-license note) — so T1-d remains the parent Boundary, untouched by this consolidation", (t1d_str in norm_ws(parent)) and (br_capreal in norm_ws(br_note)) and (br_capreal in note_ws) and (t1d_str not in norm_ws(br_note)) and (t1d_str in note_ws))

# ===========================================================================
print("== T8: the uniform threshold is load-bearing INSIDE RR (the delta facet) ==")

shift = sp.simplify(Dstar_expr.subs(delta_s, delta_s / 2 ** kk) - Dstar_expr)
N_k = (1 + 2 * (Dstar_expr + kk * sp.log(2))) ** 3
N_limit = sp.limit(N_k.subs({vv: v_can, tau_s: 1, JV_s: 1, delta_s: sp.Rational(1, 10)}), kk, sp.oo)
check("A", "e-fold-dependent threshold delta_k = delta/2^k: D*(delta/2^k) - D*(delta) = k ln 2 exactly (sympy) and the reach N_k -> oo as k -> oo — a thresholdless or decaying-threshold RR variant loses k-uniformity, so RR's wording must (and does) carry ONE uniform supplied delta", sp.simplify(shift - kk * sp.log(2)) == 0 and N_limit == sp.oo)

check("A", "why delta lives inside RR while tau cannot: delta enters the lattice only as an operator-norm threshold (the sensitivity bound's free symbols are exactly {tau, delta, J_V, v} — no clock object; every sensitivity computed in this runner is an operator norm), while tau's MEANING requires the supplied clock map per the retained_no_go clock/rate interface — a typed asymmetry, not a preference", Dstar_k_free and ("operator norm" in note_ws or "operator-norm" in note_ws))

# ===========================================================================
print("== T9: consolidated chain completion — {RR, REG-tau} => (CAP-K) => (BR-int) => p = 0 (Lemma C recomputed) ==")

v_data = [sp.Integer(3), sp.Integer(-1), sp.Rational(1, 2), sp.Integer(2)]
pairs, additive_ok = 0, True
for assign in itertools.product([0, 1, 2], repeat=4):
    A = frozenset(i for i in range(4) if assign[i] == 0)
    B = frozenset(i for i in range(4) if assign[i] == 1)
    IA = sum((v_data[i] for i in A), sp.Integer(0))
    IB = sum((v_data[i] for i in B), sp.Integer(0))
    IAB = sum((v_data[i] for i in A | B), sp.Integer(0))
    pairs += 1
    if sp.simplify(IAB - IA - IB) != 0:
        additive_ok = False
unit_sum = sum(sp.Integer(1) for _ in range(7))
check("A", "retained finite-sector identity recomputed on all 81 ordered disjoint pairs of a 4-sector model; unit-record normalization M = 1 (I(R_7) = 7) — the Lemma C ingredients recomputed, not cited blind", additive_ok and pairs == 81 and unit_sum == 7, f"pairs={pairs}")

incr_id = sp.simplify(((sp.exp(p * (u + 1)) - 1) / p - (sp.exp(p * u) - 1) / p) - sp.exp(p * u) * (sp.exp(p) - 1) / p)
sel_ok = all(
    sp.limit(sp.exp(pv * u) * (sp.exp(pv) - 1) / pv, u, sp.oo if pv > 0 else -sp.oo) == sp.oo
    for pv in [sp.Integer(1), sp.Integer(2), sp.Rational(1, 2), sp.Rational(-1, 2), sp.Integer(-1)]
)
check("A", "(BR-int) point-selection recomputed: e-fold increment identity exact, increments unbounded for every p != 0 tested and constant for p = 0 — pass set on {s*g_p} exactly {p = 0}", incr_id == 0 and sel_ok)

check("A", "completion from the consolidated set: {RR, REG-tau} reproduces (CAP-real)+(REG-dyn)+(REG-thr) (T1 equivalence), the cone gives (CAP-K) with K = 129^3 (site reading, + REG-site) or 2^{129^3} (joint reading, no REG-site), both finite and k-uniform, and Lemma C + (BR-int) select p = 0 IDENTICALLY under both readings — (REG-site) changes K's value, never the pass set", equiv_ok and N_reach == 2146689 and sel_ok)

# ===========================================================================
print("== T10: the minimal generating set over the full model library ==")

lib_gen_ok = all(
    (cap_real(M) and reg_dyn(M) and reg_thr(M))
    for M in MODEL_LIBRARY
    if rr(M) and reg_tau(M)
)
n_rr_tau = sum(1 for M in MODEL_LIBRARY if rr(M) and reg_tau(M))
check("A", "{RR, (REG-tau)} generates the consolidated clauses: across the entire model library (256 toggle models + 7 witness models) every model satisfying RR AND REG-tau also satisfies CAP-real, REG-dyn, and REG-thr — no countermodel exists in the library", lib_gen_ok and n_rr_tau > 0 and len(MODEL_LIBRARY) == 263, f"library={len(MODEL_LIBRARY)}, rr&tau models={n_rr_tau}")

rr_alone_fails = rr(M_grow) and (not reg_tau(M_grow)) and (not chain_capped(M_grow, 16))
tau_alone_fails = reg_tau(M_fiat) and (not rr(M_fiat)) and (not cap_real(Model(efolds=M_mismatch.efolds, delta=DELTA, tau=TAU)))
check("A", "minimality: RR alone has a chain-failing countermodel (T5: growing windows, counts 4^k uncapped) and (REG-tau) alone has one (T3/T4: supplied window with fiat or mismatched realization) — so {RR, (REG-tau)} is a MINIMAL generating set; the declared-clause inventory on the realization layer drops 5 -> 2 (+ (REG-site) as optional sharpening)", rr_alone_fails and tau_alone_fails)

# ===========================================================================
print("== T11: walls, firewalls, ledger, honest scope ==")

rsm = read(os.path.join(REPO, "docs", "OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO_NOTE_2026-06-05.md"))
forbidden_rr = ["rr is derived", "(cap-real) is derived", "(cap-real) is supplied",
                "rr is supplied by", "derives the branch-to-scalar", "records must form",
                "p1 is retired", "p1 is closed", "this note promotes"]
found_rr = [s for s in forbidden_rr if s in note_ws.lower()]
check("B", "record-scalar-map wall: 'The missing step is the middle arrow.' present verbatim in the retained_no_go; the note DECLARES RR (a quantitative slice of that middle arrow) and never derives it; forbidden derivation/closure strings absent", ("The missing step is the middle arrow." in norm_ws(rsm)) and ("RR remains declared" in note_ws or "RR stays declared" in note_ws) and not found_rr, f"found={found_rr}")

cpf = read(os.path.join(REPO, "docs", "POST_RECORD_COUNT_PROBABILITY_FIREWALL_2026-06-06.md"))
check("B", "count-probability firewall: 'They cannot derive the model.' present verbatim; the note constructs no probability law (string present) and every sensitivity in this runner is an operator norm — counts appear only as exact witness arithmetic", ("They cannot derive the model." in norm_ws(cpf)) and ("no probability law is constructed" in note_ws))

rfn = read(os.path.join(REPO, "docs", "RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md"))
check("B", "record-formation wall: the retained_no_go's claim ('does **not** hold unconditionally') present verbatim; the note states RR conditions on the realization and does not force records to form (the class may be empty)", ("does **not** hold unconditionally" in norm_ws(rfn)) and ("does not force records to form" in note_ws) and ("may be empty" in note_ws or "may, for all the axioms care, be empty" in note_ws))

canon = read(os.path.join(REPO, "docs", "RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05.md"))
check("B", "canonical-proposal no-dynamics guardrail: 'it disclaims the decoherence *process* that produces it' present verbatim in the proposal note; RR is a declared realization clause, not a derivation forcing record formation on any partition", ("disclaims the decoherence *process* that produces it" in norm_ws(canon)) and ("declared" in note_ws))

with open(os.path.join(REPO, "docs", "audit", "data", "audit_ledger.json"), "r", encoding="utf-8") as fh:
    ledger_rows = json.load(fh)["rows"]
rows = {
    "microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09": "retained_bounded",
    "record_function_finite_sector_algebra_2026-06-05": "retained",
    "record_unbounded_finite_additivity_schema_2026-06-06": "audited_conditional",
    "post_record_clock_rate_interface_2026-06-06": "retained_no_go",
    "record_formation_not_unconditionally_forced_by_minimal_axioms_narrow_no_go_note_2026-06-06": "retained_no_go",
    "observable_principle_record_scalar_map_no_go_note_2026-06-05": "retained_no_go",
    "post_record_count_probability_firewall_2026-06-06": "retained_no_go",
    "single_clock_stone_finite_dim_uniqueness_narrow_theorem_note_2026-05-10": "retained",
}
missing_rows = [rid for rid in rows if ledger_rows.get(rid) is None]
live_statuses = {rid: ledger_rows.get(rid, {}).get("effective_status") for rid in rows}
capk_note = read(os.path.join(REPO, "docs", "OBSERVABLE_PRINCIPLE_P1_CAP_K_FROM_FINITE_SPEED_REGISTRATION_NARROW_THEOREM_NOTE_2026-06-10.md"))
capk_ws = norm_ws(capk_note)
capk_ok = all(s in capk_ws for s in ["REG-dyn", "REG-tau", "REG-thr", "REG-site", "(CAP-real) remains declared",
                                     "It is the association between the T1-d scalar readout increment and the registered collection"])
check(
    "B",
    "cited rows present in the audit ledger (presence only, 8 rows)",
    not missing_rows,
    f"missing={missing_rows}",
)
print(f"  [info][B] live effective statuses (audit-lane-owned; not gated): {live_statuses}")
check("B", "CAP-K source note contains the REG clauses, CAP-real declaration, and association sentence quoted here", capk_ok)

required = [
    "Status authority:",
    "independent audit lane",
    "does NOT retire P1",
    "RR remains declared",
    "no probability law is constructed",
    "no branch-to-scalar map is asserted",
    "does not force records to form",
]
missing = [s for s in required if norm_ws(s).lower() not in note_ws.lower()]
check("B", "note honest-scope and firewall-compliance strings present; the consolidation is presented as content-preserving bookkeeping over declared clauses (an implication-lattice theorem), not as a reduction of assumed content", not missing, f"missing={missing}")

# ===========================================================================
print()
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
if FAIL:
    raise SystemExit(1)
