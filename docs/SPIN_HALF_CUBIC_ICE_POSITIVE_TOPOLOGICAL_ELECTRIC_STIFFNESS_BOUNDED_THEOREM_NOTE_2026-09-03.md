# Spin-Half Cubic Ice Has Positive Finite-Volume Topological Electric Stiffness at First Order

**Date:** 2026-09-03

**Claim type:** bounded_theorem

**Status authority:** independent audit only. This source changes no audit
verdict, TOE score, axiom, or approved primitive.

**Direct finite-qubit parent:**
[`SPIN_HALF_CUBIC_ICE_EXACT_RK_COULOMB_CORRELATIONS_AND_FINITE_QUBIT_PHOTON_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md`](SPIN_HALF_CUBIC_ICE_EXACT_RK_COULOMB_CORRELATIONS_AND_FINITE_QUBIT_PHOTON_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md)

**Maxwell-generator parent:**
[`U1_ROLE_COMPILED_YEE_MAXWELL_GENERATOR_AND_TIME_SELECTION_FORK_BOUNDED_THEOREM_NOTE_2026-09-03.md`](U1_ROLE_COMPILED_YEE_MAXWELL_GENERATOR_AND_TIME_SELECTION_FORK_BOUNDED_THEOREM_NOTE_2026-09-03.md)

**Axiom boundary:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

**Runner:**
[`scripts/spin_half_cubic_ice_topological_electric_stiffness_2026_09_03.py`](../scripts/spin_half_cubic_ice_topological_electric_stiffness_2026_09_03.py)

**Helper runner:**
[`scripts/spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03.py`](../scripts/spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03.py)

**Cached receipt:**
[`logs/runner-cache/spin_half_cubic_ice_topological_electric_stiffness_2026_09_03.txt`](../logs/runner-cache/spin_half_cubic_ice_topological_electric_stiffness_2026_09_03.txt)

## Result up front

The one-qubit cubic-ice carrier has a positive electric stiffness on the
`delta V<0` side of its Rokhsar-Kivelson (RK) point at first order, in the
tested finite-volume and shrinking-field-density limit.

Write the microscopic Hamiltonian near the soluble point as

```text
H(V)=H_RK + delta V N_f,
delta V=V-J,
```

where `N_f` counts flippable square plaquettes. In a fixed electric-flux
sector, first-order perturbation theory gives

```text
delta E(Phi)=delta V <N_f>_Phi.
```

For `delta V<0`, a sector with fewer flippable plaquettes lies higher. The
runner establishes that ordering in two complementary ways.

First, it exhausts all `9600` three-of-six configurations on the `L=2` torus,
constructs the complete reversible square-move graph, and finds `937`
connected components. The `864`-state zero-flux component is uniquely the
most flippable, with

```text
<N_f>_0=8.
```

All six signed unit-flux components are exactly cubic- and
inversion-degenerate. Each contains `464` states and has

```text
<N_f>_|Phi|=1 = 188/29,
<N_f>_0-<N_f>_|Phi|=1 = 44/29 > 0.
```

Every nonzero-flux component has a smaller maximum mean flippability than the
zero-flux mobile component. Reversing the perturbation sign supplies a sharp
control: for `delta V>0`, one of the many frozen zero-flippability components
wins instead.

Second, the runner constructs noncontractible alternating loops carrying
signed flux along all three cubic axes and runs chains targeting the uniform
RK measure on `L=6,8,10,12`. For each nonzero magnitude it averages six chains, one for
each axis and sign; each chain uses a different initial line placement and
random seed. Three independent chains supply each zero-flux reference. All
`120` chains preserve exact three-of-six Gauss charge and their assigned
topological flux.

At each volume, the data fit

```text
<N_f>_(L,Phi)=a_L-c_L Phi^2/L.
```

The independently fitted coefficients are

```text
L=6       c=1.674857 +/- 0.141886
L=8       c=1.884728 +/- 0.151700
L=10      c=1.449046 +/- 0.157112
L=12      c=1.260166 +/- 0.173252.
```

Every coefficient is positive by more than seven reported standard errors.
A common weighted fit with a separate intercept for each volume gives

```text
c=1.591937 +/- 0.077393.
```

An unweighted common fit gives `c=1.483284`. Its residual sum of squares is
`1.734259`, compared with

