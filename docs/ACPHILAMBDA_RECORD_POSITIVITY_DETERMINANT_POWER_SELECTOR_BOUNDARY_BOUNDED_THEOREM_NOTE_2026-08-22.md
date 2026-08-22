---
claim_id: acphilambda_record_positivity_determinant_power_selector_boundary_bounded_theorem_note_2026-08-22
claim_type: bounded_theorem
claim_scope: "On the declared phase-complete scalar-determinant surface, a real-linear map from C into positive Hermitian blocks is zero. An entrywise-holomorphic F:Omega->M_d(C) on a connected open complex domain whose image is Hermitian is constant, and is zero if 0 is in Omega and F(0)=0. For fixed rho>=0 and nonzero A_0 with Tr(A_0 rho A_0^dagger)>0, the branch-operator typing A_z=zA_0 gives sigma_z=|z|^2 sigma_1 and squared-modulus trace ratios. A nonzero positive modulus-power-one construction must leave at least one of those direct-map or scalar-amplitude hypotheses; named examples are explicitly non-exhaustive. For separately supplied additive positive blocks, coarse addition preserves the supplied fine-block calibration, while event-label cardinality alone fixes no factor. These finite facts expose independent physical typing, trace/probability, and event-calibration bridges; they do not select the charged-lepton action, measure, event carrier, determinant horn, r value, or a universal no-go."
depends_on:
  - minimal_axioms
runner: scripts/acphilambda_record_positivity_determinant_power_selector_boundary_2026_08_22.py
runner_cache: logs/runner-cache/acphilambda_record_positivity_determinant_power_selector_boundary_2026_08_22.txt
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Positive Blocks and the AC Determinant-Power Selector Boundary

**Date:** 2026-08-22

**Role:** bounded action/measure typing probe after the provisional finite
Record-law candidate

**Claim type:** bounded_theorem

**Primary runner:**
[`scripts/acphilambda_record_positivity_determinant_power_selector_boundary_2026_08_22.py`](../scripts/acphilambda_record_positivity_determinant_power_selector_boundary_2026_08_22.py)

**Cached receipt:**
[`logs/runner-cache/acphilambda_record_positivity_determinant_power_selector_boundary_2026_08_22.txt`](../logs/runner-cache/acphilambda_record_positivity_determinant_power_selector_boundary_2026_08_22.txt)

## Result up front

This probe narrows, but does not retire, the charged-lepton
count-once/count-twice fork. Let

```text
z = det_C(K).
```

Three determinant typings must be kept distinct.

1. **Direct positive block.** A nonzero real-linear map from a
   phase-complete complex `z` domain into positive Hermitian blocks is
   impossible. More generally, an entrywise-holomorphic matrix map on a
   connected open complex domain whose image is Hermitian is constant. It is
   zero when the domain contains zero and the zero determinant must map to the
   zero block.
2. **Scalar branch amplitude.** If `A_z=z A_0`, then branch-operator algebra
   gives

   ```text
   sigma_z = A_z rho A_z^dagger = |z|^2 sigma_1,
   Tr(sigma_z) = |z|^2 Tr(sigma_1).
   ```

   This establishes a squared-modulus branch-block and trace factor. It does
   not by itself identify that factor with physical probability or with the
   realified/conjugate-paired AC action horn.
3. **Positive modulus-power-one construction.** A supplied positive
   determinant ray, a direct modulus weight, or a square-root writer
   `A_z=sqrt(|z|)A_0` can produce modulus power one. These routes leave the
   real-linear/holomorphic direct-map or standard scalar-amplitude hypotheses.
   They are examples, not an exhaustive list of physical constructions.

Supplied event calibration is a separate axis. If two fine positive blocks
are assigned traces `w,w`, their sum has trace `2w`. If a coarse block of
trace `w` is instead refined into calibrated blocks with traces `w/2,w/2`,
their sum remains `w`. Thus coarse addition preserves the calibration already
supplied; the number of event labels does not create a factor. In particular,
an event quotient or rescaling can change a multiplicity factor but cannot by
itself turn the determinant exponent `|z|^2` into `|z|`.

The AC residual therefore has three independent physical interfaces:

- `W_T`: which action/measure or amplitude **typing** the determinant has;
- `W_P`: which downstream law, if any, turns a branch trace or statistical
  measure into physical probability;
- `W_E`: which K/CPT alternatives are physical events and how their fine
  blocks are calibrated.

