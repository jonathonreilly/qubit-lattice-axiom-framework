# Lane 8 — Classical Electromagnetism & Light

**Date:** 2026-06-12
**Status:** PROPOSED OPEN SCIENCE LANE on `main`; no theorem or claim
promotion. Records missing science and scopes work; closes no theorem,
promotes no status, and adds no accepted premise.
**Science priority:** HIGH-FOUNDATIONAL / HIGH-VISCERAL. "Where does light come
from, and how does it propagate?" — most of Feynman Volumes 1–2. The framework
lists the `U(1)` gauge group as derived but carries no lane lifting it to
Maxwell's equations, EM radiation, or optics.
**Approachability:** Tier B-C. Lattice-gauge → continuum Maxwell is Tier B on
standard lattice-gauge methodology; radiation/optics are Tier C; the absolute
Coulomb coupling `α(0)` is gated by Lane 2.
**Primary closure targets:** retained Maxwell's equations as the continuum limit
of the derived `U(1)` lattice gauge content; EM radiation / retarded fields with
the photon as the massless vector; the Coulomb law in physical units; and a
geometric/wave-optics follow-on.
**First parallel-worker target:** isolate the dependency chain from the derived
`U(1)` gauge content + emergent Lorentz to the continuum Maxwell equations on a
finite lattice region, identifying exactly which inputs (lattice spacing scale,
`α(0)`) are external vs. framework-derived.
**Non-claim boundary:** current EM content is scattered electrostatics notes,
not a retained classical-electrodynamics layer; this lane scopes the gap and
does not close it. It does NOT target QED-precision tests and does NOT address
strong-field / nonperturbative EM in initial scope.

## 1. Missing-science framing

The framework still has no direct answer to:

> "Does the framework reproduce Maxwell's equations? Where does light come from,
> and why does it move at `c`? Does Coulomb's law fall out, and with what
> coupling?"

Plus follow-ups: EM radiation from accelerated charges; geometric optics
(reflection/refraction); wave optics (interference/diffraction); the
polarization and masslessness of the photon.

**The current package has scattered electrostatics notes
([ELECTROSTATICS_CARD_NOTE.md](../../ELECTROSTATICS_CARD_NOTE.md),
[ELECTRIC_SIGN_LAW_NOTE.md](../../ELECTRIC_SIGN_LAW_NOTE.md),
[ELECTROSTATICS_SUPERPOSITION_PROXY_NOTE.md](../../ELECTROSTATICS_SUPERPOSITION_PROXY_NOTE.md))
and a gravity-flavored wave-propagation package, but no lane that assembles them
into the classical-electrodynamics layer.** The `U(1)` gauge group is derived;
the layer from gauge content up to fields, radiation, and light is absent.

Comparator note (kept out of the derivation, per the comparator rule): standard
lattice gauge theory recovers continuum Maxwell as the naive continuum limit of
compact `U(1)`; that established result names the target but must not be a step
in the framework-side derivation.

## 2. Current state of repo content

### Retained / retained_bounded (relevant to EM/light)

- `U(1)` gauge group — DERIVED (Tier 5 inventory item 38).
- `massless_vector_polarization_count_from_lorentz_and_gauge_bounded_theorem_note_2026-05-28`
  (retained_bounded) — two physical polarizations for a massless vector from
  Lorentz + gauge: the photon's transverse-mode count.
- Emergent Lorentz invariance — DERIVED at low energy (Tier 5 item 48), incl.
  2D exact boost covariance; supplies the `c` and the relativistic field
  structure EM needs.
- Wave-propagation package (retained_bounded, gravity-flavored but reusable):
  [WAVE_RADIATION_NOTE.md](../../WAVE_RADIATION_NOTE.md),
  [WAVE_RETARDATION_CONTINUUM_LIMIT_NOTE.md](../../WAVE_RETARDATION_CONTINUUM_LIMIT_NOTE.md),
  [DISPERSION_RELATION_NOTE.md](../../DISPERSION_RELATION_NOTE.md).
- `1/α_EM(M_Z) = 127.67` (sub-percent) — the EM coupling at the `Z` scale.

### Bounded / scaffold (electrostatics)

- ELECTROSTATICS_CARD_NOTE, ELECTRIC_SIGN_LAW_NOTE,
  ELECTROSTATICS_SUPERPOSITION_PROXY_NOTE — Coulomb-sign / superposition
  proxies on the lattice; not a retained continuum Coulomb law in physical
  units.

### Absent (the lane's gap)

- Maxwell's equations as a retained continuum limit;
- retarded EM fields / Liénard–Wiechert / radiation from accelerated charge;
- Coulomb's law in physical units with `α(0)`;
- geometric and wave optics;
- the low-energy coupling `α(0)` from framework (Lane 2 dependency).

