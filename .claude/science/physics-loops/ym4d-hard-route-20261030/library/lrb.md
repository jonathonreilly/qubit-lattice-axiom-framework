# Local real base of a polymer

Provenance: Codex, 2026-11-05, checkout `0c5554a9106f655b78593781cab1e1d337fb98d1`; research text, not an audit, no status granted. Source: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, complete account at `31a47c543775`; Balaban's constructions are credited where used. All proof steps must be written arguments; computations cannot discharge them.

## 1. Source and scope

The target is CA-I `4.4:prop-local-real-base`, lines 8110–8373. Its Route is at 8376–8389.
The complete account is by **Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text**.
The walk interpolation and cluster integral come from **Tadeusz Bałaban**, CMP 116, §§1–2.
This note does not prove the account's walk hypothesis or its underlying physical positivity theorem.
Those are explicit premises of the proposition.

Source revision: `31a47c543775`.

| Source | SHA-256 |
|---|---|
| `/tmp/sa_ym4.tex`, 32,992 lines | `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f` |
| `/tmp/sa_ca_I.tex`, 166,711 lines | `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93` |
| `/tmp/sa_ca_II.tex`, 145,624 lines | `6a1f74b05f74ba44a2186c11fb08e139178d86b15c1494a95c434212944b2b8f` |
| `/tmp/sa_ca_III.tex`, 111,583 lines | `7e36523b85fb4f85aefdd45ab175420459f24e34fe56a4e83e53a6829c7a352d` |

Entry readings: GOAL; FINISH's published-work, efficiency and rules sections; port-map Table 3; chain-ca §§3, 7.1.
The checkout does not contain `docs/ai_methodology/SCIENCE_WORKFLOW.md` or its referenced repository skills.
The task-specific owner instructions govern this research note. No prompt, ledger, audit or status file is changed.

The source search began with sa-index/README, chunk-12's neighbouring Gaussian rows, obligations 729–741, and ca-full/index.tsv.
The outline's actual matrix construction is at SA 14091–14218.
It calls the matrix gap and closeness obligations open at SA 14258–14260.
Its finite-dimensional comparison theorem, SA 13904–14089, is a conditional theorem for a **symmetric** complex covariance.

The account contains more than the outstanding heading suggests:

| CA-I lines | Role |
|---|---|
| 4608–4702 | Local background polydiscs and their radius \(\rho\). |
| 4737–4907 | Quadratic form, compressed resolvents, walk lengths and weighted norm. |
| 5120–5216 | Full-footprint interpolation; vertex values are restricted walk sums. |
| 5519–5578 | The walk hypothesis, including local analytic coefficients and datum-independent majorants. |
| 6095–6154 | Auxiliary constants and (k1), (k2), (k2′), (k3). |
| 6219–6314 | Cell resolvent, inverse root and local-family statements. |
| 6959–6984; 7162–7189 | Local accretivity and the inverse identity at interpolation vertices. |
| 7421–7627; 7629–7825 | Symmetry conventions and printed tail argument; the symmetry lemma's full statement is not printed. |
| 7827–7988 | Symmetric polymer base, with proof. |
| 7990–8108 | Threshold and three floors; constants are chosen before \(M\). |
| 8391–8562 | Continued proof of the inverse-covariance comparison and imaginary vertex bound. |
| 8564–8759 | Continued proof of (3) and (4); the opening list explicitly adds inputs. |
| 8761–8837; 9208–9355 | Consumers in the cluster lemmas, including their additional assumptions. |
| 9615–9791 | Localised-independence consumer; it needs the actual local vertex functional. |

The continued proofs must be ported, not replaced by a new Gaussian construction.

## 2. Comparison with the frozen texts

None of the four named texts proves the proposition as stated.

| Text | What transfers; exact difference |
|---|---|
| [hm](hm.md), Lemmas 1, 4, Theorems 5, 7–8 | Supplies a related local gap, grouped root, collar count and Gaussian comparison. It assumes R/W/AV on R4 intersect Rep. Its precision labels are transpose-paired. Its \(C(s)=(\chi\mathsf A(s)\chi)^{-1}\); CA interpolates the **resolvent walk family itself**. Equality at vertices does not identify the two interpolations between vertices. |
| [descent](descent.md), Theorem B | Extends the replacement construction to all R4 by changing the absolute gauge Hessian to the relative Y form. Its own Main statement and Proposition C distinguish these forms. It does not identify CA's fixed coefficients or \(\mathbf P_{\rho,Z}\) with this domain. |
| [hma](hma.md), D4 and Theorem 2 | Adopts hm's full-read carriers for the Y form. Its frozen Outstanding clause retains carrier identification. An adopted family cannot identify a preassigned CA family. |
| [piv](piv.md) | Supplies the local nonlinear pivot chart under primitive averaging and admission hypotheses. It does not identify the Gaussian carriers, the gauge form, or the local-background domains. |

The sign of \(\Gamma\) is harmless after changing the auxiliary variable's sign.
The domain, gauge form, and interpolation differences are substantive.
We therefore retain CA's three walk families and its symmetric real comparison base throughout.

## 3. The precise inputs and order

Keep every hypothesis (a)–(d) and the setting of CA-I 8110–8169.
In particular, keep the local half of (W′), the local cell-resolvent hypotheses,
and the hypotheses of the symmetric-base corollary.
Their conclusions are imported with those hypotheses; their upstream physical claims are not proved here.

