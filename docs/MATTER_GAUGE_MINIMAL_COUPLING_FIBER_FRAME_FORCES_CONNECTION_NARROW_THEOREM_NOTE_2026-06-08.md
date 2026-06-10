# Matter-Gauge Minimal Coupling from Local Fibre-Frame Redundancy

**Date:** 2026-06-08
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_minimal_coupling_fiber_frame_connection_2026_06_08.py`](../scripts/frontier_minimal_coupling_fiber_frame_connection_2026_06_08.py)
**Cached runner output:**
[`logs/runner-cache/frontier_minimal_coupling_fiber_frame_connection_2026_06_08.txt`](../logs/runner-cache/frontier_minimal_coupling_fiber_frame_connection_2026_06_08.txt)

## Claim under test

Given a local fibre-frame redundancy premise, can the matter-gauge
minimal-coupling kinematics — the link connection `U_μ(x)`, the gauge-covariant
hopping `H_cov = Σ a_x† U_μ(x) a_{x+μ} + h.c.`, and the lattice covariant
derivative `(D_μψ)(x) = U_μ(x)ψ(x+μ) − ψ(x)` — be derived as finite
frame-covariance algebra rather than inserted as a separate link-field postulate?

The wall-map of the interacting sector records that every prior note using the link
`U_μ = exp(igaA_μᵃTᵃ)` *imports* it: there is no note deriving where the connection
comes from or why a gauge field lives on the `Z³` links. This note fills that gap at
the **kinematic** level (the connection's existence and gauge law), leaving the gauge
**action**/dynamics to the separate Yang–Mills target.

## Verdict

**Yes, at the kinematic current-surface level.** The one-hop bridge
[`FIBER_FRAME_LOCAL_REDUNDANCY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-09.md`](FIBER_FRAME_LOCAL_REDUNDANCY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-09.md)
proves that local `U(3)` fibre-frame choices are passive trivialization
changes for the registered weak/Record-sector data currently present in the
cited authorities, and that the translation bridge's `U=I` reference is the
flat cross-site trivialization rather than an invariant physical fibre pinning.
With that bridge, frame-independent nearest-neighbour hopping uniquely
requires a compensating link transporter with the lattice connection law. The
covariance identity itself is unconditional finite algebra; the physical
reading remains bounded to kinematics and to the current registered surface.

## Retained foundations exercised

1. **`graph_first_su3_integration_note`** — *retained* (positive_theorem).
   Each site carries an internal **`SU(3)` fibre** = the commutant of the observable
   weak-`su(2)` action on the taste cube; the full retained commutant is
   `gl(3) ⊕ gl(1)`, so the fibre **structure group is `U(3) = SU(3) × U(1)`**, the
   abelian factor "hypercharge-like" (that note's own boundary §"What remains bounded").

2. **`tensor_product_translation_fermion_operator_bridge_narrow_theorem_note_2026-05-25`**
   — *retained* (positive_theorem). Per-site fermion operators `a_x` with the
   translation law `T_a a_x T_a† = a_{x+a}`. Its decoration
   `hopping_bilinear_hermiticity_theorem_note_2026-05-02` gives the **Hermitian,
   number-conserving nearest-neighbour hopping bilinear** `a_x† a_y + a_y† a_x`.

3. **Lattice and Quantum axioms.** `Z³` with nearest-neighbor adjacency and
   one-qubit operator algebra at each site. These axioms do not by themselves
   supply a gauge field, gauge action, dynamics, or physical `SU(3)_c`
   identification.

4. **`fiber_frame_local_redundancy_bridge_narrow_theorem_note_2026-06-09`** —
   current-surface bridge. Local `U(3)` fibre-frame changes are passive
   trivialization changes for the registered weak/Record-sector data currently
   present in the cited authorities. The flat `U=I` translation reference is a
   choice of neighbouring-fibre coordinates, since independent local bases
   rewrite it as `g(x)g(x+μ)†`; it is not a physical cross-site fibre pinning.

## The discharged current-surface bridge

The bridge note proves the local fibre-frame redundancy needed here at the
current registered-surface level:

- *Frame rotations preserve current registered data.* On the graph-first
  weak/fibre carrier `C²_weak ⊗ C³_fibre`, a local frame change has the form
  `I_2 ⊗ g(x)`. It commutes with the retained weak `su(2)` generators and
  fixes the weak central-sector projectors consumed by the Record-sector
  readout context used in the cited authorities.

- *No fibre-colour basis is selected.* The only fibre operator invariant under
  the full local `U(3)` frame group is a scalar multiple of `I_3`; a rank-one
  colour/fibre projector would add extra structure not supplied by the current
  cited authorities.

- *The retained translation bridge supplies the flat trivialization, not a
  physical pinning.* Its `T_a a_x T_a† = a_{x+a}` identity is the `U=I`
  coordinate choice. Under independent neighbouring fibre bases it is
  represented as `g(x)g(x+μ)†`, so `I` is not a local-frame-invariant
  cross-site physical object.

This bridge does not say that future colour readout contexts are impossible,
and it does not supply gauge action/dynamics. It only discharges the kinematic
frame-redundancy premise needed by this note on the current registered surface.

## The derivation

### Step 1 — The hopping term silently chooses a cross-site frame

The retained hopping `Σ_x a_x† a_{x+μ} + h.c.` contracts the fibre index of `a_{x+μ}`
(in *some* frame at `x+μ`) with that of `a_x†` (in *some* frame at `x`). Writing it as
`Σ_{x,i} a_{x,i}† a_{x+μ,i}` presupposes that "frame label `i` at `x`" means the same as
"frame label `i` at `x+μ`". The Lattice and Quantum axioms do not supply such a
canonical identification.

### Step 2 — Local frame change breaks the naive hopping

A local frame re-choice acts as `a_x → ρ(g(x)) a_x`, `g(x) ∈ U(3)`. Under a **global**
`g`, the naive hopping is invariant (`g†g = I`). Under a **local** `g(x)` it is **not**:
`a_x† a_{x+μ} → a_x† ρ(g(x))† ρ(g(x+μ)) a_{x+μ} ≠ a_x† a_{x+μ}` unless `g(x)=g(x+μ)`.
*(Runner Part 1: free hopping is global- but not local-invariant.)*

### Step 3 — Frame-independence fixes the connection law

To make the retained hopping independent of the arbitrary local frame, introduce a
compensating **link variable** `U_μ(x) ∈ ρ(U(3))` and define the **covariant hopping**

```
    H_cov = Σ_{x,μ} a_x† U_μ(x) a_{x+μ} + h.c.
