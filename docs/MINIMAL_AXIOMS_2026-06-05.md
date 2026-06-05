# Minimal Framework Axioms (Lattice, Quantum, Record) — Record v0.4

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-06-05
**Type:** meta
**Status:** current public framework axiom memo for the qubit-on-`Z^3`
package with a recorded superselection-sector readout.
**Status authority:** explicit owner approval for the Record v0.4 update is
recorded in `docs/audit/AXIOM_MINIMALITY_POLICY.md` section 6 (entry dated
2026-06-05). Audit status of downstream rows remains set only by the
independent audit lane.

**Supersedes:** `MINIMAL_AXIOMS_2026-06-04.md`. The Lattice and Quantum axioms
are unchanged verbatim. The **Record** axiom is updated from the
2026-06-04 additivity-only form to the v0.4 form below. The change is an
owner-approved Section 6 amendment, **not** a lane-internal rewording (which
Section 1 of the policy forbids). The companion
`docs/RECORD_AXIOM_V04_UPDATE_LOGIC_NOTE_2026-06-05.md` carries the full logic,
the constitutive-vs-assumed breakdown, and the non-overreach guards.

## Purpose

This note states the framework's minimal premises, named rather than treated as
bare letter codes:

1. **Lattice**
2. **Quantum**
3. **Record**

Legacy `A1`/`A2` numbering in older notes is historical. New repo surfaces
should use the axiom names above unless quoting an older document.

## The Three Framework Axioms

### Lattice

The site set is `Z^3` with standard translation action and nearest-neighbor
cubic adjacency. Finite-range locality means finite support or finite
graph-distance range with respect to this lattice when a local expression is
specified.

This axiom supplies the discrete site set and local adjacency notion. It does
not supply a dynamics, boundary condition, metric scale, lattice spacing,
continuum or infrared limit, causal cone, probabilistic independence rule, or
physical unit conversion.

### Quantum

At each site `x`, the primitive physical local degree of freedom is one qubit;
equivalently, the primitive one-site operator algebra is
`A_x ~= M_2(C)`, equivalently `Cl(3,0)` in its real-algebra reading.

This axiom supplies the one-site algebraic carrier. It does not supply a
dynamics, composition theorem beyond the named lattice placement, measurement
instrument, Born rule, species identification, gauge group, particle content,
or physical observable bridge.

### Record (v0.4)

A record is the **irreversible registration of which real (CPT-even)
superselection sector is realized**. When a finite record-readout surface is
specified, its scalar record functional is additive over disjoint record
collections:

```text
I(R_1 sqcup R_2) = I(R_1) + I(R_2)
```

with `I(empty)=0` after an explicit additive-baseline convention.

This axiom supplies, and supplies only:

- **(a) Registration of which sector.** A record picks out which
  superselection sector — i.e. which element of the *center* (the frozen /
  classically-readable structure) of the local algebra — is realized. It does
  not resolve any finer (within-sector) state.
- **(b) Irreversibility.** A record, once formed, persists; record-formation is
  not undone. (Constitutive: a structure that can unform is not a record.)
- **(c) Reality.** The recorded alternatives are real (CPT-even). This is the
  single *assumed* adjective of the axiom — see the logic note; the logical
  alternative is a `K`-odd record, which is not adopted.
- **(d) Additive scalar readout** over disjoint records, as above.

This axiom does **not** supply: the within-sector (dimension / Born) weighting
or any specific per-sector dial occupancy; a rule for record production rate or
record dynamics; measurement/decoherence dynamics; a time metric or
normalization/scale (the *ordering* induced by irreversibility is a downstream
property, not a metric); `P2`/modulus/phase-blindness; log-det structure;
source/action identification; `AC_phi_lambda` value; theta; or arbitrary
observable identification.

## What The v0.4 Update Adds, And Does Not Add

The 2026-06-04 Record axiom stated additivity only and explicitly excluded
"persistence" and "registration." The v0.4 form **adds** clauses (a)-(c)
above: a record registers *which real superselection sector*, irreversibly.

The downstream consequences of this addition are stated and proved in the
companion logic note, not asserted here:

- **T1 (time-ordering, partial).** Irreversibility orients record-formation
  into an order. This fixes the *direction*, not a time metric; it does not
  supersede or strengthen the existing emergent-time line.
