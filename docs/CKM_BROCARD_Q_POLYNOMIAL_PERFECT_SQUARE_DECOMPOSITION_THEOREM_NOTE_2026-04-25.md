# Brocard / Q Polynomial Perfect-Square Decomposition

**Type:** open_gate
**Review scope:** conditional supplied algebra and the specifically reviewed comparisons;
physical interpretation, inherited authority checks, and audit status are not certified.

**Date:** 2026-04-25

**Status:** proposed_retained

This note records conditional square-channel identities for the supplied polynomial pair.
The supplied counts are `(N_pair, N_color, N_quark) = (2, 3, 6)`.
The polynomial formulas and NLO apex map are premises here; neither physical
count selection nor upstream retained closure is established by this note.
The live claim remains an `open_gate` while the companion's three historical
status-text diagnostics fail. Their predicates and nonzero exit are preserved.

The headline closed forms:

```text
(D2)  Q(alpha_s) - P(alpha_s)  =  N_pair^6 (N_quark - 1) (N_pair^2 - alpha_s)^2
                                 =  320 (4 - alpha_s)^2.

      Scalar-multiple square channel in (4 - alpha_s); proportional to Wolfenstein
      eta_bar^2 (and hence to normalized area squared J_norm^2).

(D3)  P(alpha_s) + 3 Q(alpha_s)  =  N_pair^2 (alpha_s^2 - 4 alpha_s + 96)^2
                                  =  4 (48 perim_sq)^2
                                  =  N_pair^8 N_quark^2 perim_sq^2.

      Scalar-multiple square channel in (alpha_s^2 - 4 alpha_s + 96) = 48 perim_sq;
      proportional to perimeter-squared of the unitarity triangle.
```

So **the (P, Q) algebraic module decomposes into two scalar-multiple square
channels**:
- **normalized-area channel** `Q − P = N_pair^10 N_quark^2 · η̄²`
  (proportional to `J_norm²` in the normalized Wolfenstein plane),
- **Perimeter channel** `P + 3Q = N_pair^8 N_quark^2 · perim_sq²`.

Together they span the (P, Q) module:
```text
P  =  ((P + 3Q) − 3(Q − P))/4  =  (perimeter-channel − 3 normalized-area-channel)/4,
Q  =  ((P + 3Q) + (Q − P))/4   =  (perimeter-channel + normalized-area-channel)/4.
```

Throughout this note, "perfect-square channel" means a scalar multiple of
one square polynomial in `alpha_s`. With the displayed structural prefactors,
each channel is a literal square over the corresponding real quadratic
coefficient field; over `Q[alpha_s]` the line classification is the
classification of scalar-multiple square channels.

**Primary runner:**
`scripts/frontier_ckm_brocard_q_polynomial_perfect_square_decomposition.py`

## Statement

The supplied NLO Wolfenstein protected-γ̄ surface admits two
fundamental quartic polynomials of `α_s`:

```text
P(alpha_s)  =  (alpha_s^2 - 4 alpha_s + 96)^2  -  240 (4 - alpha_s)^2
            =  alpha_s^4 - 8 alpha_s^3 - 32 alpha_s^2 + 1152 alpha_s + 5376.

Q(alpha_s)  =  (alpha_s^2 - 4 alpha_s + 96)^2  +  80 (4 - alpha_s)^2
            =  alpha_s^4 - 8 alpha_s^3 + 288 alpha_s^2 - 1408 alpha_s + 10496.
```

`P` is the **Brocard polynomial** (universal equilateral excess; emerged
through 9+ closed-form theorems on the supplied surface). `Q` is the
**Brocard-points denominator polynomial** (Q-P sibling theorem from the
Brocard-points branch).

