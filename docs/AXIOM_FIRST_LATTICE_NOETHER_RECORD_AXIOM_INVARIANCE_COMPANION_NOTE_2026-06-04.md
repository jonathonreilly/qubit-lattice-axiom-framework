# Axiom-First Lattice Noether Theorem: Record-Axiom Invariance Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / axiom-premise restoration evidence)
**Status:** companion-only — supplies audit-friendly evidence that the
load-bearing chain of
[`AXIOM_FIRST_LATTICE_NOETHER_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_LATTICE_NOETHER_THEOREM_NOTE_2026-04-29.md)
is invariant under the 2026-06-04 Record-axiom adoption. It is not a new
theorem claim, not a status promotion, and not an attempt to perform
re-audit work. If the audit pipeline seeds this file, it is a meta
companion row; the audit lane still sets `audit_status`, and
pipeline-derived `effective_status` remains downstream of that authority.
**Companion target:** `axiom_first_lattice_noether_theorem_note_2026-04-29`
(parent note
`docs/AXIOM_FIRST_LATTICE_NOETHER_THEOREM_NOTE_2026-04-29.md`).
**Primary companion runner:**
[`scripts/audit_companion_axiom_first_lattice_noether_record_axiom_invariance_2026_06_04.py`](../scripts/audit_companion_axiom_first_lattice_noether_record_axiom_invariance_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_axiom_first_lattice_noether_record_axiom_invariance_2026_06_04.txt`](../logs/runner-cache/audit_companion_axiom_first_lattice_noether_record_axiom_invariance_2026_06_04.txt)

---

## §0. Why this companion exists

The parent narrow theorem
`axiom_first_lattice_noether_theorem_note_2026-04-29` was previously
audit-loop-resolved on 2026-05-25 as `audited_clean` (`bounded_theorem`,
class A) by a 2-of-2 cross-family judicial verdict on the narrowed scope:

> Bounded finite-Grassmann/Kawamoto-Smit staggered-carrier Noether
> statement: U(1) current (4)/(5) and the (2Z)^3 central two-step Ward
> identity (3a), with density (3) support-only.

The 2026-06-04 framework axiom update from `MINIMAL_AXIOMS_2026-05-20.md`
to `MINIMAL_AXIOMS_2026-06-04.md` (Lattice + Quantum + Record;
explicit-owner-approved per `docs/audit/AXIOM_MINIMALITY_POLICY.md`
section 6) changed the stable `minimal_axioms` premise-node note-hash
from `1d36a556` to `b8848fc8`. The audit pipeline correctly invalidated
the prior `audited_clean` snapshot via
`invalidation_reason=axiom_premise_changed:minimal_axioms:1d36a556->b8848fc8`,
returning the row to unaudited effective status.

This companion records, for the audit lane, that the parent's
load-bearing chain is **independent of the Record axiom**: it uses only
the Lattice and Quantum axiom content, plus the retained
`staggered_dirac_substep1_grassmann_forcing_bridge_narrow_theorem_note_2026-05-16`
(per-site Grassmann generators + Berezin readout), plus the named
admitted-carrier inputs (`staggered_dirac_realization_gate` and the
residual `KS-phase-form` structural admission). Adopting the Record
axiom adds a strictly additive scalar record-readout statement, which
is neither used nor invoked anywhere in the lattice Noether identity
derivation. The U(1) bilateral current (4)/(5), the central two-step
Ward identity (3a) for `(2Z)^3` translation, and the on-shell
divergence-freeness statements of the parent theorem are unchanged.

This companion is therefore audit-friendly evidence that the prior
clean verdict's substantive content survives the axiom-set change. It
is not a re-audit and does not promote status; it documents the
load-bearing-step dependency surface in machine-checkable form so the
audit lane can decide whether to honor or re-test the prior judicial
verdict on the new premise hash.

---

## §1. Scope and boundary

This companion makes one narrow auditable observation:

**(C1) Record-axiom invariance of the lattice Noether identity chain.**
The parent's load-bearing steps consist of:

