# Spatial CAR lift and local modular-seam contact form factor — Cycle 230

**Date:** 2026-07-17

**Type:** bounded_theorem

**Status:** exact finite conditional construction plus bounded numerical
interaction discriminator; audit unset

**Authority:** none

**Constitutional effect:** none

**Packaging:** draft parking branch and draft PR #5389 only

Companion runner:

```text
scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py
```

Load-bearing internal inputs:

- [Cycle 210 proper-cubic bound-object fixture](PROPER_CUBIC_BOUND_OBJECT_EQUIVALENCE_CYCLE210_NOTE_2026-07-16.md)
- [Cycle 219 common matter/field coin family](COMMON_MATTER_FIELD_COIN_FAMILY_CYCLE219_NOTE_2026-07-16.md)
- [Cycle 228 local generator/source tournament](LOCAL_GENERATOR_SOURCE_TOURNAMENT_CYCLE228_NOTE_2026-07-17.md)
- [Cycle 229 finite Fock and modular-boundary construction](FOCK_MODULAR_BOUNDARY_CURRENT_CYCLE229_NOTE_2026-07-17.md)

This note and runner change no foundation, axiom, Qualification, primitive,
registry, policy, audit, or queue surface.

## Result up front

Cycle 230 performs the spatial and interacting construction left open by
Cycle 229. On a periodic `L=3` cubic lattice with six fermionic direction
modes per coarse cell, it constructs the canonical number-preserving
**intrinsic CAR** lift of the supplied radius-one proper-cubic walk. The free
step has an onsite exterior-coin layer and an exact **depth-two fermionic
swap** stream layer. It preserves the canonical anticommutation relations,
fermion number, radius-one support, translations, and all 24 proper-cubic
frames.

The runner then supplies one local even interaction,

```text
W_g = product_x exp(i g binom(N_x,2)),
N_x = sum_a n_(x,a),
G_g = W_g Gamma(S C).
```

This gate is onsite on the declared CAR cell, number and parity preserving,
translation invariant, and proper-cubic invariant (indeed `U(6)` invariant).
It is identity on the zero- and one-particle sectors, so adding it leaves the
Cycle-219 one-particle rest-phase, curvature, and forced-inertia calibration
unchanged. For `n>=2` it applies occupation-dependent many-body phases and is
not the second quantization of a one-particle unitary. The gate order and
dimensionless `g` remain supplied candidate-law content.

The complete `L=3` Bloch basis contains all 162 one-particle modes. Filling
every mode with principal phase `theta<0` produces one full occupied-mode
projector and thereby one finite **principal-branch Slater sea ray**, rather
than a sample of selected blocks. The one-particle projector is orthogonal,
free-step invariant, translation invariant, and proper-cubic invariant. The
sea is still supplied rather than selected: changing the quasienergy phase
origin changes the occupied rank.

Within that full finite sea, the runner identifies a momentum-balanced
**two-particle/two-hole** channel whose unwrapped branch-coordinate difference
is `2 pi` to machine precision while its one-tick phase is the identity. The
contact generator has a basis-independent rank-two block on that channel.
After removing the universal plane-wave normalization, its singular values
are approximately

```text
0.49577141, 0.45566605,
```

and its Frobenius channel norm is approximately `0.67336531`. The linear-in-`g`
amplitude is `i g/L^3` times this reduced block, up to the sea-ordering sign;
equivalently, its derivative at `g=0` is `i/L^3` times the block. This is a
**machine-precision fixture resonance**, not a symbolic identity and not the
Cycle-228 diagonal seam itself.

The universal 1/L^3 factor is kept in every absolute plane-wave
coefficient; only the internal block is quoted without it.

A separate finite-volume sequence brackets the Cycle-228 numerically located
diagonal `U=-1` crossing. Holes occupy paired momenta `+/- k_<` below the crossing and
particles occupy `+/- k_>` above it, so both total momenta vanish. Its free
branch-coordinate difference approaches `4 pi`, its wrapped one-tick phase
approaches one, while all four **plane-wave-factor-stripped** internal contact
singular values remain nonzero and the sampled values lie near one. The raw plane-wave
matrix element retains the **universal `1/L^3`** normalization and therefore
decreases with volume. A rate would require the density of final states,
repeated dynamics, and a physically selected preparation and clock.

For this same contact, a nonzero reduced element also occurs at the tested
ordinary `U=+1` crossing, with the same singular values. Therefore nonzero
coupling alone is not unique to the modular seam. The seam-specific fact is
the large unwrapped coordinate becoming a near-trivial wrapped phase.

