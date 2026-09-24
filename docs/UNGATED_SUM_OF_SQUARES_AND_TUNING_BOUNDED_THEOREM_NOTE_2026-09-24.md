---
claim_id: ungated_sum_of_squares_and_tuning_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Conditional mathematics of the explicitly supplied finite model and stated limits; numerical controls do not establish physical selection or extend the analytic quantifiers."
upstream_dependencies:
  - minimal_axioms
  - local_compensation_common_field_record_limit_bounded_theorem_note_2026-09-24
runner: scripts/ungated_sum_of_squares_and_tuning_2026_09_24.py
---

**Type:** bounded_theorem
**Status:** conditional mathematical result; unaudited.

The complete source argument and its selected companion proofs follow, with the narrow corrections documented in the combined review. Dated author-status statements, seals and numerical observations are historical provenance, not audit authority. Quantum spaces, Hamiltonians, instruments, preparations and resource assumptions are supplied mathematical premises. Fresh controls corroborate the proofs within their scope.

# Exact ungated cancellation and the scope of the tuning

Root constructive diagnostics, September 23, 2026. Provisional arguments in
the supplied hard-core quantum model. These explain features of the proposed
compensation; they do not derive its physical selection.

## 1. Why ungated compensation removes every rotor Hamiltonian order

Use unsigned outward operators F_a and vacancy projections h_a=1-n_a.
The local hard-core algebra gives

    F_a^2=0,   h_a F_a=F_a,   F_a h_a=0,
    [h_a,F_c]=0 and [F_a,F_c]=0 for a!=c.               (1)

The last identity includes shared B destinations: two creation operators on
the same hard-core B site have zero product in either order. For different
destinations, site and link factors commute. The two A sites use distinct
links even if they share a B site. These statements apply to the specified
tensor-product hard-core record algebra and both normalized spins and rotors;
they are not an assumption of fermionic anticommutation.

The exactly ungated model with C0=sum_a F_a^*F_a has

    W+epsilon T+epsilon^2 C0
       =sum_a(h_a-epsilon F_a)^*(h_a-epsilon F_a).       (2)

For every P vector phi define the finite polynomial dressing

    J_epsilon phi=product_(a in A)(I+epsilon F_a)phi.    (3)

Equations (1) imply (h_a-epsilon F_a)J_epsilon phi=0 for every a.
Also P J_epsilon phi=phi, so J_epsilon is injective. At sufficiently small
epsilon its image is exactly the low spectral cluster: that cluster's
projection is norm-close to P and P maps it invertibly onto P; a vector in
the cluster with zero P projection must vanish. Subtracting the dressed
vector with the same P component proves surjectivity onto the cluster.

The canonical low Hamiltonian is therefore identically zero, at every
perturbative order, for (2). This explains the fourth-order identity
A^*C1 A=Z^*Z/2 without relying on a truncated calculation. The entire
finite-volume rotor low band is flat for this *modified* sum-of-squares
Hamiltonian. This does not contradict the nonflat H2 of the original law.

The ungated version of the proposed spin compensation additionally includes
Delta_S=D_infinity-D_S. In the joint scaling, this leaves the positive
diagonal electric Hamiltonian K D, but its rotor fourth-order magnetic
Hamiltonian still vanishes. The radius-two occupancy gate in the main
construction changes the virtual two-vacancy processes and avoids that
particular cancellation on the cube. It is an explicit extra choice.

## 2. A necessary leading condition within the specified model class

This is a restricted conditional requirement, not a principle supplied by
the record axioms. Suppose a family of bounded penalty-preserving C_S has
a strong rotor limit C_infinity, with the same uniform bounds, and suppose
its full P-density dynamics has a strongly continuous ordinary-time limit
for *every* initial trace-class P density, uniformly on compact intervals
including zero. Fix u and use t_S=u/eta, eta=delta/epsilon^2. The bounded
fourth-order and jump terms contribute o(1) on that time scale. The leading
rotor Hamiltonian is

    A_infinity=C_(0,infinity)-M_infinity.

