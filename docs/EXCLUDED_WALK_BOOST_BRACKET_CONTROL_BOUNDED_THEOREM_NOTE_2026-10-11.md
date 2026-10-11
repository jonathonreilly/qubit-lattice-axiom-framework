---
claim_id: excluded_walk_boost_bracket_control_bounded_theorem_note_2026-10-11
claim_type: bounded_theorem
claim_scope: "For the supplied antisymmetric excluded Weyl pair and canonical additive energy placement, exact compressed boost/current and boost/boost formulas give explicit prepared-packet residual bounds. The boost/current norm is o(lambda) below the lambda^(-1/2) time threshold, has a positive energy-scaled limit at that threshold, and is Theta(sqrt(lambda)) at specified small inverse-energy times. All nine actual residual expectations are o(lambda), uniformly on every fixed finite rescaled-time interval, by an explicit gapless forced-state limit and symmetric-form cancellation. Operator domains and all physical premises remain explicit."
upstream_dependencies:
  - excluded_walk_low_energy_energy_current_bounded_theorem_note_2026-10-11
runner: scripts/excluded_walk_boost_bracket_control_2026_10_11.py
---

# Boost-bracket control for the supplied excluded Weyl pair

**Date:** 2026-10-11. **Type:** bounded_theorem.

**Status:** conditional-support; provisional mathematics, without an applied
retained-status audit. The supplied walk, continuous clock, antisymmetric pair,
site exclusion, spatial coordinates and chosen energy placement are premises.

The five complete arguments below use one globally normalized positive-positive
origin-cone preparation. Part I gives the exact differential boost/current
bracket and an explicit norm bound. Part II controls its actual evolution for
times at most lambda^(-gamma), gamma<1/2. In this interval lambda*t tends to
zero, so it is shorter than the inverse-energy clock. Part III computes the
boost/boost contact correction and compares it to a rotation on the prepared
state, with the ordinary momentum chart and a periodic auxiliary operator
distinguished explicitly. Part III does not inherit Part II's time estimate.

Part IV locates the sharp power threshold for the norm in Part II using the
same packets. At time lambda^(-1/2), its norm divided by lambda tends to a
strictly positive constant. At time tau/lambda for fixed 0<tau<=1/32768,
the norm is Theta(sqrt(lambda)). These are diagonal-component norm results;
they do not imply an expectation estimate or exclude other preparations.
The complete zero-space and integrability arguments are rederived in Part IV,
with the earlier memory milestone credited as prior mathematical work.

Part V proves the actual expectation result separately: all nine residual
expectations are o(lambda), uniformly for |tau|<=T at time tau/lambda for
each fixed finite T. The complete forced state converges in H1_kappa(L2_q)
to a compressed-kernel evolution. Symmetry controls both cross terms and
the limiting kernel self-pairing vanishes. Thus a small mean is compatible
with the larger diagonal residual norm. No convergence rate, growing-tau
interval or off-diagonal norm lower bound is asserted.

The energy interval stated for the excluded state is an expectation bound.
It is not preserved individual-cone or spectral support. These estimates do
not construct an exponentiated boost, a physical rotation group, a full
Poincare algebra, or gravitational dynamics. Constants are conservative.

Each part retains its original equation and section numbering. A reference
to a section within a part refers to that part. Frozen research sources,
explicit publication edits and exact reconstruction are preserved in the
[milestone evidence](../.claude/science/physics-loops/toe-boost-bracket-control-20261011/).
The original sources' historical status prose is superseded only by the
source-bound publication review recorded there; no status is inferred from
a finite-control count.

**Parent:** [canonical current and excluded-walk premises](EXCLUDED_WALK_LOW_ENERGY_ENERGY_CURRENT_BOUNDED_THEOREM_NOTE_2026-10-11.md),
complete branch revision b9b032ae790c66e762a6296a1306bfb64ae7cd70.
**Runner:** [finite algebra and constant controls](../scripts/excluded_walk_boost_bracket_control_2026_10_11.py).
**Negative-claim scope:** [N1–N8 assessment](../.claude/science/physics-loops/toe-boost-bracket-control-20261011/NO_GO_DISCIPLINE_CHECKLIST.md).

# Part I — Prepared-state boost/current control

Source date: 2026-10-11. Original argument preserved with the publication edits recorded in the evidence packet.

**Status:** conditional mathematical result. The source-bound review and its independence limits are recorded in the publication evidence. No retained-status audit is assigned here. The supplied walk, continuous clock, antisymmetric pair sector, site
exclusion, spatial coordinates and canonical local-energy placement remain
premises. No new physical primitive, collision clock or gravity law is adopted.

The result is at the **prepared states** specified below. It does not assert
that their momentum or derivative bounds persist under the excluded evolution.

## 1. Result and exact source boundary

For the canonical energy dipole $D_a$, its actual bounded current $J_b$, and
the compressed Hamiltonian $H_D$, define on the common domain below

\[
 R_{ab}=-i[D_a,J_b]-\delta_{ab}H_D.
                                                        \tag{B1}
\]

The full bracket contains the first derivative

\[
 [H_D,J_b]\partial_{K_a}.
                                                        \tag{B2}
\]

It does not cancel. For globally normalized free packets with small individual
cone offsets, total momentum $|K|\le\lambda/4$, and

\[
 \lambda\|\partial_{K_a}\phi_\lambda\|\le B_a<\infty,
 \qquad \chi_\lambda={P\phi_\lambda\over\|P\phi_\lambda\|},
                                                        \tag{B3}
\]

the argument proves an explicit $O(\lambda^{3/2})=o(\lambda)$ **norm of the
residual applied to the state**. It is a uniform bound on this specified
preparation class with its scaled derivative norm, not an $L^2$-operator
bound obtained solely by imposing an energy window. An explicit smooth,
origin-cone, positive-positive free-band family below has $B_a<60$, and obeys

\[
 \|R_{ab}\chi_\lambda\|\le384\lambda^{3/2},\qquad
 \|[H_D,J_b]\chi_\lambda\|\le6\lambda^{5/2},\qquad
 {\lambda\over2}\le\langle\chi_\lambda,H_D\chi_\lambda\rangle
 \le3\lambda,
 \quad 0<\lambda\le1/16.                                \tag{B4}
\]

All nine $a,b$ components are covered. The constants are conservative.
The energy lower bound makes the comparison with $o(\lambda)$ nonvacuous.
A separate normalized mixed-band construction in Section 8 has small total
energy and total momentum, but has a nonzero order-$\lambda$ bracket residual.
It demonstrates why individual-momentum support is stated rather than inferred.

Load-bearing sources, all used at the following exact bytes:

| Source | SHA-256 | Use / reading coverage |
|---|---|---|
| `S/EXCLUDED_WALK_CANONICAL_CURRENT_DRAFT.md` | `79bc9fb3b9fd9b703f12de0a4ca4ebd62644c81bd6e15c07f723b6b7a1c977fe` | Complete 190-line source freshly read; canonical density, dipole, contact blocks and current, including their domain argument. |
| `WW/docs/EXCLUDED_WALK_LOW_ENERGY_ENERGY_CURRENT_BOUNDED_THEOREM_NOTE_2026-10-11.md` | `9f551fc8d3592e83d15a007495a8f9165a5ddb9bc1e98d9dd3f51b6a2584f401` | Fresh reading of lines 1–175, 370–478 and 805–844: supplied symbol, normalized antisymmetric fibers, channel and corner distinctions, preparation caveat, complete canonical dipole derivation and corrected compression of the current. Earlier campaign reading is not counted as a fresh full-note review here. |
| `S/repo_sync_rc_2045/agents/RC_C3_report.md` | `c4ca747adf80fe0f4cb1e3218c3b47813c2923427fcf41df40b4474e471fe08d` | Complete 170-line report freshly reread; motivates the selected bracket, not a theorem for this interacting Weyl pair. |
| `S/repo_sync_rc_2045/agents/RC_C3_referee.md` | `06b603b76bf1ca0abba47f56a1e98a2993df7e8953e100d07232032461cd10e0` | Complete short referee freshly reread. |
| `S/repo_sync_rc_2045/agents/RC_C3_referee_full.md` | `7e7613191d08b98a5a2f21453da66c494d4a2afdc73a0f75acd49bc852db3354` | Complete 310-line referee freshly reread; regularity, single-scalar scope, improvements and multi-band limits retained. |

Here `S=/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/resume_20261011`
and `WW=/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/walk_worktree`.
The RC copies are pinned to commit
`d009fb786d36a6cab4a7d410630b9382992faa08`; their containing manifest has SHA
`4bcc8fc339fafe9a42d2bc17ad67c23f3e55a21a35f13d740567ecaa41c44e57`.
They were byte-compared to that commit in the immediately preceding route
assessment. This derivation rehashes the copies and does not update that snapshot.

The published parent explicitly supplies the definitions used here; its
historical upstream walk source is `e0536f80a25feb0b368c10a0016a9d09b07b5bd06827751c30029d2eb1d70065`.
No result below relies on rereading all of that historical note in this task.
No new external literature theorem is invoked. The RC literature/numerical
claims are not independently reverified here or used to prove (B4).

## 2. Hilbert space, energy placement and common domain

Work in a small open total-momentum chart $U$ around zero. The relative torus
has measure $dq/(2\pi)^3$, total momentum has measure $dK/(2\pi)^3$, and the
spin space is $\mathbb C^2\otimes\mathbb C^2$. The antisymmetric fiber consists
of functions satisfying $\psi(K,-q)=-\mathsf S\psi(K,q)$, with spin swap
$\mathsf S$. The normalized constant singlet is $c$. Thus

\[
 C=|c\rangle\langle c|,\quad P=I-C,\quad
 H_0=h_1+h_2,\quad
 h_1=\sigma_1\cdot\sin(K/2+q),\quad
 h_2=\sigma_2\cdot\sin(K/2-q),\quad H_D=PH_0P.          \tag{B5}
\]

All fiber inner products below include normalized full-torus measure. $P$
is one global contact projection in each fiber, not eight corner projections.
On the full fiber $H_Dc=0$; its restriction to $P$ is the excluded walk.
The chart convention follows $k_1=K/2+q,k_2=K/2-q$. Compact $K$ support
avoids chart gluing; the full $q$ torus and the antisymmetric condition are
retained. No additional exchange normalization factor is used.

Here $\Pi_{i,x}$ projects particle $i$ onto site $x$, and $X_{i,a}$ is its
integer spatial coordinate. The local energy placement and first moment are
fixed as in the canonical source:

\[
 e_x^0={1\over2}\sum_{i=1}^2\{\Pi_{i,x},h_i\},\quad
 e_x=Pe_x^0P,\quad
 D_a=PD_{0,a}P,\quad
 D_{0,a}={1\over2}\bigl(\{X_{1,a},h_1\}+\{X_{2,a},h_2\}\bigr).
                                                        \tag{B6}
\]

These first moments agree with the spatial sums on finite-support states.
Take as the common invariant test domain the smooth antisymmetric sections,
compactly supported in $U$, smooth and periodic in $q$, and lying in $P$.
It is dense in the allowed direct integral over $U$. The compressed operators
$D_a,H_D,J_b$ preserve this test domain. The ambient operators $D_{0,a},H_0$
act on the corresponding smooth domain without the condition of lying in $P$;
they need not preserve $P$. Integration by parts has
no $K$ boundary term and no $q$ boundary term. The formulas extend to the
corresponding $H^1$ sections by approximation: $D_{0,a}:H^1\to L^2$ is
continuous, and $H_0,P,J_b$ preserve $H^1$. This also connects the chart
calculation to the finite-spatial-support definition. No essential
self-adjointness or exponentiation of the unbounded dipole is assumed.

Put $h=H_0c$, $h_a=\partial_{K_a}h$, and $H_\Delta=h_1-h_2$. Since

\[
 X_{1,a}=i(\partial_{K_a}+\tfrac12\partial_{q_a}),\qquad
 X_{2,a}=i(\partial_{K_a}-\tfrac12\partial_{q_a}),
\]

symmetrization, including $\partial_{q_a}H_\Delta=2\partial_{K_a}H_0$, gives

\[
 D_a=i(H_D\partial_{K_a}+L_a),\qquad
 L_a=P\left(\tfrac12 H_\Delta\partial_{q_a}
                         +\partial_{K_a}H_0\right)P,
 \quad
 L_a^\dagger=-P\tfrac12H_\Delta\partial_{q_a}P.          \tag{B7}
\]

The dagger in (B7) is the **fiber** adjoint in $q$, with $K$ held fixed.
In particular $L_a+L_a^\dagger=\partial_{K_a}H_D$, which also checks symmetry
of $i(H_D\partial_{K_a}+L_a)$ after integration in $K$.

For clarity, the parent contact calculation is reproduced. The $q$ part of

\[
 D_{0,a}=iH_0\partial_{K_a}
        +\tfrac i2H_\Delta\partial_{q_a}+i\partial_{K_a}H_0
\]

has fiber adjoint $\tfrac i2H_\Delta\partial_{q_a}$, which annihilates $c$.
Its value on $c$ is $ih_a$. Since $\langle c,H_0c\rangle=0$, the blocks are

\[
 CD_{0,a}P\psi=ic\langle h,\partial_{K_a}\psi\rangle,
 \qquad PD_{0,a}C(cf)=i\partial_{K_a}(hf).               \tag{B8}
\]

The free identity $i[H_0,D_{0,a}]=g_a$ uses

\[
 g_a=\sum_i\sin k_{i,a}\cos k_{i,a}
     =\sin K_a\cos(2q_a).
\]

The two derivative terms in the compressed Hamiltonian/dipole commutator
cancel, leaving the actual current

\[
 J_a=i[H_D,D_a]=Pg_aP+F_a,\qquad
 F_a=-|h_a\rangle\langle h|-|h\rangle\langle h_a|.       \tag{B9}
\]

Both form factors lie in $P$. $g_a+F_a$ itself need not preserve $P$;
the operator on the excluded space is its compression, as displayed in (B9).

## 3. Complete bracket, including the Hamiltonian/current defect

Define

\[
 r_b=g_bc,\quad r_{b,a}=\partial_{K_a}r_b,\quad
 h_{ab}=\partial_{K_a}h_b,\quad
 \ell_a=h_1\cos(2k_{1,a})+h_2\cos(2k_{2,a}).            \tag{B10}
\]

$r_b,r_{b,a},h,h_a,h_{ab}$ all lie in $P$. The free scalar multiplier
commutator is

\[
 -i[D_{0,a},g_b]=\delta_{ab}\ell_a.                    \tag{B11}
\]

Indeed only the derivatives of $g_b$ contribute; in individual momenta

\[
 \sum_{i=1}^2 h_i\partial_{k_{i,a}}
       \sum_j\sin k_{j,b}\cos k_{j,b}
 =\delta_{ab}\sum_i h_i\cos(2k_{i,a}).
\]

The exact bounded Hamiltonian/current defect, of finite rank in each relative
fiber, is

\[
\begin{split}
 A_b:=[H_D,J_b]={}&-|h\rangle\langle r_b|+|r_b\rangle\langle h|\\
 &-|H_Dh_b\rangle\langle h|-|H_Dh\rangle\langle h_b|\\
 &+|h_b\rangle\langle H_Dh|+|h\rangle\langle H_Dh_b|.
\end{split}                                                    \tag{B12}
\]

The first line is $[PH_0P,Pg_bP]$, since $H_0$ commutes with the scalar
$g_b$; the last two lines are $[H_D,F_b]$. In particular no conservation
of the canonical current has been inserted.

Write

\[
 F_{b,a}=-|h_{ab}\rangle\langle h|-|h_b\rangle\langle h_a|
         -|h_a\rangle\langle h_b|-|h\rangle\langle h_{ab}|,
\]

and define the following bounded operator of finite rank in each relative fiber:

\[
\begin{split}
 B_{ab}={}&-|h_a\rangle\langle r_b|-|h\rangle\langle r_{b,a}|
                +H_DF_{b,a}\\
 &-|L_ah_b\rangle\langle h|-|L_ah\rangle\langle h_b|\\
 &+|h_b\rangle\langle L_a^\dagger h|
                 +|h\rangle\langle L_a^\dagger h_b|.
\end{split}                                                    \tag{B13}
\]

Here $L_a$ and $L_a^\dagger$ act only on the explicitly given smooth
form factors. Thus (B13) contains no hidden differentiation of the input state.
The complete identity is

\[
 -i[D_a,J_b]\psi
   =\delta_{ab}P\ell_aP\psi+A_b\partial_{K_a}\psi+B_{ab}\psi.
                                                               \tag{B14}
\]

To check every contact term, first expand the compressed scalar-current part
using (B8):

\[
 -i[D_a,Pg_bP]\psi
 =\delta_{ab}P\ell_aP\psi
   -\partial_{K_a}\bigl(h\langle r_b,\psi\rangle\bigr)
   +r_b\langle h,\partial_{K_a}\psi\rangle.              \tag{B15}
\]

Its derivative coefficient is $-|h\rangle\langle r_b|+|r_b\rangle\langle h|$;
its constant contact terms are the first two terms of (B13). From (B7), the
remaining part is exactly

\[
 -i[D_a,F_b]=[H_D,F_b]\partial_{K_a}
                  +H_DF_{b,a}+[L_a,F_b].                \tag{B16}
\]

Inserting the rank-two $F_b$ into $[L_a,F_b]$, and integrating its right
action in $q$, gives the last four terms of (B13), with the fiber adjoint
and signs shown there. This proves (B14) without dropping differential terms.

## 4. The differential coefficient is nonzero

There is also an analytic witness, independent of any low-momentum
approximation. Let $K$ have only its $b$ component nonzero and let $j,k$
be the other two axes. Put $C_b=\cos(K_b/2)$, $S_b=\sin(K_b/2)$. Singlet
algebra gives

