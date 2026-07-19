---
claim_id: theta_post_erasure_odd_side_log_equivalence_and_additivity_incompatibility_bounded_theorem_note_2026-07-18
claim_type: bounded_theorem
claim_scope: "Bridge-conditional exact mathematics on a supplied phase-erased determinant-modulus surface. For a fixed strictly positive F on the full positive multiplicative group, block multiplicativity is equivalent to additivity of G(u)=log F(e^u); only with the additional explicit premise that G is bounded on an interval of positive length does the rebuilt support theorem give G(u)=su and F(x)=x^s. Separately, a fixed nonnegative F satisfying the scalar product-to-sum equation F(xy)=F(x)+F(y) on the full positive group is identically zero, but that equation is not Record finite additivity and is not either route-local condition of the landed parent. Finally, an explicit pair of continuous, single-valued, K-even, unit-modulus complex readouts has identical log-modulus data but different phases and different multiplicativity, proving noninjectivity only on that stated pre-erasure class. No physical readout, carrier, cross-sector transport, exhaustion, mass orientation, gauge theta, or theta-bar closure is derived."
upstream_dependencies:
  - bounded_additive_on_interval_linearity_rebuilt_support_note_2026-07-18
  - theta_cross_sector_determinant_forcing_property_characterization_bounded_theorem_note_2026-07-17
  - theta_p2_k_cpt_determinant_character_phase_erasure_bounded_note_2026-06-10
  - registrable_readout_additive_even_phase_free_narrow_theorem_note_2026-06-10
  - registrable_readout_determinant_character_algebraic_core_split_note_2026-06-18
runner: scripts/theta_post_erasure_odd_side_log_equivalence_and_additivity_incompatibility_2026_07_18.py
---

# Theta Post-Erasure Structure: Log Equivalence, A Conditional Scalar Law, And A Non-Reconstruction Example

**Date:** 2026-07-18
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** conditional algebra on supplied function classes. No class below is
adopted as framework content or identified with a physical quark readout.
**Audit-status authority:** independent audit lane only. This note sets no audit
verdict and predicts none.
**Primitive status:** no primitive is approved, registered, edited, or enlarged
here.
**Primary runner:**
[`scripts/theta_post_erasure_odd_side_log_equivalence_and_additivity_incompatibility_2026_07_18.py`](../scripts/theta_post_erasure_odd_side_log_equivalence_and_additivity_incompatibility_2026_07_18.py)
**Runner cache:**
[`logs/runner-cache/theta_post_erasure_odd_side_log_equivalence_and_additivity_incompatibility_2026_07_18.txt`](../logs/runner-cache/theta_post_erasure_odd_side_log_equivalence_and_additivity_incompatibility_2026_07_18.txt)

## Purpose And Parent Boundary

The current parent
[`THETA_CROSS_SECTOR_DETERMINANT_FORCING_PROPERTY_CHARACTERIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md`](THETA_CROSS_SECTOR_DETERMINANT_FORCING_PROPERTY_CHARACTERIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md)
isolates two route-specific forcing pairs:

1. supplied conjugate-pair cancellation plus `K`/CPT orbit constancy for a
   real scalar phase functional; and
2. a supplied continuous determinant-character law plus `K`/CPT orbit
   constancy.

The first route's cancellation normalization is not a consequence of Record
finite additivity, and it is not a scalar equation on products of positive
numbers. This note does not alter or eliminate that route. It studies the
positive-modulus coordinate of the second route after the conditional
[`phase-erasure result`](THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md)
has restricted the supplied character class to `k = 0`. It also records an
elementary product-to-sum lemma because conflating that equation with genuine
Record finite additivity would be an error. The
[`registrable-readout theorem`](REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md)
and its
[`algebraic-core split`](REGISTRABLE_READOUT_DETERMINANT_CHARACTER_ALGEBRAIC_CORE_SPLIT_NOTE_2026-06-18.md)
make the same premise separation.

## Supplied Mathematical Surface

