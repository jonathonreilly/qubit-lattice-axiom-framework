---
claim_id: admissibility_readability_continuum_alphabet_fisher_rank_and_formation_order_second_order_bounded_theorem_note_2026-09-13
claim_type: bounded_theorem
claim_scope: "On the 2x3 and 2x2x2 windows of Z^3 with the continuum unit-Bloch-vector alphabet, for the order-blind product family W_theta = prod_edges (1 + sum_a theta_a f_a) over the six covariant invariants P_1..P_4(v_x.v_y), S_1 = v_{x,d} v_{y,d} and H = sum_i v_i^4 - 3/5: the Fisher matrix at theta = 0 is exactly diag(|E|/3, |E|/5, |E|/7, |E|/9) on the Legendre block, I_{S1 S1} = I_{P1 S1} = |E|/9, I_{HH} = 16n/525, rank 6 on both windows; on the binary and six-axis alphabets the rank is 1 or 2 and 3 with the null directions named; the formation order is absent from the first-order tangent for every total order (720 on 2x3, 40320 on 2x2x2); at second order in the degree-one kernel the product conditional class separates order classes by at least 1/27 in squared L^2 distance but leaves the monotone-box and reversed orders equal on both windows, while the additive conditional class separates them by 8/27 and 8/9. Nothing is asserted beyond these windows, this family, this order in theta, or the declared alphabets and conditional classes."
upstream_dependencies:
  - minimal_axioms
  - realized_state_primitive
  - the_superlattice_role_pattern_is_a_next_nearest_neighbour_support_rule_over_roles_and_roles_are_not_record_values_bounded_theorem_note_2026-09-04
  - a_readable_matter_law_exists_on_the_5x5x5_window_the_designed_laws_record_table_completed_by_a_covariant_parity_rule_has_every_menu_nonempty_is_read_from_partial_blocks_and_keeps_the_fermion_bounded_note_2026-09-04
runner: scripts/admissibility_readability_continuum_alphabet_fisher_rank_2026_09_13.py
---

# In the continuum Bloch alphabet the six-parameter covariant rule family is fully readable from finished-window records, the finite alphabets are not, and the formation order enters the record law first at second order in the rule strength

**Date:** 2026-09-13
**Type:** bounded_theorem
**Status:** proposed_retained
**Audit:** unset; the independent audit lane owns any verdict.
**Runner:** [`scripts/admissibility_readability_continuum_alphabet_fisher_rank_2026_09_13.py`](../scripts/admissibility_readability_continuum_alphabet_fisher_rank_2026_09_13.py)
**Cache:** [`logs/runner-cache/admissibility_readability_continuum_alphabet_fisher_rank_2026_09_13.txt`](../logs/runner-cache/admissibility_readability_continuum_alphabet_fisher_rank_2026_09_13.txt)
**Runner total:** `TOTAL: PASS=63 FAIL=0` (about 8 s, exact rationals throughout).

## Result up front