\[
 \|h\|^2=N=2(C_b^2+2),\quad
 \langle h_b,h\rangle=-\tfrac12\sin K_b,\quad
 H_Dh_b=\tfrac12 r_b,\quad \langle h,H_Dh\rangle=0.
                                                               \tag{B17}
\]

For the third identity, the total-spin term along $b$ annihilates
$\sigma_{1,b}c$, while the difference-spin term gives
$H_0h_b=-\sin K_b\sin^2q_b\,c$; removing its mean gives $r_b/2$.
For the last identity put $h_i^2=\epsilon_i^2 I$ and use
$H_0^3=(\epsilon_1^2+3\epsilon_2^2)h_1+(3\epsilon_1^2+\epsilon_2^2)h_2$, whose singlet expectation
vanishes pointwise. Since $h,r_b$ are pointwise triplet and singlet,
respectively, inserting (B17) into (B12) yields

\[
 A_bh=\tfrac N2r_b+\tfrac12\sin K_b\,H_Dh,
\]

and its pointwise singlet component is

\[
 c^*A_bh(q)=2\sin K_b
     \bigl(\sin^2q_j+\sin^2q_k-2\sin^2q_b\bigr).
                                                               \tag{B18}
\]

The normalized-torus squared norm of this component is $3\sin^2K_b$: the
three independent variables $\sin^2q_i$ have mean $1/2$ and variance $1/8$.
Thus $A_bh\ne0$ for nonzero sufficiently small $K_b$, as well as generically.

Consequently (B14) is not globally a bounded $L^2$ operator, even after a
small total-momentum cutoff alone. Localize a smooth section proportional to
$h(K,q)$ near a nonzero such fiber and multiply it by $e^{iM K_a}$.
Its norm and momentum support are unchanged, while the right side of (B14)
acquires $iM A_b\psi$. This is a statement about that unrestricted
relative-momentum class. This witness is not a positive-band preparation, and
does not establish an impossibility result for every restricted band norm.
It establishes that removing (B2) algebraically would be incorrect.

## 5. Uniform constants for localized free inputs

Assume $0<\lambda\le1/16$, $|K|\le\lambda/4$, and let a free input be
supported in a union of $m\le8$ relative corner balls

\[
 \Omega_\lambda=\bigcup_{C_j\in\mathcal C}
        \{q=C_j+x:\ |x|\le3\lambda/4\},\qquad
 \mathcal C\subset\{0,\pi\}^3.
\]

The balls are disjoint in the torus. Their normalized measure satisfies

\[
 \mu(\Omega_\lambda)\le\nu_m^2\lambda^3,
 \quad \nu_m=\sqrt{9m/(128\pi^2)},
 \quad \nu_m\le\nu:=3/(4\pi)<1/4.                    \tag{B19}
\]

The estimates below apply to any smooth input with this support; positivity
and a free energy window will be imposed in Section 7. A $K$ derivative of
a smooth supported section has the same support. The exact form factors are

\[
 h(q)=2\sum_j\cos(K_j/2)\sin q_j\,\sigma_{1,j}c,
 \quad h_b(q)=-\sin(K_b/2)\sin q_b\,\sigma_{1,b}c.
                                                               \tag{B20}
\]

The following bounds use the **full torus**, including the part outside
$\Omega_\lambda$. They hold uniformly on the stated $K$ support:

| Form factor / operator | Bound used |
|---|---|
| $H_0,H_\Delta,H_D$ | operator norm at most $4$ |
| $\partial_{K_a}H_0$ | operator norm at most $1$ |
| $h$ | $\|h\|_2\le3, \|h\|_\infty\le4, \|\partial_{q_a}h\|_2,\|\partial_{q_a}h\|_\infty\le2$ |
| $h_a,h_b$ | $L^2,L^\infty$ norms at most $\lambda/8$ |
| $\partial_{q_a}h_b$ | $L^2,L^\infty$ norms at most $\lambda/8$ (zero if $a\ne b$) |
| $h_{ab}$ | $L^2,L^\infty$ norms at most $1/2$ (zero if $a\ne b$) |
| $r_b,r_{b,a}$ | $\|r_b\|_2,\|r_b\|_\infty\le\lambda/4, \|r_{b,a}\|_\infty\le1$ |
| $H_Dh$ | $\|H_Dh\|_2\le12, \|H_Dh\|_\infty\le22$ |
| $H_Dh_b$ | $\|H_Dh_b\|_2\le\lambda/2, \|H_Dh_b\|_\infty\le7\lambda/8$ |
| $L_ah,L_ah_b$ | $L^2$ norms at most $7,3\lambda/8$ |
| $L_a^\dagger h,L_a^\dagger h_b$ | $L^\infty$ norms at most $8,\lambda/2$ |

For example, $H_Dh=H_0h-c\|h\|^2$ and
$H_Dh_b=H_0h_b-c\langle h,h_b\rangle$; these subtractions are included in
the $22$ and $7\lambda/8$ bounds. For $L_a^\dagger$, first bound
$H_\Delta\partial_{q_a}u/2$ and then its constant projection by the same
supremum bound. This accounts for the factor two in $8,\lambda/2$.

For a supported fiber input $f$, each rank-one term satisfies

\[
 \||u\rangle\langle v|f\|_2
 \le\|u\|_2\|v\|_\infty\nu_m\lambda^{3/2}\|f\|_2.
\]

Summing (B12), the coefficient of $\lambda$ is bounded by

\[
 (3/4+1)+(2+3/2+11/4+21/8)=85/8<12.
\]

In (B13), the corresponding coefficient is bounded by

\[
 3+\lambda^2/32+(14+\lambda^2/8)
       +(3/2+7/8+1+3/2)\lambda
 =17+39\lambda/8+5\lambda^2/32<24.
\]

Thus, also after integrating in $K$,

\[
 \|A_b f\|\le12\nu_m\lambda^{5/2}\|f\|,
 \qquad
 \|B_{ab}f\|\le24\nu_m\lambda^{3/2}\|f\|.             \tag{B21}
\]

Only the volume of the input support was used in (B21); its location in corner
balls is used next for the free multiplier. This distinction is useful for
the counterexample in Section 8.

## 6. Global contact projection and the prepared-state theorem

Let $\|\phi_\lambda\|=1$, with the support and regularity just specified. Put

\[
 \eta=\nu_m\lambda^{3/2},\quad
 \alpha(K)=\langle c,\phi_\lambda(K)\rangle,\quad
 n_\lambda=\|P\phi_\lambda\|.
\]

Cauchy–Schwarz in the full torus gives

\[
 \|C\phi_\lambda\|\le\eta,
 \quad n_\lambda^2=1-\|\alpha\|_{L^2_K}^2\ge1-\eta^2,
 \quad
 \chi_\lambda={\phi_\lambda-c\alpha\over n_\lambda}.
                                                               \tag{B22}
\]

This is a single global normalization over $K,q$. It is not fiberwise
renormalization and does not assume that the $K$ probability law is unchanged.
The subtracted $c\alpha$ has support on the **entire** relative torus.
The physical state is therefore not exactly free-band or corner supported.

All form factors in (B12)–(B13) lie in $P$. Hence

\[
 A_b\partial_{K_a}\chi_\lambda
     ={A_b\partial_{K_a}\phi_\lambda\over n_\lambda},
 \qquad B_{ab}\chi_\lambda={B_{ab}\phi_\lambda\over n_\lambda}.
\]

There is no derivative of $n_\lambda$ with respect to $K$: it is the one
global scalar in (B22). For the multiplier defect let $M_a=\ell_a-H_0$.
On every retained corner ball, each individual $k_i$ is within $7\lambda/8$
of the corresponding corner. Consequently

\[
 \|M_a\phi_\lambda\|\le4\lambda^3,
 \qquad\|M_a\|\le8,
 \qquad
 \|PM_aP\phi_\lambda\|\le4\lambda^3+8\eta.             \tag{B23}
\]

The first inequality uses $\|h_i\|\le\lambda$ on the support and
$|\cos(2k_{i,a})-1|\le2\lambda^2$; the global bound uses
$2\|h_1\|+2\|h_2\|\le4\sqrt3<8$. The last $8\eta$ explicitly bounds
the global contact tail instead of pretending that $P$ preserves the band.

Combining (B14), (B21) and (B23) proves, with
$B_a=\lambda\|\partial_{K_a}\phi_\lambda\|$,

\[
 \boxed{\quad
 \|R_{ab}\chi_\lambda\|
 \le {4\lambda^3+\nu_m(32+12B_a)\lambda^{3/2}
                  \over\sqrt{1-\nu_m^2\lambda^3}},\qquad
 \|[H_D,J_b]\chi_\lambda\|
 \le {12\nu_m\lambda^{5/2}\over\sqrt{1-\nu_m^2\lambda^3}}.
 \quad}                                                       \tag{B24}
\]

For $a\ne b$, the $4\lambda^3+8\eta$ multiplier contribution can be
omitted. The displayed uniform form is enough for all components. It also
bounds every normalized test-vector matrix element of the residual, by
Cauchy–Schwarz. It does not furnish an $L^2$-operator bound on states whose
scaled $K$ derivatives are unrestricted.

All eight corner signs are covered: writing $q=C_j+x$ replaces $\sin x$
by $\operatorname{diag}(\pm1)\sin x$ in the one-body symbols but leaves
their norms and $\cos(2k_{i,a})$ estimates unchanged. The contact amplitudes
from different corners add coherently in the **same** $\alpha(K)$.
Using the measure of their union in (B19) bounds that interference without
an incoherent-sum assumption. At the origin this is literal small individual
momentum; at the other seven corners it is small **offset** from a different
cone. Distinct-corner pairs with total momentum near another total corner
are outside the selected $K$ chart. They are not identified with $K=0$.

## 7. A specified smooth, normalizable low-individual-momentum preparation

Here only the origin corner is populated before projection. Let $F,f$ be
fixed smooth functions of Euclidean variables $\kappa,x$, normalized with
Lebesgue $L^2$ norms one, with

\[
 \operatorname{supp}F\subset\{|\kappa|<1/4\},\qquad
 \operatorname{supp}f\subset\{5/8<|x|<3/4\},\qquad f(-x)=f(x).
\]

For a specific $f$, take the positive normalization of
$\exp[-1/((|x|-5/8)(3/4-|x|))]$ on that annulus and zero outside.
For a specific $F$ with an explicit derivative bound, set
$p(t)=(1-t^2)^2$ for $|t|<1$, zero otherwise, and let $F_0$ be the
normalized product of $p(8\sqrt3\,\kappa_j)$. Direct integration gives

