# Cubic Covariance Exact-Repair Tournament

**Date:** 2026-07-14

**Type:** meta

**Authority:** none. This is an exact finite-matrix construction and a bounded
adversarial route tournament. It is not an axiom candidate, an audit verdict,
a selection of the universe's update law, or permission to change a live
registry surface. It changes no axiom, primitive, queue, or audit state.

Companion runner:

```text
scripts/cubic_covariance_exact_repair_tournament_2026_07_14.py
```

## Result Up Front

The Cycle-7 ordered split-step defect has an exact constructive repair on a
finite carrier:

> The direct sum of all six axis orders is an exact full-cubic finite-range
> unitary with the Weyl first derivative.

For every permutation `pi` of `x,y,z`, let

```text
U_pi(k) = product over i in pi of [cos(k_i) I - i sin(k_i) sigma_i]
```

and define

```text
B(k) = direct_sum over pi in S3 of U_pi(k).
```

`B(k)` acts on an orientation register of dimension six tensored with the
two-dimensional Weyl coin, hence on `M12`. A proper cubic rotation `R` acts by
the unsigned permutation of the six order labels together with the ordinary
spin-half representative `S_R`. With

```text
T_R = P_R tensor S_R,
```

the runner verifies the exact generator identities

```text
T_R B(k) T_R^dagger = B(Rk).
```

The two checked generators produce all 24 proper cubic rotations, so their
identities give full proper-cubic covariance. Every block is a product of
three existing standard-cubic conditional edge shifts. The construction is
exactly unitary and finite range, and

```text
i partial_i B(0) = I_6 tensor sigma_i.
```

Thus it initially contains six degenerate Weyl orientation tastes.

There is also an exact invariant onsite mixer on the orientation register:

```text
P_sym   = J_6 / 6,
C_clock = 2 P_sym - I_6,
W(k)    = (C_clock tensor I_2) B(k).
```

`C_clock` commutes with every order permutation, is unitary, and leaves one
symmetric clock mode at phase `+1` while putting five orientation modes at
phase `-1`. Therefore `W` is still exact, finite-range, unitary, and
full-cubic, with one two-dimensional Weyl low-phase sector at the origin.

This positive result **does reduce the exact-law residue**. It retires both
“perhaps exact cubic covariance is impossible” and “perhaps the Lattice axiom
must be enlarged to BCC adjacency.” It does not select this repair as nature's
law. Its remaining price is explicit:

- a coherent six-state order/orientation register;
- an exact block embedding and cubic action on that register;
- the supplied `pi` clock phase in `C_clock`;
- eight spatial corners distributed across quasienergies `0` and `pi`;
- an unresolved Floquet chirality/doubling account;
- physical identification of time/tick and macro-step;
- interactions, gauge structure, state-sector preparation, and the record
  instrument.

`M12` is not a tensor power of primitive qubits. The smallest full qubit block
large enough is `M16`, from four primitive qubits, with a 12-dimensional
encoded sector and four spectator or separately gapped dimensions. Nothing
here proves that this encoded action is automatically the geometric rotation
action of a particular four-site block.

Most importantly, **primitive M2 remains open**. The tournament proves no
broad arbitrary finite-range M2 no-go. It proves only that several natural
repair families fail and that a finite block succeeds.

`M12` is minimal only in the precise **permutation orbit-completion** class:
the full cubic orbit of `U_xyz` contains six distinct ordered blocks at a
generic exact momentum, so any block-diagonal carrier that retains one copy of
each rotated image needs `6 x 2=12` dimensions. No global minimality is
claimed. A coherent non-orbit dilation or an arbitrary primitive-`M2` law
could be smaller.

## What This Does — And Does Not — Ask of the Axioms

No Lattice-axiom edit and no Qubit-axiom edit is needed for existence of an
exact cubic Weyl macro-law. Standard-cubic edges already carry every
constituent shift, and a finite block can carry the repair if the framework's
finite-composition bridge lands.

That is a compatibility theorem, not a derivation of the kinetic law. The
present axioms still do not choose `B`, `C_clock`, a block code, a handed
sector, an interacting completion, or a sampled record law. Putting any of
those choices into constitutional text would over-read this result. The exact
repair belongs first as a conditional theorem consuming a named law import.

