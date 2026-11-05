# DOM: complex-domain admission for the actual roster

Provenance: Codex, 2026-11-05, Pass 2 of Claude's `dom-draft.md`, checkout `1d6a3a0af909d7854eea7511bbf9c9f1cac0c923`; research text, not an audit, no status conferred, not yet refereed. Source material by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, is credited where used. All mathematical arguments are by hand.

This manuscript concerns assembly critical-path item 5, owned by ST1 with NL1. It proves conditional admission statements for a specified roster. Identification with every actual input domain remains open. In particular, neither record retention nor a definition of the new domain discharges ST1 Theorem 14, hypothesis 2.

## Definitions and imports

Use [ST1](st1-r4.md), including Amendments CV and GS, and [PR-lay](pr-lay.md)'s full-stencil conventions. At a depth-\(k\) read, \(\eta=L^{-k}\), \(\xi_m=L^{m-k}\), and \(\mathbf S=(\Omega_0,\ldots,\Omega_{k+1})\) is the **current longer sequence**. The precision uses its depth-\(k\) cut. Its free coordinates are nonpivot level-\(k\) bonds touching \(\Omega_{k+1}\). Write \(I\) for their three-colour coordinate set. All boxes and margins must embed in the torus.

Put \(P=(U,A',\mathbf J)\), \(\mathbf U=e^{i\eta A'}U\), with real \(U\) and independent complex \(\mathbf J\). Use ST1 (1), (6)–(10) for covariant differences, raw versus reduced datum, units and \(P\dotplus h\). A current is never replaced by the physical current at a general complex input. Norms are operator/max norms, with fixed colour conversions included in constants. Define
\[
 r_Y(P)=\max_{\text{complete reads in }Y}
 \{l|A'|,l^2|\nabla^UA'|,l^3|\mathbf J|\},\qquad
 F_Q(\gamma)=\gamma(2\log\gamma^{-1})^Q.
\]
Here \(l\) is the largest incident scale. A read of based scale \(\xi_m\) has \(l\le L\xi_m\). For \(\gamma<e^{-Q}\), differentiation of \(t^{-1/2}(\log t)^Q\) gives its supremum \(F_Q(\gamma)\) on \(t\ge\gamma^{-2}\). This tends to zero by the exponential power series.

The radius table is ST1 (Tq0): \(r_\iota(m)=C_\iota\theta_m^{-1/2}(\log\theta_m)^q\), \(C_1\ge C_0\), \(\varepsilon_m=A_0g_m\ell_m^{p_0}\), \(\delta'_m=A_1g_m\ell_m^{p_1}\), \(g_m=\theta_m^{-1/2}\), \(\ell_m=\log\theta_m\). Retain its exponent conditions, unit lifts, positive \(c_{\min}\), coefficient gaps \(d_*(m)\), and (T1)–(T3). Write \(w(m)=d_*(m)r_0(m)/2\). An initial or unfinished radius index is recorded separately: SA uses index 1 at layer zero, \(t-1\) at an unfinished top, and separate initial radii. The geometric scale and the radius index need not coincide.

**S, the background imports.** These are ST1 GEO, GEO-mark, AV/CURV, A1/F0/REG (hence its P81 chart in Lemma 5), P82–M1 and (15), PROF/RCG4, OPS/SLICE/UNQ, CH, RUN's upper bound, formation exponents (56), and the actual test support (58). They include both erosion rules, real mean-contour representatives, complete interior current stencils, every required witness enlargement, and initial/unfinished comparisons. The derivative input is [cp12](cp12.md) Theorem 3 on its admitted real layered class and fixed raw-datum balls, with P82 I1–I8 and repaired a3-derivative premises. It is not a theorem on arbitrary complex, switched references. Actual geometry retains [geoh](geoh.md)'s R/P specifications, quarantine qualification, carrier matching and Lift hypotheses. None of BOX, LOC, ST-test, complex input membership, DR or CI is hidden in S.

**M, the matrix imports.** Retain [hm](hm.md)'s R, repaired fixed-region W, AV, and its geometry and floors (23). These include complex cut-down inverses, the absolute second-jet bound, complete zero-length multiplier reads, and fixed branches. For the relative gauge form additionally retain [descent](descent.md)'s W-cov and PF. FG/UM, actual potential domains, and G-ID are separate inputs when their conclusions are used. For the optional completed absolute precision retain PR-lay's F. The relative form has its own early constants; they need not equal those for the absolute form.

**Definition 1 (proposed roster \(\mathscr R^{\flat}\)).** A reading structure includes each depth cut actually used by a fibre. At each such structure record:

1. On every required bond, plaquette and derivative stencil, the based-scale bounds
   \[
   \xi_m^2\eta^{-2}|\partial U-I|,\ \xi_m^2\eta^{-2}|\partial\mathbf U-I|<c_\sigma r_0(\nu),\quad
   \xi_m|A'|,\ \xi_m^2|\nabla^UA'|<c_\sigma r_1(\nu),\quad
   \xi_m^3|\mathbf J|<c_\sigma r_0(\nu),                 \tag{1}
   \]
   where \(c_\sigma\le1+\beta_s\) is ST1's recorded scalar coefficient and \(\nu\) is that read's supplied radius index.
2. ST1's frozen ordinary towers and R1 cores at **every consumer core level**, with all their subdomains, erosions, continuation domains and full carriers. For a core address in \(\Omega_i\), include every required core gauge box and its supplied enlargement, with bound \(C_{\rm pot}Mr_0(i)\). A top-level core alone does not supply every later depth cut.
3. Every natural gauge cube of PR-lay/hm, with an actual witness of bound \(a_{\flat}\), and its required formation carrier. Choose \(a_{\flat}<h/4\), where \(h\) is below all real/local matrix ceilings in M.

Keep every born record permanently, with its original function, units, radius set and base radius. The resulting chain domain is denoted \(\mathcal D^{\flat}_{a|\sigma}\). This is a proposed specification, not an identification with the pre-existing actual roster. In particular, a contained boundary cube does not automatically have its required enlarged carrier.

**Definition 2 (\(\mathcal K^{\flat}\)).** Fix hm's \(I,Z_0,H=Z_0^\sharp\subset Z\) and its early constants. For every IMS tent cube \(Q_c\) meeting an active coordinate base, form the rounded next-level-block box used in hm Lemma 4: enlarge by \(b_{\rm tail}+r_{\rm av}+2L\), then round outward. Denote by \(\mathscr B_I(Z)\) all such boxes contained in \(Z\). This includes the boxes of every readable grouped-root compression, including auxiliary endpoints away from \(Z_0\). Require a witness on the whole box. An additional carrier needed to *form* that witness is supplied separately; do not omit a required box merely because this formation carrier is not contained in \(Z\).

A triple belongs to \(\mathcal K^{\flat}(Z;\varrho,a_0)\) if:

1. \(r_Z(P)<\varrho\), and both normalized curvatures are \(<h/4\) on all complete reads;
2. every natural cube has a real gauge of normalized value/difference bound \(<h/4\);
3. every box of \(\mathscr B_I(Z)\) has the unweighted real gauge bound \(|A|,|\nabla A|<C_{\rm pot}Ma_0\) required by hm Lemma 3.

The real bound is consequently \(<h/2\). Use the open working enlargement with \(r_Z<r_{\rm loc}\) for line discs. Rep is imposed separately for the absolute gauge form. The draft's K4, confined to \(N_{b_{\rm gap}+2L}(Z_0)\), is insufficient.

**Definition 3 (localized datum and reference).** Let \(D_+\) be a real admitted datum of the fixed stage determining system, \(U_+=\Phi(D_+)\), and \(V=M_-(U_+)\). A local rule has the form
\(D^\sharp=\mathsf R(D_+|_{X^\sharp})\), depending also on the fixed geometric record. Its reference is \(V^\sharp=M_-(\Phi(D^\sharp))\), in CV's mean-contour representative. Put
\[
 h_j=\max_{b\in\mathfrak E}d_G(V^\sharp(b),V(b)),\qquad
 d_G(g,h)=\text{the principal SU(2) rotation angle of }gh^{-1}.
\]
The metric is globally bi-invariant, with diameter \(\pi\); below \(\pi\) it equals the norm of the principal Lie-algebra logarithm. The exact LOC consumer is \(h_j\le C_{\rm loc}e^{-c_{\rm loc}R_\sharp}\), \(R_\sharp\ge MR_t/4\), or ST1's **assumed** common-chart segment of radius \(r_B\). F6 then requires \(h_j\le\delta'_j/8\) and \(h_j<r_{\rm sol}/4\).

