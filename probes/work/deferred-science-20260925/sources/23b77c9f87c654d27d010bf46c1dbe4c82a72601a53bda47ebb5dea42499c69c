---
claim_id: dynamics_clause_record_frequencies_follow_the_one_shot_odds_exactly_when_correlations_cluster_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Under the dynamics clause of open PR 9040 and the trace rule of open PR 9041, supplied and not adopted: when records form at n unrecorded sites from a joint state rho with antipodal menus, their joint law is the same for every formation order. The frequency F of +p outcomes has E F = (1/n) sum_i (1 + <p_i.s_i>)/2 and Var F = (1/4n^2) sum_ij C_ij, where C_ij are connected correlations (exact, random 6-qubit states). So F concentrates on the one-shot odds exactly when the average connected correlation vanishes. The landed firewall's two laws with odds (2/3, 1/3) are the trace-rule laws of a product state (IID, frequency variance 2/(9n)) and of a cat state (locked, variance 2/9 for every n). The gapped Kitaev staircase tube at the clause's compass point has a non-degenerate ground state whose spin correlations vanish off same-type bonds, and its z-menu frequency variance is 0.0097 at n = 12. The ferromagnetic Heisenberg ground multiplet on a 6-site ring contains both a cat (variance 1/4) and a product (variance 1/24) with the same odds 1/2. For unique gapped ground states of finite-range generators, the standard exponential clustering theorem, imported with its hypotheses and not re-proved, gives concentration. Which ground state forms is not derived."
upstream_dependencies:
  - minimal_axioms
  - record_iid_typicality_firewall_2026-06-06
runner: scripts/dynamics_clause_record_frequencies_follow_the_odds_when_correlations_cluster_2026_09_24.py
---

# Record frequencies follow the one-shot odds exactly when correlations cluster

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** exact identities and finite checks under supplied clauses, with one imported clustering theorem; unaudited.

## Result and scope

The landed IID/typicality firewall
(`docs/RECORD_IID_TYPICALITY_FIREWALL_2026-06-06.md`) showed that one-step
odds do not fix frequencies. Two exact two-record laws with the same
marginal `(2/3, 1/3)` have different count laws. "Frequency claims require
a sequence law, not only a one-step law." This note supplies that sequence
law under the campaign's clauses, and says when frequencies follow the
odds.

- **The sequence law is the joint trace rule.** When records form at
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
- **Clustering from the clause.** At the compass point, the gapped Kitaev
  staircase tube (open PR 9048) has a non-degenerate ground state. Its spin
  correlations vanish except along same-type bonds, so record frequencies
  concentrate. For unique gapped ground states of finite-range generators,
  the standard exponential clustering theorem gives the same conclusion in
  general.
- **Degenerate ground spaces hold both kinds.** The ferromagnetic
  Heisenberg ground multiplet on a ring contains a cat, whose frequency is
  0 or 1, and a product state, whose frequency concentrates. Both have the
  same one-shot odds `1/2`. Whether frequencies follow the odds then
  depends on which ground state forms. That is not derived.

So, under the clauses, the frequency part of the Born lane reduces to a
property of the state: clustering. For unique gapped ground states it
holds automatically.

## Premises and declared objects

- **Axioms** (`docs/MINIMAL_AXIOMS_2026-06-29.md`). Record: "Only records
  are readable. A readout value is determined by record content alone."
- **The landed firewall.** Two laws with marginal `(2/3, 1/3)`:
  - IID: `Pr(N_0 = 0, 1, 2) = (1/9, 4/9, 4/9)`;
  - locked: `(1/3, 0, 2/3)`.
- **Supplied, not adopted.** The dynamics clause (open PR 9040), and the
  trace rule with antipodal menus (open PR 9041).
- **Frequency.** `F = (1/n) #{i : record at i is +p_i}`.
- **Connected correlation.**
  `C_ij = <(p_i.s_i)(p_j.s_j)> - <p_i.s_i><p_j.s_j>`, so `C_ii = 1 - <p_i.s_i>^2`.
- **Imported mathematical tool.** The exponential clustering theorem for
  lattice Hamiltonians (Hastings and Koma; Nachtergaele and Sims). A
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

## Theorem 3 — a clustering ground state of the clause

*Statement.* At the compass point, on the periodic staircase tube of 12
sites (open PR 9048):
- the ground state is non-degenerate, with gap `0.1290 |K|`;
- `<s_i> = 0`;
- `<s^a_i s^b_j> = 0` unless `(i, j)` is a bond of type `a = b`;
- for the z-menu at every site, the frequency variance is `0.0097`, below
  `1/(4n) = 0.0208`.

*Proof.* Sparse exact diagonalisation. All `12 x 11 x 9` two-site
correlators are evaluated. The largest forbidden one is `4e-14`, and 18
bond correlators are nonzero. ∎

The vanishing of spin correlations beyond same-type bonds is the known
property of Kitaev models. It follows from the conserved loop operators and
is reproduced here numerically. For unique gapped ground states of
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

The runner prints six checks in four families. All pass in under a
second:
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

- (D-dyn) and (D-tr), as in open PRs 9040 and 9041.
- **(D-relax)** extended to many sites: which state records form from. A
  clustering state gives frequencies equal to the odds; a cat state does
  not.

None is adopted.
