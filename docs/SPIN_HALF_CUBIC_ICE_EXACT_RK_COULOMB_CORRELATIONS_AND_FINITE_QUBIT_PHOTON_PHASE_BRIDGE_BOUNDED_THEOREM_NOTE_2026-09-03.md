# Spin-Half Cubic Ice: Exact RK Coulomb Correlations and the Finite-Qubit Photon-Phase Bridge

**Date:** 2026-09-03

**Claim type:** bounded_theorem

**Status authority:** independent audit only. This source changes no audit
verdict, TOE score, axiom, or approved primitive.

**Finite-clock comparison parent:**
[`U1_FINITE_CLOCK_GAUGE_MATTER_AND_CONTROLLED_TAME_MAXWELL_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md`](U1_FINITE_CLOCK_GAUGE_MATTER_AND_CONTROLLED_TAME_MAXWELL_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md)

**Reversible-photon parent:**
[`U1_LOCAL_REVERSIBLE_YEE_LEAPFROG_TICK_BOUNDED_THEOREM_NOTE_2026-09-03.md`](U1_LOCAL_REVERSIBLE_YEE_LEAPFROG_TICK_BOUNDED_THEOREM_NOTE_2026-09-03.md)

**Maxwell-generator parent:**
[`U1_ROLE_COMPILED_YEE_MAXWELL_GENERATOR_AND_TIME_SELECTION_FORK_BOUNDED_THEOREM_NOTE_2026-09-03.md`](U1_ROLE_COMPILED_YEE_MAXWELL_GENERATOR_AND_TIME_SELECTION_FORK_BOUNDED_THEOREM_NOTE_2026-09-03.md)

**Physical-role compiler parent:**
[`U1_ROLE_ENCODED_DOUBLED_INCIDENCE_NEAREST_NEIGHBOR_GAUGE_LAW_BOUNDED_THEOREM_NOTE_2026-09-03.md`](U1_ROLE_ENCODED_DOUBLED_INCIDENCE_NEAREST_NEIGHBOR_GAUGE_LAW_BOUNDED_THEOREM_NOTE_2026-09-03.md)

**Axiom boundary:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

**Runner:**
[`scripts/spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03.py`](../scripts/spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03.py)

**Cached receipt:**
[`logs/runner-cache/spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03.txt`](../logs/runner-cache/spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03.txt)

## Result up front

A microscopic three-dimensional gauge carrier with only one qubit per cubic
link realizes the exact ingredients of the established spin-half Coulomb
phase. This is a positive alternative to taking a large clock order before a
photon can appear.

Put an occupation qubit `n_(r,i)=0,1` on every positive cubic link and impose

```text
sum of the six occupations incident on r = 3.
```

With the bipartite electric field

```text
E_(r,i)=(-1)^(r_x+r_y+r_z) (n_(r,i)-1/2),
```

this is exactly `div E=0`. An alternating four-link square flip preserves the
constraint at all four corners and preserves all three electric fluxes.

The runner establishes the following finite statements.

- An exhaustive enumeration of all `C(24,12)` candidate occupations on the
  `L=2` torus finds `9600` ice configurations across all fluxes. Exactly `880`
  are in the zero-flux sector. Of those, `864` form one connected mobile orbit
  under square flips and `16` are frozen.
- The Rokhsar-Kivelson (RK) Hamiltonian on the complete mobile orbit is the
  exact graph Laplacian. Its equal-amplitude vector has residual below
  `1e-13`; the first positive eigenvalue is `0.969623617` in units of the ring
  coefficient.
- A fixed two-charge orbit contains `508` states. The charges remain at the
  two endpoints with opposite staggered sign, and the equal-amplitude vector
  is an exact zero of the RK ring Hamiltonian. A separate microscopic charge
  penalty is not included in that zero-energy statement.
- Deterministic uniform-RK Monte Carlo on zero-flux tori `L=6,8,10,12`
  remains exactly in the Gauss sector. The longitudinal structure factor at
  the first two axial momenta is zero to floating-point precision, while both
  transverse weights remain finite. The ensemble-level transverse
  polarization splits are respectively `2.37%`, `2.12%`, `3.94%`, and
  `3.73%`. Covariance matrices at axial, face-diagonal, body-diagonal, and
  generic low momenta have one longitudinal null below `2.2e-15`; their
  maximum transverse eigenvalue splits and directional weight spreads stay
  below `8.4%`. An independent `L=12` seed reproduces the sector, density,
  axial split, and off-axis tensor within the stated thresholds.