**Order of choice.** Follow IN1's actual table, including Amendment 1:

| When | Choices used here |
|---|---|
| Rows 1–2 | Exponents, fractions, geometric conventions and odd \(L\ge27\), above the existing floors. Set \(c_N=2^{-r}\). |
| Row 3, then row 4 **before \(\kappa\)** | S's structural rates and bounds in their internal order; \(M_1,R_1\); tower, chart, levelling and record constants; M's moments, IMS/root scales and \(K_0,H_0,b,d,C_\tau\); \(a_{\flat}\), the ball constant \(c_{\rm room}\) below, \(K_{\rm main}\), and any proved LOC/path/holomorphic-rule constants. All are independent of \(M,\bar\kappa\) and activity amplitudes. |
| Rows 4–5 | \(\kappa\), its rate window, then \(\bar\kappa\), response lengths and \(M\) above all ST1/hm/geometric floors. Retain DR's explicit \(E_{\bar\kappa}\), not as an early constant. |
| Rows 6–8 | BOX constants, test/radius amplitudes, \(c_{\rm ct}\), formation budgets and the numerical frame-increment bound \(\bar B\). Choose formation constants after any radius shrinkage. |
| Row 9 | One common \(X_0=\gamma^{-2}\) floor enforcing every later ceiling below. It may depend on \(M,\bar\kappa,\bar B\) and amplitudes. |

Thus a required early constant cannot be rescued by a later choice of \(M\) or \(\bar\kappa\). A new lower bound on \(M\) may depend on already fixed analytic lengths.

## Frame and record admission

**Theorem 1 (RUN-low, including eligible early operations).** Assume SA (R19): \(\theta_j\ge X_0=\gamma^{-2}\), \(\underline\lambda(j-i)-c_5\le\theta_i-\theta_j\le\bar B(j-i)\) for \(i\le j\), with fixed \(\underline\lambda>0,c_5\ge0,0\le\bar B<\infty\), and \(R_j\le LR_{j+1}\). Let \(r>1\) and \(R_j=\lceil(\log\min_{u\le j}\theta_u)^r\rceil_{L^{\mathbb N_0}}\). For \(X_0\ge\max(4,2c_5)\),
\[
 R_j\ge2^{-r}(\log\theta_j)^r.                         \tag{2}
\]
Write \(\rho_j=\log_LR_j\). If \(t\ge1+\rho_1\), the least solution of
\[
 L^{N_t^0-1}=R_{t-N_t^0+1}
\]
exists and satisfies \(2\le N_t^0\le t\). After a further **final** floor on \(X_0\), every eligible operation \(t\ge R_t\) has such a solution, in fact
\[
 2\le N_t^0\le\rho_t+2\le R_t-1.                       \tag{3}
\]
No hypothesis \(\bar B\le C\log L\) is needed.

*Proof.* R19 gives \(\min_{u\le j}\theta_u\ge\theta_j-c_5\ge\theta_j/2\). For \(\theta_j\ge4\), \(\log(\theta_j/2)\ge\frac12\log\theta_j\), proving (2). Also \(\rho_j\ge1\), and monotonicity of the running minimum together with R19 gives \(\rho_j-\rho_{j+1}\in\{0,1\}\). Hence
\[
 g(N)=N-1-\rho_{t-N+1},\quad g(1)<0,\quad
 g(N+1)-g(N)\in\{0,1\}.
\]
If \(t\ge1+\rho_1\), then \(g(t)\ge0\), proving the first assertion.

For the eligible case set \(y=\min_{u\le t}\theta_u\), \(\rho=\rho_t\), and \(N_* =\rho+2\). Since \(L\ge27\), induction on \(\rho\ge1\) gives \(\rho+3\le L^\rho\). Thus \(N_*\le R_t-1\le t\), and \(u=t-N_*+1\ge1\). Choose \(X_0\) so, for every \(y\ge X_0\),
\[
 c_5+\bar B(2+r\log_L\log y)\le y,\qquad
 (1+\log2/\log y)^r\le L.                              \tag{4}
\]
These ceilings exist for every fixed finite \(\bar B\), by exponential domination of logarithms. Rounding gives \(\rho<1+r\log_L\log y\). Consequently
\[
 \min_{v\le u}\theta_v\le\theta_u
 \le\theta_t+\bar B(\rho+1)
 \le y+c_5+\bar B(\rho+1)\le2y.
\]
Equation (4) and rounding to powers of \(L\) imply \(R_u\le LR_t\). Therefore \(g(N_*)\ge0\); the integer argument proves (3). For \(t\le\rho_1\), no solution with \(N\le t\) exists. SA 17575–17583 makes the actual class empty for \(t\le N_t=R_t\); it does not require a nonexistent operation there. Initial domain comparisons remain separately supplied. \(\square\)

**Lemma 2 (what enlarging the roster preserves).** Under S, complete formation carriers, supplied exceptional-index comparisons and compatible persistent records, every record of Definition 1 forms with ST1's margin. ST1 Lemmas 9′, 10, 11 and B4 then hold record by record. Their real-drift assertion retains the actual physical source and BOX identities.

*Proof.* At birth, ST1 (59), (T1) and (60a) bound simple curvature and current by \(\epsilon_{\rm f}r_0(m)\); the potential is zero. The adjacent/exceptional comparisons transfer this to the recorded \(\nu\), with a fixed decrease of \(\epsilon_{\rm f}\). ST1 Lemma 10 supplies towers and core witnesses on their complete carriers. Its (60) supplies each natural witness after a coupling ceiling; alignment uses a containing aligned cube, as in repaired PR-lay Lemma 6. It supplies nothing across a missing carrier. The same lemma applies at every requested core level \(i\) with address in \(\Omega_i\).

