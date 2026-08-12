# Physical Mixed-Frame Comparator: a Bounded Exact Stencil Swap Identity at L = 3 and L = 7 — Cycle 711

Date: 2026-08-02

Claim type: bounded_theorem

Status: proposed_retained

Authority: none. Audit: unset. Constitutional effect: none. This cycle edits no
axiom, foundation, Qualification, primitive, registry, policy, queue,
audit-status, or PR-control surface. No new axiom or primitive is proposed or
adopted.

**Primary runner:**
[`scripts/physical_mixed_frame_comparator_exact_stencil_swap_law_cycle711_2026_08_02.py`](../scripts/physical_mixed_frame_comparator_exact_stencil_swap_law_cycle711_2026_08_02.py);
cached stdout
[`logs/runner-cache/physical_mixed_frame_comparator_exact_stencil_swap_law_cycle711_2026_08_02.txt`](../logs/runner-cache/physical_mixed_frame_comparator_exact_stencil_swap_law_cycle711_2026_08_02.txt);
paired receipt
[`outputs/physical_mixed_frame_comparator_exact_stencil_swap_law_cycle711_2026_08_02_receipt_2026-08-02.json`](../outputs/physical_mixed_frame_comparator_exact_stencil_swap_law_cycle711_2026_08_02_receipt_2026-08-02.json).

```yaml
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the in-flight Cycle-710 finite covariance-boundary census measured a mixed-frame comparator near 4 but supplied no exact stencil derivation"
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: runner_certificate
next_trace_action: "consume the exact two-incidence stencil identity only after Cycle 710 lands, then seek an arbitrary-size incidence-count proof; the present result covers only L = 3 and L = 7"
```

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "the exact identities and finite censuses are conditional on the declared Cycle-696 compiler-source closure and its supplied LT = 2 and finite-difference step; they are established only on the stated templates and box sizes"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "finite exhaustive frame and incidence scans at L = 3 and L = 7, combined with exact symbolic differentiation for the two stated simplex configurations; census counts and off-integer witnesses remain measured"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

Finite, recomputed statements about the landed
Cycle-696 open-coframe endpoint compiler chain at box sizes L ∈ {3, 7}. The
substitution dichotomy, the two-incidence stencil decomposition, and the exact
per-simplex value −1 are exact (integer combinatorics and symbolic computation);
the swap structure of the argmax family is exact at stencil level with a
finite-difference provenance certificate; the frame-uniform census counts are
measured, not derived.

## What Cycle 710 left open

The Cycle-710 covariance-boundary census (stem
`PHYSICAL_ASSEMBLY_DEFECT_COCYCLE_LAW_AND_COVARIANCE_BOUNDARY_CYCLE710_NOTE_2026-08-02`,
in flight) measured the assembly defect E_g = Π_g^T Q Π_g − Q of the static
Hessian under the 24 proper-rotation frames and found its ceiling at every mixed
frame to sit within 2.0e-08 of the integer 4 — recorded there as measured, not
derived. This cycle derives that integer. The comparator is the exact stencil
value

    |LT × (−1 − 1)| = 4,

carried by a two-incidence face-diagonal stencil whose per-simplex mixed second
derivative is exactly −1 at the flat background, and the transport permutation
attains it by swapping that entry against an exactly-zero shared-vertex entry.
These are computational identities of the landed compiler chain.

## Setup

The compiler chain is the landed Cycle-696 static-sector assembler: path-simplex
templates on the open box, spatial edge classes (axis, face-diagonal,
body-diagonal), and the assembled static Hessian Q with matrix elements
LT × Σ (local per-simplex Hessians), where the tick multiplier LT = 2 and the
central finite-difference step 1.0e-04 are supplied compiler constants, not
fitted values. Frames are the 24 proper cubic rotations of the landed
Cycle-576 table.

The transport permutation Π_g is the bounding-box dof relabeling: a degree of
freedom (class c at site x) maps to the class of |R v_c| at the translated site,
where the translation subtracts the negative part of R v_c so that every rotated
edge is re-anchored at its bounding-box corner. The defect is E_g = Π_g^T Q Π_g − Q.

**Substituted class.** Call class c *substituted at frame R* when R v_c has
mixed signs — equivalently, when the canonical bounding-box representative of
the rotated edge differs from the geometric rotated edge by the re-anchoring
translation. This is the single combinatorial notion the whole cycle runs on.

### Imported compiler contract

Load-bearing source input: the landed
[`physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py`](../scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py)
and its four transitive local imports, all byte-bound through the primary
runner's `AUDIT_INPUT_PATHS`. This is supplied computational structure, not a
new framework primitive; this note does not derive its template set, tick
multiplier, or finite-difference convention.

