---
claim_id: local_quantum_collisions_and_rapid_mixing_bounded_theorem_note_2026-10-09
claim_type: bounded_theorem
claim_scope: "For explicitly supplied finite tensor products of 27-level velocity registers on any connected finite graph, separately marked local exchange Hamiltonians and fresh ancillary qubits converge to quantum collision and interchange channels. Their populations close for arbitrary initial coherences. At each fixed particle count, rapid interchange gives the supplied D3Q27 occupation process with a finite-horizon error bound, and microscopic arrangement multiplicity gives its exact factorial stationary law. Carrier, observable dictionary, interaction, ancillary resources, clock, schedule and scale limits are conditions."
upstream_dependencies:
  - supplied_finite_velocity_collisions_and_gibbs_equilibration_bounded_theorem_note_2026-10-08
  - minimal_axioms
runner: scripts/local_quantum_collisions_and_rapid_mixing_2026_10_09.py
---

# Local quantum collisions and rapid mixing

**Date:** 2026-10-09

**Type:** bounded_theorem

**Status:** proposed_retained

Current surface status: conditional-support. Independent retained-status audit has not occurred.

**Source baseline:** `17a95e60d85afc246fc7c163adef8869ab3f4194`.

**Runner:** [finite controls](../scripts/local_quantum_collisions_and_rapid_mixing_2026_10_09.py).

**Evidence cache:** `logs/runner-cache/local_quantum_collisions_and_rapid_mixing_2026_10_09.txt`.

The [supplied finite-velocity collision model](SUPPLIED_FINITE_VELOCITY_COLLISIONS_AND_GIBBS_EQUILIBRATION_BOUNDED_THEOREM_NOTE_2026-10-08.md)
has collision rates proportional to the product of two input occupation
numbers. This note constructs a local quantum register model whose populations
give those rates in a controlled rapid-mixing limit. Counting microscopic
arrangements also gives the factorial equilibrium weights. The interaction
operators contain no occupation-dependent matrix elements.

The tensor product, velocity registers, assigned observables, separate
interaction marks, fresh ancillary preparation, schedule and clock are
supplied mathematical conditions. Their identification with the one-qubit
`Z^3` framework remains open. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
and current approved scale, kinetic-isotropy and realized-state primitives
are respected within their stated scope; none is enlarged here. Register
encoding into physical qubits would require its own physical realization
argument. The result concerns a finite collision process; streaming,
continuum kinetics and simultaneous large-volume limits require additional
work.

## 1. Model and target

Let `V={-1,0,1}^3`. A reversible reaction `r={i,j}<->{k,l}` consists of
distinct unordered pairs with

\[
v_i+v_j=v_k+v_l,\qquad |v_i|^2+|v_j|^2=|v_k|^2+|v_l|^2.
\]

Include all such reactions and let `kappa_r>0`. Every nontrivial reaction
uses four distinct species. Shared input/output species cancel by momentum
conservation. For an input `(v,v)`, writing the output `(v+w,v-w)` makes
energy conservation `2|w|^2=0`. These observations exclude repeated-species
factors. There are 288 reversible reactions. Put
`nu_r=e_k+e_l-e_i-e_j` and `K=sum_r kappa_r`.

For `N>=2`, choose any connected finite simple graph `G=(X,E)` with
`|X|=N` and `m=|E|>0`. Supply

\[
\mathcal H=(\mathbb C^{27})^{\otimes X},\qquad z\in V^X,
\qquad n_v(z)=\#\{x:z_x=v\}.
\]

The graph may be a finite nearest-neighbor subgraph of `Z^3`. It describes
interaction and mixing slots. A label `v` does not determine the displacement
of its register across this graph: the interchange operation below swaps any
labels. A streaming position space and a rule `x -> x+v dt` are separate
physical identifications. The register counts also have no assumed
identification with permanent framework Record contents.

Supply commuting diagonal observables
`P_d=sum_x diag(v_d)_x` and `E_kin=sum_x diag(|v|^2)_x`. Total number is the
fixed number `N` of register slots. The target occupation generator is

\[
G_N f(n)=\sum_r\frac{\kappa_r}{N}\left[
n_i n_j\{f(n+\nu_r)-f(n)\}
+n_k n_l\{f(n-\nu_r)-f(n)\}\right],                 \tag{1}
\]

on `Omega_N={n>=0:sum_v n_v=N}`, omitting zero-rate terms.

## 2. Local quantum interactions and their controlled limit

Orient each graph edge for notation. For each reaction define
`A_r={(i,j),(j,i)}` and `B_r={(k,l),(l,k)}`. For each of the four choices
`s in A_r`, `t in B_r`, define on its two registers