Strong convergence of uniformly bounded H2 operators gives on this short
time interval

    rho_S(t_S) -> exp(-iu A_infinity)rho_0 exp(iu A_infinity).

Uniform ordinary-time convergence and continuity at zero would instead
give rho_0. Equality for all rank-one densities and every u forces
A_infinity to be a scalar multiple of I. If a superselection rule only
permits record-number-block-diagonal initial densities, the same argument
requires a scalar on each permitted number block; it does not constrain
unobservable relative phases between prohibited coherent blocks.

Thus cancelling the non-scalar part of the leading operator is necessary
for this particular all-state, uniform-at-zero, ordinary-time objective.
The argument does not preclude a selected subspace, a weaker local topology,
an interaction picture with changing observables, a rescaled field/time
description, or convergence only after an initial layer. Demanding this
objective is a modeling decision, not evidence that it is physically required.
The unchanged model's particular all-A initialization can also have a
controlled pre-first limit despite failing this all-state criterion.

## 3. Controlled coefficient detuning

Replace the proposed compensation by lambda_S C_S, with

    lambda_S=1+nu/eta+o(eta^(-1)),  nu finite.

Using P C_S P=M_S+D/C from the main construction, its second-order term is

    eta(lambda_S P C_S P-M_S)
       =K D + eta(lambda_S-1) P C_S P.

The extra term is uniformly bounded and converges strongly to nu M_infinity.
The fourth-order coefficient converges to the same H4_infinity^C because
lambda_S tends to one. The full trace-class argument therefore gives the
Hamiltonian h+nu M_infinity, with the same limiting formation operators.
This is a finite ordinary perturbation; the construction is not sensitive
to an O(eta^(-1)) coefficient error in the sense of losing all control.

A fixed nonzero fractional detuning instead leaves a non-scalar leading
operator on the cube's six-record sector, so it fails the all-state criterion
in Section 2. This identifies a genuine coefficient restriction for the
chosen limit. No assertion of an optimal tolerance for every possible
vanishing detuning, initial sector or weaker topology is made here.

The extra coefficient, the occupancy gate, and their physical origin remain
explicit assumptions to test. The construction establishes neither naturalness
nor a unique microscopic law.


## Landing scope and No-Go Discipline Gate

- **N1 — Domain:** the specified graph, sector, input, observable and order of limits.
- **N2 — Alternatives:** other models, initial states, instruments and resource scalings remain possible.
- **N3 — Imports:** supplied quantum and probability structures are mathematical assumptions, not new repository axioms.
- **N4 — Dependencies:** companion results retain their hypotheses; no retained grade is imported.
- **N5 — Evidence:** exact finite controls and fresh numerical diagnostics corroborate the argument; floating computations are not interval enclosures.
- **N6 — Resolution:** density convergence, energy convergence, initial power, finite time and volume limits are distinct statements.
- **N7 — Remaining work:** native selection, physical implementation and empirical identification remain separate obligations.
- **N8 — Authority:** no audit verdict or retained-grade promotion is applied.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository premise boundary; it does not derive the supplied model.
- [local_compensation_common_field_record_limit_bounded_theorem_note_2026-09-24](LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md): conditional companion source within its stated hypotheses.

## Source and verification

Source PR #8841, frozen head `fed8422aaaaff35c4da1ae613d6e889a989613b4`. Original source dispositions and recovery branches are recorded in the combined receipt. Review uses the same primary session without subagents; no separate fix reviewer or formal audit is claimed.

```bash
python3 scripts/ungated_sum_of_squares_and_tuning_2026_09_24.py
```

Fresh controls execute in a temporary directory. Full scientific stdout and generated JSON are included in the authenticated result. Historical diagnostics and deferred source remain recoverable from the original branch.
