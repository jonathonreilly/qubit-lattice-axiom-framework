# Spin-Half Cubic Ice Retains Maxwell Electric-Flux Stiffness at Two Finite Detunings

**Date:** 2026-09-03

**Claim type:** bounded_theorem

**Status authority:** independent audit only. This source changes no audit
verdict, TOE score, axiom, or approved primitive.

**Direct first-order parent:**
[`SPIN_HALF_CUBIC_ICE_POSITIVE_TOPOLOGICAL_ELECTRIC_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-03.md`](SPIN_HALF_CUBIC_ICE_POSITIVE_TOPOLOGICAL_ELECTRIC_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-03.md)

**Finite-qubit photon parent:**
[`SPIN_HALF_CUBIC_ICE_EXACT_RK_COULOMB_CORRELATIONS_AND_FINITE_QUBIT_PHOTON_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md`](SPIN_HALF_CUBIC_ICE_EXACT_RK_COULOMB_CORRELATIONS_AND_FINITE_QUBIT_PHOTON_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md)

**Physical-role compiler boundary:**
[`U1_ROLE_ENCODED_DOUBLED_INCIDENCE_NEAREST_NEIGHBOR_GAUGE_LAW_BOUNDED_THEOREM_NOTE_2026-09-03.md`](U1_ROLE_ENCODED_DOUBLED_INCIDENCE_NEAREST_NEIGHBOR_GAUGE_LAW_BOUNDED_THEOREM_NOTE_2026-09-03.md)

**Axiom boundary:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

**Runner:**
[`scripts/spin_half_cubic_ice_finite_delta_projector_stiffness_2026_09_03.py`](../scripts/spin_half_cubic_ice_finite_delta_projector_stiffness_2026_09_03.py)

**Cached receipt:**
[`logs/runner-cache/spin_half_cubic_ice_finite_delta_projector_stiffness_2026_09_03.txt`](../logs/runner-cache/spin_half_cubic_ice_finite_delta_projector_stiffness_2026_09_03.txt)

## Result up front

The one-qubit cubic-ice Hamiltonian retains a positive Maxwell-scaled electric
flux cost at two finite distances from its Rokhsar-Kivelson (RK) point. This is
a finite-population, finite-imaginary-time projector result on the mobile
components reached by the declared starts; it is not a thermodynamic-limit or
real-time-spectrum theorem.

Set the ring amplitude to one and write

```text
H(V)=-sum_p (|clockwise><counterclockwise|+h.c.)+V N_f,
delta V=V-1.
```

Every basis state has exactly three occupied links at every cubic vertex.
`N_f` counts alternating square plaquettes. The calculation projects the
lowest positive-amplitude state in fixed electric-flux components at

```text
V=0.95 and V=0.90.
```

All integer flux magnitudes `Phi=0,...,L/2` are calculated on `L=4,6,8`.
The `Phi=0,L/2` endpoints are also calculated on `L=10`. Fitting

```text
E_L(Phi)-E_L(0)=(U_L/2) Phi^2/L
```

gives the controlled volume ladder

| `V` | `U_4` | `U_6` | `U_8` | `U_10` | mean `U/|delta V|` |
|---:|---:|---:|---:|---:|---:|
| 0.95 | 0.162431 | 0.158859 | 0.161363 | 0.167899 | 3.252761 |
| 0.90 | 0.323246 | 0.316443 | 0.321798 | 0.322970 | 3.211140 |

The `L=8` values in this table use the doubled-population, nonlocal-start
control. The corresponding `256`-walker full curves agree within the declared
`15%` population threshold. The relative spread over `L=4,6,8,10` is about
`5.6%` at `V=0.95` and `2.1%` at `V=0.90`.

The direct parent obtained at first order

```text
U/|delta V|=3.183873 +/- 0.154786.
```

The two finite-detuning means differ from its central value by only about
`2.2%` and `0.9%`. No perturbation series is used in the finite-detuning
projection: within each finite graph, all powers of `delta V` enter the
ground-state eigenvector.

