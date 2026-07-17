# Distinguishable-walker antisymmetric-sector compiler probe — Cycle 239

**Date:** 2026-07-17

**Type:** bounded_theorem

**Status:** exact finite conditional construction plus route-specific resource
disposition; audit unset

**Authority:** none

**Audit:** unset

**Constitutional effect:** none

**Packaging:** draft parking branch and draft PR #5389 only

Companion runner:

```text
scripts/distinguishable_antisymmetric_fock_compiler_cycle239_2026_07_17.py
```

Load-bearing internal inputs are Cycles 210, 219, 228, and 230. This note and
runner change no foundation, axiom, Qualification, primitive, registry,
policy, audit, or queue surface.

## Result up front

The distinguishable-walker plus antisymmetric-sector escape has a strong
exact finite-torus result, but its published QCA realization does **not** meet
the Cycle-230 physical-`M2` compiler contract.

For every fixed particle number `n`, the global antisymmetric isometry

```text
E_n : wedge^n C^M -> (C^M) tensor ... tensor (C^M)
```

intertwines the Cycle-230 free walk exactly:

```text
E_n wedge^n(U) = U^(tensor n) E_n.
```

If the onsite contact is extended symmetrically to every unordered pair of
particle-type registers, the same code sector also reproduces

```text
W_g = product_x exp(i g binom(N_x,2))
```

exactly. This preserves the code, is identity for `n<=1`, retains the
Cycle-219 one-particle mass fixture, reproduces the Cycle-230 rank-two modular
contact block and seam fixture, and commutes with all 24 proper-cubic frames.
Thus there is no algebraic statistics, contact, mass, seam, or cubic-covariance
failure in the declared antisymmetric sector.

The resource disposition is different. Brun and Mlodinow's local QCA uses
`N_max` distinguishable **particle type** copies. At every spatial site its
local Hilbert space has dimension

```text
2^{d N_max},
```

where `d` is the number of walk ports. For the Cycle-230 six-port cell,
`d=6`. Exact capacity for its complete variable-particle Fock space requires
`N_max=M=6L^3`, the total number of one-particle modes. Therefore the
published embedding uses `6M=36L^3` qubits per coarse cell and `M^2` qubits in
total. This is neither constant overhead per coarse cell nor a bounded
physical-`M2` realization.

Moreover, its state isometry is the global antisymmetrizer over the active
type registers. A rank-`n` determinant contains `n!` label permutations. The
Cycle-230 `L=3` rank-73 sea uses 73 labels and has `73!` nonzero
label-permutation terms (a 106-digit number). Already a two-mode determinant
at separated cells is a Bell-rank-two state of the two type assignments, so a
bounded-radius state encoder acting on a product occupation input cannot
prepare it at arbitrary separation without a supplied entangled background,
particle-label service, or growing-depth communication. The source also uses
the first `n` types as the occupied registers and fixes an ordering convention
for fermion basis signs. The first-`n` type selection and antisymmetric code
sector are supplied global structures, not locally enforced auxiliary
constraints. The mode order is audited as an explicit convention but is only
basis bookkeeping in the cited construction; the negative resource result
does not count that convention as a separate physical ordering service.

This establishes a narrow route disposition:

```text
exact algebraic E and G at finite L:        YES
local free QCA after code state is supplied: YES
full variable-N capacity:                   YES, only with N_max=M
constant physical-M2 overhead per cell:     NO for this realization
bounded-radius state E without a service:   NO for this realization
bounded full-contact resource:              NO for this realization
```

It is **not a route-independent no-go** and creates **no axiom pressure**.
Compressing the labels into a genuinely local gauge or occupation encoding
would be a different fermionization compiler and remains logically open.

## Primary-source boundary

Only primary technical sources are used.

