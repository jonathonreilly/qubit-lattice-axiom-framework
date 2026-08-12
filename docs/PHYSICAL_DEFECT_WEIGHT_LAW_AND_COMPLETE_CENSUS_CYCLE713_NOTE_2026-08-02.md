# Physical Assembly-Defect Weight Classification and Complete Resolved-Entry Census — Cycle 713

Date: 2026-08-02

Claim type: bounded_theorem

Status: proposed_retained

Authority: none. Audit status is set only by the independent audit lane; this
note changes no axiom, approved primitive, premise registry, or policy surface.

Primary runner:
`scripts/physical_defect_weight_law_and_complete_census_cycle713_2026_08_02.py`;
cached stdout:
`logs/runner-cache/physical_defect_weight_law_and_complete_census_cycle713_2026_08_02.txt`;
paired receipt:
`outputs/physical_defect_weight_law_and_complete_census_cycle713_2026_08_02_receipt_2026-08-02.json`.

Finite, recomputed statements about the landed
Cycle-696 open-coframe endpoint compiler chain at box sizes L ∈ {3, 4, 5, 6, 7,
8, 9}. The magnitude law, its support-signature resolution, the finite census
values, and their polynomial agreement are bounded computational statements
verified by complete scan over all 18 mixed frames; the identification of the
compiler chain with the static spatial sector is inherited, not re-derived here.

```yaml
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "derive the finite weight split and support-signature mechanism, then prove any arbitrary-size counting extension rather than inferring it from seven boxes"
source_of_blocker_text: strongest_missing_lemma
reachability_to_target: supports
artifact_role: runner_certificate
next_trace_action: "derive the half-weight incidence mechanism and an arbitrary-L descriptor-count theorem, then test alternative transport definitions separately"
```

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "Complete finite scan of the supplied Cycle-696 compiler at L in {3,...,9}; polynomial and factorization statements are not extended beyond that enumerated domain."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the runner exhausts the declared finite frame-size surface, while the compiler identification, floating finite-difference values, arbitrary-size law, and alternative boundary transports are not derived here"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Finite targets inherited from Cycles 711 and 712

The [Cycle-711 exact stencil swap law](PHYSICAL_MIXED_FRAME_COMPARATOR_EXACT_STENCIL_SWAP_LAW_CYCLE711_NOTE_2026-08-02.md)
derived the mixed-frame comparator −4 exactly at `L in {3, 7}` and recorded its
per-sign census as measured, not derived. The
[Cycle-712 finite family census](PHYSICAL_MIXED_FRAME_DEFECT_CENSUS_FAMILY_LAW_CYCLE712_NOTE_2026-08-02.md)
derived the `L = 3..7` counts from a positional box-descriptor mechanism, but
took the four magnitudes {2, 2·√2, 2·√3, 4} themselves as a measured menu and
counted only the entries above the supplied cut 2.0e+00. This note extends the
same finite scan to `L = 8, 9` and classifies the sub-cut population.

This cycle derives the finite menu, classifies every remaining resolved entry,
and records the complete scanned census. Within the scanned compiler surface, the
full-weight magnitude factorizes over the two coframe-leg lengths; a separate
measured bit selects a half-weight subpopulation within the axis-axis
signature. All statements below are recomputed from the landed compiler chain
in this cycle's runner.

## Setup

The compiler chain is the landed Cycle-696 static-sector assembler: path-simplex
templates on the open box, spatial edge classes, and the assembled static
Hessian Q, with tick multiplier LT = 2 and central finite-difference step
1.0e-04 as supplied compiler constants. Each coframe variable i carries a
spatial direction vector v_i fixed by its edge class, with **support**
s_i = |v_i|² ∈ {1, 2, 3}: support 1 for the three axis classes, 2 for the three
admitted face-diagonal classes, 3 for the body-diagonal class. Frames are the 24 proper
cubic rotations of the landed Cycle-576 table; the transport permutation Π_g is
the bounding-box dof relabeling of Cycle 710, and the assembly defect is
E_g = Π_g^T Q Π_g − Q. The six constant-sign frames (the sextet) have measured
defect ceiling below 1.0e-09 at the probed `L = 3`; this is a numerical gate,
not an exact-zero theorem. The census lives on the 18 mixed frames.

### Supplied and measured inputs

- The open-box Cycle-696 compiler, its seven spatial edge classes, `LT = 2`,
  finite-difference step `1e-4`, and proper-frame table are supplied compiler
  structure. Their physical interpretation remains inherited.
