# Conditional flavor mass operator compiler — Cycle 222

**Date:** 2026-07-17

**Authority:** none

**Status:** bounded conditional construction; audit unset

**Constitutional effect:** none

**Packaging:** draft parking branch and draft PR #5389 only

Companion runner:

```text
scripts/conditional_flavor_mass_operator_compiler_cycle222_2026_07_17.py
```

## Result up front

Exact inverse-Cayley embedding of a supplied positive `C3` mass matrix into
one proper-cubic coin succeeds.  Direct block curvature reproduces the three
supplied sector masses and, under the supplied weak identity-coordinate-kick
law, bounded one-axis packets reproduce their inertial response.

The starting point is the repo's previously studied but audit-unset
conditional `C3`-circulant signed-root ansatz

```text
H = a I + B exp(i delta) C + B exp(-i delta) C^dagger.
```

It is not a retained physical flavor-mass operator.  Cycle 222 separately
supplies `r=B^2/a^2=1/2`, the bare-radian phase `delta=2/9`, an overall scale,
the positive-root chamber, the charged-lepton carrier interpretation, and the
map `M_flavor=H^2`.  It then adjoins a zero block and defines

```text
M = 0 direct-sum H^2,
S = (I-iM/3)(I+iM/3)^-1.
```

The Cycle-220 transform recovers `M` from `S` to the stated numerical
precision.  One fixed 24-dimensional register-direction coin `C(S)` contains
the adjoined zero sector and three massive sectors.  There is no species
lookup during propagation or force update.  Spectral host preparation,
source extraction, and pointer writing still use the supplied operator's
eigenvectors or eigenvalues.

At the reference point, direct dispersion extraction from each compiled
six-direction block and an independent fixed-force packet response reproduce
all three supplied `M` eigenvalues.  Supplying `Q=M` gives conditional common
acceleration; an algebraic screen of a wider commuting charge family shows
that this property identifies only the restriction `Q=cM` on the tested
massive subspace, with free normalization.  Charge on the zero sector and
noncommuting charge structure remain unconstrained.

This implements a concrete, runner-checked conditional
spectrum-to-candidate-dynamics interface within the Cycle 219–221 fixtures.
It does not close the physical spectrum-to-matter bridge: spectrum selectors,
carrier identification, Cayley normalization, preparation, response law,
contact law, and field kernels remain supplied.  It is a lossless
spectrum-to-dynamics compiler, not a mass-spectrum derivation.

## Exact compiler and conditioning

The inverse Cayley coordinate used here is standard finite-dimensional
mathematics.  For every finite Hermitian operator `M`, `I+iM/3` is invertible
and

```text
S(M) = (I-iM/3)(I+iM/3)^-1
```

is unitary without eigenvalue `-1`.  Conversely, for a unitary `S` without
eigenvalue `-1`,

```text
M(S) = 3 i (S-I)(S+I)^-1
```

is Hermitian and returns the original coordinate.  Thus the exact statement
is a bijection between all finite Hermitian mass operators and finite
unitaries without `-1`; it is not a positivity or spectrum-selection theorem.
The runner verifies the identity for the conditional flavor block and for an
unrelated indefinite Hermitian operator in a random basis.

The algebraic bijection is not uniformly well-conditioned in floating point.
At the reference hierarchy, `cond(S+I)` is about `483`.  For a sector mass
`m=-3 tan(beta/2)`,

```text
abs(dm/dbeta) = (m^2+9)/6.
```

Across the reference sectors this sensitivity rises from about `1.53` to
`3.50e5`.  The phase change corresponding to a one-percent mass change falls
from about `2.73e-3` to `4.14e-5` radians.  The compiler therefore relocates
the supplied hierarchy into increasingly precise register phases; it does not
compress or explain that hierarchy.  The full spectrum remains encoded in
`S` and `C(S)`.

## Conditional flavor input and retained boundary

The supplied input ledger begins with

```text
r = B^2/a^2 = 1/2,
delta = 2/9 radians,
a = overall scale,
H positive on the selected branch,
M_flavor = H^2.
```

