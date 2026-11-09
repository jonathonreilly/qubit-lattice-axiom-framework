# Repo search

The lead's `library/prior/repo-search-2026-11-08.md` records a five-ref search of main and PRs #10114, #10133, #10134, and #10141. Its closest hit is the TPI note: `pr/10141:R/library/tp1.md:71–88,342–358`, byte-identical to this checkout; it assumes the residual estimate and retains the terminal term. That is a consumer/assumption, not a proof of the present CL2 comparison. The digest also records related healed-restriction and collar-coordinate material, but not a proof of these four first tests. The row 611 task contains no separate “Repo prior work” block. I read the digest's TPI and healed-history entries, `t0-approach.md` R1/R7/R8/R9, and the TP1 import below. I found no direct prior proof of R7's age-use classification, the healed-collar lifetime/count, R8's coefficient dependence, or the CL2-to-PRES match. The PR snapshot adds no independent derivation.

`library/sa-index/README.md`, the matching rows in chunks 19, 20, and 24, and their neighboring rows identify RF17's age-weight obligation (outline lines 20600–20633), the RF30 count hypothesis (20947–21021), and the short-distance conditional-measure package (around 26182). These index entries are locators/status descriptions, not proof. I read the cited outline ranges 20348–20365, 20600–20635, 20935–20962, and 26180–26305. The CA-I 4.12–4.19 index README was read; no CA-I source range was needed for these YM4_1400 reading tasks. The supplied `/tmp/sa_ym4.tex`, `/tmp/sa_ca_I.tex`, and `/tmp/ym4_1400.tex` were already present, so I did not fetch them again.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of the texts read. This is a reading/index note only. It is not a proof, audit, or status grant.

Source key: `Y` = `/tmp/ym4_1400.tex`, commit `2bc0658f91d2d03ba44e20bf695067e0a56a2ed9`. `TP1` = this lane's `library/tp1.md`. Quoted ranges below were read directly. **NOT READ:** Y outside the ranges cited here; the complete outline and complete account outside the indexed/source excerpts identified above.

## 1. R7 (e)(i): RF17 and the age exponent

Y 83609–83623, the full RF17 load and bound (including the definition of the age weight):

> “A list contains regular families \(G^{(j)}\) with their own action counterterms and unpointed remainders \(H^{(j)}\). At the output radii \(\bar a_\iota\) its required load is
> \[
> \mathcal N(\mathfrak f)=\sum_{j=1}^k\omega_{k+1-j}\|G^{(j)}\|+\sum_{j\ {\rm aged}}[\bar a/a_j]^2\|H^{(j)}\|,\quad
> \omega_n=(n+1)^{3/2}L^{-\alpha_{\rm H}(n-1)},
> \]
> … The first, second and third terms pay respectively for the interaction beyond quadratic order, old-family differences, and failed Gaussian tests.”

The exact-exponent use is the displayed RF17 requirement: the old-family term is weighted by the stated \((n+1)^{3/2}L^{-\alpha_{\rm H}(n-1)}\). Y 83649–83655 then says:

> “Their general polynomial age factors do not automatically give the exact exponent \(3/2\) in \eqref{eq:flow-RF17}. One must either verify that sharper estimate or allocate a smaller positive exponential rate and prove the resulting comparison.”

Thus the text states an exact \(3/2\) in RF17, while explicitly allowing a replacement with a smaller positive exponential rate if the resulting comparison is proved. Whether any other downstream consumer requires the exact exponent rather than a summable age factor: **NOT STATED**. `rg -n 'RF17|flow-RF17' Y` found the defining equation at 83620 and this discussion at 83653; no other RF17 reference was found. The previous-outline index likewise classifies the exact age weight as a named obligation and says the cited general polynomial factors do not automatically supply it (outline 20625–20633).

## 2. R7 (e)(ii): storage, healing, redone layers, and the rim count

Definitions and count conventions:

- Y 78873–78884, label load:

  > “Put \(Z_j^+=((\Lambda_j^{\mathsf a})^c)^\sim\).”
  > “Every count is at its indicated level.”
  > “Older layers may have been redone; their counts are not a single present-day volume.”