1. Todd A. Brun and Leonard Mlodinow,
   [“Quantum cellular automata and quantum field theory in two spatial
   dimensions,”](https://arxiv.org/abs/2010.09104) *Phys. Rev. A* **102**,
   062222 (2020). This paper gives the explicit local QCA embedding. Its
   Eqs. (9)–(11) place one qubit at each port, site, and particle type and
   state `dim H_x=2^(d N_max)`. It calls the local subsystems very
   high-dimensional, restricts the theory to a completely antisymmetric
   physical subspace, and in its one-dimensional example sets `N_max` equal
   to the number of one-particle modes when the saturation condition is to
   disappear.

2. Leonard Mlodinow and Todd A. Brun,
   [“Fermionic and bosonic quantum field theories from quantum cellular
   automata in three spatial dimensions,”](https://arxiv.org/abs/2011.05597)
   *Phys. Rev. A* **103**, 052203 (2021). Its Eqs. (5)–(12) give the 3D
   distinguishable-type tensor product, the vacuum-augmented walker register,
   the direct sum of totally antisymmetric sectors, and the identical free
   update. It explicitly selects the first `n` types for an `n`-particle
   state, invokes an established ordering convention for the one-particle
   basis, says the resulting creation/annihilation operators are nonlocal,
   and treats free particles. Its conclusion leaves interactions as future
   work.

3. Todd A. Brun and Leonard Mlodinow,
   [“Quantum Electrodynamics from Quantum Cellular Automata, and the Tension
   Between Symmetry, Locality, and Positive Energy,”](https://arxiv.org/abs/2503.05998)
   *Entropy* **27**, 492 (2025). This later primary paper still describes the
   antisymmetric fermion construction as requiring high local dimension. Its
   interaction study is a different one-dimensional finite-range example;
   it does not supply the Cycle-230 3D contact compiler. It is used here only
   to prevent an overbroad claim that all finite-range interaction repairs
   are absent.

The source papers do not prove the Cycle-230 result below. Applying the
distinguishable-type construction to the supplied six-direction walk and
adding the symmetric pair contact are Cycle-239 instantiations. Conversely,
Cycle 239 does not claim that the source authors intended a one-qubit-per-site
fundamental substrate.

## Exact hypotheses

The route disposition is conditional on the following hypotheses. They are
kept separate so that changing one defines a new probe rather than silently
strengthening the conclusion.

### H1 — target theory

The target is the entire Cycle-230 finite-torus Fock space on

```text
M = 6 L^3
```

one-particle modes, not a fixed-`n` sector or a low-density approximation.
Its dimension is `2^M`, and its maximum particle number is `M`.

### H2 — route realization

The route is the Brun–Mlodinow distinguishable-walker QCA: `N_max` identical
walker types, each embedded into six local port qubits per coarse cell, with
the physical sector restricted to total antisymmetry over the active types.
No unproved compressed replacement of this embedding is counted as the same
route.

### H3 — exact capacity

All sectors through `n=M` must be represented. Since every particle type can
hold at most one walker, this implies `N_max>=M`. Choosing `N_max=M` is the
minimal exact-capacity choice and gives

```text
sum_(n=0)^M binom(M,n) = 2^M.
```

### H4 — physical compiler contract

The requested encoder and update must have bounded spatial support and
constant physical-`M2` overhead per coarse cell, uniformly in `L`. Auxiliary
constraints must be locally enforced. A global antisymmetrizer, preferred
mode ordering, particle-label assignment service, or predeclared physical
code sector is not free.

### H5 — contact realization

The fixed-particle interacting extension applies the same onsite collision
phase to every unordered label pair. It is permutation symmetric in the
particle types and therefore preserves the antisymmetric sector. This
pairwise realization is supplied by Cycle 239, not by the cited free-QCA
paper.

### H6 — covariance

Proper-cubic frames act on position and the six direction ports and act
trivially on the type labels. Every type lane receives the same one-particle
walk and the same pair-contact rule.

### H7 — schedule and time firewall

The order of contact, coin, and stream is inherited from the supplied
Cycle-230 candidate. Type labels, an antisymmetrization circuit, and layers of
pair gates are compiler controls. They are **not physical time**, not a clock,
not a rate, and not a derived temporal law.

## Exact finite construction

Let `H_1=C^M` be the Cycle-230 one-particle Hilbert space. For fixed `n`,
define

```text
E_n |j_1 wedge ... wedge j_n>
  = 1/sqrt(n!) sum_(pi in S_n) sgn(pi)
      |j_(pi(1))>_1 ... |j_(pi(n))>_n.
```

The subscripts are distinguishable type registers. Direct calculation gives

```text
E_n^dagger E_n = I,
P_tau E_n = sgn(tau) E_n.
```

For any one-particle unitary `U`, identical action on every type commutes with
the permutation action, so

```text
U^(tensor n) E_n = E_n (wedge^n U).
```

The runner verifies this with dense complex matrices for `n=1,2,3`, including
the correct ranks `6,15,20` and exchange signs.

For the contact, define the local occupation of type `t` at cell `x` by
`q_(x,t)` and apply

```text
W_pair = product_x product_(s<t) exp(i g q_(x,s) q_(x,t)).
```

On the antisymmetric code, no two types can occupy the same one-particle
mode. Therefore at each cell

```text
sum_(s<t) q_(x,s)q_(x,t) = binom(N_x,2),
```

and `W_pair E = E W_g`. The runner builds the complete two-cell,
two-particle matrix and obtains both an intertwiner residual and code leakage
below `2e-14`. A deliberately type-asymmetric phase has nonzero leakage,
showing that label-permutation symmetry is load-bearing rather than cosmetic.

The same normalized labeled-register contraction independently reproduces
the Cycle-230 `L=3` modular two-particle/two-hole contact block. Thus the
reported seam block is inherited exactly on the code; it is not replaced by
a new interaction or a wrapped-phase interpretation.

### Lawful domain

Every intertwining equality in this cycle is restricted to

```text
H_phys = H_0 direct-sum E_1(wedge^1 H_1) direct-sum ...
         direct-sum E_Nmax(wedge^Nmax H_1),
```

with the first `n` type registers active in the `n`-particle summand. It is
not an equality on the full labeled QCA Hilbert space. States with repeated
particles of one type, distinguishable multiplicities, symmetric type
content, or the wrong active-type convention are outside the declared code.
The source's local coin constraints do not uniquely fix all such ambient
sectors, and Cycle 239 makes no physical claim about them. The runner checks
that the `n=2`, six-mode code has dimension 15 inside a 36-dimensional
labeled ambient sector and separately tests preservation and deletion
leakage.

## L=3,4,5 resource audit

With `M=6L^3`, `N_max=M`, and six QCA port qubits per type and coarse cell:

| `L` | cells | `M=N_max` | qubits/cell | total QCA qubits | target Fock qubits | overhead ratio | pair gates/cell | pair-only depth floor |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 27 | 162 | 972 | 26,244 | 162 | 162 | 13,041 | 161 |
| 4 | 64 | 384 | 2,304 | 147,456 | 384 | 384 | 73,536 | 383 |
| 5 | 125 | 750 | 4,500 | 562,500 | 750 | 750 | 280,875 | 749 |

The total QCA register is `M^2` qubits while the target occupation Fock space
uses `M` qubits. The physical code has the right dimension, `2^M`, inside the
ambient `2^(M^2)` QCA space. Capacity is therefore not the failure; uniform
local overhead and code preparation are.

As a held-out-size control, the runner fits the `L=3,4` local-register values
to `36L^3` with zero intercept and predicts the withheld `L=5` value `4500`
exactly. The growth is the analytic route law, not an anomaly of one torus.

For the direct pair-gate realization, each label pair must receive the
collision phase at every cell. With two-label gates and no high-arity
shortcut, edge-coloring the complete label graph gives `N_max-1` disjoint
layers because all tested `N_max` are even. A counting ancilla or a high-arity
local gate changes this schedule but touches or aggregates all `N_max` label
lanes; it does not repair the already growing local register.

## Rank-73 sea and variable-N controls

The `L=3` principal-phase census again gives rank 73. Its exact determinant is

```text
E_73 |u_1 wedge ... wedge u_73>
 = 1/sqrt(73!) sum_(pi in S_73) sgn(pi)
   |u_(pi(1))>_1 ... |u_(pi(73))>_73.
```

The label-permutation support is

```text
73! =
4470115461512684340891257138125051110076800700282905015819080092370422104067183317016903680000000000000000.
```

The exact integer and its 106 digits are runner-controlled. This does not
mean a preparation circuit must literally enumerate every term; it means the
target state has support across all those label assignments and all 73 type
registers. A compressed preparation algorithm would still need to establish
the global antisymmetric correlations. The two-particle Schmidt-rank witness
already excludes a cellwise product encoder.

Setting `N_max=73` is a useful deletion control. It retains the `L=3`
rank-73 determinant and all smaller sectors with constant `438` port qubits
per cell, but deletes every target sector `n>=74`. A fixed `N_max=K` therefore
gives a legitimate bounded-density/fixed-cutoff construction, not the full
variable-particle Cycle-230 Fock update.

Deleting the antisymmetric restriction instead retains distinguishable
particle multiplicities and does not reproduce CAR. Deleting identical
updates on one label, or applying a type-asymmetric contact, gives nonzero
code leakage in the runner. These controls distinguish a capacity failure
from failure to preserve the declared code.

## Mass, seam, leakage, and frames

- **One-particle mass.** `E_1` merely places the Cycle-219 walker in type 1.
  The contact is identity at `n=1`; rest, curvature, and forced-inertia
  fixtures are unchanged within the previously declared tolerances.

- **Rank-73 sea.** The `L=3` negative-principal-phase census is again 73.
  The state exists exactly when `N_max>=73`; existence does not make its
  preparation bounded.

- **Contact and seam.** Symmetric all-pair collision gives the exact
  `binom(N_x,2)` phase. The labeled contraction matches the Cycle-230 modular
  block at machine precision, with the same two nonzero singular values.

- **Leakage.** Identical tensor-power free updates and symmetric pair contacts
  commute with all label permutations, so leakage is zero. A deleted lane
  update and an asymmetric contact both produce explicit nonzero leakage.

- **All 24 frames.** For every proper-cubic frame `R`, the labeled frame is
  `D(R)^(tensor n)` and commutes with the antisymmetrizer. The runner checks
  the fixed-`n` intertwiner for all 24 direction frames and separately checks
  the full `L=3` one-particle spatial walk. The type labels are scalar copies;
  they are supplied multiplicity, not a preferred spatial direction.

## Supplied-structure inventory

This route supplies all of the following:

1. `N_max` globally distinguishable particle-type registers;
2. the convention that an `n`-particle physical state uses the first `n`
   types and leaves the rest in a vacuum register;
3. a global ordering convention for one-particle modes when basis signs are
   named (bookkeeping here, not independently counted as a physical service);
4. the totally antisymmetric code-sector declaration;
5. `N_max=M` for exact full-Fock capacity;
6. six port qubits per type and cell;
7. identical coin and stream dynamics on every type;
8. the Cycle-239 all-pair symmetric contact extension;
9. the contact/coin/stream schedule;
10. the Cycle-219 coin and mass calibration; and
11. the Cycle-230 sea phase cut and contact law.

No item in this list is promoted to an axiom. The globally replicated particle
types, first-`n` selection, and predeclared antisymmetric sector are the
load-bearing supplied services. The ordering convention is recorded but not
used as an independent wall; `N_max=M` is the exact-capacity condition that
turns the label multiplicity into growing local overhead.

## N1–N8 no-go-discipline audit

The statement under audit is deliberately narrow:

> Under H1–H7, the Brun–Mlodinow distinguishable-walker realization does not
> provide a constant-overhead, bounded-radius state compiler for the complete
> Cycle-230 variable-particle Fock update.

### N1 — Alternative routes

The following escapes were actively separated:

- fixed `N_max=K`: constant overhead and exact sectors `n<=K`, but deletes
  the rest of the full Fock space;
- predeclared antisymmetric sector: exact local free evolution, contact,
  mass, seam, and frames, but supplies rather than locally constructs `E`;
- a pre-entangled auxiliary background: could evade the product-state
  preparation witness, but is additional global state resource;
- local occupation compression: removes particle labels but returns to the
  original CAR-to-`M2` compilation problem;
- local gauge/higher-form encoding: a distinct constructive route, not a
  repair internal to this particle-type QCA;
- sorting or antisymmetrization networks: can prepare finite determinants,
  but their communication support/depth grows with separation and particle
  number;
- high-arity contact/counting gates: may reduce the direct all-pair depth but
  still act on the growing set of type lanes.

None is dismissed as impossible in general.

### N2 — Condition independence

The `M^2` register, `6M` qubits per cell, and `N_max=M` requirement are one
resource wall, not three independent walls. The `n!` state support and
all-pair contact cost are additional manifestations of the same replicated
label structure. Covariance, mass, seam, and code leakage are independent
controls and they pass; they are not used to inflate the negative conclusion.

### N3 — Hidden-condition scan

The conclusion assumes a finite periodic cube, the exact complete Fock space,
the published particle-type QCA embedding, an initially unentangled local
ancilla supply, uniform bounded support/depth, and ordinary physical-`M2`
sites. It can change if one allows a particle-number cutoff, volume-dependent
local dimension, a global code-sector preparation oracle, a nonlocal
entangled resource, approximation, or a new compressed label/gauge encoding.

### N4 — Residual matching

The runner matches each wall to a number:

- `L=3,4,5` local qubits/cell: `972, 2304, 4500`;
- total QCA qubits: `26244, 147456, 562500`;
- overhead ratios: `162, 384, 750`;
- `L=3,4` fitted local-register law and held-out `L=5` prediction:
  `36L^3`, predicting `4500` exactly;
- direct pair gates/cell: `13041, 73536, 280875`;
- pair-only depth floors: `161, 383, 749`;
- rank-73 label support: exact `73!`, 106 digits;
- two-particle product-encoder distance floor:
  `sqrt(2-sqrt(2))`;
- exact fixed-sector update, contact, frame, and seam residuals: numerical
  zero at the declared machine tolerances;
- asymmetric-contact and deleted-lane leakage: explicitly nonzero.

### N5 — Rhetoric audit

The result says “this realization does not meet the contract.” It does not
say that distinguishable-particle methods, antisymmetric codes, fermions in
three dimensions, or all physical-`M2` compilers are impossible. It does not
turn a route-specific resource failure into constitutional evidence.

### N6 — Partial closure

The strongest surviving construction is substantial: for any declared fixed
`K`, the route gives a strictly local QCA free update with `6K` qubits per
cell, exact antisymmetric sectors through `n=K`, symmetric local contact,
zero leakage, all-24 covariance, and the same one-particle mass. If the global
code state is admitted as supplied, choosing `K=M` gives an exact finite-L
algebraic compiler for the entire Fock update and its seam. What remains open
is precisely bounded state preparation and uniform physical-site resources.

### N7 — Steelman

The strongest version grants the route a protected antisymmetric code sector
as the physical state space and treats the high-dimensional local QCA cell as
fundamental. Under those relaxed rules, it succeeds exactly at every finite
`L`: the free update is local, the symmetric contact is local in space,
fermionic statistics are exact, and the mass/seam/frame fixtures survive.
This is a valid constructive model. It simply answers a different substrate
question from constant-overhead compilation into physical `M2` sites.

### N8 — Cross-cycle echo

Cycle 235 achieved bounded local even-algebra support with local constraints
but lost the total-odd sector on a closed cube. Cycle 239 retains both
parities and the rank-73 state algebraically, but pays volume-growing local
label multiplicity and a global state isometry. Those complementary tradeoffs
do not yet form a shared theorem: feature splicing has not been constructed,
and the failures arise from different supplied structures. Therefore the
evidence is route-specific and produces **no axiom pressure**.

## Dependency-ledger effect and disposition

| wall | Cycle-239 effect |
|---|---|
| `C_ref` | unchanged; the sea phase cut and physical reference remain supplied |
| `C_num` | constructive at fixed finite `L`; full Fock dimension is represented exactly when `N_max=M` |
| `C_wrap` | constructive conditional inheritance; the exact Cycle-230 modular contact/seam block survives |
| `C_int` | constructive algebraically; symmetric all-label-pair contact reproduces `W_g`, but bounded resource fails |
| `C_local` | sharpened route-specific failure: local free update exists only in a `6M`-qubit cell, while state `E` is global |
| `C_source` | unchanged; neither labels nor antisymmetrization select a gravity/source law |

Route disposition: **exact finite algebraic escape; rejected as a
constant-overhead physical-M2 compiler under the present contract**.

There is no shared obstruction and no axiom conclusion. The optimal use of
this result is as a control: any later constructive compiler should preserve
Cycle 239's exact fixed-sector algebra, contact, mass, seam, and all-24
covariance while replacing the particle-type multiplicity and global state
isometry with bounded locally enforced structure.
