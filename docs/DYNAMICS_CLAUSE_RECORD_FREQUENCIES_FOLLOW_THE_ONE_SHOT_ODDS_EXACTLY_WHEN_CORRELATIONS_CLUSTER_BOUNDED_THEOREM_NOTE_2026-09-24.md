---
claim_id: dynamics_clause_record_frequencies_follow_the_one_shot_odds_exactly_when_correlations_cluster_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Under the dynamics clause of the supplied companion construction and the trace rule of the supplied companion construction, supplied and not adopted: when records are projectively read at n distinct sites of one fixed joint state rho with antipodal menus and no intervening evolution, their joint law is the same for every formation order. The frequency F of +p outcomes has E F = (1/n) sum_i (1 + <p_i.s_i>)/2 and Var F = (1/4n^2) sum_ij C_ij, where C_ij are connected correlations (exact, random 6-qubit states). So F concentrates on the one-shot odds exactly when the average connected correlation vanishes. The landed firewall's two laws with odds (2/3, 1/3) are the trace-rule laws of a product state (IID, frequency variance 2/(9n)) and of a cat state (locked, variance 2/9 for every n). On an explicitly supplied 12-site labelled graph, a numerical low-energy vector has correlations below tolerance off same-type bonds and z-menu frequency variance about 0.0097; this establishes neither a thermodynamic gap nor exact uniqueness. The ferromagnetic Heisenberg ground multiplet on a 6-site ring contains both a cat (variance 1/4) and a product (variance 1/24) with the same odds 1/2. For unique gapped ground states of finite-range generators, the standard exponential clustering theorem, imported with its hypotheses and not re-proved, gives concentration. Which ground state forms is not derived."
upstream_dependencies:
  - minimal_axioms
  - record_iid_typicality_firewall_2026-06-06
runner: scripts/dynamics_clause_record_frequencies_follow_the_odds_when_correlations_cluster_2026_09_24.py
---

# Record frequencies follow the one-shot odds exactly when the averaged connected correlation vanishes

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** exact identities and finite checks under supplied clauses, with one imported clustering theorem; unaudited.

## Result and scope

The landed IID/typicality firewall
(`docs/RECORD_IID_TYPICALITY_FIREWALL_2026-06-06.md`) showed that one-step
odds do not fix frequencies. Two exact two-record laws with the same
marginal `(2/3, 1/3)` have different count laws. "Frequency claims require
a sequence law, not only a one-step law." This note supplies that sequence
law under the supplied model's clauses, and says when frequencies follow the
odds.

- **The supplied sequence law is the joint trace rule with selective projector updates and no intervening evolution.** When records form at
  several unrecorded sites from a joint state `rho`, each by the trace rule
  on its menu, the joint law is `Tr(rho prod_i P_i)`. It is the same for
  every formation order, because single-site projectors on different sites
  commute.
- **An exact variance identity.** The frequency `F` of `+p` outcomes has
  mean `(1/n) sum (1 + <p_i.s_i>)/2`, the average one-shot odds. Its
  variance is `(1/4n^2) sum_ij C_ij`, where `C_ij` are the connected
  correlations of `p_i.s_i` and `p_j.s_j`. So frequencies concentrate on
  the one-shot odds exactly when the average connected correlation
  vanishes.
- **The firewall's two laws are two states.** The IID law is a product
  state with odds `(2/3, 1/3)`. The locked law is the cat state
  `sqrt(2/3)|00> + sqrt(1/3)|11>`. On `n` sites the product's frequency
  variance is `2/(9n)`, while the cat's stays `2/9`. Frequencies follow the
  odds for the first and never for the second.
- **Clustering from the clause.** At a supplied compass coupling, a 12-site staircase graph has numerical low-energy and correlation diagnostics. One finite size does not establish a thermodynamic gap or concentration sequence. For unique gapped ground states of finite-range generators,
  the standard exponential clustering theorem gives the same conclusion in
  general.
- **Degenerate ground spaces hold both kinds.** The ferromagnetic
  Heisenberg ground multiplet on a ring contains a cat, whose frequency is
  0 or 1, and a product state, whose frequency concentrates. Both have the
  same one-shot odds `1/2`. Whether frequencies follow the odds then
  depends on which ground state forms. That is not derived.

