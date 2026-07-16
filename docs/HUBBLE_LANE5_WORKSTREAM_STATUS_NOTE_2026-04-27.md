# Lane 5 Workstream Status: Hubble-H0 Structural Lock And Two-Gate Closure Map

**Date:** 2026-04-27
**Type:** meta
**Scope:** source-side Lane 5 dependency synthesis; no audit disposition and
no numerical `H_0` closure
**Lane:** 5 — Hubble constant `H_0` derivation
**Workstream:** `hubble-h0-20260426`

---

## 0. Headline

Before this workstream, Lane 5 closure was framed as five sub-targets
(5A `Omega_m` closure, 5B `H_0` derivation, 5C tension stance,
5D `Sigma m_nu`, 5E inflation). After this workstream, Lane 5 closure
is framed as a sharp two-gate statement:

> **Lane 5 closure requires resolving BOTH route classes:**
>
> - **(C1) absolute-scale route**, gated by the coupled active-block response,
>   physical channel/Widom, gravitational boundary/action, and action-unit
>   metrology obligations, AND
> - **one of {(C2) cosmic-history-ratio retirement,
>   (C3) direct cosmic-`L` derivation}**, with the explicit `(C2)` route
>   gated by the right-sensitive 2-real `Z_3` doublet-block
>   point-selection law on `dW_e^H = Schur_{E_e}(D_-)`.
>
> No fourth class exists. No single class is sufficient.

The source-side structural lock has an explicit operational falsifier (no
late-time `H_0` running under its supplied cosmology conditions). The 5A
`Omega_m` and 5B `H_0` sub-lanes remain gate-isolated; the `(C1)` side is a
coupled packet rather than a single microscopic selection law.

## 1. Foundation and cited model inputs

The current foundation contains exactly the Lattice, Qubit, Admissibility,
and Record axioms. The remaining rows are cited model inputs or derived source
surfaces; they are not additional axioms or approved primitives. No cycle
imports an observed quantitative value.

| Identity | Authority |
|---|---|
| Lattice, Qubit, Admissibility, and Record axioms | [MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md) |
| historical `Cl(3)`/`Z^3` substrate model | supplied model context, not a separate axiom or primitive |
| `Lambda = 3 / R_Lambda^2` (spectral-gap) | `COSMOLOGICAL_CONSTANT_SPECTRAL_GAP_IDENTITY_THEOREM_NOTE.md` |
| `w_Lambda = -1` (DE EOS) | `DARK_ENERGY_EOS_RETAINED_COROLLARY_THEOREM_NOTE.md` |
| `H_inf = c / R_Lambda` | `COSMOLOGY_SCALE_IDENTIFICATION_AND_REDUCTION_NOTE.md` |
| `Omega_Lambda = (H_inf/H_0)^2` | `OMEGA_LAMBDA_MATTER_BRIDGE_THEOREM_NOTE_2026-04-22.md` |
| FRW kinematic forward reduction | `COSMOLOGY_FRW_KINEMATIC_REDUCTION_THEOREM_NOTE_2026-04-24.md` |
| Single-ratio inverse reconstruction | `COSMOLOGY_SINGLE_RATIO_INVERSE_RECONSTRUCTION_THEOREM_NOTE_2026-04-25.md` |
| `R_base = 31/9` (DM/baryon group-theory base) | `R_BASE_GROUP_THEORY_DERIVATION_THEOREM_NOTE_2026-04-24.md` |
| Matter-radiation equality structural identity | `MATTER_RADIATION_EQUALITY_STRUCTURAL_IDENTITY_THEOREM_NOTE_2026-04-24.md` |
| `N_eff = 3 + 0.046 = 3.046` | `N_EFF_FROM_THREE_GENERATIONS_THEOREM_NOTE_2026-04-24.md` |
| `Lambda` spectral tower bridge | `GRAVITY_COSMOLOGY_TOWER_LAMBDA_SPECTRAL_BRIDGE_THEOREM_NOTE_2026-04-25.md` |
| Conditional Planck packet (`a/l_P = 1` on supplied source-unit, gravitational-carrier, and action-unit surface) | `PLANCK_SCALE_CONDITIONAL_COMPLETION_NOTE_2026-04-24.md` and 2026-04-25 packet |

## 2. Five-cycle output map

### Cycle 1 — Hubble Tension Structural Lock theorem

**Artifact:**
`docs/HUBBLE_TENSION_STRUCTURAL_LOCK_THEOREM_NOTE_2026-04-26.md` +
`scripts/frontier_hubble_tension_structural_lock.py` (5/5 PASS) +
`logs/2026-04-26-hubble-tension-structural-lock.txt`.

