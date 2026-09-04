---
claim_id: bounded_additive_on_interval_linearity_rebuilt_support_note_2026-07-18
claim_type: bounded_theorem
claim_scope: "Standalone exact support theorem, rebuilt from first principles with no framework content and no literature input used as proof: a real additive function bounded on an interval of positive length is linear, G(u) = u·G(1). The proof is the finite chain — rational homogeneity, centered boundedness by the triangle inequality, a rational-density sandwich, and the integer Archimedean squeeze. The runner supplies exact symbolic identities and finite rational consistency instances; the universal quantifiers are discharged by the written proof. This note claims nothing about any physical surface and supplies no boundedness premise for a consumer."
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
rebuilds the theorem completely — statement and proof — so that consuming
notes can cite a repo-native authority. The runner checks exact symbolic
identities and finite rational consistency instances; it is not presented as
an executable proof of the universal quantifiers. Literature versions remain
comparators and are not used.

## Statement

Let `G : R → R` satisfy `G(u + v) = G(u) + G(v)` for all real `u, v`, and
suppose there are reals `a`, `L > 0`, `B ≥ 0` with `|G(w)| ≤ B` for every
`w ∈ [a, a + L]`. Then `G(u) = u · G(1)` for every real `u`.

## Proof

- **(S1) Rational homogeneity.** `G(0) = 0` (from `G(0) = 2G(0)`),
  `G(−u) = −G(u)` (pair to zero), `G(n u) = n G(u)` for integers by
  iteration, and `G((p/q) u) = (p/q) G(u)` for rationals by combining the
  integer identities.
- **(S2) Centered boundedness.** For `w ∈ [0, L]`:
  `G(w) = G(w + a) − G(a)`, and both `w + a` and `a` lie in `[a, a + L]`,
  so `|G(w)| ≤ |G(w + a)| + |G(a)| ≤ 2B` by the triangle inequality.
- **(S3) Integer-scaling rational sandwich.** Fix real `u` and integer
  `n ≥ 1`. Pick a rational `r_n` with `n u − r_n ∈ [0, L]` (a rational in
  the interval `[n u − L, n u]`; the runner exhibits the floor-grid
  choice `r_n = floor(n u / L) · L` for rational instances). Then

  > `n G(u) = G(n u) = G(r_n) + G(n u − r_n) = r_n G(1) + G(n u − r_n)`,

  and `|G(n u − r_n)| ≤ 2B` by (S2), so

  > `|G(u) − (r_n / n) G(1)| ≤ 2B / n`, with `|r_n / n − u| ≤ L / n`.

  The runner checks the exact residual identity and interval membership on
  rational instances for `n = 1, ..., 4`, together with the symbolic
  elimination. Rational density and the universal choice for arbitrary real
  `u`, `L > 0`, and integer `n` are the written proof step.
- **(S4) Archimedean squeeze.** Combining,
  `|G(u) − u G(1)| ≤ (2B + L·|G(1)|)/n` for every `n ≥ 1`. A fixed
  nonnegative quantity bounded by `c/n` for all `n` is zero: if it were
  `X > 0`, the integer `n = floor(c/X) + 1` gives `n > c/X`, hence
  `X ≤ c/n < X`, a contradiction. Hence `G(u) = u G(1)`. The runner checks
  an exact rational instance of this integer witness and the limit `c/n → 0`.

No step uses continuity, measurability, monotonicity, or any literature
input. Positive length is used to obtain a genuine centered interval and the
rational-density choice in (S3). At `L = 0` this proof supplies no such
window; the theorem makes no claim about functions bounded only at a
singleton.

## Consumers

Potential consumers may cite this statement only when they independently
supply the positive-length interval and its bound. In particular, a
logarithmic-coordinate readout does not become bounded merely because it is
written on a compact modulus window; boundedness must be an explicit premise
or separately proved.

## Non-Claims

- No framework, axiom, or physical content; no menu, readout, or channel
  claim; nothing here bears on any lane's hypotheses.
- Does **not** claim boundedness for any consumer's functional — each
  consumer states its own boundedness input.
- Does **not** set an audit verdict; independent audit remains required.

## Verification

The primary runner uses SymPy exact arithmetic in one process. It checks
representative (S1) eliminations; the centered decomposition and exact finite
sign cases for the triangle inequality; the (S3) residual identity and window
membership on rational instances `n = 1..4`; the symbolic sandwich
elimination; an exact integer Archimedean witness and the limit `c/n → 0`;
and a finite proof guard showing that a positive mesh can fit inside a
positive-width interval whereas no positive mesh fits a zero-width interval.
These are consistency checks for the written proof, not a claim that finite
execution verifies its universal quantifiers.

Measured runner total after final verification:
`TOTAL: PASS=15 FAIL=0`.