So, under the clauses, the frequency part of the Born lane reduces to a
property of the state sequence: vanishing averaged connected correlation. For families satisfying the stated uniform clustering hypotheses, it follows from the imported theorem.

## Premises and declared objects

- **Axioms** (`docs/MINIMAL_AXIOMS_2026-06-29.md`). Record: "Only records
  are readable. A readout value is determined by record content alone."
- **The landed firewall.** Two laws with marginal `(2/3, 1/3)`:
  - IID: `Pr(N_0 = 0, 1, 2) = (1/9, 4/9, 4/9)`;
  - locked: `(1/3, 0, 2/3)`.
- **Supplied, not adopted.** The dynamics clause (the supplied companion construction), and the
  trace rule with antipodal menus (the supplied companion construction).
- **Frequency.** `F = (1/n) #{i : record at i is +p_i}`.
- **Connected correlation.**
  `C_ij = <(p_i.s_i)(p_j.s_j)> - <p_i.s_i><p_j.s_j>`, so `C_ii = 1 - <p_i.s_i>^2`.
- **Imported mathematical tool.** The exponential clustering theorem for
  lattice Hamiltonians ([Nachtergaele and Sims, Theorem 2](https://arxiv.org/html/math-ph/0506030v3)). A
  finite-range Hamiltonian with a unique ground state and a spectral gap
  bounded away from zero has connected ground-state correlations of local
  observables that decay exponentially with distance. It is used with these
  hypotheses and is not re-proved.

## Theorem 1 — the joint law and the variance identity

*Statement.* For any state `rho` of `n` unrecorded qubits and any menus:
- the joint law `P(s_1, ..., s_n) = Tr(rho prod_i P_{s_i p_i})` equals the
  law of sequential formation with collapse, in every order;
- `E F = (1/n) sum_i (1 + <p_i.s_i>)/2`;
- `Var F = (1/4n^2) sum_ij C_ij`.

*Proof.*
- Single-site projectors on different sites commute. So sequential
  collapse multiplies to the joint projector in any order.
- The record at `i` is `+1` with indicator `(1 + p_i.s_i)/2`. Expand the
  first and second moments of `F`.

The runner checks both on five random 6-qubit states with random menus, to
`3e-16`. ∎

By Chebyshev, `Pr(|F - E F| > eps) <= Var F / eps^2`. So `F` concentrates on
the average odds exactly when `(1/n^2) sum_ij C_ij -> 0`. This holds
whenever the correlations are summable, `sup_i sum_j |C_ij| < infinity`,
and then `Var F = O(1/n)`.

## Theorem 2 — the firewall's laws are a product and a cat

*Statement.*
- The product state `(sqrt(2/3)|0> + sqrt(1/3)|1>)^{(x) 2}` gives the IID
  law `(1/9, 4/9, 4/9)`.
- The cat `sqrt(2/3)|00> + sqrt(1/3)|11>` gives the locked law
  `(1/3, 0, 2/3)`.
- Both have one-record odds `2/3`.
- On `n` sites the frequency of `0` has mean `2/3` for both. Its variance
  is `2/(9n)` for the product and `2/9` for the cat, at `n = 4, 8, 12`.

*Proof.* Count laws computed from the explicit state vectors. ∎

The firewall's point is thus a property of states. One-shot odds are the
same for a product and a cat, and only the product's correlations cluster.

## Finite diagnostic — a low-energy state on a supplied labelled graph

*Statement.* For the supplied 12-site graph defined below, the numerical eigensolver diagnostics are:
- the computed lowest Ritz value is separated from the next by `0.1290 |K|`;
- `<s_i> = 0`;
- `<s^a_i s^b_j> = 0` unless `(i, j)` is a bond of type `a = b`;
- for the z-menu at every site, the frequency variance is `0.0097`, below
  `1/(4n) = 0.0208`.

*Finite diagnostic.* Sparse floating-point diagonalisation, with seeded start and residual checks. All `12 x 11 x 9` two-site
correlators are evaluated. The largest forbidden one is `4e-14`, and 18
bond correlators are nonzero. ∎

The vanishing of spin correlations beyond same-type bonds is the known
property of Kitaev models. No all-size loop-operator proof is imported here; the displayed finite graph is tested numerically. For unique gapped ground states of
finite-range generators in general, the imported exponential clustering
theorem gives summable correlations, hence `Var F = O(1/n)`.

## Theorem 4 — degenerate ground spaces hold cats and products

*Statement.* The ferromagnetic Heisenberg ring of 6 sites has a
7-dimensional ground multiplet. It contains:
- the cat `(|up...up> + |down...down>)/sqrt 2`, whose z-menu frequency is 0
  or 1 (variance `1/4`);
- the product state along `x`, whose z-menu frequency has variance
  `1/24 = 1/(4n)`.

Both have one-shot odds `1/2`.

*Proof.* Projection onto the ground space, and exact count laws. ∎

## Checks

The runner checks four families; timings and tolerances are recorded in the paired output:
- **A.** Order independence, and the moment identities.
- **B.** The firewall's laws as states, and the variances from explicit
  `n`-site states.
- **C.** The tube's correlation structure, and its variance.
- **D.** The ferromagnetic multiplet.

## What this does not do

- It does not decide which ground state forms in a degenerate ground space.
  That is a relaxation or symmetry-breaking condition. The formation site,
  time and rate stay supplied.
- The exponential clustering theorem is imported, not re-proved. Beyond the
  tube, gaps are not computed.
- Records at the same site at different times are not treated. The Record
  axiom allows one record per site.
- No physical experiment or frequency data is modelled.

## Decision points recorded

- (D-dyn) and (D-tr), as in the supplied companion construction.
- **(D-relax)** extended to many sites: which state records form from. A
  clustering state gives frequencies equal to the odds; a cat state does
  not.

None is adopted.

## Uniformity, graph and probability qualifications

Concentration here means convergence in probability of `F_n-E F_n` to zero. The converse to Chebyshev follows because `|F_n-E F_n|<=1`: its second moment is at most `epsilon^2 + P(|F_n-E F_n|>epsilon)`. Hence the variance criterion is an equivalence, while absolute summability or exponential clustering is sufficient, not necessary. Uniform summability is required over the sequence. For the imported clustering theorem use uniformly bounded finite-range interactions and degree on a fixed-dimensional lattice, a unique ground state in the applicable setting and a uniform positive spectral gap; a finite numerical gap supplies no such infinite-volume hypothesis.

The finite graph has vertices `(x,r,z)`, `x,r in {0,1}`, `z in Z/3Z`. At each z its x-bonds join `(0,r,z)` to `(1,r,z)`, its y-bonds join `(x,0,z)` to `(x,1,z)`, and its z-bonds join `(x,0,z)` to `(x,1,z+1)`. Each labelled edge contributes the product of the two Pauli components of that label, with coefficient one. This explicitly supplied labelled graph is not a proof that its diagonal z-edges are nearest neighbours of the original cubic embedding. The finite computation and identities are self-contained and do not depend on an unlanded compass-model theorem. Selective collapse and absence of intervening dynamics are essential to the order statement; single-site Born marginals alone do not determine a joint law.

## Mathematical dependencies and reproduction

- [DYNAMICS_CLAUSE_COVARIANT_NEAREST_NEIGHBOUR_TWO_QUBIT_GENERATORS_HEISENBERG_UNDER_POSSIBILITY_COVARIANCE_THREE_COUPLINGS_UNDER_FULL_SOLDERING_BOUNDED_THEOREM_NOTE_2026-09-24](DYNAMICS_CLAUSE_COVARIANT_NEAREST_NEIGHBOUR_TWO_QUBIT_GENERATORS_HEISENBERG_UNDER_POSSIBILITY_COVARIANCE_THREE_COUPLINGS_UNDER_FULL_SOLDERING_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [DYNAMICS_CLAUSE_RECORDS_ACT_AS_FIELDS_A_SITE_WITH_SIX_RECORDED_NEIGHBOURS_IS_A_QUBIT_IN_THEIR_FIELD_AND_ITS_LAW_POINTS_ALONG_IT_BOUNDED_THEOREM_NOTE_2026-09-24](DYNAMICS_CLAUSE_RECORDS_ACT_AS_FIELDS_A_SITE_WITH_SIX_RECORDED_NEIGHBOURS_IS_A_QUBIT_IN_THEIR_FIELD_AND_ITS_LAW_POINTS_ALONG_IT_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md)
- [RECORD_IID_TYPICALITY_FIREWALL_2026-06-06](RECORD_IID_TYPICALITY_FIREWALL_2026-06-06.md)

Primary runner: [dynamics_clause_record_frequencies_follow_the_odds_when_correlations_cluster_2026_09_24.py](../scripts/dynamics_clause_record_frequencies_follow_the_odds_when_correlations_cluster_2026_09_24.py). Paired output: [current runner output](../logs/runner-cache/dynamics_clause_record_frequencies_follow_the_odds_when_correlations_cluster_2026_09_24.txt). All numerical historical figures above describe the declared finite setup; current tolerances and diagnostics are in this paired output.

## No-Go Discipline Gate

This section bounds the negative subclaims; it grants neither a retained grade nor an exhaustive search over physical alternatives.

### N1 — Alternative routes

- **ATTEMPTED — Sequential projector law.** Change the joint law by reordering distinct-site projections without intervening evolution. Commutation makes the joint projector unchanged.
- **ATTEMPTED — Moment identity.** Infer concentration from marginals alone. The connected-correlation sum is the exact variance criterion, and boundedness proves its converse.
- **ATTEMPTED — Locked state.** Keep the marginal two thirds but avoid concentration. The cat state succeeds, with variance two ninths for every size.
- **ATTEMPTED — Uniform clustering.** Derive concentration from uniformly summable correlations. This succeeds; the theorem does not claim that pointwise clustering is necessary.
- **ATTEMPTED — Ground-state degeneracy.** Let a Hamiltonian alone select a frequency law. Its ferromagnetic ground space contains both cats and product states, so a preparation rule is still required.

These are the actual formulations tested in the argument and controls above. Successful escapes narrow the rejected broader claim; they are not counted as failed physical alternatives.

### N2 — Conditional structure

No count of independent physical walls is asserted. Dynamics, preparation and readout are supplied jointly; implication relations between possible derivations of them remain unresolved. The scoped results use their explicit hypotheses rather than an asserted wall-independence theorem.

### N3 — Hidden assumptions

The stated Hamiltonian, state preparation, record compression and readout are conditional mathematical inputs, not additions to the axioms. Numerical tolerances and finite graph sizes are diagnostics, not exact or thermodynamic proofs.

### N4 — Residual matching

No prior no-go is used to close an additional residual. Linked companion notes supply only their displayed covariance, projector or probability identities. The examples above do not certify other formation laws or physical models.

### N5 — Resolution

- `per_element:` Single-site projectors and connected-correlation identities are tested.
- `per_site:` Record marginals and their contribution to frequency variance are tested.
- `per_mode:` checked and not executed — no infinite-volume spectral gap is computed.
- `per_block:` Finite product, cat, labelled-graph and ferromagnetic-ring states are tested.
- `lattice_wide:` checked and not executed — uniform clustering is imported conditionally, not numerically proved.

### N6 — Partial closure

Choosing the stated supplied model yields the conditional theorem without adopting a new axiom. A convention cannot by itself select its state, dynamics or probability law. No claim that a new axiom is necessary is made.

### N7 — Strongest counter-route

Correlations can cancel in their spatial average without being uniformly absolutely summable. The exact variance identity permits that route, so exponential clustering is only sufficient. Alternatively a finite low-energy vector can look clustered without a uniform gap along any volume sequence. The note leaves that thermodynamic obligation open.

### N8 — Related work

The linked companion sources are the relevant nearby arguments rechecked for this result. Their conditional boundaries are preserved here. Similar wording or a prior finite computation does not supply a universal obstruction.
