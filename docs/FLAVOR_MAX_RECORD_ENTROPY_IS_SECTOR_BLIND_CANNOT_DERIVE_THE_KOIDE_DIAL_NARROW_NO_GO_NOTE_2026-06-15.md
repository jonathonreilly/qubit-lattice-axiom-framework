# Max-record-entropy is sector-blind: it cannot derive the Koide dial (narrow no-go)

- **Date:** 2026-06-15
- **Type:** narrow no-go
- **Claim type:** narrow_no_go
- **Status:** source note awaiting independent audit handling.
- **Primary runner:** [`scripts/frontier_max_record_entropy_sector_blind_2026_06_15.py`](../scripts/frontier_max_record_entropy_sector_blind_2026_06_15.py)
- **Cached output:** [`logs/runner-cache/frontier_max_record_entropy_sector_blind_2026_06_15.txt`](../logs/runner-cache/frontier_max_record_entropy_sector_blind_2026_06_15.txt)

## Claim

On the C₃ generation 3-space the charged-lepton block ratio `r = |b|²/a²` sits exactly (Koide
Q=2/3 to 1e-5) at `r = 1/2`. The retained siblings already establish that `r = 1/2` is a
*distinguished symmetric point* of the 2-sector (singlet|doublet) record — the maximum of the
2-sector record entropy S₂ (S₂ = ln2 at the equipartition w_singlet = w_doublet = 1/2; see
[`flavor_r_half_is_a_stationary_point_not_forced`](FLAVOR_R_HALF_IS_A_STATIONARY_POINT_NOT_FORCED_2026-06-02.md))
and the global attractor of the backward/anti-sharpening flow `r → √(r/2)`
(g'(1/2)=1/2 < 1; see
[`flavor_r_half_stable_under_thermalizing_arrow`](FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW_2026-06-02.md)),
which is the time-reverse of the retained forward sharpening separatrix `r → 2r²`
(f'(1/2)=2 > 1; see
[`flavor_r_half_is_the_records_flow_separatrix`](FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md)).
These three are one structural fact: **r = 1/2 is the symmetric, maximally-uncertain-which-sector,
least-committed value of the 2-sector record** — a valley floor in record content, not a tuned ridge.

This note settles the next question that fact provokes: *can maximizing the record entropy
DERIVE the sector-dependent Koide dial* (charged leptons r = 1/2, down-quarks r ≈ 0.597,
up-quarks r ≈ 0.773, neutrinos other)? **No.** Max-record-entropy is **sector-blind**: it returns
`r = 1/2` for *every* fermion sector, so used as a selection principle it pins r = 1/2
**universally** — a weight-leak that would force Koide Q = 2/3 on the quarks and is **falsified**
by the registered quark values. Max-record-entropy is therefore a sharper *characterization* of
the registered charged-lepton setting (it is the symmetric point), **not a derivation** of the dial.
This note **does NOT force r = 1/2** and **does NOT derive any sector's r**; r remains registered,
sector-dependent dial data (the r-dial firewall).

## The no-go (three independent obstructions)

**(N-blind) The selecting functional is gauge-uniform, so it cannot be sector-selective.**
The 2-sector partition is the C₃-isotype split of the generation carrier C³ = (trivial, 1-dim) ⊕
(E, 2-dim). That carrier is the *same shared* M₃(ℂ) for every fermion sector (retained
[`three_generation_observable_theorem`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md);
[`three_generation_observable_no_proper_quotient`](THREE_GENERATION_OBSERVABLE_NO_PROPER_QUOTIENT_NARROW_THEOREM_NOTE_2026-05-02.md);
the generations are gauge-uniform). Color and weak charge enter as a *separable tensor factor*,
uniform across the three generations; tracing it out multiplies the singlet and doublet record
weights by the **identical** gauge-dimension factor, which **cancels** in the normalized record
fractions. The runner verifies this directly: the generation-marginal record weights are invariant
under the color factor for d_color ∈ {1, 2, 3, 8}, and the entropy argmax stays r = 1/2 for every
one. A negative control pins the hinge: if the gauge rep acted with *different* multiplicity on the
singlet vs the doublet (α_s ≠ α_d — i.e. if gauge-uniformity failed), the argmax would move to
r = α_s/(2α_d) (the runner exhibits α_s=3, α_d=1 → r = 3/2). So the sector-blindness rests on the
retained gauge-uniformity of the generation carrier, not on the entropy functional alone. So
`argmax S₂` is a property of the *shared partition*, never of the sector — it gives
r = 1/2 universally. This is the same fact as the gauge-blind **degree-0 inertness** of r under
the gauge Casimir (the Casimir acts as a scalar on the gauge-uniform generation index; runner
step 5): the single sector-distinguishing channel is degree-0-invisible to r. **Uniformity is one
fact with two consequences** — the theorem that makes the Casimir invisible to r also forces the
identical record partition on every sector. A genuinely sector-dependent record *structure* (the
only firewall-OK escape) is exactly what gauge-uniformity forbids on the retained surface.

