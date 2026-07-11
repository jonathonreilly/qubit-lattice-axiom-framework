# Lane 7 — Thermalization / Kinetic Theory

**Date:** 2026-06-12
**Status:** PROPOSED OPEN SCIENCE LANE on `main`; no theorem or claim
promotion. This document records missing science and scopes work; it does not
close a theorem, promote any status, or add any accepted premise.
**Science priority:** HIGH-FOUNDATIONAL. Temperature, the equilibrium
distribution, and pressure are the layer that turns "matter exists" into
"a gas of atoms at temperature T exerting pressure on a container" — the
Feynman Lecture 1 picture. The framework currently imports this layer rather
than deriving it.
**Approachability:** Tier B-C. The equilibrium/temperature core (7A–7C) is
Tier B-C on existing record-dynamics scaffolding; the literal atomic-gas
targets (7D–7E) are Tier C and gated by Lane 2.
**Primary closure targets:** a derived equilibrium (Gibbs / maximum-entropy)
record-ensemble for a closed lattice region; temperature as a derived intensive
parameter conjugate to the additive Record readout; an H-theorem-style monotone
approach to that equilibrium for a lattice-excitation gas; and pressure as a
finitely-additive Record readout over wall-collision records.
**First parallel-worker target:** on an explicit small closed lattice region
(mirroring the 6-qubit exact construction in
`ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md`),
identify the stationary record-ensemble and test whether it is the
maximum-entropy state subject to the additive readout `I`, with temperature
read off as the conjugate Lagrange multiplier.
**Non-claim boundary:** this lane does NOT derive the past hypothesis, does NOT
derive record-production dynamics from the three axioms, and does NOT promote
any imported thermal bridge (Sommerfeld average, Stefan–Boltzmann `g*` bridge)
beyond its existing bounded status. The low-record/low-entropy boundary remains
a named open residual, not an approved admission, Tier-A item, primitive,
axiom, or accepted premise.

## 1. Missing-science framing

The framework still has no answer to the most basic thermodynamic questions:

> "Where does temperature come from? Does the framework derive the
> Boltzmann/Gibbs distribution, equipartition, or the ideal gas law? Is
> pressure a derived kinetic quantity, or is it assumed?"

Concretely, the framework currently has **no derivation** of:

- the equilibrium (Gibbs / canonical) distribution for a closed system;
- temperature as a derived parameter (the "thermal amount");
- an H-theorem / monotone approach to equilibrium for its own excitations;
- equipartition or a Maxwell–Boltzmann speed structure;
- pressure as the time-averaged drumming of confined excitations on a wall;
- the ideal gas law `PV ∝ (energy content)` shaped relation.

**Every "thermal" object currently in the package enters as a textbook import
or a bounded bridge inside the dark-matter / cosmology lane, not as a
derivation.** Examples on `main`:

- `dm_thermal_average_sommerfeld_textbook_import_note_2026-05-17` — a declared
  textbook import of the thermal average;
- `gstar_thermal_seven_eighths_stefan_boltzmann_bridge_narrow_theorem_note_2026-06-06`
  — a bounded `7/8` Stefan–Boltzmann bridge;
- `g_star_sm_content_at_leptogenesis_from_supplied_thermal_inventory_bounded_theorem_note_2026-05-28`
  — bounded, and explicitly takes the thermal inventory as *supplied*.

These consume thermal structure at their boundary. This lane is the missing
lane that would **derive** that structure on the framework substrate, so the
DM/cosmology rows stop importing it.

The honest comparator point (kept out of the derivation, per the comparator
rule): statistical mechanics is a layer logically independent of any
microdynamics — the Standard Model does not derive temperature either, and
every time-symmetric microtheory needs a low-entropy boundary input for an
arrow. So this lane's *residual* (the past hypothesis) is a shared open
problem, not a framework-specific gap and not an accepted premise here; only
the *derivation of the equilibrium structure given an explicit boundary model*
is the framework-side work.

## 2. Current state of repo content

### Retained / retained_bounded (relevant to thermalization)

- `arrow_from_record_formation_past_hypothesis_residual_note_2026-06-05`
  (retained_bounded) — the arrow's *direction* is record-formation-derived
  (away from the low-record boundary); record functionals increase
  monotonically from a low-record initial state (Quantum-Darwinism redundant
  broadcast). The microdynamics is time-symmetric; the arrow sign is an output
  of the initial condition.
- Born rule / `I_3 = 0` — DERIVED (supplies the within-sector outcome weights
  the equilibrium ensemble needs).
- `AXIOM_FIRST_GENERALIZED_SECOND_LAW_THEOREM_NOTE_2026-05-01` — a matter
  second law `δS_matter ≥ 0` under unital evolution, *direction-relative* to
  the low-entropy initial.
- `dispersion_relation_note` (retained_bounded) — free propagation / kinetic
  energy of a lattice excitation.

### Bounded_theorem / bounded (scaffold)

