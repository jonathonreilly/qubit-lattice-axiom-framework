---
claim_id: gl_f_record_value_dictionary_commuting_lock_bounded_theorem_note_2026-09-01
claim_type: bounded_theorem
claim_scope: "For any family of bounded complex-valued measurable record-value functions in a pointwise function algebra on a probability space, every word-sandwiched cross-site anticommutator moment equals exactly twice the corresponding sandwiched product moment. Thus the declared all-word annihilation criterion A(W) holds iff those product moments vanish, and it forces F_x conj(F_y) = 0 almost everywhere pairwise; when there are at least two sites, F_x = f(v_x), and the measure is equivalent to a product probability measure, it forces f = 0 almost everywhere. Exact finite witnesses on the declared pair-weight class over (S^2)^Lambda give edge lam/18, distance-2 lam^2/54, square-diagonal lam^2/(lam^4+27), and sandwich value 1/18; an N=3 Jordan-Wigner comparator has zero cross-site anticommutators and static two-point 1/2. The derived boundary is only for the declared pointwise scalar-function dictionary and A(W); no physical-matter, propagator, dynamics, GL(F)-supplier, statistics-selection, or identification-clause conclusion is claimed."
upstream_dependencies: []
runner: scripts/gl_f_record_value_dictionary_commuting_lock_check_2026_09_01.py
negative_assertion_classes: [derived_no_go_boundary]
---

# The commuting lock: pointwise record-value dictionaries tie anticommutator moments to product moments