The bounded candidate result is therefore a **first-order generator coupling** for one
supplied interaction, sea, and finite-volume sequence. It is **not a
transition probability**, decay rate, vacuum instability, physical-energy
direction, physical vacuum selector, or proof that every local interaction
couples the seam. Physical energy remains unselected. No axiom conclusion
follows.

## The decisive foundation boundary

The construction uses **six fermionic modes per coarse cell**. Its local Fock
space has dimension `2^6=64`, with local algebra `M_64`. It is therefore **not
a one-qubit-per-site compiler** for a foundation whose physical site carries
`M_2`. With one fermionic occupation mode on one physical site,
`binom(N_x,2)=0`; the displayed onsite interaction is trivial.

“Onsite” in this note means onsite at the declared six-mode CAR-cell
resolution. It does not mean that the same gate has been compiled into the
current physical-site alphabet with bounded support and no auxiliary parity
structure. The live foundation residual combines three descriptions of the
same missing bridge:

1. realize CAR statistics on the physical substrate;
2. encode the six direction modes using the admitted site resolution; and
3. preserve graded locality when the CAR cell is compiled to ordinary local
   operations.

Those are not counted as three independent impossibilities. They are one
compiler obligation. This cycle establishes no no-go for such a compiler and
does not request an axiom change.

## Exact finite spatial CAR construction

Let `c_(x,a)^dagger` create a fermion in direction mode `a` at cell `x` and
obey

```text
{c_(x,a), c_(y,b)^dagger} = delta_(x,y) delta_(a,b),
{c_(x,a), c_(y,b)} = 0.
```

The supplied one-particle step is `U=S C`, with the same six-mode onsite coin
at every cell and the conditional stream

```text
S |x,a> = |x + D_a,a>.
```

Canonical number-preserving second quantization gives

```text
Gamma(U) c_j^dagger Gamma(U)^dagger = sum_i U_(i,j) c_i^dagger.
```

Because `U` is unitary, this action preserves the CAR. Because each column of
`U` has support only in the six output modes at neighboring cells, its
Heisenberg support has the same radius-one stencil. This is intrinsic graded
fermion locality, not an ordinary Jordan–Wigner locality claim.

The stream also has a constructive two-layer fermionic-swap form. Let `A`
swap `+mu` and `-mu` at each cell. Let `B` swap `(x,-mu)` with
`(x+e_mu,+mu)` on every edge. Every swap within each layer is disjoint and

```text
S = B A.
```

The runner verifies the permutation identity on the full `L=3` one-particle
space and separately verifies that its two layers give the identical
antisymmetric two-particle action. `L=2` aliases
the positive and negative nearest neighbor in each axis; `L=3` is the
smallest periodic cube that keeps all six neighbors distinct.

At one cell, the exterior coin is

```text
Gamma(C) = direct_sum_(n=0)^6 wedge^n C,
```

a `64 x 64` unitary. The contact gate has eigenvalue
`exp(i g binom(n,2))` in its local `n`-particle sector. Both commute with
local number. The contact is identity for `n<=1`, which is why it cannot
change any one-particle mass observable.

For an antisymmetric two-particle amplitude matrix `A`, normalized by

```text
||A||_2p^2 = (1/2) Tr(A^dagger A),
```

the free and contact steps are

```text
A -> U A U^T,
A_(xa,xb) -> exp(i g) A_(xa,xb),
```

with all different-cell entries unchanged by the contact. The runner checks
antisymmetry, norm, strict support, interaction deletion at `g=0`, and a
nonzero difference between the two possible coin/stream/contact schedules.
The schedule is therefore physical law content; locality alone does not
select it.

## Full finite sea

For every momentum in the `L=3` Brillouin grid and every one of the six
bands, the runner constructs the normalized Bloch orbital

```text
u_(k,j)(x,a) = L^(-3/2) exp(i k.x) v_(k,j)(a).
```

All 162 orbitals are enumerated. They form an orthonormal basis and diagonalize
the real-space spatial walk. The supplied occupied-mode projector

```text
P_sea = sum_(theta_(k,j)<0) |u_(k,j)><u_(k,j)|
```

is then checked directly for idempotence, free-step invariance, translations,
and all proper-cubic frames. Its occupied subspace defines a unique finite
Slater sea ray up to phase. The finite fixture has no mode at the selected zero
or branch endpoint, so the ledger is unambiguous after the phase cut is
supplied.

