# R_conn Endpoint Gauge-Frame Dichotomy

**Date:** 2026-07-12
**Claim type:** bounded_theorem
**Status:** exact support on the separated open-bilocal gauge-orbit surface;
the physical connected-current matching rule remains open. Independent audit
lane review is required before this source proposal has any retained-grade
effect.
**Primary runner:**
[`scripts/frontier_rconn_endpoint_gauge_frame_dichotomy.py`](../scripts/frontier_rconn_endpoint_gauge_frame_dichotomy.py)
**Cached output:**
[`logs/runner-cache/frontier_rconn_endpoint_gauge_frame_dichotomy.txt`](../logs/runner-cache/frontier_rconn_endpoint_gauge_frame_dichotomy.txt)

## Question

Why is the equilibrium expectation of the legacy color-projection statistic

```text
C/T = (N_c^2 - 1)/N_c^2,
```

even though a Fierz dimension count does not determine a dynamical correlator
weight?

The answer is a symmetry dichotomy. The legacy script applies the trace split
to an open propagator matrix between two distinct lattice sites. In an ideal
gauge-invariant equilibrium ensemble, independent endpoint gauge rotations
make its conditional orbit average isotropic in the full `N_c^2`-dimensional
matrix space. That forces the `1 : (N_c^2-1)` split exactly, without using the
gauge action or planar dynamics. A finite Markov-chain run is only an estimator
of that expectation. Once the endpoints are physically identified, only
diagonal conjugation remains and the singlet and adjoint sectors may carry
independent weights.

This derives the old numerical target as a gauge-frame identity. It is not a
physical connected-current ratio and it does not derive `kappa_EW = 0`.

## 1. The trace split used by the legacy runner

Let `V_x` and `V_y` be the color fibers at distinct sites `x != y`, and let

```text
M : V_y -> V_x
```

be the open quark propagator matrix. The legacy runner computes

```text
T(M) = Tr(M M^dagger),
S(M) = |Tr M|^2/N_c,
C(M) = T(M) - S(M).
```

The trace in `S(M)` uses the coordinate color bases to identify `V_x` with
`V_y`. Under independent local gauge rotations,

```text
M -> Omega_x M Omega_y^dagger.
```

`T` is invariant, but `S` and `C` are not. The script also excludes the source
site from the measurement, so the coincident-point conjugation case is not in
this theorem's scope.

## 2. Exact endpoint-orbit theorem

For every complex `N_c x N_c` matrix `M` and `N_c >= 2`, independent Haar
averaging of the two endpoint frames gives

```text
integral dOmega_x dOmega_y |Tr(Omega_x M Omega_y^dagger)|^2
  = Tr(M M^dagger)/N_c.
```

Since `T` is fixed along the orbit,

```text
<S>_orbit/T = 1/N_c^2,
<C>_orbit/T = (N_c^2 - 1)/N_c^2.                 (1)
```

At `N_c=3`, equation (1) is exactly `8/9`. There is no
`O(1/N_c^4)` dynamical correction on this open-bilocal orbit surface.

### Proof

Set `U = Omega_y^dagger Omega_x`. The product of independent Haar measures
makes `U` Haar distributed. Cyclicity gives

```text
Tr(Omega_x M Omega_y^dagger) = Tr(U M).
```

The fundamental second moment,

```text
integral dU U_ij U^*_{kl} = delta_ik delta_jl/N_c,
```

then contracts the two copies of `M` to `Tr(M M^dagger)/N_c`.

The runner verifies the same identity by an independent deterministic route.
The `N_c^2` shift-clock Weyl matrices form an orthogonal unitary basis, so
Parseval gives

```text
(1/N_c^2) sum_W |Tr(W M)|^2 = Tr(M M^dagger)/N_c
```

for fixed non-normal, non-unitary matrices at `N_c=2,3,4,5`. No Monte Carlo
target is inserted.

### Equilibrium-ensemble corollary

The orbit identity applies to the ideal ensemble targeted by the legacy
lattice calculation under two explicit conditions.

First, gauge covariance of the lattice Dirac operator gives

```text
D[U^Omega] = Omega D[U] Omega^dagger.
```

Inverting this finite matrix identity gives the separated propagator law

```text
G_xy[U^Omega] = Omega_x G_xy[U] Omega_y^dagger.
```

Second, the equilibrium link measure and gauge action are invariant under the
same local transformation. For any set `X` of sites distinct from the source
`y`, define the legacy aggregate

```text
T_X = sum_(x in X) T(G_xy),
S_X = sum_(x in X) S(G_xy),
R_X = 1 - S_X/T_X,       T_X > 0.
```

`T_X` is fixed along every gauge orbit. Applying the endpoint Haar identity to
each term gives

```text
<S_X>_orbit = T_X/N_c^2,
<R_X>_orbit = (N_c^2-1)/N_c^2.                         (2)
```

Gauge invariance of the equilibrium measure lets every ensemble expectation
be replaced by its conditional orbit average. Equation (2) therefore fixes
the ideal equilibrium expectation of the script-defined aggregate and its
per-distance analogues.

This corollary does not say a finite cold-start Markov chain performs an
explicit Haar average, reaches stationarity, or returns equation (2) exactly.
Autocorrelation, incomplete thermalization, solver error, and finite sampling
remain ordinary estimator effects. They change the finite estimate, not the
equilibrium symmetry identity.

## 3. Why the theorem is kinematic

The endpoint group is `SU(N_c)_x x SU(N_c)_y`. Its action on
`Hom(V_y,V_x)` is the outer tensor product of the fundamental representation at
`x` and the dual (conjugate-fundamental) representation at `y`, and is
irreducible under the product group. By Schur's lemma, an endpoint-invariant
positive quadratic kernel is proportional to the identity on the full matrix
space. Equal weight per matrix component, and hence equation (1), follows from
the unfixed endpoint frames.

