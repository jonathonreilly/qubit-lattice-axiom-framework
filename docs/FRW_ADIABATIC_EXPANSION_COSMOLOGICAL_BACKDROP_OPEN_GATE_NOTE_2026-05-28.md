# FRW + Adiabatic Expansion Cosmological-Backdrop Open Gate

**Date:** 2026-05-28
**Claim type:** open_gate
**Status authority:** independent audit lane only. This source note is a
proposal that decomposes the FRW + adiabatic-expansion cosmological
backdrop used by the cosmology / η-cascade lanes into its
framework-derivable components and its imported components. The note
does **not** set, predict, or alter any row's effective status; audit
verdict and downstream status are set only by the independent audit
lane.
**Type:** open_gate
**proposal_allowed:** false
**Primary runner:** [`scripts/frontier_frw_adiabatic_expansion_cosmological_backdrop_open_gate.py`](../scripts/frontier_frw_adiabatic_expansion_cosmological_backdrop_open_gate.py)

## Claim

The cosmology and η lanes silently rely on a *cosmological backdrop*
combining three structural ingredients: (i) the spatial geometry on
which fields propagate, (ii) the Einstein/Friedmann dynamical law, and
(iii) the thermal history (a homogeneous, isotropic, **adiabatic**
expansion with a textbook radiation -> matter -> Lambda equation-of-state
sequence). This open gate decomposes the backdrop into:

* **framework-derivable on the current retained stack** — the qualitative
  spatial topology;
* **conditional on already-conditional retained chains** — the FRW
  kinematic / open-number reduction surface used to count late-time
  degrees of freedom;
* **supplied local backdrop premises, not registry admissions** — the
  cosmological principle (homogeneity + isotropy beyond `S^3`
  topology), adiabatic expansion (no entropy injection between
  leptogenesis and CMB), and the specific late-time equation-of-state
  evolution.

Stated as a single composition bridge:

> Given the retained `S^3` spatial topology and the
> already-conditional FRW kinematic / open-number reduction surface,
> the η-cascade's cosmological backdrop closes **only after**
> admitting the supplied premise packet C1–C3 below. The bridge
> records that admission boundary explicitly so the cosmology η-
> cascade depends on this backdrop, and the gate is upstream of the
> `(C2.η)` cycle-2 sub-lane in
> `HUBBLE_LANE5_COSMIC_HISTORY_RATIO_NECESSITY_NO_GO_NOTE_2026-04-26.md`
> (non-load-bearing context citation).

The gate introduces **no new admissions and no new repo-wide
vocabulary**. It re-bases the cosmology / η-cascade's existing
backdrop usage onto an explicit named-premise block so the conditional
chain is exposed rather than implicit. It does **not** promote any
authority, retire the parent admission, change any row's
`effective_status`, or claim that C1, C2, or the full
cosmological-fluid application of C3 are derived from `Cl(3)` on
`Z^3`.

## Honest framing up front

This is an **open gate / admission-boundary record**, not a derivation. The cosmology η-
cascade has long carried a tacit FRW + adiabatic-expansion premise
that does not appear in any single named-premise block on the retained
surface. The cosmological constant spectral-gap identity, the dark-
energy EOS retained corollary, the Ω_Λ matter-bridge identity, and the
late-time kinematic reduction are all derivations *given* this
backdrop; none of them derive the backdrop itself. The honest move is
to (a) name what the framework currently supplies (`S^3` qualitative
spatial topology + conditional FRW reduction surface), (b) name what
must be admitted on top (cosmological principle + adiabatic expansion
+ EOS sequence), and (c) record a "what would close this" roadmap.
The note does no more.

## Supplied premise packet (not axioms, not registry premises)

The following entries are the complete non-framework premise packet
for this bridge. They are supplied only for this bridge's
decomposition arithmetic; they are **not** registry accepted premises
and no new repo-wide axiom is introduced.

- **C1 Cosmological principle (homogeneity + isotropy beyond
  topology).** On scales above the retained `S^3` substrate's
  largest cubical-ball radius `R`, the matter / radiation /
  vacuum-energy fluid is approximated as spatially homogeneous and
  isotropic to leading order in the relevant cosmological power
  spectrum. Equivalently, the bulk stress-energy tensor is taken in
  the perfect-fluid form `T^μ_ν = diag(-ρ, p, p, p)` and the
  background metric is FRW on the spatial topology `S^3`.