- The density of flippable plaquettes is size-stable:

```text
L=6       0.262313
L=8       0.260063
L=10      0.259975
L=12      0.259755.
```

  It supplies a positive magnetic stiffness. A variational state carrying one
  threaded flux quantum has positive energy

```text
E_flux(L)=n_f L^3 [1-cos(2 pi/L^2)] ~ 2 pi^2 n_f/L.
```

  The measured ratios of `L E_flux/(2 pi^2 n_f)` run from `0.99746` to
  `0.99984`.

These executed results identify the static transverse projector, nonzero
magnetic stiffness, exact gauge constraint, and local quantum dynamics on a
finite qubit carrier. They do not by themselves establish a linearly
dispersing photon at the RK point: its electric stiffness vanishes and its
generic dynamics has the special RK scaling. The photon-phase bridge uses the
primary model result that an interval immediately on the `delta V<0` side has
positive electric stiffness and a stable three-dimensional `U(1)` Coulomb
phase. Conditional on positive electric and magnetic stiffness, the same
cubic curl kernel has exactly two degenerate transverse modes with

```text
omega(k)^2 = U K 4 sum_i sin^2(k_i/2).
```

Thus the bounded conclusion is:

```text
one qubit per link
    -> exact microscopic Gauss sector and local ring law
    -> exact RK state and finite charged sectors
    -> transverse Coulomb correlations and positive magnetic stiffness
    -> established adjacent stable phase with two linear photon modes.
```

The last arrow is a primary-literature phase bridge, not a new thermodynamic
calculation in this runner. No claim is made that the four framework axioms
select this law, that the coarse links are already compiled into homogeneous
physical sites, or that the emergent photon is empirically the electromagnetic
photon.

## 1. One qubit and exact Gauss law

Let `n_(r,i)` denote the occupation of the link from `r` to `r+e_i`. The local
three-of-six constraint is

```text
sum_i [n_(r,i)+n_(r-e_i,i)] = 3.
```

Because the cubic lattice is bipartite, define the staggered field displayed
above. Its lattice divergence is

```text
sum_i [E_(r,i)-E_(r-e_i,i)]
 =(-1)^(r_x+r_y+r_z)
   {sum_i[n_(r,i)+n_(r-e_i,i)]-3}.
```

The occupation constraint and zero Gauss charge are therefore the same finite
statement. This is not a rotor truncation: each link is exactly a two-state
system throughout the construction.

On a square with alternating occupations, the ring operator exchanges

```text
|1010> <-> |0101>.
```

Exactly two incident links change at each corner, one from occupied to empty
and one from empty to occupied. Every vertex charge is unchanged. Since the
move is a contractible loop, the three electric fluxes through the periodic
torus are unchanged as well. The runner checks these identities on every
tested orientation and volume and during every sampled chain.

## 2. Exact finite RK sector

For each flippable plaquette `p`, define the positive projector

```text
H_p=J (|1010>-|0101>)(<1010|-<0101|).
```

The RK Hamiltonian is `H_RK=sum_p H_p`. On the configuration graph generated
by square flips, its matrix is

```text
H_RK/J = D-A,
```

where `A` is the move graph with geometric multiplicities and `D` is its
degree matrix. It is positive semidefinite, and the equal-amplitude vector on
each connected component is an exact zero.

The `L=2` census does not assume the published state count. It enumerates all
ways to choose the required `12` occupied links among `24`, tests all eight
vertex constraints, computes all three electric fluxes, and constructs every
legal square move. It obtains

```text
all flux sectors       9600
zero-flux sector        880
connected mobile orbit  864
frozen states             16.
```

The complete mobile-orbit Hamiltonian is an `864 x 864` sparse matrix. The
five lowest eigenvalues are

```text
0,
0.969623617, 0.969623617,
1.16086551,  1.16086551,
```

up to the displayed numerical precision. This small-volume gap is not
extrapolated into a thermodynamic mass.

## 3. Static Coulomb tensor on larger tori