```

`H_cov` is invariant under the local frame change **iff** `U_μ(x)` transforms as

```
    U_μ(x)  →  ρ(g(x)) U_μ(x) ρ(g(x+μ))† .                    (parallel-transporter law)
```

This is precisely the gauge-transformation law of a **lattice connection** on the link
`(x, x+μ)`. The central identity, verified exactly,

```
    G H_cov[U] G†  =  H_cov[U'],     U'_μ(x) = g(x) U_μ(x) g(x+μ)† ,
```

(`G = ⊕_x ρ(g(x))`) holds to `6×10⁻¹⁵` *(Runner Part 2)*. Hence the spectrum of
`H_cov` is a gauge invariant.

### Step 4 — The law is unique; `D_μ` is covariant

Every other site-assignment (`g(x)Ug(x)†`, `g(x+μ)Ug(x)†`, one-sided) **breaks**
covariance *(Runner Part 3)*. The associated **lattice covariant derivative**
`(D_μψ)(x) = U_μ(x)ψ(x+μ) − ψ(x)` transforms covariantly, `(D'_μψ')(x) = g(x)(D_μψ)(x)`,
while the naive difference `ψ(x+μ)−ψ(x)` does not *(Runner Part 4)*. The connection is
exactly what repairs the difference operator.

### Step 5 — Gauge-invariant content = closed loops; minimal-coupling form

Closed-loop holonomies (plaquette traces `Tr U_p`) are gauge invariant; open Wilson
lines `Tr U_μ(x)` are not *(Runner Part 5)* — the physical, registered content is the
**closed-loop** data. Writing `U_μ = exp(iε A_μ)` with `A_μ` Hermitian (algebra-valued
connection), the unscaled covariant difference has the finite-link expansion
`(D_μψ)(x) = (ψ(x+μ)-ψ(x)) + iε A_μ(x)ψ(x+μ) + O(ε²)` — equivalently, after
dividing by `ε`, the standard first-order **minimal-coupling form** on the normalized
lattice derivative — with the residual confirmed `O(ε²)` (log–log slope `2.00`)
*(Runner Part 6)*. The same argument
with `g(x) = e^{iθ(x)}I` forces an **abelian (hypercharge-like) connection** for the
`U(1)` factor *(Runner Part 7)*.

## What the runner verifies (`PASS=23 FAIL=0`)

- `U_μ(x)`, `g(x) ∈ SU(3)`; `H_free`, `H_cov` Hermitian; `U=I` ⇒ retained free hopping.
- Free hopping global-invariant, **not** local-invariant (the problem is real).
- **Central:** `G H_cov[U] G† = H_cov[U']` under the transporter law (to `6e-15`);
  spectrum gauge-invariant.
- Transporter law **unique** — four wrong site-assignments all break covariance.
- `D_μ` covariant, naive `∂_μ` not.
- Plaquette holonomy gauge-invariant, open line not; flat connection trivial holonomy.
- Leading-order finite-link minimal coupling
  `(D_μψ)(x) = (ψ(x+μ)-ψ(x)) + iε A_μ(x)ψ(x+μ) + O(ε²)`, residual `O(ε²)`
  (slope `2.00`).
- `U(1)` factor forces an abelian connection by the same argument.

## What this closes

- The matter-gauge **minimal-coupling kinematics** are no longer an
  unstructured postulate on the current registered surface: the link
  transporter, its gauge law, the covariant derivative, and gauge invariance of
  `H_cov` follow from frame independence of nearest-neighbor hopping on the
  retained `U(3)` fibre, using the one-hop local frame-redundancy bridge.
- A reusable on-surface origin for the gauge field: it is the **bookkeeping of the
  framework's absent canonical cross-site fibre identification** — the chosen
  local fibre trivialization on the current registered surface — rather than a
  postulated `U_μ = exp(igaA)`. This does not rely on loose register-not-read
  reasoning beyond the explicit current-surface bridge above.

## What this does NOT close

- **No gauge action / dynamics for `U_μ`.** This is pure kinematics: `U_μ` here is a
  background connection, not a dynamical field with a Yang–Mills/Wilson/heat-kernel
  action. Deriving that action is the separate gauge-action target.
- **No continuum limit, no coupling value.** Part 6 is a leading-order finite-link
  consistency check, not an `a→0` statement; `g` and `g_bare=1` are untouched.
- **No physical `SU(3)_c` identification beyond the algebraic fibre** — deferred exactly
  as in `graph_first_su3_integration_note`; the abelian factor remains "hypercharge-like"
  pending the anomaly-complete identification.
- **No theorem about future colour readouts.** The local frame-redundancy
  bridge covers the registered weak/Record-sector data currently present in
  the cited authorities. It does not prove that later colour-readout contexts
  cannot register additional fibre data.

## Scope and non-claims

The covariance theorem (Steps 3–4) is an exact finite-dimensional identity, verified at
`(L=2)³` with `C³` fibres; it is representation-independent (depends only on `g†g=I`).
This note adds no new axiom, primitive, or Tier-A admission. It uses the two
cited retained theorems, the current-surface local frame-redundancy bridge,
and the Lattice, Quantum, and Record axioms. It cites the standard
fibre-bundle/connection correspondence only as mathematical method. The
physical connection reading is kinematic/current-surface only; the algebraic
covariance core is exact finite operator algebra.

## Cross-references

- Retained fibre: [`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md)
- Retained operators/translation: [`TENSOR_PRODUCT_TRANSLATION_FERMION_OPERATOR_BRIDGE_NARROW_THEOREM_NOTE_2026-05-25.md`](TENSOR_PRODUCT_TRANSLATION_FERMION_OPERATOR_BRIDGE_NARROW_THEOREM_NOTE_2026-05-25.md)
- Hopping bilinear (decoration): [`HOPPING_BILINEAR_HERMITICITY_THEOREM_NOTE_2026-05-02.md`](HOPPING_BILINEAR_HERMITICITY_THEOREM_NOTE_2026-05-02.md)
- Local fibre-frame bridge: [`FIBER_FRAME_LOCAL_REDUNDANCY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-09.md`](FIBER_FRAME_LOCAL_REDUNDANCY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-09.md)
- Downstream gauge-action target: not load-bearing for this note.
- Standard method (not an import): lattice gauge connection / parallel transport
  (Wilson 1974; Kogut–Susskind 1975); fibre-bundle origin of gauge fields.
