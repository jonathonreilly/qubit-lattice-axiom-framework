---
claim_id: admissibility_dirac_kahler_source_functional_grading_boundary_bounded_theorem_note_2026-08-23
final_path: docs/ADMISSIBILITY_DIRAC_KAHLER_SOURCE_FUNCTIONAL_GRADING_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-23.md
claim_type: bounded_theorem
claim_scope: "For the normalized complex Gaussian source functional Z_Q[barJ,J]/Z_Q[0] = exp(barJ^T Q^-1 J), the Block-107 displayed antilinear reflection equation K_ab = conj(G(b,theta a)), and the inherited Block-177 positive-slice support on the exact real 8x4 and 12x4 Dirac--Kahler fixtures at s_t in {0,1/4}, with the Block-178 rank-two isometry used only as an imposed counterroute: source differentiation derives G=Q^-1 and the raw permanent Wick tower over K=E_S^dag r G^dag E_S, which specializes to E_S^dag r G^T E_S on all four real fixtures. The full eight-source K is non-Hermitian with anti-Hermitian rank 8 on all four cells; its Hermitian part is mixed at inertias (6,2,0) on 8x4 and (4,4,0) on 12x4 in the (n_+,n_-,n_0) convention. This is not a universal no-go: the parent-supplied rank-two X gives X^dag K X exactly Hermitian, positive definite and transport-sensitive on both extents at both dials. The normalized Gaussian vacuum coefficient is 1. On all four fixtures the unnormalized one-copy coefficient Z_Q=pi^N/det Q is positive and dial-sensitive and multiplies every higher algebraic coefficient by the same positive factor, so the one-copy vacuum leg is positive and dial-sensitive. This does not Hermitianize the raw higher-sector kernel: Block 177's sector-indefiniteness theorem still requires its separately stipulated Hermitianized covariance or action-side kernel. The separate |Z_Q|^2 quantity is a doubled partition-level readout rather than the one-copy degree-zero coefficient; identifying |Z_Q|^2 specifically with Sym^0 requires an additional reweighting/doubling/sewing prescription. No physical event/source algebra, linear-field reflection selector, Hermitianization rule, |Z_Q|^2 source-sewing law, Born law, axiom amendment, obligation retirement or TOE percentage movement is established."
depends_on:
  - minimal_axioms
  - scale_reference_primitive
  - kinetic_isotropy_primitive
  - realized_state_primitive
  - admissibility_dirac_kahler_adm_seam_two_history_gram_bounded_theorem_note_2026-08-15
  - admissibility_dirac_kahler_closure_audit_two_bounded_theorem_note_2026-08-21
  - admissibility_dirac_kahler_complex_structure_synthesis_bounded_theorem_note_2026-08-23
  - admissibility_dirac_kahler_conditional_symmetric_power_theorem_note_2026-08-23
  - admissibility_dirac_kahler_rank_two_scalar_transport_counterexample_bounded_theorem_note_2026-08-23
runner: scripts/admissibility_dirac_kahler_source_functional_grading_boundary_2026_08_23.py
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: prunes
target_claim_id: admissibility_dirac_kahler_complex_structure_synthesis_bounded_theorem_note_2026-08-23
target_blocker_text: "B2b -- derive the framework's own committed functional grading."
source_of_blocker_text: next_trace_action
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Do not run another unrestricted rank or sector scan. The readout lane can advance through a derived, presentation-invariant physical event/source algebra and its field reflection, or through an independently justified event-refinement/additivity theorem that connects the Admissibility distribution to a source functional. If the specific doubled candidate |Z_Q|^2 is kept, its reweighting/doubling/sewing rule must also be explicit. At portfolio level, move the main campaign to the Wilson-Q discriminator while these interfaces remain open."
conditional_surface_status: "audited_conditional expected (dependency_not_retained; Blocks 103-178 content-bound unaudited)"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "The source-functional identities are exact symbolic differentiation statements, the prose/code orientation mismatch is an exact generic-matrix identity, and every finite-fixture result is exact rational algebra reconstructed from the inherited action. The standing is bounded because the physical linear event/source algebra and its reflection are not supplied, only two finite extents and two dials are tested, the positive rank-two restriction is imposed rather than selected, and no continuum, completeness or Nature claim follows. The broader negative vacuum reading was independently falsified and withdrawn: the one-copy unnormalized Z_Q is positive and dial-sensitive on all four fixtures."
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Source-derived functional grading boundary — the raw Wick tower is forced, its positive domain is unselected, and the doubled readout is a separate construction

