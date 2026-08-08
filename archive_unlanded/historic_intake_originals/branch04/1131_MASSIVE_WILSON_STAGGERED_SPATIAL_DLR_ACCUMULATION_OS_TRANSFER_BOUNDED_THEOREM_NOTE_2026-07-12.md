# Massive Wilson--staggered spatial DLR accumulation and OS transfer

**Date:** 2026-07-12  
**Type:** bounded_theorem  
**Status:** unaudited candidate; effective status is pipeline-derived only after independent audit.  
**Primary runner:** [`scripts/massive_wilson_staggered_spatial_dlr_accumulation_os_transfer_2026_07_12.py`](../scripts/massive_wilson_staggered_spatial_dlr_accumulation_os_transfer_2026_07_12.py)  
**Cached output:** [`logs/runner-cache/massive_wilson_staggered_spatial_dlr_accumulation_os_transfer_2026_07_12.txt`](../logs/runner-cache/massive_wilson_staggered_spatial_dlr_accumulation_os_transfer_2026_07_12.txt)

## 0. Result

Fix the supplied `SU(3)` Wilson--fundamental-staggered model, lattice spacing,
`beta>=0`, and `m>0`. Let the even periodic spatial tori tend to `Z^3`
through any van Hove sequence, after taking the unique infinite-time limit at
each finite spatial volume supplied by the
[massive staggered log-determinant theorem](MASSIVE_STAGGERED_LOGDET_HOLDER_RUELLE_INFINITE_TIME_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-07-12.md).

Then every such spatial sequence has a subsequence on which every fixed local
gauge-invariant gauge--fermion polynomial converges. Every accumulation
functional has the following properties:

1. its gauge marginal is a positive full-four-dimensional DLR probability
   for the Wilson action plus the exact massive staggered determinant;
2. it is gauge invariant and invariant under the supplied blocked lattice
   translations and surviving cubic symmetries;
3. it is time-reflection positive and adjacent-form positive;
4. its OS quotient carries a positive self-adjoint two-step contraction
   `T_2`, a nonnegative logarithmic Hamiltonian
   `H=-(2a_tau)^(-1)log T_2` on `(ker T_2)^perp`, the Euclidean semigroup,
   and the corresponding spectral real-time unitary group.

The load-bearing uniform estimate is the site-anchored version of the exact
massive infinite-time uniqueness contraction. With

```text
D=mI+M,       A=D^dagger D=m^2I-M^2,       c=m^2+16,
Q=I-A/c=(16I+M^2)/c,                       r=16/(m^2+16)<1,             (0.1)
```

define

```text
phi_(x,n)(U)=-(1/(2n)) tr_color <x|Q[U]^n|x>.                          (0.2)
```

Uniformly in every temporal and spatial volume,

```text
||phi_(x,n)||_infinity <=3 r^n/(2n),
support phi_(x,n) subset B_(2n+1)(x).                                 (0.3)
```

Only polynomially many centers have a radius-`2n+1` support containing a
fixed link. Polynomial growth times `r^n` is summable. The determinant
therefore defines a volume-uniform absolutely summable, indeed
diameter-weighted summable, compact-link interaction. The Wilson part is
finite range. This closes spatial **existence**, not spatial uniqueness.

At `beta=6` the theorem proves existence of at least one accumulation state.
It does not prove that the plaquette has one boundary-independent value, that
the spatial sequence converges without subsequences, or that there is only one
phase.

This result does not derive the Wilson-staggered dynamics, Euclidean weight,
spin structure, or physical probability rule from the Lattice, Qubit,
Admissibility, and Record axioms. It does not establish clustering, a volume-uniform spectral
gap, a unique vacuum, a continuum Lorentz/QFT limit, the Standard Model, or
GR. No axiom-update stop is established.

## 1. Supplied finite-volume family

For each even spatial three-torus `Lambda_s` and even antiperiodic temporal
circle, use the same Wilson gauge action, fundamental staggered operator,
Haar link measure, two-seam reflection convention, and local gauge-invariant
observable algebra as the coupled reflected-Gram, OS-descent, and massive
infinite-time uniqueness theorems. All periodic extents are even, so the
bipartite determinant-pairing argument applies. Temporal circumference first
tends to infinity through the massive infinite-time uniqueness limit.

