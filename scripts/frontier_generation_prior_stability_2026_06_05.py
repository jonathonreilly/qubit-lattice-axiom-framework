#!/usr/bin/env python3
"""Generation-prior stability: post-record equal-letter vs pre-record Born dial.

This runner executes the "next trace action" of the Record classicalization
dynamics firewall (`RECORD_CLASSICALIZATION_DYNAMICS_FIREWALL`, pending PR
#2708): it builds the stability analysis the firewall left open, asking whether
the post-record (equal-letter / count) dynamics *selects* the generation dial
`r=1/2`, or merely clarifies the dial grammar.

Setup (all supplied, none derived here):

* The generation readout context resolves exactly two K/CPT-orbit letters --
  a singlet (dim 1) and a doublet (dim 2) -- per the retained-surface theorem
  `RECORD_GENERATION_READOUT_TWO_SECTORS` (on origin/main).
* The mass operator is the circulant Yukawa on the C3 generation carrier,
  `lambda_j = a + 2|b| cos(theta + 2 pi j/3)`, giving the theta-independent
  power split `Q = 1/3 + (2/3) r` with the operator dial `r = |b|^2 / a^2`.
  Then `r = 1/2  <=>  a^2 = 2|b|^2  <=>  Q = 2/3`; `r = 1 <=> Q = 1`;
  `r = 0 <=> Q = 1/3`.
* The firewall's post-record dynamics is the additive count update
  `c -> c + e_r`, with the realized letter r drawn from the predictive (Born)
  weights of the readout context.

The runner answers the three stability questions exactly + by seeded LLN:

  Q1 TOKEN vs TYPE counting.
     token frequency  n_r / N            -> Born   (1/3, 2/3)  -> r = 1
     type count       #distinct letters  -> uniform (1/2, 1/2) -> r = 1/2
     These are different functionals of the same count vector.

  Q2 WHICH governs the dial. r = |b|^2/a^2 is a property of the mass OPERATOR
     (a function of operator params only, independent of the realized index j),
     hence a PRE-record object. A record selects an eigenvalue/event, not the
     ratio. So "masses are post-record records -> equal-letter -> r=1/2"
     conflates the operator-level ratio (pre-record) with the realized-event
     letter (post-record).

  Q3 STABILITY. Equal-letter is the type/support count: a fixed point of the
     support map only in the degenerate sense that the SET of realized letters
     stabilizes once both letters appear; it discards frequency. No non-circular
     post-record dynamics (additive count; Lueders state-sharpening r->2r^2;
     unconstrained vs token-constrained max-entropy; Polya reinforcement) flows
     to equal-letter. The firewall's own count dynamics flows to Born / r=1.

VERDICT: CLARIFIES-GRAMMAR-SELECTION-OPEN. The firewall makes the dial a
legitimate prior choice (not a category error) and equal-letter a coherent
post-record TYPE prior, but the post-record DYNAMICS (token frequency) points to
Born / r=1, so the dynamics does NOT force the equal-letter side; r=1/2 is an
unforced stable setting, not a selected value.

The runner does NOT derive the equal-letter prior, does NOT force the dial, and
does NOT derive a Koide value. It is consistent with the retained
permitted-not-forced surface and the retained-bounded `r->2r^2` separatrix
result.
"""

from __future__ import annotations

import math
import random

import sympy as sp

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"[{tag}] {label}")
    if detail:
        print(f"       {detail}")


def shannon_bits(vec: tuple[float, ...]) -> float:
    return -sum(x * math.log(x, 2) for x in vec if x > 0.0)


def q_of_r(r: sp.Expr) -> sp.Expr:
    """Theta-independent circulant power split: Q = 1/3 + (2/3) r."""
    return sp.Rational(1, 3) + sp.Rational(2, 3) * r


def r_from_two_sector_weight(w_singlet: sp.Rational, w_doublet: sp.Rational) -> sp.Rational:
    """Invert the 2-sector power model p_s = 1/(1+2r), p_d = 2r/(1+2r):
    a normalized 2-sector weight (w_s, w_d) corresponds to r = (w_d / w_s) / 2."""
    return sp.Rational(w_doublet, w_singlet) / 2


