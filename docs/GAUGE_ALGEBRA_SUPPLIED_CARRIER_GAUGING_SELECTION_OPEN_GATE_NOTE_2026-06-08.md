# Gauge Algebra on a Supplied Color Carrier and the Gauging-Selection Open Gate

**Date:** 2026-06-08
**Claim type:** open_gate
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runners:**
[`scripts/gauge_algebra_supplied_carrier_2026_06_08.py`](../scripts/gauge_algebra_supplied_carrier_2026_06_08.py),
[`scripts/color_base_covariance_nc_equals_d_support_2026_06_08.py`](../scripts/color_base_covariance_nc_equals_d_support_2026_06_08.py),
[`scripts/gauging_selection_discriminator_open_gate_2026_06_08.py`](../scripts/gauging_selection_discriminator_open_gate_2026_06_08.py),
[`scripts/gauge_algebra_parent_kinematic_bridge_firewall_2026_06_18.py`](../scripts/gauge_algebra_parent_kinematic_bridge_firewall_2026_06_18.py)
**Cached runner outputs:**
[`logs/runner-cache/gauge_algebra_supplied_carrier_2026_06_08.txt`](../logs/runner-cache/gauge_algebra_supplied_carrier_2026_06_08.txt),
[`logs/runner-cache/color_base_covariance_nc_equals_d_support_2026_06_08.txt`](../logs/runner-cache/color_base_covariance_nc_equals_d_support_2026_06_08.txt),
[`logs/runner-cache/gauging_selection_discriminator_open_gate_2026_06_08.txt`](../logs/runner-cache/gauging_selection_discriminator_open_gate_2026_06_08.txt),
[`logs/runner-cache/gauge_algebra_parent_kinematic_bridge_firewall_2026_06_18.txt`](../logs/runner-cache/gauge_algebra_parent_kinematic_bridge_firewall_2026_06_18.txt)

## Supplied assumptions

The algebra result is **conditional** on a supplied color-carrier realization. None of the
following is supplied by the Lattice, Quantum, and Record axioms; each is a
separate non-axiom input or existing bounded/open authority:

