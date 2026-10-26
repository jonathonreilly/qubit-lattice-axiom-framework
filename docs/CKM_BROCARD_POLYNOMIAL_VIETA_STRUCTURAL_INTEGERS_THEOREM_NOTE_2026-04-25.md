# Brocard Polynomial Vieta / Newton Structure in Pure Structural Integers

**Type:** open_gate
**Review scope:** conditional supplied algebra and the specifically reviewed comparisons;
physical interpretation, inherited authority checks, and audit status are not certified.

**Date:** 2026-04-25

Review scope: the polynomial and coefficient family below are supplied. Their
exact algebra does not establish physical pair counts or retained authority.
The companion still fails three historical status-text assertions; those
failures are preserved and are separate from its symbolic results.

**Status:** proposed_retained

This note records conditional Vieta/Newton and splitting-field identities for the supplied quartic.
The supplied counts are `(N_pair, N_color, N_quark) = (2, 3, 6)`.
The polynomial formulas and NLO apex map are premises here; neither physical
count selection nor upstream retained closure is established by this note.
The live claim remains an `open_gate` while the companion's three historical
status-text diagnostics fail. Their predicates and nonzero exit are preserved.

The headline closed forms:

```text
(V1)  P(alpha_s)  =  alpha_s^4
                     -  N_pair^3 alpha_s^3
                     -  N_pair^5 alpha_s^2
                     +  N_pair^7 N_color^2 alpha_s
                     +  N_pair^8 N_color (N_quark + 1).

(V2)  Vieta relations:
        e_1  =  +N_pair^3                       =  +8,
        e_2  =  -N_pair^5                       =  -32,
        e_3  =  -N_pair^7 N_color^2             =  -1152,
        e_4  =  +N_pair^8 N_color (N_quark + 1) =  +5376.

(V3)  Newton power sums of the four (complex) roots:
        p_1  =  N_pair^3                =  8,
        p_2  =  N_pair^7                =  128.

(V4)  STRUCTURAL FINGERPRINT (NEW):
        p_2  =  2 e_1^2.

      Equivalently:  e_2  =  -e_1^2 / 2.

      Substituting the structural-integer values of e_1 and e_2,
      this identity reduces to N_pair = 2 EXACTLY. So p_2 = 2 e_1^2 is
      a fingerprint of N_pair = 2 in the algebraic structure of P.

(V5)  Mean of the four roots = N_pair^3 / 4 = N_pair (because N_pair = 2).

(V6)  Sum of squared deviations from the mean
        =  N_pair^4 (N_quark + 1)  =  16 * 7  =  112.

(V7)  Roots over Q[sqrt(3), sqrt(5), i]:
        alpha_s^root  =  (N_pair -/+ N_pair sqrt(N_color (N_quark - 1)))
                          +/- N_pair i (sqrt(N_quark - 1) -/+ sqrt(N_color))
                      =  (2 -/+ 2 sqrt(15)) +/- 2 i (sqrt(5) -/+ sqrt(3)).

(V8)  Splitting field K = Q(sqrt(15), sqrt(-5)), [K:Q] = 4,
      Gal(K/Q) = (Z/2Z)^2, acting faithfully on the roots.
      Q(sqrt(3), sqrt(5), i) is a larger degree-eight ambient field.
```

At the supplied counts, `P(α_s)` has a
**complete pure-structural-integer expansion**, with the additional
striking property that the SECOND power sum equals **twice** the
SQUARE of the first power sum — which is uniquely satisfied at
`N_pair = 2`.

**Primary runner:**
`scripts/frontier_ckm_brocard_polynomial_vieta_structural_integers.py`

## Statement

The Brocard polynomial of the supplied NLO Wolfenstein protected-γ̄
surface is

```text
P(alpha_s)  =  (alpha_s^2 - 4 alpha_s + 96)^2  -  240 (4 - alpha_s)^2.
```

Expanded:

```text
P(alpha_s)  =  alpha_s^4  -  8 alpha_s^3  -  32 alpha_s^2
                +  1152 alpha_s  +  5376.
```

This expansion has **all five coefficients expressible in pure
structural integers** `(N_pair, N_color, N_quark)`:

```text
1     =  alpha_s^4 leading coefficient (trivially 1),
-8    =  -N_pair^3,                                    (alpha_s^3 coeff)
-32   =  -N_pair^5,                                    (alpha_s^2 coeff)
+1152 =  +N_pair^7 N_color^2,                          (alpha_s coeff)
+5376 =  +N_pair^8 N_color (N_quark + 1).              (constant)
```

So:

```text
P(alpha_s)  =  alpha_s^4  -  N_pair^3 alpha_s^3  -  N_pair^5 alpha_s^2
                +  N_pair^7 N_color^2 alpha_s  +  N_pair^8 N_color (N_quark + 1).
```

### Vieta relations on the four (complex) roots

By Vieta's formulas, for a monic quartic `α^4 + b_3 α^3 + b_2 α^2 + b_1 α + b_0`,
the elementary symmetric polynomials of the roots are:

```text
e_1  =  -b_3                   =  +N_pair^3                  =  8,
e_2  =  +b_2                   =  -N_pair^5                  =  -32,
e_3  =  -b_1                   =  -N_pair^7 N_color^2        =  -1152,
e_4  =  +b_0                   =  +N_pair^8 N_color(N_quark+1) =  +5376.
```

### Newton power sums

Using Newton's identities (`p_k = e_1 p_{k-1} - e_2 p_{k-2} + ... + (-1)^{k+1} k e_k`):

```text
p_1  =  e_1                       =  N_pair^3                 =  8,
p_2  =  e_1 p_1 - 2 e_2           =  N_pair^6 + 2 N_pair^5    =  64 + 64  =  128,
p_3  =  e_1 p_2 - e_2 p_1 + 3 e_3
     =  8 * 128 - (-32) * 8 + 3 * (-1152)
     =  1024 + 256 - 3456
     =  -2176.
```

### V4: the structural fingerprint

The `p_2 = N_pair^7 = 128` value is **special**:

```text
p_2  =  N_pair^7  =  128
2 e_1^2  =  2 * (N_pair^3)^2  =  2 N_pair^6  =  128.

So  p_2  =  2 e_1^2  EXACTLY.
```

In abstract structural-integer form (treating `N_pair` as a variable):

```text
p_2 = N_pair^6 + 2 N_pair^5,
p_2 - 2 e_1^2 = N_pair^5 (2 - N_pair).
```

For positive `N_pair`, this is **zero iff N_pair = 2** (zero is also a root without that restriction). This tests an imposed identity within the chosen coefficient family; it does not independently select the physical number of pairs. So the identity `p_2 = 2 e_1^2` is a
**fingerprint of `N_pair = 2`** in the algebraic structure of `P`.

Equivalently: `e_2 = -e_1²/2` in abstract form is `-N_pair^5 = -N_pair^6/2`,
which forces `N_pair = 2`.

### V5: mean of the roots

Mean of the four roots = `e_1/4 = N_pair^3/4 = 8/4 = 2`. In structural
integer form, `N_pair^3/4 = N_pair` (using `N_pair^2 = 4`). So the
mean of the roots equals `N_pair = 2` exactly.

### V6: algebraic squared deviations from the mean

Sum of squared deviations from the mean (in the polynomial-coefficient
sense, without complex conjugation in each square; this is not statistical variance):

```text
Sigma_i (r_i - mean)^2  =  p_2 - 2 mean p_1 + 4 mean^2
                        =  p_2 - p_1^2/4
                        =  N_pair^6 + 2 N_pair^5 - N_pair^6/4.

At N_pair = 2:
                        =  128 - 32 + 16
                        =  112
                        =  N_pair^4 (N_quark + 1)  =  16 * 7  =  112.
```

Yes: `112 = N_pair^4 (N_quark + 1)`. Clean structural-integer form.

### V7: roots over Q[√3, √5, i]

Substituting `u = 4 − α_s`, the polynomial becomes

```text
P(alpha_s = 4 - u)  =  (u^2 - 4(1 + sqrt(15)) u + 96) * (u^2 - 4(1 - sqrt(15)) u + 96).
```

