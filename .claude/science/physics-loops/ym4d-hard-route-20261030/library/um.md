# Unmarked coupling increment: CA-I Lemma 4.2:lem-unmarked

Provenance: Codex, 2026-11-05, checkout `118aee86ba0801fe88124be1fac551101d2d7467`. Research text, not an audit; grants no status. Hand proof, retaining the account's named analytic inputs; not independently reviewed. No computer-assisted proof steps.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the outline and complete account at `31a47c543775`; Tadeusz Balaban for the renormalisation construction and estimates cited there.

## 1. Source reconciliation and comparison

CA-I means [complete account I](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/theorem_0_complete_account_raw_I.tex).
CA-II and CA-III mean [part II](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/theorem_0_complete_account_raw_II.tex)
and [part III](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/theorem_0_complete_account_raw_III.tex).
SA means the [outline](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM4_sketch_500.tex).
All source ranges below refer to this revision.

The target statement is CA-I 4031–4070. Its proof is 4076–4134;
the marker is at 4084. The statement assumes the actual earlier
representation, the actual one-step small-field bounds, and the
CMP 116 (2.41) bound on the non-Gaussian remainder. It does not ask
this lemma to construct that remainder.

The label occurs at CA-I 3603, 4019, 4022–4023, 4032, 56372,
56429, 56467, 163165 and 166617. CA-III 111368 repeats its
incomplete declaration. There is no label occurrence in CA-II.
The uses at 4015–4030 and 56361–56378 need the two printed bounds,
with the ceiling \(\varepsilon_1^{\mathrm I}\le c_0/(2C_{\rm rem})\).
The assembly at 56419–56481 uses them at the newly formed step,
before choosing its next coupling. The occurrence at 163165 imposes
the same ceiling with the SU(N) constants; it adds no new conclusion.

**This label is not resolved by the later existence proof.**
CA-I 58732–58988 proves the polarisation limit and gives the needed
rooted summation argument. But 58786–58790 and 58841–58847 allow
\(C_{\mathsf h}=C_{\mathsf h}(j)\). That proof alone does not give
the uniform constant required here. The checked completions in
[ui.md](ui.md) and [oc.md](oc.md) concern different domain clauses.

The outline index was used before the source excerpts. Relevant rows
are in chunks 06, 12, 13 and 19 and their obligations. SA 6559–6743
proves the extraction implication under its core and response
hypotheses. SA 12982–13021 gives its pointed version. SA 20649–20704
uses absolute radii for the unmarked chain and states a stronger
coupling-dependent error requirement. These are useful predecessors;
they do not verify this CA application's analytic inputs. The
unmarked polymer majorant at SA 14276 onward is a different statement.

| Local text | What it supplies here |
|---|---|
| [port/p1-base.md](port/p1-base.md), §§2 and 4 | Flow arithmetic and rooted geometric counting. The actual unmarked increment remains H-RG there. |
| [port/p5-induction.md](port/p5-induction.md), A6.1, A12 and change log | The same Cauchy mechanism for a marked family, with running radii and explicit domain/response hypotheses. A12 carries P5-H-unmarked as open. Its unanchored moment placeholder is not used below. |
| [ui.md](ui.md), §§2–6 and Result | The full two-readout tower estimate, with an early \(C_{IV}\). It can supply the near-zero Cauchy domain; it does not estimate this coefficient. |
| [oc.md](oc.md), §4.1 | The unit real factor makes every own-constant cube-gauge condition automatic. |
| [in1.md](in1.md), H-SF (11)–(13) and Result | Imports the small-field coefficient estimate. Its Gaussian matrix bookkeeping does not prove the present estimate. |

The existing `lit-balaban.md` search record was reused. The local
CMP 109 and CMP 99b scans were read at the formulas used below,
including rendered pages where OCR loses factors. CMP 109 (3.13)–(3.14),
(4.2)–(4.5), (4.14), (4.35)–(4.37) and (5.10) supply the published
route. In particular, (4.4) includes **both** \(P_1A\) and
\(\Delta A\). A potential-only bound does not suffice.
The primary scans used are
[CMP 109, 249–301](/Users/jonBridger/ym4d-papers/balaban_cmp109_249.pdf),
[CMP 99, 389–434 (99b)](/Users/jonBridger/ym4d-papers/balaban_cmp99_389.pdf),
and [CMP 119, 243–285](/Users/jonBridger/ym4d-papers/balaban_cmp119_243.pdf).
Page references mean printed page numbers.