- `RECORD_CLASSICALIZATION_DYNAMICS_FIREWALL_2026-06-05.md` (bounded_theorem)
  — types the dynamics into pre-record qubit state `ρ` (unitary/CPTP), record
  instrument `{K_r}`, and post-record atom/count `e_r`, `c` with additive
  history update `c → c + e_r`; establishes "a stable route to unbounded
  recorded history." This is the bookkeeping skeleton for equilibrium
  ensembles vs. realized records.
- Decoherence rows: `decoherence_action_independence_note`,
  `decoherence_action_zero_field_per_link_phase_equality_narrow_theorem_note_2026-05-17`,
  `matched_2d_4d_decoherence_note` (retained_bounded). A *universal*
  decoherence law is deferred as "Gate A" in the review-hardening backlog.

### Comparison-only thermal imports (to be replaced, not relied upon)

- `dm_thermal_average_sommerfeld_textbook_import_note_2026-05-17`,
  `gstar_thermal_seven_eighths_stefan_boltzmann_bridge_narrow_theorem_note_2026-06-06`,
  `dm_full_closure_same_surface_thermal_*` selector rows. These are disclosed
  comparators / imports; this lane aims to make them derivable, not to cite
  them as derivation steps.

### Negative precedent (firewall to respect)

- `FLAVOR_RECORD_DYNAMICS_SHARPENS_ARROW_STABILIZER_FAILS_2026-06-02` /
  `flavor_r_half_stable_under_thermalizing_arrow_2026-06-02` (retained_bounded)
  — a thermalizing-arrow stabilizer route could **not** force the Koide value.
  Lesson: a thermalizing-arrow argument is not a free selector; do not reopen
  that route to force unrelated values.

### Absent (the lane's gap)

- equilibrium/Gibbs ensemble derived from record statistics;
- temperature as a derived intensive parameter;
- quantitative H-theorem / relaxation rate for lattice excitations;
- equipartition / Maxwell–Boltzmann structure;
- pressure as additive wall-collision record readout;
- ideal-gas-law-shaped relation;
- transport coefficients (viscosity, diffusion, conductivity).

## 3. Derivation targets

### 7A. Equilibrium ensemble from record statistics

**Target:** show that the stationary record-ensemble of a closed lattice region
under record-forming dynamics is the maximum-entropy (Gibbs) state subject to
the additive Record readout `I`. Use the nonselective ensemble object
`sum_r K_r ρ K_r^*` from the classicalization firewall (§4) as the ensemble
layer, and the generalized-second-law monotonicity to identify the stationary
point as the entropy maximizer.

**Approachability:** Tier B-C. Tractable first on the explicit small-region
construction; the general-region statement is Tier C.

### 7B. H-theorem / monotone approach to equilibrium

**Target:** strengthen the *direction-relative* `δS_matter ≥ 0` into a
quantitative monotone relaxation of a free / weakly-interacting lattice-
excitation gas toward the 7A equilibrium, with an explicit relaxation
functional. Must remain modulo the past-hypothesis boundary (7F).

**Approachability:** Tier C.

### 7C. Temperature as a derived intensive parameter

**Target:** define temperature as the parameter conjugate to the additive
Record readout `I` (energy-count) at the 7A maximum-entropy state — the
Lagrange multiplier of the constrained entropy maximization. This is where the
**Record axiom's finite additivity (extensivity) meets an intensive
equilibrium parameter**: `I` is extensive over disjoint record collections, and
its conjugate is intensive. Verify it behaves as a thermometer reading (zeroth
law: transitivity of equilibrium across a shared boundary).

**Approachability:** Tier B-C. Pairs naturally with 7A.

### 7D. Pressure as additive wall-collision record readout (the Feynman gas)

**Target:** for a confined excitation gas, identify pressure as the finitely-
additive Record readout `I` over wall-collision records, yielding an
ideal-gas-law-shaped relation `PV ∝ (energy content)`. This is the literal
Feynman Lecture 1 target: atoms drumming on the container wall.

**Depends on Lane 2** (an emergent atom exists) **and a boundary condition**
(the Lattice axiom supplies none; the wall is bound matter that reflects an
excitation — a Lane 2 follow-on). Wave-lane boundary-sensitivity rows
(`wave_static_boundary_sensitivity_note` and the fixed-beam boundary family,
retained_bounded) provide reflection scaffolding.

**Approachability:** Tier C, gated by Lane 2.

### 7E. Equipartition / Maxwell–Boltzmann structure

**Target:** derive the speed/energy distribution of lattice excitations at the
7A equilibrium and the equipartition of energy across modes.

**Approachability:** Tier C.

### 7F. Past-hypothesis residual — named open residual

**Target:** record the low-record / low-entropy boundary as an explicit open
residual and guardrail. It is not registered or approved as an accepted
premise, Tier-A item, primitive, or axiom; any future admission or primitive
treatment requires explicit owner approval. **This is a `/no-go-gate` target,
not a derivation:** the lane does not derive the past hypothesis and must not
claim to remove it.

**Approachability:** Tier A as a scoping/firewall artifact, not as closure.

### 7G. Transport coefficients (deferred follow-on)

