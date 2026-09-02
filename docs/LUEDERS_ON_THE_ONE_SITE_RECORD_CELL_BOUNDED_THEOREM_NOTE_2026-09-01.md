---
claim_id: lueders_on_the_one_site_record_cell_bounded_theorem_note_2026-09-01
claim_type: bounded_theorem
claim_scope: "Under a declared grading hypothesis whose operational half reads outcome operations on a recorded site as parity-even CP maps, the effect of a rank-one locked output on a one-site record cell is that output itself. For a rank-one output P = |p><p| any CP outcome operation with range in P has Kraus operators K = |p><v|, four free real parameters at one site, and effect E_P = sum_j |v_j><v_j|; imposing s3 K s3 = K at the even output P = n forces v0 = 0, leaving two free real parameters, so K_j = c_j n and E_P = (sum_j |c_j|^2) n = lambda P, and symmetrically v1 = 0 at P = 1-n; the completeness equation lambda_1 n + lambda_0 (1-n) = 1 has the unique solution lambda_1 = lambda_0 = 1, so E_P = P at both outputs, which is the Lueders form. The evenness is load-bearing: the odd instrument K_1 = |1><0|, K_0 = |0><1| is a complete instrument on the same two outputs with E_P = 1 - P at each. The conclusion is bounded to one site: on the two-mode cell C^2 (x) K with K = C^2 and output P = |11><11| the even Kraus operators with range in P are |11><v| with <v| in the two-dimensional parity sector span{|00>, |11>}, four free real parameters, so E_P ranges over a real-four-dimensional set of effects, and two complete even instruments with the same output carry E_P = P and E_P = |00><00|. For permanence, the Hermitian solutions of [H, n (x) 1] = 0 are exactly (1-n) (x) B(K) (+) n (x) B(K), of real dimension 8 for dim K = 2 and 18 for dim K = 3, strictly containing 1 (x) B(K) of real dimension 4 and 9; the Jordan-Wigner hopping c_x^dag c_y + h.c. is Hermitian and parity-even yet does not commute with n_x, while n_x, n_x n_y and n (x) A for Hermitian A do. The recordable rank-one frames n and 1-n have rank 2 and span the two-dimensional even algebra, not M_2(C) of rank 4. The grading hypothesis is declared by this note and consumed from no row. No axiom is amended and no status is set."
upstream_dependencies: []
runner: scripts/lueders_one_site_record_cell_check_2026_09_01.py
---

# Lüders on the one-site record cell under the grading; permanence is occupation conservation