The pinned YM3 account, `YM3/YM3_I.tex` 38427–38508, proves a
Gaussian-part comparison by marking the non-Gaussian origins.
The pinned QED3 text, `QED3/QED3.tex` 19217–19250, uses a
two-constants estimate before Cauchy extraction. Neither gives the
four-dimensional response/domain identification here. They are not
used as replacement hypotheses.

CMP 116 was absent from the supplied paper directory. Publisher and
Euclid requests returned access pages, so those attempts stopped.
Its (2.41) estimate remains the **explicit fourth hypothesis of the
target**, in the form recorded by CA-I 4053–4058, 4085–4093 and
4171–4180. No new proof of that cluster-expansion input is claimed.

There is also a useful later transcription: CA-II 83–89 writes
(2.41) as an **unpointed local** bound with prefactor
\(O(1)C_3\varepsilon_1\). CA-II 3445–3456 records an additional
early factor \(\alpha_6^{-1}\) in its version of the expansion.
Neither passage supplies the uniform extraction argument. Either
prefactor is compatible with the proof below: its coefficient of
\(\varepsilon_1\) is fixed before \(\varepsilon_1\).
We explicitly handle the unpointed convention rather than inferring
small pointed members from a bound on their sum.

## 2. The implication to prove and the quoted inputs

Keep the whole-lattice coefficient of CA-I 3764–3847 and the order
of H3. The four hypotheses, CA-I 4046–4058, are:

* \(g_0,\ldots,g_{l-1}\in(0,\gamma]\), with steps below \(l\)
  already performed along these couplings;
* the bounds in Theorem `4.20:thm-representation` at those earlier scales;
* the one-step small-field bounds on the actual unmarked output at \(l\);
* the CMP 116 (2.41) bound, with factor
  \(\varepsilon_1^{\mathrm I}\), on its remainder.

Write
\[
 E_l^{\mathfrak A}=G_l+R_l,\qquad
 \epsilon=\varepsilon_1^{\mathrm I},\qquad \xi=L^{-l}.
 \tag{1}
\]
Here \(G_l\) is the actual Gaussian normaliser, and \(R_l\) is
the actual second summand in that definition. Neither a large-field
remainder nor an arbitrary new activity is substituted for \(R_l\).
The coefficient functional, denoted by \(\mathcal B_l\), is linear;
thus
\[
 \beta_l^{\mathfrak A}-\beta_l^0=\mathcal B_l(R_l).
 \tag{2}
\]

The analytic bounds carried by hypotheses 3 and 4 are, in the
localisation in which each is stated,
\[
 \|E_l^{\mathfrak A}(X)\|_{U_l^c}\le E_0e^{-\kappa d_l(X)},
 \qquad
 \|R_l(X)\|_{U_l^c}\le A_R\epsilon e^{-\kappa d_l(X)}.
 \tag{3}
\]
The norm is a supremum on the complex regularity domain, not a bound
on the real total action. If the bound is stated for
\(E(X;\cdot,z)\), keep that pointing instead. \(A_R\) includes
the coefficient of \(\epsilon\) in the assumed (2.41), including
any early normalisation factor. A larger output decay rate may be
replaced by \(\kappa\). No part of the proof divides by a running
small-field radius. The cutoff \(\delta_{l-1}/g_{l-1}\) enters
only in supplying (3), through the two ceilings of CA-I 4171–4180.

Use the published estimates and the account's domain reading on
precisely the background used in the definition:

1. **An analytic current extension.** CMP 109, p. 272,
   (3.11)–(3.14), and pp. 281–282, (4.2)–(4.5). At the trivial
   background its four potential norms are
   \[
   \mathcal N_{l,X}(A)=\max\{
      |A|_X,|\nabla^\xi A|_X,|P_1A|_X,|\Delta^\xi A|_X\}.
   \tag{4}
   \]
   Here \(P_1=DPD^*\), \(R=1-P\), and the operators and
   differences have Balaban's normalisation. All stencil reads are
   included in the local norm. A fixed enlargement of the read can
   equivalently be absorbed in the constants below.