**Date:** 2026-08-23

**Runner:** `scripts/admissibility_dirac_kahler_source_functional_grading_boundary_2026_08_23.py`

**Parent stack:** Blocks 177 and 178

**Standing:** exact bounded theorem and forward correction. Nothing registered,
adopted or written into the axioms.

## Result in plain language

The Gaussian does answer one part of B2b. Once its action is supplied, ordinary
source differentiation fixes the covariance and every higher Wick contraction;
there is no freedom to substitute the action-side matrix for the covariance.

It does **not** finish the probability construction. On the full inherited
eight-source space, the reflected covariance is not even Hermitian. But a
specific two-dimensional restriction is exactly Hermitian, positive and
transport-sensitive. Therefore the result is not “positive grading is
impossible.” It is: **the theory has not selected which source/event subspace is
physical, or which linear-field reflection acts on it.**

There is a second, independent accounting distinction. The normalized
Gaussian's vacuum coefficient is `1`. The unnormalized one-copy coefficient is
`Z_Q`; on every tested fixture `det Q` is positive and changes between the two
dials, so `Z_Q=pi^N/det Q` is itself positive and dial-sensitive. This rescues
the vacuum leg of the one-copy Wick functional and positively rescales its
algebraic coefficients. It does not repair the raw higher-sector kernel, which
is non-Hermitian on the full support. Block 177's sector-indefiniteness theorem
therefore still needs its separately stipulated Hermitianized covariance or
action-side kernel; only its vacuum leg can use `Z_Q`. The separate candidate
`|Z_Q|^2` is a doubled partition-function readout. It is not the one-copy
coefficient unless a separate reweighting or doubling/sewing prescription is
added.

This is significant blocker identification, not TOE closure. No percentage
moves.

## The exact source derivation

Let `G=Q^-1`. The unnormalized and normalized complex Gaussian source
functionals are

\[
 \widetilde Z_Q[\bar J,J]
 = Z_Q\exp(\bar J^T GJ),\qquad
 Z_Q={\pi^N\over\det Q},\qquad
 \mathcal Z_Q={\widetilde Z_Q\over \widetilde Z_Q[0]}
 =\exp(\bar J^T GJ).
\]

Exact differentiation gives

\[
 \left.\partial_{\bar J_i}\partial_{J_j}\mathcal Z_Q\right|_0=G_{ij},
\]

and, at degree two,

\[
 \left.\partial_{\bar J_0}\partial_{\bar J_1}
 \partial_{J_0}\partial_{J_1}\mathcal Z_Q\right|_0
 =G_{00}G_{11}+G_{01}G_{10}.
\]

The same-polarity contractions vanish. At every degree, the equal-degree sector
is therefore the permanent of the two-point kernel; unequal holomorphic and
antiholomorphic degrees vanish. **The algebraic Wick number grading is derived.**
What is not derived is a Hermitian or positive Fock grading.

## Which kernel the displayed Block-107 reflection convention forces

Block 107's displayed equation is

\[
 K_{ab}=\overline{G(b,\theta a)}.
\]

With `r_(ac)=delta_(c,theta a)` and positive-slice injection `E_S`, this is

\[
 \boxed{K_S=E_S^\dagger rG^\dagger E_S}.
\]

All four Block-177 fixture matrices `Q` and `G` are exactly real, so at their
scope this reduces to the raw candidate Block 177 used,

\[
 K_S=E_S^T rG^T E_S.
\]

There is a latent orientation defect in the inherited corpus. Block 107's
runner constructs `conj(G(a,theta b))`, the transpose of its prose equation.
The runner here exercises both on a generic matrix and proves that exact
transpose relation. The old flat reflection-covariant fixture could not see the
difference, and Block 177's Hermitianization erases it. On the present exact real
fixtures the two raw forms are adjoints, so every Hermitian-part inertia below
is unchanged; on a future genuinely complex fixture, the convention must be
fixed before use.

## The full-source boundary

For the prose kernel,

