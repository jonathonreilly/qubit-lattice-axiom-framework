---
claim_id: gl_f_record_value_dictionary_commuting_lock_bounded_theorem_note_2026-09-01
claim_type: bounded_theorem
claim_scope: "For any family of complex-valued record-value functions on a measured record-configuration space (arbitrary supports), pointwise multiplication commutes, so every word-sandwiched cross-site anticommutator insertion equals exactly twice the corresponding sandwiched product insertion; hence the cross-site sandwiched-anticommutator annihilation criterion A(W) on the induced moment functional holds iff every sandwiched cross-site product moment vanishes, and full A(W) forces F_x conj(F_y) = 0 almost everywhere pairwise — for a per-site dictionary under a measure equivalent to a full-support product measure the fields vanish almost everywhere. On the declared nearest-neighbour pair-weight witness class over (S^2)^Lambda the runner certifies exact nonvanishing two-points (edge lam/18, distance-2 lam^2/54, square-diagonal lam^2-coefficient 1/27) and sandwich witness value 1/18 at every lam including lam = 0; the graded Jordan-Wigner comparator satisfies the annihilation criterion as operator identities while carrying cross-site two-point 1/2 in an explicit state. No GL(F) supplier, no statistics selection, and no identification-clause discharge is claimed."
upstream_dependencies: []
runner: scripts/gl_f_record_value_dictionary_commuting_lock_check_2026_09_01.py
---

# The commuting lock: record-value matter dictionaries tie exchange to propagation

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
(`TOTAL: PASS=32 FAIL=0`)

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
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

