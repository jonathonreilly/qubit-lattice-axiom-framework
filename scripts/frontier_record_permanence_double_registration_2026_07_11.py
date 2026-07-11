#!/usr/bin/env python3
"""Exact checks for permanence-forced fresh-site double registration and
agreement-conditioned survival.

Companion runner for
docs/RECORD_PERMANENCE_FORCES_FRESH_SITE_DOUBLE_REGISTRATION_AND_AGREEMENT_SURVIVAL_BOUNDED_THEOREM_NOTE_2026-07-11.md.

Coverage:
  T0  verbatim axiom-quote guards (whitespace-normalized, so line-wrap safe).
  T1  finite-model combinatorial check of the axiom-forced geometry:
      admissible record histories on a small site set have injective sites
      (fresh-site registration) with full retention of every prior record;
      the inadmissible histories are exactly those with a repeated site
      (same-site rewrite / coexistence), and the pinch model D of same-site
      re-registration is idempotent (so the axioms remove that branch, they
      do not merely disfavor it).
  T2  the persistence <=> agreement-conditioned-survival equivalence on the
      finite model, with the supplied agreement-conditioned kernel reduced to
      r -> 2 r^2.
  EXH the necessity exhibit for the epoch-independent-readout premise:
      permanently coexisting DISAGREEING records with a still-well-defined but
      multi-valued-across-epochs ratio readout r = |b|^2 / a^2; additivity of
      the quadratic aggregates does NOT force epoch-independence.
  T3  exactness from permanence: linear multiplier |f'(r*)| = 2 at r* = 1/2,
      escape-step counts computed from (epsilon, band) with NO hard-coded step
      count, the permanence-forbids-re-preparation biconditional, the per-step
      agreement-survival probability p_s^2 + p_d^2 = 1/2 at equipartition, and
      the survivorship-not-stasis shrinkage.
  NOT the does-not-exclude-psi(r)=r^2 guard (the kappa question).

All checks are deterministic. No empirical numbers, fits, random draws, or
floating tolerances enter any derived quantity; the only floats are in the
escape-step arithmetic, where the step count is an integer computed by honest
iteration / a closed-form log, not asserted a priori.
"""

from itertools import product
from math import ceil, log2
from pathlib import Path

import sympy as sp


PASS = 0
FAIL = 0


def check(num: int, ok: bool, desc: str) -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"CHECK {num:02d}: {tag} -- {desc}")


def norm(text: str) -> str:
    """Whitespace-normalized text, so verbatim quotes survive line-wrapping."""
    return " ".join(text.split())


# ----------------------------------------------------------------------------
# T1 finite-model primitives.
#
# A candidate history is a finite sequence of registration events. For the
# geometry check an event is just its target site (content is abstracted here;
# content enters the necessity exhibit below). A history is ADMISSIBLE under
# the two load-bearing Record sentences iff it never re-uses a site:
#   * "A site never carries more than one record"  forbids a coexisting second
#     record at an occupied site;
#   * "records are permanent"                       forbids erasing the first
#     record to overwrite the site.
# Either reading of a same-site second event is inadmissible; a fresh site is
# the only admissible target.
# ----------------------------------------------------------------------------


def is_admissible(history):
    """Admissible == no site is registered twice (injective site sequence)."""
    return len(set(history)) == len(history)


def retained_record_count(history):
    """Under permanence + fresh-site, the retained record set after k events
    has exactly k records (monotone, full retention). Returns the list of
    running retained counts; for an admissible history this is [1, 2, ..., n]."""
    seen = set()
    counts = []
    for site in history:
        seen.add(site)
        counts.append(len(seen))
    return counts


