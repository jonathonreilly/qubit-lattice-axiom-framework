---
claim_id: current_mass_filter_bounded_theorem_note_2026-10-12
claim_type: bounded_theorem
claim_type_reason: "Complete conditional analytic proof in a supplied model; finite controls and scoped algebra certificate do not establish physical realization."
claim_scope: "Chosen supplied free one-dimensional spin-chain vacuum scaling: actual normalized-current total mass, sharp-window strong convergence iff delta/a^2 diverges, and smooth actual two-flow almost-local odd creators with dense compact one-particle columns. Maximal TOTAL domains and nonuniform locality remain explicit."
upstream_dependencies:
  - concrete_gapped_chain_bounded_theorem_note_2026-10-12
  - gapped_continuum_limit_bounded_theorem_note_2026-10-12
  - gapped_chain_scattering_bounded_theorem_note_2026-10-12
runner: scripts/current_mass_filter_2026_10_12.py
artifact_role: theorem
target_claim_id: null
target_blocker_text: "A sharp spectral projection alone does not establish an almost-local spin observable."
source_of_blocker_text: handoff
next_trace_action: "Compare actual local algebras under the supplied scaling while retaining nonuniform constants and parity limits; no such result is claimed here."
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: "Actual normalized-current mass windows and smooth spin filters in the supplied one-dimensional gapped-chain family"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

**Type:** bounded_theorem


**Publication status:** The frozen source and fresh source review are accepted at conditional-support / bounded_theorem scope without a mathematical correction. Author-era pending-review and “No Lean result is claimed” statements are historical chronology. A later root-authored finite algebra certificate is separately documented below; it does not formalize the surrounding physics. Every original argument remains intact.



# Actual-current mass windows and smooth almost-local spin filters

**Author conditional proof, 2026-10-12; independent review pending.**
The supplied full-spin GNS construction gives a positive joint mass
multiplier made from the actual energy current. A shrinking spectral
window converges strongly to the one-particle projection precisely when
its squared-mass width dominates the lattice error scale. A smooth version,
with an expanding energy cutoff, is realized by smearing the two actual
local spin flows and produces almost-local odd spin creators. No exact
finite-spacing Lorentz Casimir or even-observable one-particle creator is
obtained. The construction is conditional on a chosen free one-dimensional
model, scaling family and state; it supplies no framework or physical
identification of them.

## 1. Contract and exact inputs

Write S for this note's directory. Work is confined to this note and
`S/current_mass_filter/`; root owns all repository, publication and audit
decisions. The four supplied science sources were read in full, including
the complete relevant spin lift, maximal-domain, continuum transport and
creator arguments. Their frozen identities are:

| Source | SHA-256 | Role |
|---|---|---|
| `ROOT_CURRENT_MASS_FILTER_ROUTE.md` | `f58e3483243e6382183e61d8b71c6fbed22befc98aac4c8090fd636ecfdb500f` | Unverified root proposal; root is a coauthor |
| `CONCRETE_GAPPED_CHAIN_PROBE.md` | `0aebc2ded245d9bc9ecae364db0d1a042f9642771ed788794dafd73fb7f621bd` | Actual full-spin GNS operators C21–C29, spin flows, current density and parity |
| `GAPPED_CONTINUUM_LIMIT_PROBE.md` | `617b9a1cbb541d6f207de89c10f1fbb2005fbb27f68e818f0c14a3fe67bf802d` | Specified scaling, interspace maps, actual boost transport and group limit |
| `GAPPED_CHAIN_SCATTERING_PROBE.md` | `92dcdbce72b8bd57fd4b7e4e661a9f9e34e815b312df7f0c6e360cd8ef5c9f92` | Actual odd spin creators S5–S11 and their locality; no scattering conclusion is needed below |

The current workflow was read from the root-designated worktree at HEAD
`358fdf795a5504d4d7fd13344bbbd5df5504ebea`. Its relevant instruction/source
snapshots are preserved. This bounded author task does not fetch, edit that
worktree, open PRs, classify unrelated framework premises, or rerun parent
controls. The approved primitive registry is not a source for this chosen
chain. A bounded source search is preserved; no exhaustive prior-art or
novelty claim is made. The one additional mathematical source inspected is
the locally preserved original NSY arXiv:1810.02428v2 TeX, definitions and
Theorem 3.1, for the finite-range current-flow locality estimate in §6.

Fix m,v>0 and a>0. Use exactly

\[
 g_a-J_a=m/2,\qquad 4g_aJ_a=v^2/a^2,\qquad
 I_a=(-\pi/a,\pi/a),\qquad \mathfrak h_a=L^2(I_a,dq).
 \tag{M1}
\]

The parent identifies the actual full-spin Hilbert space with
\(\mathcal F_a=\mathcal F_-(\mathfrak h_a)\). In these coordinates,

\[
 H_a=d\Gamma(E_a),\quad \Pi_a={a\over v^2}P_{\rm current,a}
       =d\Gamma(p_a),\quad
 E_a=\sqrt{m^2+{4v^2\over a^2}\sin^2(aq/2)},\quad
 p_a={\sin(aq)\over a}.                              \tag{M2}
\]

This p differs by the factor v² from the lowercase p of the continuum
parent. It is normalized actual current, not a logarithm of geometric
translation. The canonical rescaled original boost is

