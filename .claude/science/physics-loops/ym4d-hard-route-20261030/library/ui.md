# Uniform increment in the Sussman–Alpoge complete account

Provenance: Codex, 2026-11-05, checkout `f305b5e698be702c61de33f4c463a4cb75e1f025`. Research text, not an audit; grants no status. Hand proof work, not yet checked by another model.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the outline and complete account at `31a47c543775`; Tadeusz Balaban for the underlying multiscale construction and operator estimates.

## 1. Source reconciliation and comparison

The source line numbers refer to the pinned
[outline](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM4_sketch_500.tex)
and [complete account I](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/theorem_0_complete_account_raw_I.tex),
with parts II and III of the same account used for the stated cross-checks.

The target is CA-I `4.5:lem-uniform-increment`, lines 16019–16151.
Its marked step is at 16233–16241. Its direct consumer is
`4.5:thm-operator-bounds`, especially (F1), 19781–19796.
This is condition (iv) of Balaban's local configuration space, not
clause (iv) of Theorem 0.

**The source continues the proof after the marked gap.** The heading
at 16019 says “Stated; proof incomplete”. The paragraph at 16233–16240
says the argument “is not carried out in the present proof”. But the
same pinned file subsequently gives these four parts:

| CA-I lines | Label | Content |
|---|---|---|
| 16268–16460 | `4.5:prf-increment-geometry` | Rescaling, maximal-tower collar, top-layer placement and local real gauge. |
| 16462–16730 | `4.5:prf-increment-kernel` | Real base, complex datum, differentiated background and a kernel representation. |
| 16732–16937 | `4.5:prf-increment-recentring` | An infinitesimal gauge cancellation, near estimate and exponential tail. |
| 16939–16990 | `4.5:prf-increment-conclusion` | Integration and the two half-radius bounds. |

Thus the geometric and recentring mechanism is theirs. This note ports
that continuation. It does not claim a new proof mechanism. Its analytic
inputs need the same explicit treatment as elsewhere in the account.
In particular, Balaban's (189)–(190) are described as printed without
proof at CA-III 35577–35624. They must not become a new unconditional
library theorem merely because the continuation cites them.

The outline index was searched first for the increment, hereditary
domains, averaging, response kernels and gauge covariance, with adjacent
rows and obligations. It points to SA 9654, 9718, 9816,
11508–11639, 11956–12092 and 12294–12383. The related substitution-room
argument at SA 15879–15943 requires \(\alpha_1^2\le C\alpha_0\)
and a \(K^\sharp\) radius restriction (15917–15919); the present
lemma requires neither. None is a previously proved version of this
exact CA increment on all its towers. The CA index for
4.12–4.19 also keeps application admission separate from operator bounds
(CA-I 49495–49547). The existing `lit-balaban.md` search record was reused;
the available local Balaban texts were consulted directly.

| Local text | Closest result and exact difference |
|---|---|
| [cp12.md](cp12.md), D1–D3 and Theorem 3 | Its (15) gives value, gradient, physical-current and gauge derivatives on its admitted P81/P82 charts, with complex datum over an admitted real reference. This is a version of the analytic response input. It does not identify every CA tower and chart with that domain, or perform the anchored cancellation giving the second power of \(\lambda\). |
| [pw.md](pw.md), §§1, 9 and Result | Bounds its specified \(H(s),H_1(s),\mathfrak G(s)\) on the admitted DR envelope. These are switched operators at an independent current. This is not the nonlinear axial map \(U_n\circ M^\cdot\), nor its two physical readouts here. |
| [rows.md](rows.md), §1 and Result | Supplies local row, force and nonlinear estimates for exactly DR's maps, with the same admission restrictions. It does not identify those maps with the present CA response. |
| [piv.md](piv.md), §§4, 6 and Result | Gives the local pivot graph, finite reads and real-gauge covariance on HMA's working domains. It imports its primitive averaging assumptions. It is related, not the required multiscale response estimate. |
| [in1.md](in1.md), constant order and Result | Orders early geometry and response constants before \(M\), and amplitudes afterwards. It is bookkeeping for imported bounds, not a proof of this increment. |