**Claim:** on the retained surface (`w_Lambda = -1`, flat FRW with
non-interacting matter/radiation/`Lambda`), the late-time Hubble
parameter satisfies the exact identity

```text
H(a)^2 / H_0^2 = Omega_r,0 a^-4 + Omega_m,0 a^-3 + Omega_Lambda,0,
```

so the implied `H_0` is a single scalar across the entire late-time
epoch. **Operational falsifier:** any z-dependent late-time `H_0`
running falsifies retained `w_Lambda = -1`.

**Tension stance:** late-time-only resolutions of any genuine Hubble
tension are forbidden on the retained surface; resolution must come
from pre-recombination physics or measurement systematics.

**Lane 5 contribution:** Phase 1 (5C) landed on `main` as a manuscript-facing
structural commitment pending audit ratification.

### Cycle 2 — Cosmology Open-Number Reduction theorem

**Artifact:**
`docs/COSMOLOGY_OPEN_NUMBER_REDUCTION_THEOREM_NOTE_2026-04-26.md` +
`scripts/frontier_cosmology_open_number_reduction.py` (5/5 PASS) +
`logs/2026-04-26-cosmology-open-number-reduction.txt`.

**Claim:** the late-time bounded cosmology variable set

```text
S = { H_0, H_inf, R_Lambda, Omega_Lambda, Omega_m,
      q_0, z_*, z_mLambda, H(a) }
```

has **exactly 2 structural degrees of freedom at fixed admitted `R`**: the
pair `(H_0, L)` where
`L := Omega_Lambda = (H_inf/H_0)^2`. Every variable in `S` is an exact
closed-form function of `(H_0, L)` with `R = Omega_r,0` admitted.

**Program-bounding statement:** no fourth class of derivation retires
the late-time bounded cosmology surface beyond {derive `L`, derive
`H_0`, derive `R_Lambda` + one of `(L, H_0)`}.

**Lane 5 contribution:** parameter-count statement that exhausts the
late-time observables. Establishes the structural framing on which
Cycle 3 builds.

### Cycle 3 — Lane 5 Cosmic-History-Ratio Necessity No-Go

**Artifact:**
`docs/HUBBLE_LANE5_COSMIC_HISTORY_RATIO_NECESSITY_NO_GO_NOTE_2026-04-26.md`
(structural case-analysis on the cited cosmology/model surface).

**Claim:** on the four-axiom foundation plus the cited model surface, the
dimensional `(H_0, H_inf, R_Lambda)` are non-numerical (absolute-time
necessity), and the dimensionless
`L = (H_inf/H_0)^2` is non-derivable (cosmic-history-ratio necessity).
Lane 5 closure therefore requires premises from two classes:

- **(C1) absolute-scale route packet** [REQUIRED];
- **(C2) cosmic-history-ratio retirement** OR **(C3) direct cosmic-`L`
  derivation** [one of the two `L`-pathways].

No fourth class exists. No single class is sufficient.

**Lane 5 contribution:** formal closure-pathway taxonomy for Lane 5.
Sets the frame on which Cycles 4 and 5 isolate the gates.

### Cycle 4 — Lane 5 eta Retirement Gate Audit (`(C2)` gate)

**Artifact:**
`docs/HUBBLE_LANE5_ETA_RETIREMENT_GATE_AUDIT_NOTE_2026-04-26.md`
(no runner — review of retained DM-lane material).

**Gate identified:** the right-sensitive 2-real `Z_3` doublet-block
point-selection law on `dW_e^H = Schur_{E_e}(D_-)`.

**Live routes audited:** 1-flavor exact transport
(`eta/eta_obs = 0.1888`, closed but undershoots by `~5.3`); reduced-
surface PMNS support (`eta/eta_obs = 1.0` exact constructive point).
The PMNS branch's residual selector reduces exactly to the odd slot
`A13`, equivalently `sign(sin(delta))`, in the moving `Z_3` doublet
block.

**Closed routes the gate-resolving selector must avoid:** universal-
Yukawa, polar-aligned-core, two-Higgs slots, `Z_3` circulant
mass-basis, asymptotic-source / local-selector-family,
Wilson-direct-descendant constructive-transport, strong-CP /
`gamma`-transfer.

**Lane 5 contribution:** sub-lane 5A explicitly gate-isolated. Closing
the gate retires `eta` from the bounded cascade and supplies `(C2)`.