**Target:** viscosity, diffusion, and thermal conductivity for the lattice gas
(Feynman's later-chapter material).

**Approachability:** Tier C+. Deferred from initial lane closure.

## 4. Existing scaffolding to build on

- [ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md](../../ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md)
  (retained_bounded) — arrow direction + explicit small-system construction +
  past-hypothesis residual ledger.
- [RECORD_CLASSICALIZATION_DYNAMICS_FIREWALL_2026-06-05.md](../../RECORD_CLASSICALIZATION_DYNAMICS_FIREWALL_2026-06-05.md)
  (bounded_theorem) — pre-/record/post-record typed surfaces; ensemble vs.
  realized-record distinction; unbounded recorded history.
- [AXIOM_FIRST_GENERALIZED_SECOND_LAW_THEOREM_NOTE_2026-05-01.md](../../AXIOM_FIRST_GENERALIZED_SECOND_LAW_THEOREM_NOTE_2026-05-01.md)
  — `δS_matter ≥ 0` under unital evolution (direction-relative).
- `docs/ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md`
  — comparison only for how accepted inputs are governed; this lane does not
  register the past hypothesis there.
- Born rule / `I_3 = 0` (derived) — within-sector outcome weights.
- `dispersion_relation_note` (retained_bounded) — free kinetic propagation.
- Decoherence bounded rows + the deferred "Gate A" universal decoherence law.
- DM/cosmology thermal bridge/import rows — as comparison targets to replace,
  not as derivation steps.

## 5. Recommended attack approach

**Phase 1 — boundary and target scoping (Tier A):**

1. **7F: record the past-hypothesis residual.** Run `/no-go-gate`; record the
   low-record boundary as a named open residual, not an accepted premise.
   Everything downstream is conditional on an explicit boundary model.
2. **7A/7C scoping on the explicit small region.** Reuse the arrow note's
   6-qubit exact construction; test whether the stationary record-ensemble is
   the maximum-entropy state and read temperature off as the conjugate
   multiplier. Land as one source note + one exact runner + one cached output.

**Phase 2 — equilibrium core (Tier B-C):**

3. **7A: equilibrium ensemble from record statistics** (general region).
4. **7C: temperature as the conjugate of additive `I`** (zeroth-law check).
5. **7B: H-theorem / monotone relaxation.**

**Phase 3 — the literal gas (Tier C, gated by Lane 2):**

6. **7D: pressure as additive wall-collision readout + ideal-gas relation.**
7. **7E: equipartition / Maxwell–Boltzmann structure.**

**Phase 4 — deferred:**

8. **7G: transport coefficients.**

## 6. Out of scope / will not claim

- This lane does NOT derive the past hypothesis or a preferred low-entropy
  initial condition; the residual remains open (7F is a firewall, not a
  derivation or admission).
- This lane does NOT derive record-production dynamics from the three axioms;
  like the arrow note, it uses explicit record-forming models as stand-ins and
  keeps that gate open.
- This lane does NOT claim to replace standard statistical mechanics; it aims to
  reproduce its structure on the framework substrate.
- This lane does NOT close Lane 2 (an emergent atom); the literal atomic-gas
  targets (7D–7E) depend on it.
- This lane does NOT promote any imported thermal bridge (Sommerfeld average,
  Stefan–Boltzmann `g*` bridge) to retained status.
- This lane does NOT reopen the thermalizing-arrow stabilizer as a value
  selector (closed negatively for Koide; respect that firewall).

## 7. Cross-references

- Depends on: Born rule (derived), arrow-from-record (retained_bounded),
  generalized second law, the classicalization firewall, decoherence Gate A.
- Gated by: Lane 2 (atomic scale) for the literal gas/pressure targets (7D–7E);
  Lane 2 in turn depends on Lanes 6 and 1.
- Connects to: DM/cosmology thermal bridge rows (`g*`, leptogenesis thermal
  inventory) that currently import the structure this lane would derive.
- Independent of: Lanes 3 and 6 in the equilibrium/temperature core (7A–7C);
  those enter only for the literal atomic gas.
- Open residual: the past hypothesis is a shared low-boundary problem, not an
  approved admission, primitive, axiom, or chain-satisfying premise in this
  lane.

## 8. Reviewer questions

1. Is "equilibrium ensemble from record statistics" (7A) the right entry point,
   or should temperature (7C) be defined first and the ensemble characterized
   as its level sets?
2. Should 7F remain only a named open residual, or should a future
   owner-approved proposal attempt to register it? No approval is granted by
   this lane.
3. Is "pressure = finitely-additive Record readout over wall-collision records"
   (7D) the right operationalization of the Record axiom's additivity, or is
   there a cleaner extensivity→intensivity bridge for temperature/pressure?
4. Should this be Lane 7 in the active package, or a deferred follow-on, given
   it post-dates the original six-lane selection and its core (7A–7C) is
   independent of the matter-mass lanes while its gas target (7D) is gated by
   Lane 2?
5. What counts as "thermalization retained" — a structural H-theorem (7B), a
   derived temperature with zeroth-law transitivity (7C), or a quantitative
   ideal-gas-law-shaped relation (7D)?