**Date:** 2026-09-01

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/gl_f_record_value_dictionary_commuting_lock_check_2026_09_01.py`](../scripts/gl_f_record_value_dictionary_commuting_lock_check_2026_09_01.py)

**Runner cache:**
[`logs/runner-cache/gl_f_record_value_dictionary_commuting_lock_check_2026_09_01.txt`](../logs/runner-cache/gl_f_record_value_dictionary_commuting_lock_check_2026_09_01.txt)
(`TOTAL: PASS=35 FAIL=0`)

**Parents:** none. Every premise used below is declared in this note.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact measure-theoretic identity (pointwise commutation of record-value functions) plus exact finite witness computations with rational/Gaussian-rational values; every object is declared inside the note."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Run independent audit on this self-contained measure/finite-algebra theorem."
conditional_surface_status: null
negative_assertion_classes: [derived_no_go_boundary]
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

Let `(Omega, mu)` be a probability space of record configurations and
`(F_x)_{x in Lambda}` a family of bounded complex-valued measurable functions
("record-value dictionary": each declared field symbol is a function of the record
configuration, with arbitrary — in particular possibly non-local — support).
Prove:

1. **(commuting lock)** for every pair `x != y` and all polynomial words
   `u, w` in the fields and their conjugates, the pointwise identity
   `u (F_x conj(F_y) + conj(F_y) F_x) w = 2 u F_x conj(F_y) w` holds, and the
   same with `conj(F_y)` replaced by `F_y`;
2. **(dichotomy)** consequently the induced moment functional
   `W(P) = Int P dmu` satisfies the cross-site sandwiched-anticommutator
   annihilation criterion `A(W)` iff every sandwiched cross-site product
   moment vanishes — in particular every cross-site two-point
   `W(F_x conj(F_y))` vanishes;
3. **(triviality under full `A(W)`)** full `A(W)` forces
   `F_x conj(F_y) = 0` `mu`-a.e. for each pair `x != y`; if moreover
   `Lambda` has at least two sites, the dictionary is per-site
   (`F_x(omega) = f(v_x)`), and `mu` is equivalent to a product probability
   measure `sigma^{Lambda}`, then `f = 0` `sigma`-a.e.;
4. **(nonvanishing witnesses)** on the declared nearest-neighbour pair-weight
   class over `(S^2)^Lambda` with dictionary `F(v) = (v^1 + i v^2)/2`, the
   exact values: edge two-point `lam/18`; distance-2 two-point `lam^2/54`;
   square-diagonal `lam^2/(lam^4 + 27)` (two paths add); sandwich
   witness `W(conj(F_0) F_1 {F_0, conj(F_1)}) = 1/18` for **every** `lam`,
   including the product point `lam = 0`;
5. **(graded coexistence)** the Jordan-Wigner family `c_x` on `(C^2)^{tensor N}`
   satisfies the annihilation criterion as **operator identities** (every
   cross-site anticommutator is the zero operator, hence every state
   annihilates every sandwiched insertion) while an explicit state carries
   cross-site two-point exactly `1/2`.

## Imports and authority

No measured value, fit, phenomenological selector, framework premise, or
ledger row enters the proof. The complete input/support inventory is:

| input or convention | review classification | role |
|---|---|---|
| pointwise multiplication of bounded scalar functions on a probability space | `zero-input structural` plus an explicit representation choice | load-bearing for Theorems 1 and 2; it is not supplied as a framework matter dictionary |
| normalized uniform measure on `S^2`, `F=(v^1+i v^2)/2`, `-1 <= lam <= 1`, and the finite graphs `P2`, `P3`, `C4` | `explicit normalization/boundary condition` | fixes the exact witness values only |
| nearest-neighbour pair weight and induced separable qubit state | `support-only` | declared finite fixtures, not forced forms of an admissibility rule, action, or dynamics |
| Pauli basis, tensor-factor order, vacuum convention, and Jordan-Wigner string | `standard/literature correction` | recomputed exactly; supplies a comparator, not a statistics selector |

Open, unimported bridges are the choice of framework record-to-field map, the
identification of physical word composition with pointwise function
multiplication, the physical matter state/action/dynamics, and any
reconstruction from a Euclidean or Grassmann functional. The theorem neither
assumes nor supplies those bridges.

Non-load-bearing context (plain-text pointers only; nothing below consumes
them): the operator-level predicate `GL(F)` and the conditional Grassmann/CAR
selection are in
`STAGGERED_DIRAC_SUBSTEP1_STATISTICS_GL_F_CONDITIONAL_DISCRIMINATOR_BOUNDED_THEOREM_NOTE_2026-06-10.md`;
the identification-clause decomposition whose residual matter-functional
clause this note leaves unchanged, and the functional-level annihilation
criterion it certifies, are in
`GL_F_IDENTIFICATION_BRIDGE_DECOMPOSITION_NARROW_THEOREM_NOTE_2026-06-11.md`.
This note re-declares everything it uses and does not cite their grades. In
particular, those context notes do not turn the algebraic diagnostic `A(W)`
defined here into operator-level `GL(F)`.

## Obligation graph

The proof is acyclic and closes through the following nodes.

1. `P0` (proved here): declare the record-configuration measure spaces and
   the exact uniform-`S^2` moment formula; declare the nonnegative pair-weight
   witness class and verify its normalization (`Z = 1` on trees; `Z(C4) =
   1 + lam^4/27 > 0`).
2. `P1` (proved here): declare the record-value dictionary, the induced
   moment functional `W`, and the annihilation criterion `A(W)`.
3. `P2` (proved here): the commuting lock (pointwise sandwich identity), at
   functional level and as a matrix identity for cross-site qubit ladders.
4. `P3` (proved here): the dichotomy and, under full `A(W)`, pairwise
   a.e. product-vanishing; per-site triviality under a product-equivalent
   measure on at least two sites.
5. `P4` (proved here): exact nonvanishing two-point and sandwich witnesses on
   the pair-weight class.
6. `P5` (proved here): cross-route consistency — the induced separable qubit
   state reproduces the classical two-point on the hard-core ladders.
7. `P6` (proved here): graded coexistence for the Jordan-Wigner comparator.
8. `P7` (proved here): the exact pointwise-dictionary boundary combining
   `P2`--`P6`.

The primary runner checks each computational node with exact arithmetic
(sympy rationals / Gaussian rationals / symbolic `lam`; no floats). The
strongest supported scope is precisely `P0`--`P7`.

## Definitions

**Record-configuration spaces and witness measures.** For a finite graph
`Lambda` with edge set `E`, take `Omega = (S^2)^Lambda` with the product
uniform measure, and the pair weights

```text
D_lam = prod_{(x,y) in E} (1 + lam * v_x . v_y),   -1 <= lam <= 1 .
```

Because each dot product lies in `[-1,1]`, every factor and hence `D_lam` is
nonnegative on the declared interval. The associated probability measure is
`D_lam d sigma^Lambda / Z`, where `Z = Int D_lam d sigma^Lambda > 0`; `D_lam`
itself need not be normalized on a graph with cycles.

Uniform-`S^2` monomial moments are exact:
`Int n1^a n2^b n3^c = (a-1)!!(b-1)!!(c-1)!!/(a+b+c+1)!!` for even exponents,
`0` otherwise (runner group A self-tests `1, 1/3, 1/5, 1/15`, odd `-> 0`).
Graphs used: the edge `P2`, the path `P3`, the square `C4`.

**Record-value dictionary and moment functional.** A dictionary assigns each
site a bounded complex measurable function `F_x` of the record configuration
(arbitrary support). Boundedness makes every finite polynomial word used below
integrable. The witness dictionary is the `sigma_+` Bloch
coordinate `F(v) = (v^1 + i v^2)/2 = tr(sigma_+ rho(v))` for
`rho(v) = (I + v.sigma)/2`. The general moment functional is
`W_mu(P) = Int P dmu`; on the witness measures this specializes to
`W(P) = Int P D_lam d sigma^Lambda / Int D_lam d sigma^Lambda` for
polynomials `P` in the fields and their conjugates.

**Algebraic annihilation criterion `A(W)`.** `W` satisfies `A(W)` iff
`W(u {psi_x, psi_y} w) = 0` and `W(u {psi_x, conj(psi_y)} w) = 0` for all
`x != y` and all polynomial words `u, w`. This is a declared moment
diagnostic patterned on cross-site anticommutator relations. Without a
reconstruction and field-identification theorem it is not operator-level
`GL(F)` or a physical locality statement.

**Graded comparator.** `c_x = (prod_{y<x} sigma_3^(y)) sigma_+^(x)` on
`(C^2)^{tensor N}`, exact integer matrices, `N = 3`.

## Theorem 1 — the commuting lock

**Conclusion.** For any record-value dictionary and any pair `x != y`:
pointwise on `Omega`,

```text
u {F_x, F_y^#} w = 2 u F_x F_y^# w        (F^# = F or conj(F)),
```

hence `W(u {F_x, F_y^#} w) = 2 W(u F_x F_y^# w)` for every declared
probability measure and every finite polynomial sandwich. The same holds at
operator level for the cross-site qubit ladders:
`{sigma_+^(x), sigma_-^(y)} = 2 sigma_+^(x) sigma_-^(y)` as a matrix
identity, and this operator is nonzero.

**Proof.** Values of functions multiply pointwise in the commutative algebra
of measurable functions, so `F_x F_y^# = F_y^# F_x` pointwise and the
anticommutator is twice the product; multiply by `u, w` and integrate.
Cross-site qubit ladders act on distinct tensor factors, so they commute as
matrices; the runner verifies the `4 x 4` identity and its nonvanishing
exactly, and verifies the functional identity on `P3` for four sandwiches
(`u = w = 1`; an `F`-even occupation sandwich `u = (1 + v_2^3)/2`; an
`F`-even bilinear sandwich `u = conj(F_0) F_1`; the occupation sandwich on
the right).

## Theorem 2 — dichotomy and triviality under the full criterion

**Conclusion.** `A(W)` holds iff every sandwiched cross-site product moment
`W(u F_x F_y^# w)` vanishes (`x != y`); in particular every cross-site
two-point vanishes. Full `A(W)` forces `F_x conj(F_y) = 0` `mu`-a.e. for
each `x != y`; if `Lambda` has at least two sites, then for a per-site
dictionary `F_x = f(v_x)` under `mu` equivalent to the product probability
measure `sigma^{Lambda}`, `f = 0` `sigma`-a.e.

**Proof.** The equivalence is Theorem 1 divided by `2`. For the a.e.
statement take the bounded sandwich `u = conj(F_x) F_y`, `w = 1`, insertion
`{F_x, conj(F_y)}`: the annihilated moment is
`2 Int |F_x|^2 |F_y|^2 dmu = 2 Int |F_x conj(F_y)|^2 dmu`, so
`F_x conj(F_y) = 0` `mu`-a.e. For the per-site case, equivalence of measures
preserves null sets, so `f(v_x) conj(f(v_y)) = 0` for
`sigma tensor sigma`-a.e. `(v_x, v_y)` for any distinct pair, which exists by
the two-site hypothesis; by Tonelli
`(Int |f|^2 dsigma)^2 = 0`, hence `f = 0` `sigma`-a.e.

## Theorem 3 — nonvanishing witnesses on the pair-weight class

**Conclusion.** With the `sigma_+` Bloch dictionary: edge two-point
`W(F_0 conj(F_1)) = lam/18` on `P2`; mixed edge anticommutator `lam/9`
(value `1/18` at `lam = 1/2`); same-type anticommutator `W({psi_0, psi_1}) =
0` by the `U(1)` symmetry of the base measure (so the **mixed**
anticommutator is the failing witness); distance-2 two-point `lam^2/54` on
`P3`; square-diagonal two-point `lam^2/(lam^4 + 27)` on `C4` with
`lam^2`-coefficient exactly `1/27` (the two length-2 paths add); at
`lam = 0` every cross-site two-point vanishes yet the sandwich witness
`W(conj(F_0) F_1 {F_0, conj(F_1)}) = 2 Int |F_0|^2 |F_1|^2 = 1/18` for
**every** `lam` — so even the product measure fails full `A(W)` unless the
dictionary is a.e. trivial, exactly as Theorem 2 requires.

**Proof.** Exact monomial integration against the expanded pair-weight
density (runner group C; all values are the displayed rationals in `lam`).
Independent cross-route (runner group D): the induced separable qubit state
`R = Int (tensor_x rho(v_x)) D_lam / Z` has exact unit trace and satisfies
`tr(R sigma_+^(0) sigma_-^(n-1)) = W(F_0 conj(F_{n-1}))` on `P2` and `P3`.

## Theorem 4 — graded coexistence

**Conclusion.** The Jordan-Wigner family satisfies exact CAR
(`{c_x, c_y} = 0`, `{c_x, c_y^dag} = delta_xy I`): every cross-site
anticommutator is the **zero operator**, so every state annihilates every
sandwiched insertion — the annihilation criterion holds identically — while
the state `chi = (c_0^dag + c_1^dag)|0>` carries
`<c_0^dag c_1> = 1/2 != 0`.

**Proof.** Exact integer matrix computation at `N = 3` (runner group E): all
`2N^2` anticommutator identities, vacuum annihilation, the two-point value
`1/2`, and the vanishing of the anticommutator insertion in the same state.

## Corollary — exact boundary of the pointwise dictionary

Within the representation defined here, `A(W)` is equivalent to vanishing of
all sandwiched cross-site product moments. Therefore no functional in this
specific pointwise scalar-function class can satisfy `A(W)` while retaining a
nonzero such moment. Under the additional same-function, product-equivalence,
and at-least-two-site hypotheses, full `A(W)` makes that per-site dictionary
zero almost everywhere. The finite pair-weight fixtures exhibit nonzero
moments and a nonzero sandwich; they establish examples, not genericity.

The Jordan-Wigner computation is an explicit noncommutative comparator in
which cross-site anticommutators vanish and a static two-point expectation is
nonzero. It shows that the scalar pointwise-multiplication premise is
load-bearing; it does not select Jordan-Wigner, CAR, or any statistics class.
Nothing here identifies a static two-point moment with a propagator, supplies
dynamics, maps framework matter words to pointwise products, or treats a
Grassmann/Berezin or reconstructed operator functional as a commuting scalar
dictionary. Consequently the existing matter-functional identification
clause remains open and unchanged.

## No-Go Discipline Gate

The only negative assertion class is `derived_no_go_boundary`: inside the
declared pointwise scalar-function representation, `A(W)` and a nonzero
sandwiched cross-site product moment cannot coexist. This is not a claim that
all matter representations, functional reconstructions, or statistics routes
have been excluded.

### N1 — alternative-route enumeration

| normalized attack route | execution marker | result at the scoped boundary | current-cycle evidence |
|---|---|---|---|
| allow each scalar field to depend nonlocally on the entire record configuration | `ATTEMPTED` | Theorem 1 is pointwise and support-blind, so arbitrary shared/nonlocal dependence does not alter scalar commutativity. | Theorem 1 and runner group B |
| replace the finite witness law by an arbitrary correlated or singular probability measure | `ATTEMPTED` | boundedness keeps the words integrable and the pointwise identity survives integration; no density or product structure is used for the basic boundary. | Theorem 1's pre-integration identity |
| arrange cancellation of every unsandwiched two-point moment | `ATTEMPTED` | the exact `lam=0` fixture realizes this cancellation, but the allowed sandwich `u=conj(F_x)F_y` exposes the nonnegative product norm and fails full `A(W)`. | Theorem 2 and runner C8--C11 |
| use zero divisors or disjoint supports so different fields are nonzero but every cross-site product vanishes | `ATTEMPTED` | this is a genuine survivor and fixes the scope: the general theorem concludes pairwise product-zero, not individual field triviality; individual triviality is stated only for one shared per-site function under product-equivalence on at least two sites. | Theorem 2's pairwise-product conclusion and the N2 countermodel |
| replace pointwise scalar multiplication by a noncommutative or graded operator carrier | `ATTEMPTED` | the exact Jordan-Wigner comparator evades the commutative premise; it defeats any physical or all-representation extrapolation, which this note expressly does not make. | Theorem 4 and runner group E |

These are distinct support, measure, observable-cancellation, zero-divisor,
and carrier-algebra mechanisms. The first three fail to falsify the scoped
identity, the fourth fixes its narrowest consequence, and the fifth is an
open outside-class construction rather than a route claimed closed.

### N2 — condition-independence audit

Let `C1` be pointwise scalar commutativity, `C2` the all-word criterion
`A(W)`, and `C3` the extra package used only for individual per-site
triviality (one common `f`, product-equivalent measure, and at least two
sites).

| pair | does the first imply/close the second? | does the second imply/close the first? | independent? |
|---|---|---|---|
| `C1`, `C2` | no; the pair-weight sandwiches violate `C2` inside `C1` | no; Jordan-Wigner satisfies the anticommutator condition outside `C1` | yes |
| `C1`, `C3` | no; an arbitrary pointwise dictionary need not be per-site or product-equivalent | no; the extra measure/dictionary form does not by itself impose the annihilation criterion | yes |
| `C2`, `C3` | no; disjoint-support scalar fields can satisfy `C2` without `C3` | no; the declared `lam=0` per-site product fixture has `C3` form but fails `C2` | yes |

Inside `C3`, the common-function, product-equivalence, and two-site
conditions are separately load-bearing: dropping the common function admits
nontrivial disjoint-support fields; dropping product-equivalence permits a
measure concentrated where the pairwise product vanishes; dropping the
two-site condition makes `A(W)` vacuous. No independent-wall count is claimed.

### N3 — hidden-condition scan

All load-bearing conditions are explicit: a probability space, bounded
complex scalar functions, pointwise multiplication and conjugation, finite
polynomial words, and the all-word quantifier in `A(W)`. The stronger
individual-triviality statement additionally declares a common per-site
function, product-measure equivalence, and at least two sites. Uniform `S^2`,
the Bloch normalization, `-1 <= lam <= 1`, finite graphs, Pauli conventions,
and site order belong only to the fixtures. “Standard” applies only to the
recomputed Jordan-Wigner methodology; “context” files are non-load-bearing;
“canonical cache” and `PASS` are integrity evidence, not scientific authority.

### N4 — residual matching

No prior no-go or retained wall is used as evidence for this theorem. The two
named files are plain-text context rather than support citations:

| context locator | residual it records | residual claimed closed here | match/disposition |
|---|---|---|---|
| `docs/STAGGERED_DIRAC_SUBSTEP1_STATISTICS_GL_F_CONDITIONAL_DISCRIMINATOR_BOUNDED_THEOREM_NOTE_2026-06-10.md:72` | operator-level `GL(F)` is an explicit conditional predicate | none | not a witness; context only |
| `docs/GL_F_IDENTIFICATION_BRIDGE_DECOMPOSITION_NARROW_THEOREM_NOTE_2026-06-11.md:345` | the matter-functional clause remains undischarged by that construction | none | not a witness; explicitly left unchanged |

The residual-support witness count is therefore zero; no mismatched citation
is being used to authorize the derived boundary.

### N5 — rhetoric and resolution certificate

The primary runner and its pinned cache emit one substantive line for each
required resolution. At `per_element` it checks pointwise scalar algebra; at
`per_site` it checks declared cross-site pairs and the three-site CAR
comparator; at `per_block` it checks `P2`, `P3`, `C4`, and the finite tensor
carrier. `per_mode` and physical `lattice_wide` claims are explicitly not
executed and not made. “Cannot coexist” refers only to `A(W)` plus a nonzero
sandwiched product moment in the declared scalar pointwise algebra.

### N6 — partial-closure path scan

Changing the word representation from pointwise scalar products to a
noncommutative, graded, Grassmann, time-ordered, or reconstructed operator
product is a legitimate construction path, not a new axiom and not excluded.
Likewise, supplying a framework record-to-field dictionary and a physical
matter state/action would be a separate bridge. This theorem does not relabel
either task as solved, required-by-axiom, or impossible.

### N7 — steelman

The strongest objection to a physical reading is decisive: physical matter
correlations may be represented by Grassmann variables, time ordering, an OS
reconstruction, or another dictionary whose word product is not pointwise
multiplication of complex record values. Such a representation can satisfy
operator anticommutation and retain nonzero two-point expectations, as the
finite Jordan-Wigner comparator already demonstrates. The objection defeats
the original physical/propagator extrapolation, so that extrapolation has been
removed; it does not falsify the remaining conditional function-algebra
identity because it changes its load-bearing representation premise.

### N8 — cross-cycle echo

Repository GL(F) work already separates these layers:

| prior surface | later disposition of the similar wall | applicability here |
|---|---|---|
| `STAGGERED_DIRAC_SUBSTEP1_STATISTICS_GL_F_CONDITIONAL_DISCRIMINATOR_BOUNDED_THEOREM_NOTE_2026-06-10.md` | operator `GL(F)` remains a conditional discriminator, not an unconditional supplier | its hard-core/Jordan-Wigner split is the same outside-class escape tested here |
| `GL_F_FROM_BEREZIN_RP_RECONSTRUCTION_NARROW_THEOREM_NOTE_2026-06-10.md` | CAR is reconstructed only after a Grassmann/Berezin action surface is supplied | that reconstruction mechanism remains open and is not a scalar-function counterexample |
| `GL_F_IDENTIFICATION_BRIDGE_DECOMPOSITION_NARROW_THEOREM_NOTE_2026-06-11.md` | the matter-functional clause is explicitly not retired | this note cannot retire it without the missing physical dictionary/product bridge |
| `GL_F_MULTILOOP_GRADED_NET_COCYCLE_NARROW_NO_GO_NOTE_2026-06-10.md` | the static multi-loop selection route closes narrowly, while carrier selection remains open | it reinforces that the present static comparator supplies no statistics selector |

The applicable mechanisms—changing carrier algebra and supplying a
reconstruction/identification—are already admitted in N1, N6, and N7. This
note records one exact scalar-algebra boundary and one comparator while leaving
carrier choice, reconstruction, identification, and dynamics open.

**No-Go Discipline result:** `PASS` for the scoped
`derived_no_go_boundary`; broader physical and all-representation negatives
are withdrawn.

## Executable claim block

The following block is the canonical machine-bound restatement of the
theorem conclusions.

```text
commuting_lock: W(u {psi_x, psi_y^#} w) = 2 W(u psi_x psi_y^# w)  (bounded scalar pointwise dictionaries on probability spaces)
dichotomy: A(W) <=> every sandwiched cross-site product moment vanishes
full_criterion_consequence: F_x conj(F_y) = 0 a.e. pairwise; shared per-site f is a.e. zero (product-equivalent measure, at least two sites)
edge_two_point: lam/18
edge_mixed_anticommutator: lam/9
same_type_anticommutator: 0
distance2_two_point: lam^2/54
square_diagonal_two_point: lam^2/(lam^4 + 27)   (lam^2-coefficient 1/27)
sandwich_witness_value: 1/18  (independent of lam, nonzero at lam = 0)
graded_comparator: cross-site anticommutators = 0 as operators; two-point 1/2 in an explicit state
runner_total: PASS=35 FAIL=0
```

## Proof boundary

Theorems 1 and 2 hold for probability spaces and bounded, arbitrary-support,
pointwise scalar-function dictionaries exactly as stated; the individual
a.e.-triviality leg is scoped to its stated hypotheses (one shared per-site
function, measure equivalent to a product probability measure, and at least
two sites), and no broader dictionary survey is claimed.
The witness computations are scoped to the declared value space `S^2`, the
declared nearest-neighbour pair-weight measure class on `P2`/`P3`/`C4`, and
the declared `sigma_+` Bloch dictionary. This note supplies no `GL(F)`
predicate at operator level, selects no statistics class, discharges no
identification clause, registers no admission, and derives no measure,
propagator, action, or dynamics: the pair-weight class is a witness class, not
a forced form. The graded comparator shows algebraic coexistence only; no
uniqueness, physical-carrier, infinite-volume, or continuum claim is made.
Sets, promotes, or changes no row's effective status.

## Review record

Self-contained landing: zero upstream dependencies; every premise is
declared in this note and every computational node is certified by the
primary runner with exact arithmetic (`PASS=35 FAIL=0`). The corollary is a
scoped `derived_no_go_boundary` for one representation class, accompanied by
the landed N1-N8 packet; outside-class construction paths remain open. Hard
landing conditions are a fresh exact-boundary runner/cache
pair, a current zero-dependency citation-manifest entry, and passing
repository pipeline, strict-lint, and changed-evidence gates; independent
audit remains a separate lane.