The condition `r=1/2` remains supplied.  The bare-radian hierarchy phase
remains supplied.  In particular, no bridge identifies the repo's
dimensionless value `L_3(1,2)=2/9` with the angle `2/9` radians.  The overall
mass scale remains supplied.  `M_flavor=H^2` remains supplied: the runner
shows that the same compiler transports `H`, `H^2`, and `I+H`, producing
different spectra while satisfying the same Cayley identity.

In contract language: r=1/2 remains supplied, and M_flavor=H^2 remains
supplied.

The retained upstream
[DFT-coordinate theorem](../../../CHARGED_LEPTON_REGISTERED_MASS_DFT_COORDINATE_THEOREM_NOTE_2026-07-11.md)
is narrower.  Every supplied positive mass triple has exact `C3`
discrete-Fourier coordinates and

```text
Q = 1/3 + 2r/3,
```

with `r` unselected.  It neither identifies a physical charged-lepton
operator nor derives the phase.  A July
[registered-angle note](../../../ACPHILAMBDA_R_ETA_VALUE_FACE_REGISTERED_ANGLE_FUNCTIONAL_EXACTNESS_RELOCATION_NOTE_2026-07-05.md)
is context only and is not a Cycle-222 dependency; its current runner is
`26/27` because its Qualification quotation no longer matches the live memo.
Cycle 222 does not repair or consume that foundation-adjacent result.

The reference packet scale is `a=16`.  The irrational offset
`a=16+sqrt(2)` was frozen before evaluation.  Its 64-tick light-sector inertia
estimate misses the predeclared `0.5%` tolerance by about `0.64%`, while its
two heavier sectors remain within `0.01%`.

After that failure, the windows `128,160,192,256` and the weaker forcing were
fixed.  Reference and initial held-out estimates remain within `0.2%` at all
four tested windows; four finite windows do not prove convergence.  Only then
was `a=16+pi` frozen as a post-repair held-out scale.  Its 160-tick result
passes the same `0.2%` criterion.  These scales are numerical lattice-unit
choices, not physical fits.

## Positive-root chamber and Koide boundary

The signed roots are

```text
h_k = a + 2 a sqrt(r) cos(delta + 2 pi k/3).
```

While all three are nonnegative,

```text
Q(H^2) = sum(h_k^2) / [sum(abs(h_k))]^2
       = (1+2r)/3.
```

Near the chosen branch the positive-root chamber is
`abs(delta)<=pi/12`, modulo the `C3` permutations.  At `r=1/2` inside that
chamber, `Q=2/3`; changing `abs(delta)` within the chosen mirror branch
changes both nontrivial normalized mass ratios without changing `Q`.
The spectra at `delta` and `-delta` are identical, so mass data alone cannot
select that mirror or chirality.

This statement fails outside the chamber because squaring erases the sign but
the square root in `Q` restores an absolute value.  The runner retains the
negative control `delta=0.3`: one signed root is negative and
`Q(H^2)=0.634574`, not `2/3`.  Thus neither `r=1/2` nor the formal circulant
surface alone is sufficient.

At the reference conditional point the supplied positive masses are
approximately

```text
0.416797464, 86.181343304, 1449.401859236
```

with normalized ratios approximately

```text
1 : 206.770316 : 3477.472837.
```

These are compiler inputs in arbitrary lattice units, not charged-lepton mass
predictions.

## Operational tournament

For each massive eigensector, the runner compares:

1. the eigenvalue of the compiled `M`;
2. a rest-phase lift whose winding is selected using that same `M`;
3. low-momentum dispersion extracted directly from the compiled block;
4. response to one fixed identity-charge force; and
5. response after separately supplying `Q=M`.

Item 2 is an `M`-informed supplied phase lift, not an independent operational
reading.  Items 3 and 4 are independent numerical responses of the compiled
walk.  Dispersion tracking no longer reconstructs `common_species(beta)` or
uses target branch metadata: it diagonalizes the extracted six-direction
block at neighboring momenta and follows the scalar branch by overlap.

The fixed-force evolution likewise uses the complete compiled coin and no
species lookup during its propagation or force update.  Host code still uses
spectral projectors to prepare the initial three-sector packet and to measure
sector weights.  The experiment is one-coordinate propagation under a
proper-cubic internal coin; the exact 24-frame coin covariance is not itself
a fully rotated three-dimensional packet-response experiment.

