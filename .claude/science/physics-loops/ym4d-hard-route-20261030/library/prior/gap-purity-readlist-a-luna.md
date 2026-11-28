# Repo search

- The row 1694 brief contains no separate “Repo prior work” entries. The required lead digest, `library/prior/repo-search-2026-11-08.md`, is a full search for earlier PI, GW, M3, TPI and GEOH targets. It reports exact snapshot copies and older soft-route analogues. Those are not this Wilson-purity literature-reading target. Its stated boundary excludes the target lane and does not search purity campaign rows.
- This checkout is at `49b21cf18c4a6d329cfbb452f27aca2f23e53bf7`. `FINISH.md` row 1694 assigns this six-paper reading task. Row 1682 and `library/gap-purity-crux-card.md` define the shared target. `library/open-registry.md` has related purity entries R11, R12 and TWO-PER (lines 1018–1020), with other row owners. They address candidate gap inputs, not these six citations or their attached questions. No open-registry row owns this literature-reading task. I will keep those distinct.
- Current hit from the local record: row 1682 says the card's seed is (PUR-io), a neutral-sector transfer-matrix purity bound for SU(2) Wilson theory. It requires a uniform-in-cutoff estimate at fixed physical size beyond the account's range, selective against weak 4D compact U(1), and new relative to the seed. Row 1682 section 4.4 asks six external-literature questions. The registry's related seed routes do not answer those source-specific questions.

## Source and index checks

- The full-read SA index says chunk 02 covers the one-bond transfer calculation. Its rows 88–93 give GL3 at outline lines 2210–2231: the SU(2) Wilson convolution eigenvalues are positive Bessel coefficients, and their ratios are part of the transfer setup. The adjacent rows classify the calculation as proved in detail in the outline. I read the cited outline source lines 2197–2257. In particular, \(c_l=2e^{-\beta}I_{2l+1}(\beta)/\beta\), so \(c_l/c_0=I_{2l+1}(\beta)/I_1(\beta)\). This confirms the SU(2) side of item 1's comparison.
- Searching the SA chunk files and obligations for the six first authors and named subjects found only the chunk-02 Bessel and Wilson convolution rows above. The CA-I 4.12–4.19 index was searched for the six authors and those subjects; it has no matching entry. Its indexed domain is the reblocking/flow range CA-I 42670–56650, not a result for these six papers.
- I created the download directory /tmp/sa-gap-purity-readlist-a-luna.745Z2O. It contains the two required Sussman–Alpoge source downloads. It also contains separate folders for each paper. These are scratch files only. Nothing was downloaded into the repository or committed.
- The PDF text extractor is unavailable. I extracted local PDF text with pypdf. The full texts of items 4–6 were read. Publisher/bot controls blocked items 1–3. I did not bypass them. Their results below are marked as provisional where the primary paper could not be read in full.

## 1. Hartman and Watson: Bessel ratio as a Laplace transform

