# Bridge-1 Gauge Algebra Forced, Gauging Selection Admitted — No-Go Note

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-08
**Type:** named-obstruction no-go (with a positive consolidation rider)
**Claim type:** no_go
**Status:** no-go proposal. Records the honest Bridge-1 verdict: the Standard
Model gauge **algebra** `su(N_c) ⊕ su(2) ⊕ u(1)` is forced as the carrier
symmetry (with `N_c = d` a genuine covariation), while the **gauging selection**
— which symmetry is dynamically gauged, the physical-color identification
`MR_color`, and the chiral `su(2)_L` — is the irreducible admission. Adds no
axiom, no fitted/imported value. Audit verdict set by the independent audit lane.
**Authority role:** no-go source proposal (Bridge-1 gauge-group residual).
**Primary runners:**
[`scripts/bridge1_gauge_algebra_forced_gauging_admitted_2026_06_08.py`](../scripts/bridge1_gauge_algebra_forced_gauging_admitted_2026_06_08.py)
(forced algebra, PASS=4),
[`scripts/bridge1_color_base_covariance_Nc_equals_d_2026_06_08.py`](../scripts/bridge1_color_base_covariance_Nc_equals_d_2026_06_08.py)
(`N_c = d` covariation, PASS=4), and
[`scripts/bridge1_gauging_discriminator_blindness_no_go_2026_06_08.py`](../scripts/bridge1_gauging_discriminator_blindness_no_go_2026_06_08.py)
(discriminator blindness, PASS=4); exact numpy.

## The bridge

Bridge-1 is the gauge group on the links of the `{Lattice, Quantum, Record}`
framework. The carrier is the per-site qubit `M_2(ℂ) = Cl(3,0)` (Quantum) on
`Z^3` (Lattice). The question: do the three axioms fix the **gauge group** that
acts on the links, or only part of it?

## What is FORCED (gauge algebra; runner-checked from the axioms)

1. **`qubit → u(2)`.** The infinitesimal automorphisms of `M_2(ℂ)` are `su(2)`
   (the three Paulis close `[σ_i,σ_j] = 2i ε_{ijk} σ_k`); with the central
   `u(1)` the link connection algebra is `u(2) = su(2) ⊕ u(1)` (dim 4). This is
   the retained `QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04`.
2. **`N_c = d` is a genuine covariation, not a coincidence.** The taste cube is
   `{0,1}^d` (one taste qubit per spatial axis). Selecting one axis as the weak
   `su(2)` fiber leaves the `d-1` residual axes as the base `(ℂ^2)^{⊗(d-1)}`;
   the residual permutation group `S_{d-1}` splits it, and the fully-symmetric
   (trivial-isotype) block is `Sym^{d-1}(ℂ^2)` of dimension `(d-1)+1 = d`. By
   Schur–Weyl the `S_{d-1}` commutant on that block is `gl(d)`, semisimple part
   `su(d)`. So the color block dimension **co-varies** with the lattice
   dimension: `d=2 → su(2)`, `d=3 → su(3)`, `d=4 → su(4)`, `d=5 → su(5)`
   (runner table). Hence `N_c = d = dim Z^d` at `d=3` is a **derivation**, the
   color number tracking the spatial dimension under counterfactual variation —
   not a matched-pair coincidence. This **affirms and sharpens** the retained
   `CL3_COLOR_AUTOMORPHISM_THEOREM` / `GRAPH_FIRST_SU3_INTEGRATION_NOTE`.
3. **The SM gauge algebra is the carrier symmetry.** On `ℂ^{N_c}(base) ⊗
   ℂ^2(fiber)` the color `su(N_c)` and weak `su(2)` **commute**; with the
   central `u(1)` the carrier's symmetry algebra is `su(N_c) ⊕ su(2) ⊕ u(1)`.
   At `d=3`: `su(3) ⊕ su(2) ⊕ u(1)`, dim `8+3+1 = 12` — exactly the SM gauge
   algebra. Both `su(2)` on `ℂ^2` and `su(N_c)` on `ℂ^{N_c}` act **irreducibly**
   (complex commutant = scalars, Schur).

## What is ADMITTED — the gauging selection (the no-go)

The three axioms fix the symmetry **algebra** but do not fix the **gauging**:
*which* symmetry is dynamically gauged, the physical-color identification
`MR_color`, and the chiral `su(2)_L`. An adversarial campaign hunted ten
framework-native discriminators (maximality / "gauge everything that acts",
anomaly cancellation, faithfulness, reflection positivity, the color-base
derivation, color-singlet records / confinement, the chirality grading `ε`,
Lorentz / spacetime emergence, local tomography / the complex `i`, and
minimality). **All ten failed**; each is provably blind to, or circular with,
the gauging selection. The rock-solid, independently re-derived facts:

- **Maximality is blind.** On the dim-6 carrier the SM algebra (dim 12) and the
  full `u(6)` (dim 36) **both** act irreducibly, so the
  Record/indistinguishability criterion (`gauge = what records cannot
  distinguish`) returns the **same** verdict (commutant = scalars) for both. It
  cannot select dim-12; the only cut from `u(6)` to dim-12 is the factor-local
  `ℂ^{N_c} ⊗ ℂ^2` split, which **is** `MR_color` — circular.