The current Minimal Axioms supply none of these choices. This packet makes no
minimal-axiom edit and retires no TOE obligation.

## 1. Exact supplied surface

The theorem uses only the following finite objects and assumptions.

- `K` is a finite complex matrix and `z=det_C(K)`.
- The exact real-linear test surface contains the rank-one kernels `[1]`,
  `[-1]`, `[i]`, and `[-i]`; `det([z])=z`.
- A supplied branch block is a positive semidefinite finite matrix `sigma`.
  Its trace is a candidate mathematical weight, not an axiomatically supplied
  probability.
- For the amplitude identity, `rho>=0`, `A_0` is nonzero, and
  `A_z=zA_0`. Ratios require `Tr(sigma_1)>0`.
- For the holomorphic identity, `Omega` is connected and open and
  `F:Omega->M_d(C)` is entrywise holomorphic with Hermitian image. The zero
  conclusion additionally requires `0 in Omega` and `F(0)=0`.
- For the coarse-block identity, positive fine blocks and their additive
  coarse block are supplied theorem-domain data. Their physical event meaning
  and normalization are not inferred from label cardinality.

The branch identity itself does not assert that an arbitrary `A_z` family is
a complete or trace-nonincreasing instrument. The runner also supplies one
exact `c=1/9` fixture with positive completion so the displayed conditional
ratios occur inside a valid finite instrument.

The only determinant identity consumed is `det([z])=z`, reproved by the
runner. Two older sources are non-load-bearing consistency context:
`ACPHILAMBDA_OCCUPANCY_DETERMINANT_POWER_SPLIT_EXACT_SUPPORT_NOTE_2026-07-04.md`
and
`ACPHILAMBDA_FERMIONIC_REALIFICATION_PFAFFIAN_POWER_IDENTITY_NARROW_THEOREM_NOTE_2026-07-12.md`.
The latter warns that a complex-to-Majorana coordinate rewrite does not itself
add an independent conjugate physical carrier. Neither source proves the
present lemmas and neither is a dependency edge.

The current [Minimal Axioms](MINIMAL_AXIOMS_2026-06-29.md) supply a local
probability-distribution slot and fixed Records while leaving distribution
values, source/action, measurement/event calibration, Born weights, and
physical-observable identification downstream. The August 13 revision also
removed finite additivity from Record. Therefore positive blocks, trace
weighting, and coarse additivity below are explicit theorem hypotheses, not
Record content.

## 2. Phase-complete linear and holomorphic maps

Let `B:C->Herm(H)` be real-linear and suppose `B(z)>=0` at both `z` and `-z`.
Real linearity gives `B(-z)=-B(z)`. Both `B(z)` and `-B(z)` are positive
semidefinite, so for every vector `v`,

```text
0 <= v^dagger B(z) v <= 0.
```

Every quadratic form vanishes and polarization gives `B(z)=0`. Applying this
at the `+/-1` and `+/-i` fixtures makes `B` zero on their real span, all of
`C`. The runner supplies an exact rank-four `Herm(2)` polarization
certificate and directly checks that multiplying a positive block by `i`
does not leave it Hermitian or real-trace positive.

For the holomorphic result, let `F:Omega->M_d(C)` be entrywise holomorphic on
a connected open complex domain and suppose every `F(z)` is Hermitian. For
every vector `v`,

```text
f_v(z) = v^dagger F(z) v
```

is holomorphic and real-valued. Writing `f_v=u+i v_im`, Hermiticity gives
`v_im=0`; the Cauchy--Riemann equations then force both derivatives of `u` to
vanish. Thus each `f_v` is constant, and polarization makes `F` constant. If
`0 in Omega` and `F(0)=0`, then `F` is zero. The runner checks the exact
rank-four Cauchy--Riemann certificate.

These statements do not cover nonholomorphic positive maps, affine
normalizations, or a physically restricted positive determinant domain.

## 3. Scalar-amplitude typing gives a squared-modulus trace factor

For supplied `rho>=0` and fixed nonzero `A_0`, set

```text
A_z = z A_0,
sigma_z = A_z rho A_z^dagger.
```

Then exactly

```text
sigma_z
  = z A_0 rho conjugate(z) A_0^dagger
  = |z|^2 sigma_1.
```

Taking the trace preserves that factor. When `Tr(sigma_1)>0`, a finite menu
with the same underlying nonzero block has conditional trace ratios

```text
q_j = |z_j|^2 / sum_k |z_k|^2,
```