\[
 K^\dagger=E_S^\dagger GrE_S.
\]

On the full space, reflection covariance

\[
 rQ^\dagger r=Q
\]

would imply `rG^dagger r=G` and make `K` Hermitian. It fails at the inherited
fixtures. Exact `(0,0)` witnesses are independent of the two tested dials:

| extent | `(r Q^dag r-Q)_(0,0)` |
|---|---:|
| `8x4` | `-997/27456` |
| `12x4` | `3167/10560` |

On all four extent/dial cells, the selected raw kernel has anti-Hermitian rank
`8`. Hermitianizing it is an additional real-part prescription, not a source
derivative, and gives

| extent | `s_t=0` | `s_t=1/4` |
|---|---:|---:|
| `8x4` | `(6,2,0)` | `(6,2,0)` |
| `12x4` | `(4,4,0)` | `(4,4,0)` |

Every tuple is `(n_+,n_-,n_0)`. Thus the full inherited source algebra does not
supply a Hermitian-positive reflected functional at these four cells.

## The positive counterroute, preserved with full force

Block 178's parent-supplied isometry is

\[
 X=\left[{4e_0+3e_4\over5},
          {4e_2+3e_6\over5}\right],\qquad X^\dagger X=I_2.
\]

For the source-derived raw covariance kernel—not merely its Hermitian part—the
compression `C=X^dag K X` is exactly Hermitian and positive definite at both
extents and both dials. The prose and code orientations agree after this
compression. Its half-trace moves by the following exact positive amounts from
`s_t=0` to `s_t=1/4`:

| extent | exact half-trace gap |
|---|---:|
| `8x4` | `73977924244224/1492124486100431` |
| `12x4` | `150346029799280479942166602650413136160/2455275247171512614379752553769527826469` |

This is a real positive source-sector counterroute. It blocks any claim that no
source convention or subspace works. It does not finish B2b because `X` was an
imposed falsifier, not a physical event/source selector derived from the four
axioms, the action or Record.

The independent structural check sharpens that last sentence. `X` intertwines
translation by two spatial sites, and the inherited `Q` and `r` commute with
that translation. This explains why its `2x2` compressions have the form
`a I + b sigma_x`. It does **not** select the `3:4` time-slice mixture: every
pair of weights `(u,v)` in the same two-column support has exactly the same
period-two intertwining property. Moreover, the displayed `X` subspace is not
invariant under `r`, `Q` or the action-side form; every corresponding leakage
residual has rank `2` on both extents and dials. Thus the only identified
structure explains the shape of the positive counterexample, not why Nature
would choose its weights or domain.

## The vacuum-category correction

For the same normalized Wick functional,

\[
 \mathcal Z_Q[0,0]=1.
\]

That degree-zero coefficient is positive and exactly dial-independent. For the
unnormalized one-copy functional it is `Z_Q`. On all four exact fixtures tested
here,

\[
 \det Q(s_t=0)>0,\qquad \det Q(s_t=1/4)>0,
 \qquad \det Q(0)\ne\det Q(1/4).
\]

Because `pi^N>0`, `Z_Q=pi^N/det Q` is therefore positive and dial-sensitive at
both extents. Multiplying the normalized source functional by this positive
factor rescales every algebraic source coefficient. It would preserve the
inertia of a separately supplied Hermitian sector Gram, but the actual raw
higher-sector kernel remains non-Hermitian on the full support. Thus the
one-copy vacuum coefficient is repaired at finite-fixture scope; the particle
sector/reflection problem is not.

The quantity used by the doubled readout candidate is instead

\[
 |Z_Q|^2=Z_QZ_{Q^\dagger}={\pi^{2N}\over|\det Q|^2}.
\]

Block 176 explicitly identifies this as a **partition-function-level** pairing,
not a field-configuration pairing. Block 177 calculates its determinant
factorization separately from the source sectors, and its sole named grading
premise does not identify this doubled scalar with the one-copy degree-zero
coefficient.

One mathematically clean way to use the doubled candidate would be to declare

\[
 \mathcal F_Q[\bar J,J]=|Z_Q|^2\exp(\bar J^T GJ).
\]

