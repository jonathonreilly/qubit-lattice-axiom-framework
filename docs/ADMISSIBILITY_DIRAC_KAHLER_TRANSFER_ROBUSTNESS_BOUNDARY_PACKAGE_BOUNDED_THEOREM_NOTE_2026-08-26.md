---
claim_id: admissibility_dirac_kahler_transfer_robustness_boundary_package_bounded_theorem_note_2026-08-26
final_path: docs/ADMISSIBILITY_DIRAC_KAHLER_TRANSFER_ROBUSTNESS_BOUNDARY_PACKAGE_BOUNDED_THEOREM_NOTE_2026-08-26.md
claim_type: bounded_theorem
claim_scope: "Finite exact results for the Block-190 carrier at m=9/20: four unit-volume width measurements at c=5/13; two classified shear endpoints at T=16 and t0=3; a declared [4/4] interpolation model fitted to ten carrier values, checked at two withheld values and projectively at seven probes; six first-order volume-response slice sums with their per-anchor parity pattern; and seven positive volume samples. The interpolation-model Sturm theorem is not promoted to a continuum identity for the carrier."
runner: scripts/admissibility_dirac_kahler_transfer_robustness_boundary_package_2026_08_26.py
status: proposed_retained
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "finite robustness and boundary probes for the transfer-monodromy carrier"
source_of_blocker_text: review_loop
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Derive the carrier coefficient symbolically or prove an a priori degree bound before drawing any between-probe conclusion from the interpolation model."
conditional_surface_status: "stacked on unmerged ancestor artifacts; scientific content is proposed for retention and remains audit-required"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact finite-dimensional linear algebra at declared rational fixtures plus an exact theorem about an explicitly typed interpolation model"
audit_required_before_effective_retained: true
bare_retained_allowed: false
parent_ref: origin/physics-loop/toe-axiom-closure-block199-heavy-metric-operator-completion-20260826
parent_commit: 725269c6057deed9b7ac1f72a315297a9f99f35a
current_main: 76df4becc8233080bc5a10a4baf55f83e80f8f2d
registered: 0
adopted: 0
axiom_movement: none
---

# Finite exact transfer-robustness probes and a fenced interpolation model

**Date:** 2026-08-26

**Type:** `bounded_theorem`

**Status:** `proposed_retained` — author proposal only; independent audit is
required before any effective retained status.

**Standing:** conditional support on an unmerged PR stack. Nothing is registered,
adopted, or added to the axioms.

## Result

The exact runner establishes four finite results for the declared carrier:

1. At unit volume and `(m,c)=(9/20,5/13)`, the landed deep monodromy factors
   recur at `T=16,20,24`; the `T=12, t0=3` slot is instead the seam mirror and
   has a different factor. The near-boundary `t0=1` factor census agrees at
   `T=12,16,20,24`. These are finite width observations, not an all-`T` theorem.
2. At `T=16`, `t0=3`, and `m=9/20`, the carrier is exactly classified at two
   shears separated by `19/1703936`. The lower point has positive reciprocal
   heavy and light pairs; the upper point has a real negative reciprocal heavy
   pair. These two classifications do not locate a boundary.
3. A declared `[4/4]` rational interpolation model for the normalized heavy
   coefficient matches fourteen distinct exact carrier probes. Exact Sturm
   arithmetic classifies that model, not the carrier between probes.
4. Six exact first-order volume-response slice sums, their per-anchor parity
   pattern, and seven positive volume samples are reproduced. The response is
   a derivative of a finite matrix, not a force or susceptibility; the volume
   points are samples, not an interval.

## Authority and dependencies

The construction is inherited from the following artifacts and is not
redefined here:

- [Block 190 carrier and monodromy](ADMISSIBILITY_DIRAC_KAHLER_WIDTH_FAMILY_TRANSFER_MONODROMY_BOUNDED_THEOREM_NOTE_2026-08-25.md)
- [Block 194 finite failure-mode census](ADMISSIBILITY_DIRAC_KAHLER_TRANSFER_PACKAGE_MC_GENERALITY_BOUNDED_THEOREM_NOTE_2026-08-25.md)
- [Block 191 cell-average assembly](ADMISSIBILITY_DIRAC_KAHLER_BOUNDARY_MODE_VOLUME_SENSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-25.md)
- [Block 105 Hodge input](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md)
- [Block 199 finite heavy symmetrizer theorem](ADMISSIBILITY_DIRAC_KAHLER_HEAVY_METRIC_OPERATOR_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-26.md)
- [Batch-2 adversarial findings](../.claude/science/physics-loops/generator-program-20260821/scout_batch2_findings.md)