At the RK point, equal-time diagonal observables are uniform averages over
the classical ice configurations in the selected connected sector. The
runner uses a fixed-seed checkerboard chain. Within each orientation, the
four plaquette colors share no links, so accepted flips can be applied in
parallel. Every candidate is accepted with probability one half. The forward
and reverse proposal probabilities are equal, giving the uniform measure as
a stationary distribution.

For axial momentum `k`, exact Gauss law requires the longitudinal electric
amplitude to vanish. A Coulomb ensemble has the transverse projector

```text
<E_i(k) E_j(-k)> proportional to
delta_ij - q_i q_j^*/|q|^2,
q_i=exp(i k_i)-1.
```

The sampled axial modes obey that pattern. At `L=6,8,10,12`, the longitudinal
powers are between `2.25e-34` and `1.66e-33`. The averaged first- and
second-momentum transverse weights remain between `0.363` and `0.392`, rather
than collapsing with volume. For each of the three axes, the two transverse
Cartesian powers are ensemble-averaged before their relative split is taken;
averaging a per-configuration absolute split would instead measure ordinary
sample fluctuations and is not the symmetry observable.

The runner also forms the complete complex `3 x 3` covariance at momentum
indices

```text
(1,0,0), (1,1,0), (1,1,1), (2,1,0).
```

These probe an axis, face diagonal, body diagonal, and a generic direction.
At every size each covariance has one lattice-divergence null. Across all
four directions, the largest split of the two transverse eigenvalues is
`8.04%`, and the largest spread of their mean weight is `8.32%`. This tests
the three-dimensional tensor rather than inferring it from axial powers
alone. A second `L=12` chain with an independent seed gives flippability
density `0.260018`, axial split `2.95%`, maximum tensor split `9.47%`, and
directional weight spread `3.54%`.

This is a finite-volume static Coulomb diagnostic. It corresponds to dipolar
power-law correlations in real space, but the runner does not fit a real-space
exponent or assert a thermodynamic limit from four sizes.

## 4. Charged sectors at the soluble point

Flipping one link in the checkerboard configuration changes the two endpoint
degrees from `3` to `4`. The endpoints lie on opposite cubic sublattices, so
their staggered Gauss charges are opposite. Plaquette flips conserve every
vertex degree and therefore cannot move or create the fixed charges.

The runner exhausts the connected `L=2` orbit from this configuration. It has
`508` states with the same charge signature and an exact equal-amplitude zero
of the RK ring Hamiltonian. This verifies that one fixed-charge sector carries
the same RK projector zero. The graph-Laplacian argument applies separately
to every connected fixed-charge sector, but this finite calculation does not
compare different charge separations. The underlying easy-axis spin model may
assign a nonzero local creation energy to each charge; that separate term is
not part of `H_RK`.

The runner does not claim to resolve the first-order `1/R` spinon potential
away from the RK point. The primary calculation used much longer chains and a
special separation-versus-volume geometry. A short fixed-volume path scan is
not precise enough to reproduce that coefficient and is not treated as
negative evidence.

## 5. Positive magnetic stiffness

Let `n_f` be the orientation-averaged probability that a plaquette is
flippable in the uniform RK ensemble. Average over the three states obtained
by threading one magnetic flux quantum along each cubic direction. Direct
evaluation of the plaquette projectors gives

```text
E_flux(L)=J n_f L^3 [1-cos(2 pi/L^2)].
```

The positive measured `n_f` values above give

```text
E_flux(L)=2 pi^2 J n_f/L + O(L^-5).
```

This is the expected finite-volume magnetic-flux energy and identifies a
nonzero magnetic stiffness. The measured density converges near `0.260`,
independently matching the value reported for this cubic model.

At the exact RK point, the electric stiffness `U` is zero. Moving to the
adjacent side selected by `delta V=V-J<0` produces the generic quadratic
effective Hamiltonian

```text
H_eff=(U/2) sum E^2 + (K/2) sum (curl A)^2 + corrections.
```

The primary source establishes positive `U` there from the static-charge
response and argues stability of the resulting three-dimensional compact
`U(1)` Coulomb phase. The present runner independently establishes the
microscopic carrier, the RK sector data, the Coulomb tensor, and positive
magnetic stiffness; it imports rather than repeats that long-run phase
determination.

