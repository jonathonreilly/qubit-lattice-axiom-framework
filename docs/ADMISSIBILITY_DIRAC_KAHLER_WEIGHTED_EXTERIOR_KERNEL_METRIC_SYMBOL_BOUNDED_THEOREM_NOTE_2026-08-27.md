---
claim_id: admissibility_dirac_kahler_weighted_exterior_kernel_metric_symbol_bounded_theorem_note_2026-08-27
final_path: docs/ADMISSIBILITY_DIRAC_KAHLER_WEIGHTED_EXTERIOR_KERNEL_METRIC_SYMBOL_BOUNDED_THEOREM_NOTE_2026-08-27.md
claim_type: bounded_theorem
claim_scope: "Exact finite exterior-algebra construction of a constant-coefficient nearest-neighbor kernel from the declared D3(g,V) carrier; necessary and sufficient metric-volume normalization V^2=det(g) for full generalized-Clifford closure at positive g; exact flat-rule intertwiner, a landed two-dimensional shear window, and one genuinely three-direction rational witness. No framework selection of D3 or g, variable metric, physical time, Lorentzian signature, dynamics, gravity law, or continuum limit is supplied."
runner: scripts/admissibility_dirac_kahler_weighted_exterior_kernel_metric_symbol_2026_08_27.py
status: proposed_retained
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the constant positive three-metric symbol is not yet a variable spacetime operator, and the framework axioms do not yet select D3, g, or a Lorentzian continuation"
source_of_blocker_text: physics_loop
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Construct the variable-cell transport/connection required for D3(g_s,V_s)-adjointness across neighboring cells, then test the OS/Wick interface without assuming a physical time direction."
conditional_surface_status: "stacked on an unmerged ancestor chain; proposed science remains review- and audit-required"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact rational-function identities, an exact normalization selector, an explicit flat intertwiner, and exact finite rational witnesses"
audit_required_before_effective_retained: true
bare_retained_allowed: false
parent_ref: origin/physics-loop/toe-axiom-closure-block212-joint-pin-order-extended-alphabet-20260827
parent_commit: 4e9931a970ded94f769553da9e6d77770d612f64
scientific_parent: block_209_three_direction_rule_geometry
current_main: 66e478505e055faf4a5b9e6f4883211e44304718
registered: 0
adopted: 0
axiom_movement: none
---

# The metric-weighted exterior kernel and its exact finite symbol

**Date:** 2026-08-27

**Type:** `bounded_theorem`

**Status:** `proposed_retained` — a review proposal, not an audit verdict.

## Result in plain language

Block 209 produced a finite three-dimensional geometry candidate

```text
D3(g,V) = diag(V, V g^-1, E g E/V, 1/V).
```

This block makes it carry a propagation kernel instead of merely being a cell
weight. The construction is canonical once `D3` and the exterior differential
are supplied: take exterior multiplication and add its adjoint in the `D3`
inner product. The resulting direction matrices square to the inverse-metric
quadratic form, including all off-diagonal direction mixing.

The calculation also removes one freedom. Full closure on all exterior degrees
occurs exactly when

```text
V^2 = det(g).
```

Thus `V` cannot remain an independent positive scale if it is to be the volume
used by this metric Kähler-Dirac kernel. It must equal the positive metric
volume `sqrt(det(g))`. This is a selection theorem **inside the declared D3
candidate family**. It is not a derivation that Nature or the four framework
axioms select `D3`.

## 1. Supplied finite objects

Use direction order `(t,x,y)` only as a coordinate label and set

```text
g = [[1,    c_tx, c_ty],
     [c_tx, 1,    c_xy],
     [c_ty, c_xy, 1   ]].
```

The exterior basis is the eight corners

```text
1, dy, dx, dx^dy, dt, dt^dy, dt^dx, dt^dx^dy,
```

with corner index `4t+2x+y`. Let `epsilon_d` be left exterior multiplication
by the one-form in direction `d`. These exact integer matrices obey

```text
epsilon_d^2 = 0,
epsilon_d epsilon_e + epsilon_e epsilon_d = 0.
```

The supplied inner-product candidate is Block 209's