`sqrt(15) = sqrt(N_color × (N_quark - 1)) = sqrt(3 × 5)` is the
**natural irrationality of the supplied surface**. Each quadratic
factor has discriminant

```text
Delta_+/-  =  16(1 +/- sqrt(15))^2 - 384  =  -128 +/- 32 sqrt(15)  <  0.
```

Both negative, so all four roots are complex. Solving each quadratic
in `u` gives

```text
u  =  2(1 +/- sqrt(15)) +/- 2i(sqrt(5) -/+ sqrt(3))

      =  2(1 +/- sqrt(N_color (N_quark - 1)))
          +/- 2i (sqrt(N_quark - 1) -/+ sqrt(N_color)).
```

So the four roots in `α_s = 4 - u` form:

```text
alpha_s^root  =  4 - u
              =  (2 -/+ 2 sqrt(15)) +/- 2i (sqrt(5) -/+ sqrt(3))

      =  (N_pair -/+ N_pair sqrt(N_color (N_quark - 1)))
          +/- N_pair i (sqrt(N_quark - 1) -/+ sqrt(N_color)).
```

### V8: Galois group

The splitting field is `K = Q(sqrt(15), sqrt(-5))`, of degree four,
with faithful Galois group `(Z/2Z)^2` (the Klein four group).
All displayed roots lie in K because `i sqrt(5) = sqrt(-5)` and
`i sqrt(3) = sqrt(15) sqrt(-5)/5`. Conversely, sums of conjugate
root pairs recover `sqrt(15)`; the two imaginary root differences
recover `sqrt(-5)`. Thus the roots generate K. The independent
square classes 15 and -5 give degree four.

The larger ambient radical field `L = Q(sqrt(3), sqrt(5), i)` has
degree eight and group `(Z/2Z)^3`. Simultaneously negating all three
generators fixes K and every root. Its root action is nonfaithful,
with kernel of order two; the quotient is Gal(K/Q), not Gal(L/Q).
The faithful Klein-four action is transitive on the roots.

## Supplied Inputs

| Input | Source on `main` | Role |
| --- | --- | --- |
| `(rho_bar, eta_bar)` apex coords | [`CKM_NLO_BARRED_TRIANGLE_PROTECTED_GAMMA_THEOREM_NOTE_2026-04-25.md`](CKM_NLO_BARRED_TRIANGLE_PROTECTED_GAMMA_THEOREM_NOTE_2026-04-25.md) | supplied input |
| `N_pair = 2`, `N_color = 3`, `N_quark = 6` | [`CKM_MAGNITUDES_STRUCTURAL_COUNTS_THEOREM_NOTE_2026-04-25.md`](CKM_MAGNITUDES_STRUCTURAL_COUNTS_THEOREM_NOTE_2026-04-25.md) | supplied input |
| `rho = 1/6`, `eta = sqrt(5)/6` | [`CKM_CP_PHASE_STRUCTURAL_IDENTITY_THEOREM_NOTE_2026-04-24.md`](CKM_CP_PHASE_STRUCTURAL_IDENTITY_THEOREM_NOTE_2026-04-24.md) | supplied input |

The sources explicitly condition their own algebra on upstream inputs. Here,
counts and the NLO apex are supplied premises, and the displayed polynomial
formulas define the algebraic problem. No source Status text supplies an audit
verdict. The physical identification and upstream dependency closure remain
open obligations; no observational comparator enters these calculations.

## Numerical Verification

All identities verified via sympy:

| Identity | Form | Verified? |
| --- | --- | --- |
| V1 leading | `1` | trivial |
| V1 α_s³ coeff | `−N_pair³ = −8` | exact integer |
| V1 α_s² coeff | `−N_pair⁵ = −32` | exact integer |
| V1 α_s coeff | `+N_pair⁷ N_color² = +1152` | exact integer |
| V1 const | `+N_pair⁸ N_color(N_quark+1) = +5376` | exact integer |
| V1 polynomial | `P(α_s)` matches structural form | sympy `simplify(diff) == 0` |
| V2 e_1 | `+N_pair³` | `sum(roots) == 8` |
| V2 e_2 | `−N_pair⁵` | exact |
| V2 e_3 | `−N_pair⁷N_color²` | exact |
| V2 e_4 | `+N_pair⁸N_color(N_quark+1)` | exact |
| V3 p_1 | `N_pair³ = 8` | sympy exact |
| V3 p_2 | `N_pair⁷ = 128` | sympy exact |
| V3 p_3 Newton | `e_1 p_2 − e_2 p_1 + 3 e_3` | sympy exact |
| V4 fingerprint | `p_2 = 2 e_1²` | sympy exact |
| V4 abstract | `e_2 = −e_1²/2 ⟺ N_pair = 2` | symbolic solve |
| V5 mean | `N_pair = 2` | sympy exact |
| V6 variance | `N_pair⁴(N_quark+1) = 112` | sympy exact |
| V7 factoring | `P` over `Q[√15]` | sympy exact |
| V7 disc | both quadratic discriminants `< 0` | numerical |
| V8 Galois | degree-four splitting field with faithful Klein-4 action | exact root-action check |
| V9 Disc(P) | `> 0` (4 complex roots) | sympy `discriminant > 0` |

## Algebraic scope

### What this lets the framework state cleanly

The displayed polynomials are supplied algebraic inputs. This note packages
their identities without certifying the companion physical interpretations.

This note delivers:

1. **NEW pure-structural-integer expansion** (V1): all five
   coefficients of `P(α_s)` expressed entirely in terms of
   `(N_pair, N_color, N_quark)`. No floating constants.

2. **NEW Vieta relations in structural integers** (V2): the four
   elementary symmetric polynomials of the roots have the form

   `(+N_pair³, −N_pair⁵, −N_pair⁷ N_color², +N_pair⁸ N_color(N_quark + 1))`.

3. **NEW structural fingerprint** (V4): the identity `p_2 = 2 e_1²`
   uniquely forces `N_pair = 2`. This is the **algebraic signature
   within the supplied coefficient family** in the Brocard polynomial.

4. **NEW root-statistics in structural integers** (V5, V6):
   - Mean of roots = `N_pair = 2`.
   - Sum of squared deviations from mean = `N_pair⁴(N_quark + 1) = 112`.

5. **NEW root-form in structural integers** (V7): each of the four
   complex roots involves `√(N_color (N_quark − 1))`, `√(N_quark − 1)`,
   and `√N_color` — the natural irrationals of the supplied surface.

6. **NEW Galois-group structure** (V8): the splitting field has
   `(Z/2Z)²` Galois group over `Q`, acting faithfully on the roots.
   The degree-eight ambient radical field has a nonfaithful root action.

### Why this counts as pushing the science forward

The Brocard polynomial `P(α_s)` has emerged through a series of
companion theorems as the **universal algebraic invariant** of the
supplied NLO Wolfenstein protected-γ̄ surface, controlling six
classical equilateral conditions (Brocard inequality, Weitzenbock,
Steiner inellipse circular limit, Marden foci coincidence, Pedoe
similarity-deficit metric, Napoleon side² product). This note shows
that **all of P's algebraic content — coefficients, Vieta relations,
power sums, root structure, Galois group — is in pure structural
integers `(N_pair, N_color, N_quark)`**.

The most striking result is the **structural fingerprint** (V4):
the identity `p_2 = 2 e_1²` (sum of squared roots = twice squared
sum of roots) is **uniquely forced by `N_pair = 2`**. For any other positive
value of `N_pair`, the abstract Vieta relation
`e_2 = −e_1²/2 ⟺ −N_pair⁵ = −N_pair⁶/2` would fail. So `N_pair = 2`
is **algebraically encoded** in the second power sum of the
Brocard polynomial — independently of any geometric interpretation.

This is **algebraic rigidity at the level of polynomial structure**.
The framework's `N_pair = 2` is not just a counted-pair structural
integer — it is the unique value that makes the Brocard polynomial
satisfy `p_2 = 2 e_1²`. Within this supplied coefficient family and for positive `N_pair`, imposing
`p_2 = 2 e_1²` forces `N_pair = 2`. No statement about arbitrary revised
coefficient families follows.