This multiplies **every** source coefficient by `|Z_Q|^2`, not only degree zero.
A genuinely doubled product with independent sources has a larger bigraded
tower and needs a sewing rule to reduce to one `K`. Either construction is a
valid mathematical definition; treating it as the physical readout is an
additional selection or bridge not supplied by the current foundation.

The forward correction is therefore precise:

- Block 177's exact determinant factorization and the separate positivity and
  dial sensitivity of both `Z_Q` and `|Z_Q|^2` survive at the four fixtures.
- Its symmetric-power indefiniteness lemma survives for a supplied Hermitian
  mixed kernel.
- Its vacuum leg can use positive one-copy `Z_Q`; no doubled-vacuum glue is
  needed for that leg. The sector-indefiniteness theorem still needs the
  separately stipulated Hermitianized covariance or action-side kernel and is
  not realized by the raw one-copy tower as written.
- The raw covariance permanent tower is actually derived, so calling every
  Wick-sector identification a premise is too broad.
- Replacing the raw kernel by its Hermitian part or by the action-side form is an
  added premise.
- Calling `|Z_Q|^2` specifically the vacuum sector of that one-copy tower needs
  a second, previously unnamed reweighting/doubling/sewing premise.

No parent file is edited here.

## No-Go Discipline Gate

This gate follows the fresh `origin/main` no-go-discipline skill. It evaluates
one narrow negative statement only: **the current supplied foundation plus the
five content-bound parent constructions do not yet derive a unique physical
linear event/source domain, its field reflection, or the identification of the
specific doubled scalar `|Z_Q|^2` with the one-copy source tower's degree-zero
sector.** It does not test or assert that such structures cannot exist.

### Target contract

| Field | Contract |
|---|---|
| Target statement | Derive from the supplied foundation a physical source/event algebra, a field-level reflection making its source kernel Hermitian-positive, and—if the Block-176 doubled candidate is used—a sewing rule identifying `|Z_Q|^2` with the same functional's degree-zero sector. |
| Quantifiers/domain | The exact real `8x4` and `12x4` fixtures at `s_t in {0,1/4}`; symbolic source differentiation is dimension-general, while every matrix-sign statement is fixture-bounded. |
| Allowed premises | `minimal_axioms`, the complete approved primitive registry, and Blocks 107/170/176/177/178 only as explicitly conditional content parents. |
| Forbidden weakenings | An imposed positive subspace is not a physical selector; a Hermitian part is not a source derivative; a positive partition scalar is not automatically an event probability; two extents are not a limit. |
| Completion witness | A presentation-invariant Record-to-source map, a field reflection/source convention with a positive event domain, and a common normalized or unnormalized generating functional whose event probabilities reproduce the Admissibility distribution. |
| Outcomes that do not count | More rank scans, positivity of one imposed compression, determinant factorization alone, or owner adoption silently treated as derivation. |

### N1 — alternative-route enumeration

The family labels use the tuple `(primary object; mechanism; terminal
obligation)` rather than agent, notation or artifact type.