This does not select a physical sea. Under the rephasing
`U -> exp(i delta) U`, the rank of the same principal-Arg prescription
changes. Neither the realized-state primitive nor the scale or
kinetic-isotropy primitives supply a quasienergy zero, filling, preparation,
or thermodynamic representation.

## Contact matrix element and normalization

Write the two-body generator as

```text
H_int = g sum_x binom(N_x,2)
      = g sum_x sum_(a<b) n_(x,a) n_(x,b),
W_g = exp(i H_int).
```

For normalized Bloch orbitals and a momentum-conserving double excitation,
the Slater–Condon matrix element is, up to the sign fixed by sea ordering,

```text
<p1 p2; h1 h2 | H_int | sea>
  = (g/L^3) delta_(kp1+kp2,kh1+kh2)
    [(vp1^dagger vh1)(vp2^dagger vh2)
     -(vp1^dagger vh2)(vp2^dagger vh1)].
```

There is no extra factor of two: the `a<b` sum already equals
`binom(N_x,2)`. The runner independently sums the spatial onsite wedges and
recovers the internal form-factor block divided by `L^3`.

Degenerate band eigenvectors are not unique. The runner never retains one
chosen entry as the result. It builds the full map between the relevant
degenerate pair subspaces and reports its singular values and Frobenius norm.
Those are invariant under arbitrary unitary basis changes inside each
degenerate band. The same singular spectrum is recovered in all 24
proper-cubic frames.

The nonzero derivative

```text
d/dg <2p2h|W_g|sea> at g=0
```

shows that this supplied analytic gate family is not identically decoupled
from the named channel. It does not by itself give a finite-time population,
a probability, or an irreversible process. In a finite closed unitary system
it can instead describe coherent dressing or oscillation.

## The two complementary modular witnesses

### Complete small spatial fixture

The complete `L=3` sea contains a momentum-balanced channel with holes at

```text
k_h1 = (2 pi/3)(0,1,0),
k_h2 = -k_h1,
```

and particles at

```text
k_p1 = (2 pi/3)(1,1,1),
k_p2 = -k_p1.
```

The selected occupied and empty band subspaces give a branch-coordinate
difference of `2 pi` to machine precision. The full contact block is rank two
and nonzero. This is a complete-small-fixture modular resonance. It is not a
symbolic equality and is not itself a discretization converging to the
Cycle-228 `U=-1` diagonal root.

### Actual diagonal seam sequence

For each sampled even torus size, take the adjacent diagonal grid values
that bracket the numerical `U=-1` root `q0`:

```text
q_< = 2 pi floor(q0 L/(2 pi))/L,
q_> = q_< + 2 pi/L.
```

Two occupied modes at `+/-q_<(1,1,1)` and two empty modes at
`+/-q_>(1,1,1)` conserve total momentum. As the bracket shrinks,

```text
theta_h -> -pi,
theta_p -> +pi,
Delta_theta_2p2h = 2 theta_p - 2 theta_h -> 4 pi,
exp(i Delta_theta_2p2h) -> 1.
```

The reduced contact block remains full rank; the four sampled singular values
stay near one. “Unsuppressed” here means only that the internal reduced
coefficient does not vanish over the sampled seam brackets. Conditional on an
exact transverse crossing, the branch-coordinate limit is algebraic; the
numerical form-factor trend is not promoted to an exact limiting value. The absolute normalized
plane-wave coefficient still scales as `g/L^3`. No thermodynamic rate is
computed.

A one-particle/one-hole transfer across the same diagonal root carries
nonzero momentum and is exactly forbidden by translation conservation for
this homogeneous contact. The balanced second pair is not optional
bookkeeping; it is the smallest channel tested here that restores momentum.

## Cross-lane effect

### Occurrence and records

The construction supplies coherent many-body alternatives and an explicit
interaction derivative. It does not prepare the sea, choose an outcome,
write a record, or turn amplitudes into occurrence frequencies. Tensoring
one or more passive non-record factors leaves the displayed matrix element
unchanged. This is ordinary tensor-spectator invariance; it neither constructs
a Record nor establishes record redundancy.

### Time

The strict update supplies an integer step label. The `4 pi -> 1` alias shows
that the wrapped phase alone cannot retain this branch coordinate. Any clock
intended to recover that coordinate needs additional winding/history content
or a different construction. No clock rate, lapse, or record-count time is
derived here.

### Inertia and mass

