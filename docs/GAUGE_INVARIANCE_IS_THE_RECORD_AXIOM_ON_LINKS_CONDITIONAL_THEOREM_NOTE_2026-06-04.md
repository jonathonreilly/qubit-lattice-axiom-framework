# Local Gauge Invariance Is the Record Axiom Applied to Links (Conditional Theorem)

**Date:** 2026-06-04
**Type:** theorem (conditional)
**Claim type:** conditional theorem — derives the local gauge constraint (the Gauss law /
gauge invariance) from the Record axiom, **conditional on** the "qulink" ontology (links carry
a relational constituent per endpoint). Does **not** touch the gauge dynamics.
**Claim scope:** adopt the qulink ontology: each lattice **link** between two node-qubits carries
one constituent ("rishon") per endpoint, and the constituent at a vertex gauge-transforms with
that vertex's node-qubit. Then the **Record axiom** — *the physical observable is the additive
logarithm of the record, and only fully-pinned (both-endpoint-determined) quantities are
observables* — selects **exactly** the gauge-invariant algebra: the commutant of the per-vertex
Gauss-law generators. Equivalently, the record-count of a link (0 / 1 / 2 endpoints recorded)
equals its gauge-invariance level (variant at both vertices / variant at one — the "lost half" /
invariant). So **local gauge invariance is not a separate postulate — it is the Record axiom
applied to links.**
**actual_current_surface_status:** conditional theorem; the lattice-gauge math (Gauss law,
Wilson line, gauge-invariant = commutant) is **standard** and is reproven from Pauli primitives
in the runner; the **contribution** is the bridge to the Record axiom. **Conditional** on
adopting qulinks (a genuine new edge degree of freedom, not currently on the surface). Not retained.
**bare_retained_allowed:** false
**Status:** independent audit required.
**Runner:** [`scripts/audit_companion_gauge_invariance_from_record_axiom_on_links_exact.py`](./../scripts/audit_companion_gauge_invariance_from_record_axiom_on_links_exact.py)

## Context

The framework places a complex qubit `M₂(ℂ)` on each **site** of `Z³` and reads observables via
the **Record axiom**. A proposed extension ("qulinks") promotes the lattice **links** to dynamical
degrees of freedom — a Quantum Link Model — where the gauge connection lives on links. A separate
result established that the natural connection between two `M₂(ℂ)` site-algebras is forced to be
**SU(2)** (`Aut M₂(ℂ) = SO(3)`, state-action `SU(2)`). This note asks: given qulinks, does **local
gauge invariance (the Gauss law)** follow from the Record axiom, or must it be postulated?

## Statement (reproven, numpy/exact)

Model a single link as two node-qubits `A`, `B` (matter) and two link-constituents `a`, `b` (one
per endpoint), `a` at the `A`-vertex and `b` at the `B`-vertex. The **Gauss-law generator** at a
vertex is the total gauge charge there (matter + its incident constituent): for U(1),
`G_A = σ^z_A + σ^z_a`, `G_B = σ^z_b + σ^z_B`; for SU(2),
`S^α_A = ½(σ^α_A + σ^α_a)`, `S^α_B = ½(σ^α_b + σ^α_B)`. An operator is **gauge-invariant at a
vertex** iff it commutes with that vertex's generator. "Recorded at a vertex" = the matter there is
pinned = the vertex generator is resolved.

1. **0 records — bare link** (`σ⁺_a σ⁻_b`): gauge-**variant at both** vertices. Not an observable.
2. **1 record — half-dressed** (`σ⁻_A σ⁺_a σ⁻_b`): invariant at `A`, **variant at `B`**. This is
   exactly the **"lost half"** — gauge-invariant at one vertex only, hence still gauge-dependent and
   **not yet a record**.
3. **2 records — Wilson line** (`σ⁻_A σ⁺_a σ⁻_b σ⁺_B`): gauge-**invariant at both** vertices. A
   genuine record / observable.
4. The **record-count equals the number of vertices where the Gauss law holds**, monotone 0→1→2.
5. **Completeness:** the full gauge-invariant algebra equals the **commutant** of `{G_A, G_B}`
   (dimension 36 = 6×6 vertex-balanced operators for U(1)) — a genuine constraint, not the whole
   `256`-dimensional operator space. So "observable = fully-pinned record" is **exactly**
   "observable = gauge-invariant," for the entire algebra, not just the examples.
6. **SU(2)** (the framework's qubit-link group): the bare link is variant at both vertices; the
   double-singlet (Wilson-type) observable is invariant at both. Same structure.

All six checks pass exactly.

## What this means

Standard gauge theory **postulates** that physical observables are gauge-invariant. Here that
postulate is **derived**: a gauge-variant quantity depends on the local frame at an *unrecorded*
vertex, so it is not fully pinned, so by the Record axiom it is not a record, so it is not an
observable. The surviving observables are precisely the relational (both-endpoint-pinned)
quantities — which is exactly the gauge-invariant algebra. **Gauge invariance = relationalism =
the Record axiom on links.** The "half-recorded" link is the precise image of a gauge-dependent
quantity: real, but not yet a fact.

## Honest scope — what is NOT claimed

- **Gauge *constraint*, not gauge *dynamics*.** This derives the Gauss law / gauge invariance (the
  kinematic constraint and the observable algebra). It says **nothing** about the gauge coupling or
  the Hamiltonian — `β=6`, the Wilson action, and the time-evolution remain inputs. A separate
  investigation confirmed no known approach (Quantum Link Models, D-theory, string-nets) derives
  the coupling from within.
- **Conditional on qulinks.** It assumes the link carries relational constituents per endpoint — a
  genuine new edge degree of freedom, not currently on the framework surface. The site-only axioms
  do not contain it.
- **The math is standard lattice gauge theory.** Gauss law, Wilson line, gauge-invariant =
  commutant are textbook; they are reproven from primitives. The **contribution** is the
  identification "gauge-invariant observable = fully-pinned record," i.e. the Record axiom *is* the
  reason observables are gauge-invariant.
- Does **not** address color SU(3) (the qubit-link gives SU(2); SU(3) needs extra per-link
  structure), nor the dynamics, nor any quantitative SM parameter.

## Trace gate

```yaml
trace_class: derivation_of_a_postulate
target_blocker_text: "local gauge invariance / the Gauss law is postulated, not derived"
source_of_blocker_text: standard_gauge_theory
reachability_to_target: derives (conditional on qulinks)
artifact_role: theorem
next_trace_action: "decide whether to adopt the qulink ontology; if so, this discharges the gauge-invariance postulate. Separately, the gauge DYNAMICS (coupling/Hamiltonian) remains an input."
```

## Forbidden imports / reprove-and-cite

- The Gauss law, Wilson line, and "gauge-invariant = commutant of the gauge generators" are
  **standard lattice gauge theory** (Kogut–Susskind; Quantum Link Models, Chandrasekharan–Wiese) —
  cited as comparators and **reproven** from Pauli primitives in the runner, never imported as a
  derivation input. No PDG values. No fitted parameters.

## Cross-references

- The qulink ontology and the SU(2)-from-link result (the gauge group of a connection between two
  `M₂(ℂ)` site-algebras is forced to be SU(2)).
- `MINIMAL_AXIOMS_2026-06-04.md` — the Record axiom (additive-log observable) this note leverages.