```text
(D1) The pair (P, Q) generates a 2-dimensional Q-module within the ring
     of polynomials in alpha_s. A general linear combination decomposes as

       alpha P + beta Q  =  (alpha + beta) (alpha_s^2 - 4 alpha_s + 96)^2
                            + (-240 alpha + 80 beta) (4 - alpha_s)^2.

(D2) NEW scalar-multiple square decomposition (1) -- normalized-area channel:
       Q(alpha_s) - P(alpha_s)  =  N_pair^6 (N_quark - 1) (N_pair^2 - alpha_s)^2
                                  =  320 (4 - alpha_s)^2.

     This is a scalar-multiple square in (N_pair^2 - alpha_s) = (4 - alpha_s),
     with structural-integer scaling N_pair^6 (N_quark - 1) = 64 * 5 = 320.

(D3) NEW scalar-multiple square decomposition (2) -- Perimeter channel:
       P(alpha_s) + 3 Q(alpha_s)  =  N_pair^2 (alpha_s^2 - 4 alpha_s + 96)^2
                                   =  4 (alpha_s^2 - 4 alpha_s + 96)^2.

     This is a scalar-multiple square in (alpha_s^2 - 4 alpha_s + 96) = 48 perim_sq,
     with structural-integer scaling N_pair^2 = 4. Equivalently:
       P + 3Q  =  N_pair^8 N_quark^2 perim_sq^2  =  9216 perim_sq^2.

(D4) Two scalar-multiple square subspaces of the (P, Q) module:
       Line A: {(alpha, 3 alpha) : alpha in Q}  ->  P + 3Q channel,
       Line B: {(alpha, -alpha) : alpha in Q}  ->  Q - P channel.

     ALL other linear combinations alpha P + beta Q (with (alpha, beta)
     not on either line) have BOTH (alpha_s^2 - 4 alpha_s + 96)^2 and
     (4 - alpha_s)^2 components, and are therefore NOT single-square channels
     in alpha_s.

     The two lines are independent in the (alpha, beta) parameter space,
     so the scalar-multiple square-channel subset = (Line A) union (Line B), a
     1-dimensional union of two 1-D affine subspaces, including their common zero polynomial.

(D5) Normalized geometric interpretation -- normalized area vs perimeter channels:
       Q - P  =  N_pair^10 N_quark^2 eta_bar^2,
       P + 3Q  =  N_pair^8 N_quark^2 perim_sq^2.

     where:
       eta_bar  =  sqrt(5) (4 - alpha_s)/24  =  normalized area J_norm in the
                   Wolfenstein-normalized unitarity plane (J_norm = eta_bar),
       perim_sq  =  (alpha_s^2 - 4 alpha_s + 96)/48  =  a^2 + b^2 + c^2
                    of the unitarity triangle (sum of squared sides).

(D6) Cross-channel identity (NEW):
       (P + 3Q)(Q - P)  =  N_pair^8 (N_quark - 1) (alpha_s^2 - 4 alpha_s + 96)^2 (4 - alpha_s)^2
                         =  1280 (alpha_s^2 - 4 alpha_s + 96)^2 (4 - alpha_s)^2.

     The product of the two square channels is itself a scalar-multiple
     square (squared-cross-product), with structural integer 1280 = N_pair^8 (N_quark - 1).

(D7) The (P, Q) module is fully scalar-multiple-square-decomposable on the
     supplied surface:
       P  =  ((P + 3Q) - 3(Q - P)) / 4,
       Q  =  ((P + 3Q) + (Q - P)) / 4.

     The two scalar-multiple square channels span the module under linear
     combination over Q.
```

## Supplied Inputs