```text
D3(g,V) = diag(W0,W1,W2,W3),
W0 = V,
W1 = V g^-1,
W2 = E g E/V,       E = diag(1,-1,1),
W3 = 1/V.
```

No import of a continuum Dirac operator is made. All matrices are built
directly on this eight-element finite exterior carrier.

## 2. The weighted link matrices

Define the adjoint of `epsilon_d` with respect to `D3` by

```text
epsilon_d^dagger = D3^-1 epsilon_d^T D3,
Gamma_d = epsilon_d + epsilon_d^dagger.
```

Each `Gamma_d` is exactly self-adjoint in the supplied inner product:

```text
Gamma_d^T D3 = D3 Gamma_d.
```

On a periodic coordinate lattice, let the centered difference be

```text
nabla_d = (T_d - T_d^-1)/2
```

and define the constant-cell kernel

```text
K_D3 = sum_d Gamma_d nabla_d.
```

Equivalently, the forward hop in direction `d` carries `Gamma_d/2` and the
backward hop carries `-Gamma_d/2`. Because the link matrices are
`D3`-self-adjoint and the centered differences are antisymmetric, `K_D3` is
skew-adjoint in the product `D3` inner product.

At momentum `k`, put `q_d = sin(k_d)`. The Fourier symbol is

```text
K_D3(k) = i Gamma(q),
Gamma(q) = sum_d q_d Gamma_d.
```

## 3. Where the volume condition comes from

Let `iota_d^(g)` be contraction with the co-metric:

```text
iota_d^(g) = sum_e (g^-1)_de epsilon_e^T.
```

The runner evaluates the `D3` adjoint separately on every adjacent degree.
It finds

```text
degree 1 -> 0:  epsilon_d^dagger = iota_d^(g),
degree 2 -> 1:  epsilon_d^dagger = [det(g)/V^2] iota_d^(g),
degree 3 -> 2:  epsilon_d^dagger = iota_d^(g).
```

The only mismatch is the middle lowering map. It is not a numerical accident
or a fitted coefficient: it is the exact rational function
`rho = det(g)/V^2`.

Consequently all six generalized-Clifford residuals

```text
Gamma_d Gamma_e + Gamma_e Gamma_d - 2(g^-1)_de I8
```

are divisible by `V^2-det(g)`. Setting `V^2=det(g)` kills them identically.

Necessity on the positive-metric domain is also exact. For each direction,

```text
tr[Gamma_d^2 - (g^-1)_dd I8]
    = 4 [det(g)/V^2 - 1] (g^-1)_dd.
```

If `g` is positive definite, `(g^-1)_dd>0`. Full closure therefore forces
`det(g)/V^2=1`. Together with sufficiency, this proves:

> For positive `g` and positive `V`, the full eight-component D3-adjoint
> exterior kernel obeys the generalized Clifford algebra if and only if
> `V^2=det(g)`.

## 4. The metric symbol

On that locus,

```text
Gamma(q)^2 = q^T g^-1 q I8,
-K_D3(k)^2 = sin(k)^T g^-1 sin(k) I8.
```

This is the requested off-diagonal weighted symbol. For example, its mixed
`t-x` term is

```text
2 (g^-1)_tx sin(k_t) sin(k_x).
```

The squared finite symbol therefore carries the exact co-metric quadratic
form rather than only three independently rescaled coordinate squares.

For positive `g`, the quadratic form is nonnegative. This is a Euclidean
co-metric statement. The coordinate called `t` has not been identified as
physical time, no Lorentzian signature has been derived, and no physical
light cone is claimed.

## 5. Exact flat bridge to the landed covariant rule

At `g=I3`, `V=1`, the carrier is `D3=I8`. The three exterior generators are
ordinary real symmetric `Cl(3,0)` generators. The runner supplies an explicit
integer matrix `S` with

```text
S^T S = 8 I8,
det(S) = 4096,
Gamma_d S = S diag(G_d,G_d),
```

where the `G_d` are exactly Block 209's real `4 x 4` generators. Thus the
flat exterior carrier is two exact copies of the landed pre-staggered rule,
not merely another representation with matching eigenvalues.