The joint flux-and-volume fit strongly favors `Phi^2/L`. Its residual sums of
squares are

```text
V=0.95: 0.00014972,
V=0.90: 0.00007401.
```

At both detunings the runner requires this to be less than `20%` of the best
among four controls: linear in `|Phi|`, linear in `|Phi|/L`, unscaled
`Phi^2`, and a nonzero-sector step. Separately on each complete `L=4,6,8`
ladder, the quadratic law beats the linear-flux fit.

This is direct positive movement on the finite-qubit photon-phase seam. The
electric coefficient neither exists only as a derivative at the RK point nor
collapses immediately at finite detuning. It remains bounded because the
calculation does not establish the infinite-volume ground state, a finite
interval of `V`, the magnetic stiffness at the same detunings, or a linear
real-time photon pole.

## 1. Exact positive projector

On an `L^3` torus there are

```text
M=3 L^3
```

square-plaquette roots. Inside a fixed mobile component, the RK Hamiltonian is
the graph Laplacian

```text
H_RK=D-A,
```

where `D_CC=N_f(C)` and `A` counts square flips. Therefore

```text
H(V)=H_RK+delta V N_f.
```

For `0<=V<=1`, define

```text
G=I-H(V)/M.
```

Its off-diagonal entry for each allowed square flip is `1/M`, and its diagonal
entry is

```text
1-V N_f(C)/M >= 1-V >= 0.
```

Thus `G` is entrywise nonnegative at both tested detunings and has the same
eigenvectors as `H`. On each connected component, its Perron vector is the
lowest-energy positive-amplitude eigenvector of `H`.

The column sum at configuration `C` is

```text
b(C)=1-delta V N_f(C)/M.
```

One exact importance-sampled step with constant trial state is:

1. multiply the walker weight by `b(C)`;
2. choose one of the `M` plaquettes uniformly;
3. if it is flippable, execute the flip with probability `1/b(C)`;
4. otherwise remain in `C`.

The flip probability for each allowed destination is exactly `1/(M b(C))`.
The remaining probability is the normalized diagonal of `G`. Fixed-population
systematic resampling is performed after a declared number of these exact
steps; the approximation is in the finite walker population and projection
time, not in a Trotterized Hamiltonian.

## 2. Mixed estimator

For the constant trial state, the row sum of the Hamiltonian is

```text
E_local(C)=V N_f(C)-N_f(C)=delta V N_f(C).
```

If `psi_0` is the positive ground vector in the component, symmetry of `H`
gives

```text
E_0
 = <1|H|psi_0>/<1|psi_0>
 = delta V sum_C N_f(C) psi_0(C) / sum_C psi_0(C).
```

The projector population samples the last ratio. The reported energy is
therefore the mixed estimator

```text
E_0=delta V <N_f>_mixed.
```

This identity is independently checked on the complete `L=2` component
graphs. Exact sparse diagonalization gives

| `V` | `Phi` | exact `E_0` |
|---:|---:|---:|
| 0.95 | 0 | -0.402736506 |
| 0.95 | 1 | -0.328353309 |
| 0.90 | 0 | -0.810822412 |
| 0.90 | 1 | -0.664101443 |

For each row, direct eigenvector evaluation of the mixed estimator agrees to
`1e-9`, and a `2048`-walker projector independently reproduces the exact
energy inside its declared stochastic tolerance.

## 3. Finite-volume protocol

The primary `L=4,6,8` populations use:

```text
walkers                 256
uniform-RK warmup       100 attempted sweeps
projector burn          150 attempted sweeps
projector samples       300, one per attempted sweep
```

One attempted sweep means `M` exact single-plaquette Green-function steps per
walker. Ten time blocks supply the displayed internal sampling errors.

The `L=10` endpoint populations use the same counts. The population control
at `L=8` uses:

```text
walkers                 512
uniform-RK warmup       150 attempted sweeps
projector burn          250 attempted sweeps
projector samples       500
```

