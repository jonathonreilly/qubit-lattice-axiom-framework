# The Phase-Type Insertion Characterized: the Triality Phase Extends the Abelian Theta Slot Exactly and Carries a Theta-Like Flip Table, but Reads Only the Center/Abelian Shadow — No Single-Link Class-Weight Insertion Reads the Chiral Sign, Which the Path-Antisymmetrized Multi-Link Chain Observable Reads Exactly (Bounded Theorem)

**Date:** 2026-07-02
**Type:** bounded_theorem
**Claim type:** bounded_theorem (exact finite constructions plus one scoped
single-link no-go; not a terminal no-go, not a discharge of the theta
admission).
**Status authority:** independent audit lane only. This note does not set an
audit verdict, edit registries, register primitives, change axioms, retire or
re-grade any Tier-A admission, or claim Strong-CP closure.
**Current-main posture (2026-07-07):** theta is already retired from live
Tier-A by retained derivation. This note banks a historical bounded support
calculation for the theta-side phase-insertion campaign; it does not reopen,
modify, or re-grade the theta retirement record or
`tier_a_admissions.json`.
**Primary runner:**
[`scripts/theta_phase_insertion_triality_flip_table_single_link_nogo_chain_reader_2026_07_02.py`](../scripts/theta_phase_insertion_triality_flip_table_single_link_nogo_chain_reader_2026_07_02.py)
**Runner cache:**
[`logs/runner-cache/theta_phase_insertion_triality_flip_table_single_link_nogo_chain_reader_2026_07_02.txt`](../logs/runner-cache/theta_phase_insertion_triality_flip_table_single_link_nogo_chain_reader_2026_07_02.txt)

## Question

The theta residual asks whether a phase-type gluing insertion can carry the
orientation-odd datum that real class-weight observables miss. The target
must be frame-licensed, have the expected phase-conjugation flip behavior,
and distinguish what a single-link class-weight insertion can and cannot
read.

Question answered here: construct the natural phase-insertion class, derive
its exact transformation table and read content, and determine whether a
single-link insertion can do the job at all.

## Answer

Four exact results (invariant-projector evaluation throughout — no group
integration; all checks are earned by this runner):

1. **The insertion class, and its abelian shadow.** The triality-phase
   weight

   ```text
   w_alpha = 1 + c (e^{i alpha} chi_F + e^{-i alpha} chi_Fb)
   ```

   is a class function whose `U(1)` case is exactly
   `1 + 2c cos(phi + alpha)` — an argument-shifted abelian theta-slot
   shape, with Fourier coefficients `c e^{+-i alpha}` at `n = +-1`
   (runner A1-A2). The nonabelian extension phases the characters by
   triality, the center-grading structure tracked in
   [`GAUGE_CENTER_SECTOR_RECORD_CONTEXT_AND_THETA_Q_CHARACTER_GRADING_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-07-01.md`](GAUGE_CENTER_SECTOR_RECORD_CONTEXT_AND_THETA_Q_CHARACTER_GRADING_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-07-01.md);
   this is a phase on fusion labels, not a lattice shift of the torus dual.

2. **Theta-like flip table (exact).** For the phased star `G_alpha` on the
   link star (runner B1-B5):

   ```text
   dagger:    G_alpha(S^dag triple) = G_{-alpha}(S);
   bar:       G_alpha(conj triple)  = G_{-alpha}(S);
   transpose: G_alpha(S^T triple)   = G_alpha(S)     for every alpha;
   ```

   `G_alpha` is real (conjugate channel pairing) and diagonal-conjugation
   invariant at every `alpha`. The insertion transforms under the
   orientation-reversal flips exactly as a theta angle should — the flips
   conjugate the phase — while remaining a licensed, frame-free observable.

3. **What it reads — the center/abelian shadow, exactly.** The alpha-odd
   part `O = G_alpha - G_{-alpha}` matches the exact channel formula
   (projector vs formula, 1e-12; runner C1) and is nonzero (|O| = 0.162 at
   the fixed staples). Its pair channels are exact transport composites —
   `I(F,1,F) = tr(S3 S1)/3`, `I(1,F,F) = tr(S3 S2)/3` (runner C3) — so the
   single-link phase reads the **imaginary parts of pair-composite traces**
   plus the epsilon channel: precisely the abelian/center shadow of
   orientation-odd data, consistent with the abelian case where the theta
   slot reads the flux sign.

