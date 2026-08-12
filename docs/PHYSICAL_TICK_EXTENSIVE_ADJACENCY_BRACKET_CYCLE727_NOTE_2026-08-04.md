# Exact declared spatial-pair charge bracket in a supplied two-slab model — Cycle 727

Date: 2026-08-04

Claim type: bounded_theorem

Status: proposed_retained

Authority: none. Audit status is set only by the independent audit lane.
Constitutional effect: none. This note edits no axiom, foundation,
Qualification, primitive, premise registry, policy, queue, or audit verdict.

The result is an exact finite theorem of a **supplied** structural model. The
model is one spatial unit cube crossed with two equal slab intervals, using its
24 corners; a piece is a normalized-volume-one corner 4-simplex; a dissection
is 48 such pieces with disjoint interiors and total normalized volume 48; and
the declared charge counts the ten vertex pairs whose spatial `L1` separation
exceeds one while assigning zero charge to slab-coordinate separation. The
framework does not select that piece class or charge functional.

**Primary runner:**
[`scripts/physical_tick_extensive_adjacency_bracket_cycle727_2026_08_04.py`](../scripts/physical_tick_extensive_adjacency_bracket_cycle727_2026_08_04.py);
cached stdout
[`logs/runner-cache/physical_tick_extensive_adjacency_bracket_cycle727_2026_08_04.txt`](../logs/runner-cache/physical_tick_extensive_adjacency_bracket_cycle727_2026_08_04.txt);
paired receipt
[`outputs/physical_tick_extensive_adjacency_bracket_cycle727_2026_08_04_receipt_2026-08-04.json`](../outputs/physical_tick_extensive_adjacency_bracket_cycle727_2026_08_04_receipt_2026-08-04.json).

**Independent checker:**
[`scripts/physical_tick_extensive_adjacency_bracket_cycle727_independent_check_2026_08_04.py`](../scripts/physical_tick_extensive_adjacency_bracket_cycle727_independent_check_2026_08_04.py);
cached stdout
[`logs/runner-cache/physical_tick_extensive_adjacency_bracket_cycle727_independent_check_2026_08_04.txt`](../logs/runner-cache/physical_tick_extensive_adjacency_bracket_cycle727_independent_check_2026_08_04.txt).
It does not import the primary. It pins the primary source, re-enumerates the
finite geometry with separate exact determinant and cofactor code, rebuilds all
sample-point memberships and both certificates, verifies the four carried
dissections, exercises hostile controls, reruns the primary, and requires the
committed receipt to equal the live receipt.

```yaml
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "separate a finite declared spatial-pair charge theorem from any framework-selected tick geometry or physical assembly cost"
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: runner_certificate
next_trace_action: "derive or reject the slab realization, piece-class selection, and charge-functional bridges before any physical or longer-run interpretation"
```

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "exact finite arithmetic for the supplied two-slab corner-simplex model and declared spatial-pair charge"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "both bounds and both attaining witnesses are exact over a finite, explicitly supplied model; none of its physical identifications is derived"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact target and obligation graph

**Exact target.** Bound the declared spatial-pair charge over every dissection
of `{0,1}^3 x {0,1,2}` into normalized-volume-one corner 4-simplices, and
exhibit a dissection attaining each bound.

**Obligation graph.** A enumerates all five-corner subsets and selects the
17,280 unimodular pieces. B assigns the declared spatial-pair and diagnostic
slab-span charges. C builds 364 piece orbits and 17,472 boundary-free sample
points. D checks the floor and ceiling multiplier inequalities on every piece.
E verifies the two 48-piece attaining families by exact volume and exhibited
separating normals. F repeats the one-slab control in the same execution. The
independent checker reconstructs A–F without importing the primary and binds
the live receipt.

**Strongest missing lemma.** No framework principle selects corner 4-simplices
as assembly cells or selects zero charge for separation in the slab coordinate.
Nor is the slab coordinate identified with a physical rule tick. Therefore the
finite theorem is not a physical cost law and has no automatic multi-cell,
longer-run, boundary-free, or continuum extension.

## Premise accounting

- The **Lattice** axiom in the
  [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) supplies the spatial `Z^3`
  nearest-neighbour adjacency used to label a spatial pair as one-step or
  exceeding-one-step. It does not supply a time direction, a simplex complex,
  or a cost functional.