- `assemble_static_hessian(L, wrap=False)` — the assembled Q and its dof index.
- `simplex_local_hessian(p, step)` — per-template local Hessian at supplied FD step.
- `frame_site_map(L, R)` — the site relabeling of the open box under frame R.
- `CELL`, `SPATIAL_CLASSES`, `CLASS_ELL` — templates, spatial classes, edge lengths.
- Supplied constants: LT = 2, FD step 1.0e-04 (both printed and gated by the runner).

## Claims

**Exact target.** On the declared Cycle-696 compiler bytes, templates, and
constants, prove for every mixed frame at L = 3 and L = 7 that each measured
argmax defect entry is the transport swap of an assembled zero with an assembled
`-4` whose two local incidences each have exact symbolic mixed derivative `-1`.

**Obligation graph.** T1's finite frame classification is proved here by all-24
enumeration. T2's representative incidence count is proved here by an exhaustive
open-box template scan, and its two local derivatives are proved symbolically.
For T3, the runner independently derives all 48 unordered L = 3 entries in the
measured `-4` family, finds all three complementary face-diagonal class pairs and
all 12 translated local template/slot configurations, and proves the derivative
`-1` symbolically for every configuration; the L = 3 and L = 7 argmax scans then
gate that their nonzero sides use all and only those exact configurations. T4 is
a measurement only. The strongest missing lemma is an arbitrary-L incidence and
boundary-count classification; neither arbitrary size nor a census formula is
proved here.

### T1 — Substitution dichotomy (exact)

Over all 24 frames:

1. the substituted set is empty exactly on the constant-sign sextet
   {1, 4, 9, 15, 18, 23} — the frames whose matrix has all nonzero entries of
   one sign — and these are exactly the frames of the Cycle-707 stabilizer
   analysis;
2. every one of the 18 mixed frames substitutes exactly 2 face-diagonal classes
   and 1 body-diagonal class;
3. axis (nearest-neighbor) classes are never substituted at any frame.

So the covariance boundary of Cycle 710 is re-derived combinatorially: a frame
has zero substitution defect exactly when it is constant-sign, and every other
frame carries the same substitution signature (2 face + 1 body).

### T2 — Exact stencil integers (exact)

At L = 3, for the disjoint complementary face-diagonal pair — class 5 at site
(2,1,0) against class 11 at site (1,1,0), whose edges are vertex-disjoint:

1. the pair carries exactly 2 path-simplex incidences,
   (template 0, slots (5,1)) and (template 18, slots (8,5));
2. each incidence has mixed second derivative exactly −1 at the flat background
   (symbolic, see the derivation sketch);
3. the assembled entry equals LT × (sum of the two local values) bit-for-bit,
   hence equals LT × (−2) = −4 exactly at stencil level;
4. the shared-vertex complementary pair — the same two classes both anchored at
   (0,0,0), sharing a vertex — carries 0 incidences and an assembled entry that
   is exactly 0.0.

The stencil family for this pair type is therefore the exact integer set
{0, −4}: which of the two values appears is decided purely by the incidence
count at the pair separation.

### T3 — Swap attainment of the comparator (exact at stencil level)

At every one of the 18 mixed frames, at both box sizes L = 3 and L = 7:

1. every argmax entry of |E_g| (threshold 3.5) is a 0 ↔ 4 magnitude swap: the
   entry pairs a dof pair whose Q-entry is exactly at one stencil value with its
   transported image at the other;
2. every such entry is a face-face pair with exactly one substituted endpoint,
   and the two orientations (first endpoint substituted vs second) occur in
   equal numbers — 1152 each at L = 3, 31104 each at L = 7, summed over frames;
3. the ceiling of |E_g| carries one bit pattern across all 18 mixed frames and
   across both box sizes, and its deviation from 4 is 1.3e-08;
4. the measured deviation is numerically accounted for by the two local
   finite-difference errors: the per-incidence FD error at step h contracts by
   ratio 4.09 and 3.93 when h is halved (second-order central differences
   contract by 4), and the budget LT × (err0 + err1) = 1.3e-08 matches the
   assembled-entry deviation within the gate's `1e-3` relative tolerance.

The exact-family closure is exhaustive for this finite claim: across the three
complementary face-diagonal class pairs, the L = 3 assembler exposes 48
unordered `-4` entries and 12 distinct translated local template/slot
configurations. Every one of those 12 configurations is checked symbolically,
and both box-size scans verify that every argmax nonzero side resolves only to
that same closed configuration set.

Together with T2 this derives the Cycle-710 comparator: the mixed-frame ceiling
is the exact stencil integer 4 = |LT × (−1 − 1)|, attained by substitution
swaps of the {0, −4} family. The finite-difference halving ratios and budget
agreement account numerically for the measured floating deviation without
promoting that attribution to a symbolic equality.