This is the readability block of the derivation campaign
(`docs/TOE_DERIVATION_CAMPAIGN_AXIOM_SUFFICIENCY_BY_UNDERDETERMINATION_WITNESSES_NOTE_2026-09-13.md`,
PR #8093). The question is whether the framework's law is in principle an
observable of its own records when the letters are the unit Bloch vectors the
Qubit axiom supplies, rather than the binary letters on which the earlier
readability results were computed.

- **Readable (Theorem 1).** For order-blind product rules in the six covariant
  invariants, the Fisher matrix of the finished-window law at the uniform point
  is `diag(|E|/3, |E|/5, |E|/7, |E|/9)` on the four Legendre directions, with
  `I_{S1 S1} = I_{P1 S1} = |E|/9` for the soldered direction and
  `I_{HH} = 16n/525` for the cubic site anisotropy; rank 6 on `2x3` (`|E| = 7`,
  `n = 6`) and on `2x2x2` (`|E| = 12`, `n = 8`). Every direction of the rule is
  readable from records alone. The closed form is proved for any finite window.
- **Not readable on finite alphabets (Theorem 2).** On the binary `z` alphabet
  the same six-parameter family has Fisher rank 1 (`2x3`) and 2 (`2x2x2`); on
  the six-axis alphabet rank 3 on both windows. The null directions are named:
  `P_2`, `P_4`, `H`, `P_1 - P_3`, and on `2x3` also `S_1` (binary);
  `H`, `P_1 - P_3`, `P_4 - (5/12) P_2` (six-axis). This is the exact continuum
  counterpart of the binary no-go: the unreadable directions are those whose
  invariants become constant, or coincide, on the finite letter set.
- **The formation order is not in the first-order tangent (Theorem 3).** For
  every total formation order (720 on `2x3`, 40320 on `2x2x2`) and every
  normalised conditional class, the finished-window law is
  `1 + theta T_1 + O(theta^2)` with one and the same `T_1 = sum_edges g_e`.
  Order-mixture directions are null directions of the Fisher matrix at the
  uniform point: the order is unreadable at leading order in the rule strength.
- **The order enters at second order, and the two admissible conditional
  classes disagree about how (Theorems 4 and 5).** In the degree-one kernel
  the second-order coefficient is `c_sigma = A - (1/3) sum_w iota_sigma(w) v_q.v_q'`
  for the product conditional class (apex-less, as Lemma L of the
  formation-order census requires) and `c_sigma = A - sum_w iota_sigma(w) (v_x.v_q)(v_x.v_q')`
  for the additive class (apex-resolved), where `iota_sigma(w) = 1` when both
  arms of the wedge `w = (x; q, q')` are recorded before its apex. Squared
  `L^2` separations between order classes are at least `1/27` (product) and
  `1/9` (additive). For a two-order mixture the leading Fisher information for
  the mixing weight is `theta^4` times this distance.
- **A blind spot of the product class (Theorem 6).** The monotone-box and
  reversed orders have equal wedge-pair vectors on both windows, so the product
  class does not separate them at second order (distance `0`), although their
  recorded-set multisets `K` differ on the cube (the formation-order census,
  PR #8102, separates them at the `K` level). The additive class separates them
  at second order by `8/27` and `8/9`. The class hierarchy is
  pair-vector (26 / 448) <= `K` (28 / 542) <= apex-vector (36 / 710) on
  `2x3` / `2x2x2`; the middle numbers reproduce the census of PR #8102.

Recorded decision points (findings, not gates): (i) the Qubit alphabet must be
the continuum one for the law to be readable; a finite letter set leaves named
rule directions unobservable; (ii) whether the conditional at a formation step
composes its recorded neighbours as a product or as a sum is not fixed by the
Admissibility sentence and is visible in the records at second order.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the Record axiom makes only records readable; whether the rule that produced them is recoverable from finished-window statistics, and whether the formation order leaves any trace in them, is not stated by the axioms"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "carry the Fisher computation to degree-two kernels and to the 3x3x3 window; test whether the K-level separation of monotone-box and reversed orders appears at third order in the product class; feed the product-versus-additive composition finding to the composition and law selection block"
conditional_surface_status: "if a clause fixed the composition rule of a formation step (product or additive), the second-order record law below is the exact readable trace of the formation order in that reading"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "every statement is an exact finite computation in rational arithmetic on declared windows, alphabets, rule families and formation orders, or an algebraic identity proved for a general finite window and checked on both windows"
```

## Premises and declared objects

**Axiom text used (quoted from `docs/MINIMAL_AXIOMS_2026-06-29.md` on
`origin/main`).** Lattice: sites `Z^3`, nearest-neighbour adjacency, standard
translations and proper cubic rotations. Qubit: the one-site algebra is
`M_2(C)`; the pure local possibilities are the unit Bloch vectors
`v in S^2`, on which the proper rotations act by `SO(3)`. Admissibility: "one
fixed nearest-neighbor admissibility rule, covariant under lattice translations
and proper cubic rotations. For each site, the probability distribution over
the possibilities is determined by, and varies with, the nearest-neighbor
conditions." Record: records form, only records are readable, records are
permanent. Formation order is not a record and is not readable. The realized
state primitive supplies the pick; the law supplies the odds.

**Declared alphabets.** `continuum`: `v` uniform on `S^2` at the base point,
with the exact moments `E[x^a y^b z^c] = (a-1)!! (b-1)!! (c-1)!! / (a+b+c+1)!!`
for even exponents and `0` otherwise. `binary_z`: `v in {+e_z, -e_z}` with equal
weights. `six_axis`: `v in {+-e_1, +-e_2, +-e_3}` with equal weights, so
`E[v_i^2] = 1/3` and all odd or mixed moments vanish.

**Declared windows.** `2x3` (`n = 6`, `|E| = 7`, 10 wedges, 6 arm pairs) and
`2x2x2` (`n = 8`, `|E| = 12`, 24 wedges, 12 arm pairs). A wedge `w = (x; q, q')`
is a site `x` with two distinct neighbours `q, q'` inside the window; an arm
pair is the unordered pair `{q, q'}`.

**Declared covariant invariants.** Edge invariants `P_k(v_x . v_y)`,
`k = 1..4` (Legendre polynomials of the cosine, `SO(3)`-invariant, unsoldered)
and the soldered edge invariant `S_1 = v_{x,d(e)} v_{y,d(e)}` where `d(e)` is
the lattice direction of the edge (invariant under the proper cubic group
acting simultaneously on the lattice and on the Bloch vector). Site invariant
`H = sum_i v_i^4 - 3/5` (cubic anisotropy of the letter, mean zero on the
sphere). `PARAMS = [P_1, P_2, P_3, P_4, S_1, H]`.

**Declared rule family (order-blind).** `W_theta(v) = prod_{e in E} (1 + sum_a theta_a f_a(e))`
with the static law `mu_theta = W_theta / Z_theta`. At `theta = 0` the law is the
uniform product measure on the alphabet, and the Fisher matrix is the
covariance matrix of the sufficient statistics `T_a = sum_e f_a(e)` (mean
subtracted), computed exactly as a rational matrix.

**Declared formation model for order-dependent rules.** A total order `sigma`
of the sites; at its turn the site `x` sees its recorded neighbours
`A_x = { y ~ x : sigma(y) < sigma(x) }` and draws from the conditional
`r(p | v|A_x)`. Two conditional classes are declared, both normalised at every
step: the product class `r(p|A) = prod_{q in A} (1 + theta p . v_q) / Z(v|A)`
and the additive class `r(p|A) = (1 + theta sum_{q in A} p . v_q) / Z`,
`Z = 1` exactly for the additive class. The degree-one kernel `g_e = v_x . v_y`
is the common seed. `mu_sigma = prod_x r(v_x | v|A_x)` is the finished-window
law for the order `sigma`. Named orders: monotone-box (lexicographic in the box
coordinates, so `x` records `x - e_d`), reversed (`x` records `x + e_d`), the
uniform mixture over all orders, and the static law.

## Prior art and what is new

- **Binary readability no-go.** The superlattice role-pattern note (2026-09-04)
  states at nearest-neighbour range: "the minimal covariant nearest-neighbour
  table over records is the all-permissive one." With two letters the
  covariant nearest-neighbour table has no free direction to read. This note
  computes the same question on the alphabet the Qubit axiom actually supplies
  and finds six readable directions.
- **Stipulation R and partial reading.** The readable-matter-law note
  (2026-09-04) declares "**Stipulation R, the marginal reading of an unrecorded
  neighbour.** For a partial profile the menu is the union over completions of
  its open offsets." and notes that its full catalog "is a mathematical oracle;
  no finite physical observations or probability rule providing it are
  derived." The present note reads finished windows only and needs no
  stipulation about unrecorded neighbours.
- **Continuum record alphabet (PR #7926, readability campaign 2026-09-04).**
  That work lifted the finite-alphabet abundance no-go constructively with a
  record-echo rule and a fibred Born theorem. It concerned abundance of
  covariant rules, not their identifiability from records; identifiability is
  the content here.
- **Formation-order census (PR #8102, concurrent).** Lemma L there proves that
  for symmetric product conditionals `mu_sigma` depends on `sigma` only through
  the multiset `K(sigma)` of recorded sets of size at least two, and counts 28
  laws on `2x3` and 542 on `2x2x2`. This note reproduces those counts with
  independent code, locates the first order in the rule strength at which
  `K` becomes visible (second), and exhibits that the product class is blind to
  a `K`-difference at that order (monotone-box versus reversed on the cube).
- **Sharp-Record Fisher Tangent Space Narrow Theorem Note (2026-06-06).** An
  earlier Fisher-tangent computation for sharp records in a different setting;
  cited by title as the nearest prior use of the Fisher rank as the readability
  criterion.
- **Design note (PR #8093).** Readability block: "Fisher information of the
  finished-window law with respect to the parameters of a covariant rule
  family; rank deficiency marks the unreadable directions. Computed exactly
  (symbolic) on `2x3` and `2x2x2` for polynomial rule families in the invariants
  of the possibility-covariance block." Success criterion: full rank for
  order-blind rules. The order-blind characterisation there is "`mu_sigma` is
  independent of `sigma`".

New here: the closed-form continuum Fisher matrix and its proof for any finite
window; the exact rank collapse and null directions on two finite alphabets;
the proof that the formation order is absent from the first-order tangent for
every order and every normalised conditional class; the exact second-order
coefficients of the product and additive classes with their Gram matrices; the
pair-vector / `K` / apex-vector hierarchy with exact counts; the monotone-box
versus reversed blindness of the product class at second order.

## Exact target and obligation graph

Target: is the rule `r(p | q)` identifiable from finished-window record
statistics in the Bloch alphabet, for order-blind rules, and what trace does an
order law leave? Obligations discharged here: (O1) the Fisher matrix of the
order-blind family at the uniform point, exactly, with rank; (O2) the same on
two finite alphabets with the null space named; (O3) the tangent at first order
in the rule strength for every total order; (O4) the second-order coefficient
for two conditional classes in closed form, validated against truncated series
of the exact normalised law; (O5) exact `L^2` separations between order classes
and the named-law table. Not undertaken: degree-two kernels for order laws,
windows beyond eight sites, base points other than the uniform law, and any
statement about which conditional class the framework realises.

## Theorem 1 (continuum Fisher matrix of the order-blind family, closed form)

**Statement.** On any finite window `W = (V, E)` in `Z^3` with the continuum
alphabet, the Fisher matrix of `mu_theta` at `theta = 0` in the basis
`[P_1, P_2, P_3, P_4, S_1, H]` is

    I[P_i, P_j] = delta_ij |E| / (2i + 1),     I[S_1, S_1] = I[P_1, S_1] = |E| / 9,
    I[P_k, S_1] = 0  (k = 2, 3, 4),            I[H, H] = 16 n / 525,
    I[H, anything else] = 0.

Its rank is 6 whenever `|E| >= 1` and `n >= 1`. Runner values: `2x3`
`diag = 7/3, 7/5, 1, 7/9, 7/9, 32/175`, `I[P_1, S_1] = 7/9`, rank 6; `2x2x2`
`diag = 4, 12/5, 12/7, 4/3, 4/3, 128/525`, `I[P_1, S_1] = 4/3`, rank 6.

**Proof.** At `theta = 0` the law is the product of uniform measures and
`I_ab = Cov(T_a, T_b)`. (i) *Edges decorrelate.* For two distinct edges sharing
a vertex `v`, the wedge identity `E_v[P_i(u . v) P_j(v . w)] = delta_ij P_i(u . w) / (2i + 1)`
(Funk-Hecke, or the addition theorem for spherical harmonics) followed by
averaging over the free endpoint `u` or `w` gives `0` for `i, j >= 1`, because
`E_u[P_i(u . w)] = 0` on the sphere. Disjoint edges are independent. So the
covariance of two edge sums is a sum over single edges. (ii) *One edge.*
`E[P_i(t) P_j(t)] = delta_ij / (2i + 1)` for `t = v_x . v_y`, whose density on
`[-1, 1]` is uniform. `E[(v_d w_d)^2] = E[v_d^2] E[w_d^2] = 1/9`.
`E[(v . w) v_d w_d] = sum_c E[v_c v_d] E[w_c w_d] = E[v_d^2] E[w_d^2] = 1/9`, and
`E[P_k(v . w) v_d w_d] = 0` for `k >= 2` because `v_d w_d` lies in the degree-one
component of the two-point kernel. (iii) *Site term.*
`E[(sum_i v_i^4)^2] = 3 E[v_1^8] + 6 E[v_1^4 v_2^4] = 3/9 + 6/105 = 41/105`, so
`Var(sum_i v_i^4) = 41/105 - 9/25 = 16/525`; distinct sites are independent;
`H` is uncorrelated with every edge term because `E_{v_y}[P_k(v_x . v_y)] = 0`
and `E_{v_y}[v_{y,d}] = 0`. (iv) The matrix is block diagonal with the
`2x2` block `[[|E|/3, |E|/9], [|E|/9, |E|/9]]` of determinant `2|E|^2/81 > 0`,
positive diagonal entries elsewhere, hence rank 6. The runner evaluates every
entry by exact polynomial expectation and compares with this prediction
(check family S2).

**Reading.** Every direction of the six-parameter covariant rule is an
observable of the finished-window record statistics, with information growing
linearly in the number of recorded edges. The soldered direction `S_1` is
readable but partly aliased with `P_1` (their information angle is fixed by
`I[P_1, S_1]^2 / (I[P_1, P_1] I[S_1, S_1]) = 1/3`).

## Theorem 2 (finite alphabets collapse the rank, with the null directions named)

**Statement.** Same family, same windows.

| alphabet | window | rank | null directions |
|---|---|---|---|
| `binary_z` | `2x3` | 1 | `P_2`, `P_4`, `H`, `P_1 - P_3`, `S_1` |
| `binary_z` | `2x2x2` | 2 | `P_2`, `P_4`, `H`, `P_1 - P_3` |
| `six_axis` | `2x3` | 3 | `H`, `P_1 - P_3`, `P_4 - (5/12) P_2` |
| `six_axis` | `2x2x2` | 3 | `H`, `P_1 - P_3`, `P_4 - (5/12) P_2` |

**Proof.** On `binary_z` the cosine `t = v_x . v_y` takes the values `+-1`, so
`P_2(t) = P_4(t) = 1` and `P_3(t) = P_1(t)` identically, and
`H = 1 - 3/5` is constant; these give the null vectors `P_2, P_4, H, P_1 - P_3`.
On `2x3` there is no edge in the `z` direction, so `S_1 = v_{x,d} v_{y,d}`
vanishes identically on `+-e_z` letters, the fifth null vector; on `2x2x2`
`S_1` equals `P_1` restricted to the four `z`-edges, an independent direction,
hence rank 2. On `six_axis` the cosine takes the values `-1, 0, 1`, on which
`P_3 = P_1`, `P_4 - (5/12) P_2 = 7/12` is constant, and `H = 1 - 3/5 = 2/5` is
constant; the remaining three directions `P_1, P_2, S_1` have a nonsingular
covariance, hence rank 3. The runner computes the exact covariance on each
alphabet, its rank, and checks that each named vector is in the null space and
that the named vectors span it (check family S3).

**Reading.** This is the continuum-alphabet resolution of the binary no-go:
what the binary alphabet could not read is exactly the set of covariant
invariants that are constant, or coincide, on the letter set. Readability of
the law is a property of the alphabet the Qubit axiom supplies, not of the
geometry of the window.

## Theorem 3 (the formation order is absent from the first-order tangent)

**Statement.** For every total order `sigma` of the window (720 on `2x3`,
40320 on `2x2x2`), every conditional class in which each step is normalised,
and the Legendre kernel `g = P_d(p . v_q)` (checked for `d = 1, 2` on `2x3` and
`d = 1` on `2x2x2`; the proof below holds for every `d >= 1`),

    mu_sigma = 1 + theta T_1 + O(theta^2),     T_1 = sum_{e in E} g_e,

with `T_1` independent of `sigma`. Consequently the direction of any
order-mixture `L_pi = (1 - pi) L_sigma + pi L_sigma'` is a null direction of the
Fisher matrix at the uniform point.

**Proof.** At its turn the site `x` draws from `r(p | v|A_x) = (1 + theta sum_{q in A_x} g(p, v_q) + O(theta^2)) / Z(v|A_x)`
in either class, and `Z = 1 + O(theta^2)` because `E_p[P_d(p . q)] = 0` on the
sphere for `d >= 1` (the runner checks this for `d = 1..4` as an exact identity
of polynomial expectations). Multiplying over sites, every edge `xy` contributes
its kernel exactly once, at the later endpoint, so the first-order coefficient is
`sum_e g_e` regardless of which endpoint is later. The runner computes the
first-order coefficient of the exact normalised product for all orders and
verifies the identity (check family S4). The mixture statement is immediate:
`d L_pi / d pi = L_sigma' - L_sigma = O(theta^2)`.

**Reading.** At leading order in the rule strength the records carry no
information about the order in which they formed. Whatever an order law says
must be read from second-order record correlations or higher.

## Theorem 4 (second-order coefficients of the two conditional classes, closed form)

**Statement.** With the degree-one kernel `g_e = v_x . v_y`, write
`A = sum_{e < e'} g_e g_e'` (the static second-order coefficient, `E[A] = 0`) and,
for a wedge `w = (x; q, q')`, `iota_sigma(w) = 1` when both `q` and `q'` are
recorded before `x` under `sigma` and `0` otherwise. Then, as exact identities
of the normalised finished-window law,

    mu_sigma = 1 + theta T_1 + theta^2 c_sigma + O(theta^3),
    product class:   c_sigma = A - (1/3) sum_w iota_sigma(w) (v_q . v_q'),
    additive class:  c_sigma = A - sum_w iota_sigma(w) (v_x . v_q)(v_x . v_q').

The product coefficient depends on `sigma` only through the multiset of arm
pairs `{q, q'}` whose apex is recorded last (apex-less, in agreement with Lemma
L of PR #8102); the additive coefficient depends on the apex `x` as well
(apex-resolved).

**Proof.** In the product class, at the turn of `x` with recorded set `A_x`,
`prod_{q in A_x} (1 + theta p . v_q) = 1 + theta sum_q p . v_q + theta^2 sum_{q < q'} (p . v_q)(p . v_q') + ...`
and the normaliser is `Z = 1 + theta^2 sum_{q < q'} E_p[(p . v_q)(p . v_q')] + O(theta^3) = 1 + (theta^2 / 3) sum_{q < q'} v_q . v_q' + O(theta^3)`,
using `E_p[(p . q)(p . q')] = (1/3) q . q'` (runner check). Dividing, the
`theta^2` term at `x` is `sum_{q<q'} [(v_x . v_q)(v_x . v_q') - (1/3) v_q . v_q']`;
the first part, summed over all sites and added to the cross terms between
different sites, reassembles `A` (every pair of distinct edges appears once),
and the second part is the wedge sum with `iota_sigma`. In the additive class
`Z = 1 + theta sum_q E_p[p . v_q] = 1` exactly, there is no `theta^2` term inside
one site's factor, so relative to the product `prod_e (1 + theta g_e)` the
coefficient loses exactly the same-apex products `(v_x . v_q)(v_x . v_q')` over
recorded wedges. The runner validates both closed forms against the truncated
`theta`-series of the exact normalised law, coefficient by coefficient, for the
monotone-box and reversed orders on `2x3` (both classes) and the monotone-box
order on `2x2x2` (both classes), and confirms `E[A] = 0` on both windows
(check families S4, S5, S6).

## Theorem 5 (exact second-order separations and the class hierarchy)

**Statement.** Let `dist^2(sigma, sigma') = || c_sigma - c_sigma' ||^2` in
`L^2` of the uniform product measure. (a) *Grams.* The apex terms
`(v_x . v_q)(v_x . v_q')` have Gram matrix `1/9` on the diagonal, `1/27` between
two wedges sharing the same arm pair with different apices, and `0` otherwise;
its rank equals the number of wedges (10 on `2x3`, 24 on `2x2x2`), so the
additive coefficient map `iota_sigma -> c_sigma` is injective. The arm-pair
terms `v_q . v_q'` have Gram matrix `(1/3) I` (6 and 12 pairs). Hence

    product:  dist^2 = |Delta pair-vector|^2 / 27,
    additive: dist^2 = (Delta iota)^T G_apex (Delta iota).

(b) *Counts.* Over all orders the pair-vector, the recorded-set multiset `K`,
and the apex-vector `iota_sigma` take 26, 28, 36 values on `2x3` and 448, 542,
710 on `2x2x2`; the pair-vector is a function of `K`, and `K` is a function of
the apex-vector, so pair-vector <= `K` <= apex-vector as partitions of the
orders. The `K` counts reproduce the census of PR #8102 with independent code.
(c) *Separations.* Product class: minimum nonzero `dist^2 = 1/27` on both
windows, maximum `18/27` (`2x3`, all 325 pairs of pair-vector classes) and
`48/27` (`2x2x2`, all 100128 pairs). Additive class: minimum `1/9` on both
windows, maximum `38/27` (`2x3`, all 630 pairs of apex-vector classes) and
`5/3` (`2x2x2`, the 709 pairs monotone-box versus every other class).
(d) *Apex-latest frequency.* Over the uniform mixture of all orders every wedge
has its apex recorded last with frequency exactly `1/3`.

**Proof.** (a) `E[(v_x . v_q)^2 (v_x . v_q')^2] = E_x[ E_q[(v_x . v_q)^2] E_q'[(v_x . v_q')^2] ] = 1/9`;
for two wedges `(x; q, q')` and `(y; q, q')` with `x != y`,
`E[(v_x . v_q)(v_x . v_q')(v_y . v_q)(v_y . v_q')] = E[ (1/3)(v_q . v_q') (1/3)(v_q . v_q') ] = (1/9)(1/3) = 1/27`;
any other pair of wedges leaves a free unit vector with zero mean. The arm-pair
Gram is `E[(v_q . v_q')^2] = 1/3` on the diagonal and zero off it. Rank and
injectivity are exact rational rank computations. (b) The pair-vector is the sum
over sites of the arm pairs inside each recorded set, hence a function of the
multiset `K`; each recorded set `A_x` is the set of arms of the wedges with apex
`x` and `iota = 1` together with the singleton recorded neighbours, and the
singletons are determined by the wedge data, so `K` is a function of `iota`.
Counts are enumerations over all 720 and 40320 orders. (c) Exact minimisation
and maximisation of the quadratic forms in (a) over the enumerated classes.
(d) A wedge's apex is the latest of its three sites in exactly one third of the
orders by symmetry; the runner counts.

**Corollary (what a second-order separation buys).** For the two-order mixture
`L_pi = (1 - pi) mu_sigma + pi mu_sigma'` at fixed small `theta`, the Fisher
information for `pi` at the uniform point is
`I_pipi = E[(mu_sigma' - mu_sigma)^2] + O(theta^5) = theta^4 dist^2(sigma, sigma') + O(theta^5)`.
The separations in (c) are therefore the leading coefficients of the
information that finished records carry about the order law, and a zero
separation means the two orders are indistinguishable from records at this order
in the rule strength.

## Theorem 6 (named order laws; a blind spot of the product class)

**Statement.** On each window the monotone-box order has exactly one recorded
map (5 linear extensions on `2x3`, 48 on `2x2x2`, all recording `x - e_d` at
`x`), and the reversed order records `x + e_d`. The second-order separations
are exact:

| window | pair | product `dist^2` | additive `dist^2` |
|---|---|---|---|
| `2x3` | static vs uniform mixture | `2/27` | `38/243` |
| `2x3` | static vs monotone-box | `2/27` | `2/9` |
| `2x3` | monotone-box vs reversed | `0` | `8/27` |
| `2x2x2` | static vs uniform mixture | `16/81` | `32/81` |
| `2x2x2` | static vs monotone-box | `2/9` | `2/3` |
| `2x2x2` | monotone-box vs reversed | `0` | `8/9` |

The monotone-box and reversed orders have equal pair-vectors on both windows,
so the product class does not separate them at second order. Their recorded-set
multisets `K` are equal on `2x3` and differ on `2x2x2`; on the cube the census
of PR #8102 therefore separates two laws that agree to second order in the
degree-one kernel, and the separation is at third order or beyond. The
additive class separates them at second order by `8/27` and `8/9`.

**Proof.** Product-class distances are `|Delta pair-vector|^2 / 27` (Theorem
5a); the static law has pair-vector zero, and for the uniform mixture the
pair-vector is the average over orders, giving
`dist^2 = sum_pairs mult^2 / 243` with `mult` the number of wedges on a pair
(each apex is latest with frequency `1/3`, hence the `1/9 . 1/27`). For the
monotone-box order `m` is the vector of apex-latest wedges, `|m|^2 = 2` on
`2x3` and `6` on `2x2x2`, giving `2/27` and `2/9`. Under the reversal
`x -> -x` every wedge `(x; q, q')` with apex latest maps to a wedge whose apex
is earliest; on these windows the reversed order's apex-latest wedges have the
same arm pairs as the monotone order's (the arms of a box wedge are
`x - e_d, x - e_d'`, and reversal sends the pair `{x - e_d, x - e_d'}` at apex `x`
to the pair `{x' + e_d, x' + e_d'}` at apex `x'`, which is the same unordered
pair of sites when `x' = x - e_d - e_d'`), so the pair-vectors agree while the
apices differ, which is why the additive class sees them. The additive values
are the apex Gram form on the difference of the two indicator vectors (Theorem
5a), evaluated exactly. The runner enumerates the linear extensions, checks the
recorded maps, checks the `K`-multiset equality on `2x3` and inequality on
`2x2x2`, and verifies each table entry against the closed forms (check family
S6).

**Reading.** A rule whose formation step multiplies the influence of its
recorded neighbours writes the order into the records more coarsely than a rule
that adds them. Which of the two the framework realises is not fixed by the
Admissibility sentence; the composition and law selection block takes this up.

## No-Go Discipline Gate

The negative statements here are (i) the rank collapse on finite alphabets and
(ii) the absence of the order at first order and of the monotone/reversed
difference at second order in the product class.

- **N1 alternative routes.** Other invariants than the six declared could be
  readable on a finite alphabet; the claim is about this family only. Other
  kernels (degree two and higher) could separate monotone-box from reversed at
  second order in the product class; only the degree-one kernel is computed.
- **N2 wall independence.** The finite-alphabet null vectors are algebraic
  identities on the letter set (`P_3 = P_1` on `{-1, 0, 1}` and so on),
  independent of the window and of the normalisation.
- **N3 hidden walls.** The base point is the uniform law. Away from `theta = 0`
  the Fisher matrix can change rank; no statement is made there.
- **N4 residual matching.** The rank deficit equals the number of named null
  vectors in every row of the Theorem 2 table (`6 - 1 = 5`, `6 - 2 = 4`,
  `6 - 3 = 3`), and the named vectors span the null space (runner check).
- **N5 rhetoric.** No route is described as unique or final; "unreadable" means
  a zero row of an exact Fisher matrix at the declared base point.
- **N6 partial closure.** Larger windows increase `|E|` and `n` linearly in the
  continuum entries; they do not lift a finite-alphabet null vector, which is
  letter-set algebra.
- **N7 steelman.** One could argue that `binary_z` is not a fair alphabet
  because `S_1` vanishes on `2x3` for lack of `z`-edges; the `2x2x2` row shows the
  rank rising to 2 for exactly that reason, and the `six_axis` rows show a
  rotation-covering finite alphabet still losing three directions.
- **N8 cross-cycle echo.** The binary all-permissive result of 2026-09-04 and
  the finite-alphabet rows here are the same phenomenon at two ranges; the
  continuum lift of the abundance no-go in PR #7926 is the constructive side.

## Falsifiers

- Any entry of the continuum Fisher matrix differing from Theorem 1 on any
  finite window in `Z^3`.
- A vector outside the span of the named null vectors annihilated by a finite-
  alphabet Fisher matrix in Theorem 2, or a named vector not annihilated.
- A total order on either window whose first-order coefficient differs from
  `T_1`, in either normalised class.
- A `theta`-series of the exact normalised law whose second-order coefficient
  differs from the closed forms of Theorem 4 for any order or class.
- A monotone-box versus reversed pair-vector difference on either window, or a
  `K`-multiset equality on `2x2x2`.
- Any runner check failing, or a mutation of a load-bearing constant passing
  the full suite.

## Boundaries and non-claims

- Windows `2x3` and `2x2x2` only; the Theorem 1 closed form is proved for any
  finite window but checked on these two.
- The rule family is the declared six-parameter product family at its uniform
  base point; nothing is asserted about other families, other base points, or
  the values the framework's rule actually takes.
- Order laws are computed in the degree-one kernel to second order in `theta`;
  the third-order and higher content, where the cube's `K`-difference between
  monotone-box and reversed must appear for the product class, is not computed.
- The two conditional classes are declared models of a formation step; the
  axioms do not fix which, if either, is realised. The difference between them
  is recorded as a decision point for the composition and law selection block,
  not resolved here.
- No physical rate, clock, or formation unit is used; "order" means a total
  order of sites, "second order" means the power of the rule strength.
- Readability here is identifiability at the level of Fisher information from
  finished-window statistics; it says nothing about how many windows a finite
  observer must read, nor about partial windows (Stipulation R is not used).

## Imports

None beyond the four axioms and the realized state primitive. The uniform
measure on `S^2` at the base point is the `SO(3)`-invariant probability
measure on the pure possibilities of `M_2(C)`, not an added weighting: it is
the `theta = 0` member of the declared family, and every statement is about
derivatives at that member. The Legendre invariants are the complete set of
`SO(3)`-invariant two-point polynomials up to degree four; `S_1` is the lowest
soldered invariant; `H` is the lowest nonconstant cubic-invariant site
polynomial. The two conditional classes are declared models, not imports of a
dynamics. The formation-order census (PR #8102) and the handed-rule census
(PR #8105) are concurrent campaign results and are cited, not depended on.

## Review record

- **Seat.** One Fable 5.1 seat wrote the runner, the note, the mutation
  census and the independent recomputation; no subagents were used at any
  stage, per the owner's instruction for the execution phase of the campaign.
- **Independence sources.** (i) Every continuum Fisher entry is compared with
  the analytic closed form of Theorem 1, which was derived by hand before the
  runner printed it. (ii) The sphere moments were recomputed by an independent
  Gamma-function formula for every even exponent triple of degree at most eight
  and agree with the double-factorial rationals. (iii) The one-edge Legendre
  Gram was recomputed by explicit-sum Legendre polynomials and 20-point
  Gauss-Legendre quadrature and agrees with `delta_ij / (2i + 1)`. (iv) A Monte
  Carlo sample of 400,000 wedges (seed 20260913) gives every wedge cross-moment
  `|E[P_i(u . v) P_j(v . w)]| <= 0.0008` (standard error about `0.0005`) and
  `Var(sum_i v_i^4) = 0.03044` against the exact `16/525 = 0.03048`. (v) The
  monotone-box apex-latest count `|m|^2 = 2` on `2x3` was done by hand and gives
  the `2/27` in the Theorem 6 table. (vi) The `K`-multiset counts 28 and 542
  were recomputed by code written for this note and match PR #8102.
- **Mutation census.** Six external copies of the runner, each with one exact
  substitution, all run to completion; a mutation is caught when the total
  reports at least one failure.

| mutation | substitution | result |
|---|---|---|
| sphere moment denominator | `dfact(a + b + c + 1)` -> `dfact(a + b + c - 1)` | `PASS=37 FAIL=26` |
| Legendre recursion coefficient | `Fr(2 * k + 1, k + 1)` -> `Fr(2 * k - 1, k + 1)` | `PASS=48 FAIL=15` |
| wedge indicator | `q in Q[x] and qq in Q[x]` -> `or` | `PASS=61 FAIL=2` |
| six-axis even moment | `Fr(1, 3)` -> `Fr(1, 2)` | `PASS=59 FAIL=4` |
| product-class normaliser | `Fr(-1, 3)` -> `Fr(-1, 2)` | `PASS=58 FAIL=5` |
| recorded neighbours | `pos[y] < pos[x]` -> `pos[y] > pos[x]` | `PASS=61 FAIL=2` |

  Every mutation is caught. The two-failure mutations are caught by exactly the
  checks that test the mutated quantity (the apex-latest frequency and the
  monotone/reversed recorded maps), which is the intended granularity.
- **Vacuity guard.** No check compares a quantity with itself; each family
  compares a runner computation with a hand-derived prediction, an independent
  code path, or an enumeration count from another PR.
- **Budget.** Exact rationals throughout; 8 sites at most; no dense operator
  spaces; about 8 s wall clock; stdout under 6000 characters.

## Verification

```bash
python3 scripts/admissibility_readability_continuum_alphabet_fisher_rank_2026_09_13.py
```

Expected final line: `TOTAL: PASS=63 FAIL=0`. Check families:

| family | content | checks |
|---|---|---|
| S1 | sphere moments, one-edge Legendre and soldered Grams, wedge decorrelation, `H` moments | 6 |
| S2 | continuum Fisher matrix equals the Theorem 1 closed form, rank 6, both windows | 6 |
| S3 | finite-alphabet Fisher ranks and named null spaces, both alphabets, both windows | 11 |
| S4 | normalisation identities; first-order tangent equals `T_1` for all 720 and 40320 orders; apex-latest frequency `1/3` | 6 |
| S5 | `E[A] = 0`; `K` census 28 and 542; Grams and ranks; class counts; min and max separations | 14 |
| S6 | named laws: linear extensions, recorded maps, table entries, closed-form identities, `theta`-series validation | 20 |

The cached output is at
`logs/runner-cache/admissibility_readability_continuum_alphabet_fisher_rank_2026_09_13.txt`.