- **Anomaly cancellation is a one-sided filter, never a selector.** The
  symmetric cubic `d_{abc}` is identically `0` for `su(2)` (anomaly-free for any
  content) and nonzero for `su(3)` (`max|d| = 1/√3`). Anomaly-freedom constrains
  a *given* content; it never selects which group is gauged, and writing the
  content presupposes `MR_color` (circular).
- **The chirality grading `ε` is blind to the coupling.** `[Γ_ε, T^a] = 0`
  (`ε` and the weak generators live on different tensor factors), and
  `{Γ_ε, D·T^a} = {Γ_ε, D·T^a·P_L} = {Γ_ε, D·T^a·P_R} = 0`. So `ε` carries
  **zero** information about whether the connection rides `P_L`, `P_R`, or
  neither — chiral `su(2)_L` is a separate spin/chirality admission.
- **Color is complex; spatial rotation is real.** The reality test (∃ invariant
  bilinear) gives nullspace `0` for the `su(3)` fundamental (strictly complex,
  `3 ≠ 3̄`) but `≥1` for the `so(3)` spatial vector (real). So color `su(3)` is
  **not** a complexification of the spatial 3-frame; the Lorentz/spacetime route
  points the wrong way.

Net: the dim-12 SM algebra has no extremal or monotone property under any
maximality / minimality / faithfulness / anomaly / positivity functional;
reaching it requires first imposing the factor-locality split = `MR_color`. Six
routes now prune to the same `MR_color` residual (the five in
`COLOR_SU3_MATTER_REALIZATION_RESIDUAL_MAP_2026-06-05` plus the campaign's
maximality route).

## A campaign no-go that was REFUTED (process record)

The campaign's color-base lens claimed `N_c = 3 = dim Z^3` is a *matched-pair
coincidence* (asserting the base is `Sym^2(ℂ^2)`, dim 3, **independent of `d`**),
and recommended demoting the retained claim. Independent re-derivation
**refutes** this: the base is `Sym^{d-1}(ℂ^2)` (dim `d`), whose exponent `d-1`
varies — the lens hardcoded the `d=3` instance (`Sym^2`, two qubits) and read it
as `d`-independent. `N_c = d` genuinely co-varies, so the retained claim
**stands** and is *not* demoted. This is the same failure mode as the closed
`det_C` reframe: a self-consistent multi-agent no-go whose load-bearing
covariance claim was false, caught by re-deriving the bridge from primitives.

## Verdict

`{Lattice, Quantum, Record}` force the SM gauge **algebra** `su(N_c=d) ⊕ su(2) ⊕
u(1)` as the symmetry of the link carrier (a genuine derivation, including the
`N_c = d` covariation). They do **not** force the **gauging selection** — which
symmetry is dynamically gauged, the physical-color identification `MR_color`, or
the chiral `su(2)_L` — because every framework-native discriminator is provably
blind to it or circular with `MR_color`. **The gauging selection is the
irreducible Bridge-1 admission.**

## What is and is not claimed

- **Is:** the gauge algebra `su(d) ⊕ su(2) ⊕ u(1)` is forced (with `N_c = d`
  covariation); the gauging selection (`MR_color` + chiral `su(2)_L`) is admitted
  and unreachable by maximality/anomaly/faithfulness/RP/chirality/Lorentz/
  composition/minimality; the campaign's `N_c=3`-coincidence claim is refuted.
- **Is not:** does **not** claim the gauging is impossible to derive in a richer
  theory; does **not** re-derive the carrier itself; does **not** demote any
  retained claim; introduces no axiom and changes no prediction. Using `MR_color`
  to argue any gauging conclusion is flagged as circular.

## Load-bearing inputs

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) — the Lattice
  `Z^3`, the Quantum qubit `M_2(ℂ)=Cl(3,0)`, and the Record readout; all algebra
  facts (`su(2)` closure, `Sym^{d-1}(ℂ^2)` dimensions, Schur–Weyl `gl(d)`
  commutant, `d_{abc}`, the `ε` anticommutation, the reality bilinear) are
  reproven in the three runners.

Companion + context (plain references, not load-bearing deps):
`CL3_COLOR_AUTOMORPHISM_THEOREM.md`, `GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`,
`QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04.md`,
`COLOR_SU3_MATTER_REALIZATION_RESIDUAL_MAP_2026-06-05.md`,
`TWO_ENDPOINT_GAUSS_LAW_INVARIANCE_PROFILE_BOUNDED_THEOREM_NOTE_2026-06-05.md`,
`STAGGERED_DIRAC_CHIRALITY_PARITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md`,
`ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md`.

## Forbidden-imports check

No PDG / fitted / literature numerical comparator is consumed. The `su(2)`/`su(3)`
algebra, the `Sym^{d-1}(ℂ^2)` symmetric-block dimensions and their `gl(d)`
commutant (Schur–Weyl), the cubic `d_{abc}`, the `ε`/`P_{L,R}` anticommutation,
and the invariant-bilinear reality test are all reproven in the runners from the
three axioms. The Standard Model gauge group is named as the comparator target,
never as a derivation input.