The contact is identity in the one-particle sector, so the previously tested
rest-phase, low-momentum curvature, and forced-response mass remain equal for
that sector. This is coexistence of a supplied interaction with the mass
contract, not an interacting bound-state spectrum, renormalized mass, or
selected species law.

### Gravity and source

Particle number has an exact local continuity law because every onsite
factor preserves it and the stream only moves it across one edge. Number is
not thereby energy or gravitational charge. Conversely, the Cycle-229 local
deviation generator `dGamma(K)` does not commute with the contact generator
`V=sum_x binom(N_x,2)`. Thus `K` alone is not a conserved interacting source
for this candidate generator. A dressed
or action-derived total ledger remains live; no stress tensor, reciprocal
field equation, or geometry follows.

### Born/probability

The full finite boundary-conditioned sea and a nonzero coherent derivative
do not supply frame weights, a prepared-state link, repeated-record
frequencies, or the Born rule. This cycle makes no probability claim.

## Prior work and claim boundary

Cycle 230 does not claim a new general fermionization or interacting-QCA
construction. It **uses/reproduces** the canonical number-preserving second
quantization of the supplied finite-range one-particle walk: on a finite
periodic lattice, `U=S C` lifts to `Gamma(U)=Gamma(S)Gamma(C)`, preserves the
CAR, and inherits finite Heisenberg support. Causal fermionic dynamics, local
fermionic-gate decompositions, and a three-dimensional Dirac example are
established by Farrelly and Short [1].

Likewise, onsite number-preserving four-fermion interactions and explicit
discrete-time transition/scattering calculations already occur in the
one-dimensional **Thirring quantum cellular automaton** [2,3]. Bisio et al.
define a one-dimensional Dirac walk combined with the most general onsite
number-preserving two-fermion phase (`U_2=W_2 V_2`) and analytically solve its
two-particle scattering and bound states.

Gupta and Short supply the distinct modular-quasienergy Dirac-sea boundary
whose interaction sensitivity is being probed here [4]. They identify the
modular boundary and derive a generic perturbative modular-energy/rate
framework, but explicitly leave evaluation in a specified interacting model
for future work. They do not compute this seam form factor or a model-specific
rate.

The fixture-specific work is narrower: instantiating the CAR lift for the
supplied six-mode, radius-one, proper-cubic walk; checking its exact support
and covariance on the declared finite torus; fixing the supplied finite-volume
branch projector/sea; and evaluating the band-spinor form factor of one
explicitly declared local even interaction for named modular channels. An
explicit filled-sea seam form factor for this fixture goes beyond the direct
primary sources cited below; **global priority is not claimed**.

A spatial CAR lift must also be distinguished from an onsite tensor-product
qubit compiler in three dimensions. The cited higher-dimensional
constructions use additional structure: auxiliary Majorana modes and a
constrained subsector [1], distinguishable walker registers followed by a
global antisymmetry restriction [6], or gauge/rishon parity degrees of freedom
[7]. Mlodinow and Brun's scoped direct-occupation/local-creator no-go [5] does
not forbid spatial CAR automorphisms; together with the absence of a compiler
here, it underscores that this construction is not a demonstrated no-ancilla
onsite-qubit realization. In the infinite-lattice reading, the safe object is
a quasi-local CAR-algebra automorphism; this cycle does not thereby construct
a normalizable filled-sea vector in the empty-Fock representation.

References:

1. T. C. **Farrelly and Short**, “Causal Fermions in Discrete Space-Time,”
   *Physical Review A* **89**, 012302 (2014),
   <https://doi.org/10.1103/PhysRevA.89.012302>, arXiv:1303.4652.
2. A. Bisio, G. M. D'Ariano, P. Perinotti, and A. Tosini, “The Thirring
   quantum cellular automaton,” *Physical Review A* **97**, 032132 (2018),
   <https://doi.org/10.1103/PhysRevA.97.032132>, arXiv:1711.03920.
3. A. Bisio, P. Perinotti, A. Pizzamiglio, and S. Rota, “A Perturbative
   Approach to the Solution of the Thirring Quantum Cellular Automaton,”
   *Entropy* **27**, 198 (2025), <https://doi.org/10.3390/e27020198>,
   arXiv:2406.19917 (first posted 2024).
4. C. **Gupta and Short**, “The Dirac Vacuum in Discrete Spacetime,” *Quantum*
   **9**, 1845 (2025), <https://doi.org/10.22331/q-2025-09-03-1845>,
   arXiv:2412.03466.