None of these comparisons licenses replacing the account's background
map by our independent-current response.

## 2. The statement and its inherited inputs

Keep every hypothesis of CA-I 16019–16151, including its reading
conventions, representative and tower. In particular, put
\[
 \xi=L^{-j},\quad \lambda=L^{n-j},\quad \eta=L^{-n}=\xi/\lambda,
 \quad \ell_q=L^{q-n}\quad(0\le q\le n).
\]
At the fixed point \(x\in X^{\sim2}\), write
\[
 \Phi_1(V)=\eta^{-2}\bigl(\partial U_n(M^\cdot V)(p)-1\bigr),
 \qquad \Phi_2(V)=J_n(M^\cdot V)(b),                         \tag{1}
\]
where \(p\) is based at \(x\), and \(b_-=x\). We must prove
\[
 |\Phi_i(e^{i\xi A}\mathbf U)-\Phi_i(\mathbf U)|
       \le \tfrac12 C_{IV}\alpha_2\lambda^2,
 \qquad i=1,2.                                             \tag{2}
\]
For a fine potential direction \(Z\), the notation
\(D\Phi_i(W)[Z]\) means the derivative along
\(s\mapsto e^{is\eta Z}W\) at zero. In the same notation,
\(DM^\cdot(W)[Z]\) is the left-trivialised datum velocity
\((1/i)(dM^\cdot/ds)(M^\cdot W)^{-1}\); it is not divided by
the source length \(\ell_c\).
Both current and curvature in (1) are the physical readouts of the
minimiser. The independently supplied \(\mathbf J\) is not substituted
for \(J_n\).

The following are the account's standing analytic inputs, not new
assumptions introduced to make (2) work.

* **Averages.** Balaban CMP 98, Propositions 2, 6 and 7, give real
  averaged curvature, analytic averaging on a fixed complex twist ball,
  the level factor \(\ell_q\), and the two-endpoint-block read. Their
  uses are written at CA-I 16479–16575 and 16838–16852. We use the
  associated local directional estimate in the form
  \[
   |DM^\cdot(W)[Z](c)|\le C_A\ell_c\sup_{E_c}|Z|,            \tag{3}
  \]
  with the output left-trivialised, \(E_c\) the actual double-block
  read, and \(C_A=C_A(d,L)\). This keeps an unspecified early constant;
  it does not need the particular numerical prefactor \(2c_Q\).
* **The analytic background.** Balaban CMP 102, Theorem 1 and
  Proposition 9, with (172), (181) and (190), supply the fixed real
  minimiser, its analytic Landau chart, axial covariance, and derivative
  estimates for \(\mathcal H\), \(\nabla\mathcal H\) and
  \(D^*D\mathcal H\). CA-I 16462–16730 uses this input, specifically
  its \(D^*D\) member at 16682–16683. The value and gradient members
  are also restated at CA-II 85845–85883. At a source of level \(q\), the functional
  kernel has the factor \(\ell_q^{-d}\). At an output of local unit
  one, its other scale factors equal one.
* **Local readouts.** CA-I `4.5:lem-curvature-remainder`, 14083–14132,
  gives the analytic local remainder and its differentiated bound in
  \(\mathcal J(e^{i\eta H}U_0)=\mathcal J(U_0)+D^*D H+F(U_0,H)\).
  The axial map is the nested contour/mean map described at
  16587–16633, with the same averaging radius.
