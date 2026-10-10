---
claim_id: spatial_quantum_collision_realization_bounded_theorem_note_2026-10-09
claim_type: bounded_theorem
claim_scope: "For supplied labelled position-velocity registers, the summed Lindblad generator of separately marked one- and two-register jumps has exact occupation rates and population closure for arbitrary coherences. Fresh ancillary qubits realize a finite gate schedule with an explicit diamond-norm error to the generator. The fixed ordered schedule is controlled by that bound; the carrier, instruments, clock and rates are supplied."
upstream_dependencies:
  - supplied_finite_velocity_collisions_and_gibbs_equilibration_bounded_theorem_note_2026-10-08
runner: scripts/spatial_quantum_collision_realization_2026_10_09.py
---

# Spatial quantum collision realization

**Date:** 2026-10-09

**Type:** bounded_theorem

**Status:** proposed_retained

Current surface status: conditional-support. Independent retained-status audit has not occurred.

**Source baseline:** `17a95e60d85afc246fc7c163adef8869ab3f4194`; continued from `b178e3a5d4c1d1301255596d10ac4e1bc2aeb192`.

**Runner:** [finite controls](../scripts/spatial_quantum_collision_realization_2026_10_09.py).

**Evidence cache:** `logs/runner-cache/spatial_quantum_collision_realization_2026_10_09.txt`.

This note proves an exact quantum population realization of local spatial
transport and collisions, together with a quantitative finite gate
approximation. The [supplied collision contract](SUPPLIED_FINITE_VELOCITY_COLLISIONS_AND_GIBBS_EQUILIBRATION_BOUNDED_THEOREM_NOTE_2026-10-08.md)
fixes the finite reaction set; no persistence or rapid-mixing theorem is used.

The tensor carrier, labelled positions and velocities, separate instruments,
fresh ancillary preparation, rates, clock and schedule are supplied. The
construction defines locality in these supplied spatial labels; its native
one-qubit-per-site realization is a separate physical question.

| Proof obligation | Disposition |
|---|---|
| Local jump definition and collision multiplicity | Proved in Sections 1–2 |
| Population closure for arbitrary coherences and count lumping | Proved in Section 3 |
| Exact ancillary dilation and diamond approximation | Proved in Section 4 |
| Conservation and resource/locality accounting | Established in Sections 2 and 5 |
| Native spatial-qubit encoding and autonomous clock | Open extensions, not asserted by this supplied construction |

## 1. Finite cells, scale convention, and target chain

Fix integers `m>=3`, `N>=1`, let

\[
 X=(\mathbb Z/m\mathbb Z)^3,\quad M=|X|=m^3,\quad
 \ell=2\pi/m,\quad w=m^{-3},\quad \Omega=Nw.
\]

The physical cell labels are `ell x` on the `2pi`-periodic torus. The cell
weight `w` is for **normalized torus measure**; it is not `ell^3`.
Supply `b,c>0`, velocities `V={-1,0,1}^3`, and every distinct conservative
unordered pair exchange

\[
 r:\{i,j\}\leftrightarrow\{k,l\},\qquad
 v_i+v_j=v_k+v_l,\quad |v_i|^2+|v_j|^2=|v_k|^2+|v_l|^2,
\]

with positive equal forward/reverse coefficients `kappa_r`; put
`K=sum_r kappa_r`. There are 288 such exchanges in the source model.
Every nontrivial exchange uses four distinct velocities: a shared species
cancels by momentum, and a repeated input `v,v` would have outputs `v+a,v-a`
with energy excess `2|a|^2`, hence would be trivial. Consequently the products
below require no repeated-input factor or falling factorial.

An occupation state is `n=(n_{x,v})>=0` with `sum n=N`; let `e_{x,v}` denote
its coordinate unit vector, and `nu_{x,r}` the reaction vector confined to
cell `x`. For `v_d!=0` put `s_d(v)=sign(v_d)` and

\[
 \xi_{x,v,d}=e_{x+s_d(v)e_d,v}-e_{x,v},\qquad
 q_{v,d}=b|v_d|/\ell.
\]

The occupation generator is

\[
\begin{split}
 Gg(n)={}&\sum_{x,v,d:v_d\ne0}q_{v,d}n_{x,v}
       [g(n+\xi_{x,v,d})-g(n)]\\
 &+\sum_{x,r}\frac{c\kappa_r}{\Omega}
 \{n_{x,i}n_{x,j}[g(n+\nu_{x,r})-g(n)]
   +n_{x,k}n_{x,l}[g(n-\nu_{x,r})-g(n)]\}.
\end{split}                                                    \tag{1}
\]