### T4 — Frame-uniform census (measured, not derived)

At each box size, the rounded census of defect entries with |E| > 2 is
identical across all 18 mixed frames:

- L = 3: values ±4: 64, ±3: 224, ±2: 136 per frame;
- L = 7: values ±4: 1728, ±3: 4896, ±2: 4056 per frame;

with census keys exactly {±2, ±3, ±4} and argmax family sizes 128 (L = 3) and
3456 (L = 7) per frame. The counts and the frame-uniformity are measured, not
derived — no counting formula is claimed in this cycle.

## Derivation sketch

**Dichotomy (T1).** The bounding-box canonicalization stores every edge class
by the absolute-value vector |v| and anchors it at the bounding-box corner. A
rotated edge R v needs re-anchoring exactly when R v has mixed signs. For a
constant-sign frame no direction acquires mixed signs; for any other frame the
scan over the 7 spatial classes gives exactly 2 face classes and 1 body class
with mixed signs — verified by complete scan over all 24 frames.

**Vertex-disjointness kills the arc-cosines (T2).** The per-simplex action is a
sum over the ten hinges of area × deficit-angle terms A_hinge · θ_hinge in the
squared-length variables. For a vertex-disjoint slot pair (the two edges share
no vertex of the 4-simplex), differentiating any single hinge term once in each
of the two slot lengths and evaluating at the flat background leaves no
arc-cosine atom: every surviving per-hinge value is a rational number. With the
shared flat squared-length vector (1, 2, 3, 4, 1, 2, 3, 1, 2, 1) in lexicographic
edge order, the surviving per-hinge values are, per hinge pair:

| hinge pair | (0,1) | (0,2) | (0,3) | (0,4) | (1,2) | (1,3) | (1,4) | (2,3) | (2,4) | (3,4) |
|---|---|---|---|---|---|---|---|---|---|---|
| template 0, slots (5,1) | −1/8 | 1/4 | −1/4 | 1/8 | 0 | 1/2 | −1/4 | −3/8 | 1/4 | 0 |
| template 18, slots (8,5) | 0 | 1/4 | −1/4 | 1/8 | −3/8 | 1/2 | −1/4 | 0 | 1/4 | −1/8 |

Each displayed representative row sums to 1/8, and the slot edges are face diagonals of squared length
2, so the mixed second derivative in the two lengths is
4 · √2 · √2 · (−1/8) = −1 exactly, for both incident configurations. The paired
runner certifies the total symbolically and gates every surviving per-hinge
value rational; a wrong-background rejector (one squared length perturbed by 1)
gives exactly −3·√7/7, at distance 1.3e-01 from −1, so the symbolic gate
discriminates. The runner repeats the exact `-1`, rational-hinge, and no-surviving-
arc-cosine test for every one of the 12 configurations; the table shows the two
configurations of the representative T2 pair rather than substituting for that
full enumeration.

**Incidence count (T2).** A complete scan of the path-simplex templates over
the open box at the pair separation gives exactly the two incidences named above for the
disjoint pair and none for the shared-vertex pair; assembly linearity then
fixes the entries to LT × (−2) and 0.

**Swap attainment (T3).** At a mixed frame the transport permutation carries a
face-diagonal dof with one substituted endpoint onto a dof pair at the other
stencil value: the {0, −4} family swaps, so |E| picks up entries of magnitude
exactly 4 at stencil level. The complete scan confirms every argmax entry is
of this form — and only face-face pairs with exactly one substituted endpoint
appear.

## Honest boundary

- **The census counts are measured, not derived.** The per-frame counts
  (64/224/136 at L = 3, 1728/4896/4056 at L = 7, argmax families 128 and 3456)
  and their frame-uniformity are verified by complete scan but no counting
  formula is derived. Deriving the counts is the named next target.
- **Observed both-clean witness.** At each tested size, the scan finds an entry
  in the both-clean block (both endpoints unsubstituted) with magnitude
  2.8e+00, matching 2·√2 within 2.0e-07. This is a positive finite witness at
  L = 3 and L = 7; no conclusion about other sizes or every possible
  localization notion is drawn.
- **Observed off-integer-distance witness.** At each tested size, the largest
  measured distance from an integer over the scanned mixed-frame entries is
  4.6e-01, matching 2·√3 − 3 within 2.0e-07. The exact integer identity in this
  note is restricted to the argmax swap family and its stated stencil values.
- **Exactness lives at stencil level.** The assembled floats carry FD
  truncation and roundoff. Exact status comes from the symbolic closure of all
  12 local configurations; the convergence-ratio and budget gates account for
  the observed floating deviation numerically within their stated tolerances.
- **Scope.** Two box sizes (L = 3, 7), the landed template set, the supplied
  compiler constants. No continuum statement, no statement about other pair
  types' stencil families beyond the {0, −4} face-diagonal family used by the
  argmax law.

