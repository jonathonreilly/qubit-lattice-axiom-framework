---
claim_id: energy_filters_and_actual_repeated_formation_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Conditional mathematics of the explicitly supplied finite model and stated limits; numerical controls do not establish physical selection or extend the analytic quantifiers."
upstream_dependencies:
  - minimal_axioms
  - prepared_flat_sector_with_electric_dynamics_and_formation_bounded_theorem_note_2026-09-24
  - cube_six_record_rotor_point_spectrum_bounded_theorem_note_2026-09-24
runner: scripts/energy_filters_and_actual_repeated_formation_2026_09_24.py
---

**Type:** bounded_theorem
**Status:** conditional mathematical result; unaudited.

The complete source argument and its selected companion proofs follow, with the narrow corrections documented in the combined review. Dated author-status statements, seals and numerical observations are historical provenance, not audit authority. Quantum spaces, Hamiltonians, instruments, preparations and resource assumptions are supplied mathematical premises. Fresh controls corroborate the proofs within their scope.

# Energy filters and actual repeated formation in the original Hamiltonian

Root-authored conditional theorem candidate, 2026-09-23. Analytic draft before
new controls or independent reconstruction. The Hamiltonian is the original
supplied model. A changed first-formation instrument is explicitly introduced
in sections 4–6; it is not derived from a reservoir or native axioms.

## 1. Fixed sources and the question

The eight-site ring prepared-sector note defines H2_S, H4_S, physical spin
embeddings, the compact flat projector F at H2=-4, and

    eta = K S(S+1),  H6_S = eta H2_S + delta H4_S,
    h_F = K F D2 F + delta F H4 F.                         (1)

The original first jump has flat weight one half. Merely substituting a
prepared state for that actual output would change the problem. Here we ask
whether an explicit spectral selection of the actual output has a limit,
and what happens to the same prescription on the cube. The ring's F is the
entire physical normalizable eigenspace at -4. The cube's physical H2 on
l²(Z^5) tensor C^36 has no eigenvalues. Both are previously independently
checked fixed-graph results, not assumptions about general lattices.

All statements below concern the deterministic effective target model. No
new uniform theorem about microscopic energy measurements, a frequency-
resolved thermal bath, histories conditioned on random microscopic marks,
or increasing spatial volume is claimed. The filter changes the supplied
birth instrument and might be spatially nonlocal.

## 2. A shrinking spectral-window lemma

Let A_n be uniformly bounded selfadjoint operators on a common Hilbert space,
A_n -> A strongly, and eta_n -> infinity. Write H_n=eta_n A_n. Fix a vector
psi whose spectral measure for A has no atoms. For every nonnegative width
w_n with w_n/eta_n -> 0,

    sup_c || 1_[c-w_n,c+w_n](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/579577555dee1be53055423c046538ff9057e45a/.claude/science/mobile-record-formation-20260920/campaign12h_fourth/energy_selected_formation_author/H_n) psi || -> 0.           (2)

The convergence is uniform when psi ranges over a fixed norm-compact subset
of the atomless spectral subspace. It holds as well for vectors approaching
that compact subset in norm. The center c is arbitrary and may depend on n;
a chemical-energy offset is therefore not excluded by silently fixing c.

Proof. Bounded strong convergence of selfadjoint A_n gives f(A_n)->f(A)
strongly for continuous f on a common compact spectral interval, by polynomial
approximation. If (2) fails, select centers c_n and a subsequence with a
positive spectral weight. Their rescaled centers must lie within a common
bounded interval up to a vanishing error. Take a further subsequence
c_n/eta_n -> a. For any d>0, the shrinking intervals are eventually inside
[a-d,a+d]. A continuous bump equal to one there, supported inside
[a-2d,a+2d], bounds their weights from above. Its limiting expectation is at
most the A-spectral measure of [a-2d,a+2d]. Let d decrease to zero. The result
is the assumed zero atom at a, a contradiction. Projections are contractions;
a finite norm net proves the uniform assertion on a compact set, and then
the statement for convergent approximants. This proof requires no absolutely
continuous density and supplies no quantitative rate.

A version at one fixed rescaled center a only requires psi to have zero
spectral mass at a; other eigenvalues of A are then allowed.

Apply this to the full physical finite-spin six-record operator with

    A_S=H2_S+(delta/eta) H4_S.

The normalized link shifts converge strongly to the rotor shifts, and every
coefficient here is a fixed finite sum of finite products. Thus A_S->H2
strongly and its norm is bounded independently of S. Extend finite physical
operators by zero and identify their physical subspaces in the rotor space;
those subspaces increase strongly to the identity. This convention has no
effect on fixed-state limits. In the cube, every fixed vector satisfies (2).
In the ring, vectors in (1-F) satisfy its fixed-center version at -4.

This concerns the distribution of output energy in a stipulated Hamiltonian.
It is not a statement that a formation event violates conservation of energy.
Particle-number-dependent scalar offsets and the energy of an actual source
must be included before making any resource claim.

## 3. Ring functional calculus and an energy-defined preparation