Zero-rate transitions are omitted. This finite process is nonexplosive.
Its density is `F_{x,v}=n_{x,v}/Omega`, so `w sum_{x,v} F_{x,v}=1`.
Directly applying (1) to each coordinate gives the exact state-conditional
drift

\[
 GF_{x,v}=\frac b\ell\sum_{d:v_d\ne0}|v_d|
 [F_{x-s_d(v)e_d,v}-F_{x,v}]
 +c\sum_r\kappa_r\nu_{r,v}
 [F_{x,i}F_{x,j}-F_{x,k}F_{x,l}].                  \tag{2}
\]

This is the upwind streaming operator plus local mass-action collisions.
It does not replace `E[F_i F_j]` with `E[F_i]E[F_j]`. In particular it is not
a closed deterministic equation for finite-population expectations.
Setting `b=1/delta`, `c=1/delta^2` gives the requested diffusive scaling.
All jumps preserve the global supplied number, velocity sum, and energy sum.

## 2. Register Hilbert space and actual jump multiplicities

Supply the finite Hilbert space

\[
 \mathcal H=(\mathbb C^{X\times V})^{\otimes N},\qquad
 z=((x_a,v_a))_{a=1}^N,\qquad
 n_{x,v}(z)=\#\{a:(x_a,v_a)=(x,v)\}.
\]

It has dimension `(27M)^N`. The particles are labels in this construction;
no bosonic or fermionic statistics are imposed. Number is fixed. Define the
diagonal global observables `P_d=sum_a (v_a)_d` and
`E=sum_a |v_a|^2`, with no assigned positional energy.

For each `a,x,v,d` with `v_d!=0`, define a one-register partial isometry

\[
 J^{\rm hop}_{a;x,v,d}
 =|x+s_d(v)e_d,v\rangle_a\langle x,v|\otimes I_{\ne a},
 \qquad q_j=b|v_d|/\ell.                            \tag{3}
\]

For every unordered label pair `a<b`, cell `x`, and reaction `r`, put
`A_r={(i,j),(j,i)}`, `B_r={(k,l),(l,k)}`. For each of the **four** choices
`s in A_r`, `t in B_r`, define

\[
\begin{split}
 |x,s\rangle_{ab}&=|x,s_1\rangle_a|x,s_2\rangle_b,\\
 J^{\rm col}_{ab;x,r;s,t}
 &=|x,t\rangle\langle x,s|+|x,s\rangle\langle x,t|,
 \qquad q_j=\gamma_r=\frac{c\kappa_r}{2\Omega},
\end{split}                                                    \tag{4}
\]

with the identity on spectator registers. It is a Hermitian partial
isometry with `J^2=P_j`, the diagonal source/target projection.
Every operator (3)–(4) commutes with each `P_d` and `E`.

The finite supplied Lindblad generator is

\[
 \mathcal L(\rho)=\sum_j q_j\mathcal D[J_j](\rho),\qquad
 \mathcal D[J](\rho)=J\rho J^\dagger-\tfrac12\{J^\dagger J,\rho\}.
                                                               \tag{5}
\]

The sum includes all hop and collision marks above. A configuration `z`
has exactly `n_{x,v}` labels that can execute a specified hop (3).
For the forward direction of a specified collision at `x`, it has exactly
`n_{x,i}n_{x,j}` eligible **unordered label pairs**. Each such pair has one
input orientation once `a<b` is fixed, not two. It has two target arrangements,
one for each assignment of `k,l` to `a,b`. Thus its total forward rate is

\[
 n_{x,i}n_{x,j}\times 2\gamma_r
 =\frac{c\kappa_r}{\Omega}n_{x,i}n_{x,j}.           \tag{6}
\]

The reverse count is identical. No rapid label mixing, independence of
particles, or uniform fiber averaging enters (6). The four marks cover the
two possible existing input orientations and two possible output orientations;
an individual pair activates only two marks in a specified direction.

## 3. Population closure, including arbitrary coherences

Each `J_j` is a partial permutation of the full computational basis: it maps
a subset injectively to basis vectors with coefficient one. Write its source
projection as `P_j=J_j^dagger J_j`, and its partial map as `sigma_j`.
For every diagonal `D_f=diag(f(z))`,