- The registered
  [kinetic-isotropy primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
  supplies equal tick/edge graining only. It does not identify a rule variation
  with a physical tick, select the finite box, or force the slab coordinate to
  carry zero charge.
- The corner set, minimal-volume piece restriction, dissection definition, and
  declared charge are explicit **model inputs introduced here**.
- The landed
  [Cycle 725 theorem](PHYSICAL_EXACT_ADJACENCY_DISSECTION_BRACKET_CYCLE725_NOTE_2026-08-03.md)
  is the direct one-slab dependency and provenance for the model boundary and
  comparison `[108,128]`. This runner also remeasures both one-slab endpoints,
  so the numerical doubling does not trust a copied value.

## Exact finite result

Normalized volume means
`|det(v_1-v_0, ..., v_4-v_0)|`, equal to `4!` times Euclidean
4-volume. The two-slab box has normalized volume 48, so a dissection by
normalized-volume-one pieces has exactly 48 pieces.

Among the `C(24,5)=42,504` five-corner subsets, the exact normalized-volume
spectrum is:

| volume | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|---:|
| subsets | 13,152 | 17,280 | 9,840 | 1,472 | 680 | 64 | 16 |

The declared spatial-pair charge on the 17,280 minimal pieces has spectrum
`{3:432, 4:2592, 5:7488, 6:4896, 7:1872}`. Piecewise counting alone would give
only `[144,336]` for a 48-piece family.

The exact theorem is:

> Over every dissection in the supplied minimal-volume corner-simplex class,
> the declared spatial-pair charge lies in `[216,256]`, and both endpoints are
> attained.

The proof uses one boundary-free sample point per piece orbit carried around the
48-element box group (24 proper spatial rotations times slab reversal). This
gives 17,472 distinct points in 364 point orbits, 48 points per orbit. Every
point is tested against every minimal piece with exact integer barycentric
numerators; boundary incidences are zero.

For piece `p`, let `BO[p,o]` count interior sample points from point orbit `o`,
and let `BX[p]` be its declared charge. If integer orbit multipliers `u`, a
constant `Z`, and a positive denominator `D` obey

`BO[p] · u + Z <= D BX[p]`

on every minimal piece, summing over any dissection gives the lower bound
`48(sum(u)+Z)/D`. Reversing the inequality gives the upper bound. The primary
and independent checker both verify every uncompressed piece inequality.

- Floor certificate: `D=2`, `sum(u)+Z=9`, least slack 0, tight on 13,392
  pieces, hence `48*9/2=216`.
- Ceiling certificate: `D=288`, `sum(u)+Z=1536`, least slack 0, tight on 6,336
  pieces, hence `48*1536/288=256`.
- Endpoint witnesses: each has 48 unimodular pieces, normalized volumes sum to
  48, and all 1,128 piece pairs have an exhibited separating integer normal.
  Their charges are 216 and 256.

The one-slab controls have 2,672 minimal pieces and 24-piece attaining
dissections of charges 108 and 128. Thus both observed endpoints double for
this two-slab box. This is a finite equality at slab counts one and two, not a
law for arbitrary slab count.

## Diagnostic slab-span charge

The runner separately counts vertex pairs whose slab-coordinate separation
exceeds one. That diagnostic charge has spectrum
`{0:5344, 1:1744, 2:4944, 3:3040, 4:2208}`. It vanishes exactly on the 5,344
slab-confined minimal pieces; 11,936 pieces cross the middle slab. Both
attaining spatial-pair-charge witnesses happen to be slab-confined.

This diagnostic makes the model choice visible. The theorem's declared charge
is not the sum of the spatial-pair and slab-span charges, and the framework does
not force either functional. A later nonzero slab weight defines a different
optimization problem.

## Independent and hostile evidence

The independent checker performs a second exact enumeration, reconstructs the
48-element action and all 364 orbits, regenerates all 17,472 point numerators,
recomputes the full 17,280-by-364 membership matrix, and checks both certificates
and all four witnesses. It pins the primary source SHA-256 and verifies that the
committed receipt equals the primary's live receipt byte-for-value after JSON
decoding.

Its landed hostile controls alter four different mechanisms: the spatial-cost
threshold, the floor constant, the ceiling denominator, and one endpoint-witness
corner. Each is rejected. Review-time direct-source mutations additionally
require the primary and checker processes to return nonzero and forbid a
positive terminal verdict; those executions are review evidence, not silently
promoted into a broader theorem.

## Boundary and honest read

- The bracket is exact only for this 24-corner, two-slab box and the 17,280
  normalized-volume-one corner 4-simplices.
- Coarser corner pieces, added vertices, nonsimplicial cells, larger spatial
  blocks, more slab intervals, alternative boundary conditions, and continuum
  limits are not covered.
- The declared spatial-pair charge ignores slab-coordinate separation. That is
  a model definition, not “the axiom's own asymmetry.”
- The physical rule-to-tick bridge and the identification of physical assembly
  cells with the supplied simplices remain open.
- No metric, action, curvature, field equation, framework model-selection rule,
  or physical cost law is derived.
- No `no_go` claim ships. Named open walls below prevent an overbroad negative
  reading of this positive finite theorem.

## Review record

Iteration 1 of combined adversarial science review (Sol, 2026-08-12) returned
FIX_THEN_PROCEED on the submitted packet. The submitted wording incorrectly
called zero slab-coordinate charge an axiom-imposed asymmetry; it is now an
explicit model choice. The raw cold output was not a canonical cache, the
runner returned exit 0 after red gates, the receipt was unbound and not emitted,
the note lacked required claim/status/trace surfaces and real dependencies, and
several claimed off-artifact cross-checks had no landed implementation. The
repair makes all primary arithmetic exact and fail-closed; adds a source-pinned
independent checker, content-bound receipt, canonical caches, harness and graph
integration; removes uncarried claims; and lands the N1–N8 discipline record.
Audit remains unset and no audit verdict data is edited.

## No-Go Discipline Gate

This is the committed N1–N8 record for the bounded theorem's named walls. It
does not turn the positive finite result into a no-go.

**N1 — Alternative route enumeration.** Every enumerated route has an explicit
marker.

1. Exact subset route: **ATTEMPTED** — the primary and independent checker use
   separate determinant/cofactor implementations to enumerate all 42,504
   subsets and reproduce the full volume and charge spectra.
2. Dual-certificate route: **ATTEMPTED** — both implementations check every
   floor and ceiling inequality over all 17,280 minimal pieces, without trusting
   orbit representatives alone.
3. Primal-witness route: **ATTEMPTED** — four carried one- and two-slab families
   are checked by exact normalized volume, charge, and a separating normal for
   every piece pair.
4. Seam-crossing route: **ATTEMPTED** — all 11,936 seam-crossing minimal pieces
   are included in both certificate sweeps; they are not removed by a stacked
   ansatz.
5. Sample-device route: **ATTEMPTED** — all 17,472 pinned sample points are
   tested against every piece, zero boundary incidences are required, and the
   independent checker rebuilds the membership matrix.
6. Alternative-charge route: **ATTEMPTED** — the complete slab-span spectrum is
   computed separately. It confirms that a nonzero slab charge changes the
   problem and remains outside the theorem rather than being rhetorically
   excluded.

**N2 — Wall-independence audit.** Four open walls are named: TR (physical
rule-to-tick realization), PS (framework selection of corner-simplex pieces),
CF (framework selection of the charge functional, including slab weight), and
EX (coarser/noncorner/nonsimplicial/multi-cell/longer-run/continuum extension).

| wall pair | independence witness |
|---|---|
| TR / PS | A tick realization could be supplied without selecting simplicial cells; a simplicial model could be studied with no physical tick realization. |
| TR / CF | A realized clock does not choose a cost functional; a declared functional can be evaluated on an abstract slab coordinate. |
| TR / EX | Realizing one tick does not prove arbitrary-run or continuum extension; finite extension can be studied without a physical clock. |
| PS / CF | Selecting simplices does not assign their pair charges; the same charge can be evaluated on other cell classes. |
| PS / EX | A one-box simplex theorem does not select larger domains; larger finite simplex boxes do not settle nonsimplicial selection. |
| CF / EX | Fixing a charge does not prove its asymptotics; extending the domain does not force zero or nonzero slab weight. |

**N3 — Hidden-wall scan.** The note and both runners were scanned for universal,
physical, axiom-forced, arbitrary-run, continuum, and model-selection wording.
The original “axiom's own asymmetry” sentence was removed. Denominator statements
refer only to these certificates' exact values; symmetry refers only to the
finite box action; “exact” refers only to integer arithmetic on the supplied
finite objects.

**N4 — Residual matching.** Cycle 725's residuals — tick realization and
simplex identification — remain TR and PS here. The new zero-slab-weight choice
is separately exposed as CF. The two-slab calculation closes no Cycle 725
residual beyond evaluating one additional finite box. No dependency audit status
is inherited.

**N5 — Rhetoric audit.** The primary emits a five-line resolution certificate.
`per_element` covers every subset, piece, charge, and certificate inequality;
`per_site` covers every point-piece incidence; `per_mode` covers all 364 orbits
and both multiplier vectors; `per_block` separates the one- and two-slab boxes;
`lattice_wide` is explicitly checked and not executed. The canonical primary
cache preserves these lines.

**N6 — Partial-closure paths.** TR can close through a rule-to-clock
construction; PS through a framework-derived cell complex; CF through an action
or resource law selecting pair weights; EX through new finite enumerations or an
analytic gluing/subadditivity theorem. These routes are independent and none is
claimed closed here.

**N7 — Steelman.** The strongest counter-reading is that a valid physical model
might use coarser or nonsimplicial cells, added vertices, or a nonzero slab weight
and therefore have costs outside `[216,256]`. The packet accepts that objection:
such models are outside the quantified class. The finite certificate remains
valid because it never quantifies over them.

**N8 — Cross-cycle echo.** Cycle 723 and Cycle 724 already distinguish supplied
corner/stencil calculations from framework selection; Cycle 725 explicitly
leaves tick realization and simplex identification open; Cycle 726 studies a
different declared facet-charge model. This note preserves those boundaries and
does not turn repeated finite evidence into an axiom, a model-selection theorem,
or an arbitrary-size law.

**Status: PASS.** Every enumerated N1 route is ATTEMPTED, all six wall pairs are
audited, the hidden-wall and rhetoric scans are explicit, partial closure and the
steelman remain live, and no no-go is shipped.
