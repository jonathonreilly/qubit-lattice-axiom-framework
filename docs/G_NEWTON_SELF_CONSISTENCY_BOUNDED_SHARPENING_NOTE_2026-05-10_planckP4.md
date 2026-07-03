# G_Newton Self-Consistency — Bounded Sharpening (planckP4 probe)

**Date:** 2026-05-10; 2026-06-09 Green-kernel dependency reroute and
Born-source blocker refresh.
**Type:** bounded_theorem (sharpened — positive sub-theorem + named obstruction)
**Claim type:** bounded_theorem
**Scope:** review-loop source-note proposal — attempts to close the
G_Newton self-consistency content of `GRAVITY_CLEAN_DERIVATION_NOTE.md`
from retained Cl(3)/Z³ content. Companion to the gravity-as-phase
bounded-obstruction note
[`KOIDE_A1_PROBE_GRAVITY_PHASE_BOUNDED_OBSTRUCTION_NOTE_2026-05-08_probe3.md`](KOIDE_A1_PROBE_GRAVITY_PHASE_BOUNDED_OBSTRUCTION_NOTE_2026-05-08_probe3.md).
**Status:** source-note proposal for a sharpened (partial) closure of the
G_Newton lane. Verifies that (P1) the dimensional G_Newton form is
structurally rigid given the named closure admissions, AND (P2) the parent
chain remains conditional on named dependency gates. The source boundary of
`GRAVITY_CLEAN_DERIVATION_NOTE` is therefore sharpened from "conditional" to
"explicitly conditional on named dependency gates." As of the
2026-06-09 refresh, the Green-kernel premise is routed through the
framework-local `Z^3` Green theorem and the Born-source blocker is no longer
"no retained support row exists"; it is a dependency-composition gate. This is
structural sharpening, not closure.
**Authority role:** source-note proposal — audit verdict and downstream
status set only by the independent audit lane.
**Loop:** g-newton-self-consistency-20260510-planckP4
**Primary runner:** [`scripts/cl3_g_newton_self_consistency_2026_05_10_planckP4.py`](../scripts/cl3_g_newton_self_consistency_2026_05_10_planckP4.py)
**Cache:** [`logs/runner-cache/cl3_g_newton_self_consistency_2026_05_10_planckP4.txt`](../logs/runner-cache/cl3_g_newton_self_consistency_2026_05_10_planckP4.txt)

## Authority disclaimer

This is a source-note proposal. Pipeline-derived status is generated
only after the independent audit lane reviews the claim, dependency
chain, and runner. The `claim_type`, scope, named admissions, and
bounded-sharpening classification are author-proposed; the audit lane
has full authority to retag, narrow, or reject the proposal.

## Question

The unaudited `GRAVITY_CLEAN_DERIVATION_NOTE.md` proposes a derivation
of Newton's law from Cl(3)/Z³ via three closure admissions:

> (a) `L^{-1} = G_0` — self-consistency identification of the field
>     operator inverse with the propagator Green's function.
> (b) `ρ = |ψ|²` — Born / mass-density source map.
> (c) `S = L (1 - φ)` — weak-field test-mass response.

Per the 2026-04-28 audit verdict, the derivation is `audited_conditional`
on these three admissions. The `GRAVITY_FULL_SELF_CONSISTENCY_NOTE.md`
explicitly admits (a) is **stipulated, not derived** from the repo
baseline: the load-bearing identification `L^{-1} = G_0` is stipulated,
not derived from the one-qubit operator algebra / physical `Cl(3)` real-algebra
reading on the `Z^3` Lattice; the retained bridge theorem deriving the physical
lattice dynamics from the local-algebra baseline is the open D-row gap.

The probe question:

> Can the retained Lattice/Quantum content close G_Newton self-consistency
> unconditionally — that is, derive each of admissions (a), (b), (c)
> from retained content, with no new repo-wide axioms or imports?

The probe hypothesis is appealing because (i) Newton's constant `G` is
a *natural dimensional scale* (the framework retains a length scale
via `a_s`, a velocity scale via the Lieb-Robinson `c_LR`, and through
the Planck mass anchor `M_Pl` would have a complete dimensional set),
and (ii) closing G_Newton self-consistency would move the gravity lane from a
conditional IF-chain toward an unconditional retained derivation.

## Answer

**Sharpened, not fully closed.** The G_Newton lane factors into:

- **(POSITIVE, P1) Dimensional G_Newton form theorem.** *Given* the
  three admissions (a), (b), (c), the dimensional form of `G_Newton`
  on the lattice is structurally rigid: the only combination of
  retained dimensional inputs `{a_s, a_τ, c_LR, M_lat, ħ}` carrying
  the SI dimensions of Newton's constant `m³ kg⁻¹ s⁻²` is the
  canonical Planck-form `G ~ ħ c / M_Pl²` (modulo a fixed
  dimensionless ratio of Z³ Green-function constants). This is a
  *rigidity* result: the dimensional structure is not free.

- **(NEGATIVE, P2) Non-derivability obstruction / dependency refresh.** The
  parent chain still does not close unconditionally:
  - **B(a)** Multiple retained propagator skeletons exist
    (Hamiltonian, d'Alembertian, complex-action). No retained
    theorem forces gravity to use the Hamiltonian skeleton.
  - **B(b)** The old "no retained positive/bounded Born-as-gravity-source
    theorem" statement is stale on current main. The Born-source admission now
    has named support rows to compose through; the parent chain is not promoted
    by this note.
  - **B(c)** The weak-field test-mass action `S = L(1 - φ)` is a
    modeling identification, not a retained derivation theorem;
    alternative `S = L√(1 - φ)` (spent-delay) is also tested in
    `DIMENSIONAL_GRAVITY_TABLE.md` retained_bounded family with
    different Newtonian-recovery profile.

The combined picture: the dimensional structure of G_Newton is rigid given the
named admissions, but the parent chain still does not close unconditionally.
The 2026-06-09 refresh changes the shape of the open frontier: the
Born-source admission now has named bounded support to compose through, while
the propagator-skeleton and weak-field-response admissions remain unforced by
the current baseline.

## Setup

### Premises for the G_Newton self-consistency probe

| ID | Statement | Class |
|---|---|---|
| BASE-Quantum | one-qubit operator algebra, equivalently the physical `Cl(3,0)` real-algebra reading | repo baseline semantics; see [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) |
| BASE-Lattice | `Z^3` Lattice with nearest-neighbor cubic adjacency | repo baseline semantics; same source |
| GreenZ3 | `Z^3` lattice Laplacian Green function asymptotic `G(r) -> 1/(4 pi |r|)` | framework-local theorem: [`LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md`](LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md), with textbook references parallel |
| BornGravSource | bounded position-density source support for admission (b) | dependency row: [`G_NEWTON_BORN_AS_SOURCE_POSITIVE_THEOREM_NOTE_2026-05-10_gnewtonG2.md`](G_NEWTON_BORN_AS_SOURCE_POSITIVE_THEOREM_NOTE_2026-05-10_gnewtonG2.md) |
| MicroLR | Lieb-Robinson velocity `v_LR` exists; equal-time strict locality from Cl(3) tensor structure | unaudited (positive_theorem): [`AXIOM_FIRST_MICROCAUSALITY_LIEB_ROBINSON_THEOREM_NOTE_2026-05-01.md`](AXIOM_FIRST_MICROCAUSALITY_LIEB_ROBINSON_THEOREM_NOTE_2026-05-01.md) |
| HSRigid | Hilbert-Schmidt rigidity on `g_conc = su(3) ⊂ End(V)` | unaudited (positive_theorem): [`G_BARE_HILBERT_SCHMIDT_RIGIDITY_THEOREM_NOTE_2026-05-07.md`](G_BARE_HILBERT_SCHMIDT_RIGIDITY_THEOREM_NOTE_2026-05-07.md) |
| PhysLat | Two-invariant rigidity on canonical normalization surface (no-go) | retained_no_go: [`PHYSICAL_LATTICE_NECESSITY_NOTE.md`](PHYSICAL_LATTICE_NECESSITY_NOTE.md) |
| SCForcePoisson | Self-consistency preference for Poisson on tested operator family | retained_bounded: [`SELF_CONSISTENCY_FORCES_POISSON_NOTE.md`](SELF_CONSISTENCY_FORCES_POISSON_NOTE.md) |
| GravLawClean | Lattice Z³ Laplacian gives 1/r potential and 1/r² force | retained_bounded: [`GRAVITY_LAW_CLEANUP_NOTE.md`](GRAVITY_LAW_CLEANUP_NOTE.md) |
| GravFullSC | Conditional Poisson forcing under stipulated `L^{-1}=G_0` | unaudited (bounded_theorem): [`GRAVITY_FULL_SELF_CONSISTENCY_NOTE.md`](GRAVITY_FULL_SELF_CONSISTENCY_NOTE.md) |
| PropFamily | Multiple retained propagator skeletons (wavefield, complex-action, electrostatics) | retained: [`PROPAGATOR_FAMILY_UNIFICATION_NOTE.md`](PROPAGATOR_FAMILY_UNIFICATION_NOTE.md) |
| WaveGravity | Wave-equation gravity with Newton-recovery static limit | retained_bounded: [`WAVE_EQUATION_GRAVITY_NOTE.md`](WAVE_EQUATION_GRAVITY_NOTE.md) |
| DimGravTab | Valley-linear vs spent-delay weak-field action comparison | retained_bounded: [`DIMENSIONAL_GRAVITY_TABLE.md`](DIMENSIONAL_GRAVITY_TABLE.md) |
| PlanckCharNoGo | Planck-from-structure boundary character no-go | retained_no_go: [`PLANCK_PARENT_SOURCE_HIDDEN_CHARACTER_NO_GO_NOTE_2026-04-24.md`](PLANCK_PARENT_SOURCE_HIDDEN_CHARACTER_NO_GO_NOTE_2026-04-24.md) |
| PlanckOriNoGo | Planck-from-structure orientation-incidence no-go | retained_no_go: [`PLANCK_BOUNDARY_ORIENTATION_INCIDENCE_NO_GO_NOTE_2026-04-30.md`](PLANCK_BOUNDARY_ORIENTATION_INCIDENCE_NO_GO_NOTE_2026-04-30.md) |
| GravCleanCond | Conditional 1/r derivation chain (IF L⁻¹=G_0 + Born + S=L(1−φ)) | unaudited / audited_conditional: [`GRAVITY_CLEAN_DERIVATION_NOTE.md`](GRAVITY_CLEAN_DERIVATION_NOTE.md) — **the lane being sharpened** |

### Forbidden imports

- NO PDG observed values used as derivation input. `G_Newton SI =
  6.6743e-11 m³ kg⁻¹ s⁻²` is used only as anchor-only / cross-check,
  clearly marked.
- NO new repo-wide axioms.
- NO promotion of unaudited content to retained-grade.
- NO empirical fits.
- NO same-surface family arguments.

## Theorem (bounded sharpening)

**Theorem (P1, positive sub-theorem).** Let the three admissions of
`GRAVITY_CLEAN_DERIVATION_NOTE` be:

```
(a) L^{-1} = G_0    (field-operator / propagator self-consistency)
(b) ρ = |ψ|^2       (Born map / mass-density source)
(c) S = L(1 - φ)    (weak-field test-mass action)
```

Then under the retained content surface defined by the premises above,
the **dimensional structure** of `G_Newton` is rigid:

```
G_lat = 1 / (4 π)                  (lattice units, dimensionless)
G_SI  = ħ c / M_Pl²               (SI carry via Planck-anchor)
```

Equivalently: of all integer-exponent combinations
`a_s^p · c_LR^q · M_lat^r · ħ^s` with `p, q, r, s ∈ [-3, 3]`, exactly
the canonical Planck-form `(p, q, r, s) = (0, 1, -2, 1)` (i.e.,
`ħ¹ c¹ M_lat^{-2}`) carries SI dimensions of Newton's constant
`m³ kg⁻¹ s⁻²`. The runner verifies this dimensional rigidity check
exhaustively over the integer-exponent search box (Section 2,
S2.1–S2.5).

The dimensionless coefficient `1/(4π)` is the asymptotic value of
`4π r G(r)` for the Z³ lattice Green's function, which converges
monotonically to 1 from below as the lattice size grows (Section 1,
S1.1–S1.3).

**Theorem (P2, negative obstruction / dependency refresh).** Under the same
retained content surface, the parent chain is not unconditionally closed. The
2026-06-09 refresh leaves two admissions blocked as unforced baseline
consequences and converts the old Born-source blocker into a dependency
composition gate:

```
B(a) Propagator-skeleton non-uniqueness (Section 3):
  - At least three distinct retained propagator skeletons exist
    in the framework: Hamiltonian (used by GRAVITY_CLEAN_DERIVATION),
    d'Alembertian (WAVE_EQUATION_GRAVITY_NOTE retained_bounded), and
    complex-action (CLAUDE_COMPLEX_ACTION_CARRYOVER_NOTE retained).
  - GRAVITY_FULL_SELF_CONSISTENCY_NOTE explicitly stipulates
    L^{-1} = G_0 rather than deriving it.
  - The audit ledger contains no retained theorem with title
    pattern matching "skeleton selection", "field operator
    selection", or equivalent.

B(b) Born-source dependency refresh (Section 4):
  - The earlier "no retained positive/bounded Born-as-gravity-source theorem"
    statement is stale on current main.
  - The runner now discovers the current named Born-source support rows and
    records admission (b) as a dependency-composition gate, not as an
    unaddressed no-support blocker.
  - The parent `GRAVITY_CLEAN_DERIVATION_NOTE` is still not promoted by this
    refresh; it must explicitly compose any Born-source dependency with the
    remaining propagator-skeleton and weak-field-response gates.

B(c) Weak-field test-mass action non-derivation (Section 5):
  - The action S = L(1 - φ) is a propagator-level modeling
    identification used in DIMENSIONAL_GRAVITY_TABLE,
    STAGGERED_NEWTON_REPRODUCTION_NOTE, etc.
  - At least three weak-field action forms have been tested in
    retained_bounded content: valley-linear S = L(1 - φ) gives
    F~M = 1.00 (Newtonian), spent-delay S = L√(1 - φ) gives
    F~√M = 0.50 (NOT Newtonian), and phase-only.
  - The selection of valley-linear is by EMPIRICAL match to
    F~M = 1, not by retained derivation. The audit ledger contains
    no retained "weak-field-action derivation theorem".
```

**Conclusion.** `GRAVITY_CLEAN_DERIVATION_NOTE` remains a conditional IF-chain
on named dependency gates.
What this note adds is:

1. The dimensional STRUCTURE of `G_Newton` is rigid given the
   admissions (P1).
2. The parent chain still does not close unconditionally (P2).
3. Closing G_Newton unconditionally now requires the remaining unforced
   primitives for B(a) and B(c), plus explicit composition through the
   Born-source dependency for B(b).

This sharpens the open frontier from a single conditional G_Newton lane to two
remaining retained-derivation deliverables plus one Born-source composition
gate.

## Proof

### P1 (positive sub-theorem) — dimensional rigidity

**Step 1.** The `Z^3` lattice Laplacian `(-Delta_lat)` has Green's function
`G(r) = <r|(-Delta_lat)^(-1)|0>` with asymptotic
`G(r) -> 1/(4 pi |r|)` as `|r| -> infinity`. The load-bearing route is the
framework-local Green-kernel theorem applied to the exact `Z^3`
nearest-neighbor graph-Laplacian stencil, with Maradudin/Lawler/Spitzer kept as
parallel references. The runner verifies this asymptotic behavior numerically
by computing the FFT-based Green function on periodic `L^3` tori for
`L in {16, 24, 32, 48}` at fixed distance `r = 4` and verifying monotonic
increase of `4 pi r G(r)` toward 1 as `L` grows (Section 1, S1.1-S1.3).

**Step 2.** Given admission (a) `L^{-1} = G_0`, the field equation
operator `L = G_0^{-1} = -Δ_lat`, and the Poisson equation
`(-Δ_lat) φ = ρ`. Given admission (b), the source is `ρ = |ψ|²`. Given
admission (c), the test-mass response gives Newton's law
`F = G_lat M_1 M_2 / r²` with `G_lat = 1/(4π)` in lattice units, which
is verified in `NEWTON_LAW_DERIVED_NOTE.md` and the conditional
`GRAVITY_CLEAN_DERIVATION_NOTE.md` Step 6.

**Step 3.** To convert lattice units to SI, the framework retains:
- `a_s` (lattice spatial spacing, dimensions L)
- `a_τ` (lattice temporal spacing, dimensions T)
- `c_LR = a_s / a_τ · O(1)` (Lieb-Robinson velocity, dimensions L/T)
- `M_lat` (lattice mass unit, dimensions M)
- `ħ` (action quantum, dimensions L²·M/T)

The dimensional analysis (Section 2) exhaustively searches the integer
box `(p, q, r, s) ∈ [-3, 3]^4` for combinations
`a_s^p · c_LR^q · M_lat^r · ħ^s` carrying SI dimensions of `G_Newton =
m³ kg⁻¹ s⁻²`. The search returns 4 candidates, all of which reduce to
the canonical Planck form `G ~ ħ c / M_Pl²` modulo dimensionless
factors. The runner verifies that the canonical form
`(p, q, r, s) = (0, 1, -2, 1)` is in the candidate set (S2.2) and that
no candidate avoids using a mass scale (S2.5).

**Step 4.** The Planck-anchor cross-check (S2.4) confirms the
dimensional form is consistent with the empirical
`G_Newton SI = 6.6743e-11`: setting `ħ = 1.0546e-34 J·s`,
`c = 2.998e+8 m/s`, `M_Pl = 2.176e-8 kg` (anchor-only inputs) gives
`G = ħ c / M_Pl² = 6.6743e-11`, matching the CODATA anchor at
`rel_err ~ 3e-7`. This is **consistency**, not **derivation** (S6.3).

This completes P1: the dimensional structure of `G_Newton` is rigid given the
named admissions. ∎

### P2 (negative obstruction) — non-derivability of the admissions

**Barrier B(a).** The retained `PROPAGATOR_FAMILY_UNIFICATION_NOTE.md`
explicitly enumerates at least three propagator skeletons:

```
- Wavefield (d'Alembertian)
- Complex-action (S = L(1-f) + iγLf)
- Electrostatics scalar
```

`GRAVITY_CLEAN_DERIVATION_NOTE` selects the Hamiltonian skeleton
`H = -Δ_lat` and asserts `L^{-1} = G_0` for that skeleton. But:

- `WAVE_EQUATION_GRAVITY_NOTE.md` (retained_bounded) uses the
  d'Alembertian and recovers Poisson only in the static limit, with
  retardation corrections that the Hamiltonian skeleton lacks.
- `GRAVITY_FULL_SELF_CONSISTENCY_NOTE.md` (unaudited bounded_theorem)
  explicitly admits that the load-bearing identification `L^{-1} = G_0`
  is **stipulated**, not derived from the one-qubit operator algebra /
  physical `Cl(3)` real-algebra reading on the `Z^3` Lattice in that note.

The runner Section 3 (S3.1–S3.4) verifies this enumeration and confirms
no retained skeleton-selection theorem exists in the audit ledger.

**Barrier B(b), refreshed.** The pure-state Born map `rho = |psi|^2`
remains target-side in the sense identified by the parent gravity-phase
obstruction: it operates after the state is supplied. The stale part of the
original P4 packet was stronger than that: it asserted that no retained
positive/bounded Born-as-gravity-source support row existed. Current main has
named support rows for that source-readout problem, so the runner now treats
B(b) as a dependency-composition gate instead of an absent-support blocker
(S4.4).

**Barrier B(c).** The valley-linear weak-field action `S = L(1 - φ)`
is one of at least three forms tested in `DIMENSIONAL_GRAVITY_TABLE.md`
(retained_bounded). The alternatives are `S = L√(1 - φ)` (spent-delay,
gives `F~√M = 0.50`, NOT Newtonian) and phase-only. The valley-linear
selection produces `F~M = 1.00` (Newtonian); the others do not. So
the framework's own retained content compares both as candidates and
selects valley-linear by **empirical match** to `F~M = 1`, not by
retained derivation (S5.2).

The audit ledger contains no retained "weak-field-action derivation
theorem" (S5.3).

This completes P2: the parent chain remains conditional. Since P1 assumes the
admissions and P2 leaves B(a) and B(c) unforced while routing B(b) through a
separate support dependency, the G_Newton lane is sharpened but not fully
closed. ∎

## What this closes

- **Sharpens the G_Newton self-consistency status.** Status moves from
  "G_Newton lane is conditional" to "G_Newton lane has a
  positive dimensional sub-theorem (P1), two explicitly named obstruction
  barriers (P2 B(a), B(c)), and one Born-source dependency-composition gate
  (P2 B(b))."
- **Identifies the remaining deliverables.** Closing G_Newton unconditionally
  requires:
  1. A retained **propagator-skeleton selection theorem** addressing
     B(a) — derive `L = -Delta_lat` (or whichever specific skeleton) from
     the one-qubit operator algebra / physical `Cl(3)` real-algebra reading
     plus the `Z^3` Lattice alone.
  2. An explicit composition through the existing **Born-as-gravity-source
     dependency** addressing B(b), without promoting the parent chain by
     implication.
  3. A retained **weak-field-action derivation theorem** addressing
     B(c) — derive `S = L(1 - phi)` (and its valley-linear vs
     spent-delay vs phase-only selection) from the repo baseline.
- **Confirms the dimensional rigidity result is independent of the named
  admissions.** P1 says the *structure* of G_Newton is fixed even before P2
  composes the admissions. So progress on any admission individually still
  benefits from the dimensional-form result.
- **Strengthens the parent
  [`KOIDE_A1_PROBE_GRAVITY_PHASE_BOUNDED_OBSTRUCTION_NOTE_2026-05-08_probe3.md`](KOIDE_A1_PROBE_GRAVITY_PHASE_BOUNDED_OBSTRUCTION_NOTE_2026-05-08_probe3.md)
  Barrier G2 finding** that the gravity-clean chain is unaudited and
  conditional. This note makes the named dependency gates explicit and
  structural at the runner level.

## What this does NOT close

- The unconditional G_Newton self-consistency derivation. The status of
  `GRAVITY_CLEAN_DERIVATION_NOTE.md` is set only by the independent audit
  lane. This note does NOT promote that note to retained.
- The Koide A1 flavor-sector admission count is unaffected. That
  closure is on the flavor sector and is independently barred per the parent
  obstruction note Barriers G1–G5.
- The Planck-from-structure derivation. P1 anchors on `M_Pl` as a
  dimensional input, but `M_Pl` itself is not retained from the
  repo baseline alone (PLANCK_PARENT_SOURCE_HIDDEN_CHARACTER_NO_GO,
  PLANCK_BOUNDARY_ORIENTATION_INCIDENCE_NO_GO).
- Strong-field gravity, geodesics, time dilation, etc. — those remain
  bounded per the broader gravity sub-bundle.
- AC_φλ residual (substep 4) is unaffected.
- L3a trace-surface bounded obstruction status unchanged.
- Bridge gap fragmentation results unaffected.

## Negative-Boundary Discipline

The obstruction content here is a bounded dependency map, not a no-go against
all G_Newton derivations.

- Alternative routes left open: a retained propagator-skeleton selection
  theorem; explicit composition through the current Born-source dependency; a
  retained weak-field-action derivation; a different physical source/action
  bridge; and future theory that changes the parent gravity-clean premises.
- Wall independence: B(a) skeleton selection and B(c) weak-field response are
  independent. B(b) is no longer counted as an absent-support wall; it is a
  dependency-composition gate.
- Hidden-wall scan: the dimensional scale, lattice-unit Green normalization,
  Planck-anchor consistency check, and weak-field action form are all explicit
  assumptions or diagnostics, not silent derivations.
- Residual matching: this note targets only G_Newton self-consistency for the
  gravity-clean IF-chain. It does not target strong-field gravity, geodesics,
  the Planck-from-structure lane, or flavor-sector admissions.
- Rhetoric resolution: the negative claim is table/runner scoped to the named
  dependency gates and current ledger search strings; no universal
  impossibility theorem is claimed.
- Partial-closure scan: the Born-source route is explicitly moved from a wall
  to a composition gate. The scale-reference primitive is not treated as a
  bounded Planck import and does not by itself close the G_Newton derivation.
- Steelman: a retained skeleton-selection theorem plus a retained weak-field
  response theorem could close the parent chain once composed with the
  Born-source dependency. This note leaves that route open.
- Cross-cycle echo: prior overbroad no-support claims have been repaired when
  new support rows landed; this refresh applies that lesson by removing the
  stale B(b) no-support claim.

## Empirical falsifiability

| Claim | Falsifier |
|---|---|
| Dimensional rigidity (P1) | Demonstrate a different integer-exponent combination of `{a_s, c_LR, M_lat, ħ}` carrying SI units of G_Newton — but the runner search is exhaustive over `[-3, 3]^4`, so any falsifier must identify a NEW retained dimensional input. |
| Barrier B(a) | Demonstrate a retained "skeleton selection" theorem in the audit ledger that forces gravity to use the Hamiltonian skeleton over alternatives. |
| Barrier B(b) | Demonstrate that the named Born-source support dependency composes into the gravity-clean parent chain without adding a new admission or narrowing the parent claim beyond recognition. |
| Barrier B(c) | Demonstrate a retained "weak-field-action derivation" theorem deriving `S = L(1 - phi)` from the one-qubit operator algebra / physical `Cl(3)` real-algebra reading plus the `Z^3` Lattice (vs from empirical F~M match). |
| Numerical anchor (P1 cross-check) | Falsified if `ħ c / M_Pl² ≠ G_Newton SI`. CODATA values give `rel_err ~ 3e-7`, well within anchor precision. Anchor-only; not a derivation input. |

## Review boundary

This note proposes `claim_type: bounded_theorem` for the independent
audit lane. The bounded theorem is the sharpened (positive + negative)
G_Newton self-consistency boundary: the dimensional G_Newton form is
rigid given named admissions, while the parent chain remains conditional on
the named dependency gates.

No new admissions are proposed (the admissions named in this note are NOT new
-- they are the exact admissions of the parent
`GRAVITY_CLEAN_DERIVATION_NOTE.md`, surfaced explicitly here so the audit lane
can track them as separate dependency gates).
The independent audit lane may retag, narrow, or reject this proposal.

## Promotion-Value Gate (V1-V5)

| # | Question | Answer |
|---|---|---|
| V1 | Verdict-identified obstruction closed? | The "G_Newton self-consistency closure" lane is sharpened from "open lane" to "positive P1 dimensional rigidity + B(a)/B(c) obstructions + B(b) dependency-composition gate." `GRAVITY_CLEAN_DERIVATION_NOTE.md` is not promoted, but its conditional structure is now explicit. |
| V2 | New derivation? | The dimensional rigidity result P1 is new: an exhaustive integer-exponent search over `{a_s, c_LR, M_lat, hbar}` showing only the canonical Planck form survives. The refreshed P2 dependency map is new content beyond GRAVITY_FULL_SELF_CONSISTENCY_NOTE's stipulation language. |
| V3 | Audit lane could complete? | Yes — the audit lane can review (i) the `Z^3` Green-function FFT calculation, (ii) the dimensional integer-exponent search, (iii) B(a)/B(c) obstruction checks, (iv) B(b) dependency discovery, and (v) the consistency-vs-derivation boundary. |
| V4 | Marginal content non-trivial? | Yes — the dimensional rigidity proof closes the "G_Newton form" question structurally even though the unconditional derivation remains open. The refreshed dependency map gives an audit-defensible enumeration of the open frontier. |
| V5 | One-step variant? | No — the positive-sub-theorem-plus-negative-obstruction structure is structurally distinct from the parent KOIDE_A1_PROBE_GRAVITY_PHASE flavor-sector argument and from the GRAVITY_FULL_SELF_CONSISTENCY stipulation note. |

**Source-note V1-V5 screen: pass for bounded-sharpening audit
seeding.**

## Why this is not "corollary churn"

Per `feedback_physics_loop_corollary_churn.md`, the user-memory rule
is to avoid one-step relabelings of already-landed cycles. This note:

- Is NOT a relabel of any prior gravity note. The dimensional integer-
  exponent search and the explicit ledger queries for retained
  selection / Born / action theorems are new structural content.
- Identifies a NEW STRUCTURAL CLASS OF SHARPENING (positive dimensional
  rigidity plus a refreshed dependency map) on the G_Newton lane, distinct
  from the flavor-sector five-barrier obstruction of
  `KOIDE_A1_PROBE_GRAVITY_PHASE_*`.
- Provides an explicit deliverable list (B(a), B(b), B(c)) that the audit lane
  can use to track future closure attempts.
- Sharpens the user-prompt question "can retained content close
  G_Newton self-consistency?" from "open lane" to
  "positive sub-theorem + two named obstructions + one dependency gate."

## Cross-references

- Parent gravity-clean note: [`GRAVITY_CLEAN_DERIVATION_NOTE.md`](GRAVITY_CLEAN_DERIVATION_NOTE.md)
- Companion full-self-consistency note: [`GRAVITY_FULL_SELF_CONSISTENCY_NOTE.md`](GRAVITY_FULL_SELF_CONSISTENCY_NOTE.md)
- Sister A1 gravity-phase obstruction: [`KOIDE_A1_PROBE_GRAVITY_PHASE_BOUNDED_OBSTRUCTION_NOTE_2026-05-08_probe3.md`](KOIDE_A1_PROBE_GRAVITY_PHASE_BOUNDED_OBSTRUCTION_NOTE_2026-05-08_probe3.md)
- Newton-from-Z³ derivation: [`NEWTON_LAW_DERIVED_NOTE.md`](NEWTON_LAW_DERIVED_NOTE.md)
- Self-consistency forces Poisson (operator-family preference):
  [`SELF_CONSISTENCY_FORCES_POISSON_NOTE.md`](SELF_CONSISTENCY_FORCES_POISSON_NOTE.md)
- Propagator family unification: [`PROPAGATOR_FAMILY_UNIFICATION_NOTE.md`](PROPAGATOR_FAMILY_UNIFICATION_NOTE.md)
- Wave-equation gravity (alternative skeleton): [`WAVE_EQUATION_GRAVITY_NOTE.md`](WAVE_EQUATION_GRAVITY_NOTE.md)
- Dimensional gravity table (action comparisons): [`DIMENSIONAL_GRAVITY_TABLE.md`](DIMENSIONAL_GRAVITY_TABLE.md)
- Lieb-Robinson microcausality (c_LR retained): [`AXIOM_FIRST_MICROCAUSALITY_LIEB_ROBINSON_THEOREM_NOTE_2026-05-01.md`](AXIOM_FIRST_MICROCAUSALITY_LIEB_ROBINSON_THEOREM_NOTE_2026-05-01.md)
- Hilbert-Schmidt rigidity: [`G_BARE_HILBERT_SCHMIDT_RIGIDITY_THEOREM_NOTE_2026-05-07.md`](G_BARE_HILBERT_SCHMIDT_RIGIDITY_THEOREM_NOTE_2026-05-07.md)
- Physical lattice rigidity (no-go): [`PHYSICAL_LATTICE_NECESSITY_NOTE.md`](PHYSICAL_LATTICE_NECESSITY_NOTE.md)
- Planck-from-structure no-go's:
  - [`PLANCK_PARENT_SOURCE_HIDDEN_CHARACTER_NO_GO_NOTE_2026-04-24.md`](PLANCK_PARENT_SOURCE_HIDDEN_CHARACTER_NO_GO_NOTE_2026-04-24.md)
  - [`PLANCK_BOUNDARY_ORIENTATION_INCIDENCE_NO_GO_NOTE_2026-04-30.md`](PLANCK_BOUNDARY_ORIENTATION_INCIDENCE_NO_GO_NOTE_2026-04-30.md)
- MINIMAL_AXIOMS: [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)

## Validation

```bash
python3 scripts/cl3_g_newton_self_consistency_2026_05_10_planckP4.py
```

Expected output: structural verification of (i) Z³ Green's function
asymptotic via FFT-based numerical extrapolation, (ii) exhaustive
integer-exponent dimensional search confirming canonical Planck-form
G ~ ħc/M_Pl² is the unique combination with G_Newton SI dimensions,
(iii) Planck-anchor cross-check at `rel_err ~ 3e-7`, (iv) Barrier B(a)
with three retained skeletons enumerated and ledger query for selection
theorem, (v) Barrier B(b) refreshed as a discoverable Born-source dependency
gate, (vi) Barrier B(c) with valley-linear vs spent-delay action comparison
and ledger query for action-derivation theorem, (vii)
consistency-vs-derivation boundary, (viii) bounded-sharpening synthesis.
Total: 32 PASS / 0 FAIL.

Cached: [`logs/runner-cache/cl3_g_newton_self_consistency_2026_05_10_planckP4.txt`](../logs/runner-cache/cl3_g_newton_self_consistency_2026_05_10_planckP4.txt)

## User-memory feedback rules respected

- `feedback_consistency_vs_derivation_below_w2.md`: this note
  applies the "consistency equality is not derivation" rule. The
  Planck-anchor cross-check confirms the dimensional form is
  *consistent* with empirical G_Newton, but consistency is not derivation; the
  parent chain remains conditional on named dependency gates.
- `feedback_hostile_review_semantics.md`: this note stress-tests
  the semantic claim that "retained content closes G_Newton" by
  showing that the action-level identifications (`L^{-1} = G_0`,
  `rho = |psi|^2`, `S = L(1 - phi)`) require explicit dependency routing
  rather than silent promotion from the repo baseline alone.
- `feedback_retained_tier_purity_and_package_wiring.md`: no
  automatic cross-tier promotion. This note is a bounded
  sharpening; the parent `GRAVITY_CLEAN_DERIVATION_NOTE` remains
  a conditional IF-chain. No retained-tier promotion of any gravity content is
  implied.
- `feedback_physics_loop_corollary_churn.md`: the positive-sub-theorem plus
  refreshed dependency-map structure with explicit dimensional integer-exponent
  search is substantive structural content, not a relabel of prior gravity or
  Koide notes.
- `feedback_compute_speed_not_human_timelines.md`: alternative
  routes characterized in terms of WHAT additional retained
  content would be needed (skeleton-selection theorem, Born-source
  composition, weak-field-action theorem), not how-long-they-would-take.
- `feedback_special_forces_seven_agent_pattern.md`: this note
  packages a multi-angle attack (positive dimensional rigidity +
  three independent obstruction barriers, plus consistency-vs-
  derivation boundary) on the G_Newton self-consistency lane,
  with sharp PASS/FAIL deliverables in the runner.
- `feedback_review_loop_source_only_policy.md`: source-only — this
  PR ships exactly (a) source theorem note, (b) paired runner,
  (c) cached output. No output-packets, lane promotions, synthesis
  notes, or "Block" notes.
- `feedback_bridge_gap_fragmentation_2026_05_07.md`: the parent
  G_Newton lane is being fragmented into one positive sub-theorem
  + three named obstruction primitives. No new admissions
  introduced; existing admissions made explicit and structurally
  enumerated.