The spatial exhaustion is supplied regulator data. A local observable is
embedded into every sufficiently large centered torus before its expectation
is compared. No boundary-independence claim is made.

The gauge marginal at every finite regulator is the probability

```text
d mu_L(U)=Z_L^(-1) exp(-S_W,L(U)) det D_L(U) product_e dHaar(U_e).       (1.1)
```

Positivity follows from the bipartite pairing at `m>0`. Compactness of
`SU(3)` controls gauge polynomials; the mass controls fermionic insertions.

## 2. Volume-uniform determinant interaction

### 2.1 Exact contraction at every volume

The covariant staggered hop is anti-Hermitian and obeys `||M||<=4` in four
dimensions on periodic boxes and on open boxes. Consequently (0.1) gives

```text
0<=Q<=rI,                     r<1,                                    (2.1)
```

with no volume-dependent constant. The exact identities

```text
log det D=(dim D/2)log c -(1/2)sum_(n>=1) Tr(Q^n)/n,                  (2.2)
A^(-1)=c^(-1)sum_(n>=0)Q^n,
D^(-1)=A^(-1)D^dagger                                                   (2.3)
```

converge in operator norm for every fixed `m>0`.

Let `P_x` project onto the three colors at site `x`. Splitting the trace in
(2.2) into site traces gives the constant density `(3/2)log c` plus (0.2).
Since `Q` has lattice range two, `P_x Q^n P_x` depends only on links in the
ball `B_(2n+1)(x)`. Also

```text
|tr(P_x Q^n P_x)|<=rank(P_x)||Q^n||<=3r^n,                            (2.4)
```

which proves (0.3).

### 2.2 Absolute and first-moment summability

The conditional gauge log density is `-S_W+sum_(x,n)phi_(x,n)` up to the
gauge-independent constant in (2.2), or equivalently its interaction energy
is `S_W-sum_(x,n)phi_(x,n)`. Regard each `phi_(x,n)` as a log-weight
interaction supported on `B_(2n+1)(x)`. For a
fixed positive-oriented link `e`, the number of centers `x` whose ball can
contain `e` is bounded by a dimension-four polynomial `C_4(2n+2)^4`.
Therefore

```text
sup_e sum_(X contains e)||Phi_X^F||_infinity
 <=C sum_(n>=1)(2n+2)^4 r^n/n < infinity,                             (2.5)

sup_e sum_(X contains e)(1+diam X)||Phi_X^F||_infinity
 <=C' sum_(n>=1)(2n+2)^5 r^n/n < infinity.                           (2.6)
```

Both constants depend on `m` but not on the finite volume. The Wilson
plaquette interaction has finite range and is bounded for every fixed
`beta`, so it obeys the same norms.

On a periodic torus, orders whose support wraps around are not literally the
same interaction as on `Z^4`. Their contribution to a local conditional
energy is bounded by a polynomial in the circumference times `r` to a fixed
positive multiple of that circumference. It vanishes along the van Hove
limit. Thus wrap terms do not contaminate the limiting specification.

Equations (2.5)--(2.6) are stronger than the fixed-spatial-volume temporal
Hölder estimate of the massive infinite-time uniqueness theorem: their anchoring and constants are local in all
four Euclidean directions.

## 3. Quasilocal DLR specification and existence

For a finite link set `Delta`, define its relative energy by summing all
Wilson and determinant interaction terms whose supports meet `Delta`, with
the exterior links held fixed. Equations (2.5)--(2.6) make this sum uniformly
convergent. It is continuous in the compact product topology and changes by
an exponentially small amount when two exterior configurations agree on a
large neighborhood of `Delta`.

Normalizing the corresponding Haar density gives a proper quasilocal DLR
kernel `gamma_Delta`. Compatibility follows from the same finite interaction
sums and then uniform convergence. This is the actual specification of the
Wilson-plus-log-determinant gauge marginal; no local determinant surrogate is
inserted.

The advertised order of limits is iterated, not silently joint. At each fixed
finite spatial torus, first pass the finite-temporal-circle cylinder DLR
identities through the unique infinite-time limit. The same volume-uniform
`Q` tail controls this passage, so the resulting finite-spatial,
infinite-time measure satisfies every local cylinder DLR identity. Only then
let the spatial tori grow and extract a spatial subsequence.