- The strict comparison cut `2.0` and the two finite per-sign anchor counts
  `424` (`L = 3`) and `10680` (`L = 7`) are imported from Cycle 711 only as
  cross-check targets. The runner recomputes the entries that meet them.
- The unpinned/one-axis-pinned/two-axis-pinned interpretation is imported from
  Cycle 712. The complete resolved-entry values at `L = 3..9`, including the
  new `L = 8, 9` data, are measured by this runner.
- No fitted, observational, or literature constant enters. The displayed
  polynomials are interpolation/finite-agreement descriptions, not supplied
  physics inputs.

## Theorem I — the weight law

For every mixed frame and every box size in the scan, every **resolved** entry
of the assembly defect, defined here by `|E_ij| > 1e-9`, satisfies

> |E_ij| = w · LT · |v_i| · |v_j| = w · LT · √(s_i s_j),  w ∈ {1, 1/2},

matched within 2.0e-07, with worst deviation 6.1e-08 over all 2,418,192 resolved
entries scanned, and **zero resolved entries** left unclassified. Entries at or
below the numerical floor are outside the classification. Two facts sharpen it:

- **Half weight is axis-locked.** The realized signature set of the w = 1/2
  population is exactly {(1, 1)} — half weight occurs on axis-by-axis pairs and
  nowhere else. Its magnitude is therefore always 1.0e+00.
- **Full-weight signature support.** The realized signature set is exactly
  {(1,1), (1,2), (2,1), (1,3), (3,1), (2,2)} at every scanned frame and size.

Consequently the support signature determines the full-weight magnitude, while
the extra measured weight bit distinguishes magnitudes 1 and 2 inside the
axis-axis signature. The Cycle-712 menu is the list of values
LT·√(s_i s_j) that the realized full-weight signatures produce: (1,1) → 2,
(1,2) and (2,1) → 2·√2, (1,3) and (3,1) → 2·√3, (2,2) → 4, plus the half-weight
value 1 that the Cycle-712 cut had removed. The cut 2.0e+00
is exactly the full/half separator: the largest half-weight magnitude is
1.0e+00 and the smallest full-weight magnitude is 2.0e+00, so the entries above
the Cycle-712 cut coincide with the full-weight entries at every frame and size.

The law is not a fit to a plausible-looking form. The additive alternative
LT·√(s_i + s_j) — which agrees at signature (2,2), where both read 4 — misses by
at least 0.54 wherever the two differ. Swapping the axis and body-diagonal
support assignments leaves 1656 entries outside the law at a single frame and
size. A site-graded diagonal ramp on Q, noncommuting with the relabeling,
leaves 272 entries outside it. A uniform diagonal shift, by contrast,
leaves the defect exactly unchanged — the relabeling is a permutation, so a
multiple of the identity cancels between the two terms of E_g.

## Theorem II — the complete finite census and polynomial agreement

Per mixed frame, and identically for all 18 of them, the counts agree with the
following integer polynomials at every scanned size `L = 3..9`:

| population | per sign | L = 3 … 9 |
|---|---|---|
| full weight | 48(L−1)³ + 8(L−1)² + 4(L−1) | 424, 1380, 3216, 6220, 10680, 16884, 25120 |
| half weight | 16(L−1)² | 64, 144, 256, 400, 576, 784, 1024 |
| all resolved entries (both signs) | 96(L−1)³ + 48(L−1)² + 8(L−1) | 976, 3048, 6944, 13240, 22512, 35336, 52288 |

Plus and minus counts are equal for both weights at every scanned size and
frame. The magnitude-resolved finite census agrees with one integer polynomial
per magnitude and sign at every scanned size:

| magnitude | signature | per sign |
|---|---|---|
| 4 | (2,2) | 8(L−1)³ |
| 2·√3 | (1,3), (3,1) | 8(L−1)³ |
| 2·√2 | (1,2), (2,1) | 12(L−1)³ + 16(L−1)² |
| 2 | (1,1), w = 1 | 20(L−1)³ − 8(L−1)² + 4(L−1) |
| 1 | (1,1), w = 1/2 | 16(L−1)² |

The four full-weight rows partition the full-weight population, and their
cubic coefficients 8 + 8 + 12 + 20 = 48, quadratic coefficients 16 − 8 = 8, and
linear coefficient 4 reassemble the full-weight polynomial exactly.