- **C2 Adiabatic expansion (no entropy injection in the cosmology
  era used by the η-cascade).** Between the heavy-Majorana
  leptogenesis era and the CMB-recombination era used by the η /
  `Ω_b` / `Ω_DM` / `Ω_m` / `Ω_Λ` cascade, the comoving entropy
  density `s a^3` is conserved up to the standard `g_{*S}(T)`
  step-function bookkeeping. No additional reheating / decay /
  late-decoupling injection is admitted on this surface.

  2026-06-18 C2 entropy-bookkeeping partial bridge: the finite
  source-free bookkeeping identity behind `s a^3 = const` and
  `g_{*S}(T) T^3 a^3 = const` is no longer a pure textbook import on
  this branch; see
  [FRW_C2_SOURCE_FREE_ENTROPY_BOOKKEEPING_BOUNDED_SUPPORT_NOTE_2026-06-18.md](FRW_C2_SOURCE_FREE_ENTROPY_BOOKKEEPING_BOUNDED_SUPPORT_NOTE_2026-06-18.md).
  This proves only the finite source-free entropy bookkeeping. It
  does not derive that the real leptogenesis-to-CMB window is
  source-free and does not derive the Standard Model `g_*S` table.

- **C3 Standard FRW equation-of-state sequence on the retained
  cosmology surface.** The standard radiation -> matter -> Λ
  equation-of-state taxonomy
  `w_r = 1/3`, `w_m = 0`, `w_Lambda = -1`
  is admitted as the textbook FRW component classification on the
  late-time bounded surface, exactly as already used in
  `COSMOLOGY_FRW_KINEMATIC_REDUCTION_THEOREM_NOTE_2026-04-24.md`.
  `w_Lambda = -1` itself is supplied separately by the existing
  `DARK_ENERGY_EOS_RETAINED_COROLLARY_THEOREM_NOTE.md`;
  C3 admits only the non-Λ component labels.

  2026-06-18 C3 kinetic-label partial bridge: the non-Λ ideal kinetic
  component labels `w_r = 1/3` and `w_m = 0` are no longer pure
  textbook import on this branch for finite signed-permutation kinetic
  surfaces; see
  [FRW_C3_EOS_COMPONENT_LABELS_KINETIC_BRIDGE_BOUNDED_SUPPORT_NOTE_2026-06-18.md](FRW_C3_EOS_COMPONENT_LABELS_KINETIC_BRIDGE_BOUNDED_SUPPORT_NOTE_2026-06-18.md).
  This does not derive C1 or C2, does not derive the full FRW
  backdrop, and does not by itself prove that the ideal labels apply
  to the actual cosmological fluids.

  2026-06-18 C3 perfect-fluid lift partial bridge: the ideal kinetic
  component labels now have a finite stress-tensor lift into the
  mixed perfect-fluid form used by this parent note; see
  [FRW_C3_KINETIC_COMPONENT_PERFECT_FLUID_LIFT_BOUNDED_SUPPORT_NOTE_2026-06-18.md](FRW_C3_KINETIC_COMPONENT_PERFECT_FLUID_LIFT_BOUNDED_SUPPORT_NOTE_2026-06-18.md).
  This proves the finite component-aggregation step only. It does not
  derive C1 or C2 and does not derive real cosmological species
  allocation into those ideal components.

This bridge proves: **if** the retained `S^3` spatial topology is
combined with the already-conditional FRW kinematic / open-number
reduction surface and the supplied premise packet C1–C3, **then** the
cosmological backdrop used by the η-cascade and the late-time
bounded cosmology variable set is the explicit conditional surface
recorded below. It does **not** claim to derive C1, C2, or C3 from
`Cl(3)` on `Z^3`; after the 2026-06-18 partial bridge, the narrower
statement is that C1, C2, and the full cosmological-fluid application
of C3 remain outside this parent note, except for the two partial
finite C3 bridges named above and the partial finite C2 bookkeeping
bridge.

## Decomposition table