**(N-import) The entropy-MAX selection sign is an unforced import, and is not even unique.**
The only *retained* records flow is the forward sharpening map `r → 2r²`, whose dynamics points
*away* from 1/2 (r = 1/2 is its unstable separatrix). Choosing the entropy-*increasing* /
backward sign that makes 1/2 an attractor is an unaudited arrow-posit, not one of the three
axioms (Lattice, Quantum, Record) and not retained — and it re-introduces a weighting *reading* the
Record axiom (register-not-read) does not supply. Worse, "maximum entropy" is ambiguous: maximizing the
2-cell *weight* entropy gives r = 1/2, but maximizing the *state* (von Neumann) entropy — the
maximally-mixed generation state I/3, block weights (1/3, 2/3) — gives **r = 1** (dimension
weighting). Selecting the weight-uniform reading that lands on 1/2 is itself a measure choice
(runner step 4), consistent with the weighting-principle dial of
[`flavor_r_half_is_the_records_flow_separatrix`](FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md)
and the weighting-blindness of the record dynamics.

**(N-relocate) The max-uncertainty *initial state* clause relocates r into the past hypothesis.**
Reading r = 1/2 as the least-committed / maximally-uncertain initial condition identifies it with
a past-hypothesis-class input. The past hypothesis is explicitly *not* an entry of the
`realized_state` primitive (it is a separate, stronger input), so this relocates r = 1/2 into the
past hypothesis rather than deriving it from the axioms — with no reduction in input count. Two
further mismatches: r = 1/2 is the entropy *maximum* (the wrong sign for a low-entropy past
boundary), and it is a *within-sector marginal*, which a *global* past-hypothesis statement
structurally cannot fix (the same obstruction derived in a sibling lane,
`COLOR_PURITY_DOES_NOT_REDUCE_TO_PAST_HYPOTHESIS_SLOT`).

## Significance

The owner intuition — "a knife-edge is an upside-down valley; the sharpness must be a signal" — is
**vindicated as structural content and given a precise scope.** The 1e-5 sharpness of the
charged-lepton r = 1/2 is real and meaningful: it marks r = 1/2 as the *symmetric / max-record-
uncertainty* value of the 2-sector record (a valley floor under the backward flow, a peak of S₂,
the separatrix of the forward flow — one point read three ways). That dissolves the
"astronomically unlikely tuned ridge" worry. **But the symmetry that distinguishes r = 1/2 does
not distinguish the sector**, so the signal does *not* promote to a derivation of the dial: the
selecting functional is gauge-blind and would weight-leak to a universal r = 1/2. The signal
therefore points *out of* the record-and-entropy channel — toward the sector-dependent weighting
prior / couplings, which the record dynamics is provably blind to and conserves rather than
selects. This sharpens what r = 1/2 *is* (the registered symmetric setting) while closing the
max-record-entropy avenue for deriving the sector spread.

## Boundary (honest)

- Does **NOT force r = 1/2** and does **NOT derive** r for any sector; it shows that *forcing*
  r = 1/2 universally (via max-record-entropy) is a weight-leak. r stays registered dial data.