Let a nonzero determinant block have modulus `x in (0, infinity)`. Independent
block composition supplies multiplication `x, y -> x y`. A fixed modulus
readout is a function `F : (0, infinity) -> [0, infinity)`. The following
conditions are separate:

- **(P-hom)** `F(x y) = F(x) F(y)` for all positive `x, y`.
- **(P-log)** for strictly positive `F`, the coordinate function
  `G(u) = log F(e^u)` obeys `G(u+v) = G(u)+G(v)` for all real `u, v`.
- **(P-bdd)** there exist real `a`, `L > 0`, and `B >= 0` such that
  `|G(w)| <= B` for every `w in [a,a+L]`.
- **(P-scalar)** `F(x y) = F(x)+F(y)` for all positive `x, y`.

`(P-scalar)` is an independent algebraic hypothesis. It is not the parent's
conjugate-pair-cancellation condition and is not the Record axiom's finite
additivity over pairwise-disjoint record collections.

If a nonnegative multiplicative `F` vanishes at one `x_0`, then
`F(x)=F(x_0)F(x/x_0)=0` for every `x`. Otherwise it is strictly positive and
`G` is defined. Also, `F(1)=F(1)^2`, so a nonzero multiplicative function has
`F(1)=1`.

## Exact Results

### T1 — Log equivalence and the separately supplied regularity premise

For strictly positive `F`, `(P-hom)` holds if and only if `(P-log)` holds. If
`F` is multiplicative, taking logarithms gives

```text
G(u+v) = log F(e^(u+v)) = log(F(e^u)F(e^v)) = G(u)+G(v).
```

Conversely, if `G` is additive, writing `x=e^u`, `y=e^v` and exponentiating
gives `F(xy)=F(x)F(y)`.

This equivalence alone does **not** force a power law: discontinuous additive
functions exist, and `F(x)=exp(A(log x))` is multiplicative for any additive
`A`. If `(P-bdd)` is additionally supplied, the
[`rebuilt bounded-additive support theorem`](BOUNDED_ADDITIVE_ON_INTERVAL_LINEARITY_REBUILT_SUPPORT_NOTE_2026-07-18.md)
applies to `G` and gives `G(u)=s u`, where `s=G(1)`. Therefore and only under
that added regularity premise, `F(x)=x^s`.

### T2 — Conditional scalar product-to-sum degeneracy

Let a fixed `F : (0,infinity) -> [0,infinity)` obey `(P-scalar)` on the full
positive multiplicative group. Setting `x=y=1` gives
`F(1)=2F(1)`, hence `F(1)=0`. For arbitrary `x>0`,

```text
F(x)+F(1/x)=F(1)=0.
```

Both summands are nonnegative, so `F(x)=0`. Thus `(P-scalar)` has only the zero
solution on this exact domain. Conversely, `(P-hom)` does not imply
`(P-scalar)`: `F(x)=x` is multiplicative, while
`F(2*3)=6 != 5=F(2)+F(3)`.

This is a standalone conditional function equation. It does not say that
Record finite additivity, conjugate-pair cancellation, or any physical readout
satisfies `(P-scalar)`, and therefore it does not remove either forcing pair in
the current parent.

### T3 — Narrow log-modulus non-reconstruction example

On `C^x`, define

```text
r_flat(z) = 1,
r_twist(z) = exp(i (1 - Re(z)/|z|)).
```

Both readouts are continuous, single-valued, `K`-even under complex
conjugation, and have unit modulus, so their logarithmic modulus is identically
zero. They nevertheless have different phases at `z=i`:
`r_flat(i)=1` and `r_twist(i)=e^i`. The flat readout is multiplicative, whereas
at the pair `(i,-i)`:

```text
r_twist(i*(-i)) = r_twist(1) = 1,
r_twist(i) r_twist(-i) = e^(2i) != 1.
```