## 3. Derivation targets

### 8A. Continuum Maxwell from `U(1)` lattice gauge content

**Target:** derive the source-free Maxwell equations as the continuum limit of
the derived compact-`U(1)` plaquette action on the `Z^3` lattice (+ emergent
Lorentz for the time axis), with the field strength `F_{μν}` as the
plaquette-curvature continuum object. **Approachability:** Tier B (standard
lattice-gauge methodology on the framework substrate).

### 8B. Radiation / retarded fields / photon

**Target:** retarded EM fields and radiation from accelerated sources, with the
photon as the massless transverse vector (lean on the polarization-count row +
the wave-radiation/retardation package). **Approachability:** Tier B-C.

### 8C. Coulomb's law in physical units

**Target:** promote the electrostatics proxies to a retained `1/r` Coulomb law
with the correct coupling, using `α(0)`. **Depends on Lane 2** for `α(0)` / the
nonrelativistic physical-unit bridge (same firewall as the atomic Rydberg
gate). **Approachability:** Tier B post-Lane-2.

### 8D. Geometric + wave optics (follow-on)

**Target:** reflection/refraction (Fermat / eikonal limit) and
interference/diffraction from the retained wave equation. **Approachability:**
Tier C.

### 8E. `α(0)` running bridge

**Target:** connect retained `1/α_EM(M_Z) = 127.67` to the low-energy `α(0) ≈
1/137` via a retained QED running bridge. **Shared with Lane 2.**
**Approachability:** Tier B-C.

## 4. Existing scaffolding to build on

- Derived `U(1)` gauge group + canonical plaquette/coupling package.
- [MASSLESS_VECTOR_POLARIZATION_COUNT_FROM_LORENTZ_AND_GAUGE_BOUNDED_THEOREM_NOTE_2026-05-28.md](../../MASSLESS_VECTOR_POLARIZATION_COUNT_FROM_LORENTZ_AND_GAUGE_BOUNDED_THEOREM_NOTE_2026-05-28.md)
- [WAVE_RADIATION_NOTE.md](../../WAVE_RADIATION_NOTE.md),
  [WAVE_RETARDATION_CONTINUUM_LIMIT_NOTE.md](../../WAVE_RETARDATION_CONTINUUM_LIMIT_NOTE.md),
  [DISPERSION_RELATION_NOTE.md](../../DISPERSION_RELATION_NOTE.md)
- [ELECTROSTATICS_CARD_NOTE.md](../../ELECTROSTATICS_CARD_NOTE.md),
  [ELECTRIC_SIGN_LAW_NOTE.md](../../ELECTRIC_SIGN_LAW_NOTE.md),
  [ELECTROSTATICS_SUPERPOSITION_PROXY_NOTE.md](../../ELECTROSTATICS_SUPERPOSITION_PROXY_NOTE.md)
- Emergent Lorentz (derived) for the time axis and `c`.

## 5. Recommended attack approach

**Phase 1 (Tier B):** 8A — continuum Maxwell from the plaquette action on an
explicit finite region; land as one source note + one exact/lattice runner +
one cached output.
**Phase 2:** 8B radiation/photon; 8E `α(0)` running bridge.
**Phase 3 (post-Lane-2):** 8C Coulomb in physical units.
**Phase 4:** 8D optics.

## 6. Out of scope / will not claim

- Does NOT target QED-precision tests (g−2, Lamb shift — those are Lane 2);
  the EM coupling is reproduced at sub-percent, not at QED precision.
- Does NOT address strong-field / nonperturbative EM (Schwinger pair
  production, etc.) in initial scope.
- Does NOT re-derive the `U(1)` gauge group (already derived) or emergent
  Lorentz (already derived); it builds on them.
- Does NOT close `α(0)` independently of Lane 2.

## 7. Cross-references

- Depends on: derived `U(1)` + plaquette package, emergent Lorentz; Lane 2 for
  `α(0)` and physical-unit Coulomb.
- Connects to: Lane 2 (atomic) shares the `α(0)` bridge; the wave-propagation
  package (gravity-flavored) is reused here for EM radiation.
- Independent of: Lanes 3, 6 (matter masses) in the field-equation core.

## 8. Reviewer questions

1. Is continuum Maxwell from the plaquette action (8A) the right entry point,
   or should the photon/polarization route (8B) lead?
2. Should `α(0)` (8E) be owned here or by Lane 2, given both need it?
3. What counts as "classical EM retained" — source-free Maxwell (8A), full
   Maxwell with the physical Coulomb coupling (8C), or radiation (8B)?
4. Should optics (8D) be a Lane 8 follow-on or its own later lane?
