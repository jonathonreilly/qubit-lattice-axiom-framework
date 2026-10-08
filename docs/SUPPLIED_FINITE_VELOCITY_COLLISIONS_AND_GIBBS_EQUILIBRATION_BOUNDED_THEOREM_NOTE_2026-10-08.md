---
claim_id: supplied_finite_velocity_collisions_and_gibbs_equilibration_bounded_theorem_note_2026-10-08
claim_type: bounded_theorem
claim_scope: "Supplied D3Q27 reversible mass-action collisions with every allowed pair exchange present and fixed positive equal forward/reverse rates. Exactly five additive invariants; unique global positive ODE trajectories; a unique positive Gibbs equilibrium per positive compatibility class; convergence using accepted initial-state-dependent mass-action persistence. The finite occupation process has exact drift, quadratic variation and conditional factorial-Gibbs stationary laws, and a fixed-velocity finite-horizon mean-square LLN uniform in particle number. No velocity refinement, continuum kinetic equation, native dynamics or physical clock is identified."
upstream_dependencies: []
runner: scripts/supplied_finite_velocity_collisions_and_gibbs_equilibration_2026_10_08.py
---

# Supplied finite velocity collisions and Gibbs equilibration

**Date:** 2026-10-08

**Type:** bounded_theorem

**Status:** conditional-support; proposed mathematical support, unaudited.

**Source baseline:** `ed04ee2736b5bddb4e9064966505e3c3dfe003de`.

**Runner:** [exact finite checks](../scripts/supplied_finite_velocity_collisions_and_gibbs_equilibration_2026_10_08.py).

**Evidence:** [content-pinned output](../logs/runner-cache/supplied_finite_velocity_collisions_and_gibbs_equilibration_2026_10_08.txt).

The supplied model below has exactly five additive collision invariants:
number, three momentum components and energy. Its 27 velocities have 288
reversible collision pairs.
Every positive concentration trajectory converges to the unique positive
Gibbs state with the same five conserved moments. A finite population jump
process implements the same conditional drift and converges to that ODE on
any fixed time interval as particle number grows, with an explicit error bound.

The velocities, energy, reactions and rates are supplied mathematical data.
They are not identified with immutable record content or selected by the
framework axioms. This is a finite model for a kinetic comparison. It establishes
neither a Boltzmann–Grad limit nor a hydrodynamic limit. The general convergence
of detailed-balanced mass-action systems has prior mathematical routes; this
note does not claim that result as new or family 149 as uniquely necessary.
The contribution here is the complete finite collision contract, its matching
import, exact certificates and finite-population error estimate.

## 1. Model and accepted mathematical input

Let `V={-1,0,1}^3`, in lexicographic order, and let `e_v` denote the coordinate
vector of species `v` in `R^27`. Its assigned one-particle energy is `|v|^2`.
An unordered pair permits repetitions. Declare two **distinct** pairs
`a={i,j}` and `b={k,l}` to be collision partners exactly when

\[
v_i+v_j=v_k+v_l,\qquad
|v_i|^2+|v_j|^2=|v_k|^2+|v_l|^2.
\tag{1}
\]

Include **every** such pair exchange, in both directions. Give each reversible
pair `r` one fixed number `kappa_r>0`, used in both directions. Rates may differ
between pairs. Choose an arbitrary orientation and write

\[
\nu_r=e_k+e_l-e_i-e_j,\quad
x_r(f)=f_i f_j,\quad y_r(f)=f_k f_l,\qquad
F(f)=\sum_r\kappa_r\nu_r\bigl(x_r(f)-y_r(f)\bigr).
\tag{2}
\]

The concentration equation is `dot f=F(f)`. Time has the units supplied by
these rates. The count of distinct unordered pair-complexes is 378; the
construction has 288 reversible pairs, or 576 directed reactions.

Every nontrivial collision uses four distinct species. If the two pairs share
one velocity, momentum conservation makes the other velocities equal, contrary
to distinctness. If an input is `(v,v)`, momentum gives output `(v+w,v-w)`;
energy conservation gives `2|w|^2=0`, again the same pair. In particular there
is no repeated-species combinatorial factor in (2).

Write `A` for the five-row matrix whose column at `v` is
`(1,v_x,v_y,v_z,|v|^2)^T`, and `S=span_R{nu_r}`. For positive `f^0` set

\[
P=(f^0+S)\cap(0,\infty)^{27},\qquad M=\sum_v f_v^0>0.
\tag{3}
\]