4. **The single-link no-go, and the reader that exists.** `O` is
   transpose-**even** for every alpha while the chiral datum
   `d = tr(S1 S2 S3) - tr(S1 S3 S2)` flips sign under transpose with
   `|d| = 0.667` at the fixed staples (runner C4): **no single-link
   class-weight insertion — real or phased, at any alpha — reads the chiral
   sign.** Naive per-plaquette imaginary-action theta candidates fall inside
   this class. The reader exists one level up: the path-antisymmetrized
   chain observable `D = tr(S1 S2 S3) - tr(S1 S3 S2)` is
   diagonal-conjugation invariant (frame-licensed, configurational),
   transpose-odd, nonzero, with exactly the dagger/bar parity table
   (runner D1-D3).

**Consequence for (ii').** The insertion is now characterized from both
ends. On the abelian surface the comparison object is the 4D carrier note's
`e^{i theta Q}` with `Q` the cross-plane flux pairing
([`THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md`](THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md)).
On the nonabelian side, this note fixes its required support: the theta
insertion must be a
**multi-link (cross-plane, path-ordered) phase object** — single-link phases
supply only the center shadow — and the cross-plane cup structure of the
linked 4D pairing is exactly of that multi-link shape. What remains of
(ii') is its derivation half alone: derive, from the framework surface, the
multi-link phase insertion whose abelian reduction is the linked
`e^{i theta Q}` and whose nonabelian content reads the chain datum `d`.

## Source surface (named authorities)

1. **Record axiom, current clauses used** (approved axiom node
   `minimal_axioms`,
   [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md); the memo
   is under active clarification on main — the sentences used here are
   quoted from the current tip):

   > "Only records are readable. A readout value is determined by record
   > content alone."

   Used as licensing discipline (the insertion class is class-function =
   frame-free; the chain reader is configurational); record occurrence is
   not claimed.

2. **Center/triality grading comparison surface** (bounded theorem note,
   audit-lane authority remains independent):
   [`GAUGE_CENTER_SECTOR_RECORD_CONTEXT_AND_THETA_Q_CHARACTER_GRADING_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-07-01.md`](GAUGE_CENTER_SECTOR_RECORD_CONTEXT_AND_THETA_Q_CHARACTER_GRADING_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-07-01.md).

3. **4D carrier/intersection comparison surface** (bounded theorem note,
   audit-lane authority remains independent):
   [`THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md`](THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md).

4. **Retired theta registry text**
   ([`docs/audit/data/tier_a_admissions.json`](audit/data/tier_a_admissions.json),
   gauge side): the historical residual was "localized to the
   multi-plaquette / large-gauge-winding account"; this note shows the
   theta-capable insertion is necessarily multi-link in this support
   surface. The retired registry entry is context, not a proof premise.

5. **Wall chronology labels:** references to prior wall labels below are
   context labels for the decomposition, not load-bearing dependencies on
   open sibling PRs. Every identity T1-T4 is earned inline by this runner.

No external comparator, measured value, fitted number, Monte Carlo, or
continuum input enters anywhere.

## Theorem statements

**T1 (insertion class; runner A1-A2, B4-B5).** `w_alpha` is a class
function reducing to the real weight at `alpha = 0`; its `U(1)`
truncation is exactly the abelian argument-shifted theta slot; the phased
star is real and diagonal-conjugation invariant for every alpha.

**T2 (flip table; runner B1-B3).** Dagger and bar conjugate the phase
(`alpha -> -alpha`); transpose preserves `G_alpha`. (One-line
change-of-variables arguments with the phase carried through; verified at
projector-exactness for three alphas.)

**T3 (read content; runner C1-C3).** The exact channel decomposition of the
alpha-odd part; nonvanishing; the pair channels are the transport
composites, so the read content is the imaginary parts of pair-composite
traces (center/abelian shadow) plus the epsilon channel.

**T4 (single-link no-go + chain reader; runner C4, D1-D3).** `O` is
transpose-even for every alpha while `d` is transpose-odd and nonzero: no
single-link class-weight insertion reads the chiral sign. The
path-antisymmetrized chain observable reads it exactly, is frame-licensed
and configurational, and carries the dagger/bar parity table.

## Corollary (wall state)

```text
W_theta_Q_context (current decomposition):
  (i-a)      defect closure on the abelianized multi-plaquette dual
             (unchanged);
  (i-b''-a') global-sheet proof sliver (unchanged);
  (i-b''-b)  sector-level closed-surface statement (unchanged);
  (ii'-final) the derivation half alone: derive from the framework surface
             the MULTI-LINK phase insertion whose abelian reduction is the
             linked e^{i theta Q} (4D cross-plane pairing) and whose
             nonabelian content reads the chain datum d. The construction
             half is now supplied: the insertion class exists (triality
             phase at single-link level — reads the center shadow; the
             chain reader at multi-link level — reads the chiral sign),
             its flip table is theta-like, and single-link candidates are
             foreclosed for the chiral-sign job.

W_theta_bar_assembly: unchanged by this note.
```

## Identification checkpoint (what objects these are)

The flips (dagger, bar, transpose) are named as mathematical operations on
staple tuples; no identification with physical C, P, T is asserted (that
identification is downstream content requiring its own bridge — the flip
table is supplied so that a future bridge can consume it). The insertion
class and the chain reader are constructions in the gluing calculus on a
witness weight class; no claim is made that the framework action contains
them (that is exactly (ii'-final)), that records register them, or that the
fixed staples model the physical sector.

## Relation to the RP-half no-go (route independence)

The retained no-go row
[`STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16.md`](STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16.md)
forecloses only "the RP half-square identity alone cannot derive a
no-bare-theta-slot exclusion." No reflection positivity appears here; this
note constructs phase insertions rather than forbidding them, and its
scoped negative (single-link class weights cannot read the chiral sign) is
a support-locality statement, not a bare-theta-slot exclusion.

## What moves

| Prior state | After this note |
|---|---|
| (ii') = wish-list of required properties (five arrows) | insertion class constructed with its exact flip table and read content; requirements confirmed realizable |
| abelian theta-slot shape vs nonabelian insertion — relation unclear | exact at this finite truncation: the triality phase is the argument-shifted abelian slot at U(1) and the center-shadow reader at SU(3); shift = phase only abelianly |
| naive per-plaquette imaginary-action theta candidates | FORECLOSED for the chiral-sign job (transpose-evenness of every single-link class-weight insertion) |
| where the chiral sign is readable | exactly located in this witness: path-antisymmetrized multi-link chain observables (frame-licensed, configurational, dagger/bar parity table) |
| (ii') support requirement | sharpened: the chiral-sign reader is multi-link/cross-plane in this construction, consistent with the registry's multi-plaquette account |

## What remains

```text
(i-a)       defect closure (unchanged);
(i-b''-a')  global-sheet proof sliver (unchanged);
(i-b''-b)   sector-level closed-surface statement (unchanged);
(ii'-final) derive the multi-link phase insertion from the framework
            surface (abelian reduction = the linked e^{i theta Q};
            nonabelian content = the chain datum d).
```

## Non-claims

This note does not claim:

- Strong-CP closure, theta retirement, or any change to the Tier-A registry;
- a derivation of the insertion from the framework surface (that is
  (ii'-final), stated as the surviving derivation half);
- physical C/P/T identification of the dagger/bar/transpose flips;
- that the truncated weights or fixed staples model the physical action or
  sector;
- exclusion of multi-link insertions (they are the constructive target; the
  no-go is scoped to single-link class-weight insertions);
- that records register the insertion, the chain reader, or any staple
  datum;
- any new axiom, import, primitive, or admission.

## No-Go Discipline Gate (for the negative boundary)

**Status:** PASS as bounded scoping inside positive constructions. The
negative content is exactly: single-link class-weight insertions — real or
phased, any alpha — are transpose-even, hence cannot read the chiral sign
(exact identity plus discriminating witness: O(S^T) = O(S) at 1e-12 while
d flips sign with |d| = 0.667).

### N1 — Alternative-route enumeration

| Route to a chiral-sign-reading theta insertion | Standing here |
|---|---|
| real single-link class weights | EXCLUDED by the same transpose-evenness mechanism |
| phased single-link class weights (any alpha) | EXCLUDED here (transpose-evenness for all alpha) — includes naive per-plaquette imaginary-action candidates |
| triality/center phase as the full theta | INSUFFICIENT alone: reads exactly the center shadow |
| path-antisymmetrized multi-link chain observables | CONSTRUCTED: read d exactly, frame-licensed, configurational |
| multi-link cross-plane phase insertion (abelian reduction = e^{i theta Q}) | OPEN — (ii'-final), the derivation half |
| non-class-function weights | NOT LICENSED here as frame-free insertions; not pursued |
| operational primitive registration | OWNER-GOVERNANCE ROUTE, not proposed (standing direction 2 -> 0) |

### N2 — Wall-independence audit

Nothing here binds the mass side or `W_theta_bar_assembly`. The single-link
no-go is scoped to class-weight insertions on one shared link; it does not
constrain multi-link objects (it locates the target there). The flip table
is exact for the constructed class; no claim extends it beyond class
weights.

### N3 — Hidden-wall scan

The insertion class is explicit; the flip table and channel formula are
verified at projector exactness with validation guards. The discriminating
structure of the no-go is explicit: the SAME staples show O invariant and
d flipped. The U(1) shadow is verified by quadrature against the
argument-shifted slot shape.

### N4 — Residual matching

The (ii') structural target is split into its construction half (supplied
here) and derivation half ((ii'-final)). The Tier-A registry's
multi-plaquette localization is respected: the chiral-sign reader is
necessarily multi-link. The abelian slot, no-lattice-shift boundary, and
center-shadow read are matched at the scoped finite level.

### N5 — Rhetoric audit

No "closes/exhausted/only-route" framing. The no-go is scoped
(single-link, class weights); the constructive target is named; the
derivation half is stated as the surviving content, not as done.

### N6 — Partial-closure path scan

Live paths: derive (ii'-final) — candidate shapes include a multi-link
phase as the nonabelian lift of the linked cup-pairing phase, with the
triality phase as its center shadow; settle (i-b''-a'); build
(i-b''-b); (i-a); and the separate theta-bar assembly side.

### N7 — Steelman

A hostile reviewer can press: (1) "The triality phase is just a chemical
potential for N-ality; calling it a theta slot oversells." The note claims
exactly what is proven: it is the argument-shifted abelian theta-slot
shape at U(1), it carries the theta-like flip table, and it reads only the
center shadow — the
insufficiency is stated as a theorem, not hidden. (2) "The single-link
no-go depends on the truncation." The transpose-evenness argument is
change-of-variables plus channel pairing — it holds for any class-weight
truncation; the runner witnesses it at the working truncation. (3) "The
chain reader is trivially d itself." Yes — the content is that d is
frame-licensed, configurational, multi-link, and exactly the datum every
single-link insertion misses; triviality of the formula is a feature (the
reader exists and is simple), not a gap. All three absorbed into scope.

### N8 — Cross-cycle echo

Cumulative guard added here: do not retry single-link phase insertions
(any alpha) for the chiral-sign job — the transpose-evenness forecloses
the whole class, including naive
per-plaquette imaginary-action theta discretizations; and do not treat the
triality phase as more than the center shadow. Future cycles citing this
chain must supply (i-a), (i-b''-a'), (i-b''-b), and (ii'-final) explicitly.

## Verification

Run:

```bash
python3 scripts/theta_phase_insertion_triality_flip_table_single_link_nogo_chain_reader_2026_07_02.py
```

Expected close:

```text
TOTAL: PASS=14 FAIL=0
```

Sections: A abelian shadow (the U(1) argument-shift identity and its phased
Fourier pair); B flip table (dagger/bar conjugate alpha; transpose
preserves; reality; diagonal-conjugation invariance at alpha != 0); C read
content (exact channel formula; nonzero read; transport-composite
identities; the transpose-even/chiral-flip discriminating pair); D chain
reader (diagonal-conjugation invariance; transpose-oddness; dagger/bar
parity table).