Equivalently, enumerate a countable dense local cylinder algebra as
`F_1,F_2,...` and write `mu^infinity_(L_s(j))` for the unique temporal limit
at the `j`th spatial volume. Temporal full-sequence convergence lets one
choose an even `L_t(j)` so that the finite torus and
`mu^infinity_(L_s(j))` differ by less than `1/j` on `F_1,...,F_j` and on the
finitely many local conditional expressions used for those cylinders. Thus
every spatial accumulation point of the time-first states is also a diagonal
finite-torus accumulation point. The volume-uniform interaction and wrap-tail
bounds then pass the finite DLR identities to exactly that iterated-limit
state. This diagonal bridge is a proof device; it does not replace the stated
time-first order.

The product link space `(SU(3))^E(Z4)` is compact and metrizable on the
countable lattice. Hence every sequence of those finite-spatial,
infinite-time gauge probabilities has weakly convergent subsequences. The
uniform interaction tail makes their cylinder DLR identities stable under the
spatial subsequence. Every accumulation measure `mu` therefore satisfies

```text
mu gamma_Delta=mu                                                     (3.1)
```

for every finite `Delta`. This is existence of a full-four-dimensional DLR
state for every `beta>=0,m>0`.

The compact-spin DLR existence theorem and diagonal compactness are external
mathematical machinery, not framework axioms or supplied physical laws. A
standard reference is Hans-Otto Georgii, *Gibbs Measures and Phase
Transitions*, second edition, Chapter 4, “The existence problem,” DOI
[`10.1515/9783110250329`](https://doi.org/10.1515/9783110250329). The
model-specific work is (0.1)--(2.6), which verifies the compact-alphabet and
summability hypotheses for the actual massive staggered determinant.

No uniqueness theorem is used or asserted in this section. Distinct spatial
subsequences or boundary conditions may select distinct DLR phases.

## 4. Uniform local gauge--fermion bounds

The smallest singular value of `D=mI+M` is at least `m`, so

```text
||D^(-1)||<=1/m                                                       (4.1)
```

at every volume and for every gauge configuration. A balanced degree-`2q`
Grassmann monomial has conditional expectation equal to a `q` by `q` minor
of `D^(-1)`. Compression cannot increase operator norm, and therefore

```text
|det[(D^(-1))_(x_i,y_j)]|<=m^(-q).                                   (4.2)
```

Every fixed local gauge--fermion polynomial is a finite sum of such terms
with compactly bounded gauge coefficients. It has a uniform expectation
bound `C_F(m)` independent of spatial volume. Unbalanced insertions vanish by
fermion-number symmetry.

Equation (2.3) also gives volume-uniform quasilocality. If the endpoints are
at distance `R` from a changed link set, every low power of `Q` agrees and
the remaining tail is bounded by

```text
variation_R D^(-1)
 <=2(m+4)/(m^2+16) sum_(n>=floor((R-1)/2)) r^n
 <=C(m)r^floor((R-1)/2).                                             (4.3)
```

Fixed-size Wick minors inherit the same exponential tail. They are therefore
continuous observables of the limiting gauge DLR state.

Choose a countable dense local algebra generated by rational-coefficient
Peter--Weyl gauge polynomials and finitely supported Grassmann monomials.
The bounds above permit a diagonal spatial subsequence on which every member
converges. Linearity and the bounds extend the result element by element to
the stated local polynomial algebra. This constructs the full limiting
gauge--fermion Euclidean functional `omega` over the gauge DLR marginal.

## 5. Symmetries and positivity survive the limit

Gauge invariance and every supplied blocked translation/cubic symmetry are
exact finite-volume local identities. For a fixed local polynomial, its
support and transformed support fit inside every sufficiently large box.
Passing the identity through the selected subsequence gives the corresponding
identity for `omega`.

For every positive-time local polynomial `F`, finite-volume time-reflection
positivity gives

```text
omega_L(Theta(F)F)>=0.                                                 (5.1)
```

The expression is one fixed local expectation, so the limit gives

```text
omega(Theta(F)F)>=0.                                                   (5.2)
```

The same argument applies to every finite reflected Gram matrix and to the
adjacent reflected form. Reflection-compatible boxes are essential here;
positivity is not inferred from arbitrary spatial boundary data.

## 6. State-specific infinite-spatial-volume OS transfer

On the positive-time local algebra define

```text
B_0(F,G)=omega(Theta(F)G),
B_2(F,G)=omega(Theta(F)tau_2(G)).                                     (6.1)
```

At every finite spatial volume, the massive infinite-time uniqueness theorem
supplies the positive self-adjoint contraction constructed by the coupled OS
descent theorem. Thus its matrix elements obey

```text
|B_(2,L)(F,G)|^2<=B_(0,L)(F,F)B_(0,L)(G,G),
0<=B_(2,L)(F,F)<=B_(0,L)(F,F).                                       (6.2)
```

All terms are fixed local expectations, so (6.2) passes to `omega`. It
follows that `B_2` kills the `B_0` null space and defines a bounded positive
self-adjoint contraction `T_2` on the completed OS quotient. Spectral
calculus then gives

```text
H=-(2a_tau)^(-1)log T_2                                                (6.3)
```

on `(ker T_2)^perp`, together with `exp(-tH)` at the available two-step
Euclidean times and the spectral unitary `exp(-itH)`.

This reconstruction is canonical only after an accumulation state has been
selected. If multiple spatial DLR phases occur, the theorem does not identify
their OS Hilbert spaces or Hamiltonians with one another.

## 7. What the beta-six wall actually is

Several existing beta-six notes ask for a unique thermodynamic plaquette
value, a noncritical bulk phase, clustering, or a physical transfer gap.
Those are strictly stronger than existence of a DLR accumulation state.
They are context, not dependencies of this theorem.

In particular:

- compactness and (2.5) prove at least one `beta=6` DLR accumulation state;
- they do not prove that all exhaustions or boundaries give the same state;
- they do not compute the plaquette in any selected state;
- the uniform fermion mass resolvent does not imply a coupled gauge gap.

The remaining obstruction is ordinary spatial phase/infrared analysis. Live
routes include Dobrushin uniqueness at small `beta` and large `m`, polymer or
cluster expansions, chessboard/reflection estimates, and constructive RG.
Failure to have completed those routes is not evidence that an axiom update
is necessary.

## 8. Runner contract

Run:

```bash
python3 scripts/massive_wilson_staggered_spatial_dlr_accumulation_os_transfer_2026_07_12.py
```

The runner uses a reduced `1+1` `SU(3)` carrier for finite matrix certificates
and analytic four-dimensional majorants for the volume theorem. It checks
volume-independent `Q` and inverse bounds on several nonuniform finite
certificates, the site-anchored interaction bound, exact
finite propagation, exponential response to remote spatial changes, Wick
minor bounds, convergence of the dimension-four absolute/first-moment
majorants, and the source boundary/N1--N8 contract. Compactness, the DLR
subsequence theorem, and OS completion are mathematical theorems; the runner
checks their actual model-specific hypotheses rather than pretending to prove
them by sampling. The `3+1` claim is carried analytically by `||M||<=4` and
the dimension-four sums (2.5)--(2.6), not by the reduced numerical carrier;
the runner does not numerically prove the full `3+1` theorem.

## 9. Honest boundary and next theorem

The result takes a controlled subsequential spatial accumulation limit at fixed lattice
spacing. It does not give full-sequence spatial convergence or boundary
independence. It permits phases and gives no uniform rate of convergence in
the box size.

The next exact target is a separate Dobrushin or polymer theorem proving a
nonempty small-`beta`, large-`m` uniqueness wedge with independently checked
influence constants. Only after that controlled full-sequence region is
secure should the campaign attempt a lattice-spacing scaling theorem.

## 10. No-Go Discipline N1--N8

This is a positive existence theorem with named downstream walls. The walls
are stress-tested here so that “not proved” is not inflated into “impossible.”

### N1 — alternative-route enumeration

| Route | Status | Test and result | Why it does not close more than claimed |
|---|---|---|---|
| Site-anchored exact `Q` interaction | `ATTEMPTED` | Equations (0.1)--(2.6) give uniform absolute and first-moment summability for every `m>0`. | Compactness gives accumulation states, not uniqueness. |
| Direct diagonal local-functional extraction | `ATTEMPTED` | Equations (4.1)--(4.2) uniformly bound every fixed local Wick polynomial. | A diagonal subsequence may depend on phase or boundary. |
| Small-`beta`, large-`m` Dobrushin comparison | `ATTEMPTED` | Independent scratch derivations found a live nonempty wedge but disagreed on coarse influence constants. | It is deliberately deferred until one constant convention survives a separate review. |
| Pure-gauge strong-coupling/polymer expansion | `ATTEMPTED` | Repo notes contain a small-`beta` pure-gauge floor. | They do not include the actual staggered determinant and do not reach `beta=6`. |
| Finite-volume Perron positivity | `ATTEMPTED` | The pure-gauge finite transfer kernel has a simple positive top state. | No uniform-in-volume gap or coupled fermion theorem follows. |
| Uniform matter resolvent/matter gap | `ATTEMPTED` | `||D^(-1)||<=1/m` controls fermionic locality and Wick insertions. | It does not control gauge-sector spatial phase multiplicity. |
| Reflection positivity/chessboard estimates | `ATTEMPTED` | Reflection positivity survives every accumulation state and leaves this route available. | No chessboard estimate selecting one Wilson-staggered phase is proved here. |
| Constructive RG or continuum scaling | `ATTEMPTED` | The local interaction now has an exact massive fermion tail suitable for an RG input. | No running-coupling, uniform correlation, or scaling estimate is supplied. |

### N2 — wall-independence audit

| Left condition | Right condition | Left closes right? | Right closes left? | Independent? | Witness |
|---|---|---:|---:|---:|---|
| supplied Wilson-staggered dynamics | positive fermion mass | No | No | Yes | Action choice and mass domain are distinct supplied data. |
| supplied Wilson-staggered dynamics | spatial DLR existence | No | No | Yes | A finite regulator action need not have controlled thermodynamic accumulation without stability/locality. |
| supplied Wilson-staggered dynamics | spatial uniqueness/phase selection | No | No | Yes | An action may have phases; uniqueness does not select the action. |
| supplied Wilson-staggered dynamics | continuum/SM/GR closure | No | No | Yes | Regulator selection and universality/dynamical geometry are distinct. |
| positive fermion mass | spatial DLR existence | No | No | Yes | Mass supplies this proof's fermion summability, while other massless systems can possess DLR states. |
| positive fermion mass | spatial uniqueness/phase selection | No | No | Yes | A fermion resolvent bound does not exclude gauge phases. |
| positive fermion mass | continuum/SM/GR closure | No | No | Yes | Fixed positive bare mass neither proves nor is forced by the target continuum. |
| spatial DLR existence | spatial uniqueness/phase selection | No | No | Yes | Existence permits several DLR states. |
| spatial DLR existence | continuum/SM/GR closure | No | No | Yes | A lattice Gibbs state can have no controlled nontrivial continuum. |
| spatial uniqueness/phase selection | continuum/SM/GR closure | No | No | Yes | A unique lattice phase does not prove Lorentz/QFT/SM/GR scaling. |

### N3 — hidden-condition phrase scan

| Mandated phrase | Hits and classification |
|---|---|
| `we assume` | No load-bearing hit. |
| `by construction` | No use as a proof substitute. |
| `as is standard` | No hit; compact-spin DLR machinery is named as external mathematics. |
| `the framework provides` | No hit. |
| `bridge context` | No hit. |
| `background` | Boundary/background configurations occur only as explicit DLR variables, not hidden physical premises. |
| `naturally` | No hit. |
| `obviously` | No hit. |
| `standard QFT` | No hit. |
| `registered` | No hit used to grant a premise. |
| `canonical` | Explicitly restricted in Section 6 to a selected accumulation state; cross-phase canonicity is denied. |

### N4 — citation/residual matching

| Cited witness and location | Witness residual | Present residual | Match? | Disposition |
|---|---|---|---:|---|
| [Massive staggered log-determinant infinite-time uniqueness theorem](MASSIVE_STAGGERED_LOGDET_HOLDER_RUELLE_INFINITE_TIME_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-07-12.md), Sections 2--7 | Unique infinite-time functional and exact `Q` locality at fixed spatial volume; spatial limit open | Make the `Q` bounds volume-local and extract spatial DLR/OS accumulation states | Yes | Sole direct in-repo science dependency. |
| `docs/INTERACTING_TRANSFER_MATTER_GAP_AND_GAUGE_REDUCTION_BOUNDED_NOTE_2026-05-30.md` | Conditional matter-sector floor; coupled gauge gap open | Existence of spatial DLR states | No | Context only; not a dependency. |
| `docs/SU3_BULK_CRITICALITY_PREMISE_RIGOROUS_FLOOR_NOTE_2026-06-09.md` | Small-`beta` pure-gauge polymer floor | All-`beta` existence with dynamical staggered determinant | No | Context only; not a dependency. |
| beta-six plaquette closure/backbone notes | Unique numerical thermodynamic observable and hierarchy control | Existence of at least one DLR accumulation state | No | Stronger open target; not a dependency. |
| Compact-spin DLR compactness theorem | Absolutely summable quasilocal interaction has Gibbs accumulation states | Equations (2.5)--(2.6) verify the actual interaction hypothesis | Yes | Explicit external mathematics. |

### N5 — rhetoric and resolution audit

| Statement / resolution | Tested? | Permitted conclusion |
|---|---:|---|
| One fixed local gauge polynomial | Yes | Converges along a common spatial subsequence. |
| Every fixed-degree local gauge--fermion polynomial | Yes, element by element | Defines one accumulation Euclidean functional. |
| Countable local algebra simultaneously | Yes, by diagonal extraction | One common subsequence exists. |
| Arbitrary nonlocal or volume-growing observable | No | No convergence or bound claimed. |
| One DLR accumulation phase | Yes | Has gauge/RP/adjacent/OS structure. |
| All spatial phases coincide | No | No uniqueness or boundary-independence claim. |
| `beta=6` state existence | Yes | At least one accumulation state exists. |
| Unique `beta=6` plaquette value or gap | No | Explicitly open. |
| Every fixed `m>0` | Yes | Existence, with constants deteriorating as `m->0`. |
| `m=0` | No | No massless thermodynamic theorem. |

### N6 — partial-closure, convention, reframe, and primitive scan

The result retires a mathematical existence wall through a local interaction
estimate; it does not rename a supplied premise. The van Hove exhaustion and
boundary convention are regulator choices, not new axioms. The approved
Lattice, Qubit, Admissibility, and Record baseline supplies no Euclidean weight,
probability rule, determinant, dynamics, or phase-selection law. No approved
primitive is enlarged. Dobrushin, polymer, chessboard, and RG routes remain
live, so **No axiom-update stop** is triggered.

### N7 — hostile steelman

A hostile reviewer should argue that periodic finite-volume determinants are
global objects, so a weak limit of their normalized measures need not satisfy
the DLR equations of the proposed infinite interaction. That objection defeats
a compactness-only proof. The response is the site-anchored exact expansion:
each order has support `B_(2n+1)(x)` and norm `3r^n/(2n)`, the number of
relevant centers grows only polynomially, and both the interaction and wrap
tails converge uniformly. Those estimates make the finite conditional
identities stable and are the reason a DLR claim, rather than bare weak
accumulation, is permitted.

A second hostile argument is that existence is nearly automatic and does not
move the TOE. It is limited, but it removes a real regulator wall: the coupled
infinite-time Euclidean/OS object now survives infinite spatial volume for the
actual massive determinant. It still does not address action selection,
probability, phases, or continuum universality.

### N8 — cross-cycle echo

| Prior surface | Similar wall | Retirement mechanism and applicability |
|---|---|---|
| Coupled OS subsequential infinite-time transfer | Compactness gave a state but not temporal uniqueness | The massive infinite-time theorem added a one-dimensional Hölder uniqueness theorem; spatial compactness now gives existence only. |
| Massive fixed-spatial-volume Ruelle uniqueness | Exponential temporal memory on a compact block alphabet | Site anchoring makes the estimate uniform in all four directions, but three-dimensional phase transitions forbid reusing one-dimensional uniqueness. |
| Pure-gauge finite-volume Perron notes | Simple top state at every finite volume | A uniform gap was not obtained; the present theorem avoids claiming one. |
| Beta-six plaquette campaign | Finite data did not determine the infinite-volume observable | DLR existence does not determine a unique value and therefore does not retire that wall. |
| Fixed-background fermion locality notes | Massive fermions were local while the gauge measure remained open | The determinant is now included in an absolutely summable gauge interaction, closing existence but not gauge infrared uniqueness. |

The repeated successful mechanism is to replace a volume-wide constant by a
site-anchored summable density. The repeated warning is that compactness and
locality prove existence, not phase uniqueness.
