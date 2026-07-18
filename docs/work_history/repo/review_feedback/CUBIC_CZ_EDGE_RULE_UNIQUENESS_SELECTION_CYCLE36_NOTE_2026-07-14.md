# Cubic CZ-Edge Rule Uniqueness and Selection Attack — Cycle 36

**Date:** 2026-07-14

**Type:** authority-free first-principles candidate-class classification,
exact diagonal-Clifford census, physical-equivalence attack, record-protocol
witness, one-assumption-at-a-time enlargement, TOE residual ledger, and
N1–N8 scoped obstruction audit

**Authority:** none. This note does not amend an axiom, register a primitive,
select the exact law, boundary, instrument, pointer category, or equivalence
relation, and does not issue an audit verdict. It changes no live policy,
registry, audit, or review-queue surface. **No live axiom or primitive edit is
justified** by this probe.

## Result up front

The Cycle 33 all-edge `CZ` composition rule is **not unique at the global-law
level** under the smallest useful exact class tested here.

The class is deliberately narrow and physically legible:

1. one qubit is kept at each named cubic site;
2. each named site's selected local `Z` record projectors are fixed pointwise;
3. the update is a range-one diagonal Clifford automorphism;
4. it is translation covariant, proper-cubic covariant, and uses the same
   undirected coupling on every nearest-neighbor edge;
5. it is nontrivially entangling and its **global update** is involutive; and
6. support, radius, and circuit layer are minimized before any numerical
   coefficient is selected.

This is a **selected-Z subclass**, not a consequence of the bare Qubit axiom.
The Qubit axiom privileges no possibility. Pointwise `Z` preservation is a
candidate law-selected pointer restriction used to make the smallest exact
selection question finite.

Every homogeneous range-one diagonal Clifford law in this class has phase

```text
q(z) = b sum_x z_x + 2 c sum_<xy> z_x z_y        (mod 4),
```

where `b` is in `Z_4` and `c` is in `Z_2`. Entanglement forces `c=1`.
Global involution forces `b` even. Exactly two laws remain:

```text
U_0 = product_<xy> CZ_xy,
U_1 = Z_all U_0,
Z_all = product_x Z_x.
```

Equivalently, with `epsilon` in `{0,1}`,

```text
U_epsilon = Z_all^epsilon product_<xy> CZ_xy,

alpha_epsilon(Z_x) = Z_x,
alpha_epsilon(X_x) = (-1)^epsilon X_x product_(y nearest x) Z_y.
```

On infinite `Z^3`, `U_epsilon` is shorthand for the induced quasilocal
automorphism, not a claim that an infinite product is an element of the
quasilocal algebra. Every finite-support observable sees only its finite
causal cone. `Z_all` likewise denotes the common onsite-`Z` automorphism.

Both laws are homogeneous, proper-cubic covariant, translation covariant,
radius one, globally involutive, nontrivially entangling, and tied on minimal
support and depth. Geometry and minimality do not choose between them. The
remaining algebraic bit is the **uniform per-step onsite-Z parity**.

The two laws are not related by the foundation-licensed *static* group:
lattice translations, proper cubic maps, and a common onsite `PU(2)` recoding.
With a fixed coherent boundary and fixed record dictionary, seven disjoint
one-site records distinguish them with certainty:

```text
K_x = X_x product_(y nearest x) Z_y,
<K_x>_(U_0 |+...+>) = +1,
<K_x>_(U_1 |+...+>) = -1.
```

But there is an exact **time-dependent transported equivalence**. The
alternating frame `F_t=Z_all^t` obeys

```text
F_(t+1) U_0 F_t^dagger = U_1.
```

If boundary, instruments, readout labels, and every adaptive protocol are
co-transported, the two presentations have the same transported statistics.
That is law-relative equivalence, not the current foundation-static
equivalence. Therefore Cycle 36 isolates a real semantic/physical gate:

> Is the physical instrument and record category fixed across time, or may it
> be transported by an alternating onsite frame as part of the law's
> presentation?

Until that gate is derived or stated, `epsilon` may be either a
record-distinguishable law bit or a conditionally quotiented presentation bit.
This is not a ruling and not an axiom proposal.