| Family | Honesty marker | Attempt and why it does not close the target under the allowed premises | Authority/evidence |
|---|---|---|---|
| Raw full-source functional; Gaussian differentiation; positive reflected kernel | `ATTEMPTED` | Differentiation fixes `G` and its permanent tower, but the displayed raw `K` is non-Hermitian with anti-Hermitian rank `8` on all four cells, so this full inherited support does not furnish the required positive event domain. | Current runner `FULL_SOURCE_BOUNDARY`; the approved baseline explicitly leaves source/action and physical-observable identification open (`MINIMAL_AXIOMS_2026-06-29.md:173-188`). |
| Symmetry-selected compression; period-two translation; unique physical `X` | `ATTEMPTED` | `X^dag K X` is positive and dial-sensitive, but every weight pair `(u,v)` has the same translation intertwining and the displayed subspace leaks under `r`, `Q` and the action form; the symmetry does not select the weights or identify Record events. | Current runner `PERIOD_TWO_DOES_NOT_SELECT_WEIGHTS` and `X_NOT_SELECTED_BY_INVARIANCE`; choices not fixed by supplied structure remain conditional (`MINIMAL_AXIOMS_2026-06-29.md:85-90`). |
| Hermitianized/action-side kernel; real-part or action substitution; source-functional identification | `ATTEMPTED` | Hermitianization produces a matrix but is not the derivative of `exp(barJ GJ)`, and the action-side form is a different object; either requires a separately justified source/observable bridge. | Current runner `SOURCE_TWO_POINT` and `FULL_SOURCE_BOUNDARY`; the source/action bridge is outside axiom content (`MINIMAL_AXIOMS_2026-06-29.md:140-146,187`). |
| One-copy unnormalized functional; multiply by `Z_Q`; positive dial-sensitive vacuum leg | `ATTEMPTED` | This route **succeeds for degree zero** at the four fixtures and defeats the broader vacuum negative: `det Q>0` at both dials and changes exactly. It rescales all algebraic coefficients but does not Hermitianize the raw higher-sector kernel, identify `|Z_Q|^2`, or select the physical source domain. | Current runner `ONE_COPY_VACUUM_RESPONSE`, `VACUUM_CATEGORY_SPLIT` and `FULL_SOURCE_BOUNDARY`; no Born/readout selection is supplied at `MINIMAL_AXIOMS_2026-06-29.md:140-150,173-187`. |
| Doubled/reweighted functional; `F_Q=|Z_Q|^2 exp(barJ GJ)` or two independent copies; common sector sewing | `ATTEMPTED` | The first definition is algebraically consistent but rescales every sector; the genuine doubled product is bigraded. Neither construction is selected as the physical probability law by the current foundation. | Current runner `VACUUM_CATEGORY_SPLIT`; the complete foundation rule is `MINIMAL_AXIOMS_2026-06-29.md:108-112` and the registry is `docs/audit/data/axiom_premise_nodes.json:1-49`. |
| Effect-algebra route; complete event partitions plus noncontextual refinement/additivity; trace/Born representation | `ATTEMPTED` | Repository scan finds conditional trace-forcing theorems, but the current axioms do not supply the full eligible effect/event domain, context selection or additivity needed to apply them to this source functional. The route remains live rather than ruled out. | `BORN_FORM_EFFECT_MENU_SITEWISE_FORCING_AND_PRODUCT_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md` is currently unaudited; the retained foundation boundary is `MINIMAL_AXIOMS_2026-06-29.md:140-150,173-187`. |

Six materially distinct families were examined. The live one-copy and effect-
algebra routes force the result to remain a partial narrowing, not a no-go.

### N2 — wall-independence audit

After the one-copy correction, the collapsed wall set has three members:

- `W_E`: derive the physical linear event/source domain and Record-to-source map;
- `W_R`: derive the field-level reflection/source convention and positivity on
  that domain;
- `W_D`: if the doubled candidate is kept, derive the rule identifying
  `|Z_Q|^2` with the one-copy tower or replace that tower explicitly.

| Pair | Close first implies second? | Close second implies first? | Independent? |
|---|---|---|---|
| `W_E`, `W_R` | No: an event domain need not carry the required reflection. | No: a reflection can be defined on an imposed algebra without making it the Record event domain. | Yes |
| `W_E`, `W_D` | No: identifying physical events does not select one-copy versus doubled normalization. | No: an algebraic doubling rule does not identify physical Record events. | Yes |
| `W_R`, `W_D` | No: reflection covariance does not choose a partition/source normalization. | No: doubling or reweighting does not make the raw kernel Hermitian-positive. | Yes |

The earlier “positive dial-sensitive vacuum” wall is removed: `Z_Q` closes it
on these fixtures. Physical interpretation of `s_t` and exhaustiveness of the
action family are scope exclusions, not additional walls in this claim.

### N3 — hidden-wall scan

The note was searched for the skill's full phrase list and close variants.

| Search hit | Location | Classification | Disposition |
|---|---|---|---|
| `registered` / `registration` | standing, scope fences and this gate | Cited foundation boundary or non-load-bearing status language | Kept with `axiom_premise_nodes.json:1-49` and each registry `current_path` as authority; no construction is promoted. |
| `construction` | doubled functional and parent descriptions | Non-load-bearing mathematical option | Annotated as a definition or conditional construction, never as supplied physics. |
| `framework` | statements about what the current foundation selects | Cited authority | Narrowed to the explicit Open Gates in `MINIMAL_AXIOMS_2026-06-29.md:173-188`. |
| `we assume`, `by construction`, `as is standard`, `the framework provides`, `bridge context`, `background`, `naturally`, `obviously`, `standard QFT`, `canonical` | no load-bearing hit | No hidden condition found | No new wall promoted. |