Each row of the cosmological backdrop is decomposed into a single
load-bearing class:

| Backdrop ingredient | Framework status (live ledger 2026-05-28) | Class on this bridge |
|---|---|---|
| Spatial topology `S^3` (qualitative compact closed three-manifold) | `unaudited` positive-theorem on the cone-capped cubical ball derivation surface | framework-derivable (conditional on lane audit) |
| FRW kinematic reduction surface (late-time closed-form table) | `unaudited` positive-theorem on the matter-bridge + EOS retained chain | conditional on retained chain |
| Cosmology open-number reduction (two structural DoF at fixed `R`) | `unaudited` positive-theorem on the same chain | conditional on retained chain |
| `N_eff = 3 + 0.046 = 3.046` (active-neutrino bookkeeping) | `unaudited` positive-theorem (active count 3 from three retained generations; +0.046 textbook) | conditional on retained chain + textbook correction |
| Cosmological principle (homogeneity + isotropy on scales above the `S^3` ball radius) | not derived; not supplied by any retained note | **local supplied premise C1** |
| Adiabatic expansion (no entropy injection in the leptogenesis -> CMB window) | finite source-free entropy and `g_*S T^3 a^3` bookkeeping now have bounded support; the real no-injection era and the `g_*S` table are not derived | **local supplied premise C2, narrowed by the 2026-06-18 entropy-bookkeeping partial bridge; real source-free window remains supplied** |
| Standard radiation -> matter -> Lambda equation-of-state taxonomy (`w_r=1/3`, `w_m=0`; `w_Lambda=-1` separately retained) | `w_Lambda = -1` is handled by a separate corollary; `w_r=1/3` and `w_m=0` now have exact finite kinetic bounded support for ideal component labels, and those component tensors have a finite perfect-fluid lift | **local supplied premise C3, narrowed by the 2026-06-18 kinetic-label and perfect-fluid-lift partial bridges; real species allocation remains supplied** |

The local-supplied-premise label is deliberately non-registry language. This
note does **not** add C1, C2, or C3 to `docs/audit/data/tier_a_admissions.json`
and does **not** claim membership in the Tier-A registry.

## Proof-walk

| Step | Statement | Load-bearing input |
|---|---|---|
| (B1) | The cone-capped cubical ball `M_R = B_R ∪ cone(∂B_R)` is PL homeomorphic to `S^3` for every `R ≥ 2`, supplying the qualitative spatial topology used by the FRW background | Retained S^3 general-R derivation (`S3_GENERAL_R_DERIVATION_NOTE.md`) |
| (B2) | On the (B1) topology combined with C1 + C3, the homogeneous-isotropic perfect-fluid stress-energy form on a flat FRW background is the relevant cosmology surface; this is the explicit setup already used by the FRW kinematic reduction theorem | C1 + C3 supplied premise packet + already-conditional FRW reduction note; the ideal non-Lambda kinetic labels in C3 have bounded support from the 2026-06-18 kinetic bridge, and their finite component tensors lift to the perfect-fluid form in the 2026-06-18 fluid-lift bridge |
| (B3) | On the (B2) background plus the retained `w_Λ = −1` corollary, the late-time bounded cosmology variable set has exactly two structural degrees of freedom at fixed admitted radiation `R := Ω_r,0`, by the open-number reduction theorem | Retained dark-energy EOS corollary + already-conditional open-number reduction note |
| (B4) | On the (B3) background plus C2 (adiabatic expansion), the comoving entropy `s a^3` is conserved across the leptogenesis -> CMB window, which is the load-bearing premise that lets the η-cascade factorize as `η = (s/n_γ) · C_sph · d_N · ε_1 · κ_axiom[H]` (the leptogenesis transport-decomposition theorem) | C2 supplied premise + already-conditional transport-decomposition note; finite source-free entropy and `g_*S` bookkeeping are supported by the 2026-06-18 entropy-bookkeeping bridge, while the real no-injection era remains supplied |
| (B5) | The (B4) factorization plus the retained `N_active = 3` and the textbook `Δ N_eff = 0.046` correction yields `N_eff = 3.046` as the radiation-era effective relativistic count used by the cosmology η-cascade | C3 radiation component label, with finite ideal-kinetic support for `w_r=1/3` and a finite perfect-fluid lift; already-conditional `N_eff` note; textbook `Δ N_eff` correction remains separate |
| (B6) | Conclusion: the cosmology η-cascade's cosmological backdrop closes only after admitting C1 + C2 + C3 on top of the retained `S^3` topology and the already-conditional FRW kinematic / open-number / `N_eff` / transport-decomposition chain. This is the admission boundary the bridge records | (B1) + (B2) + (B3) + (B4) + (B5) |