## 6. Conditional photon mode count

For the cubic forward-difference symbol `q_i=exp(i k_i)-1`, the curl kernel
has eigenvalues

```text
0, |q|^2, |q|^2,
|q|^2=4 sum_i sin^2(k_i/2).
```

The null vector is the Gauss direction. If `U>0` and `K>0`, Hamilton's
equations give two physical frequencies

```text
omega(k)=sqrt(U K) |q(k)|
        =sqrt(U K) |k| + O(|k|^3).
```

The runner checks the eigenvalue multiplicity at every nonzero momentum on
`L=4,6,8,12`. Along the first axial momentum, `omega/|k|` increases toward one
on `L=8,16,32,64,128`, reaching above `0.9998`. This mode count is exact for
the quadratic effective kernel. It is not presented as a direct
diagonalization of the interacting spin-half Hamiltonian.

## 7. Program consequence and remaining work

The previous finite-clock bridge showed that a finite `q`-qubit register can
approach a Maxwell tangent as its clock order grows. This source answers a
different and more severe question: fixed local dimension two is compatible
with a stable three-dimensional photon phase. A large on-link clock is not a
necessary condition for emergent light.

That is meaningful progress for the light lane because it removes local
Hilbert-space size as the obvious obstruction. It also explains why a
spin-half ring with only one effective spatial direction can be gapped without
speaking against the three-dimensional carrier: the cubic model has three
plaquette orientations and two transverse directions.

The next high-value direct test is the microscopic dynamical phase, not
another small algebraic block. A sign-free quantum Monte Carlo calculation,
controlled duality bound, or finite-size gauge-reduced spectrum should test
`delta V<0` for volume-stable linear transverse gaps and charge `1/R`
response. That would replace the primary-literature bridge with a repo-native
thermodynamic calculation.

Separate program obligations remain:

- compile coarse link qubits and four-link ring terms into the homogeneous
  nearest-neighbor physical-site law;
- couple the spin-half charge defects to the program's matter carrier and
  close local energy/current exchange on the same model;
- determine whether Admissibility selects this supplied law or only permits
  it; and
- identify and normalize the emergent `U(1)` field as physical
  electromagnetism rather than merely a photon-like gauge sector.

No axiom edit follows from this result. The cubic roles, three-of-six
constraint, RK coupling, perturbation direction, and physical identification
are all supplied. Admissibility does not choose a Hamiltonian, and Record is
untouched.

## 8. Prior-art and contribution boundary