- **T2 (classical/quantum cut).** The recordable/frozen structure is exactly
  the real Wedderburn center of the local algebra; within-block structure is
  reversible/quantum and unrecorded. This is the genuine new derived content.
- **T3 (measure dial).** On the recorded partition, the sector weight is a free
  dial `r(s) = 2^(s-1)` with two symmetry-distinguished settings: `r=1/2`
  (block-count / equipartition, the *symmetric* setting) and `r=1`
  (Born / dimension, the *default* setting).

**Non-overreach (binding frame).** The v0.4 axiom does **not** force any
generation modulus value. In particular it does **not** force the
charged-lepton Brannen modulus `r=1/2`: that value is the *symmetric* setting
on the derived dial `T3`, a stable distinguished setting where the
charged-lepton sector sits — **not forced, not exclusive**. Other sectors
occupy other settings (the per-sector occupancy `s` is a standing input, not an
axiom consequence). The framework default is `r=1` (Born/dimension). Any
reading on which the axiom "selects `r=1/2`" for all sectors is an overreach
and is explicitly disclaimed.

## Audit-Pipeline Treatment

The machine-readable source of this axiom set is the stable `minimal_axioms`
entry in `docs/audit/data/axiom_premise_nodes.json`. Dependencies on
`minimal_axioms` chain-satisfy without making downstream rows
`retained_bounded`.

The audit lane updates the `minimal_axioms` source pointer to this memo only
after independent review of the v0.4 language and logic. Until then, this memo
records the owner-approved language; the registry pointer and any downstream
re-evaluation remain audit-lane decisions. No downstream row is promoted,
bounded, or re-statused by this memo.

**Primary runner:** `scripts/record_axiom_v04_update_verifier_2026_06_05.py`
checks the elementary algebra behind T2 (center = block labels) and T3 (the
dial `r(s)=2^(s-1)` with its two distinguished settings) plus the non-overreach
guard. It does not derive or enlarge the axiom set.

Axioms and approved primitives are not Tier-A admitted derivation targets.
Depending on the Lattice, Quantum, or Record axiom, or on an explicitly
approved primitive such as `scale_reference_primitive`, must not be treated as
a source of bounded status. Bounded status belongs to non-axiom Tier-A
admissions recorded in `docs/audit/data/tier_a_admissions.json`.

## Relation To The Older Observable-Principle Parent

`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` is not this axiom note and is not an
approved axiom-premise node. It remains a broader conditional parent that
packages additive scalar observables with further readout/log-det/modulus
structure. That older parent must not be moved wholesale into
`docs/audit/data/axiom_premise_nodes.json`.

The v0.4 Record axiom adds the superselection-registration clause (a) and the
reality clause (c). It does **not** import P2/modulus, log-det, source/action,
within-sector Born weights, a time metric, normalization, scale, or arbitrary
observable identification. Rows that require any of those must still cite
separate retained authorities or remain bounded/pending per the ledger.

## Open Gates And Admissions Outside The Axioms

The three axioms do not close, import, or rename the framework's downstream open
gates. In particular, the following remain outside axiom content:

- the per-sector dial occupancy `s` (which setting each fermion sector takes;
  its direction is structural — colorless → `s=0`/`r=1/2` — but its magnitude
  is the standing Yukawa-texture / color-generation-bridge input);
- the staggered-Dirac/finite-Grassmann realization and `AC_phi_lambda`;
- the generation-factor chirality grading (an off-block, `C_3`-orbit-splitting
  operator; orthogonal to the dial — it commutes with the holomorphy structure);
- the strong-CP theta admission;
- `P2`/modulus/phase-blindness and any log-det readout theorem;
- arrow *metric*, measurement, decoherence, and record-production dynamics;
- source/action and physical-observable identification;
- `g_bare = 1` convention handling;
- the scale-reference primitive and the separate gravity self-consistency
  question that the framework's natural unit equals the Planck length.

## Historical Context

The April 15 through May 20 sequence separated the one-qubit local algebra and
the `Z^3` lattice from downstream realization gates. The 2026-06-04 memo added
Record as a narrow additivity-only premise. This 2026-06-05 memo updates Record
to v0.4 (registration of which real superselection sector, irreversibly),
under owner approval, to make the classical/quantum cut and the measure dial
explicit framework-derived content while holding the non-overreach frame on
`r=1/2`. It does not re-promote older A3/A4 material or any later derivation
target.