\[
 q_j\mathcal D[J_j]^*(D_f)
 =q_j\operatorname{diag}\bigl(
  1_{\operatorname{dom}\sigma_j}(z)
   [f(\sigma_j z)-f(z)]\bigr).                     \tag{7}
\]

Indeed `P_j` is diagonal and `J_j^dagger D_f J_j` is diagonal because the
map is injective. Therefore the adjoint generator preserves the whole
diagonal algebra. For any initial density matrix, with arbitrary coherences
or entanglement, its populations follow the classical labelled chain obtained
from the marks (3)–(4). The assertion also holds with an untouched quantum
reference; no full dephasing assertion is needed.

Equation (6) and the hop count show that every labelled configuration with
the same occupation has the same total rate to each occupation target. This
is exact strong lumpability: if `Lf(z)=f(n(z))` denotes the lift, the classical
labelled generator `Q` satisfies `Q L=L G`. Power-series expansion, valid in
finite dimension, gives `exp(tQ)L=L exp(tG)`. Consequently the populations of
`exp(t mathcal L)(rho)` have occupation law `mu_rho exp(tG)`, where
`mu_rho(n)=sum_{z:n(z)=n}rho_{zz}`. Initial coherence cannot change this law.

Keeping different collision marks distinct matters. For example,
`J=|t><s_1|+|t><s_2|` has off-diagonal `J^dagger J`; its target gain contains
`rho_{s_1,s_2}+rho_{s_2,s_1}`. That merged operator is not the instrument
specified in (4) and need not close populations. This is an explicit
counterexample to that replacement only, not a general exclusion theorem.

## 4. Fresh-ancilla channel and a finite-step error

For any one of the partial isometries `J=J_j`, rate `q=q_j`, and step `h>0`,
prepare a fresh independent ancilla in `|0>`. Let `P=J^dagger J` and use
the Hermitian system–ancilla coupling

\[
 H_j=i\sqrt q\bigl(J\otimes|1\rangle\langle0|
             -J^\dagger\otimes|0\rangle\langle1|\bigr),\qquad
 W_{j,h}=\exp(-i\sqrt h H_j).
\]

The ancilla phase convention is immaterial to the reduced channel. The
subspaces `ran(P) tensor |0>` and `ran(JJ^dagger) tensor |1>` decompose into
orthogonal two-state rotations, giving exactly

\[
 K_0=I-P+\cos(\sqrt{hq})P,\qquad
 K_1=\sin(\sqrt{hq})J,\qquad
 \Phi_{j,h}(\rho)=K_0\rho K_0^\dagger+K_1\rho K_1^\dagger.
                                                               \tag{8}
\]

`K_0^dagger K_0+K_1^dagger K_1=I`, so this is a channel at every `h`.
Its adjoint sends `D_f` to `D_f` plus the right side of (7) with rate `q`
replaced by the one-gate jump probability `sin^2(sqrt(hq))`. In particular the directed hop has a
forward probability and no reverse probability in that gate. The reverse
term in the Hermitian system–ancilla Hamiltonian acts on an excited ancilla,
which is not the supplied initial ancilla state. A Hermitian system-only
position exchange with a symmetric bath would instead produce reverse hops.

Compose each marked channel once, in any fixed order, to get `Phi_h`.
Put `Lambda=sum_j q_j`. Counting marks, using
`sum_{v,d}|v_d|=54`, gives the deliberately loose but explicit value

\[
\begin{split}
 \Lambda
 &=54NM\frac b\ell+4\binom N2 M\sum_r\gamma_r\\
 &=\frac{54Nb}{w\ell}+\frac{(N-1)cK}{w^2}.
\end{split}                                                    \tag{9}
\]

**Finite-step proposition.** In the diamond norm with no factor one-half,
if `h Lambda<=1/4`, then for all `T>=0`,

\[
 \|\Phi_h^{\lfloor T/h\rfloor}-e^{T\mathcal L}\|_\diamond
 \le \frac83 Th\Lambda^2+2h\Lambda.               \tag{10}
\]

**Proof.** For one gate set `x=hq`, `u=cos(sqrt x)-1`,
`p=sin^2(sqrt x)`. Equation (8) expands as

\[
 \Phi_{j,h}(\rho)=\rho+u(P\rho+\rho P)
                   +u^2P\rho P+pJ\rho J^\dagger.
\]

For `0<=x<=1/4`, Taylor remainder bounds and
`0<=t-sin t<=t^3/6` at `t=sqrt x` give