| supplied input | authority | ledger role |
|---|---|---|
| the taste-cube / fiber-base split and the **`C³(base) ⊗ C²(fiber)` carrier factorization** | [`COLOR_SU3_MATTER_REALIZATION_RESIDUAL_MAP_2026-06-05.md`](COLOR_SU3_MATTER_REALIZATION_RESIDUAL_MAP_2026-06-05.md) | `MR_color` residual (meta) |
| the **selected weak axis** + the residual-swap base split → `su(3)` on `Sym²(ℂ²)` | [`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md), [`CL3_COLOR_AUTOMORPHISM_THEOREM.md`](CL3_COLOR_AUTOMORPHISM_THEOREM.md) | retained (algebraic embedding; physical-color identification explicitly deferred there) |
| the single-qubit fibre algebra boundary `qubit → u(2)` | [`QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04.md`](QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04.md) | bounded local-algebra support |
| the current-surface local-fibre-frame redundancy and link-transporter law | [`FIBER_FRAME_LOCAL_REDUNDANCY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-09.md`](FIBER_FRAME_LOCAL_REDUNDANCY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-09.md), [`MATTER_GAUGE_MINIMAL_COUPLING_FIBER_FRAME_FORCES_CONNECTION_NARROW_THEOREM_NOTE_2026-06-08.md`](MATTER_GAUGE_MINIMAL_COUPLING_FIBER_FRAME_FORCES_CONNECTION_NARROW_THEOREM_NOTE_2026-06-08.md) | retained-bounded kinematic bridge |
| the **two-endpoint Gauss carrier / gauging principle** | [`TWO_ENDPOINT_GAUSS_LAW_INVARIANCE_PROFILE_BOUNDED_THEOREM_NOTE_2026-06-05.md`](TWO_ENDPOINT_GAUSS_LAW_INVARIANCE_PROFILE_BOUNDED_THEOREM_NOTE_2026-06-05.md) | unaudited model convention |

## 2026-06-18 kinematic bridge update

The link-connection part of the old supplied-input list is no longer being
used as an unstructured convention. On the current registered `U(3)` fibre
surface, two retained-bounded one-hop authorities now supply the kinematic
bridge:

- [`FIBER_FRAME_LOCAL_REDUNDANCY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-09.md`](FIBER_FRAME_LOCAL_REDUNDANCY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-09.md)
  proves that local `U(3)` fibre-frame changes rewrite a flat cross-site
  trivialization as a link transporter rather than as a physical pinning.
- [`MATTER_GAUGE_MINIMAL_COUPLING_FIBER_FRAME_FORCES_CONNECTION_NARROW_THEOREM_NOTE_2026-06-08.md`](MATTER_GAUGE_MINIMAL_COUPLING_FIBER_FRAME_FORCES_CONNECTION_NARROW_THEOREM_NOTE_2026-06-08.md)
  proves the finite current-surface covariance theorem: frame-independent
  nearest-neighbour hopping forces the lattice connection law and the
  covariant difference on the retained `U(3)` fibre.

This update retires only the *kinematic link-transporter convention* on the
current surface. It does **not** select the factorwise `su(3) ⊕ su(2) ⊕ u(1)`
subgroup, does **not** derive `MR_color` or factor-locality, does **not**
derive chiral `su(2)_L`, and does **not** supply gauge action, dynamics,
couplings, or a continuum limit.

## Bounded support — the factor-preserving algebra, GIVEN the carrier

**Given** the supplied `C³(base) ⊗ C²(fiber)` carrier, the runner verifies (exact, finite):
`su(2) = Aut(M₂(ℂ))` closes on the fiber (`u(2) = su(2)⊕u(1)`); `su(3)` has no faithful irrep
below dim 3, so color needs the 3-dim base; `su(3)⊗I` and `I⊗su(2)` **commute**, and with the
central `u(1)` the **factor-preserving** algebra of this supplied carrier split is
`su(N_c) ⊕ su(2) ⊕ u(1)` — at `d=3`, dim `8+3+1 = 12`.

This is not the full internal algebra on the six-dimensional carrier. The unrestricted
anti-Hermitian algebra on `C³⊗C² ≅ C⁶` is `u(6)` (dim 36). The runner now checks that the
factor-preserving dim-12 algebra plus the 24 cross-factor tensors
`su(3)⊗su(2)` spans the full `u(6)`. Thus the cut from `u(6)` to
`su(3)⊕su(2)⊕u(1)` is exactly the supplied factor-locality / `MR_color`
premise. It is **not** derived from the Lattice, Quantum, and Record axioms.

## Counterfactual support — `N_c = d`

Under an **assumed** `Z^d` taste-cube family with one selected weak axis, the residual base
is `Sym^{d-1}(ℂ²)` (dim `d`) and its `S_{d-1}` symmetric-isotype commutant is `gl(d)` →
color block `su(d)`, so `N_c = d` along the family (runner table `d=2..6`). At the `Z³`
baseline this gives `N_c = 3`, **consistent with** the retained graph-first `SU(3)` result on
the live `d=3` surface. This is **support** — it shows `N_c` tracks the (assumed) lattice
dimension, addressing a "matched-pair coincidence" worry — **not** a from-axioms derivation
(the `Z^d` family, taste-cube, and weak-axis selection are assumed). The repo baseline is
`Z³`; the live derivation of the `d=3` color structure remains the retained graph-first note.

## The gauging-selection open gate

The supplied carrier plus supplied factor-locality premise fixes a candidate
factor-preserving **algebra** but does not fix the **gauging selection**:
which symmetry is dynamically gauged, the physical-color identification
`MR_color`, the chiral `su(2)_L`, or why cross-factor `u(6)` generators are
dynamically absent. The discriminator runner tests **four** candidate
discriminators and finds each blind to or circular with the selection: (1)
maximality cannot distinguish the dim-12 factor-preserving algebra from the
full `u(6)` (both irreducible → same commutant); (2) the anomaly `d`-tensor is a one-sided filter (`su(2)` `d_{abc}≡0`,
`su(3)` `d_{abc}≠0`), never a selector; (3) the chirality grading `ε` commutes with the color
generators (blind to the coupling chirality); (4) color is strictly complex (`3 ≠ 3̄`) while
the spatial `so(3)` vector is real (color ≠ complexified spatial). These four do **not close**
the gate. (A broader lens set was explored in an exploratory campaign, but only these four are
runner-backed here; closing the selection as a *no-go* would require the full N1–N8 route
enumeration with retained-authority failures, which this note does **not** assert.)

## 2026-06-16 Post-Audit Conditional Boundary

Independent audit correctly leaves this row conditional. The finite checks show
that the supplied `C³(base) ⊗ C²(fiber)` carrier supports a commuting
`su(3) ⊕ su(2) ⊕ u(1)` subalgebra and that four tested discriminators do not
select the gauged subgroup. They do **not** prove that this dim-12 subalgebra is
unique against the full `u(6)` carrier algebra, do not derive `MR_color`, and do
not derive chiral `su(2)_L`.

The 2026-06-18 kinematic bridge update changes the boundary in one narrow
place: local-fibre-frame covariance now supplies the current-surface link
transporter and lattice connection law as retained-bounded kinematics. The
remaining supplied/open inputs are the carrier factorization and
factor-locality/`MR_color`, the selection of the factorwise subgroup rather
than full `u(6)` or a non-factor-local conjugate, the physical-color
identification, chiral `su(2)_L`, and gauge action/dynamics.

The repair boundary is therefore:

```text
supplied carrier + supplied weak-axis/fiber split
  + retained-bounded local-frame link-connection kinematics
  => conditional algebraic support for the candidate dim-12 subalgebra
     and a four-discriminator open gate.
```

Any clean promotion requires a separate retained bridge deriving or admitting
the carrier/gauge-selection principle and the chiral weak coupling surface.

### 2026-06-16 Exact independence addendum

[`GAUGE_GAUGING_SELECTION_CONJUGATION_INDEPENDENCE_NO_GO_NOTE_2026-06-16.md`](GAUGE_GAUGING_SELECTION_CONJUGATION_INDEPENDENCE_NO_GO_NOTE_2026-06-16.md)
adds a narrow exact negative boundary for one tempting repair route. On the
same supplied `C³(base) ⊗ C²(fiber)` carrier, a non-factor-local unitary
conjugate of the factorwise `su(3) ⊕ su(2) ⊕ u(1)` algebra has the same
dimension, closure, and scalar commutant while being a distinct embedding; the
full `u(6)` carrier algebra also has scalar commutant. Therefore
irreducibility, scalar-commutant/record-indistinguishability, or
conjugation-invariant carrier algebra data cannot select the factorwise
dim-12 gauging. This prunes that repair route only. It does **not** derive
`MR_color`, the factorwise carrier/gauge-selection principle, or chiral
`su(2)_L`, and it does not change this row's audit status.

### 2026-06-18 Factor-local normalizer addendum

[`GAUGE_FACTOR_LOCAL_SELECTOR_NORMALIZER_THEOREM_NOTE_2026-06-18.md`](GAUGE_FACTOR_LOCAL_SELECTOR_NORMALIZER_THEOREM_NOTE_2026-06-18.md)
adds the positive finite-algebra companion to the conjugation-independence
no-go. On the same supplied `C^3(base) x C^2(fiber)` carrier, if one supplies
the rule that infinitesimal gauged generators preserve the base and fiber
observable algebras separately, the exact normalizer is uniquely
`u(3) x I_2 + I_3 x u(2)`, i.e. `su(3) + su(2) + u(1)` after the shared center
is counted once. The 24 `su(3) x su(2)` cross tensors are then exactly the
non-factor-local complement to full `u(6)`.

This closes no physical selection bridge by itself. It localizes the remaining
gap: the row still requires a retained source or explicit admission for
`MR_color`, for the physical factor-algebra preservation rule, and for chiral
`su(2)_L`. The addendum changes no audit status.

## What is and is not claimed

- **Is:** GIVEN the supplied carrier and its supplied factor-locality premise, the
  factor-preserving algebra is `su(N_c)⊕su(2)⊕u(1)` (dim 12 at `d=3`), with
  the factors commuting and acting irreducibly (bounded support); the full
  unrestricted carrier algebra is `u(6)` and the missing `u(6)`-to-factorwise
  selection is exposed rather than hidden; `N_c=d` holds along an assumed
  `Z^d` family, consistent with the retained `d=3` graph-first result
  (counterfactual support); local-frame covariance supplies the current-surface
  link-transporter and connection law as retained-bounded kinematics; the
  gauging subgroup selection is **not closed** by the four tested
  discriminators (open gate).
- **Is not:** does **not** claim the SM gauge algebra is *forced from the axioms* (the carrier
  is supplied); does **not** claim the gauging selection is an *irreducible admission / no-go*
  (it is an open gate, not a closed no-go, and no N1–N8 walk is asserted); does **not** derive
  the carrier, the factorwise subgroup selection, chiral `su(2)_L`, or
  `MR_color`; adds no axiom or fitted value.

## Boundaries (honest)

- **Conditional factor-preserving algebra, not an axiom-level derivation.** Every
  factorwise algebra statement is "given the supplied `C³⊗C²` carrier and the
  supplied factor-locality / `MR_color` premise"; the carrier itself is the
  non-axiom `MR_color`/graph-first realization, and the full internal algebra
  on the carrier is `u(6)`.
- **Counterfactual support, not a theorem about `Z³`.** The `N_c=d` covariance lives in an
  assumed `Z^d` family; on the baseline `Z³` it only re-supports the retained `d=3` surface.
- **Open gate, not a no-go.** The four discriminators are runner-backed support that the
  selection is not closed by them; this is not a proof that no discriminator can close it.

## Forbidden-imports check

No PDG / fitted / literature value is consumed. The algebra (Aut `M₂`, the
`su(3)` irrep dimension, the `[su(3),su(2)]=0` commutation, the full `u(6)`
dimension and `su(3)⊗su(2)` complement, the `Sym^{d-1}(ℂ²)`/`gl(d)`
commutant, the `d_{abc}` tensor, the `ε`/color commutator, the reality
bilinear) is reproven in the runners from the qubit and lattice primitives.
The Standard Model gauge group is named as the comparator target only.
