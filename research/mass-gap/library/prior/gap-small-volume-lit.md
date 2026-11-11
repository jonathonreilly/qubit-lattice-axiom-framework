# Small-volume finite-volume spectrum and coupling literature

## Repo search

The lead's row-729 instruction says `origin/main` and open YM4D PR branches were searched before queuing. The task gives no “Repo prior work” paths to open, so I cannot enumerate the lead's branch hits. The existing `library/prior/repo-search-2026-11-08.md` is for row 531, and reports soft-route and posted-note hits. It has no small-volume spectrum or coupling result. In this checkout I found no completed `gap-small-volume-lit.md`; `library/open-registry.md` has no owner for this reading item.

The closest source is `library/gap-phys-seed.md` §§1.2 and 2.2. It marks the periodic-box values as recalled from van Baal's review and says the primary papers were unread. `library/prior/gap-seed-lit.md` entries on Lüscher and van Baal give a bibliographic lead and say the Lüscher article was not obtained; its van Baal reading covered §§1 and 7. `library/prior/gap-fullread-1.md` concerns unrelated source topics. These hits are orientation or recalled claims, not full-text work on the assigned scope. This note supplies page-based literature findings. It proves no new physics statement.

The Sussman–Alpoge outline index has no entry for these finite-volume papers or the twisted Polyakov coupling. I searched its outline chunks, `obligations.md`, and the CA-I 4.12–4.19 index. The outline's nearby mass-gap rows say a positive gap needs a spectral-support exclusion (lines 588–599 and 31871–31882). I checked those source lines. CA-I says its Theorem 0 does not assert a mass gap (lines 2706–2713). The five papers below concern finite-volume calculations and coupling definitions. They do not close that separate gap question. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.

**Provenance:** written by Codex, gpt-6-luna high, on checkout `ee962db5bfa8d69490f6973818aac2e17df49b67`. Research note; no audit or status is granted.

**Read in full:** van Baal (2000), §§2–4 (printed pp. 9–50); de Divitiis et al. (1994), entire article (pp. 1–17, including appendices). **Not read in full:** Lüscher (1983), Lüscher–Münster (1984), Koller–van Baal (1988). No lawful open full text was obtained for the first two papers. For Koller–van Baal, an author-hosted PostScript was obtained but could not be converted with installed tools. See each source entry for the exact limit. I did not bypass a TLS failure or a publisher access request.

## Source status and findings

### Lüscher, Nucl. Phys. B219 (1983) 233

**Read status: NOT READ (pp. 233–261).** The located third-party mirror failed TLS verification because its certificate had expired. I did not bypass TLS. The publisher page offers purchase access. No lawful open copy was obtained. Its publisher abstract says the paper develops a one-loop method for periodic-box energy expansions and gives no low-level numbers. This is only an abstract, not a reading of the article pages.

### Lüscher and Münster, Nucl. Phys. B232 (1984) 445

**Read status: NOT READ (pp. 445–472).** ScienceDirect exposes the abstract and asks for institutional sign-in to view the full text. No sign-in was attempted. The abstract says the authors complete a one-loop computation for SU(2) in an $L^3$ periodic box and judge the crossover likely near $z\simeq2$. I found no author or institutional copy during this task. This is only an abstract, not a reading of the article pages.

### Koller and van Baal, Nucl. Phys. B302 (1988) 1

**Read status: NOT READ (pp. 1–64).** The author-hosted corrected PostScript copy and table supplement were downloaded to `/Users/jonBridger/ym4d-papers/dl-2026-11-11/koller-vanbaal-1988/`. This machine has no PostScript-to-PDF converter. `cupsfilter` has no PostScript filter, and Homebrew could not install Ghostscript because `/opt/homebrew` is not writable. I did not change system permissions. I rely only on van Baal's review when I describe this work.

### van Baal, hep-ph/0008206, §§2–4

**Read status: READ IN FULL for the requested scope.** The complete §§2–4 (printed pp. 9–50) were read from the arXiv PDF in `/Users/jonBridger/ym4d-papers/dl-2026-11-11/van-baal-2000/`. Table 1 on p. 33 was checked against the rendered PDF page.

### de Divitiis, Frezzotti, Guagnelli, and Petronzio, Nucl. Phys. B422 (1994) 382

**Read status: READ IN FULL.** The entire article, pp. 1–17, was read from the arXiv PDF in `/Users/jonBridger/ym4d-papers/dl-2026-11-11/de-divitiis-et-al-1994/`. Pages 18–19 contain figures only. The article itself identifies its one-loop diagram and lattice-position sums as algebraic-program and numerical-program computations; I report those as the authors' calculations, not hand proofs.