Transporting Block 209's word staggering through this same `S` gives an exact
orthogonal `Omega_8(s)`. On all eight anchor parities and all three links,

```text
Omega_8(s)^T [Gamma_d/2] Omega_8(s+e_d)
    = eta_d(s) I8/2.
```

So the construction returns to the landed scalar eta link in the flat limit.
The exact `(4,4)` and `(4,4,4)` momentum histograms are respectively

```text
{0:4, 1:8, 2:4},
{0:8, 1:24, 2:24, 3:8},
```

which are precisely the finite `sum_d sin^2(k_d)` values and multiplicities.

## 6. Exact landed two-dimensional window

Set

```text
c_tx = 3/5,
c_ty = c_xy = 0,
V = 4/5.
```

Then `det(g)=16/25=V^2`. On the `tx` exterior subspace, `D3` restricts exactly
to the landed two-dimensional shear-Hodge form

```text
diag(V, V [[1,c],[c,1]]^-1, 1/V).
```

For `q_y=0`, the weighted symbol obeys

```text
Gamma(q)^2
  = [q_t^2 - 2c q_t q_x + q_x^2]/(1-c^2) I8.
```

This is an exact overlap with the landed 2D geometry at a rational
metric-volume point. It is not an interpolation or a continuum approximation.

## 7. A genuinely three-direction rational witness

To prove that the construction is not only a decoupled-plane result, choose

```text
c_tx = c_ty = c_xy = 11/50,
V = 117/125.
```

Then

```text
det(g) = 13689/15625 = (117/125)^2,

g^-1 = (1/1404) [[1525,-275,-275],
                  [-275,1525,-275],
                  [-275,-275,1525]].
```

All eight leading principal minors of `D3` are positive. Every off-diagonal
co-metric entry is nonzero, and all six generalized-Clifford identities hold
exactly. Across all `64` momenta of the `4^3` grid, the quadratic values and
multiplicities are

```text
0             : 8
1525/1404     : 24
625/351       : 12
25/12         : 2
100/39        : 12
5125/1404     : 6
```

The split away from the flat `{0,1,2,3}` histogram is the exact finite effect
of direction mixing.

## 8. Why scalar eta reweighting is insufficient

If one keeps scalar staggered links and merely gives the three axes scalar
magnitudes `w_d`, their square has the form

```text
sum_d w_d^2 sin^2(k_d).
```

Its mixed derivatives with respect to two different `sin(k_d)` variables are
zero. A sheared co-metric instead has mixed derivative `2(g^-1)_de`, nonzero
at the rational witness above. Therefore axis-by-axis scalar weights cannot
carry the off-diagonal metric.

At least one structural change is necessary: matrix-valued link mixing as
constructed here, oblique hops, or another carrier with the same mixed
anticommutators. The present construction chooses the first and remains
nearest-neighbor along the coordinate axes.

## 9. What advanced, and what remains open

This block closes the constant-cell design question posed after the flat
dispersion scout:

- an explicit weighted kernel now exists;
- its square is the exact inverse-metric quadratic form;
- its flat limit is exactly tied to the landed covariant rule;
- its 2D restriction meets the landed shear-Hodge form;
- and compatibility selects `V=sqrt(det(g))` inside the D3 family.

It does **not** yet supply:

- a derivation selecting `D3` or `g` from the four framework axioms;
- a rule for varying `g` and `V` from cell to cell;
- the transport/connection terms needed for adjointness when neighboring
  cells have different carriers;
- a physical temporal direction, Lorentzian continuation, causal cone, or
  dispersion relation solved for energy;
- record-production dynamics, a gravity field equation, backreaction, or a
  continuum limit.

The next load-bearing science block is the variable-cell transport problem.
It must determine whether neighboring `D3(g_s,V_s)` carriers admit a local
link transport that preserves the weighted adjoint and reduces to this
constant-cell kernel. Only after that construction is explicit is an OS/Wick
or physical cone analysis licensed.

## Reproduction

```bash
python3 scripts/admissibility_dirac_kahler_weighted_exterior_kernel_metric_symbol_2026_08_27.py
```

Expected result:

```text
TOTAL: PASS=18 FAIL=0
```