| Input | Source on `main` | Role |
| --- | --- | --- |
| `(rho_bar, eta_bar)` apex coordinates | [`CKM_NLO_BARRED_TRIANGLE_PROTECTED_GAMMA_THEOREM_NOTE_2026-04-25.md`](CKM_NLO_BARRED_TRIANGLE_PROTECTED_GAMMA_THEOREM_NOTE_2026-04-25.md) | supplied input |
| `N_pair = 2`, `N_color = 3`, `N_quark = 6` | [`CKM_MAGNITUDES_STRUCTURAL_COUNTS_THEOREM_NOTE_2026-04-25.md`](CKM_MAGNITUDES_STRUCTURAL_COUNTS_THEOREM_NOTE_2026-04-25.md) | supplied input |
| `rho = 1/6`, `eta = sqrt(5)/6` | [`CKM_CP_PHASE_STRUCTURAL_IDENTITY_THEOREM_NOTE_2026-04-24.md`](CKM_CP_PHASE_STRUCTURAL_IDENTITY_THEOREM_NOTE_2026-04-24.md) | supplied input |

The sources explicitly condition their own algebra on upstream inputs. Here,
counts and the NLO apex are supplied premises, and the displayed polynomial
formulas define the algebraic problem. No source Status text supplies an audit
verdict. The physical identification and upstream dependency closure remain
open obligations; no observational comparator enters these calculations.

## Derivation

### General linear combination

For any rationals `α, β`, the linear combination `α P + β Q` is

```text
alpha P + beta Q  =  alpha [(alpha_s^2 - 4 alpha_s + 96)^2 - 240 (4 - alpha_s)^2]
                     + beta [(alpha_s^2 - 4 alpha_s + 96)^2 + 80 (4 - alpha_s)^2]

                  =  (alpha + beta) (alpha_s^2 - 4 alpha_s + 96)^2
                     + (-240 alpha + 80 beta) (4 - alpha_s)^2.
```

To classify scalar multiples of polynomial squares, put `y = alpha_s - 2`,
`X = y^2 + 92`, `Y = 2 - y`, `A = alpha + beta`, and
`B = -240 alpha + 80 beta`. If `A != 0`, normalize the leading coefficient:
a scalar-square representation of `A X^2 + B Y^2` must have the form
`A (y^2 + c y + d)^2`. Its cubic coefficient forces `c = 0`. Its linear
coefficient is then zero, whereas `X^2 + (B/A)Y^2` has linear coefficient
`-4B/A`, so `B = 0`. Conversely `B = 0` is a scalar square. If `A = 0`,
`B Y^2` is a scalar square directly, including the zero polynomial at
`A = B = 0`. Thus the two lines, including their common origin, are exactly:

- **Line A**: `−240 α + 80 β = 0 ⟺ β = 3α`. Combination becomes
  `(α + 3α)(α_s² − 4α_s + 96)² = 4α (α_s² − 4α_s + 96)²`.
- **Line B**: `α + β = 0 ⟺ β = −α`. Combination becomes
  `(−240α + 80(−α))(4 − α_s)² = −320α (4 − α_s)²`.

These are the only two scalar-multiple square subspaces. Every other `(α, β)`
gives a combination with both square components, which is not itself a
single-square channel. The runner verifies this generically by coefficient
comparison against an arbitrary quadratic square, not only by testing one
off-line example.

### D2: Q − P scalar-multiple square channel (normalized-area channel)

Setting `α = −1, β = 1` in Line B:

```text
Q - P  =  (240 + 80) (4 - alpha_s)^2  =  320 (4 - alpha_s)^2.
```

In structural integers: `320 = 64 · 5 = N_pair⁶ (N_quark − 1)`. So:

```text
Q - P  =  N_pair^6 (N_quark - 1) (4 - alpha_s)^2  =  N_pair^6 (N_quark - 1) (N_pair^2 - alpha_s)^2.
```

### D3: P + 3Q scalar-multiple square channel (Perimeter channel)

Setting `α = 1, β = 3` in Line A:

```text
P + 3Q  =  4 (alpha_s^2 - 4 alpha_s + 96)^2.
```

In structural integers: `4 = N_pair²`, and using
`α_s² − 4α_s + 96 = 48 perim_sq`:

```text
P + 3Q  =  N_pair^2 (48 perim_sq)^2
        =  N_pair^2 * 2304 perim_sq^2
        =  N_pair^10 N_color^2 perim_sq^2
```

Because `N_pair² × 2304 = 4 × 2304 = 9216 = (N_pair⁴ N_quark)² = N_pair⁸ N_quark²`,

So:

```text
P + 3Q  =  N_pair^8 N_quark^2 perim_sq^2  =  (N_pair^4 N_quark perim_sq)^2.
```

This is a perfect square equal to `(N_pair⁴ N_quark × perim_sq)²` —
clean structural-integer form.

### D5: normalized geometric interpretation

The two scalar-multiple square channels are tied to **normalized CKM triangle quantities**:

- **normalized-area channel** `Q − P`: proportional to `(4 − α_s)²` and hence to
  `η̄² = 5(4 − α_s)²/576`. So `Q − P = 320(4−α_s)² = 320 × 576/5 × η̄² = 36864 η̄²`.
  In structural integers: `36864 = N_pair^10 N_quark² = 1024 × 36`. So:

  ```text
  Q - P  =  N_pair^10 N_quark^2 eta_bar^2.
  ```

  Define `J_norm = eta_bar`, twice the signed area of the unit-base
  triangle. This is not the physical Jarlskog invariant. For an exact
  unitary CKM matrix with nonzero `V_cd V_cb*` and `z_bar = -V_ud V_ub*/(V_cd V_cb*)`,
  `|J| = |V_cd V_cb*|^2 |eta_bar|`. Consequently
  `Q - P = 36864 J_norm^2 = 36864 J^2 / |V_cd V_cb*|^4`.
  This conversion requires CKM magnitudes in addition to the apex.

- **Perimeter channel** `P + 3Q`: proportional to `(α_s² − 4α_s + 96)²`
  and hence to `(48 perim_sq)²`. So:

  ```text
  P + 3Q  =  N_pair^8 N_quark^2 perim_sq^2.
  ```

These are the two **normalized geometric channels** of the (P, Q)
module on the supplied surface.

### D6: cross-channel identity

```text
(P + 3Q)(Q - P)  =  4 (alpha_s^2 - 4 alpha_s + 96)^2 × 320 (4 - alpha_s)^2
                  =  1280 (alpha_s^2 - 4 alpha_s + 96)^2 (4 - alpha_s)^2.
```

`1280 = 4 × 320 = N_pair² × N_pair⁶ (N_quark − 1) = N_pair⁸ (N_quark − 1)`.
So:

```text
(P + 3Q)(Q - P)  =  N_pair^8 (N_quark - 1) (alpha_s^2 - 4 alpha_s + 96)^2 (4 - alpha_s)^2.
```

This is a perfect square of `√(1280) (α_s² − 4α_s + 96)(4 − α_s) =
N_pair⁴ √(N_quark − 1) (α_s² − 4α_s + 96)(4 − α_s)`, since
`√(N_pair⁸) = N_pair⁴`. This displayed factor is not asserted to be
the principal square root: for real `alpha_s`, that root uses
`abs(4 - alpha_s)` because `alpha_s^2 - 4 alpha_s + 96 > 0`.

In normalized geometric terms: the cross-channel product `(P + 3Q)(Q − P) ∝ perim_sq² · η̄² = perim_sq² · J_norm²`,
i.e. proportional to the product of the **perimeter-squared and the
normalized-area squared** of the unitarity triangle.

### D7: module decomposition

From `Line A: P + 3Q = X` (perimeter channel) and `Line B: Q − P = Y` (normalized-area channel),
solving for `(P, Q)`:

```text
P + 3Q  =  X,
Q - P  =  Y.

Adding the two: P + 3Q + Q - P = X + Y => 4Q = X + Y => Q = (X + Y)/4.
Subtracting: (P + 3Q) - 3(Q - P) = X - 3Y => P + 3Q - 3Q + 3P = X - 3Y => 4P = X - 3Y => P = (X - 3Y)/4.
```