conditional on landing in one of those displayed determinant branches. In
the runner's completed instrument, the menu `{1,2i}` has unconditional branch
probabilities `(1/45,4/45)` and completion probability `8/9`; only after
conditioning on the determinant branches are the ratios `(1/5,4/5)`. The
single `z=3+4i` fixture has branch probability `5/9`, completion probability
`4/9`, and trace ratio `25` relative to `z=1`.

The trace-to-probability interpretation in that fixture comes from the
separately supplied instrument semantics. The general algebraic identity
supplies only branch blocks and their traces. Current Record supplies neither
a trace/Born law nor finite additivity. A separate provisional Record-law
source proposal is not a dependency and is not yet effective retained
science.

Finally, `|z|^2 sigma_1` is only a squared-modulus branch factor. Showing that
the actual charged-lepton determinant is this amplitude, and showing that its
carrier is the physical realified/conjugate-paired horn, remain `W_T`.

## 4. Coarse addition preserves supplied calibration

For supplied orthogonal rank-one blocks with traces `w,w`, where `w>0`,

```text
sigma_0 = w P_0,
sigma_1 = w P_1,
sigma_coarse = sigma_0 + sigma_1,
Tr(sigma_coarse) = 2w != w.
```

That is one valid calibration. A different valid calibration starts from a
coarse operation `A` and refines it using orthogonal-output isometries:

```text
A_0 = V_0 A / sqrt(2),
A_1 = V_1 A / sqrt(2),
A_0^dagger A_0 + A_1^dagger A_1 = A^dagger A.
```

The fine traces are then `w/2,w/2` and the coarse trace stays `w`. The runner
checks the corresponding exact positive-block fixtures. Therefore addition
preserves a supplied calibration, while one versus two labels selects no
normalization. Coherent combination before positive blocks form, an affine
reference-arm instrument, and an indivisible K/CPT event are also outside the
equal-`w` fixture.

This finite sum is a theorem-domain assumption. It is not derived from Record
or the Minimal Axioms. It constrains neither determinant exponent nor the
physical event map without `W_T`, `W_P`, and `W_E`.

## 5. Non-exhaustive routes that remain live

| Axis | Example mechanism | Missing physical supplier |
|---|---|---|
| `W_T` | positive determinant ray, `sigma_z=z sigma_1` for `z>=0` | prove the actual action stays positive and enters as a direct weight |
| `W_T` | nonholomorphic modulus, `sigma_z=|z| sigma_1` | derive phase erasure and its carrier |
| `W_T` | square-root writer, `A_z=sqrt(|z|)A_0` | derive this nonlinear amplitude map |
| `W_T` | Euclidean positive determinant as path-measure weight | connect the finite positive determinant sector to the actual AC generation carrier |
| `W_T/W_E` | phase-sensitive positive homogeneous or coherent/affine instrument | derive the map and its physical event interpretation |
| `W_E` | one indivisible K/CPT event | prove the conjugate labels are not independent events |
| `W_E` | normalized two-event refinement with fine weights `w/2,w/2` | derive the event instrument and calibration |
| `W_P` | downstream trace/Born or normalized path-measure law | derive probabilities from the chosen physical carrier |

These are constructive targets, not a complete classification. The runner
checks only the positive-ray, square-root, amplitude, and two displayed
calibration mechanisms.

## 6. AC occupancy consequence

The standing AC obligation asks for a physical matter action and measure that
distinguish the count-once `det_C` realization from a count-twice
`|det_C|^2`/conjugate-paired realization without inserting the desired value.
This packet turns that residual into three explicit questions:

1. **`W_T`, carrier typing:** Is the determinant an amplitude, a direct
   statistical weight, or input to another derived map?
2. **`W_P`, probability bridge:** What physical law maps that carrier to
   outcome probabilities and normalization?
3. **`W_E`, event calibration:** Which K/CPT alternatives are registrable
   events, and what fine-block normalization does the instrument supply?

Standard scalar-amplitude typing answers only the algebraic exponent question:
it gives a squared-modulus branch factor. With a separately established
trace-as-probability law, conditional outcome ratios inherit that factor. A
separate physical-carrier theorem is still needed to identify this with the
AC count-twice horn. Conversely, a positive first-power path remains
mathematically open, and event calibration can change a multiplicity without
changing the determinant exponent.

This is useful route reduction, but no formal obligation is retired. The
physical charged-lepton action, probability bridge, and event carrier are
still missing. The observed charged-lepton `r` value is not used in any proof.

