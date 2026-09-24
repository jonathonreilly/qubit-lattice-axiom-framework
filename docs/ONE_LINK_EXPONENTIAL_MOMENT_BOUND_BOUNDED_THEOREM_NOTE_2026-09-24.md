---
claim_id: one_link_exponential_moment_bound_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Conditional mathematics of the explicitly supplied finite model and stated limits; numerical controls do not establish physical selection or extend the analytic quantifiers."
upstream_dependencies:
  - minimal_axioms
  - local_pair_form_and_general_graph_magnetic_dynamics_bounded_theorem_note_2026-09-24
  - local_volume_dynamics_with_commuting_electric_terms_bounded_theorem_note_2026-09-24
runner: scripts/one_link_exponential_moment_bound_2026_09_24.py
---

**Type:** bounded_theorem
**Status:** conditional mathematical result; unaudited.

The complete source argument and its selected companion proofs follow, with the narrow corrections documented in the combined review. Dated author-status statements, seals and numerical observations are historical provenance, not audit authority. Quantum spaces, Hamiltonians, instruments, preparations and resource assumptions are supplied mathematical premises. Fresh controls corroborate the proofs within their scope.

# One-link exponential field moments in the compensated target

Root analytic result, September 23, 2026. This is a finite-time theorem for
the **supplied compensated rotor target**, conditional on its already checked
local pair Hamiltonian and actual formation channels. It strengthens the
separate finite-time second-moment candidate for preparations with a
one-link exponential moment. It says nothing about an autonomous formation
energy supply, a microscopic spin-uniform limit, or time-uniform tightness.

## Statement

Let G be a finite simple bipartite graph of maximum degree z, and let
`e=(a,b)` be one oriented link with a in A. The effective A sites always
carry charges +/-1; B sites carry 0,+/-1. Links are integer rotors and
the formation jump is exactly `sqrt(kappa) P j_(a,b,sigma) F_a P`, either
with resolved signs or with their stipulated coherent sum on each marked
edge. The Hamiltonian is

    H_G=K D_G+V_G,
    V_G=-2 delta sum_(a<c sharing B) S_ac^* S_ac,
    S_ac=F_c F_a P.

Take K>0, delta,kappa>=0 and lambda>=0. Define

    C_h=4 delta z^4(z-1),
    R_e=2 kappa z(z-1)^2,
    c_z(lambda)=4 C_h sinh(lambda/2)
                 +12 exp(lambda/2) sinh(lambda/2) R_e.       (1)

For every normal initial density with finite indicated one-link moment,
the exact finite-graph evolution satisfies, separately for s=+1 and -1,

    <exp(s lambda E_e)>_t
       <= exp[c_z(lambda)t] <exp(s lambda E_e)>_0.            (2)

No moments on other links are required; the bound is independent of G's
size and K. The same estimate holds for the local marginal of the checked
infinite target on Z^d, z=2d, from any locally normal initial state with
that one-link exponential moment. For an initial zero field,

    Pr_t(|E_e|>=R) <= 2 exp[-lambda R+c_z(lambda)t]           (3)

for every R>=0 and lambda>0. Equation (3) is a tail bound on the exact
state, uniform over finite induced volumes at each fixed time.

There is also a simple optimized consequence. Put
`A_z=2 C_h+6 R_e=8 delta z^4(z-1)+12 kappa z(z-1)^2`.
Since `c_z(lambda)<=A_z(exp(lambda)-1)`, an initial zero field and
`R>A_z t>0` give

    Pr_t(|E_e|>=R)
       <=2 exp[-R log(R/(A_z t))+R-A_z t].                   (3a)

This Poisson-form Chernoff tail applies to each sign of one link; a finite
set of links gets the sum of their bounds. If `A_z=0`, the zero-field state
keeps that link at zero. This is finite-time local field tightness, not a
uniform-in-time bound.

## Why every local term shifts one link by at most one

A jump first sends an old A record to a B neighbor different from the
marked B site, then forms the new pair on the marked edge. Thus a fixed
link can be the old-hop edge or the marked edge, never both, and each
summand changes its E coordinate by 0 or +/-1. The coherent instrument
only adds the two sign summands; it does not change their shift support.