The proof-walk does **not** cite the Wilson plaquette action, staggered
phases, Brillouin-zone labels, link unitaries, lattice scale `u_0`, a
Monte Carlo measurement, or a fitted observational value. It does not
derive C1, C2, or the full FRW application of C3 from `Cl(3)` on
`Z^3`.

## What this admission bridge retires vs leaves admitted

To be explicit about scope:

**Retired to bounded-derived class on this bridge's surface (no new
work; only re-basing onto the explicit C1–C3 packet):**

- The ideal kinetic component labels `w_r = 1/3` and `w_m = 0` are
  now supported by
  [FRW_C3_EOS_COMPONENT_LABELS_KINETIC_BRIDGE_BOUNDED_SUPPORT_NOTE_2026-06-18.md](FRW_C3_EOS_COMPONENT_LABELS_KINETIC_BRIDGE_BOUNDED_SUPPORT_NOTE_2026-06-18.md)
  on finite signed-permutation kinetic surfaces. This is a partial
  C3 narrowing only.
- The finite component tensors for those ideal labels now assemble
  into the parent perfect-fluid form by
  [FRW_C3_KINETIC_COMPONENT_PERFECT_FLUID_LIFT_BOUNDED_SUPPORT_NOTE_2026-06-18.md](FRW_C3_KINETIC_COMPONENT_PERFECT_FLUID_LIFT_BOUNDED_SUPPORT_NOTE_2026-06-18.md).
  This is also a partial C3 narrowing only. No retained-grade row is
  promoted, demoted, or rebased by this note, and the parent FRW
  backdrop remains open.
- The finite source-free entropy and `g_*S T^3 a^3` bookkeeping behind
  C2 is now supported by
  [FRW_C2_SOURCE_FREE_ENTROPY_BOOKKEEPING_BOUNDED_SUPPORT_NOTE_2026-06-18.md](FRW_C2_SOURCE_FREE_ENTROPY_BOOKKEEPING_BOUNDED_SUPPORT_NOTE_2026-06-18.md).
  This is a partial C2 narrowing only. It does not prove that the
  actual cosmological window is source-free.

**Left admitted (the admission boundary recorded by this bridge):**

- **C1** — the cosmological principle beyond the retained `S^3`
  topology;
- **C2 residual** — the physical no-entropy-injection claim for the
  leptogenesis -> CMB window and the source authority for the
  `g_*S(T)` inventory;
- **C3 residual** — real species allocation of the actual cosmological
  radiation / matter content into the ideal finite kinetic components
  (`w_Λ = −1` is separately handled and is **not** admitted here).

This is the honest scope: the bridge retires only narrow finite C2/C3
bookkeeping and label/lift imports and does not retire the
cosmological-backdrop admission. It records the admission boundary and
exposes the conditional chain that the η-cascade depends on,
parallel to the way
`HYPERCHARGE_ALPHA_THIRD_NORMALIZATION_BRIDGE_BOUNDED_NOTE_2026-05-25.md`
(non-load-bearing voice-template citation) re-bases the hypercharge
`α = 1/3` admission onto an explicit P1–P4 premise packet without
eliminating the admission.

## Roadmap — what would close each admission

This is a "what would close this" companion roadmap, supplied because
the prompt requested one. It is **not** load-bearing for any claim
above; the roadmap items are open and remain so.

- **Closing C1 (cosmological principle).** Would require a framework-
  internal *early-universe coherence* argument: a derivation that the
  retained primordial spectrum content combined with a finite-`R`
  cubical-ball substrate forces approximate large-scale homogeneity
  / isotropy as a structural consequence rather than as an admitted
  initial-condition statement. The `PRIMORDIAL_SPECTRUM_NOTE.md` row
  (non-load-bearing roadmap pointer) is the natural starting
  authority on this lane, currently `unaudited` bounded-grade. No
  retained-grade closer exists at the time of writing.