\[
F_{xy;r;s,t}=|t\rangle\langle s|+|s\rangle\langle t|,
\qquad \gamma_r=\frac{\kappa_r(N-1)}{4m}.            \tag{2}
\]

The operator is Hermitian, with square the projection onto the two displayed
pair states. It commutes with every `P_d` and `E_kin`. Let `U_xy` be the
full register SWAP; it is a Hermitian unitary preserving the same observables.

Fix `epsilon>0`. For each operator `A=sqrt(gamma_r)F` or
`A=epsilon^(-1/2)U_xy`, supply a fresh independent ancillary qubit in
`|0_z>`, apply `W_h=exp(-i sqrt(h) A tensor X_anc)`, and retain that ancilla
without further interaction, or trace it out. Its reduced channel is exactly

\[
\Phi_{A,h}(\rho)=\cos(\sqrt h A)\rho\cos(\sqrt h A)
                 +\sin(\sqrt h A)\rho\sin(\sqrt h A).          \tag{3}
\]

This follows by taking the two ancilla matrix entries of `W_h`. Kraus
completeness is the identity `cos^2+sin^2=I`. In the two-state support of
`F`, the exchange probability is `sin^2(sqrt(h gamma_r))`. The outside
subspace is unchanged. Different operators and time steps use different
ancillas. This distinction is a condition on the interaction model.

Compose all these channels once per macrostep in any fixed order to obtain
`Phi_h`. At fixed graph and `epsilon`, its generator limit is

\[
\mathcal L_\epsilon\rho=
\epsilon^{-1}\sum_{xy\in E}(U_{xy}\rho U_{xy}-\rho)
+\sum_{xy,r,s,t}\gamma_r\mathcal D[F_{xy;r;s,t}](\rho),
\quad
\mathcal D[F](\rho)=F\rho F-\tfrac12\{F^2,\rho\}.     \tag{4}
\]

**Proposition 1 (channel bound).** Set
`Lambda=m/epsilon+(N-1)K`. If `h Lambda<=1/4`, then, in diamond norm,

\[
\|\Phi_h^{\lfloor T/h\rfloor}-e^{T\mathcal L_\epsilon}\|_\diamond
\le 8Th\Lambda^2+2h\Lambda\qquad(T\ge0).             \tag{5}
\]

The convention for trace/diamond norm includes no factor one-half.

**Proof.** For one `A`, write `a=||A||` and `ad_A(rho)=[A,rho]`.
Equation (3) is `cos(sqrt(h) ad_A)`, while
`D[A]=-ad_A^2/2`. Since `||ad_A||_diamond<=2a`, the cosine remainder after
`I-h ad_A^2/2` is at most
`(2/3)h^2 a^4 exp(2 sqrt(h)a)`. The exponential remainder after
`I+h D[A]` is at most `2h^2 a^4 exp(2h a^2)`. For `h a^2<=1/4`, their
sum is less than `6h^2 a^4`.

Every local channel and Lindblad semigroup is completely trace-norm
contractive. Telescoping the local replacements costs at most
`6h^2 sum_A a^4`. A double Duhamel integral for two bounded generators
`B,C`, whose individual and summed semigroups are contractive, bounds
`||e^{hB}e^{hC}-e^{h(B+C)}||` by `h^2||[B,C]||/2`.
For the successive generators `D[A]`, use
`||D[A]||_diamond<=2a^2`. Summing this splitting bound costs at most
`4h^2 sum_{A<B} a^2 b^2 <=2h^2(sum_A a^2)^2`.
Here `sum_A a^2=m/epsilon+4m sum_r gamma_r=Lambda`.
Thus one step differs from `exp(h L_epsilon)` by at most `8h^2 Lambda^2`.
Telescoping the steps gives `8Th Lambda^2`; the final time remainder is
at most `h||L_epsilon||_diamond<=2h Lambda`. ∎

An exact time convention realizes these gates within the macrostep. If
there are `J` gates, give each duration `h/J` and Hamiltonian
`(J/sqrt(h)) A tensor X_anc`. The total duration is `h`. The singular
coupling scaling, growing schedule and fresh resource supply are explicit.
Taking the ancillary free Hamiltonian to be zero makes every gate commute
with the supplied total energy and momentum; their full spectral laws are
conserved. Physical preparation, switching and control costs require a
separate apparatus account.

## 3. Population closure and rapid interchange

For a diagonal register observable `D_g=diag(g(z))`, conjugation by a SWAP
permutes its entries. For one `F` in (2), `D[F]^*D_g` has diagonal entry
`g(z with pair t)-g(z)` on the pair `s`, the reverse on `t`, and zero
elsewhere. The spectator-register entries remain fixed. The diagonal algebra
is consequently invariant under the adjoint of (4), and also under each
finite-step channel (3).