5. L. Mlodinow and T. A. Brun, “Quantum field theory from a quantum cellular
   automaton in one spatial dimension and a no-go theorem in higher
   dimensions,” *Physical Review A* **102**, 042211 (2020),
   <https://doi.org/10.1103/PhysRevA.102.042211>, arXiv:2006.08927.
6. L. Mlodinow and T. A. Brun, “Fermionic and bosonic quantum field theories
   from quantum cellular automata in three spatial dimensions,” *Physical
   Review A* **103**, 052203 (2021),
   <https://doi.org/10.1103/PhysRevA.103.052203>, arXiv:2011.05597.
7. N. Eon, G. Di Molfetta, G. Magnifico, and P. Arrighi, “A relativistic
   discrete spacetime formulation of 3+1 QED,” *Quantum* **7**, 1179 (2023),
   <https://doi.org/10.22331/q-2023-11-08-1179>, arXiv:2205.03148.

## N1 — alternative routes

The candidate construction was attacked through these distinct routes. All
current-cycle evidence is in the [companion runner](../../../../scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py).

| Attack route | Marker | Outcome and evidence |
|---|---|---|
| spatial CAR may be nonlocal | **ATTEMPTED** | `spatial_car_controls` constructs the radius-one generator action and exact two-layer fermionic stream; ordinary onsite-qubit locality remains open |
| the sea may be another sampled block | **ATTEMPTED** | `finite_sea_controls` enumerates all 27 `L=3` momenta and all six bands into one occupied projector |
| the channel may violate Pauli exclusion | **ATTEMPTED** | `l3_modular_channel_controls` uses exterior wedges of distinct occupied and empty orbitals |
| the channel may violate momentum conservation | **ATTEMPTED** | the balanced channel has zero total momentum; an unbalanced channel with nonzero internal overlap cancels in the direct spatial sum |
| a chosen degenerate eigenvector may fake the coupling | **ATTEMPTED** | the full subspace map is reported; random internal unitary rotations preserve its singular values |
| a preferred cubic frame may fake the result | **ATTEMPTED** | the spatial walk, finite channel, and seam sequence are checked in all 24 proper-cubic frames |
| the contact may destroy the one-particle mass contract | **ATTEMPTED** | the local contact is identity on `N<=1`; rest, curvature, and forced-response mass are rerun |
| nonzero coupling may be unique to the seam | **ATTEMPTED** | the same contact has the same reduced singular spectrum at the tested `U=+1`, `delta=10^-3` control; only the branch coordinate differs |
| finite range may automatically protect the seam | **ATTEMPTED** | this onsite contact stays full rank over the sampled seam brackets; zero-sum kernels and internal selection rules remain untested live alternatives |
| a nonzero derivative may already be decay | **ATTEMPTED** | no finite-time population or rate is computed, so the claim is narrowed to the Slater–Condon generator block |
| the principal sea may depend on the phase reference | **ATTEMPTED** | rephasing changes occupied rank; an interacting or dressed-vacuum calculation remains a live untested route |

No broad no-go is asserted.

## N2 — wall-independence

Cycle 229's six residual workstreams are updated rather than multiplied:

| Workstream | Cycle-230 status | Independent remaining content |
|---|---|---|
| `C_ref` | open | Select the phase origin, sea, and preparation. |
| `C_num` | open | Decide the physical number reference/superselection content. |
| `C_wrap` | open | Supply or derive a physical winding/history pull-back. |
| `C_int` | partial | One supplied contact has a nonzero derivative; select and iterate the actual interaction and compute a rate or protection theorem. |
| `C_local` | partial | Intrinsic spatial CAR locality is constructed; the physical `M_2` compiler is open. |
| `C_source` | partial classification | Number current survives and free `K` changes; physical energy/stress/source remains open. |

“Interaction choice” and “transition rate” are not counted as independent
walls: the latter is downstream of an interacting completion. CAR statistics,
six-mode capacity, and qubit locality are grouped into one physical-resolution
compiler obligation. Record occurrence and Born frequencies remain outside
this interaction probe rather than being relabeled as energy problems.

The complete pairwise directional audit uses the collapsed six-workstream
set above. “No” means there is no implication from closing the row's first
workstream to closing the second.