\[
 \int p^2=256/315,\quad \int(p')^2=256/105,\quad
 \|F_0\|_2=1,\quad\|\partial_{\kappa_a}F_0\|_2=24,
 \quad\operatorname{supp}F_0\subset\{|\kappa|\le1/8\}.
\]

Convolve $F_0$ with the positive, normalized $C^\infty$ radial mollifier
proportional to $\exp[-1/(1-512^2|y|^2)]$ on $|y|<1/512$, zero otherwise,
and normalize the result in $L^2$. Translation in $H^1$ and Minkowski give

\[
 \|\eta_{1/512}*F_0-F_0\|_2\le24\sqrt3/512<1/8,
 \quad\|\partial_{\kappa_a}F\|_2\le192/7,
 \quad\operatorname{supp}F\subset\{|\kappa|\le65/512<1/4\}.
                                                               \tag{B25}
\]

The temporary $\eta_{1/512}$ denotes this mollifier, not the contact bound
$\eta$ in (B22). This construction is smooth; the intermediate polynomial
is used only to supply its derivative constant.

Let $\Pi_{++}(K,q)$ be the product of the two positive one-body projectors,
and define

\[
 u_\lambda(K,q)=(2\pi)^3\lambda^{-3}
           F(K/\lambda)f(q/\lambda)\Pi_{++}(K,q)c,
 \quad Z_\lambda=\|u_\lambda\|,
 \quad\phi_\lambda=u_\lambda/Z_\lambda.                 \tag{B26}
\]

The factor $(2\pi)^3\lambda^{-3}$ compensates both normalized torus
measures and both three-dimensional changes of variables. This is a genuine
normalizable direct-integral packet, not a fixed $K$ fiber or a direction delta.
The even relative envelope and $\mathsf S c=-c$ give the required
antisymmetry. On its support

\[
 \lambda/2\le|q\pm K/2|\le7\lambda/8,
 \quad A=|\sin(q+K/2)|,\ B=|\sin(q-K/2)|\ge3\lambda/8.
\]

For these small arguments $\epsilon(y)\ge(7/8)|y|$. Thus

\[
 \lambda<35\lambda/32\le A+B\le7\lambda/4<2\lambda.
                                                               \tag{B27}
\]

There is no mixed-band cancellation in (B27): the free packet uses only the
positive-positive projector and both individual energies are small. Also

\[
 w_\lambda=\|\Pi_{++}c\|^2
 ={1+\sin(q+K/2)\cdot\sin(q-K/2)/(AB)\over4}
 \in[1/4,1/2].
\]

The positivity follows from the exact numerator identity
$\sin(q+K/2)\cdot\sin(q-K/2)=\epsilon(q)^2-\epsilon(K/2)^2>0$.
Consequently

\[
 Z_\lambda^2=\int |F(\kappa)|^2|f(x)|^2w_\lambda\,d\kappa\,dx
 \in[1/4,1/2].                                           \tag{B28}
\]

For one positive Pauli projector,
$\|\partial_{K_a}\Pi_+\|\le1/(4A)$, and similarly with $B$. Therefore

\[
 \lambda\|\partial_{K_a}\Pi_{++}\|\le4/3,
 \quad
 \lambda\|\partial_{K_a}\phi_\lambda\|
 \le2\|\partial_{\kappa_a}F\|_2+8/3
 \le384/7+8/3<60.                                       \tag{B29}
\]

All $q$ derivatives exist and are square integrable for each $\lambda>0$,
so the packet belongs to the common domain. No uniform $q$-derivative bound
is needed in (B24), because the exact normal ordering has removed derivatives
of the input in $q$. Both global normalization constants $Z_\lambda,n_\lambda$
are scalars depending on $\lambda$, not functions differentiated in $K$.

Using $\nu_m\le1/4$, $n_\lambda\ge1/2$, (B29), and
$\lambda^3\le\lambda^{3/2}$, (B24) gives the first two bounds of (B4).
For the energy bound, $\langle c,H_0c\rangle=0$, (B27), and support-volume
Cauchy–Schwarz give

\[
 \|CH_0\phi_\lambda\|\le2\lambda\eta,
 \quad
 {\lambda-4\lambda\eta^2\over n_\lambda^2}
 \le\langle\chi_\lambda,H_D\chi_\lambda\rangle
 \le{2\lambda+4\lambda\eta^2\over n_\lambda^2}.
                                                               \tag{B30}
\]

Since $\eta^2\le\lambda^3/16$, these lie inside $[\lambda/2,3\lambda]$
on the stated range. This completes the prepared-state construction.

## 8. A restricted failure: small total energy is not enough

At $q_0=(\pi/4,0,0)$, $K=(t,0,0)$, take the free $(+,-)$ band. Its
individual energies tend to $1/\sqrt2$, while its total energy and the
free $x,x$ multiplier defect are exactly

\[
 E(t)=\sqrt2\sin(t/2),\qquad
 (\ell_x-H_0)_{+,-}
 =-\sqrt2\sin t\cos(t/2)-\sqrt2\sin(t/2).
\]

Thus the defect divided by $t$ tends to $-3/\sqrt2$, and divided by the
small total energy tends to $-3$. A point in momentum space is not a
normalizable counterexample; the following packets give one.

Choose fixed smooth normalized envelopes $F_*(\kappa)$ in the ball of radius
$1/64$ about $(1/8,0,0)$, and $f_*(x)$ in a ball of radius $1/64$.
For example the positive normalized standard radial bumps used above, after
these translations and dilations, suffice. Let
$\tau=|+x\rangle\otimes|+x\rangle$. On the patch $q=q_0+\lambda x$, set

\[
 v_\lambda=Z_*^{-1}(2\pi)^3\lambda^{-3}
       F_*(K/\lambda)f_*((q-q_0)/\lambda)\Pi_{+,-}(K,q)\tau.
\]

Here $Z_*$ is the global norm of the numerator in this definition, so
$\|v_\lambda\|=1$. The individual bands are uniformly separated
from zero on this patch, $\Pi_{+,-}\tau\to\tau$ uniformly, and $Z_*\to1$.
The two patches near $q_0,-q_0$ are disjoint. Hence

\[
 \phi^*_\lambda(K,q)
 ={v_\lambda(K,q)-\mathsf S v_\lambda(K,-q)\over\sqrt2}
\]

is exactly normalized and antisymmetric. Exchange changes $(+,-)$ to $(-,+)$
on the second patch and preserves the same energy. Its $K$ support obeys
$|K|<\lambda/4$, its relative support has volume $O(\lambda^3)$, and
$\lambda\|\partial_K\phi^*_\lambda\|$ is bounded. Prepare the actual
allowed state $\chi^*_\lambda=P\phi^*_\lambda/\|P\phi^*_\lambda\|$.

Uniform Taylor expansion on these fixed scaled supports gives

\[
 E(K,q)/\lambda\to\kappa_x/\sqrt2,
 \qquad
 (\ell_x-H_0)_{+,-}(K,q)/\lambda\to-3\kappa_x/\sqrt2.
                                                               \tag{B31}
\]

For instance at general nearby $q$, the first-order coefficient is
\[
 (\cos2q_x-1)\kappa\cdot\nabla\epsilon(q)
 -2\kappa_x\sin2q_x\epsilon(q).
\]
It tends to the displayed value at $q_0$. The two-patch limit is the same
by exchange.

The finite-rank estimates in (B21) used only support volume and the same
small-$K$ bounds, so their contribution is still $O(\lambda^{3/2})$.
The global contact-tail multiplier contribution is also $O(\lambda^{3/2})$.
Removing the outer contact projection from $M_x\phi^*_\lambda$ costs only
$O(\lambda^{5/2})$, because $M_x\phi^*_\lambda=O(\lambda)$ with the same
small support. Thus this normalized, globally projected family satisfies

\[
 \lim_{\lambda\downarrow0}{\|R_{xx}\chi^*_\lambda\|\over\lambda}
 ={3\over\sqrt2}
     \left(\int\kappa_x^2|F_*(\kappa)|^2d\kappa\right)^{1/2}>0,
 \quad
 {\langle\chi^*_\lambda,H_D\chi^*_\lambda\rangle\over\lambda}
 \longrightarrow{1\over\sqrt2}\int\kappa_x|F_*|^2d\kappa>0.
                                                               \tag{B32}
\]

For the energy expectation, the same support argument bounds the projection
correction by $O(\lambda^4)$; the packet's free total energy is $O(\lambda)$.
This construction is outside the $(+,+)$, low-individual-momentum preparation
in Section 7 and outside the central timelike shell condition $E>|K|$.
It does not refute that theorem or supply a general obstruction for other
preparations. It refutes the replacement of its actual premises by “small
total energy and small total momentum.”

## 9. Finite evidence, provenance and remaining obligations

`boost_current/exact_controls.py` builds three-dimensional relative Fourier
polynomials with all four spin entries and quadratic $K$-Taylor jets, using
exact Gaussian rational arithmetic. Its left side forms $D_0$ directly from
the four terms $X_ih_i,h_iX_i$ in (B6), then takes the nested compressed
commutators. Its right side uses (B12)–(B14). All nine components agree exactly;
the three current identities and three $A_b$ identities also agree. A finite
polynomial has the exact nonzero $A_0$ norm squared
$8619295744/75418890625$. The remaining controls check the rational constants,
the envelope integrals and the mixed-channel leading symbol. The first full
execution exited zero with 23 assertion families; its complete output is
`boost_current/first_run.log`.

The separate `boost_current/axis_witness_control.py` uses $4\times4$ Pauli
matrices and exact circle moments, without that Fourier/jet implementation.
It checks the six identities supporting (B17)–(B18), including the exact
singlet-component squared norm $3\sin^2K_b$. Its first execution exited zero;
the complete output is `boost_current/axis_witness.log`. These distinct
calculational representations help detect normalization and sign errors.
Both are this derivation author's controls, not independent scientific review,
and neither proves the support estimates or the asymptotic packet claims by
numerics. Those arguments are given above. No numerical continuum extrapolation
is substituted for them.

A preliminary tool experiment found that the installed exact
`GaussianRational` type has no `.conjugate()` method; the helpers therefore
form conjugates from its real/imaginary rational fields. That setup error
preceded the saved helpers. No scientific failed run or counterexample was
discarded: the first full saved runs both succeeded, and the mixed-band and
unbounded differential-coefficient limitations are retained explicitly.

Exact note/helper/log/source identities and first-run outcomes are recorded
in `boost_current/receipt.json`; `boost_current/checkpoint.json` is the current
recovery pointer. The source files named in Section 1 remain unchanged.

The result addresses one necessary boost/current comparison, not the full
Poincaré or hypersurface-deformation algebra. RC C3's exact regular local
single-scalar obstruction is not being transplanted to this two-record,
spinful, interacting model, nor is its converse being inferred from (B24).
Interband terms, contact corrections and the derivative term have actually
been computed here. Rotational/dipole commutators, gravitational constraints,
density-improvement freedom and an exact closing algebra remain outside this
calculation.

In particular, the current estimate from the earlier walk sources does not
control the unbounded dipole. To extend (B24) to the actual states
$e^{-itH_D}\chi_\lambda$, one must control their differentiated $K$ profiles
and their form-factor overlaps, including any dressing outside the initial
free support. An undifferentiated small state-norm error does not provide
that information; $[H_D,J_b]\partial_{K_a}$ in (B14) can magnify a derivative
error. No fixed-time or growing-time stability of this preparation class,
boost drift bound, new native law, or exact GR conclusion follows from the
prepared-state theorem alone.


# Part II — Growing-time boost/current control

Source date: 2026-10-11. Root-authored conditional extension, with a completed selective independent source review. No physical axiom or audit status is changed.

## Exact premise and claim

The premise is the complete 744-line
`EXCLUDED_WALK_BOOST_CURRENT_PROBE.md`, SHA-256
`903261f54d72d6e81d0c82d5cd976bd4dd46a55c1dd4567fe23d8bce07fe1923`.
Root read and reconstructed its whole argument, all 319 lines of the Fourier
control, the separate 74-line Pauli control, and both full logs. Its exact
normal form and preparation are used here; this is not a claim that its
author controls independently certify the premise. The canonical parent
source and original source revisions remain those pinned in that probe.

Use its common smooth domain, fixed contact projection P, H=PH0P,
A_b=[H,J_b], B_ab, and

    R_ab = -i[D_a,J_b] - delta_ab H
         = delta_ab P M_a P + A_b partial_Ka + B_ab,
    M_a = ell_a-H0.                                      (E1)

The section-7 free packet phi_lambda is globally normalized, supported at
|K|<=lambda/4 and in the origin relative cone, and has

    B_a := lambda ||partial_Ka phi_lambda|| < 60.

Set n=||P phi_lambda||, chi=P phi_lambda/n and
psi(t)=exp(-itH)chi. The norm n is one scalar over the entire direct integral.
For 0<lambda<=1/16, all t>=0 and every a,b, the conditional extension is

    ||R_ab psi(t)|| <= lambda^(3/2) (384+1129 t+18 lambda t^2),  (E2)
    ||[H,J_b]psi(t)|| <= lambda^(5/2) (6+18t).                  (E3)

In particular, for each fixed 0<=gamma<1/2,

    sup_{0<=t<=lambda^(-gamma)} ||R_ab psi(t)||
        <=1536 lambda^(3/2-gamma)=o(lambda).                    (E4)

The actual energy expectation stays in [lambda/2,3lambda] by conservation. This is not a spectral-support statement. The comparison
with the energy scale remains nonvacuous during this growing physical-time
interval. This proves control on the evolved states themselves if the
explicit proof below; it does not claim that they remain corner
supported or have the same derivative norm as the initial free packet.

## Uniform operator and propagator estimates

All operations preserve the small K support. On that support the premise's
form-factor table also gives, without a relative-momentum support assumption,

    ||A_b|| <=12 lambda,  ||B_ab|| <=24,  ||M_a|| <=8.           (E5)

Indeed apply ||u><v||<=||u||_2||v||_2 and use ||v||_2<=||v||_infinity
for the normalized torus. The same term sums in B12/B13 are respectively
(85/8)lambda<12lambda and
17+(39/8)lambda+(5/32)lambda^2<24. The original supported-input estimates
are stronger by the support-volume factor; (E5) does not use that factor.
Consequently, for any allowed H1 section w on the K chart,

    ||R_ab w|| <=32||w||+12lambda||partial_Ka w||.              (E6)

The fixed P is K-independent. Thus ||partial_Ka H||<=1, since each of the
two free one-body derivatives has norm at most 1/2. For U(t,K)=exp(-itH(K)),
the bounded-operator Duhamel derivative gives

    partial_Ka U(t)=-i integral_0^t U(t-s)(partial_Ka H)U(s) ds,
    ||partial_Ka U(t)||<=t.                                  (E7)

The same estimate holds for U0(t)=exp(-itH0). It is valid fiberwise uniformly
in K, and then on the direct integral. Differentiating smooth sections gives
||partial_Ka(U0(t)phi)||<=||partial_Ka phi||+t||phi||.

There is no unproved dipole-domain propagation hidden here. Multiplication
by H0 and the fixed projection P preserve smooth sections compactly supported
in K and periodic in q. Their commutators with each q derivative, and their
K derivatives, are bounded on L2, with bounded higher derivatives. Duhamel
and iteration therefore preserve each finite Sobolev order for each finite
t. Equivalently one may first work on smooth sections and use the H1 bound
to extend (E1). No self-adjoint extension or exponentiation of D is used.

## A comparison retaining the contact forcing

Let eta=nu_m lambda^(3/2), with the source's nu_m<=1/4. Define

    f(t)=U0(t)phi_lambda,
    alpha(t,K)=<c,f(t,K)>,
    v(t)=P f(t)/n,
    w(t)=psi(t)-v(t).                                       (E8)

The free evolution preserves the relative support and the global norm of
phi. The projected comparison v need not have unit norm at later times;
we retain the same initial scalar n everywhere. Full-torus Cauchy-Schwarz
and (E7) give

    ||alpha(s)||_{L2_K}<=eta,
    ||partial_Ka alpha(s)||_{L2_K}<=eta(B_a/lambda+s).          (E9)

In the second bound partial_Ka f has the same support as f. The contact
coefficient is a bounded linear functional on each relative fiber, so the
derivative commutes with its integral. Smooth compact support justifies the
calculation; approximation then gives the corresponding H1 statement.

Since h=H0 c and PH0C f=h alpha, direct differentiation gives

    i partial_t v=H v+h alpha/n,
    w(0)=0,
    w(t)= i/n integral_0^t U(t-s)h alpha(s) ds.                (E10)

This sign can be checked from i partial_t(psi-v)=H(psi-v)-h alpha/n.
The norm estimates do not discard the forcing or suppose the projected
comparison solves the interacting equation.

Using ||h||<=3 and ||partial_Ka h||<=lambda/8,

    ||w(t)||<=3 eta t/n,                                    (E11)
    ||partial_Ka w(t)||
       <= eta/n (3t^2+3B_a t/lambda+lambda t/8).              (E12)

For (E12), differentiate all three factors U(t-s), h, alpha(s).
Their integrated bounds are respectively 3eta t^2/2,
lambda eta t/8, and 3eta(B_a t/lambda+t^2/2), divided by n.
This is explicit derivative control, not an inference from the small
undifferentiated error (E11).

## Applying the full bracket to the evolved state

For the free comparison f(t), the scaled derivative bound is
B_a+lambda t. Repeating B21-B24 of the premise without changing the
normalizing denominator to ||P f(t)|| yields

    ||R_ab v(t)||
       <=[4lambda^3+eta(32+12B_a+12lambda t)]/n.              (E13)

In detail A and B annihilate c, as do their relevant right form factors,
so their input can be f(t) or its K derivative. The multiplier term must
retain the global contact tail and is bounded by 4lambda^3+8eta.
No actual-evolution support restriction is imposed on w.

Combining (E6), (E11)-(E13) gives the more general explicit bound

    ||R_ab psi(t)|| <= 1/n [4lambda^3 + eta {
       32+12B_a+(96+36B_a+12lambda+(3/2)lambda^2)t
       +36lambda t^2 }].                                   (E14)

Use n>=1/2, eta<=lambda^(3/2)/4, B_a<=60, and lambda<=1/16.
The constant term is at most (8+376)lambda^(3/2); the linear coefficient
inside the braces is less than 2257, hence its contribution is at most
1129t lambda^(3/2). The quadratic contribution is 18lambda t^2 lambda^(3/2).
This proves (E2). For t<=lambda^(-gamma), gamma<=1/2, lambda t<=1,
so 18lambda t^2<=18t and 384+1147t<=1531lambda^(-gamma).
The relaxed integer 1536 gives (E4); strict gamma<1/2 makes it o(lambda).
At gamma=1/2 this argument gives only O(lambda), not the little-o conclusion.

For the bounded current commutator, the supported-input bound and (E5)
instead give

    ||A_b psi(t)|| <=12nu_m lambda^(5/2)/n
                     +12lambda(3eta t/n),                   (E15)

which proves (E3). A consequence for the same actual evolving state is

    |<J_b>_{psi(t)}-<J_b>_chi|
         <=lambda^(5/2)(6t+9t^2).                           (E16)

Here d<J_b>/dt=i<[H,J_b]> follows for bounded H and J_b, and integration
uses (E3) with the evolving unit vector. This is a bound on the canonical
current already identified by the source, not a new momentum definition.

## Limits and next check

The supplied excluded walk, its clock, physical projection, canonical energy
placement, smooth positive-positive origin-cone preparation, and scaled
derivative bound remain premises. The result controls one boost/current
bracket and its actual finite-time evolution; it does not supply boost/boost
closure, a gravity constraint algebra, a law for many particles, or a
uniform operator estimate on an unrestricted energy window. The mixed-band
counterexample and nonzero differential coefficient in the premise remain
unchanged. Higher time scales require a stronger estimate; none are excluded.

No finite computation proves the Hilbert-space estimates above. A selective
review must check the fixed global normalization, the contact-forcing sign,
propagator differentiation, all three differentiated factors, the global
versus supported form-factor bounds, and the time/error powers. This draft
does not silently upgrade the original source's prepared-state-only status.


# Part III — Boost/boost contact correction and rotation domains

Date: 2026-10-11. External bounded derivation, not a repository publication.

**Status:** proposed conditional mathematical result; author completion and
cold read recorded in boost_rotation/receipt.json, independent review
pending. The supplied walk, continuous clock, antisymmetric pair sector,
site exclusion, spatial coordinates and canonical symmetric energy placement
remain premises. No physical continuous rotation group, full Poincare
algebra, collision clock or gravitational dynamics is inferred.

The estimate is at the specified prepared states. No persistence of their
derivative or support bounds under excluded evolution is asserted.

## 1. Result and source boundary

For the dipoles D_a defined below, the complete boost/boost bracket is

\[
 i[D_a,D_b]
   =P\mathcal M^{\rm lat}_{ab}P
     +i\left(Q_a\partial_{K_b}-Q_b\partial_{K_a}\right),
 \qquad Q_a=|h_a\rangle\langle h|+|h\rangle\langle h_a|.
                                                        \tag{BR1}
\]

The two second-K-derivative contact terms cancel. The remaining first
derivatives in BR1 must be retained. The free first-order expression
\(\mathcal M^{\rm lat}\) has the exact periodic orbital coefficients
\(\sin k_a\cos k_a\) and face-spin coefficients \(\cos k_a\cos k_b\).
Its one-body formula is matched prior art, identified in Section 10.
The contact formula and quantitative globally projected comparison are the
new derivation here.

On smooth origin-cone free preparations \(\phi_\lambda\) with
\(|K|\le\lambda/4,\ |q|\le3\lambda/4,\ \|\phi_\lambda\|=1\), put

\[
 B_j=\lambda\|\partial_{K_j}\phi_\lambda\|,\qquad
 V_j=\lambda\|\partial_{q_j}\phi_\lambda\|,\qquad
 \chi_\lambda=P\phi_\lambda/\|P\phi_\lambda\|.
                                                        \tag{BR2}
\]

All norms include both normalized measures. For the specified smooth
positive-positive family in Section 8, \(B_j<60,\ V_j<2^{18}\).
With \(0<\lambda\le1/16\), the proof gives for all a,b

\[
 \boxed{
 \|(i[D_a,D_b]-\mathcal M^{\rm chart}_{ab})\chi_\lambda\|
       \le 2^{17}\lambda^{3/2}.
 \ }                                                    \tag{BR3}
\]

Here \(\mathcal M^{\rm chart}\) is the ordinary orbital-plus-spin expression
in the origin chart, not an asserted global physical rotation generator.
A smooth periodic auxiliary comparator agrees with it exactly on these
prepared states. Both the global contact tail and the chart-boundary issue
are treated explicitly below. BR3 is a statewise norm estimate on the
derivative-bounded class, not an unrestricted L2 operator-norm limit.

The frozen sources used are:

| Source | SHA-256 | Role |
|---|---|---|
| EXCLUDED_WALK_BOOST_CURRENT_PROBE.md | 903261f54d72d6e81d0c82d5cd976bd4dd46a55c1dd4567fe23d8bce07fe1923 | Complete B1–B32 source freshly read; model, domain, contact blocks, global normalization and specified smooth ++ preparation |
| EXCLUDED_WALK_CANONICAL_CURRENT_DRAFT.md | 79bc9fb3b9fd9b703f12de0a4ca4ebd62644c81bd6e15c07f723b6b7a1c977fe | Complete 190-line source freshly read; actual local density and energy dipole, not just its current formula |
| Published low-energy energy-current parent | 9f551fc8d3592e83d15a007495a8f9165a5ddb9bc1e98d9dd3f51b6a2584f401 | Lines 1–175, 370–478 and 805–844 freshly read; supplied fibers, all-corner distinction, canonical dipole and projection caveat |
| ROOT_EXCLUDED_WALK_BOOST_CURRENT_REVIEW.md | c019d73e57462fd5e71ff3dc0552cc49fdcf02f604184e6c779ffc7e5dacd300 | Complete independent review of the frozen B source; not independent review of this new derivation |

Paths and precise reading/search coverage are bound in boost_rotation/.
The evolving boost/current draft at
d89611986626dbabcf6f9f5c487733d2a520cb9249b7ed0b3a27be35874fd929
is an identity guard and scope context only. Its time bounds are not used
as a theorem for this new bracket. No new external literature theorem is
invoked. Existing elementary Pauli, integration-by-parts and Sobolev
calculations are supplied explicitly.

## 2. Supplied Hilbert space, placement and common domain

Fix \(U=\{K\in\mathbb R^3:|K|<1/8\}\) inside the origin total-momentum
chart and use the full relative torus \(\mathbb T^3\), with measures
\(dK/(2\pi)^3\) and \(dq/(2\pi)^3\). The stated K supports are compact
in this chart for the entire range \(0<\lambda\le1/16\).
The spin space is \(\mathbb C^2\otimes\mathbb C^2\), with swap \(\mathsf S\).
Antisymmetry means
\(\psi(K,-q)=-\mathsf S\psi(K,q)\). The normalized constant singlet is c.
Set

\[
 C=|c\rangle\langle c|,\quad P=I-C,\quad
 k_1=K/2+q,\quad k_2=K/2-q,
\]
\[
 h_i=\sigma_i\cdot\sin k_i,\quad H_0=h_1+h_2,\quad
 H_D=PH_0P,\quad h=H_0c,\quad h_a=\partial_{K_a}h .
                                                        \tag{BR4}
\]

P is one global contact projection in each full-torus fiber, not one
projection per cone. No exchange multiplicity or half-torus normalization
is inserted. The trigonometric symbols are periodic even where their
displayed lifted arguments cross a torus face.

The selected local density and energy first moment are

\[
 e_x^0=\tfrac12\sum_{i=1}^2\{\Pi_{i,x},h_i\},\qquad
 e_x=Pe_x^0P,\qquad
 D_a=PD_{0,a}P,\quad
 D_{0,a}=\tfrac12\sum_{i=1}^2\{X_{i,a},h_i\}.
                                                        \tag{BR5}
\]

These agree with the finite-spatial-support first moments. Our common
test domain consists of smooth antisymmetric sections, compactly
supported in U, smooth periodic in q, and lying in P. D_a preserves
this domain, so both products in [D_a,D_b] are defined. Ambient D0 acts
on the corresponding domain without the P restriction.

The individual derivatives are
\(X_{1,a}=i(\partial_{K_a}+\partial_{q_a}/2)\) and
\(X_{2,a}=i(\partial_{K_a}-\partial_{q_a}/2)\). Thus

\[
 D_{0,a}=iH_0\partial_{K_a}
       +\tfrac i2(h_1-h_2)\partial_{q_a}
       +i\partial_{K_a}H_0.                             \tag{BR6}
\]

All its coefficients are smooth periodic in q. Products of dipoles
map H2 to L2 continuously on compact K supports; after the cancellation
below their commutator expression extends continuously H1 to L2.
The latter is the extension of the common-core expression, not a claim
that each individual product is defined on every H1 section.
No essential self-adjointness or exponentiation of the dipoles is assumed.

## 3. Free bracket, signs and spin term

For one body let \(s_j=\sin k_j,\ c_j=\cos k_j\) in this section only, and
write \(d_a=i(h\partial_a+h_{,a}/2)\), with \(h=\sigma\cdot s\).
For a different pair of axes a,b, direct multiplication gives

\[
 [d_a,d_b]
  =-\tfrac12\{h,h_{,a}\}\partial_b
   +\tfrac12\{h,h_{,b}\}\partial_a
   -\tfrac14[h_{,a},h_{,b}].                            \tag{BR7}
\]

The h-squared second derivatives cancel. The constant second-symbol
derivatives cancel by equality of mixed derivatives. Pauli algebra gives
\(\{h,h_{,a}\}/2=s_ac_a I\) and
\([h_{,a},h_{,b}]=2i\epsilon_{abd}\sigma_dc_ac_b\).
Operators on the two individual particles commute. Consequently

\[
 i[D_{0,a},D_{0,b}]=\mathcal M^{\rm lat}_{ab}
 =-i\sum_{i=1}^2
   (j_{i,a}\partial_{k_{i,b}}-j_{i,b}\partial_{k_{i,a}})
  +\tfrac12\epsilon_{abd}
      \sum_{i=1}^2\sigma_{i,d}\cos k_{i,a}\cos k_{i,b},
\quad j_{i,a}=\sin k_{i,a}\cos k_{i,a}.                  \tag{BR8}
\]

Repeated d is summed; a,b are fixed. The a=b expressions are zero.
The sign is the convention \([D_a,D_b]=-i\mathcal M_{ab}\).
At the origin the spin term tends to
\(\epsilon_{abd}(\sigma_{1,d}+\sigma_{2,d})/2\).

In K,q coordinates define

\[
 g_a=\sin K_a\cos(2q_a),\qquad
 w_a=\tfrac12\cos K_a\sin(2q_a),\qquad
 S^{\rm lat}_{ab}=
 \tfrac12\epsilon_{abd}\sum_i\sigma_{i,d}\cos k_{i,a}\cos k_{i,b}.
\]

Then the fully periodic free expression is

\[
 \mathcal M^{\rm lat}_{ab}
 =-i(g_a\partial_{K_b}-g_b\partial_{K_a}
                   +w_a\partial_{q_b}-w_b\partial_{q_a})
      +S^{\rm lat}_{ab}.                               \tag{BR9}
\]

These orbital vector fields have zero divergence for a different from b.
Their periodicity, not an assumption of continuous lattice rotations,
justifies the q integration by parts on the full common core.

## 4. Exact compression defect

The singlet has zero expectation of H0. In BR6, the fiber adjoint of
\(i(h_1-h_2)\partial_{q_a}/2+i\partial_{K_a}H_0\) is
\(i(h_1-h_2)\partial_{q_a}/2\), which annihilates c.
Acting on c before taking the adjoint instead gives ih_a. Thus the
off-diagonal contact blocks are, including every K derivative,

\[
 CD_{0,a}P\psi=ic\langle h,\partial_{K_a}\psi\rangle,\qquad
 PD_{0,a}C(cf)=i\partial_{K_a}(hf).                      \tag{BR10}
\]

Expand the two compressed products:

\[
 [D_a,D_b]
  =P[D_{0,a},D_{0,b}]P-PD_{0,a}CD_{0,b}P
                                +PD_{0,b}CD_{0,a}P.
\]

On an allowed test section their last two terms are exactly

\[
 \partial_{K_a}\bigl(h\langle h,\partial_{K_b}\psi\rangle\bigr)
 -\partial_{K_b}\bigl(h\langle h,\partial_{K_a}\psi\rangle\bigr).
                                                        \tag{BR11}
\]

Expanding BR11 gives \(Q_a\partial_{K_b}\psi-
Q_b\partial_{K_a}\psi\); the two copies of
\(h\langle h,\partial_{K_aK_b}\psi\rangle\) cancel.
There is no constant contact term because the inner blocks in BR10
contain only a first derivative of the state. This proves BR1.
As a consistency check,
\(Q_a=\partial_{K_a}|h\rangle\langle h|\), so
\(\partial_{K_b}Q_a-\partial_{K_a}Q_b=0\); the displayed correction
in i[D_a,D_b] has the expected symmetry on the common domain.

The exact form factors are

\[
 h=2\sum_j\cos(K_j/2)\sin q_j\,\sigma_{1,j}c,\qquad
 h_a=-\sin(K_a/2)\sin q_a\,\sigma_{1,a}c.                \tag{BR12}
\]

They lie in P. In particular Q_a annihilates c. BR1 does not assert
that the compressed angular expression is conserved by H_D or closes
the other rotation/boost brackets.

## 5. Ordinary chart expression and the torus issue

On the fundamental cell \(q\in(-\pi,\pi)^3\), the ordinary origin-chart
orbital-plus-spin expression is

\[
 \mathcal M^{\rm chart}_{ab}
 =-i(K_a\partial_{K_b}-K_b\partial_{K_a}
                   +q_a\partial_{q_b}-q_b\partial_{q_a})
  +\Sigma_{ab},\qquad
 \Sigma_{ab}=\tfrac12\epsilon_{abd}(\sigma_{1,d}+\sigma_{2,d}).
                                                        \tag{BR13}
\]

The q coordinates in BR13 are bounded representatives, not smooth global
functions on the torus. This gives a well-defined H1-to-L2 expression
on that chosen cell. For a different from b it is symmetric on smooth
periodic sections with compact K support: a coefficient q_a is independent
of its differentiation variable q_b, whose two periodic face terms
cancel, and conversely. This observation does not make it a smooth
global rotation vector field or establish a group representation.

There is a concrete loss of the common smooth/H1 core. Choose a nonzero
smooth radial K envelope G, compact in U, and
\(\psi=G(K)c\cos q_a\). This is antisymmetric and lies in P.
For a different from b, its q contribution under BR13 is
\(-iG(K)c\,q_b\sin q_a\). Its two q_b face traces differ by
\(-2\pi iG(K)c\sin q_a\). Hence the image is not in H1 of the torus.
The expression cannot be silently treated as preserving the full
periodic dipole core. This witness concerns this chart expression and
this core; it is not an obstruction to every restricted domain or
approximate rotation construction.

For a smooth periodic auxiliary comparison, fix a smooth even cutoff
\(\rho(t)=1\) on \(|t|\le1\) and \(\rho(t)=0\) on \(|t|\ge2\) inside
\((-\pi,\pi)\), and put \(\tau(t)=t\rho(t)\), periodically extended.
For definiteness, with \(\theta(u)=e^{-1/u}\) for u>0 and zero otherwise,

\[
 \rho(t)={\theta(4-t^2)\over\theta(4-t^2)+\theta(t^2-1)}.
\]

Define the auxiliary operator

\[
 \mathcal M^{\rm aux}_{ab}
 =-i(K_a\partial_{K_b}-K_b\partial_{K_a}
                +\tau(q_a)\partial_{q_b}-\tau(q_b)\partial_{q_a})
       +\Sigma_{ab}.                                   \tag{BR14}
\]

It preserves the common smooth domain and antisymmetry. Its q orbital
field has zero divergence, and \(\Sigma_{ab}c=0\). Fiber integration
therefore gives
\(C\mathcal M^{\rm aux}\psi=\mathcal M^K C\psi\), where
\(\mathcal M^K=-i(K_a\partial_{K_b}-K_b\partial_{K_a})\).
Also \(\mathcal M^{\rm aux}(c\alpha)=c\mathcal M^K\alpha\).
Thus it commutes with P on this domain.

On a free packet supported in \(|q|<3\lambda/4<1\), BR14 and BR13
agree. They also agree on its global contact subtraction \(c\alpha(K)\),
since that subtraction has no q derivative and its spin term vanishes.
Consequently

\[
 \mathcal M^{\rm aux}_{ab}\chi_\lambda
       =\mathcal M^{\rm chart}_{ab}\chi_\lambda
 \quad\hbox{exactly}.                                  \tag{BR15}
\]

The image in BR15 is smooth periodic: its nonconstant q part is supported
away from the faces. No continuous rotation symmetry, global Lie-group
action or uniqueness of this auxiliary continuation is claimed.

## 6. Quantitative free and contact estimates

Let \(0<\lambda\le1/16\) and use the support in BR2. Define

\[
 \nu_1=\sqrt{9/(128\pi^2)},\qquad \eta=\nu_1\lambda^{3/2}.
                                                        \tag{BR16}
\]

The relative support's normalized volume is at most \(\eta^2\).
Write \(\alpha(K)=\langle c,\phi_\lambda(K)\rangle\) and
\(n=\|P\phi_\lambda\|\). Cauchy–Schwarz, also for a K derivative, gives

\[
 \|\alpha\|\le\eta,\quad
 \|\partial_{K_j}\alpha\|\le\eta B_j/\lambda,\quad
 n^2=1-\|\alpha\|^2\ge1-\eta^2,\qquad
 \chi_\lambda=(\phi_\lambda-c\alpha)/n.                  \tag{BR17}
\]

This is one global normalization over K and q. In particular n is
not differentiated in K. The contact subtraction occupies the full torus.

Put \(V_{ab}=\mathcal M^{\rm lat}_{ab}-\mathcal M^{\rm aux}_{ab}\);
the symbol V_ab is an operator here, distinct from the derivative norms
V_j in BR2. On the free support, elementary sine/cosine remainders give

\[
 |g_j-K_j|\le {109\over384}\lambda^3<\lambda^3/3,\qquad
 |w_j-q_j|\le {39\over128}\lambda^3<\lambda^3/3,
\]
\[
 \|S^{\rm lat}_{ab}-\Sigma_{ab}\|
       \le {49\over128}\lambda^2 .                     \tag{BR18}
\]

For the first bound use \(|K_j|^3/6+2|K_j|q_j^2\).
For the second use \(2|q_j|^3/3+K_j^2|q_j|/2\).
For the third use
\(|1-\cos k_{i,a}\cos k_{i,b}|
\le(k_{i,a}^2+k_{i,b}^2)/2\) and \(|k_i|\le7\lambda/8\).
The two spin terms each have the prefactor 1/2. Therefore, with

\[
 C_{ab}={49\over128}
             +{B_a+B_b+V_a+V_b\over3},
 \qquad \|V_{ab}\phi_\lambda\|\le C_{ab}\lambda^2.        \tag{BR19}
\]

This estimates the actual state derivatives, not merely the multiplier
symbols.

For the global tail set \(r_j=g_jc\), whose fiber mean is zero and
whose norm is at most \(\lambda/4\). Since the auxiliary spin term
annihilates c and the q derivatives of c alpha vanish,

\[
 PV_{ab}(c\alpha)
   =-i r_a\partial_{K_b}\alpha
      +i r_b\partial_{K_a}\alpha+s_{ab}\alpha,\qquad
 s_{ab}=S^{\rm lat}_{ab}c\in P.                         \tag{BR20}
\]

The constant K coefficients of the auxiliary expression disappear under
the outer P. If \(C_j=\cos(K_j/2)\), \(T_j=\sin(K_j/2)\), then

\[
 s_{ab}=-\epsilon_{abd}\sigma_{1,d}c
 (C_aT_b\cos q_a\sin q_b+T_aC_b\sin q_a\cos q_b).
\]

Thus \(\|s_{ab}\|\le|T_a|+|T_b|\le\lambda/4\), uniformly on the full
torus, and

\[
 \|PV_{ab}(c\alpha)\|
 \le\eta\left({B_a+B_b\over4}+{\lambda\over4}\right).    \tag{BR21}
\]

No corner-support assumption is applied to that output.

Finally, \(\|h\|\le3,\ \|h_j\|\le\lambda/8\) on the full torus,
whereas on the free input support
\(|h(q)|\le3\lambda/2,\ |h_j(q)|\le3\lambda^2/32\).
For any supported f these yield

\[
 \|Q_j f\|
  \le {15\over32}\lambda^2\eta\|f\|,\qquad
 \|(Q_a\partial_{K_b}-Q_b\partial_{K_a})\phi_\lambda\|
 \le {15\over32}\lambda\eta(B_a+B_b).                   \tag{BR22}
\]

The same uniform fiber estimates integrate over K. Since Q_j c=0,
they apply after global projection by dividing by n.

## 7. Prepared-state theorem with every parameter explicit

Combine BR1, commutation of P with BR14, and BR17–BR22. For every
normalized smooth origin-cone preparation in BR2, not necessarily a
positive band vector, the result is

\[
 \boxed{
 \|(i[D_a,D_b]-\mathcal M^{\rm aux}_{ab})\chi_\lambda\|
 \le
 {C_{ab}\lambda^2+
 \nu_1\lambda^{3/2}
   \left((B_a+B_b)/4+\lambda/4+
                      (15/32)\lambda(B_a+B_b)\right)
  \over \sqrt{1-\nu_1^2\lambda^3}} .
 \ }                                                    \tag{BR23}
\]

BR15 identifies this with the chart-expression residual on the prepared
states. All norms and normalizations are global direct-integral ones.
For a=b the exact residual is zero; the uniform estimate is harmless.
For derivative norms bounded independently of lambda this is
O(lambda^(3/2)), in particular o(1) and o(lambda).
It also bounds every normalized test-vector matrix element by
Cauchy–Schwarz. It does not remove the derivative premises.

## 8. The specified smooth, normalizable ++ family

Use exactly the origin family B25–B29 from the frozen boost/current
source. Its K envelope F is the normalized convolution of the L2-normalized
product of \(p(8\sqrt3\,\kappa_j)\), where
\(p(t)=(1-t^2)^2\) on \(|t|<1\) and zero outside, with the normalized
smooth radial bump proportional to
\(\exp[-1/(1-512^2|y|^2)]\) on \(|y|<1/512\).
It obeys \(\|F\|=1,\ |\kappa|\le65/512<1/4\) on its support and
\(\|\partial_{\kappa_j}F\|\le192/7\).
The relative envelope is the positive L2 normalization of

\[
 f(x)\ \propto\
 \exp\!\left[-{1\over (|x|-5/8)(3/4-|x|)}\right],
 \qquad 5/8<|x|<3/4,                                  \tag{BR24}
\]

extended by zero. It is smooth, radial and even. Let

\[
 u_\lambda=(2\pi)^3\lambda^{-3}
      F(K/\lambda)f(q/\lambda)\Pi_{++}(K,q)c,\qquad
 Z_\lambda=\|u_\lambda\|,\quad \phi_\lambda=u_\lambda/Z_\lambda.
                                                        \tag{BR25}
\]

The prefactor compensates both normalized torus measures and both
three-dimensional rescalings. The packet is a normalizable antisymmetric
direct-integral state. Both individual momenta lie between lambda/2 and
7lambda/8 in length, their positive sine energies A,B are at least
3lambda/8, and their sum lies in [lambda,2lambda].
Its singlet ++ weight lies in [1/4,1/2], hence
\(Z_\lambda\in[1/2,1/\sqrt2]\). These are the same pointwise bounds and
global normalization proved in B26–B28, whose full argument was read.

For completeness the needed additional q derivative has an explicit
constant. Put \(r_0=11/16,\ u=16(r-r_0)\) and
\(g(u)=\exp[-256/(1-u^2)]\). On \(|u|\le1/32\),
\(g(u)^2\ge e^{-513}\), so
\(\int_{-1}^1g^2du\ge e^{-513}/16\). With
\(y=1/(1-u^2)\ge1\),
\[
 |g'(u)|^2=512^2u^2y^4e^{-512y}
       \le512^2e^{-512},
\]
because \(y^4e^{-512y}\) decreases for y>=1.
Consequently
\[
 {\int(g')^2\over\int g^2}\le32e\,512^2<96\,512^2.
\]
Radial symmetry, \(5/8\le r\le3/4\), and dr=du/16 now give

\[
 \|\partial_{x_j}f\|^2
  ={1\over3}{\int r^2|g_r'|^2dr\over\int r^2g^2dr}
  <{1\over3}{36\over25}\,16^2\,96\,512^2
   ={18\over25}2^{32}<2^{32}.                          \tag{BR26}
\]

The elementary inequality e<3 follows, for example, by bounding the
exponential series tail after 1+1 by a geometric series.
For a positive Pauli projector,
\(\|\partial_{q_j}\Pi_+\|\le1/(2A)\), and similarly with B.
The product derivative therefore obeys
\(\lambda\|\partial_{q_j}\Pi_{++}\|\le8/3\).
Using the one global Z_lambda gives

\[
 B_j\le384/7+8/3<60,\qquad
 V_j\le2\|\partial_{x_j}f\|+16/3<2^{18}.                \tag{BR27}
\]

All higher derivatives exist for each positive lambda, so the actual
projected state belongs to the commutator's common domain. Its energy
expectation remains in [lambda/2,3lambda] by B30; this does not assert
spectral support of the projected state.

In BR23 use \(B_a+B_b\le120,\ V_a+V_b\le2^{19}\),
\(\nu_1<1/4,\ n\ge1/2,\ \sqrt\lambda\le1/4\).
The resulting coefficient of lambda^(3/2) is at most

\[
 2\left[
 {1\over4}\left({49\over128}+{120+2^{19}\over3}\right)
 +{1\over4}\left(30+{1\over64}+{15\over32}{120\over16}\right)
 \right]<2^{17}.                                      \tag{BR28}
\]

This proves BR3 with conservative explicit constants and with the
original specified smooth packet, not a delta direction or fixed K fiber.

## 9. Corners, global tail and scope

The preparation before projection occupies only the origin cone.
The contact subtraction is constant in q and therefore occupies the
whole torus, including all seven other relative corners. BR20–BR22
use full-torus norms of its outputs; its q derivative is zero, rather
than being assumed confined to the origin.

For a genuinely populated different relative corner C in {0,pi}^3,
write q=C+x and \(\varepsilon_j=\cos C_j=\pm1\). The two individual
cone offsets are K/2+x and K/2-x. Their j=sin(k)cos(k) orbital
coefficients have the same leading offsets, but BR8's leading spin is
\[
 \tfrac12\epsilon_{abd}\varepsilon_a\varepsilon_b
                   (\sigma_{1,d}+\sigma_{2,d}).
                                                        \tag{BR29}
\]
It is the spin in that reflected cone frame; the origin spin cannot
be substituted uniformly at all corners. The ordinary q coordinate
in BR13 is likewise not the offset x at another corner. Distinct
total-momentum corners are outside the chosen K chart. Neither the
projection nor low total energy erases these distinctions.

One may construct additional smooth periodic patch comparators, but their
matching, corner spin and derivative hypotheses would have to be stated.
BR3 is only the origin preparation theorem. The failure of the unrestricted
chart expression to preserve H1 does not refute BR3 or an appropriately
specified other-domain construction.

The current and boost/current estimates from the parent do not by
themselves control this boost/boost residual at evolved states. The new
comparison uses q as well as K derivatives, and its global-tail estimate
uses the exact prepared-state decomposition. A norm-only approximation,
or a time interval justified for a different bracket, cannot replace
these premises. No fixed or growing time result is asserted here.

## 10. Prior art, controls and unresolved work

The pinned-main search at a13caa4885f547c8d206265b031ba7649e539fd9
is preserved in boost_rotation/prior_art_search.log. The complete
2026-09-25 note whose title begins “The walk carries an exact boost
charge” was read. Its T3 is matching prior art for BR7–BR9 for one
free walker, and hence for the additive free pair. Its T4 already records
the reflected corner spin. Its scope explicitly excludes excluded records;
its long-wave comparison is formal and does not supply this projected
statewise norm theorem or the torus-domain argument.

The complete 2026-05-30 free Dirac Poincare representation note was also
read. Its supplied continuum free-field/mass-shell algebra is context,
not a proof for this excluded lattice pair or its compressed placement.
The remaining displayed search hits concern coin-frame rotations, other
free carriers, scalar or source conventions, indexes and historical
methodology. Their complete source notes were not all read in this recovery.
The saved search and the two complete matching/context notes establish the
stated local scope comparison, not an exhaustive literature or open-PR
novelty search or independent recertification of those sources.

The distinct exact finite control in
`boost_rotation/exact_rotation_controls.py` forms differential-operator
compositions from a symbolic second Taylor jet of the one-body Pauli symbol.
It also uses a separate four-dimensional compression fixture with a complex,
nonconstant contact form factor. The latter is an abstract realization of
BR10, not a finite-site approximation of the excluded walk. The control
imports none of the earlier Fourier/jet boost-current helper.

Its first complete execution, recorded at 2026-10-11T21:59:16Z, exited zero
and emitted 63 distinct assertion records and `TOTAL: PASS=63 FAIL=0` in
`boost_rotation/first_run.log`. The categories are 12 Pauli-jet checks,
11 abstract-compression checks, 32 corner checks, seven exact constant or
volume checks, and one chart-face-jump check. In-process omission and sign
changes expose missing spin and contact terms. These are not separate
executions of mutated source files or a general tamper certificate.
`boost_rotation/execution.json` binds the command, timeout, source and log.
The unchanged successful calculation was not rerun during recovery.

These are the originating author's controls. They complement the analytic
domain and support estimates; they do not prove a continuum packet limit,
independent review, physical rotation representation or time extension.
Recovery checked the complete derivation, complete control source and full
saved output, and completed this evidence prose. This is author completion,
not an independent audit of the theorem. Exact source identities, reading
limits and the author check are recorded in `boost_rotation/receipt.json`
and `boost_rotation/AUTHOR_COMPLETION.md`.

The initial 589-line candidate and every pre-existing boost_rotation file
are preserved byte-for-byte in
`boost_rotation/recovery_initial_20261011T2202Z/`. Recovery followed reported
context-compaction failures of the originating author; the available first
complete control run succeeded. No failure transcript or compiler run is
inferred from that report.

A separate independent review of this complete new argument remains open.
The fixed supplied placement, band preparation, chart and explicit derivative
norms are part of the theorem, not hidden framework deductions. The precise
core counterexample in Section 5 is retained; neither it nor the scope
stress-test in the author record claims that every rotation construction is
impossible, or that a formal no-go submission packet has passed.


# Part IV — A sharp time threshold for the boost/current norm

2026-10-11. Author research composition by `spectral_edge_recovery`, with the
shorter-time mean-ergodic route suggested by root. Conditional supplied-model
result; selective independent review pending. This document is neither an
independent review of itself nor a framework no-go or audit verdict.

The exact smooth, globally normalized positive-positive origin-cone packets
B25–B30 do give a counterexample to an `o(lambda)` bracket bound at inverse-energy
times. More precisely, write

    R_ab = -i[D_a,J_b] - delta_ab H,
    psi_lambda(t) = exp(-itH) chi_lambda,
    c0 = (2pi)^(-3/2).

For each diagonal component b there is an explicit fixed nonzero vector
Gamma_b in the rescaled direct integral, defined in (T17), such that

    T_lambda R_bb psi_lambda(t_lambda)/(lambda^(3/2) t_lambda)
        -> Gamma_b in L2,
    whenever t_lambda -> infinity and lambda t_lambda ->0.       (T1)

Here T_lambda is an isometry defined in (T7); it does not discard the contact
tail. In particular the residual norm divided by lambda tends to the
positive number `c_b=||Gamma_b||` at `t_lambda=lambda^(-1/2)`. For each fixed
`1/2<gamma<1`, the residual is asymptotic to
`c_b lambda^(3/2-gamma)` at `t_lambda=lambda^(-gamma)`. The prior E4 bound
for `gamma<1/2` is therefore sharp in its power threshold for these packets
and this norm of the diagonal bracket.

For every fixed `0<tau<=1/32768`, a separate direct estimate gives

    liminf_(lambda->0) ||R_bb psi_lambda(tau/lambda)||/sqrt(lambda)
        >= tau c_b/2
        >= c0 (integral f) tau/(18 sqrt(6)) >0,                 (T2)

and a finite upper bound on the corresponding limsup. Thus the norm is
`Theta(sqrt(lambda))` at those fixed small inverse-energy times. No existence
of its exact limit at fixed tau is needed or claimed here. The energy
**expectation** remains in `[lambda/2,3lambda]` by conservation. An evolving
spectral-window assertion is not intended. The conclusion concerns the norm
of this supplied bracket on this preparation, not a current-expectation rate,
a many-body law, or an adopted physical boost law.

## 1. Exact premises, source identities and authorship

All paths below are relative to this external research directory unless
otherwise stated. Sources are preserved byte for byte. The receipt records
complete paths, sizes, hashes, read coverage and the published-memory copy.

| Source | SHA-256 | Role |
|---|---|---|
| `EXCLUDED_WALK_BOOST_CURRENT_PROBE.md` | `903261f54d72d6e81d0c82d5cd976bd4dd46a55c1dd4567fe23d8bce07fe1923` | B5–B30: exact operators, common domain, normal form, specified packet and energy expectation |
| `ROOT_EXCLUDED_WALK_BOOST_CURRENT_REVIEW.md` | `c019d73e57462fd5e71ff3dc0552cc49fdcf02f604184e6c779ffc7e5dacd300` | Prior independent source review; not a review of the new result |
| `EXCLUDED_WALK_EVOLVED_BOOST_CONTROL_DRAFT.md` | `d89611986626dbabcf6f9f5c487733d2a520cb9249b7ed0b3a27be35874fd929` | Root's E1–E16: domain propagation, full contact Duhamel formula, supported free-comparison bound |
| `EXCLUDED_WALK_EVOLVED_BOOST_REVIEW.md` | `9cd540482c4cef79471530223dbbde93d36a6ba0aded1c99becf36a68ae263b9` | This author's prior independent E review; not independent evidence for T1–T24 |
| `boost_current_inverse_energy/sources/PUBLISHED_MEMORY_CURRENT_BOUNDED_THEOREM_NOTE_2026-10-11.md` | `3954606703f9a66665fb1ee9a27079f7f14e5183f28a8511a38743ef5d455aa1` | Prior published derivation of the physical kernel and I0; both are rederived here and are not logical premises |
| `EXCLUDED_WALK_DEGENERATE_DYNAMICS_PROBE.md` | `b8f923be6e50de14ba0bb1a35ccfd71aec7575fd710693535cf0417c76daa876` | D12–D14 bounded current expansion; D8–D11 were examined for the preserved longer route, but are not needed by the main proof |
| `EXCLUDED_WALK_DEGENERATE_DYNAMICS_REVIEW.md` | `c0a788f05c291a900acf3bc1002e139f2c0eba749ee6cdc7b08c6bf4812dc9a2` | Prior review of the fixed-vector gapless limit; not a license to apply it to arbitrary lambda-dependent packets |
| `EXCLUDED_WALK_CANONICAL_CURRENT_DRAFT.md` | `79bc9fb3b9fd9b703f12de0a4ca4ebd62644c81bd6e15c07f723b6b7a1c977fe` | Fixed symmetric energy placement underlying B9; unchanged prior complete coverage reused |

The B source specifies the model and preparation. The memory source records
an earlier derivation of zero-space identities rederived below; its existing
review does not cover this proof. Root authored E and suggested the growing
time `lambda t->0` mean-ergodic route, and then the folded-cube bound on I0.
This author checked that bound, derived the full-torus coupling, rescaled
bracket and forcing, derivative estimates and fixed-tau lower bound, and
wrote the controls. Root's
initial suggestion that a zero-mode phase might matter was a question, not
evidence. No independent review of this composition has yet been performed.

The lattice, pair sector, generator clock, contact rule, total-momentum chart,
canonical local energy placement and preparation are supplied premises. No
registered native primitive is needed or adopted for this dimensionless
conditional calculation. Neither the cited notes' status nor this result is
promoted to formally retained status by the author controls.

## 2. Hilbert space, operators and domains

Take `0<lambda<=1/16`, with indices a,b,j in {1,2,3}. Use the full
relative torus with `dmu=dq/(2pi)^3` and total-momentum measure
`dK/(2pi)^3` in a fixed chart about zero. Spin is `C^2 tensor C^2`. The
normalized constant singlet is c; set `C=|c><c|`, `P=I-C`, and

    h_1=sigma_1.sin(K/2+q),  h_2=sigma_2.sin(K/2-q),
    H0(K,q)=h_1+h_2,  H(K)=P H0(K)P on ran P,
    h(K)=H0(K)c=2 sum_j cos(K_j/2) sin(q_j) T_j,
    h_b(K)=-sin(K_b/2) sin(q_b) T_b,  T_j=sigma_(1,j)c.

Even singlet and odd triplet coefficients implement antisymmetry. There is
no half-torus factor or additional exchange normalization. P is one fixed
full-torus contact projection in each fiber and is independent of K.

For the source's symmetric energy first moment, use the common smooth
antisymmetric domain, periodic in q, compactly supported in K and in ran P:

    D_a=i(H partial_Ka + Dcal_a),
    Dcal_a=P[(H_Delta/2) partial_qa + partial_Ka H0]P,
    H_Delta=h_1-h_2,
    J_b=P[sin K_b cos(2q_b)]P-|h_b><h|-|h><h_b|.              (T3)

`Dcal_a` here is the source B7 fiber differential operator. It is distinct
from the bounded operator `L_b` below. The exact source normal form is

    R_ab = C_ab(K)+A_b(K) partial_Ka,
    A_b=[H,J_b],
    C_ab=delta_ab P(ell_a-H0)P+B_ab,
    ell_a=h_1 cos(2k_(1,a))+h_2 cos(2k_(2,a)).                (T4)

For completeness, the bounded constant contact coefficient is

    r_b=sin K_b cos(2q_b)c,   r_(b,a)=partial_Ka r_b,
    F_b=-|h_b><h|-|h><h_b|,   F_(b,a)=partial_Ka F_b,
    B_ab=-|h_a><r_b|-|h><r_(b,a)|+H F_(b,a)
         -|Dcal_a h_b><h|-|Dcal_a h><h_b|
         +|h_b><Dcal_a^dagger h|+|h><Dcal_a^dagger h_b|,
    Dcal_a^dagger=-P(H_Delta/2) partial_qa P.

All form factors in this formula are smooth. The displayed q derivatives
act only on those form factors, not on the input. Consequently A_b,C_ab are
bounded operators with smooth K dependence, and (T4) extends continuously
from the common domain to sections in `H1_K(L2_q)`. For `|K|<=lambda/4`, the
source bounds, now applied globally in q, give

    ||A_b||<=12lambda,  ||C_ab||<=32,
    ||R_ab w||<=32||w||+12lambda||partial_Ka w||.              (T5)

The source's smaller support-volume estimates must not be applied to a
contact tail or to the actual evolved state. They will be used only for
the free comparison in (T10).

For every fixed lambda and finite physical t, the actual state is in the
common smooth domain: H0 is a smooth multiplier, P is fixed, and all
commutators with q derivatives and all K derivatives are bounded. Duhamel
iteration propagates every finite Sobolev order. Nothing in this proof
requires bounds on those orders uniform in t or lambda, nor exponentiation
or essential self-adjointness of the unbounded D_a.

## 3. The specified normalized packet and its exact contact amplitude

Retain exactly the B25–B30 functions. The nonnegative, smooth, real F has
Lebesgue L2 norm one, support `|kappa|<=65/512<1/4`, and
`||partial_(kappa_b)F||<=M=192/7`. It is obtained by convolving the normalized
product of `p(8sqrt(3) kappa_j)`, where `p(t)=(1-t^2)^2` on `|t|<1`
and is zero outside, with the normalized positive radial mollifier
`exp[-1/(1-512^2|y|^2)]` on `|y|<1/512`, zero outside. One global L2
normalization follows convolution. The source's translation bound gives M.

The real f is the positive Lebesgue L2 normalization of

    exp[-1/((|x|-5/8)(3/4-|x|))],   5/8<|x|<3/4,

and is zero elsewhere. It is even and smooth. Write `m_f=integral f>0`.
Let Pi_++ be the product of the two positive Pauli projectors, and set

    u_lambda=(2pi)^3 lambda^-3 F(K/lambda) f(q/lambda) Pi_++ c,
    Z_lambda=||u_lambda||,  phi_lambda=u_lambda/Z_lambda,
    n_lambda=||P phi_lambda||,  chi_lambda=P phi_lambda/n_lambda. (T6)

Both Z_lambda and n_lambda are global scalars over K and q. They have no K
derivative. These are normalizable smooth packets, with a fixed finite
spread in the rescaled K variable; no direction delta or fixed fiber is
substituted. The physical chi includes the contact subtraction on the
entire relative torus.

For `K=lambda kappa,q=lambda x`, define

    e_lambda=(|sin(lambda(x+kappa/2))|
                     +|sin(lambda(x-kappa/2))|)/lambda,
    w_lambda=||Pi_++(lambda kappa,lambda x)c||^2.

On the support, `1/4<=w_lambda<=1/2`, `1<=e_lambda<=2`, and

    Z_lambda^2=integral |F(kappa)|^2 |f(x)|^2 w_lambda dkappa dx
        in [1/4,1/2].

The six-dimensional Jacobian and `(2pi)^3 lambda^-3` in (T6) cancel exactly.
Define the isometry, extending sections by zero outside the K chart,

    (T_lambda u)(kappa,q)=lambda^(3/2)/(2pi)^(3/2) u(lambda kappa,q),
    T_lambda: L2(dK/(2pi)^3 dmu) -> L2(dkappa dmu).             (T7)

All states and comparisons considered here retain the fixed compact kappa
support of F. The full q torus is unchanged by T_lambda.

The exact free contact coefficient at physical time s/lambda is

    a_lambda(s,kappa)
      =<c,exp[-i(s/lambda)H0(lambda kappa)]phi_lambda(lambda kappa)>
      =F(kappa)/Z_lambda integral f(x) w_lambda(kappa,x)
                                      exp[-is e_lambda(kappa,x)] dx. (T8)

In this inner product the q measure is normalized. Its lambda^3 Jacobian
cancels the lambda^-3 preparation factor; the `(2pi)^3` cancels as well.
In particular a_lambda is order one in each rescaled fiber. Its L2_K norm
still has the factor `lambda^(3/2)/(2pi)^(3/2)`.

The two momenta `x+/-kappa/2` are separated from zero by 1/2. The scaled
sines extend smoothly to lambda=0 on these compact supports. Thus, on any
fixed finite s interval, a_lambda and its kappa derivatives through order
two, including their first s derivatives, converge uniformly to

    e=|x+kappa/2|+|x-kappa/2|,
    w=[1+(x+kappa/2).(x-kappa/2)/(|x+kappa/2||x-kappa/2|)]/4,
    Z0^2=integral |F|^2 |f|^2 w,
    a(s,kappa)=F(kappa)/Z0 integral f(x) w(kappa,x) exp[-is e] dx,
    a0(kappa)=a(0,kappa),   N=m_f/Z0.                          (T9)

Only one kappa derivative is needed below. Also, exactly,
`n_lambda^2=1-lambda^3 c0^2 ||a_lambda(0)||^2_L2(dkappa) ->1`.
The packet's conserved physical energy expectation lies in
`[lambda/2,3lambda]` by B30; projection does not preserve an exact free band.

## 4. Exact contact forcing and the free-comparison remainder

Let `f_free(t)=exp(-itH0)phi_lambda`, `v(t)=P f_free(t)/n_lambda`, and
`w_phys(t)=psi_lambda(t)-v(t)`. The name w_phys is unrelated to the
projector weight w in (T9). Keep the same initial n_lambda at all times.
The comparison v need not have norm one later. Direct differentiation gives

    i partial_t v=H v+h alpha(t)/n_lambda,
    alpha(t,K)=<c,f_free(t,K)>,
    w_phys(t)= i/n_lambda integral_0^t exp[-i(t-s)H]h alpha(s) ds.

The sign is positive: `i partial_t(psi-v)=H(psi-v)-h alpha/n_lambda`.
This identity retains both the initial full-torus tail and all its forcing.

The source's supported bounds apply to f_free and its K derivative, since
free evolution preserves the relative support. With
`eta<=lambda^(3/2)/4`, `B_a=lambda||partial_Ka phi_lambda||<60`, E13 gives

    ||R_ab v(t)||
       <=[4lambda^3+eta(32+12B_a+12lambda t)]/n_lambda.         (T10)

The `8eta` multiplier contribution inside this expression is the bound on
the full-torus contact subtraction. For `t->infinity,lambda t->0`, division
by `lambda^(3/2)t` makes (T10) vanish. At `t=tau/lambda` with fixed tau,
division by sqrt(lambda) makes it vanish. Thus a nonzero limit or lower
bound for the forced correction at those scales cannot be canceled by v.
This is a norm estimate on the full free comparison, not an orthogonality
assumption between its pieces.

Set `U_lambda(r,kappa)=exp[-ir H(lambda kappa)/lambda]`. Exactly,

    W_lambda(tau):=lambda^(-1/2) T_lambda w_phys(tau/lambda)
       = i c0/n_lambda integral_0^tau U_lambda(tau-s,kappa)
                              h(lambda kappa) a_lambda(s,kappa) ds. (T11)

## 5. The full physical zero space and elementary averaging

Put `s_j=sin q_j`, `epsilon=|s|`, `v0=sum_j s_j T_j`, `v_b=s_b T_b`,
`H_*=H(0)`, and

    I0=integral dmu/(4epsilon^2),
    zeta=v0/(2epsilon^2 sqrt(I0)),  ||zeta||=1,
    1/12<=I0<=9/8.

For completeness, fold the eight periodic copies into
`Q=[-pi/2,pi/2]^3`. Concavity of sine gives
`|sin q_j|>=2|q_j|/pi` on Q. Enclose Q in the radius
`R=pi sqrt(3)/2` ball and integrate its radial upper bound:

    I0 = 8/[4(2pi)^3] integral_Q 1/epsilon^2 dq
       <=1/(16pi) integral_(|q|<=R) |q|^(-2) dq
       =R/4=pi sqrt(3)/8<9/8.

This also proves finiteness at all cone points. The lower bound follows
pointwise from `epsilon^2<=3`. The following full physical kernel identities
agree with the published memory derivation, but the needed assertions and
the I0 bounds are rederived here directly from the supplied operator:

    Pi=F_transverse+|zeta><zeta|,
    H0(0) zeta=c/sqrt(I0),   H_*zeta=0,
    h0:=h(0)=2v0,   ||h0||=sqrt(6),
    Pi h0=zeta/sqrt(I0).                                    (T12)

Here F_transverse is the pointwise transverse-triplet projection, not the
packet envelope F. It kills v0. The last equality also follows from
`<zeta,2v0>=1/sqrt(I0)`. The auxiliary constant c is not a physical zero
mode. To check completeness, the singlet/triplet matrix of H0(0) is
`[[0,2s^T],[2s,0]]`. If a physical psi satisfies H_*psi=0, then
`H0(0)psi=beta c`; subtracting `beta sqrt(I0) zeta` leaves exactly a
free transverse zero vector. Conversely those vectors and zeta are killed
by H_*. This proves the full physical kernel assertion. Zeta is an L2
vector with integrable cone singularities; it need not belong to the
dipole's H1_q domain.

For the fixed vector h0 define

    M_t h0=(1/t) integral_0^t exp(-ir H_*)h0 dr.

The spectral multiplier is 1 at E=0 and
`(1-exp(-itE))/(itE)` elsewhere. Its modulus is at most one and it tends to
zero for each fixed nonzero E. Dominated convergence against the finite
spectral measure of h0 therefore proves

    M_t h0 -> Pi h0  in L2 as t->infinity.                    (T13)

This argument needs no gap, no inverse on the full complementary space,
no rate, and no assertion of operator-norm convergence.

The supplied Hamiltonian also has the global bounds, for all needed kappa,

    ||H(lambda kappa)-H_*||<=lambda |kappa|,
    ||partial_(kappa_a) H(lambda kappa)||<=lambda,
    h(lambda kappa)=h0+O(lambda^2) in C1_kappa(L2_q).

The first two follow directly by differentiating each Pauli symbol; each
one-body directional derivative has norm at most half the direction norm.
Consequently, with `U_*lambda(r)=exp(-ir H_*/lambda)`,

    ||U_lambda(r,kappa)-U_*lambda(r)||<=r |kappa|,
    ||partial_(kappa_a) U_lambda(r,kappa)||<=r.               (T14)

These are bounded-operator Duhamel estimates. Differentiating an integral
in (T11) differentiates its propagator, form factor and source. The source
already includes both the projector and phase derivatives. No derivative
of a global normalizing constant is introduced.

## 6. Rescaled bracket and a nonzero canonical coupling

Set the bounded operator

    L_b=P cos(2q_b)P+|v_b><v0|+|v0><v_b|,
    ||L_b||<=1+sqrt(3)<3.

Taylor expansion of the exact current (T3), or D13–D14, gives in operator
norm uniformly on compact kappa sets

    J_b(lambda kappa)/lambda -> kappa_b L_b,
    A_b(lambda kappa)/lambda -> kappa_b[H_*,L_b],
    C_ab(lambda kappa) -> delta_ab H_*(L_b-I).                 (T15)

For the last identity, on the smooth core the constant term of the
commutator is `H partial_Ka J_b+[Dcal_a,J_b]-delta_ab H`.
At K=0 the operator J_b is exactly zero, so its q derivative and the fiber
commutator are zero, while `partial_Ka J_b=delta_ab L_b`. This proves the
stated identity on the core. The bounded coefficient C_ab then extends it
to all physical L2 vectors. It does not apply D_a to zeta.

For diagonal b let

    Q_(lambda,b)=C_bb(lambda kappa)
                       +[A_b(lambda kappa)/lambda] partial_(kappa_b),
    Q_(0,b)=H_*(L_b-I)+kappa_b[H_*,L_b] partial_(kappa_b).

Thus `T_lambda R_bb u=Q_(lambda,b) T_lambda u`, and Q_lambda converges in
operator norm `H1_kappa(L2_q)->L2` on the fixed support to Q_0. On that
support `|kappa|<=1/4`, its two coefficient norms obey

    ||H_*(L_b-I)||<16,
    ||kappa_b[H_*,L_b]||<6.                                 (T16)

These bounds are global in q and apply to the complete contact correction.
For a field z valued in the fixed kernel of H_*, together with its kappa
derivative, `Q_(0,b)z=H_*L_b partial_(kappa_b)(kappa_b z)`.

The two canonical finite-rank terms are essential in the following exact
calculation. Cubic symmetry gives
`<v0,zeta>=1/(2sqrt(I0))`, `<v_b,zeta>=1/(6sqrt(I0))`. Therefore

    L_b zeta=cos(2q_b) zeta+v_b/(2sqrt(I0))+v0/(6sqrt(I0)),
    H0(0)L_b zeta=[1-s_b^2+epsilon^2/3]c/sqrt(I0),
    H_*L_b zeta=(epsilon^2/3-s_b^2)c/sqrt(I0).

The constant singlet mean in the middle line is exactly `1/sqrt(I0)` and
is removed by P. Write `p_b(q)=epsilon^2/3-s_b^2`. Separate circle moments
`integral sin^2=1/2`, `integral sin^4=3/8` give
`integral p_b=0` and `integral p_b^2=1/12`.
Thus define the explicit rescaled vector

    Gamma_b(kappa,q)
       = i c0 H_*L_b zeta partial_(kappa_b)(kappa_b a0)/sqrt(I0)
       = i c0 p_b(q)c partial_(kappa_b)(kappa_b a0)/I0,
    c_b:=||Gamma_b||
       =c0 ||partial_(kappa_b)(kappa_b a0)||/(sqrt(12) I0).    (T17)

Positivity of F,f and `1/4<=w<=1/2` yields `||a0||>=N/4>0`.
For any compactly supported C1 scalar a0, integration by parts gives

    Re<a0,partial_(kappa_b)(kappa_b a0)>=||a0||^2/2,
    ||partial_(kappa_b)(kappa_b a0)||>=||a0||/2.

There is no K-boundary term. In particular

    c_b>=c0 N/(8sqrt(12) I0)>0.                              (T18)

This rules out a cancellation by the K-envelope derivative on the actual
normalizable packet. It is not a claim about a single momentum fiber.

## 7. The shorter-time asymptotic and the power threshold

Let `t=t_lambda->infinity`, `sigma=lambda t->0`. Divide the exact physical
time Duhamel formula by `lambda^(3/2)t` after applying T_lambda:

    Y_lambda = T_lambda w_phys(t)/(lambda^(3/2)t)
       =i c0/(n_lambda t) integral_0^t exp[-i(t-s)H(lambda kappa)]
                          h(lambda kappa)a_lambda(lambda s,kappa) ds.

The propagator difference from `exp[-i(t-s)H_*]` has norm at most
`lambda(t-s)|kappa|`. Its kappa derivative has norm at most
`lambda(t-s)`; the reference propagator has zero kappa derivative.
Also `h(lambda kappa)-h0=O(lambda^2)` in C1 and

    sup_(0<=s<=t) ||a_lambda(lambda s)-a0||_(C1_kappa)
          =O(lambda t)+o(1).

The latter follows from (T9) and the uniform first time derivatives of the
source. Differentiating every factor under the time integral now gives

    Y_lambda - i c0 a0 M_t h0 ->0 in H1_kappa(L2_q).           (T19)

For example, each propagator error or differentiated propagator contributes
at most a constant times `lambda t`; the form-factor error contributes
`O(lambda^2)` and the source contributes its displayed C1 error. Factors
`1/n_lambda-1` tend to zero. All kappa support lies in one compact set,
so the uniform estimates imply the stated H1 convergence. Applying (T13),

    Y_lambda -> i c0 a0 zeta/sqrt(I0) in H1_kappa(L2_q).

Combining this with (T15), (T17), and the vanishing free-comparison term
(T10) proves the vector convergence (T1). Norm continuity proves all its
stated consequences, including

    ||R_bb psi_lambda(lambda^(-1/2))||/lambda ->c_b>0,
    ||R_bb psi_lambda(lambda^(-gamma))||/
                    lambda^(3/2-gamma) ->c_b,  0<gamma<1.    (T20)

For `gamma<1/2` this is consistent with the prior little-o bound. At and
above the threshold it gives an actual lower obstruction for the same
preparation. No rate of convergence in (T13) is needed to assert this
asymptotic; a numerical onset in lambda is not supplied.

## 8. Fixed small inverse-energy times

This step proves (T2) directly and does not extrapolate (T1) to constant
`lambda t`. Fix `tau>0`. The source limits and `n_lambda->1` permit replacing
`h(lambda kappa),a_lambda,n_lambda` by `h0,a,1` in (T11), with an error
vanishing in H1_kappa. In proving this, the differentiated propagator is
bounded by tau in (T14), independently of lambda.

Compare that integral to

    V_lambda(tau)=i c0 tau a0 M_(tau/lambda) h0.

By (T13), V_lambda converges in H1_kappa to
`V(tau)=i c0 tau a0 zeta/sqrt(I0)`, and `Q_(0,b)V=tau Gamma_b`.
The following explicit source bounds hold for every `s>=0`, with
`M=192/7`, `N=m_f/Z0` and `r=1/4`:

    ||a(s)||<=N/2,             ||a(s)-a0||<=Ns,
    ||partial_b a0||<=N(M/2+1),
    ||partial_b a(s)-partial_b a0||<=Ns(M+5/2).               (T21)

Here and below these scalar norms are in L2(dkappa), and partial_b means
`partial_(kappa_b)`. To verify them, `e<=2`, `|partial_b e|<=1`, and
`|partial_b w|<=1` on the support. The last bound follows by differentiating
the two unit vectors in w, whose denominators are at least 1/2. Use
`|exp(-is e)-1|<=s e`, `||F||=1` and `||partial_b F||<=M`.
The derivative of the phase contributes the final `s/2` in `s(M+5/2)`;
it is not omitted.

Let `E_lambda=W_lambda-V_lambda`. Write the undifferentiated integrand
error as `(U_lambda-U_*lambda)h0 a0+U_lambda h0(a(s)-a0)`.
For its derivative, use

    (partial_b U_lambda)h0 a(s)
      +(U_lambda-U_*lambda)h0 partial_b a0
      +U_lambda h0(partial_b a(s)-partial_b a0).

The reference propagator has no kappa dependence. Insert (T14), (T21) and
`||h0||=sqrt(6)`; integrate `tau-s` and s separately. This gives

    limsup ||E_lambda||
        <=c0 sqrt(6) N tau^2 (r/4+1/2)
         =c0 sqrt(6) N tau^2 (9/16),
    limsup ||partial_b E_lambda||
        <=c0 sqrt(6) N tau^2
             [1/4+r(M/2+1)/2+(M+5/2)/2]
         =c0 sqrt(6) N tau^2 (13/8+9M/16).                  (T22)

Every norm here is the full rescaled direct-integral norm. Terms from the
vanishing replacements in (T11) are already included as zero in the
limsup. No physical state is assumed to stay corner-supported.

The W_lambda are uniformly H1 on this finite time interval, so the
coefficient convergence (T15), bounds (T16), and (T10) yield

    limsup ||lambda^(-1/2) T_lambda R_bb psi_lambda(tau/lambda)
                                        -tau Gamma_b||
      <=c0 sqrt(6) N tau^2
          [16(9/16)+6(13/8+9M/16)]
       =c0 sqrt(6) N tau^2 (3117/28)
       <112 c0 sqrt(6) N tau^2.                             (T23)

This is an error about a specified vector, not an assertion that the left
hand vector has a limit. The leading vector lies in the physical zero
space before applying Q_0; the error generally does not. This is why the
full coefficient bounds 16 and 6 are used. Applying only the restriction
of Q_0 to zero-space errors would be unjustified.

For `tau<=1/32768` and `I0<=9/8`,

    112 sqrt(6) tau <= 1/(16sqrt(12) I0).

Indeed the worst-case product on the left after rearrangement is
`12096 sqrt(2)/32768<1`. With (T18), the error in (T23) is at most
`tau c_b/2`. Norm inequalities prove

    tau c_b/2 <= liminf ||R_bb psi_lambda(tau/lambda)||/sqrt(lambda)
       <= limsup ||R_bb psi_lambda(tau/lambda)||/sqrt(lambda)
       <=tau c_b+112c0 sqrt(6)N tau^2.                       (T24)

Finally `Z0<=1/sqrt(2)` implies `N>=sqrt(2)m_f`; (T18) and
`I0<=9/8` give the explicit second lower bound in (T2). This completes
both claimed time regimes. At these fixed tau the energy-scaled norm
`||R_bb psi||/<H>` diverges at least as a positive multiple of
`lambda^(-1/2)`. This ratio uses the conserved positive energy expectation;
it asserts nothing about the expectation of R_bb itself.

## 9. Controls, unsuccessful routes and verification limits

`boost_current_inverse_energy/inverse_energy_controls.py` is a single author
control with full stdout/stderr and a 120-second recorded timeout. Its
baseline completed with exit 0 on Python 3.13.5, NumPy 2.4.4, SciPy 1.17.1,
and SymPy 1.14.0. The receipt binds the source, executable, versions and logs.

The exact controls separately arrange the two algebraic expressions for
`H_*L_b zeta`, retain the full-torus mean subtraction, integrate the circle
moments, and check the dilation pairing and conservative time constant.
They exercise calculations already justified above; successful assertions
are not additional mathematical premises. A separate short exact control
checks the folded-cube normalization in the new self-contained I0 proof.
The pre-amendment note, map and wording scan are preserved; the main helper
and its existing logs are unchanged.

A separate noncommuting three-vector model uses `H_*=diag(0,1,-2)`, a linear
bounded matrix B(kappa), a kappa-dependent form factor, a normalized Gaussian
scalar envelope and a kappa-dependent forcing phase. The augmented matrix
exponential is compared with the actual vector obtained by integrating the
Hermitian spectral decomposition. Its kappa derivative uses the exponential
Frechet derivative and all source factors, and is compared with a five-point
derivative of that independently computed integral. The baseline vector
error was about `1.1e-15`, derivative error about `4.9e-12`. Shorter-time and
fixed-tau sequences resolve the corresponding kernel responses in this
finite model. This gapped fixture is not a torus discretization and supplies
no continuum convergence rate or theorem.

Three separate source files, each with exactly one literal replacement,
actually failed: omitting the current rank terms, reversing the Duhamel
source sign, and omitting the source-clock derivative. Their complete
sources, stdout, tracebacks, command metadata and exit codes are preserved.
These failures show that the selected controls distinguish these errors;
they are author consistency evidence, not selective independent review.

Routes that were insufficient or deliberately not used are preserved:

- Substituting `t=tau/lambda` into the prior E2 bound gives only an upper
  `O(sqrt(lambda))` estimate. It cannot prove a counterexample.
- Isolating the initial physical zero projection loses its cancellation
  with the free component at t=0. The exact forced comparison is necessary.
- A fixed K fiber or a direction delta does not meet the requested
  normalizability condition. Equations (T6)–(T9) use the actual packet.
- An L2 limit alone cannot pass through `A_b partial_Ka`. Equations
  (T19) and (T22) explicitly control the kappa derivative.
- An inverse on the whole gapless complement, or operator-norm averaging
  over its unit ball, is not available. The proof uses one fixed vector
  and its finite spectral measure instead.
- Zeta is singular. Applying D_a to it would exceed the demonstrated
  domain. Only bounded coefficients of the exact normal form act on it.
- A longer forced effective-dynamics route was worked out before root's
  mean-ergodic suggestion. Its analysis and proposed stronger fixed-tau
  convergence are preserved in
  `boost_current_inverse_energy/FIXED_TAU_ROUTE_NOT_USED.md`; no assertion
  from that file is needed or certified by this note. The simpler main
  proof uses the more conservative interval `tau<=1/32768`.

The prior `gamma<1/2` estimate has `lambda t->0`: it does not reach an
order-one rescaled energy-time. T20 locates a norm obstruction earlier,
while T24 reaches specified fixed positive rescaled energy-times. No claim
is made at arbitrary tau, for a different packet, for all low-energy
vectors, for boost/boost closure, or for a many-body or gravity algebra.
Other phases or contact-orthogonal preparations can have a different
forcing coefficient. The model clock and physical interpretation remain
supplied, and independent scientific review of T1–T24 remains open.

## 10. Scoped negative-claim discipline

This is a conditional counterexample inside a specified positive asymptotic
calculation. It does not close all routes to a boost law. The following
records the N1–N8 checks without claiming a formal negative-packet PASS or
retained authority for the newly authored proof.

**N1, actual cancellation/admissibility attacks.** Five mechanisms were
examined analytically: (i) spectral phase cancellation of the fixed contact
forcing, resolved at the asserted times by T13/T19/T22; (ii) vanishing
preparation contact amplitude, resolved for this positive F,f and Pi_++ by
T9/T18; (iii) cancellation by the canonical finite-rank current terms,
resolved by the full polynomial calculation preceding T17; (iv) cancellation
by K differentiation of the packet envelope, resolved by the compact
integration-by-parts identity; and (v) failure of global normalization or
admissible commutator domain, resolved for each finite lambda,t by T3–T11
and the bounded normal-form extension. Each was ATTEMPTED in this cycle.
These are concrete mechanisms, not an exhaustion claim. Their closure
here rests on a new author proof with cited source premises; it has not
received retained authority. A route count is not evidence of validity.

**N2, condition relationships.** No multiple independent-wall count is
asserted. The supplied Hamiltonian, contact rule, current/dipole placement,
packet and clock jointly specify one conditional theorem. They are not
presented as mutually independent obstacles to other research programs.

**N3, hidden hypotheses.** “Canonical” means exactly T3 from the specified
symmetric placement. “Physical” means ran P, excluding the auxiliary c.
Global normalization means T6/T8, not per-fiber normalization. Smoothness
and fixed support are explicit; the singular limit is used only through
bounded operators. The positive F,f choice and positive-positive band are
load-bearing for `a0` and are not silently generalized.

**N4, exact residual matching.** The source's mixed-band prepared-state
counterexample and the degenerate note's dressed-state current response
concern different preparations/observables. Neither is a negative witness
for T1 or T2. E1 matches the exact R_ab definition and is used as an identity;
its earlier upper bound is not a lower-bound witness. Only this note's new
norm calculation supplies the present obstruction.

**N5, resolution.** The assertions concern the normalized direct integral
for each diagonal component b and the explicit time regimes above. They
are not per-mode statements or operator-norm statements on a spectral
window. No negative assertion is made for untested current expectations,
other off-diagonal components or all packets.

**N6, alternatives.** Changing envelope phases, imposing contact
orthogonality, testing weaker observables, or changing the energy placement
changes the terminal question. Those are open alternatives; this result
neither requires a new axiom nor rules them out. No primitive absence is
used as a premise.

**N7, strongest challenge.** A small L2 contact correction could have a large
or canceling K derivative, and a fixed-fiber zero-mode argument could fail
after true global normalization. The terminal obligation is therefore a
full direct-integral H1 estimate followed by the complete R normal form,
not a zero-mode overlap heuristic. T7–T11, T19 and T22–T23 address those
specific mechanisms. For larger fixed tau, phase cancellation remains
unresolved and is outside the asserted interval.

**N8, prior echoes.** A bounded read-only search of the stored main and
working-tree refs for boost/inverse-energy/zero-space/current combinations
is recorded in `boost_current_inverse_energy/bounded_search.json`. It
found no matching doc line. This
is not a repository-wide or literature novelty claim. The nearby mixed-band
and dressed-current constructions were read and distinguished as in N4;
no old framework wall or its retirement is inherited by this counterexample.

The entire packet remains external research evidence, with no repository,
editable prompt, original source, prior review, audit status or physical
primitive changed. The next scientific gate is an independent check of
this authored theorem and its hypotheses.

---

# Part V — Actual boost/current expectations at inverse-energy time

Source date: 2026-10-11. Conditional supplied-model mathematical result.
The complete source-bound independent review found no required repair within
X1–X35. Review identities, authorship and limits are recorded in the milestone
evidence. This publication applies no retained-status audit or physical premise.

For exactly the globally normalized B25–B30 packets and the actual excluded
evolution, the result of the calculation is

\[
 \boxed{\quad
 \lim_{\lambda\downarrow0}\sup_{|\tau|\le T}
 \left|\frac{\langle\psi_\lambda(\tau/\lambda),
          R_{ab}\psi_\lambda(\tau/\lambda)\rangle}{\lambda}\right|=0
 \quad (0\le T<\infty),\qquad a,b=1,2,3. \quad}           \tag{X1}
\]

Here `R_ab=-i[D_a,J_b]-delta_ab H` uses the complete canonical bracket,
including `[H,J_b] partial_Ka`. This is an asymptotic expectation statement; the
finite-lambda expectation is not asserted to be identically zero. It does
not contradict T1–T24: for small fixed positive tau, the norm of the
diagonal residual on this same state is of order `sqrt(lambda)`. The leading residual
vector is orthogonal to the leading forced correction in precisely the
pairing relevant to the expectation.

The proof below also gives the actual forced correction's fixed-time
`H1_kappa(L2_q)` limit. It uses a spectral cutoff on a compact family of
fixed residual vectors, not a gap, a bounded inverse on the entire
complement, or operator-norm averaging.

## 1. Exact contract, sources, and retained limitations

The target is the expectation in (X1), with fixed arbitrary finite rescaled
time, the exact B25–B30 preparation, the one global contact projection, and
the original two global normalization constants. Replacing the state by a
fixed K fiber, a direction delta, a separately normalized fiber, a
contact-free state, or a dressed kernel state would not answer this target.
An estimate on `||R_ab psi||` alone also would not answer it.

Let `S` be the original research directory recorded in the milestone's
EVIDENCE_MAP.json; its source bytes are preserved there. These are the frozen mathematical
sources read completely for this derivation:

| Source relative to S | SHA-256 | Use |
|---|---|---|
| `EXCLUDED_WALK_BOOST_CURRENT_PROBE.md` | `903261f54d72d6e81d0c82d5cd976bd4dd46a55c1dd4567fe23d8bce07fe1923` | B5–B30 operators, full normal form, domains, global/supported bounds, exact preparation |
| `EXCLUDED_WALK_EVOLVED_BOOST_CONTROL_DRAFT.md` | `d89611986626dbabcf6f9f5c487733d2a520cb9249b7ed0b3a27be35874fd929` | E8–E13 exact forced comparison and its supported residual estimate |
| `BOOST_CURRENT_INVERSE_ENERGY_PROBE.md` | `76ed691c581d4da282041b99fa53da48d1461b47ddccb765b736969a191b4990` | T3–T16 normalized source, full physical zero space, rescaled normal form; T17–T24 norm result distinguished from the new expectation |
| `BOOST_CURRENT_INVERSE_ENERGY_REVIEW.md` | `d3c3d00b69b302beb88aef4a1b649f5e685ff7a08bc2c117755fcafde4d74796` | Source-bound independent review of T1–T24, not of the present argument |
| `boost_inverse_energy_review/PROOF_RECONSTRUCTION.md` | `c0a06917dc1f24207d85656781e250104c81dd613a9a937a140088149bf2f131` | Complete prior reconstruction, checked against the needed source premises |

The supplied sine-Pauli Hamiltonian, antisymmetric pair sector, exclusion
projection, coordinates, clock, symmetric energy placement, and preparation
remain premises. This note does not derive their physical identification from
the framework axioms. The registered scale, kinetic-form isotropy, and
realized-state primitives are not invoked to supply these dimensionless
model choices. No new physical axiom or primitive is proposed.

Publication status fields are `target_claim_type: bounded_theorem`,
`actual_current_surface_status: conditional-support`,
`trace_class: upstream_support`, `reachability_to_target: supports`,
`audit_required_before_effective_retained: true`, and
`bare_retained_allowed: false`. The specific mathematical expectation target
is addressed; a full boost algebra or physical law is not thereby established.
The older archived `FIXED_TAU_ROUTE_NOT_USED.md` supplies no theorem premise
and was not reopened or promoted here.

Root suggested the possible kernel-orthogonality and symmetric-cross-term
mechanism. The recovered checkpoint suggested a C2/finite-difference route
for derivatives. Both were proposals. The present author supplies the
cutoff estimate, the differentiated error equation, and the full expectation
proof below. These are new author work, not independent review.
After the complete diagonal draft was preserved, root also proposed checking
the all-component identity `Q_0,ab z=H_*L_b partial_a(kappa_b z)`. Its
index structure and symmetry are checked explicitly in Section 6. The same
proof covers all nine expectations; no off-diagonal norm lower bound is
claimed. The pre-extension diagonal draft remains byte-for-byte preserved.

## 2. Hilbert space, exact state, and normalization

The relative fiber `mathcal H` is the antisymmetric part of
`L2(T^3,dq/(2pi)^3; C2 tensor C2)` satisfying
`u(-q)=-S_swap u(q)`, restricted to `ran P`, where

    c = the constant unit singlet,
    C=|c><c|,  P=I-C,
    H0(K)=sum_j [sigma_(1,j) sin(K_j/2+q_j)
                       +sigma_(2,j) sin(K_j/2-q_j)],
    H(K)=P H0(K)P on mathcal H,
    h(K)=H0(K)c=2 sum_j cos(K_j/2) sin(q_j) T_j,
    T_j=sigma_(1,j)c.                                      (X2)

Every relative inner product uses the complete normalized torus. In
particular P is one full-torus projection in each K fiber. Total momentum
has measure `dK/(2pi)^3` in the original compact-support chart. Inner
products are conjugate linear in the first entry.

For the exact B25 envelope, let `p(t)=(1-t^2)^2` for `|t|<1` and zero
otherwise. Let F0 be the positive L2 normalization of
`product_j p(8sqrt(3) kappa_j)`. Let eta be the positive L1 normalization
of `exp[-1/(1-512^2|y|^2)]` for `|y|<1/512` and zero otherwise. Then
`F=(eta*F0)/||eta*F0||_2`. It is real, smooth, supported in
`|kappa|<=65/512<1/4`, with `||F||_2=1`
and `||partial_j F||_2<=192/7`. The radial f is the positive L2
normalization of

    exp[-1/((|x|-5/8)(3/4-|x|))],  5/8<|x|<3/4,

and zero outside. Thus f is smooth, even, and has `integral f>0`.
Let Pi_++ be the product of the two positive Pauli projectors and use exactly

    u_lambda=(2pi)^3 lambda^-3 F(K/lambda) f(q/lambda) Pi_++ c,
    Z_lambda=||u_lambda||, phi_lambda=u_lambda/Z_lambda,
    n_lambda=||P phi_lambda||,
    chi_lambda=P phi_lambda/n_lambda,
    psi_lambda(t)=exp(-itH)chi_lambda.                        (X3)

Both Z_lambda and n_lambda are single global scalars over K and q. They
have no K or kappa derivative. The state psi has norm one. Its conserved
energy expectation obeys `[lambda/2,3lambda]` for `0<lambda<=1/16` by B30.
This is not a claim of exact interacting spectral support.

Set `c0=(2pi)^(-3/2)` and use the K-only isometry

    (T_lambda u)(kappa,q)=c0 lambda^(3/2) u(lambda kappa,q),
    T_lambda partial_Kj=lambda^-1 partial_kappaj T_lambda.    (X4)

The target space is `L2(dkappa;mathcal H)` and the entire q torus remains.
All states and comparisons below have the same compact kappa support.

For `y_+=x+kappa/2`, `y_-=x-kappa/2` and `|kappa|<=1/4`, let

    e_lambda=(|sin(lambda y_+)|+|sin(lambda y_-)|)/lambda,
    w_lambda=[1+sin(lambda y_+).sin(lambda y_-)
                  /(|sin(lambda y_+)||sin(lambda y_-)|)]/4,
    Z_lambda^2=integral |F|^2 |f|^2 w_lambda dkappa dx,
    a_lambda(s,kappa)=F(kappa)/Z_lambda
             integral f(x)w_lambda(kappa,x)exp[-is e_lambda(kappa,x)] dx.
                                                               (X5)

This is exactly `<c,exp[-i(s/lambda)H0(lambda kappa)]
phi_lambda(lambda kappa)>`, not its rescaled L2 norm. The q Jacobian
`lambda^3/(2pi)^3` cancels the packet factor `(2pi)^3 lambda^-3`.
The six-dimensional change of variables in the norm likewise cancels the
square of that factor. Therefore

    1/4<=w_lambda<=1/2,  1/2<=Z_lambda<=1/sqrt(2),
    n_lambda^2=1-c0^2 lambda^3 ||a_lambda(0)||^2_(L2 dkappa)->1.
                                                               (X6)

Because `|y_+|,|y_-|>=1/2` on the fixed support, scaled sine divided by
lambda extends smoothly to lambda=0, with uniformly nonzero denominators.
The limiting objects are

    e=|y_+|+|y_-|,
    w=[1+y_+.y_-/(|y_+||y_-|)]/4,
    Z0^2=integral |F|^2|f|^2 w,
    a(s,kappa)=F(kappa)/Z0 integral f(x)w(kappa,x)exp[-is e] dx.
                                                               (X7)

Extend a_lambda and a by zero outside this small kappa set; they already
vanish on an open neighborhood of its boundary because of F's support.
On each compact s interval, a_lambda converges to a with all kappa
derivatives needed here (orders zero, one, and their first s derivatives),
uniformly in kappa. The same quantities are uniformly bounded. They are
compactly supported in kappa. This follows by differentiating the explicit
fixed-support integrals; no derivative of either global normalizer appears.

## 3. Exact forcing and coefficient regularity

Define the free comparison and its exact error using the initial n_lambda:

    f_free(t)=exp(-itH0)phi_lambda,
    v_lambda(t)=P f_free(t)/n_lambda,
    w_phys,lambda(t)=psi_lambda(t)-v_lambda(t).

The projected comparison is not renormalized as time changes. Direct
differentiation, including `P H0 C f_free=h<c,f_free>`, gives

    i partial_t v_lambda=H v_lambda+h<c,f_free>/n_lambda,
    w_phys,lambda(0)=0,
    w_phys,lambda(t)=i/n_lambda integral_0^t
                 exp[-i(t-s)H]h<c,f_free(s)> ds.               (X8)

The plus i has the sign shown because the source in the equation for
psi-v is negative. The formula contains the entire contact tail and its
forcing; no homogeneous zero-mode initial tail is added separately.

Put

    G_lambda(kappa)=H(lambda kappa)/lambda,
    U_lambda(r,kappa)=exp[-irG_lambda(kappa)],
    W_lambda(tau)=lambda^-1/2 T_lambda w_phys,lambda(tau/lambda),
    g_lambda(s,kappa)=c0 h(lambda kappa)a_lambda(s,kappa)/n_lambda.

Then exactly

    W_lambda(tau)=i integral_0^tau U_lambda(tau-s)g_lambda(s) ds,
    i partial_tau W_lambda=G_lambda W_lambda-g_lambda,
    W_lambda(0)=0.                                          (X9)

Write `H_*=H(0)`. Taylor expansion of the exact sine symbol gives

    G_lambda=H_*/lambda+B(kappa)+E_lambda(kappa),
    B(kappa)=sum_j kappa_j V_j,
    V_j=P[(sigma_(1,j)+sigma_(2,j))cos(q_j)/2]P,
    ||E_lambda||+sum_j ||partial_j E_lambda||=O(lambda),
    h(lambda kappa)=h0+O(lambda^2) in C1_kappa(mathcal H),
    h0=2 sum_j sin(q_j)T_j.                                 (X10)

All norms here are uniform on any fixed compact kappa set. To see the
orders directly, split each symbol into difference-spin times
`sin(q_j)cos(lambda kappa_j/2)` plus total-spin times
`cos(q_j)sin(lambda kappa_j/2)`. The cosine remainder divided by lambda
is O(lambda); its first kappa derivative is O(lambda). The sine remainder
is smaller. Each V_j is bounded self-adjoint and annihilates c before
compression. Also

    ||partial_j G_lambda||<=1,
    ||partial_j U_lambda(r)||<=|r|.                          (X11)

The latter follows from the bounded-operator Duhamel derivative; its sign
and exact integrand are

    partial_j U_lambda(r)
       =-i integral_0^r U_lambda(r-u)(partial_j G_lambda)
                                            U_lambda(u) du.

With `g(s,kappa)=c0 h0 a(s,kappa)`, (X6)–(X10) give

    g_lambda -> g in C1_kappa(mathcal H), uniformly for |s|<=T.
                                                               (X12)

In particular W_lambda is uniformly bounded in `H1_kappa(mathcal H)` on
each finite tau interval. Differentiating (X9) under its integral produces
exactly these three factors:

    (partial_j U_lambda) h(lambda kappa) a_lambda,
    U_lambda (partial_j h(lambda kappa)) a_lambda,
    U_lambda h(lambda kappa) partial_j a_lambda.              (X13)

Each carries the same constant `i c0/n_lambda`. Bounds (X11), (X5)–(X7),
and (X10) bound every term uniformly; support is compact. The last term
includes both projector-weight and clock-phase derivatives in a_lambda.

## 4. A gapless cutoff lemma for the full perturbed propagator

Here is the analytic step that was not established by T1–T24. Let H_* be
bounded self-adjoint on a Hilbert space, let Pi be its exact kernel
projection, and Q=I-Pi. Let

    G_lambda(kappa)=H_*/lambda+V_lambda(kappa)

be self-adjoint with uniformly bounded V_lambda on a compact parameter set.
Suppose r(s,kappa) belongs to ran Q, is continuous in (s,kappa), is C1 in
s, and r and partial_s r are uniformly bounded on `[0,T]` times that set.
Then

    sup_(0<=t<=T,kappa)
      ||integral_0^t exp[-i(t-s)G_lambda(kappa)]r(s,kappa) ds|| ->0.
                                                               (X14)

Proof. Put `S_delta=1_{|H_*|>=delta}` and
`x_delta=H_*^-1 S_delta r`. This inverse is used only after the cutoff,
so `||x_delta||<=delta^-1||r||` and
`||partial_s x_delta||<=delta^-1||partial_s r||`. The family of r values
is compact because its parameter domain is compact and r is continuous.
Since `S_delta->Q` strongly as delta decreases to zero, convergence is
uniform on that compact family:

    epsilon_delta=sup_(s,kappa)||(I-S_delta)r(s,kappa)|| ->0.   (X15)

For clarity, this uniformity follows by a finite epsilon-net and the
uniform operator bound `||I-S_delta||<=1`; it is not operator-norm
convergence on the complementary unit ball.

Since `H_*=lambda(G_lambda-V_lambda)` and
`partial_s U_lambda(t-s)=iU_lambda(t-s)G_lambda`, integration by parts gives

    integral_0^t U_lambda(t-s)S_delta r(s) ds
      =-i lambda[U_lambda(t-s)x_delta(s)]_(s=0)^(s=t)
       +i lambda integral_0^t U_lambda(t-s)partial_s x_delta(s) ds
       -lambda integral_0^t U_lambda(t-s)V_lambda x_delta(s) ds.
                                                               (X16)

No commutation of V_lambda with H_* or with the cutoff was used. Hence the
left side of (X14) is at most

    T epsilon_delta
     +lambda/delta [2 sup||r||+T sup||partial_s r||
                         +T sup||V_lambda|| sup||r||].        (X17)

First hold delta fixed and take lambda to zero, then take delta to zero.
This proves the lemma without a gap or a specified convergence rate. The
same argument applies to a finite set of such residual fields. Negative
times are covered by reversing time and replacing G_lambda,H_* by their
negatives, with the source evaluated at the reversed time.

## 5. The actual forced fixed-time H1 limit

Use the physical Hilbert space mathcal H throughout. Let Pi be the full
kernel projection of H_* and let

    A(kappa)=Pi B(kappa)Pi restricted to ran Pi,
    z(tau,kappa)=i integral_0^tau
              exp[-i(tau-s)A(kappa)] Pi g(s,kappa) ds.
                                                               (X18)

A is bounded self-adjoint on the fixed space ran Pi. Extend its evolution
only on that space in this formula. Thus

    z(0)=0,  i partial_tau z=A z-Pi g,
    Pi z=z,  Pi partial_j z=partial_j z.                     (X19)

The last assertion holds because Pi is independent of kappa. Smooth
bounded parameter differentiation of A and the source proves that z,
partial_j z, and their time derivatives are continuous and bounded on
compact (tau,kappa) sets. They have the same compact kappa support as F.

Let `D_lambda=W_lambda-z`. Its exact equation, using (X9)–(X12), is

    i partial_tau D_lambda=G_lambda D_lambda+r+e_lambda,
    D_lambda(0)=0,
    r=Q(B z-g),
    e_lambda=E_lambda z+g-g_lambda.                          (X20)

Every value of r is in ran Q, and its values and time derivatives form
bounded continuous families on compact sets. By (X14), its Duhamel
integral vanishes uniformly. Also e_lambda and its first kappa derivatives
tend uniformly to zero. Unitarity bounds the integral of e_lambda by T
times its supremum. Therefore

    sup_(|tau|<=T,kappa)||D_lambda(tau,kappa)|| ->0.           (X21)

For each j, differentiate the exact error equation:

    i partial_tau(partial_j D_lambda)
      =G_lambda partial_j D_lambda
          +(partial_j G_lambda)D_lambda+partial_j r+partial_j e_lambda,
    partial_j D_lambda(0)=0,
    partial_j r=Q(V_j z+B partial_j z-c0 h0 partial_j a).
                                                               (X22)

The D_lambda term vanishes in its Duhamel integral by (X11) and (X21).
The partial_j e_lambda term vanishes by (X10)–(X12). The partial_j r
term is again a fixed Q-valued field with bounded continuous values and
time derivative, so (X14) applies to it. This proves uniform first kappa
derivative convergence. Compact support converts it to

\[
 \sup_{|\tau|\le T}\|W_\lambda(\tau)-z(\tau)\|_{H^1_\kappa(
                       \mathcal H)}\longrightarrow0.       \tag{X23}
\]

Equation (X22) explicitly retains differentiation of the propagator through
partial_j G_lambda. Equation (X12) retains both form-factor and source
derivatives. Thus (X23) does not infer derivative convergence from L2
convergence alone, and does not require a C2 interpolation claim.

For this particular model, the full kernel can also be identified directly.
Write `s_j=sin q_j`, `epsilon=|s|`, `v0=sum_j s_j T_j`, and

    I0=integral dmu/(4epsilon^2),
    zeta=v0/(2epsilon^2 sqrt(I0)).

Folding the eight sine-squared cells and integrating the radial `|q|^-2`
majorant gives `1/12<=I0<=pi sqrt(3)/8<9/8`, so zeta is an L2 physical
vector. At K=0 the singlet/triplet form of H0 is
`[[0,2s^T],[2s,0]]`. If a physical vector is killed by PH0P, then
`H0 u=beta c`. Subtracting `beta sqrt(I0) zeta` leaves a transverse
triplet field. Conversely every transverse triplet field and zeta is
killed by PH0P. They are orthogonal. Thus

    Pi=F_transverse+|zeta><zeta|,
    Pi h0=zeta/sqrt(I0),
    z(tau,kappa)=i c0/sqrt(I0) integral_0^tau
              exp[-i(tau-s)A(kappa)]zeta a(s,kappa) ds.       (X24)

The excluded auxiliary c is not a physical zero mode. The transverse
subspace is retained in A; z is not assumed to remain proportional to
zeta. Zeta's possible lack of H1_q regularity is harmless: the proof uses
bounded fiber operators and kappa derivatives, never D_b zeta.

## 6. Complete bracket, symmetric form, and its kernel action

The B/T normal form on physical sections is

    R_ab=C_ab(K)+A_b(K)partial_Ka,
    A_b=[H,J_b],
    C_ab=delta_ab P(ell_a-H0)P+B_ab,
    J_b=P[sin K_b cos(2q_b)]P-|h_b><h|-|h><h_b|,
    h_b=partial_Kb h.                                      (X25)

Here B_ab is exactly all of B13/T4. No rank term is deleted. All
coefficients are smooth bounded fiber operators; B13 contains no derivative
of the input in q. They extend R continuously from the common smooth core
to `H1_K(L2_q)` on compact K support. The stronger supported estimates are
used below only on f_free, never on the physical correction.

Define

    v_b(q)=sin(q_b)T_b,
    L_b=P cos(2q_b)P+|v_b><v0|+|v0><v_b|.

Expanding the exact current, including both rank terms, gives

    partial_Ka J_b(0)=delta_ab L_b,
    A_b(lambda kappa)/lambda -> kappa_b[H_*,L_b],
    C_ab(lambda kappa) -> delta_ab H_*(L_b-I).                (X26)

The last assertion can be checked before expanding ranks: on the common
core, with `D_a=i(H partial_Ka+Dcal_a)`, its constant coefficient is
`H partial_Ka J_b+[Dcal_a,J_b]-delta_ab H`. Since J_b(0)=0 as an
operator and as a q-dependent expression, the commutator term vanishes
there. Continuity of the bounded normal form gives the stated L2 identity.
This argument does not apply the unbounded Dcal to zeta.

For each pair a,b, put

    Q_lambda,ab=C_ab(lambda kappa)
                    +[A_b(lambda kappa)/lambda]partial_a,
    Q_0,ab=delta_ab H_*(L_b-I)+kappa_b[H_*,L_b]partial_a.

Then, on the fixed compact support,

    T_lambda R_ab u=Q_lambda,ab T_lambda u,
    Q_lambda,ab -> Q_0,ab in norm H1_kappa(mathcal H)->L2.       (X27)

Both exact and limiting first-order forms are symmetric on compact-support
H1 sections. For the exact form this follows first on the common smooth
core because D_a is symmetric, J_b is bounded self-adjoint and preserves
the core, and H is bounded self-adjoint. Consequently `-i[D_a,J_b]-delta_ab H`
is symmetric there. Continuity `H1_K(L2_q)->L2` and density extend the
pairing identity to the stated Sobolev domain. Alternatively, its coefficient
identity is `C_ab-C_ab^*=partial_Ka A_b`, with `A_b^*=-A_b`.
Integration by parts therefore gives the same form identity directly.
No self-adjoint extension or exponentiation of D_a is needed.

The limiting coefficient identity is explicit:

    delta_ab{H_*(L_b-I)-[H_*(L_b-I)]^*}=delta_ab[H_*,L_b]
       =partial_a(kappa_b[H_*,L_b]).                       (X28)

For any kernel-valued H1 field z, its first derivative is also kernel
valued. The complete limiting bracket therefore has the exact action

    Q_0,ab z=H_* L_b (delta_ab z+kappa_b partial_a z)
             =H_* L_b partial_a(kappa_b z),
    <z,Q_0,ab z>=0.                                        (X29)

The output in the first identity is in ran H_*, which is orthogonal to
ker H_* because H_* is bounded self-adjoint. Equivalently, move H_* to
the first entry and use H_*z=0. The identity holds after integrating over
kappa and pointwise in kappa wherever the derivative exists. It does not
say Q_0,ab z is the zero vector. For a unequal to b, both constant terms
in (X28) vanish and partial_a kappa_b=0; the first-order part is still
symmetric and (X29) still applies.

Combining (X23) and (X27) also supplies the vector limit

    lambda^-1/2 T_lambda R_ab psi_lambda(tau/lambda)
                   -> Q_0,ab z(tau) in L2,                 (X30)

uniformly for bounded tau, once the free-comparison estimate below is
inserted. A possibly nonzero vector in (X30) is compatible with the
vanishing pairing (X29).

## 7. Every term in the actual expectation

For `|tau|<=T`, free evolution preserves f_free's relative support and
`lambda||partial_Ka f_free(tau/lambda)||<=60+T`. The full source estimate,
including its global contact subtraction, is

    ||R_ab v_lambda(tau/lambda)||
       <=[4lambda^3+eta(32+12 B_a+12|tau|)]/n_lambda
       <=C_T lambda^(3/2),
    eta<=lambda^(3/2)/4,  B_a<60.                           (X31)

Also `||v_lambda||<=1/n_lambda=O(1)` and by (X9) or (X23),

    ||w_phys,lambda(tau/lambda)||=sqrt(lambda)||W_lambda(tau)||
                                                 <=C_T sqrt(lambda).
                                                               (X32)

For every fixed lambda>0 and finite physical time, psi, v and w_phys
belong to the same smooth compact-K-support domain. The commutators of
H and H0 with each individual first q or K derivative are bounded, all
derivatives of their coefficients are bounded, and P preserves smoothness.
Duhamel and induction therefore propagate every finite Sobolev order.
The bounds need not be uniform at these high orders. Thus the exact
symmetric pairing is legitimate:

    <v,R_ab w_phys>=<R_ab v,w_phys>.                        (X33)

In the following exact decomposition, every vector is evaluated at
physical time tau/lambda and W at rescaled time tau:

    <psi,R_ab psi>/lambda
       =<v,R_ab v>/lambda
          +2 Re<R_ab v,w_phys>/lambda
          +<W_lambda,Q_lambda,ab W_lambda>.                 (X34)

The first term is O_T(sqrt(lambda)) by (X31). The sum of cross terms
is O_T(lambda) by (X31)–(X33). This use of symmetry is essential: bounding
`<v,R_ab w_phys>` by `||v||||R_ab w_phys||` would give an inadequate
estimate. There is no assumption that v and w_phys are orthogonal.

The last term converges uniformly on bounded tau intervals to
`<z,Q_0,ab z>` by (X23) and (X27). For example, expand its difference as

    <W-z,Q_lambda,ab W>
       +<z,(Q_lambda,ab-Q_0,ab)W>
       +<z,Q_0,ab(W-z)>.

Uniform H1 bounds, coefficient convergence, and strong H1 convergence
make all three terms vanish. By (X29), the limiting pairing is zero.
Together with the first two bounds in (X34), this proves (X1).

There is a useful weaker-topology cross-check of this final step. The
expectation alone only needs (X21), a uniform H1 bound from (X13), and
symmetry of Q_0,ab. Indeed

    <W,Q_0,ab W>-<z,Q_0,ab z>
      =<W-z,Q_0,ab W>+<Q_0,ab z,W-z>,                        (X35)

which tends to zero already by strong L2 convergence and uniform H1
boundedness. The coefficient difference is controlled by (X27). Thus
the expectation proof has this additional check; it is not logically
dependent on inferring a derivative limit from a state-norm limit.

At tau=0, W=z=0 and (X31) directly gives the result. Negative finite
tau obeys the same estimates with absolute times as explained after
(X17). No statement here covers tau growing without bound as lambda
tends to zero, and no numerical rate for the gapless limit is claimed.

## 8. Checks, failed shortcuts, and remaining scientific gate

The new load-bearing argument is the explicit analytic proof (X14)–(X23)
and the exact symmetric-form decomposition (X34). The spectral theorem for
a bounded self-adjoint operator, unitarity, finite-net compactness, bounded
operator differentiation, and integration by parts are the mathematical
tools used; all relevant hypotheses are checked above. No external
literature value or continuum extrapolation supplies a theorem premise.
`boost_current_expectation/AUTHOR_CHECK.md` records a corrected-approximate-
solution check of the cutoff identity, an explicit continuous-spectrum
diagnostic for the absence of a claimed rate, the all-index form check,
and the small-tau match to the previously checked Gamma_b. These remain
author checks, with no claim of independent review.

The source's nonzero differential coefficient and mixed-band counterexample
remain unchanged. The previously reviewed T1–T24 norm obstruction remains
unchanged. In particular (X1) is not a norm improvement, a uniform operator
claim on a low-energy window, or a result for other preparations.

The following shortcuts were considered and not used as proof:

* Substituting inverse-energy time in the old norm upper bound does not
  decide the expectation. Its failure as a tool is preserved, not recast
  as a physical obstruction.
* Isolating the initial Pi component ignores its cancellation with the
  projected free state. Equation (X8) keeps the exact initial condition.
* An inverse on the complete gapless complement is unavailable in this
  argument. Only the cut-off inverse in (X16) is used.
* Compact-vector convergence is not operator-norm convergence. The finite
  epsilon-net proof in (X15) specifies exactly the uniformity used.
* A kernel-only bound on an unproved error would be invalid. Equations
  (X20)–(X22) first control the entire physical error with unitary estimates.
* Dropping the source's phase derivative, the derivative coefficient of R,
  either canonical current rank term, or the common-domain check would
  leave a different calculation. Each is retained explicitly.
* The recovered C2/finite-difference proposal is unnecessary: direct
  differentiation of the exact error equation proves the needed statement.

The separate source-bound independent review checked the cutoff limit,
the differentiated error equation, exact normalization and symmetric form
pairings, and reconstructed an alternative free-primitive/Volterra proof.
Root's mechanism suggestions are disclosed coauthorship. A finite-dimensional
model or passing provenance check cannot certify this infinite-dimensional
gapless theorem. No scientific runner is claimed to do so.

Full source identities, recovery copies, author checks and limitations are
preserved losslessly under the milestone evidence's `boost_current_expectation/`
and `boost_expectation_review/` paths. The original checkpoint and
initial manifest were copied byte for byte before further work. No
editable prompt files changed. No repository edits, PR, merge, audit,
physical-axiom change, other-chat message, delegation, model override, or
campaign-deadline extension was performed by this worker.