The controlled-phase layer also remains a **constraint/preparation layer, not
the full `L*`**. It prepares graph/cluster-type correlations and supplies exact
local-to-global composition. It does not propagate stored `Z` content, choose
an actual record, define a clock, or supply matter and gravity.

## 1. Why this is the smallest useful candidate class

The foundation-maximal record category contains every one-site possibility in
`M_2(C)`. No entangling unitary preserves all named one-site factors. Cycle 21
proved that a full named-factor automorphism is only a site permutation plus
onsite recodings. An entangling search must therefore do one of two things:

- select a smaller pointer/record category; or
- transport the site net itself and separately prove record and cost closure.

This cycle takes the first route and keeps each local `Z` projector fixed
pointwise. A unitary that fixes the complete computational projector algebra
is diagonal. Clifford, nearest-neighbor range, and cubic homogeneity make the
class exactly enumerable while retaining a real entangler. This is the
smallest class containing the Cycle 33 rule and a meaningful competitor.

The restrictions do different jobs:

- pointwise local-`Z` preservation keeps locked record contents at their named
  sites during the constraint step;
- range one implements the supplied nearest-neighbor adjacency;
- one coefficient on every undirected edge removes axis and endpoint
  privilege;
- Clifford gives an exact finite stabilizer census, not a claim that Nature
  must be Clifford;
- global involution tests Cycle 33's stated reversible period-two property;
  and
- minimizing support/radius prevents an unused larger stencil from hiding a
  selector.

The classification is exact for this class. It is not a classification of all
qubit QCAs, all finite-depth Clifford circuits that merely normalize the
*global* diagonal algebra, or all non-Clifford local unitaries.