The imported Gaussian, carrier, action, reflection matrix, support, dials and
`X` remain conditional finite-fixture inputs. The complete primitive-registry
check also confirms that scale reference, kinetic isotropy and realized-state
evaluation supply no event/source selector, readout bridge, weighting or
normalization rule.

### N4 — residual matching

| Cited witness | Witness residual | Residual used here | Match? / disposition |
|---|---|---|---|
| `MINIMAL_AXIOMS_2026-06-29.md:140-150,173-188` | Source/action, context selection, Born values and extra readout rules lie outside axiom content. | Whether the supplied foundation already selects `W_E`, `W_R` or `W_D`. | **Yes**; retained foundation boundary. |
| Block 107 note line `4` and runner lines `329-347` | Displayed `K_ab=conj(G(b,theta a))` equation and its implemented index order. | Which raw kernel that displayed convention produces. | **Yes for orientation only**; it is not cited as a physical field-reflection selector. |
| Block 170 runner lines `137-146` | Gaussian covariance `G=Q^-1`; `Theta(A)=r conj(A) r` is a construction of that block. | Covariance object and absence of a supplied linear-field `Theta`. | **Yes at construction scope**; no all-reflections conclusion is taken. |
| Block 176 note lines `205-218` | `Z(Q)Z(Q^dag)` is a partition-function-level pairing rather than a field-configuration pairing. | Category of the doubled `|Z_Q|^2` candidate. | **Yes**; no claim is made that Block 176 disproves a one-copy vacuum. |
| Block 177 runner lines `516-537` | `Sym^n` direct-sum identification is named as a premise and its vacuum readout is separately imposed. | Whether Block 177 supplies a `|Z_Q|^2`-to-`Sym^0` sewing premise. | **Yes only for the doubled identification**; dropped as evidence against positive one-copy `Z_Q`. |
| Block 178 note lines `201-224` | `X` falsifies an action-side rank-one-only thesis. | Positivity of `X^dag K X` for the raw covariance kernel. | **No as a witness**; Block 178 is kept only as provenance for `X`, and the covariance result is recomputed directly by this runner. |

After the nonmatching use of Block 178 and the overbroad vacuum use of Block
177 are dropped, the current exact recomputation plus the retained foundation
boundary still support the narrowed statement. No prior no-go is used as a
substitute for this calculation.

### N5 — rhetoric audit and resolution level

| Resolution | Executed? | Narrow result |
|---|---|---|
| per element | Yes, symbolic | Source differentiation fixes `G`; degree two is the permanent; normalized, one-copy and doubled coefficients are distinct. |
| per site | Yes, four exact finite cells | The full eight-source raw kernel is non-Hermitian, while one imposed rank-two restriction is positive. |
| per mode | Yes, two exact dial values at two extents | The rank-two half-trace and `det Q` change; physical interpretation of the dial is not executed. |
| per block | Yes, direct parent-object comparison | Block 179 derives the algebraic Wick part of B2b, detects the Block-107 transpose mismatch, and repairs the vacuum accounting. |
| lattice wide | Checked and not executed — two extents and two dials are not a limit or complete source-algebra census. | No continuum, all-action, universal OS or physical-event theorem. |
| whole TOE | Checked and not executed — audit retention and end-to-end obligation closure are outside this packet. | Zero axiom or obligation retirement and zero percentage movement. |

The five required execution-certificate lines land in
`logs/runner-cache/admissibility_dirac_kahler_source_functional_grading_boundary_2026_08_23.txt`.
Safe wording is: **“The supplied Gaussian forces a raw permanent tower; at the
four fixtures a positive source restriction and a positive dial-sensitive
one-copy vacuum exist, but the physical source domain and the specific doubled
readout identification remain unselected.”** The universal phrases “no
positive grading exists” and “no positive dial-sensitive same-tower vacuum
exists” are withdrawn.

### N6 — partial-closure path scan