2. **The first response in this norm.** The paragraph between
   (4.4) and (4.5), CMP 109, p. 282, bounds the first derivative
   \(H_l=D\mathbf H_l(0)\) in all four members of (4), by
   \(B_3\) times the datum norm, with exponential decay from its
   support to \(X\). The free-boundary replacement is the one in
   (4.35)–(4.37), pp. 290–291. It gives numbers \(C_H,\sigma>0\),
   fixed independently of \(l,X\), such that
   \[
    \mathcal N_{l,X}(H_l\delta_x)
        \le C_H e^{-\sigma\operatorname{dist}(x,X)}.
    \tag{5}
   \]
   A smaller fixed positive rate is sufficient here. We do not use
   a stronger rate than that supplied by the cited response estimate.
3. **The hereditary reading of the domain.** Use the continuation
   ported in [ui.md](ui.md), with its retained background/averaging
   inputs, and the two tower rules of CA-I 32950–33080. The
   far-case argument, CA-I 33888–33935, explains its application
   at each hereditary label with cube letter \(M/L\). Section 3
   below checks the required inclusion at the unit background.

These are inherited analytic inputs of the account, not new
hypotheses about an arbitrary response. In particular the account
cites the inverse-covariance bounds and walk expansion of CMP 99b
(3.132) as printed without proof (CA-I 13142–13173). The use of
Balaban's response estimate retains that dependency. Likewise this
note does not independently prove the background derivative input
retained in ui. It completes the extraction implication under the
account's standing inputs, as the target lemma itself does for (2.41).

The normalisation in (5) matters. The datum \(\delta_x\) is on the
unit lattice of the current step. The represented fine link is
\(e^{i\xi A}\), so its tangent is \(i\xi H_l\delta_x\),
while its admissible link radius is proportional to \(\xi\).
Their quotient has no \(\xi^{-1}\) loss. The first differences
and the two second-order operators are already normalised in (4);
one must use (5) for them, rather than applying a difference operator
to a value-only estimate and paying \(\xi^{-1}\) or \(\xi^{-2}\).
At zero current the Landau response is the operator
\(G_0Q^*(QG_0Q^*)^{-1}\) of CMP 99b (3.126). On the homogeneous
whole-lattice tower its datum and output local block lengths in
step units are one. Thus (5) is the uniform estimate on this very
operator, not on a response from a different hierarchy. The
identification with the account's limit is CA-I 58834–58855.

One can pass the norm bound to that limit before doing Cauchy
extraction. Apply the cited estimate on an exhausting free-boundary
domain containing the source and all local reads. For a fixed mesh,
the value, first-difference and Laplacian members pass through
their finite stencils. For \(P_1H_l\), use its absolutely convergent
walk/kernel representation: first truncate the read and walk
lengths, take the common-term limit, and then remove the truncation
under the exponential majorant of the cited operator estimates.
The bounds for these four members have the same constants before
the limit. This preserves (5); a finite-stencil bound with a new
mesh-dependent constant would not.

## 3. One absolute Cauchy domain, including the current and all labels

At background one, the extension of CMP 109 (3.13) is
\[
 \Xi_l(A)=\left(e^{i\xi A},\,
        (\Delta^\xi-P_1)A+F(1,A)\right).
 \tag{6}
\]
The lower-order background term in (3.13) vanishes at one.
The remainder \(F(1,A)\) is analytic, has zero constant and
linear parts, and on a sufficiently small ball obeys
\[
 |F(1,A)|_X\le C_F\mathcal N_{l,X}(A)^2.
 \tag{7}
\]
This is the flat-background specialisation of the local-current
estimate CA-I 14083–14132, or directly (3.11)–(3.14).
\(C_F\) is independent of the fine mesh. At the flat point the
hierarchy weights at the output are one.

Choose an auxiliary number \(a>0\), after the absolute radii and
before \(\epsilon\), so that
\[
 a<\min\{1,\alpha_2,\alpha_1/8,\alpha_0/(2C_{IV})\},
 \qquad 2a+C_Fa^2<\alpha_0/2.
 \tag{8}
\]
It may be decreased to meet the analytic radius in (7). This is a
choice of a ball inside the existing domain, not a new condition on
the running couplings. The early H3 ceilings and floors used in ui
remain those already imposed in the account.