\[
 |u+x/2|\le x^2/24,\quad u^2\le x^2/4,\quad |p-x|\le x^2/3.
\]

The completely bounded trace norms of `rho->P rho+rho P`,
`rho->P rho P`, and `rho->J rho J^dagger` are at most `2,1,1` respectively.
Thus `||Phi_{j,h}-I-h q D[J]||_diamond<=2x^2/3`.
Writing `B_j=q_j D[J_j]`, we have `||B_j||_diamond<=2q_j`.
The integral remainder

\[
 e^{hB_j}-I-hB_j=\int_0^h(h-s)e^{sB_j}B_j^2\,ds
\]

has norm at most `2h^2 q_j^2`, because its semigroup is CPTP and has diamond
norm one. Hence the local replacement error is at most `8h^2 q_j^2/3`.

All products and partial-sum Lindblad semigroups are contractions. A double
Duhamel integral gives
`||exp(hA)exp(hB)-exp(h(A+B))||<=h^2||[A,B]||/2`
for the successive Lindblad sums used here. Since
`||[B_i,B_j]||<=8q_iq_j`, telescoping the splitting costs at most
`4h^2 sum_{i<j}q_iq_j`. Together the one-macrostep error is at most

\[
 h^2\left[\frac83\sum_jq_j^2+4\sum_{i<j}q_iq_j\right]
 \le\frac83h^2\Lambda^2.
\]

Telescoping `floor(T/h)` steps gives the first term of (10). The leftover
interval of length less than `h` has norm at most
`h||mathcal L||_diamond<=2hLambda`, which gives the second. The proof is
uniform over system states and untouched references. ∎

For completeness, the splitting identity is obtained by differentiating
`F(s)=exp((h-s)(A+B)) exp(sA) exp(sB)`. Its derivative contains
`exp(sA)B-B exp(sA)=integral_0^s exp((s-u)A)[A,B]exp(uA) du`.
Every semigroup factor is contractive; integrating the triangle
`0<=u<=s<=h` yields the stated factor `h^2/2`.

For any occupation observable `f` and any density matrix `rho`, (7)–(10)
therefore imply

\[
\left|\operatorname{Tr}\bigl(\Phi_h^{\lfloor T/h\rfloor}(\rho)
                 D_{f\circ n}\bigr)
       -\sum_n\mu_\rho(n)(e^{TG}f)(n)\right|
 \le\|f\|_\infty\left[\frac83Th\Lambda^2+2h\Lambda\right].       \tag{11}
\]

Each finite gate closes labelled populations, but the fixed register-specific
schedule generally breaks permutation symmetry during the macrostep. No exact
finite-step occupation lumping is asserted. The exact lumping in Section 3
belongs to the summed generator; (11) is the controlled finite-step result.
Applying the occupation measurement as a channel also bounds total-variation
distance between its finite-step and target occupation laws by
`(4/3) T h Lambda^2+h Lambda`, using the conventional factor one-half in total
variation. This compares distributions even though the finite-step occupation
sequence need not be Markov by itself.

At `b=delta^-1`, `c=delta^-2`,

\[
 \Lambda=\frac{54N}{\delta w\ell}
               +\frac{(N-1)K}{\delta^2w^2}.        \tag{12}
\]

For any desired finite positive error `eta`, one may choose the gate step
last, after `N,m,delta,T`, with

\[
 0<h\le\min\left\{\frac1{4\Lambda},
       \frac\eta{(8/3)T\Lambda^2+2\Lambda}\right\}.
\]

This exhibits a controlled finite approximation. It does not assert uniform
resources, coupling strength, or gate complexity as those parameters scale.

## 5. Supplied locality and physical boundaries

In particle-register support, hops act on one register and collisions on two.
In the supplied spatial labels, a hop joins adjacent cells in its velocity's
coordinate direction, and each reaction acts only at one cell. However, the
Hilbert tensor factors are particle labels, not native spatial qubits. All
label pairs must be addressable under the same-cell projector. Calling these
operators nearest-neighbor interactions on an actual one-qubit-per-site
`M_2` carrier would require a separate encoding and realization proof.

The construction supplies independently marked instruments. It also supplies
directional ancilla preparation, an ordered schedule, a clock, and rate
coefficients. If there are `J` marks, allotting each duration `h/J` with
Hamiltonian `(J/sqrt h) H_j` realizes (8) within a macrostep of duration `h`.
This has singular coupling as `h->0`. A finite run uses
`J floor(T/h)` fresh ancillas, or an explicitly supplied reset apparatus.
Tracing an ancilla, or retaining it permanently without further interaction,
gives the same reduced channel. Reuse without reset is not assumed.