The primitive-registry check was run before any supply claim. The complete
allowlist contains `minimal_axioms`, scale reference, kinetic isotropy and the
realized-state primitive. Their current source notes supply respectively the
four-axiom baseline, units, `c_t=c_s`, and pointwise realized-state evaluation;
none supplies a source selector, field reflection, readout bridge, probability
weighting or normalization rule. They are approved premises, not walls, and no
primitive is misclassified here.

| Candidate path | Current status | What it would close | What remains |
|---|---|---|---|
| Use the unnormalized one-copy `Z_Q exp(barJ GJ)` | Executed exactly in this block | Positive, dial-sensitive degree-zero leg at the four fixtures | The raw higher sectors remain non-Hermitian; `W_E`, `W_R`, and any desire to use specifically `|Z_Q|^2` remain |
| Define `F_Q=|Z_Q|^2 exp(barJ GJ)` | Available mathematical reweighting, not adopted | Algebraic common-tower bookkeeping for the doubled scalar | Why Nature/Admissibility chooses it; every sector is rescaled |
| Use a genuine doubled functional with independent sources and sew its bigrading | Unexecuted conditional construction | A literal amplitude-times-conjugate field theory | The sewing map, positive event domain and Record interpretation |
| Block-176 reflection-pairing candidate | Open PR #7330; content-bound unaudited and explicitly a candidate | Could provide an owner-adopted doubled readout convention | Adoption is not derivation and does not close `W_E` or `W_R` |
| Full finite-effect-partition trace theorem | Landed source, current audit status `unaudited` | Conditional trace/Born form once a full eligible event algebra and grading are supplied | Physical event-domain eligibility and source connection |
| Record program compiler #7316 | **Open**; exact carrier/trace compiler, explicitly conditional | Encodes supplied preparation and binary/ternary programs | Same-law writer/genesis, physical calibration and trace-law selection remain open |
| Record writer/formation/menu chain #7319-#7324 | **Open**; homogeneous writer, birth process, spatial trials and continuum low-arity menus | Supplies substantial conditional scaffolding toward a physical event domain | Preparations, formation laws, trace branch and setting coverage are selected content rather than derived source/reflection authority |
| W1 nonselection #7325 | **Open** bounded countermodel | Proves equal support/rate does not select cross-program effect functionality | Leaves a selected action/current/joint theorem live; it does not close `W_E` or `W_R` |
| Marked Gaussian Record law #7326 | **Open** selected-law construction | Gives an explicit event quotient, refinement pushforward and source-to-event bridge, so it is the closest conditional model of `W_E` | Its Gaussian action, additive source, clock calibration and bridge are expressly not derived from the four axioms |
| Amplitude/effect pincer #7317-#7318 | **Open** conditional parent chain | Shows the amplitude-level and effect-level readout gaps meet at one interface object | Identifies the question but does not select the readout law |
| Schur Record response #7327 | **Open** bounded theorem | Derives positive action-side precision and local trace response | Joint alternative ensemble and physical Record event/clock/write bridge remain open |
| Joint Record sector #7328 | **Open** bounded construction | Gives one positive joint partition/conditional object | Per-arm calibration, alternative base measure and physical sector selection are imposed/open |
| Gaussian dilation #7329 | **Open** bounded construction | Proves finite algebraic realization of the joint interface | Physical nearest-neighbor realization, auxiliary ontology, source/event/clock selection and autonomous write remain open |
| Current newest stack #7330-#7333 | **Open** on 2026-08-23 | Supplies the conditional complex/readout parents, rank-two falsifier and finite locality compiler used or checked here | No PR in the full #7316-#7333 inventory ratifies a primitive, derives the field reflection, or positively retains an end-to-end law |

An explicit reweighting can retire an accounting wall as a convention; it is
not called a new axiom. A physical event/source selector may come from a
retained derivation, an owner-approved primitive/law update, or a different
end-to-end construction. The open Record chain contains several serious
conditional constructions—especially #7326—but none is silently treated as
retained authority or as closure of `W_E`/`W_R`. Future PRs must be rechecked.
This note chooses none of those governance outcomes.

### N7 — hostile-reviewer steelman