- **Closing C2 (adiabatic expansion).** Would require a framework-
  retained inflation-reheating treatment that derives `s a^3`
  conservation across the leptogenesis -> CMB window from primitives
  rather than admitting the physical no-injection era. The
  2026-06-18 entropy-bookkeeping partial bridge proves the finite
  source-free algebra, including `g_*S T^3 a^3 = const`, but it does
  not prove that the real window is source-free or derive the
  Standard Model `g_*S(T)` inventory. The retained heavy-Majorana
  scale and the `N_eff` derivation give the input/output endpoints of
  the window, but the in-window physical no-injection statement
  remains open. No retained-grade closer exists today.
- **Closing C3 (EOS component labels).** The 2026-06-18 kinetic-label
  partial bridge derives the ideal finite kinetic labels
  `w_r = 1/3` and `w_m = 0` on signed-permutation kinetic surfaces.
  The 2026-06-18 perfect-fluid-lift partial bridge proves that those
  component tensors assemble into the mixed perfect-fluid form used by
  the parent FRW surface. The remaining C3 work is real species
  allocation: prove that the actual cosmological radiation/matter
  content used by the η-cascade is exhausted by those ideal finite
  kinetic components, with the required homogeneity/isotropy and
  thermal-history hypotheses made explicit. The `w_Λ = −1` corollary
  already exists on its own surface.

The roadmap is descriptive only. C1, the physical no-injection part of
C2, and the real species-allocation part of C3 are not claimed
derivable on the current retained surface, and the bridge does not
predict that any of them will close.

## Context Surfaces

- `S3_GENERAL_R_DERIVATION_NOTE.md`
  — supplies the qualitative compact closed three-manifold spatial
  topology in step (B1). Live ledger status: `unaudited`,
  `positive_theorem`.
- `COSMOLOGY_FRW_KINEMATIC_REDUCTION_THEOREM_NOTE_2026-04-24.md`
  — supplies the late-time kinematic-reduction surface used in step
  (B2). Live ledger status: `unaudited`, `positive_theorem`.
- `COSMOLOGY_OPEN_NUMBER_REDUCTION_THEOREM_NOTE_2026-04-26.md`
  — supplies the two-structural-DoF open-number-reduction surface
  used in step (B3). Live ledger status: `unaudited`,
  `positive_theorem`.
- `DARK_ENERGY_EOS_RETAINED_COROLLARY_THEOREM_NOTE.md`
  — supplies the `w_Λ = −1` retained corollary used in step (B3).
  Live ledger status: `unaudited`, `positive_theorem`.
- `DM_LEPTOGENESIS_TRANSPORT_DECOMPOSITION_THEOREM_NOTE_2026-04-16.md`
  — supplies the leptogenesis transport-decomposition factorization
  used in step (B4). Live ledger status: `unaudited`,
  `positive_theorem`.
- `N_EFF_FROM_THREE_GENERATIONS_THEOREM_NOTE_2026-04-24.md`
  — supplies the active-neutrino count used in step (B5). Live
  ledger status: `unaudited`, `positive_theorem`.

These are context surfaces for this open gate, not retained-grade
load-bearing dependencies. The gate records that the backdrop remains open
until the relevant surfaces and C1-C3 are independently resolved.

## Non-Load-Bearing Context

The following are referenced for orientation only. Per the repo's
cycle-break / non-load-bearing convention, these are listed in
backtick form so the citation-graph builder does not register them as
load-bearing dependency edges.

- `ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md` is the canonical
  Tier-A admission registry. This bridge does **not** add C1, C2, or
  C3 to the Tier-A registry.
- `HUBBLE_LANE5_C3_VACUUM_TOPOLOGY_NO_ACTIVE_ROUTE_NOTE_2026-04-27.md`
  is the orthogonal `(C3)` direct-vacuum/topology audit no-go. This
  bridge is **not** a (C3) candidate; it sits on the (C2.η)-prior
  background side.