For a magnetic term, a nonzero path of `S_ac^*S_ac` first emits records
from distinct A sites a,c to distinct vacant B destinations, then returns
one record to c and one to a. A fixed link incident on a can be used by
the outbound and inbound a hops. If they use the same B destination, that
destination still contains a's old charge when it returns: if the c return
had taken that record, the destination would instead be empty and the a
return could not use it. Hence the two shifts cancel. If the link is used
only once, its net change is +/-1. No other factor in the pair term uses
that link because it has a unique A endpoint. This establishes shift
support in `{-1,0,1}` for every physical charge and field word. It closes
the apparent shift-two risk from composing two unit-shift operators;
hard-core occupancy is essential.

The exact control checks this support on all 65 physical matter words,
with a Gauss field for each, in path8, ring8 and cube8, and on all 52
independently reconstructed path7 words. The ring checks two nonzero
circulation translations on every word. Those controls corroborate the
path argument; the argument, not finite sampling, covers other graphs and
all electric translations.

## Weighted generator estimate

The electric D_G is diagonal and strongly commutes with E_e. Only magnetic
pairs containing a can shift E_e; there are at most z(z-1). Since
`||F_a||<=z`, `||S_ac||<=z^2` and `||[E_e,S_ac]||<=z`,

    ||[E_e,V_G]|| <= C_h.                                  (4)

Decompose V_G into link-shift components V_m under conjugation by
`exp(i theta E_e)`. Fourier projection is contractive. As m=0,+/-1 only,
`||V_+1||+||V_-1||<=2||[E_e,V_G]||<=2 C_h`.

Only channels anchored at a can shift E_e. There are at most z marked
edges and two signs. Each resolved channel has norm at most
`sqrt(kappa)(z-1)`. The sign ranges are orthogonal on each marked edge,
so each coherent channel has squared norm at most
`2 kappa(z-1)^2`. In either convention,

    sum_(channels touching e) ||L_mu||^2 <= R_e.            (5)

For a bounded positive invertible diagonal weight W whose adjacent E
ratios lie between `exp(-lambda)` and `exp(lambda)`, set
`B=W^(1/2)LW^(-1/2)` and `C=W^(-1/2)LW^(1/2)`. Since a jump has only link
shifts 0,+/-1, each Fourier component has norm at most ||L|| and

    ||B||<=3 exp(lambda/2)||L||,
    ||B-C||<=4 sinh(lambda/2)||L||.                  (6)

The exact weighted dissipator identity is

    W^(-1/2) D_L^*(W) W^(-1/2)
      =[B^*(B-C)+(B-C)^*B]/2.                       (7)

Its operator norm is at most
`12 exp(lambda/2)sinh(lambda/2)||L||^2`.
The weighted Hamiltonian commutator has norm at most
`2sinh(lambda/2)(||V_+1||+||V_-1||)`, or
`4 C_h sinh(lambda/2)`. Terms not touching e commute with W and do not
enter either estimate. Thus, as a quadratic-form bound,

    L_G^*(W) <= c_z(lambda) W.                        (8)

## Domain and volume passage

For s=+1 use the bounded monotone cutoff
`w_R(E)=exp(lambda min(E,R))`; for s=-1 replace E by -E. Add epsilon I,
epsilon>0, to make it boundedly invertible. Adjacent values of this
weight still have ratios between `exp(-lambda)` and `exp(lambda)`, so
(6)-(8) hold with the *same* c_z, independent of R and epsilon.
The cutoff commutes with D_G; its bounded Heisenberg weak equation is
legitimate for every trace-class input without a full generator-domain
assumption. Gronwall gives (2) for the cutoff. First send epsilon to zero,
then increase R monotonically. The initial cutoff expectation is no more
than the initial exponential expectation, so monotone convergence proves
(2) for unbounded W.

For the infinite target use the uniform finite-volume estimate for each
fixed bounded local `w_R(E_e)`. The checked spatial local-norm convergence
on bounded observables transfers its expectation to a locally normal
state. The finite-volume inequality in fact holds on the full effective
A/B/rotor tensor space: its shift and norm arguments do not require Gauss
at boundary vertices. Thus one can use the ordinary finite-volume
restrictions of an infinite Gauss state without imposing artificial
boundary Gauss constraints. The same cutoff inequality survives; then
increase R. This
argument does not assert norm time continuity of the full rotor algebra,
a global infinite-volume density matrix, or exchange of microscopic and
volume limits. Applying Markov's inequality to the two signs yields (3).

## Verification and limits

The completed exact control found no shift-two output among magnetic and
actual resolved-jump rows in path8, ring8 or cube8, and none in the
independent 52-state path7 matrix. It checked 130 ring circulation
translations and the weighted dissipator identity on a separate exact
five-level matrix with a saturated exponential weight. The control is
source-bound and reproducible; it is not an independent theorem review.