The laws were fitted on L ∈ {3, 4, 5, 6} and then tested against L = 7, 8 and 9.
A cubic interpolated through the four fitting sizes predicts the full-weight
count and the resolved-entry count at all three held-out sizes with no residual;
L = 8 and L = 9 were measured by no earlier cycle. Independently, the
polynomials reproduce the landed Cycle-711 per-sign census totals 424 at L = 3
and 10680 at L = 7, and — after the two magnitudes 2·√2 and 2·√3 are merged, as
the Cycle-711 rounded buckets merge them — its bucket composition as well.

## Finite polynomial grading and the carrier

The finite fits have cubic, quadratic, and linear terms. On the scanned boxes,
their Cycle-712 descriptor interpretation is respectively unpinned,
one-axis-pinned, and two-axis-pinned populations. The leading coefficient is
96 resolved defect entries per unit-cell factor `(L-1)^3` per mixed frame, 48
per sign; the fitted subleading terms are `48(L-1)^2` and `8(L-1)`.

The carrier size and support-signature partition are frame-independent: exactly
**30 ordered edge-class pairs** carry full-weight entries at every scanned frame
and size. They are partitioned as 8 pairs of type (1,1), 7 each of types (1,2)
and (2,1), 2 each of types (1,3) and (3,1), and 4 of type (2,2). The identities
of the pairs form three frame-dependent carrier sets. Seven spatial classes
admit 49 ordered pairs, so the per-frame complement contains 19 pairs and
varies with the carrier identity set.

Scope limit: only the supplied open-box relabeling is executed. Alternative
boundary re-anchorings and arbitrary box sizes remain outside this result.

## Exact target and proof obligations

**Exact target.** For the imported Cycle-696 open-box compiler at each
`L in {3,...,9}`, classify every resolved entry of `E_g` at all 18
mixed frames by the two-leg weight menu; report the complete finite counts,
their agreement with the displayed integer polynomials, and the finite carrier
census.

Obligation graph:

1. The 18 analyzed maps are bijective label relabelings: checked exactly by
   integer permutation enumeration at every scanned size.
2. Every entry above the declared `1e-9` numerical floor belongs to exactly one
   weight branch within `2e-7`: checked exhaustively over 2,418,192 entries.
3. The frame-uniform sign, magnitude, and carrier censuses equal the displayed
   formulas at all seven sizes: checked by exact integer comparison after the
   finite floating classification.
4. Arbitrary-`L` extension remains open. Four sizes determine each cubic and
   three held-out sizes test it, but finite interpolation is not induction.
5. Alternative boundary transports remain open and are outside the executed
   comparison.

The strongest missing lemma is an arbitrary-size combinatorial derivation of
the weight bit and descriptor counts from the stencil incidence rules. That
lemma is needed only for a universal polynomial or boundary-convention theorem,
outside the finite `L = 3..9` target.

Degenerate and boundary cases: the smallest scanned box is `L = 3`; all 18
mixed frames and every matrix entry above the declared numerical floor
are included. The six constant-sign frames are checked separately only for a
numerical ceiling at `L = 3` and are not part of the weight census.

## Scope boundary

- **The weight bit is measured, not derived.** Theorem I says that w ∈ {1, 1/2}
  and that w = 1/2 occurs only on axis-by-axis pairs. The selection of *which*
  axis-axis entries take half weight and why that population splits while every
  other realized signature carries only the full branch remains open.
- **Signature-set completeness is measured.** The exact six-signature set is a
  complete finite-scan statement; its incidence mechanism remains open.
- **Signs are not classified.** The census is sign-balanced, and the magnitudes
  are fully determined, but which entry carries which sign is left to the
  Cycle-711 swap law and the Cycle-712 descriptor.
- **Finite scan, not induction.** The polynomials are verified at seven sizes,
  three of them held out from the fit. That is strong evidence and a clean
  extrapolation, not a proof for all L.
- **Alternative transports remain open.** The scan uses one supplied open-box
  relabeling. Other re-anchorings and interior-changing transport definitions
  are outside the executed comparison.
- **This is the static spatial sector.** No dynamical or interacting statement
  is made, and no claim about the wrapped stencil, which the Cycle-696 header
  places outside the executed path.

## The next paths opened

- **Derive the weight bit.** The half branch is exactly the axis-by-axis
  signature and exactly the per-sign 16(L−1)² surface population — the same quadratic
  that carries the Cycle-712 wall family. Testing whether the half branch *is*
  the wall family, entry for entry, is a sharp finite question and would turn
  the weight bit into a positional statement.