Hence the map from this stated class of complex readouts to log-modulus data is
not injective, and log-modulus data alone does not determine the full complex
block law on this class. This is not a claim about strictly positive readouts,
the fixed `k=0` power family, or data augmented by a phase index or cocycle.

### T4 — Interaction with the current parent

The parent determinant-character route remains exactly the supplied continuous
character law plus orbit constancy. T1 only re-expresses its strictly positive
modulus coordinate and classifies that coordinate if `(P-bdd)` is supplied.
The parent's conjugate-pair-cancellation route is untouched by T2. T3 only
records information loss before one restricts to the phase-erased character
class.

The physical carrier, quark readout map, cross-sector correspondence,
exhaustion statement, mass orientation, gauge-side theta, and
`theta_bar = theta_gauge + arg det(M_u M_d)` remain open.

## No-Go Discipline Gate

T2 and T3 contain narrow negative consequences. They are stress-tested
separately below. Every N1 route is marked `ATTEMPTED`; no route is assigned
premise weight from a prior audit verdict.

### N1 — Five attacks on T2

| attack route | exact attempted construction and disposition | marker |
|---|---|---|
| Drop nonnegativity | `F(x)=log x` is a nonzero signed solution of `(P-scalar)` on the full group. It exits the nonnegative codomain and proves that premise essential. | ATTEMPTED |
| Remove inverses by restricting the domain | On the multiplicative submonoid `[1,infinity)`, `F(x)=log x >= 0` is nonzero and obeys the equation. It exits the stated full-group domain. | ATTEMPTED |
| Use genuine Record finite additivity | `I(C)=|C|` is nonzero and additive on finite disjoint record collections. It does not induce `F(xy)=F(x)+F(y)`, confirming that no Record/product bridge is available from additivity alone. | ATTEMPTED |
| Shift the composition baseline | For `c>0`, the constant `F(x)=c` obeys `F(xy)=F(x)+F(y)-c`. It exits the exact normalization in `(P-scalar)`. | ATTEMPTED |
| Retain only sparse product support | On the tested relation `{2,3,6}`, values `F(2)=F(3)=1`, `F(6)=2` are nonnegative and nonzero. The set lacks the identity and inverse closure used by the theorem. | ATTEMPTED |

These attacks defeat broader versions of T2 and are the reason the result is
restricted to a fixed nonnegative function, the exact unshifted equation, and
the full positive group.

### N1 — Five attacks on T3

| attack route | exact attempted construction and disposition | marker |
|---|---|---|
| Restrict to strictly positive readouts | Then `log|r|=log r` reconstructs `r` pointwise. This is outside the complex phase-bearing class of T3. | ATTEMPTED |
| Restrict to the bounded `k=0` power class | Under T1 plus `(P-bdd)`, log-modulus determines the slope `s` and hence `F(x)=x^s`. This is an explicit partial closure, not a refutation of the broad-class discriminator. | ATTEMPTED |
| Supply the winding index | Inside the continuous character class, log-modulus together with the integer `k` reconstructs `|z|^s exp(i k arg z)`. The extra phase datum is absent from T3. | ATTEMPTED |
| Supply the phase-cocycle defect | The defect `arg(r(z_1z_2)/(r(z_1)r(z_2)))` decides full-complex multiplicativity even without reconstructing pointwise phase. It is additional data. | ATTEMPTED |
| Weaken the target to modulus multiplicativity | Equality of `log|r(z_1z_2)|` with the sum of the two input log moduli decides the modulus-only law. T3 concerns the full complex law. | ATTEMPTED |

### N2 — Independence and collapse audit

For T2, the raw assumptions collapse to three premises: `(D)` the full group
domain, `(N)` nonnegativity, and `(E)` the exact unshifted product-to-sum
equation. “Fixed single-variable function” is syntax of `(E)`, not a fourth
independent wall.