```text
linear in |Phi|       3.623267
linear in |Phi|/L     4.413888
quadratic in Phi      4.410875
nonzero-sector step  27.987299.
```

Every model receives an independent intercept at each volume, so this
comparison tests the flux dependence rather than the extensive background.

For `delta V<0`, the measured first-order flux cost is therefore

```text
Delta E(Phi)
 =|delta V| [<N_f>_0-<N_f>_Phi]
 =|delta V| c Phi^2/L + finite-volume corrections.
```

Matching it to the Maxwell topological-sector energy

```text
Delta E_Maxwell(Phi)=U Phi^2/(2L)
```

gives, in the displayed electric-field normalization,

```text
U/|delta V|=2c=3.183873 +/- 0.154786.
```

This is the electric coefficient missing from the direct parent. That parent
already measures positive magnetic stiffness on the same one-qubit carrier.
Together they give a positive `U K` product and hence two conditional linear
Maxwell branches in the quadratic long-wavelength theory.

The result is bounded. It is a first derivative at the RK point, measured on
four finite volumes. It does not independently establish the complete
thermodynamic phase at finite `delta V`, its real-time spectrum, or a physical
site compiler. Those stronger statements remain separate.

## 1. Exact topological-sector graph

The microscopic variables and staggered electric flux are defined in the
direct parent. On `L=2`, the runner enumerates every choice of `12` occupied
links among `24`, then retains exactly those with three occupied links at all
eight vertices. It obtains `9600` states across `125` electric-flux triples.

For every state, the runner constructs all alternating square flips with
their geometric multiplicities. It checks that every destination is in the
ice set, that every move preserves the complete flux triple, and that the
reverse edge has the same multiplicity. Breadth-first search then partitions
the graph into `937` connected components, `177` of them mobile.

At the RK point, the equal-amplitude state on each connected component is an
exact zero of the RK projector Hamiltonian. The derivative of its energy with
respect to `V` is the component mean of `N_f`. Thus component flippability is
the exact finite-volume first-order discriminator; no fitted Hamiltonian
coefficient is inserted.

Only one mobile component attains mean flippability `8`, and it has zero
electric flux. Cubic rotations and flux inversion generate six unit-flux
components. The runner obtains their equal size and mean as exact integer
relations, not floating-point coincidences:

```text
size=464,
29 sum_state N_f(state)=188 x 464.
```

For `delta V<0`, maximizing `<N_f>` minimizes the first-order energy. The
zero-flux component is therefore selected exactly on this torus. All
nonzero-flux maxima lie below it. For the opposite sign, an `N_f=0` frozen
component has the smallest shift. This sign-reversal control distinguishes
the perturbative selection from a hard-coded preference for zero flux.

## 2. Constructing controlled nonzero flux

Starting from the checkerboard ice configuration, choose a straight
noncontractible loop along one cubic axis. Occupations alternate along that
loop. Flipping the whole loop changes one incoming and one outgoing link at
each visited vertex, so every three-of-six constraint survives. Depending on
the transverse parity, the loop changes the signed electric flux by `+1` or
`-1`.

The runner derives that sign by evaluating the flux before and after each
candidate loop. It inserts the requested number of same-sign loops, verifies
the resulting full flux triple, and rejects any construction that changes a
vertex degree. Local square moves then sample within the assigned sector
without changing the flux.

The largest magnitude is `Phi=L/2`. Therefore the field density in the fit
window obeys

```text
|Phi|/L^2 <= 1/(2L),
```

which decreases from `1/12` at `L=6` to `1/24` at `L=12`. The refinement is
not a fixed large-background-field test.

## 3. Symmetry-averaged Monte Carlo protocol

For every `L` and every magnitude `Phi=1,...,L/2`, the protocol runs all six
signed-axis sectors

```text
(+/-Phi,0,0), (0,+/-Phi,0), (0,0,+/-Phi).
```

Each chain starts from a shifted set of noncontractible flux lines, uses `500`
thermal sweeps, and then takes `500` samples separated by two full
checkerboard sweeps. Ten consecutive blocks per chain estimate uncertainty.
The six nonzero-flux chains provide `3000` samples per magnitude. Three
independent zero-flux replicas provide `1500` samples per volume.

The largest signed-axis range is `3.375` times the estimated standard error
of one chain. Pooling all signs and axes therefore removes a visible cubic
orientation choice while retaining the between-chain variation in the block
error. This is a sampling control, not a proof of large-volume ergodicity.