So:

```text
P  =  ((P + 3Q) - 3(Q - P)) / 4  =  (perimeter channel - 3 * normalized-area channel) / 4,
Q  =  ((P + 3Q) + (Q - P)) / 4   =  (perimeter channel + normalized-area channel) / 4.
```

This is the **inverse decomposition**. The two scalar-multiple square channels
`(X, Y) = (P + 3Q, Q − P)` form a complete basis for the (P, Q)
module, with `(P, Q)` recovered by linear combinations of `(X, Y)`.

## Numerical Verification

All identities verified via sympy:

| Identity | Form | Verified? |
| --- | --- | --- |
| D2 Q − P | `320 (4 − α_s)² = N_pair⁶ (N_quark − 1) (N_pair² − α_s)²` | sympy `simplify(diff) == 0` |
| D2 struct | `320 = N_pair⁶ (N_quark − 1)` | exact integer |
| D3 P + 3Q | `4 (α_s² − 4α_s + 96)² = N_pair² (α_s² − 4α_s + 96)²` | sympy `simplify(diff) == 0` |
| D4 Line A | `P + 3Q proportional to (α_s² − 4α_s + 96)²` | sympy exact |
| D4 Line B | `Q − P proportional to (4 − α_s)²` | sympy exact |
| D4 generic classification | coefficient comparison against an arbitrary quadratic square forces `β = 3α` or `β = −α` | sympy exact |
| D5 normalized area | `Q − P = 36864 η̄² = N_pair^10 N_quark² η̄²` | sympy `simplify(diff) == 0` |
| D5 Perimeter | `P + 3Q = 9216 perim_sq² = N_pair⁸ N_quark² perim_sq²` | sympy `simplify(diff) == 0` |
| D6 cross | `(P + 3Q)(Q − P) = 1280 (α_s²−4α_s+96)² (4−α_s)²` | sympy `simplify(diff) == 0` |
| D6 square factor | `F = N_pair⁴ √(N_quark−1) (α_s²−4α_s+96)(4−α_s)`; product `= F²` | sympy squared-identity check |
| D7 inverse P | `P = ((P+3Q) − 3(Q−P))/4` | sympy exact |
| D7 inverse Q | `Q = ((P+3Q) + (Q−P))/4` | sympy exact |

## Algebraic scope

### What this lets the framework state cleanly

The displayed polynomials are supplied algebraic inputs. This note packages
their identities without certifying the companion physical interpretations.

This note delivers:

1. **NEW scalar-multiple square decomposition** of the (P, Q) module into two
   distinct channels, each with structural-integer scaling:
   - normalized-area channel `Q − P = N_pair^10 N_quark² η̄²`,
   - Perimeter channel `P + 3Q = N_pair⁸ N_quark² perim_sq²`.

2. **NEW characterization of scalar-multiple square channels**: the
   set of `(α, β)` such that `αP + βQ` is a scalar multiple of one
   square polynomial consists of exactly two lines `(Line A: β = 3α)`
   and `(Line B: β = −α)`. All other `(α, β)` give mixed-channel
   combinations.

3. **NEW normalized geometric interpretation**: the two scalar-multiple square channels
   correspond to two specific normalized geometric quantities — normalized area squared
   and perimeter-squared — and their structural-integer scalings are
   exact powers of `N_pair, N_quark`.

4. **NEW cross-channel identity**: the product of the two channels is
   itself a scalar-multiple square of `N_pair⁴ √(N_quark − 1) (α_s² − 4α_s + 96)(4 − α_s)`.

5. **NEW module decomposition**: `P` and `Q` are recovered as linear
   combinations of the two scalar-multiple square channels:
   `P = (perimeter − 3·normalized area)/4`, `Q = (perimeter + normalized area)/4`.

### Why this counts as pushing the science forward