- **Derive the signature-set completeness.** A stencil-incidence account of
  why the exact realized set stops at the six reported signatures is the
  natural next target for the Cycle-711 machinery.
- **Propagate the fitted leading density to the response floor.** The
  Cycle-709 minus-branch response-floor note
  `PHYSICAL_MINUS_BRANCH_RESPONSE_FLOOR_ASSEMBLY_DEFECT_LAW_CYCLE709_NOTE_2026-08-02`
  consumes the assembly defect through a solve. A finite defect census with a
  factorized magnitude law is a stronger input to a future floor-scaling law
  than an isolated measured count.
- **Test the factorization against the source-side census.** The full-weight
  magnitude factorizes over the two coframe-leg lengths, while the additional
  half-weight bit remains positional. Whether the same two-part structure holds
  for the source-side edit sets is a direct question for the Cycle-708 signed
  classification.

## Relation to the interacting cycle

This cycle stays inside the static spatial sector of the landed 3+1 module. The
frame sextet that carries the numerical near-zero ceiling is the same
constant-sign sextet whose source-stabilizer role is analyzed in
`PHYSICAL_SOURCE_STABILIZER_COSET_COLLAPSE_K_SIGN_LAW_CYCLE707_NOTE_2026-08-01`;
the landed Cycle-708 classification is complementary source-side context. The
[Cycle-710 finite assembly-defect cocycle and mixed-frame comparator](PHYSICAL_ASSEMBLY_DEFECT_COCYCLE_AND_MIXED_FRAME_COMPARATOR_CYCLE710_NOTE_2026-08-02.md)
supplied the finite defect object this cycle classifies. Cycle 708 is not used
as a premise or numerical input here.

## Runner

`scripts/physical_defect_weight_law_and_complete_census_cycle713_2026_08_02.py`
— finite check, stdlib + numpy, self-contained against the Cycle-696 compiler
chain. `AUDIT_INPUT_PATHS` declares that compiler and its four transitive
script imports, and `AUDIT_TIMEOUT_SEC = 600`; no sibling cycle's numeric
output is read at runtime. Gate groups: the numerical sextet ceiling and
relabeling bijectivity; complete magnitude classification with zero unclassified entries and the
weight-law deviation ceiling; half-weight signature locking, realized full
signatures and signature-set completeness; the additive-law rejector, the full/half
separator, and the coincidence of the Cycle-712 cut with the weight split; sign
balance and frame uniformity; the three census polynomials and the four
magnitude polynomials at L = 3..9; held-out cubic extrapolation to L = 7, 8, 9;
the Cycle-711 census anchors; carrier size and carrier signature partition; and
three operator-level rejectors — support shuffle, uniform-shift invariance, and
a site-graded ramp. Prints TOTAL: PASS=28 FAIL=0 with a JSON receipt in
`outputs/`.

## Load-bearing dependencies

- [Cycle 710](PHYSICAL_ASSEMBLY_DEFECT_COCYCLE_AND_MIXED_FRAME_COMPARATOR_CYCLE710_NOTE_2026-08-02.md)
  supplies the bounded finite assembly-defect object and mixed-frame comparator
  interpretation used here.
- [Cycle 711](PHYSICAL_MIXED_FRAME_COMPARATOR_EXACT_STENCIL_SWAP_LAW_CYCLE711_NOTE_2026-08-02.md)
  supplies the finite strict-cut anchor census and exact `0 <-> -4` local swap
  context used as cross-checks.
- [Cycle 712](PHYSICAL_MIXED_FRAME_DEFECT_CENSUS_FAMILY_LAW_CYCLE712_NOTE_2026-08-02.md)
  supplies the finite component-box descriptor interpretation used for the
  polynomial grading.

Provenance-only mentions of Cycles 707, 708, and 709 above deliberately remain
non-linking because no result here depends on their claims.

## Review record

Review removed the submitted universal statement that every boundary
re-anchoring preserves the fitted cubic population. The runner constructs no alternative transport,
so that negative conclusion was unsupported. The durable result is the finite
weight classification, finite per-frame carrier census, and polynomial
agreement on the declared `L = 3..9` surface. Review also replaced an exact-zero claim for the
constant-sign sextet with the numerical ceiling actually gated at `L = 3`,
made the `1e-9` resolved-entry floor explicit, and bound the runner cache to the
complete transitive compiler-source closure. Independent audit remains required
before any effective retained grade.