## 7. Axiom decision

There is no minimal-axiom edit in this packet. The memo already puts
source/action, measurement, probability values, and observable identification
downstream. The three open interfaces sit exactly there.

An axiom update would become scientifically warranted only if independent
work showed that one of these interfaces is genuinely foundational and cannot
be derived from retained physics. The present finite lemmas establish neither
necessity nor uniqueness. Editing the axioms now would choose the AC answer
rather than derive it.

## 8. Scope and non-claims

- This is not a universal no-go against count-once physics.
- It is not a classification of all positive nonlinear determinant maps.
- It does not derive the physical charged-lepton matter action, measure,
  determinant typing, K/CPT carrier, physical event map, or calibration.
- It does not derive a universal Born/trace law, Record process, gravity
  coupling, continuum theory, or charged-lepton mass formula.
- It does not equate a coordinate presentation with an independent conjugate
  physical sector.
- It does not edit an axiom, primitive, audit verdict, obligation status, or
  TOE percentage.
- It does not claim that the routes in section 5 are exhaustive.

## 9. No-Go Discipline Gate

The packet contains negative-flavored subclaims, so the current N1--N8
protocol is applied to the exact bounded statements. The broad claim “no
count-once theory can work” fails this gate and is not shipped.

### N1 — alternative-route enumeration

| Family | Test against the narrow result | Disposition |
|---|---|---|
| Restricted positive determinant ray | Direct positive weight on `z>=0`; runner also tests failure at `z=-1`. | **ATTEMPTED; live outside scope.** It changes the phase-complete hypothesis. |
| Direct modulus weight | `z->|z|sigma` is positive and first-power. | **ATTEMPTED algebraically; live.** It is nonholomorphic and nonlinear. |
| Square-root writer | `A_z=sqrt(|z|)A_0`; exact runner fixture. | **ATTEMPTED; live.** It changes scalar-amplitude typing. |
| Euclidean determinant measure | [`STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md`](STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md) gives a finite positive staggered-determinant source candidate used as path-weight context. | **ATTEMPTED as boundary context; live and currently unaudited.** The cited source is not retained authority here and requires an actual AC carrier bridge. |
| Phase-sensitive positive homogeneous map | For `sigma>=0`, `B(z)=(|z|+Re z)sigma>=0`. | **ATTEMPTED analytically; live.** It is neither real-linear nor holomorphic. |
| Coherent/affine pre-block construction | Combine K/CPT paths coherently or with a reference arm before positive fine blocks form. | **ATTEMPTED as a premise-boundary construction; unresolved.** It lies outside the supplied fine-block premise, so it does not falsify the additive identity and is not physically ruled out. |
| One-event quotient | Form one indivisible event before refinement. | **ATTEMPTED as a premise-boundary construction; live.** The two-block sum is then undefined, so it changes `W_E` rather than the determinant exponent. |
| Calibrated normalized split | `A_j=V_jA/sqrt(2)` gives fine weights `w/2,w/2`. | **ATTEMPTED exactly; live.** It disproves any cardinality-only factor rule. |

The named families are non-exhaustive. They leave intact only the exact
real-linear, holomorphic, scalar-amplitude, and supplied-addition statements.

### N2 — wall-independence audit

| Pair | Why the first does not close the second | Why the second does not close the first | Verdict |
|---|---|---|---|
| `W_T` / `W_P` | Choosing an amplitude or path weight does not derive its probability law. | A trace/Born law does not identify which AC object enters it. | independent absent a linking theorem |
| `W_T` / `W_E` | Determinant exponent does not decide whether K/CPT labels are physical events. | Event identity does not decide amplitude versus direct-weight typing. | independent absent a linking theorem |
| `W_P` / `W_E` | A probability functional does not calibrate the event partition it acts on. | An event partition and instrument do not derive a universal trace/Born rule. | independent absent a linking theorem |

Positive ray, modulus, square-root, and Euclidean-measure routes are candidate
closures of `W_T`, not extra walls. One-event and calibrated-split routes are
candidate closures of `W_E`.

### N3 — hidden-condition scan

| Phrase/class | Classification |
|---|---|
| positive branch block | supplied finite operator data; not called Record content |
| trace weight | candidate mathematical quantity; physical probability requires `W_P` |
| standard amplitude typing | exact conditional equation `A_z=zA_0`; load-bearing `W_T` premise |
| coarse addition | supplied finite block-sum convention; not a Minimal-Axiom or Record theorem |
| current Minimal Axioms | authority only for the explicit non-supply boundary |
| physical event map/calibration | open `W_E`, never inferred from labels |