Conversely, failure of the simple same-coin repairs below is not evidence that
the axiom must carry an orientation clock. The positive block is a witness of
possibility; uniqueness and selection remain separate questions.

## Foundation and Primitive Boundary

The live foundation supplies the standard lattice `Z3`, its six nearest
neighbors and proper cubic rotations, one `M2(C)` algebra per primitive site,
a static nearest-neighbor admissibility rule, and append-only readable
records. The registered realized-state primitive supplies a pointwise
realized slot. It does not supply a selector, measure, unitary, randomizer,
orientation clock, time step, tensor-block code, or record-formation
instrument.

The direct-sum construction is therefore an exact answer to a mathematical
existence question. Its physical use remains conditional on a justified
finite-composition and encoding bridge. The generated finite-composition work
is a possible retirement route for part of that bridge, not authority silently
claimed here.

## Primary-Literature Boundary

The literature is used to locate the problem, not to inflate the runner's
finite checks:

- D'Ariano, Erba, and Perinotti classify minimal-coin isotropic walks in their
  stated homogeneous Cayley-graph setting and find the three-dimensional BCC
  Weyl solutions:
  [Isotropic quantum walks on lattices and the Weyl equation](https://arxiv.org/abs/1708.00826).
- Bisio, D'Ariano, Perinotti, and Tosini give the exact Weyl and paired Dirac
  QCAs and their continuum sectors:
  [Free quantum field theory from quantum cellular automata](https://arxiv.org/abs/1601.04832).
- Raynal independently analyzes unitarity constraints for three-dimensional
  Weyl quantum cellular automata:
  [Simple derivation of the Weyl and Dirac quantum cellular automata](https://arxiv.org/abs/1703.05890).
- D'Ariano, Perinotti, and Tosini show how scalar walks and coarse-grained
  blocks can carry relativistic behavior, emphasizing that carrier size and
  coarse graining are substantive parts of the construction:
  [Theoretical foundations of quantum cellular automata](https://arxiv.org/abs/1902.10227).

Those classifications have their own graph, homogeneity, locality, carrier,
and isotropy hypotheses. None is cited here as a theorem excluding every
finite Laurent-polynomial `M2` unitary on the present standard-cubic carrier.
Nielsen-Ninomiya-type results likewise constrain chirality under their stated
Hamiltonian/regularity assumptions; they do not by themselves settle this
discrete-time Floquet carrier.

## Route 1 — Finite Phase Cycling

The proper cubic group sends one ordered split step through all six axis
orders. The signed-axis stabilizer of one order has size four, giving orbit
size six.

Cycling only the three even permutations is insufficient. Those three close
under the 120-degree body-diagonal rotation, but a 90-degree cubic rotation
maps them to the three odd permutations. So a three-phase cycle can respect an
index-two rotational subgroup but not all 24 proper cubic rotations.

A deterministic six-phase clock has another exact obstruction if the six
phases are exactly the regular order labels. A phase permutation commuting
with every left `S3` order action must lie in the right-regular centralizer.
The runner exhausts all `6!` permutations and finds exactly six:

```text
identity:          six 1-cycles
three elements:   three 2-cycles
two elements:     two 3-cycles
```

There is no commuting single six-cycle. Hence a full-covariant deterministic
permutation clock on these labels splits into at least two cycles. Extra
invariant coherent mixing can gap that multiplicity; `C_clock` below is one
such exact mixer. The mixer is additional law content, not forced by the
group action.

## Route 2 — Group/Orbit Twirling

The amplitude average over all six orders collapses exactly to

```text
A(k) = c_x c_y c_z I
     - i [s_x c_y c_z sigma_x
          + c_x s_y c_z sigma_y
          + c_x c_y s_z sigma_z].
```

This is finite range, exactly full-cubic, and has the Weyl first derivative.
It is not unitary. At

```text
c_x=c_y=c_z=s_x=s_y=s_z=1/sqrt(2),
```

the runner obtains exactly

```text
A^dagger A = (1/2) I.
```

This is not a normalization nuisance: momentum-dependent polar
renormalization generally destroys finite range.

Twirling the unitary channels rather than their amplitudes is completely
positive, trace preserving, finite range, and cubic covariant, but it is not a
unitary channel. At the same exact momentum it sends `|0><0|` to

```text
[[1/2, 1/6],
 [1/6, 1/2]],
```

with purity `5/9` and determinant `2/9`. It could be a sampled or open-system
law only after its randomizer/environment and record semantics are supplied.

## Route 3 — Palindromic Products

The Cycle-7 half-angle Strang expression needs a precise locality caveat. An
individual factor `S_i(k_i/2)` is anti-periodic under `k_i -> k_i+2 pi`, so it
is not itself a translation-invariant primitive `Z3` substep. The complete
five-factor macro contains each half-axis twice. Its signs cancel, its Laurent
powers are integral, and the complete macro can be a legal finite-range
unitary. The illegality attaches to treating the half-factor as an independent
primitive shift, not to the whole macro polynomial.

The entirely primitive full-shift palindrome

```text
P(k) = S_x S_y S_z S_z S_y S_x
```

is exactly unitary and finite range. It approximates

```text
exp[-2 i (k_x sigma_x+k_y sigma_y+k_z sigma_z)]
```

with third-order local error. Its cubic covariance defect also begins at third
order, but an exact rational fixture proves the defect is nonzero. Palindromic
ordering improves the continuum approximation by one order; it does not give
exact full-cubic covariance.

## Route 4 — Once-Each Orbit Products

Another natural repair multiplies each of the six ordered walks exactly once,
hoping the full orbit cancels the order dependence. Product order still
matters. The runner enumerates all `6! = 720` once-each products at a generic
exact Gaussian-rational momentum fixture and compares each against both cubic
generators. No product is covariant under both.

This is a strict finite-class result. It does not exclude products with
repeated orbit elements, momentum-dependent coefficients, ancillary carriers,
quantum-signal-processing sequences, or arbitrary paraunitary Laurent
polynomials.

## Route 5 — Exact Orientation-Block Repair

The direct sum succeeds because a cubic rotation may permute the order sector
rather than demanding that one two-dimensional block be fixed:

```text
B(k) = direct_sum_pi U_pi(k).
```

For a signed axis permutation `R`, let `rho_R` be its unsigned permutation.
The spin action sends each conditional shift to the corresponding signed
rotated shift, so

```text
S_R U_pi(k) S_R^dagger = U_(rho_R pi)(Rk).
```

The left-regular permutation matrix `P_R` moves the source block to that new
label, giving

```text
(P_R tensor S_R) B(k) (P_R tensor S_R)^dagger = B(Rk).
```

Every factor still uses one current standard-cubic edge. Direct sum and an
onsite orientation mixer do not enlarge spatial range.

Within this exact orbit-completion construction the carrier size is forced:
orbit-stabilizer gives six labels, and the runner verifies that all six blocks
are distinct at a generic exact fixture. This establishes `M12` minimality
inside that class only, not among all possible cubic paraunitaries or
dilations.

At `k=0`, every order has the same derivative. The price of covariance is
therefore initially six identical orientation tastes, not six different
continuum velocities.

### Invariant clock gap

The symmetric clock vector is fixed by every order permutation. The reflection

```text
C_clock = 2 |sym><sym| - I_6
```

is consequently unitary and cubic invariant. Multiplying `B` by it gives a
phase-`+1` two-dimensional symmetric sector and a phase-`-1` ten-dimensional
orthogonal sector at the origin. Compressing the first derivative to the
symmetric sector gives exactly `sigma_i`.

This is an exact orientation-taste gap at one continuum point. It is not a
complete species theorem. At all eight momenta with each `k_i` equal to `0` or
`pi`, every order block is the same scalar `+I` or `-I`. Consequently the
repaired law retains eight spatial corners across the two clock
quasienergies. The runner deliberately does not assign their net chirality:
that requires a proper Floquet-band and quasienergy analysis.

### Carrier cost

An abstract `6 x 2` carrier is `M12`. A tensor block of primitive qubits has
dimension `2^n`, so four qubits (`M16`) are the smallest uncompressed carrier.
A physical realization must provide:

- a 12-dimensional invariant code;
- four spectator states and their harmless dynamics;
- the exact rotation representation on the chosen geometric block;
- finite local gates or a direct admissibility/update law implementing `W`;
  and
- stability of the code and gap under interactions and records.

The dimension count proves room, not implementation.

## Is the Internal Clock Physics or Scheduling?

For this construction, the internal phase is physical carrier content. The
six `U_pi` are different exact maps because the Pauli shifts do not commute.
`C_clock` coherently mixes their labels. A superposition of labels and its
relative phase affect later amplitudes, so the label cannot simultaneously be
declared a mere execution-order linear extension.

This sharpens the relation to causal schedule equivalence:

- If multiple schedules are merely total-order linear extensions of one fixed
  causal predecessor DAG and produce the same boundary map, schedule can be
  gauge.
- Here, replacing `xyz` by `yxz` changes the exact boundary unitary at order
  `k^2`. That equality premise fails.
- A future formulation might make phase boundary-reconstructible from a
  richer causal structure, avoiding a persistent onsite clock record. No such
  reconstruction theorem is proved here.
- A live-read asynchronous order can change permanent records and is plainly
  physical; this probe does not use such record feedback.

Accordingly the current block clock is neither an unobservable simulator loop
index nor a free global scheduler. It is an encoded internal degree of freedom
unless a separate causal reconstruction retires it.

## Primitive `M2` Route — Narrow Result, Broad Open Problem

The simplest real, range-one, standard cubic-covariant ansatz is

```text
U(k) = [a+c sum_i cos(k_i)] I - i b sum_i sin(k_i) sigma_i.
```

Exact unitarity requires

```text
[a+c sum cos]^2 + b^2 sum sin^2 = 1
```

pointwise. The cross term `cos(k_x)cos(k_y)` forces `c=0`; then the
`cos^2(k_x)` coefficient forces `b=0`; only the constant phases `a=+/-1`
remain. So this natural range-one ansatz cannot carry a nontrivial Weyl
unitary.

This is **no broad arbitrary finite-range M2 no-go**. Higher Laurent range,
more intricate paraunitary factorizations, momentum-dependent scalar/vector
terms, and non-split constructions remain unclassified in this probe.

The exact finite-range Hamiltonian

```text
H(k) = sum_i sin(k_i) sigma_i
```

shows why the conjunction matters: `H` is exactly cubic and Weyl at first
order, and `exp(-itH)` is exactly cubic and unitary. For nonzero generic `t`,
its one-axis restriction contains `exp[+/- i t sin(k)]`, which has infinitely
many Fourier harmonics, so the exact exponential is not finite range. The
block construction is the route found here that satisfies all four demands at
once.

## Collapsed-Wall Truth Table

| Fixture | Weyl first order | exact cubic | exact unitary | finite range |
|---|---:|---:|---:|---:|
| ordered split step | yes | no | yes | yes |
| six-order amplitude twirl | yes | yes | no | yes |
| exponential of covariant `H` | yes | yes | yes | no |
| orientation block `W` | yes | yes | yes | yes |
| identity | no | yes | yes | yes |

This table matters because it shows that covariance, unitarity, finite range,
and the Weyl derivative are logically distinct walls. The block result is not
obtained by re-labeling any one of them.

## No-Go-Discipline Stress Test

### N1 — Alternative routes

The tournament explicitly tested or bounded:

1. the original ordered split step;
2. three-phase even-order cycling;
3. all six deterministic order phases;
4. six-order amplitude twirling;
5. six-order channel twirling;
6. half-step and full-step palindromes;
7. all 720 once-each orbit products;
8. a direct-sum orientation block;
9. an invariant coherent clock mixer;
10. a narrow real range-one primitive-`M2` ansatz; and
11. an exactly cubic Hamiltonian followed by exponentiation.

Unsearched routes remain named: arbitrary finite-range `M2` paraunitaries,
repeated or weighted product formulas, smaller nonregular dilations,
quantum-signal-processing constructions, causal-phase reconstruction, and
interacting/gauge completions.

### N2 — Wall independence

The collapsed-wall table gives a concrete witness for failure of each property
while the other three can survive. The positive orientation block satisfies
all four. Therefore “unitary,” “finite range,” “cubic,” and “Weyl first
order” were not treated as synonyms, and the negative fixtures do not share
one hidden generic failure.

### N3 — Hidden-wall scan

The positive block exposes rather than hides:

- finite tensor composition and the `M12`-inside-`M16` code;
- the coherent order register and its cubic representation;
- the supplied clock phase and selected symmetric quasienergy sector;
- the distinction between physical internal phase, a
  boundary-reconstructible causal phase, and an execution-order linear
  extension;
- macro-range versus whether an apparent half-step is a legal primitive
  substep;
- a handed/Floquet species analysis at all eight corners;
- preparation near the chosen node;
- time orientation and tick identification;
- interaction/gauge stability; and
- the record instrument and sampled outcome law.

None is supplied by the realized-state primitive.

### N4 — Residual matching

The Cycle-7 exact `O(k^2)` proper-cubic defect is retained as the target, not
replaced by a generic “lattice anisotropy” slogan. D'Ariano-style
classifications are used only inside their graph/carrier/isotropy hypotheses.
Hamiltonian doubling theorems are not silently extended to arbitrary Floquet
walks. Finite generated composition is recorded as a bridge still needing
physical realization. The exact positive block directly matches the missing
covariance identity.

### N5 — Rhetoric and scope

Every negative conclusion is finite and named:

- the equal-amplitude six-order twirl is nonunitary;
- the corresponding channel twirl is nonunitary as a channel;
- no once-each product among the 720 tested is fully covariant;
- no commuting permutation of the regular order register is one six-cycle;
- the displayed full-shift palindrome is not exactly cubic; and
- the displayed range-one `M2` ansatz is trivial under exact unitarity.

There is no claim that all primitive-`M2` laws, all dilations, all clocks, all
blocks, or all cubic QCAs are excluded.

### N6 — Partial-closure paths

Several useful partial routes survive:

- the ordered walk already resolves BCC support into present cubic edges;
- a palindrome improves the covariance defect from second to third order;
- amplitude twirling gives an exact cubic finite-range contraction;
- channel twirling gives an exact cubic finite-range CPTP law;
- the six-order block gives exact cubic finite-range unitarity;
- `C_clock` isolates one Weyl phase sector at the origin; and
- a causal reconstruction theorem could someday retire the persistent clock
  interpretation.

These are recorded as constructive rungs, not dismissed because they do not
complete the TOE.

### N7 — Steelman

The strongest live alternative is that a smaller or primitive-`M2`
paraunitary Laurent polynomial exists and the six-order block is extravagant.
The literature found does not close that class, and this tournament did not
enumerate it. A second strong alternative is that order phase is reconstructible
from an exact causal boundary and need not be stored as an internal state. Both
would improve the result and remain legitimate open searches.

### N8 — Cross-cycle echo

Two earlier warning patterns recur. First, Cycle 7 retired an apparent BCC
geometry residue by showing it was generated by cubic micro-edges; this cycle
likewise retires an apparent exact-covariance impossibility by enlarging the
derived carrier, not the constitution. Second, schedule-equivalence work shows
that a total simulator order can be gauge only when the causal boundary map is
order-independent. The present noncommuting order maps fail that condition,
so calling the clock “mere scheduling” would repeat a convention/physics
collapse in the opposite direction.

## Exact-Law Residue After the Repair

The repair removes one existence uncertainty, but selection remains:

```text
retired:
  BCC adjacency as new primitive geometry
  exact full-cubic finite-range unitary existence with a Weyl sector on a finite block

still exact-law content:
  carrier/block code and rotation representation
  clock mixer phase
  chirality and spatial-corner treatment
  physical time/tick and macro-step interpretation
  interaction and gauge law
  prepared low-energy/quasienergy sector
  record instrument and outcome law

still open mathematically:
  arbitrary primitive-M2 finite-range paraunitary repair
  smaller exact dilation
  causal/boundary reconstruction of the phase
```

So this probe argues against an axiom addition for cubic covariance. It also
argues against treating the block construction as derived physics merely
because it exists. The honest next object is a conditional theorem: if the
exact encoded block law and its clock mixer are imported, then the present
lattice and qubit substrate supports a full-cubic finite-range unitary Weyl
sector. Whether that law is forced, empirically selected, or replaceable by a
smaller construction remains open science.