Schumacher and Werner's primary QCA treatment supplies the mathematical type:
translation-compatible finite-propagation lattice dynamics can be specified
by local rules with commuting translates
([Schumacher and Werner, 2004](https://arxiv.org/abs/quant-ph/0405174)).
It does not select this rule.

## 2. Exact finite edge census

Normalize away a global phase and enumerate every two-qubit diagonal gate
whose four entries are fourth roots of unity:

```text
D(e_01,e_10,e_11) = diag(1, i^e_01, i^e_10, i^e_11).
```

There are `4^3=64` such gates. The runner conjugates both Pauli `X`
generators and recognizes a Clifford exactly. The resulting census is:

| filter | exact count |
|---|---:|
| fourth-root diagonal gates modulo global phase | 64 |
| diagonal Clifford gates | 32 |
| endpoint-exchange-symmetric diagonal Cliffords | 8 |
| symmetric and entangling | 4 |
| symmetric, entangling, and edge-gate involutive | 2 |

The four symmetric entanglers are

| `a` | exponent tuple `(0,e_01,e_10,e_11)` | edge gate |
|---:|---|---|
| 0 | `(0,0,0,2)` | `CZ` |
| 1 | `(0,1,1,0)` | `(S tensor S) CZ` |
| 2 | `(0,2,2,2)` | `(Z tensor Z) CZ` |
| 3 | `(0,3,3,0)` | `(S^dagger tensor S^dagger) CZ` |

On the degree-six cubic lattice, placing one such gate on every edge gives

```text
product_<xy> [(S^a_x S^a_y) CZ_xy]
 = (product_x S_x^(6a)) product_<xy> CZ_xy
 = Z_all^(a mod 2) U_0.
```

Thus four edge presentations collapse to the two global laws `U_0` and
`U_1`.

If one requires each *edge gate* to square to the identity, only `a=0,2`
remain and both compile to `U_0`. That would make `CZ` appear unique. But
**edge-gate involution is an extra assumption** about a chosen decomposition,
not a consequence of global-law involution. The physical update is the global
automorphism. Applying involution to an arbitrary factorization would select
a presentation before physical equivalence has been settled.

Gottesman's stabilizer formalism is the primary algebraic authority for the
Clifford/Pauli calculation
([Gottesman, 1997](https://arxiv.org/abs/quant-ph/9705052)). The `64/32/8/4/2`
census and cubic collapse above are independently recomputed by the local
runner.

## 3. Exact global classification

A diagonal Clifford phase polynomial has linear terms over `Z_4` and
quadratic controlled-`Z` terms with coefficient `2`. Translation covariance
makes the onsite coefficient common. Proper cubic covariance and undirected
endpoint symmetry make the nearest-neighbor coefficient common across all six
directions. Range one excludes more distant quadratic terms. Up to a global
phase,

```text
q(z)=b sum_x z_x + 2c sum_<xy> z_x z_y.
```

There are eight homogeneous range-one laws `(b,c)`. Four have `c=1` and are
entangling. Squaring removes the quadratic part automatically and leaves

```text
2b sum_x z_x.
```

Involution for every finite-support configuration requires `2b=0 mod 4`, so
`b=0` or `2`. These are precisely `U_0` and `U_1`.

Both candidates use the same two-site entangling support, the same radius-one
causal cone, the same commuting edge layer, and no privileged cubic axis.
There is no further simplicity ordering between them. An onsite `Z` is not
costlier when the odd-`a` edge presentation compiles it into the identical
homogeneous edge layer.

The diagonal hierarchy is much larger away from Clifford phases. Cui,
Gottesman, and Krishna characterize diagonal gates in the Clifford hierarchy
using root-of-unity polynomial phases
([Cui, Gottesman, and Krishna, 2016](https://arxiv.org/abs/1608.06596)). That
source supports the phase-polynomial type, not any framework selection.

## 4. Static physical-equivalence attack

Suppose a common onsite unitary `V` statically conjugates `alpha_0` to
`alpha_1`. The only nontrivial one-site observables fixed by either update are
on the `Z` axis. Any `X` or `Y` component grows the six-neighbor `Z` support.
Therefore `V` must map the `Z` axis to itself, possibly reversing it.

There are two cases:

1. `V` is diagonal in `Z`. It commutes with both diagonal global updates, so
   it cannot change `epsilon`.
2. `V` is diagonal times `X`. Common `X` complements every bit. For the cubic
   graph,

   ```text
   2 sum_<xy> (1-z_x)(1-z_y)
    = 2|E| - 2d sum_x z_x + 2 sum_<xy> z_x z_y  (mod 4),
   ```

   with `d=6`. The variable term vanishes modulo four, leaving only a global
   phase. Again `epsilon` is unchanged.

Translations and proper cubic rotations also preserve a uniform onsite bit.
Thus the two updates are inequivalent under the foundation-static common
onsite/site group.

The runner checks this on the `3 x 3 x 3` periodic cubic graph: 27 sites, 81
undirected edges, degree six at every site. It also enumerates the 24 signed
onsite Clifford frames and the eight that normalize the `Z` axis. The proof
above covers continuous `PU(2)`, not only those 24 controls.

This conclusion is conditional on the selected-`Z` physical category. It is
**not a no-go against** a larger law-relative equivalence.

## 5. Strongest equivalence steelman: alternating frame

Let

```text
F_t=Z_all^t.
```

Because `Z_all` commutes with `U_0`, at every integer step

```text
F_(t+1) U_0 F_t^dagger = Z_all U_0 = U_1.
```

On the infinite lattice this equation is an equality of quasilocal
automorphisms, verified on every finite-support observable. The runner's
finite matrices check the corresponding finite-causal-cone identity.

This is an exact history-dependent change of presentation. If an instrument
at step `t` is replaced by its `F_t`-transport, the boundary is transported,
and all outcome labels and feed-forward branches are carried along, every
adaptive protocol probability is unchanged. That is the strongest surviving
steelman: `epsilon` may be a temporal gauge bit rather than new physics.

The foundation currently licenses common static onsite recoding. It does not
currently declare arbitrary time-dependent recoding of a fixed physical
record dictionary to be identity. A locked `X`-context record changes its
sign label under alternating `Z`; a fixed decoder can therefore expose the
difference. The law-selected physical instrument category determines whether
that sign is a fact or a transported name.

## 6. Exact record-protocol witness

Use one center site `x` and its six nearest neighbors. Prepare the coherent
all-plus boundary and run one update. Then make seven pairwise-disjoint
one-site records: `X` at the center and `Z` at every neighbor. Multiply their
scalar signs after readout. This measures

```text
K_x=X_x product_(y nearest x) Z_y.
```

Since

```text
alpha_0(K_x)=X_x,
alpha_1(K_x)=-X_x,
```

the parity is deterministically `+1` for `U_0` and `-1` for `U_1`. The
runner contracts the 128 amplitudes of this seven-site causal-cone witness
exactly.

Two controls matter:

- on an all-zero `Z` boundary, both diagonal laws act identically;
- on the plus boundary, every final `Z`-only transcript has the same uniform
  probability under both laws.

Therefore **boundary changes observability; it does not select epsilon**.
Likewise **instrument changes observability; it does not select epsilon**.
A coherent boundary and a transverse fixed record protocol expose the bit;
`Z`-only records hide it. Neither control tells Nature which law to use.

The graph-state/cluster interpretation is standard: a uniform controlled-
phase layer acting on plus states produces stabilizer correlations, and
adaptive single-qubit measurement can turn such correlations into a
measurement-driven computation
([Raussendorf, Browne, and Briegel, 2001](https://arxiv.org/abs/quant-ph/0108118)).
That result makes the instrument dependence unsurprising; it does not supply
this framework's record instrument or actuality rule.

## 7. Enlarge one assumption at a time

### 7.1 Non-Clifford controlled phase, with involution retained

Replace every `CZ` by

```text
C_theta=diag(1,1,1,exp(i theta)).
```

This keeps pointwise `Z` records, exchange symmetry, range one, translation
covariance, proper-cubic covariance, and commuting edge order. For any finite
configuration containing exactly one occupied nearest-neighbor pair, global
involution requires

```text
exp(2 i theta)=1.
```

Hence `theta=0` or `pi`; nontrivial entanglement selects `theta=pi`. Allowing a
symmetric onsite edge phase does not rescue a continuous alternative. A
single occupied site first quantizes that onsite phase, and an adjacent pair
still independently forces `2 theta=0 mod 2pi`.

So global involution is the first exact algebraic selector of the entangling
controlled phase. It selects `CZ` rather than a continuum, but it does **not**
select the residual onsite parity `epsilon`.

If involution is dropped, the phase continuum opens immediately. On
`C_theta |++>`, fixed one-site/two-site record contexts give

```text
<X tensor I> = (1+cos theta)/2,
<X tensor Z> = (1-cos theta)/2,
<Y tensor I> = sin(theta)/2.
```

Thus `theta=pi/2` and `theta=pi` are exactly record-distinguishable once those
instruments are admitted.

### 7.2 Edge order, with pointwise local-Z preservation retained

Order does nothing. Every diagonal edge gate commutes with every other one,
including non-Clifford controlled phases. The runner checks all 4,096 ordered
pairs in the finite 64-gate census.

Order first becomes physical after relaxing pointwise preservation of each
named local `Z` coordinate. A directed `CNOT` normalizes the global diagonal
algebra but sends target `Z` to two-site `ZZ`. On a three-site path, from
record word `100`,

```text
CNOT_(0->1) then CNOT_(1->2): 111,
CNOT_(1->2) then CNOT_(0->1): 110.
```

Final `Z` records distinguish the schedules. But this enlargement imports a
control/target orientation and an update partition. Those are precisely the
new selectors; they are outside the undirected, no-privileged-axis baseline.

### 7.3 Boundary

The same `U_epsilon` accepts both all-zero and coherent all-plus boundaries.
The first masks the candidate difference and the second permits a transverse
stabilizer witness. This repeats Cycle 33's boundary-independence result at
the selection layer: an exact local update does not choose its own global
history datum.

### 7.4 Instrument

A `Z`-only record category quotients the two candidates operationally for the
displayed one-step boundary tests. A fixed transverse `X/Z` category separates
them. Full time-dependent co-transport quotients them again. Hence the first
irreducible operational selector is not a preferred measurement angle by
itself; it is the exact definition of the physical record/instrument category
and its permitted temporal equivalences.

### 7.5 Selector ladder

The one-at-a-time result is:

```text
range-one homogeneous pointwise-Z entangler
  + global involution
    -> controlled phase theta=pi
    -> two global laws U_0 and U_1 remain

fixed temporal record dictionary + coherent boundary + transverse instrument
    -> epsilon is a measurable binary law atom

fully co-transported temporal dictionary/boundary/instruments
    -> epsilon is a conditional quotient
```

Nothing in cubic symmetry, minimal support, minimal radius, Clifford closure,
or global involution chooses `epsilon`. The exact-law program must derive it,
supply it, or prove that the transported quotient is the physical category.

## 8. What the CZ layer does and does not buy

The positive content is substantial but narrow. `CZ` supplies:

- one exact local-to-global quasilocal automorphism;
- cubic and translation covariance;
- a commuting no-schedule constraint layer;
- entanglement and graph-state stabilizer correlations;
- finite adaptive protocol contraction once a boundary and instruments are
  supplied; and
- a clean laboratory for deciding static versus transported record identity.

It is a **constraint/preparation layer, not the full `L*`** because it is
diagonal, period two, and leaves every local `Z` content stationary. The
following TOE fields remain:

- **kinetic propagation**: transport, dispersion, a Hamiltonian/action, and a
  controlled continuum/Lorentz/CPT limit;
- **record trigger**: when and where a record forms, which admissible
  possibility locks, physical permanence, and the actual realized branch;
- **boundary/history**: the exact global state/history datum or a law that
  derives it;
- **instrument category**: the physical pointer contexts, record maps,
  decoder, adaptivity, and permitted temporal equivalences;
- **probability-to-frequency**: weights, actuality, typicality, and observed
  long-run frequency;
- **clock metric**: tick identity, local rate, synchronization, arrow, and
  relativistic time;
- **fermion statistics**: fermionic composition, chirality, generations,
  interactions, masses, and couplings;
- **gauge dynamics**: gauge fields, constraints, charges, and their kinetic
  law;
- **capacity renewal**: how permanent finite-capacity record sites support
  continuing history and what thermodynamic cost is paid; and
- **gravity field equation**: source, curvature response, equivalence
  principle, and the classical/continuum limit.

Selecting `epsilon` would close none of those fields. It would only complete
one very small constraint-layer specification.

## 9. Consequence for axiom need

Cycle 36 does not support inserting “all-edge `CZ`” into the axioms. Even this
narrow class leaves a binary global-law residue and an unresolved physical
equivalence category. More importantly, a selected constraint layer is not a
record-formation law and not a complete dynamics.

The constitutional pressure remains at the type level:

1. an exact law or exact record-faithful law-equivalence class must ultimately
   be fixed or uniquely derived;
2. the boundary/history relation must be fixed or derived;
3. the physical instrument/record category and allowed temporal recodings
   must be fixed or derived; and
4. actuality/record formation must be fixed or derived separately from the
   reversible constraint layer.

Those may eventually compress into one exact compositional Law clause, but
this probe does not establish the wording or prove that they are one atom.
The correct current status is conditional construction plus an exact residual
ledger.

## 10. No-Go Discipline gate

**No-Go Discipline status:** `FAIL` for unconditional physical inequivalence;
that broad claim is demoted to `partial-narrowing`.

The exact retained classification is:

> In the homogeneous range-one pointwise-`Z`-preserving diagonal Clifford
> class, cubic covariance, nontrivial entanglement, global involution, and
> minimum support/radius do not uniquely select the all-edge `CZ` global law;
> `Z_all U_CZ` survives with equal structural cost.

This retains two representatives under **foundation-static equivalence only**.
It is not a no-go against deriving one candidate from additional physical
content, and it is not a no-go against quotienting them under a proved
transported record equivalence. The unconditional claim that the two
representatives are physically inequivalent is not shipped.

### N1 — Alternative-route enumeration

| route | honesty marker | attack attempted | exact result and authority |
|---|---|---|---|
| fourth-root diagonal edge census | ATTEMPTED | Exhaust all `64` fourth-root diagonal two-site gates and filter Clifford, endpoint symmetry, entanglement, and edge involution. | Four symmetric entanglers survive before cubic compilation; [runner](../../../../scripts/cubic_cz_edge_rule_uniqueness_selection_cycle36_2026_07_14.py), lines 136–173. |
| global phase-polynomial census | ATTEMPTED | Enumerate every homogeneous range-one diagonal Clifford phase polynomial compatible with the selected class. | Exactly `U_0` and `U_1` survive global involution and equal support/radius; runner, lines 188–218. |
| foundation-static quotient | ATTEMPTED | Apply translations, proper cubic rotations, and common onsite `PU(2)` recodings that preserve the selected `Z` axis. | The uniform onsite parity survives; this proves inequivalence under the stated static group only; runner, lines 221–268. |
| temporal co-transport | ATTEMPTED | Transport boundary, instruments, decoder, outcome labels, and adaptive branches with `F_t=Z_all^t`. | The two representatives are conditionally one transported law class; this defeats unconditional physical inequivalence; section 5 and [Cycle 39](TEMPORAL_PROTOCOL_EQUIVALENCE_ALTERNATING_FRAME_CYCLE39_NOTE_2026-07-14.md), lines 27–69. |
| non-Clifford controlled phase | ATTEMPTED | Replace `CZ` by `C_theta`, allow a symmetric onsite edge phase, and retain global involution. | Involution selects `theta=pi` but does not select the residual onsite parity; runner, lines 335–379. |
| fixed boundary and instrument | ATTEMPTED | Compare zero/plus boundaries and fixed `Z`-only versus transverse record instruments. | The fixtures mask or distinguish `epsilon`; they do not select it; runner, lines 311–332. |
| edge order and directed enlargement | ATTEMPTED | Exhaust diagonal order and then leave the class with directed `CNOT` schedules. | Diagonal order is inert; directed order becomes visible only after importing orientation and a partition; runner, lines 382–410. |

All seven routes were attempted in this cycle or its exact Cycle-39 follow-up.
The five-route minimum is exceeded.

### N2 — Wall-independence audit

The raw continuous-phase condition `W_theta` is retired inside the tested
class: global involution forces `theta=pi` once nontrivial entanglement is
required. It is not counted in the collapsed wall set.

The collapsed set is exactly:

- `W_epsilon`: identify the exact representative or prove the physical
  transported quotient;
- `W_B`: fix or derive the boundary/history datum;
- `W_I`: fix or derive the physical record/instrument category and its
  permitted temporal recodings; and
- `W_A`: supply or derive actual record formation and one-outcome history.

All six unordered pairs are tested:

| pair | does closing the first automatically close the second? | does closing the second automatically close the first? | independent? |
|---|---|---|---|
| `W_epsilon`, `W_B` | No; a representative or quotient does not choose a boundary. | No; a boundary can expose parity without selecting the representative or quotient. | Yes |
| `W_epsilon`, `W_I` | No; law identity alone does not define the physical instrument category. | No; defining the category does not by itself prove the exact representative/quotient theorem. | Yes |
| `W_epsilon`, `W_A` | No; selecting or quotienting parity does not actualize a record. | No; one actual record does not identify the counterfactual law representative. | Yes |
| `W_B`, `W_I` | No; a boundary does not define the allowed instruments. | No; an instrument category does not select the history datum. | Yes |
| `W_B`, `W_A` | No; a supplied boundary does not cause one actual record. | No; an actual record does not determine the full boundary/history datum. | Yes |
| `W_I`, `W_A` | No; an instrument category does not make an outcome occur. | No; occurrence does not determine the complete physical instrument category. | Yes |

### N3 — Hidden-wall scan

| searched phrase | classification |
|---|---|
| `we assume` | Absent outside this quoted scan key. |
| `by construction` | Absent outside this quoted scan key. |
| `as is standard` | Absent outside this quoted scan key. |
| `the framework provides` | Absent outside this quoted scan key. |
| `bridge context` | Absent outside this quoted scan key. |
| `background` | Absent outside this quoted scan key. |
| `naturally` | Absent outside this quoted scan key. |
| `obviously` | Absent outside this quoted scan key. |
| `standard QFT` | Absent outside this quoted scan key. |
| `registered` | Absent outside this quoted scan key. Primitive provenance is handled by the explicit registry check in N6. |
| `canonical` | Absent outside this quoted scan key. |

| load-bearing term | explicit classification |
|---|---|
| “preserves records” | Pointwise preservation of a selected local `Z` projector algebra, not every Qubit possibility. |
| “involutive” | A filter on the global update, not on an arbitrary edge factorization. |
| “same law” | Split into foundation-static conjugacy and time-dependent complete-protocol transport. |
| “minimum depth” | A commuting-layer convention; the compiled onsite phase is not charged twice. |
| “witness” | A stated boundary plus a stated record instrument, not an undeclared measurement premise. |

No hidden condition is promoted by this scan; the collapsed N2 count remains
four.

### N4 — Exact residual matching

| cited witness | witness residual | residual for which it was considered | match? | disposition |
|---|---|---|---|---|
| `scripts/cubic_cz_edge_rule_uniqueness_selection_cycle36_2026_07_14.py`, lines 136–218 | Exact finite edge census and global phase-polynomial classification inside the declared class. | Whether the declared filters leave one or two representatives. | Yes | Retain as exact support for `U_0/U_1`. |
| same runner, lines 221–268 | Static common-onsite/site quotient and the finite alternating-frame identity. | Inequivalence under foundation-static equivalence only. | Yes | Retain at that resolution; do not extend it to all temporal equivalences. |
| same runner, lines 311–332 | A fixed coherent boundary and transverse instrument distinguish the representatives. | Whether Nature selects one representative. | No | **drop as selection evidence**; retain only as an observability witness. |
| [Cycle 39](TEMPORAL_PROTOCOL_EQUIVALENCE_ALTERNATING_FRAME_CYCLE39_NOTE_2026-07-14.md), lines 27–69 | Complete co-transport gives equality; a fixed odd-time record separates. | Whether the boundary alone selects `epsilon`. | No | Drop as boundary-selection evidence; retain for the temporal-category fork. |

After the two mismatches are dropped, the runner still proves the narrow
two-representative classification and static quotient result. It does not
prove a physical selector.

### N5 — Resolution and rhetoric audit

| resolution | tested? | exact result | permitted rhetoric outside that resolution |
|---|---|---|---|
| per two-site fourth-root diagonal gate | Yes | Exhaustive `64/32/8/4/2` census. | Exact only for that finite gate domain. |
| per homogeneous global range-one diagonal Clifford phase | Yes | Exactly `U_0` and `U_1` survive. | “Not unique” is permitted for the declared phase-polynomial class. |
| finite `3 x 3 x 3` periodic cubic control | Yes | Degree six collapses four edge presentations to two global laws and preserves parity under the tested static group. | Supports the analytic cubic calculation; it is not a census of every QCA. |
| seven-site causal cone | Yes | A fixed coherent boundary/transverse instrument distinguishes parity; `Z`-only records mask it. | Observability only, not selection. |
| every finite-support observable under `F_t` | Yes, analytically | The alternating-frame automorphism identity holds quasilocally. | Conditional presentation equivalence only. |
| complete transported finite adaptive protocol | Yes, by Cycle 39 | Statistics agree when every named temporal object is co-transported. | Defeats unconditional physical inequivalence. |
| all translation-covariant Clifford QCAs, non-diagonal circuits, encoded pointers, and non-Clifford automorphisms | No | Not classified. | No claim. |
| full TOE law, boundary, actuality, matter, or gravity | No | Not tested by this constraint-layer census. | No claim. |

The allowed conclusion is the narrow two-representative result. The disallowed
conclusions are “no complete law can be unique” and “the two representatives
are unconditionally different physics.” The finite census is exhaustive only
at the resolutions marked tested above.

### N6 — Partial-closure paths

Primitive registry check complete: the approved scale-reference,
kinetic-isotropy, and realized-state primitives are premise nodes, not walls,
and none supplies `epsilon`, a boundary, an instrument category, an update, or
actual record-formation dynamics.

| candidate closure path | source and status | what it would close | classification |
|---|---|---|---|
| global involution | this note and runner, exact in the declared class | retires `W_theta` by selecting `theta=pi` | Derived closure; no new axiom. |
| complete temporal co-transport | Cycle 39, exact conditional classification | closes the parity quotient branch of `W_epsilon` if the physical category is proved closed under the transport | Equivalence theorem/definition path. |
| fixed temporal record dictionary | this note, exact conditional separator | makes parity physically measurable and narrows `W_I`; it does not select parity | Conditional theorem path. |
| boundary or kinetic compatibility selector | Cycle 33 boundary controls and the open kinetic lane | could select a representative or derive a unique boundary | Live physics derivation, not yet closure. |
| exact-law-selected pointer algebra | Cycle 21 site-net classification, live route | could retire the selected-`Z` restriction and determine the physical normalizer | Law theorem path. |
| approved primitive registry | `docs/audit/data/axiom_premise_nodes.json` and each listed source note, checked | closes none of `W_epsilon`, `W_B`, `W_I`, or `W_A`; approved primitives remain valid premises rather than walls | Registry accounting, not a new premise. |

No result here says “new axiom required.” A theorem, equivalence definition,
conditional datum, or later exact-law completion may retire a wall.

### N7 — Strongest surviving steelman

**Hostile reviewer:** “Your claimed physical distinction is an artifact of
holding the dictionary fixed. The exact family `F_t=Z_all^t` transports
`U_0` into `U_1` at every step. Cycle 39 carries the boundary, instruments,
decoder, outcomes, idle calibrations, and feed-forward branches with it and
preserves every finite adaptive transcript probability. If physical records
are the relational objects in that closed transported category, there is one
law class, not two physical laws. Your fixed-decoder separator proves only
that changing the update while refusing to transport the rest changes the
experiment.”

| hostile route | strongest authority | convincing? | required gate outcome |
|---|---|---|---|
| complete temporal co-transport | section 5 and Cycle 39, lines 27–69 | Yes | `FAIL` for unconditional physical inequivalence; demote to `partial-narrowing` and retain two representatives under foundation-static equivalence only. |

The steelman is convincing. The broad no-go is therefore not shipped. The
narrow finite-class classification survives because co-transport does not turn
the two phase polynomials into one representative under the explicitly stated
static group.

### N8 — Cross-cycle echo

| prior source | similar earlier wall | retired or narrowed since? | mechanism and applicability here |
|---|---|---|---|
| Cycle 20 adaptive full-abstraction theorem | Update-only separation versus complete protocol transport. | Narrowed: complete transport preserves adaptive statistics conditionally. | The same functorial transport is the live hostile route here; it prevents an unconditional inequivalence claim. |
| Cycle 21 foundation site-net classification | Fixed named-site normalizer versus a law-selected or transported record category. | Narrowed to an explicit category fork. | The same category distinction applies to `W_I`; selected-`Z` cannot be silently treated as foundation-maximal. |
| Cycle 33 local-to-global glue | A local rule does not select its displayed zero/plus boundary. | Not retired for the involutive `CZ` architecture; a unique invariant-boundary theorem remains live. | That theorem could retire `W_B`; therefore boundary independence here is architecture-bounded. |
| Cycle 39 temporal protocol classification | Static inequivalence versus alternating temporal co-transport. | The unconditional physical distinction was retired and replaced by a law-relative fork. | Directly applies: it causes the N7 demotion while preserving the static two-representative census. |

The cross-cycle scan therefore finds an already successful narrowing mechanism:
complete object transport can retire an apparent representative-level wall.
That mechanism is applied here rather than dismissed.

## Reproduction

Run:

```bash
python3 scripts/cubic_cz_edge_rule_uniqueness_selection_cycle36_2026_07_14.py
```

The runner changes no files. It checks the `64/32/8/4/2` edge census, the two
global laws on degree-six cubic geometry, the static-equivalence obstruction,
the alternating-frame identity, the seven-record stabilizer separator, the
non-Clifford phase formulas and involution filter, the schedule witness, the
TOE residual ledger, and every N1–N8 section.

Expected result: `PASS=136`, `FAIL=0`.