The strongest objection is constructive: **this packet is already closer to a
positive theorem than its boundary language suggests.** The unnormalized
one-copy Gaussian supplies a positive, dial-sensitive degree-zero coefficient,
the exact `X` restriction proves that a positive transport-responsive source
sector exists, and Admissibility already supplies a neighboring-condition-
dependent probability distribution while Record locks one supported result
(`MINIMAL_AXIOMS_2026-06-29.md:55-83`). A presentation-invariant
Record-to-effect map could therefore select a positive domain; complete
effect-partition refinement/additivity could force a trace representation; and
an explicit doubled functional could then be tested rather than assumed. This
is a concrete mechanism that defeats every universal no-go. **Terminal obligation:** construct the Record/event map `D_eta`, a field reflection
`Theta_D` for which the raw covariance functional is positive on `D_eta`, and a
normalization/sewing map whose event weights equal the Admissibility measure.
Until that terminal obligation is attempted, only partial narrowing is honest.

### N8 — cross-cycle echo

The prescribed docs phrase search and a walk of physics-loop
`NO_GO_LEDGER.md` files were run. The directly similar rows are:

| Prior file | Similar wall | Retired since? | Mechanism and applicability here |
|---|---|---|---|
| `.claude/science/physics-loops/post-record-selector-supplied-boundary-20260608/NO_GO_LEDGER.md:3-5` | Finite SPD/normalization arithmetic is not selector authority. | No | Applies directly: positive `X` and positive `Z_Q` are existence results, not physical selection. |
| `.claude/science/physics-loops/toe-axiom-closure-block176-complex-structure-synthesis-20260823/NO_GO_LEDGER.md:10-24` | `|det Q|^-2` is a partition-level candidate, not a derivation. | No | The candidate remains live; this block separates it from the one-copy tower rather than rejecting it. |
| `.claude/science/physics-loops/toe-axiom-closure-block177-conditional-symmetric-power-20260823/NO_GO_LEDGER.md:11-44` | Covariance/action mismatch and conditional sector uniqueness. | **Partly** | Raw Wick grading is now derived and its vacuum leg is repaired with `Z_Q`; the higher-sector Hermitianization premise, physical domain/reflection and doubled-readout selection remain. |
| `.claude/science/physics-loops/toe-axiom-closure-20260809/NO_GO_LEDGER.md:19` | A supposed type-capacity wall. | Yes, by an explicit injective encoding | Shows that a definition/refactor can retire algebraic capacity without new physics; likewise explicit sewing can retire bookkeeping, but not select Nature's law. |
| `.claude/science/physics-loops/toe-axiom-closure-20260809/NO_GO_LEDGER.md:186-193` | Broad “normalization makes gravity impossible” reading. | Yes, by a null-anchor repair | The analogous repair was searched here and found: one-copy `Z_Q` defeats the broad vacuum claim. It does not close the independent selector walls. |

Other docs-search hits concerned different residuals—gravity contact/source
maps, historical review notes or label-only no-gos—and were dropped under N4
rather than counted as support. No prior retirement mechanism was ignored.

Gate result: **PASS for the narrowed partial-boundary claim**. The broader
negative “there is no positive, dial-sensitive vacuum in the Gaussian's own
tower” **failed**, was demoted, and is withdrawn. The packet ships only exact
positive identities, four-cell boundaries and named live routes; it ships no
universal no-go.

## Decision cut

Bank the source derivation, the positive subspace and the repaired one-copy
vacuum leg. Block 177 can use positive `Z_Q` for degree zero, but its particle
sectors still require the separately stipulated Hermitianized/action kernel;
do not call the raw one-copy tower a Hermitian graded sum. Do not spend the main
campaign on another unrestricted compression or sector scan. Do not edit the
minimal axioms yet: their Open Gates already correctly withhold Born weights
and source/observable identification, and this result does not choose which
additional law Nature uses.

If the readout lane resumes, require one of two theorem-shaped supplies first:

1. a presentation-invariant physical event/source algebra plus field
   reflection; or
2. a complete event-refinement/additivity theorem that selects squared
   amplitude.

If the readout must be `|Z_Q|^2` rather than the already viable one-copy `Z_Q`,
also require an explicit doubled-functional or reweighting/sewing rule.

Until then, the main science budget moves to the independent Wilson-`Q`
discriminator.

**TOE:** zero axiom retirement; zero obligation retirement; zero TOE percentage
movement; retained-positive end-to-end theory count remains zero.