Norm, positive normalized sector weights, scalar-band occupancy, and boundary
leakage remain controlled.  Pre, post, and symmetric kick schedules agree for
all three sectors at the repaired 160-tick weak-force protocol.  The frozen
64-tick failure remains visible rather than being removed.

The algebraic charge screen, within the listed commuting family and on the
three massive eigenspaces, is

```text
I, M, 2M, M+7P0, M+I, M^2, and one generic commuting polynomial f(M),
```

where `P0` projects onto the adjoined zero sector.  `M`, `2M`, and `M+7P0`
give sector-independent `q_i/m_i`.  The last is globally different from `M`
but gives bit-for-bit identical response rows when dynamically rerun on all
three tested matter packets.  The other family members are an algebraic
screen.  Hence the evidence fixes at most

```text
Q restricted to support(M) = c M restricted to support(M).
```

It does not fix `c`, the zero-sector charge, or off-diagonal/noncommuting
charge structure.  `Q=M` is inserted, so conditional common acceleration is
not a derivation of gravitational coupling or the equivalence principle.

The Cycle-216 comparison is narrower still.  One host-extracted source mass
and one gradient sampled from the finite scalar field are converted into the
ordinary weak coordinate kick.  The field array does not enter the packet
evolution site by site.  This is a constant-gradient response consistency
check, not local matter-field dynamics and not a gravity theory.

## Adjoined zero sector

The `0` in `0 direct-sum H^2` is supplied and then interpreted as a field
sector.  The runner now extracts that sector and verifies exact equality to
the existing Cycle-214 field coin.  A generic complex packet evolved for
eleven one-axis steps agrees exactly between the complete register coin and
the standalone field coin.

This establishes coexistence inside the compiled coin.  No local vertex in
Cycle 222 couples the zero sector to matter.  The separate Cycle-216 scalar
fixture used for the sampled-gradient response is not generated by this
adjoined block.

## Clock and phase seam

The two heavier reference phases wrap around the unit circle.  Their
`M`-informed winding integers are `5` and `77`; the light sector uses `0`.
The principal phase does not determine the winding.  Discrete unitary
evolution therefore supplies quasienergy modulo `2 pi`, while dispersion and
fixed-force inertia remain locally measurable without choosing a global
phase lift.

A physical clock, continuation history, or composition law must determine
whether and how a winding is observable.  Until that is supplied or derived,
rest-phase equality is conditional and may not be counted as independent
support for the mass bridge.

## Binding, composition, and pointers

The compiled register can occupy the supplied Cycle-210 shared contact
sector, but the Cycle-221 diagnosis survives every flavor change:
equal-direction kinematics keeps the prepared object coincident.  Identity
contact, rest-phase deletion, and register deletion remain coincident;
deleting the complete contact replacement releases the object.  The mass
operator controls phase and tested response but does not cause binding.

The supplied additive operator

```text
M_total = M tensor I + I tensor M
```

factorizes the corresponding rest unitary.  This checks the chosen
composition rule at both reference and held-out scales; it excludes binding
and field energy and does not derive composition.

A reversible controlled-projector write correlates one supplied mass
eigenspace with an abstract two-state pointer, and a second unitary creates a
redundant copy.  These orthogonal redundant pointers preserve the matter mass
operator at operator level and preserve the prepared pointer-sector norm
weights.  They are not permanent Records, do not select an outcome, and do
not implement a local record-formation map.  Earlier declared
spectator-factor/record-count bookkeeping tests remain the campaign's
redundancy control; Cycle 222 adds only the narrower coherent-pointer check.

## Ontology and Qualification boundary

The conditional bare-metal interpretation is that mass is an eigenvalue of a
conserved working-state operator.  It is not archive count and is not a
species number consulted during the update.  This interpretation is not yet
licensed by the current one-site foundation.

Qualification remains open.  The coherent register amplitudes must ultimately
be one of:

1. derived from the complete record corpus;
2. eliminated operationally into a record-to-record process kernel; or
3. admitted explicitly as a wider law-governed ontology.

