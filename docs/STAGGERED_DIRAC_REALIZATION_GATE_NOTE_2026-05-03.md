# Staggered-Dirac Realization Gate Note

**Date:** 2026-05-03 (2026-05-21: §2.1 recognition added — the
in-flight substep work has matured into a single bounded source-side
closure proposal for the kinetic-and-algebra surface
`STAGGERED_DIRAC_GATE_CLOSURE_SYNTHESIS_THEOREM_NOTE_2026-05-17.md`,
with `AC_φλ` (substep-4 species labeling) recognized as the explicit
irreducible admitted-context residual structurally analogous to the
P1 admitted-context residual on
`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`; the gate's source-side
`open_gate` status is unchanged pending audit-lane ratification —
see §2.1; citation-graph plain-text-references-only convention
preserved per the §"Citation-graph note" rule)
**Type:** open_gate
**Claim scope:** A1 (Cl(3) local algebra) + A2 (Z^3 spatial substrate)
plus admissible mathematical infrastructure forces (or sufficiently
constrains) the Grassmann staggered-Dirac realization, including the BZ
corner doubler structure that maps to three SM matter generations.
**Status authority:** independent audit lane only. This source note is a
citeable open-gate parent for the staggered-Dirac realization derivation
chain; it is not itself a retained theorem and does not supply a verdict.
**Authority role:** canonical parent identity for the staggered-Dirac
realization gate in the audit ledger. Pure-meta packaging note: the
in-flight derivation work lives on the supporting notes listed below.

## Why this note exists

This note is META infrastructure. It does NOT close the gate. Its only
function is to provide the canonical parent identity that the audit
ledger can cite when downstream lanes record this gate in
`admitted_context_inputs`.

The in-flight derivation work for the staggered-Dirac realization gate
is spread across several existing notes, none of which by itself plays
the canonical-parent role. Without a single parent note, downstream
lanes that need to admit "the staggered-Dirac realization derivation
target is not yet closed" have no single citeable object to point at.
This note is that object.

The framework's restored axiom set (A1 + A2 only) is recorded in the
2026-05-03 minimal-axioms note (file `MINIMAL_AXIOMS_2026-05-03.md`,
landing under the axiom-reset PR series). That memo recategorizes the
staggered-Dirac realization from "axiom A3" to "open gate". This note is
the canonical parent identity for that recategorized gate.

## Statement

> A1 (Cl(3) local algebra) + A2 (Z^3 spatial substrate) plus admissible
> mathematical infrastructure forces (or sufficiently constrains) the
> Grassmann staggered-Dirac realization, including the BZ corner doubler
> structure that maps to three SM matter generations.

The closure of this statement requires:

1. forcing the Grassmann fermion realization on the A1+A2 surface
   (rather than admitting it as an independent axiom);
2. forcing the staggered-Dirac kinetic structure on Z^3 from A1+A2 plus
   admissible mathematical infrastructure;
3. forcing the BZ-corner doubler structure (8 corners → `1 + 1 + 3 + 3`
   by Hamming weight) from the staggered structure;
4. forcing the physical-species reading of the `hw=1` triplet as three
   SM matter generations on the accepted Hilbert/locality/information
   surface.

Pieces of (1)-(4) exist in the in-flight notes below. Closure of the gate
requires either a single canonical proof packet that runs (1)-(4)
end-to-end on A1+A2, or a coordinated chain of retained-grade theorems
on the supporting notes that together discharge each step.

## Hypothesis set used

This note's load-bearing content is identity assignment only. It uses
no upstream load-bearing mathematical hypotheses. It only:

- names the two framework axioms (A1, A2) the gate must close on;
- names the four substeps the closure must discharge;
- enumerates the existing in-flight supporting notes by filename.

The framework axioms themselves and the supporting derivations are
carried by their own notes; this parent note does not re-derive them
and does not depend on them as upstream citations.

## In-flight supporting work (plain-text references)

These are the existing notes that carry the in-flight derivation pieces
for the staggered-Dirac realization gate. They are referenced in plain
text (filenames in backticks) and are NOT load-bearing upstream
dependencies of this parent note. They are downstream consequences /
supporting attempts; the gate's parent identity does not depend on them.
See PR #306 cleanup pattern (citation-graph artifact repair): markdown
links in body would otherwise be parsed as one-hop upstream deps.

The supporting in-flight chain:

- `PHYSICAL_LATTICE_NECESSITY_NOTE.md` — closes the substrate-level
  physical-lattice reading on the accepted one-axiom Hilbert / locality
  / information surface; retained no-go on the narrowed
  two-invariant canonical-surface rigidity statement.
- `THREE_GENERATION_STRUCTURE_NOTE.md` — local algebraic / spectral
  content of the three-generation matter structure (in-scope items
  (1)-(4) on the physical-lattice surface).
- `THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md` — exact observable-sector
  theorem on the retained `hw=1` triplet: the triplet already carries
  an exact irreducible generation algebra `M_3(C)`, so no proper exact
  quotient survives on that surface.