The exact implementation is
[the Block-200 runner](../scripts/admissibility_dirac_kahler_transfer_robustness_boundary_package_2026_08_26.py).

## 1. Finite width measurements

At each `T=12,16,20,24`, the carrier has full rank, `d_K^2=0`, the declared
reflection/covariance residuals vanish, and both inverse residuals vanish.
The two-site spatial shift `U` supplies the heavy/light sector label.

The deep census at `T=16,20,24` is

```text
(22569375 z^2 - 233631106 z + 22569375)^2
(39529825 z^2 - 109432706 z + 39529825)^2.
```

At `T=12`, `t0=3` equals `T/2-3`, the seam-mirror slot, and instead has census

```text
(22569375 z^2 - 233631106 z + 22569375)
(39529825 z^2 - 109432706 z + 39529825)^2
(48554286398375 z^2 - 376762652339458 z + 35686537764375).
```

The near-boundary slot `t0=1` agrees at all four tested widths with census

```text
(22569375 z^2 - 233631106 z + 22569375)
(39529825 z^2 - 109432706 z + 39529825)^2
(43033320714375 z^2 - 445467467014578 z + 48554286398375).
```

No induction or structural proof in `T` is supplied.

## 2. Two exact shear endpoint classifications

Fix `T=16`, `t0=3`, `m=9/20`, and unit volume. Define

```text
c_low  = 1213333/1703936,
c_high = 151669/212992,
c_high - c_low = 19/1703936.
```

At `c_low`, the primitive heavy and light quadratics are

```text
22731666619014252910884 z^2
- 9037516115117032760684071897 z
+ 22731666619014252910884,

1965446916440236496410958116 z^2
- 5106576818903321739356333897 z
+ 1965446916440236496410958116.
```

At `c_high`, they are

```text
7068274392254939356 z^2
+ 2206352658131956553649497 z
+ 7068274392254939356,

479836341843952799153956 z^2
- 1246694110992835465220297 z
+ 479836341843952799153956.
```

All four are palindromic and occur with multiplicity two. Their discriminants
and margins `|b|-2a` are strictly positive. The lower endpoint therefore has
real positive reciprocal pairs; the upper endpoint has a real negative
reciprocal heavy pair and a positive reciprocal light pair.

This establishes only the two endpoint classifications. The word “bracket”
means their ordered separation; it does not assert continuity, uniqueness, or
the location of an edge between them.

## 3. The `[4/4]` interpolation model

Ten exact carrier values determine a one-dimensional `[4/4]` fit. In primitive
normalization the declared model is

```text
beta_fit(c) = -2 N(c)/D(c),
N(c) = 1362 c^4 + 800 c^3 - 5529 c^2 - 1600 c + 5448,
D(c) =  400 c^4 + 800 c^3 - 1681 c^2 - 1600 c + 1600,
gcd(N,D) = 1.
```

The fit points are

```text
1/3, 1/4, 3/4, 1/5, 2/5, 3/5, 4/5, 1/6, 5/6, 1/7.
```

The withheld points `1/2` and `2/3` reproduce respectively
`-27607/2019` and `-98418/2071` with exact zero residual. At seven probes
(`1/2`, `2/3`, `1/3`, `3/4`, `4/5`, `c_low`, `c_high`), the primitive carrier
quadratic agrees projectively with `(D(c),-2N(c),D(c))`.

### Exact theorem about the model

Sturm counting gives, on `(c_low,c_high)`:

```text
# roots of D       = 1,
# roots of N       = 0,
# roots of N - D   = 0,
# roots of N + D   = 0.
```

Moreover, `D(c_low)>0`, `D(c_high)<0`, while `N` is positive at both endpoints.
Thus the interpolation model has one denominator pole and no numerator zero in
the bracket. On each component of the bracket punctured at that pole,
`|beta_fit|>2`. At `D=0`, the ratio `beta_fit` is undefined; the associated
projective model quadratic `(D,-2N,D)` degenerates to a linear polynomial.

### Why this is not a carrier theorem

No symbolic expression or a priori rational-degree bound for the carrier
coefficient has been proved. Finite agreement therefore cannot establish a
continuum identity. Concretely, let `S` be the fourteen distinct rational probe
shears and choose a rational `c_*` between the endpoints with `c_*` not in `S`
and `D(c_*) != 0`. Then

```text
beta_alt(c) = beta_fit(c) + A product_{s in S}(c-s)
```

agrees with every probe for any rational `A`; choosing
`A=-beta_fit(c_*)/product_{s in S}(c_*-s)` makes `beta_alt(c_*)=0` exactly.
This does not claim `beta_alt` is the carrier. It proves that the finite data
alone do not distinguish a pole-only continuation from a continuation with a
numerator zero. The carrier mechanism between probes remains open.

