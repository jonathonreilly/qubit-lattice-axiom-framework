# Cubic One-Qubit Clifford-QCA Uniqueness Attack — Cycle 40

**Date:** 2026-07-14

**Type:** authority-free bounded primary-source/math classification,
proper-cubic representation split, exact radius-one symplectic census,
static and transported protocol-equivalence attack, fixed-record witnesses,
conditional positive closure, and N1–N8 scoped obstruction audit

**Authority:** none. This note does not amend an axiom, register a primitive,
select a law, carrier-rotation action, boundary, record instrument, or physical
equivalence relation, and does not issue an audit verdict. It changes no live
policy, registry, queue, audit, or retained surface. **No live axiom or
primitive edit is justified** by this probe.

**Outcome class:** partial narrowing with a conditional positive closure. The
radius-one Clifford symplectic census is exhaustive in its stated domain. It
is not a universal no-go for cubic dynamics and not a complete exact-phase
classification.

## Result up front

There is no unconditional nontrivial unique one-qubit cubic Clifford-QCA law
under the live inputs. The first reason is more basic than a missing coupling:

> The **first surviving selector is the onsite cubic-rotation action** on the
> qubit's Pauli module.

The proper cubic rotation group is `O_cubic^+ ~= S_4`. The projective onsite
one-qubit Clifford action on Pauli axes reduces to
`Sp(2,F_2) ~= S_3`. Up to onsite Clifford conjugacy, there are three
homomorphism types:

1. **site-only/trivial:** rotations move lattice sites and do not recode the
   onsite Pauli labels;
2. **sign quotient:** `S_4 -> C_2 -> S_3`; and
3. **axis quotient:** `S_4 -> S_4/V_4 ~= S_3`, the full permutation action on
   the three unsigned Pauli axes.

The live Lattice and Qubit axioms do not link spatial rotations to one of
these onsite actions. Qubit says no possibility is privileged; it does not
declare the qubit to be a spatial spinor, a scalar, or a sign representation.

For a translation-invariant, range-one, standard-six-neighbor one-qubit
Clifford QCA, the exact finite census is:

| onsite cubic action | center coefficient options | `+x` coefficient options after stabilizer | symplectic skeletons | neighbor-coupled skeletons |
|---|---:|---:|---:|---:|
| site-only/trivial | 16 | 16 | 24 | 18 |
| sign quotient | 4 | 4 | 4 | 2 |
| full Pauli-axis quotient | 2 | 4 | 1 | 0 |

Thus the action choice changes whether nontrivial neighbor dynamics exists at
all. Full Pauli-axis locking leaves only the identity symplectic skeleton in
this radius-one cardinal-neighbor class. Site-only covariance leaves 18.

For the literal site-only action, the 18 neighbor-coupled skeletons reduce to
four classes under common onsite Clifford conjugacy. They remain four under
arbitrary *static* translation-invariant Clifford-QCA similarity:

```text
L_s,
L_(1+s),
L_s H,
L_(1+s) H,

s = x+x^-1+y+y^-1+z+z^-1.
```

The first two are involutive shears. The last two are propagating companion
rules with trace polynomials `s` and `1+s`. Fixed finite Pauli-record
protocols distinguish all four.

Allow every **uniformly bounded-range time-dependent Clifford frame** and
transport the complete protocol. The two shears become exactly equivalent by
an alternating onsite frame, but neither companion can join them and the two
companions cannot join each other. Three uniformly local symplectic protocol
classes survive:

```text
{L_s, L_(1+s)},
{L_s H},
{L_(1+s) H}.
```

This three-class result is not merely a radius-one frame search. Uniform
bounded range over `F_2` forces the frame sequence eventually to repeat, which
would make positive powers of the two updates similar. Their trace-power
polynomials rule that out exactly.

If arbitrary finite-horizon frames of growing range are permitted, every pair
of reversible laws can be transported into every other pair recursively.
That mathematical quotient is exact but erases law selection by definition;
it is not an infinite-time uniformly local physical equivalence.

There is one useful positive result:

> **Conditional one-skeleton closure.** Choose the site-only rotation action,
> require a neighbor-coupled *symplectic involution*, and quotient by complete
> protocol transport under uniformly onsite Clifford frames. Then the two
> shears are one nontrivial symplectic skeleton class.