Therefore, for **every** initial density matrix, including arbitrary
coherences and entanglement, its diagonal probabilities evolve as the
finite-state chain with backward generator

\[
Q_\epsilon=\epsilon^{-1}S+C.                          \tag{6}
\]

Here `S` interchanges the two labels across each graph edge at rate one;
`C` exchanges each ordered pair `s<->t` in (2) at rate `gamma_r`.
An edge carrying `{i,j}` has total forward reaction rate `2 gamma_r`.
This conclusion concerns populations; it does not require the full
density matrix to become diagonal. The proof also applies with an
untouched quantum reference.

Let `F_n={z:n(z)=n}` and let `P` average functions uniformly on each
fiber. Connected-graph transpositions generate all permutations of the
vertices, so `S` is irreducible on each `F_n`. Symmetry gives its uniform
stationary law. Direct counting yields

\[
|F_n|=\frac{N!}{\prod_v n_v!},\qquad
\Pr(z_x=i,z_y=j\mid n)=\frac{n_i n_j}{N(N-1)}\quad(i\ne j).    \tag{7}
\]

This is sampling without replacement, with no independence hypothesis.
Two input orientations and two output arrangements give the averaged
forward reaction intensity

\[
m\frac{2n_i n_j}{N(N-1)}\,2\gamma_r
=\frac{\kappa_r n_i n_j}{N}.                         \tag{8}
\]

The reverse computation is identical. Thus `PCP` on functions of `n`
is exactly the target generator (1).

**Theorem 2 (fixed-count averaging).** In the sup norm on functions of
`z`, put

\[
R=\int_0^\infty(e^{tS}-P)\,dt,\quad B=\|R\|_\infty,
\quad c=\|C\|_\infty\le(N-1)K.
\]

For every `f=Pf` and `0<=t<=T`,

\[
\|e^{tQ_\epsilon}f-e^{tPCP}f\|_\infty
\le 2\epsilon Bc(1+Tc)\|f\|_\infty.                 \tag{9}
\]

**Proof.** The finite symmetric generator `S` has kernel `ran P` and
strictly negative spectrum on its complement. The integral exists and
`SR=-(I-P)`, `RP=PR=0`. If `lambda` is the smallest positive eigenvalue of
`-S` across nonconstant fibers, the loose bound `B<=sqrt(27^N)/lambda`
follows from its Euclidean spectral bound and norm comparison. Only
finiteness at each fixed graph and count is needed.

Set `u(t)=exp(tPCP)f`, a Markov contraction on fiber-constant functions,
and `v(t)=u(t)+epsilon RCu(t)`. Then

\[
Q_\epsilon v=PCu+\epsilon CRCu,\qquad
v'=PCu+\epsilon RCPCu.
\]

Initial and final corrector terms each cost at most
`epsilon Bc||f||`; the integrated residual costs at most
`2epsilon T Bc^2||f||`, since `exp(tQ_epsilon)` is contractive. Duhamel's
formula gives (9). Finally the collision exit rate at any configuration is
at most `sum_edges,r 2gamma_r=(N-1)K/2`; the generator sup norm is at
most twice that exit rate. ∎

Combining (5) and (9) gives, for a count observable `f`, its lift
`f_tilde(z)=f(n(z))`, and every density matrix `rho`,

\[
\left|\operatorname{Tr}(\Phi_h^{\lfloor T/h\rfloor}(\rho)D_{\widetilde f})
-\sum_z\rho_{zz}(e^{TG_N}f)(n(z))\right|
\le \|f\|_\infty\left[8Th\Lambda^2+2h\Lambda
                +2\epsilon Bc(1+Tc)\right].          \tag{10}
\]

The controlled order is `h->0` at fixed `N,G,epsilon`, then `epsilon->0`
at fixed `N,G`. A subsequent increasing-count or volume limit needs
corresponding uniform estimates or an explicit choice of `h_N,epsilon_N`.
The constants here are not claimed uniform in those limits. Fast mixing
can remove spatial variation; this theorem does not identify the graph
with physical streaming space.

## 4. Equilibrium and boundary cases

**Proposition 3 (arrangement equilibrium).** For every finite
`epsilon>0`, the stationary occupation law of the microscopic population
chain on the lift of any communicating component `C_N` of (1) is

\[
\pi_{C_N}(n)=Z_{C_N}^{-1}\prod_v\frac{q_v^{n_v}}{n_v!},
\quad q_v=\exp(\alpha+u\cdot v-\beta|v|^2),          \tag{11}
\]

for any real `alpha,u,beta`.