1. The Step 1 infinitesimal Lie-generator symmetry condition
   `[T^A, M]_{xz} = 0` on the admitted finite-Grassmann staggered-Dirac
   carrier;
2. The Step 2 local-α promotion + bilateral-hop reindex giving the
   on-shell conserved bilateral current
   `J^{µ,A}_x = (1/2) η_µ(x) [χ̄_x T̂^A χ_{x+µ̂} + χ̄_{x+µ̂} T̂^A χ_x]`
   (Eq. 5 of parent);
3. The Step 3 on-shell divergence vanishing `∂^L_µ J^{µ,A}_x = 0`
   (Eq. 10 of parent);
4. The Step 4a specialization of (5) to the U(1) phase generator
   `T̂^A = i · I`, giving the fermion-number current (4) of parent;
5. The Step 4b exact localized two-step Ward identity (3a) for the
   `(2Z)^3` central two-step generator `D^{(2ρ)} = (S^{(+2ρ̂)} -
   S^{(-2ρ̂)})/2`, using `[M_KS, D^{(2ρ)}] = 0`;
6. The Step 5 one-site-shift counterexample using the
   Kawamoto-Smit phase periodicity `η_µ(x + 2ρ̂) = η_µ(x)` versus
   `η_µ(x + µ̂) ≠ η_µ(x)` for the affected directions.

None of items 1-6 use the Record axiom's additive scalar record-readout
content. They use only:

- the Lattice axiom (`Z^3` lattice, `(2Z)^3` index-2 sublattice
  translation, finite-range nearest-neighbour cubic adjacency);
- the Quantum axiom (one-qubit / `Cl(3,0)` local algebra surface,
  retained per the Cl(3) split + dim-2 narrow theorems);
- the retained
  `staggered_dirac_substep1_grassmann_forcing_bridge_narrow_theorem_note_2026-05-16`
  (per-site `(χ_x, χ̄_x)` Grassmann generators with anticommutation
  `(G1)-(G3)`, Berezin integration, per-site Fock dim 2, and the
  Berezin determinant readout `Z_F[M] = det(M)`);
- the named admitted-carrier inputs unchanged from the parent
  (`staggered_dirac_realization_gate` carrier `M_KS` and the residual
  `KS-phase-form` structural admission), which remain admitted at
  exactly the same tier on the new axiom set.