* **Hierarchy summation.** CMP 96, Lemma 2.1, (2.59)–(2.61), is used
  with the early gap floors of CA-I 13402–13430 and 19445–19451.
  At \(\sigma=\delta_0/8\), it gives an early finite number \(S\) with
  \[
   \sup_y\sum_{c\in\mathfrak B_n}
        e^{-(\sigma/2)d(y,y_c)}\le S.                      \tag{4}
  \]
  The bounded number of bond rows at a site is included in \(S\).
  These floors concern \(R_1\mathfrak M\), before the later cube size
  \(M\); they are already standing conditions in the consumer.

The account's operator theorem explicitly assumes the averaging
derivative extension (CA-I 19585–19587), the corollary supplying
\(C_H\) and its accompanying statements (19588–19590), and the
frame-map Baker–Campbell–Hausdorff bound (19594–19596).
The proof below retains that dependency. In particular it is not a
rebuild of the printed, unproved calculation (189). This distinction
matters: the completed increment is an implication on the account's
existing analytic inputs, just as it is used by the operator theorem.

**Rate correction.** The first-derivative bound quoted from (190)
has rate \(\delta_0/8\), explicitly at CA-II 85874–85877 and
CA-III 35617. The continuation displays \(\delta_0/4\) in its
kernel estimate at CA-I 16723. The cited weaker bound does not imply
that stronger rate. We use \(\sigma=\delta_0/8\) throughout.
Section 6 shows that the lemma's original floor \(\delta_0M\ge32\)
still suffices. No change to its statement is needed.

## 3. Geometry and the kernel at a top point

**Geometry.** This ports CA-I 16268–16460. In level-\(n\) units,
the distance of \(x\) from \(X^c\) is at least \(2M/\lambda\).
Let \(x_0=y_x\) be the base of its top block, so
\(|x-x_0|_\infty\le1\). Put \(r=M/\lambda\) and
\(Q=\{z:|z-x_0|_\infty\le r\}\). Then \(Q\subset X\).

The collar hypothesis is
\(\operatorname{depth}(X\setminus\Omega_n)\le r/2\).
For \(|z-x_0|_\infty\le r/2+2\), its depth in \(X\) is at least
\(3r/2-3\ge r>r/2\). Here \(r\ge M\ge2R_1M_1\ge8d\ge6\).
Consequently this whole neighbourhood is in \(\Omega_n\).
In particular \(\ell(y_x)=1\).

For completeness, the maximal tower satisfies the required collar
bound. A point of \(\Omega_p\) farther than
\((R_1+dL)M_1\ell_p\) from its complement lies in a level-\(p+1\)
cube satisfying the defining gap. Maximality keeps that cube. Thus
\[
 \operatorname{depth}(X\setminus\Omega_n)
 \le (R_1+dL)M_1\sum_{p<n}\ell_p
 \le \frac{2(R_1+dL)M_1}{L}\le R_1M_1                 \tag{5}
\]
in level-\(n\) units. The last inequality follows from
\(2dL\le(L-2)R_1\), using \(L\ge4d\) and \(R_1\ge L\).
Multiplication by \(\lambda\le1\) gives at most \(R_1M_1\) in
level-\(j\) units. The floor \(2R_1M_1\le M\) finishes the claim.
For an arbitrary tower the collar bound is a hypothesis; no
maximality argument is applied to it.

The cube \(Q\) has side \(2M\) in level-\(j\) units. Reading
\((\rho1)\), CA-I 13096–13099, and \(c_{12}L\ge2\), give a real
gauge on it with \(U=e^{i\eta\widehat A_0}\), where
\[
 \widehat A=\lambda A,\quad \widehat A'=\lambda A',\quad
 |\widehat A_0|\le a_0^Q\lambda,\qquad
 a_0^Q:=\tfrac12 c_{12}LMB\alpha_0.
\]
The superscript distinguishes this local amplitude from the account's
early constant \(a_0\). Extend the real gauge outside \(Q\).
Gauge covariance and unitarity preserve all norms and the norm of the
increment of each readout. Hence work in this gauge. The third ceiling
of the lemma gives
\[
 s:=a_0^Q+\tfrac12\alpha_1+\alpha_2\le c_\sharp\le\tfrac14.  \tag{6}
\]
No estimate below uses \(M\alpha_1\).