- Y 83989–84001, field-count setup:

  > “For the field estimate fix an admitted label through \(k\), with layers \(\Gamma_n=\Omega_n\setminus\Omega_{n+1}\), \(\Omega_0=T_\ell\) and \(\Omega_{k+1}=\emptyset\).”
  > “Write \(\#_n(D)=\#(\mathbb T^{(n)}\cap D)\). This is a site count, equal to volume in level-\(n\) units when \(D\) is a union of those unit cubes. It is not a count of localization cells.”

- Y 62080–62094, label-region nesting:

  > “The regions are nested, \(T_\ell\supset\Omega_1\supset\Lambda_1\supset\dots\supset\Lambda_k\), with gaps of at least \(cM\check R_j\) in level-\(j\) units.”

- Y 84038–84040:

  > “\(\mathcal R_j\) consists of domains outside \(Z_j^+\), and \(Z_j^+\) is the stored large-field region enlarged by one cell layer.”

- Y 84108–84115, count:

  > “The needed geometrical count is \(\sum_j\#_j(Z_j^+)\le C\sum_n\#_n(\Gamma_n)\). It includes the stored collars of healed components, not just the re-done small-field regions. It is an actual window/history count and is not proved by a local Cauchy estimate.”

Rules stated for storage, healing, and lifetime:

- Y 62080–62094:

  > “The regions are nested, … with gaps of at least \(cM\check R_j\) in level-\(j\) units.”
  > “Each operation \(\mathbf R\) has stage sequences and prepared sequences … on which the backgrounds … are formed, and drop-outs keep nests.”
  > “In these sequences and nests the boxes are only unions of \(M\)-cubes, and the only lower bound on the gaps is one \(M\)-cube of the later level.”
  > “A history records every outcome: \(P_t\), \(Q_t\), \(R_t\), the collars and rims, and the outcomes inside \(\mathbf R\). It determines the label, the creations and the ages.”

- Y 62103–62121:

  > “We set \(t_\flat:=t-\mathsf N_t\).”
  > “The nest consists of increasing boxes in \(\Omega_l^c\cap X\). Each box is what remains of the large-field region of scale \(l\) after the stage that integrates the stored fields of level \(l-1\).”
  > “Healed (every test passed): \(\Omega_l,\Lambda_l,S_l\mapsto\Omega_l\cup X,\Lambda_l\cup X,S_l\setminus X\) for \(l\le t\), and \(X\) leaves the label.”
  > “Island … [has] \(X\subset Z_t\) remain … On it, \(\mathbf T'_t(X)\) is kept together with its variables, its measure and its factors.”
  > “Drop-out … \(X\) remains in \(Z_t\) and retains … the operations carried out up to that point.”
  > “A mark persists until a later healed component or island swallows it.”

- Y 62128–62136:

  > “Marks wait: a mark of level \(s\) lying inside a class component of level \(t\) satisfies \(s<t_\flat\). Hence standing marks that share a part are nested, their windows \((s_\flat,s]\) are disjoint, and at any one place and level at most one drop-out mark is active.”
  > “Finally, a term created at a moment \(\mu\) … retains permanently the space in which it was made.”
  > “\(Z_{[j,t]}\) is the union of all components that were healed or became islands at levels \(j,\dots,t\).”

- Y 62195–62197:

  > “The class of \(\mathbf R\) depends on the past: it depends on every object whose creation falls in the window \((t_\flat,t]\), or which carries a mark at a level in \([t_\flat,t)\).”
  > “The recursion is not monotone: a later region may cover a healed place once more.”
  > “Window lemma: no creation within the window of \(t\) has been healed.”
  > “Erasing clusters of healed components from a history yields a history with the same label.”

- Y 78723–78743:

  > “In a history over \(\bar H\) the healed components of the current level \(t\) form a compatible family \(\mathfrak X\). Restricting to a subfamily deletes the entire ancestral cluster of each omitted component.”
  > “Write \(\mathcal Y(\mathfrak X)\) for the domains, other than single collars, that contain at least one collar of a healed or second-class component … Here the collar is the whole enlargement \(C^\sim\). The single-collar terms are included in the component operations.”
  > “For \(Y\in\mathcal Y(\emptyset)\) let \(Y^{\mathfrak X}\) be \(Y\) together with each healed collar sharing a cube with \(Y\).”

**Containment or collars not shown by the label (quotes only):**

> “Erasing clusters of healed components from a history yields a history with the same label.” (Y 62197)

> “\(Z_j^+=((\Lambda_j^{\mathsf a})^c)^\sim\).” (Y 78873)

> “The needed geometrical count is \(\sum_j\#_j(Z_j^+)\le C\sum_n\#_n(\Gamma_n)\). It includes the stored collars of healed components, not just the re-done small-field regions.” (Y 84108–84115)

## 3. R8 (e): \(b_l^0\) and its background

Definition and RF10 statement, Y 83250–83321:

> “The localized Gaussian family is required to satisfy
> \[
> \Phi_l(V)=\sum_X\sum_{z\in X}N^{(l)}(X,P_V,z),\qquad |N^{(l)}|\le E_{\mathsf N}e^{-\delta_{\mathsf N}Md_l(X)},\qquad b(N^{(l)})=b_l^0.
> \]
> The constants depend only on \(L\). No coupling occurs in these terms. Nonwrapping terms agree on all common lifts, and their pointed totals are covariant under every unit lattice isometry.” (Y 83250–83264)

> “Input B3 requires, with the fixed momentum convention \((2\pi)^{-4}dq\),
> \[
> c_0=\frac{11N^2}{12\pi^2}\log L,\quad
> \left|\sum_{l=1}^k b_l^0-kc_0\right|\le c_2,\quad
> |b_{l+1}^0-b_l^0|\le C_\alpha L^{-\alpha l}\quad(0<\alpha<1).
> \]
> Thus \(b_l^0\to c_0\).” (Y 83305–83316)

Background statements, Y 83317–83500:

> “The numerical value in \eqref{eq:flow-RF10} requires the actual lattice trace calculation. It is not deduced by quoting a continuum perturbative coefficient.”

> “The one-loop calculation has three steps: compose the actual Gaussian integrals, compare their averaging constraints with a positive mass, and evaluate the massive lattice coefficient. The proofs below concern the constructed homogeneous physical background. The complex-current localization requirements in \eqref{eq:flow-RF9} remain separate.”

> “For such functionals the background substitution is required to preserve the coefficient.”

> “For the actual Gaussian densities, coefficient preservation is proved in \S\ref{abc:section}.”

> “The constrained Gaussian logarithms satisfy \(\Psi_k=\Phi_k+\Psi_{k-1}\circ p_k\) … Coefficient preservation then gives \(\sum_{l\le k}b_l^0=b[\Psi_k]\).”

> “On the admitted real critical backgrounds with nondegenerate physical Gaussians, \cref{pgg:physical-saddle} gives the representation … Here \(U=U_k(V)\) is the actual critical background, \(J=\nabla_{\rm fine}A(U)=J_{\eta_k}(U)\), and \(\mu=\nabla_{\rm block}(A\circ U_k)(V)\).” (Y 83364–83403)

The text calls the coefficient by level, \(b_l^0\), and gives the quoted homogeneous-background and actual-background statements. It does not state in these ranges that the coefficient varies with the history or torus. **NOT STATED:** an explicit sentence saying “depends only on level” or an explicit history/torus independence formula for \(b_l^0\).

## 4. R9 (e): CL2 beside TP1 import PRES

### CL2 and its stated data (Y 102741–102785)

> “Fix the exterior sigma-field of the run window, with value \(e\). The identity concerns that specified sigma-field and the resummed positive term. A finer history or interpolation resolution need not be positive or carry the same conditional measure.”

> “In an admitted real pivot chart write the raw logarithms as \(a=(p,u)\). Suppose the constraints \(q(p,u)=0\) have invertible \(D_pq\) and solution \(p=\varphi(u)\). If the original coordinate density is \(w(p,u)\), the constrained density is
> \[
> w(\varphi(u),u)|\det D_pq(\varphi(u),u)|^{-1}\,du.
> \]
> … The domain is the image of the actual integration set; a product window is an identity to establish.”

> “On a positive component the complete conditional density may be written
> \[
> d\nu_e(y)=Z_e^{-1}1_{D_e}(y)\exp\{-\tfrac12y^{\mathsf T}Q_ey-\ell_e^{\mathsf T}y+P_e(y)\}\,dy.
> \]
> The actual extraction rule fixes \(Q_e\). The complete \(P_e\) contains old activities, nonlinear action, coarea and Haar logarithms, boundary and stored terms, and healed-origin remainders. A factor outside this exponential is carried in every numerator, or absorbed where its logarithm exists. Zeros require a domain or a decomposition.”

> “The extraction rule, sigma-field, domain, normalizer and observable numerators all belong to the required identification.”

> “For the exact calculus below assume a bounded piecewise smooth domain and a density in \(C^1(\overline D)\), or in \(W^{1,1}(D)\) with the indicated integrable traces and integration-by-parts identity. All displayed force integrals are required to be integrable. A rectangle suffices. Unbounded domains require an exhaustion and justified boundary limits.”

CL2 displays the normalized density and its domain/normalizer. **NOT STATED:** a particular observable numerator (including a \(\operatorname{tr}(F^2)\) numerator) or an explicit integral formula defining \(Z_e\) in this CL2 passage. The text explicitly says numerator identification is required and that outside factors are carried in each numerator.

### TP1 import PRES in full (TP1 lines 103–117)

> “**PRES — SC1's exact formed-source identity.** At level \(k_1\) there is a positive unsourced law \(\mathbb P\) on retained histories, block fields and stored variables \(y\), and a holomorphic exponent
> \[
> Z(z)/Z(0)=\mathbb E_{\mathbb P}e^{\Phi(z;y)},\quad \Phi(0;y)=0,\quad
> \Phi=\Phi^{\rm pt}+\Phi^{\rm reg}+\Phi^{\rm live}+\Phi^{\rm far},
> \]
> with differentiation through the expectation valid twice near zero.
> Here \(Z\) is the Wilson partition function with source \(z_1f+z_2h\);
> \(\Phi^{\rm pt}=\sum_p\varphi_p(z_1f(x_p)+z_2h(x_p);y)\).
> The marginal on histories is exactly the law used in AG.
> **Outstanding:** [ref-73.md](ref-73.md) establishes an abstract transport identity; identifying its logarithm with this formed exponent, with the following bounds, remains an input.”

### Differences, field by field

| Field | CL2 passage | TP1 PRES |
|---|---|---|
| Conditioning | “exterior sigma-field of the run window, with value \(e\)” | No sigma-field is named. |
| Positive object | “resummed positive term” and “positive component” | “positive unsourced law \(\mathbb P\)” on histories, block fields, stored variables. |
| Variables | Pivot chart \((p,u)\), reduced variable \(y\) | Stored variable \(y\), plus histories and block fields. |
| Domain | “image of the actual integration set”; \(D_e\); bounded piecewise smooth or stated \(W^{1,1}\) condition | No \(D_e\) or integration domain stated. |
| Density/exponent | \(1_{D_e}\exp\{-\frac12y^TQ_ey-\ell_e^Ty+P_e(y)\}\,dy\) | \(e^{\Phi(z;y)}\), with \(\Phi=\Phi^{pt}+\Phi^{reg}+\Phi^{live}+\Phi^{far}\). |
| Numerator | Observable numerators are named as required; no observable formula is displayed. Outside factors are carried in every numerator. | Source numerator is \(Z(z)\), the Wilson partition function with source \(z_1f+z_2h\); no conditional observable numerator is displayed. |
| Normalizer | \(Z_e^{-1}\) in the conditional density; an explicit defining integral is **NOT STATED** in this passage. | \(Z(0)^{-1}\) on the left and expectation under \(\mathbb P\); \(\Phi(0;y)=0\). |
| Fixed quadratic/extraction | “The actual extraction rule fixes \(Q_e\).” | No \(Q_e\) or extraction rule appears in PRES. |
| Differentiation | Force integrability and domain regularity for later calculus | Differentiation through expectation valid twice near zero. |

## 5. R1 (e): proper-background geometry and history windows/collars

Geometry fixed before the proposition:

- Y 10511–10525:

  > “The regions \(\Omega_0\supset\cdots\supset\Omega_k\) are unions of the assigned aligned cubes of side \(\mathfrak M\xi_j\) … The separation condition is
  > \[
  > \operatorname{dist}_\infty(\Omega_j^c,\Omega_{j+1})>\rho\xi_j,\qquad \rho\ge C_{\rm geom}L.
  > \]
  > The number \(C_{\rm geom}\) is chosen large enough for the fixed one-step path neighborhoods and collars used below.”

- Y 14927–14945:

  > “Fix powers \(\mathfrak M,R_1,\rho\) of \(L\) with \(L\ge13\), \(\mathfrak M\ge\mathfrak m^{\rm s}\), \(R_1\ge L\), \(R_1\mathfrak M\ge L^2\rho\), and \(\rho\ge\mathfrak r^{\rm s}\). Every level-\(k\) coordinate circle has at least \(6\rho\) sites. The gap in \eqref{mb:separation} is greater than \(R_1\mathfrak M\xi_j\).”

- Y 35270–35273 and 35635–35643:

  > “Use \(L\ge13\), and the aligned separated geometry of \cref{mb:datum-descent-critical-ascent}; increase its floors below when choosing a fixed local regularity patch.”
  > “For the geometry fixed above there are \(a_0,a_1,C_B>0\), independent of depth and volume, with \(C_Ba_1<a_0\), such that every real mixed datum whose ordinary and mixed test holonomies are within \(\varepsilon\le a_1\) of one has a constrained-critical configuration …”

Rules stated for admissible histories, windows, and collars:

- Y 62080–62094:

  > “The regions are nested … with gaps of at least \(cM\check R_j\) in level-\(j\) units.”
  > “Each operation \(\mathbf R\) has stage sequences and prepared sequences … and drop-outs keep nests.”
  > “In these sequences and nests … the only lower bound on the gaps is one \(M\)-cube of the later level.”
  > “A smallness \(e^{-c\check R_j}\) from a separation is available only at regions produced by steps.”

- Y 62037 and 62048:

  > “The collar [is] the set of stored bonds whose distance from \(\Lambda_t\), measured in level-\(k\) units, is at most \(\varpi_T\).”
  > “The waiting collar is the set that keeps \(X\cap\Omega_{m_\flat}\) apart from the floor.”
  > “The collar of a component \(X\) means the enlarged component \(X^\sim\), that is, \(X\) together with one layer of \(M\)-cubes of its level.”

- Y 62103–62136, operation windows and marks:

  > “We set \(t_\flat:=t-\mathsf N_t\).” The operation prepares increasing nests for \(t_\flat<l\le t\), and a marked component is healed, an island, or a drop-out as quoted in section 2 above.
  > “Marks wait: a mark of level \(s\) lying inside a class component of level \(t\) satisfies \(s<t_\flat\). Hence standing marks that share a part are nested, their windows \((s_\flat,s]\) are disjoint, and at any one place and level at most one drop-out mark is active.”

- Y 62195–62197, locality and the window lemma:

  > “Two regions made of level-\(t\) cells that do not touch are separated by at least one cell. One cell exceeds the largest range of a bond test, of a pivot bond and of a collar.”
  > “The class of \(\mathbf R\) depends on every object whose creation falls in the window \((t_\flat,t]\), or which carries a mark at a level in \([t_\flat,t)\).”
  > “The recursion is not monotone: a later region may cover a healed place once more.”
  > “Window lemma: no creation within the window of \(t\) has been healed.”

- Y 63684–63705, class conditions:

  > “A component \(X\) of \(Z_k\) belongs to the class when” it is a single small component throughout \(k_\flat\le i\le k\); “for \(k_\flat<i\le k\), step \(i\) creates nothing in it, and it does not absorb a second component”; and “it has not been acted on by any operation whose level lies in \([k_\flat,k)\), the lower end point included.” The text names these conditions “single boxes,” “quiet,” and “quarantine.”

The displayed geometry gives the stated level-to-level gaps. The history passages separately state stage-window, non-touching, and collar-range rules. **NOT STATED:** a sentence in these quoted ranges asserting that every admissible history automatically satisfies the full `bgc:proper-background` separation hypothesis for regions of different birth levels.

**NOT READ:** Y outside the source ranges quoted above; outline ranges outside the locator excerpts above; CA-I source ranges (its bounded index was consulted, but no account passage was needed). No proofs or computer-assisted steps were performed.
