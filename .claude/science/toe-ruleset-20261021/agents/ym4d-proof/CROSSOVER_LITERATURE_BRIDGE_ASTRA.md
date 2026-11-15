# Crossover literature bridge: Gaussian normalization and the Kirk v4 handoff

Date: 2026-10-29. Author-side literature/check unit; no independent audit verdict.

| Field | Value |
|---|---|
| Target | Full Wilson continuum existence **and** a gap in the physical continuum Hilbert space |
| Target status / claim type | `open` / `open_gate` |
| Result of this unit | Exact finite-dimensional normalization calculation; bounded replacement lemma; scoped import-screen finding |
| Negative-result scope | `partial-narrowing`; no whole-paper rejection, route impossibility, or negative-route packet PASS |
| Source under examination | Harold D. Kirk, version 4, 2 August 2026, [Zenodo record 21765806](https://zenodo.org/records/21765806) |
| Source PDF SHA-256 | `b91c6c2b9ba7cd4d5476aa6a2e823569507682c24cf103933ff9f97c73260bed` |
| Methodology pin | current-main `ca2bc7ddf64790da96cd43d42017d000fbfe4808`, supplied by the parent researcher |

The checked conclusion is narrow but consequential: the block **operator**-norm hypothesis printed in Kirk Lemma 3.26 does not imply its displayed, core-size-independent determinant bound. An exact two-core Gaussian family retains all normalizers and makes the omitted rank factor explicit. This is upstream of the claimed all-exterior irregular estimate and the joint Haar/optical forest admission. Accordingly, the selected proof chain does not presently furnish a checked continuum producer for this lane. It remains possible to repair that chain by a different, size-aware expansion. Nothing here proves that the Wilson continuum theory or its physical mass gap fails to exist.

The useful positive output is a dimension-aware Gaussian normalization lemma, together with a concrete original-literature organization that could make its extensive cost payable. The elementary compact-Haar pivot calculation also survives intact. These results do not close any row of [MASS_GAP_TARGET.md](MASS_GAP_TARGET.md).

## Scope, criteria, and source coverage

The criteria in [checks/crossover_import_criteria.md](checks/crossover_import_criteria.md) were frozen before the computational diagnostic, after observing the possible rank omission analytically; this is not a blinded test. The exact source/read manifest is [checks/crossover_import_manifest.json](checks/crossover_import_manifest.json). The previous review's register and manifest were consulted as leads, not as a substitute for the present source reading. Full third-party PDFs and extracted texts remain in `/tmp`; the publication unit contains URLs, hashes, original calculations, and concise analysis.

For Kirk, the exact extracted-text intervals read are recorded in the manifest. In particular, this unit read the complete displayed Lemma 3.26–Theorem 3.31 chain, its invocation of Corollary 4.2, and the indicated Section 6 consumers. It did **not** validate every optical-symbol certificate, normal-chart construction, marked weak-RG estimate, tightness argument, OS limit, or nontriviality argument in the 118-page manuscript. A theorem statement with the desired endpoint is not a validation of its upstream proofs.

The target remains the same continuum hierarchy used for existence, with cutoff- and volume-uniform physical decay, operator-dependent but cutoff-independent prefactors and onset, a dense centered reflected source algebra, and a nonzero finite-energy excited sector. The fixed-spacing small-coupling result already proved in [MASS_GAP_LOCAL_BLOCK_ASTRA.md](MASS_GAP_LOCAL_BLOCK_ASTRA.md) does not meet that target. This unit does not repeat its proof or the completed Faizal–Shabir counterchecks.

### Normalization dictionary

Use normalized Haar measure and

\[
 d\mu_{\beta_W}(U)=Z^{-1}
 \exp\!\left\{\beta_W\sum_p\frac{\Re\operatorname{Tr}U_p}{N}\right\}
 \prod_e dm(U_e)
\]

for the ordinary defining-representation `SU(N)` Wilson convention. Kirk writes the plaquette action as
\(w_{G,\rho}=c_\rho(1-\Re\operatorname{Tr}\rho(U)/d_\rho)\) and the Boltzmann weight as \(e^{-\sum_pw_{G,\rho}(U_p)/u}\). Thus, for the same defining representation and invariant metric, \(\beta_W=c_\rho/u\), up to the field-independent partition-function factor. The value of \(c_\rho\) is metric-dependent; it is not silently set to \(2N\). Here \(u\) is the coupling variable, not the lattice spacing.

Kirk's handoff interval is a fixed positive coupling interval \(I_\star=[\bar u,\bar u_+]\). Finiteness of a one-pivot oscillation at this interval is compatible with very poor constants as \(\bar u\downarrow0\). It is the exact, uniformly controlled approach to that handoff from arbitrarily fine cutoffs, and the subsequent full-source estimate, that needs proof. No change to this lane's particular blocking scheme is required merely to recognize a valid separate construction.

## 1. Exact rank witness for the Gaussian supplier

Kirk Lemma 3.26, PDF p.20, starts with finite-dimensional core spaces \(H_X\), a block-diagonal positive precision, and

\[
 K=Q_{\rm diag}^{-1/2}Q_{\rm cross}Q_{\rm diag}^{-1/2},\qquad
 \sup_X\sum_{Y\ne X}e^{a_Gd(X,Y)}
 \max_{0\le j\le3}\|D^jK_{XY}\|\le\kappa<1/8.
\]

The norm displayed on the blocks is the operator norm; no trace/HS norm or dimensional factor is supplied. The stated conclusion is uniform in the number **and sizes** of cores. Its proof expands \(\frac12\operatorname{Tr}\log(I+K)\) and bounds cyclic trace words using this row, without their trace factor.

Let there be two cores, each of real dimension \(d\), and set

\[
 Q_{\rm diag}=I_{2d},\qquad
 K=\begin{pmatrix}0&tI_d\\tI_d&0\end{pmatrix},\qquad 0<t<1/8.
\]

Take zero exterior means, no non-Gaussian factors, and no structural marks. Choose a fixed distance with \(e^{a_Gd(X,Y)}=2\) and \(t=1/64\); the printed row is then \(\kappa=1/32\), independently of \(d\). The precision eigenvalues are \(1+t\) and \(1-t\), each with multiplicity \(d\), so positivity is uniform too.

If \(\gamma_Q\) and \(\gamma_I\) are the **normalized** Gaussians, the exact density ratio is

\[
 r_d(x,y):=\frac{d\gamma_Q}{d\gamma_I}(x,y)
       =(1-t^2)^{d/2}\exp(-t\,x\cdot y).
 \tag{1}
\]

Consequently,

\[
 \log r_d(0,0)=\frac d2\log(1-t^2),\qquad
 \operatorname{Tr}K^2=2dt^2.
 \tag{2}
\]

The second trace word already grows linearly with core dimension at fixed operator row. The usual estimate is \(|\operatorname{Tr}M|\le d\|M\|\), not \(|\operatorname{Tr}M|\le\|M\|\). Cyclic-to-rooted combinatorics cannot remove this factor.

Under a literal norm controlling values at the origin, including the usual regulator norms whose regulator equals one there, (2) contradicts the claimed dimension-independent logarithmic row. If the intended norm quotients all field-independent scalars, the origin test alone must instead be read as a failure of the **printed determinant inference**: that inference explicitly includes and bounds connected normalization cycles. Such a quotient would require a separate, exact treatment of the omitted normalizers, their dependence on core geometry, and any source dependence. The text's scalar-removal sentence does not supply a rank estimate.

Two normalization checks make this distinction operational.

* Dropping the prefactor in (1) changes the normalized integral from one to \((1-t^2)^{-d/2}\). A once-only scalar bookkeeping rule can move this factor; it cannot make it dimension-free.
* If a source changes \(t\), the scalar term has derivatives
  \[
  \partial_t\tfrac d2\log(1-t^2)=-\frac{dt}{1-t^2},\qquad
  \partial_t^2\tfrac d2\log(1-t^2)
      =-\frac{d(1+t^2)}{(1-t^2)^2}.
  \]
  These are algebraic derivatives with respect to t; taking t itself as the structural mark would violate the small marked-row hypothesis because the weighted first derivative would be 2. For an admissible marked witness, set `t(s)=t0(1+s)`, `t0=1/64`, `|s|<=1/4`. The weighted block row through derivative order three is at most `max(2t0(1+1/4),2t0,0,0)=5/128<1/8`. At s=0 the derivatives of the logarithmic normalizer with respect to s are

  `-d t0^2/(1-t0^2)` and `-d t0^2(1+t0^2)/(1-t0^2)^2`.

  Subtracting the zero-source vacuum constant does not remove these nonzero, rank-dependent responses. This correctly parameterized example tests the general marked lemma; it is **not** a claim that Kirk's actual fixed optical precision has this source dependence. Even for fixed precision, normalizers of different decompositions into bad cores need not be one common scalar across the sum of label histories. This paragraph is the scoped CIB-R2 correction; the unmarked rank argument is unchanged.

Corollary 4.2, PDF pp.23–24, is itself a correct trace-sensitive Gaussian estimate:

\[
 \mathbb E_\Sigma e^{\sum_i\langle\zeta_i,B_i\zeta_i\rangle}
 \le \exp\!\left\{\frac{\sum_i\operatorname{Tr}(CB_i)}
 {1-2\|C\|\|\sum_iB_i\|}\right\}.
\]

Its denominator is controlled by an operator norm, but its numerator still counts modes. Applying it to \(B\) proportional to an identity on a growing core therefore does not provide the size-independent bound claimed in Lemma 3.26.

This example is an elementary positive Gaussian model. It is not an example of a massless Wilson theory, nor a counterexample to the actual Karcher optical matrix. It disproves the generic determinant estimate from the stated block-row hypotheses; identifying the actual Wilson matrix with this witness would be an additional, unjustified claim.

### Downstream dependence

| Source location | Consumed statement | Effect of the finding |
|---|---|---|
| Lemma 3.27, p.21 | Exponential resolvent/operator rows admit the actual precision to Lemma 3.26 | Such rows alone do not discharge the missing trace/mode budget |
| Theorem 3.28, pp.21–22, equations (4)–(5) | Normalized cross-core Gaussian activities have root mass \(C\kappa_G(R_G)\) uniform in core sizes | The displayed proof invokes the failed generic determinant inference |
| Theorem 3.31, pp.22–23 | Irregular composition has small parameter \(C(\eta_0+\theta_u+\kappa_G)\) | Its Gaussian contribution needs a repaired estimate |
| Proposition 6.8, pp.58–59 | Complete reference/regular/irregular interaction inventory | The irregular supplier is not independently closed by this review |
| Corollary 6.40–Lemma 6.41, pp.72–73 | Joint Haar/optical forest admission includes the cross-core Gaussian activities | The same missing supplier remains upstream |
| Theorem 6.43, p.73 | Uniform physical two-root decay | This review cannot import it as proved through that chain |

This dependency analysis is a proof-screening result, not a statement that every other argument in these sections is incorrect.

## 2. A checked replacement that retains the mode cost

For a real rectangular matrix \(B\), suppose \(\|B\|_{\rm op}\le k<1\), and put

\[
 Q=\begin{pmatrix}I&B\\B^T&I\end{pmatrix}.
\]

The Schur determinant identity gives
\(\det Q=\det(I-B^TB)=\det(I-BB^T)\). If
\(L=\frac12\log\det Q\), then

\[
 \frac12\|B\|_{\rm HS}^2\le -L
 \le\frac{\|B\|_{\rm HS}^2}{2(1-k^2)}.
 \tag{3}
\]

Proof: diagonalize \(B^TB\) and apply
\(x\le-\log(1-x)\le x/(1-k^2)\) to each eigenvalue \(0\le x\le k^2\), then sum. Zero eigenvalues and unequal core dimensions cause no difficulty. Thus the correct control quantity is the sum of squared singular values. The family \(B=tI_d\) has \(\|B\|_{\rm HS}^2=dt^2\); a fixed-rank family or \(t=c/\sqrt d\) has a genuinely uniform normalization budget. These are meaningful passing controls, not merely alternate implementations of the failing case.

For a general self-adjoint finite matrix \(K\), with \(\operatorname{Tr}K=0\) and \(\|K\|_{\rm op}\le k<1\), the same spectral argument gives the coarser bound

\[
 \left|\tfrac12\operatorname{Tr}\log(I+K)\right|
 \le\frac{\|K\|_{\rm HS}^2}{4(1-k)}.
 \tag{4}
\]

Indeed \(|\log(1+x)-x|\le x^2/[2(1-k)]\) for \(|x|\le k\); summing cancels the linear term. These are bounded mathematical support lemmas, with no novelty claim and no continuum conclusion.

There is also an exact local alternative. Let the blocks be fixed-size lattice cells of dimension \(r\), rather than arbitrarily large bad cores; assume \(K_{xx}=0\) and \(\sup_x\sum_y\|K_{xy}\|\le\kappa<1\). Define

\[
 g_x=\frac12\sum_{n\ge2}\frac{(-1)^{n+1}}n
                  \operatorname{tr}(K^n)_{xx}.
\]

At finite volume the series converges absolutely,
\(\sum_xg_x=\frac12\operatorname{Tr}\log(I+K)\), and

\[
 |g_x|\le\frac r2\sum_{n\ge2}\frac{\kappa^n}{n}
       \le\frac{r\kappa^2}{4(1-\kappa)}.
 \tag{5}
\]

The proof bounds each rooted matrix word by its product of block norms and retains the fixed trace factor \(r\). An exponential entrywise row can similarly pay the length of its reported loop. This proves a local trace-cycle budget, not the full marked polymer estimate or its closure under changing core partitions.

Under a genuinely proved exponentially local **site** kernel, separation of two large cores can give a bound of the form
\(\|K_{XY}\|_{\rm HS}^2\le C|I(X)|e^{-cR_G}\); the extensive factor remains. Kirk's bad-core weight has a suppression exponential in core size. There is therefore a plausible repair: keep the trace cycles locally owned and pay their extensive cost from a quantified reserve of the same bad-core charge, while retaining regular and source costs. This is a live calculation to do, not a new primitive or an assumption that the repair succeeds. Uniform marked versions, exterior means, label normalization, and the complete source algebra still need treatment.

### An original-literature route to that repair

[Abdesselam–Rivasseau, *Trees, forests and jungles*, hep-th/9409094v1](https://arxiv.org/abs/hep-th/9409094v1), Theorem III.1, Theorems IV.3 and IV.5, and especially Section V.E, PDF pp.31–33, provide a suitable finite-volume organization. Equation (V.E.3) uses two nested forests: the first joins neighboring large-field cells, and the second supplies covariance links between the resulting components. The forest vertices stay at the level of fixed-size cells. This is exactly where an extensive mode budget can remain visible instead of being compressed into a dimension-free giant-core vertex.

The positivity proof of Theorem IV.5 writes the interpolated covariance as a convex combination of block restrictions of the original positive covariance. The normalized Gaussian measure in (V.E.3) is therefore retained; its normalization is not dropped. The assumptions in Section V.E include a large-field probability bound with a small factor per cell, summable covariance connections, and small derivatives outside the large-field region. Its convergence discussion uses those assumptions; the forest identity does not prove them for Yang–Mills. Section V.A likewise distinguishes the exact expansion from the separate amplitude bounds needed for convergence.

This is a transferable **identity and ownership mechanism**, not a crossover theorem. The exact matching task is: prove its local charge, interpolation-stable covariance decay, and derivative costs for the actual conditioned/blocked Wilson law, with the source insertions and all labels retained. A trace-aware use of this organization would bypass the specific rank omission without assuming the physical mass gap that it is meant to establish. No theorem from a scalar model is silently promoted to a gauge-theory theorem.

## 3. Separated pivots do not alone pay arbitrary incidence by diameter

The proof of Theorem 6.10, PDF pp.60–61, and Lemma 6.30, pp.67–68, use a diameter lower bound proportional to \(R(n(A)-1)\) to pay a factor exponential in the number \(n(A)\) of pivots hit by a reference activity. The asserted scope includes every finite active carrier family. A linear lower bound follows along a single ordered straight path, but not from separation in four dimensions.

Take the \(q^4\) lattice points of \(\{0,R,\ldots,(q-1)R\}^4\), as pivots on \(q^3\) parallel paths. They have pairwise spacing at least \(R\) and a connected hull. Their \(\ell^1\) diameter is \(4R(q-1)\), so

\[
 \frac{\operatorname{diam}A}{R(n(A)-1)}
   =\frac{4(q-1)}{q^4-1}\longrightarrow0.
 \tag{6}
\]

Larger fixed separation accommodates bounded pivot buffers without changing this conclusion. A spanning-tree length or support-size charge can pay \(R(n-1)\); diameter alone cannot. The scripted cases include \(q=2,3,5,9\) and the passing single-path control.

This is a counterexample to the **geometric implication used in the proof**, not yet to the actual family of reference activities. If those activities hit at most two pivots, or obey a stronger tree-length estimate, the required conclusion may be repairable. That structural information has to be supplied for the exact reference inventory. The existing diameter row by itself does not supply it. No synthetic many-body activity is represented here as an activity of the Wilson measure.

The manuscript does print potential stronger suppliers: §4.6 uses the support-tree weight `exp(kappa tau(X))`, Lemma 6.22/(59) asserts a support-size weight, and Appendix A Theorem A.20(E1)/(233) gives `exp(a1 tau(X))` for the reference, regular and irregular activities. Their retained reserve and complete upstream hypotheses have not been validated here. They may repair the literal diameter step if matched to the exact inventory; the finding is not that every stronger estimate is absent from the paper.

## 4. The compact-Haar part has a valid bounded form

For clarity, the basic pivot mechanism can be reconstructed directly from the finite-volume Wilson measure at \(\beta_W\ge0\). On a nondegenerate four-dimensional hypercubic lattice, a link belongs to at most six plaquettes. At fixed values \(\eta\) of all other links, its conditional energy has oscillation at most \(12\beta_W\), since each normalized real character lies in \([-1,1]\). Therefore its **normalized** conditional density satisfies

\[
 \nu_\eta(dU)=\epsilon\,dm(U)+(1-\epsilon)\widetilde\nu_\eta(dU),
 \qquad \epsilon=e^{-12\beta_W}.
 \tag{7}
\]

This follows because the partition-function integral lies between the minimum and maximum of the unnormalized density. It is uniform in the conditioned exterior at this fixed \(\beta_W\).

If a pivot set shares no plaquette, conditioning all nonpivot links gives an **exact product** of these normalized conditionals. For a bounded insertion \(\Phi\) whose Haar integral in each pivot separately vanishes, expanding the product in (7) kills every term containing at least one Haar component. Hence

\[
 \left|\mathbb E(\Phi\mid\eta)\right|
 \le(1-e^{-12\beta_W})^M\|\Phi\|_\infty.
 \tag{8}
\]

For example, a normalized character of a simple Wilson loop in a nontrivial irreducible representation is separately Haar-centered in each loop edge: the loop word is \(B U^{\pm1}C\), and the Haar average of the representation matrix is zero. The conflict graph of loop edges sharing a plaquette has maximum degree at most 18, so a greedy independent set supplies \(M\ge\lceil|\gamma|/19\rceil\). This proves an arbitrary-fixed-\(\beta_W\) perimeter upper bound for this restricted observable class, including all exterior normalizers. It is an elementary calculation, not a new continuum result.

The source algebra needed for a physical gap is much larger than these separately centered loop carriers. Marginalizing optical modes creates interactions among pivots, and those interactions must be estimated in the complete measure. A perimeter upper bound alone is neither an area law nor exponential clustering of the dense physical source algebra. Thus (8) verifies the reusable compact step without validating the missing optical/joint admission.

## 5. Diagnostics, limits, and next live obligation

[checks/crossover_import_attempt01.py](checks/crossover_import_attempt01.py) is an immutable snapshot of the first executed diagnostic. Its [receipt](checks/crossover_import_attempt01.receipt.json) records the command, hashes, and successful exit; [stdout](checks/crossover_import_attempt01.stdout.json) records the runtime versions and **79/79 checks**. There were no earlier failed runs hidden by replacement.

The checks include exact rational determinants and an independent plus/minus diagonalization; rejected missing-rank, wrong-Schur-sign, and omitted-normalizer mutations; zero-coupling, fixed-rank, and fixed-HS controls; rectangular Schur identities; analytic marked normalizers checked by high-precision finite differences; the four-dimensional pivot geometry and a single-path control; and an exact finite-group product-minorization illustration. The finite-group check tests the algebra of (8), not `SU(N)` integration or continuum physics. The asymptotic rank and geometry conclusions are proved by (2) and (6), not by extrapolating finite tests. There is no lattice simulation here.

**Review corrections CIB-R1/CIB-R2.** The original runner and its 79/79 output remain preserved. Its geometry calculation inserted the displayed diameter formula without independently checking it; a wrong coefficient survived. The [additive corrected runner](checks/crossover_import_exact_v2.py) now computes the actual point-set diameter from all signed coordinate extrema and compares it to that formula. It also tests the admissible marked responses above and rejects missing chain factors. The [repair receipt](checks/crossover_import_control_fix_receipt.json) binds the new evidence and affected review. These corrections do not turn the finite controls into a continuum result.

The numerical values are only diagnostics. At \(t=1/64\), \(-\log r_d(0,0)\) rises from approximately \(0.000122085\) at \(d=1\) to \(128.0156\) at \(d=1,048,576\), with precisely the same printed operator row. The proof is its exact linear dependence on \(d\).

The scope checks required by the no-go discipline are recorded without manufacturing a global negative result:

| Check | Disposition |
|---|---|
| N1, route coverage | The rank calculation, geometric test, local trace repair, and Haar reconstruction are the actual work; fewer than five independent normalized negative routes were exercised. No packet PASS or exhaustive-search claim. |
| N2, wall independence | The determinant and exponential-moment omissions are the same mode-count issue, not two independent walls. Geometry is a separate proof inference, with actual-factor realization unresolved. |
| N3, hidden universals | Uniformity is proved only in the parameters stated in (3)–(8). No complete optical/source continuum estimate is asserted. |
| N4, prior-authority use | The previous review and known failed Faizal–Shabir route are not premises of the present calculations. |
| N5, resolution | Exact per-mode and per-core trace accounting; a fixed-cell repair bound; finite-volume Haar algebra. No continuum or all-cutoff certificate. The runner includes a resolution certificate. |
| N6, allowed premises | Finite-dimensional linear algebra, normalized Gaussian/Haar integration, and the explicitly stated Wilson law. No added axiom, primitive, fitted target, or premise-registry mutation. |
| N7, strongest repair | The actual optical matrix may have enough local trace control, and bad-core probability may pay the extensive determinant cost. The two-level jungle expansion supplies a plausible way to retain that cost. This defeats a broad no-go and is the next live target. |
| N8, cross-cycle check | A pinned-main search for the Kirk/core-trace supplier found no corresponding prior theorem; unrelated Kirkwood–Salsburg references were classified context-only. No novelty or absence-of-all-literature claim. |

The immediate reusable obligation is to replace Lemma 3.26's giant-core row by a fixed-cell or explicitly size-weighted Gaussian/jungle inventory and prove that the original bad-core action has enough **remaining** charge after all cutoffs, normalizers, sources, and reporting costs. Separately, replace the reference-diameter-to-incidence step by an actual bounded-incidence or tree-length estimate. Neither task can be discharged by quoting BKAR, optical positivity, or compactness alone.

The inspected 1994 original source supplies the organizational mechanism, not those Yang–Mills estimates. Primary records for the older infrared-cutoff/UV-stability literature were located, but no new theorem from them is imported without its hypotheses and proof coverage. The newly located [Sussman–Alpoge project repository](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment) describes tentative, incompletely vetted work and a developing YM4 existence argument; its README is a research lead, not a continuum-existence or mass-gap input.

**Disposition:** retain the exact bounded calculations and the live local-charge repair direction. Keep full continuum existence and the physical continuum mass gap **OPEN**. No source/shared-summary/audit status was changed by this unit.