**Kernel.** Put \(W_t=e^{it\eta\widehat A}\mathbf U\),
\(V_t=M^\cdot W_t\), \(V_0^{\rm r}=M^\cdot U\), and
\(U_0=U_n(V_0^{\rm r})\). The superscript avoids confusing the real
base with \(V_{t=0}=M^\cdot\mathbf U\). The source's real-curvature
and averaging estimates place
\[
 V_t=e^{iB_t}V_0^{\rm r},\qquad
 |B_t(c)|\le c_Q(\tfrac12\alpha_1+\alpha_2)\lambda\ell_c
       \le\tfrac12 C_1\bar\varepsilon_1.                   \tag{7}
\]
This is CA-I 16555–16561. The whole segment stays in the prescribed
complex chart over the same real base. We do not infer chart existence
from the condition (iv) that we are trying to reproduce.

Write
\[
 U_n(V_t)=\bigl(e^{i\eta\mathcal H(B_t)}U_0\bigr)^{g(B_t)}.
\]
For a datum variation \(\beta=(1/i)\dot V V^{-1}\), the derivative
of \(\log(V(V_0^{\rm r})^{-1})/i\) has norm at most two.
Indeed \(\|B_t\|\le1/8\), so
\(\|e^{iB_t}-1\|\le1/7\) and \(\|e^{iB_t}\|\le8/7\).
Differentiating the absolutely convergent logarithm series bounds its
derivative by \((1-1/7)^{-1}\); multiplying by \(8/7\) gives
\(4/3<2\).

More precisely, set
\(\dot B=(1/i)D\log_{e^{iB_t}}[i\beta e^{iB_t}]\), so
\(|\dot B(c)|\le2|\beta(c)|\) on each datum bond.
The supplied derivative estimates therefore bound the value, first
difference and \(D^*D\) readouts of
\(h=\delta\mathcal H(B_t)[\dot B]\). The local unit at the output
is one. The finite plaquette expansion bounds the first variation of
\(\eta^{-2}(\partial(e^{i\eta\mathcal H}U_0)-1)\) by a fixed
multiple of the value and first difference of \(h\).
For the current, the exact identity in §2 gives
\[
 \delta\mathcal J=D^*D h+\partial_HF(U_0,\mathcal H)[h].      \tag{8}
\]
The second term is bounded by the supplied local remainder estimate.
The first uses the \(D^*D\) member of the background derivative input;
a value estimate for \(h\) alone would not suffice.

The derivative of \(g\) also has the local bound stated at
CA-I 16674–16676. The scale count in that bound is as follows.
Differentiate the nested contour products and their iterated mean.
The real-base transports are unitary. At level \(q\), the
already-iterated averaging bound of §2 gives a relative perturbation
of size \(C\ell_q\sup|\mathcal H|\), and a variation of size
\(C\ell_q\sup|h|\). Thus the contour product and its derivative
are bounded by
\[
 \exp\!\left(C\sup|\mathcal H|\sum_{q\le n}\ell_q\right),
 \qquad
 C\sup|h|\sum_{q\le n}\ell_q\,
 \exp\!\left(C\sup|\mathcal H|\sum_{q\le n}\ell_q\right).
\]
Here \(\sum_{q\le n}\ell_q\le L/(L-1)\). The normalising
iterated mean is the one in CA-I 16597–16607; its analytic differential
and inverse are covered by the supplied frame-map bound. Applying
them to this contour variation costs another early constant. This
uses the bound for the full iterated map, rather than multiplying a
fixed one-step constant once per level. The result is
\(C_g e^{C_g\sup_{\Delta(y_x)}|\mathcal H|}\sup_{\Delta(y_x)}|h|\),
independent of the number of levels.
The frozen-radius choice gives
\(\sup_{\Delta(y_x)}|\mathcal H|\le\mathfrak r_g\le1\)
(CA-I 16614–16627). Thus both the adjoint factors and their derivatives
cost an early constant. Their derivatives multiply bounded local
curvature or current readouts, so add no inverse mesh power.