Let `(Omega, mu)` be a probability space of record configurations and
`(F_x)_{x in Lambda}` a family of complex-valued measurable functions
("record-value dictionary": each matter field is a function of the record
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
   `F_x conj(F_y) = 0` `mu`-a.e. for each pair `x != y`; if moreover the
   dictionary is per-site (`F_x(omega) = f(v_x)`) and `mu` is equivalent to a
   product measure `sigma^{Lambda}` with `sigma` of full support, then
   `f = 0` `sigma`-a.e.;
4. **(nonvanishing witnesses)** on the declared nearest-neighbour pair-weight
   class over `(S^2)^Lambda` with dictionary `F(v) = (v^1 + i v^2)/2`, the
   exact values: edge two-point `lam/18`; distance-2 two-point `lam^2/54`;
   square-diagonal `lam^2`-coefficient `1/27` (two paths add); sandwich
   witness `W(conj(F_0) F_1 {F_0, conj(F_1)}) = 1/18` for **every** `lam`,
   including the product point `lam = 0`;
5. **(graded coexistence)** the Jordan-Wigner family `c_x` on `(C^2)^{tensor N}`
   satisfies the annihilation criterion as **operator identities** (every
   cross-site anticommutator is the zero operator, hence every state
   annihilates every sandwiched insertion) while an explicit state carries
   cross-site two-point exactly `1/2`.

## Imports and authority

Imported scientific authority: none. The measure spaces, the pair-weight
witness class, the dictionary, the annihilation criterion, and the
Jordan-Wigner comparator are definitions internal to this theorem; the
Jordan-Wigner construction is standard methodology recomputed in full by the
runner. No observational value, no framework premise, and no ledger row
enters the proof. The nearest-neighbour pair-weight family is a **declared
witness class**, not a consumed "forced form" of any admissibility rule.

Non-load-bearing context (plain-text pointers only; nothing below consumes
them): the operator-level predicate `GL(F)` and the conditional Grassmann/CAR
selection are in
`STAGGERED_DIRAC_SUBSTEP1_STATISTICS_GL_F_CONDITIONAL_DISCRIMINATOR_BOUNDED_THEOREM_NOTE_2026-06-10.md`;
the identification-clause decomposition whose residual matter-functional
clause this note's corollary narrows, and the functional-level annihilation
criterion it certifies, are in
`GL_F_IDENTIFICATION_BRIDGE_DECOMPOSITION_NARROW_THEOREM_NOTE_2026-06-11.md`.
This note re-declares everything it uses and does not cite their grades.

## Obligation graph

The proof is acyclic and closes through the following nodes.

1. `P0` (proved here): declare the record-configuration measure spaces and
   the exact uniform-`S^2` moment formula; declare the pair-weight witness
   class and verify it is a probability class (`Z = 1` on trees; `Z(C4) =
   1 + lam^4/27`).
2. `P1` (proved here): declare the record-value dictionary, the induced
   moment functional `W`, and the annihilation criterion `A(W)`.
3. `P2` (proved here): the commuting lock (pointwise sandwich identity), at
   functional level and as a matrix identity for cross-site qubit ladders.
4. `P3` (proved here): the dichotomy and, under full `A(W)`, pairwise
   a.e. product-vanishing; per-site triviality under a product-equivalent
   full-support measure.
5. `P4` (proved here): exact nonvanishing two-point and sandwich witnesses on
   the pair-weight class.
6. `P5` (proved here): cross-route consistency — the induced separable qubit
   state reproduces the classical two-point on the hard-core ladders.
7. `P6` (proved here): graded coexistence for the Jordan-Wigner comparator.
8. `P7` (proved here): the interface corollary combining `P2`--`P6`.

The primary runner checks each computational node with exact arithmetic
(sympy rationals / Gaussian rationals / symbolic `lam`; no floats). The
strongest supported scope is precisely `P0`--`P7`.

## Definitions

**Record-configuration spaces and witness measures.** For a finite graph
`Lambda` with edge set `E`, take `Omega = (S^2)^Lambda` with the product
uniform measure, and the pair-weight probability densities

```text
D_lam = prod_{(x,y) in E} (1 + lam * v_x . v_y),   -1 <= lam <= 1 .
```

Uniform-`S^2` monomial moments are exact:
`Int n1^a n2^b n3^c = (a-1)!!(b-1)!!(c-1)!!/(a+b+c+1)!!` for even exponents,
`0` otherwise (runner group A self-tests `1, 1/3, 1/5, 1/15`, odd `-> 0`).
Graphs used: the edge `P2`, the path `P3`, the square `C4`.

**Record-value dictionary and moment functional.** A dictionary assigns each
site a complex measurable function `F_x` of the record configuration
(arbitrary support). The witness dictionary is the `sigma_+` Bloch
coordinate `F(v) = (v^1 + i v^2)/2 = tr(sigma_+ rho(v))` for
`rho(v) = (I + v.sigma)/2`. The moment functional is
`W(P) = Int P D_lam / Int D_lam` on polynomials `P` in the fields and their
conjugates.

**Annihilation criterion `A(W)`.** `W` satisfies `A(W)` iff
`W(u {psi_x, psi_y} w) = 0` and `W(u {psi_x, conj(psi_y)} w) = 0` for all
`x != y` and all polynomial words `u, w` — the functional-level form of
cross-site graded locality: every word-sandwiched cross-site anticommutator
insertion is annihilated.

**Graded comparator.** `c_x = (prod_{y<x} sigma_3^(y)) sigma_+^(x)` on
`(C^2)^{tensor N}`, exact integer matrices, `N = 3`.

## Theorem 1 — the commuting lock

**Conclusion.** For any record-value dictionary and any pair `x != y`:
pointwise on `Omega`,

```text
u {F_x, F_y^#} w = 2 u F_x F_y^# w        (F^# = F or conj(F)),
```

hence `W(u {F_x, F_y^#} w) = 2 W(u F_x F_y^# w)` for every measure and every
sandwich. The same holds at operator level for the cross-site qubit ladders:
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
each `x != y`; for a per-site dictionary `F_x = f(v_x)` under `mu`
equivalent to `sigma^{Lambda}` with `sigma` of full support, `f = 0`
`sigma`-a.e.

**Proof.** The equivalence is Theorem 1 divided by `2`. For the a.e.
statement take the sandwich `u = conj(F_x) F_y`, `w = 1`, insertion
`{F_x, conj(F_y)}`: the annihilated moment is
`2 Int |F_x|^2 |F_y|^2 dmu = 2 Int |F_x conj(F_y)|^2 dmu`, so
`F_x conj(F_y) = 0` `mu`-a.e. For the per-site case, equivalence of measures
preserves null sets, so `f(v_x) conj(f(v_y)) = 0` for
`sigma tensor sigma`-a.e. `(v_x, v_y)`; by Tonelli
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

## Corollary — the matter-functional interface is narrowed

Within this note's definitions: a moment functional of commuting
record-value fields satisfies the cross-site graded-locality annihilation
criterion **only at the price of its own matter content** — the criterion is
equivalent to the vanishing of all sandwiched cross-site products (Theorem
1/2), full annihilation trivializes a per-site dictionary a.e. under a
product-equivalent full-support measure (Theorem 2), and the declared
witness class shows nonvanishing cross-site correlation is generic (Theorem
3). In the commuting frame the exchange functional and the propagator are
the **same object** (exact ratio `2`); grading is precisely what makes them
independent — the graded comparator has exchange functional identically `0`
with propagator `1/2` (Theorem 4). Consequently, any identification of the
physical matter correlation functional with a law-level moment functional of
commuting record-value fields carrying nonvanishing cross-site correlation
fails the annihilation criterion, and one meeting the criterion carries a.e.
trivial fields under the stated hypotheses; a matter functional with both
the criterion and nonvanishing propagation therefore lives in the
graded/operator-level construction class, which Theorem 4 exhibits as
nonempty on the qubit carrier. This narrows where a matter-functional
identification can succeed and opens the graded-construction path; it
discharges nothing and supplies no selector.

## Executable claim block

The following block is the canonical machine-bound restatement of the
theorem conclusions.

```text
commuting_lock: W(u {psi_x, psi_y^#} w) = 2 W(u psi_x psi_y^# w)  (all record-value dictionaries, all measures)
dichotomy: A(W) <=> every sandwiched cross-site product moment vanishes
full_criterion_consequence: F_x conj(F_y) = 0 a.e. pairwise; per-site dictionary a.e. trivial (product-equivalent full-support measure)
edge_two_point: lam/18
edge_mixed_anticommutator: lam/9
same_type_anticommutator: 0
distance2_two_point: lam^2/54
square_diagonal_two_point: lam^2/(lam^4 + 27)   (lam^2-coefficient 1/27)
sandwich_witness_value: 1/18  (independent of lam, nonzero at lam = 0)
graded_comparator: cross-site anticommutators = 0 as operators; two-point 1/2 in an explicit state
runner_total: PASS=32 FAIL=0
```

## Proof boundary

Theorems 1 and 2 hold for arbitrary measured record-configuration spaces and
arbitrary-support dictionaries exactly as stated; the a.e.-triviality leg is
scoped to its stated hypotheses (per-site dictionary, measure equivalent to
a full-support product measure) and no broader dictionary survey is claimed.
The witness computations are scoped to the declared value space `S^2`, the
declared nearest-neighbour pair-weight density class on `P2`/`P3`/`C4`, and
the declared `sigma_+` Bloch dictionary. This note supplies no `GL(F)`
predicate at operator level, selects no statistics class, discharges no
identification clause, registers no admission, and derives no measure or
dynamics: the pair-weight class is a witness class, not a forced form. The
graded comparator shows coexistence only; no uniqueness or physical-carrier
claim is made. Sets, promotes, or changes no row's effective status.

## Review record

Self-contained landing: zero upstream dependencies; every premise is
declared in this note and every computational node is certified by the
primary runner with exact arithmetic (`PASS=32 FAIL=0`). The corollary is
stated as an interface narrowing, not a route closure: the
graded/operator-level construction class is exhibited nonempty and is the
opened path. Hard landing conditions are a fresh exact-boundary runner/cache
pair, a current zero-dependency citation-manifest entry, and passing
repository pipeline, strict-lint, and changed-evidence gates; independent
audit remains a separate lane.
