# Lane 9 — Phases of Matter & Phase Transitions

**Date:** 2026-06-12
**Status:** PROPOSED OPEN SCIENCE LANE on `main`; no theorem or claim
promotion. Records missing science and scopes work; closes no theorem,
promotes no status, and adds no accepted premise.
**Science priority:** HIGH-FOUNDATIONAL. Solid / liquid / gas, melting and
boiling, order parameters, latent heat — Feynman Lecture 1's ice → water →
steam. The natural sequel to the thermalization lane (Lane 7): once temperature
and an equilibrium ensemble exist, phase structure is the next question.
**Approachability:** Tier C. Gated by Lane 7 (temperature / equilibrium) and
Lane 2 (interacting atoms); critical-phenomena scaffolding (universality)
partially exists.
**Primary closure targets:** an order-parameter / free-energy framework derived
from record statistics; the solid/liquid/gas distinction as
symmetry-breaking on the emergent continuum; a first-order transition with
latent heat (Clausius–Clapeyron); and a critical-point / universality result.
**First parallel-worker target:** on the Lane 7 equilibrium ensemble for an
interacting lattice region, identify an order parameter and show a
non-analyticity (a phase boundary) in the derived free energy as a function of
the Lane 7 temperature.
**Non-claim boundary:** depends on Lane 7 and Lane 2; does not derive or
admit the past-hypothesis residual inherited as open from Lane 7; does not
claim to replace standard statistical mechanics of phase transitions.

## 1. Missing-science framing

The framework has no answer to:

> "Why does matter form solids, liquids, and gases? What drives melting and
> boiling? Is there a derived order parameter, a latent heat, a critical point?"

This is the **other half of Feynman Lecture 1** — the ice/water/steam phases —
and it has no lane. The closest inventory item is "strongly correlated systems"
(Tier 4 item 31, deferred), which is adjacent but not the same as the
equilibrium phase structure of ordinary matter.

**Substrate-vs-material caution (bake this into the lane).** Feynman's ice
crystal is an *emergent, material* lattice of atoms that can *melt*; the
framework's `Z^3` is the *fixed substrate of space*, which cannot melt. The two
must not be conflated. The solid phase in this lane is broken **emergent**
translation symmetry of a many-atom state on the continuum, not a property of
the substrate `Z^3`. This distinction is a correctness requirement for every
target below.

## 2. Current state of repo content

### Retained / retained_bounded (relevant)

- (Lane 7, once landed) equilibrium ensemble + temperature + generalized
  second law — the thermodynamic substrate this lane builds on.
- Emergent Lorentz / continuum limit (derived) — needed to speak of broken
  *emergent* translation symmetry rather than substrate structure.

### Bounded / scaffold

- [UNIVERSALITY_CLASSIFIER_NOTE.md](../../UNIVERSALITY_CLASSIFIER_NOTE.md) —
  universality-class classification scaffolding, directly relevant to critical
  phenomena (9D).
- "Strongly correlated systems" (Tier 4 item 31) — deferred; adjacent
  many-body scaffolding.

### Absent (the lane's gap)

- order-parameter / free-energy framework from record statistics;
- solid/liquid/gas distinction as emergent symmetry breaking;
- first-order transition + latent heat (Clausius–Clapeyron);
- critical exponents / a derived universality result;
- equation of state across phases.

## 3. Derivation targets

### 9A. Order parameter & free energy from record statistics

**Target:** on the Lane 7 equilibrium ensemble for an interacting lattice
region, derive a free-energy functional and identify an order parameter whose
non-analyticity marks a phase boundary. **Approachability:** Tier C (gated by
Lane 7).

### 9B. Solid / liquid / gas as emergent symmetry breaking

**Target:** characterize the gas (full emergent translation symmetry), liquid
(short-range order), and solid (broken emergent translation symmetry — a
*material* crystal on the continuum, distinct from substrate `Z^3`) as distinct
equilibrium phases. **Approachability:** Tier C (gated by Lane 2 interactions).

### 9C. First-order transition + latent heat

**Target:** a melting/boiling transition with a derived latent heat and the
Clausius–Clapeyron slope of the phase boundary. **Approachability:** Tier C.

### 9D. Critical point + universality

**Target:** a continuous transition with derived critical exponents and a
universality-class assignment, using the universality classifier scaffolding.
**Approachability:** Tier C (the classifier exists; the equilibrium ensemble
does not yet).

## 4. Existing scaffolding to build on

- Lane 7 (thermalization / kinetic theory) — direct parent; supplies
  temperature, equilibrium, the H-theorem.
- [UNIVERSALITY_CLASSIFIER_NOTE.md](../../UNIVERSALITY_CLASSIFIER_NOTE.md) — for 9D.
- Lane 2 (atomic) — interacting-atom content for 9B/9C.
- Emergent continuum / Lorentz (derived) — to keep "solid" an emergent-matter
  statement, not a substrate one.

## 5. Recommended attack approach

**Phase 1 (after Lane 7 core):** 9A — order parameter + free-energy
non-analyticity on the Lane 7 ensemble; land as one source note + one runner +
one cached output.
**Phase 2 (after Lane 2 interactions):** 9B solid/liquid/gas; 9C latent heat.
**Phase 3:** 9D critical exponents / universality.

## 6. Out of scope / will not claim

- Does NOT conflate the substrate `Z^3` with a material crystal; "solid" is
  broken emergent symmetry of a many-atom state.
- Does NOT derive or admit the past hypothesis (inherited as an open residual
  from Lane 7's 7F).
- Does NOT claim to replace standard statistical mechanics of phase
  transitions; it reproduces the structure on the framework substrate.
- Does NOT close Lane 7 or Lane 2; it depends on both.
- Does NOT target exotic phases (superconductivity, quantum Hall, topological
  order) in initial scope.

## 7. Cross-references

- Depends on: Lane 7 (temperature/equilibrium/H-theorem); Lane 2 (interacting
  atoms); emergent continuum/Lorentz (derived).
- Uses: the universality classifier for 9D.
- Independent of: Lanes 3, 6 (matter masses) in the order-parameter core.
- Conceptual link: resolves the substrate-vs-material-lattice distinction
  raised in the Feynman-Lecture-1 discussion that motivated Lanes 7–9.

## 8. Reviewer questions

1. Is "order parameter + free-energy non-analyticity on the Lane 7 ensemble"
   (9A) the right entry point, or should an explicit small-system transition be
   demonstrated first?
2. Should the substrate-vs-material caution be elevated to a named firewall
   note (it is a recurring conflation risk)?
3. What counts as "phase structure retained" — one demonstrated transition
   (9A/9C), or the full solid/liquid/gas trichotomy (9B)?
4. Should Lane 9 wait on Lane 7 landing before activation, or proceed in
   parallel on the equilibrium-ensemble assumption?