- `frontier_generation_rooting_undefined.py` (in `scripts/`) — proves
  no proper taste projection preserves Hamiltonian `Cl(3)` on `Z^3`
  (no-rooting theorem; three independent obstructions).
- `GENERATION_AXIOM_BOUNDARY_NOTE.md` — older reduced-stack witness
  preserved for boundary documentation; reduced-stack `M_3(C)`
  reconstruction on `H_hw=1` plus reduced-stack witness explaining the
  earlier five-item-memo substrate-premise role.

These notes have their own audit verdicts and run their own primary
runners. This parent note has no runner of its own.

## Closure status

**Open at the source-side parent identity.** Pieces of an "A1+A2 forces
the staggered-Dirac realization" chain exist across the in-flight
supporting notes above. The canonical-parent packaging is the only
function of this note; substantive closure of the gate is the in-flight
work on the supporting notes. The 2026-05-21 §2.1 recognition records
the named bounded closure target for the audit lane.

## 2.1 2026-05-21 gate-closure-synthesis recognition

This section is the gate parent's recognition that the in-flight
substep work has matured into a single bounded source-side closure
proposal for the kinetic-and-algebra surface, and an explicit
named irreducible residual for the species-label identification.
It does **not** change the gate's source-side `open_gate` status —
the audit-lane-only authority rule (`Status authority: independent
audit lane only` per the synthesis note's header) keeps the gate
`open_gate` until the audit lane ratifies the synthesis. This
recognition records the named closure path for audit-lane review.

Citation-graph convention reminder: per the §"Citation-graph note"
rule below, this gate parent uses plain-text backtick references
only (no markdown links) so the citation-graph builder does not
parse the supporting-note filenames here as upstream dependency
edges. The supporting notes are downstream consequences /
supporting attempts at closing this gate; this gate's parent
identity is upstream of them, not downstream.

### 2.1.1 Named bounded closure target

The named bounded closure target for substeps (1), (2), (3) of this
gate is the source-note synthesis
`STAGGERED_DIRAC_GATE_CLOSURE_SYNTHESIS_THEOREM_NOTE_2026-05-17.md`,
which packages the chain T2 (substep-1 Grassmann partition forcing
+ Jordan-Wigner cross-site CAR bridge) → T3 (substep-2 Kawamoto-Smit
phase forcing + Kähler-Dirac equivalence) → T4 (substep-3 BZ-corner
1+1+3+3 Hamming-orbit decomposition + species-reduction bridge) →
T5 (substep-4 AC_λ simultaneous-diagonalization bridge supplying
the three pairwise-orthogonal hw=1 states) into a single end-to-end
bounded source. The synthesis was filed source-side as
`claim_type: bounded_theorem` with `Status authority: independent
audit lane only`; the live audit-ledger row at filing was
`effective_status: unaudited / effective_status_reason: awaiting_audit`.
On the 2026-05-21 re-architecture review (synthesis note §0.1), the
synthesis's claim-boundary was formalized as the bounded closure of
the kinetic-and-algebra surface with `AC_φλ` (substep-4 species
labeling) carried as an explicit irreducible admitted-context
residual.

The honest framing recorded by §2.1 of this gate parent is:

- **substeps (1), (2), (3)**: bounded closure achievable from current
  primitives + admissible standard math + the named upstream stack;
  the synthesis is the single named source for that closure.
- **substep (4) species-label identification (`AC_φλ`)**: explicit
  irreducible residual classified as a `no_go` within `A_min` by
  the substep-4 labeling audit-companion
  `STAGGERED_DIRAC_SUBSTEP4_LABELING_NO_GO_NOTE_2026-05-17.md`;
  closure requires one of three named external inputs (labeling
  convention / `C_3`-breaking dynamics / PDG-empirical), exhaustive
  within `A_min`.

The closure path is therefore: (i) audit-lane review of the
gate-closure synthesis on the corrected (bounded kinetic-and-algebra
+ `AC_φλ` admitted-context) scope; (ii) inherited lifts of the
substep-1/2 narrow-bridge `audited_conditional` / `unaudited` rows;
(iii) `AC_φλ` remains admitted-context unless and until one of the
three named external inputs lands as a separate retained primitive.

### 2.1.2 Structural backing for `AC_φλ` as admitted-context (P1 analogy)

`AC_φλ`'s admitted-context status is structurally analogous to how
`P1` (scalar additivity on independent subsystems) is treated in
`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` under the
`OBSERVABLE_PRINCIPLE_P1_CAMPAIGN_CLOSURE_SYNTHESIS_NOTE_2026-05-18.md`:

- Both admit a finite, well-named symmetry-breaking input
  (`AC_φλ`: `C_3`-orbit labeling on the hw=1 corner basis;
  `P1`: scalar additivity on independent subsystems).
- Both have a multi-route negative-result derivation portfolio
  backing the admitted-context classification (P1: 11 distinct
  routes per the P1 campaign synthesis; `AC_φλ`: 2026-05-09 AC
  narrowing + 2026-05-10 positive ratchet attempt + 2026-05-17
  labeling no-go).
- Both leave the parent note's source-side audit row at a
  conditional / awaiting-audit tier with the admitted-context atom
  explicitly named, rather than as a `missing_bridge_theorem`
  flag.

Treating `AC_φλ` as explicit admitted-context residual (with the
substep-4 labeling no-go as audit-companion) is the same shape as
the P1 admitted-context treatment. It is a legitimate framework-scope
admission, not a hidden derivation gap.

### 2.1.3 Source-side status of this gate parent

The gate parent's source-side `open_gate` claim_type stays unchanged.
The gate ratifies as `bounded` or `retained_bounded` only after the
audit lane reviews the synthesis on the re-architected scope and
either ratifies the bounded closure or names a specific corrective
target. Per the standing audit-lane-only authority rule, this §2.1
section makes no source-side promotion claim; it records the named
closure path so the audit lane has a single citeable target.

## Honest scope

This parent note:

- does **not** close the staggered-Dirac realization gate;
- does **not** supply any new mathematical content;
- does **not** carry a runner of its own;
- does **not** add citation-graph upstream dependencies (no markdown
  links in body to other notes; supporting-note references are
  plain-text only);
- **does** provide a single citeable open-gate parent identity for
  downstream `admitted_context_inputs` references.

When the in-flight chain closes, the parent identity here can become
eligible for independent audit/governance retagging as a
`positive_theorem`-typed theorem note (or be replaced by a single
canonical proof packet that runs (1)-(4) end-to-end on A1+A2). Until
then, this note remains `open_gate` in the audit ledger.

## Explicit named obstructions / repair targets remaining open

The substantive obstructions remain on the supporting notes; they are
listed here for navigation, not as load-bearing claims of this parent
note:

- **Forcing the Grassmann partition from A1+A2.** The current package
  uses the finite local Grassmann / staggered-Dirac partition as part
  of its modeling-ingredient bundle. Whether A1+A2 plus admissible
  mathematical infrastructure (spectral analysis, lattice partition
  evaluation, perturbative low-energy EFT running) **forces** the
  Grassmann reading vs. simply being **compatible** with it is the
  central content of this gate.
- **Staggered taste structure.** The Kawamoto-Smit gamma realization
  on `C^8` is irreducible
  (`scripts/frontier_generation_rooting_undefined.py`). What the gate
  needs is a forcing argument from A1+A2 to that specific
  taste-realization, not just a no-rooting result on the irreducible
  realization once chosen.
- **Substrate-fundamentality bridge.** The narrowed retained no-go in
  `PHYSICAL_LATTICE_NECESSITY_NOTE.md` shows two-invariant rigidity on
  the canonical normalization surface, but the wider one-axiom
  substrate-level forcing (Part 9 logical commentary in that runner)
  is delegated to the Hilbert / locality / information chain and not
  itself load-bearing on the narrowed scope.
- **Physical-species bridge.** The step from "exact observable
  separation + no-proper-quotient closure" to "physically distinct
  species sectors of the accepted theory" depends on accepted
  Hilbert/no-proper-quotient semantics outside the local algebraic
  reconstruction (carried in `GENERATION_AXIOM_BOUNDARY_NOTE.md` as
  out-of-scope admitted-context).

## What this note is not

- not a retained theorem;
- not a re-derivation of any in-flight supporting note;
- not a runner-bearing claim;
- not a publication-package promotion proposal;
- not a unilateral re-axiomatization (it implements the recategorization
  recorded in the 2026-05-03 minimal-axioms memo).

## Lanes that depend on this gate

Any lane whose derivation defines fermion fields, fermion-number
operators, fermion correlators, fermion bilinears, or staggered Dirac
action — essentially every lane that touches matter content. Examples
named in the 2026-05-03 minimal-axioms memo:

- `coleman_mermin_wagner` (needs Hamiltonian),
- `cpt_exact` (needs staggered structure),
- `lattice_noether` (needs action),
- `spin_statistics` (needs Grassmann),
- three-generation, baryon/meson singlet, fermion-parity `Z_2`,
  `Q̂` integer spectrum, hopping bilinear, etc.

Those lanes are typed `bounded_theorem` with this gate's parent identity
listed in `admitted_context_inputs` until the gate closes. When the gate
closes, those lanes become eligible for independent audit/governance
retagging as `positive_theorem`; the audit pipeline recomputes
`effective_status`, but it does not silently invent a new `claim_type`.

## Citation-graph note

This note has no upstream load-bearing dependencies. Plain-text
references to the framework axioms memo and to the in-flight supporting
work are pointers for readers, not upstream deps. Following the PR
[#306](https://github.com/jonathonreilly/cl3-lattice-framework/pull/306)
cleanup pattern, supporting-note filenames are written as plain text in
backticks rather than as markdown links so the citation-graph builder
does not parse them as upstream dependency edges. The supporting notes
are downstream consequences / supporting attempts at closing this gate;
the gate's parent identity is upstream of them, not downstream.