This is stronger than global color conjugation, but it is not extra dynamics.
Changing the action, coupling, mass, or propagator dressing changes `M` and
`T`; it cannot change the orbit fraction in equation (1).

The ideal equilibrium expectation of the old runner's diagnostic is therefore
an exact gauge-orbit identity. A finite run estimates that expectation. Its
agreement with `8/9` cannot validate a physical matching rule.

## 4. Gauge-invariant closure restores two channel weights

Suppose a parallel transporter or another physical construction identifies the
two endpoints. The resulting matrix `H` transforms by diagonal conjugation,

```text
H -> Omega H Omega^dagger.
```

Now

```text
End(C^N_c) = 1 direct-sum adj
```

is a multiplicity-free decomposition. Every positive Hermitian quadratic
kernel commuting with diagonal conjugation has the form

```text
K = a P_1 + b P_adj,       a >= 0, b >= 0,              (3)
```

where

```text
P_1(H)   = (Tr H/N_c) I,
P_adj(H) = H - P_1(H).
```

Writing `d_adj=N_c^2-1`, the kernel-trace adjoint fraction is

```text
R_adj(a,b) = d_adj b/(a + d_adj b).                     (4)
```

For a nonzero denominator,

```text
R_adj(a,b) = d_adj/(d_adj+1)  if and only if  a=b.      (5)
```

Symmetry and positivity do not impose equation (5). For `N_c=3`, both

```text
K_equal   = P_1 + P_adj       -> R_adj = 8/9,
K_unequal = 2 P_1 + P_adj     -> R_adj = 4/5
```

are strictly positive and diagonal-conjugation equivariant. The runner checks
their positivity, equivariance, and different fractions directly.

## 5. The large-N remainder does not select the finite coefficient

Let `q_N=a_N/b_N`. Equation (4) becomes

```text
R_adj(N) = (N^2-1)/(N^2-1+q_N).
```

For `b_N>0`, take the explicit family

```text
q_N = 1 + c/N^2,
```

with fixed real `c` and `q_N>0` (automatically for all sufficiently large
`N`).

The exact difference from the dimension fraction is

```text
R_adj(N) - (N^2-1)/N^2
  = -c(N^2-1)/[N^2(N^4+c)]
  = O(1/N^4).                                             (6)
```

Every fixed `c` obeys the same `O(1/N^4)` bound, but the finite value changes.
For example, `c=1` gives `R_adj(3)=36/41`, not `8/9`. Thus an
`O(1/N_c^4)` remainder does not specialize to exact `8/9` at `N_c=3`; the
coefficient or the finite equality `q_3=1` still needs a dynamical theorem.

## 6. Three meanings of connected

The old symbol hid three inequivalent uses of `connected`:

1. a connected cumulant, with products of expectation values subtracted;
2. a quark-line-connected or same-fermion-loop current correlator; and
3. the frame-dependent trace/traceless coordinate of an open color matrix
   after choosing an identification `V_x ~= V_y`.

Equation (1) concerns item 3 after endpoint gauge-orbit averaging. The word
`adjoint` applies only after diagonal conjugation supplies a single identified
color fiber; it is not an invariant label for the open product-group object. A
color-blind same-line electroweak current uses the full cyclic color trace and
may contain both Fierz coordinates. Ordinary Wick-disconnected terms are
products of separate fermion-loop traces. Neither topology is defined by
`S(M)=|Tr M|^2/N_c` for a separated open propagator.

The exact `8/9` orbit identity therefore cannot be renamed as item 1 or item 2.
A physical positive derivation would have to define a gauge-invariant current
or readout, compute its channel weights, and show how it matches the continuum
coupling.

## 7. Scope and relation to the current R_conn row

The current `RCONN_DERIVED_NOTE.md` already retires the unconditional physical
`R_conn=8/9` statement and preserves `8/9` only as exact channel-count support.
This note does not edit or reclassify that settled row. It supplies the missing
first-principles equilibrium expectation for the legacy Monte Carlo diagnostic
and sharpens the type boundary between the open-bilocal orbit statistic and a
physical current.

Earlier `EW_KAPPA_SELF_ENERGY_OBJECT_PIN_MC_UNDECIDABLE_NO_GO_NOTE_2026-06-08.md`
states the gauge-orbit reading and checks it stochastically. The new content
here is the exact product-group/diagonal-group classification, the deterministic
finite-unitary-basis certificate, and the exact large-N coefficient family.
Those files are relation context, not load-bearing dependencies of equations
(1)--(6).

## 8. What this note does not claim

- It does not claim the open `S` and `C` pieces are gauge-invariant
  observables.
- It does not identify the orbit fraction with a cumulant- or
  quark-line-connected observable.
- It does not claim that the finite legacy Markov chain is exactly at
  equilibrium or exactly Haar-averaged.
- It does not claim diagonal-conjugation dynamics must have unequal weights;
  it proves only that symmetry and positivity permit them.
- It does not derive `kappa_EW = 0`, `K_EW=9/8`, or an unconditional EW
  normalization.
- It does not exclude a future gauge-invariant adjoint-current or matching
  theorem.
- It does not apply or predict an audit verdict.

## 9. Verification

```bash
python3 scripts/frontier_rconn_endpoint_gauge_frame_dichotomy.py
```

The runner checks projector algebra, ranks, the Fierz/Parseval split, Weyl
unitary-basis orthogonality, the exact endpoint-orbit fraction for
`N_c=2,3,4,5`, positive diagonal-conjugation kernels with equal and unequal
weights, failure of unequal weights under independent endpoint rotations, and
the exact `O(1/N_c^4)` coefficient family.