## 4. First-order volume response

For a local anchor `(s,x)` and its reflected image, the runner computes the
exact derivative of the finite monodromy trace using

```text
dB = diag(-1,-169/144,-169/144,1),
dB[1,2] = dB[2,1] = 65/144.
```

Summing all four spatial anchors gives

| `s` | exact slice sum |
| ---: | ---: |
| 1 | `0` |
| 2 | `-3924317879963744/17744088856432749` |
| 3 | `-285033126329023712/147867407136939575` |
| 4 | `-73354817263464195597509202636832/5276875808912607540299962640625` |
| 5 | `38264746670503590368/3696685178423489375` |
| 6 | `0` |

At each slice, `x=0,2` agree and `x=1,3` agree. On `s=2,3,4,5` the two
parity-labelled values are distinct and neither equals the four-anchor sum. At
`s=1,6`, both values coincide at zero. The endpoint zeros hold per anchor, and
both parity values change from negative at `s=4` to positive at `s=5`.

These values are traces of a first derivative of a finite rational matrix.
They are not identified with a susceptibility, force, coupling, or energy.

## 5. Seven exact positive volume samples

At `T=16`, `t0=3`, `m=9/20`, `c=5/13`, each tested volume

```text
1/100, 1/10, 1/5, 2/5, 3/5, 4/5, 6/5
```

has two distinct palindromic quadratic factors, each squared, with positive
leading coefficient, positive discriminant, and positive margin `|b|-2a`.
Hence every tested factor has two distinct real positive reciprocal roots.

This corrects two readings of the scout record: `(1/10,1]` excludes `1/10`
even though `1/10` is positive, and the positive probes `1/100` and `6/5` lie
outside its two stated ends. The result is seven samples. It proves neither
positivity between samples nor a maximal positivity interval.

## No-Go Discipline Gate

This packet governs one narrow derived boundary: **the fourteen finite values,
without an additional regularity theorem, do not uniquely determine an
unrestricted rational continuation.** It does not declare a no-go for deriving
the carrier law. The symbolic-identity/degree-bound route remains open.

### N1 — Alternative routes

| Route | Marker | Attempt and outcome |
| --- | --- | --- |
| Impose `[4/4]` degree | ATTEMPTED | The ten fit values then determine the displayed model, but the degree restriction is an extra premise not supplied by the finite data or by [Block 190](ADMISSIBILITY_DIRAC_KAHLER_WIDTH_FAMILY_TRANSFER_MONODROMY_BOUNDED_THEOREM_NOTE_2026-08-25.md). |
| Analytic identity theorem | ATTEMPTED | Fourteen isolated points have no accumulation point, so the identity theorem does not apply. |
| Endpoint continuity / intermediate value | ATTEMPTED | Continuity and absence of a singularity would be additional carrier hypotheses; endpoint signs alone neither determine a continuation nor distinguish a pole from a zero. |
| Palindromy and `U` grading | ATTEMPTED | These symmetries fix the pointwise quadratic form and sector label, but [Block 190](ADMISSIBILITY_DIRAC_KAHLER_WIDTH_FAMILY_TRANSFER_MONODROMY_BOUNDED_THEOREM_NOTE_2026-08-25.md) supplies no shear-degree bound. |
| Add finitely many probes | ATTEMPTED | For any finite probe set, multiplying `(c-s)` over the set produces an exact perturbation that vanishes at every probe; finite enlargement alone does not close the identity bridge. |

These are distinct mechanisms: assumed complexity class, analytic uniqueness,
topological continuity, algebraic symmetry, and finite sampling.

### N2 — Wall independence

The raw absences “no symbolic formula” and “no sufficient degree bound” collapse
to one wall: **no identity-determining carrier regularity theorem**. A symbolic
formula would decide the question directly; a sufficient degree bound would
make a finite exact reconstruction decisive. No independent multi-wall count is
claimed.

### N3 — Hidden-wall scan

“By construction” refers only to the displayed `beta_alt`, whose probe
equalities are explicit. “The framework provides” is not used to supply a
degree bound, analyticity class, or continuity premise. No standard-QFT,
canonical, registered, or background assumption carries the boundary.

### N4 — Residual matching