The measured orbit means are:

```text
L=6:  169.2593, 169.1357, 168.2900, 166.8390
L=8:  400.1993, 400.2510, 399.9897, 398.4503, 396.7370
L=10: 780.5727, 779.6630, 779.6877, 778.8550, 778.0757, 776.4027
L=12: 1347.9060, 1347.1087, 1346.7343, 1345.9627,
      1345.5970, 1344.4800, 1343.5380.
```

Within each row, entries run from `Phi=0` through `Phi=L/2`. Individual small
flux steps can fluctuate upward, as the `L=8, Phi=1` value does. The theorem
does not require pointwise monotonicity. Its load-bearing test is the resolved
quadratic coefficient at each volume and the common controlled model
comparison.

## 4. Extracting the electric stiffness

The effective electric energy of a uniform topological flux is

```text
(U/2) L^3 (Phi/L^2)^2 = U Phi^2/(2L).
```

The microscopic first-order cost has the same volume and flux dependence.
Equating coefficients gives `U=2c|delta V|`. No empirical value, photon speed,
or target coefficient is used in the fit. The volume intercepts absorb only
the extensive zero-flux flippability.

The four `c_L` values are not assumed equal. Their range is `0.625`, or about
`39.9%` of their mean; the runner requires this relative spread to stay below
`50%`. The common weighted coefficient is more than twenty reported standard
errors above zero. The unweighted coefficient differs from it by `6.8%`,
inside the stated `25%` consistency bound.

The quadratic-over-volume form is also discriminating. With the same four
free intercepts and one common slope, its residual is less than half that of
the nearest named control. A linear flux cost, an unscaled `Phi^2` cost, and a
mere nonzero-sector offset do not describe the finite data as well.

This establishes positive topological electric stiffness at first order in
the stated protocol. It does not bound higher orders in `delta V` uniformly
with volume. The primary spin-liquid analysis supplies the stronger phase
stability argument; this runner supplies a direct executable coefficient and
its scaling tests.

## 5. Consequence for the photon bridge

The direct parent established on the same carrier:

- exact one-qubit Gauss-preserving square-ring dynamics;
- the complete `L=2` zero-flux RK sector;
- axial and off-axis transverse Coulomb covariance on `L=6,8,10,12`; and
- positive magnetic stiffness from threaded magnetic flux.

This source adds the complementary first-order electric term. In the
quadratic long-wavelength Hamiltonian

```text
H_eff=(U/2)||E||^2+(K/2)||curl A||^2,
```

the expansion point has positive `K`, and the first derivative produces
positive `U` into the tested side. Thus both are positive to first order. The
cubic curl kernel then has one Gauss-null direction and two equal branches

```text
omega(k)^2=U K 4 sum_i sin^2(k_i/2).
```

The new content is the sign, scaling, and magnitude of `U` in a microscopic
one-qubit model. The mode-count identity and positive magnetic term come from
the parents. A direct real-time or imaginary-time many-body spectrum at
finite `delta V` remains unexecuted.

## 6. Program boundary and next target

This result removes two candidate blockers at once:

```text
finite local dimension two is compatible with magnetic stiffness,
finite local dimension two is compatible with positive electric stiffness.
```

It materially strengthens the light lane because the two coefficients needed
for a linear photon now coexist on the same exact microscopic carrier. It is
not merely another imposed Maxwell generator: the coefficient is a falsifiable
statistic of the supplied qubit Hamiltonian and its topological sectors.

The shortest remaining physics test is dynamical and thermodynamic. A
sign-free quantum Monte Carlo calculation or controlled duality analysis at
finite `delta V<0` should resolve a volume-stable linear transverse spectrum
or the equivalent charge `1/R` response. Those are alternative diagnostics
of the same phase obligation, not two separate walls.

The physical-site compiler remains separate. Coarse cubic links and square
ring terms must still be realized by one homogeneous nearest-neighbor rule on
the framework's physical `Z^3` sites. Matter coupling, Admissibility
selection, and empirical electromagnetic identification also remain open.

No axiom edit follows. The ice sector, ring Hamiltonian, perturbation sign,
and couplings are supplied model content. Admissibility does not select them,
and Record is untouched.

## 7. Prior-art and contribution boundary