It also changes the initialization. Instead of beginning only from the
checkerboard ice state, it flips two oppositely oriented noncontractible lines
whose net electric flux is zero, then adds the requested net-flux lines. This
is a nonlocal start relative to the elementary square moves. Agreement does
not prove that all disconnected mobile components have been found, but it is
a direct initialization/component sensitivity control.

Every population ends with exact three-of-six vertex degree and exact assigned
electric flux for every walker. Incrementally maintained `N_f` is recomputed
from scratch on the final population. The minimum resampling effective
population stays above `90%` of nominal, and at least `25%` of the final
walkers remain distinct at every `L>=4` run. These thresholds guard against a
numerically positive answer produced by immediate population collapse.

The largest inserted flux is `Phi=L/2`; hence the field density obeys

```text
Phi/L^2 <= 1/(2L).
```

The endpoint sequence is therefore a shrinking-field-density rather than a
fixed strong-field test.

## 4. What the scaling discriminates

For a Maxwell electric term

```text
H_E=(U/2) sum_links E^2,
```

a uniform topological flux `Phi` spreads over an `L^2` cross-section. Its
energy is

```text
(U/2) L^3 (Phi/L^2)^2 = U Phi^2/(2L).
```

That is the observed joint dependence on both flux and volume. A linear flux
cost would indicate a different string-like response. An unscaled `Phi^2`
cost would fail the volume normalization. A step would say only that sectors
differ, not that they carry a stiffness. The fit compares all five using one
through-origin coefficient per detuning.

The primary `L=4,6,8` curves also allow the flux shape to be tested before
combining volumes. Every fitted `U_L` is positive by more than six reported
internal standard errors, and every quadratic residual is below one quarter
of its same-volume linear control.

The result is nonperturbative in the limited but important sense that `V=0.95`
and `V=0.90` are diagonalized by power projection, not evaluated by truncating
the derivative at `V=1`. It is not nonperturbative in the stronger sense of a
rigorous infinite-volume construction.

## 5. Program consequence

The finite-qubit light chain now contains, on the same microscopic carrier:

```text
one occupation qubit per cubic link
 -> exact three-of-six Gauss sector
 -> local four-qubit square-ring Hamiltonian
 -> RK Coulomb correlations and positive magnetic response
 -> positive first-order electric stiffness
 -> positive finite-detuning Phi^2/L electric stiffness.
```

The last arrow is new here. It removes the specific concern that the electric
coefficient could be a derivative-only artifact that disappears as soon as
one leaves the RK point.

It does not close the whole photon phase. The next direct physics target is a
finite-detuning dynamical observable: an imaginary-time transverse correlator
whose lowest pole scales linearly with lattice momentum, or an independently
resolved static-charge `1/R` potential. Those diagnose the same remaining
phase wall and should not be counted as separate TOE obligations.

The physical-site compiler remains independent. The role compiler realizes
edge/face incidence with one neighbor-conditioned law, but this source does
not compile the ice constraint and ring Hamiltonian into an orthogonal
one-qubit-per-physical-site composite. Admissibility selection and the
empirical electromagnetic dictionary also remain open.

No axiom change is proposed. The Hamiltonian, detunings, component starts, and
projection rule are supplied model content. The current Admissibility axiom
does not select them.

## 6. Prior-art and contribution boundary