### Cycle 5 — Lane 5 Planck `(C1)` Gate Audit

**Artifact:**
`docs/HUBBLE_LANE5_PLANCK_C1_GATE_AUDIT_NOTE_2026-04-26.md`
with source-packet runner
`scripts/frontier_hubble_lane5_planck_c1_gate_source_packet.py`.

**Gate identified:** a coupled residual packet, not one premise:

- (G1a) a compatible active-block `Cl_4(C)`/CAR response on `P_A H_cell`;
- (G1b) separate normal/self-dual-tangent channel, tangent-symbol, and
  Widom applicability/normalization conditions;
- the separately supplied gravitational boundary/action identification for
  the source-unit/Wald leg; and
- (G2) action-unit metrology beyond the dimensionless phase convention.

No single conditional unifies the three Planck-lane targets. Abstract
Clifford/CAR algebra supplies neither the physical channel law nor the
gravitational/Wald identification, and it does not break the absolute
action-unit rescaling freedom.

**Closed shortcut routes:** finite-automorphism-only response,
carrier-only parent-source scalar, simple-fiber Widom carrier,
multipocket selector axioms, primitive-edge-entropy direct relabeling,
algebraic finite-Schmidt-spectrum (Baker's theorem).

**Lane 5 contribution:** sub-lane 5B (absolute scale) has its coupled gate
isolated. The current packet retires no numerical input; resolving all listed
obligations would supply a future `(C1)` route premise.

## 3. Symmetric two-gate map

The two Lane 5 closure gates are remarkably symmetric:

| | `(C2)` gate (Cycle 4) | `(C1)` gate (Cycle 5) |
|---|---|---|
| **Gate object** | right-sensitive 2-real `Z_3` doublet-block point-selection law | coupled active-block response, channel/Widom, gravitational-carrier, and action-metrology packet |
| **Algebraic domain** | `dW_e^H = Schur_{E_e}(D_-)` (charged-lepton response) | `P_A H_cell ⊆ H_cell` (rank-four primitive boundary block) |
| **What it pins** | `(delta, q_+)` in the moving `Z_3` doublet block | no single object; all independent `(C1)` obligations must be resolved |
| **Resulting closure** | conditional `(C2)` route premise | future `(C1)` route premise only after the whole coupled packet is resolved |
| **Sub-lane** | 5A (cosmic-history-ratio retirement) | 5B (absolute-scale anchor) |
| **Adjacent live route** | reduced-surface PMNS support, `eta/eta_obs = 1.0` exact constructive point | separate conditional Clifford response and source-unit/gravitational-carrier/action-metrology supports; no single bridge closes `(C1)` |
| **Closed shortcuts** | universal-Yukawa, two-Higgs slots, `Z_3` circulant, polar-aligned-core, asymptotic-source / local-selector-family, Wilson-direct-descendant, strong-CP/`gamma`-transfer | finite-automorphism-only response, carrier-only parent-source scalar, simple-fiber Widom, multipocket selector, primitive-edge-entropy, algebraic finite-Schmidt-spectrum |

The `(C2)` gate is one microscopic point-selection law on a primitive
algebraic block. The `(C1)` gate is instead the coupled packet of response,
channel/Widom, gravitational-carrier, and action-metrology obligations listed
above; it is not one edge-selection law. Each route records only its scoped
shortcut exclusions, and both route classes remain necessary (per Cycle 3)
for Lane 5 closure.

## 4. What each cycle did and did not retire

| Cycle | Imports retired | Imports clarified | Imports left open |
|---|---|---|---|
| 1 | none | `H_0` (locks structural form, doesn't retire numerical value) | `H_0`, `T_CMB`, `eta`, `alpha_GUT`, `R_Lambda` |
| 2 | none | reduces `S` to `(H_0, L)` count | same |
| 3 | none | classifies closure pathways into `{(C1), (C2), (C3)}` | same |
| 4 | none | identifies `(C2)` gate | same |
| 5 | none | identifies `(C1)` gate | same |

**Net:** no numerical input retired. The workstream's contribution is
**structural** — the closure pathway is now a sharp two-gate statement
rather than a five-target list.

## 5. Outstanding open premises

To close Lane 5, the `(C1)` route and one of the `(C2)`/`(C3)` routes must
each be derived or separately supplied. The current four axioms do not resolve
them.

### (C1) Coupled absolute-scale route packet

This route requires all of the following, with their premise provenance kept
separate: a compatible active-block Clifford/CAR response; the physical
normal/self-dual-tangent channel law, tangent symbol, and Widom conditions;
the gravitational boundary/action identification; and action-unit metrology
that breaks the `(S,kappa)` rescaling degeneracy.

### (C2) The right-sensitive `Z_3` doublet-block point-selection law

A derivation from the four-axiom foundation plus explicitly cited PMNS/CP
model conditions of a
microscopic selector law on the moving `Z_3` doublet block that fixes
`(delta, q_+)` and is right-sensitive (resolves
`sign(sin(delta))`).

### Alternative `(C3)` route (not yet opened in this workstream)

A direct framework-internal structural derivation of `L` itself,
independent of the cosmic-history matter cascade. No active route
exists; the only fresh closure of any kind would have to come from a
vacuum/topology argument outside the existing DM/leptogenesis lane.

### Out of scope

- `T_CMB` numerical value — explicitly deferred (5E inflation
  territory).
- `alpha_GUT` — separate gauge-coupling unification lane.
- `Sigma m_nu` cosmological integration — Lane 4 owns; couples to
  Lane 5 only at integration step.

## 6. Manuscript-surface implications

The structural lock theorem (Cycle 1) is the only Lane 5 cycle that
adds a manuscript-surface prediction with explicit operational
falsifier. The recommended manuscript weave is:

- `docs/publication/ci3_z3/INPUTS_AND_QUALIFIERS_NOTE.md` §2
  (cosmology windows): cite the structural lock alongside the matter-
  bridge identity; update phrasing to reflect late-time `H_0(z)`
  running is forbidden on the retained surface.
- `docs/publication/ci3_z3/WHAT_THIS_PAPER_DOES_NOT_CLAIM.md`: revise
  the Hubble-tension framing — the framework's commitment to ΛCDM at
  late times rules out late-time-only tension resolutions.
- `docs/lanes/open_science/05_HUBBLE_CONSTANT_DERIVATION_OPEN_LANE_2026-04-26.md`
  §4 scaffolding list: add the new Lane 5 artifacts. Update §5 Phase 1
  (5C) to "landed on `main` pending audit"; reframe Phases 2-5 as the
  two-gate `(C1)`/`(C2)` work.

Cycles 2-5 are infrastructure for the reviewer/integration pipeline.
They sharpen what Lane 5 closure requires; they do not themselves move
the manuscript-facing prediction surface.

## 7. Cross-references

### Workstream artifacts

- Cycle 1: `HUBBLE_TENSION_STRUCTURAL_LOCK_THEOREM_NOTE_2026-04-26.md`
- Cycle 2: `COSMOLOGY_OPEN_NUMBER_REDUCTION_THEOREM_NOTE_2026-04-26.md`
- Cycle 3: `HUBBLE_LANE5_COSMIC_HISTORY_RATIO_NECESSITY_NO_GO_NOTE_2026-04-26.md`
- Cycle 4: `HUBBLE_LANE5_ETA_RETIREMENT_GATE_AUDIT_NOTE_2026-04-26.md`
- Cycle 5: `HUBBLE_LANE5_PLANCK_C1_GATE_AUDIT_NOTE_2026-04-26.md`

### Adjacent open lanes

- DM/leptogenesis (`(C2)` gate-resolving selector).
- Planck-scale (`(C1)` gate-resolving derivation).

## 8. Boundary

This is a consolidation/status note, not a new theorem. It does not
retire any input, does not promote any cycle's claim to a new tier,
and does not introduce new numerical content. It synthesizes the
five-cycle workstream output into a single read-first surface for the
post-workstream review-and-integration pipeline.

A runner is not authored: the consolidation is editorial / navigational
content over the existing Hubble-H0 artifacts.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [cosmology_open_number_reduction_theorem_note_2026-04-26](COSMOLOGY_OPEN_NUMBER_REDUCTION_THEOREM_NOTE_2026-04-26.md)
- [hubble_lane5_cosmic_history_ratio_necessity_no_go_note_2026-04-26](HUBBLE_LANE5_COSMIC_HISTORY_RATIO_NECESSITY_NO_GO_NOTE_2026-04-26.md)
- [hubble_lane5_eta_retirement_gate_audit_note_2026-04-26](HUBBLE_LANE5_ETA_RETIREMENT_GATE_AUDIT_NOTE_2026-04-26.md)
- [hubble_lane5_planck_c1_gate_audit_note_2026-04-26](HUBBLE_LANE5_PLANCK_C1_GATE_AUDIT_NOTE_2026-04-26.md)