The microscopic model, its RK point, and the adjacent stable `U(1)` spin
liquid are due to M. Hermele, M. P. A. Fisher, and L. Balents,
[“Pyrochlore Photons: The U(1) Spin Liquid in a S=1/2 Three-Dimensional
Frustrated Magnet”](https://arxiv.org/abs/cond-mat/0305401) (2004). That source
states the three-dimer cubic model, square ring exchange, exact RK ground
state, `864+16` zero-flux census, dipolar correlations, positive magnetic
stiffness, first-order spinon Coulomb potential, and stable adjacent phase.

The repo-specific contribution is not invention of quantum spin ice. It is
the executable junction to the current framework and light stack: an
independent full `L=2` flux-resolved enumeration, exact neutral and charged RK
matrices, deterministic larger-volume Gauss and transverse-tensor checks,
measured flippability and flux-stiffness ladders, and an explicit separation
between what the runner establishes, what the primary phase result supplies,
and what the framework axioms do not select.

Open PR #7911 studies a spin-half ring without three-dimensional transverse
geometry; it is context only and no result is imported. The finite-clock
parent provides a different regulator and a controlled tangent, not this
fixed-dimension phase result.

## 9. Executable evidence

The runner reports `TOTAL: PASS=14 FAIL=0`. It checks:

- one-qubit link variables and the exact three-of-six/Gauss identity;
- local square-flip constraint and electric-flux preservation;
- all `9600` `L=2` ice states, all flux sectors, the `880` zero-flux states,
  and the `864+16` mobile/frozen decomposition;
- positivity, equal-amplitude zero, and low spectrum of the exact mobile RK
  matrix;
- exact Gauss and zero-flux preservation in every Monte Carlo chain;
- longitudinal pinch suppression and ensemble-level transverse degeneracy;
- off-axis rank-two covariance and low-momentum directional isotropy;
- independent-seed reproduction at `L=12`;
- finite transverse weights at the first two axial momenta;
- an exact `508`-state fixed opposite-charge RK orbit;
- the positive size-stable flippability density;
- positive threaded-flux energy and its `1/L` scaling; and
- the conditional two-polarization cubic Maxwell kernel.

## No-Go Discipline Gate

This is a positive finite-qubit bridge with explicitly bounded phase,
compiler, matter, and identification statements. The gate prevents the
unexecuted microscopic thermodynamic calculation from being restated as a
global obstruction or as a completed derivation.

### N1 — Alternative route enumeration

| Honesty | Route family | Outcome |
|---|---|---|
| **ATTEMPTED** | spin-half cubic Gauss and square-ring algebra | **Positive:** exact with one qubit per link. |
| **ATTEMPTED** | exhaustive `L=2` all-flux and zero-flux enumeration | **Positive:** `9600`, `880`, and `864+16` are independently recovered. |
| **ATTEMPTED** | exact neutral and fixed-charge RK graph Hamiltonians | **Positive:** both have the predicted equal-amplitude zero on their connected orbit. |
| **ATTEMPTED** | larger-torus static transverse tensor | **Positive in scope:** four sizes retain the Gauss projector, off-axis rank-two covariance, and finite transverse weight. |
| **ATTEMPTED** | measured magnetic flux stiffness | **Positive:** `n_f` is size-stable and `E_flux` has the variational `1/L` scaling. |
| **IMPORTED** | adjacent spin-half `U(1)` Coulomb phase | **Positive primary result:** supplies positive electric stiffness and phase stability. |
| **ATTEMPTED** | finite-clock tame-Maxwell route | Parent establishes the exact finite carrier and tangent but not its full many-link phase. |
| **OPEN** | repo-native sign-free dynamical phase calculation | Would directly test the volume-stable `z=1` spectrum and `1/R` charge response. |
| **OPEN** | homogeneous physical-site compiler | Would realize link roles, constraints, and ring terms from one covariant nearest-neighbor rule. |
| **OPEN** | spin-half matter coupling | Would join mobile charged defects and field energy on this same carrier. |

The route families differ in microscopic carrier, observable, or terminal
obligation. A small ring spectrum and a three-dimensional phase calculation
are not treated as repeated versions of one test.

### N2 — Wall-independence and collapse audit

The direct `1/R` charge test, positive electric stiffness, and volume-stable
linear spectrum are diagnostics of one microscopic phase obligation. They are
collapsed into `W1`, not counted as three independent blockers.

```text
W1 = repo-native thermodynamic and dynamical confirmation of the phase,
W2 = homogeneous nearest-neighbor physical-site compiler,
W3 = mobile matter and exact backreaction on the same spin-half carrier,
W4 = Admissibility selection and empirical electromagnetic identification.
```

| Pair | Does either automatically close the other? | Independent? |
|---|---:|---:|
| W1, W2 | no | yes |
| W1, W3 | no | yes |
| W1, W4 | no | yes |
| W2, W3 | no | yes |
| W2, W4 | no | yes |
| W3, W4 | no | yes |

No impossibility is inferred from this wall set.

### N3 — Hidden-condition scan

The cubic link graph, bipartite staggering, three-of-six sector, square-ring
law, RK tuning, zero-flux sector, fixed Monte Carlo seeds, four finite sizes,
and conditional positive-stiffness kernel are explicit. The exact `L=2`
orbit does not imply a thermodynamic gap. The uniform classical chain samples
equal-time RK observables, not generic real-time dynamics. Sector ergodicity
is established exhaustively only at `L=2`. The adjacent phase result is cited
as an external primary input rather than embedded as runner output. The
physical-site compiler and law selection are not assumed.

### N4 — Residual matching

| Surface | Exact residual there | Match here |
|---|---|---|
| spin-half ring PR #7911 | no three-dimensional transverse geometry | **geometry-specific resolution:** three square orientations are present here |
| finite-clock parent | exact finite carrier but thermodynamic clock phase open | **alternative carrier:** fixed dimension two with primary-established phase |
| Maxwell-generator parent | supplied noncompact quadratic generator | **infrared match:** same cubic curl eigenvalues once `U,K>0` |
| reversible-tick parent | exact finite-depth update of field amplitudes | **different obligation:** no microscopic spin-half compiler for that tick |
| physical-role compiler parent | collective edge/face roles on physical sites | **partial match:** role route exists, but the ice constraint and ring term are not compiled here |

The one-direction ring result is not cited against the cubic model, and the
primary phase result is not mislabeled as a new first-principles derivation.

### N5 — Rhetoric and resolution audit

“Finite-qubit photon-phase bridge” means exact one-qubit microscopic
ingredients plus a cited, established phase of that same model. It does not
mean that this runner directly computes the thermodynamic photon. “Coulomb
correlations” refers to the finite-volume transverse tensor protocol stated
above. “Zero-energy charged orbit” is restricted to the RK ring Hamiltonian
and does not erase local spinon creation energy.

The cached runner contains the five-resolution execution certificate:

```text
per_element: one occupation qubit per link and every four-link alternating plaquette move are checked
per_site: exact three-of-six Gauss constraints and a fixed opposite-charge sector are checked
per_mode: longitudinal pinch suppression, transverse weights, and conditional Maxwell polarizations are checked
per_block: the complete 864-state L=2 RK orbit and L=6 through L=12 Monte Carlo tori are checked
lattice_wide: finite-volume Coulomb correlations and flux stiffness are resolved; a thermodynamic phase proof is not executed
```

### N6 — Partial-closure paths and primitive boundary

No new axiom or approved primitive is required or proposed. `W1` is an
ordinary supplied-model calculation accessible to sign-free quantum Monte
Carlo, duality bounds, or gauge-reduced spectra. `W2` is a local compiler
problem. `W3` can reuse the charge/current accounting of the gauge-matter
parents but must be built on this carrier. `W4` is the remaining selection and
physical-identification question. The four axioms permit this supplied model;
they do not derive its Hamiltonian or couplings.

### N7 — Steelman

A hostile reviewer should reject any claim that the four finite Monte Carlo
sizes prove the stable `z=1` phase. Static RK correlations do not measure the
generic real-time spectrum, and the exact RK point has vanishing electric
stiffness. That objection is correct. The positive phase statement here rests
on the cited primary calculation for the same microscopic model; a repo-native
repeat remains `W1`.

The reviewer should also note that this is a known condensed-matter
construction and that link qubits are not yet homogeneous physical lattice
sites. Both points are correct and stated. The new program value is the
finite-payload compatibility result and its executable junction to the light
stack, not priority for quantum spin ice.

### N8 — Cross-cycle echo

The earlier spin-half ring cycle found a gap because it had no transverse
geometry. This cycle does not repeat that setup with a larger matrix; it adds
the full cubic constraint, all three plaquette orientations, topological flux
sectors, and larger-volume Coulomb observables. The finite-clock cycle reached
a controlled tangent by increasing local payload. This cycle changes the
route by holding the payload to one qubit and using an emergent constrained
phase. Neither result is promoted into axiom selection or empirical
electromagnetism.

**Gate result:** PASS. Seven distinct executed or imported route families are
separated, three direct routes remain open, dependent phase diagnostics are
collapsed into one wall, and no global no-go or thermodynamic overclaim is
shipped.

## Falsifiers

The bounded theorem fails if any of the following occurs:

- the three-of-six constraint differs from staggered lattice Gauss law;
- any alternating square flip changes a vertex charge or electric flux;
- the exhaustive `L=2` all-flux, zero-flux, mobile, or frozen counts differ;
- the mobile RK matrix is not positive or its equal vector is not a zero;
- the sampled chains leave their exact Gauss or zero-flux sector;
- longitudinal axial power is nonzero, off-axis covariance loses its
  longitudinal null, or transverse weights collapse over the stated sizes;
- the fixed-charge orbit changes its charge signature or lacks its RK zero;
- the flippability density is not positive and size-stable in the stated
  protocol;
- the threaded-flux energy is nonpositive or fails the displayed `1/L`
  variational scaling; or
- the positive-stiffness cubic curl kernel fails to have exactly two equal
  transverse branches at any tested nonzero momentum.

## Verification

Run:

```text
python3 scripts/spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03.py
```

Expected final line:

```text
TOTAL: PASS=14 FAIL=0
```