The scan found no unnamed bridge beyond `W_T`, `W_P`, and `W_E`. In
particular, “standard instrument” is not used to smuggle completeness or a
universal probability law into the general branch identity.

### N4 — residual matching

The finite lemmas prove map-typing facts; the AC obligation asks for the actual
physical matter carrier. A squared-modulus trace factor is not itself the
realified/conjugate-paired AC horn, and an additive factor of two is not a
determinant-power result. No prior no-go, contextual determinant note, or
desired mass ratio is used as a witness. The result therefore ships as bounded
route reduction with the three mismatched physical residuals explicit.

### N5 — rhetoric audit and execution certificate

| Resolution | Tested? | Exact scope |
|---|---:|---|
| per-element | Yes | scalar fixtures `z in {1,-1,i,-i}` and determinant typings |
| per-site | No | no site action or site-to-event lift |
| per-mode | No | no fermion-mode or K/CPT independence theorem |
| per-block | Yes | `Herm(2)` positivity, Kraus blocks, and two calibration fixtures |
| lattice-wide | No | no lattice action, continuum lift, or charged-lepton theory |

The runner prints substantive `per_element:`, `per_site:`, `per_mode:`,
`per_block:`, and `lattice_wide:` lines. The cached stdout must match the
landed runner exactly. Every broader physical phrase is excluded.

### N6 — partial-closure path and primitive scan

The approved primitive registry and relevant source memos were checked.

- `scale_reference_primitive` supplies units only.
- `kinetic_isotropy_primitive` supplies kinetic-form graining only.
- `realized_state_primitive` supplies pointwise evaluation, not weighting or
  probability.
- `minimal_axioms` supplies the probability-distribution slot and fixed
  Records while leaving the values, source/action, and calibration downstream.

No primitive is relabeled as a wall. Positive partial closures remain
available without an axiom edit: derive a positive AC action (`W_T`), derive a
trace or normalized-measure law (`W_P`), or derive the physical instrument and
its normalized refinement (`W_E`). The exact `w/2,w/2` split is a concrete
partial-closure construction, not a rhetorical escape.

### N7 — strongest steelman

The strongest positive critic combines all three missing interfaces.
[`STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md`](STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md)
is the exact repository source candidate for a configuration-wise positive
first-power staggered determinant that may enter the path measure directly
(`W_T`); a derived normalized-measure-to-outcome rule may connect that measure
to observable records (`W_P`); and an independently calibrated one-event or
normalized two-event instrument may avoid artificial K/CPT double counting
(`W_E`). The cited source is currently unaudited, is non-load-bearing here,
and does not establish the AC carrier.
Executing these three links could positively close count-once without
contradicting any lemma here. This is why no broad no-go or axiom selection is
allowed.

### N8 — cross-cycle echo

Repository ledgers and the relevant August 13 correction were checked.

- The block-28 determinant-power ledger says determinant algebra does not
  select the physical horn. The later Pfaffian note reinforces that a
  coordinate rewrite is not a new physical carrier.
- The block-29 Record-orbit ledger says outcome labels do not select
  determinant power. The calibrated split here strengthens that boundary.
- `MINIMAL_AXIOMS_2026-06-29.md` records the August 13 removal of scalar
  intensity and finite additivity from Record.
- `FINITE_DYADIC_PRODUCT_REGISTRATION_TRUNCATED_BARYCENTER_BOUNDED_THEOREM_NOTE_2026-08-13.md`
  records the corresponding prior repair: a supplied finite-product
  construction must not be advertised as a Record-bit theorem.

This packet follows that retirement mechanism by saying “supplied positive
block/trace convention,” never “Record trace law” or “Record additivity.” No
convention-only repair closes `W_T`, `W_P`, and `W_E` together.

**Gate result:** PASS for the exact bounded finite lemmas and corrected
three-interface residual. FAIL for a universal count-once no-go, a physical AC
horn selection, or a framework-wide probability theorem; none is shipped.

## Verification

Run:

```bash
python3 scripts/acphilambda_record_positivity_determinant_power_selector_boundary_2026_08_22.py
```

Expected result:

```text
TOTAL: PASS=12 FAIL=0
```

Every named hostile mutation must produce exactly one failed check.