Retention keeps identical functions, so ST1 M2's scalar gaps apply. Its Lemma 11 compares each simple read using (66), each frozen tower using (49), and each R1 element using Lemma 9′. None of these estimates depends on the number of records. Witnesses stay fixed under complex substitution and are transported under physical real drift. Its telescoping proof therefore applies unchanged, including its physical-current and stored-transport hypotheses. \(\square\)

**Outstanding — roster realization and local coverage.** Definition 1 adds conditions. It has not been shown to be the roster on every actual local CI fibre, or to cover all its integration/substitution inputs. A smaller domain preserves an already known bound by restriction; it does not prove formation on that domain, actual integral coverage, or the requisite restriction/overlap identifications. CI-form explicitly takes suprema over arbitrary points of each declared local fibre, not only restrictions of a global field. This obligation is retained throughout.

**Theorem 3 (PR-lay's D (19)).** Let \(P\in\mathcal D^{\flat}_{a|\sigma}\), with Definition 1 covering the current longer sequence. Then every required read satisfies
\[
 l|A'|,l^2|\nabla^UA'|\le(1+\beta_s)L^3r_1(\nu),\quad
 l^3|\mathbf J|\le(1+\beta_s)L^3r_0(\nu).               \tag{5}
\]
Thus D holds with \(\lambda_\sigma=L^3\) and \(C'_\lambda\ge L^3\). Under PR-lay R/W/G/B/Q, its Theorem 8 applies after a final coupling ceiling.

*Proof.* A complete stencil cannot cross two layer boundaries: its diameter is at most \(2\eta\), while a full intervening layer has width \(>\rho_0\eta>2\eta\). Thus \(l/\xi_m\le L\). Multiply (1) by the corresponding first, second or third power. Since \(\log\theta_\nu>1\), \(L^3\le C'_\lambda(\log\theta_\nu)^{2r_R}\). The actual radius index remains \(\nu\), including exceptional reads. Uniformly,
\[
 r(P)\le\varrho_\gamma:=L^3(1+\beta_s)C_1F_q(\gamma)\to0. \tag{6}
\]
PR-lay's real-background and gauge estimates still require B and Q. At a line point \(P_z=(U,zA',z\mathbf J)\), \(r(P_z)=|z|r(P)\). A fixed disc \(|z|\le R\) is admitted to the **operator working class** by its line-disc proof and a ceiling on \(R\varrho_\gamma\). Such points need not lie in the chain domain, nor satisfy (5) with the unchanged constant when \(|z|>1\). \(\square\)

**Lemma 4 (room at an admitted real background).** Assume S and that every record at \(P_0=(U,0,J_+(U))\) holds with half its declared radius, as in B4. There is an early \(c_{\rm room}>0\), independent of depth, \(M,\bar\kappa\), such that
\[
 \max_b\frac{\max\{l|H|,l^2|\nabla^UH|,l^3|K|\}}{r_0(m(b))}
 <c_{\rm room}
 \quad\Longrightarrow\quad P_0\dotplus(H,K)\in\mathcal D^{\flat}_{a|\sigma}. \tag{7}
\]
All required carriers and exceptional comparisons are assumed. This is an open weighted ball, not a product of independent derivative coordinates.

*Proof.* Apply the estimates in ST1 Lemma 11 with the available half-radius margin in place of a transition gap. T2 gives
\(L^{-a v}r_0(m+v)\le(2/L)^v r_0(m)\) for \(a\ge1\). Across a tower, the layer-distance estimate gives a fixed multiple of \(r_0\) after summing the exponentially weighted comparison, exactly as in that lemma. Thus every normalized simple/tower increment is bounded by \(C c_{\rm room}r_0\), with early \(C\). For a core, use Lemma 9′ with \(\tau_0=1/2\); choose \(c_{\rm room}\) below its finitely many displayed constants, including the adjacent \(L^3\), radius-ratio and current margins. Choose it smaller for the supplied exceptional comparisons. All margins are at least a fixed multiple of \(c_{\min}r_0\). The real witnesses are unchanged. The small logarithm and intrinsic tower maps are holomorphic on this open ball. This \(c_{\rm room}\) is distinct from IN1's later, unrelated \(c_{\rm ball}\). \(\square\)

## The corrected R4 clause

**Lemma 5 (the draft's explicit shallow-layer point).** Consider the proposed analytic record class, with compatible frozen geometries, ordinary radius indices through \(k\), and the carriers in Lemma 2. Suppose a layer \(m\) contains a direction-1 bond \(b\), at distance \(>3\xi_m\) from every other layer. Require also that each core tower whose **full input carrier** meets the tent support below has core level \(i\le m\). This extra requirement concerns input reads, not output addresses. Enlarge \(K_a\) to at least one and put
\[
 r_{\min}=\min_{\ell\le k}r_0(\ell),\quad
 s_0=\frac{c_{\min}r_{\min}}{16K_aK^\sharp},\quad
 n_0=\left\lceil\log_L\frac{2a_1}{s_0}\right\rceil+1.
\]
Assume S, the fixed absolute smallness ceilings, \(m\le k-n_0\), and that \(Z\) contains the \(2\xi_m\)-neighbourhood of \(b\). For \(s_0/2<s<s_0\), set
\[
 P_s=(I,A_s,0),\quad
 (A_s)_\mu(y)=\delta_{\mu1}s\xi_m^{-1}
       (1-|y-b_-|_\infty/\xi_m)_+\sigma_3.                 \tag{8}
\]
Then \(P_s\) belongs to this chain record class but violates hm/descent's unweighted R4 bound \(|A'|<a_1\) on \(Z\).

*Proof.* The scalar tent has difference at most \(\eta/\xi_m\). Therefore \(\xi_m|A_s|\le s\), \(\xi_m^2|\nabla A_s|\le s\). All links commute, so a plaquette is exactly the exponential of its signed link sum. The bound \(|e^{ix\sigma_3}-I|\le|x|\) gives normalized curvature at most \(2s\). These bounds include the edge of the support. Older based scales on this support are no larger; their corresponding normalized bounds only decrease. Their current radii are at least \(c_{\min}r_{\min}\).

For an ordinary frozen tower use its own ambient sequence in ST1 Lemma 8: \(E_U=0\), \(E_{A_s}\le s\), so its normalized read is at most \(K_as\), with the top conversion paid by \(K^\sharp\). The additional factor \(L^{p-i}\) when comparing to ST1 (14) is at most one. For an R1 tower, the extra factor in ST1 (R2) must also be checked. By the full-carrier hypothesis \(i\le m\) whenever it reads a nonzero perturbation. In level-\(i\) units both \(|A_s|\) and \(|\nabla A_s|\) are at most \(s\). With \(\lambda_p=L^{-(i-p)}\), the Lipschitz calculation in ST1 Lemma 9′ gives
\[
 |G_n(P_s)-G_n(P_0)|
 \le K^\sharp\max\{\lambda_p|A_s|,\lambda_p^2|\nabla A_s|\}
 \le K^\sharp s\lambda_p.
\]
This is below \(c_{\min}r_{\min}\lambda_p\); omitting \(\lambda_p\) would not prove core membership. Lemma 8 also supplies the open tower domains. A core not reading the support is unchanged. Every real witness is the zero gauge potential. All normalized estimates are at most \(2K_aK^\sharp s<c_{\min}r_{\min}/8\). Finally
\(|A_s(b)|=sL^{k-m}>(s_0/2)L^{n_0}>a_1\). \(\square\)

**Outstanding — the original counterexample's full-carrier claim.** This checks the displayed point with the stated carrier hypothesis. The draft checks which core addresses meet the support, but a tower can read beyond its output address; that argument does not verify every full input carrier. It also supplies no passing history realizing the required shallow support. Thus its actual-domain counterexample is not established as stated. The elementary scale obstruction is real, and the point is a counterexample for any record geometry satisfying the additional hypothesis; it is not a proof that every actual support realizes it. Nor is every point outside R4: \((I,0,0)\) belongs to both classes.

**Theorem 6 (hm and descent on \(\mathcal K^{\flat}\)).** Assume M and
\[
 L^2(1+C_{\rm pot}M)a_0<h/16,\quad
 \varrho<\min(r_{\rm loc}/2,1/(2H_0)),\quad |\tau-1|\le1/2. \tag{9}
\]
Hm Theorems 7–8 and its UM corollary hold on \(\mathcal K^{\flat}\cap\mathrm{Rep}\). Descent Theorem 5 holds on \(\mathcal K^{\flat}\) for the Y3 relative form. The matrices have the original symmetry, holomorphy, normalization, restriction and wall-factorization conclusions, with
\[
 \|C_*\|+\|C_*^{-1}\|+\|\Gamma_*\|\le K_0,\quad
 \operatorname{Re}C^{-1}\ge c_L/2,\quad \|C\|\le2/c_L,
\]
\[
 \|\tau^{-1}C-C_*\|+\|\tau^{1/2}\Gamma-\Gamma_*\|
 \le H_0(e^{32\bar\kappa-dM}+\varrho)+C_\tau|\tau-1|.     \tag{10}
\]
FG/UM and its whole-domain integrand hypotheses remain necessary. For the Gaussian functional require the right side of (10) to be at most \(\varepsilon_0(K_0)\). For UM require each of its exponential and remaining terms to be at most \(\varepsilon_*/2\), where \(\varepsilon_* =\min(\varepsilon_0,(3D_0M^4)^{-1})\), together with hm's \(W_0\), tilt and insertion ceilings. Physical identification still requires G-ID.

*Proof.* The nine uses of the old class in the draft's proposed rereading are as follows.

1. Hm Lemma 1 reads only the local regular class and W on complete hulls. Definition 2 supplies that class.
2. Hm Lemma 2's conversion from R4 is unnecessary: \(r_Z<\varrho\) is explicit. Its separate line-disc proof uses the real bound and scaled complex size. It gives displacement \(H_1r_Z\) here with the same early constants.
3. Hm Lemma 3 needs a small real gauge on each actual extension box and Rep on its protected blocks. Definition 2(3), (9) and Rep supply exactly these.
4. Its IMS argument then gives real gap \(3c_L/4\), complex gap \(5c_L/8\), and short-label gap \(c_L/2\). Whole-torus uses of R have the global real bound.
5. **The correction:** hm Theorem 5 compresses about every root-entry endpoint to a radius-\(nr_c\) coordinate ball. Its tents can be far from \(Z_0\). Each nonzero tent meets an active coordinate and hence has its box in \(\mathscr B_I(Z)\) whenever that grouped hull is readable. Thus the same contraction \(q_*<1\), grouped Neumann series and integral give \(U_{\rm root}\) and displacement \(2U_{\rm root}r_Z/r_{\rm loc}\). The draft's narrower K4 did not justify this step.
6. Tag and collar counting in hm Lemma 6 uses only the fixed geometry.
7. Theorem 7 now gives \(H_0(E_M+r_Z)+C_\tau|\tau-1|\), with \(E_M=e^{32\bar\kappa-dM}\). Substitute \(r_Z<\varrho\), rather than using R4 to bound it.
8. Theorem 8 and Corollary 13.1 use these matrix bounds and the separately imported FG/UM hypotheses. Their proof is unchanged with (10) and its stated ceiling.
9. Every condition of Definition 2 is preserved by real gauges: norms conjugate unitarily, and a witness \(h\) becomes \(hg^{-1}\). Descent Lemma 1 therefore supplies Rep without changing bounds. Lemma 4's colour-grouped covariant pair coefficients and Theorem 5's conjugation argument apply. Use the early constants for the replacement form, including its analytic gauge-label bound.

These checks cover the proofs, not merely the theorem statements. They introduce no physical Gaussian identification or new integrand bound. \(\square\)

**Theorem 7 (conditional chain-to-\(\mathcal K^{\flat}\) inclusion).** Suppose Definition 1 covers the current longer sequence and the necessary core level \(k\ge1\). Assume its top gap \(\operatorname{dist}_\infty(\Omega_{k+1},\Omega_k^c)\ge LM\), and supply an early \(e_c\) bounding the extra core-gauge formation-carrier reach in level-\(k\) units. Impose the additional later floor
\[
 M\ge b_{\rm gap}+e_c+3.                                \tag{11}
\]
Then every chain point restricted to a complete matrix read domain lies in \(\mathcal K^{\flat}(Z;\varrho_\gamma,a_0^\gamma)\), where \(a_0^\gamma=C_0F_q(\gamma)\), after the final ceilings
\[
 L^2(1+\beta_s)C_0F_q(\gamma)<h/4,
 \qquad \text{(9) with }(\varrho,a_0)=(\varrho_\gamma,a_0^\gamma). \tag{12}
\]
For \(k=0\), the initial gauge/box supply is a separate premise.

*Proof.* Equation (5) supplies complex size; (1) supplies normalized curvatures with the factor \(L^2\). Natural witnesses are recorded. Every active-coordinate base is within distance one of \(\Omega_{k+1}\). A nonzero IMS tent meets such a base. Its extension box is within \(b_{\rm gap}\) of it, by hm Lemma 4's explicit size calculation. Including the carrier and rounding to core \(M\)-cubes adds at most \(e_c+M\). By (11), the resulting distance is less than \(2M<LM\). The whole core address is therefore in \(\Omega_k\), and its recorded witness gives Definition 2(3), since \(r_0(k)\le a_0^\gamma\). This argument covers all auxiliary root coordinates. It makes no assumption that the entire selected support \(Z_0\) lies near \(\Omega_{k+1}\). Real gauge invariance gives the same inclusion after descent's representative change. \(\square\)

## Substitution and the counterterm ball

**Theorem 8 (the precise complex-membership implication).** Fix an input \(P\in\mathcal D^{\flat}_{a|+}\), including every required R1 working core, and all ST1 absolute/chart ceilings. Assume compatible records, S, CI for the target activity, and an actual DR map on the full switch polydisc with ST1 (16), specification at one, source-free vanishing, restriction, common-lift transport and splitting. At a stage also assume the completed F4 source; at a main step assume its coordinate/source supply; at an output assume BOX. If the source budget (71) has \(a_X<1/2\), then
\[
 P\dotplus(zh_Y(s;P,\xi))^\delta\in\mathcal D^{\flat}_{a|-},
 \qquad |z|<\rho_X=(2a_X)^{-1}>1,
 \quad |s_\Delta|<e^{\bar\kappa},                           \tag{13}
\]
with half of every target gap left. Compositions have Theorem 14's holomorphy and bounds. Theorems 3 and 7 apply to admitted target reads under their respective geometry and ceilings. Stage contours additionally retain ST-test\(^{\rm hol}\), FC-mean-match, FC-test and FC2's analytic majorants; use SLOT-ST and, for a CA presentation, SLOT-CA/FM-match as Amendment GS requires.

*Proof.* ST1 Lemma 13 gives pinned norm \(<r_*/2\) on the stated disc. Lemma 2 permits ST1 Lemma 11 for the specified record list. This proves (13). Lemmas 5 and 8 of ST1 keep each intrinsic continuation defined; CI permits composition with the old activity. F4's use on passing real support requires the pivot bound and LOC proved conditionally below. No statement here replaces the assumed membership of \(P\). \(\square\)

**Outstanding — actual input membership.** To apply (13) to an external parameter domain \(\mathcal E\), one still needs the map \(\zeta\mapsto P_+(\zeta)\) and
\(P_+(\mathcal E)\subset\mathcal D^{\flat}_{a|+}\), including its independent current and all local carriers. Taking \(\mathcal E=\mathcal D^{\flat}_{a|+}\) proves an implication on that chosen domain, not this identification for every original evaluation. B4 proves real admission; CI-base concerns initial activities, not arbitrary input points. DR's distilled Theorem 4 itself retains regular-pair admission, PW/NL, column/local estimates and regional compatibility. [ci-form](ci-form.md) H-D additionally retains complex-pair identification. Thus the draft's elimination of ST1 L1542's hypothesis 2 is not justified.

**Corollary 9 (conditional H-ct radius).** At a main step, suppose cp12's variable \(B\) is identified with a completed source of size at most \(C_A\delta_{\rm src}\), where
\[
 \mathfrak B_k(2r_k^{\rm ct})=\{B:\sup|g_kB|<2c_{\rm ct}r_0(k)\},
 \qquad \delta_{\rm src}=2c_{\rm ct}r_0(k).
\]
Assume Theorem 8's input membership and DR on this entire source ball. For an early structural \(K_{\rm main}\), the additional choice
\[
 c_{\rm ct}\le(4E_{\bar\kappa}K_{\rm main})^{-1}            \tag{14}
\]
makes (13) hold on the doubled ball after a final coupling ceiling.

*Proof.* ST1 Lemma 13's main-step geometry gives \(Q_X\le C/(a r_0(k))\), where \(a>0\) is its fixed main-step coefficient gap. Its \(E_X\le1\). Set
\[
 K_{\rm main}=2C_DC_AC_{\rm lev}C/(a r_*).
\]
The maximum in ST1 (71) is at most the sum, so
\[
 a_X\le c_{\rm ct}E_{\bar\kappa}K_{\rm main}
 +2c_{\rm ct}r_0(k)C_DE_{\bar\kappa}C_AK_{\rm pin}/\epsilon_{\rm lev}.
\]
The first term is at most \(1/4\); the second is less than \(1/4\) for small \(\gamma\). The same ceiling puts \(C_A\delta_{\rm src}\) below DR's specified source threshold. For the distilled DR choice these late factors are \(E_{\bar\kappa}=e^{48\bar\kappa}\) and \(s_D=\epsilon_De^{-64\bar\kappa}\). All constants in \(K_{\rm main}\) precede \(\kappa\); these exponentials do not. Apply Theorem 8. \(\square\)

This ceiling is compatible with cp12: \(c_{\rm ct}\) is chosen at IN1 row 6, after \(\bar\kappa\), before formation bounds. Its Hessian factor becomes
\((c_{\rm ct}C_0)^{-2}(\log\theta_k)^{-2q}\); the larger fixed coefficient is paid by the final ceiling. Cp12 C1–C3, D7's compatible joined systems and localized derivative estimates, the identification of \(\Psi_z\), and coverage of its centres/fluctuation shifts are still needed. Neither (14) nor ST1 tower room proves these. SA 9767–9772 also assumes enlarged simple **and** tower conditions; it does not discharge them for the actual decoupled maps.

## LOC and the stage tests

**Lemma 10 (locality cannot supply LOC-form on all real data).** Choose the fixed chart radius \(r_B<\pi/3\), as permitted by ST1's chart shrinkage. On a sufficiently large determining system with a remote row, no local real rule can put both references within raw distance \(r_B\) for every admitted datum. In particular it cannot supply LOC-form universally.

*Proof.* Take the flat datum \(D_0=M_+(I)\). Choose a determining node \(v\), outside all local data carriers, with an incident remote row \(c\). Set a real site gauge to \(g(v)=e^{i3r_B\sigma_3}\) and to \(I\) at other nodes; extend it to bare sites. By exact averaging covariance,
\(D_1=M_+(I^g)\) has rows \(g(c_-)g(c_+)^{-1}\). It is exactly flat, satisfies all datum-loop curvature tests, and is admitted by A1/F0/REG and real gauge covariance. It agrees with \(D_0\) on the local input, but \(d_G(D_0(c),D_1(c))=3r_B\). A local rule returns the same \(D^\sharp\) for both. If LOC-form held for both, the triangle inequality would give \(3r_B\le2r_B\). \(\square\)

This replaces the draft's unverified slowly varying row assignment by exactly flat data. Its inference that \(\delta_B\le r_B/40\) alone makes \(r_B\) small was also invalid. This lemma concerns all admitted real data, not a constructed positive-measure history.

**Lemma 11 (LOC-decay from an admitted path).** Suppose \(D_+\) and \(D^\sharp\) are joined on \([0,1]\) by a piecewise \(C^1\) path of admitted real data of the **same** determining system. Suppose its rows are constant within distance \(R_\sharp/2\) of the full stage carriers, and
\[
 \left|i^{-1}\dot D_s(c)D_s(c)^{-1}\right|\le C_{\rm path}.
\]
Require S, ST1 (15), its carrier/gauge readout, and regular uniqueness uniformly along that path. Then
\[
 h_j\le C_F C_{\rm path}S_4(a)e^{-aR_\sharp/2},
 \qquad a=\min(1,\theta_4/2),                             \tag{15}
\]
with early constants. Under Theorem 1's frame assumptions, F6's two smallness conclusions hold after a coupling ceiling.

*Proof.* Intrinsic centre independence in ST1 Lemma 5 glues the local continuations along the path. At a real centre, (15) of ST1 and the mean-contour product estimate bound the **right-trivialized row velocity** of \(M_-(\Phi(D_s))\) by
\(C_F\sum_c e^{-\theta_4d(b,y_c)}|i^{-1}\dot D_s(c)D_s(c)^{-1}|\).
Only distant rows vary. The separation floor gives \(a\rho_0\ge16\log L\). ST1 Lemma 2's summation, with fixed carrier losses absorbed in \(C_F\), bounds the velocity by the right side of (15). Group distance is at most integrated speed. This avoids differentiating a possibly undefined global \(\log V_s\). For sufficiently small \(\gamma\), the integrated distance is below the principal-log radius.

By Theorem 1, \(R_\sharp\ge c_N\ell_t^r/4\). RUN and the finite increment bound give \(\theta_j/\theta_t\in[1/2,2]\) on the waiting window after a final ceiling: its width is \(O(\ell_t^r)\), whereas \(\theta_t=e^{\ell_t}\). Since \(r>1\), \(e^{-c\ell_t^r}/\delta'_j\to0\) uniformly there. This gives \(h_j\le\delta'_j/8\) and \(h_j<r_{\rm sol}/4\). \(\square\)

**Lemma 12 (LOC-flat — Outstanding).** Construct one rule \(\mathsf R\), real on real data and holomorphic on specified complex local charts, such that for every stage:

1. it uses only \(D_+|_{X^\sharp}\) and the fixed geometry;
2. \(D^\sharp=D_+\) on every row of \(X^\sharp\);
3. its global output is admitted for the same determining system and satisfies the actual (56), (58) loop tests;
4. it has a path as in Lemma 11, with \(C_{\rm path}\) fixed before \(\kappa\), independently of \(M,\bar\kappa\);
5. both background references use CV. For ST-test\(^{\rm hol}\), also supply Lemma 14's quantitative chart and full-real-slice properties.

*Attempt and precise remaining failures.* The general extension and path have not been constructed. There is a hand construction on the exactly pure-gauge sector. Choose a spanning forest of the local row graph. Products along its paths define node values \(q_v\), equal to \(I\) at each root. Set other node values to \(I\), and put \(D^\sharp(c)=q_{c_-}q_{c_+}^{-1}\). When the local cycle products are identity this agrees with every local edge. These products and inverses are holomorphic. If the global datum is \(g_vg_w^{-1}\), then on a local component \(q_v=g_vg_{\rm root}^{-1}\). Choose a real logarithm of each node value of norm at most \(\pi\). On each local component move \(g_v\) by the common right factor from \(I\) to \(g_{\rm root}^{-1}\); outside its vertices move each \(g_v\) to \(I\). This gives a flat path, constant on local rows, with row speed at most \(2\pi\). It supplies Lemma 11's path when those rows cover its protected neighbourhood.

For curved data the same construction fails already at agreement: every output cycle product is identity, while a non-tree input edge can close a nontrivial plaquette. Retaining those edges and cutting off the remaining potentials requires one controlled gauge/patching construction on the whole cell collar. ST1 supplies small gauges on fixed carrier boxes, not that uniform extension. Tree holonomies can accumulate with path length; ordinary holomorphy of their products gives no uniform complex radius.

A second route uses the background of a restricted system with a boundary current. For \(\Omega'_q=\Omega_q\cap X^\sharp\), any deeper member reaching the artificial boundary loses A1/P82's positive separation margin. SA 17578's quiet-cell statement does not establish the required margin for this cut. Eroding the members can restore separation but changes the determining map. SA's joined-sequence comparison at 9783–9789 and 9913 sketches a possible comparison using single-layer collars and a defect-of-lifts estimate. It does not supply the present same-system extension/path or its uniform holomorphic rule. Those precise hypotheses must be proved for the actual component.

A third route cuts off in a single gauge and interpolates its potential. Hm Lemma 3 does this on one small-potential box. It does not provide a small gauge over a cell-sized \(X^\sharp\), agreement on all datum rows, or control of the nonabelian commutator curvature throughout the interpolation. The derivative estimate controls a path **after** admission, so continuation using that estimate cannot assume admission at the next point without its own extension argument. No topological obstruction or universal nonexistence theorem for LOC-flat is claimed. These failures leave its extension and path clauses open.

**Theorem 13 (ST-test's pivot clause).** Assume S, the local rule's agreement/admission clauses, the actual free-row test \(d_G(D_{\rm old}(b),V^\sharp(b))<\delta'_j\), the fibre equation \(F(D_{\rm old})=D_+\), and ST1 RUN/(56)/(58) on every old datum loop used below. Require the pivot double blocks to lie in the declared \(X^\sharp\) carriers. Then every removed row, pivots included, is within \(r_{\rm sol}/4\) of \(V^\sharp\), after a coupling ceiling. Locality of the test additionally requires ST1 F7's remaining quarter-cell read reach.

*Proof.* SA 8167 chooses the pivot of \((y,y+Le_\mu)\), \(y\in L\mathbb Z^4\) in level-\(j\) units, at \((y+he_\mu,y+(h+1)e_\mu)\), \(h=(L-1)/2\). It crosses a block face; it is not at the block centre. Complete this bond to a plaquette by a unit step in a transverse direction. The parallel opposite edge has a transverse coordinate shifted by one, so cannot be a pivot. The transverse edges have longitudinal coordinate \(h\) or \(h+1\) modulo \(L\), neither zero for \(L\ge5\), so neither can be a transverse pivot. The plaquette lies in the same double block. ST1 Lemma 12's alignment/separation makes these old level-\(j\) rows; each other edge is free removed or retained. This proves the needed ISO assertion from the actual geometry, beyond mere independence of pivot equations.

Retained rows agree exactly: \(F\) copies them and the localized datum agrees with \(D_+\). For a pivot \(p\), solve its plaquette product for that edge. Bi-invariance and the product triangle inequality give
\[
 d_G(D_{\rm old}(p),V^\sharp(p))
 \le3\delta'_j+d_G(\partial D_{\rm old},I)+d_G(\partial V^\sharp,I).
\]
The first curvature uses the explicitly assumed (58), not the words “older tests retained.” The second uses the admitted localized background, ST1 (59) and AV/CURV on the complete carrier. For small group defects, \(d_G(W,I)\le2|W-I|\), by \(|e^{i\alpha\sigma}-I|=2\sin(|\alpha|/2)\). Thus both terms are at most a fixed multiple of \(A_0F_{p_0+2r_R}(\gamma)\). The displayed sum and the free-row bound tend to zero, proving the assertion. This proves the quantitative clause; selection and compatibility of the actual passing factor, including its older densities, remain the ST-test design input. \(\square\)

**Lemma 14 (the exact ST-test\(^{\rm hol}\) requirement).** Under S, a sufficient quantitative extension of LOC-flat is the following. For each real datum in use, there are early \(r_{\mathsf R},C_{\mathsf R}>0\), uniform in histories and volume, such that
\[
 B\longmapsto B^\sharp(B)
 =i^{-1}\Log\!\left[\mathsf R(e^{iB}D^0_+)\,
                         \mathsf R(D^0_+)^{-1}\right]
\]
is holomorphic for \(\|B\|<r_{\mathsf R}\), real for real \(B\), and \(\|B^\sharp(B)\|\le C_{\mathsf R}\|B\|\). Its image and the original datum stay in their admitted continuation charts. Require real LOC uniformly on the **whole real slice of a fixed ball**, not only on the shrinking passing set. Finally supply the actual-coordinate bound \(\|B\|\le C_{\rm raw}r_1(i)\), with early \(C_{\rm raw}\) and the correct recorded index. Then ST-test\(^{\rm hol}\) holds with early \(r_{\rm hol},M_*\) and \(\|Y\|\le C_{\rm raw}r_1(i)\).

*Proof.* On fixed smaller admitted raw charts, ST1 (15), its summable readout and AV give an early Lipschitz constant \(C_V\) for the reference rows and their relative logarithm. Choose \(r_{\rm hol}\) below \(r_{\mathsf R}/2\), \(\delta_B/[4(1+C_{\mathsf R})]\), and a fixed logarithm radius divided by \(4C_V(1+C_{\mathsf R})\). Real LOC makes the centre discrepancy smaller than a quarter of that logarithm radius after a coupling ceiling. Composition is then holomorphic on the ball and uniformly bounded; one may shrink the early ball to take \(M_*=1\). Reality and CV are preserved. For \(B=X+iY\), both Hermitian parts have norm at most \(\|B\|\); the actual-coordinate bound and a final ceiling give \(\|X\|<r_{\rm hol}/4\). The assumed full-real-slice LOC is exactly the hypothesis used by ST1 FC7's two-constants argument. \(\square\)

**Outstanding — quantitative localized charts.** LOC-flat's ordinary holomorphy does not prove Lemma 14's uniform ball, bounded image or full-real-slice LOC. The draft's choices \(r_{\rm hol}=\min(r_B,r_{\rm sol},r_u)/8\), \(M_*=1\) therefore do not follow. A small bound on real values gives no uniform complex bound: \(\epsilon\sin(Nz)\) already exhibits the missing control. Nor does a fluctuation test imply \(\|X\|<\delta'_j\) for the independent datum \(D_+\).

The proposed replacement factor \(C_QL(1+\beta_s)\) is valid for a row whose AV read has \(\xi_{\rm row}\le L\xi_m\) and **the same radius index**. If its index is adjacent to \(i\), T2 adds a factor at most two. The actual full reference chart needs these carrier/index comparisons on every row. A verified fixed factor can be absorbed in an enlarged early \(C_{\rm raw}\); no precise universal correction of ST1 L154 follows merely from the largest-incident-scale convention.

## BOX, local domains and the older tower route

**Theorem 15 (BOX's exact conditional use).** At an output, let \(\mathcal B_t\) be geoh's specified complete-stencil loop family. Assume:

* **BOX-bg:** \(D_{\rm out}\) is admitted and its background is the canonical real regular critical background; its loops in \(\mathcal B_t\) obey \(C_{\rm bx}C(M)\varepsilon_t\), and every other loop obeys the inherited (58), converted to output levels;
* **BOX-id:** at real parameters the preceding background is \((e^{i\eta H}U_{\rm out})^g\), with real \(g\), the independent/plain-current identity, and surviving stored transports of ST1 Lemma 12;
* **BOX-resp:** the output response has DR's full-polydisc properties and \(n_b(H,K)\le C(M)E_{\bar\kappa}\delta'_t e^{-\mu d_+(b,S_{\rm bx})}\).

Under S, geoh/ST1's full source-carrier geometry and Theorem 1, these clauses give output record formation and drift for compatible persistent records with prior real admission. With Theorem 8's input and CI premises, they also give complex substitution.

*Proof.* A1 supplies the canonical background once datum admission is given. On \(\mathcal B_t\), geoh gives exponent \(N_t^0-1\). By (2), \(L_\flat^{2(N_t^0-1)}\to\infty\) uniformly as \(\gamma\to0\). Thus the B1 ceiling \(C_{\rm bx}C(M)\le C_{\rm te}L_\flat^{2(N_t^0-1)}\) puts the affected loops within (58). The remaining loops satisfy it by hypothesis. Lemma 10 of ST1 forms the records. BOX-resp and the top-layer carrier give B2's budget \(O(C(M)E_{\bar\kappa}(A_1/C_0)\ell_t^{p_1-q})+O(C(M)E_{\bar\kappa}\delta'_t)\to0\). BOX-id supplies B3's physical drift; Lemma 2 and Theorem 8 finish. \(\square\)

**Outstanding — actual BOX.** Unchanged complete loops inherit their tests algebraically. For straddling loops, neither DR nor the small ratio \(\delta'_t/\varepsilon_t\) proves the converted inherited threshold without a matching exponent and a positive margin for the preceding value. Even scalar bounds \(x<T\), \(|\Delta x|\le\epsilon\) do not imply \(x+\Delta x<T\). SA 17656's box-minimizer statement assumes a mild-curvature continuation class and yields its stated curvature estimate; it does not identify every output current, carrier or switched response. The draft's table claiming all straddling loops follow from BOX-id/resp contradicts its own unproved item 13(5). They remain open here.

**Lemma 16 (IN1 restriction and PR1(5b)'s conditional replacement).** Under S and Theorem 8's premises on a coherently supplied local roster, restricting to a smaller full read carrier preserves all its contained records, and (13) preserves the retained target records. ST1 supplies the tube room and half-gap increment budget needed by its own stage substitution, without importing layered-a3 (1).

*Proof.* Restriction only deletes reads; the functions and their units are retained. Lemmas 2 and 4 supply the conditional real/complex room. For each tower, ST1 Lemma 8 gives raw datum norm \(<\delta_B/4\); ST1 Lemma 5 gives distance at least \(\delta_B/8\) from its intrinsic tube complement. ST1 Lemma 11 bounds each read increment by its fixed constant times the weighted shift and leaves half its gap. Its Theorem 14 applies those estimates on the full source/switch discs. These are precisely the two bounds its stage composition consumes. \(\square\)

This does **not** validate the draft's proposed IN1 domain by taking only records whose full carriers lie inside \(X\). Such a rule can omit a tower or witness required at a boundary, and it proves no identification with IN1's declared pair domain, ties or creation-domain reads. A legitimate specification must supply a monotone full-read carrier family, all required records, and compatibility with IN1 H-E/H-SF and CI-form on every local fibre. These remain part of roster realization.

The literal layered-a3 (1) asks for a particular lifted-design derivative bound along its own path, with \(r_a^{\rm lift}\sum_lu_l\sqrt{1+|m-l|}e^{-D|m-l|}\). A finite increment estimate alone does not prove that derivative inequality or identify that path. The frozen consumers retain IN1/PR-lay's discussions and outstanding labels; the older assembly and stage-resp retain the explicit derivative contract. None of ST1's operative lemmas imports it. Thus **a separate PR1(5b) proof is unnecessary for the conditional ST1 route just specified**. This is conditional replacement of its consumer role, not a proof of layered-a3 (1), and not an unconditional claim that the actual T0 construction has already been matched to that route.

## Definitions supplied and source record

The definitions supplied or made explicit in this distillation are:

1. The current longer sequence at each consumer depth cut; the distinction between its geometric scale \(m\) and recorded radius index \(\nu\); the complete-read norm \(r_Y\), scalar envelope \(F_Q\), and grouped import names S and M.
2. The proposed persistent roster \(\mathscr R^\flat\), its chain domains \(\mathcal D^\flat_{a|\sigma}\), all-consumer-level core and natural-witness supply, and the early room constant \(c_{\rm room}\). The plain real triple in Lemma 4 has the physical current; hm's matrix reference remains \((U,0,0)\).
3. The auxiliary frame quantities \(\rho_j,g(N),y,N_*\); the tent point \(P_s\), \(r_{\min},s_0,n_0\), its full-carrier qualification and the core unit factor \(\lambda_p\).
4. The complete IMS box family \(\mathscr B_I(Z)\), the class \(\mathcal K^\flat\) and its open working enlargement, the formation-carrier reach \(e_c\), and \(\varrho_\gamma,a_0^\gamma\). Rep, the matrices and their tags are the imported hm/descent definitions.
5. The conditional identification of cp12's doubled source ball, its early \(K_{\rm main}\) and new ceiling (14); \(\rho_X\) and \(a_X\) keep ST1's definitions, including \(\rho_X=\infty\) at \(a_X=0\).
6. The local rule \(\mathsf R\), datum \(D^\sharp\), reference \(V^\sharp\), bi-invariant distance \(d_G\), discrepancy \(h_j\), and admitted-path norm \(C_{\rm path}\); the pure-gauge forest values \(q_v\).
7. The precise ISO plaquette and RET support readings; the quantitative localized coordinates \(B^\sharp(B)\), \(r_{\mathsf R},C_{\mathsf R},C_V,C_{\rm raw},r_{\rm hol},M_*\). The dimension-four sum \(S_4\) is ST1 Lemma 2's imported summable kernel.
8. The names BOX-bg/id/resp and the full-read local-roster restriction in Lemma 16. These specify conditional interfaces; they do not define missing actual history maps into existence.

All upstream line references use [revision 31a47c543775](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/tree/31a47c543775). The domains, frame, CH geometry, background-comparison programme and relative gauge form are credited to **Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text**. The background and walk methods imported through the library retain their credit to Tadeusz Bałaban and Jonathan Dimock.

The [bounded source-check record](../checks/dom-pass2/source-checks.md) lists the outline and CA-I index entries and source excerpts checked, including CA-I 53773 and SA 17656, which the draft left unread. Y3's relative form and trace convention were checked at 31510–31542 and 3633–3647. CA-II and CA-III were fetched once for source completeness; no passage of either is quoted or used as an additional premise here or in the DOM draft. No whole upstream file was read. [Local identities](../checks/dom-pass2/local-sources.sha256) and [upstream identities](../checks/dom-pass2/upstream-sources.sha256) record revisions, not mathematical evidence. The arguments above use no computer-assisted discharge.

## Result

Theorem 1 proves RUN-low, including the eligible early-level preparation and \(N_t^0\le R_t-1\), under R19 with an arbitrary fixed finite \(\bar B\). On the proposed, coherently supplied roster, the text proves PR-lay D, the corrected \(\mathcal K^\flat\) matrix implication, record and substitution room, and the conditional counterterm-radius budget. It proves the conditional pivot estimate and LOC-decay from an admitted path, and supplies an exactly pure-gauge extension/path. The local LOC-form counterexample is exact in its stated class.

Full DOM for the actual history is **Outstanding**. In particular, the curved LOC-flat extension and path, its quantitative complex chart, actual roster/local-fibre coverage and input membership, and BOX's straddling-loop/source identifications remain open. The original shallow-point claim also retains its full-carrier and actual-history qualifications. The imports are S and M in full, R19, all specified initial/unfinished and geometric comparisons, actual DR and CI on their whole domains, and, where invoked, FG/UM, PF, G-ID, F and the Amendment GS/contour matching inputs. Distilled DR and CI-form are not treated as refereed supply.

The corrections made to the draft's arguments are:

* Replaced its declaration of an “actual” enlarged roster by a proposed roster with explicit coverage obligations; added every consumer depth cut and required core level. Restriction of an old bound does not identify a changed consumer domain or an integral.
* Removed the unsupported early \(\bar B\le C\log L\) restriction and supplied the stronger eligible-level bound using only final coupling ceilings. Kept exceptional radius indices separate from geometric scales.
* Restricted the explicit R4 counterexample to verified full-carrier geometry and supplied the missing \(L^{-(i-p)}\) core-tower factor. Replaced the support-only K4 by all IMS boxes needed by auxiliary root entries, added floor (11), retained the Gaussian/UM ceilings, and removed the unsupported assertion about all of \(Z_0\)'s location.
* Distinguished operator line-disc admission from membership in a chain domain; retained the input-membership premise and the smaller-ball identification obligations. The \(c_{\rm ct}\) shrinkage is compatible with cp12 but conditional.
* Replaced the LOC-form argument by exact pure-gauge data; integrated right-trivialized velocity in LOC-decay; supplied the restricted forest construction and the precise failures of three curved-data routes.
* Corrected the pivot position, separated ISO from the retained-loop assumption (58), and replaced qualitative holomorphy and an inferred passing-test bound by explicit quantitative chart hypotheses. No uniform value \(M_*=1\) or universal raw-coordinate factor is inferred without those hypotheses.
* Retained BOX's straddling-loop gap and the local-domain boundary-carrier gap. Limited PR1(5b)'s replacement to the two controls actually used by ST1; its different derivative formula is not proved.

The draft's proposed corrections to frozen consumers have these dispositions; **none of those files was edited**:

| Frozen passage | Verdict |
|---|---|
| hm L33; descent (2) | Their unweighted R4 definitions and theorems are not wrong. The draft's assertion that their hypotheses are *never* met on shallow supports is false (the flat point suffices). The extension in Theorem 6 is justified only with the repaired \(\mathcal K^\flat\) and all its named premises. |
| IN1 L44 and “full admission” | No erroneous definition is established. The proposed contained-record rule does not supply IN1's boundary reads, whole local pair domains or actual coverage; the draft's claimed replacement is unproved. |
| PR-lay L254 | The warning is correct. Current-scale records give (19) on the proposed domain, but adoption and coverage remain required. Its actual-domain mark cannot be removed here. |
| ST1 L154, ST-test\(^{\rm hol}\) factor | \(C_QL(1+\beta_s)\) is a valid same-index AV bound, not a universal corrected value; adjacent indices and full carriers require their own factors. An established early \(C_{\rm raw}\) can replace it without changing FC7's argument. The complex-chart obligation remains. |
| ST1 L1542, hypothesis 2 | Correct as written. Target retention does not prove membership of the external input. The draft's proposed deletion is rejected. |
| cp12 (27), L565 | The additional ceiling (14) is valid for the identified ST1 source ball. It does not verify every old-window datum condition, centre, fluctuation shift, independent current or \(\Psi_z\) identification. Cp12's coverage mark stays. |
| assembly-status L127 / item 5 | The literal unweighted-R4 inclusion is not supplied. Theorems 6–7 give a conditional weighted replacement interface; its actual adoption is open. The draft's unconditional refutation/closure is stronger than its checked counterexample and coverage evidence. |
| assembly-status L51 / item 5, PR1(5b) | Its separate proof is unnecessary for the specified conditional ST1 route. An actual T0 replacement still requires identification with that route; no backlog/status change follows from this text. |
| geoh-draft's CA-I 53773 reading | The quoted upper bound is present. Theorem 1 now proves \(N_t^0\le R_t-1\) under the stated eligible-level hypotheses, beyond the draft's \(N_t^0\le t\). |

This is research text, **not yet refereed**. It grants no scientific or audit status.