Assigning zero free energy to the ancillas makes each coupling commute with
the supplied global kinetic energy and momentum, since the system endpoints
have equal values. This preserves their full spectral laws for the enlarged
model; it does not account for physical preparation, switching, clock, or
erasure costs. In particular directed transport is a supplied open-system
instrument, not a derivation of an arrow of time from native axioms.

The `N=1` case has no collision gates and the second term of (9) vanishes.
The zero velocity does not hop. Empty inputs do not collide. The restriction
`m>=3` keeps directed neighbors distinct; smaller periodic grids can be handled
with explicit identification of coincident or null hops, but are not used in
the stated theorem. No uniqueness or convergence of the full quantum
stationary state is claimed.

## 6. Exact author discriminator and review scope

The author runner `scripts/spatial_quantum_collision_realization_2026_10_09.py` was executed with Python
3.13.5. It uses only standard-library rational arithmetic and imports no
repository source or data. Reproduce from the repository root with:

```sh
python3 scripts/spatial_quantum_collision_realization_2026_10_09.py
```

The complete baseline output is `logs/runner-cache/spatial_quantum_collision_realization_2026_10_09.txt`; the
complete mutation outputs are the branch-local `SPATIAL_RUNNER_MUTATIONS.txt`. The run checked:

- Two exact `6x6` system–ancilla unitaries, one directed hop and one reversible
  exchange, on all nine system matrix units each. A rational circle point
  `cos(theta)=3/5`, `sin(theta)=4/5` gives exact completeness and population
  closure, including off-diagonal inputs and a spectator state. These are
  exact channel checks; this particular angle is not used as evidence for the
  small-step hypothesis in (10).
- All 4,096 labelled four-particle arrangements of four velocities and two
  occupied cells inside a full `3x3x3` torus, covering 330 occupation fibers.
  The direct per-label/per-pair transition enumeration and the separately
  implemented occupation products agree on 15,920 outgoing occupation targets.
  Streaming destinations outside the two initially occupied cells are kept.
  The census uses `w=1/27`, `Omega=4/27`, `b/ell=7/5`, `c=5/7`, and
  `kappa=11/13`, hence `gamma=1485/728`. A state with `n_i=n_j=2` at one
  cell has forward rate `1485/91`; separating the species gives rate zero.
- The full pair-group enumeration of `V={-1,0,1}^3` gives 288 reversible
  reactions, four distinct species in each, and 54 hop marks per label/cell.
- An exact finite-step counterexample to occupation lumping: order the four
  collision channels as `(s_1,t_1),(s_1,t_2),(s_2,t_1),(s_2,t_2)`, with
  `s_1=(i,j)`, `s_2=(j,i)`, `t_1=(k,l)`, `t_2=(l,k)`. At jump probability
  `p`, the total product-occupation probabilities from `s_1,s_2` differ by
  `-2p^2(1-p)`. At `p=16/25`, they are respectively `8992/15625` and
  `544/625`, despite the same initial occupation. Their first-order rates
  agree, consistently with the generator theorem.
- A merged-source jump has target derivative `1` on the matrix unit `E_01`;
  the separately marked jumps have derivative zero. This directly exposes
  the coherence term that invalidates that replacement.

Four deliberate mutations were run separately and each exited nonzero:
`--mutant gamma` doubles the pair coefficient, `--mutant drop_output` removes
one output arrangement, `--mutant symmetric_hop` inserts backward streaming,
and `--mutant merged_mark` falsely demands population closure of a merged
noninjective mark. They are controls of the discriminator, not additional
physical exclusions.

The finite checks are author controls of the decisive steps, not proofs of
all `N,m` and not independent review. The all-size statements rely on the
displayed algebra and counts. Selective independent review reconstructs normalization (6), the partial-
permutation condition (7), and the Duhamel constants (10). Its source identities
and final packaging confirmation are in the branch-local
`QUANTUM_INDEPENDENT_REVIEW.md`. This is research review, not retained-status
audit. Finite partial-permutation/channel algebra and the diamond-norm
splitting estimate are concrete later Lean targets; no formal run is claimed.


```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Realize spatial collision and transport populations with controlled quantum channels."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Supply and test a native spatial-qubit encoding with autonomous dynamics."
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Finite quantum realization and channel approximation under explicit carrier and instrument choices."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