### Falsifiable structural claim

The conditional identities (V1-V8) have the following scope:

```text
The supplied NLO Wolfenstein protected-γ̄ surface
  + supplied CKM_MAGNITUDES (N_pair = 2, N_color = 3, N_quark = 6)
forces:
  P(alpha_s) = alpha_s^4
               - N_pair^3 alpha_s^3
               - N_pair^5 alpha_s^2
               + N_pair^7 N_color^2 alpha_s
               + N_pair^8 N_color (N_quark + 1).

  p_2 = 2 e_1^2  (signature of N_pair = 2).
  Mean of roots = N_pair = 2.
  Algebraic squared-deviation sum = N_pair^4 (N_quark + 1) = 112.
```

Changing the supplied coefficient family can change P. The fingerprint
residual depends only on N_pair, so changes to N_color or N_quark alone
do not break that identity. It is a conditional algebraic relation, not
a physical count-selection theorem.

## What This Claims

- `(V1)`: Conditional expansion of the Brocard polynomial in pure
  structural integers (5 coefficients).
- `(V2)`: Conditional Vieta relations on the four roots in pure
  structural integers.
- `(V3)`: Conditional Newton power sums `p_1, p_2, p_3, p_4`.
- `(V4)`: Conditional STRUCTURAL FINGERPRINT `p_2 = 2 e_1²`,
  which uniquely forces `N_pair = 2`.
- `(V5)`: Conditional mean-of-roots identity `mean = N_pair = 2`.
- `(V6)`: Conditional squared-deviation identity = `N_pair⁴ (N_quark + 1)`.
- `(V7)`: Conditional root form in structural irrationals
  `√(N_color(N_quark-1)), √(N_quark-1), √N_color`.
- `(V8)`: NEW classification of the Galois group of the splitting
  field as `(Z/2Z)²` with faithful Klein-4 root action.

## What This Does NOT Claim

- Does **not** modify any retained authority.
- Does **not** promote any support-tier theorem to retained.
- Does **not** cite unmerged branches as load-bearing.
- Does **not** introduce a new `d`-selector or `N_color`-selector;
  all structural integers are supplied inputs. The fingerprint
  `p_2 = 2 e_1²` algebraically forces `N_pair = 2` GIVEN the form
  of `P(α_s)`, not as an independent constraint on the framework.
- Does **not** depend on any α_s-running pipeline.
- Does **not** make a direct CKM-observable claim about the
  Brocard polynomial; its observable consequences flow through
  the companion theorems (Brocard angle, Weitzenbock, Steiner,
  Marden, Pedoe, Napoleon, Brocard points, nine-point pencil).

## Reproduction

```bash
python3 scripts/frontier_ckm_brocard_polynomial_vieta_structural_integers.py
```

Historical expected count was 26/0. The reviewed execution is 28 PASS /
3 FAIL (three upstream status-text assertions); symbolic checks pass.
A source Status line is not a retention certificate.

The runner:

- Reads each cited authority file from disk.
- Extracts the verbatim `Status:` line and prints it as documentary metadata, not authority proof.
- Runs the preserved historical tier-text predicates, which currently fail; they do not verify retention.
- Searches the counts text for the supplied values, then uses fixed counts `(2, 3, 6)` in the algebra.
- Computes the structural-integer expansion of `P(α_s)` and matches
  against the explicit form by `simplify(diff) == 0`.
- Solves `P(α_s) = 0` symbolically via sympy and computes Vieta
  relations and Newton power sums.
- Verifies the structural fingerprint `p_2 = 2 e_1²` exactly.
- Symbolically verifies the abstract identity
  `e_2 = -e_1²/2 ⟺ N_pair = 2`.
- Verifies factorization over `Q[√15]` and computes discriminants of
  each quadratic factor.

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

- The Brocard polynomial appears in 6+ closed forms across the
  Brocard-angle, Symmedian/Brocard-circle, Steiner-Marden, Weitzenbock,
  Pedoe, Brocard-points, Napoleon-triangles, and Nine-point-pencil
  branches. This note packages the polynomial's algebraic skeleton.

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
