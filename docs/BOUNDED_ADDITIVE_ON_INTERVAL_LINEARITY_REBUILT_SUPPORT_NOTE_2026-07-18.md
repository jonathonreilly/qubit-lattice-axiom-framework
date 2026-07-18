---
claim_id: bounded_additive_on_interval_linearity_rebuilt_support_note_2026-07-18
claim_type: bounded_theorem
claim_scope: "Standalone exact support theorem, rebuilt from first principles with no framework content and no literature input used as proof: a real additive function bounded on an interval of positive length is linear, G(u) = u·G(1). The proof is the finite chain — rational homogeneity by elimination, centered boundedness by the triangle decomposition, the integer-scaling rational sandwich |G(u) − (r_n/n)·G(1)| ≤ 2B/n with r_n/n within L/n of u, and the Archimedean squeeze — with every load-bearing step gated exactly in the runner. Purpose: retire the 'named standard mathematics' invocations of this theorem in the menu-family and theta lanes by supplying the repo-native rebuilt authority those notes can cite instead; this note claims nothing about any physical surface."
runner: scripts/bounded_additive_on_interval_linearity_rebuilt_2026_07_18.py
---

# Bounded Additive Functions On An Interval Are Linear: Rebuilt Support Theorem

**Date:** 2026-07-18
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** standalone exact mathematics; no framework surface, axiom
content, or physical claim; built so that citing notes carry a rebuilt
authority instead of a named-import.
**Audit-status authority:** independent audit lane only. This note sets no
audit verdict and predicts none.
**Primary runner:**
[`scripts/bounded_additive_on_interval_linearity_rebuilt_2026_07_18.py`](../scripts/bounded_additive_on_interval_linearity_rebuilt_2026_07_18.py)
**Runner cache:**
[`logs/runner-cache/bounded_additive_on_interval_linearity_rebuilt_2026_07_18.txt`](../logs/runner-cache/bounded_additive_on_interval_linearity_rebuilt_2026_07_18.txt)

## Purpose

Several lane notes invoke, as named standard mathematics, the theorem
that an additive real function bounded on a nondegenerate interval is
linear. Under the build-the-cited-algebra discipline, a named invocation
whose content is load-bearing is an import in disguise. This note
rebuilds the theorem completely — statement, proof, and gated steps — so
that consuming notes can cite a repo-native authority whose every
load-bearing identity the runner checks. The literature versions remain
comparators and are not used.

## Statement

Let `G : R → R` satisfy `G(u + v) = G(u) + G(v)` for all real `u, v`, and
suppose there are reals `a`, `L > 0`, `B ≥ 0` with `|G(w)| ≤ B` for every
`w ∈ [a, a + L]`. Then `G(u) = u · G(1)` for every real `u`.

## Proof (every load-bearing step gated)

- **(S1) Rational homogeneity.** `G(0) = 0` (from `G(0) = 2G(0)`),
  `G(−u) = −G(u)` (pair to zero), `G(n u) = n G(u)` for integers by
  iteration, and `G((p/q) u) = (p/q) G(u)` for rationals by combining the
  integer identities (formal eliminations in the runner).
- **(S2) Centered boundedness.** For `w ∈ [0, L]`:
  `G(w) = G(w + a) − G(a)`, and both `w + a` and `a` lie in `[a, a + L]`,
  so `|G(w)| ≤ |G(w + a)| + |G(a)| ≤ 2B` (triangle decomposition gated).
- **(S3) Integer-scaling rational sandwich.** Fix real `u` and integer
  `n ≥ 1`. Pick a rational `r_n` with `n u − r_n ∈ [0, L]` (a rational in
  the interval `[n u − L, n u]`; the runner exhibits the floor-grid
  choice `r_n = floor(n u / L) · L` for rational instances). Then

  > `n G(u) = G(n u) = G(r_n) + G(n u − r_n) = r_n G(1) + G(n u − r_n)`,

  and `|G(n u − r_n)| ≤ 2B` by (S2), so

  > `|G(u) − (r_n / n) G(1)| ≤ 2B / n`, with `|r_n / n − u| ≤ L / n`.

  The exact residual identity and the interval membership are gated on
  rational instances for `n = 1, ..., 4`, and the inequality chain is
  gated formally.
- **(S4) Archimedean squeeze.** Combining,
  `|G(u) − u G(1)| ≤ (2B + L·|G(1)|)/n` for every `n ≥ 1`. A fixed
  nonnegative quantity bounded by `c/n` for all `n` is zero: if it were
  `X > 0`, any integer `n > c/X` gives `X ≤ c/n < X`, a contradiction
  (the runner gates the contradiction witness and the exact limit
  `c/n → 0`). Hence `G(u) = u G(1)`.

No step uses continuity, measurability, monotonicity, or any literature
input; the interval's positive length `L > 0` is exactly where
degenerate-interval vacuity is excluded (a singleton gives no (S2)
window, and the runner carries a rejector showing the sandwich loses its
`1/n` decay without it).

## Consumers

The menu-family and theta lanes invoke this statement where their
additive functionals are bounded on an interval (weights valued in
`[0, 1]`; logarithmic readouts bounded on compact modulus windows).
Those notes' invocations are to be rewired to cite this rebuilt
authority; until each rewiring lands, their wording marks the theorem as
named-standard — the transitional state this note exists to retire.

## Non-Claims

- No framework, axiom, or physical content; no menu, readout, or channel
  claim; nothing here bears on any lane's hypotheses.
- Does **not** claim boundedness for any consumer's functional — each
  consumer states its own boundedness input.
- Does **not** set an audit verdict; independent audit remains required.

## Verification

The primary runner gates every load-bearing step exactly (sympy, exact
arithmetic, single process): the (S1) eliminations (zero, negation,
integer, rational); the (S2) triangle decomposition; the (S3) residual
identity and interval membership on rational instances `n = 1..4` with
the formal inequality chain; the (S4) contradiction witness and exact
limit; and the degenerate-interval rejector (no `1/n` decay at `L = 0`).
Mutation checks (one load-bearing mutation per family, reverted) are
recorded in the PR body.

Measured runner total after final verification:
`TOTAL: PASS=15 FAIL=0`.
