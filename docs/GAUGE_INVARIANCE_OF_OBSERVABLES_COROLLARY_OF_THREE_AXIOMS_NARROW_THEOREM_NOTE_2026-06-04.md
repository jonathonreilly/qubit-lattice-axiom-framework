# Gauge Invariance of Observables Is a Corollary of {Quantum, Locality, Record} (Narrow Theorem)

**Date:** 2026-06-04
**Type:** theorem (narrow)
**Claim type:** narrow theorem — local gauge invariance **of observables** is a corollary of
the three existing axioms. **No additional axiom is required** — in particular, **no
quantum-link / "qulink" ontology** is needed; that was scaffolding in an earlier framing.
**Claim scope:** From `{Quantum: each site is its own qubit M₂(ℂ), no canonical cross-site
basis}` + `{Locality + minimality: no global frame is postulated}` + `{Record: an observable
is a determined record}`, it follows that **the observables are exactly the gauge-invariant
(relational) quantities**. Standard gauge theory *postulates* "observables are gauge-invariant";
here it is a *consequence of the observable principle*. This is the gauge **constraint** (which
quantities are physical), **not** the gauge **dynamics** (the gauge-invariance of the action,
gauge bosons, minimal coupling, β=6 — all separate and untouched).
**actual_current_surface_status:** narrow theorem resting on the existing three axioms; the
lattice-gauge math (Gauss law, Wilson line, gauge-invariant = commutant) is **standard** and is
reproven from Pauli primitives in the runner; the **contribution** is the grounding of
"observables are gauge-invariant" in the Record axiom. Not retained.
**bare_retained_allowed:** false
**Status:** independent audit required.
**Runner:** [`scripts/audit_companion_gauge_invariance_from_record_axiom_on_links_exact.py`](./../scripts/audit_companion_gauge_invariance_from_record_axiom_on_links_exact.py)

## The derivation (axiom-level; no new structure)

1. **Quantum** — each site carries its *own* qubit `M₂(ℂ)`. There is no canonical identification
   of one site's basis with a neighbour's.
2. **Locality + minimality** — no *global* frame is postulated (adding one would be extra,
   non-minimal structure). Hence the only thing relating adjacent sites' bases is a **connection
   (relative frame)**, and a **local gauge transformation is an independent choice of basis at
   each site**. The connection's value is fixed by nothing — it is gauge freedom.
3. **Record** — an observable is a *determined* record. A gauge-variant quantity changes under
   the unfixed local-frame choice, so it is **not determined → not a record → not an observable**.
4. ∴ **The observables are exactly the gauge-invariant (relational) quantities** — the Gauss-law
   constraint.

Every premise is already on the surface. The "qulink" (dynamical link-qubit) ontology is **not**
used: the connection between per-site qubits already exists the moment there are local interactions,
and its gauge freedom is the per-site frame freedom of premise 2.

## Verification (concrete finite-dim illustration, numpy, 6/6)

The rishon realization (one link-constituent per endpoint) makes the chain explicit and
finite-dimensional. Node-qubits `A, B` (matter) + constituents `a, b` (one per endpoint). The
**gauge generator at a vertex is the per-site qubit's own su(2)** acting on the site and its
incident link-end (`S^α_A = ½(σ^α_A + σ^α_a)`) — i.e. the gauge symmetry *is* the intrinsic
per-site frame rotation, not an added symmetry. Then:

1. **0 records — bare link**: gauge-variant at both vertices → not an observable.
2. **1 record — half-dressed**: invariant at one vertex, variant at the other — the **"lost half"**
   — still gauge-dependent, not yet a record. (In the rishon model the link entropy falls exactly
   2→1 bit; see the companion `node_link_record` check.)
3. **2 records — Wilson line**: gauge-invariant at both → a genuine record / observable.
4. **record-count = number of vertices where the Gauss law holds**, monotone 0→1→2.
5. **Completeness**: the gauge-invariant algebra = the **commutant** of `{G_A, G_B}` (dim 36 = 6×6
   for U(1); the whole algebra, not just examples).
6. **SU(2)** (the link automorphism group `Aut M₂(ℂ)=SO(3)`): same structure.

The rishon model is an **illustration** of the axiom-level chain above, *not* a premise of it.

## What is and is not gained

- **No new axiom.** Gauge invariance of observables drops out of the three axioms read minimally.
- **One fewer brute postulate.** "Observables are gauge-invariant" is normally *postulated* (the
  Gauss-law constraint) or read off an assumed gauge-invariant action. Here it is a **corollary of
  the Record axiom** + per-site Quantum — the observable principle *explains* gauge invariance.
- **Constraint, not dynamics.** This says *which* quantities are physical. It says nothing about
  the gauge-invariance of the *action*, the gauge bosons, minimal coupling, or β=6 — those are the
  gauge **dynamics**, separate and still an input. No quantitative SM parameter is touched.
- Does **not** address color SU(3) (the link automorphism gives SU(2); SU(3) needs extra per-link
  structure), and does **not** require or establish the dynamical-link (qulink) ontology.

## Trace gate

```yaml
trace_class: derivation_of_a_postulate
target_blocker_text: "observables-are-gauge-invariant is an independent postulate"
source_of_blocker_text: standard_gauge_theory
reachability_to_target: derives (from the existing three axioms; no new axiom)
artifact_role: theorem
next_trace_action: "build the electroweak gauge KINEMATICS on top (SU(2) from the link automorphism + U(1); flag color SU(3) as the gap). Separately, the gauge DYNAMICS / coupling remains an input."
```

## Forbidden imports / reprove-and-cite

- The Gauss law, Wilson line, and "gauge-invariant = commutant of the gauge generators" are
  **standard lattice gauge theory** (Kogut–Susskind; Quantum Link Models, Chandrasekharan–Wiese) —
  cited as comparators and **reproven** from Pauli primitives in the runner, never imported as a
  derivation input. No PDG values; no fitted parameters.

## Cross-references

- `MINIMAL_AXIOMS_2026-06-04.md` — the Record axiom (additive-log observable) and the per-site
  Quantum / Locality axioms this corollary rests on.
- The SU(2)-from-link-automorphism result (`Aut M₂(ℂ)=SO(3)`, state-action SU(2)) — the gauge
  *group* that pairs with this gauge *constraint*.