Write \(H=Z'_0\), \(I=\mathbb B(Z_0)\), \(\chi=\chi_I\), and \(\theta=\theta_K=\theta_0/4\).
The parameter cubes are those outside \(\operatorname{int}H\).
Only these cubes contribute to \(m(\varpi)\). Cubes inside \(H\) have fixed multiplier one.
This is the meaning of \(W(\emptyset)=H\) in CA-I 8159 and of the parameter set at 8141.
Coefficients with unread footprints are omitted before evaluation.
The parameter \(\kappa_1\) is positive in the stated Bałaban setting:
CA-I 1492–1495 fixes it above \(4L\kappa+1\).

For a matrix kernel use the weighted Schur norm
\[
 |K|_a=\max\left\{\sup_b\sum_{b'}|K(b,b')|e^{a|b-b'|},
 \sup_{b'}\sum_b|K(b,b')|e^{a|b-b'|}\right\}.
 \tag{1}
\]
For walk families replace the summand by its sum over \(\varpi\), weighted by
\(e^{a d(\varpi;b,b')}\). This is CA-I 4875–4907.
The two Schur sums multiply under kernel composition, by the triangle inequality.
They dominate the operator norm. CA-I 4908–4983 proves both facts.

On \(\mathbf P_{\rho,Z}\), the three **assigned** families obey
\[
 |||K|||_\theta\le B_K,\qquad
 B_{\mathsf A}=\mathsf B,\quad B_C=8S/\gamma_*,
 \quad B_{\mathsf M}=4S(2/\gamma_*)^{1/2}.
 \tag{2}
\]
For \(\mathsf A\) the stronger rate is \(\delta_{\mathsf A}\ge8\theta\).
Every step domain has sup-diameter at most \(4\ell\le M/12\).
These are (W′), cell-resolvent (v), and CA-I 7474–7491, 7530–7540.
In particular, (2) is an absolute family bound, not merely a bound on a sum with cancellations.

Use the account's order, CA-I 6095–6154, 7990–8050:

1. Fix \(\mathsf B,\delta_{\mathsf A},\gamma_*,\rho_w\) and the fixed profile.
   Choose \(r'\), hence \(r,\theta_0,\theta,S\), satisfying (k1).
2. Choose \(\ell\) under (k2), (k2′). All lattice sums and Gaussian comparison constants below
   depend only on these early data. In fact the comparison constants use only
   \((\mathsf B,\gamma_*,S,\theta,\delta_{\mathsf A})\).
3. Fix their positive smallness threshold \(\varepsilon_0^{P'}\), decreased as permitted by
   Definition 4.4:def-base-floors. It absorbs all comparison constants and is at most
   \(\min(3,\mathsf B)\).
4. For the already selected \(\kappa_1\), choose the allowed power \(M\) above (k3), (b),
   and the two \(M\)-floors in (d). Fix the required radius ratio
   \(\mathcal R_{\mathbf P}\) above its floor. Then choose the primed and unprimed radii
   below their ceilings, preserving this ratio.

No early constant is chosen from a later \(M\). The necessary floors exist because they
are finitely many lower bounds. The radius window opens by decreasing the unprimed radii,
as CA-I 5822–5909 specifies. The small potential and cutoff parameters of Balaban's
vertex integral retain their own later ceilings.

## 4. Weighted walks: proof of (2σ)

Let \(d_\varpi=d(\varpi;b,b')\). If a walk meets a parameter cube, its footprint leaves \(H\).
Choose a point \(x\) of that footprint outside \(H\), or approach such a point from its interior.
Since \(H\supset Z_0^{+M}\), its sup-distance from \(Z_0\) is at least \(M\).
A tree defining \(d_\varpi\) meets the step domain containing \(x\).
Thus that tree comes within \(4\ell\) of \(x\).
If \(\operatorname{dist}_\infty(b_-,Z_0)\le M/4\), its length is at least
\[
 M-M/4-4\ell\ge 2M/3.
\]
For \(C\), every row belongs to \(I\), and the endpoint convention allows
\(\operatorname{dist}_\infty(b_-,Z_0)\le1\).
Here \(M\ge48\ell\) and \(\ell\ge2r+4>4\), so \(1\le M/4\).
In both cases the weaker bound
\[
 d_\varpi\ge M/3,\qquad d_\varpi\ge |b-b'|
 \tag{3}
\]
suffices. The same observation holds at columns of \(C\).

The assumed cube count and first inequality in (b) give
\[
 \kappa_1m(\varpi)\le81\kappa_1+
       \frac{162\kappa_1}{LM}d_\varpi
 \le81\kappa_1+\frac{\theta}{4}d_\varpi.
 \tag{4}
\]
For a contributing walk, split the remaining \(3\theta d_\varpi/4\) into two equal parts.
By (3),
\[
 e^{\kappa_1m(\varpi)-\theta d_\varpi}
 \le e^{81\kappa_1-\theta M/8}
       e^{-(3\theta/8)|b-b'|}.
 \tag{5}
\]
Multiply by \(|K_\varpi|e^{\theta d_\varpi}\), sum, and apply (2).
This proves the first bound of (2σ) with precisely
\(\eta_1=e^{81\kappa_1-\theta M/8}\).
The interpolation difference consists exactly of these walks.
The reference contribution of each is zero, so no factor two is needed.

For the Schur estimate on \(C\), spend all the remaining rate on (3).
Both the row and column sums are bounded by
\[
 |C(\sigma;\mathsf u)-\mathsf T_H(\mathsf u)^{-1}|_0
 \le \frac{8S}{\gamma_*}e^{81\kappa_1-\theta M/4}.
 \tag{6}
\]
Here the identification at \(\sigma=0\) is Corollary 4.4:cor-localised-covariance,
CA-I 7162–7189, not an identity between interpolation and inversion away from vertices.

The second inequality in (b) is \(243\kappa_1\le\theta M/64\).
Consequently \(81\kappa_1\le\theta M/192\). Therefore
\[
 \eta_1\le e^{-23\theta M/192}\le e^{-\theta M/64}=\bar\eta,\qquad
 e^{81\kappa_1-\theta M/4}\le e^{-47\theta M/192}.
 \tag{7}
\]
These estimates hold at the full radius \(\rho\), as required.

For later use, (4) without the crossing condition gives the all-row bound
\(B_Ke^{81\kappa_1}\) at rate \(3\theta/4\).
On rows within \(M/4\), split into untagged and tagged walks.
Equations (2), (5) give the bound \(2B_K\) at rate \(3\theta/8\).
Both statements hold in Schur norm and entrywise. For the near-row statement,
the Schur norm means the kernel with those rows retained; its column sum is
also bounded by the restricted absolute family sum. For \(C\), retain all rows.

## 5. Field displacement: proof of (2U)

Fix the real local \(U\) and write
\(\mathsf u=(e^{i\xi A'}U,\mathbf J)\in\mathbf P_{\varsigma,Z}\).
The radial path
\[
 z\longmapsto\mathsf u_z=(e^{iz\xi A'}U,z\mathbf J)
\]
lies in \(\mathbf P_{\rho,Z}\) for \(|z|<\rho/\varsigma\).
This follows directly from the bounds defining that polydisc;
no complex curvature constraint was added to it (CA-I 4623–4636).
No extension of \(U\) outside \(Z\) occurs.

Suppose \(F(z)\) is any of the resulting matrix functions, bounded by \(D\)
on this disc in a specified Banach norm. On a circle of radius \(R<\rho/\varsigma\),
Cauchy's coefficient formula gives \(\|F_n\|\le D R^{-n}\).
Sum the positive-degree coefficients at \(z=1\), then let \(R\uparrow\rho/\varsigma\):
\[
 \|F(1)-F(0)\|\le D\sum_{n\ge1}(\varsigma/\rho)^n
      =D\,\frac{\varsigma}{\rho-\varsigma}.
 \tag{8}
\]
This also applies entrywise after multiplying by \(e^{\theta|b-b'|}\).
Use (2) for \(K^H\), and the last paragraph of §4 for \(K(\sigma)\).
It gives both bounds of (2U), including the stated replacements
\((2B_Ke^{81\kappa_1},3\theta/8)\) at all rows and
\((2B_K,3\theta/8)\) at controlled rows.
The factor two in the first replacement is harmless.
The Cauchy estimate is for a fixed real base and independent complex field/current coordinates.

## 6. Port of (1), (2s), and (2Γ)

This section ports CA-I 7827–7988 and 8391–8562.
It does not replace their symmetric-base construction.
Set \(T_0=\mathsf T_H(U,0)\), \(A_0=\operatorname{sym}\operatorname{Re}T_0\),
\(C_0^{\rm cv}=A_0^{-1}\), and \(G=\operatorname{Re}\Gamma(0;U,0)\).

For real \(v\), local coercivity gives
\[
 v^{\mathsf T}A_0v=\operatorname{Re}(v^{\mathsf T}T_0v)
       \ge(5\gamma_*/8)|v|^2.
\]
Since \(A_0\) is real symmetric, the same lower bound holds for complex vectors.
The symmetric-base corollary supplies
\[
 A_0\le\mathsf B,\quad |A_0(b,b')|\le\mathsf B e^{-\delta_{\mathsf A}|b-b'|},
\quad
 |T_0-A_0|_0\le\eta_{\rm sym},
 \tag{9}
\]
and the stronger entry bound
\[
 |(T_0-A_0)(b,b')|\le4\mathsf B
 e^{-\delta_{\mathsf A}\max(\mathsf r_s,|b-b'|)}
 \le\eta_{\rm sym}e^{-\delta_{\mathsf A}|b-b'|/2}.
 \tag{10}
\]
Inverting the positive eigenvalues proves both covariance inequalities in (1).

Write \(\mathcal L(a)=\sup_b\sum_{b'}e^{-a|b-b'|}\).
These lattice sums are finite uniformly in the torus.
For example, lifting torus displacements to nearest representatives bounds the sum
by the corresponding sum on \(\mathbb Z^4\), times the finite bond multiplicity.
That sum factors into four convergent geometric sums.
The same argument bounds
\(S''=\sup_b\sum_{b'}|b-b'|e^{-\delta_{\mathsf A}|b-b'|/2}\).

Here is the source's inverse comparison, with its constants retained.
Set
\[
 d_{\rm CT}=\min\{\delta_{\mathsf A}/2,\ 5\gamma_*/(16\mathsf B S'')\}.
\]
Conjugating \(A_0\) by \(e^{d_{\rm CT}|b-b'|}\), for a fixed column \(b'\),
changes it by a matrix of norm at most
\(\mathsf B d_{\rm CT}S''\le5\gamma_*/16\).
Indeed \(|e^t-1|\le |t|e^{|t|}\), and both Schur sums have this bound.
The conjugated matrix has inverse norm at most \(16/(5\gamma_*)\).
Thus
\[
 |A_0^{-1}(b,b')|\le\frac{16}{5\gamma_*}e^{-d_{\rm CT}|b-b'|}.
 \tag{11}
\]
Also \(|T_0^{-1}(b,b')|\le(8S/\gamma_*)e^{-\theta|b-b'|}\), by (2).
Apply
\[
 T_0^{-1}-A_0^{-1}=T_0^{-1}(A_0-T_0)A_0^{-1}.
\]
For \(a=\min(\theta,d_{\rm CT})\), convolution twice, halving the rate each time, gives
\[
 |(T_0^{-1}-C_0^{\rm cv})(b,b')|
 \le C_s\eta_{\rm sym}e^{-\theta_s|b-b'|},\quad
 \theta_s=a/4,\quad
 C_s=\frac{8S}{\gamma_*}\frac{16}{5\gamma_*}
       \mathcal L(a/2)\mathcal L(a/4).
 \tag{12}
\]
For clarity, the convolution inequality is
\(e^{-a u-a v}\le e^{-a|b-b'|/2}e^{-a u/2}\)
when \(u+v\ge|b-b'|\). This proves the remaining part of (2s).

In \(\Gamma_0\), keep the intermediate bond \(b_1\) in \(I^c\), as the definition requires.
The two factor bounds and convolution give
\[
 |\Gamma_0(b,b')|\le\mathsf B B_{\mathsf M}\mathsf S
        e^{-\theta|b-b'|/2},\qquad \mathsf S=\mathcal L(\theta/4).
 \tag{13}
\]
Taking real parts cannot increase an entry norm. This completes (1).

For (2Γ), call \(b_1\) near if
\(\operatorname{dist}_\infty(b_{1,-},Z_0)\le5M/6\).
At such bonds the symmetric-base corollary bounds
\[
 |\operatorname{Im}\mathsf M^H(b_1,b')|
 \le2B_{\mathsf M}e^{-\theta\max(\mathsf r_s,|b_1-b'|)}.
\]
At every \(b\in I\), its other bound gives
\[
 |\operatorname{Im}\mathsf A^H(b,b_1)|
 \le2\mathsf B e^{-\delta_{\mathsf A}\max(\mathsf r_s,|b-b_1|)}.
\]
At far \(b_1\), \(|b-b_1|\ge5M/6-1\ge M/2\).
Use \(\operatorname{Im}(XY)=(\operatorname{Im}X)(\operatorname{Re}Y)
+(\operatorname{Re}X)(\operatorname{Im}Y)\).
In the term containing \(\operatorname{Im}\mathsf A^H\), spend half the rate
on \(\mathsf r_s\) for all \(b_1\). Do the same in the term containing
\(\operatorname{Im}\mathsf M^H\) at near \(b_1\).
For the latter term at far \(b_1\), spend half of the first factor's rate on \(M/2\).
The remaining convolution, with rate halved once more, yields exactly
\[
 |\operatorname{Im}\Gamma_0(b,b')|
 \le\mathsf B B_{\mathsf M}\mathsf S
 [4e^{-\theta\mathsf r_s/2}+e^{-\theta M/4}]
 e^{-\theta|b-b'|/4}
 \le B_{\mathsf M}\mathsf S(\eta_{\rm sym}+\mathsf B\bar\eta)
 e^{-\theta|b-b'|/4}.
 \tag{14}
\]
Extending the restricted \(b_1\)-sums to all bonds only enlarges these nonnegative bounds.

## 7. Port of full-radius coercivity: (3)

This is CA-I 8583–8631, now with its (2σ) input proved.
For \(\mathsf u\in\mathbf P_{\rho,Z}\), put \(T=\mathsf T_H(\mathsf u)\) and
\(E=C(\sigma;\mathsf u)-T^{-1}\).
The localised-covariance corollary gives
\(\operatorname{Re}\langle v,Tv\rangle\ge5\gamma_*|v|^2/8\) and \(\|T\|\le\mathsf B\).
Put \(t=\gamma_*/(4\mathsf B S)\le1/4\).
Condition (k2) says \(e^{-\theta_0\ell/8}\le t\).
Since \(M\ge48\ell\) and \(\theta=\theta_0/4\),
\[
 e^{-\theta M}\le t^{96}.
\]
Equations (6)–(7) then imply
\[
 \mathsf B\|E\|\le2t^{45/2}\le\tfrac12,\qquad
 \mathsf B^2\|E\|\le\frac{\gamma_*}{2S}t^{43/2}\le\frac{\gamma_*}{16}.
 \tag{15}
\]
The Neumann series for \(I+TE\) proves invertibility of \(C=T^{-1}(I+TE)\), and
\[
 \|C^{-1}-T\|\le
 \frac{\mathsf B^2\|E\|}{1-\mathsf B\|E\|}
 \le\gamma_*/8.
\]
Hence \(\operatorname{Re}\langle v,C^{-1}v\rangle\ge\gamma_*|v|^2/2\),
which is stronger than the printed \(3\gamma_*/8\).
This proof uses (b), (k2), (k3), and the previously established local covariance bounds.
It does not use any floor from (d).

## 8. Products and the four perturbation estimates: (4a)

Here we supply the kernel and product estimates that CA-I 8568–8572 lists as
additional inputs to its continued proof. We then follow its four steps at 8646–8692.
Put \(t_\rho=\varsigma/(\rho-\varsigma)\).

### Products with a row near the polymer

Consider a product of \(p\le3\) of the assigned kernels, with any coordinate
projections between them. Retain every intermediate bond \(b_1,\ldots,b_{p-1}\)
and the separate walks \(\varpi_1,\ldots,\varpi_p\) in its expansion. Write
\[
 D=\sum_{j=1}^p d(\varpi_j;b_{j-1},b_j),\qquad
 N=\sum_{j=1}^p m(\varpi_j),\qquad B_\Pi=\prod_{j=1}^pB_{K_j}.
\]
The multiplicity in \(N\) is intentional: the interpolation is applied separately
to each factor. Applying (4) to each walk gives
\[
 \kappa_1N\le81p\kappa_1+\theta D/4.
 \tag{16}
\]
The absolute family sums with weight \(e^{\theta D}\) have both Schur sums at
most \(B_\Pi\). To see this directly, sum the last endpoint and last walk first
for the row sum, then work backwards through the factors. Each sum costs at
most its \(B_{K_j}\). For the column sum work forwards instead. A coordinate
projection only removes terms.

Suppose the initial row is within \(M/4\) of \(Z_0\) and \(N\ge1\).
Join the trees of the \(p\) walks at their common endpoints. The resulting
connected graph contains the initial endpoint and meets a step domain outside
\(H\), and its length is at most \(D\) (or arbitrarily close to it if an infimum
defines a walk length). The geometric argument of (3) gives \(D\ge M/3\).
Also \(D\ge|b_0-b_p|\). Thus
\[
 e^{\kappa_1N-\theta D}
 \le e^{81p\kappa_1-\theta M/8}e^{-(3\theta/8)|b_0-b_p|}
 \le\bar\eta\,e^{-(3\theta/8)|b_0-b_p|}.
 \tag{17}
\]
The last inequality uses \(81p\kappa_1\le243\kappa_1\le\theta M/64\);
in fact the first exponential is at most \(e^{-7\theta M/64}\).

The product at zero keeps exactly the terms with \(N=0\). Subtracting it
therefore leaves the terms estimated in (17), with no subtraction loss.
The difference has weighted Schur norm at rate \(3\theta/8\) at most
\(B_\Pi\bar\eta\), on the indicated rows. The zero product has norm at most
\(B_\Pi\) at rate \(\theta\). Since \(\bar\eta\le1\), their sum has norm at
most \(2B_\Pi\) at rate \(3\theta/8\). Without the row restriction, (16) gives
the bound \(B_\Pi e^{81p\kappa_1}\) at rate \(3\theta/4\).
These are the two required classes of product bounds.
Transposing the entire product gives the corresponding statement for a
column near \(Z_0\).

Apply the same radial Cauchy argument (8) to the product, rather than estimating
its factors one at a time at far intermediate rows. Its displacement in the
datum is bounded by \(2B_\Pi t_\rho\) in the controlled-row norm.
In particular, keeping \(\chi^c\) in the two-factor product defining \(\Gamma\),
\[
 |\Gamma(\sigma;\mathsf u)-\Gamma_0|_{3\theta/8}
 \le \mathsf B B_{\mathsf M}(\bar\eta+2t_\rho).
 \tag{18}
\]
The norm here is for the rectangular matrix whose rows belong to \(I\);
both of its Schur sums are controlled by the preceding proof.
This estimate is stronger than the rate \(\theta/32\) used at CA-I 8678–8681.

### The covariance, inverse, coupling, and determinants

Choose once, before \(M\),
\[
 a=\tfrac12\min\{\theta_s,\theta/32\}>0.
\]
Equations (5), (8), (12), (14), (18), and finite lattice sums imply
\[
 |E'|_a+|\Gamma-G|_a\le D_0\hat\varepsilon,\qquad
 E'=C(\sigma;\mathsf u)-C_0^{\rm cv},\quad
 \hat\varepsilon=\bar\eta+t_\rho+\eta_{\rm sym}.
 \tag{19}
\]
Here \(D_0\) depends only on the early data displayed in the proposition.
For the first term use exactly the decomposition in CA-I 8653–8654:
\[
 E'=[C(\sigma;\mathsf u)-\mathsf T_H(\mathsf u)^{-1}]
 +[\mathsf T_H(\mathsf u)^{-1}-T_0^{-1}]
 +[T_0^{-1}-A_0^{-1}].
 \tag{20}
\]
For the second term use
\(\Gamma-G=(\Gamma-\Gamma_0)+i\operatorname{Im}\Gamma_0\).
Every entrywise exponential used here has rate strictly larger than \(a\),
so the conversion to (19) costs only an early lattice sum.

Let \(Q\ge1\) bound \(|A_0|_a,|C_0^{\rm cv}|_a,|G|_a,D_0\);
(9), (11), and (13) supply such a \(Q\) uniformly in the regions and level.
If \(Q D_0\hat\varepsilon\le1/2\), the weighted Schur algebra gives
\[
 \begin{split}
 C^{-1}&=(I+A_0E')^{-1}A_0
       =A_0-A_0E'A_0+R_2,\\
 |C^{-1}-A_0|_a&\le2Q^2D_0\hat\varepsilon,\qquad
 |R_2|_a\le2Q^3D_0^2\hat\varepsilon^2 .
 \end{split}
 \tag{21}
\]
Indeed the terms of degree at least two are
\((A_0E')^2(I+A_0E')^{-1}A_0\).
This proves the inverse comparison and its Neumann remainder, part (i).
Its base inputs are precisely
\[
 C_0^{\rm cv}\ge\mathsf B^{-1}\ge5\gamma_*/(8\mathsf B^2),\qquad
 1/\|C_0^{\rm cv}\|\ge5\gamma_*/8,\qquad
 (C_0^{\rm cv})^{-1}=A_0,
 \tag{22}
\]
with the decay in (9); no further Combes–Thomas argument is needed.

For part (ii), taking entrywise real parts in (19) gives the bound for
\(R_3=\operatorname{Re}\Gamma-G\). For part (iii), telescope
\[
 \begin{split}
 \Gamma^{\mathsf T}C\Gamma-G^{\mathsf T}C_0^{\rm cv}G
 ={}&(\Gamma-G)^{\mathsf T}C\Gamma
   +G^{\mathsf T}(C-C_0^{\rm cv})\Gamma\\
   &+G^{\mathsf T}C_0^{\rm cv}(\Gamma-G).
 \end{split}
 \tag{23}
\]
Transposition preserves the norm (1), including for rectangular matrices.
After decreasing the threshold so that \(D_0\hat\varepsilon\le1\), all
unchanged factors have norm at most \(Q+1\). Thus (23) has norm
at most an early constant times \(\hat\varepsilon\), with exponential
entrywise decay at rate \(a\). This proves the asserted form estimate in real
\(X\), using the bilinear transpose required by the analytic prefactor.

For part (iv), set \(E_1=C^{-1}-A_0\), \(E_2=\operatorname{Re}E_1\),
where this real part is entrywise. Then
\[
 \det(C^{-1})=\det A_0\,\det(I+C_0^{\rm cv}E_1),\qquad
 \det(\operatorname{Re}_{\rm ent}C^{-1})
 =\det A_0\,\det(I+C_0^{\rm cv}E_2).
 \tag{24}
\]
If an \(m\)-dimensional matrix \(N\) has \(\|N\|\le u\le1/2\), the convergent
series for \(\log(I+N)\) proves
\[
 |\log\det(I+N)|\le m\sum_{j\ge1}u^j/j\le2mu.
 \tag{25}
\]
The determinant is nonzero throughout this ball, so this logarithm fixes
the branch. Equations (19), (21), and (25) give the determinant quotients
and their inverses a bound \(\exp(C\hat\varepsilon m)\).
The same proof applies with \(\operatorname{sym}E_1\) or
\(\operatorname{sym}\operatorname{Re}_{\rm ent}E_1\), since their norms do not
increase. These are the determinants of the actual Gaussian densities.

Thus all four estimates described in the account's continued proof hold with
one early constant \(C_P\hat\varepsilon\). Enlarge \(C_P\) to cover the
constants in (19)–(25), and shrink \(\varepsilon_0^{P'}\) to satisfy their
finitely many smallness inequalities. This is exactly the absorption
permitted at CA-I 8015–8021; it happens before choosing \(M\).

## 9. The actual Gaussian integral: (4b)

We port the real integration argument at CA-I 8694–8738, making its density
convention explicit. CA-I 7313–7314 defines \(d\mu_C\) as the **normalized**
density proportional to \(\exp(-B^{\mathsf T}C^{-1}B/2)\).
The account expressly allows a nonsymmetric localized matrix
(CA-I 7324–7364). Therefore put
\[
 H_C=\operatorname{sym}(C^{-1}),\qquad C_s=\operatorname{sym}C.
\]
The density is
\((2\pi)^{-m/2}(\det H_C)^{1/2}
\exp(-B^{\mathsf T}H_CB/2)\).
The square root is continued from \(A_0\) using (25).
Normalization follows from the real positive Gaussian formula and
successive identity theorems in the symmetric matrix entries; this is the
argument in SA 14023–14034, applied to \(H_C\).
This convention matters: \(\det C^{-1}\) is not in general the normalizing
determinant when \(C\) is nonsymmetric. The algebraic estimates (24) hold
as written; the density estimates use their symmetrized versions.

For clarity we give the actual majorant, retaining the \(B\)-then-\(X\)
order of the account. Let
\[
 \mathcal J(F)=\int d\mu_0(X)\,
 e^{-\frac12X^{\mathsf T}\Gamma^{\mathsf T}C\Gamma X}
 \int d\mu_C(B)\,e^{-B^{\mathsf T}\Gamma X}F(B).
 \tag{26}
\]
This is CA-I 7306–7314 and, at scalar parameter \(s=1\),
CA-II 3606–3618. Let \(m\) be the real coordinate dimension on \(I\), and
\(n\) the dimension of \(X\). The following proof is uniform in both.

Choose the early number
\[
 K=1+\mathsf B+\frac8{5\gamma_*}
       +\mathsf B B_{\mathsf M}\mathsf S^2.
\]
It bounds \(\|A_0\|,\|C_0^{\rm cv}\|,\|G\|\), and \(A_0\ge K^{-1}\).
By (19), after an early enlargement of \(C_P\),
\[
 \|C-C_0^{\rm cv}\|+\|\Gamma-G\|\le\delta:=C_P\hat\varepsilon.
 \tag{27}
\]
Assume first that \(|F(B)|\le F_*e^{\lambda|B|^2}\), with \(\lambda\ge0\).
We will use only \(\delta\le1/(2K)\), and two explicit smaller bounds below.
The inverse identity gives
\[
 \|C^{-1}-A_0\|\le2K^2\delta,\qquad
 \|C\|,\|\Gamma\|,\|\operatorname{Re}_{\rm ent}\Gamma\|\le2K.
\]
Write
\[
 R=\operatorname{Re}_{\rm ent}H_C,\quad
 J=\operatorname{Re}_{\rm ent}\Gamma,\quad
 P=\operatorname{Re}_{\rm ent}(\Gamma^{\mathsf T}C_s\Gamma),\quad
 D_B=R-2\lambda I.
\]
These quadratic forms are real symmetric. Put
\(h=2K^2\delta+2\lambda\). If \(Kh\le1/2\), then
\[
 D_B\ge(2K)^{-1},\qquad
 \|D_B^{-1}-C_0^{\rm cv}\|\le2K^2h
       =4K^4\delta+4K^2\lambda .
 \tag{28}
\]
Taking absolute values in (26), then performing the real \(B\)-integral,
gives the bound
\[
 F_*\frac{|\det H_C|^{1/2}}{\det D_B^{1/2}}
 \int d\mu_0(X)\exp\!\left(\tfrac12X^{\mathsf T}D_X X\right),
 \qquad
 D_X=J^{\mathsf T}D_B^{-1}J-P .
 \tag{29}
\]
No contour is moved across a cutoff.

At \(\delta=\lambda=0\), \(J=G\), \(D_B=A_0\), and
\(P=G^{\mathsf T}C_0^{\rm cv}G\). Consequently \(D_X=0\).
Equivalently,
\[
 \int d\mu_{C_0^{\rm cv}}(B)e^{-B^{\mathsf T}GX}
   =e^{\frac12X^{\mathsf T}G^{\mathsf T}C_0^{\rm cv}GX},
 \tag{30}
\]
which cancels the reference prefactor exactly. This is the zeroth-order
cancellation in Bałaban (2.24) and CA-I 8700–8706.

Here is the small remainder in (29), with no reality assumption on the
true matrices. Expanding the two factors of \(J\), using
\(\|J-G\|\le\delta\), and then (28), gives
\[
 \|J^{\mathsf T}D_B^{-1}J-G^{\mathsf T}C_0^{\rm cv}G\|
 \le 10K^6\delta+4K^4\lambda .
\]
For example, the first two terms of this expansion cost
\(\delta(2K)(2K)+K(2K)\delta=6K^2\delta\), and the last costs
\(K^2(4K^4\delta+4K^2\lambda)\).
The three terms of (23), now in operator norm and with real parts,
give
\[
 \|P-G^{\mathsf T}C_0^{\rm cv}G\|\le7K^2\delta.
\]
It follows that
\[
 \|D_X\|\le v:=17K^6\delta+4K^4\lambda.
 \tag{31}
\]
If \(v\le1/2\), the remaining integral converges absolutely and equals
\(\det(I-D_X)^{-1/2}\).

These estimates give the required volume cost as well.
Over the real coordinates, \(J^{\mathsf T}D_B^{-1}J\) has rank at most
\(m\). If \(\Gamma=X_1+iX_2\) and \(C_s=C_1+iC_2\), then \(P\) factors
through the \(2m\) rows of \(\binom{X_1}{X_2}\), with middle matrix
\(\left(\begin{smallmatrix}C_1&-C_2\\-C_2&-C_1\end{smallmatrix}\right)\).
Hence \(\operatorname{rank}D_X\le3m\).
The real spectral theorem and
\(-\log(1-v)\le2v\) imply
\[
 \det(I-D_X)^{-1/2}\le e^{3mv}.
 \tag{32}
\]
Furthermore
\[
 \|C_0^{\rm cv}(H_C-A_0)\|\le2K^3\delta=:a_1,\qquad
 \|C_0^{\rm cv}(D_B-A_0)\|\le Kh=:a_2.
\]
All eigenvalues of either relative perturbation have modulus at most its
norm. Thus, for \(a_2\le1/2\),
\[
 \frac{|\det H_C|^{1/2}}{\det D_B^{1/2}}
 \le(1+a_1)^{m/2}(1-a_2)^{-m/2}
 \le e^{m(3K^3\delta+2K\lambda)}.
 \tag{33}
\]
Combining (29), (31)–(33) gives the explicit sufficient estimate
\[
 \int\!\!\int|\text{integrand of (26)}|
 \le F_*\,e^{68K^6(\delta+\lambda)m}.
 \tag{34}
\]
It has no cost proportional to the auxiliary dimension \(n\).
The inequalities used are elementary real Gaussian integration, finite
matrix algebra, and convergent series, not numerical checks.

The input \(F\) is the one in the account, not a new test integrand chosen
to replace it. CA-II 3562–3567 and 3600–3624 write its terms as
\[
 (-1)^{|P_{\rm fail}|}\chi_{Y_0}\chi^c_{P_{\rm fail}}\,
 \exp\!\left[\sum_{Y\in D}\tau(Y)V(Y,B)\right].
 \tag{35}
\]
The finite sums and the \(\tau\)-contours belong to the prior Mayer expansion.
In the stated setting of Bałaban (2.14), the potentials have the form and
bounds (1.42), (1.43), (1.36). We retain these inputs, exactly as CA-II
3530–3537 does; they are not conclusions about arbitrary potentials from
(a)–(d). Their already-established bound is
\[
 \sum_{Y\in D}|\tau(Y)|\,|V(Y,B)|
 \le c_V\alpha_4|B|^2+c_V\alpha_4 M^{-4}|Y_0|.
 \tag{36}
\]
This is the bound ported at CA-II 3710–3722; \(c_V\) is an early constant.
Each failed test forces \(|B(b)|\ge T\). Pointwise, their product is at most
\[
 \exp(-\gamma_2T^2|P_{\rm fail}|/2)
 \exp\!\left(\frac{\gamma_2}{2}\sum_{b\in P_{\rm fail}}|B(b)|^2\right).
 \tag{37}
\]
Thus (34) applies with
\[
 F_*=\exp(c_V\alpha_4M^{-4}|Y_0|-\gamma_2T^2|P_{\rm fail}|/2),
 \qquad \lambda=c_V\alpha_4+\gamma_2/2.
\]
It preserves the failed-test factor of Bałaban (2.26).
Together with the determinant bounds, this proves the Gaussian estimates
used in (2.16)–(2.17) and (2.23)–(2.26), with
\(\alpha_5=O(\hat\varepsilon)+O(\alpha_4)+\gamma_2\), just as at
CA-I 8695–8718. Fine-coordinate dimensions convert to the account's
volume convention with the fixed bond/color multiplicity, or one factor
of \((LM)^4\) per \(LM\)-cube. The later cluster-expansion ceilings on
\((LM)^4\alpha_4,(LM)^4\gamma_2\) are retained; no resummation claim is
inferred merely from convergence of (26).

For instance the explicit early bounds
\[
 \delta\le(68K^6)^{-1},\qquad \lambda\le(16K^4)^{-1}
 \tag{38}
\]
imply \(Kh<1/2\) and \(v\le1/2\).
Choose \(\varepsilon_0^{P'}\le(68K^6C_P)^{-1}\), along with the
earlier bounds of §8. Choose the later free parameters \(\alpha_4,\gamma_2\)
below the bound on \(\lambda\) and their existing ceilings.
This respects the account's order. The first two floors give
\(\bar\eta,t_\rho\le\varepsilon_0^{P'}/3\); the last gives
\(\eta_{\rm sym}\le\varepsilon_0^{P'}/3\), since
\[
 4\mathsf B e^{-\theta\mathsf r^*/2}
 =4\mathsf B\,\frac{\varepsilon_0^{P'}}{12\mathsf B}
 =\varepsilon_0^{P'}/3.
\]
Thus (38) is delivered by the original floors after their expressly allowed
early threshold reduction. This proves (4b).

## 10. Local admission and analyticity: (4c)

The potentials in (35) already depend on the local datum on \(Y\subset Z_0\).
The exterior \(\sigma\)-interpolation acts on the three Gaussian operators;
it does not substitute a new \(\sigma\)-dependent background into these
potentials. This is explicit in CA-II 3600–3617. The fixed real cutoffs are
kept throughout. Where a potential is only defined for \(|B|<T\) on its
support, evaluate it on that support of the cutoff and set the integrand
to zero outside it. This makes a Borel integrand, with (36) as its
majorant, without requiring analyticity of a sharp cutoff.

Port the equal-level case of Theorem 4.8:thm-restriction-units,
CA-I 33276–33397. A representative on \(Z\) has a fixed decomposition
\(\mathbf U=U'U\). Restrict both factors and the current to \(Y'\subset Z\).
Every plaquette, bond and cube tested there is also tested in \(Z\);
the same gauge on each tested cube supplies its gauge bound.
At equal levels there is no change in lattice units or any radius.
For the hereditary clause, a label \((p,W)\) of
\(\mathfrak T_{k+1}(Y')\) satisfies
\(W\subset Y'\subset Z\), so belongs to \(\mathfrak T_{k+1}(Z)\).
It asks for the same restriction, rule and constant
\(a_0L^{-(k+1-p)}\). All these conditions are therefore inherited,
including the strict inequalities. This proves
\[
 \mathsf u|_{Y'}\in
 U^{\Sigma^1}_{k+1}
 (Y';(1+\beta)\alpha_0,(1+\beta)\alpha_1,\alpha_0)
 \tag{39}
\]
in the sense of representatives used in the proposition.
Restriction also commutes with the gauge action, so the assertion holds
on the specified classes of orbits. Neither simple connectivity nor an
extension to the full torus is involved.
For \(Y'\subset Z_0\), (39) is exactly the admission needed in (35).

On the finite lattice the set of parameter cubes is finite.
Each assigned walk coefficient is analytic in the readable datum and
each walk multiplier is a square-free monomial in the \(\sigma\)'s.
Absolute convergence from (4) permits grouping the walks by their set
of parameter cubes. There are finitely many such sets. Consequently
each \(K(\sigma;\mathsf u)\), for fixed \(\mathsf u\), is a polynomial
in \(\sigma\), with analytic local coefficients.
This also proves analyticity in a neighborhood of the closed polydisc,
not only termwise holomorphy in its interior.

Part (3) keeps \(C\) invertible there. The bounds in §§8–9 leave a strict
positive margin in both real integrations. The logarithmic determinant
branch for \(H_C\) is fixed by (25); the same estimates hold on a
neighborhood of the closed polydisc, by continuity and compactness.
For fixed admissible local data the integrand in (26), (35) is analytic
in \(\sigma\) on that neighborhood and has a uniform integrable
Gaussian majorant. To see the latter before integrating, complete the
real \(B\)-square in (29): \(D_B\ge(2K)^{-1}\),
\(I-D_X\ge I/2\), and
\(\|D_B^{-1}J\|\le4K^2\). The resulting triangular change of real
coordinates has bounded inverse, so the joint real quadratic form is
bounded below by a positive early multiple of \(|B|^2+|X|^2\).
Small enlargements of the parameter set retain half this margin.
Fubini and Morera now prove analyticity of each term, and hence of
the finite combination defining the actual \(f(\sigma)\).

At a vertex, the interpolation identity already proved at CA-I
5154–5194 gives \(K(1_{\sigma'};\mathsf u)=K^{W(\sigma')}(\mathsf u)\).
The integral just constructed therefore is the specified vertex
functional, including its original \(F\).
Its analyticity implies the \(C^1\) hypothesis on the real parameter
cube needed by Lemma 4.4:lem-vertex-formula.
All coefficients, potential arguments, and cutoffs have used only
\(\mathsf u|_Z\). This proves all of (4c).

## 11. Uses and scope of this proof

The literal label search in all three account files has occurrences only
in CA-I. Besides the target and its continued proofs, the occurrences are
in the cluster-base remark (8761–8837), the fixed-rule cluster remark
(9208–9353), and the localised-independence corollary (9615–9791).
The first two use the real comparison pair, the four perturbation
estimates, full-polydisc positivity and same-level admission.
The last uses the actual local vertex functional, not a replacement
Gaussian with a different interpolation. Sections 4–10 supply precisely
these properties for the assigned families.
The other walk operators inside previously formed local potentials retain
the consumer's separate (f1), (f4) inputs (CA-I 9762–9767).
This does not turn the exterior interpolation of (26) into a new nonlinear
background substitution.
The clause-(0) assembly subsequently invokes the localised-independence
corollary at CA-III 111058–111064. Its other premises remain in force.

Three possible shortcuts have been excluded in this proof: replacing the
resolvent interpolation by an inverse of an interpolated precision;
assuming every partial sum is real symmetric; and extending a local
datum globally before applying Cauchy's formula. None is needed.
The unprinted full symmetry-lemma statement is not reconstructed here:
we retain hypothesis (a) and port its explicitly stated symmetric-base
corollary and proof. This is an implication with the proposition's
premises, not a proof of those upstream premises or of T0.

Verification was by reading the cited arguments and the written
inequalities. No numerical run, symbolic computation, test suite, audit,
or independent review discharges a step here. The new text is only this
file; no prompt or status file is changed.
Proved here by Codex; not yet checked by another model.

## Result

**Proof**

Proposition 4.4:prop-local-real-base of the Sussman–Alpoge complete account,
CA-I 8110–8373, holds under its hypotheses (a)–(d) and its stated
Bałaban-(2.14) setting, for its preassigned local walk families and its
normalized Gaussian convention. All constants can be chosen in the
account's order, with the allowed threshold decrease made before \(M\).
Clauses (1), (2s), (2Γ) follow in §6; (2σ) and (2U) in §§4–5;
(3) in §7; and (4a), (4b), (4c) in §§8, 9, 10 respectively.
The actual vertex functional is analytic on a neighborhood of the closed
\(\sigma\)-polydisc at the stated local hereditary representatives,
without a global extension. This is a research proof of that conditional
proposition; it grants no retained or audit status.
