# LAYER-THM: the conditional layer part

**Distilled by Codex from Codex generation texts; not refereed.**

FINISH row 451, `layer-distil`. Source checkout:
`5175a10c0a885a7e8c8a4c44ef0e8f43eaa8d8f1`, 7 November 2026.
Research text, not an audit; this part grants no scientific or frozen status.
All proofs are written arguments. No run discharges a mathematical assertion.

Credit Tadeusz Bałaban for the averages, gauges, propagators, walks and
response method. Credit Ethan Sussman and Levent Alpoge, with Claude and
Codex as authors of their account, for the account and outline. The carrier
input `b98p5-r3.md` was written by Claude; its local analytic port was
written by Codex. These attributions are distinct from independent review.

The generation sources, in order, are [layer-pkg](layer-pkg.md),
[walks-gw](walks-gw.md), [layer-r3](layer-r3.md) and [adm-pl](adm-pl.md).
The repairs are those of [layer-thm-gate](../gates/layer-thm-gate.md),
[b98p5-r3-gate](../gates/b98p5-r3-gate.md) and
[pi-r2-gate](../gates/pi-r2-gate.md). The named analytic inputs are
[Theorem PI](print-inverse-r2.md) and [B98-P5](b98p5-r3.md), at their
repaired scopes. Earlier acceptance of a component is not a check of this
distillation or of the later GW, current-identification and admission texts.

I, II, III and SA denote the supplied files
`theorem_0_complete_account_raw_{I,II,III}.tex` and `YM4_sketch_500.tex`
at owner-supplied revision `31a47c543775`. References are physical lines.
The source directory is a snapshot, not a separately established Git HEAD.
The recorded byte identities are:

| Source | SHA-256 |
|---|---|
| I | `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93` |
| II | `6a1f74b05f74ba44a2186c11fb08e139178d86b15c1494a95c434212944b2b8f` |
| III | `7e36523b85fb4f85aefdd45ab175420459f24e34fe56a4e83e53a6829c7a352d` |
| SA | `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f` |

## 1. Contract, objects and named imports

The target is the layer package **assumed** at I 72392–72399, with the
concrete uses U01–U34 located by `layer-find.md`. It comprises clauses
(a)–(f), a corollary, parameterization, a uniqueness domain and the current
rider. Its missing clause (e) is not reconstructed by choosing a convenient
fifth statement. Below it is an explicit unresolved import. Thus the result
is one implication, with a substantive proof of the specified clauses and
no claim that the account's whole construction satisfies its premises.

The outline index, its neighbouring rows and `obligations.md` lead to
SA 10354–10464 and 10562–10582: reduce the equation before switching;
physical inverse identities do not hold for arbitrary switched sums.
SA 5663–5759, 9593–9625, 10111–10139, 11550–11568 and 15901–15931 keep
local gauges, full domains and larger-disc admission as inputs. The
conditional comparison already in II §5.8 is reused, not re-proved.
Balaban's original papers are not evidence newly inspected here; the
attribution uses `lit-balaban.md` and quotations in the cited notes/account.

### 1.1 Norms and the fixed equation

Fix a finite four-dimensional hierarchy, $SU(N)$, odd $L\ge3$,
fine spacing $\eta$, and $\ell_j=L^j\eta$. Use the enlarged cells,
full difference stencils and actual admitted weights of the consumer.
Put
\[
 N_y(a)=\max\{\ell_y|a|_y,\ell_y^2|\nabla_Wa|_y\},\qquad
 N_y^\Delta(a)=\max\{N_y(a),\ell_y^3|\Delta_Wa|_y\},
 \tag{1}
\]
where $\Delta_W$ is the component covariant Laplacian, not the Wilson
Hessian $\mathcal D(W)$. Write $E,E^\Delta,B,F$ for these first-order
and graph field spaces, dimensionless block data, and sources of weight
$-3$. For an admitted positive $p\in\mathfrak M_\delta$,
\[
 \|a\|_p=\sup_yN_y(a)/p(y),\quad
 \|a\|_p^\Delta=\sup_yN_y^\Delta(a)/p(y),\quad
 |f|_{-3,p}=\sup_y\ell_y^3|f|_y/p(y),\quad
 \|d\|_{\mathrm{dat},p}=\|j\|_p^\Delta+|b|_p,
 \qquad d=(j,b).
 \tag{2}
\]
The first datum $j$ is a field. The base current $J$ is an independent
complex source with only its weight-$-3$ ceiling; no derivative or
own-current condition is imposed. Block weights use the consumer's actual
block-to-cell convention. In particular $p=1$ is admitted and
$p(z)\le e^{\delta d^\wedge(y,z)}p(y)$. Any further conditions defining
$\mathfrak M_\delta$ must also be met. Transposes use the physical
bilinear trace pairings, with fine measure $\eta^4$ and row measure
$\ell_j^4$, not Hermitian adjoints.

At switches one the specified operators are
\[
\begin{gathered}
 G_0=(\mathcal D(W)+D_0RD_0^T+Q^TaQ)^{-1},\quad
 q_0=(QG_0Q^T)^{-1},\quad a=\ell^{-2},\\
 H_0=G_0Q^Tq_0\ell^{-1},\qquad B_0=G_0-G_0Q^Tq_0QG_0,\\
 G_\pi^J=(I-G_0\Theta'_J)^{-1}G_0,\quad
 q_J=(QG_\pi^JQ^T)^{-1},\quad H^J=G_\pi^JQ^Tq_J\ell^{-1},\\
 \langle A,\Theta_JA\rangle=2\langle H^JC^{(2)}(\ell A),J\rangle,
 \qquad \widetilde G^J=(I-B_0\Theta_J)^{-1}B_0.
 \tag{3}
\end{gathered}
\]
Here $Q,Q'$ are the literal CMP 98 rows, $R$ is the scalar gauge
projection, and $\Theta'_J\ne\Theta_J$. At switches these symbols mean
the assigned words and composites, not inverses of switched operators.
Each primitive concatenation, including its side branches, receives one
factor per distinct visited decoupling cube. A composite retains the
**product of its primitive tags**. Identity pieces are expanded as
$I=\sum_\tau h_\tau^2I$, with the PI cutoffs and full footprints.
Retagging a composite by its union defines a different function.

Set $H=H^J(\sigma)$, $G=\widetilde G^J(\sigma)$, $SA=\ell A$,
$\Gamma=G\Theta_J$ and $T_\sigma=I+\Gamma$. The equation is
\[
 z=-T_\sigma j+\Gamma H_0b-GV'_\sigma(z+H_0b),\quad
 A'=z+H_0b,\quad X=C_\sigma(SA'-SHX),\quad h=A'-HX.
 \tag{S5}
\]
The seven-term nonlinearity is fixed, not an arbitrary quadratic map.
Writing $D(A)=X(A)$, $\mathfrak D=D_AD$,
$D_3=D-C^{(2)}(SA)$, $\mathfrak D_3=D_AD_3$, it is
\[
\begin{split}
 V'(A)={}&-\mathfrak D_3^TH^TJ-Q^T\mathsf kD
 -\mathfrak D^T\mathsf k^TQA+\mathfrak D^T\ell^{-1}\mathsf kD\\
 &+(I-H\mathfrak D)^T\nabla V_0(A-HD)
 -\Lambda^T\mathfrak j_J(HD)-\mathfrak D^TH^T\mathfrak k_J(\Lambda A),
 \qquad \mathsf k=(q_J-a)\ell^{-1}.
 \tag{4}
\end{split}
\]
All coefficients, pairings and tags are those of I 14156–14375 and
15266–15320. At $j=0,\sigma=1$ this is the account's block chart.
Identification of another field equation with (S5) is a premise below.

### 1.2 Named imports and premises

The list has nine groups. A name denotes its entire stated scope, not
merely a bound at the physical centre. UA's six names are kept separate
because their missing suppliers differ. Constants are common over all
invocations, intermediate bases, determining sets and full parameter
domains $D_U$, independent of mesh, depth and volume. They may depend on
fixed rank, (L), Hölder exponents, chosen model geometry and switch radius.