\[
 B_a=d\Gamma(b_a),\quad
 b_a=i(E_a\partial_q+E_a'/2)-aE_a/2,
 \qquad \operatorname{Dom}b_a=H^1_{\rm per}(I_a).       \tag{M3}
\]

Only the parent's stated conditional scope is imported. Its spin/GNS
identification is not independently re-proved by the controls below.

## 2. Joint calculus, positivity, thresholds and full domains

H_a and Pi_a strongly commute: in every n-sector they are multiplication
by the real symmetric functions
\(h=\sum_jE_a(q_j)\), \(p=\sum_jp_a(q_j)\), and their direct-sum
spectral projections commute. Define, by this joint spectral calculus,

\[
 c_{a,n}=h^2-v^2p^2,\quad C_a=M_{c_{a,n}},\quad
 M_a=M_{\sqrt{c_{a,n}}},\quad c_{a,0}=0.                \tag{M4}
\]

All such notation includes the maximal multiplication domain and Hilbert
direct sum: for example Dom C_a consists of Psi with
\(\sum_n\int c_{a,n}^2|\Psi_n|^2<\infty\). Positivity follows from
an all-momenta, all-n calculation, not from an infrared fit:

\[
 d_j:=E_j^2-v^2p_j^2
    =m^2+{4v^2\over a^2}\sin^4(aq_j/2)\ge m^2.         \tag{M5}
\]

For two terms set A=E_iE_j−v²p_i p_j. Since E_l>|vp_l|,
A>0, and direct expansion gives

\[
 A^2-d_i d_j=v^2(E_i p_j-E_j p_i)^2\ge0.
 \tag{M6}
\]

Thus A≥sqrt(d_i d_j). Expanding the square of the totals in M4 yields

\[
 c_{a,n}\ge\left(\sum_j\sqrt{d_j}\right)^2\ge n^2m^2,
 \qquad mN\le M_a\le H_a\le E_{a,\max}N,
 \quad E_{a,\max}=\sqrt{m^2+4v^2/a^2}.                 \tag{M7}
\]

These are pointwise multiplier inequalities and hence their usual form
inequalities on the indicated form domains. In particular, at fixed a,

\[
 \operatorname{Dom}H_a=\operatorname{Dom}M_a=\operatorname{Dom}N,
 \quad \operatorname{Dom}C_a=\operatorname{Dom}H_a^2
                         =\operatorname{Dom}N^2.      \tag{M8}
\]

The equivalences follow by squaring the two-sided multiplier bounds in
the definition of each domain. Also |p|≤h/v implies
Dom H_a²⊂Dom Pi_a². Consequently the algebraic difference
H_a²−v²Pi_a², on its natural intersection domain, actually equals C_a
on Dom N² at this fixed a. This equality is proved here rather than
assumed in the definition. It is not uniform in a. In the continuum
one-particle sector the maximal mass-squared multiplier is the bounded
constant m², while H² has a proper unbounded domain; transferring M8
to that limit would be false. Cancellations in total current also forbid
identifying Dom Pi_a with Dom N without another argument.

The n-particle threshold nm is sharp as an infimum. Antisymmetric
products of n nonzero packets in disjoint intervals arbitrarily near
q=0 approach n²m² in M4. Pauli exclusion removes coincident tuples,
not these disjoint packets. For n≥1 equality c=n²m² can occur only
when every q_j=0, by M5–M7. This is a null set for the continuum
momentum measures used here. In particular the spectral projection of
the two-particle sector at C_a=4m² is zero, though 4m² is in its
spectrum. A squared-mass window extending strictly above 4m² contains
nonzero two-particle vectors: take small distinct momenta near +epsilon
and −epsilon, for which c=4E_a(epsilon)² tends to 4m², and small
disjoint neighborhoods. A window merely ending at 4m² does not leak
two-particle vectors in this representation. An atomic finite-volume
model would require a separate endpoint analysis.

## 3. Sharp windows, necessary scale, and strong versus norm convergence

For 0<delta_a<3m² put

\[
 F_a=\mathbf1_{[m^2,m^2+\delta_a]}(C_a).               \tag{M9}
\]

It annihilates the vacuum and every n≥2 sector exactly. On the
one-particle sector it is the characteristic function of
\(D_a(q)\le\delta_a\), with D_a the nonnegative correction in M5.
If a²delta_a<4v², this is exactly |q|≤Q_a, up to endpoints, where

\[
 Q_a={2\over a}\arcsin\!\left[
              \left({a^2\delta_a\over4v^2}\right)^{1/4}\right].
 \tag{M10}
\]

If that inequality fails the whole one-particle circle is selected.
In either case all packets supported in |q|≤R⊂I_a are fixed when

\[
 {v^2a^2R^4\over4}\le\delta_a,                       \tag{M11}
\]

because |sin x|≤|x|. No packet smoothness is needed for M11.

Let J_a be zero extension from h_a into h=L²(R,dq), let
\(\mathcal I_a=\Gamma_-(J_a)\), and let P1 be the continuum
one-particle projection. Then \(\mathcal I_a^*\mathcal I_a=1\) on the
lattice Fock space and \(\mathcal I_a\mathcal I_a^*=\Gamma(1_{I_a})\)
on the continuum Fock space. These are
isometries and projections, not global unitary identifications.
For delta_a→0,

\[
 \mathcal I_aF_a\mathcal I_a^*\longrightarrow P_1
 \text{ strongly}\quad\Longleftrightarrow\quad
 {\delta_a\over a^2}\longrightarrow\infty.             \tag{M12}
\]

Sufficiency: M11 fixes every compactly supported one-particle vector
eventually, the operators vanish in every other sector, and density
extends convergence using their norm bound one. Necessity: if the
ratio fails to diverge, choose a sequence along which it is bounded
by L. Uniformly on a fixed compact q-set,
D_a(q)/a²→v²q⁴/4. A nonzero packet in a small compact interval with
v²q⁴/4>L+1 is then killed along that sequence, contradicting M12.

More generally, if delta_a/a²→L<infinity, dominated convergence
gives the one-particle limit
\(\mathbf1_{\{|q|\le(4L/v^2)^{1/4}\}}P_1\); for L=0 this is
the zero operator. The endpoint sets are null. Thus delta_a/a²→L with
0<L<infinity retains a proper momentum band, and delta_a=o(a²) loses all
fixed L² packets in the limit. A dimensionally consistent successful
choice is delta_a=m²(am/v)^gamma with 0<gamma<2.

The norm difference from P1 is one for every a after embedding, since
vectors outside I_a are missed. More substantively, for small a a
nonempty part of the one-particle circle lies outside M10; normalized
packets there also witness \(\|F_a-P_{1,a}\|=1\) before embedding.
No full-Fock operator-norm or uniform packet-rate claim follows from M12.

## 4. The actual boost commutator and its bounded-group limit

On the finite-particle smooth periodic common core, C29 of the concrete
parent, with the exact normalizations M2–M3, gives

\[
 [B_a,H_a]=iv^2\Pi_a,\qquad [B_a,\Pi_a]=iT_a,
 \quad T_a=d\Gamma(E_a\cos(aq)),
\]
\[
 [B_a,C_a]=2iv^2\Pi_a(H_a-T_a).                        \tag{M13}
\]

One can also derive the last line directly as
\(i\sum_jE_j\partial_{q_j}c_{a,n}\); the zeroth-order origin and
half-density terms commute with multipliers. The cross terms of the
totals in M4 are indispensable. For one particle the last multiplier
is nonzero whenever sin(aq)(1−cos(aq))≠0. Thus finite-a C_a is not
a central Lorentz Casimir. On an n-particle patch |q_j|≤R, its absolute
multiplier is at most

\[
 v^2a^2n^2 E(R)R^3,\qquad E(R)=\sqrt{m^2+v^2R^2}.      \tag{M14}
\]

This follows from |p|≤nR and
h−t≤nE(R)a²R²/2. It is a fixed-n bound, not uniform in n.
The sharp projection F_a generally fails to preserve Dom B_a: a
smooth function nonzero at Q_a acquires a jump there. An unqualified
infinitesimal commutator [B_a,F_a] on the smooth core is therefore
not being asserted.

There is nevertheless a direct, strong bounded-group result. Put
W_a(s)=exp(−isB_a) and fix S<infinity. The actual one-particle flow
is the parent's complete characteristic with speed E_a. Since its
periodic lift obeys E_a(q)≤m+v|q|, either time direction carries a
packet initially supported in [−R,R] into [−R_S,R_S], where

\[
 R_S=(R+m/v)e^{vS}-m/v.                               \tag{M15}
\]

This support statement follows from the scalar Gronwall bound and the
inverse-flow support orientation. If pi/a>R_S there is no endpoint
crossing for these packets. If also M11 holds with R_S, both the
packet and its transported packet are fixed by F_a. Hence

\[
 [W_a(s),F_a]J_a^*f=0\quad (|s|\le S)                \tag{M16}
\]

for every such one-particle f. In all other sectors the commutator is
already zero, since boosts preserve particle number. Under the rate
condition in M12, M16 eventually holds for each compact f. The bound
\(\|[W_a(s),F_a]\|\le2\), compact-packet density and the isometries
then prove, for every continuum Fock vector Psi,

\[
 \sup_{|s|\le S}\|
 \mathcal I_a[W_a(s),F_a]\mathcal I_a^*\Psi\|
 \longrightarrow0.                                  \tag{M17}
\]

This proof does not need to infer a finite-a Lie algebra from the
continuum group. It also agrees with composition of M12 and the
parent's locally uniform strong boost limit. The apparent coexistence
with M13 is explained by the changing support and shrinking a.

Even M17 has a sharp norm obstruction. For a nonempty proper window,
the coordinate u=integral dq/E_a turns its one-particle support into
a proper interval on the u-circle, and W_a translates that circle
with an irrelevant phase. For s not an integer multiple of its period
L_a, the interval and its translated version differ on positive
measure. The difference of their characteristic multipliers has norm
one. Therefore \(\|[W_a(s),F_a]\|=1\) in that case. Fixed nonzero s
is not a period for all sufficiently small a because L_a→infinity.

## 5. Explicit smooth compact joint symbols

Let theta be the C-infinity step equal to 0 on (−infinity,0], equal
to 1 on [1,infinity), and for 0<x<1 equal to
\(e^{-1/x}/(e^{-1/x}+e^{-1/(1-x)})\). Define

\[
 \chi(z)=\theta(2(1-z))\theta(2(1+z)),\quad
 \eta_\Lambda(e)=\theta(2e/m-1)\theta(2-e/\Lambda),
\]
\[
 F_{\delta,\Lambda}(e,p)=\eta_\Lambda(e)
       \chi\!\left({e^2-v^2p^2-m^2\over\delta}\right),
 \qquad 0<\delta<m^2,\quad\Lambda\ge m.                \tag{M18}
\]

Here 0≤F≤1, chi=1 on [−1/2,1/2] and is supported in [−1,1].
The symbol is smooth and compactly supported: on its support
m/2≤e≤2Lambda, and |p|≤2Lambda/v, since delta<m².
Its energy support is strictly positive. Write

\[
 G_a=F_{\delta_a,\Lambda_a}(H_a,\Pi_a).                \tag{M19}
\]

M7 makes G_a vanish in all sectors except n=1. On that sector it
multiplies by eta(E_a)chi(D_a/delta_a), and fixes every compact packet
with E(R)≤Lambda_a and v²a²R⁴/4≤delta_a/2. Consequently,

\[
 \delta_a\to0,\quad a^2/\delta_a\to0,\quad
 \Lambda_a\to\infty
 \quad\Longrightarrow\quad
 \mathcal I_aG_a\mathcal I_a^*\to P_1\text{ strongly}. \tag{M20}
\]

A fixed finite Lambda instead gives eta_Lambda(E)P1, not P1.
The same argument as M15–M17 gives locally uniform strong vanishing
of the bounded group commutators with G_a; on each fixed compact
packet they are exactly zero eventually. At fixed a, G_a is a smooth
one-particle multiplier and zero on other sectors. It preserves
Dom B_a and its commutator with B_a extends to a bounded operator.
Its multiplier, initially calculated on the common core, is

\[
 i v^2p\,\eta_\Lambda'(h)\chi((c-m^2)/\delta)
 +{2iv^2\over\delta}p(h-t)\eta_\Lambda(h)
                       \chi'((c-m^2)/\delta).         \tag{M21}
\]

It vanishes on n≠1 by the open spectral separation of those sectors
from the symbol and its derivatives. No uniform bound for M21 as
a→0 is claimed.

## 6. Realizing the smooth filter inside the spin algebra

Let alpha_t be the actual energy flow and kappa_s the actual normalized
current flow. Their canonical implementations are e^{itH_a} and
e^{isPi_a}. They leave the vacuum invariant and preserve parity. The
parent supplies the full-spin implementations, and the spin representation
is faithful: the product representation is isometric on every local matrix
algebra and hence on its norm completion, and composing with the spin
automorphism preserves this property. Strong commutation in M2 thus
implies alpha_t kappa_s=kappa_s alpha_t on the spin algebra.

These are both genuine local spin dynamics at every a. The current has
the finite-range density

\[
 j_{a,x}={1\over4a}(X_xY_{x+1}-Y_xX_{x+1}),
 \qquad \|j_{a,x}\|\le {1\over2a}.                    \tag{M22}
\]

It is the literal normalized representative C4, not a proposed
geometric interpolation. For F(d)=e^{−d}(1+d)^{−3} on Z, each
nearest-neighbor interaction has finite F-norm: only distances zero
and one occur and at most two bonds contain a fixed site. Its norm is
bounded by a fixed numerical constant times g_a+J_a for energy and
1/a for current. The local factors are M2, the interactions bounded,
Hermitian, autonomous and finite range, and the metric is the usual
countable-chain metric. These verify the hypotheses of NSY Theorem 3.1;
thermodynamic flow existence is also a parent input. Its finite-volume
LR bound passes to the norm limit. Averaging over exterior local
unitaries gives, for a local C supported in B_L(0), either flow rho,

\[
 \|(1-\mathbb E_{B_R})\rho_t(C)\|
 \le K(2L+1)\|C\|e^{-(R-L-V_{\rho,a}|t|)},             \tag{M23}
\]

when the displayed distance is positive; the trivial bound 2||C|| is
always available. Fixed constants can be enlarged to absorb integer
floors, and V_{rho,a}≥1 can be chosen with
V_{rho,a}≤K_{m,v}(1+a^{-1}). This follows by putting the temporal
factor exp(2C_F||Phi||_F|t|) of the inspected theorem into the spatial
exponential. K does not need a new physical identification.

For a rapid almost-local spin A, define its centered error
epsilon_A(R)=||A−E_{B_R}A||, and use the exact Fourier convention

\[
 w_F(t,s)={1\over(2\pi)^2}\int_{\mathbb R^2}
 F(e,p)e^{-i(te+sp)}\,de\,dp,\qquad
 F(e,p)=\int w_F(t,s)e^{i(te+sp)}\,dt\,ds,
\]
\[
 \mathcal B_{a,F}(A)=\int_{\mathbb R^2}
     w_F(t,s)\alpha_t\kappa_s(A)\,dt\,ds.             \tag{M24}
\]

Compact smooth F has a Schwartz Fourier kernel by integration by
parts, so this is an absolutely convergent Bochner integral in algebra
norm. No unbounded operator product or double-operator integral is
needed. The norm is at most ||w_F||_1||A||. Fourier inversion and
vacuum invariance give the exact vacuum formulas

\[
 \pi(\mathcal B_{a,F}(A))\Omega
           =F(H_a,\Pi_a)\pi(A)\Omega,
\]
\[
 \pi(\mathcal B_{a,F}(A)^*)\Omega
           =\overline{F(-H_a,-\Pi_a)}\pi(A^*)\Omega=0
 \quad\text{for M18}.                                \tag{M25}
\]

The last equality follows from H_a≥0 and the strictly positive
energy support of F. On arbitrary excited vectors the smeared operator
is not F(H_a,Pi_a)pi(A): it filters energy/current *differences*.
Norm Fubini and convolution show that its transfer support for the
actual R² action, with characters exp(i(te+sp)), is contained in
supp F. Indeed further smearing by g replaces w_F by g*w_F, whose
transform is hat(g)F; disjoint Fourier support makes the convolution
zero. The adjoint support is reflected. This is transfer relative to
the actual current flow, not continuous geometric spatial transfer.

Here is the required almost-locality proof with dependence retained.
Put V_a=max(V_{energy,a},V_{current,a},1) and

\[
 W_N(F)=\int(1+|t|+|s|)^N|w_F(t,s)|\,dt\,ds.
\]

Approximate A by C=E_{B_{R/8}}A. On the rectangle
|t|≤R/(8V_a), |s|≤R/(8V_a), first approximate kappa_s(C) by its
expectation in B_{R/2}, using M23; then approximate its energy
evolution in B_R. Both errors are bounded by K_a R exp(−R/4)||A||,
after enlarging constants for floors. The original A-to-C error costs
at most 2epsilon_A(R/8) after 1−E_{B_R}. Outside that rectangle,
|t|+|s|>R/(8V_a), so the weighted kernel tail is bounded by
(8V_a/R)^N W_N(F). Integration gives, for all sufficiently large R,

\[
 \begin{split}
 \|(1-\mathbb E_{B_R})\mathcal B_{a,F}(A)\|
 &\le \|w_F\|_1
 [2\epsilon_A(R/8)+K_a R e^{-R/4}\|A\|]\\
 &\quad+2\|A\|(8V_a/R)^N W_N(F).                     \tag{M26}
 \end{split}
\]

This is rapid almost locality for each fixed a, F and A. Replacing
w_F by its time/current derivatives and integration by parts proves
all mixed norm derivatives of the filtered element. In particular no
norm differentiability of the seed A was assumed. The LR hypotheses
and composition estimates are checked for the actual two flows.

The shrinking symbol has explicit nonuniform bounds. Put
lambda=Lambda/m≥1 and epsilon=delta/m²<1, and use dimensionless
x=e/m, y=vp/m. Its support has area at most 8lambda² and lies in
|x|,|y|≤2lambda. The chain rule gives, for each multi-index alpha,

\[
 \|\partial^\alpha F\|_\infty
 \le C_\alpha(1+\lambda/\epsilon)^{|\alpha|}            \tag{M27}
\]

in these dimensionless coordinates. Each derivative of
(x²−y²−1)/epsilon has size at most 4lambda/epsilon at first order,
2/epsilon at second order and zero above second order; derivatives of
the cutoffs are bounded with the upper-cutoff derivatives carrying
lambda^{-1}. This proves M27 term by term by the ordinary chain rule.
For an integer L with 2L>N+2, integration by parts with (1−Delta)^L,
followed by integration of (1+u²+z²)^{-L}(1+|u|+|z|)^N in two
dimensions, gives

\[
 W_N(F_{\delta,\Lambda})
 \le C_{N,L,m,v}\lambda^2(1+\lambda/\epsilon)^{2L}.
 \tag{M28}
\]

The scaling is w(t,s)=(m²/v)k(mt,ms/v), which accounts for the
constant C in this moment conversion. If delta=m²(am/v)^gamma
and Lambda=m(am/v)^{−beta}, beta>0, then M28 grows at most as
(am/v)^{−2beta−2L(beta+gamma)} for small a. Combined with V_a=O(a^{-1}),
M26 is an explicit a-dependent locality estimate. This upper bound
does not assert a necessary optimal divergence. It supplies no uniform
physical-radius local-net limit. The exact odd seeds below also have
a-dependent localization constants, which must not be hidden.

## 7. Actual creators and the parity boundary

The scattering parent supplies the odd spin elements
A_{a,x}=gamma_a^{-1}(S_x^−), with A_{a,x}Omega the one-particle
site basis and A_{a,x}*Omega=0. Their exponential localization for
each a, and the almost locality of their smooth packet sums, are
imported exactly at S5–S11. A normalized flat-measure packet
f∈C_c^infinity(R) supported inside I_a corresponds to the parent's
circle wavefunction sqrt(2pi/a) f(k/a), extended periodically by zero.
Its Fourier packet element A_a(f) is an actual bounded odd almost-local
spin element with vacuum column f in h_a.

Choose M18 so that E(R)≤Lambda and v²a²R⁴/4≤delta/2 on supp f.
Then M24–M25 construct an odd almost-local creator B_a(f) with

\[
 \pi(B_a(f))\Omega=f,\qquad \pi(B_a(f)^*)\Omega=0,
 \quad\operatorname{Sp}_{\alpha\kappa}(B_a(f))
                          \subset\operatorname{supp}F_{\delta,\Lambda}.
 \tag{M29}
\]

This gives a dense family of continuum compact packet columns along
the scaling, while retaining the actual spin algebra and both smooth
flow derivatives. For a general almost-local A, M25 removes its entire
off-one-particle vacuum column, with any surviving one-particle part
filtered by M19. It does not prove convergence in norm of the operators
B_a(f), whose seed norms and localization constants may depend on a.

Parity is exact. The parent gamma preserves spin parity, and in the
product representation parity is (−1)^N with an even vacuum. Hence
every even spin A has pi(A)Omega in even Fock space. Both F_a and G_a
therefore annihilate every such vacuum vector. The smooth construction
preserves the parity of A, so an even seed has zero vacuum column
after filtering too. This does not mean its filtered operator is zero
on excited states. Odd creators M29 are not observables of a parity-even
vacuum algebra. No one-particle observable in that even algebra, and no
change of its excitation threshold to m, follows from this theorem.

## 8. Scope stress check and open obligations

The root proposal's principal statements survive at their stated scope.
The sharp-window threshold endpoint, the fixed-a product-domain equality,
the necessary window rate, and the direct compact-packet commutation
argument are refinements. The additional construction is the
actual two-flow smooth filter M18–M29 and its nonuniform moment/locality
bookkeeping. It does not promote the root's input to independent evidence.

The negative observations have narrow, exhibited witnesses. Replacing
current by branch momentum q makes E_a²−v²q² negative near the edge
for sufficiently small a. Omitting interparticle cross terms changes
the threshold. A convergent finite ratio delta_a/a² gives the band in §3,
and o(a²) gives zero. A merely bounded ratio need not have a limit.
A fixed energy cutoff gives eta(E)P1. High-momentum packets obstruct norm
convergence, sharp cutoffs fail the boost derivative domain, and even
seeds have zero odd vacuum columns. These are distinct failed inferences,
not independent walls against a physical theory. Smooth filtering and
odd full-spin creators are explicit surviving routes. No theorem excludes
other densities, dynamics, dimensions, parity extensions, or local-net
limits; their construction has not been attempted here.

The analytic statements above have no intentionally open internal lemma.
Their load-bearing review targets are the maximal domains and endpoint
measure in §2, the moving-window necessity and embeddings in §3, the
bounded-group versus derivative-domain distinction in §4, and the actual
two-flow locality and Fourier scaling in §6. The parent's conditional
spin realization remains an explicit dependency. The next substantial
physical obligation is a controlled map of local algebras in the continuum
limit; strong vector/filter convergence and fixed-a almost locality do
not discharge it. Framework selection of the model is also outside scope.

No Lean result is claimed. The potentially delicate issues here are
operator domains, a moving spectral window and localization constants;
an elementary polynomial formalization alone would not resolve them.
The full analytic source is to be frozen before scientific controls.

### No-Go Discipline Gate: scope record, no packet PASS

| Item | Result at this note's exact scope |
|---|---|
| N1, alternatives | ATTEMPTED: actual-current sharp windows succeed strongly; replacing current by branch momentum fails positivity; changing the width scale gives the explicit alternative limits in §3; smooth compact symbols succeed with almost locality; replacing even seeds by the actual odd creators succeeds. These are actual alternatives and scope checks, not five closed attack families against one universal no-go. No N1 packet PASS is claimed. |
| N2, dependence | The local stress mismatch and M13 are the same finite-a obstruction. The norm-window witness and group norm-commutator witness use the same omitted/shifted momentum support. The even-seed boundary instead uses exact parity, while the fixed-cutoff limit uses the chosen eta. No count or proof of independent physical walls is asserted. |
| N3, hidden premises | The chain, state, m,v,a family, actual current normalization, full Fock space, positive gap, continuum measure, comparison maps, window scale, energy cutoff, finite boost times and a-dependent locality constants are all explicit. “Canonical” refers to C28's supplied GNS identification. No registered primitive is used to derive this dynamics or choose this state. |
| N4, residual matching | Concrete C28–C29 gives precisely M13 after the M2–M3 scaling. Continuum (9)–(13), (23) gives precisely the complete flow and speed used in M15. Scattering S5–S11 gives precisely the odd spin seeds and their localization. No unrelated negative claim is imported. |
| N5, resolutions | Local spin elements and their parity are handled in §§6–7; modes and every finite-particle block in §§2–5; Hilbert full-Fock strong convergence by boundedness/density. A uniform physical local-net limit and sitewise continuum observable convergence are not tested or claimed. |
| N6, partial closure | Normalizing actual current is explicitly realized by M22. Smooth filtering and the expanding cutoff solve the stated creator/filter task. A convention change does not make C_a central, and no new-axiom necessity is claimed. |
| N7, steelman | A critic can keep the exact finite-a noncentrality, use smooth filters and odd creators, and still obtain a strong continuum one-particle selection. That construction is proved here. To extend it to a local continuum net, supply uniform physical-region localization estimates and comparison maps of algebras; the present estimates neither prove nor exclude that extension. |
| N8, prior comparison | The complete supplied continuum parent explicitly preserves finite-a scalar-closure failure while proving a changing-family group limit. The supplied scattering parent supplies actual odd creators without a joint geometric spectral gap. This note uses both live mechanisms; it does not recycle either finite-a observation into a blanket no-go. |

The no-go skill's five-family submission schema is not certified by this
positive conditional probe. Root's later publication decision must preserve
this limitation if a separate negative-claim packet is required.

## 9. Frozen evidence, real diagnostic failure and handoff

The analytic source through §8 was frozen before scientific execution at
SHA-256 `4916b1ead5abcc222cd55a1b82e249ca30642ec20639e2237c9fb1fd1b2526d1`.
Those bytes remain in `current_mass_filter/frozen/ANALYTIC_BEFORE_CONTROLS.md`.
The initial source/control manifest was
`4fbd7dc80c4f32340e0117adf78c93cae38f7a6654b94e77f0ddd56a9265e645`;
the reference-refined second manifest is
`ad53d96e9dbe1bfd59cdd79351dcd103dabf7e00b0ec8a3a8ca06bf6fba30010`.
The candidate formulas, proof, fixtures and acceptance tolerances did not
change between the executions. Root received the analytic identity before
controls and is a coauthor, not an independent reviewer of this work.
During final source inspection, two summary sentences were tightened to
require a convergent finite ratio for the stated critical-band limit;
the quantified statement and its proof in §3 already had that hypothesis.
A merely O(a²) width may oscillate and need not have one strong limit.
This post-control scope clarification and one wording cleanup are preserved
as a literal analytic delta; no formula or control criterion changed.

The finite controls use separate literal Pauli tensors for current,
Hermitian kernel eigenvalues for energy, directional finite differences
for the boost bracket, direct quadrature for captured packet norms,
occupation-space parity/transfer matrices, and actual unitary conjugations
integrated against an asymmetric Gaussian for Fourier signs. They share
the specified parent model and conventions. These are different-method
author checks, not an independent mathematical review.

| Check | Actual result and limitation |
|---|---|
| Literal seven-site current, two nonunit parameter fixtures | Current eigenvalues and eigenvector residuals meet the `2e-12` tolerance; the largest eigenvalue discrepancy is `1.78e-15`. This checks normalization/orientation in one-flip coordinates, not a finite-volume ground state. |
| Total mass and thresholds | Explicit n=1,2,3,5 tuples agree with kernel totals. The n=2 opposite-momentum example has C=`3.312947559375325`, above `4m²=3.3124` and below the deliberately enlarged edge `3.320681`. The endpoint's zero spectral atom is proved analytically. |
| Actual boost derivative | The largest sampled analytic/finite-difference discrepancy is `4.22e-10`; at q=.71 the nonzero bracket is about `.0811215982`. This is not a certified numerical error bound and cannot check the origin potential, which commutes with C. |
| Moving Gaussian packet | For m=1,v=.9 and gamma=1, the projection norm error falls from `.0721779` at a=.4 to `9.76598e-6` at a=.0125. At the latter spacing gamma=2 gives `.162068`, gamma=3 gives `.667485`. Their limits are proved by M12, not fitted. |
| Characteristic support | Both time directions and both endpoints obey M15 at the tested spacings, with M11 separately checked. This illustrates support containment, not a norm limit. |
| Compact transfer and parity | The finite odd seed keeps a unit one-particle vacuum column and loses its three-particle column. The even seed's column and the filtered odd adjoint column are exactly zero. The infinite spin construction remains §§6–7. |
| Double Fourier clock | Direct 32- and 48-node Gaussian integrations of actual energy/current conjugations agree with the Fourier convention below `7.3e-16`. The Gaussian tests signs only; compact transfer and almost locality are proved in §6. |

The initial baseline really failed. For gamma=3 at a=.025 and .0125,
the float64 kernel-root references shifted the Gaussian loss by
`3.3348046546421983e-11` and `3.039185569875258e-11`, beyond the
unchanged `2e-11` tolerance. The full first source, protocol, streams,
arrays, receipts and mutants remain under `frozen/revision_1/`.
Before the second execution, the revision was declared: only the
window-root reference was evaluated at 70 decimal digits from the
original kernel determinant `4(g−J cos k)²+4J² sin² k`, followed by
the current subtraction. It does not use simplified M5. The original
float64 roots remain in every final result. The refined losses differ by
`1.67e-16` and `5.55e-17` in the formerly failing fixtures. This resolves
the observed cancellation sensitivity without an analytic correction or
a relaxed criterion. Neither precision provides interval certificates.

The final baseline exits zero. Each literal source mutant has a targeted
rejecting witness, and the full results preserve all surviving rows:

| Source variant | Rejection and meaningful survivor |
|---|---|
| Multiply current by v² | Literal Pauli and total-mass/boost comparisons reject it. Tests taking supplied joint coordinates do not exercise the changed current function. |
| Replace current by branch q | Literal current and mass checks reject it; an edge witness has negative proposed mass squared. Unrelated symbol/parity tests survive. |
| Drop multiparticle cross terms | The low-momentum n=2 value becomes `1.6562` instead of `3.3124123`. The selected high-momentum n=5 lower-bound test still passes although its total-mass identity fails. One-particle checks are unchanged. |
| Declare mass central | Nonzero finite-difference brackets reject it. The zero mode and a tiny bracket below tolerance survive. Static symbolic identities do not execute the mutated numerical function. |
| Square root instead of fourth root in M10 | Every window radius/loss comparison rejects it; unrelated current, parity and clock tests survive. |
| Delete energy cutoff | The high-energy mass-shell support witness changes from zero to one. Low-energy column and parity checks survive and cannot certify compact support. |
| Reverse transfer energy | The creator column disappears and the adjoint column becomes nonzero. Parity remains correct. |
| Reverse Gaussian current sign | The direct double-flow comparison differs by `.319902`. M18 is even in p and cannot itself discriminate this sign convention. |

Every scientific subprocess had an actual 60-second timeout; none timed
out. Both nine-process executions retain complete streams, exact argv,
cwd, source hashes, time limits, elapsed times and exit codes. Initial
read-only and preparation tool calls predated the subprocess recorder;
their absent local process timing/stream receipts are not invented.
Inspected source bytes, the exact preparer, bounded search output and
operational history are preserved. Truncated displays were recovered by
reading the complete affected source/result portions.

The additional primary theorem is
[Nachtergaele–Sims–Young, arXiv:1810.02428v2](https://arxiv.org/abs/1810.02428v2),
Theorem 3.1 with its interaction and F-function definitions. Its raw TeX
and prior fetch receipt are inventoried under `sources/external_raw/` and
are not proposed publication outputs. The parent carries thermodynamic
existence; this note checks the current interaction and two-flow composition.

The [evidence README](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/e26e2de4fd64ee49d0745cbf02fd05355494b569/.claude/science/physics-loops/toe-current-mass-20261012/EVIDENCE_MAP.json),
[current checkpoint](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/e26e2de4fd64ee49d0745cbf02fd05355494b569/.claude/science/physics-loops/toe-current-mass-20261012/EVIDENCE_MAP.json), final manifest
and receipt bind the deliverable. The next action is independent analytic
review, especially M8, M12, M16–M17 and M23–M28. All publication/audit
decisions remain with root. No Git, prompt, axiom, audit-status or repository
execution-surface change was made. The selected model and reasoning effort
were preserved; no work was subdelegated.


## Publication evidence and limits

**Author/checker pairing:** Same selected model family and reasoning effort, separate author/reviewer contexts with candidate formulas exposed; not blinded or diverse-family. Root supplied the route and is a coauthor. The Lean formalization is root-authored scoped kernel checking, not independent reconstruction of the surrounding physics. Mechanical packaging adds no scientific review.

Finite spacing has a noncentral mass observable and fails exact scalar Lie closure. Sharp windows need not preserve the boost domain; operator-norm convergence fails. Smooth creator locality constants depend on spacing and window/cutoff scales. Even seeds have zero filtered vacuum columns, not necessarily zero filtered operators on excited states. No interacting, three-dimensional, framework-selector, physical-particle or continuum local-net theorem is supplied.

The original baseline failed two gamma=3 Gaussian-loss rows at a=.025 and .0125. The unchanged tolerance was retained while the reference alone was refined to a 70-digit original-kernel determinant; original float64 roots remain in every final result. All original failed streams and revision maps are preserved. All eight literal candidate mutants historically reject as whole runs; every passing, changed and unchanged subrow remains available. Those historical outcomes are not predictions of the publication execution.

The protocol’s historical all-n label describes an implemented two-particle SymPy specialization of M13. The general identity rests on the analytic proof. The accepted [live README clarification](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/e26e2de4fd64ee49d0745cbf02fd05355494b569/.claude/science/physics-loops/toe-current-mass-20261012/AUTHOR_EVIDENCE_README.md) records this limit without changing frozen wording. Reviewer mechanisms include literal current matrices, finite-difference refinement, moving windows and actual two-flow conjugation; the canonical-vacuum supplement followed exposure. No combined author/reviewer count is promoted as independence.

The later scoped Lean certificate (`formalization/current_mass_threshold/README.md`) proves only the finite-sum threshold from nonnegative energies and individual mass bounds, deriving the pair inequality and retaining all cross terms. The [human-readable source](../formalization/current_mass_threshold/MassThreshold.lean) and runtime reproduction record (`formalization/current_mass_threshold/README.md`) accompany the successful object/diagnostics and all five compiler attempts in the complete evidence archive. The two initial 120-second timeouts are inconclusive; the later sequential false controls reject with explicit False goals. This root-authored certificate does not cover M13, dispersion, infinite Fock sums, maximal domains, spectral endpoints, filter limits or locality. No new Lean compilation occurs in publication.

Direct proof inputs are [Concrete chain](CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md) for the actual GNS/generators, [Continuum limit](GAPPED_CONTINUUM_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-12.md) for the supplied scaling and group comparison, and [Scattering S5–S11](GAPPED_CHAIN_SCATTERING_BOUNDED_THEOREM_NOTE_2026-10-12.md) for the actual odd seeds and columns. The exact-Lie massive-carrier theorem and pending local-algebra routes are not imported.

Complete source reviews, root coverage, original sources, receipts, raw matrices, failures, survivors and timing are reconstructable through the [evidence map](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/e26e2de4fd64ee49d0745cbf02fd05355494b569/.claude/science/physics-loops/toe-current-mass-20261012/EVIDENCE_MAP.json). External source content remains outside the repository; [versioned identities and exposure records](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/e26e2de4fd64ee49d0745cbf02fd05355494b569/.claude/science/physics-loops/toe-current-mass-20261012/EXTERNAL_SOURCE_INVENTORY.json) are retained. At source preparation, canonical execution and all eight original variants are unrun; actual outcomes belong to the separate runtime verification record. Global combined validation and strict audit lint are separate independent landing gates; no audit verdict or retained promotion is applied.