The cubic spin-half model and the first-order topological-sector strategy are
from M. Hermele, M. P. A. Fisher, and L. Balents,
[“Pyrochlore Photons: The U(1) Spin Liquid in a S=1/2 Three-Dimensional
Frustrated Magnet”](https://arxiv.org/abs/cond-mat/0305401) (2004). That work
states that `delta V<0` selects the zero-flux sector, measures the static
spinon potential, and establishes the adjacent stable `U(1)` phase.

The repo-specific contribution is an independent executable realization of
the topological-stiffness route: complete all-flux component enumeration,
exact unit-flux cost, `120` signed-axis and shifted-initialization chains, a
shrinking field-density ladder, four independent positive coefficients, and
a controlled common-scaling comparison that yields the displayed `U`
coefficient. This does not claim priority for the model or method.

## 8. Executable evidence

The runner reports `TOTAL: PASS=11 FAIL=0`. It checks:

- exact partition of all `9600` states into `937` reversible,
  flux-preserving components;
- unique maximal flippability of the zero-flux mobile component;
- exact signed-axis and cubic degeneracy of the six unit-flux components;
- the `delta V<0` selection and opposite-sign frozen-sector control;
- exact Gauss and assigned-flux preservation in all `120` large-volume
  chains;
- a positive independently resolved `c_L` on every volume;
- a bounded coefficient range and spread across `L=6,8,10,12`;
- preference for `Phi^2/L` over four named controls with equal intercept
  freedom;
- a positive weighted common coefficient and derived `U/|delta V|`;
- shrinking fitted field density with volume; and
- a normalized signed-axis sampling-spread control.

## No-Go Discipline Gate

This is a positive first-order stiffness theorem with a deliberately
unexecuted thermodynamic phase question. The gate prevents the remaining
dynamic calculation from being inflated into several independent blockers or
from being treated as a negative result.

### N1 — Alternative route enumeration

| Honesty | Route family | Outcome |
|---|---|---|
| **ATTEMPTED** | exact all-flux component graph | **Positive:** zero flux is uniquely most flippable and unit flux has exact positive cost. |
| **ATTEMPTED** | signed-axis noncontractible-loop sectors | **Positive:** all `120` chains preserve exact Gauss charge and assigned flux. |
| **ATTEMPTED** | four-volume `Phi^2/L` scaling | **Positive:** every `c_L` and the common coefficient are resolved above zero. |
| **ATTEMPTED** | linear, unscaled-quadratic, and sector-step controls | **Discriminating:** all have larger common-fit residuals. |
| **ATTEMPTED** | magnetic threaded-flux route | Direct parent supplies positive `K` on the same carrier. |
| **IMPORTED** | static-charge `1/R` response and phase stability | Primary model result; not restated as runner output. |
| **OPEN** | finite-`delta V` sign-free dynamical calculation | Would test the full phase and linear spectrum directly. |
| **OPEN** | homogeneous physical-site compiler | Would realize the constrained link model under the framework's local rule. |
| **OPEN** | matter coupling on the spin-half carrier | Would join mobile charge, current, and field work on this model. |

These routes differ by sector observable, scaling law, or terminal obligation.
The exact small graph and the four-volume Monte Carlo are independent
resolutions, not duplicated descriptions of one number.

### N2 — Wall-independence and collapse audit

The finite-`delta V` spectrum, stable thermodynamic phase, and charge `1/R`
response are diagnostics of one remaining phase obligation and collapse into
`W1`.

```text
W1 = repo-native finite-delta-V thermodynamic and dynamical phase test,
W2 = homogeneous nearest-neighbor physical-site compiler,
W3 = mobile matter and exact backreaction on the spin-half carrier,
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

The supplied cubic link graph, three-of-six sector, RK tuning, first-order
`delta V` expansion, topological-flux normalization, finite even volumes,
maximum `Phi=L/2`, fixed seeds, shifted initial flux lines, checkerboard local
updates, sample counts, block estimator, and symmetry pooling are explicit.
Large-volume ergodicity within a flux sector is not proved. The standard-error
figures do not include an independent rigorous autocorrelation bound. The
shrinking field density controls the field amplitude but does not interchange
the `delta V` and thermodynamic limits. The supplied law is not attributed to
the framework axioms.

### N4 — Residual matching

| Surface | Exact residual there | Match here |
|---|---|---|
| direct finite-qubit parent | positive magnetic stiffness but electric coefficient imported | **direct partial resolution:** positive first-order `U` is now computed |
| finite-clock parent | controlled Maxwell tangent, full many-link phase open | **alternative carrier:** fixed local dimension two and topological-sector stiffness |
| Maxwell-generator parent | supplied positive quadratic electric term | **microscopic coefficient match:** `U=2c|delta V|` in the stated normalization |
| primary spin-liquid source | long-run phase and static-charge response | **independent finite protocol:** exact graph plus topological-flux scaling |
| physical-role compiler parent | collective edge/face roles | **unmatched remainder:** ice constraint and ring term are not yet compiled |

The computed first derivative is not mislabeled as the full finite-perturbation
phase.

### N5 — Rhetoric and resolution audit

“Positive electric stiffness” means the positive coefficient of the
first-order `Phi^2/L` topological energy on the stated finite protocol. It
does not mean a uniform all-orders thermodynamic bound. “Resolved” uses the
displayed block errors and controls; the unproved large-volume mixing caveat
remains explicit. The derived `U` is a model coefficient, not an observed
electromagnetic constant.

The cached runner contains the five-resolution execution certificate:

```text
per_element: each noncontractible alternating loop and each local plaquette move are checked
per_site: exact three-of-six Gauss charge is preserved in every signed-flux chain
per_mode: electric topological flux has positive quadratic stiffness in the Maxwell normalization
per_block: all 9600 L=2 states and signed-axis Monte Carlo orbits on L=6 through L=12 are checked
lattice_wide: finite-volume electric stiffness is resolved; a thermodynamic phase proof is not executed
```

### N6 — Partial-closure paths and primitive boundary

No axiom or approved primitive is added. `W1` is a supplied-model phase
calculation. It can be approached by sign-free quantum Monte Carlo, a
continuous-time RK/master-equation method, or a controlled duality bound.
`W2` is a compiler construction, and `W3` can reuse the gauge-matter energy
accounting of the light parents only after the carrier map is explicit. `W4`
is the selection and physical-identification boundary. None requires turning
this measured coefficient into an axiom.

### N7 — Steelman

A hostile reviewer should reject a claim that four finite volumes and
first-order perturbation theory prove the stable photon phase. The local
Markov chain may have unmeasured mixing time, the block error is not a
rigorous autocorrelation theorem, and the `delta V` radius need not be uniform
in `L`. These objections are correct and define `W1`.

They do not erase the exact `L=2` sign result or the fact that every larger
volume independently gives positive curvature with a common scaling law that
beats the named controls. The appropriate conclusion is the bounded
first-order stiffness theorem, not either a complete phase proof or a
negative verdict.

### N8 — Cross-cycle echo

The direct parent stopped at static RK correlations and positive magnetic
stiffness. This source attacks its named missing electric coefficient with a
new topological observable, exact all-flux enumeration, symmetry-related
chains, volume scaling, and alternative-law controls. It is not an algebraic
restatement of the parent. The earlier finite-clock route supplied a tangent
by payload refinement; this route holds the local payload at one qubit and
measures the stiffness emerging from constrained many-body sectors.

**Gate result:** PASS. Six executed or imported route families are separated,
three further routes remain open, dependent phase diagnostics are collapsed
into one wall, and the first-order boundary is explicit.

## Falsifiers

The bounded theorem fails if any of the following occurs:

- the exact move graph omits a state, crosses flux sectors, or is not
  reversible with geometric multiplicity;
- the zero-flux mobile component is not the unique maximizer of mean
  flippability;
- any signed unit-flux component differs in size, mean, or first-order cost;
- any constructed noncontractible loop changes a vertex Gauss charge or has
  the wrong signed flux;
- any Monte Carlo chain leaves its assigned sector;
- any fitted `c_L` is nonpositive or unresolved at the stated threshold;
- the four-volume coefficient loses significance or exceeds the stated
  relative spread;
- `Phi^2/L` fails to beat any named equal-intercept control by the stated
  residual factor;
- the weighted and unweighted common coefficients disagree outside the
  stated bound;
- the field-density window fails to shrink; or
- the signed-axis spread exceeds four estimated single-chain standard
  errors.

## Verification

Run:

```text
PYTHONPATH=scripts python3 scripts/spin_half_cubic_ice_topological_electric_stiffness_2026_09_03.py
```

Expected final line:

```text
TOTAL: PASS=11 FAIL=0
```