## Periodic box: what is proved and what is computed

**Lüscher (1983), article pages NOT READ.** The publisher abstract alone says that periodic-box Hamiltonian eigenvalues have a power-series expansion in $g^{2/3}$ and that the paper works out a method through one loop. It says no numbers for the low levels are given. Since pp. 233–261 were not available as a lawful open full text, I do not attribute a detailed proof or hypothesis to a particular page of that article.

**Effective Hamiltonian, as reported in van Baal's review.** In §2, pp. 9–10, the nine spatially constant SU(2) modes are parametrized by $c_i^a$. The review gives the effective Hamiltonian in equation (9), with its derivative and quartic classical-potential terms followed by loop corrections. The leading two terms have energy scale $g^{2/3}/L$ after rescaling $c$ by $g^{2/3}$. It says Bloch-degenerate perturbation theory gives a rigorous framework for integrating out nonzero momentum modes (p. 9). It also says Lüscher computed terms through order $g^{8/3}$ (p. 10). This is a weak-coupling expansion, not an all-volume Hamiltonian theorem.

The review's §2, pp. 12–13, imposes field-space boundary conditions in equation (13) for the gauge and electric-flux identifications. It says the low levels are obtained by computing matrix elements of the effective Hamiltonian and solving by Rayleigh–Ritz; it notes that the second moment gives lower bounds (p. 13). Thus the effective operator and its perturbative framework are derived, while its displayed low-level values are spectral computations. The review presents the decimal eigenvalues as computed values, not exact symbolic eigenvalues.

**The scalar coefficient $\epsilon_1$.** Equation (12), p. 11, gives $\epsilon_1=4.116719735$ and $m_0=L^{-1}\epsilon_1g^{2/3}(L)$ to lowest order. The review says this value was already computed by Lüscher and Münster. It also says $\epsilon_1$ and the wave-function coefficient $B=0.206$ can be computed from the leading effective Hamiltonian by setting the $\alpha_i$ and $\gamma_i$ corrections to zero. The decimal $\epsilon_1$ is a computed spectral value. I did not read Lüscher–Münster's article pages, so its own derivation, numerical error and exact theorem status are **NOT READ**.

**Periodic electric-flux splitting.** The review calls the derivation of the flux energy a challenge and says the Path Decomposition Expansion supplies a rigorous framework for the semiclassical calculation (p. 11). Equation (12) there states

$$
\Delta E=2L^{-1}\lambda B^2g^{5/3}(L)\exp\!\left[-S/g(L)+\epsilon_1T/g^{2/3}(L)\right]\{1+f(g(L))\},
$$

for the one-unit flux energy $E_0(e)-E_0(0)$. The review gives $S=12.4637$, $T=3.9186$, $\lambda=0.6997$, $B=0.206$, and says $f(g)=O(g)$ was shown (p. 11). The asymptotic tunnelling form and its stated remainder are the analytic result as characterized by this review. Its decimal constants and $\epsilon_1$ are computed inputs. It is a small-coupling asymptotic formula, not a finite-coupling estimate valid at arbitrary $L$.

## Volume ranges quoted by the review

For the periodic box, the review says field-space boundary identifications begin to affect low-lying glueball states once $z=m_0L>0.9$ (§2, p. 12). It also calls the Lüscher–Münster curves below $z=0.95$ insensitive to those identifications (p. 17). The Lüscher–Münster abstract reports a likely small-to-large-volume crossover near $z\simeq2$; that article's pp. 445–472 are **NOT READ**, so this is an abstract report only.

Koller and van Baal's intermediate-volume treatment is summarized in §2, pp. 14–18. The review compares the low states with the sphaleron barrier and says instanton effects become important at $z_0$ around 5–6 (p. 15). It cautions that $z$ should not be much larger than $2\pi$, the scale of the integrated-out nonzero modes (p. 15). It reports lattice agreement up to about 0.75 fm for the regime where the zero-momentum Hamiltonian should work (p. 18). These are ranges estimated from the barrier and comparison data, not a uniform theorem in $z$. The Koller–van Baal article itself (pp. 1–64) is **NOT READ**.

The review describes the crossover itself as likely near $z\simeq2$ (citing Lüscher–Münster) and the wider zero-momentum effective-Hamiltonian description as useful until instanton effects turn on around $z_0=5$–6. These statements concern different approximations and do not give a sharp common boundary between phases.

## Twisted box: one-loop spectrum

For SU(2) with magnetic twist $m=(1,1,1)$, §3.4, p. 33, equation (44) gives