The candidate also prices a 24-dimensional register-direction coin against
the foundation's one-site `M2(C)` algebra.  No strict nearest-neighbour
one-qubit encoding, lawful preparation, autonomous population, or physical
pointer/Record interface is supplied here.  That mismatch cannot be hidden by
calling the register a label.

## Supplied-content ledger

This compiler does not derive or select:

- the `C3`-circulant signed-root ansatz `H`, its cyclic generator/basis, or
  the unresolved `delta` versus `-delta` mirror;
- the physical identification of the formal `C3` carrier with charged
  leptons;
- the positive-root chamber, `r=1/2`, or the holomorphic polarization;
- `delta=2/9` radians, its exactness, or a dimensionless-to-radian bridge;
- `M_flavor=H^2` rather than another positive function of `H`;
- the overall scale, hierarchy ordering, or observed mass values;
- the adjoined zero block or its field interpretation;
- the inverse-Cayley normalization `3` and common-cone rest map;
- the Cycle-219/220 coin and update law `C(S)`, including its projector split,
  even-sector phase, and directional streaming;
- the full 24-dimensional local register-direction ontology;
- spectral packet preparation, phase winding, or clock branch;
- the interpretation of `M` eigenvalues, block curvature, and `F/a` under a
  supplied identity-coordinate kick as mass and inertia;
- the contact trigger, shared-register ownership, or persistent object;
- the coordinate kick, `Q=M` charge law, or coupling normalization;
- restriction to a commuting charge family, zero-sector charge, or
  noncommuting charge structure;
- additive composition, binding energy, or field energy;
- the scalar Green fixture, source extraction, local field coupling, or
  nonlinear/tensor gravity;
- occurrence, permanent Record formation, readout statistics, or Born
  frequencies;
- the abstract pointer Hilbert spaces, projector-controlled write/copy,
  squared-norm weights, or coherent working-state ontology; or
- particle abundance, chirality, gauge charge, and boundary conditions.

It is not a mass-spectrum derivation, not a gravity theory, and not an axiom
result.  There is no axiom conclusion.

## Attribution and novelty boundary

Koide's charged-lepton relation is prior phenomenology: Y. Koide,
*Fermion-boson two-body model of quarks and leptons and Cabibbo mixing*,
*Lettere al Nuovo Cimento* 34, 201–205 (1982):

<https://doi.org/10.1007/BF02817096>

Cyclic Hermitian three-family textures are also prior work; see Koide:

<https://arxiv.org/abs/hep-ph/0005137>

The explicit `Z3` cosine parameterization and empirical
`delta_L approximately 2/9` attribution appear in P. Żenczykowski:

<https://arxiv.org/abs/1301.4143>

Carl Brannen's unpublished manuscript *The Lepton Masses* is a historical
source for the observation:

<https://brannenworks.com/MASSWS2.pdf>

Rivero and Gsponer discuss the related Koide/Brannen setting and display a
cyclic matrix; that paper is theirs, not Brannen's:

<https://arxiv.org/abs/hep-ph/0505220>

Apadula, Bisio, D'Ariano, and Perinotti already treat mass as an extra quantum
degree of freedom in a Dirac quantum walk:

<https://arxiv.org/abs/1806.03940>

Finite-dimensional Cayley parametrization of unitaries, dynamical mass
operators, equality conditions among rest, inertial, and gravitational
internal-energy operators, cyclic Hermitian flavor textures, and mass as a
quantum-walk degree are prior work.  See, respectively:

- <https://doi.org/10.1016/j.laa.2023.10.017>
- <https://arxiv.org/abs/1205.1372>
- <https://arxiv.org/abs/1502.00971>

Cycle 222 claims none of those ingredients as new.  Its bounded repo-local
contribution is their explicit executable composition with the Cycle-220
proper-cubic coin and the stated multi-readout and ablation tournament.  No
global novelty search has established that composition as literature-new.

This work remains only on the draft parking branch and draft PR #5389.  It
changes no foundation, axiom, primitive, registry, policy, queue, or audit
surface.

## Verification

```text
python3 scripts/conditional_flavor_mass_operator_compiler_cycle222_2026_07_17.py
```