First the prepared theorem has a purely Hamiltonian variant:

    exp[-it(H6_S+4eta)] F psi -> exp(-it h_F) F psi      (3)

strongly, uniformly for t in compact subsets of the whole real line. To see
this without assuming a new adiabatic theorem, set kappa=0 in sections 4–5
of the source proof. The common expansion has Fop=K D2+delta H4, unchanged
quadratic weighted bounds, and the same crossing corrector Q_h. The residual
is bounded by sqrt(h)+eta^-1 h^-3+eta^-1+eta^-2 h^-5. For negative times use
the unitary group and integrate Duhamel over [t,0]; the weighted estimates
hold on [-T,T] with |t|. The choice h=eta^-2/7 gives the same eta^-1/7 core
bound. Unitarity and density extend the assertion to all flat vectors and
their convergent physical spin embeddings. No dissipative inverse is used.

For every g in C0(R), (3) and the shrinking-window lemma imply

    g(H6_S+4eta) -> g(h_F) F                            (4)

strongly on the whole physical rotor space. For g with integrable Fourier
transform, integrate (3) by dominated convergence to prove (4) on F. Uniform
approximation then covers C0(R). On (1-F), first take g of compact support;
the fixed-center lemma bounds its norm by a shrinking spectral window for
H6_S/eta at -4. Approximate a general C0 function uniformly by those of compact
support. The right side of (4) is zero on (1-F). This is a degenerate limit
of functional calculus; it does not assert a selfadjoint limiting operator
on the whole space whose identity is F.

Choose any positive sequence R_S with

    R_S -> infinity,       R_S/eta -> 0,
    Pi_S = 1_[-R_S,R_S](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/579577555dee1be53055423c046538ff9057e45a/.claude/science/mobile-record-formation-20260920/campaign12h_fourth/energy_selected_formation_author/H6_S+4eta).                    (5)

Then Pi_S -> F strongly. For phi in F, (4) for nonnegative compact functions
approaching one makes its ordinary centered spectral measures tight. Since
R_S tends to infinity, ||(1-Pi_S)phi|| tends to zero. On (1-F), the
fixed-center lemma applies because R_S/eta tends to zero. Contraction and
the orthogonal decomposition prove the claim. Physical spin cutoffs may
be applied to each initial vector; their strong convergence changes nothing.

For a fixed ordinary window [-R,R], convergence of its sharp projector
requires h_F to have no eigenvalues at its endpoints. A smooth C0 filter
always obeys (4). In particular the accepted weight of such a filter on a
first output is ||g(h_F) F B psi||², not automatically one half. Only the
expanding but subfast window (5) recovers the full flat contribution.

## 4. An explicit changed instrument, and its exact ring rate

Keep the original finite-spin target Hamiltonian in each particle-number
sector. Modify only the first effective birth jumps, from N=4 to N=6:

    L_(mu),S = sqrt(kappa) Pi_S B_(mu),S.               (6)

Use the original jumps sqrt(kappa) B_(mu),S for N=6 to N=8. Here mu means
either each resolved edge/sign channel or the originally stipulated coherent
sum of the two signs per edge; use the same convention throughout. Equation
(6) is a legitimate contraction-filtered jump, with the loss L*L that belongs
to it. We do not use the old total first rate after rejecting outputs.

The initial ring state has A occupied by positive records, empty B sites,
and an arbitrary normalizable Gauss-compatible rotor field. Each resolved
first B maps it by a unit field shift to a single adjacent-B-pair charge
configuration. In the compact basis of the prepared note, the diagonal of
F on every such configuration is 1/2. The F-paired partner uses the other
adjacent B pair. It is not the opposite sign output of the same edge.
Consequently

    B_(e,sigma)* F B_(e,sigma) = I/2,
    B_(e,+)* F B_(e,-) = 0,
    sum_mu B_mu* F B_mu = 8 I.                        (7)

These are operator identities on the initial field space, not calculations
at one chosen flux. The original unfiltered sum is 16 I. Controls must check
the charge and cut shifts in (7) exactly before this candidate is packaged.

Since Pi_S->F and B_S,B_S* converge strongly with bounded norms, (6) and its
loss converge strongly to sqrt(kappa) F B and 8 kappa I respectively. The
initial Hamiltonian, after its scalar -8eta, converges on the common electric
domain to h4=8K f²+24delta I. This follows from the exact initial identity
H2_S=-8+8f²/[S(S+1)] and the bounded H4_S->24 I. The common-diagonal
interaction-picture argument gives strong first-sector no-event convergence.

The actual filtered output F B phi is now in the prepared sector. For any
fixed initial field, the convergent finite-spin outputs may be inserted in
the prepared no-event theorem by contraction and strong approximation.
No assumption about microscopic conditioning is required to use this
deterministic target Duhamel expansion.

## 5. Full target density and two actual formations on the ring