Collecting these terms gives
\[
 D\Phi_i(W_t)[Z]
   =\sum_{c\in\mathfrak B_n}\ell_c^d
             K_i(t;c)\,DM^\cdot(W_t)[Z](c),
 \qquad
 \|K_i(t;c)\|\le K\ell_c^{-d}e^{-\sigma d(y_x,y_c)}.         \tag{9}
\]
The notation treats the kernel as a linear map on colour components;
it is the trace-pairing formula of CA-I 16720–16729. All fixed norm
conventions are absorbed in \(K=K(d,L)\). Passing among the finitely
many local output stencils changes \(K\), not \(\sigma\).
This derivation is a port using the analytic input of §2; it is not
an independent proof of that input.

The two-endpoint-block read in (3) has a fixed physical diameter
\(R_A=R_A(d,L)\), since \(\ell_c\le1\). The hierarchy metric
dominates physical displacement, up to a fixed endpoint-block
offset. Choose one early \(c_g\ge1\), enlarged if necessary, so
that, with \(D_c=d(y_x,y_c)\),
\[
 \sup_{z\in E_c}(|z-x_0|_1+1)\le c_g(D_c+1),
 \qquad
 E_c\not\subset\{|z-x_0|_\infty\le r/2\}
       \Longrightarrow D_c\ge r/2-c_g.                   \tag{10}
\]
These follow by adjoining at most the two endpoint blocks to a
hierarchy path. Each block has side at most one. Enlarging \(c_g\)
also includes a fine-bond endpoint. No count of fine sites is used.

## 4. Exact infinitesimal cancellation

This is the recentring of CA-I 16732–16851. Choose a site cutoff
\(0\le\chi\le1\) which equals one on the cube of radius \(r/2\),
vanishes outside the cube of radius \(3r/4\), and has each coordinate
difference quotient at most \(4/r\). The piecewise-linear function
of \(|z-x_0|_\infty\) with these two radii has these properties.
Define
\[
 \nu_0(z)=-\sum_{\mu=1}^d\widehat A_\mu(x_0)(z-x_0)_\mu,
 \qquad \nu(z)=\chi(z)\nu_0(z).                           \tag{11}
\]
In particular \(\nu(x_0)=0\) and \(\|\nu\|\le dM\alpha_2\).
The smaller support only makes the source's cutoff choice explicit.
It ensures every bond with a nonzero endpoint value of \(\nu\)
lies inside \(Q\), since \(r/4>\eta\).

Fix \(t\). For sufficiently small complex \(z\), the gauge
\(w_z=e^{iz\nu}\) keeps the datum in the chart. This neighbourhood
may depend on \(\nu\); no uniform radius in \(z\) is required.
Covariance of the average and the axial branch gives
\[
 M^\cdot(W_t^{w_z})=(M^\cdot W_t)^{\bar w_z},\qquad
 U_n((M^\cdot W_t)^{\bar w_z})
       =U_n(M^\cdot W_t)^{\widetilde{\bar w_z}}.             \tag{12}
\]
Here \(\bar w_z\) is restriction to hierarchy sites, and its tilde
is the block-constant extension in Balaban (181). The second identity
is used only infinitesimally. It holds for real gauges by covariance
and uniqueness, extends to complex data by holomorphy, and then to
complex gauge directions by complex linearity of the derivative.
Equivalently it is the local analytic covariance stated immediately
after (181). This avoids any assertion that a large complex gauge
preserves the whole domain.

