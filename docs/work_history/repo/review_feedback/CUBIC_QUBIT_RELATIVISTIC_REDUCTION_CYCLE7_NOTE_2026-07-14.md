# Cubic-Qubit Relativistic Reduction — Cycle 7

**Date:** 2026-07-14

**Type:** meta

**Authority:** none. This is a literature-grounded compatibility study and an
exact finite algebraic probe. It is not an axiom candidate, an audit verdict,
or a claim that a free one-particle kinetic law is the framework's complete
sampled-record law. It changes no live axiom, primitive, registry, or audit
surface.

## Result Up Front

The strongest relativistic route found in this cycle does **not require a
Lattice-axiom edit** and does **not require a Qubit-axiom edit**:

> A published three-dimensional Weyl quantum-cellular-automaton macro-step on
> the body-centered-cubic graph factors exactly into three conditional shifts
> along ordinary nearest-neighbour edges of the present standard cubic graph.

In momentum variables, set

```text
S_i(q_i) = cos(q_i) I - i sin(q_i) sigma_i.
```

Then the exact product

```text
U_-(q) = S_x(q_x) S_y(q_y) S_z(q_z)
```

is the published `A^-` Weyl walk, while

```text
U_+(q) = S_x(q_x) S_y(-q_y) S_z(q_z)
```

is its opposite-handed `A^+` partner. Each factor propagates only along one of
the six edges already named by the Lattice axiom. Their three-step support is
the eight body diagonals. Thus the BCC adjacency can be a derived macro-graph,
not new bare geometry.

This is a real compatibility result, but it does not derive the update law.
The exact ordered product, its three-phase schedule, time orientation, Pauli
frame/handedness, block/Fock interpretation, mass or Wilson parameter, physical
species branch, and low-momentum state restriction all remain law-level
content or downstream theorem obligations. The exact micro-law is unitary and
periodic on the Brillouin zone. The rotationally symmetric Weyl equation is a
continuum effective law: the ordered product differs from it at order `q^2`
and is not exactly covariant under every proper cubic rotation.

So the route removes a possible constitutional geometry/carrier change, but
it does not remove the need to identify the universe's fixed update law. It
reduces constitutional content in one place and exposes law-level content in
another.

## Foundation Used, And Nothing More

The present foundation supplies:

- the standard lattice `Z^3`, its six nearest neighbours, translations, and
  proper cubic rotations;
- one algebra `M_2(C)` at each primitive site;
- a static nearest-neighbour-covariant menu rule; and
- append-only readable records.

The Admissibility axiom expressly does not supply dynamics. The registered
kinetic-isotropy primitive supplies the structural equality `c_t=c_s`; it does
not supply an update operator, Lorentz invariance, a time step, a mass, a
chirality selector, or a sampled outcome law. The scale-reference and
realized-state primitives likewise do not provide those items.

The finite tensor-product composition needed for a block route may ultimately
be derivable from commuting faithful local embeddings plus generatedness. That
is a live retirement path, not authority silently assumed here. The probe uses
finite matrices only to establish what such a block could carry if the
composition bridge lands.

## Primary Literature Boundary

The literature claims used here are limited to primary sources:

- D'Ariano, Erba, and Perinotti classify homogeneous local isotropic quantum
  walks with minimal coin `s=2`. In three dimensions their nontrivial solution
  is on a BCC Cayley graph and leaves two Weyl walks:
  [Isotropic quantum walks on lattices and the Weyl equation](https://arxiv.org/abs/1708.00826).
- Bisio, D'Ariano, Perinotti, and Tosini give the exact BCC Weyl matrices and
  couple opposite sectors into a four-component Dirac QCA with a normalized
  mass parameter:
  [Free quantum field theory from quantum cellular automata](https://arxiv.org/abs/1601.04832).
- Bialynicki-Birula constructs a synchronous discrete-time Weyl evolution from
  eight body-diagonal neighbours and gives the four-component massive
  coupling:
  [Weyl, Dirac, and Maxwell equations on a lattice as unitary cellular automata](https://arxiv.org/abs/hep-th/9304070).
- Nielsen and Ninomiya establish the paired-chirality obstruction under their
  stated regularity/locality assumptions:
  [Absence of neutrinos on a lattice](https://doi.org/10.1016/0370-2693(81)91026-1).
- Susskind's three-spatial-dimensional staggered construction identifies the
  simplest result as an isodoublet of massless Dirac fields:
  [Lattice fermions](https://doi.org/10.1103/PhysRevD.16.3031).
- Wilson supplies the lattice gauge-theory construction whose additional
  momentum-dependent term lifts the naive corner modes:
  [Confinement of quarks](https://doi.org/10.1103/PhysRevD.10.2445).

The runner does not re-prove the published classifications or their interacting
field-theory claims. It exactly checks only the finite identities stated below.

## Route 1 — Ordered Cubic Split-Step QCA

### Exact micro-law

Writing `c_i=cos(q_i)` and `s_i=sin(q_i)`, direct Pauli multiplication gives

```text
U_-(q) = u_-(q) I - i sigma . n_-(q),

u_-   = c_x c_y c_z - s_x s_y s_z,
n_-x  = s_x c_y c_z + c_x s_y s_z,
n_-y  = c_x s_y c_z - s_x c_y s_z,
n_-z  = c_x c_y s_z + s_x s_y c_z.
```

These are exactly the published BCC `A^-` expressions. Reversing the sign of
the middle conditional shift gives the published `A^+` expressions. The
identity is symbolic, not a continuum fit. Because every `S_i` is unitary,
the product is exactly unitary for every lattice momentum.

In position space, each substep moves conditional amplitudes by `+e_i` or
`-e_i`. After the ordered `x,y,z` sequence the support is exactly

```text
(+/-1, +/-1, +/-1),
```

the eight BCC body diagonals. Every constituent move is nevertheless one
standard-cubic nearest-neighbour edge. The earlier apparent BCC-versus-cubic
constitutional fork is therefore resolved constructively if a three-substep
macro-law is allowed.

### Continuum effective law

At `q=0`,

```text
i partial_i U_-(0) = sigma_i.
```

Therefore

```text
U_-(q) = I - i(q_x sigma_x + q_y sigma_y + q_z sigma_z) + O(|q|^2).
```

The probe confirms second-order convergence to the unsplit Weyl exponential.
A time-symmetric five-factor splitting improves the local error to order
`|q|^3`, but still supplies an ordered update prescription.

This distinction is load-bearing. A 90-degree cubic rotation maps the
first-order Weyl term covariantly, but the exact ordered product has a nonzero
covariance defect beginning at order `|q|^2`. The exact D'Ariano BCC walk is
isotropic under the particular transitive generator symmetry used in the
classification; that is not the same assertion as exact covariance of this
single ordered split-step under all 24 proper cubic rotations named in the
live Lattice axiom.

Possible repairs include a cyclic physical phase, a symmetrized composition,
or a larger block whose phase is internal. Each is additional exact law
content until selected by a deeper forcing theorem. A global three-phase
schedule is not contained in a single `M_2` site; if phase must itself be a
local physical state rather than a global law clock, it needs a block carrier.

### Supplied atoms on this route

The exact factorization still consumes:

1. the exact three-factor update and its coefficients;
2. an axis order or an exact phase-cycling/symmetrization rule;
3. a choice of handed Pauli frame (`A^+` versus `A^-`, or both);
4. a time orientation and identification of one macro-step with a physical
   or emergent tick;
5. a state sector concentrated near the selected continuum node, together
   with a controlled scaling limit;
6. a block/composition interpretation if the law is to be a many-body field
   rather than a one-particle quantum walk; and
7. an interacting/gauge completion with stability of the effective light
   cone under renormalization.

The approved equality `c_t=c_s` can reduce the independent speed bookkeeping.
It does not select any item above.

## Route 2 — Bipartite/Staggered `2^3` Block

This route remains fully compatible with one `M_2` per primitive site because
it uses several primitive sites as one effective carrier. On the eight parity
vertices `a in {0,1}^3`, define

```text
(Gamma_i psi)(a) = eta_i(a) psi(a xor e_i),
eta_i(a) = (-1)^(sum of a_j preceding i).
```

The runner verifies exactly

```text
{Gamma_i,Gamma_j} = 2 delta_ij I_8.
```

The bipartite parity operator

```text
epsilon(a) = (-1)^(a_x+a_y+a_z)
```

anticommutes with every `Gamma_i`. Hence the finite free block

```text
H_stag = sum_i sin(k_i) Gamma_i + m epsilon
```

satisfies

```text
H_stag^2 = [sum_i sin^2(k_i) + m^2] I_8
```

exactly. No primitive-site algebra change is needed.

The eight-dimensional representation is not one four-component Dirac field.
The commutant of the four displayed Clifford generators has dimension four,
so it contains a two-dimensional multiplicity space: two Dirac tastes. This
matches Susskind's primary-source isodoublet statement. Removing one taste is
not achieved by renaming a block origin; it needs an additional projection,
rooting, boundary, interaction, or other physical selection whose locality and
record consequences must be proved.

The runner also tests the apparent convention residue. All six axis orderings
of the Kawamoto-Smit signs are related by local sign gauge transformations and
constant axis signs. A choice of coordinate ordering is therefore not, by
itself, six new physical constants. The eight possible block origins modulo
two likewise may be coordinate convention if observables and translation
action are shown to be origin-independent. The physical residue is instead:

- which exact staggered kinetic operator is the update law;
- how the eight primitive qubits compose into the effective one-particle or
  many-body carrier;
- the fermionic occupation/CAR structure and physical number sector;
- the two-taste content or a proved taste-reduction mechanism;
- the mass coefficient and any interaction/gauge links; and
- the time/continuum identification.

This corrects an over-broad reading of “one qubit forces staggered.” One
primitive onsite `M_2` cannot contain an independent four-generator Dirac
Clifford algebra, but a finite block of primitive sites can. Staggering is one
economical escape, not a theorem excluding every block-Wilson or Floquet
route.

## Route 3 — Block Wilson/Dirac Law

Let an effective four-dimensional block carry

```text
alpha_i = tau_x tensor sigma_i,
beta    = tau_z tensor I.
```

These matrices satisfy the Dirac Clifford relations exactly. The standard
spatial Wilson block has

```text
H_W(k) = sum_i sin(k_i) alpha_i
       + [m + r sum_i (1-cos(k_i))] beta.
```

It is range-one on the standard cubic graph at the effective-block level and
squares exactly to a scalar. At the eight spatial Brillouin-zone corners, for
`m=0,r=1`, the effective masses are

```text
0, 2, 4, 6     with degeneracies     1, 3, 3, 1.
```

Thus the seven non-origin spatial sine nodes are lifted in this free spatial
probe. The exact law nevertheless contains a supplied Wilson parameter `r`
and bare mass `m`, uses an effective `M_4` block, and breaks the naive chiral
symmetry used by the unwanted partner modes. It does not select a generation,
mass hierarchy, gauge representation, or outcome law. A complete Euclidean
space-time doubling or interacting continuum proof is outside this finite
spatial calculation.

The route is therefore compatible with the Qubit axiom only through a derived
block-composition theorem. It is not compatible with the claim that one
primitive onsite `M_2` alone already carries a massive Dirac particle.

## The Narrow Onsite-Mass Theorem

For a general complex `2 x 2` matrix

```text
B = a_0 I + a_x sigma_x + a_y sigma_y + a_z sigma_z,
```

the three conditions

```text
{B,sigma_x}={B,sigma_y}={B,sigma_z}=0
```

force `a_0=a_x=a_y=a_z=0`. Thus one primitive onsite `M_2` that already uses
all three Pauli directions for a Weyl kinetic term has no nonzero
momentum-independent Dirac mass matrix.

This is the only no-go retained from the cycle. It is deliberately narrow:
an `M_4` block, a staggered `2^3` cell, a paired-Weyl QCA, non-ultralocal
operators, or an extra dimension leaves its hypotheses and can evade it. The
explicit `M_4` and staggered constructions above do evade it.

## Naive Two-Band Doubling Control

The spatial two-band law

```text
H_naive(k) = sum_i sin(k_i) sigma_i
```

has eight nodes at the corners `k_i in {0,pi}`. Linearizing at a corner gives
chirality sign

```text
chi = (-1)^(number of pi components).
```

There are four `+` and four `-` nodes. A low-momentum statement about the
origin therefore does not by itself erase the other exact lattice sectors.
This finite census is consistent with, but is not a re-proof of, the full
Nielsen-Ninomiya theorem. A physical state restriction, Wilson lifting,
staggered taste interpretation, boundary mechanism, or other selector remains
required.

## Exact Micro-Law Versus Continuum Effective Law

| question | exact lattice answer | continuum answer | residual |
|---|---|---|---|
| adjacency | three standard-cubic substeps exactly generate the BCC support | body diagonal becomes one effective propagation step | exact phase schedule |
| unitarity | exact at every Brillouin-zone momentum | norm-preserving Weyl/Dirac evolution | does not select the law |
| rotations | ordered split has only the exact covariance its product actually carries | full Weyl rotational covariance at first order | exact cubic repair or controlled irrelevance |
| chirality | both handed branches and/or paired lattice nodes exist | one may expand about a chosen Weyl node | physical branch/state selector |
| mass | zero on primitive `M_2`; allowed on a block | continuum Dirac mass near a node | supplied `m` or mass theorem |
| species | staggered cube has two tastes; Wilson lifts spatial corners | one desired Dirac sector may remain | taste/species identification |
| time | a discrete update label is supplied | `Delta t` is mapped to continuum time | clock/tick theorem |
| outcomes | unitary amplitudes are propagated | quantum probabilities may be assigned | sampled-record instrument and actualization |

The last row cannot be folded into the kinetic result. The sibling
`COMPLETE_SAMPLED_LAW_PAIR_AXIOM_UNDERDETERMINATION_NOTE_2026-07-14.md`
constructs two complete sampled append laws with the same structural
interface and different readable transcript probabilities. Selecting a
Weyl/Dirac/Wilson/staggered unitary kernel does not distinguish that pair.
Therefore this cycle narrows the reversible kinetic law; it fixes no sampled
record transcript probability unless an exact instrument/actualization law is
also supplied or derived.

## Atom Ledger After The Three Probes

The residue is best treated as a dependency graph, not inflated into a count
of independent axioms:

1. **Exact kinetic-law package.** Update matrix or Hamiltonian, coefficients,
   locality range, exact symmetry action, and any substep schedule.
2. **Effective carrier package.** Generated finite-block composition,
   one-particle sector, fermionic CAR/Fock interpretation, and translation
   action on blocks.
3. **Branch/parameter package.** Chirality or paired content, mass `m`, Wilson
   `r` or staggered taste content, and gauge representation.
4. **Time/continuum interface.** Time orientation, micro-step or macro-step to
   tick map, low-momentum/narrow-band state domain, scaling limit, and error
   control.
5. **Interaction and record package.** Gauge/interacting completion, stability
   of the limiting cone, exact record-producing instrument, transcript
   weights, and actual sample/history semantics.

Packages 4 and 5 consume the earlier packages; they are downstream jobs, not
claimed pairwise-independent walls. The current axioms do not derive package
1. The exact factorization removes primitive adjacency as an additional root.
A generated-composition theorem could substantially retire package 2.
Coordinate ordering and block origin may retire as gauge/convention once their
observable equivalence is proved. None of those reductions chooses mass,
chirality, tastes, or sampled record probabilities.

## Constitutional Consequence

The three probes answer the immediate constitutional question cleanly:

- **No lattice-axiom change:** the BCC Weyl support is exact three-step
  reachability on the existing six-neighbour lattice.
- **No qubit-axiom change:** effective `M_4` and `M_8` carriers can be finite
  blocks of primitive qubits, conditional on the composition bridge.
- **Law-level content remains:** the present axioms name no exact update,
  phase schedule, branch, mass, taste rule, continuum domain, or sampled
  record instrument.

It would therefore be premature to add Weyl, Dirac, Wilson, staggering, or a
three-phase clock to the constitutional prose. The productive next target is a
forcing theorem over a sharply stated law class: can locality, exact
record-preservation, translation/cubic covariance, reversible open-sector
dynamics, and a minimal block carrier select one operational-equivalence class
of update? If yes, the selected law can remain theorem output. If no, the
underivable extensional law reference—not BCC geometry or a larger primitive
onsite algebra—is the constitutional content that must be priced.

This note is therefore **not an axiom candidate**. It says what an eventual
bare-metal law sentence must determine and which apparent lattice/qubit edits
it need not make.

## No-Go Discipline

The only negative claim is the primitive-onsite statement above. No absolute
no-go against relativistic reduction from the current substrate is made; the
split-step, staggered, and block-Wilson constructions are positive
counterexamples to any such broad claim.

### N1 — Alternative-route enumeration

| route | status | result against the narrow onsite claim |
|---|---|---|
| primitive onsite `M_2` Weyl plus constant mass | `EXACTLY TESTED` | three anticommutators force the mass matrix to zero |
| paired-Weyl `M_4` QCA | `EXACTLY TESTED` | evades the scope; exact unitary massive block exists, with supplied `m` |
| `2^3` staggered/bipartite block | `EXACTLY TESTED` | evades the scope; exact Clifford block exists, with two tastes |
| `M_4` Wilson block | `EXACTLY TESTED` | evades the scope; lifts seven spatial corner modes, with supplied `r,m` |
| ordered split-step/Floquet QCA | `EXACTLY TESTED` | gives massless Weyl on primitive `M_2`; mass again needs a paired/block carrier |
| non-ultralocal or extra-dimensional fermions | `LIVE` | outside the finite onsite theorem; not foreclosed |

The broad “one qubit lattice cannot yield Dirac dynamics” claim fails this
gate and is not shipped.

### N2 — Wall-independence audit

The residual packages are not advertised as independent walls. There is a
direct dependency chain:

```text
exact micro-law
    -> carrier and physical branch
    -> time/continuum theorem
    -> interacting sampled-record predictions.
```

Closing an upstream package does not automatically close the downstream one:
the exact split-step leaves mass, state domain, and record probabilities open.
Conversely a claimed continuum or transcript result must expose which exact
upstream law it consumes. The root removed here is adjacency mismatch; the
root proved narrowly absent is an onsite `M_2` mass matrix.

### N3 — Hidden-wall scan

The phrases “conditional shift,” “three phases,” “macro-step,” “Pauli frame,”
“block,” “fermionic,” “low momentum,” “mass,” “Wilson,” “taste,” and
“continuum” all carry content not present in the four axioms. They are stated
as imports or theorem targets. “By construction” is used only for explicit
finite matrices. “Standard” identifies a literature form and never grants it
framework authority.

### N4 — Exact residual matching

- The BCC compatibility result retires only the fundamental-adjacency
  mismatch in the earlier isotropic-Weyl compatibility note.
- The all-period site-license tick dichotomy classifies a one-component,
  radius-one-in-sites, single unitary tick. The split-step product is not a
  counterexample: its one-particle coin has two components and its complete
  macro-step has radius three in primitive sites. Treating the three factors
  as separate radius-one ticks instead requires an exact three-phase schedule.
- The onsite dimension proof supports only a primitive-site mass obstruction;
  it does not support the older broad claim that one-qubit substrate uniquely
  forces a staggered scheme once finite blocking is allowed.
- The Kawamoto-Smit phase-forcing result applies inside a supplied naive-Dirac
  spin-diagonalization class. It can retire axis-sign gauge duplication but
  does not select that kinetic class.
- The sampled-law discriminator exactly matches the outcome-kernel residual,
  not the reversible kinetic residual.

No residual is reused as evidence for a different lane.

### N5 — Resolution and rhetoric audit

| statement | tested resolution | licensed conclusion |
|---|---|---|
| BCC factorization | exact Bloch matrices and exact three-step support | current adjacency can realize this macro-step |
| rotation defect | one ordered free split-step; small momenta sampled numerically | defect begins at second order for this law, not for every possible composition |
| onsite mass | all complex `2 x 2` matrices | no constant anticommuting mass on primitive `M_2` |
| staggered tastes | free `2^3` block Clifford representation | two tastes in this block, not a universal interacting rooting no-go |
| Wilson lifting | eight spatial Brillouin corners | seven spatial corners lifted, not a full interacting space-time proof |
| sampled outcomes | inherited paired-law exact control | kinetic selection alone does not select transcript probabilities |

Continuum language is never substituted for an exact lattice identity.

### N6 — Partial-closure paths

- Existing Lattice content plus three substeps closes BCC reachability.
- Kinetic isotropy can close one speed ratio after a time interface exists.
- Generated local-algebra composition may close the finite block carrier.
- Local sign gauge equivalence closes the six staggered axis-order
  presentations as distinct physical branches.
- Translation covariance may close the eight block origins as coordinate
  choices.
- A symmetry/minimality classification could close much of the exact kinetic
  package, provided its symmetry group matches the live one exactly.
- A unique ergodic instrument or deterministic global-history theorem could
  close the sampled-law package.

These retirement routes remain open and are not converted into premises.

### N7 — Strongest steelman

The strongest positive alternative is one exact qubit-native periodic law on
the six-neighbour lattice whose three phases are generated internally, whose
block algebra and CAR sector are derived, whose symmetry orbit contains both
ordered presentations without extra physical labels, and whose unique stable
low-energy sector is a massive chiral interacting field. If the same law also
generates append-only records and a unique operational transcript measure,
then update, clock, matter, and outcome content could collapse to one bare
metal rule. The exact split-step factorization makes this a concrete research
program, not something the onsite mass obstruction rules out.

### N8 — Cross-cycle echo

This cycle revisits three older claims without counting them again:

1. the BCC mismatch from the isotropic-Weyl note is reduced from a possible
   constitutional conflict to a three-phase law question;
2. the site-license tick results remain valid in their one-component,
   radius-one single-tick class; this two-component/radius-three macro-law
   leaves that class and therefore pays exactly the phase/carrier residue
   recorded here;
3. the staggered realization gate remains open on carrier, CAR, taste, and
   interactions, but not because primitive adjacency forbids a block; and
4. the complete sampled-law pair remains an independent lower bound after the
   kinetic reduction, because both members can share the same reversible
   structural interface.

The exact identities are new constructive information. Repeated walls are
bookkeeping links, not independent evidence counts.

## Verification

Run:

```bash
python3 scripts/cubic_qubit_relativistic_reduction_probe_2026_07_14.py
```

The PASS count includes related algebraic and source-boundary checks. It is not
an independent evidence count and does not elevate this meta note to retained
authority.