The spin-half cubic model, RK point, dual Maxwell description, first-order
spinon potential, and stable adjacent `U(1)` phase are due to M. Hermele,
M. P. A. Fisher, and L. Balents,
[“Pyrochlore Photons: The U(1) Spin Liquid in a S=1/2 Three-Dimensional
Frustrated Magnet”](https://arxiv.org/abs/cond-mat/0305401) (2004).

This source makes no priority claim for the model, projector methods, or the
phase. Its repo-specific contribution is the independently executable finite
protocol: the exact positive Green function, four exact small-graph controls,
all-flux ladders at three volumes, `L=10` shrinking-density endpoints, two
finite detunings, nonlocal-start and doubled-population controls, and the
five-way joint scaling comparison.

## 7. Executable evidence

The runner reports `TOTAL: PASS=12 FAIL=0`. It checks:

- exactly `3L^3` four-link square moves on `L=2,4,6,8,10`;
- three neutral noncontractible line-pair start controls;
- the exact constant-trial mixed-estimator identity in four `L=2` cases;
- projector agreement with all four exact `L=2` ground energies;
- exact Gauss charge, assigned flux, and flippability accounting in every
  final walker;
- effective-population and distinct-final-state collapse controls;
- resolved positive stiffness on each complete `L=4,6,8` flux ladder;
- same-volume preference for quadratic over linear flux dependence;
- positive shrinking-density `L=10` endpoints;
- doubled-population, nonlocal-start agreement at `L=8`;
- joint preference for `Phi^2/L` over four named controls; and
- volume stability and agreement with the independent first-order
  coefficient.

## No-Go Discipline Gate

This positive result leaves a deliberately bounded phase statement. The gate
below prevents finite projector evidence from being promoted into a
thermodynamic theorem or its remaining diagnostics from being multiplied into
separate walls.

### N1 — Alternative route enumeration

| Route | Outcome |
|---|---|
| exact finite graph | **Positive control:** four `L=2` energies and mixed estimators agree exactly. |
| first-order topological response | **Positive parent:** supplies `U/|delta V|=3.183873(154786)` at the RK boundary. |
| finite-detuning positive projector | **Positive here:** two detunings and four volumes retain `Phi^2/L`. |
| nonlocal start and population doubling | **Positive control:** `L=8` endpoint stiffness agrees within `15%`. |
| static-charge potential | **Open direct diagnostic:** tests `1/R` at finite detuning. |
| imaginary-time transverse spectrum | **Open direct diagnostic:** tests the linear photon pole. |
| controlled duality/stability analysis | **Imported primary route:** supplies the adjacent stable phase, not new runner output. |
| orthogonal physical-site compiler | **Open independent route:** compiles the coarse carrier into physical sites. |

The static-charge and spectrum calculations are alternate diagnostics of one
phase obligation, not independent reasons to discount the positive result.

### N2 — Wall-independence and collapse audit

After this calculation the live walls are

```text
W1 = thermodynamic and dynamical completion of the finite-detuning phase,
W2 = homogeneous nearest-neighbor physical-site compiler,
W3 = mobile matter and exact backreaction on the spin-half carrier,
W4 = Admissibility selection and empirical electromagnetic identification.
```

`W1` contains the real-time pole, finite-volume-to-infinite-volume control,
finite-detuning magnetic response, and static-charge potential. These are
coupled phase diagnostics and are collapsed into one wall. `W2` does not prove
phase stability. `W3` does not select the law. `W4` does not supply the
microscopic spectrum. None automatically closes another.

### N3 — Hidden-condition scan

The cubic link graph, periodic even volumes, three-of-six sector, ring
amplitude, two values of `V`, fixed mobile-component starts, flux range,
walker counts, warmup, burn, sampling length, resampling rule, seeds, and fit
models are supplied explicitly. The calculation assumes neither that local
square moves connect every ice state nor that the sampled component is the
global minimum among all mobile components. Internal block errors are not a
rigorous population-control or autocorrelation theorem.

The physical lattice law does not follow from the projector. Record formation,
measurement, electromagnetic calibration, and a continuum limit are absent.

### N4 — Residual matching

| Surface | Residual there | Match here |
|---|---|---|
| first-order parent | finite-detuning persistence unexecuted | **direct partial resolution:** two finite detunings retain the coefficient and scaling |
| finite-qubit parent | stable phase imported, direct dynamics open | **strengthened but not closed:** finite-detuning electric tower is computed |
| primary spin-liquid result | stable adjacent phase and universal description | **independent bounded numerical match:** no replacement of its thermodynamic argument |
| role compiler | edge/face incidence but no ice-ring orthogonal composite | **unmatched:** no compiler claim here |
| minimal axioms | dynamics and law values not selected | **unmatched:** supplied Hamiltonian remains supplied |

The theorem survives if either open-PR parent loses status: its formulas and
runner inputs are explicit on this stack. Their status is not imported as an
audit premise.

### N5 — Rhetoric and resolution audit

“Retains stiffness” means the displayed positive `Phi^2/L` coefficient in the
declared finite projector protocol. “Finite detuning” means exactly `V=0.95`
and `V=0.90`, not an interval. “Nonperturbative” refers only to projection of
the complete finite Hamiltonian rather than truncation in `delta V`.
“Maxwell” names the discriminating topological energy law, not an empirical
identification with laboratory electromagnetism.

The five-resolution certificate says:

```text
per_element: every accepted square flip is checked;
per_site: every final walker preserves Gauss charge;
per_mode: the electric topological-flux tower is fitted;
per_block: exact L=2 and projector L=4,6,8,10 are combined;
lattice_wide: finite-volume stiffness is resolved, a thermodynamic phase is not.
```

### N6 — Partial-closure paths and primitive boundary

No axiom or approved primitive is added. Positive continuations are:

- measure the lowest imaginary-time transverse pole across `L` at finite
  detuning;
- measure the finite-detuning charge potential with source separation and
  volume controls;
- add a finite-detuning magnetic twist response on the same projector;
- sample additional nonlocal starts and larger populations/volumes; or
- build the orthogonal spatial composite for the ice constraint and ring
  term.

The kinetic-isotropy primitive does not select this Hamiltonian, its detuning,
or its time interpretation.

### N7 — Steelman

A hostile reviewer can correctly object that fixed-population stochastic
reconfiguration has population bias, finite projection time, and unproved
autocorrelation control. They can also object that one family of mobile starts
does not classify every disconnected ice component. These objections prevent
a thermodynamic phase theorem.

They do not erase the four exact small-graph controls, the positive coefficient
on every full finite ladder, the shrinking-field endpoint at `L=10`, or the
agreement under a doubled population and nonlocal initialization. The proper
claim is the bounded finite-detuning stiffness result, not either full phase
closure or no progress.

### N8 — Cross-cycle echo

The direct parent measured the first derivative of the topological energy at
the RK point and named finite detuning as the next shortest physics test. This
source executes that test with a different method and two nonzero detunings.
The older finite-clock route supplies another microscopic carrier but not this
spin-half many-body projection. The physical-role compiler names the separate
site-realization wall and is not silently reused as a phase theorem.

**Gate result:** PASS. Eight route families are separated, dependent phase
diagnostics are collapsed, the finite-population and component boundaries are
explicit, and the positive finite-detuning result is preserved without a
thermodynamic or empirical overclaim.

## Falsifiers

The bounded theorem fails if any of the following occurs:

- `G=I-H/M` has a negative entry at either tested `V`;
- the sampled transition probabilities differ from normalized columns of
  `G`;
- the constant-trial mixed estimator differs from exact diagonalization on
  `L=2`;
- any local update changes a vertex charge or assigned electric flux;
- incrementally maintained and recomputed `N_f` disagree;
- any complete `L=4,6,8` curve has unresolved or nonpositive `U_L`;
- the quadratic curve fails the declared same-volume linear control;
- either `L=10` endpoint loses positive stiffness;
- the doubled-population/nonlocal-start `L=8` result disagrees beyond `15%`;
- `Phi^2/L` fails the declared joint model comparison;
- the volume spread or first-order comparison exceeds `20%`; or
- effective population or final-state diversity crosses its collapse bound.

## Verification

Run:

```text
PYTHONPATH=scripts python3 scripts/spin_half_cubic_ice_finite_delta_projector_stiffness_2026_09_03.py
```

Expected final line:

```text
TOTAL: PASS=12 FAIL=0
```