We claim that \(\mathcal N_{l,X}(A)<a\) implies
\(\Xi_l(A)|_X\in U_l^c(X,\alpha_0,\alpha_1)\), including
the one-power hereditary reading.

For the representative choose the real factor \(U=1\). Its
plaquettes, cube-gauge potentials and all real tower readouts are
identically trivial; this is also the observation in oc, §4.1.
The complex factor has potential \(A\), with value and gradient
less than \(a\). Its plaquettes satisfy
\(|\partial e^{i\xi A}-1|<C_{14}a\xi^2<\alpha_0\xi^2\)
by ui's clause (iii). Its independently supplied current in (6)
is less than \(2a+C_Fa^2<\alpha_0\). Thus clauses (i)–(iii)
hold. In particular, no assertion that an arbitrary small
potential has a small physical current is being made.

For clause (iv), fix a label \((p,Z)\) and either tower rule.
Put \(\mu=L^{p-l}\le1\). In level-\(p\) units the same
configuration is
\[
 e^{i\xi A}=e^{i\xi_p A^{\flat}},\qquad
 A^{\flat}=\mu A|_Z,\qquad
 |A^{\flat}|<\mu a,\quad
 |\nabla^{\xi_p}A^{\flat}|<\mu^2a\le\mu a.
 \tag{9}
\]
Use ui on \(Z\), with cube letter \(M'=M/L\), gauge constant
\(LB^{109}\), and radii
\((\mu\alpha_0,\mu\alpha_1,\mu a)\). The unit background
satisfies every half-radius hypothesis. Its averaged datum is one;
the complex datum displacement has the margin required in ui by
its averaging estimate and the already imposed ceiling
\(c_Q(\alpha_1+a)\le C_1\bar\varepsilon_1/2\).
The other ceilings decrease when multiplied by \(\mu\).
The product \(M'LB^{109}=MB^{109}\) keeps the cube-gauge
ceiling unchanged before that multiplication.

Both towers have collar at most \(R_1M_1\) in their top units,
by CA-I 32950–33050. The existing floors
\(\delta_0M\ge32L\), \(M\ge2LR_1M_1\) therefore give
the ui floors and collar condition at \(M'\). Its two-layer
interior is exactly \(Z^{\wr p}\). At every truncated depth
\(1\le n\le p\), ui consequently gives
\[
 |\Phi_i(e^{i\xi_p A^{\flat}})-\Phi_i(1)|
 \le \tfrac12 C_{IV}\mu a\,L^{2(n-p)}
 <\mu\alpha_0 L^{2(n-p)},\qquad i=1,2.
 \tag{10}
\]
Here \(\Phi_i(1)=0\). The curvature inequality in (10),
multiplied by \(L^{-2n}\), is
\(|\partial U_n-1|<\mu\alpha_0\xi_p^2\); the current
inequality is already
\(|J_n|<\mu\alpha_0(L^n\xi_p)^2\).
These are precisely CA-I 33058–33074 and 33119–33126 at this
label. The real-factor half is zero. The same \(a\) works for
every label, however large \(l\) is. This proves the claim.

Only values and first differences of \(A\) enter (9)–(10).
The second-order members of (4) are needed separately for the
independent current in (6). No uniform estimate on that current is
obtained by treating it as an additional arbitrary tower input.

## 4. Identification and the mixed Cauchy estimate

Every local scalar term is gauge invariant. Its first derivative
at \((1,0)\) is zero in both slots: constant gauge transformations
fix this point, and an invariant linear functional on a copy of
\(\mathfrak{sl}_N\) vanishes. Indeed it vanishes on every
commutator, and these span \(\mathfrak{sl}_N\). Apply this
argument to each bond slot separately. Differentiating local gauge
invariance once more shows that the Hessian annihilates a pure
gauge tangent \((D\omega,0)\). This is the two-slot version of
CMP 109 (4.14), also used at CA-I 58823–58833.

The Landau response satisfies \(RD^*H_l=0\). At the flat point,
\[
 D^*DH_l=(\Delta^\xi-DPD^*)H_l
        =(\Delta^\xi-P_1)H_l.
 \tag{11}
\]
Thus \(D\Xi_l(0)H_l\) is the actual first potential/current
response. An axial representative differs only by a pure gauge
tangent, which the Hessian annihilates. The term involving
\(D^2\Xi_l\) in the second-order chain rule is multiplied by
the zero first derivative. Consequently, for every local term \(f\),
\[
 D^2(f\circ\Xi_l)(0)[H_l\delta_x,H_l\delta_y]
 =D^2f(1,0)[\mathfrak h_\infty\delta_x,
                         \mathfrak h_\infty\delta_y].
 \tag{12}
\]
This establishes the identification with Definition 4.2, including
the current slot. It does not equate the nonlinear extension (6)
with the physical pair for arbitrary \(A\).

Suppose \(\|f\|_{U_l^c}\le S e^{-\kappa d_l(X)}\).
Let \(d_x=\operatorname{dist}(x,X)\),
\(q_x=C_He^{-\sigma d_x}\), and similarly for \(y\).
On the joint complex polydisc
\[
 |s|<a/(4q_x),\qquad |t|<a/(4q_y),\qquad
 A=sH_l\delta_x+tH_l\delta_y,
 \tag{13}
\]
we have \(\mathcal N_{l,X}(A)<a/2\), by (5). Section 3 admits
the entire polydisc. Although a distant-source coefficient in (13)
can be large, every read of this local function and every one of
its hereditary labels remains inside \(X\) and satisfies the
displayed norm bound. No global smallness of that coefficient is
required.

The two one-variable Cauchy formulas, followed by (12), give
\[
 \left|D^2f(1,0)[\mathfrak h_\infty\delta_x,
                         \mathfrak h_\infty\delta_y]\right|
 \le \frac{16C_H^2}{a^2}\,S\,
       e^{-\kappa d_l(X)-\sigma(d_x+d_y)}.
 \tag{14}
\]
The factor is independent of the number of fine bonds in \(X\),
since these are directional Cauchy formulas, not a sum of bounds
for individual Hessian entries. For the remainder \(S=A_R\epsilon\).
This is the uniform replacement for the scale-dependent
\(C_{\mathsf h}(l)/a_l\) argument in the later existence proof.

## 5. Pointing, rooted summation and the second moment

**Pointing convention.** Apply (14) directly when (3) is a bound
on the specified pointed local members. If (3) is in the unpointed
notation of CMP 116, use, for purposes of estimating its coefficient,
the auxiliary pointing
\[
 w_X(z)=\frac{\mathbf1_{X\cap\mathbb Z^4}(z)}
                  {|X\cap\mathbb Z^4|},\qquad
 \widetilde f(X;\cdot,z)=w_X(z)f(X;\cdot).
 \tag{15}
\]
Every localisation domain here contains unit-lattice sites.
The weights are field independent, nonnegative, at most one, and
sum to one. Thus (14) holds for \(\widetilde f\) with the same
\(S\). This is an estimate of a fixed functional under a
partition of unity, not an assertion that each original pointed
member is small whenever their sum is small.

The coefficient is unchanged. For each finite localisation sum,
summing (15) over \(z\) is the identity before and after either
derivative. The bounds below prove absolute convergence of the
twice-differentiated, second-moment sums, so this identity passes
to the whole-lattice coefficient. If the unpointed and pointed
localisation formulas file terms in different domains, apply the
same argument first to their finite-volume total: both are the
literal remainder of the same fluctuation integral. Its Hessian
on the same minimal orbit is identical. More explicitly, on a
finite torus \(V\), let \(\mathcal L_V(s,t)\) be this remainder
evaluated at the actual minimal pair over
\(e^{i(s\delta_x+t\delta_y)}\). The two localisation identities
and the vanishing first derivatives give
\[
 \sum_{X,z}D^2R^{\rm pointed}_{l,V}(X;1,0,z)
                     [\mathfrak h_V\delta_x,\mathfrak h_V\delta_y]
 =\partial_s\partial_t\mathcal L_V(0,0)
 =\sum_XD^2R^{\rm unpointed}_{l,V}(X;1,0)
                     [\mathfrak h_V\delta_x,\mathfrak h_V\delta_y].
\]
Take the common-lift limit of Definition 4.2 for each fixed pair
\(x,y\), before taking its second moment. Absolute convergence on
the original side is supplied by hypothesis 3 and the existence result already built
into that definition; on the unpointed side it follows below.
For the auxiliary pointing the same estimates apply on the torus.
For a wrapping domain, (g3)
gives \(d_l(X)>\varsigma/(4M)-2\). Splitting off half of the
polymer decay and using (17), the sum of wrapping contributions
at a fixed pair is at most an early constant times
\(S\varsigma^4e^{-\frac12\kappa(\varsigma/(4M)-2)}\), which
tends to zero. The factor \(\varsigma^4\) counts the unit-lattice
base points. The non-wrapping terms have the common lifts.
Thus the two whole-lattice kernels agree at each
pair, and the second-moment bound below applies to that common kernel.
The fixed-\(l\) convergence proof suffices for this identification;
we do not use its constant for the uniform estimate.

This also follows from the original pointing identity CMP 119
(3.38)–(3.42), pp. 274–275. In particular we have not assumed that
the pointed tensor itself is invariant under a change of pointing;
only its sum over the base point, and hence \(\mathcal B_l\), is.

Let \(\widehat\Pi_f(x,y,z)\) denote the pointed tensor using
either the originally bounded pointing or (15). Put
\[
 \rho=\tfrac14\min\{\sigma,\kappa/M\}>0.
 \tag{16}
\]
Use the rooted counting estimate and its reserved half rate from
CA-I 58877–58879:
\[
 \sum_{X\ni z}e^{-\kappa d_l(X)/2}\le K_0.
 \tag{17}
\]
This is the ordinary early counting floor on \(\kappa\), already
used by the account. Let \(c_d\) account for the fixed convention
for cube diameter and bond endpoints. For \(z\in X\), the
diameter bound (g2), CA-I 3748–3753, gives
\[
 |x-z|+|y-z|\le d_x+d_y+2Md_l(X)+4c_dM.
 \tag{18}
\]
By (16),
\[
 e^{-\kappa d_l(X)-\sigma(d_x+d_y)}
 \le e^{4c_dM\rho}
    e^{-\rho(|x-z|+|y-z|)}e^{-\kappa d_l(X)/2}.
 \tag{19}
\]
Equations (14), (17) and (19) therefore give
\[
 |\widehat\Pi_f(x,y,z)|
 \le C_*S e^{-\rho(|x-z|+|y-z|)},\qquad
 C_*:=16C_H^2a^{-2}K_0e^{4c_dM\rho}.
 \tag{20}
\]
All polymer sums are rooted at \(z\); there is no unweighted sum
over all translates of a polymer.

For clarity, the two remaining sums can be done without replacing
them by an unspecified second-moment theorem. Define
\[
 S_\rho=\sum_{v\in\mathbb Z^4}e^{-\rho|v|},\qquad
 T_\rho=\sum_{v\in\mathbb Z^4}|v|^2e^{-\rho|v|}.
 \tag{21}
\]
Both are finite. The number of sites in a sup-norm ball of integer
radius \(n\) is \((2n+1)^4\); hence the shell sums are bounded
by a polynomial of degree at most six times \(e^{-\rho n}\).
For every integer \(m\ge0\), the exponential series gives
\(n^me^{-\rho n}\le m!(2/\rho)^m e^{-\rho n/2}\),
so a geometric series proves the asserted finiteness by hand.

Taking bond origins \(x=u,y=0\), with their fixed endpoint costs
already included in \(c_d\), the triangle inequality gives
\[
 \begin{aligned}
 \sum_{u,z}|u|^2e^{-\rho(|u-z|+|z|)}
 &\le2\sum_{u,z}(|u-z|^2+|z|^2)
                  e^{-\rho(|u-z|+|z|)}\\
 &=4S_\rho T_\rho.
 \end{aligned}
 \tag{22}
\]
This proves all the absolute convergence needed above, including
the sum over base points and the interchange with the second
moment. Since \(|u_\mu u_\nu|\le|u|^2\),
\[
 |\mathcal B_l(f)|\le C_{\rm ext}S,
 \qquad C_{\rm ext}:=4C_NC_*S_\rho T_\rho.
 \tag{23}
\]
Here \(C_N\) is only the fixed finite colour contraction in the
account's coefficient convention; it can be omitted for an
individual normalised colour component. It depends on \(N\),
not on \(l\). Thus (2), (3) and (23) give
\[
 |\beta_l^{\mathfrak A}-\beta_l^0|
       \le C_{\rm ext}A_R\epsilon,
 \qquad
 |\beta_l^{\mathfrak A}|\le C_{\rm ext}E_0.
 \tag{24}
\]
The latter is also the second-moment consequence of CMP 109 (5.10).
Our smaller positive rate in (16) is sufficient for this scalar
conclusion; we need not improve it to the example rate printed there.

## 6. Constant order and the clause (0) consumer

Set
\[
 C_{\rm rem}=C_{\rm ext}A_R,\qquad
 C_\beta=C_{\rm ext}E_0.
 \tag{25}
\]
The dependency order is the account's order, not a simultaneous
smallness choice:

* The response, current-remainder, averaging and ui constants are
  early constants of the cited estimates. The rooted counting rate
  is fixed before \(M\); \(\kappa\) has its Stage-3 floors.
* \(M\) is fixed next with its existing floors. The absolute radii
  \(\alpha_1,\alpha_0,\alpha_2\) are then chosen as in Stage 7.
  The auxiliary radius \(a\) in (8) reads only these early letters.
* The amplitude \(E_0\), the coefficients in the assumed remainder
  bound (including \(C_3\) or its early \(\alpha_6^{-1}\)
  factor), and hence (25), are fixed before
  \(\varepsilon_1^{\mathrm I}\). This is compatible with
  CA-I 1614–1636. More explicitly, CA-II 3296–3306 writes
  \(C_3=4(L+2)^4O(1)E_0C_1^{116}\alpha_4^{-1}
  \alpha_6^{-1}M^{\bar q}e^{C_2^{116}\kappa_1}\);
  the superscript here distinguishes those two published absolute
  constants from the cutoff constants. Every factor precedes
  \(\varepsilon_1\). The possible additional factor
  \(\alpha_6^{-1}\) in CA-II 3443–3456 has the same property.
* Now choose \(\varepsilon_1^{\mathrm I}\) downward, including
  \(\varepsilon_1^{\mathrm I}\le c_0/(2C_{\rm rem})\).
  Finally choose \(\gamma\) with the one-step ceilings and the
  two conditions supplying (3).

Neither constant in (25) depends on \(l\) or on
\(\varepsilon_1^{\mathrm I}\); in particular \(C_\beta\)
satisfies the weaker requirement of being fixed before \(\gamma\).
No factor \(g_{l-1}^{-1}\), \(\delta_{l-1}^{-1}\), or
number of fine bonds has entered (25).

For the use at CA-I 4015–4030, the already supplied one-loop interval
bound consequently yields
\[
 \sum_{l=i+1}^n\beta_l^{\mathfrak A}
 \ge (n-i)c_0-2c_2-(n-i)C_{\rm rem}\epsilon
 \ge \tfrac12(n-i)c_0-2c_2.
 \tag{26}
\]
At the new step of clause (0), CA-I 56419–56481, all the inputs of
this proof use \(g_{l-1}\) and earlier couplings. The estimate does
not use the coupling that the assembly is about to define. Thus it
has exactly the order needed for hypothesis (b). No representation
theorem, Gaussian one-loop law, marked coefficient estimate, or
proof of T0 has been added by (26).

## Result

**Proof**

Under exactly the four hypotheses of CA-I
Lemma `4.2:lem-unmarked`, with the account's named Balaban analytic
inputs and hereditary-domain reading retained, there are constants
\(C_{\rm rem}\), fixed before \(\varepsilon_1^{\mathrm I}\),
and \(C_\beta\), fixed before \(\gamma\), such that for every
\(l\ge1\),
\[
 \boxed{\quad
 |\beta_l^{\mathfrak A}-\beta_l^0|
       \le C_{\rm rem}\varepsilon_1^{\mathrm I},
 \qquad |\beta_l^{\mathfrak A}|\le C_\beta .\quad}
\]
They are given by (25). Sections 3–5 supply the missing uniform
domain, full-current response, Cauchy and rooted second-moment
argument at (*). The unpointed form of (2.41) is sufficient by
(15) and the coefficient identity; no unproved smallness of an
arbitrary pointing is required. This proves the stated extraction
implication and grants no further scientific status.