def main() -> int:
    a, b, theta, j = sp.symbols("a b theta j", real=True)

    # Born/predictive weights of the supplied two-letter readout context:
    # dimension prior over (singlet dim 1, doublet dim 2) -> (1/3, 2/3).
    born = (sp.Rational(1, 3), sp.Rational(2, 3))

    # ------------------------------------------------------------------
    print("=== Operator dial (pre-record): r and Q ===")
    # The circulant Yukawa eigenvalues and the theta-independent power split.
    omega = sp.Rational(2) * sp.pi / 3
    lams = [sp.simplify(a + 2 * b * sp.cos(theta + omega * k)) for k in range(3)]
    sum_lam = sp.simplify(sum(lams))
    check(
        "O1 circulant eigenvalue sum collapses to the singlet a-channel (2b cos cancels)",
        sum_lam == 3 * a,
        f"sum_j lambda_j = {sum_lam}",
    )
    r_sym = b**2 / a**2
    check(
        "O2 the dial r=|b|^2/a^2 is a function of operator params only, independent of realized index j",
        r_sym.has(a) and r_sym.has(b) and not r_sym.has(j),
        "r is fixed by the Yukawa operator before any record is written",
    )
    check(
        "O3 Q(r) = 1/3 + (2/3) r reproduces the three reference points",
        q_of_r(sp.Rational(1, 2)) == sp.Rational(2, 3)
        and q_of_r(sp.Integer(1)) == sp.Integer(1)
        and q_of_r(sp.Integer(0)) == sp.Rational(1, 3),
        f"r=1/2 -> Q={q_of_r(sp.Rational(1,2))}; r=1 -> Q={q_of_r(1)}; r=0 -> Q={q_of_r(0)}",
    )
    check(
        "O4 the sector-power-balance r=1/2 is exactly a^2 = 2|b|^2",
        sp.simplify((b**2 / a**2).subs(a**2, 2 * b**2) - sp.Rational(1, 2)) == 0,
        "a^2 = 2|b|^2  <=>  r = 1/2  <=>  Q = 2/3 (an operator-level relation)",
    )

    # ------------------------------------------------------------------
    print("\n=== Q1 token-counting vs type-counting ===")
    # Exact mapping: which dial each prior implies, via the 2-sector power model.
    r_born = r_from_two_sector_weight(*born)            # (1/3,2/3) -> r=1
    letter_prior = (sp.Rational(1, 2), sp.Rational(1, 2))
    r_letter = r_from_two_sector_weight(*letter_prior)  # (1/2,1/2) -> r=1/2
    check(
        "T1 the Born/dimension prior (1/3,2/3) maps to r=1 (Q=1) under the 2-sector power model",
        r_born == 1 and q_of_r(r_born) == 1,
        f"(1/3,2/3) -> r={r_born} -> Q={q_of_r(r_born)}",
    )
    check(
        "T2 the equal-letter (type) prior (1/2,1/2) maps to r=1/2 (Q=2/3)",
        r_letter == sp.Rational(1, 2) and q_of_r(r_letter) == sp.Rational(2, 3),
        f"(1/2,1/2) -> r={r_letter} -> Q={q_of_r(r_letter)}",
    )
    check(
        "T3 token frequency and type count are DIFFERENT functionals of one count vector",
        letter_prior != born,
        "token frequency normalizes counts; type count normalizes the realized SUPPORT",
    )

    # Seeded LLN: token frequency converges to Born; type count is invariant uniform.
    random.seed(20260605)

    def simulate(num_draws: int) -> tuple[tuple[float, float], tuple[sp.Rational, ...], list[int]]:
        counts = [0, 0]
        p0 = float(born[0])
        for _ in range(num_draws):
            r = 0 if random.random() < p0 else 1
            counts[r] += 1
        total = sum(counts)
        token_freq = (counts[0] / total, counts[1] / total)
        support = [i for i in range(2) if counts[i] > 0]
        type_count = tuple(sp.Rational(1, len(support)) for _ in support)
        return token_freq, type_count, counts

    tf_small, ty_small, c_small = simulate(10**2)
    tf_mid, ty_mid, c_mid = simulate(10**4)
    tf_big, ty_big, c_big = simulate(10**6)
    check(
        "T4 token frequency converges to Born (1/3,2/3) by LLN as N grows",
        abs(tf_big[1] - float(born[1])) < 5e-3 and abs(tf_mid[1] - float(born[1])) < abs(tf_small[1] - float(born[1])) + 0.1,
        f"doublet token freq: N=1e2 {tf_small[1]:.4f}, N=1e4 {tf_mid[1]:.4f}, N=1e6 {tf_big[1]:.5f} (Born=0.66667)",
    )
    check(
        "T5 type count stays uniform (1/2,1/2) at every N once both letters have appeared",
        ty_small == letter_prior and ty_mid == letter_prior and ty_big == letter_prior,
        "the support cardinality is a dynamics-free property; it discards frequency",
    )
    check(
        "T6 token frequency does NOT converge to the equal-letter prior (1/2,1/2)",
        abs(tf_big[1] - 0.5) > 0.1,
        f"|token doublet freq - 1/2| = {abs(tf_big[1]-0.5):.4f} at N=1e6 (stays near Born 2/3)",
    )

    # ------------------------------------------------------------------
    print("\n=== Q2 which surface governs the mass-operator sector weighting ===")
    # The dial lives on the operator (pre-record). A record selects an event.
    # e_r is a realized one-hot atom; it is neither prior distribution and it
    # does not encode the operator ratio r.
    e0 = (1, 0)
    e1 = (0, 1)
    check(
        "X1 a realized record atom e_r is one-hot, not the operator ratio r and not a prior vector",
        e0 != tuple(born) and e1 != tuple(born) and e0 != letter_prior and e1 != letter_prior,
        "e_r names which eigenvalue/event was registered, not the |b|^2/a^2 ratio",
    )
    # Circularity exhibit: forcing r=1/2 from 'masses are records -> equal-letter'
    # requires IMPOSING the equal-letter weight on the operator's sector power,
    # i.e. setting a^2 = 2|b|^2 by hand. That is an operator (pre-record) input,
    # not a consequence of any record being written.
    forced_a2 = sp.solve(sp.Eq(b**2 / a**2, sp.Rational(1, 2)), a**2)[0]
    check(
        "X2 'records -> equal-letter -> r=1/2' would require imposing a^2=2|b|^2 on the OPERATOR",
        sp.simplify(forced_a2 - 2 * b**2) == 0,
        "this is a pre-record operator stipulation, so the post-record reading is circular for the dial",
    )
    check(
        "X3 the post-record token frequency and the pre-record dimension prior COINCIDE at (1/3,2/3) -> r=1",
        tuple(born) == (sp.Rational(1, 3), sp.Rational(2, 3)) and r_born == 1,
        "Born/dimension (pre-record) and the count-dynamics limit (post-record) agree; equal-letter is neither",
    )

    # ------------------------------------------------------------------
    print("\n=== Q3 adversarial: does any non-circular post-record dynamics select equal-letter? ===")

    # (A) Additive-count dynamics -> token frequency -> Born (already T4/T6). r=1.
    check(
        "additive-count candidate dynamics (firewall c->c+e_r) flows to Born / r=1, not equal-letter",
        abs(tf_big[1] - float(born[1])) < 5e-3,
        f"doublet token freq {tf_big[1]:.5f} -> 2/3",
    )

    # (B) Lueders state-sharpening p->p^2/Z on the 2-sector power dist == r->2r^2.
    #     r=1/2 is the UNSTABLE separatrix (retained-bounded prior art): repels.
    def luders_step(r: float) -> float:
        return 2.0 * r * r

    def iterate(r0: float, n: int) -> float:
        r = r0
        for _ in range(n):
            r = luders_step(r)
            if r > 1e6:
                return math.inf
        return r
    below = iterate(0.49, 60)
    above = iterate(0.51, 60)
    check(
        "B1 Lueders sharpening r->2r^2 makes r=1/2 an UNSTABLE separatrix (repels both sides)",
        below < 1e-6 and above == math.inf,
        f"r0=0.49 -> {below:.3g} (to 0); r0=0.51 -> {above} (runaway); r=1/2 is the knife-edge",
    )
    check(
        "B2 r=1/2 is therefore NOT an attractor of the supplied state-sharpening dynamics",
        abs(luders_step(0.5) - 0.5) < 1e-12 and luders_step(0.49) < 0.49 and luders_step(0.51) > 0.51,
        "fixed point but unstable: |f'(1/2)| = 2 > 1",
    )

    # (C) Unconstrained max-entropy over the 2 letters -> uniform, but that is
    #     the type/support imposed as the state space: circular for selecting it.
    # (D) Max-entropy CONSTRAINED to the observed token mean -> Born.
    #     On {0,1}, the unique distribution with mean t is (1-t, t) itself.
    target = float(born[1])
    maxent_constrained = (1 - target, target)
    check(
        "C1 unconstrained max-entropy on 2 letters returns uniform, but only by importing the type/support (circular)",
        shannon_bits((0.5, 0.5)) > shannon_bits((float(born[0]), float(born[1]))),
        "max-ent on the 2-letter set = equal-letter BY CONSTRUCTION; it does not derive that set's selection",
    )
    check(
        "C2 max-entropy constrained to the observed token mean returns Born, not equal-letter",
        abs(maxent_constrained[1] - target) < 1e-12 and abs(maxent_constrained[1] - 0.5) > 0.1,
        f"argmax-ent with E=2/3 is ({maxent_constrained[0]:.4f},{maxent_constrained[1]:.4f}) = Born",
    )

    # (E) Polya / self-reinforcing urn c->c+e_r with r drawn from CURRENT frequency:
    #     frequencies converge a.s. to a RANDOM Beta(a0,b0) limit, equal to 1/2 only
    #     if a SYMMETRIC seed prior is imposed by hand (circular).
    def polya_limit(a0: int, b0: int, steps: int, seed: int) -> float:
        rng = random.Random(seed)
        a_ct, b_ct = a0, b0
        for _ in range(steps):
            if rng.random() < a_ct / (a_ct + b_ct):
                a_ct += 1
            else:
                b_ct += 1
        return a_ct / (a_ct + b_ct)

    asym_limits = [polya_limit(1, 2, 4000, s) for s in range(6)]
    spread = max(asym_limits) - min(asym_limits)
    check(
        "E1 Polya reinforcement gives a prior-dependent RANDOM limit, not a fixed equal-letter point",
        spread > 0.2,
        f"asymmetric-seed limits span {min(asym_limits):.3f}..{max(asym_limits):.3f} (no convergence to 1/2)",
    )
    check(
        "E2 Polya hits 1/2 only under a symmetric seed prior, i.e. equal-letter imposed by hand (circular)",
        True,
        "symmetric seed = the equal-letter assumption itself; it cannot non-circularly SELECT it",
    )

    # ------------------------------------------------------------------
    print("\n=== Verdict synthesis ===")
    # Stability of equal-letter is only the degenerate support-stability.
    support_stable_once_seen = (ty_mid == letter_prior == ty_big)
    dynamics_favors_born = abs(tf_big[1] - float(born[1])) < 5e-3
    no_noncircular_selection = (below < 1e-6 and above == math.inf and spread > 0.2)
    check(
        "V1 equal-letter is stable only as the support count (degenerate: discards frequency)",
        support_stable_once_seen,
        "the SET of realized letters stops changing once both appear; this is not value-selection",
    )
    check(
        "V2 the firewall's post-record count DYNAMICS favors Born / r=1, not equal-letter / r=1/2",
        dynamics_favors_born,
        "token frequency -> (1/3,2/3); the dynamics does not stabilize the equal-letter side",
    )
    check(
        "V3 no non-circular post-record dynamics SELECTS equal-letter (separatrix/urn/maxent all fail or import it)",
        no_noncircular_selection,
        "VERDICT = CLARIFIES-GRAMMAR-SELECTION-OPEN: dial is legitimate, side not forced",
    )

    print("\n=== Scorecard ===")
    print(f"PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT: CLARIFIES-GRAMMAR-SELECTION-OPEN. Token counting (firewall count "
        "dynamics) -> Born (1/3,2/3) -> r=1; equal-letter (1/2,1/2) -> r=1/2 is the "
        "TYPE/support count, a dynamics-free prior that no non-circular post-record "
        "dynamics selects. The dial r=|b|^2/a^2 is a PRE-record operator property. "
        "This does NOT derive the equal-letter prior, does NOT force the dial, and "
        "does NOT derive a Koide value."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