**PI.** Import repaired Theorem PI of `print-inverse-r2.md` §§2–3, with
its flat input [F] and fixed order of constants. Use literal corner blocks,
no inward rows, fine field bonds with at least one endpoint in $\Omega_0$,
scalar sites in $\Omega_0$, zero extension, and the compressed
**whole-action** Hessian. Its coefficient read includes protruding
plaquettes in $\Omega_0^+$. Require (S1-loc): one real small gauge on
each complete $N(x)$, half-width $r_N\ell_{\lambda(x)}$, with
$\ell_{\lambda(z)}|A|,\ell_{\lambda(z)}^2|\nabla A|\le L^2a_0$.
Exterior sites have height zero. Require (S2) and exterior (S2+) on all
coefficient reads, the separated-tower floors, divisibility and torus room.
PI supplies the bare inverse and
\[
 |q_0(y,y')|\le C_q\ell_j^{-2}\ell_{j'}^{-4}
 e^{-\delta_qd(y,y')},
 \tag{5}
\]
with source measure $\ell_{j'}^4$, absolute local walks, spare decay
and same-grid setting compatibility. Use at most $\delta_q/17$ for
the anchored-tree reserve $17D_X(n+1)$, and impose shell floors at the
common smaller rate. PI does not supply termwise lattice covariance of
the account's entire one-family input.

**GW.** Import the graph-walk theorem of `walks-gw.md`, with its common
choice of PI constants in strong source/output spaces and its literal
word convention. In particular, for every admitted weight and
$|\sigma|\le e^{\kappa_1}$,
\[
\begin{split}
 \|H_0b\|_p^\Delta&\le C_\kappa|b|_p,\qquad
 \|Gf\|_p^\Delta\le g_\Delta|f|_{-3,p},\\
 \|G\Theta_Ju\|_p^\Delta&\le C_\kappa|J|_{-3}\|u\|_p,\qquad
 \|D(GV'_\sigma)(A)u\|_p^\Delta\le C_\kappa r\|u\|_p
 \quad(N(A)\le2r).
 \tag{6}
\end{split}
\]
Retain its first-order, Hölder, physical-transpose and local-vertex
majorants and locally uniform absolute tails. Every endpoint graph
majorant includes source measures, full stencils and cutoff coefficient
reads. This import is on the chosen admitted PI class, not an arbitrary
older radius or another word assignment with the same unswitched sum.

**AV (B98-P5).** Import the local analytic port, as used by `b98p5-r3`
§§3–4 and repaired by its gate, on $\mathfrak S^{\rm pl}$ or a supplied
complete-carrier frame. Besides S1–S3, its real reference obeys
\[
 \|U_r(\partial p)-I\|_F\le\sqrt N\alpha
 (\eta/\ell_{\lambda(p)})^2,\qquad \alpha\le8a,
 \quad\lambda(p)=\min_{x\in p}\lambda(x).
 \tag{PL}
\]
It supplies the literal nonlinear average, fine physical derivative
densities, second and third directional derivatives and transpose
contractions on a common larger analytic ball. In four dimensions the
counting derivative is $\eta^4$ times the density. Keep the increment
and background thresholds of the cited published statements separately
from the port's explicit constants. The local port has not been
independently certified by the carrier checks.

**UA (uniform admission).** Assume `adm-pl` Theorem UA on every actual
read throughout $D_U$, with the following named premises.

* **R:** a specified real reference $W=e^{i\eta a'}U_r$, S1–S3,
  and complete-read plaquette witnesses with coefficient at most $8a$
  after grade conversion. A witness is a direct bound, a full gauge,
  the post-step crossing proof, the thick-cover proof, or (12) below.
* **A0:** every positive-height row and transpose has its full double
  block, branch, local-lift room and finer collar in that domain; include
  actual minimizer-tube and bounded-gauge premises where that route is used.
  AV is the analytic input. A supplied frame can replace the PL carrier route.
* **L0:** every full PI patch has its real S1-loc gauge, by matched
  thickness or direct supply, with S2+ on all exterior coefficients.
  Identify rows, spaces, Hessian, boundary, rates, currents and room.
* **S:** every stage/earlier-frame Q5 and Q8 read and its grade conversion
  is covered; beyond $Y^+$, supply an admitted ambient reference or
  (12). If cube heredity is used, retain its exceptional cube supplier.
* **T:** independently admit all reached intermediate bases and data
  on the entire prescribed complex domain, including the actual
  minimizer/product tubes. A layer estimate cannot admit its own input.
* **P2:** for paired uses, admit both real-reference cutoff families,
  the free finer collar and T for complex parents and interpolations.

R's **plaquette component**, but not its S1–S3 or reference-entry
requirements, may instead be supplied by the hereditary clause
\[
 |U_r(\partial p)-I|\le a(\eta/\ell_{\lambda_F(p)})^2
 \quad\text{for every retained earlier frame }F
 \text{ and every complete read }p\text{ in }F.
 \tag{12}
\]
Raw frames, both tower rules and required collars are included.
This is `adm-pl` (12), an additional clause, not a printed property
of relaxed $K_{109}$ or $K_P$. New references and frames need entry.

**ID (equations and structural inputs).** Match each use's actual
operators and nonlinear functions to (3)–(4), (S5) and the admitted
coordinates. Retain **EQ**, their gauge/conjugation/restriction
intertwiners including tags; **LC**, full-footprint component restriction
and both datum slots zero on any asserted zero-data component; and
**PH**, K6 at I 15669–15701 on its admitted unswitched own-current
block chart. For PH, both solutions lie in the present uniqueness
domain or in that chart's known uniqueness domain. Its current is
the physical increment. These hypotheses include transport of bounded
complex-gauge overlap charts, not invariance under all complex gauges.
They do not identify independent-current functions from their physical
values alone.

**M (switched current).** Supply the actual reduced $P_1(\sigma)$ and
$m_H(\sigma)$ assignments, including their local diagonal terms, with
holomorphy, physical pairings, full-footprint locality and
\[
 |P_1u|_{-3,p}\le p_1\|u\|_p,\qquad
 |m_Hb|_{-3,p}\le m_1|b|_p.
 \tag{7}
\]
Identify the current used by each link with the rider (18)–(19) below.
Also retain the native local coefficient input **RJ**, for
$K_W=D_1^TD_1+D_0D_0^T-\Delta_W$ and the analytic remainder $F(W,0)=0$:
\[
\begin{split}
 \ell_y^3|K_WB|_y&\le18d\,\mathsf p(W)\ell_y|B|_y,\quad
 \mathsf p(W)\le1,\\
 \ell_y^3|F(W,h)|_y&\le K_J(\mathsf p(W)+\Theta_0+\Theta_1)
 (\Theta_0+\Theta_1),\quad \Theta_0+\Theta_1\le2N_y(h),
 \quad N_y(h)\le1/20.
 \tag{RJ}
\end{split}
\]
For cut riders include the transport, collar and field-smallness
conditions in §2. M is not supplied by the bounded candidate (M1) below.

**FM/FD (field convention).** For a source-bearing use, identify its
prescribed first-slot operator $B_\sigma^{\rm use}$, rows, boundaries,
tags and source space with a GW operator for which
\[
 \|B_\sigma^{\rm use}f\|_p^\Delta\le K_\#|f|_{-3,p}
 \tag{FD}
\]
and full-footprint support hold. **FM** is equality of the actual
forced equation with (S5) at its **prescribed** datum
$j=B_\sigma^{\rm use}f$, including its nonlinear convention and branch.
If the force is $-G_\sigma f$, this requires
$(T_\sigma B_\sigma^{\rm use}-G_\sigma)f=0$.

**E(e).** Supply the literal unnamed clause (e) and its applicability
and transport on the domains where U01/U08 assert the whole package.
No independent mathematical content for it was found in the generation
sources. The specialization result below is proved but is not assigned
as a substitute for that clause. The full six-clause reading remains
parametric in this unresolved statement.

**RC.** For U33 import II 5.8:thm-response-comparison
(55882–56284), the energy-difference lemma (57711–57865) and the
three-member consequence (58123–58205), with all their native hypotheses.
Match the responses, independent slot vectors, cross-grid map, logarithms,
frames and boundaries on the full data domains. Supply exact pairing,
real references, six-residual and extension/transfer identities, local
action, constraint, divergence, projection and gauge-component comparisons,
the native Hölder/multiplier estimates, discrepancy profiles and radii.
Where the actual response uses the other off-shell functional, complex
ancestors or nontrivial switches, supply the additional linear comparison
and defects described in §3.8. A separate N1 bound on each frame is not RC.

## 2. Statement of the conditional theorem

**Theorem LAYER (implication).** Assume PI, GW, AV, UA and ID on the
specified common domains. Assume M/RJ for the four-entry current package,
FM/FD at source-bearing uses, E(e) for the literal whole-package assertions,
and RC for U33. Then the following layer package holds, with the
qualifications in its clauses and the final table.

On the admitted analytic base/switch domain the inputs give constants
$h,h_0,g,\theta,c,v$, enlarged to at least one where appropriate, such that
\[
 \|SH\|\le h,\quad\|H_0\|_{B\to E}\le h_0,\quad
 \|G\|_{F\to E}\le g,\quad\|\Theta_J\|_{E\to F}\le\theta,
 \tag{8}
\]
\[
 C(0)=DC(0)=0,\quad\|D^2C(u)\|\le c\ (|u|<s_C),\qquad
 V'(0)=DV'(0)=0,\quad |V'(A)|_{-3}\le vN(A)^2\ (N(A)<s_V).
 \tag{9}
\]
The latter estimate is on the inner branch with the analytic room used
below. Put $q=gv$, $t=1+g\theta$, $k=g\theta h_0$,
$a_*=1+h_0+t+k$, and choose
\[
 0<r\le\min\{s_C/32,s_V/8,(64ch)^{-1},(64q)^{-1}\},\quad
 r_X=8cr^2,\qquad\varepsilon=r/(8a_*).
 \tag{10}
\]
Reduce $r$ using the uniform weighted constants so that
$c_wr h_1\le1/2$, $\nu\le1/2$, and the rider's local smallness
holds where it is used. The weighted bounds needed in the proof are
\[
\begin{array}{lll}
 \|Hb\|_p\le h_1|b|_p,&\|H_0b\|_p\le h_0|b|_p,&
 \|\Gamma u\|_p\le\gamma\|u\|_p,\\
 |DC(v)Su|_p\le c_wr\|u\|_p,&
 \|D(GV')(A)u\|_p\le\nu\|u\|_p,&\\
 \|H_0b\|_p^\Delta\le h_\Delta|b|_p,&
 \|\Gamma u\|_p^\Delta\le\gamma_\Delta\|u\|_p,&
 \|D(GV')(A)u\|_p^\Delta\le\nu_\Delta\|u\|_p.
\end{array}
 \tag{W}
\]
Here $|v|\le3r$, $N(A)\le2r$, and $\|Su\|_{0,p}\le\|u\|_p$.
These are deductions from the named majorants, not a premise called N1.

**(a) Small solution.** If $\|d\|_{\mathrm{dat},1}<\varepsilon$,
(S5) has exactly one solution in
\[
                         N(z)\le r,\qquad |X|\le r_X.
 \tag{11}
\]
The triple $(h,A',X)$ is jointly holomorphic in admitted base coordinates,
independent current, switches and data, and vanishes at zero datum.
Uniqueness is only in (11), not among all fields.

**(b) Four entries.** At a fixed kernel, for any two admitted data and
every admitted weight,
\[
 \max\{\|\delta A'\|_p^\Delta,\|\delta h\|_p,
 |P_1\delta A'|_{-3,p},|m_H\delta X|_{-3,p}\}
 \le B_H\|\delta d\|_{\mathrm{dat},p}.
 \tag{N1}
\]
There is no graph-norm conclusion for $h$. The intermediate
$|\delta X|_p$ estimate is not an extra consumed entry.

**(c) Covariance and reality.** EQ transports the solution whenever the
transported data and solution lie in the target uniqueness domain.
Real inputs give real solutions. Bounded complex-gauge charts agree on
their admitted overlaps after shrinking the datum radii to fit both balls.

**(d) Physical identification.** Under PH, at $j=0,\sigma=1$ and
$J=\mathcal J(W)$, $h$ is the specified Landau representative of
Balaban's response and the rider is its physical current increment.
Holomorphic continuation stays within that paired physical family.

**(e) Unspecified side clause.** The literal clause is retained solely
through E(e). No independent proof or invented replacement is asserted.
The independently proved specialization property is: restricting the
parameters/data, or giving identical operators in two admitted descriptions,
gives the same small solution on the overlap with the same bounds.

**(f) Components.** Under LC, solution and rider commute with restriction
to retained wall-components. Both vanish on a component with zero data.
Vanishing off the retained region also requires the field forcing there
to vanish; a bounded extension of the independent current does not imply it.
Exempting a subfamily of cubes is substitution of switch value one there.

**Corollary.** Relative to zero datum, each local N1 entry is bounded by
$B_H\|d\|_{\mathrm{dat},p}p(y)$, and independently
\[
                   N_y(HX)\le N_y^\Delta(A')+N_y(h).
 \tag{13}
\]
For admitted $p(y)=e^{-\delta_Pd^\wedge(y,\operatorname{supp}b)}$
the block-only bound is $B_H\sup|b|\,p(y)$. Under FM/FD the field-source
bound at $j=B_\sigma^{\rm use}f,b=0$ is
$B_HK_\#\sup\ell^3|f|\,e^{-\delta_Pd^\wedge(y,\operatorname{supp}f)}$,
with the corresponding component support. Mixed data use the sum norm (2).

**Parameterized form.** Holomorphic substitution is allowed on the
admitted domain. A finite chain is jointly holomorphic only if every
intermediate image stays in its own domain on the whole product polydisc.
Cauchy estimates apply on closed subpolydiscs with an actual surrounding
margin. No uniform boundary derivative estimate follows from an open tube.

**Current rider.** Define, with the actual assignments supplied by M,
\[
 J^\sharp[1]=(\Delta_W-P_1+K_W)A'-m_HX+F(W,h),
 \tag{18}
\]
\[
 J^\sharp[\chi]=(\Delta_W-P_1+K_W)(\chi A')-\chi m_HX
       -[D_1^TD_1,\chi]HX+F(W,\chi h).
 \tag{19}
\]
They are holomorphic. With $K_{\mathsf j}=3+18d+9K_J$,
\[
 \ell_y^3|\delta J^\sharp[1]|_y\le K_{\mathsf j}
 \max\{N_y^\Delta(\delta A'),N_y(\delta h),
 \ell_y^3|P_1\delta A'|_y,\ell_y^3|m_H\delta X|_y\}
 \tag{20}
\]
when the two local fields have $N_y(h_i)\le1/40$.
For the repaired bump of §3.6, let
$\chi=t+\tau\widehat\chi_\square$, $0\le t\le1$, with
scale $M\ell_\square$, $M\ge2L^2$. Require elementary transport
norm at most $\vartheta\le5/4$, the collar bound
$\ell_y\le L\ell_\square$ wherever its commutator stencil meets
the bump, and $N_y(\chi h)\le1/40$. Put
$c_d=(2+4\vartheta)(d-1)$, $c_\zeta=2c_d$. Then
\[
\begin{split}
 \ell_y^3|J^\sharp[\chi]|_y\le(K_{\mathsf j}+c_\zeta)
 \max\{&N_y^\Delta(\chi A'),N_y(\chi h),
 \ell_y^3|P_1(\chi A')|_y,\ell_y^3|\chi m_HX|_y,\\
 &|\tau|N_y(HX)\mathbf1[\widetilde\Delta(y)\cap\square\ne\varnothing]\}.
 \tag{21}
\end{split}
\]
This is an implication for a furnished triple; it does not claim that
cutting a triple solves a new layer equation. U27 instead uses the local
second slot $\chi J^\sharp[1]$, not $J^\sharp[\chi]$.

Under RC, U33 additionally has the linear, full-domain comparison of
§3.8. Every conclusion and every table row retains the named imports
and the consumer's other explicitly supplied antecedents.

## 3. Proof

### 3.1 Admission and a common order of constants

The following are the admission deductions of `adm-pl`, with the repaired
B98 carrier input. They supply implications from UA's witnesses; they
do not establish those witnesses throughout the induction.

In one real gauge containing a plaquette and both parallel-bond
difference pairs, suppose $U_r=e^{i\eta A}$,
$\ell|A|,\ell^2|\nabla A|\le r$, $\sqrt N r\le1$.
Replace the two shifted potentials by their values at the initial corner.
Duhamel's formula, whose outer factors are unitary, costs
$2\sqrt Nr\eta^2/\ell^2$. Integrating the remaining group commutator
in its two parameters costs at most $2Nr^2\eta^2/\ell^2$. Hence
\[
 \|U_r(\partial p)-I\|_F
 \le(2\sqrt Nr+2Nr^2)(\eta/\ell)^2
 \le4\sqrt Nr(\eta/\ell)^2.
 \tag{22}
\]
Conjugation back preserves this norm. For normalized HS divide by
$\sqrt N$; in operator norm the same calculation gives
$2r+2r^2\le4r$. A gauge at level $m$, read at the client's level
$q$, therefore costs $4rL^{2(q-m)_+}$; a direct curvature bound
of coefficient (b) costs $bL^{2(q-m)_+}$. Ordinary and covariant
differences are not interchangeable without their stated comparison.

For a post-step crossing plaquette, let its corners lie in $\Omega_n$
with one inside and one outside $\Omega_{n+1}$, $1\le n\le k$.
Set $s_n=CM\ell_n\ge2\eta$, $C\in\{1,2\}$, and require
\[
 \operatorname{dist}_\infty(\Omega_n^c,\Omega_{n+1})\ge s_n,
 \qquad
 \operatorname{dist}_\infty(\Omega_{n+1}^c,\Omega_{n+2})\ge s_n.
 \tag{23}
\]
In the admitted nonwrapping lift choose a fine-lattice cube of side
$s_n$ containing the four corners. Each site of its half-open lift
is at distance less than $s_n$ from each corner. The inside corner
and first gap place the cube in $\Omega_n$; the outside corner and
second gap exclude $\Omega_{n+2}$. The cube meets
$\Omega_{n+1}^c$, so it is a tested cube. Its supplied gauge on its
intersection with the actual domain contains the whole plaquette.
Equation (22), with $r_n=BCM\alpha_{0,n}$, proves coefficient
$4BCM\alpha_{0,n}$. Single-stratum plaquettes have the direct
coefficient at most $(1+\beta)\alpha_{0,n}$. Thus use
\[
 C_{\rm post}=\max\{1+\beta,4BCM\},\qquad
 \sup_n\alpha_{0,n}\le
 \min\{a/C_{\rm post},(\sqrt NBCM)^{-1}\},\quad
 \sup_n\alpha_{1,n}\le a/(1+\beta).
 \tag{24}
\]
These give S1′ and the existing twist ceiling on the covered domain.
They supply no raw $n=0$ stratum, no outside values and no new real
reference. A graph-distance gap must first be converted to the sup norm.

The thick-cover route is also explicit. At each level $q$, including
zero for an **all-plaquette** result, require aligned cells of side
$s_q\ge12g_q$, a multiple of $g_q=M_b\ell_q$, and the stated gap
and lift floors. For $q=\lambda(p)$, every cell met by the product
of the plaquette's coordinate ranges contains a corner. All such cells
are in $\Omega_q$. Their product union is a box there with each
side at least $12g_q$. Aligned rounding encloses the plaquette in
a size-$12g_q$ cube: if a run $[e_0,e_1]$ has length at most
$11g_q$, start at the grid point just below $e_0$, unless the
right boundary requires the last length-$12g_q$ interval in the
box. Either interval contains the run. A corner outside
$\Omega_{q+1}$ makes it a test cube; the gap excludes
$\Omega_{q+2}$. Equation (22) gives PL with $\alpha=4r$.
Thus $r\le a$ suffices for PL, and $r\le a/4$ for S1′,
once the other S clauses are supplied.

The weaker carrier-only argument needs thickness only at positive
levels. The carrier $E_c$ of a height-$j$ row lies in
$\Omega_{j-1}$ when $RM_b\ge L$, so PL gives
\[
 \|U_r(\partial p)-I\|_F\le8\sqrt NL^2a(\eta/\ell_j)^2
 \quad(p\subset E_c).
 \tag{25}
\]
Alternatively, under thickness, if its second block leaves
$\Omega_j$, round at level $j-1$; the two gaps put the resulting
cube in $\Omega_{j-1}\setminus\Omega_{j+1}$. If both blocks lie
in $\Omega_j$, round inside the product of their included thick
cells; the next gap excludes $\Omega_{j+2}$. In either case one
size-12 test cube contains the carrier, at level $j-1$ or $j$.
Equation (22) gives the sharper $4\sqrt NL^2a$ in (25).
Height-zero averaging is linear; this does not exempt height-zero
plaquettes from an all-plaquette hypothesis.

The two tower rules remain distinct. Rule r2 gives thickness when
its cell/test-grid ratio is divisible and at least 12, with the gap
and room floors. Increasing the gap in rule r1 does not enlarge its
cells to side 12. The latter needs a separate full plaquette or gauge
supplier. On a paired frame, keep the half-open blocks: for anchored
blocks choose the coordinatewise greatest corner of $p$; for centred
blocks choose a positive-level corner if one exists, otherwise the
greatest corner at level zero. The existing size-$2\ell_r$ box then
contains all four bonds and both difference pairs, with
$\ell_r\ge\ell_{\lambda(p)}$. This proves coefficient $4r_0$
without adjoining boundary sites. The finer collar still needs those
frames over its own complete determining set.

The carrier gauge of B98, fixed by $U_r$, follows by plaquette
slides along a coordinate tree. At most $2(d-1)\ell_j/\eta$
slides are needed per bond. Equation (25) bounds its deviation by
$16d\sqrt NL^2a\eta/\ell_j$. On $E_c\subset\Omega_{j-1}$
the twist has scaled Frobenius size at most $L\sqrt Na_1$.
The logarithm/product estimate therefore gives the supplied frame
$W=e^{i\eta B}$, $\ell_j\|B\|_{\infty,F}<\rho/8$, using
the constants of `adm-pl` (7):
\[
\begin{gathered}
 p_0=8dL,\quad n_*=4d(4L+1)^d,\quad r_0=(2^{24}p_0)^{-1},\\
 B_*=2^{24}n_*^2L^dr_0^{-2},\quad
 \rho=r_0/(2^{20}B_*),\quad K_*=128d^2L^2,
 \quad a_B=\rho/(16\sqrt NK_*),\\
 a=\tfrac12\min\{a_B,a_0^{PI},a_1^{PI},(16\sqrt N)^{-1}\}.
 \tag{26}
\end{gathered}
\]
If $\ell_j\|v\|_F<\rho/16$, set
$B_v=(i\eta)^{-1}\log(e^{i\eta v}e^{i\eta B})$. With
$h_*=\eta/\ell_j\le1$, the exponential series gives
\[
 \|e^{i\eta v}e^{i\eta B}-1\|_F
 \le h_*(3\rho/16)e^{3\rho/16}<h_*\rho/4.
\]
Since $\rho<1/16$, the logarithm series is bounded by twice
this quantity. Thus $\ell_j\|B_v\|_F<\rho/2$. Every carrier
bond has grade at least $j-1$, so
\[
 r_A=\rho/(64L),\qquad
 \sup_b\ell_{\lambda(b)}\|v(b)\|_F<4r_A
 \tag{27}
\]
fits all these larger carrier balls. AV now gives derivatives and
transpose densities with spare Cauchy room at radius $r_A$.
The repaired constants valid for both account norm conventions are
$c_4=\rho/\sqrt N$, $C_2=4N/\rho$, $C'=8N/\rho$,
$C_3=16N/\rho$. Bounded complex conjugations of adjoint norm
at most $K$ in both directions require radius $r_A/K$; the
right-logarithmic derivative loses at most $K^2$. For an ambient
matrix derivative also include the averaged output's matrix norm.

For a minimizer-supplied reference keep the **actual** positive
$C_1^{(172)}$. With $\chi_N=1$ for operator-norm data and
$\chi_N=\sqrt N$ for normalized-HS data, a sufficient log-datum
radius is
\[
 r_{\rm ext}=\min\{(2\chi_N)^{-1},
 C_1^{(172)}\epsilon_1/(2\chi_N)\}.
 \tag{28}
\]
The exponential bound then meets the published continuation radius.
Also require $\epsilon_2=B_5\epsilon_1$,
\[
 B_3\epsilon_1\le8a,\quad B_5\epsilon_1\le a,\quad
 48d\sqrt NB_5\epsilon_1\le\log2,\quad
 B_3\epsilon_1\le\alpha_0^{(98)},\quad
 B_5\epsilon_1\le\alpha_1^{(98)}.
 \tag{29}
\]
The published gauge identification is a retained input. Once applicable,
its path product estimate, with $t_j=d\sqrt N\epsilon_2L^{j+1}\eta$,
gives adjoint norms bounded by
$\exp(10\sum_jt_j)\le\exp(15d\sqrt N\epsilon_2)\le2$.
The factor 4 for right-logarithmic row derivatives follows by covariance
on the input and output legs. A doubled tube requires $2r_c<r_{\rm ext}$,
or the corresponding bound for the actual nonlinear datum map.
For a proved bound $\|B(z)\|\le C_{\rm dat}\|z\|$, radius
$r_{\rm ext}/(4C_{\rm dat})$ supplies a doubled ball.
Replacing $C_1^{(172)}$ by $\max(C_1^{(172)},1)$ is invalid.
For $r_c=a_A/10,\epsilon_1=a_A/2$, the doubled comparison needs
$C_1^{(172)}>4\chi_N/5$; lowering $a_A$ does not change that ratio.

Clause (12) is preserved exactly by a defined fixed-real-reference
layer, complete-read restriction, discarding retained frames, unitary
gauge and simultaneous change of units. In the first three operations
the bound is literally an old inequality; conjugation preserves it;
unit changes preserve $\eta/\ell$. A new grade lower than the old
one weakens the bound. Raising the grade by $g$ costs $L^{2g}$
and needs a fresh gain. For finitely many frames, putting
$h(p)=\max\{\ell_{\lambda_F(p)}:F\text{ reads }p\}$ shows that
(12) is precisely $|U_r(\partial p)-I|\le a(\eta/h(p))^2$.
The analogous coefficient $8\sqrt Na$ is the least Frobenius PL
condition for that reference and read family. This proves heredity of
the plaquette clause only; S2, currents and new entries remain inputs.

The final coupling ceiling can implement supplied radius envelopes
without computation. If the source gives
$\gamma_0^{(k)}\le A t_k^p e^{-t_k/2}$, $p\ge0$, it suffices that
\[
 t_\gamma\ge\max\{4,2p+c_\beta,64p^2,
                         4\log^+(2A/\epsilon)\}.
 \tag{30}
\]
Indeed $\log t\le2\sqrt t$ follows by integration, whence
$p\log t\le t/4$ for $t\ge64p^2$, and the envelope is at most
$Ae^{-t/4}\le\epsilon/2$. Keep the source's run-wide lower bound
on $t_k$. Grade losses replace $\epsilon$ by $aL^{-2s}$,
or by the gauge ceiling from (22). Smallness supplies no missing read.

Choose PI/GW's stronger flat and comparison constants first, then
the fixed tile size $M_t$, its scale/gap floors and common rates.
In particular
\[
\begin{gathered}
 r_N=7M_t,\quad\widehat r=(2L+2)M_t,\quad D_X=24L^2M_t,\\
 2r_NL+1\le11M_b,\quad R_1\ge24,\quad
 R_1M_b\ge\max\{\rho'_F,4L(\widehat r+L)+1,3\log L/\delta_q\}.
 \tag{31}
\end{gathered}
\]
The sizes are the prescribed powers/multiples of (L).
Fix $\kappa_1$ and compatible switch geometry, with
\[
 T_{\rm side}\ge\max\{2\widehat r+2,t_FM_F\}\ell_k,
 \qquad M_{\rm dec}\ge\max\{4\widehat r+8L,64\kappa_1/\mu\}.
 \tag{32}
\]
Choose the real, twist and independent-current ceilings and datum
radii afterwards, before the final running-coupling ceiling. GW's
primitive current ceiling can precede $\kappa_1$; the optional
calibrated conversion in §3.7 requires an additional ceiling after it.
Recompute all later constants if the fixed tile size changes.

PI Proposition 3.1 gives S1-loc only on matched thick towers at
anchors with $N(x)\subset\Omega_0$. Boundary-crossing patches
still need their whole real gauge and S2+. The whole torus removes
that boundary issue, not thickness or row identification. UA now
gives $\mathfrak S^{\rm pl}$, Avg and Loc on its stated complete
reads with common constants, by (22)–(32) and the named inputs.
It has not given ID, M or an independent entry proof for T.

### 3.2 From the imported walks to the primitive estimates

Here is the retained proof chain of `walks-gw`, specifying what its
import proves and where the stronger norm is used. The flat inverse,
local Poisson estimates and local averaging port remain its named inputs;
they are not new assertions of this distillation.

For the mixed variables $(A,h_s,\lambda,\mu_s,\nu_s)$, the strong
output sizes are respectively
\[
\begin{array}{c|l}
 A&m|A|, m^2|\nabla A|, m^3|\Delta_{\rm comp}A|\\
 h_s&m^2|h_s|, m^3|\nabla h_s|, m^4|\Delta_{\rm comp}h_s|\\
 \lambda&|\lambda|, m|\nabla\lambda|, m^2|\Delta_{\rm comp}\lambda|\\
 \mu_s&m^4|\mu_s|\\
 \nu_s&|\nu_s|
\end{array}
 \tag{33}
\]
and the five source sizes are $m^3|f|,m^2|g_1|,m^4|g_2|,|g_3|,|g_4|$.
Call the resulting norms Z and V. They are not PI's energy spaces.
Cell-confined V sources have bounded energy-dual norm by their physical
cell volume and row measures. Flat individual transitions summing to
$q_F<1/2$ give local energy decay $Ce^{-ad(y,z)}$. The scale sum is
controlled by the written counting bound
\[
 \sum_{d(y,z)\le t}(m_z/m_y)^b
 \le5L^{8+|b|}(1+t)(3+2t)^4
       e^{(8+|b|)(\log L)t/\rho_g}.
 \tag{34}
\]
A path of cost $t$ crosses at most $1+t/\rho_g$ whole levels;
counting endpoints on each grid proves this bound. Lift torus paths
to overcount. A sufficiently large gap leaves a convergent shell sum
$\sum(n+2)^5e^{-a'n/2}$, also with the finite power shifts needed
by the physical pairings. No polynomial-growth assumption is used.

The flat mixed equations first give $\Delta h_s$ from its bounded
source and row terms, then $\Delta A$ using $\nabla h_s$, then
$\Delta\lambda$ using $\nabla A,h_s$. Jensen's inequality and the
physical row/column bounds control the row terms. The local Poisson
input gives value, gradient, gradient Hölder and Laplacian bounds in
that order. Its kernel proof bounds derivatives of orders $0,1,2,3$
by $C(|x|+\eta)^{-2-q}$; a low/high-frequency split and integration
by parts yield these powers. For a divergence source, subtract its
value at the output in the mixed second derivative, leaving
$\int_\eta^{Cs}t^{\epsilon-1}dt$; move the constant part onto the
cutoff and use the stated Caccioppoli bounds for the harmonic remainder.
At outer or artificial bare boundaries $m=\eta$, pointwise $L^2$
and finite differences give the same powers on zero extensions. Thus
the flat mixed inverse has a uniform V-to-Z bound $B_Z$.

In a supplied local gauge with small
$e=\sup(m|B|+m^2|\partial B|)$, difference expansion gives
\[
 \|(M_r(U)-M_r(1))X\|_V\le C_Ze\|X\|_Z.
 \tag{35}
\]
Covariant differences differ by (c) with
$|c|\le Ce/m, |\partial c|\le Ce/m^2$. Literal row errors have
row bound $Ce$ and physical column bound $Ce(\eta/m)^4$, whose
fine volume cancels under transpose. Replace both factors in a row
mass. In the polarized Wilson Hessian write the curl as $d+L_B$.
The cross terms cost $Ce(m^{-1}|\partial v|+m^{-2}|v|)$.
For $E=(P-I)^2P^{-1}/2$, $P-I=O(\eta^2e/m^2)$; bound its outer
difference by $2/\eta$. Its $d^*Ed$ term is bounded by
$C\eta^3e^2m^{-4}|\partial v|\le Ce^2m^{-1}|\partial v|$,
and its other terms are smaller first-order or mass terms. The
$P-P^{-1}$ commutator is a local mass term. No second derivative
of $B$, or derivative of $J$, is used. The same expansion compares
real-reference and complex-background graph norms, including their
full stencils. These are the coefficient and norm comparisons in GW.

Choose the radii after $M_t$ so $B_ZC_Ze\le1/8$. Local inverses
then have V-to-Z norm at most $3B_Z$. Cutoff product rules, row/column
oscillations across their carriers, and the bare boundary stencils give
$\|[M_r,h_\tau]X\|_V\le C_{\rm com}M_t^{-1}\|X\|_Z$.
For $S_\tau=h_\tau M_\tau^{-1}h_\tau$,
$T_\tau=[M_\tau,h_\tau]M_\tau^{-1}h_\tau$, choose
\[
 \theta_Z=3B_Zc_Z^2C_{\rm com}/M_t\le(4D_*)^{-4},
 \quad D_*=3(20L)^4.
\]
The exact identity $M\sum S_\tau=I+\sum T_\tau$ and overlap
give a convergent parametrix. Each actual word
$S_{\tau_0}(-T_{\tau_1})\cdots(-T_{\tau_n})$ has V-to-Z
norm at most $3B_Zc_Z^2\theta_Z^n$. Its transpose is estimated
by the reversed left-parametrix word; individual words are not
assumed symmetric. The source/output powers are dual under their
physical measures, which proves the column bounds. Full footprints
contain the endpoint differences and all cutoff coefficient reads.

Restrict each word's input to a normalized source cell and take its
output-cell graph norm to define a nonnegative $k_\omega(y,z)$.
For first-order inputs use smooth cell partitions, not differentiated
indicators. The geometry gives $d(y,z)\le D_X(n+1)$ and
$t_\omega\le17D_X(n+1)$. With
$\mu=\log(1/\theta_Z)/(140D_X)$, the split of the word bound gives
\[
 k_\omega(y,z)\le C\theta_Z^{n/2}
             e^{-\mu d(y,z)-2\mu t_\omega}.
 \tag{36}
\]
The walk count is at most $D_*^n$, while
$D_*\theta_Z^{1/4}\le1/4$. Reserve a quarter power for tails.
Endpoint differences pass to the sum in the graph norm, not merely
in an energy norm. The bare G0 endpoint, PI's $q_0$ words and
physical row bounds give absolute graph majorants for $G_0,H_0,B_0$.
The assigned $B_0$ expansion uses its specified constituent words;
the direct mixed-inverse block is not substituted at switches.

A tree of layer length $t$ has axial length at most $\ell_kt$.
Double its edges and subdivide into arcs of length at most
$M_{\rm dec}\ell_k/2$. Each arc meets at most sixteen cubes.
Consequently at most $16+64t/M_{\rm dec}$ cubes are met, including
the complete-footprint representatives. Thus (32) gives, for a
primitive concatenation and its local insertions,
\[
 |\sigma_\omega|\le e^{16\kappa_1}e^{\mu t_\omega}.
 \tag{37}
\]
The insertion length costs are charged before the current ceiling.
One spare exponential pays the tag; another supplies weights and
decay. Fixed composites retain their primitive product tags. The
source proof bounds union tags too, without identifying the two maps.

For the current-dependent first-order branches retain the divergence
allocation. Vector sources $f=f_0+Dg$ with $g\in C^\epsilon$
give first gradients in $C^\beta$, $0<\beta<\epsilon<1$.
Scalar sources $f=f_0+D^*g$, bounded $g$, give $C^\alpha$,
$0<\alpha<1$. The flat Poisson estimate, coefficient comparisons
and cutoff product rule apply in these source spaces; the rightmost
cutoff is included. Reversed scalar words give their differentiated
column estimate without dualizing a Hölder seminorm. Choose constants
for this finite collection of norms before choosing $M_t$.
The actual insertion has
\[
 \Theta'_JA=\mathfrak k_J(\Lambda A)+D\varphi,\qquad
 \varphi=RG'(\mathfrak j_J(A)+m_3)+RG'D^*m_4,
 \quad m_3=O([D\Lambda A,J]),\quad m_4=O([\Lambda A,J]).
 \tag{38}
\]
Move the one difference by the bilinear pairing; $J$ is never
differentiated. The preceding scalar then vector bounds give an
absolute first-order majorant $C_1|J|_{-3}$ for $G_0\Theta'_J$.
Choose $C_1j_*\le1/4$. The compression correction has majorant
$C_2|J|_{-3}$; impose $C_2j_*\le1/4$. Neumann expansions then
give $G_\pi^J,q_J,H^J$ and their physical transposes. These are
expansions at one, subsequently tagged, not inverses at $\sigma$.
The smooth $h_\tau^2I$ terms in $R$ have bounded multiplier
derivatives; no sharply tagged identity is inserted. A transpose
after switching is the transpose of its assigned tagged words.

AV's density, of size $C\ell_c^{-3}$, with coarse transpose
measure $\ell_c^4$ and bounded adjacent-height incidence, gives
weighted local vertex and transpose bounds. GW's local Wilson
calculation uses the cubic term
$\tfrac12\operatorname{tr}(D_UA)\sum_{i<j}i[X_i,X_j]$.
In its first variation use
$\delta[F,G]=[\delta F,G]+[F,\delta G]+\eta[\delta F,\delta G]$.
The transported-edge error has a factor $\eta\nabla_UA$, which
pays a difference bounded by $2/\eta$; curvature cubic errors have
the extra $\eta^2\ell^{-2}(a_0+a_1)$. The exponential series
bounds degree at least four. This supplies the quadratic source
and linear derivative majorants for $V_0'$, not analyticity alone.
Pair the averaging Hessian density with $H^{J,T}J$ to obtain
$\theta^*\le C_3|J|_{-3}$ for $\Theta_J:E\to F$, and impose
$b^*\theta^*\le1/4$.

For completeness, the nonlinear absolute summation is retained.
Let $a(t)=Ct^2/(1-t/s)$ dominate all averaging coefficients with
one density leg, and $H_*$ the switched lift majorant. The positive
series $d(t)=a(t+H_*d(t))$ is obtained by iteration from zero.
Choose $16r<s/2$, $64H_*Cr\le1$, $H_*a'(16r)\le1/4$.
For $0\le t\le8r$, the map preserves $0\le x\le8Ct^2$
and contracts there. Monotone coefficient sums converge; convergence
at $8r$ and $sup_n n^q2^{-n}<\infty$ give two differentiated
series on $0\le t\le4r$. Expansion of the actual inner equation
is dominated term by term, so it is that same small branch. Marking
one input leg gives its weighted density and transpose; two markings
give the second derivative. The remainder $d_3=d-a_2t^2$ starts
in degree three.

With constants for each factor and its transpose in their matched
physical norms, the seven terms of (4) have the positive majorant
\[
\begin{split}
 v_*(t)={}&H_*J_*d_3'(t)+Q_*K_*d(t)+K_*Q_*t d'(t)
                         +K_*d(t)d'(t)\\
 &+(1+H_*d'(t))w(t+H_*d(t))
 +\Lambda_*c_jJ_*H_*d(t)+H_*c_kJ_*\Lambda_*t d'(t),
 \quad w(t)=C_Wt^2/(1-t/s_W).
 \tag{39}
\end{split}
\]
For example $Q^T$ maps block power $-3$ to F,
$\mathsf k:B\to\text{block }-3$,
$\mathsf k^T:\text{block }-1\to\text{block }-4$,
$H^{J,T}:F\to\text{block }-4$, and
$\Lambda^T:\text{scalar }-4\to F$. The local insertions and
averaging-density transpose close all remaining legs. Scale factors
cancel at each matched composition; they do not accumulate with its
length. Every term in (39) starts at degree two. Its derivative marks
exactly one field leg, so $|DV'_\sigma(A)|_{E_p\to F_p}\le
v_*'(2r)\le C_\kappa r$. The radius is chosen inside the convergence
disc, hence this last constant works for every smaller $r$.

In $G=\sum_{n\ge0}B_0(\Theta_JB_0)^n$, give the graph norm
only to the leftmost bare word. The nonnegative sum is bounded by
$b_\Delta^*/(1-b^*\theta^*)$. Applying (37) to each complete
primitive concatenation gives the stronger $G:F_p\to E_p^\Delta$
bound in (6). Composing with $\Theta_J$ and (39) gives the other
two graph lines. Finite products and positive analytic series have
vanishing absolute tails: first truncate their length, then their
finitely many factor sums. This proves the locally uniform convergence
and the weighted endpoint majorants used in (6), (8)–(9) and (W).

Explicitly, if a kernel majorant includes its source measures and
satisfies $sup_y\sum_z k(y,z)e^{\delta d^\wedge(y,z)}\le K$, then
\[
 \operatorname{size}_y(Of)
 \le\sum_zk(y,z)p(z)\|f\|_p\le Kp(y)\|f\|_p.
 \tag{40}
\]
Local factors cost their finite-range weight ratio; products multiply
constants. This proves the estimates for every admitted weight, not
just exponential examples. On the small inner branch,
\[
 D_AX=(I+DC(SA-SHX)SH)^{-1}DC(SA-SHX)S,
 \tag{41}
\]
whose weighted inverse is at most two when $c_wr h_1\le1/2$.
Thus the primitive bounds used next have been supplied by the named
imports and admissions, without assuming their desired N1 consequence.

### 3.3 The two contractions and the uniqueness domain

For $N(A')\le2r$, $|X|\le8cr^2$,
$|SA'-SHX|\le2r+8chr^2\le17r/8<3r$.
Taylor's integral formula gives $|C(v)|\le c|v|^2/2$ and
$\|DC(v)\|\le c|v|$. The inner map's image is at most
$9cr^2/2<r_X$, and its contraction factor at most $3chr\le3/64$.
For $N(A')\le4r$ use the auxiliary ball $|X|\le32cr^2$: its
argument is at most $9r/2$, its image at most $81cr^2/8$, and its
contraction factor at most $9/128$. Uniqueness identifies the two
branches and gives the required surrounding analytic room.

The datum ceiling gives $N(H_0b)\le r/8$ and
$N(-T_\sigma j+\Gamma H_0b)\le r/8$. On $N(z)\le r$,
$N(A')\le9r/8<2r$; the outer image is at most
$r/8+4qr^2\le3r/16<r$. For $N(A)\le2r$, Cauchy on
$A+\zeta u$, $N(u)=1,|\zeta|=2r$, gives
$\|D(GV')(A)\|\le16qr^2/(2r)=8qr\le1/8$.
Apply norm-one linear functionals for the vector-valued estimate and
integrate along segments. Both Picard sequences converge geometrically
in the common balls. Their locally uniform holomorphic limits are
holomorphic by Cauchy's formula. Zero solves the zero-data equation.
The nested uniqueness proves exactly (11), establishing (a).

### 3.4 Four weighted entries and the linearized response

Let $D_*=\|\delta d\|_{\mathrm{dat},p}$ and compare two solutions
at the same kernel. The outer equation is
$A'=-j+H_0b+\Gamma(-j+H_0b)-GV'(A')$.
The connecting segment lies in $N(A')<2r$. By (W),
\[
 \|\delta A'\|_p\le(1+\gamma)(1+h_0)D_*+\nu\|\delta A'\|_p,
 \qquad K_A=2(1+\gamma)(1+h_0).
\]
Thus $\|\delta A'\|_p\le K_AD_*$. Subtracting the inner equations
and integrating $DC$ along their segment yields
\[
 |\delta X|_p\le c_wr(\|\delta A'\|_p+h_1|\delta X|_p)
 \le K_XD_*,\qquad K_X=2c_wrK_A.
 \tag{42}
\]
Apply the graph norm directly to the outer equation, not to $HX$:
\[
 \|\delta A'\|_p^\Delta\le K_\Delta D_*,\quad
 K_\Delta=1+h_\Delta+\gamma_\Delta(1+h_0)+\nu_\Delta K_A.
 \tag{43}
\]
The remaining entries are bounded by
$(K_A+h_1K_X)D_*$, $p_1K_AD_*$ and $m_1K_XD_*$.
Consequently N1 holds with
\[
 B_H=\max\{1,K_\Delta,K_A+h_1K_X,p_1K_A,m_1K_X\}.
 \tag{44}
\]
Only the last two constants use M. Denote the first two response bounds
by **V** when a consumer needs no current identification. Equation (13)
is the triangle inequality and $N\le N^\Delta$, independently of N1.

At zero datum,
$D_jA'=-T_\sigma$, $D_bA'=T_\sigma H_0$, $DX=0$.
Hence
\[
 \|T_\sigma j\|_p^\Delta\le(1+\gamma_\Delta)\|j\|_p^\Delta,
 \quad
 \|T_\sigma H_0b\|_p^\Delta
 \le(h_\Delta+\gamma_\Delta h_0)|b|_p.
 \tag{45}
\]
This gives the repaired U07 map $\mathsf T^{\mathsf L}=T_1H_0$,
without a graph norm on $h$ or $H^J$. At one the separate bare
argument is also retained. If $B_0:F_p\to E_p$ has norm $b_0$,
graph norm $b_\Delta$, and $b_0\theta\le1/2$, then
$G=B_0+B_0\Theta_JG$ gives
$\|Gf\|_p\le2b_0|f|_{-3,p}$ and
$\|Gf\|_p^\Delta\le b_\Delta(1+2b_0\theta)|f|_{-3,p}$.
Thus the unswitched U07 bound is
$[h_\Delta+b_\Delta(1+2b_0\theta)\theta h_0]|b|_p$.
The bare graph estimate follows from $B_0=G_0-H_0\ell QG_0$
and its native source-to-block bound. None of these unswitched
identities is silently continued to switches. The alternative
$\mathsf T^\sharp=H^J$ is a different map.

### 3.5 Structure, parameterization and physical identification

Apply an EQ intertwiner to (S5). It gives the target equations, so
uniqueness proves covariance when the transported solution is admitted.
Conjugation preserves the ball for real inputs. A bounded complex gauge
has a finite common norm conversion $K$, including inverse and overlap
compositions. At datum size $s$, transported $z$ is bounded by
$K(K_A+h_0)s$, and transported $X$ by $KK_Xs$. Choose these
below $r,r_X$ and the pulled-back datum below $\varepsilon$.
The overlap glues even though the entire larger ball need not be invariant.

PH is the account's K6 identification, reused on its admitted diagonal
domain. If both branches lie in its uniqueness ball, they agree; or
compare them in (11). Equality on an open real block-data set extends
by successive one-variable identity theorems. This argument never
leaves the physical current graph. It proves (d), not equality of
independent-current extensions.

Full-footprint restriction commutes with each primitive word and local
vertex. Their connected footprints and absolute sums cannot join
different retained components. LC then lets both Picard sequences
restrict term by term; uniqueness gives (f). On zero-data components
use the zero solution. Outside the retained region the equation can
still read $-j$, which explains the field-support proviso. Exempted
cubes have switch value one, inside the same polydisc; the same tag
bounds apply. E(e) is separately needed to transfer the unnamed side
clause along with the proved ones.

Specialization and holomorphic parameterization follow by composition
and uniqueness, with T ensuring every intermediate image. Cauchy estimates
retain their actual margin. Taking the second datum zero in N1 proves
the corollary, including its exponential profiles when they are admitted.
This completes all specified structural clauses; (e) has exactly the
content supplied by E(e), and no more.

### 3.6 The current rider and the repaired cutoff

For $N_y(h_i)\le1/40$, put $D=N_y(h_1-h_2)$. If $D=0$,
locality gives zero remainder difference. Otherwise the disc
$h_2+z(h_1-h_2)$, $|z|\le1/(40D)$, lies in the $1/20$ ball.
RJ bounds its scaled remainder by $0.11K_J$ and its difference
from the centre by $0.22K_J$. If the disc radius is at least one,
divide the difference by $z$ and use the maximum principle. If it
is smaller, the endpoint bound suffices. In either case the difference
at one is at most $8.8K_JD\le9K_JD$.
In (18) the other terms cost $1+1+18d+1$ times the four-entry
maximum. The $K_W\delta A'$ term uses
$N_y(\delta A')\le N_y^\Delta(\delta A')$, not an unsupported
bound by $N_y(\delta h)$. This proves (20).

For the commutator, let $T_\mu$ be covariant forward translation,
$\nabla_\mu=(T_\mu-I)/\eta$,
$\nabla_\mu^T=(T_\mu^{-1}-I)/\eta$, and use ordinary scalar
differences $f_\alpha=\partial_\alpha\chi$,
$g_\mu=\partial^-_\mu\chi$. Ad-invariance of the bilinear trace
pairing makes the transpose formula valid for complex links. Multiplication
gives exactly
\[
 [\nabla_\mu^T\nabla_\alpha,\chi]B
 =f_\alpha\nabla_\mu^TT_\alpha B
 -(\partial^-_\mu f_\alpha)T_\mu^{-1}T_\alpha B
 -g_\mu T_\mu^{-1}\nabla_\alpha B.
 \tag{46}
\]
Use $\nabla_\mu^TT_\mu=-\nabla_\mu$ and
$\nabla_\mu^TT_\nu=T_\mu^{-1}\nabla_\nu+
\nabla_\mu^T-\nabla_\nu$. Summing the two curl terms over
$\mu\ne\nu$ gives gradient coefficient $2+4\vartheta$ and
value coefficient $1+\vartheta^2\le2+4\vartheta$ per index.
For scalar first/second difference bounds $s_1,s_2$,
\[
 \ell_y^3|[D_1^TD_1,\chi]B|_y
 \le c_d(\ell_ys_1+\ell_y^2s_2)N_y(B).
 \tag{47}
\]
The full stencil is included and no link derivative is introduced.

Use the existing explicit cutoff repair. Let $v_0$ on $[0,1]$
rise linearly with slope $9/2$ to $3/2$ on the first third,
remain $3/2$ on the middle third and fall with slope $-9/2$
on the last third; extend by zero. Its integral is one. Put
\[
 e_0=1/200,\quad c_0=99/100,\quad
 v_e(u)=c_0^{-1}v_0((u-e_0)/c_0),\quad
 k_e(u)=(e_0-|u|)_+/e_0^2,\quad v=v_e*k_e,
\]
\[
 q(u)=1-\int_{-\infty}^u v(s)\,ds,\qquad
                           \zeta(x)=q(3|x|-1).
 \tag{48}
\]
Both convolution factors have integral one. The second distributional
derivative of the trapezoid is a finite sum of point masses; after
convolution it is a sum of continuous triangles. Thus $v\in C^2$,
supported on $[0,1]$, with $\|v\|_\infty\le50/33$ and
$\|v'\|_\infty\le45000/9801$. The resulting cutoff is one on
$[-1/3,1/3]$, zero outside $(-2/3,2/3)$, constant near zero,
and has $|\zeta'|\le50/11<5$, $|\zeta''|<42$.
Tensor-product mixed second derivatives are less than 25. Finite
differences obey the same bounds by integration.

For the scaled bump, $s_1\le5|\tau|/(M\ell_\square)$,
$s_2\le42|\tau|/(M\ell_\square)^2$. On a meeting stencil,
\[
 \ell_ys_1+\ell_y^2s_2
 \le|\tau|\{5/(2L)+42/(4L^2)\}\le2|\tau|.
\]
Elsewhere the commutator vanishes. Equation (47) gives the **unchanged**
$c_\zeta=2c_d$. Bound the other four terms of (19) by the same
RJ argument applied to $\chi A',\chi h,\chi X$ in the displayed
positions. This proves (21). It proves U14's rider implication and
its formerly marked commutator step, with the cutoff correction.
U15 needs only (13) and its own size hypothesis (e2).

The actual current identification remains distinct from these estimates.
At $j=0,\sigma=1$, write $\Xi=\Theta_JA'-V'(A')$,
$P_0=I-G_0Q^Tq_0Q$, $\Delta_a=G_0^{-1}$. The account gives
$QA'=\ell^{-1}b$ and
$\Delta_aA'=P_0^T\Xi+Q^Tq_0\ell^{-1}b$.
Substituting these into its chart current yields (18), with
\[
                  m_c=Q^T\mathsf k+\Lambda^T\mathfrak j_JH-\Delta'H.
 \tag{M1}
\]
Here $\Delta'=\mathcal D(W)-D_1^TD_1$ is a first-order local
curvature correction. With the same expression at switches, substitution
of $h=A'-HX$, without an inverse identity, gives only
\[
 J_{\rm def}=P_0^T\Xi+Q^T(q_0-a)\ell^{-1}b
                      -\Delta'A'-m_cX+F(W,h).
 \tag{M2}
\]
If $L_\sigma=\Delta_W+K_W-P_1(\sigma)$, its difference from
the rider is exactly
\[
 \mathcal D_\sigma=P_0^T\Xi+Q^T(q_0-a)\ell^{-1}b
                              -(\Delta'+L_\sigma)A'.
 \tag{M3}
\]
The candidate has the weighted bound
$|m_cb|_{-3,p}\le(c_Qc_k+c_\Lambda c_jh+c_{\Delta'}h)|b|_p$
by (40) and the matched first-order legs. Absolute tails and holomorphy
follow by the same majorants. This proves a bound for the candidate,
not the identity or locality required of the actual $m_H$.

### 3.7 Field data and the limitation of a calibrated conversion

At one, $T_1=(I-B_0\Theta_J)^{-1}$. Multiplication of (S5)
by $I-B_0\Theta_J$ gives
\[
                    z=-j+B_0\{\Theta_JA'-V'(A')\}.
 \tag{49}
\]
Thus the force $-B_0f$ is exactly the datum $j=B_0f$, with
this sign. A physical constraint using $QB_0=0$ does not extend
to an arbitrary field datum.

For the specified primitive bare $B_\sigma$, set the independent
current to zero in GW's stronger G estimate. All current vertices
disappear and the nonnegative majorant becomes a subseries. This proves
FD, holomorphy and component support on its admitted class. If instead
the use defines the composite
$B_\sigma^{\rm comp}=G_0(\sigma)-H_0(\sigma)\ell QG_0(\sigma)$,
its graph constant is $g_0^\Delta+h_0^\Delta c_{\ell QG_0}$.
These operators agree at one; their switched word assignments have
not thereby been identified. Full-footprint confinement proves that
a component where the source is zero contributes zero for either
specified construction. Actual completion sources
$G''(\sigma)J_c+[G''(\sigma)-G''(1)]Q''{}^*\mu$ get a graph
bound by the triangle inequality only after their operator and F-space
matches. A boundary-distance gain additionally needs its marked-footprint
bound. Value decay alone supplies neither assertion.

At arbitrary switches the prescribed substitution is precisely
\[
 z=-T_\sigma B_\sigma f+G_\sigma\Theta_\sigma H_0(\sigma)b
                                      -G_\sigma V'_\sigma(A').
 \tag{50}
\]
FM must match this equation to the consumer's equation. For the
alternative force $-G_\sigma f$, GW does allow a **different** datum
under an additional ceiling $\|\Gamma\|_{E_p^\Delta\to E_p^\Delta}
\le C_\kappa|J|_{-3}\le1/2$:
\[
 T_\sigma^{-1}=\sum_{n\ge0}(-\Gamma)^n,\quad
 j_{\rm eff}=T_\sigma^{-1}G_\sigma f,\quad
 \|j_{\rm eff}\|_p^\Delta\le2g_\Delta|f|_{-3,p}.
 \tag{51}
\]
The geometric series converges in norm; multiplication leaves a vanishing
remainder on either side. Uniform convergence on smaller parameter
polydiscs proves holomorphy. Every term, including the identity, preserves
retained components. Require $2g_\Delta|f|_{-3,p}+|b|_p<\varepsilon$
and the unweighted datum ceiling. Then $-T_\sigma j_{\rm eff}=-G_\sigma f$
exactly. At one $j_{\rm eff}=B_0f$. At switches this does not prove
$j_{\rm eff}=B_\sigma f$, so it does not replace U02's or U26's
prescribed datum. The proof is retained without changing their conventions.

### 3.8 The already available profile comparison and its missing bridge

The imported §5.8 theorem concerns the constrained critical point $X$ of
\[
 \Sigma_0(X)=W_U(X)+\tfrac12\langle L_gX,L_gX\rangle
                         -\langle C_U(X),m\rangle,
 \quad L_g=RD^*,\quad Q_U(\eta X)=B,
 \tag{52}
\]
with its native bilinear pairings and $m=H_U^\dagger J$ in the
presented-pair case. Under its exact pairing, real-reference, collar,
six-residual, weighted calculus and local comparison hypotheses,
\[
 |Y[X';U']-X|_x\le C_B^\sharp(Ap(x)M(x)+p_\delta(x)),
 \tag{53}
\]
where $p\in\mathfrak M_\rho$, $M\in\mathfrak M_\tau^A$,
$p_\delta\in\mathfrak M_{\rho+\tau}$, $\rho+\tau\le5\delta_1$,
$M\le1$, $p_\delta\le4p$, and the full absolute radius,
collar-datum and mismatch inequalities hold. Its graph norm also has
a gradient Hölder member; N1 cannot substitute for it. Complex final
data at the theorem's real references are already allowed.

For U33 take $\rho=5\delta_1/2$, $\tau=\delta_1$.
The sum $7\delta_1/2<5\delta_1$ is admissible. A profile whose
weight inequality has factor (L) uses $A=L$, not the narrower
unit-factor class. If a datum discrepancy is bounded by $cpM$, take
$p_\delta=c(pM)^{[\rho+\tau]}$; the existing hull properties give
$cpM\le p_\delta\le cApM$. Retain $cAM\le4$ and the absolute
radius ceiling. For zero data use zero-data uniqueness or the stated
positive-majorant limit. The rate calculation is
\[
 \sum_y e^{-4\delta_1d(x,y)}|a|_yp(y)
 \le p(x)\sum_y e^{-3\delta_1d(x,y)/2}|a|_y,
\]
\[
 \sum_xe^{-3\delta_1[d(x_0,x)+d(x,y)]/2}
 \le c_1^b e^{-\delta_1d(x_0,y)}.
 \tag{54}
\]
Triangle inequality and summability at $\delta_1/2$ prove the second
line. This preserves the budget $4=5/2+1+1/2$ in units of
$\delta_1$. With RC, (53), the existing three-member consequence
and (54) supply the requested linear profile. The six residual
estimates themselves are imported from their written account proof.

The necessary identification is substantive. II 58620–58685 distinguishes
the other off-shell functional
\[
 \Sigma_{\rm off}(X)=W_U(X)-\langle C_U(X),m_P\rangle
 +\tfrac12\langle L_gX+K_PC_U(X),L_gX+K_PC_U(X)\rangle.
 \tag{55}
\]
Holding the base fixed and temporarily matching $m$, the difference
from (52) is
$\langle L_gX,K_PC(X)\rangle+\tfrac12\langle K_PC(X),K_PC(X)\rangle$.
On a tangent $u$ to the nonlinear constraint its derivative is
\[
 r_P(X)[u]=\langle L_gu,K_PC(X)\rangle
       +\langle L_gX+K_PC(X),K_PDC(X)u\rangle.
 \tag{56}
\]
Thus using the same critical point requires this residual to vanish,
or a new bound for its difference in the comparison. Also match
$H_U^\dagger J$ with the actual current-dependent slot vector.
The account identifies a zeroth-order operator on a supremum-only
mismatch as the obstruction; weight tempering does not change its order.
Its proposed Hölder-mismatch preservation under a step is outstanding.

The exact same-space contraction comparison, when its transport and
common norm are supplied, makes the separate issue visible. Write
$A_i=F_i-G_iV_i(A_i)$, $F_i=T_i(-j_i+H_{0,i}b_i)$. Then
\[
\begin{split}
 \delta A&=R_A-G_1[V_1(A_1)-V_1(A_2)],\\
 R_A&=F_1-F_2-(G_1-G_2)V_2(A_2)-G_1[V_1(A_2)-V_2(A_2)].
\end{split}
 \tag{57}
\]
A contraction factor $\nu<1$ gives
$\|\delta A\|_p\le(1-\nu)^{-1}\|R_A\|_p$. The inner residual
is $R_X=C_1(S_1(A_2-H_1X_2))-C_2(S_2(A_2-H_2X_2))$, giving
$|\delta X|_p\le2(|R_X|_p+c_wr\|\delta A\|_p)$.
The response difference also contains $(H_1-H_2)X_2$; graph comparison
requires comparing the two covariant Laplacians. These are kernel/base
residuals, not data differences at a fixed kernel. A nonlinear cross-grid
map requires its own transported residual identity.

At $\sigma=1$ and for (52), the existing theorem covers the paired
real-reference family with its native hypotheses. The complex-ancestor
corollary II 58369–58489 assumes a fourfold admitted polydisc and
real-trace growth control and yields only a square-root mismatch bound.
II 58490–58619 leaves the comparison of confined-switch constraint and
stationarity defects unproved. Neither result supplies the linear
full-domain bound for the general (55)/(S5) family. Those are precisely
the additional RC premises; no new comparison is claimed here. This
finishes the proof of the stated implication. ∎

## 4. Outstanding premises and source disagreements

Each paragraph distinguishes a proved implication from its missing
application to the account. All quantifiers are over the actual full
domains, not a finite census of sampled instances.

**Outstanding — PI.** The repaired bare inverse is available on its
stated local class. Every use still must identify its literal rows,
corner convention, spaces, whole-action Hessian, boundary coefficients
and metric with that class, and supply S1-loc, S2/S2+, floors and room.
The account sometimes uses an inner-plaquette action; no boundary equality
with PI is automatic. Its symmetric outline rows are not the older literal
rows merely by name. This match is needed by the inverse and walk inputs
in §3.2 at every construction call. Same-grid setting compatibility also
does not supply an unproved termwise lattice-covariance assertion under EQ.

**Outstanding — GW.** The written graph-walk deduction is imported on
the common strong-norm PI class; this distillation is not its independent
check. Supply the exact word assignment, all endpoint and cutoff reads,
rate comparisons and common constant choice on each actual localized or
completion domain. These are needed for the A′ graph member of N1,
U07 and FD. PI's energy theorem alone supplies none of those additional
pointwise/Hölder endpoint assertions. No estimate here is uniform in an
arbitrarily changed tile size or at an older preassigned analytic radius.

**Outstanding — AV.** The local analytic B98-P5 port, including its
fine derivative densities, Hessian contractions, physical transposes and
larger ball, remains a named input. The carrier checks did not check that
port. Every actual carrier and tube must lie in its repaired domain and
meet separately retained published thresholds. This input is needed by
the inner equation, every averaging leg of (4), and the nonlinear
majorants in §3.2. A value bound on the average cannot replace it.

**Outstanding — R.** Identify the real reference and its full S1–S3
and complete-read plaquette witnesses at each entry, including raw and
exterior strata. The class named at I 10178 is not identified with a full
CMP 109 or CMP 102 class by its wording. R is needed for (PL), then the
carrier/frame deduction at U01–U13, U16–U17, U22/U24/U26/U31 and any
other newly entered domain. Clause (12) replaces only R's plaquette
part when actually imposed on that same reference and read family; it
does not prove the remaining class clauses or new-reference entry.

**Outstanding — A0.** Supply complete double blocks for every row and
transpose, the actual branch, gap/lift room and finer collars. For
minimizer references supply the published continuation and gauge inputs
on their actual larger domains. Equations (26)–(27) prove local averaging
room after a frame is supplied; they do not admit the original minimizer
tube. Equations (28)–(29), the doubled-disc margin and the actual datum-map
bound are needed for those uses, especially U11, U31–U33, and localized
or completion carriers. Shrinking a replacement tube does not verify the
consumer's original tube.

**Outstanding — L0.** Supply an ordinary real potential and its first
derivative on each whole PI patch, including patches crossing the outer
boundary, and S2+ on every exterior coefficient. PL, an axial carrier
potential, separation alone and localized (c1)–(c3) do not provide these
patches. This is needed by the actual local inverse at U05–U09, U22/U24,
completion U26 and every earlier-frame/interface call in U34, as well
as inherited calls elsewhere. Interior thickness invokes Proposition
3.1 only after its grids and floors are matched.

**Outstanding — S.** Stage clauses Q5/Q8 must cover all complete reads
with their grade conversions, including the continuation beyond $Y^+$.
I 110268–110317 defines relaxed $K_{109}$ and $K_P$; it does not
include full CMP 109 (i)–(iii). I 119615–119650 requires a global pair
with direct bounds on $Y^+$, whose unlocalized continuation reads beyond
it. These missing ambient reads affect U19–U30 and U34. If cube heredity
is used, its exceptional case $C=2,j+1=k,m=k_0+1,N_0\ge2$,
I 134496–134532, retains the separately owned `O-stage-cubes` supplier.
Clause (12) preserves the real plaquette part without solving that gauge
cover or the new-entry problem.

**Outstanding — T.** Supply independent existence, admission and a
uniform analytic margin for all reached intermediates on each prescribed
product domain. The small-solution conclusion cannot be its own entry
proof; finite-dimensional openness gives no uniform infimum over depths
and histories. This is needed by U02/U03's four-link chain, the U05–U09
bidiscs, healing/completion U17/U26, the U27/U28 product and U30–U33
compositions. The separately registered CW, CH and L17/ER7 suppliers
retain their premises. A previously proved theorem with its larger-domain
hypothesis is not an unconditional supplier of that hypothesis.

**Outstanding — P2.** Admit both cutoff references, exactly paired
sets, the free finer $\Lambda'_0$ collar and the entire complex-parent
and interpolation domains. Real frames and equality at a real centre do
not admit those domains. P2 is needed for U32's continued paired identity
and U33's comparison, in addition to their local operator and averaging
certificates. It includes no identification of different fine plaquettes
or references by the same-reference hereditary argument (12).

**Outstanding — ID/EQ/PH/LC.** Match the actual maps to (S5), with
their seven terms, coordinates, gauges and tags. Supply EQ's actual
intertwiners; PI's fixed-grid locality is not all lattice covariance.
PH is available only on K6's admitted unswitched own-current chart with
its uniqueness and datum-domain hypotheses, needed at U01, U07, U11/U12,
U21/U22 and U32 where physical identification is read. LC requires every
full stencil and both actual data to be confined or zero; it is needed
at U01/U02/U04, U23/U25 and U34. A bounded independent-current extension
alone does not prove zero first-slot forcing. These are structural
application premises, not new consequences of operator norm bounds.

**Outstanding — M, specifically (M3).** Supply the literal reduced
current-word assignment, its diagonal localization, the P1/mH bounds
(7), and equality with the current of each link. The candidate (M1) has
a bound but leaves defect (M3). On a flat admitted torus, $J=0$, with
all switches zero in a nonempty full family, all primitive sums vanish;
at $j=0$, (S5) gives $A'=X=h=0$. Yet the formula (M2) gives
$J_{\rm def}=-Q^Ta\ell^{-1}b$, while the rider gives zero. Choose
a nonzero averaging row and sufficiently small (b) so the former is
nonzero. Also (M1) gives $m_c=-Q^Ta\ell^{-1}\ne0$, whereas
I 72720–72728 requires a zero kernel for the empty retained region.
These are the source's symbolic tests of the two proposed extensions,
not a refutation of the unnamed layer theorem. M is needed by the last
two N1 entries and every actual rider use; the untagged candidate cannot
serve as its supplier. Relocalizing the mass changes a definition and
needs a matching proof.

**Outstanding — RJ.** Supply the analytic local coefficient bounds,
transport ceiling, complete commutator stencils, collar geometry and
smallness used in (20)–(21) on the actual complex domain. The rider
proof establishes the inequalities for a furnished triple under these
inputs; it neither supplies that triple nor its current identification.
U14 is precisely this implication. U18 additionally needs its separate
product-profile estimate for the nonlocal $P_1(\widehat\chi A')$
tail. U27 reads the uncut rider multiplied by $\chi$; replacing it
by the cut rider would change that consumer.

**Outstanding — FD.** GW proves the field-datum graph bound for its
specified primitive bare operator and, separately, the displayed composite.
Match each actual $\widetilde G_0$ or $G''$, all its tags and boundary
conditions, and every source to one of these exact constructions on its
whole domain. This is needed at U01–U04, healing U17, completion U26,
and inherited source-bearing calls. In particular identify $Q''{}^*\mu$
in F and any marked boundary-distance estimate for the completion
difference. I 142537 assumes its graph estimate; a similar operator name
or pointwise decay does not prove the match.

**Outstanding — FM.** Establish the literal force identity (50) for
the consumer's prescribed field datum, including the branch and support.
If its force is $-G_\sigma f$, prove
$(T_\sigma B_\sigma^{\rm use}-G_\sigma)f=0$; if it uses the
bare switched equation, match that equation's own resolvent instead.
Unswitched (49) is proved. Primitive union tags and products of tags
prevent automatic continuation of that identity. The calibrated datum
(51) supplies a different forced equation and cannot rename the data
in U02 or U26. FM is needed at the source-bearing uses listed under FD,
and for support conclusions inherited by U23/U25/U34.

**Outstanding — E(e).** Recover the original clause and verify it on
the relevant domains, or explicitly weaken U01/U08 to their named
concrete consequences. No formula for the missing predicate was found
by the generation census. Composition and uniqueness prove specialization,
but the earlier gate's acceptance of that proposed reading does not
identify it with the original. U01's whole-package transfer and U08's
side-clause assertion still consume E(e). The displayed concrete
calculations use only the other named clauses; that does not prove an
unspecified predicate. The conditional table retains E(e) at these two
blanket assertions rather than claiming its recovery.

**Outstanding — RC.** Supply U33's actual response/slot identity with
(52), or control the additional residual (56) for (55), including the
Hölder mismatch and its preservation. Supply the native six-residual,
projection, extension, multiplier and radius hypotheses, exact pairing,
both collars, and linear comparison on any complex-ancestor and
nontrivial-switch domains actually claimed. The existing §5.8 theorem
already proves the conditional profile estimate at real references with
complex final data. Its later square-root and confined-switch statements
do not provide the required full-disc linear gain. No re-proof of that
existing theorem is needed; the missing bridge is its use for these
actual functions. The global stage-response identification remains with
its registered owner `shift-map`.

**Source disagreements retained at the weaker claim.** `layer-pkg` leaves
GW open; `walks-gw` supplies it only on its chosen admitted class, which
is the scope used here. `layer-r3` proves FD for specified GW operators
but not their identification at every completion. Its M3 defect prevents
using the older unswitched current algebra at arbitrary switches.
`b98p5-r3` claims a decided census and whole-tube coverage; its gate
withdraws those claims and repairs the half-open geometry, norm factors,
published thresholds and Cauchy margin. `adm-pl` supplies the post-step
crossing implication but retains its raw/domain/reference gaps. In
particular I 10681/10701 belong to the proof of the post-step conclusion,
not the separate one-power alternative. Earlier PL109 assignments to
U19/U27 or relaxed $K_P$ cannot survive `adm-pl`'s definitions check;
the final table uses S, R where needed, A0, L0 and T instead. Full CMP
109 membership, where explicitly supplied on the complete reference,
still gives the stated conditional PL implication.

The failed routes are retained only as reasons not to reuse them:

* **B4 / graph $h$:** the checked independent-current counterexample
  refutes the extra mesh-free Laplacian member under a common analytic
  datum radius; the four entries of N1 survive.
* **First-order holomorphy to graph bounds:** Cauchy cannot create a
  norm absent from its bounding circle; GW needs strong endpoint words.
* **Switched inverse identities:** a shared cube is tagged once in a
  primitive and repeatedly in a product; equality at one is insufficient.
* **Current reduction after switching:** (M3) remains, with the explicit
  zero-switch failure above; reduction before switching still needs the
  actual localized diagonal assignment.
* **Cube tests or separation alone:** the known island/thin-finger and
  crossing-bond examples leave carriers or boundary coefficients uncontrolled.
* **Compressed parent inverse:** eliminating the exterior produces
  $A_{12}A_{22}^{-1}A_{21}$, so restriction is not a new Dirichlet inverse.
* **Class-name or core-only admission:** relaxed $K_{109}/K_P$, or
  Q5 only on $Y^+$, does not control every ambient read.
* **Shrinking $a_A$ alone:** it does not improve the fixed ratio of the
  consumer tube to the actual $C_1^{(172)}\epsilon_1$ radius.
* **Physical-diagonal continuation:** a factor $J-\mathcal J(W)$
  vanishes there without vanishing at independent currents.
* **Replacing clause (e):** specialization is redundant and cannot
  identify an unspecified original assertion.
* **Same-kernel N1 for U33:** it has no bound for the residuals (56)–(57)
  or for changing the base's Laplacian.
* **Fractional-power or vertex interpolation for RC:** $x^\alpha/x$
  diverges as $x\downarrow0$ for $0<\alpha<1$; vertex control does
  not prove the missing full-disc linear comparison.
* **Printed cutoff with both derivative bounds 5:** a flat-ended
  transition of width $1/3$ can drop at most $5/36<1$ under that
  second-derivative ceiling; (48) repairs it with the same final $c_\zeta$.

## 5. Result

This is a distillation of a **conditional layer theorem**, not a proof
that the actual induction is admitted. It retains the two contractions,
the four weighted entries, the GW endpoint argument and its exact scope,
the supplied admission implications, source conversions, U07's direct
linearization, covariance/locality, the repaired current rider, and the
existing conditional U33 supplier. Clause (e) remains an explicit
unresolved import. M3, actual source conventions, full admission and the
additional RC comparisons remain Outstanding at their precise uses.

The part makes no new mathematical claim beyond those source implications.
It does not reopen the separately owned PI, B98-P5, stage-response,
exceptional cube, or uniform-domain tasks. There was no prior
`library/prior/layer-distil.md` at the pinned checkout. The referenced
workflow file is absent there. Only `library/layer-thm-part.md` is written;
no editable prompt, account text, registry, audit or platform instruction
is changed. Source identities and the Outstanding paragraphs above form
the recovery record. Balaban's unavailable originals and a new independent
referee reading of this part remain outside this distillation.

The final table concerns the **layer content actually consumed**, with
the weaker corrected norms. “Covered” is an implication from the named
furnished inputs. “Covered conditionally” names the additional premises
needed on the actual domain; it never asserts those premises have been
verified. For E(e), it is explicitly a formal conditional coverage of an
unrecovered assertion. No row certifies every other part of its surrounding
consumer theorem.

To keep the dependencies readable, use:

* **D[U]** = PI, GW, AV, ID and UA's **R,A0,L0,T**, on the exact
  domain in that row. S/P2 are additional where shown. An inherited D
  retains the originating domain obligations; it is not a new admission.
* **V[U]** = the first two bounds in (42)–(44) from D[U], with every
  used weight admitted. **N[U]** = N1 from D[U] and **M[U]**, including
  (7). These are proved consequences, not assumptions of N1 itself.
* **RJ[U]**, **EQ**, **PH**, **LC**, **FM/FD**, **E(e)** and **RC**
  have exactly their named meanings above. **TL** is (45) and its
  unswitched U07 refinement. For a furnished triple, its originating
  D/FM obligations remain with that originating call.
* Where D uses a direct supplied frame, A0/AV may use that route;
  where (12) is imposed, it replaces only R's plaquette component.
  S and P2 never waive L0, T or a new-reference entry.

| Use and source | Actual domain / datum | Final coverage and named inputs |
|---|---|---|
| U01 — I 72373–72538 | Exempted-switch family; general datum and $j=\widetilde G_0(\sigma)f$ corollary. | **Covered conditionally:** D[U01], N[U01], RJ, EQ/PH/LC and FM/FD on complete footprints give the concrete clauses, corollary and rider. The blanket (a)–(f) transfer additionally requires **E(e)**; its content is not recovered. |
| U02 — I 73103–73140 | Four reached links; stage 3 prescribes $\widetilde G_0(\sigma)J_3$. | **Covered conditionally:** D and N at each of the four images, RJ, LC, FM/FD, and the induction's actual membership and datum-size hypotheses. Any use of full CMP 109 requires that explicit representative and its inclusion ceilings, not its class name. |
| U03 — I 73546–73633 | Four global determining sets $\mathbf B''_k,\mathbf B''_k,\mathbf B_1,\mathbf B_k$, with independent switches. | **Covered conditionally:** D on the full product domain, T for every intermediate image, and inherited FM/FD where source-bearing. The local scaffold is not a determining set. Existence/parameterization adds no M premise. |
| U04 — I 89955–90008 | Source-presentation input (i4), with furnished layers. | **Covered conditionally:** originating D, N, RJ, LC, FM/FD and its explicitly supplied presentation hypotheses. The presentation does not prove its own operator or domain match. |
| U05 — I 94180–94286 | Real and perturbed bases on $\mathbf B_k(C),\mathbf B''_k(C)$, core and bidisc. | **Covered conditionally:** D at both bases/sets and N where the four-entry constant is used; the stated real-base, shifted-base and core admission. Radius choice follows these common inputs. $\mathsf p(U_0)\le1$ is not PL's small ceiling. |
| U06 — I 94303–94422 | Two block-only calls $(0,d^0),(0,f)$, including crossing/core logarithms. | **Covered conditionally:** D inherited from U05 with full-bidisc data and base inclusion. Zero at zero follows by (a); PH and FM are unnecessary for that assertion. |
| U07 — I 94448–94586 | Linearization on the explicitly relaxed local class. | **Covered conditionally for $\mathsf T^{\mathsf L}$:** D and TL; PH for physical identification. L0 and R/A0 are still needed on that relaxed class. $\mathsf T^\sharp=H^J$ is a different map and receives no graph bound here. |
| U08 — I 94608–94843 | Localized small-solution scope under (c1)–(c3). | **Covered conditionally:** D, N, RJ, EQ/PH and parameterization give the concrete conclusions. Whole side-clause scope additionally needs **E(e)**. Geometry (c1)–(c3) does not supply boundary gauges, collar frames or T. |
| U09 — I 94846–95085 | Whole bidisc for the two local constructions. | **Covered conditionally in repaired norms:** D inherited from U05–U08, N, RJ and independent T on that bidisc. Use graph A′ and first-order h. The source's membership argument using the layer theorem is not its entry proof. |
| U10 — I 95682–95700 | Real zero-datum base of the furnished block chart. | **Covered conditionally:** inherited D from U06 and EQ on its conjugation-stable domain; conjugate the unique solution and differentiate. No new current identification is needed for reality. |
| U11 — I 95750–95790 | Shifted real critical base, own current, block-data derivative. | **Covered conditionally:** D, PH, EQ and TL where its bound is read, with the matched physical free-current identity. The actual shifted minimizer tube and boundary problem remain in A0/L0/T. |
| U12 — I 95872–95908 | Physical/holomorphic overlap of the local chart. | **Covered conditionally:** inherited D, EQ, admitted overlap and PH for its physical reading. The alternative $\mathsf T^\sharp$ form retains its separate (3.36) condition; it is not identified with TL. |
| U13 — I 99780–99796, 99878–99892 | Common constants for the two localized systems. | **Covered conditionally:** common D, N and RJ from U05/U08, before later ceilings. Listing four floors alone gives neither the exterior model nor a uniform domain. |
| U14 — I 111489–111732 | Partner of a furnished cut triple/current. | **Covered:** furnished representation **M**, **RJ**, the stated collar/transport and $N_y(\chi h)\le1/40$, and repaired cutoff (48) imply (21). No fresh inverse or average is used. The originating layer retains its D. |
| U15 — I 112180–112230 | Seminorm combination of furnished entries. | **Covered:** $h=A'-HX$, norm definitions and the consumer's own **(e2)** give (13) and its size bound. N1, PI, AV and B4 are not needed for this calculation. |
| U16 — I 112580–112650 | Two weighted Lipschitz calls at fixed kernels. | **Covered conditionally:** D and N at both specified admitted exponential weights and the datum norm (2). Source-bearing origins retain FM/FD. The idle X norm and graph h are not consumed. |
| U17 — I 114790–114880 | Healing continuation on all of $\mathbf B''_k$, source-bearing links 3/4. | **Covered conditionally:** D, N at weight one, RJ, FM/FD and the separate amplitude/composition/core hypotheses. Agreement with a real base on the core does not admit the other carriers or completion tube. |
| U18 — I 115382–115410 | Inherited (T)/(L) bounds and cut P1 tail. | **Covered conditionally:** originating D/N from U16/U17, RJ, admitted weights, inherited FM/FD where applicable, and the separate **product-profile bound for $P_1(\widehat\chi A')$**. N1 alone does not supply that tail. |
| U19 — I 116555–116669 | Stage frame, relaxed $K_P$, block datum $(0,b)$, full switch disc. | **Covered conditionally:** D, **S**, N, RJ, the actual stage/chart identification and all datum/collar/switch ceilings. Complete Q5/Q8 reads and ambient admission beyond $Y^+$ are required; no automatic PL109 claim survives. |
| U20 — I 125775–125792 | Constant $66B_HK_{\rm cv}$ inherited from stage bounds. | **Covered conditionally:** U19's admitted **V** constant, or its stronger N constant, and the separately supplied $K_{\rm cv}$. Multiplication of constants adds no new M requirement when only response size is read. |
| U21 — I 131621–131695 | Frozen frame, heredity image, raw/starred points, block datum. | **Covered conditionally in repaired norms:** D, **S**, N, RJ, PH only in the physical subcase, and the actual heredity-image admission. Normalize this source's $C_H^\sharp$ to $\max(C_H^\sharp,1)$, as proposed there, or supply its explicit datum ceiling. This is distinct from the forbidden normalization of $C_1^{(172)}$. |
| U22 — I 131725–131746 | Distinct localized $\mathbf B_Z$ and its ambient continuation. | **Covered conditionally:** originating U21 conditions plus D on this new set, N for the entries read, PH and the expressly assumed **same-constant localized certificate**. U08's different geometry does not supply it. |
| U23 — I 136750–136770 | Off-domain continuation and component splitting. | **Covered conditionally:** D, **S**, LC and FM/FD if source-bearing, with both actual data zero on every asserted off-Y footprint. The G1 conclusion omits raw clauses; current extension alone supplies no field-support proof. |
| U24 — I 137562–137603 | Interrupted response on $\mathbf B_Z$, outside earlier space geometry. | **Covered conditionally:** U22's originating premises, D and N at the admitted exponential profile, and the source's **local input 10 with shift ceiling**. Its exceptional localized-domain assumption is retained. |
| U25 — I 137978–138001 | Gluing an arrested continuation. | **Covered conditionally:** D, **S**, LC, admitted branch overlap and FM/FD where source-bearing, with complete interface reads and the source's continuation input. Clause (12) preserves only its fixed-reference plaquette part; cube heredity retains its supplier if used. |
| U26 — I 138640–138667; 142530–142543 | Actual completion G″ sources, raw points and separate core. | **Covered conditionally:** D, **S**, new-reference **R**, N, RJ, FM/FD for the exact completion operators, F-space admission of $Q''{}^*\mu$, and separate threshold/frame conversions. I 142537's assumed graph estimate is not an operator identification. |
| U27 — II 13888–14105 | All-block dilation on the full product domain, $j=0$, current slot $\chi J^\sharp[1]$. | **Covered conditionally:** U19's D/**S**, N, uncut RJ, the **stage-family/space identification**, and all named bump, room, entry, absorption and weighted-space hypotheses. Compare $\delta_0/8$ with the actual common GW rate. Fixed-reference PL invariance does not admit its own layer. |
| U28 — II 15390–15404 | Reuse of U27 data and product-domain containment. | **Covered conditionally:** precisely U27's admitted D/**S**, T for every contained map, N where reused, and the separate **A-slot assumptions**. No enlarged operator domain follows merely from reuse. |
| U29 — II 20790–20808 | Furnished bracket current formula. | **Covered conditionally:** furnished **M**, **RJ** when bounded, formula (19) and the bracket's domain/locality hypotheses. The originating U27 call retains D and any inherited FM/FD. Only the P1 term is nonlocal in the cut multiplier. |
| U30 — II 23160–23177, 23990–24005 | Parameterized brackets and carrier compositions. | **Covered conditionally:** D, **S**, T at every intermediate/carrier, M, RJ and N when estimates are read, plus inherited FM/FD where source-bearing. Core bounds must cover each complete read. |
| U31 — II 51814–52070 | Nonlinear block datum $Q_B(W;\eta(t+\bar t\zeta)H^w)$ on both frames. | **Covered conditionally:** D and V, the complete **averaging-domain/size bound** keeping this datum in the ball on the full disc, and the separate cross-construction **B1/B2** comparisons. This value use needs no rider mH. |
| U32 — II 52107–52186 | Exactly paired critical parents, $\sigma=1$, complex ancestor and block-data discs. | **Covered conditionally:** D, **P2**, PH, exact pairing and the stated **refinement/relative-real-slice** inputs. The identity continues inside this paired admitted family, not to independent-current extensions. |
| U33 — II 52390–52518 | General rippled parents, two cutoffs and full interpolation domains. | **Covered conditionally:** D on both sides, **P2**, and **RC** with all native hypotheses of (52)–(54), the actual slot/response identification or residual (56) control, and any required linear complex-ancestor/switched extension. The account already supplies the real-reference conditional profile theorem; N1 alone does not give this row. |
| U34 — III 49210–49288, 49454–49502 | Relaxed earlier-frame class, direct clauses on $Y^+$, cutoff current and interface stencils. | **Covered conditionally:** D, **S**, ambient/new-entry **R** or its imposed (12) plaquette replacement, LC and FM/FD for source-bearing origins, at every earlier frame and full boundary read. The literal printed relaxed class does not establish these premises; its invocation of the response theorem at the stencil cannot prove its own admission. |