On the block containing \(x\), this extension equals
\(e^{iz\nu(x_0)}=1\). Plaquette holonomy and the current transform
at their starting site. Therefore both readouts (1) are unchanged
by (12), exactly. With
\[
 D_{W_t}\nu(b)=\eta^{-1}
     \bigl(\operatorname{Ad}_{W_t(b)}\nu(b_+)-\nu(b_-)\bigr),
\]
the fine-potential velocity is
\((1/(i\eta))(dW_t^{w_z}/dz)_{z=0}W_t^{-1}=-D_{W_t}\nu\).
The Ward identity is consequently
\[
 D\Phi_i(W_t)[-D_{W_t}\nu]=0.
\]
The velocity of \(W_t\) with respect to \(t\) is \(\widehat A\).
Thus the **exact** replacement is
\[
 \frac{d}{dt}\Phi_i(W_t)
    =D\Phi_i(W_t)[\widetilde A_t],\qquad
 \widetilde A_t:=\widehat A+D_{W_t}\nu.                    \tag{13}
\]
There is no finite gauge move, no remainder in (13), and no condition
\(M\alpha_2\ll1\). The field \(\widetilde A_t\) is a tangent
direction, not another point required to lie in the nonlinear domain.

## 5. Near and far sizes

On \(Q\), \(W_t=e^{it\eta\widehat A}e^{i\eta\widehat A'}
e^{i\eta\widehat A_0}\). For matrix norms in the account's
conventions, (6) and the exponential series give
\[
 \|\operatorname{Ad}_{W_t(b)}-1\|
       \le e^{2\eta\lambda s}-1
       \le4\eta\lambda s\le\eta\lambda.                  \tag{14}
\]
For the middle inequality, use
\(e^u-1\le u/(1-u)\le2u\) when \(0\le u\le1/2\).
The same estimate holds for \(\mathbf U=W_0\).

The hypothesis is on the covariant derivative of \(A\). In these
units it gives
\(\|\nabla^\eta_{\mathbf U}\widehat A\|<\alpha_2\lambda^2\).
Let \(\nabla_0^\eta\) denote the ordinary forward difference.
Its difference from the covariant one is bounded by
\(\eta^{-1}\|\operatorname{Ad}_{\mathbf U}-1\|
\|\widehat A\|\). Hence
\[
 \|\nabla_0^\eta\widehat A\|\le2\alpha_2\lambda^2.         \tag{15}
\]
This includes the commutator term left implicit at CA-I 16863–16872.
It uses adjacent values only, not a long nonunitary transport.

On a bond \((z,z+\eta e_\mu)\) whose endpoints lie where \(\chi=1\),
\[
 D_{W_t}\nu=-\widehat A_\mu(x_0)
       +\eta^{-1}(\operatorname{Ad}_{W_t}-1)\nu_0(z+\eta e_\mu).
\]
Telescope (15) along a coordinate path inside the cube, and use
\(|\nu_0(v)|\le\alpha_2\lambda|v-x_0|_1\). Equations (13)–(15)
give
\[
 |\widetilde A_t(z)|
       \le3\alpha_2\lambda^2(|z-x_0|_1+1).                 \tag{16}
\]
The factor \(\lambda^2\) is now on the near sources themselves.

On any bond meeting the support of \(\nu\), both endpoints are in
\(Q\). The product difference formula and the cutoff bound give
\[
 |\nabla_0^\eta(\chi\nu_0)|\le(1+4d)\alpha_2\lambda,
 \qquad
 \eta^{-1}|(\operatorname{Ad}_{W_t}-1)\nu|
       \le dM\alpha_2\lambda.
\]
Adding \(|\widehat A|<\alpha_2\lambda\) yields the global bound
\[
 |\widetilde A_t|\le C_f(1+M)\alpha_2\lambda,
 \qquad C_f:=2+5d.                                       \tag{17}
\]
If neither endpoint meets the support, \(D_{W_t}\nu=0\), so (17)
also holds outside \(Q\). No small-potential gauge outside \(Q\)
is being assumed.

## 6. Summation and constant choice

Call a source near when its entire read \(E_c\), including bond
endpoints, lies in the inner cube. Apply (3), (9), (10) and (16).
The source measure cancels its inverse density:
\(\ell_c^d\ell_c^{-d}=1\). The remaining \(\ell_c\le1\)
can be discarded. The near contribution is at most
\[
 3c_g C_AK\alpha_2\lambda^2
       \sum_c(D_c+1)e^{-\sigma D_c}
       \le N\alpha_2\lambda^2,
 \quad
 N:=3c_gC_AKS\left(1+\frac{2}{e\sigma}\right).              \tag{18}
\]
The last step is by (4) and the elementary inequality
\((u+1)e^{-\sigma u}\le(1+2/(e\sigma))e^{-\sigma u/2}\).
It follows by maximising \(u e^{-\sigma u/2}\) for \(u\ge0\).

For every remaining source, (10) gives
\(D_c\ge M/(2\lambda)-c_g\). Split its exponential into two
equal factors. Sum one using (4), and use (17) on its velocity.
The far contribution is at most
\[
 F_0(1+M)\alpha_2\lambda
        e^{-\sigma M/(4\lambda)},
 \qquad F_0:=C_AKC_fS e^{\sigma c_g/2}.                    \tag{19}
\]
This bound is valid also when the near set is empty.

Here the weaker quoted rate suffices without a stronger floor. Set
\[
 a:=\sigma M/4=\delta_0M/32\ge1.
\]
For \(0<\lambda\le1\), write the exponential as two equal factors.
The inequality \(v e^{-v}\le1/e\), at \(v=a/(2\lambda)\), gives
\[
 e^{-a/\lambda}
   \le \frac{2\lambda}{ea}e^{-a/2}
   \le\frac2e\lambda e^{-a/2}.                            \tag{20}
\]
Also, by differentiating \(u e^{-\sigma u/8}\),
\[
 (1+M)e^{-\sigma M/8}\le1+\frac8{e\sigma}.                \tag{21}
\]
Equations (19)–(21) bound the far contribution by
\[
 F\alpha_2\lambda^2,
 \qquad F:=\frac2e F_0\left(1+\frac8{e\sigma}\right).       \tag{22}
\]
Thus a permissible choice, made before \(M\), is
\[
 \boxed{C_{IV}:=\max\{4C_{14},\ 2(N+F)\},
             \qquad C_{14}=9(2d+2).}                      \tag{23}
\]
All symbols defining \(N,F\) are early constants depending on
\((d,L)\) in the account's conventions. Neither the depth nor the
number of bonds occurs. The only use of \(M\) in this estimate is
the stated floor and the bounded expression (21).

Combining the near and far bounds gives
\( |d\Phi_i(W_t)/dt|\le\tfrac12C_{IV}\alpha_2\lambda^2\)
for every \(0\le t\le1\). The path is analytic by (7), so the
fundamental theorem of calculus proves (2).

The original half-radius hypothesis and
\(\alpha_2\le\alpha_0/C_{IV}\) now give, strictly,
\[
 |\Phi_i(W_1)|<\tfrac12\alpha_0\lambda^2
                  +\tfrac12\alpha_0\lambda^2
                =\alpha_0\lambda^2.                     \tag{24}
\]
Multiplying the curvature inequality by \(\eta^2\), with
\(\eta^2\lambda^2=\xi^2\), gives exactly
\[
 |\partial U_n(M^\cdot W_1)-1|<\alpha_0\xi^2,
 \qquad |J_n(M^\cdot W_1)|<\alpha_0(L^n\xi)^2.             \tag{25}
\]
The real factor remains \(U\), so its half of condition (iv) is
unchanged. The potential and elementary curvature conclusions are
the already written part of the source proof, CA-I 16158–16231.
Our choice (23) preserves its requirement \(C_{IV}\ge4C_{14}\).
For \(j=0\) the list of sub-towers is empty.

## 7. Consumer and order check

First fix \(L\) and the propagator, averaging, gap and counting
constants. Fix \(C_1\), then \(C_H\), then
\(\bar\varepsilon_1\) as at CA-I 12783–12808. Fix (23) during
this same early stage. Next come \(M_1\), \(\kappa,\kappa_1\),
the enlargement constants and \(B\), and then \(M\). Choose
\(\alpha_1\), \(\alpha_0\), \(\alpha_2\) afterwards, respecting
the sum ceilings and
\(\alpha_2\le\min\{\alpha_1/8,\alpha_0/C_{IV}\}\).
This is CA-I 19375–19498. The local quantity \(a_0^Q\) in (6)
is bounded by an early ceiling; it never defines an early constant.

The proof uses no comparison between \(\alpha_0\) and
\(\alpha_1\), no upper bound on \(M\), and no
\(j-n\)-dependent restriction on \(\alpha_2\). If the cube letter
is \(M/L\), the same proof and the same \(C_{IV}\) apply with
the rescaled data specified in the source. Its floors become
\(\delta_0M\ge32L\) and \(2LR_1M_1\le M\), exactly as at
CA-I 16147–16150 and 19914–19917.

All occurrences of `4.5:lem-uniform-increment` were searched in the
three CA files. Besides the declaration and its own proof parts,
the uses are:

| CA-I location | Use and what this note supplies |
|---|---|
| 17928 | Only the elementary plaquette estimate, in the real-point frame comparison. This use does not need the marked increment step. |
| 19525; 20001 | Frozen datum radius and frame-map room. Their inherited analytic inputs remain those of §2. |
| 19985 | The fluctuation radius is at most \(\alpha_2/3\); this supplies the admitted displacement used by the consumer. It is not needed in the proof of the increment for a given \(A\). |
| 19783 | (F1) applies the lemma to \(A(t_\square)\), with amplitude at most \(2\alpha_2/3\). Equations (24)–(25) give its full condition (iv) on every sub-tower. Its separate independent-current bound is CA-I 19787–19790. |
| 19828 | (F6) uses the same maximal tower of \(X\). Any other tower is covered only when it already meets the stated collar and initial condition (iv). No window admission is inferred. |
| 19915; 19943; 20053 | Cube floors, amplitude ceilings and their order. The weaker-rate calculation (20) retains them unchanged. |
| 20118 | The large local gauge cube uses the hypothesis (1.12), not the cube cap in CMP 102 Theorem 1. This is exactly how §3 obtained its gauge. |

There are no occurrences of that label in CA-II or CA-III.
The proof of (2) never invokes its consumer, the free-current operator
theorem. In particular it does not use that theorem to supply its
own background derivative bound.

## Result

**Proof**

On the standing analytic-background, averaging and hierarchy inputs
of CA §4.5, the marked increment step of
`4.5:lem-uniform-increment` holds on its full stated tower class:
\[
 |\Phi_i(e^{i\xi A}\mathbf U)-\Phi_i(\mathbf U)|
      \le\tfrac12 C_{IV}(d,L)\alpha_2 L^{2(n-j)},\qquad i=1,2,
\]
with \(C_{IV}\) chosen by (23) before \(M\). It reproduces both
halves of condition (iv) with the account's original floors and
ceilings, and supplies exactly the use at CA-I 19783 and 19828.

This is a port and completion of the estimate in the source's own
continuation, CA-I 16268–16990. The uniform increment was not absent
from that continuation. The proof above makes its cutoff, covariant
difference and weaker-rate tail estimates explicit. It does not
claim a new route or an independent closure of the inherited
Balaban (189)–(190)/\(C_H\) input. Those remain cited inputs with
their source status; no T0 or audit status changes. Every estimate
here is by hand. Not yet checked by another model.