The accepted external mathematical input is OpenAI/math family 149's
**initial-state-dependent boundedness and persistence theorem** at commit
`adc7f1241b42e322a6451854ab7e4b4c146bf78a`:

> For any finite weakly reversible mass-action network of positive dimension,
> fixed strictly positive reaction rates, and strictly positive initial state,
> a global forward solution exists and all global forward solutions from that
> state have every coordinate between some `epsilon` and `epsilon^-1` for all
> nonnegative times, with `0<epsilon<1`.

This is a paraphrase of the production theorem
[`OAI.Problem326.global_bounded_persistent_solution`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Analysis/MassAction/Main.lean#L73).
Its [production definitions](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Analysis/MassAction/Model.lean#L9)
use finite complexes in `N^d`, finite directed nontrivial reactions, return
paths for weak reversibility, and the monomial vector field in (2). The
[comparator mapping](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/MassAction.json)
names that production theorem and permits `propext`, `Quot.sound` and
`Classical.choice`. The accompanying [scope description](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/149.md)
identifies the September 25 boundedness/persistence result. The challenge
statement's placeholder is not the production proof.

Matching OpenAI Lean verification is accepted mathematical import support
for this packet. Another full external build or independent reconstruction
is not a prerequisite. The stronger October 5
common absorbing set for an entire positive compatibility class is not needed
and is not included in this Lean-supported import. The epsilon here may depend
on the initial state. The production definitions and theorem statement were
read and matched, not merely inferred from the catalogue title.

All import hypotheses are met: dimension 27, finite integer pair-complexes,
both directions of every reaction, positive fixed rates, and positive `f^0`.
We also use finite-dimensional ODE existence/uniqueness and continuation,
finite-dimensional compactness and convex optimization, finite-state jump
martingales, the martingale L2 maximal inequality and Gronwall's inequality.
Their objects and uses are specified below. None is a framework physics premise.

## 2. Exactly five additive collision invariants

**Proposition 1.** A function `h:V->R` satisfies
`h_i+h_j=h_k+h_l` for every collision (1) if and only if

\[
h(v)=\alpha+u\cdot v+\theta|v|^2
\quad(\alpha,\theta\in\mathbb R,\ u\in\mathbb R^3).
\tag{4}
\]

Consequently `S=ker A`, `rank A=5` and `dim S=22`.

**Proof.** Any coordinate rectangle supplies a collision: for example
`(x,y,z),(x',y',z) <-> (x,y',z),(x',y,z)` preserves both moments in (1).
Degenerate rectangles give the same identity tautologically. The invariant
condition therefore gives all mixed coordinate differences equal to zero.
Taking one coordinate at a time relative to the origin yields

\[
h(x,y,z)=h(x,0,0)+h(0,y,0)+h(0,0,z)-2h(0,0,0).
\]

A function on `{-1,0,1}` is a polynomial of degree at most two. Thus
`h=alpha+sum_d(u_d v_d+theta_d v_d^2)`. Write `a_x=(1,0,0)`,
`a_y=(0,1,0)` and `a_z=(0,0,1)` for the velocity-space unit axes.
The collision `{a_x,-a_x}<->{a_y,-a_y}` forces `theta_x=theta_y`, and the
corresponding x/z collision forces `theta_x=theta_z`. This proves (4). Conversely each
function in (4) is preserved by (1). The five displayed functions are linearly
independent: evaluate at zero and at the positive and negative coordinate
axes. Hence the annihilator of `S` is exactly their span. ∎

The runner checks every coordinate rectangle, the axis-pair collisions and
all 1,440 row-column conservation identities. Independently, modular elimination
selects a 22-by-22 stoichiometric minor, whose determinant is then computed
by integer Bareiss elimination: it is `-1`. A five-by-five invariant minor has
determinant `2`. The complete row/column indices are printed in the cache.
The analytic proof establishes the invariant classification; the exact minors
provide a second finite certificate.

## 3. Positive trajectories and their Gibbs limit

**Proposition 2.** Every strictly positive `f^0` has a unique global solution
in `P`, and all five moments `Af(t)` are constant.

**Proof.** The vector field is polynomial, hence locally Lipschitz.
`A nu_r=0` proves conservation, including total mass `M`. While the solution
is positive, every coordinate is at most `M`. Put `K=sum_r kappa_r`. Each loss
term involving species `i` contains `f_i` times a partner concentration;
therefore `F_i(f)>=-MK f_i`. Integration gives
`f_i(t)>=f_i(0) exp(-MKt)` on any finite interval in that region. Thus no
coordinate reaches zero at a finite endpoint. The mass bound places the
solution in a compact box on every finite interval, so the local ODE continues
for all positive time. Local uniqueness gives global uniqueness. ∎

Define the continuous entropy functional on the nonnegative orthant by

\[
H(f)=\sum_v f_v(\log f_v-1),\qquad 0\log0=0.
\tag{5}
\]

**Proposition 3.** There is exactly one positive equilibrium in `P`. It is
the unique minimizer of `H` over `{f>=0:Af=Af^0}` and has the form

\[
f_v^*=\exp(\alpha+u\cdot v-\beta|v|^2),
\qquad \alpha,\beta\in\mathbb R,\quad u\in\mathbb R^3.
\tag{6}
\]

The parameter `beta` is not restricted to be positive. No physical temperature
identification is asserted.

**Proof.** The feasible set is closed, nonempty and compact, by the fixed
positive total mass. It contains the strictly positive point `f^0`. Continuity
and strict convexity of `H` give a unique minimizer. If a minimizer `q` has a
zero coordinate, move along the feasible segment `(1-epsilon)q+epsilon f^0`.
The contribution of the zero coordinates to the entropy difference is
`epsilon log(epsilon) sum_{q_i=0} f_i^0+O(epsilon)`; the positive coordinates
contribute `O(epsilon)`. For sufficiently small positive epsilon the difference
is negative, a contradiction. The minimizer is therefore positive. Its
first-order derivative `log f^*` annihilates `ker A=S`, so Proposition 1 gives
(6). Each collision has `f_i^* f_j^*=f_k^* f_l^*`, hence this state is stationary.

For any positive state, differentiation gives the exact identity

\[
\frac{d}{dt}H(f(t))=-D(f(t)),\qquad
D(f)=\sum_r\kappa_r(x_r-y_r)\log\frac{x_r}{y_r}\ge0.
\tag{7}
\]

Indeed `nu_r dot log f=log(y_r/x_r)`, and the logarithm is strictly increasing.
Equality holds exactly when every pair has `x_r=y_r`, since all rates are
positive. Then `log f` is a collision invariant and has the form (4).
Conversely such a logarithm makes every flux vanish. In particular a positive
stationary state has `D=0`, since its entropy derivative is zero; it is the
unique constrained minimizer already found. ∎

**Theorem 4.** Every strictly positive solution converges to `f^*` as
`t->infinity`.

**Proof.** Apply the accepted persistence theorem after the hypothesis match
in Section 1. For this initial state, the solution lies in a compact positive
box for all nonnegative time. Both `F` and the first derivatives of `D` are
bounded there, so `D(f(t))` is uniformly continuous in time. Equation (7) and
the lower bound for `H` show `integral_0^infinity D(f(t)) dt<infinity`.
A nonnegative uniformly continuous function with finite integral tends to
zero: otherwise separated intervals around infinitely many values bounded
below contribute an infinite integral. Every limit point of the trajectory
therefore has `D=0` and the fixed moments. Proposition 3 identifies that point
as `f^*`. Compactness then forces the whole trajectory to converge. ∎

This proof uses only the imported bound for each initial state, not a common
bound or a rate uniform over the class. It supplies no quantitative
long-time relaxation rate. Detailed-balanced mass-action convergence has
other established mathematical routes; those were not exhausted here.
Family 149 is a sufficient tool for this supplied-model theorem, not a claim
of necessity or novelty for the general convergence result.

## 4. Finite particle process, drift and noise

Fix an integer `N>=1` and the finite state space

\[
\Omega_N=\{n\in\mathbb Z_{\ge0}^{27}:\ \sum_v n_v=N\}.
\]

For each reaction `r`, jump from `n` to `n+nu_r` at rate
`kappa_r n_i n_j/N` and to `n-nu_r` at rate `kappa_r n_k n_l/N`.
A transition with zero rate is omitted. The four species are distinct, so
a positive forward rate guarantees the proposed target has nonnegative
coordinates, and its reverse has positive rate. This defines a finite-state
continuous-time Markov chain with no explosion. Every jump preserves `An`.

Write `f^N=n/N`, so `sum_v f_v^N=1`. The population process therefore
corresponds to the ODE's unit-mass sector; the ODE in Section 3 also permits
other positive total masses. For functions on the finite density grid,

\[
\mathcal L_N\varphi(f)=N\sum_r\kappa_r\left[
 x_r(f)\{\varphi(f+\nu_r/N)-\varphi(f)\}
+y_r(f)\{\varphi(f-\nu_r/N)-\varphi(f)\}\right],
\tag{8}
\]

again omitting zero-rate terms at the boundary.

**Proposition 5.** The process

\[
M^N(t)=f^N(t)-f^N(0)-\int_0^t F(f^N(s))\,ds
\tag{9}
\]

is a square-integrable vector martingale starting at zero. Its predictable
quadratic covariation is

\[
\langle M^N\rangle_t=\frac1N\int_0^t R(f^N(s))\,ds,\qquad
R(f)=\sum_r\kappa_r\nu_r\nu_r^{\mathsf T}(x_r(f)+y_r(f)).
\tag{10}
\]

Thus the martingale `sqrt(N) M^N` has bracket `integral R ds`, and `A R=0`.

**Proof.** Apply (8) to the coordinate functions. Their jump increment is
`+nu_r/N` or `-nu_r/N`, giving conditional drift exactly (2). The bracket is
the sum, over jumps, of rate times the outer product of the jump increment.
Both directions have the same outer product and give the factor `1/N`
in (10). Finiteness of the state space and rates gives square integrability
on finite intervals. Finally `A nu_r=0` term by term. ∎

These formulas describe state-conditional drift. The expectation evolves by
`E F(f^N)`; no replacement by `F(E f^N)` is assumed. The runner compares the coordinate generator to a
separate polynomial drift implementation and checks every entry of (10),
including zero coordinates, at `N=3,36,378`.

**Proposition 6.** Let `C` be any communicating component of `Omega_N`, and
let `q>0` have the Gibbs form (6). The unique stationary law on `C` is

\[
\pi_C(n)=Z_C^{-1}\prod_v\frac{q_v^{n_v}}{n_v!},\qquad n\in C.
\tag{11}
\]

The proof applies separately within each communicating component;
classification of those components is outside the claimed theorem.

**Proof.** For an allowed forward jump `m=n+nu_r`, direct cancellation gives

\[
\frac{\pi_C(m)}{\pi_C(n)}
=\frac{q_kq_l}{q_iq_j}\frac{n_i n_j}{(n_k+1)(n_l+1)}
=\frac{n_i n_j}{m_km_l}.
\]

The two equal rate constants therefore give
`pi_C(n) kappa_r n_i n_j/N=pi_C(m) kappa_r m_k m_l/N`.
This proves detailed balance. Every positive-rate edge has its reverse, so
communicating components are closed. Each is a finite irreducible chain and
has the unique stationary law (11). This includes singleton components, which
can occur for small `N`. ∎

The runner exhausts all 378 states for `N=2` and all 576 directed transitions,
using exact rational factorial-Gibbs weights and nonuniform positive rational
rates. Because reacting `N=2` states have only unit factorials, it also checks
all 288 pair exchanges at `N=4` with source counts `(2,2,0,0)`: the target/source
weight ratio and forward/reverse rate ratio are both four. Omitting factorials
fails this latter control. No arbitrary-`N` connectivity is inferred.

A finite GKLS realization is also immediate on the Hilbert basis `|n>`,
`n in C`: for each allowed directed transition use
`L_mn=sqrt(rate(n,m)) |m><n|`. On diagonal density matrices this gives exactly
the chain above, and `diag(pi_C)` is stationary. Every diagonal conserved
observable `(An)_a` commutes with the jumps, since its endpoint values agree.
This is a supplied finite quantum realization; its state space and dissipative
instruments are extra model data.

## 5. A fixed-velocity finite-horizon law of large numbers

Let `Delta={f>=0:sum_v f_v=1}`, let `f^0` be any fixed strictly positive point
in `Delta`, and let `f(t)` be its ODE solution. For each `N`, allow any random
initial `f^N(0)` on the `N`-particle density grid. No positivity of its individual
coordinates, exact matching of its five moments to `f^0`, or independence
assumption on those coordinates is needed. Put `K=sum_r kappa_r`.

**Theorem 7.** For every finite `T>=0`, in Euclidean norm,

\[
\mathbb E\sup_{0\le t\le T}\|f^N(t)-f(t)\|_2^2
\le 2e^{8KT}\left(
\mathbb E\|f^N(0)-f^0\|_2^2+\frac{4KT}{N}\right).
\tag{12}
\]

The constant is independent of `N` and of the initial grid law. In particular,
mean-square convergence of the initial densities implies mean-square uniform
convergence on each fixed interval. The velocities and all rates are fixed
while `N` tends to infinity.

**Proof.** For `f,g in Delta`, each reaction has four distinct species, and

\[
|x_r(f)-x_r(g)|+|y_r(f)-y_r(g)|
\le |f_i-g_i|+|f_j-g_j|+|f_k-g_k|+|f_l-g_l|
\le2\|f-g\|_2.
\]

Since `||nu_r||_2=2`, (2) gives the Lipschitz bound
`||F(f)-F(g)||_2<=4K||f-g||_2`. For four nonnegative coordinates with sum at
most one,

\[
f_i f_j+f_k f_l\le\tfrac14,
\]

because `4(ab+cd)<=(a+b+c+d)^2`; the difference is
`(a-b)^2+(c-d)^2+2(a+b)(c+d)>=0`. Consequently
`tr R(f)<=K` throughout `Delta`.

The martingale isometry and (10) give
`E||M^N(T)||_2^2=E tr <M^N>_T<=KT/N`. The vector L2 maximal inequality,
applied to its norm, gives
`E sup_{t<=T}||M^N(t)||_2^2<=4KT/N`.
Subtract the ODE integral equation from (9). Pathwise Gronwall gives

\[
\sup_{t\le T}\|f^N(t)-f(t)\|_2
\le e^{4KT}\left(\|f^N(0)-f^0\|_2+
\sup_{t\le T}\|M^N(t)\|_2\right).
\]

Squaring, using `(a+b)^2<=2a^2+2b^2`, and taking expectation proves (12). ∎

This finite-time result does not require the persistence import. That import
is used for the long-time conclusion in Theorem 4. Bound (12) grows with `T`;
it does not exchange the limits `N->infinity` and `t->infinity`. A fluctuation
limit, a limit of stationary laws, a growing velocity mesh and a continuum
Boltzmann equation would each need their own additional argument. The exact
drift and noise in (8)–(10) state a usable interface for those future questions.

## 6. Scope, checks and later audit targets

The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) distinguish supplied update
laws, time metrics and record-production dynamics from axiom content. This
note adopts none of those as new framework premises. Its conserved additive
quantities are defined by this model, not by reinstating finite additivity in
the Record axiom. The existing [finite marked-collision supply note](FINITE_ENERGY_SUPPLY_FOR_MARKED_COLLISION_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md)
is a contextual interface for supplied GKLS dynamics, not a premise selecting
these reactions. The kinetic and fluid open lanes still need physical
identification, an appropriate microscopic law and their respective limits.

Reproduce the exact finite checks with:

```bash
python3 scripts/supplied_finite_velocity_collisions_and_gibbs_equilibration_2026_10_08.py
```

The standalone runner uses only the Python standard library and declares
`AUDIT_TIMEOUT_SEC=120`. It reads no mutable external or off-repo data and
needs no empirical calibration. Its complete output is in the `runner_cache`
envelope linked above. The executed total is `TOTAL: PASS=14 FAIL=0`. The checks
cover network construction, weak reversibility, four-species support, all
conservation identities, rectangle/axis generators, independent exact rank
certificates, rational Gibbs balance, nonuniform rates, exact prime-log entropy
coefficients, a positive nonstationary same-moment witness, the exhaustive
`N=2` chain, nontrivial `N=4` factorial ratios, and the drift/noise constants
used in (12). The analytic arguments
above establish general positivity, minimization and limiting statements;
finite PASS counts are not a substitute for those proofs or an audit verdict.

Concrete later Lean targets for this new packet are:

1. Define `V=Fin 3 -> {-1,0,1}` and the finite reaction relation; prove the
   rectangle/axis invariant classification, `S=ker A`, and exact rank 22.
2. Construct the production `ReactionNetwork 27`, prove its weak reversibility
   and positive rates, and apply the accepted persistence declaration with
   the precise monomial convention in (2).
3. Formalize the entropy derivative, strict positivity of its dissipation
   away from pairwise balance, the interior constrained minimizer, and the
   compact-trajectory convergence proof. This covers the new composition of
   the accepted import with our invariant calculation.
4. Formalize the finite occupation generator, feasibility of jumps, factorial
   detailed balance, the martingale drift and predictable bracket, including
   the `1/N` density normalization and the invariant null directions.
5. Prove the uniform-on-`Delta` Lipschitz and trace bounds and the finite-horizon
   estimate (12) using the vector martingale maximal and Gronwall inequalities.

Those are audit work for our new proofs, not a present claim of a new Lean
formalization. No audit status or citation graph is changed by this note.
Independent review should concentrate on the invariant proof, persistence
hypothesis match, constrained-entropy argument, finite generator normalization
and the quantifiers/constants in (12).

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "Supplied fixed-velocity reversible collision model; mathematical persistence import accepted; new invariant, entropy and finite-population arguments proposed for independent review."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