- Does **NOT close the sector-selective avenue**. The one non-falsified escape is a record-*structure*
  channel distinct from the degree-0-invisible Casimir — e.g. whether the gauge rep sets a different
  *number* of registered record sectors per fermion (a color-dressed einselection basis for the
  colored sectors, derived from the axioms rather than imported). The retained surface
  (gauge-uniform generations + degree-0 inertness) says color does not refine the C₃ singlet|doublet
  split, so this is currently **closed but not walled** — the next path this opens.
- The positive three-way characterization (separatrix / backward-attractor / entropy-max coincide
  at r = 1/2) is the content of the retained siblings; this note adds only the *sector test* and its
  negative consequence for derivation.
- Inputs: the cubic-lattice C₃ generation structure and the gauge-uniform generation carrier (both
  retained). No new axiom; no fitted parameter; r and the sector weights are free symbols.

## No-Go Discipline Gate

- **N1 alternative routes.** Non-uniform singlet/doublet multiplicities, a sector-dependent
  record-structure basis, an added weighting prior, or a separate past-hypothesis input remain
  live routes. This note rules out only the gauge-uniform C₃ two-sector max-record-entropy
  selector as a sector-selective derivation.
- **N2 wall independence.** N-blind is a tensor-factor cancellation; N-import is the missing
  max-entropy selection rule and sign; N-relocate is the separate initial-condition reading. Any
  one of the three can fail without proving the other two.
- **N3 hidden-wall scan.** The live inputs are the retained C₃ generation split, the retained
  gauge-uniform generation carrier, the retained r=1/2 sibling facts, and the current registered
  sector dial values used as a consistency check. No probability rule, normalization convention,
  new axiom, new primitive, or sector-weighting measure is imported.
- **N4 residual matching.** The named residual is exactly sector-selective weighting or
  sector-selective record structure. The no-go does not close that residual.
- **N5 rhetoric audit.** "Cannot derive the Koide dial" means "cannot derive the sector-dependent
  dial by this max-record-entropy selector." It does not mean r=1/2 is false, forced, or forbidden.
- **N6 partial-closure scan.** The positive r=1/2 characterization is retained as a structural
  fact about the charged-lepton setting; only its promotion to a universal selector is blocked.
- **N7 steelman.** If a future retained theory supplies a sector-dependent record basis or
  weighting prior, max-entropy could be part of that larger theory. Then the sector dependence
  comes from the new retained input, not from the gauge-uniform two-sector entropy functional.
- **N8 cross-cycle echo.** This is the same firewall pattern as the gauge-blind degree-0 and
  record-weighting lanes: a shared carrier can characterize a registered value but cannot by
  itself choose different sector weights.

## Dependencies

Dependency edges (retained):
- [`flavor_r_half_is_the_records_flow_separatrix`](FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md) — the forward sharpening flow r → 2r² (r = 1/2 unstable separatrix).
- [`flavor_r_half_stable_under_thermalizing_arrow`](FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW_2026-06-02.md) — the backward-flow attractor / S₂ maximum at r = 1/2.
- [`flavor_r_half_is_a_stationary_point_not_forced`](FLAVOR_R_HALF_IS_A_STATIONARY_POINT_NOT_FORCED_2026-06-02.md) — S₂ stationary at r = 1/2, not forced.
- [`three_generation_observable_theorem`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md) and [`three_generation_observable_no_proper_quotient`](THREE_GENERATION_OBSERVABLE_NO_PROPER_QUOTIENT_NARROW_THEOREM_NOTE_2026-05-02.md) — the gauge-uniform shared M₃(ℂ) generation carrier.
- [`koide_frobenius_isotype_split_uniqueness`](KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md) — declines to rank the (1,1) vs (1,2) isotype weighting (retained no-go).

Context (no edge): `realized_state_primitive` (the past hypothesis is carved out as a separate
stronger input; r is registered dial data); `color_purity_does_not_reduce_to_past_hypothesis_slot`
(a global past-hypothesis statement cannot fix a within-sector marginal); the gauge-blind degree-0
inertness derivation for r.

## Forbidden-imports check

No new axiom. Max-record-entropy / maxent / past-hypothesis are treated as the *proposed* escape
and shown to fail (import + sector-blind + relocation) — none is adopted. r and the per-sector
weights are free symbols, never computed or forced; Q = 1/3 + 2r/3 is the standard Koide-block
relation. The note does not author any audit status.