- `HYPERCHARGE_ALPHA_THIRD_NORMALIZATION_BRIDGE_BOUNDED_NOTE_2026-05-25.md`
  is the voice-template admission bridge mirrored here (re-basing an
  existing admission onto an explicit named-premise block without
  eliminating the admission).
- `PRIMORDIAL_SPECTRUM_NOTE.md`, `COSMOLOGY_SCALE_IDENTIFICATION_AND_REDUCTION_NOTE.md`,
  `COSMOLOGICAL_CONSTANT_SPECTRAL_GAP_IDENTITY_THEOREM_NOTE.md`,
  `OMEGA_LAMBDA_MATTER_BRIDGE_THEOREM_NOTE_2026-04-22.md`,
  `R_BASE_GROUP_THEORY_DERIVATION_THEOREM_NOTE_2026-04-24.md`,
  `MATTER_RADIATION_EQUALITY_STRUCTURAL_IDENTITY_THEOREM_NOTE_2026-04-24.md`,
  and `COSMOLOGY_SINGLE_RATIO_INVERSE_RECONSTRUCTION_THEOREM_NOTE_2026-04-25.md`
  are the broader cosmology-cascade context this bridge sits next to;
  none are load-bearing for the admission decomposition above.

The non-framework inputs are exactly C1–C3. The row remains unaudited
until the independent audit lane reviews this note, its dependencies,
supplied premise packet, and runner.

## Boundaries

This bridge does **not** close:

- derivation of the cosmological principle (C1) from `Cl(3)` on
  `Z^3`;
- derivation of the real no-entropy-injection era or the `g_*S(T)`
  inventory (C2 residual) from a framework-retained
  inflation-reheating treatment;
- real species allocation of the actual cosmological fluids into the
  ideal matter / radiation kinetic components (C3 residual);
- the numerical value of `H_0`, `Ω_Λ`, `Ω_m`, or any other late-time
  cosmology observable (those remain on the open-number-reduction
  surface, unchanged);
- the Planck-scale anchor that gives `R_Λ` numerically (Planck lane;
  separate);
- any continuum-limit numerical claim such as plaquette, mass, or
  coupling values;
- any parent theorem / status promotion (the bridge records the
  admission boundary as a separate bounded identity candidate;
  downstream status of every cited cosmology authority is decided by
  the audit lane on its own row);
- promotion of any Tier-A registry entry (the Tier-A registry is
  untouched by this note).

The bridge re-bases the cosmology η-cascade's existing FRW + adiabatic
backdrop usage onto the explicit C1–C3 premise packet. The 2026-06-18
C2 entropy-bookkeeping bridge narrows only the finite source-free
bookkeeping algebra, and the C3 kinetic-label and perfect-fluid-lift
partial bridges narrow only the ideal non-Lambda component labels and
their finite stress-tensor assembly; they do **not** eliminate the
parent admission. It formally exposes the conditional chain. It
introduces no new repo-wide tag, no new "cosmological backdrop class",
no new "FRW landing tier", and no new theorem class.

## Downstream Source-Boundary Firewall

This open gate may not be cited downstream as a retained derivation of any of
the following:

- C1, the physical no-injection part of C2, or the real
  species-allocation part of C3;
- FRW dynamics;
- entropy conservation or adiabatic expansion;
- observational cosmology parameters;
- parent theorem status.

C1-C3 also may not be moved into a registry, admission file, or premise file
by citing this packet. Such a move requires a separate source note, runner,
review, and independent audit. Future use must separately prove or explicitly
admit the cosmological principle, physical adiabatic expansion /
entropy-source absence, matter and radiation real species allocation,
FRW dynamics, observational-parameter
bridges, and any parent-status closure.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_frw_adiabatic_expansion_cosmological_backdrop_open_gate.py
```

Expected:

```text
TOTAL: PASS=72 FAIL=0
VERDICT: open gate passes; FRW + adiabatic backdrop decomposition is recorded as an unresolved C1-C3 premise boundary with partial bounded support for finite C2 entropy bookkeeping, the ideal non-Lambda C3 kinetic labels, and their finite perfect-fluid lift. No new admissions are introduced; no row's effective status is changed.
```