| Cited artifact | Its residual | Current residual | Match/use |
| --- | --- | --- | --- |
| [Block 190](ADMISSIBILITY_DIRAC_KAHLER_WIDTH_FAMILY_TRANSFER_MONODROMY_BOUNDED_THEOREM_NOTE_2026-08-25.md) | Defines the finite carrier and monodromy | Missing identity bridge in shear | No; construction authority only |
| [Block 194](ADMISSIBILITY_DIRAC_KAHLER_TRANSFER_PACKAGE_MC_GENERALITY_BOUNDED_THEOREM_NOTE_2026-08-25.md) | Finite failure-mode census is not a boundary curve | Finite interpolation is not yet a carrier identity | Similar caution, not an exact residual witness |
| This runner | Fourteen probe equalities and explicit counter-interpolant | Non-uniqueness from those values alone | Yes; direct exact witness |

No prior no-go is counted as proof of the current boundary.

### N5 — Rhetoric audit

The five execution-certificate lines below are byte-identical to the primary
runner output. They restrict the result to the heavy coefficient at one finite
block and explicitly mark unexecuted resolutions.

### N6 — Partial-closure paths

Three non-axiom routes remain live: derive the carrier coefficient symbolically;
prove a determinant/rational-degree bound; or find a recurrence that makes a
finite set identity-determining. Each would close the wall by mathematics, not
by importing new physics or changing a convention. No “new axiom required”
claim is made.

### N7 — Steelman

The strongest hostile case is that the finite carrier matrices may force a low
rational degree after exact determinant cancellation; if that degree is `[4/4]`
or lower, the current fit plus withheld checks could become an identity theorem,
and the model pole could become a carrier pole. This is concrete and actionable.
Therefore a broad carrier no-go would be premature and is withdrawn. The source
ships only the exact data-alone non-identifiability lemma and names symbolic
degree control as the next obligation.

### N8 — Cross-cycle echo

The closest prior wall is [Block 194](ADMISSIBILITY_DIRAC_KAHLER_TRANSFER_PACKAGE_MC_GENERALITY_BOUNDED_THEOREM_NOTE_2026-08-25.md),
which fenced a finite census from becoming a boundary curve. The applicable
retirement mechanism is the same here: a symbolic law or sufficient degree
bound. No later landed artifact cited by this block supplies that mechanism, so
the route stays open rather than being declared impossible.

**Gate disposition:** `PASS` for the narrow partial-attempt boundary above;
`FAIL/WITHDRAWN` for any claim that the carrier itself must have the fitted pole
or cannot have a numerator zero or unimodular crossing between probes.

## Arithmetic controls

- Every mass, shear, and volume supplied to the runner is an exact SymPy
  rational or integer.
- `nsimplify` is absent.
- The imported Hodge helper can introduce a `Float` when passed a plain Python
  integer volume. The runner passes an exact SymPy integer and gates the absence
  of `Float` entries in every cached carrier object.
- The baseline has 33 checks in families `A` through `G` and 33 declared
  mutations. Each mutation changes only its assigned family.

N5: per_element: checked — fourteen exact values of the heavy-sector coefficient do not determine an unrestricted rational continuation; the explicit beta_alt construction preserves every probe and inserts one additional rational zero.
N5: per_site: checked and not executed — the interpolation boundary concerns one compressed scalar coefficient as shear varies, not a sitewise response; no between-probe site claim is made.
N5: per_mode: checked — only the U=-1 heavy compression is fitted; the U=+1 light compression is classified at the two endpoints and receives no interpolation or between-probe conclusion.
N5: per_block: checked — all interpolation statements are restricted to T=16, t0=3, m=9/20 and unit volume; other cores, widths, masses, and carrier families are not classified.
N5: lattice_wide: checked and not executed — no all-T, generic-parameter, continuum, dynamics, gravity, energy, or Nature conclusion is drawn from the finite exact probes.

## Limitations and reopen conditions

Not supplied:

- an identity or degree bound for the carrier coefficient as a function of `c`;
- carrier behavior between the exact shear probes;
- a located shear edge or a volume interval;
- an all-width result;
- a generic `(m,c)` theorem;
- a second-order or finite-volume response law;
- an Osterwalder–Schrader reconstruction, transfer Hamiltonian, energy, mass,
  gravity sector, continuum limit, or dynamics.

Reopen the interpolation question only after deriving the carrier coefficient
symbolically or proving a degree bound strong enough to make the finite values
identity-determining. Additional samples alone can strengthen a census but do
not supply that bridge.

## Reproduction

```bash
python3 scripts/admissibility_dirac_kahler_transfer_robustness_boundary_package_2026_08_26.py
python3 scripts/admissibility_dirac_kahler_transfer_robustness_boundary_package_2026_08_26.py --list-mutations
```

## Decision cut

Nothing is registered or adopted. No prior landed claim is edited. The valid
finite exact observations are retained as a proposal; the draft's unsupported
continuum interpolation, carrier pole-mechanism, and every-slice-distinct parity
claims are withdrawn. This is a statement about a finite formal construction,
not about Nature.