The Brocard polynomial `P(α_s)` and Q-polynomial `Q(α_s)` are the
**two fundamental quartic polynomials** of the supplied NLO Wolfenstein
protected-γ̄ surface. This note shows that the algebraic structure of
the (P, Q) pair has a **canonical scalar-multiple square decomposition** into
two channels, each tied to a normalized triangle quantity:

- The **normalized-area channel** `Q − P` is purely a scalar-multiple square in
  `(4 − α_s)`, proportional to `J_norm²`. This separates the normalized area from the perimeter; conversion to
  physical CP violation additionally requires CKM magnitudes.
- The **Perimeter channel** `P + 3Q` is purely a scalar-multiple square in
  `(α_s² − 4α_s + 96)`, proportional to `perim_sq²`. This decouples
  the triangle-shape magnitude from the rest.

The fact that the (P, Q) module decomposes **exactly** into these two
scalar-multiple square channels — with structural-integer scaling factors —
is a strong algebraic statement about the supplied surface. It says:
the protected-γ̄ structure forces a clean separation of the algebraic
content into "normalized area" and "sum of squared side lengths"
components, with no mixed terms when expressed in the right linear basis.

This is the **algebraic skeleton of the (P, Q) system** on the supplied
surface, complementing the Vieta structural-integer expansion of `P`
itself (companion theorem). Together they give the complete algebraic
characterization of the Brocard-polynomial / Q-polynomial pair.

### Falsifiable structural claim

The conditional identities (D2-D7) have the following scope:

```text
The supplied NLO Wolfenstein protected-γ̄ surface
  + supplied CKM_MAGNITUDES (N_pair = 2, N_color = 3, N_quark = 6)
forces:
  Q - P  =  N_pair^6 (N_quark - 1) (N_pair^2 - alpha_s)^2  (normalized-area channel),
  P + 3Q  =  N_pair^8 N_quark^2 perim_sq^2                  (Perimeter channel).

  The set of scalar-multiple square-channel linear combinations alpha P + beta Q is
  exactly the union of two lines (beta = 3 alpha) and (beta = -alpha).
```

The displayed identities hold for the displayed polynomial and apex premises.
No universal assertion is made for changed premises. In particular,
`eta_bar -> -eta_bar` preserves squared side lengths, `eta_bar^2`, and these
polynomials while reversing the signed apex direction. It therefore does not
break the two square identities.

## What This Claims

- `(D2)`: Conditional scalar-multiple square decomposition
  `Q − P = N_pair⁶ (N_quark − 1) (N_pair² − α_s)²`.
- `(D3)`: Conditional scalar-multiple square decomposition
  `P + 3Q = N_pair² (α_s² − 4α_s + 96)²`.
- `(D4)`: Conditional characterization of the two scalar-multiple square
  subspaces of the (P, Q) module.
- `(D5)`: Conditional normalized geometric interpretation: normalized-area channel
  `Q − P = N_pair^10 N_quark² η̄²`; Perimeter channel
  `P + 3Q = N_pair⁸ N_quark² perim_sq²`.
- `(D6)`: Conditional cross-channel identity
  `(P + 3Q)(Q − P) = N_pair⁸ (N_quark − 1) (α_s² − 4α_s + 96)² (4 − α_s)²`.
- `(D7)`: Conditional module decomposition: `P = (Perimeter − 3 normalized area)/4`,
  `Q = (Perimeter + normalized area)/4`.

## What This Does NOT Claim

- Does **not** modify any retained authority.
- Does **not** promote any support-tier theorem to retained.
- Does **not** cite unmerged branches as load-bearing.
- Does **not** introduce a new `d`-selector or `N_color`-selector;
  all structural integers are supplied inputs.
- Does **not** depend on any α_s-running pipeline.
- Does **not** make a direct CKM-observable claim about the (P, Q) pair;
  the scalar-multiple square channels are derived algebraic structures of the
  Brocard polynomial and the Q-polynomial.