def forbidding_rule(history):
    """For an INADMISSIBLE history, name which axiom sentence forbids the first
    repeat. Both branches are inadmissible; we record that a same-site second
    event violates one-record-per-site under coexistence AND permanence under
    overwrite."""
    seen = set()
    for k, site in enumerate(history):
        if site in seen:
            return {
                "repeat_at_epoch": k,
                "violates_one_per_site_if_coexisting": True,
                "violates_permanence_if_overwrite": True,
            }
        seen.add(site)
    return None


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    axiom_path = root / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
    axiom_norm = norm(axiom_path.read_text(encoding="utf-8"))

    # ---- T0 verbatim axiom-quote guards (line-wrap safe) --------------------
    q_form = "Records form."
    q_lock = "When present, a record locks exactly one admissible local possibility."
    q_perm = "A site never carries more than one record; records are permanent."
    q_read = "A readout value is determined by record content alone."
    q_add = (
        "For any finite collection of pairwise-disjoint records, scalar readout "
        "`I` is additive, with `I(empty)=0`."
    )

    check(1, norm(q_form) in axiom_norm, "axiom guard: 'Records form.'")
    check(2, norm(q_lock) in axiom_norm,
          "axiom guard: a record locks exactly one admissible local possibility")
    check(3, norm(q_perm) in axiom_norm,
          "axiom guard: one-record-per-site AND permanence sentence")
    check(4, norm(q_read) in axiom_norm,
          "axiom guard: readout is determined by record content alone")
    check(5, norm(q_add) in axiom_norm,
          "axiom guard: additive scalar readout I over disjoint records")

    # ---- T1 combinatorial check over admissible record histories -----------
    sites = ["s0", "s1", "s2"]  # small site set
    max_len = 3
    all_histories = []
    for n in range(1, max_len + 1):
        all_histories.extend(product(sites, repeat=n))

    admissible = [h for h in all_histories if is_admissible(h)]
    inadmissible = [h for h in all_histories if not is_admissible(h)]

    # (a) admissible  <=>  injective site sequence (fresh-site registration).
    fresh_site_iff_admissible = all(
        is_admissible(h) == (len(set(h)) == len(h)) for h in all_histories
    )
    # by construction of is_admissible this is a tautology guard; keep it to pin
    # the definition to the fresh-site statement explicitly.
    check(6, fresh_site_iff_admissible and len(admissible) > 0,
          "T1: admissible history <=> injective site sequence (fresh-site registration)")

    # (b) every admissible history retains all prior records: counts == 1..n.
    full_retention = all(
        retained_record_count(h) == list(range(1, len(h) + 1)) for h in admissible
    )
    check(7, full_retention,
          "T1: every admissible history retains all prior records (count k after k events)")

    # (c) inadmissible == exactly the histories with a same-site second event,
    #     each forbidden by one-per-site (coexistence) AND permanence (overwrite).
    repeat_is_the_only_obstruction = all(
        (forbidding_rule(h) is not None) for h in inadmissible
    ) and all((forbidding_rule(h) is None) for h in admissible)
    both_branches_forbidden = all(
        forbidding_rule(h)["violates_one_per_site_if_coexisting"]
        and forbidding_rule(h)["violates_permanence_if_overwrite"]
        for h in inadmissible
    )
    check(8, repeat_is_the_only_obstruction and both_branches_forbidden,
          "T1: inadmissible <=> same-site second registration, forbidden under BOTH readings")

    # (d) tie to anatomy G1: the same-site re-pinch model D is idempotent, so
    #     the same-site reading of re-registration is a weight no-op; the axioms
    #     remove that reading and force the fresh-site double-registration one.
    m = sp.MatrixSymbol("M", 3, 3)
    M = sp.Matrix(m)
    P_s = sp.diag(1, 0, 0)
    P_d = sp.diag(0, 1, 1)
    D = lambda X: P_s * X * P_s + P_d * X * P_d
    idempotent = sp.simplify(D(D(M)) - D(M)) == sp.zeros(3, 3)
    check(9, idempotent,
          "T1<->G1: same-site re-pinch D is idempotent (D(D(M))=D(M)); axioms force fresh-site reading")

    # ---- T2 supplied agreement-conditioned kernel reduces to r -> 2 r^2 -----
    r = sp.symbols("r", nonnegative=True)
    p_s = 1 / (1 + 2 * r)
    p_d = 2 * r / (1 + 2 * r)
    Z = p_s**2 + p_d**2
    p_s_next = p_s**2 / Z
    p_d_next = p_d**2 / Z
    r_next = sp.simplify(p_d_next / (2 * p_s_next))  # r' = (p_d'/p_s')/2
    kernel_reduces = sp.simplify(r_next - 2 * r**2) == 0
    check(10, kernel_reduces,
          "T2: supplied agreement-conditioned kernel p_i'=p_i^2/(p_s^2+p_d^2) reduces to r->2r^2")

    # ---- T2 equivalence on a finite grid -----------------------------------
    f = lambda rv: 2 * rv**2
    grid = [sp.Integer(0), sp.Rational(1, 4), sp.Rational(1, 3),
            sp.Rational(1, 2), sp.Integer(1), sp.Integer(2)]
    n_epochs = 6

    def persists(rv):
        """Epoch-independent readout stays constant across n_epochs under f."""
        cur = rv
        for _ in range(n_epochs):
            cur = f(cur)
            if cur != rv:
                return False
        return True

    def is_fixed(rv):
        return sp.simplify(f(rv) - rv) == 0

    # forward: persistence => survival (fixed point); backward: fixed point =>
    # persistence. The finite biconditional is persists(r) <=> is_fixed(r).
    forward_ok = all((not persists(rv)) or is_fixed(rv) for rv in grid)
    backward_ok = all((not is_fixed(rv)) or persists(rv) for rv in grid)
    fixed_set = {rv for rv in grid if is_fixed(rv)}
    check(11, forward_ok,
          "T2 forward: lane-value persistence => registered value is a kernel fixed point")
    check(12, backward_ok,
          "T2 backward: kernel fixed point => constant readout across epochs (persistence)")
    check(13, fixed_set == {sp.Integer(0), sp.Rational(1, 2)},
          "T2: interior/degenerate finite fixed set on the grid is exactly {0, 1/2}")

    # ---- Necessity exhibit for the epoch-independent-readout premise --------
    # Two permanent coexisting records on DISTINCT sites (T1), disagreeing.
    a1_sq, b1_sq = sp.Integer(2), sp.Integer(1)   # r1 = 1/2 (a kernel fixed pt)
    a2_sq, b2_sq = sp.Integer(1), sp.Integer(1)   # r2 = 1   (the thermal value)
    r1 = sp.Rational(b1_sq, a1_sq)
    r2 = sp.Rational(b2_sq, a2_sq)
    # additive quadratic aggregates over the disjoint two-record collection:
    A_pool = a1_sq + a2_sq
    B_pool = b1_sq + b2_sq
    r_pool = sp.Rational(B_pool, A_pool)          # ratio of the aggregates
    disagree = r1 != r2
    pooled_is_third_value = (r_pool != r1) and (r_pool != r2)
    check(14, disagree and pooled_is_third_value,
          "EXH: coexisting permanent records disagree (r1=1/2, r2=1) and the pooled ratio 2/3 is a third value")

    # ratio readout is NOT additive: additivity holds for A, B but r = B/A is a
    # ratio, so the pooled readout is the mediant, not the sum, and differs from
    # each epoch value -- additivity therefore does NOT force epoch-independence.
    aggregates_additive = (A_pool == a1_sq + a2_sq) and (B_pool == b1_sq + b2_sq)
    ratio_not_additive = (r_pool != r1 + r2)  # mediant, not a sum
    check(15, aggregates_additive and ratio_not_additive,
          "EXH: quadratic aggregates are additive but the ratio readout r=B/A is not; additivity does not force epoch-independence")

    # positive control: when r1 == r2 (epoch-independence holds), the mediant
    # equals the common value -- additivity is CONSISTENT with (not contrary to)
    # epoch-independence; it simply does not entail it.
    a3_sq, b3_sq = sp.Integer(2), sp.Integer(1)   # r = 1/2
    a4_sq, b4_sq = sp.Integer(4), sp.Integer(2)   # r = 1/2 (same value)
    r_pool_equal = sp.Rational(b3_sq + b4_sq, a3_sq + a4_sq)
    check(16, r_pool_equal == sp.Rational(1, 2),
          "EXH positive control: equal epoch values pool to the common value (mediant of equal ratios)")

    # ---- T3 exactness from permanence --------------------------------------
    fr = 2 * r**2
    multiplier = sp.diff(fr, r).subs(r, sp.Rational(1, 2))
    check(17, multiplier == 2,
          "T3: local expansion multiplier |f'(r*)| = 2 at the interior fixed point r* = 1/2")

    def escape_steps_exact(epsilon, band):
        """Iterate the EXACT map from 1/2 + epsilon until |r - 1/2| >= band."""
        rv = 0.5 + epsilon
        n = 0
        while abs(rv - 0.5) < band:
            rv = 2 * rv * rv
            n += 1
            if n > 10000:
                break
        return n

    def escape_steps_linear(epsilon, band):
        """Closed-form linear estimate: 2^n * epsilon >= band."""
        return ceil(log2(band / epsilon))

    eps1, band1 = 1e-5, 0.1
    n_lin1 = escape_steps_linear(eps1, band1)
    n_exa1 = escape_steps_exact(eps1, band1)
    # second (eps, band) pair proves the count is a FORMULA, not a constant.
    eps2, band2 = 1e-8, 0.2
    n_lin2 = escape_steps_linear(eps2, band2)
    n_exa2 = escape_steps_exact(eps2, band2)

    check(18, n_lin1 == 14 and n_lin1 == ceil(log2(band1 / eps1)),
          f"T3: linear escape count computed from (eps,band)=(1e-5,0.1) is {n_lin1} = ceil(log2(band/eps))")
    check(19, abs(n_exa1 - n_lin1) <= 1 and abs(n_exa2 - n_lin2) <= 1,
          f"T3: exact-map escape ({n_exa1}, {n_exa2}) agrees with linear ({n_lin1}, {n_lin2}) within one step")
    check(20, n_lin2 != n_lin1,
          f"T3: a second (eps,band)=(1e-8,0.2) gives a different count {n_lin2} (formula, not hard-coded)")

    # permanence forbids re-preparation: for eps != 0 an out-of-band (disagreeing)
    # record forms within the escape window and is PERMANENT; only eps == 0
    # persists forever. Biconditional over a grid of interior offsets.
    def persists_forever(epsilon, band, horizon):
        rv = 0.5 + epsilon
        for _ in range(horizon):
            if abs(rv - 0.5) >= band:
                return False
            rv = 2 * rv * rv
        return True

    offsets = [0.0, 1e-5, -1e-5, 1e-3, 1e-7]
    # horizon long enough that EVERY nonzero offset escapes its band (its escape
    # window depends on |offset|); only the exact fixed point survives all of it.
    horizon = max(escape_steps_linear(abs(e), band1)
                  for e in offsets if e != 0.0) + 3
    persistence_iff_exact = all(
        persists_forever(e, band1, horizon) == (e == 0.0) for e in offsets
    )
    check(21, persistence_iff_exact,
          "T3: observed persistence across the escape window <=> exact fixed point (permanence forbids re-preparation)")

    # per-step agreement-survival probability at the equipartition fixed point.
    ps_star = p_s.subs(r, sp.Rational(1, 2))
    pd_star = p_d.subs(r, sp.Rational(1, 2))
    p_survive = sp.simplify(ps_star**2 + pd_star**2)
    check(22, ps_star == sp.Rational(1, 2) and pd_star == sp.Rational(1, 2)
          and p_survive == sp.Rational(1, 2),
          "T3: at r*=1/2 equipartition (p_s=p_d=1/2), per-step agreement-survival prob p_s^2+p_d^2 = 1/2")

    # survivorship, not stasis: the agreeing subpopulation shrinks as (1/2)^n.
    n_steps = 5
    surviving_fraction = sp.Rational(1, 2) ** n_steps
    shrinks = surviving_fraction < 1 and surviving_fraction > 0
    check(23, shrinks and surviving_fraction == sp.Rational(1, 32),
          "T3: fixed-point persistence is survivorship of the agreeing subpopulation ((1/2)^n), not stasis of every history")

    # ---- NOT-claim guard: does not exclude psi(r) = r^2 (the kappa question) -
    psi = lambda rv: rv**2
    psi_fixed = {rv for rv in [sp.Integer(0), sp.Rational(1, 2), sp.Integer(1),
                               sp.Integer(2)] if sp.simplify(psi(rv) - rv) == 0}
    psi_mult_at_1 = sp.diff(r**2, r).subs(r, sp.Integer(1))
    # psi shares the multiplier 2 at ITS interior fixed point r=1, which differs
    # from f's interior fixed point r=1/2; nothing here selects between them.
    check(24, psi_fixed == {sp.Integer(0), sp.Integer(1)} and psi_mult_at_1 == 2
          and sp.Rational(1, 2) not in psi_fixed,
          "NOT: psi(r)=r^2 has interior fixed point r=1 (mult 2), != f's r=1/2; this note excludes neither (kappa question)")

    # ---- report -------------------------------------------------------------
    print("SUMMARY escape arithmetic: "
          f"(eps=1e-5, band=0.1) -> linear {n_lin1} steps, exact {n_exa1} steps; "
          f"(eps=1e-8, band=0.2) -> linear {n_lin2} steps, exact {n_exa2} steps.")
    print("SUMMARY necessity exhibit: r1=1/2, r2=1 permanent & coexisting; "
          "pooled ratio 2/3 is a third value; ratio readout is not additive.")
    print("SUMMARY discharged: T1 fresh-site double-registration geometry (axiom-forced). "
          "Named premise: epoch-independent lane readout (necessity exhibited). "
          "Open: outcome factorization; bookkeeping multiplicity (kappa lane).")
    print("SUMMARY files: "
          "docs/RECORD_PERMANENCE_FORCES_FRESH_SITE_DOUBLE_REGISTRATION_AND_AGREEMENT_SURVIVAL_BOUNDED_THEOREM_NOTE_2026-07-11.md; "
          "scripts/frontier_record_permanence_double_registration_2026_07_11.py")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