**(C1) is the only auditable companion observation.** Anomaly closure
for the quantum currents, full energy-momentum tensor conservation, the
staggered taste-shift group, and any retagging from `bounded_theorem`
to `positive_theorem` remain explicitly out of scope, exactly as in the
parent note (parent's "Honest status" and "Not in scope" sections).

This companion does **not**:

- introduce a new minimal-axiom statement (the explicit-owner-approved
  axiom set is fixed at `MINIMAL_AXIOMS_2026-06-04.md`);
- change the parent's claim scope, claim type, or admitted-context
  inputs (carrier gate + `KS-phase-form` residual remain admitted);
- assert anything about Record-axiom content or its scope;
- re-audit `axiom_first_lattice_noether_theorem_note_2026-04-29` or any
  other ledger row;
- modify the audit ledger, the audit queue, or any status field.

The audit lane decides whether (C1) is sufficient evidence to re-honor
the previous judicial verdict or whether a fresh per-site audit is
warranted on the new premise hash.

---

## §2. The Record axiom is not used by the load-bearing chain

The Record axiom (`MINIMAL_AXIOMS_2026-06-04.md` §"Record") says:

> When a finite record-readout surface is specified, its scalar record
> functional is additive over disjoint record collections:
>
>     I(R_1 sqcup R_2) = I(R_1) + I(R_2)
>
> with `I(empty) = 0` after an explicit additive-baseline convention.

The parent's load-bearing chain defines no record surface, asks no
question about scalar record additivity, and writes no record
functional `I(.)`. It performs finite-Grassmann/algebraic manipulations
of the admitted canonical action `S_F = χ̄ M χ` plus the bilateral-hop
reindex argument (parent §Step 2) plus the discrete two-step Ward
identity (parent §Step 4b). The operator content of the conserved
currents (Eqs. 3a, 4, 5), the symmetry condition (Eq. 6), the on-shell
divergence-freeness (Eq. 10), and the Kawamoto-Smit periodicity
`η_µ(x + 2ρ̂) = η_µ(x)` are fixed by:

- finite-Grassmann algebra on the admitted carrier (retained substep-1
  Grassmann theorem; named `KS-phase-form` admission);
- discrete index counting on the `Z^3` lattice and its `(2Z)^3`
  sublattice (Lattice axiom);
- one-qubit local operator algebra `M_2(C) ≅ Cl(3,0)` per site (Quantum
  axiom);
- standard variational Noether technique adapted to the finite
  Grassmann action (elementary algebra, not an imported black box per
  parent's "Hypothesis-set summary").

The Record axiom adds an additive scalar record functional. It does
not modify (and is not modified by) the Lattice index structure on the
`(2Z)^3` sublattice, the Quantum one-qubit local algebra used for the
Grassmann carrier, the bilateral-hop reindex argument, or the
discrete-vs-infinitesimal split between Step 4a (U(1) Lie generator)
and Step 4b (`(2Z)^3` discrete shift Ward identity). So the parent's
identity content is invariant under the axiom-set change.

This invariance is what the companion runner verifies block-by-block:
every load-bearing arithmetic check passes using only Lattice +
Quantum + retained-Grassmann content (plus the admitted carrier inputs
exactly as in the parent), and a "Record-axiom counterfactual" block
confirms that the bilateral-current divergence and the two-step
commutator vanish identically whether or not a Record-axiom statement
is appended.

---

## §3. Companion runner block plan

`scripts/audit_companion_axiom_first_lattice_noether_record_axiom_invariance_2026_06_04.py`
verifies the Record-axiom invariance of the lattice Noether identity
load-bearing chain. Each block runs as an independent
numeric/algebraic check; nothing is hard-coded against an expected
target value beyond standard finite-dimensional algebra. The runner
reports `PASS` / `FAIL` per check; the cached output records the run.

**Block 1 — Kawamoto-Smit phase periodicity on the `(2Z)^3` sublattice.**
Verifies `η_µ(x + 2ρ̂) = η_µ(x)` for every direction
`µ ∈ {1, 2, 3}`, every shift direction `ρ ∈ {1, 2, 3}`, and every
sample site `x` on a free pure-staggered `L=4` block. Each component of
`2ρ̂` is even, so the parity sum defining `η_µ` is unchanged. (Lattice
axiom only.)

**Block 2 — One-site shift breaks the staggered symmetry.**
Exhibits direction(s) `µ` and site(s) `x` where
`η_µ(x + µ̂) ≠ η_µ(x)`, confirming the parent's Step 5 statement that
one-site shifts are NOT pure translations of `M_KS`. (Lattice axiom
only.)

**Block 3 — Symmetry condition (6) for the U(1) phase generator.**
On a free pure-staggered `L=3` block, builds `M = m + M_KS` and the
generator `T = i · I`, and verifies `[T, M] = 0` to machine precision.
(Retained Grassmann content + Quantum axiom for the one-qubit local
algebra carrier of the Cl(3) reading.)

**Block 4 — Two-step shift commutator vanishes.**
On the free pure-staggered `L=4` block, constructs the two-site shift
operator `S^{(2µ̂)}` for each direction `µ` and verifies
`S^{(2µ̂)} M_KS - M_KS S^{(2µ̂)} = 0` to machine precision. This is
Step 4b's load-bearing commutator `[M_KS, D^{(2ρ)}] = 0`. (Lattice
axiom + retained Grassmann content.)

**Block 5 — Central two-step generator skew-adjointness.**
Constructs `D^{(2ρ)} = (S^{(+2ρ̂)} - S^{(-2ρ̂)})/2` for each direction
`ρ` and verifies `D^{(2ρ)†} = -D^{(2ρ)}` to machine precision; also
verifies `[M_KS, D^{(2ρ)}] = 0`. This is the Step 4b skew-adjoint
linear generator used in the localized Ward identity (3a). (Lattice
axiom + retained Grassmann content.)

**Block 6 — Bilateral current (5) → fermion-number current (4) under
U(1) phase.**
Substitutes `T̂^A = i · I` into the bilateral current
`J^{µ,A}_x = (1/2) η_µ(x) [χ̄_x T̂^A χ_{x+µ̂} + χ̄_{x+µ̂} T̂^A χ_x]`,
multiplies by the canonical convention factor `-i`, and verifies the
result equals
`J^µ_x = -(1/2) η_µ(x) [χ̄_x χ_{x+µ̂} + χ̄_{x+µ̂} χ_x]` symbolically
across a sampled set of (site, direction) pairs on the L=3 block,
checking the resulting linear-form coefficients agree to machine
precision. (Step 4a load-bearing closure.)

**Block 7 — On-shell divergence of the bilateral current.**
Builds a representative free-pure-staggered classical
expectation-level current `J^µ_x` constructed from `M^{-1}` (the
parent runner's E3 surface) and verifies the lattice divergence
`∂^L_µ J^µ_x = Σ_µ (J^µ_x - J^µ_{x-µ̂}) = 0` site-by-site to machine
precision. This is the parent's Eq. (10) on the admitted free carrier.

**Block 8 — Localized two-step Ward identity (3a).**
On the L=3 block, samples nontrivial local envelopes `ω_x` and
verifies that, for a randomly drawn `χ` satisfying the free-massless
equation `M_KS χ = 0` (when nontrivial nullspace exists; otherwise
sampled `χ, χ̄`), the identity
`δ_ω S_F = Σ_x ω_x [-(χ̄ D^{(2ρ)})_x (Mχ)_x + (χ̄ M)_x (D^{(2ρ)}χ)_x]`
holds and equals zero on-shell to machine precision. This is the
parent's Eq. (3a). (Step 4b load-bearing exact-localized identity.)

**Block 9 — Static-source scan of parent note's load-bearing chain.**
Scans the parent note's load-bearing chain (Hypothesis set used,
Statement, Proof Steps 1-5, Hypothesis-set summary) and confirms zero
Record-axiom usage tokens. Token set:
`{"I(R_1", "I(R)", "scalar record", "record functional",
"record-readout", "additive record", "additive scalar record",
"MINIMAL_AXIOMS_2026-06-04"}`. Confirms `MINIMAL_AXIOMS_2026-05-20.md`
is the cited axiom memo, and the parent's load-bearing scope is
unchanged.

**Block 10 — Record-axiom counterfactual.**
Re-runs Blocks 1, 3, 4, 5, 6 under an explicit "Record axiom is
asserted" outer scope and an explicit "Record axiom is not asserted"
outer scope; verifies that the symmetry commutator `[T, M] = 0`, the
two-step commutator `[M_KS, S^{(2µ̂)}] = 0`, the skew-adjoint
`D^{(2ρ)†} = -D^{(2ρ)}`, and the bilateral-current → fermion-number
specialization are identical under both scopes. The counterfactual is
a tautology at the calculation level (no Record-axiom content enters
any of the Step 1-5 algebraic manipulations), which is precisely the
substantive content of (C1).

**Block 11 — Axiom-name vs axiom-content separation.**
Verifies that the parent's `MINIMAL_AXIOMS_2026-05-20.md` citations
refer to the historical two-axiom wording for the one-qubit local
algebra and `Z^3` lattice, and that those content statements are
preserved in `MINIMAL_AXIOMS_2026-06-04.md` under the explicit names
Quantum and Lattice. Confirms the Record axiom is a third, additive,
non-overlapping statement that does not consume any Lattice or Quantum
content.

**Block 12 — Hypothesis-set parity across the axiom-set change.**
Confirms that the parent's hypothesis set — Lattice + Quantum + the
retained substep-1 Grassmann narrow theorem + the named admitted
carrier inputs (`staggered_dirac_realization_gate` and `KS-phase-form`
residual) — has the same content (and tier) under both
`MINIMAL_AXIOMS_2026-05-20.md` and `MINIMAL_AXIOMS_2026-06-04.md`. The
retained substep-1 Grassmann row is independently `retained_bounded`
on both memos; the admitted carrier inputs remain admitted at the same
tier; no input migrates to a different tier under the axiom-set
change.

**Block 13 — Independent recomputation of the U(1)-current closure
arithmetic.**
Repeats the (5) → (4) closure check three independent ways on the L=3
block: (a) symbolic substitution of `T̂ = i · I` into the operator
expression for (5); (b) explicit numeric construction of (4) and (5)
on representative test fields; (c) coefficient-by-coefficient
comparison after the convention factor `-i`. Verifies all three routes
agree to machine precision.

Total: 13 blocks, with the exact PASS/FAIL count recorded in the
SHA-pinned cached runner output.

---

## §4. Audit-pipeline boundaries

This companion asserts no theorem claim and no status promotion. The
companion source and runner read as `meta` audit-companion evidence.
Per [`docs/audit/README.md`](audit/README.md) (the auditor sets
`claim_type`, the auditor sets `audit_status`, and the pipeline derives
`effective_status`), no status field changes are implied by this PR.
The audit lane decides whether to re-honor the prior judicial verdict
on the new premise hash; this companion only supplies machine-checkable
evidence on whether the new Record axiom disturbs the load-bearing
chain.

The Record-axiom-invariance observation here is structurally narrow:
it does not extend to any downstream claim that consumes the parent's
output. Each downstream claim must be examined independently against
the new axiom-set premise hash. The 26+ other rows recently
axiom-invalidated under the same hash change are out of scope of this
companion; they are listed in the audit queue's
`axiom_premise_changed` cohort and should be examined separately as
the audit lane reaches them.

---

## §5. Audit-ordering and integration

This companion does not migrate the parent's
`MINIMAL_AXIOMS_2026-05-20.md` citations to
`MINIMAL_AXIOMS_2026-06-04.md`. Both are valid framework axiom memos;
the 2026-06-04 memo cites the 2026-05-20 memo as the "local-algebra
authority and historical source for the prior two-axiom wording." A
separate citation-migration PR (if desired) can refresh the parent
note's load-bearing dependency citations; this companion is independent
of that text update and is content-only.

This companion's load-bearing-chain invariance observation depends
only on the Quantum and Lattice content being preserved across the two
memos — verified in Block 11 — on the retained substep-1 Grassmann
theorem being independently `retained_bounded` on both memos —
verified in Block 12 — and on the Record axiom adding a strictly
additive non-overlapping statement — confirmed by direct reading of
`MINIMAL_AXIOMS_2026-06-04.md` §"Record" (Block 11).

---

## §6. References

- Parent note:
  [`AXIOM_FIRST_LATTICE_NOETHER_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_LATTICE_NOETHER_THEOREM_NOTE_2026-04-29.md)
- Parent runner:
  `scripts/axiom_first_lattice_noether_check.py`
- Prior judicial verdict snapshot:
  `docs/audit/data/audit_ledger.json` row
  `axiom_first_lattice_noether_theorem_note_2026-04-29`,
  `previous_audits[-1]` (`audited_clean`, `bounded_theorem`, class A,
  cross-family verdict, 2026-05-25, archived 2026-06-04 with
  `invalidation_reason=axiom_premise_changed:minimal_axioms:1d36a556->b8848fc8`)
- New framework axioms:
  [`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md)
- Predecessor framework axioms (still authoritative for local-algebra
  and lattice content):
  [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md)
- Retained substep-1 Grassmann dependency (independent of axiom-set
  change):
  [`STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md`](STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md)
- Axiom-minimality policy and explicit-owner-approval ledger:
  [`docs/audit/AXIOM_MINIMALITY_POLICY.md`](audit/AXIOM_MINIMALITY_POLICY.md)
- Audit lane authority statement:
  [`docs/audit/AUDIT_LANE_AUTHORITY.md`](audit/AUDIT_LANE_AUTHORITY.md)
- Companion pattern precedent:
  [`YT_WARD_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md`](YT_WARD_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md)