The bound requires a finite initial exponential moment on the observed
link. The earlier second-moment candidate covers some states this theorem
does not. Neither candidate yet has a completed independent review after
the checker usage interruption. At fixed lambda, (2) grows exponentially
with t, so it does not give uniform future field tightness or pointwise
decay of the infinite-volume birth rate. Original-law large-spin formation
outputs may have field scale growing with spin and need not have a
spin-uniform initial exponential moment. A field-only or native physical
identification is not inferred.


## Companion result retained in this unit

# Direct absolute one-link field tail

Root corollary after the blind independent PRE and its comparison suggested
using the same weighted-generator lemma with an absolute-value weight.
The earlier root note `ONE_LINK_EXPONENTIAL_MOMENT_BOUND.md` is left byte
unchanged at SHA-256
`e9665bd438eb597d5163ee458766b0ac686f3060bf7aa828c4b930fbf756aeb3`.
The independent PRE had already proved a coarser absolute-value bound before
seeing that note; its separate comparison is
`local_field_exponential_independent/POST_COMPARISON.md`.

Keep precisely the supplied compensated target, degree bound z and actual
resolved or coherent channels of the root note. Let

    C_h=4 delta z^4(z-1),
    R_e=2 kappa z(z-1)^2,
    c_z(lambda)=4 C_h sinh(lambda/2)
       +12 exp(lambda/2)sinh(lambda/2) R_e.

For any fixed link e, lambda>=0 and finite initial absolute one-link
exponential moment, the finite-graph target satisfies

    <exp(lambda |E_e|)>_t
       <= exp[c_z(lambda)t] <exp(lambda |E_e|)>_0.        (1)

The same holds for a locally normal infinite-volume target state via the
checked bounded-local-observable volume limit, provided its chosen-link
initial moment is finite. This is a finite-time, volume-uniform bound on
the exact target; it imposes no moments on other links.

For the domain passage use
`W_N=exp(lambda min(|E_e|,N))`. It is bounded and boundedly invertible,
commutes strongly with the diagonal electric Hamiltonian, and is monotone
in N. The function `n -> min(|n|,N)` changes by at most one across adjacent
integer fields. Thus every ratio of adjacent W_N eigenvalues lies between
`exp(-lambda)` and `exp(lambda)`. The root weighted Hamiltonian and jump
lemmas apply with exactly the same `c_z(lambda)`, independently of N.
Gronwall on the bounded weak Heisenberg equation followed by monotone
convergence proves (1); no epsilon regularizer is needed for this weight.
The full effective tensor argument also applies before imposing boundary
Gauss constraints when passing to infinite volume.

For an initial zero field, (1) gives the sharper direct tail

    Pr_t(|E_e|>=R) <= exp[-lambda R+c_z(lambda)t].         (2)

Put `A_z=2 C_h+6 R_e`. Since
`c_z(lambda)<=A_z(exp(lambda)-1)`, choosing
`lambda=log(R/(A_z t))` for `R>A_z t>0` gives

    Pr_t(|E_e|>=R)
      <= exp[-R log(R/(A_z t))+R-A_z t].                 (3)

For a finite set of links, sum (2) or (3) over them. If `A_z=0` and the
field begins at zero, it remains zero. The earlier two-sided sum bound with
prefactor two remains valid, but (2)-(3) are stronger because the absolute
weight is controlled directly. Neither result gives all-future tightness,
spin-uniform microscopic preparation, or a physically selected reservoir.


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
- [local_pair_form_and_general_graph_magnetic_dynamics_bounded_theorem_note_2026-09-24](LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md): conditional companion source within its stated hypotheses.
- [local_volume_dynamics_with_commuting_electric_terms_bounded_theorem_note_2026-09-24](LOCAL_VOLUME_DYNAMICS_WITH_COMMUTING_ELECTRIC_TERMS_BOUNDED_THEOREM_NOTE_2026-09-24.md): conditional companion source within its stated hypotheses.

## Source and verification

Source PR #8873, frozen head `a7e3dae5c667e9ba0c9561a9bcf87b0401e21a5a`. Original source dispositions and recovery branches are recorded in the combined receipt. Review uses the same primary session without subagents; no separate fix reviewer or formal audit is claimed.

```bash
python3 scripts/one_link_exponential_moment_bound_2026_09_24.py
```

Fresh controls execute in a temporary directory. Full scientific stdout and generated JSON are included in the authenticated result. Historical diagnostics and deferred source remain recoverable from the original branch.