| Pair | first closes second? | second closes first? | independent? | Reason |
|---|---:|---:|---:|---|
| `C_ref`, `C_num` | no | no | yes | selecting a sea need not supply cross-number coherence, and a number reference need not select a sea |
| `C_ref`, `C_wrap` | no | no | yes | a chosen phase zero can still wrap; a winding carrier need not choose the zero |
| `C_ref`, `C_int` | no | no | yes | vacuum selection does not choose an interaction; an interaction does not select its vacuum |
| `C_ref`, `C_local` | no | no | yes | a physical sea does not compile CAR to `M_2`; a compiler does not select filling |
| `C_ref`, `C_source` | no | no | yes | choosing a sea does not derive stress/source; a source law does not choose the sea |
| `C_num`, `C_wrap` | no | no | yes | number reference and quasienergy winding are distinct reference structures |
| `C_num`, `C_int` | no | no | yes | superselection content does not choose the interaction, or conversely |
| `C_num`, `C_local` | no | no | yes | a number reference does not construct a bounded-support compiler, or conversely |
| `C_num`, `C_source` | no | no | yes | number-sector meaning does not identify physical stress/energy, or conversely |
| `C_wrap`, `C_int` | no | no | yes | retaining winding does not choose dynamics; an interaction need not retain winding |
| `C_wrap`, `C_local` | no | no | yes | winding history and substrate compilation are separate constructions |
| `C_wrap`, `C_source` | no | no | yes | an unwrapped coordinate need not be a conserved source; a source need not preserve that coordinate |
| `C_int`, `C_local` | no | no | yes | an abstract-CAR interaction does not compile itself; a compiler does not select a coupling |
| `C_int`, `C_source` | no | no | yes | interacting dynamics need not identify conserved stress; a source ledger does not select the dynamics |
| `C_local`, `C_source` | no | no | yes | a physical-site compiler does not determine energy/stress, and an energy ledger does not compile CAR |

No pair collapses further. Rate remains folded into `C_int`; CAR statistics,
cell capacity, and parity locality remain folded into `C_local`.

## N3 — hidden-wall scan

The construction supplies all of the following:

- `beta=-0.3` and the Cycle-219 common-family coin;
- periodic finite tori and Bloch plane-wave normalization;
- six CAR modes per coarse cell and graded locality;
- Fermi statistics and number-preserving second quantization;
- principal `Arg` and the `theta<0` sea;
- the numerical `U=-1` root used to choose the shrinking brackets;
- the numerical `U=+1` root used for the ordinary-crossing control;
- the four hard-coded `L=3` target phases that identify the reported
  degenerate band subspaces;
- dimensionless contact strength `g=0.37` as one arbitrary nonzero diagnostic
  value used for finite gate and schedule checks; no sensitivity sweep was
  performed;
- the derivative at `g=0`, rather than finite-time transition statistics;
- no prepared state, record apparatus, clock, or probability law.

The local site in the contact statement is not silently identified with the
foundation's `M_2` physical site.

The mandatory hidden-phrase scan found only the following hits among
`we assume`, `by construction`, `as is standard`, `the framework provides`,
`bridge context`, `background`, `naturally`, `obviously`, `standard QFT`,
`registered`, and `canonical` (including close variants):

| Phrase hit | Classification | Disposition |
|---|---|---|
| “canonical number-preserving [second quantization/lift]” | cited established machinery | kept with Farrelly–Short [1] and the explicit finite exterior construction; CAR statistics remain a declared input under `C_local` |
| “canonical anticommutation relations” | declared algebraic condition | kept as the definition checked under unitary generator action; it is not attributed to the axioms |

There are no other hits. The scan therefore promotes no additional wall. All
construction-specific inputs are listed above rather than hidden behind those
phrases.

## N4 — residual matching

The exact residual-match audit is:

| Cited witness | Witness residual | Cycle-230 use | Match? |
|---|---|---|---:|
| `docs/work_history/repo/review_feedback/FOCK_MODULAR_BOUNDARY_CURRENT_CYCLE229_NOTE_2026-07-17.md:44-45` | full finite-torus sea, spatial many-body QCA, interacting law, and onsite-qubit compiler absent | closes only the finite occupied projector, intrinsic spatial CAR, and one supplied interaction at coarse-cell resolution | yes, partial |
| same file `:93-95` | require a declared local proper-cubic interaction plus nonzero element, rate, or symmetry theorem | supplies one declared contact and nonzero first-order element; rate/protection remains open | yes, partial |
| same file `:185-187` | `Gamma(S)Gamma(C)`, full finite sea, local encoding, and interacting Fock law unexecuted | executes the first, finite occupied projector, and one interaction; leaves `M_2` encoding open | yes, partial |
| `docs/work_history/repo/review_feedback/LOCAL_GENERATOR_SOURCE_TOURNAMENT_CYCLE228_NOTE_2026-07-17.md:131,313-314` | physical energy, local additive Fock energy, and stress remain unselected | reports `[V,dGamma(K)]!=0` only as a discriminator and keeps energy/stress open | yes, residual preserved |
| `docs/work_history/repo/review_feedback/COMMON_MATTER_FIELD_COIN_FAMILY_CYCLE219_NOTE_2026-07-16.md:60,75` | conditional one-particle rest/dispersion/inertial/exchange mass agreement | reruns only the one-particle rest/curvature/forced subset because the contact is identity there | yes, input coexistence only |
| [Minimal Framework Axioms, Qubit / Site Possibility](../../../MINIMAL_AXIOMS_2026-06-29.md#qubit--site-possibility) | the full one-site possibility domain has algebraic presentation `M_2(C)` | exposes rather than closes the `M_64` coarse-cell to physical-`M_2` compiler interface | yes, exact interface mismatch |

No nonmatching citation is used as evidence for closure. The result matches the
open surfaces named by Cycle 229 as follows:

- the previously unexecuted `Gamma(S)Gamma(C)` spatial CAR candidate is now
  executed on a finite torus;
- the previously absent local interaction and matrix-element discriminator
  is now executed for one supplied contact;
- the physical sea, phase reference, rate, physical-site compiler, and
  physical source remain open exactly where Cycle 229 placed them;
- the Cycle-229 deviation current remains a one-particle/free coordinate, not
  Fock energy or stress.

The current foundation's `M_2`-site language and its withheld dynamics are
scope constraints, not evidence that the compiler is impossible. Prior
fermion-QCA literature is context and precedent, not a discharge of this
fixture's substrate compiler.

## N5 — resolution

The rhetoric audit checks every broad negative phrase at the resolutions it
could otherwise be read to cover:

| Scoped phrase | Resolutions actually tested | Resolutions not tested | Narrow final reading |
|---|---|---|---|
| this construction is not a one-qubit/site compiler | six-mode generator, `M_64` cell, finite `L=3` intrinsic CAR | bounded-support encoding into physical `M_2`, auxiliaries/gauge, infinite lattice | absence of a demonstrated compiler here, not compiler impossibility |
| the form factor is not a probability or rate | one generator matrix element, four finite-volume block samples | repeated histories, density of final states, thermodynamic limit, records | first derivative only |
| the contact does not alter one-particle mass | local `N=0,1` sectors and one-particle rest/curvature/forced response | dressed many-body dispersion, bound states, renormalization | exact only for the supplied one-particle sector |
| free `K` is not conserved by this contact generator | one explicit antisymmetric two-particle witness on the full `L=3` one-particle space | other interactions, dressed generators, thermodynamic representation | `[V,dGamma(K)]` is nonzero for this candidate only |
| physical energy remains unselected | one-particle spectral coordinates, finite particle/hole branch coordinate, contact derivative | clock calibration, action variation, stress/source, measurement | an interpretation/selection residual, not an energy no-go |
| no record result follows | passive tensor spectators only | actual Record formation, readout, frequency, Born statistics | no Record semantics were constructed in this cycle |

Additional tested resolutions are all 162 `L=3` modes, all 24 proper-cubic
frames, a complete-small-fixture modular channel, four sampled seam brackets,
and exact two-particle norm/schedule/deletion controls. A complete interaction
basis, dressed vacuum, and thermodynamic Fock representation are not tested.

## N6 — primitive and reframe

The [scale-reference primitive](../../../SCALE_REFERENCE_PRIMITIVE_NOTE.md)
supplies units only. The
[kinetic-isotropy primitive](../../../KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
supplies the form `c_t=c_s`, not the walk, `g`, a clock, or a rate. The
[realized-state primitive](../../../REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md)
supplies a pointwise evaluation slot only, not this sea, filling, or
preparation.

Accordingly, reported quantities are called an **unwrapped branch
coordinate**, **wrapped one-step phase**, and **first interaction-gate
derivative**. They are not renamed physical energy, time, probability, or
source. No primitive registration and no axiom conclusion follow.

Live partial-closure paths that do not require declaring a new axiom are:

| Candidate path | Current status | What it could close |
|---|---|---|
| bounded block encoding of six CAR modes across physical `M_2` sites, with explicit parity/gauge support | unbuilt | `C_local` at physical resolution |
| Cycle-204 nonlinear `tan(omega)` clock-map/composition route | live conditional route; it does not store winding | a physical energy coordinate if its readout and composition law can be derived |
| autonomous history/winding or amended-law route from Cycles 228–229 | unbuilt | `C_wrap` without naming wrapped phase as energy |
| prepared/dressed sea selected by the interacting update or boundary data | unbuilt | parts of `C_ref` and possibly `C_num` |
| action- or clock-response-derived conserved ledger | unbuilt | `C_source` without promoting free `K` |
| symmetry or zero-sum interaction form factor | live alternative | protect or narrow `C_int` without changing the substrate axioms |

The approved primitive registry was checked: realized-state, kinetic-isotropy,
and scale-reference primitives supply none of the sea, interaction, compiler,
clock, rate, or source content above. Proposed reframings carry no premise
weight until approved.

## N7 — steelman

> A hostile reviewer should treat the free `theta<0` sea as an arbitrary
> reference Slater determinant, not the interacting vacuum, and the nonzero
> derivative as coherent dressing in a finite closed system rather than
> decay. Gupta–Short [4] deliberately leave the specified-interaction
> calculation open; Farrelly–Short [1] show that higher-dimensional locality
> can require auxiliary structure. A zero-sum proper-cubic kernel, an internal
> selection rule, a dressed vacuum, an amended walk, or a physical `M_2`
> compiler may suppress or remove the channel. The universal `1/L^3`
> coefficient must be combined with final-state density and repeated dynamics
> before any rate exists.

That steelman is convincing, so every broad instability/protection/no-compiler
claim is demoted. Only the supplied finite conditional construction is
proposed for review.

Likewise, failure of `[V,dGamma(K)]=0` only rejects free `K` alone as the
conserved ledger for this supplied interaction generator. It does not reject a dressed
or action-derived conserved energy. A broad instability, no-energy, or
no-compiler conclusion would fail this steelman and is not shipped.

## N8 — cross-cycle echo

Repository searches for `structurally undecidable`, `no retained primitive`,
`requires new axiom`, `cannot be derived from A_min`, `spatial CAR`,
`winding`, and `onsite-qubit compiler` give the following relevant echoes:

| Prior wall | Prior status | Candidate Cycle-230 effect | Retirement mechanism applicable here? |
|---|---|---|---|
| Cycle 229 `C_local`: spatial CAR and onsite compiler absent | open | intrinsic finite spatial CAR is constructed; physical `M_2` compiler remains open | yes: explicit conditional construction partially addresses it; no axiom move |
| Cycle 229 `C_int`: no specified local interaction element | open | one supplied contact generator has a nonzero balanced block | yes: explicit import plus bounded calculation; rate/protection still open |
| Cycle 228/227 physical energy/stress/source | open | number continuity is classified and free `K` fails one candidate-generator commutator | no retirement; action/clock-response route remains live |
| Cycle 204 nonlinear `tan(omega)` clock-map/composition wall | open | the contact probe neither derives the clock readout nor its composition law, and Cycle 204 stores no winding | no retirement; a derived deformed-composition route remains live |
| Cycles 228–229 winding/history wall | open | the sampled `4pi -> 1` alias sharpens the information lost by a wrapped one-step phase | no retirement; autonomous history/winding or an amended-law route remains live |
| `STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md`: statistics not forced by the named substrate | open at forcing resolution | Cycle 230 supplies CAR as a condition rather than deriving it | no retirement; a compiler/derivation is the next target |
| Cycle 229 expectation that a sea alone removes wrapping | rejected for the named fixture | full `L=3` sea plus seam sequence preserves the same warning | same mechanism: explicit counterfixture, not new axiom content |

No similar wall is declared retired by convention or axiom change here. The
partial-closure mechanism that worked is explicit imported structure followed
by a bounded calculation; the next cycle should apply that same discipline to
the `M_64 -> M_2` compiler rather than declare it impossible.

Therefore:

- **N1–N8 PASS for the narrow candidate:** given the supplied CAR cell,
  principal sea cut, and `W_g`, a full
  finite sea and a nonzero first-order momentum-balanced modular channel
  coexist with the prior one-particle mass law;
- **N1–N8 FAIL for every broader claim:** physical instability, decay rate, selected vacuum, physical
  energy, universal seam coupling, compiler impossibility, or axiom need.

The bounded construction is proposed for parking-branch review. The broad
negative and positive claims are not asserted.
