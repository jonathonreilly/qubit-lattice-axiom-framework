# Lane 10 — Continuum / Hydrodynamics

**Date:** 2026-06-12
**Status:** PROPOSED OPEN SCIENCE LANE on `main`; no theorem or claim
promotion. Records missing science and scopes work; closes no theorem,
promotes no status, and adds no accepted premise.
**Scope caveat (read first):** this lane **overlaps Lane 7's transport target
(7G) and the existing emergent-continuum work**. It is scoped separately at the
owner's request, but reviewers should explicitly decide whether to keep it
standalone or fold it into Lane 7. The recommendation in the Lane 7 scoping was
to fold; this document keeps the fold-vs-standalone decision live (reviewer
question #1).
**Science priority:** MEDIUM-FOUNDATIONAL. The macroscopic fluid limit —
Euler / Navier–Stokes, sound — that turns a thermalized excitation gas into the
continuous "fluid in a container" of everyday experience.
**Approachability:** Tier C. Gated by Lane 7 (equilibrium + transport) and the
emergent-continuum limit.
**Primary closure targets:** a coarse-graining map from lattice excitations to
continuum hydrodynamic fields; Euler / Navier–Stokes from the derived
conservation laws; a sound-speed / dispersion result; and transport
coefficients (shared with Lane 7's 7G).
**First parallel-worker target:** derive the continuity + momentum equations
(Euler limit) for a thermalized lattice-excitation gas by coarse-graining the
Lane 7 equilibrium ensemble, using the retained lattice Noether continuity
identity.
**Non-claim boundary:** does not derive or admit the past-hypothesis residual
inherited as open from Lane 7; does not claim turbulence or strong-shock
regimes; substantially overlaps Lane 7 and may be retired into it.

## 1. Missing-science framing

The framework has no answer to:

> "Does the framework give the continuum fluid equations — Euler, Navier–Stokes
> — and the speed of sound, as the macroscopic limit of its excitations?"

This is the bridge from Lane 7's *microscopic* kinetic gas to the *macroscopic
continuum* fluid. It is genuinely absent as a lane, but it is **not** a
clean-slate gap: Lane 7's transport target (7G), the retained lattice Noether
continuity identity, the dispersion-relation note, and the broader
emergent-continuum work (emergent Lorentz, discrete-to-continuum gravity) all
already cover pieces of it. Hence the standing fold-vs-standalone question.

## 2. Current state of repo content

### Retained / retained_bounded (relevant)

- [AXIOM_FIRST_LATTICE_NOETHER_THEOREM_NOTE_2026-04-29.md](../../AXIOM_FIRST_LATTICE_NOETHER_THEOREM_NOTE_2026-04-29.md)
  — lattice Noether / abstract-bilinear continuity: the conservation-law
  backbone for continuity + momentum equations.
- [DISPERSION_RELATION_NOTE.md](../../DISPERSION_RELATION_NOTE.md)
  (retained_bounded) — excitation dispersion; the seed of a sound-speed result.
- Emergent Lorentz / continuum limit (derived) and discrete-to-continuum
  gravity (retained on a canonical textbook target) — existing continuum-limit
  machinery.

### Bounded / scaffold

- Lane 7's 7G (transport coefficients) — same physical content as this lane's
  transport target.

### Absent (the lane's gap)

- coarse-graining map lattice excitations → hydrodynamic fields;
- Euler / Navier–Stokes from the conservation laws;
- derived speed of sound;
- transport coefficients (viscosity, diffusion, thermal conductivity) — shared
  with 7G.

## 3. Derivation targets

### 10A. Coarse-graining to hydrodynamic fields

**Target:** a derived map from the Lane 7 equilibrium ensemble of lattice
excitations to continuum density / velocity / energy fields. **Approachability:**
Tier C (gated by Lane 7).

### 10B. Euler / Navier–Stokes from conservation laws

**Target:** the continuity and momentum equations (Euler, ideal limit) from the
retained lattice Noether continuity identity, then the dissipative
Navier–Stokes corrections. **Approachability:** Tier C.

### 10C. Speed of sound

**Target:** a derived sound speed from the dispersion relation + equation of
state. **Approachability:** Tier B-C (dispersion scaffolding exists).

### 10D. Transport coefficients (shared with Lane 7 7G)

**Target:** viscosity, diffusion, thermal conductivity. **Explicitly shared
with Lane 7's 7G** — to be owned by exactly one lane after the
fold-vs-standalone decision. **Approachability:** Tier C+.

## 4. Existing scaffolding to build on

- [AXIOM_FIRST_LATTICE_NOETHER_THEOREM_NOTE_2026-04-29.md](../../AXIOM_FIRST_LATTICE_NOETHER_THEOREM_NOTE_2026-04-29.md)
- [DISPERSION_RELATION_NOTE.md](../../DISPERSION_RELATION_NOTE.md)
- Lane 7 (equilibrium ensemble, temperature, H-theorem, transport).
- Emergent continuum / Lorentz machinery (derived).

## 5. Recommended attack approach

**Phase 0:** resolve fold-vs-standalone with reviewers (this lane vs. Lane 7
7G).
**Phase 1 (after Lane 7 core):** 10A coarse-graining; 10B Euler limit from
lattice Noether continuity.
**Phase 2:** 10C sound speed; 10D transport (single-owner).
**Deferred:** dissipative Navier–Stokes, turbulence (out of initial scope).

## 6. Out of scope / will not claim

- Does NOT claim turbulence, strong shocks, or boundary-layer theory in initial
  scope.
- Does NOT derive or admit the past hypothesis (inherited as an open residual
  from Lane 7).
- Does NOT duplicate Lane 7's 7G transport ownership — that must be assigned to
  one lane.
- Does NOT re-derive the continuum limit or conservation laws already retained;
  it applies them.

## 7. Cross-references

- Depends on: Lane 7 (equilibrium/transport); retained lattice Noether
  continuity; dispersion note; emergent continuum.
- Overlaps: Lane 7 7G (transport) — fold candidate.
- Independent of: Lanes 2, 3, 6 in the conservation-law core (the literal
  atomic fluid would gate on Lane 2).

## 8. Reviewer questions

1. **Fold or standalone?** Should this lane be retired into Lane 7 (as 7G +
   a continuum-limit sub-target), or kept as a separate macroscopic-fluid lane?
2. If standalone, which lane owns transport coefficients (10D vs. 7G)?
3. What counts as "hydrodynamics retained" — the Euler limit (10B), or the full
   dissipative Navier–Stokes?
4. Is the retained lattice Noether continuity identity sufficient for 10B, or is
   an additional local-equilibrium closure premise required?