**Citation.** Philip Hartman and Geoffrey S. Watson, “’Normal’ distribution functions on spheres and the modified Bessel functions,” *The Annals of Probability* 2 (1974), no. 4, 593–607, DOI [10.1214/aop/1176996606](https://doi.org/10.1214/aop/1176996606). The row citation has the right authors, title, year, journal, volume and pages. I add the issue, full given names and DOI.

**Access.** The journal PDF request returned an Incapsula bot-check page. So I did not read the paper in full. The result below is provisional. The paper citation is verified from the DOI record and the indexed bibliography, but I cannot give an internally verified theorem number or exact page for the transform.

**Answer to 4.4 question 1 (provisional).** The Hartman–Watson transform gives a probability law on \(s>0\) with Laplace transform \(I_{\sqrt{2z}}(\beta)/I_0(\beta)\). Exponentially tilt that law by \(e^{-s/2}\) and normalize it. The result has transform

\[
\int e^{-\lambda s}\,\eta_\beta(ds)=\frac{I_{\sqrt{1+\lambda}}(\beta)}{I_1(\beta)},\qquad \lambda\geq0.
\]

Thus the proposed map is a Laplace transform of a probability measure for every \(\beta>0\). Its support is \((0,\infty)\), with support closure \([0,\infty)\). Differentiating at zero gives

\[
\mathbb E_{\eta_\beta}[s]= -\frac12\left.\partial_\nu \log I_\nu(\beta)\right|_{\nu=1}.
\]

This mean is finite and positive. The original article's exact density and support claims need confirmation from its blocked full text.

**Use for (PUR-io): UNLIKELY.** It represents a single-link spectral coefficient as an average of heat coefficients. It may help the heat-kernel comparison in section 4.3, Component 1(a). The same modified Bessel structure occurs for the compact U(1) one-link kernel: its Fourier weights are \(I_n(\beta)/I_0(\beta)\), with integer Laplacian modes \(n^2\). The transform method therefore works in the Abelian model too. It gives no fixed-physical-box purity estimate and no SU(2)-specific gap.

**Repository first-author search.** Hartman occurs in the strategy file and several unrelated gap notes. No library/prior file records a full read of Hartman and Watson. The current read was incomplete because the PDF was blocked. Hartman also occurs in SA-index chunk 02 only as the Bessel topic context; the outline source itself supplies the normalized SU(2) coefficient stated above.

## 2. Kent: infinite divisibility of von Mises–Fisher laws

**Citation.** John T. Kent, “The infinite divisibility of the von Mises-Fisher distribution for all values of the parameter in all dimensions,” *Proceedings of the London Mathematical Society* (3) 35 (1977), no. 2, 359–384, DOI [10.1112/plms/s3-35.2.359](https://doi.org/10.1112/plms/s3-35.2.359). The row citation's page range was marked unverified; it is correct. The first initial is J. T., and I add the issue and DOI.

**Access.** Wiley returned HTTP 403 for its PDF endpoint. The primary article was not read in full. The journal record verifies the citation and the paper's title and scope. The mathematical answer below is provisional.

**Answer to 4.4 question 2 (provisional).** The title and journal record state infinite divisibility for every concentration parameter and every sphere dimension, which includes the 3-sphere. Since \(S^3\) is the underlying manifold of \(SU(2)\), the centered isotropic laws are candidates for central \(SU(2)\) convolution. The exact identification of Kent's spherical convolution with group convolution needs the full paper's definitions, which I could not inspect. Even if that identification holds, infinite divisibility means each fixed-\(\beta\) law has convolution roots. It does not prove that the laws at two different \(\beta\) values are ordered by convolution. A parameterized convolution semigroup is a stronger claim.

**Use for (PUR-io): UNLIKELY.** A convolution root representation may give another description of the transfer kernel. It does not compare the neutral-sector purity at different couplings. The circle \(S^1=U(1)\) is also within the all-dimensions title, so infinite divisibility is not selective against compact U(1). No sign or fixed-box purity bound follows.

**Repository first-author search.** Kent occurs in the strategy file and two gap notes. No library/prior entry records a full read of this paper. The current read was blocked by the publisher. The SA index has no Kent entry.

## 3. Araki: trace inequality

**Citation.** Huzihiro Araki, “On an inequality of Lieb and Thirring,” *Letters in Mathematical Physics* 19 (1990), no. 2, 167–170, DOI [10.1007/BF01045887](https://doi.org/10.1007/BF01045887). The title, author, year, journal, volume, issue and pages in row 1682 are correct. I add the issue and DOI.

**Access.** The Springer PDF was blocked. A prior literature note, library/prior/gap-lit-transport.md, also records that the publisher exposes only the abstract and requires a subscription for the PDF. I did not pay or try to bypass the block. The source-specific answer below is provisional; I did not read the article in full.

**Answer to 4.4 question 3 (provisional).** The standard Araki–Lieb–Thirring trace inequality, in the form used by section 4.3, is for positive operators. For \(A,B\geq0\), \(r\geq1\), and \(q>0\), it compares
\[
\operatorname{Tr}(B^{1/2}AB^{1/2})^{rq}
\leq
\operatorname{Tr}(B^{r/2}A^rB^{r/2})^q .
\]
Putting \(A=e^{-sC/n}\), \(B=e^{-V/n}\), \(r=n/m\geq1\), and \(q=m\) compares the \(n\)-step trace with the \(m\)-step trace for integers \(n\geq m\). It gives the Component 1(c) monotone chain. The Trotter limit gives a lower comparison with the continuous-time trace. If the gauge projection and neutral projection commute with the positive factors, their ranges reduce the operators, and the same inequality holds on those ranges. If a projection remains inserted between noncommuting factors, this substitution is not justified without another argument. The trace inequality can compare traces; it does not compare their ratio \(D(u)\), which defines purity. A ratio of two quantities that each decrease need not decrease.

**Use for (PUR-io): UNLIKELY.** With common reducing projections and trace-class products, ALT supplies the monotone trace comparison in Component 1(c). The Wilson transfer construction in the outline has the needed gauge-invariant context, but the 4.3 proposal still needs to check the actual common reducing spaces and trace domains. Even if it does, the inequality is generic and the purity ratio is uncontrolled. The same positive-operator inequality applies to compact U(1), so it gives no Abelian exclusion.

**Repository first-author search.** Araki occurs in the strategy file and library/prior/gap-lit-transport.md. The prior note says the 1990 article was not read in full. It found generic ALT mentions, but no full statement or Wilson transfer application. The current source was also blocked; this row adds no primary-source read. The SA index has no matching Araki item.

## 4. Ozawa: order units and sums of squares

**Citation.** Narutaka Ozawa, “Noncommutative real algebraic geometry of Kazhdan’s property (T),” *Journal of the Institute of Mathematics of Jussieu* 15 (2016), no. 1, 85–90, DOI [10.1017/S1474748014000309](https://doi.org/10.1017/S1474748014000309). The row citation is correct; the journal record also gives the online publication date as 2014. The print year remains 2016.

**Full text read.** I read the six-page arXiv version, arXiv:1312.5431v3 (2015), which matches the journal text. It states the main theorem and proves Lemmas 2–3 and Proposition 4.

**Answer to 4.4 question 4.** The key “order unit” is the Laplacian \(\Delta_\mu\) in the augmentation ideal \(I[\Gamma]\), not an arbitrary positive operator. Lemma 2 (arXiv pp. 4–5; journal pp. 88–89) proves it is an order unit because the support of the symmetric generating measure controls \((1-x)^*(1-x)\) for each support element, and
\[
(1-xy)^*(1-xy)\leq2(1-x)^*(1-x)+2(1-y)^*(1-y)
\]
extends control from generators to every group element. The main theorem then gives a finite exact sum-of-squares witness for \(\Delta_\mu^2-\kappa\Delta_\mu\). Its rational version gives rational coefficients when the measure and gap are rational and the spectral gap is strict.

The proposed Lemma OU captures one useful operator consequence for block projections. Its displayed identity and anticommutator row-sum bound imply \(H^2\geq(\gamma-\rho)H\). This proves a spectral gap for \(H=\sum Q_x\) when \(\gamma>\rho\). It does not capture all of Ozawa's result. It does not make \(H\) an order unit in an augmentation ideal, prove an exact group-ring sum-of-squares identity, or supply the required decomposition for the YM transfer operator. Its hypotheses must still be built for the actual block conditional expectations.

**Use for (PUR-io): UNLIKELY.** Lemma OU can certify a finite block gap if its exact algebraic identity is found. It does not carry the bound to increasing cutoffs or fixed physical size. The projection inequality is also group-blind. For compact U(1), the abstract projection lemma remains valid. The theorem's group-property-(T) premise does not apply to the infinite compact Abelian gauge group, and the weak-coupling photon is massless.

**Repository first-author search.** Ozawa occurs in the strategy file. No prior file records a full read of this article. This lane read it in full. The SA index has no Ozawa entry.

## 5. Kaluba, Kielak and Nowak: property (T) for Aut(F_n) and SL_n(Z)

**Citation.** Marek Kaluba, Dawid Kielak and Piotr W. Nowak, “On property (T) for Aut(\(F_n\)) and SL\(_n(\mathbb Z)\),” *Annals of Mathematics* (2) 193 (2021), no. 2, 539–562, DOI [10.4007/annals.2021.193.2.3](https://doi.org/10.4007/annals.2021.193.2.3); arXiv:1812.03456. The row citation is correct. I add the issue, DOI and preprint identifier.

**Full text read.** I read the 24-page arXiv v2 text. The paper contains Theorem 1 and Sections 2–5, including its sum-of-squares construction and proofs.

**Answer to 4.4 question 5.** The lift uses more than disjoint-support commutation. Section 3 defines the family \(G_n\), alternating-group actions, equivariant inclusions \(G_n\hookrightarrow G_{n+1}\), and edge labels for generators. Opposite edges label commuting generators (pp. 5–6). Lemma 3.6 uses that commutation to write the opposite-edge term \(Op_n\) as a sum of squares (p. 8). The lift then uses the alternating-group orbit counts in Lemmas 3.7–3.8 and Proposition 4.1 to transfer a finite certificate from \(n\) to larger \(n\) (pp. 9–11). For \(SAut(F_n)\), Theorem 5.9 uses the \(n=5\) certificate to reach \(n\geq7\), and a separate induction handles \(n=6\) (pp. 18–19).

This has a Knabe-like local-to-global shape, but it is not only the disjoint commutation relation. The orbit symmetry, nested group family and a base sum-of-squares certificate are also essential. The proof states an abstract set of sufficient structural assumptions. It does not invoke an additional hidden relation beyond those assumptions in the lift. The base certificate itself is group-specific.

**Use for (PUR-io): NO.** This is a group-ring spectral-gap certificate for groups of automorphisms and special linear groups. It does not give a Wilson transfer estimate on a fixed physical box. The lifting mechanism is not selective for SU(2) gauge theory. Compact U(1) is Abelian, so disjoint local generators commute there too; that fact does not create the missing mass gap. Weak 4D compact U(1) has massless photons.

**Repository first-author search.** Kaluba occurs in the strategy file only. No library/prior file records a previous full read. This lane read the full text. The SA index has no Kaluba entry.

## 6. Gowers, Green, Manners and Tao: Marton's conjecture

**Citation.** W. T. Gowers, Ben Green, Freddie Manners and Terence Tao, “On a conjecture of Marton,” arXiv:2311.05762v2 (12 December 2023), 33 pages. The row citation's authors, title and identifier are correct. The version read states the polynomial Freiman–Ruzsa theorem in characteristic 2. Its bibliography still lists the odd-characteristic extension as a manuscript, so I do not cite that extension as a published result.

**Full text read.** I read all 33 pages of arXiv v2, including the proof of Theorem 1.8, Proposition 2.1, the fibring lemma and its appendices.

**Answer to 4.4 question 6.** Proposition 4.1 (p. 15, equation (4.1)) gives the fibring identity. For independent \(Z_1,Z_2\) in an abelian group and a homomorphism \(\pi:H\to H'\),
\[
d[Z_1;Z_2]
=
d[\pi Z_1;\pi Z_2]
+d[Z_1\mid\pi Z_1;Z_2\mid\pi Z_2]
+I[Z_1-Z_2:(\pi Z_1,\pi Z_2)\mid\pi(Z_1-Z_2)].
\]
The last term is a nonnegative conditional mutual information. Corollary 4.2 (p. 16) is the four-variable identity used in the proof.

The strict descent is Proposition 2.1 (p. 6, equation (2.2)): if \(d[X_1;X_2]>0\), the authors construct \(X'_1,X'_2\) with \(\tau[X'_1;X'_2]<\tau[X_1;X_2]\). The fibring identity alone does not give this strict inequality. The proof also needs several entropy bounds, an entropic Balog–Szemerédi–Gowers lemma, and the characteristic-2 endgame. Equation (7.4) uses \(U+V+W=0\); Lemma 7.2 and the estimates on pp. 22–25 close the descent. This does not produce an analogue of the strategy file's symmetric size defect \(\delta_{ij}\). That defect concerns thermal sizes and scale doublings, which do not occur in the paper.

**Use for (PUR-io): NO.** The theorem concerns entropy of random variables on \(\mathbb F_2^n\), not SU(2) transfer spectra or Wilson measures. Its exact fibring identity is an abstract abelian-group identity, but the strict descent uses the finite characteristic-2 structure. Compact U(1) is not a group of exponent two. The proof supplies no signed Wilson estimate and no fixed-box purity bound. The identity itself is not selective against compact U(1).

**Repository first-author search.** Gowers occurs in the strategy file only. No library/prior file records a previous full read. This lane read the full text. The SA index has no Gowers entry.

## Result

This reading found no literature result that supplies a new (PUR-io) estimate. The Hartman–Watson transform and Kent's divisibility are group-blind one-link representations. ALT can compare projected traces under common reducing-subspace hypotheses, but it does not control their purity ratio. Ozawa and Kaluba–Kielak–Nowak give algebraic spectral-gap methods for different operators and group families. Gowers–Green–Manners–Tao prove an entropy descent on finite characteristic-2 groups. None gives the fixed-physical-size Wilson SU(2) estimate or distinguishes it from weak compact U(1).

Items 1–3 remain provisional because their primary PDFs were blocked. Item 1's formula follows from the Hartman–Watson transform and a tilt, but its original theorem/page and density were not checked. Item 2's exact spherical-convolution convention was not checked. Item 3's original theorem statement was not checked. No proof was written, no computation was run, and this reading makes no status claim.

Credit for the SA outline and account belongs to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. No statement above upgrades their status or grants scientific or audit status.