**Proof.** Every microscopic transition in `S` and `C` has equal reverse
rate, so the uniform law is reversible on every microscopic component.
Each occupation component lifts to one microscopic component: swaps
connect every fiber, and can place any available reacting pair on an
edge before a collision. Conversely all microscopic edges project either
to an occupation collision or to no count change. Uniform microscopic
weight pushes forward to `|F_n|`, hence to `1/prod n_v!` by (7).
The multiplier `prod q_v^{n_v}` is constant on the component by the five
conserved moments, giving (11). Finite irreducibility gives uniqueness
for the classical population chain on that component. ∎

This does not assert uniqueness of the full quantum stationary state,
nor classify components solely by their five integer moments. Empty
input species give zero rate. Repeated occupancy of an output velocity
uses different registers and is allowed. The proof covers every
`n in Omega_N` and every finite `N>=2`. For `N=1` use no collisions;
the occupation generator is zero. `N=0` is outside (1). At `N=2` one
edge has `gamma_r=kappa_r/4` and two output arrangements, giving the
required rate `kappa_r/2`.

The normalization (2) intentionally matches supplied `kappa_r` using
`N,m`. With fixed local `gamma_r` instead, the effective coefficient is
`kappa_{r,N}=4m gamma_r/(N-1)`. On an open cubic box of side `L>=2`,
`N=L^3`, `m=3L^2(L-1)`, so fixed `gamma_r=kappa_r/12` gives
`kappa_{r,N}=kappa_r L^2/(L^2+L+1)`. Its coefficient approaches `kappa_r`;
the other scale limits still need the bounds stated above. A covariant
choice of velocity rates may be made constant on proper-cubic reaction
orbits. The finite census finds 19 such orbits; no rate values are selected.

## 5. Finite evidence and scope

The runner uses the Python standard library and no repository or external
input data. It declares `AUDIT_TIMEOUT_SEC=120`. Reproduce with:

```bash
python3 scripts/local_quantum_collisions_and_rapid_mixing_2026_10_09.py
```

The cache envelope separately binds the runner and the two declared
`AUDIT_INPUT_PATHS`: this note and the supplied-collision parent. Those
identity reads are performed by the cache tool; the runner computes its
finite model without reading either note.

Its exact enumeration checks all D3Q27 reaction supports, all 24 proper
cubic rotations, and rational fiber averages on paths with `N=2,...,6`
plus an `N=4` square: 240 fibers and 5,712 arrangements. It checks
factorial weights by direct arrangement counts and detailed-balance
ratios. The actual six-dimensional system-plus-ancilla unitary is
checked on all nine matrix units of a three-state system, including
off-diagonal inputs. This tests the population-closure step.

A separate 36-state four-slot path example uses the reaction
`{+x,-x}<->{+y,-y}` with `kappa=1`. Its three occupation classes are
`(2,2,0,0)`, `(1,1,1,1)`, `(0,0,2,2)`. At `t=1` from `(i,i,j,j)`,
the total-variation errors relative to (1) for
`epsilon=1,1/4,1/16,1/64,1/128` are respectively
`0.121481489`, `0.0400839585`, `0.00991848163`, `0.00246091328`,
`0.00122872639`. The local chain is evaluated by Poisson uniformization;
the target three-state probabilities are separately evaluated by an
analytic eigenmode formula and generator uniformization. Each series
uses a tail bound below `1e-15`. Floating roundoff is not interval-certified.
The configurations `(i,i,j,j)` and `(i,j,i,j)` have immediate forward
rates `1/2` and `3/2`, illustrating the finite mixing data that (9)
averages. These are finite positive calculations, not a general exclusion
of other microscopic mechanisms.

The analytic arguments establish the all-count and fixed-graph limits;
finite controls alone do not establish those quantifiers. The runner
has four check groups, all passing in the captured run. Seven author
mutation controls were detected with nonzero results. They target the coupling
normalization, output multiplicity, reverse transitions, environmental
index, mixing scale and factorial weights. Independent review and audit
remain separate steps.

Binary quantum collision models and repeated-interaction limits have
established precedents: [Carlen, Carvalho and Loss](https://arxiv.org/abs/1804.10280v2)
and [Attal and Pautrat](https://arxiv.org/abs/math-ph/0311002v2).
Their abstracts were inspected for context. No theorem from those papers
is used to supply a missing hypothesis here; the finite proofs above are
self-contained. No novelty claim for these general methods is made.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
target_claim_id: null
target_blocker_text: "Construct microscopic dynamics realizing the supplied finite-velocity collision law."
source_of_blocker_text: user_goal
artifact_role: theorem
next_trace_action: "Calculate an actual native carrier channel and its observable dictionary."
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Local quantum channels and finite-state averaging with explicitly supplied physical interfaces."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