**Date:** 2026-09-01
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/lueders_one_site_record_cell_check_2026_09_01.py`](../scripts/lueders_one_site_record_cell_check_2026_09_01.py)
**Runner cache:**
[`logs/runner-cache/lueders_one_site_record_cell_check_2026_09_01.txt`](../logs/runner-cache/lueders_one_site_record_cell_check_2026_09_01.txt)
**Parents:** none. Every premise used below is declared in this note.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite-dimensional theorem on a one-site record cell and on a one-site-plus-one-mode cell: the forced effect of a rank-one locked output under the grading, its failure on the larger cell, and the commutant classification behind permanence."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Run independent audit on this self-contained finite-dimensional theorem and route the declared grading hypothesis, in particular its operational half, to the owner as a science-level decision."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

One site carries `M_2(C)`; the enlarged cell carries `M_2(C) (x) B(K)` with `K = C^2` or `K = C^3`, and the two-mode cell carries `M_4(C)` in the basis `|00>, |01>,
|10>, |11>`. The target is the conjunction of the two statements below, which are exactly the two check groups `A` and `B` of the primary runner, seven checks and
six checks respectively.

1. `T1` (`A`). Under the declared hypothesis, an outcome operation on the one-site record cell with a rank-one locked even output has effect equal to that output:
   `E_P = P`, the Lüders form. The evenness is load-bearing, since a complete odd instrument on the same two outputs has `E_P = 1 - P`, and the conclusion is
   bounded to one site, since on the two-mode cell two complete even instruments with the same rank-one output carry different effects.
2. `T2` (`B`). Under the declared hypothesis, permanence of a record at site `x` is conservation of that site's occupation: the Hermitian solutions of `[H, n_x] =
   0` are the commutant `(1-n) (x) B(K) (+) n (x) B(K)`, strictly larger than `1 (x) B(K)`; hopping off the recorded site is excluded while phase, density-density
   and record-conditioned action on `K` survive; and the spanning condition that would give the narrower obstruction is false on the even sector.

## Declared hypothesis

The following is a hypothesis declared by this note. It is not axiom content, it is consumed from no row, and it carries no dependency weight.

```text
Grading hypothesis (declared): the site algebra M_2(C) carries the parity grading Ad(s3)
(even = span{E00, E11}, odd = span{E01, E10}); distinct sites compose by the graded
product; a state is readable only through its parity-even content; and, operationally,
an outcome operation on a recorded site is a CP map whose Kraus operators are
parity-even, that is block-diagonal for the grading.
```

The first three clauses mirror a candidate clause recorded elsewhere as a science-level decision awaiting its owner, plain-text pointer with no grade and no weight:
`MATTER_GRADED_COMPOSITION_AXIOM_UPDATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-01.md`, "no grade, no weight". The fourth clause, the operational reading, is declared
here in the same way and is the clause that does the work in Theorem 1; it is a hypothesis about which operations are physically available, not a theorem of this
note. Nothing here amends, extends, or reinterprets an axiom, and nothing here sets a status of any kind. Every theorem below is conditional on the displayed
hypothesis; read without it, the theorems are statements about the commutant of `s3`, the commutant of `s3 (x) s3`, and the commutant of `n (x) 1`, which is what
the runner actually computes.

## Context re-declared, not imported

A companion note, plain file name with no grade and no dependency weight,
`RECORD_OBSERVABLE_QUOTIENT_AND_RANK_ONE_FORMATION_OUTCOME_OPERATION_NORMAL_FORM_BOUNDED_THEOREM_NOTE_2026-07-11.md`, proves for a rank-one locked output `P =
|p><p|` that any CP outcome operation with range in `P` has Kraus operators `K_j = |p><v_j|`, hence `J_P(rho) = Tr(E_P rho) P` with `E_P = sum_j |v_j><v_j|`; states
that it does not derive `E_P = P`, the Lüders and Born special case needing a separate effect-selection theorem; and derives, under a supplied condition that the
recordable rank-one frames span `M_2(C)`, a permanence obstruction `H in 1_x (x) B(K)`. This note re-declares that normal form and recomputes it in check `A1a`
rather than citing it, cites no grade of that note or of any other, and gives the effect-selection theorem the grading hypothesis makes available on the one-site
cell.

## Imports and authority

Imported scientific authority: none load-bearing. Kraus decompositions of CP maps, instruments as effect-resolving families, and commutants of projections in finite
dimension are standard methodology; every object is redeclared here and every statement is recomputed in full by the primary runner. No observational value, no
fitted number, and no framework premise enters any proof. Non-load-bearing context pointers, plain file names with no grade and no dependency weight:

- `RECORD_OBSERVABLE_QUOTIENT_AND_RANK_ONE_FORMATION_OUTCOME_OPERATION_NORMAL_FORM_BOUNDED_THEOREM_NOTE_2026-07-11.md` (whose normal form and whose open
  effect-selection question this note recomputes and addresses).
- `MATTER_GRADED_COMPOSITION_AXIOM_UPDATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-01.md` (whose clause the first three lines of the hypothesis mirror).

This note re-declares everything it uses and cites none of their grades.

## Obligation graph

The proof is acyclic. Each node after `P0` is checked by the correspondingly lettered runner group.

1. `P0` (declared here): the Pauli matrices, the matrix units of `M_2(C)`, `n = E11`, the lowering operator `c = E01`, the grading `Ad(s3)`, the Kraus form of an
   outcome operation and of an instrument, the two-mode basis, the total parity `s3 (x) s3`, and the Jordan-Wigner pair.
2. `P1` (`A`): the rank-one normal form, the evenness constraint, the forced effect `lambda P`, the completeness solve, the odd counter-instrument, and the two-mode
   caveat.
3. `P2` (`B`): the commutant of `n (x) 1` at `dim K = 2` and `dim K = 3`, the commutant of `M_2(C) (x) 1`, the hopping exclusion, the surviving terms, and the rank
   of the recordable frames.

The strongest supported scope is precisely `P0`--`P2`.

## Definitions

Write `one` for the `2 x 2` identity, `s1, s2, s3` for the Pauli matrices, and `E00, E01, E10, E11` for the matrix units of `M_2(C)`, with `E01 = |0><1|` and `n =
E11 = |1><1|`. The **lowering operator** is `c = E01`, so that `c^dagger c = n` and `s3 = 1 - 2n`. The **parity grading** of the site algebra is `Ad(s3)`, whose
`+1` eigenspace is `span{E00, E11}` and whose `-1` eigenspace is `span{E01, E10}`; an operator `K` is **even** when `s3 K s3 = K` and **odd** when `s3 K s3 = -K`.
An **outcome operation** is a CP map in Kraus form `J(rho) = sum_j K_j rho K_j^dagger`; it has **range in the output** `P` when `P K_j = K_j` for every `j`, and its
**effect** is `E = sum_j K_j^dagger K_j`. An **instrument** is a finite family of outcome operations whose effects sum to the unit. A **locked rank-one output** is
`P = |p><p|`. The **Lüders form** at an output `P` is `E_P = P`.

The **enlarged cell** is `C^2 (x) K` with the record site first and `K = C^2` or `K = C^3`, carrying `n_x = n (x) 1`. The **two-mode cell** is the case `K = C^2`
read as a second fermionic mode, with basis `|00>, |01>, |10>, |11>`, **total parity** `s3 (x) s3` whose `+1` eigenspace is `span{|00>, |11>}` and whose `-1`
eigenspace is `span{|01>, |10>}`, and the **Jordan-Wigner pair**

```text
c_x = c (x) one,   c_y = s3 (x) c,   n_x = c_x^dagger c_x = n (x) one,   n_y = c_y^dagger c_y = one (x) n.
```

The **hopping** term is `c_x^dagger c_y + c_y^dagger c_x`. Real dimensions of spaces of Hermitian matrices are counted as real dimensions throughout; `B(K)` denotes
all operators on `K`, and `1 (x) B(K)` its image acting trivially on the record site.

## Theorem 1 — on the one-site record cell the even instrument is the Lüders instrument

**Conclusion.** Under the declared hypothesis: (1) for the rank-one locked output `P = |1><1| = n`, range in `P` alone forces `K = |1><v|` with `<v| = (K_10,
K_11)`, four free real parameters, effect `E = K^dagger K = |v><v|`, and `K rho K^dagger = Tr(E rho) P` for every Hermitian `rho`, which is the normal form
re-declared above; (2) adding evenness `s3 K s3 = K` forces `v_0 = 0`, leaving two free real parameters, so `K = c n` and, for any family `K_j = c_j n`,

```text
E_P = (sum_j |c_j|^2) n = lambda P,    lambda = sum_j |c_j|^2 >= 0,
```

`lambda` being a sum of squares of real parameters; (3) symmetrically, at the even output `P = 1-n` evenness forces `v_1 = 0`, `K = c (1-n)` and `E_P = |c|^2 (1-n)
= lambda P`; (4) for the exhaustive even instrument with the two outputs `P_1 = n` and `P_0 = 1-n` the completeness equation `lambda_1 n + lambda_0 (1-n) = 1` has
the unique solution `lambda_1 = lambda_0 = 1`, hence `E_P = P` at both outputs, which is the Lüders form; (5) the evenness is load-bearing, since the odd instrument
`K_1 = |1><0| = c^dagger` at output `P_1 = n` and `K_0 = |0><1| = c` at output `P_0 = 1-n` has ranges in its outputs and effects summing to `1`, but satisfies `s3 K
s3 = -K` and carries `E_{P_1} = 1-n` and `E_{P_0} = n`, that is `E_P = 1 - P` at both outputs; (6) the conclusion is bounded to one site: on the two-mode cell with
output `P = |11><11|` the even Kraus operators with range in `P` are exactly `|11><v|` with `<v|` supported on the `+1` parity sector `span{|00>, |11>}` of
dimension `2`, four free real parameters, so `E_P` is supported on that sector and ranges over the whole real-four-dimensional space of Hermitian operators there,
exhibited by four such effects of real rank `4`; and (7) two complete even instruments on that cell, one with outcome Kraus operator `|11><11|` and one with outcome
Kraus operator `|11><00|`, share the output `P = |11><11|` and carry the different effects `E_P = P` and `E_P = |00><00|`.

**Proof.** Item 1 solves `P K = K` for a symbolic complex `2 x 2` matrix in independent real parameters: the first row vanishes, the second is `<v|`, and `K =
|1><v|`, `K^dagger K = |v><v|` and `K rho K^dagger = Tr(E rho) P` are then exact identities on a symbolic Hermitian `rho`. Item 2 adds the linear system `s3 K s3 =
K` to that solve; the joint solution sets `K_10 = 0`, that is `v_0 = 0`, so `K` is a complex multiple of `n`, and the effect of a family is computed symbolically.
Item 3 is the same solve at the complementary output. Item 4 solves the two-unknown linear system supplied by items 2 and 3 together with completeness; the solution
is unique and gives `E_{P_1} = n = P_1` and `E_{P_0} = 1-n = P_0`. Item 5 is a direct computation on the two exhibited Kraus operators, including their oddness and
the completeness of the pair. Items 6 and 7 solve `P K = K` together with `(s3 (x) s3) K (s3 (x) s3) = K` for a symbolic complex `4 x 4` matrix, exhibit four
effects whose real span has rank `4`, and verify evenness, range and completeness of both exhibited instruments.

**Reading, not theorem.** Item 4 is the effect-selection statement the companion note leaves open, obtained here from the operational half of the declared
hypothesis rather than from a new principle: on a cell whose even algebra is two-dimensional and whose even rank-one projectors are the two outputs themselves, an
even Kraus operator into a rank-one output has nowhere to point except that output. Item 6 says the same fact negatively: the argument uses the smallness of the
one-site even algebra, so it stops as soon as the even sector is larger than the output. This observes two computations and derives neither.

## Theorem 2 — permanence of a record is conservation of the recorded occupation

**Conclusion.** Under the declared hypothesis, on `C^2 (x) K` with the record at the first factor: (1) for `dim K = 2` the Hermitian solutions of `[H, n (x) 1] = 0`
are exactly the block-diagonal family `(1-n) (x) B(K) (+) n (x) B(K)`, of real dimension `8 = 2 dim(K)^2`, strictly containing `1 (x) B(K)` of real dimension `4 =
dim(K)^2`, with `n (x) 1` itself commuting and lying outside `1 (x) B(K)`; (2) for `dim K = 3` the same computation gives real dimension `18 = 2 dim(K)^2` against
`9 = dim(K)^2`, with the same block-diagonal form and the same strict containment; (3) the narrower obstruction is exactly what the spanning condition would give,
since the Hermitian solutions of `[H, X (x) 1] = 0` for all `X in M_2(C)` are exactly `1 (x) B(K)`, of real dimension `4` at `dim K = 2`; (4) on the two-mode cell
the Jordan-Wigner pair anticommutes, `n_x = c_x^dagger c_x` and `n_y = c_y^dagger c_y`, and the hopping `c_x^dagger c_y + c_y^dagger c_x` is Hermitian and
parity-even yet fails to commute with `n_x`, while `n_y` and `n_x n_y` commute with `n_x`, both occupations being projectors; (5) the freedom that survives is
strictly larger than an action on `K` alone: the phase term `n_x`, a projector, sits beside the density-density term `n_x n_y` and the record-conditioned term `n
(x) A` for symbolic Hermitian `A`, the last two Hermitian and commuting with `n_x`, and adjoining `n (x) s1` to a real basis of `1 (x) B(K)` raises the rank from
`4` to `5`; (6) the spanning condition itself is false on the even sector, the recordable rank-one frames being `n` and `1-n`, of rank `2`, spanning the
two-dimensional even algebra `span{1, n}` rather than `M_2(C)` of rank `4`, with the odd unit `E01` adjoined raising the rank to `3`.

**Proof.** Items 1 and 2 solve `[H, n (x) 1] = 0` for a symbolic Hermitian matrix in real parameters at `dim K = 2` and `dim K = 3`; in each case every cross-block
entry vanishes identically, the solved family equals `(1-n) (x) H_0 (+) n (x) H_1` on its two Hermitian blocks, and the real dimension is read off as the rank of
the basis obtained by switching on one free real parameter at a time, which also establishes that the parameters are independent. The comparison family `1 (x) B(K)`
is spanned by the images of the `dim(K)^2` Hermitian matrix units, each of which commutes with `n (x) 1`, and the strictness is the rank increase on adjoining `n
(x) 1`. Item 3 is the same style of solve against the two generators `s1 (x) 1` and `s3 (x) 1`, together with the check that `1, s1, s3, s1 s3` has rank `4` in
`M_2(C)`. Item 4 computes the anticommutators, the two occupations, the Hermiticity and parity of the hopping, the three commutators and the two projector
identities, all exact. Item 5 is two commutator computations, two Hermiticity checks, a projector identity and one rank computation. Item 6 is a rank computation on
the stacked frames.

**Consequence.** The obstruction that permanence places on the generator is `[H, n_x] = 0`, not `H in 1 (x) B(K)`. The recorded site keeps its occupation, so
nothing may hop off it or onto it; but the generator may still carry a phase on the recorded site, couple its density to the densities of other sites, and act on
`K` conditionally on the record. Under the hypothesis the difference is not a technicality: it is the whole difference between a record that freezes its cell and a
record that only freezes its occupation.

## Corollary — what this changes

Under the declared hypothesis, and on the one-site and one-site-plus-one-mode surfaces proved above:

1. The effect-selection question the companion note leaves open,
   `RECORD_OBSERVABLE_QUOTIENT_AND_RANK_ONE_FORMATION_OUTCOME_OPERATION_NORMAL_FORM_BOUNDED_THEOREM_NOTE_2026-07-11.md` (plain-text pointer, no grade, no weight),
   is settled on the one-site record cell: `E_P = P`, the Lüders form, by Theorem 1 items 2, 3 and 4. What supplies it is the operational half of the declared
   hypothesis, not a new selection principle.
2. That settlement does not extend upward. By Theorem 1 items 6 and 7 the same question is open again on the two-mode cell, where two complete even instruments
   share an output and carry different effects; a lane needing `E_P = P` on a larger cell needs a further premise and must say which.
3. The permanence obstruction weakens. Under the spanning condition it reads `H in 1 (x) B(K)`, real dimension `4` at `dim K = 2`; under the hypothesis the
   recordable frames do not span, and the obstruction is occupation conservation `[H, n_x] = 0`, of real dimension `8` at `dim K = 2` and `18` at `dim K = 3`
   (Theorem 2 items 1, 2, 3 and 6). Hopping off a recorded site stays excluded; phase, density-density coupling and record-conditioned action on `K` become
   available.

## What does not move

- No formation rule is supplied: nothing here says when a record forms, at which site, or at what rate.
- No rate, coupling, or absolute unit appears. The parameters `lambda`, `c_j`, and the Hermitian blocks of Theorem 2 stay free throughout.
- No site selection is performed. The recorded site is given, not derived.
- No dynamics beyond the commutant classification is claimed: no Hamiltonian is selected, no evolution is solved, and no time-dependence is computed.
- No axiom text is amended, extended, reworded, or reinterpreted, and the grading hypothesis, including its operational half, is declared here rather than consumed
  from a row.
- No status value is set, predicted, or implied. No premise registry, citation manifest, or axiom-premise node is created or edited.

## Interfaces named for other lanes, not moved here

These interfaces are named so that a later note can consume them; nothing here moves them.

- Lanes that need the Lüders form on a record readout: by Theorem 1 item 4 they have it on the one-site cell under the declared hypothesis, and may cite this note
  in place of an effect-selection premise, provided their cell is one site.
- Lanes that model a record cell as a site plus an environment mode: by Theorem 1 items 6 and 7 they do not have it, and by Theorem 2 items 1 and 2 their permanence
  constraint is the occupation commutant, not the narrower algebra.
- Lanes that build a generator on a lattice with records: by Theorem 2 items 4 and 5 the admissible terms at a recorded site are phase, density-density, and
  record-conditioned action on the rest of the cell; hopping across the recorded site is not among them.

## Remaining live routes

1. Cells of three or more sites, and record cells whose environment factor carries its own grading beyond `Ad(s3)`: nothing here is claimed there.
2. A derivation of the operational half of the hypothesis, that outcome operations on a recorded site are parity-even, rather than its declaration. This note proves
   nothing about whether such a derivation exists.
3. Outputs of rank higher than one, and instruments with more than two outputs on the one-site cell.
4. Whether the two-mode freedom of Theorem 1 item 6 is narrowed by a further physical requirement, for instance one restricting Kraus operators to fixed particle
   number rather than fixed parity.

## Executable claim block

The canonical machine-bound restatement of the two theorem conclusions.

```text
site_algebra_and_declared_grading: M_2(C) with Ad(s3), even = span{E00,E11}, odd = span{E01,E10}
locked_output_normal_form: P = |p><p|, K = |p><v|, E_P = sum_j |v_j><v_j|
range_in_P_free_real_parameters_one_site: 4
even_kraus_free_parameters_and_constraint_one_site: 2, v0 = 0 at P = n and v1 = 0 at P = 1-n
even_effect_form_one_site: E_P = lambda P with lambda = sum_j |c_j|^2 >= 0
completeness_solution_and_uniqueness: lambda_1 = lambda_0 = 1, unique
lueders_on_the_one_site_cell: E_P = P at both outputs n and 1-n
odd_instrument_effects: E_P = 1 - P at both outputs
two_mode_output_and_parity_sector_dimension: P = |11><11|, span{|00>,|11>}, 2
two_mode_even_kraus_free_real_parameters: 4
two_mode_effect_freedom_real_dimension: 4
two_even_instruments_same_output_effects: P and |00><00|
occupation_commutant_real_dimension_dimK_2_and_3: 8 and 18, equal to 2 dim(K)^2
inner_algebra_real_dimension_dimK_2_and_3: 4 and 9, equal to dim(K)^2
commutant_of_M2_tensor_one_real_dimension: 4
hopping_parity_even_and_commuting_with_n_x: yes and no
terms_commuting_with_n_x: n_x, n_x n_y, n (x) A
one_site_inner_basis_rank_with_conditional_term: 4 -> 5
recordable_frame_rank_and_full_algebra_rank: 2 and 4
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=13 FAIL=0
```

## Proof boundary

Every statement is proved on one site, on `C^2 (x) K` with `dim K = 2` and `dim K = 3`, and on the two-mode cell, in complex dimensions `2`, `4` and `6`. Nothing is
claimed about three or more sites, about infinite lattices, or about any algebra other than those. The grading hypothesis is declared, not derived, and every
theorem is conditional on it; the operational half, that outcome operations on a recorded site are parity-even CP maps, is the load-bearing clause of Theorem 1 and
is a hypothesis about available operations, not a result. Theorem 1 treats rank-one outputs and the exhaustive two-output instrument, and takes the Kraus form of a
CP map as the definition of an outcome operation rather than deriving it. Theorem 2 classifies Hermitian generators commuting with a given occupation and says
nothing about which of them is realized, about time evolution, or about how a record forms. The two-mode statements of Theorem 1 items 6 and 7 are existence
statements: they exhibit two even instruments, and do not classify all of them beyond the support statement proved. No axiom is amended, no status is set, and no
registry entry is created.

## Review record

This note is self-contained: `upstream_dependencies` is empty, every object is declared in "Definitions", the grading hypothesis with its operational half is
displayed verbatim in "Declared hypothesis" and used nowhere implicitly, and both companion notes named in "Imports and authority" are plain-text pointers carrying
no grade and no weight, their content re-declared and recomputed here rather than imported. Hard landing conditions are a fresh exact runner and cache pair closing
at `PASS=13 FAIL=0` with runtime under two seconds and stdout under `5500` characters, a current zero-dependency citation-manifest entry, and passing repository
pipeline, strict-lint, and changed-evidence gates; independent audit remains a separate lane.