## The next paths opened

- **Derive the census counts.** The frame-uniform counts (T4) now sit one step
  above a counting argument: the argmax family size should follow from the
  substituted-class orbit sizes and the open-box boundary combinatorics. The
  same machinery should decide the ±3 and ±2 families.
- **Propagate the swap law to the response floor.** The Cycle-709 minus-branch
  floor (stem
  `PHYSICAL_MINUS_BRANCH_RESPONSE_FLOOR_ASSEMBLY_DEFECT_LAW_CYCLE709_NOTE_2026-08-02`,
  in flight) consumes the assembly defect through a solve; the exact swap
  structure derived here is the natural input for an exact floor statement.
- **Path-symmetrized assembly.** The substitution dichotomy suggests a
  symmetrized transport (average over re-anchoring choices) whose defect could
  vanish on a larger frame set; whether the sextet boundary moves under
  symmetrization is a sharp, finite question.

## Relation to the interacting cycle

This cycle stays inside the static spatial sector of the landed 3+1 module: the
tick multiplier LT enters only as the supplied constant multiplying the
per-simplex sum. The K-endpoint transport and the source-stabilizer analysis of
[PHYSICAL_SOURCE_STABILIZER_COSET_COLLAPSE_K_SIGN_LAW_CYCLE707_NOTE_2026-08-01](PHYSICAL_SOURCE_STABILIZER_COSET_COLLAPSE_K_SIGN_LAW_CYCLE707_NOTE_2026-08-01.md)
sit downstream of the same frame sextet; the dichotomy of T1 gives that sextet
a purely combinatorial characterization (constant-sign matrices), sharpening
the boundary that the in-flight Cycle-708 classification (stem
`PHYSICAL_SOURCE_EDIT_SET_SIGNED_STABILIZER_CLASSIFICATION_CYCLE708_NOTE_2026-08-02`)
maps at the signed level.

## Runner

The primary runner linked above is a finite exhaustive and symbolic check using
stdlib, numpy, and sympy. Gate groups: substitution
dichotomy over all 24 frames; incidence decomposition with bit-for-bit entry
match; exact symbolic per-simplex values with a perturbed-background rejector;
FD provenance (convergence ratios and finite error budget); swap census over
all 18 mixed frames at both box sizes with bitwise comparator uniformity;
frame-uniform rounded census; sextet cross-checks (plus branch 7.1e-15, minus
branch 1.2e-10, identity frame exactly 0.0). It writes a JSON receipt with
coarse-precision values only and ends with `TOTAL: PASS=55 FAIL=0`.

## Citations

- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md) — the four-axiom
  foundation; proper cubic rotations are the frame set.
- [PHYSICAL_OPERATIONAL_SOURCE_RESPONSE_READOUT_CHAIN_CYCLE700_NOTE_2026-07-25](PHYSICAL_OPERATIONAL_SOURCE_RESPONSE_READOUT_CHAIN_CYCLE700_NOTE_2026-07-25.md)
  — the source-response readout chain this lane extends.
- [PHYSICAL_SOURCE_STABILIZER_COSET_COLLAPSE_K_SIGN_LAW_CYCLE707_NOTE_2026-08-01](PHYSICAL_SOURCE_STABILIZER_COSET_COLLAPSE_K_SIGN_LAW_CYCLE707_NOTE_2026-08-01.md)
  — the source-stabilizer sextet this cycle characterizes combinatorially.
- [FINITE_REGGE_PLAQUETTE_SCATTERING_DIAGNOSTICS_CYCLE576_BOUNDED_THEOREM_NOTE_2026-07-22](FINITE_REGGE_PLAQUETTE_SCATTERING_DIAGNOSTICS_CYCLE576_BOUNDED_THEOREM_NOTE_2026-07-22.md)
  — the frame table and deficit-angle machinery.
- Compiler chain: the linked Cycle-696 runner above (landed; LT = 2 and the FD
  step are its supplied constants).
- In flight, context only: cycles 708–710, stems backticked above.

## Review record

Independent review narrowed two earlier refutation-style boundary sentences to
the positive finite witnesses actually executed at L = 3 and L = 7; no broader
scientific conclusion is attached to those witnesses. The load-bearing
Cycle-696 source closure is now explicit and cache-bound.

Outstanding at landing, as hard landing conditions: (1) the exact heads of
predecessor PRs #5892 and #5895 must already be contained in `origin/main`; (2)
the primary runner must be rerun through `scripts/runner_cache.py` with a fresh
five-file input fingerprint and exit 0; and (3) the citation-graph manifest must
be regenerated from the final proposed landing tree and its added-node and
dependency-edge delta inspected before acknowledgment.