Let U4(t)=exp(-it h4-4kappa t) and
U6(t)=exp(-it h_F-2kappa t) on F. For any initial density rho0 in the
initial rotor field sector, the limit is the sequential completely positive
evolution with first jumps sqrt(kappa) F B, second jumps sqrt(kappa) B F,
and a stationary fully occupied eight-record sector. Explicitly,

 rho4(t)=U4(t)rho0 U4(t)*,
 rho6(t)=kappa sum_mu integral_0^t
      U6(t-s) F B_mu rho4(s) B_mu* F U6(t-s)* ds,
 rho8(t)=kappa sum_nu integral_0^t B_nu rho6(s) B_nu* ds.    (8)

The finite-spin counterpart converges to (8) in trace norm, uniformly on
compact ordinary times. For finite-rank initial densities, use strong
convergence of the first propagator and jumps, the prepared result for the
source range, and uniform boundedness of all jump operators. Strong
convergence is uniform on each compact source-vector curve, by finite norm
nets. Apply dominated convergence to the two finite time integrals. Extend
to arbitrary trace-class densities using complete positivity and trace-norm
contraction of the full finite and limiting channels. Both instruments have
the same number probabilities because their two loss identities coincide.

Using (7) and F Gamma6 F=4kappa F gives exactly

    p4(t)=exp(-8kappa t),
    p6(t)=2[exp(-4kappa t)-exp(-8kappa t)],
    p8(t)=[1-exp(-4kappa t)]².                         (9)

Thus repeated formation and the retained prepared electric dynamics arise
from the specified filter on actual outputs, rather than replacement of an
unfiltered output by fiat. It is still a finite eight-site system: formation
stops when it is full, and the N=8 field stops in this target. Formula (9)
does not extend to an unfiltered instrument or a larger graph automatically.

## 6. What the identical type of filter does on the cube

In the cube choose any real centers c_S and nonnegative widths w_S=o(eta),
and replace the first jump by

    sqrt(kappa) 1_[c_S-w_S,c_S+w_S](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/579577555dee1be53055423c046538ff9057e45a/.claude/science/mobile-record-formation-20260920/campaign12h_fourth/energy_selected_formation_author/H6_S) B_(mu),S.      (10)

The shrinking-window lemma and the cube's no-point-spectrum theorem make
every such jump converge strongly to zero on fixed initial rotor vectors.
The bound is uniform on compact sets; B_S converges strongly uniformly on
those sets. The associated first loss converges strongly to zero and is
uniformly bounded. The initial common electric Hamiltonian plus its bounded
magnetic interaction has the same strong limit as before. Its interaction-
picture Dyson series with the vanishing bounded loss proves convergence to
unitary evolution in N=4. Trace conservation then implies that the total
probability of either later number sector tends to zero uniformly on every
fixed time interval. This conclusion is about the explicitly filtered
instrument (10), with fixed kappa; it is not a rate calculation for a derived
energy-conserving reservoir.

Allowing centers c_S, widening w_S sublinearly in eta, or allowing compact
families of finite-energy initial fields does not evade this conclusion.
Widths of order eta, changing kappa with S, spin-dependent input states
without compactness, different graphs with flat bands, Hamiltonian changes,
and different instruments lie outside it. In particular local compensation
is a separate changed-Hamiltonian construction already under review; it is
not ruled out or derived here.

## 7. What remains to be established

The spectral and semigroup arguments above are self-contained given the
source identities and the prepared proof's checked estimates. New controls
are to check (7), the purely Hamiltonian extension, and finite-spin energy
selection on the full physical ring sectors. Numerical sizes cannot prove
(2)–(5) or replace the no-point-spectrum certificate on the cube. No new
microscopic convergence result has yet been claimed for (6) or (10).

The filter is additional supplied physics. To replace it by a finite-resource
reservoir requires a Hamiltonian for that reservoir, its coupling, the energy
offset conventions, and an order-of-limits derivation of the instrument.
The present result supplies a concrete target and a geometry-dependent
constraint on that proposal. It does not select the construction, establish
a spatial field phase, supply an inexhaustible source, or advance a native
TOE claim to retained status.


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
- [prepared_flat_sector_with_electric_dynamics_and_formation_bounded_theorem_note_2026-09-24](PREPARED_FLAT_SECTOR_WITH_ELECTRIC_DYNAMICS_AND_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-24.md): conditional companion source within its stated hypotheses.
- [cube_six_record_rotor_point_spectrum_bounded_theorem_note_2026-09-24](CUBE_SIX_RECORD_ROTOR_POINT_SPECTRUM_BOUNDED_THEOREM_NOTE_2026-09-24.md): conditional companion source within its stated hypotheses.

## Source and verification

Source PR #8845, frozen head `579577555dee1be53055423c046538ff9057e45a`. Original source dispositions and recovery branches are recorded in the combined receipt. Review uses the same primary session without subagents; no separate fix reviewer or formal audit is claimed.

```bash
python3 scripts/energy_filters_and_actual_repeated_formation_2026_09_24.py
```

Fresh controls execute in a temporary directory. Full scientific stdout and generated JSON are included in the authenticated result. Historical diagnostics and deferred source remain recoverable from the original branch.