$$
z_r=m_rL=2\sqrt2\pi+\frac{g^2(L)\gamma_r}{16\pi^2},\qquad
z_{e_n}=E_{e_n}L=\sqrt2\pi+\frac{g^2(L)\gamma_{e_n}}{16\pi^2}\quad(n\ne3).
$$

Table 1 on p. 33 lists these one-loop coefficients $\gamma$. I checked the rendered table against the PDF:

| State | $\gamma$ | State | $\gamma$ |
|---|---:|---|---:|
| $A_1^+$ | -92.08 | $T_1^+$ | 14.74 |
| $A_1^-$ | -91.93 | $A_1^+$ (next listed level) | 25.56 |
| $T_2^+$ | -41.26 | $E^-$ | 36.07 |
| $E^+$ | -22.90 | $E^+$ (next listed level) | 36.38 |
| $T_2^+$ | -7.39 | $e$ | -5.43 |
| $T_2^+$ | -6.59 | $e_2$ | -1.16 |
| $T_2^+$ | 7.53 |  |  |

The repeated cubic labels are repeated levels as printed; the table does not give additional labels for them. The review explicitly says $z_0$ decreases with increasing volume in this perturbative regime. It must turn around when the mass stabilizes and $z_0$ grows linearly with $L$ (p. 33). This is a computed one-loop trend, not a proved monotonicity theorem for all volumes. The review reports twisted and periodic results becoming indistinguishable for $z_0>6$ in Monte Carlo data (p. 34), and says the transition to large volume starts around 0.75 fm for the plotted flux data (p. 34).

## Twisted Polyakov-loop and Schrödinger-functional couplings

Van Baal's §3.3, pp. 27–29, describes the Schrödinger-functional (SF) coupling as the response to a constant chromoelectric background with prescribed initial and final gauge fields. It reports that this coupling agrees very well with perturbative running through the largest volume then probed, about $L=0.35$ fm. It then states that nonperturbative running must deviate from perturbation theory at large volume (p. 28). This is an expectation about running, not a theorem bounding the SF coupling between two boxes.

The review describes the twisted Polyakov (TP) coupling as a ratio of Polyakov-loop expectation values with twisted boundary conditions. It reports agreement with perturbation theory and, after scale matching, with the SF coupling. Its largest reported volume, $L=0.28$ fm, lies slightly but significantly below the perturbative result (pp. 28–29). The review does not supply a large-$L$ theorem for the TP coupling or an inequality comparing its values at $L$ and $2L$.

De Divitiis, Frezzotti, Guagnelli and Petronzio, pp. 1–6, define the SU(2) TP coupling from a twisted-to-untwisted Polyakov-loop correlation ratio at separation $L/2$ (equation (10), p. 5), then set $O(L)=T(L)g^2(L)$ (equation (11), p. 6). Their paper presents the one-loop conversion to standard schemes. Its stated purpose includes finite-size step scaling from a smaller box to a doubled box (pp. 2–3), but it does not compute or prove a nonperturbative large-box step-scaling inequality. Its one-loop calculation, equations (25)–(28), gives $\Lambda_{TP}/\Lambda_{MS}=1.6136(2)$ (p. 11). The reported coefficient is fitted using numerical sums over lattice sizes; the authors state that they used FORM and a numerical FORTRAN program (pp. 7–10). This is a perturbative scheme-matching computation.

## Relation to the Sussman–Alpoge outline and account

The indexed outline rows at lines 588–599 give an explicit positive spectral measure with polynomially decaying correlations whose support reaches zero. Lines 31871–31882 state that a gap needs an interval of spectral support excluded above the vacuum. The complete account at CA-I lines 2706–2713 likewise lists a mass gap among the statements its Theorem 0 does not assert. The CA-I index for items 4.12–4.19 contains no small-volume spectrum, periodic-box effective Hamiltonian, twisted TP coupling or flux-splitting result. These texts do not establish the infinite-volume mass gap.

Credit the finite-volume results to Martin Lüscher; Martin Lüscher and Gernot Münster; Jeffrey Koller and Pierre van Baal; and Pierre van Baal, as applicable above. Credit the TP-coupling definition and calculation to G. M. de Divitiis, R. Frezzotti, M. Guagnelli and R. Petronzio. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the outline and complete account.

**RESULT:** the previously recalled small-volume numbers and coupling summaries are now located in the read portions of van Baal's review and the full de Divitiis et al. article. The three named older journal articles remain **NOT READ** beyond their accessible abstracts or the review's account. This is a literature report, not a proof or status change.