That does not yet give one exact law. Each site-only symplectic skeleton has
at least four homogeneous Pauli phase/sign lifts, fixed record protocols read
those signs, and the physical record category has not been proved closed
under the alternating frame. The conditional closure is the strongest
surviving steelman, not an axiom result.

## 1. Foundation and primitive boundary

The supplied carrier is exactly one `M_2(C)` possibility algebra per named
site of standard `Z^3`. Lattice supplies nearest-neighbor adjacency,
translations, and proper cubic rotations. It does not supply an action of
those rotations on the onsite Pauli axes. Admissibility supplies an
availability rule, explicitly not dynamics.

The approved kinetic-isotropy primitive fixes only `c_t=c_s` at the kinetic
form level. Its source explicitly supplies no phase, selector, or dynamics.
The realized-state primitive permits pointwise evaluation at a realized
law-admissible state, but supplies no state, boundary, preparation, or
selection. Neither chooses a Clifford QCA, a cubic representation, or an
equivalence relation.

This cycle therefore treats every update, rotation action, boundary, and
record protocol as a named conditional test input. It grants none of them
premise status.

## 2. Primary-source boundary

Only primary sources are used for the external mathematical comparison. The
finite counts and obstruction proofs in this note are independently
recomputed by the companion runner.

| Primary source | Use here | Boundary |
|---|---|---|
| Schlingemann, Vogts, and Werner, [*On the structure of Clifford quantum cellular automata*](https://arxiv.org/abs/0804.4447) | Translation-invariant Clifford QCAs induce symplectic cellular automata on the Pauli/Weyl phase space. | The paper does not supply this framework's cubic action, exact radius-one census, or physical record quotient. |
| Schumacher and Werner, [*Reversible quantum cellular automata*](https://arxiv.org/abs/quant-ph/0405174) | A reversible QCA is a finite-propagation automorphism of the quasilocal algebra. | Locality does not select a law or record instrument. |
| Haah, [*Clifford Quantum Cellular Automata: Trivial group in 2D and Witt group in 3D*](https://arxiv.org/abs/1907.02075) | Three-dimensional translation-invariant Clifford QCAs have meaningful circuit/shift/stabilized equivalence data and can carry nontrivial boundary-form information in the paper's domain. | Stable equivalence permits operations outside the live fixed one-`M_2` carrier question and is not fixed-record protocol equivalence. Its explicit 3D examples must not be silently imported as radius-one qubit solutions. |
| D'Ariano, Erba, and Perinotti, [*Isotropic quantum walks on lattices and the Weyl equation*](https://arxiv.org/abs/1708.00826) | For two-dimensional internal walk carriers, the action of an isotropy group and the chosen Cayley graph are load-bearing parts of a uniqueness classification. | Their 3D Weyl result uses the admissible quantum-walk graph/support and a single-particle walk, not this standard-cardinal many-body Clifford-QCA class. |

The literature supports the representation type and warns that equivalence
and isotropy data matter. It is not cited as proof of the new finite counts.

## 3. Laurent-polynomial QCA representation

Let

```text
R = F_2[x^+/-1,y^+/-1,z^+/-1]
```

with involution `bar(x)=x^-1`, and similarly for `y,z`. A
translation-invariant Pauli string is a vector in `R^2`; the two components
encode its `X` and `Z` support. A one-qubit Clifford QCA has symplectic
skeleton

```text
Q in Mat_2(R),
bar(Q)^T lambda Q = lambda,
lambda = [[0,1],[1,0]].
```

This condition preserves every translated Pauli commutator. It also gives a
finite-range inverse:

```text
Q^-1 = lambda bar(Q)^T lambda.
```

For range one on the live graph, every entry of `Q` is supported in

```text
{0,+/-e_x,+/-e_y,+/-e_z}.
```

This is a symplectic skeleton. It records Pauli supports modulo Pauli signs.
An exact Clifford automorphism additionally chooses a compatible sign/phase
lift. A skeleton obstruction is therefore decisive—phases cannot create a
missing neighbor support—but a skeleton uniqueness result is weaker than an
exact-law uniqueness result.

## 4. The cubic-action split is exhaustive in the Clifford phase space

The proper cubic group acts on the six displacement vectors. To state
covariance on the Pauli module, choose a homomorphism

```text
rho: O_cubic^+ ~= S_4 -> Sp(2,F_2) ~= S_3.
```

The runner generates all 24 signed-permutation rotations and all six
`GL(2,2)` matrices. It then generates every homomorphism from two generators
and verifies the multiplication table. Exactly ten homomorphisms occur:

```text
1 with image size 1,
3 with image size 2,
6 with image size 6.
```

Conjugating by an onsite Clifford identifies the maps with the same image
type. These are precisely the trivial, sign-quotient, and axis-quotient cases
listed above. No `C_3` image occurs because `S_4` has no normal subgroup with
the required quotient.

This exhausts **Clifford onsite covariance actions on Pauli phase space**.
A non-Clifford onsite covariance action remains unclassified. Such an action
need not normalize the Pauli module, so it lies outside this finite symplectic
enumeration.

## 5. Exact radius-one covariance reduction

Let `A_0` be the coefficient matrix at the center and `A_+` the coefficient
at `+e_x`. Cubic covariance gives

```text
A_(R h) = rho(R) A_h rho(R)^-1.
```

Therefore:

- `A_0` must commute with the full image of `rho`;
- `A_+` must commute with the image of the stabilizer of `+e_x`; and
- all other directional coefficients are forced by one rotation taking
  `+e_x` to that direction.

This reduces the raw `2^28` coefficient assignments to 256, 16, and 8
candidates in the three representation types. The runner constructs every
candidate and tests the complete Laurent identity
`bar(Q)^T lambda Q=lambda`, not only zero-momentum unitarity.

### 5.1 Site-only action

All six direction coefficients are equal. Define the cubic neighbor sum

```text
s=x+x^-1+y+y^-1+z+z^-1.
```

Every entry is in `{0,1,s,1+s}`. Because `bar(s)=s`, the symplectic condition
reduces to

```text
det Q = 1 in F_2[s].
```

The exact census contains 24 matrices. Six are onsite `SL(2,F_2)` maps and 18
are neighbor coupled.

### 5.2 Sign-quotient action

Only four center and four stabilized-edge matrices survive covariance. Four
are symplectic, of which two are neighbor coupled. With

```text
H=[[0,1],[1,0]],
N=I+H=[[1,1],[1,1]],
```

the two nonlocal skeletons may be written

```text
I+sN,
H+sN.
```

They are statically distinct but related at skeleton level by an alternating
onsite `H` frame. Exact lift signs still require a separate audit.

### 5.3 Full Pauli-axis quotient

The center commutant has two elements and the stabilized-edge commutant has
four. Of the eight candidates, only the onsite identity is symplectic. Hence:

> With the full proper-cubic axis permutation acting on the one-qubit Pauli
> module, there is no neighbor-coupled range-one Clifford symplectic QCA on
> the standard six cardinal neighbors.

This is a narrow carrier/support obstruction. It does not exclude larger
radius, multiple qubits per cell, BCC/body-diagonal support, non-Clifford QCA,
or a non-Clifford covariance representation.

## 6. Site-only action: four exact static skeleton classes

Use

```text
L_f = [[1,0],[f,1]],
C_f = L_f H = [[0,1],[1,f]].
```

The four onsite-conjugacy representatives and their generator actions are:

| representative | `alpha(X_0)` | `alpha(Z_0)` | skeleton behavior |
|---|---|---|---|
| `L_s` | `X_0 product_N Z` | `Z_0` | involutive shear |
| `L_(1+s)` | `Y_0 product_N Z` | `Z_0` | involutive shear |
| `C_s=L_s H` | `Z_0` | `X_0 product_N Z` | propagating companion |
| `C_(1+s)=L_(1+s)H` | `Z_0` | `Y_0 product_N Z` | propagating companion |

Here `product_N` runs over the six nearest neighbors; irrelevant Hermitian
Pauli signs are omitted only in this skeleton table.

All 18 nonlocal matrices lie in four common-onsite Clifford orbits of sizes
`6,6,3,3`. The representatives also remain distinct under an arbitrary
static translation-invariant Clifford-QCA similarity, not merely onsite
similarity.

Two similarity invariants prove it:

1. `tr(Q)` distinguishes each companion from the shears and distinguishes
   `C_s` from `C_(1+s)`:

   ```text
   tr(L_s)=tr(L_(1+s))=0,
   tr(C_s)=s,
   tr(C_(1+s))=1+s.
   ```

2. For a shear, the ideal generated by all entries of `Q-I` is invariant
   under similarity. It is `(s)` for `L_s` and `(1+s)` for `L_(1+s)`.
   These are distinct proper ideals; their generators sum to one and neither
   is a Laurent monomial unit.

Each representative has an explicit finite-depth Clifford implementation:
the all-edge `CZ` layer gives `L_s`; adding a common onsite phase
transvection gives `L_(1+s)`; and composing with common onsite Hadamard gives
the companion pair. Thus these are not formal polynomial ghosts.

## 7. Exact phase/sign fibre

The symplectic matrix forgets whether a mapped Hermitian Pauli string has a
plus or minus sign. For the site-only action, composing any of the 24
skeletons with one of the four common onsite Pauli automorphisms preserves
translation symmetry, proper-cubic site covariance, and range. This gives at
least

```text
24 x 4 = 96
```

exact homogeneous Clifford lifts before physical equivalence is imposed.

The fibre is record-visible with a fixed dictionary. Identity and common
onsite `Z` have the same symplectic skeleton, but on an `X+` preparation a
fixed `X` record returns `+` for one and `-` for the other. Consequently a
unique symplectic skeleton is not yet a unique exact protocol law.

This cycle gives a lower bound and exact separator; it does not enumerate
every projective lift for every nontrivial `rho`.

## 8. Fixed finite record protocols separate the four classes

No tomography assumption is needed for an explicit separator. Use finite
product boundaries and one-site Pauli records.

1. Prepare the center in `X+` and its six neighbors in `Z+`. A final center
   `X` record has expectation `1` under `L_s` and `0` under `L_(1+s)`.
   Thus one transcript is deterministically `+`; the other is unbiased.
2. On the same boundary, a final center `Z` record has expectation `1` under
   `C_s` and `0` under `C_(1+s)`.
3. Prepare every site in `Z+`. A center `X` record has expectation `0` for
   either shear and `1` for either companion.

These are finite causal-cone protocols. They do not derive that the framework
admits those preparations or instruments. They prove the conditional:

> If the complete fixed local Pauli protocol category is physical, the four
> skeleton classes are record-distinguishable.

## 9. Uniformly local time-dependent protocol equivalence

Let source and target skeletons be `A` and `B`. A time-dependent frame family
transports the repeated update exactly when

```text
B = F_(t+1) A F_t^-1,
```

or equivalently

```text
F_(t+1)=B F_t A^-1.
```

### 9.1 Positive shear equivalence

Let `L_1` be the onsite transvection and choose

```text
F_t=L_1^t.
```

Since all lower shears commute and `L_1^2=I` over `F_2`,

```text
F_(t+1) L_s F_t^-1=L_(1+s)
```

for every `t`. The frame is onsite and period two. At exact Clifford level an
onsite phase frame supplies the corresponding transport, with phase/sign
corrections included in the transported instruments.

### 9.2 General uniform-range obstruction

Suppose every `F_t` has support inside one fixed finite radius. There are only
finitely many binary Laurent matrices with that support. Hence some frame
repeats: `F_(t+p)=F_t` for a positive `p`. Iterating the transport equation
gives

```text
B^p F_t=F_t A^p.
```

Therefore `A^p` and `B^p` must have the same trace.

For a companion `C_f`, define

```text
t_p(f)=tr(C_f^p).
```

Cayley–Hamilton in characteristic two gives

```text
t_0=0,
t_1=f,
t_p=f t_(p-1)+t_(p-2).
```

Every `t_p(f)` is nonzero. Write `p=2^k m` with `m` odd. Frobenius gives
`t_p(f)=t_m(f)^(2^k)`. For odd `m`, `t_m` is monic of degree `m`, and
`t_m(f+1)+t_m(f)` has nonzero degree-`m-1` leading term. Therefore

```text
t_p(s) != t_p(1+s)
```

for every positive `p`. The substitution of the formal `f` by the Laurent
polynomial `s` is injective: the highest `f^n` term contains the unique extreme
Laurent monomial `x^n`, which cannot be canceled by lower powers. The formal
inequality therefore remains an inequality in the full three-variable
Laurent ring.

A shear has zero trace for every power because it is
involutive and `tr(I)=0` in characteristic two. It follows that:

- no uniformly bounded-range Clifford frame connects a shear to a companion;
- no such frame connects `C_s` to `C_(1+s)`; and
- the two shears form the only nontrivial collapse among the four.

The runner additionally exhausts every range-one frame and verifies the same
three-class partition directly.

### 9.3 Why arbitrary finite-horizon transport is broader

For any invertible `A,B` and any initial `F_0`, the recursion above defines an
exact frame for every finite time. For `C_s -> C_(1+s)` with `F_0=I`, the
polynomial degrees begin

```text
0,0,2,4,6,8,10,...
```

The finite adaptive full-abstraction theorem then transports every finite
protocol exactly, but the apparent local record dictionary spreads without a
uniform bound. Calling all such pairs one physical law would make every
reversible dynamics presentation-equivalent. That is a coherent mathematical
category, but it is too broad to select a local infinite-time TOE unless the
framework derives that growing records remain the same local physical
records.

## 10. Does any nontrivial unique class exist?

At three different levels:

1. **Current foundation, all permitted Clifford cubic actions:** no. The
   action `rho` is not selected, and the three actions give 18, 2, and 0
   nonlocal skeletons.
2. **Site-only action, static equivalence:** no. Four exact skeleton classes
   remain, plus sign/phase fibres.
3. **Site-only action + neighbor coupling + symplectic involution + uniformly
   local complete-protocol transport:** yes, conditionally, at skeleton
   level. The two shears are the only involutive nonlocal onsite-conjugacy
   classes and the alternating onsite frame identifies them.

This **conditional one-skeleton closure** is important. It shows exactly what
a future selection theorem could buy without claiming that the needed inputs
already derive. It still does not select a full TOE law: exact phase lift,
record-category closure, boundary/history, actual record formation,
probability, propagation phenomenology, matter, and gravity remain separate.

The first selectors, in order, are:

```text
onsite cubic-rotation action
  -> dynamical polynomial class (involutive shear or one of two companions)
  -> physical protocol-equivalence category
  -> Clifford phase/sign lift and fixed record dictionary.
```

## 11. Axiom consequence

No verbatim axiom addition follows. In particular, “proper-cubic covariant
one-qubit QCA” is not yet a unique referent: it needs the carrier rotation
action and the exact protocol equivalence typed.

There are three non-axiomatic closure routes worth preserving:

- clarify, as a definition of the existing Lattice/Qubit product structure,
  that proper cubic rotations act on sites only and leave onsite content
  labels untouched;
- state involution as a named conditional input, derive the one-skeleton
  theorem, and run an import-retirement audit against later propagation and
  record science; or
- define physical law identity as a complete uniformly local
  record/boundary/cost-preserving protocol autoequivalence and prove the
  actual record category closes under it.

Each route requires review, but none should be mislabeled “a new axiom is
mathematically forced.” The kinetic-isotropy and realized-state primitives do
not close these selectors and must not be enlarged to do so.

## 12. No-Go Discipline gate

**Gate status:** PASS for the narrow claim; broad uniqueness/no-go rhetoric is
demoted to **partial narrowing**.

The scoped negative claim is:

> The current inputs do not uniquely select a nontrivial homogeneous
> translation/proper-cubic-covariant radius-one one-qubit Clifford-QCA exact
> protocol law on the standard six-neighbor lattice. In the exhaustive
> Clifford phase-space census, the onsite cubic action changes the candidate
> count; under site-only action at least three uniformly local transported
> skeleton classes and exact phase fibres survive.

This is not a universal no-go against a unique cubic law, a larger-radius
Clifford law, a block/ancilla construction, a non-Clifford law, or the
conditional involutive one-skeleton closure.

### N1 — Alternative-route enumeration

The cycle includes **at least five attack routes**:

| route | marker | attempted uniqueness escape | result |
|---|---|---|---|
| site-only cubic action | ATTEMPTED | let full spatial symmetry act only on sites and select a unique range-one symplectic map | exact census leaves 18 nonlocal skeletons, four static classes, three uniform-transport classes |
| full Pauli-axis action | ATTEMPTED | lock the cubic axes to the three Pauli axes and use the stronger covariance to select a rule | only identity survives, so this action gives a narrow carrier/support obstruction rather than a nontrivial law |
| sign-quotient action | ATTEMPTED | use the remaining nontrivial homomorphism type | two nonlocal skeletons survive and collapse only conditionally under alternating transport |
| arbitrary static Clifford-QCA similarity | ATTEMPTED | identify the four site-only representatives using a non-onsite frame | trace and the `Q-I` entry ideal separate all four |
| uniformly bounded time-dependent frames | ATTEMPTED | transport complete protocols while retaining an infinite-time local record dictionary | the shears collapse, but trace powers leave three classes |
| arbitrary finite-horizon full transport | ATTEMPTED | quotient every reversible representative by history-dependent frames | exact, but frames grow in range and the quotient becomes universal rather than selective |
| global symplectic involution | ATTEMPTED | remove propagating companions and select the simplest reversible rule | succeeds conditionally at skeleton level after uniform shear transport; exact lift/category closure remains |
| stabilized 3D Clifford-QCA class | ATTEMPTED | import a circuit/shift/stabilized class invariant | Haah's equivalence changes the classification question; stabilization changes the live carrier question and fixed protocol closure is separate |

### N2 — Pairwise wall-independence table

Raw sub-obligations about boundary, instruments, decoder labels, record cost,
and phase frames collapse into `E`, the physical protocol-equivalence closure.
Exact Pauli signs collapse into the exact-law/equivalence identity rather than
being counted as a new wall. The collapsed set is:

```text
R = onsite cubic-rotation action,
D = dynamical symplectic class within that action,
E = exact physical law/protocol equivalence, including phase, record,
    boundary, and cost closure.
```

**Pairwise wall-independence table:**

| pair | closing first closes second? | closing second closes first? | independent? |
|---|---|---|---|
| `R,D` | no—trivial `R` still has three transported classes | no—a chosen matrix does not explain how rotations act on content | yes |
| `R,E` | no—choosing a representation does not define physical gauge | no—an equivalence functor does not choose the spatial/internal action | yes |
| `D,E` | no—a selected skeleton does not prove phase/record closure | no—uniform equivalence still has three classes to choose among | yes |

No inflated boundary/instrument wall count is used downstream.

### N3 — Hidden-wall scan

The note and runner were scanned for the required phrases. “Registered”
appears only when describing the cited approved-primitive registry status and
is non-load-bearing. “By construction” is avoided as a proof step. “Standard”
modifies the explicitly supplied six-neighbor lattice, not an imported QFT
result. “Clifford onsite action,” “uniform range,” “fixed protocol,” and
“symplectic skeleton” are all explicit scope conditions, not hidden premises.
This is the required **hidden-wall scan**.

### N4 — Residual matching

**Residual-matching table:**

| cited witness | witness residual | Cycle 40 residual | match? / use |
|---|---|---|---|
| `CUBIC_CZ_EDGE_RULE_UNIQUENESS_SELECTION_CYCLE36_NOTE_2026-07-14.md:16,82` | two selected-`Z` diagonal rules and transported-frame fork | full non-diagonal radius-one Clifford skeleton/equivalence | partial only; used as seed and phase-fibre control, not proof of the new census |
| `FOUNDATION_SITE_NET_RECORD_EQUIVALENCE_CLASSIFICATION_CYCLE21_NOTE_2026-07-14.md:21-50` | static common-onsite/site equivalence versus law-selected record category | static and transported QCA equivalence | match for equivalence typing only; not a law-count witness |
| `ADAPTIVE_RECORD_PROTOCOL_QCA_FULL_ABSTRACTION_THEOREM_NOTE_2026-07-14.md:179` | exact finite adaptive frame transport | exact finite-horizon transport and uniform-range qualification | exact match for finite transport; uniform obstruction is new here |
| `CUBIC_SPLIT_STEP_QW_QCA_PRIMARY_SOURCE_UNIQUENESS_AUDIT_2026-07-14.md:297,357` | live-carrier and space/carrier rotation action in quantum-walk constructions | one-qubit Clifford QCA rotation action | partial; used to motivate the representation split, not to transfer a walk no-go |
| Schlingemann–Vogts–Werner `0804.4447` | symplectic cellular representation of Clifford QCA | Laurent symplectic skeleton type | exact type match; finite cubic counts remain runner-derived |

Nonmatching quantum-walk and stabilized-QCA conclusions are explicitly
dropped as proof of the radius-one count.

### N5 — Resolution audit

The **resolution audit** is:

| resolution | tested? | statement licensed |
|---|---|---|
| one translated Pauli generator | yes | exact support and fixed-record witnesses |
| complete radius-one coefficient ball | yes | exhaustive skeleton counts for each Clifford `rho` type |
| all Clifford homomorphisms `S_4 -> S_3` | yes | three onsite-action conjugacy types |
| static translation-invariant QCA frames of arbitrary range | yes for the four representatives via similarity invariants | four site-only classes remain |
| uniformly bounded time-dependent Clifford frames | yes via eventual-period/trace theorem | exactly three site-only skeleton classes |
| exact phase/sign fibre | lower bound and separator only | at least four lifts per site-only skeleton; no complete lift census claimed |
| larger-radius Clifford QCA | no | **larger-radius Clifford QCA remain open** |
| stabilized/multi-qubit carrier | no | no fixed-carrier conclusion transferred |
| non-Clifford rule or covariance action | no | **non-Clifford QCA remain open** and the non-Clifford onsite covariance action remains unclassified |

Every negative sentence is restricted to the tested resolution.

### N6 — Partial-closure paths

The explicit **partial-closure paths** are:

1. a reviewed interpretation/definition clarification can choose the
   site-only action without adding dynamical physics;
2. a named involution import yields the conditional one-skeleton theorem and
   can later be retired if propagation/record science derives it;
3. a physical full-abstraction definition plus record/boundary/cost closure
   can quotient exact representatives without selecting their spelling; and
4. a block/BCC/larger-carrier theorem can leave the radius-one obstruction's
   domain rather than contradict it.

No route is mislabeled as an automatically required new axiom. The primitive
registry check confirms that kinetic isotropy and realized-state reference do
not already close `R`, `D`, or `E`.

### N7 — Strongest surviving steelman

The **strongest surviving steelman** is hostile to the negative wording:

> The cycle has almost produced the desired uniqueness theorem. Read the
> existing Lattice/Qubit product literally so cubic rotations act on sites,
> not on an internal spin label. Demand the already-attractive period-two
> reversible bare-metal constraint. Then the exhaustive census removes both
> propagating companion classes, leaving only `L_s` and `L_(1+s)`. The exact
> alternating onsite Clifford frame identifies those two with uniform range,
> and the adaptive transport theorem preserves every protocol in a closed
> record category. Therefore one nontrivial symplectic law class is selected;
> the remaining phase signs may be representation choices once the record
> functor is transported.

This steelman succeeds at skeleton level. Accordingly the output is partial
narrowing, not a broad no-go. The next exact targets are phase-lift involution
and physical record-category closure for that one class.

### N8 — Cross-cycle echo

The **cross-cycle echo** finds three prior retirement mechanisms:

- Cycle 36 reduced a continuous controlled phase to `pi` using global
  involution, then exposed a residual frame bit. The same mechanism removes
  Cycle 40's companions but needs exact phase/category closure.
- Cycle 21 separated foundation-static equivalence from a larger law-selected
  record category. Cycle 40 preserves that separation and uses uniform
  locality as the new infinite-time test.
- The adaptive full-abstraction note retired representative phases only after
  all boundaries, instruments, decoders, records, and costs were transported.
  Cycle 40 applies the same mechanism and proves where uniform range blocks
  it.
- The split-step/BCC audit kept larger carrier and graph routes alive instead
  of calling cardinal one-qubit failure universal. Cycle 40 does the same.

No structurally similar retired wall has been ignored.

## Reproduction

Run:

```bash
python3 scripts/cubic_one_qubit_clifford_qca_uniqueness_cycle40_2026_07_14.py
```

The runner changes no files. It verifies the cubic group and all ten
homomorphisms, the three exact radius-one censuses, the 24/18/four-class
site-only reduction, static similarity invariants, fixed record separators,
the uniform-frame partition and trace-power controls, growing finite-horizon
transport, conditional involutive closure, primary-source boundary, primitive
contract, and N1–N8 surface.

Expected result: `PASS=127`, `FAIL=0`.