| pair | does the first imply the second? | does the second imply the first? | independent? |
|---|---|---|---|
| `D`, `N` | no: `log x` is signed on the full group | no: `log x` is nonnegative on `[1,infinity)` without inverse closure | yes |
| `D`, `E` | no: `F(x)=x` is defined on the full group but fails `E` | no: `log x` obeys `E` on `[1,infinity)` | yes |
| `N`, `E` | no: `F(x)=x` is nonnegative but fails `E` | no: signed `log x` obeys `E` | yes |

For T3, “unknown phase” and “unknown full complex block law” are not counted as
two independent walls. Supplying the full phase together with the modulus
reconstructs the readout and permits testing its law; conversely, supplying
only the phase-cocycle defect can decide the law without reconstructing the
phase. They are two consequences of one information-loss boundary, with a
one-way closure relation.

### N3 — Hidden-condition scan

| wording scanned | classification |
|---|---|
| “supplied mathematical surface” | explicit non-satisfying condition; no framework adoption |
| “independent block composition” | explicit determinant multiplication law; not inferred from Record |
| “strictly positive” | explicit domain condition for the logarithm |
| “bounded” | explicit `(P-bdd)` premise with interval, positive length, and bound |
| “phase-erased” / `k=0` | conditional result inside the cited determinant-character class, not physical exhaustion |
| “Record” / “registrable” | context used to separate laws; no direct Record premise is consumed by T1–T3 |

No appeal to “standard,” “natural,” “canonical,” background QFT, or a hidden
bridge supplies a theorem premise.

### N4 — Residual matching

| cited source | source residual | residual used here | match? |
|---|---|---|---|
| [`THETA_CROSS_SECTOR_DETERMINANT_FORCING_PROPERTY_CHARACTERIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md`](THETA_CROSS_SECTOR_DETERMINANT_FORCING_PROPERTY_CHARACTERIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md), lines 61–89 and 138–150 | two route-specific supplied pairs; physical carrier/readout/correspondence open | parent scope only; neither route is removed | yes |
| [`THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md`](THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md), lines 24–65 | `k=0` only inside a supplied continuous character class; evenness alone is insufficient | conditional post-erasure character surface only | yes |
| [`REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md`](REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md), lines 44–83 and 138–153 | Record finite additivity is distinct from phase-group homomorphism | `(P-scalar)` is explicitly not Record additivity | yes |
| [`BOUNDED_ADDITIVE_ON_INTERVAL_LINEARITY_REBUILT_SUPPORT_NOTE_2026-07-18.md`](BOUNDED_ADDITIVE_ON_INTERVAL_LINEARITY_REBUILT_SUPPORT_NOTE_2026-07-18.md), statement and proof | additive `G` is linear only with a positive-length interval bound | power classification uses explicit `(P-bdd)` | yes |
| [`REGISTRABLE_READOUT_DETERMINANT_CHARACTER_ALGEBRAIC_CORE_SPLIT_NOTE_2026-06-18.md`](REGISTRABLE_READOUT_DETERMINANT_CHARACTER_ALGEBRAIC_CORE_SPLIT_NOTE_2026-06-18.md), lines 26–83 | homomorphism and orbit structure are supplied separately from Record | premise separation and no physical closure | yes |

### N5 — Rhetoric and resolution audit

| statement | tested resolution | resolutions not claimed |
|---|---|---|
| T2 zero-solution result | one fixed scalar function on every element of the full positive group, using identity and inverse | disjoint-record unions, determinant sectors, physical blocks, modes, sites, and lattices |
| `(P-scalar)` is not Record finite additivity | exact interface comparison: scalar multiplication versus finite disjoint union | no claim that every possible bridge between interfaces is impossible |
| T3 noninjectivity | pointwise on `C^x` plus one exact two-block composition pair | physical carrier, mode, site, lattice, action, or exhaustion statements |

Accordingly, the note says “on this exact function class” and “log-modulus
alone,” never “no route exists” or “the framework cannot derive” the physical
result.

### N6 — Partial-closure paths