## Reproduction

```bash
python3 scripts/frontier_ckm_brocard_q_polynomial_perfect_square_decomposition.py
```

Expected for the current supplied source inputs:

```text
TOTAL: PASS=25, FAIL=3
```

Exit code 1 records the three historical status-text failures. The conditional
symbolic identities pass; this is not a successful retention check.

The runner:

- Reads each cited authority file from disk.
- Extracts the verbatim `Status:` line and prints it as documentary metadata, not authority proof.
- Runs the preserved historical tier-text predicates, which currently fail; they do not verify retention.
- Searches the counts text for the supplied values, then uses fixed counts `(2, 3, 6)` in the algebra.
- Computes `P, Q` symbolically and verifies all six identities (D2-D7)
  by `simplify(diff) == 0` via sympy.
- Checks that off-line linear combinations are NOT single-square channels.
- Verifies the cross-channel identity and the module decomposition
  inverse relations.

## Cross-References

**Supplied-input sources (Status extraction is documentary only):**

- [`CKM_NLO_BARRED_TRIANGLE_PROTECTED_GAMMA_THEOREM_NOTE_2026-04-25.md`](CKM_NLO_BARRED_TRIANGLE_PROTECTED_GAMMA_THEOREM_NOTE_2026-04-25.md)
  — `(rho_bar, eta_bar)` apex coordinates.
- [`CKM_MAGNITUDES_STRUCTURAL_COUNTS_THEOREM_NOTE_2026-04-25.md`](CKM_MAGNITUDES_STRUCTURAL_COUNTS_THEOREM_NOTE_2026-04-25.md)
  — `N_pair = 2`, `N_color = 3`, `N_quark = 6`.
- [`CKM_CP_PHASE_STRUCTURAL_IDENTITY_THEOREM_NOTE_2026-04-24.md`](CKM_CP_PHASE_STRUCTURAL_IDENTITY_THEOREM_NOTE_2026-04-24.md)
  — `rho = 1/6`, `eta = sqrt(5)/6`.

**Companion barred-triangle closed forms (cited for context, not
load-bearing here):**

The Brocard polynomial `P(α_s)` and Q-polynomial `Q(α_s)` appear in
9+ companion closed-form theorems (Brocard angle, Symmedian/Brocard
circle, Steiner-Marden, Weitzenbock, Pedoe, Brocard points,
Napoleon, nine-point pencil, Vieta structural integers, Orthic
triangle). This note provides the scalar-multiple square decomposition of
the (P, Q) module that completes the algebraic characterization.

**NOT cited as derivation input:**

- Any support-tier note.
- Any unmerged branch.
- Any candidates-tier theorem.

## Current claim status and repair record

```yaml
actual_current_surface_status: open
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: historical status-text diagnostics fail; physical identification is not established here
source_of_blocker_text: review_loop
artifact_role: conditional algebraic support
next_trace_action: separate canonical algebra evidence from historical diagnostics and resolve the physical input bridge
reachability_to_target: conditional algebra only; physical identification and evidence separation remain open
conditional_surface_status: supplied polynomial and count premises
hypothetical_axiom_status: none introduced
admitted_observation_status: none
claim_type_reason: historical documentary diagnostics fail; conditional algebra is preserved without retained certification
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

The downstream consumer of this algebraic support is not yet identified here.
The formulas above preserve the original conditional mathematical content.
The earlier retained-closure wording is withdrawn. Historical status-text
predicates remain unchanged and their failures remain visible in the paired
cache; a Status string is not retention evidence. These open rows require a
separate decision about canonical algebra evidence and the physical input
bridge before any theorem-grade promotion. No audit outcome is prescribed.

This repair also corrects the runner's extra factor four in the side-sum
formula and labels the cross-product factor as an algebraic square factor,
not the principal root. The coefficient proof supplies the square-line
classification, and the reflection witness replaces the unsupported universal
off-surface assertion.