| candidate path | what it closes | classification here |
|---|---|---|
| Prove a Record-to-product-scalar bridge | would make T2 relevant to a named readout, without changing its algebra | separate bridge theorem; not supplied or foreclosed |
| Re-express the multiplicative readout as `G=log F` | supplies a viable additive coordinate law | T1 exact reframe; no new axiom |
| Supply `(P-bdd)` | classifies the additive coordinate as linear | explicit bounded theorem input; independent audit still required |
| Restrict to positive or fixed `k=0` readouts | closes T3 pointwise reconstruction | honest class restriction |
| Supply winding or phase-cocycle data | closes phase reconstruction or law testing | additional observable data, not silently assumed |

No statement says a new axiom is required. Existing or future bridge, class,
and information augmentations remain live.

### N7 — Strongest hostile steelmen

**Against an overbroad T2 reading.** Record finite additivity concerns disjoint
record unions, whereas `(P-scalar)` concerns multiplication of positive channel
values. The current parent deliberately separates conjugate-pair cancellation
from the determinant-character law. Therefore the scalar lemma cannot demote
the parent cancellation route or say anything physical about Record without a
new interface theorem. **Disposition:** accepted in full; T2 is retained only
as a standalone conditional equation, and the parent-facing elimination claim
is withdrawn.

**Against an overbroad T3 reading.** On strictly positive readouts, or on the
bounded `k=0` power class, log-modulus does reconstruct the readout; with a
winding index or phase-cocycle it can also settle phase or multiplicativity.
Therefore no universal information-theoretic obstruction exists.
**Disposition:** accepted in full; T3 claims only noninjectivity on the stated
unrestricted complex class, witnessed by two explicit regular readouts.

### N8 — Cross-cycle echo

The prescribed current-tree search found 44 documents with broad wall-shaped
phrasing and 74 `NO_GO_LEDGER.md` files. The relevant echoes were inspected:

| prior artifact | later/narrowing mechanism | application here |
|---|---|---|
| current cross-sector parent | a global property-set claim was narrowed to two route-specific forcing pairs | do not map `(P-scalar)` onto the cancellation route |
| determinant-character algebraic-core split | separate exact homomorphism algebra from physical readout identification | keep T1 mathematical and T4 physically open |
| `registrability-bridges-20260610/NO_GO_LEDGER.md` | K/CPT evenness alone was rejected using a phase-dependent cosine witness | retain the explicit character-class boundary |
| `tier-a-elimination-block08-theta-mass/NO_GO_LEDGER.md` | updated axioms were refused as a determinant-channel bridge | do not treat Record or this note as carrier/readout authority |

The same premise-separation mechanism is applied here. No similar retired wall
was found that licenses physical closure.

**No-Go Discipline status:** PASS for the two narrowly stated consequences;
the broader parent-facing and universal-impossibility readings are explicitly
withdrawn.

## Non-Claims

- Does **not** derive a physical quark readout, registrability, orbit transport,
  carrier, cross-sector correspondence, or exhaustion theorem.
- Does **not** identify `(P-scalar)` with Record finite additivity or
  conjugate-pair cancellation.
- Does **not** infer a power family without the explicit `(P-bdd)` premise.
- Does **not** claim that log-modulus fails to reconstruct on every restricted
  class or after phase/cocycle data are supplied.
- Does **not** touch gauge-side theta, theta-bar, or an action-level bare slot.
- Does **not** set an audit verdict; both new claim IDs enter independent audit
  as unaudited.

## Verification

The primary runner uses exact SymPy arithmetic in one process. It checks the
exponential/log bridge, representative power-family consistency, the explicit
boundedness/source needles, multiplicative degeneracy, the two-step T2 proof,
the `6 != 5` converse witness, all five T2 boundary attacks, the continuous
K-even T3 discriminator at exact points, representative T3 partial closures,
and source needles against the current parent, phase-erasure note,
registrability note, and rebuilt support theorem. These are exact finite checks
and source guards, not a replacement for the written universal proofs.

Measured runner total after final verification is recorded in the paired
cache.
