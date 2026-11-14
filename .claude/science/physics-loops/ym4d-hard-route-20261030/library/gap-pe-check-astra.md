# Repo search

Checked before derivation, 2026-11-13. Searches used `git -C /Users/jonreilly/Projects/Physics grep -n -i -E ... <refs> -- '*.md' '*.tex' | head`, without history searches. Refs: origin/main = 993f5e4f6d11a7e20a1cab9612c5749a53bae073; pr/10114 = f76f6c649cff7dffbab664d8976e680e8f287fe9; pr/10133 = 89faef229ff6e6bde42baad15ed8270c2f4087d8; pr/10134 = 1e70c7211a2cdbc39001e619f1dd89db45e25851; pr/10141 = c73ad7b177d94f89ff37b77386936e3d52b48b05.

- `operator Peierls|gap-pe-max|gap-pe-check|fibre.wise gauge|Theorem BAD`: no hits on those five refs (completed, cap 25). No target-specific prior digest exists. The supplied row 880 has no “Repo prior work” lines. The November 8 repo digest was read in full; its targets are earlier RG suppliers, not this check.
- `Helffer.Sj.strand|convex.maximal.correlation|twisted thin|operator Peierls`, excluding this lane and historical snapshots: 12 hits, below cap 50. Relevant source: `pr/10114:.claude/science/toe-ruleset-20261021/agents/ym4d-proof/PROOF.md:6477–6482` proposes a convex chart and “Helffer–Sjöstrand + Combes–Thomas for W1-cl”; pr/10133 repeats it. This is method history for a different soft-kernel law, not this theorem.
- `origin/main:docs/SHORT_TIME_ROTOR_BRIDGE_AND_ENDPOINT_HESSIAN_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-16.md:90–119`: the bridge Hessian obeys `D+C*diag(cos)C >= (1-r)D`, assuming `r<1`. It cites Carlen–Cordero-Erausquin–Lieb, arXiv:1106.0709v2, for the covariance/gradient identity. Useful primary-source pointer; a different bridge measure, not the twisted Wilson chart. All PR refs repeat the source pointer.
- `origin/main:docs/FINITE_CLOCK_CONDITIONAL_GAUSSIAN_MIXTURE_WARD_RESIDUAL_AND_HAAR_QUADRATURE_BOUNDED_THEOREM_NOTE_2026-09-14.md:222–235`: its Dario–Wu comparison explicitly does not treat the finite-clock gauge law. Related method only. Broad Faddeev–Popov and HS discovery searches hit their caps; no absence claim uses them.
- This checkout, `library/convex-maximal-correlation.md` (whole file): under `S_xx>=A_x`, `S_yy>=A_y` and normalized mixed Hessian norm `<=r<1`, maximal correlation is `<=r`. Its middle-variable section already uses the weighted HS argument and explicitly leaves the HS form and boundary sign as cited gaps. Credit this prior method; it does not supply the present chart or HS0.
- `library/open-registry.md`: no hit for the target labels, operator Peierls, Faddeev, Helffer, convexity, CH-D or Theorem BAD. No conflicting owner was located. This is the explicitly assigned check of new text, not a new proof lane.

Outline search used `library/sa-index/README.md`, chunk rows and neighbours, and `obligations.md`, for Peierls, Faddeev, Helffer/Sjöstrand, convexity, transfer, chessboard and twist. Source at 31a47c543775: `YM4_sketch_500.tex:2313–2335` already constructs the gauge-projected positive transfer operator and `Z=Tr L^s` (GL8); `7660–7681` proves normalized gauge/tree integration identities; `7883–7895` distinguishes the Landau determinant from the axial case. These are prior transfer and measure methods, not the thin-fibre chart theorem. The CA full index finds no HS/Peierls/thin-twist result under those terms. No claim of exhaustive absence is made. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. Balaban's papers are not imported: the bounded term search in `library/lit-balaban.md` finds no input needed here; no claim below rests on an unread Balaban paper.

# Check record

Task: FINISH row 880, gap-pe-check-astra. Research text only; no scientific or audit status is granted. Runs may guide or refute and never discharge a proof.

Provenance: OpenAI Codex, requested checker configuration gpt-6-astra xhigh; source checkout ebbc65f414b15c0fa7ceb39e889587eae336a689. Source P = `library/gap-pe-max.md`, Claude Fable 5.2 max, row 862. S = `library/gap-s1-opus.md`; C = `library/gap-twist-chart.md`. The model/effort label is the supplied task configuration, not an independently queried runtime identifier.

Scope: the statements requested in row 880, their necessary definitions and proof steps. No audit, status edit, numerical proof, new all-M attack or source repair. Existing source summaries were locators; the actual cited passages were read. “FAILS” distinguishes a false statement from a failed inference where stated.

Checkpoint: all requested statements checked; report verified against the pinned sources. Source files remain untouched. No open check item remains in this dispatch; the separate all-M and continuum questions retain their scope and owners.


## 1. Rectangular BAD and T3 — HOLDS

P:277–298; S:125–166,178–253. Fix n, beta, delta_1 and the even ring length M. The auxiliary time length N is even and tends to infinity. The rectangular extension keeps the same epsilon: reflection has two site planes in each direction; the chessboard maximization first makes N columns equal, then M rows. Each disseminated plaquette is counted at most four times. Its event costs at least delta_1 NM/4. The small-ball partition lower bound is exp[-n^2 NM(6 log beta+27)]. Thus BAD is epsilon_1^{|S|} with exactly P's constant. No square geometry is used.

Here is the operator check, without treating a small probability as an operator norm bound. For even N, self-adjointness and the Hilbert–Schmidt property give

    ||T^b||^N <= Tr[(T^b)^N]
                 <= Z_N (2M epsilon_1)^(N/2).

The trace really is the integral with one bad-slab indicator per slab, because each slab has its own temporal links. Select only even slabs. Their two-row sets are disjoint, so every witness set has N/2 different base points. This justifies BAD and the factor (2M)^(N/2). Also

    Z_N <= lambda_0^(N-2) ||T||_HS^2.

The prefactor disappears after the N-th root and N→infinity. Therefore `||T^b|| <= lambda_0 sqrt(2M epsilon_1)`. Positivity of T^b as a quadratic form is neither asserted nor needed. The indicator, M and delta_1 must stay fixed while N grows, as they do here. This is a global operator estimate, not a conditional Peierls estimate.


## 2. F4 — HOLDS

P:347–353, with definitions 307–319. The imported uniqueness statement is S:305–312 at D={b}, not uniqueness of a global gauge inferred from small plaquettes alone. Its source is C:174–177: winding around both fibre circles puts a gauge transformation near one central sign; the transverse equation then contracts its logarithm to zero. This statement applies separately on each fibre because `2r^2<=delta_0` and `r<=epsilon_1(n)`. It gives `g_b=s_b`, `xi'_b=xi_b`. On each base link, opposite signs would put a product of two radius-r exponentials at -1, distance 2pi from 1; its distance is at most 2r<pi. Thus signs agree modulo `delta s`, and injectivity of exp gives `Y'=Y`. Flatness of eps is unnecessary for this uniqueness assertion.


## 3. F5, including J1–J3 — HOLDS

P:355–386. Check the measure before the estimates. Order output links as fibre, then base. The differential of Theta is block triangular: its fibre diagonal blocks are M_xi, its base diagonal blocks are exponential differentials. Base-link derivatives with respect to gauges occur only below that diagonal and add no determinant. With normalized gauge Haar, the remaining fibre normalization is one constant c_F per fibre.

The redundancy is precisely 2^{|D|}, by F4. Flat sign fields in a fixed cohomology class number 2^{|D|-c(D)}. Their ratio is 2^{-c(D)}, exactly the printed factor. Thus the quotient is not obtained by silently deleting a Faddeev–Popov determinant: it contains J on each fibre. At xi=0, J(0)=sqrt(det Delta_0^F), a useful normalization check. The exponential Haar density is also correct: radial Lebesgue measure is `4pi s^2 ds`, and radial Haar is `pi^{-1} sin^2(s/2) ds`; their quotient is `sin^2(s/2)/(4pi^2 s^2)=varrho(s)`.

For J1, the orthogonal decomposition `range D_0^F` plus `T_F` gives singular values of M_0 equal to those of D_0^F together with ones. The derivative estimate is dimension free: each site starts two fibre links and

    sum_l (|lambda(y_l)|+|zeta'(l)|/2)^2
       <= (9/4)(||lambda||^2+||zeta'||^2)
       <= 4(||lambda||^2+||zeta'||^2).

Duhamel gives the stated first and second derivative bounds. Therefore `||M_0^{-1}(M_xi-M_0)||<=1/2` at the printed radius. For J2, the determinant derivative yields

    6n^2 [4sqrt(2)/sqrt(mu_n)+32/mu_n]
       <= 240n^2/mu_n.

Using `sup|zeta|<=||zeta||_2` gives exactly the asserted quadratic-form bound, not a dimension-free bound invented for the fibre. J3 follows from the printed nonnegative radial and tangential derivatives, with their finite limits at zero. No new Jacobian estimate beyond J2 is needed downstream.


## 4. F6 — HOLDS

P:392–407. The slab complex has two cyclic rows joined by M squares, hence is an annulus. A flat Z_2 field has one spatial holonomy, equal on both boundary circles. F4 makes that holonomy an actual gauge-orbit datum on the small chart. This is why K^g has two disjoint holonomy blocks, not because the full Wilson operator preserves those chart labels. The centre flip exchanges them.

The domain is a product in xi and Y. Time reversal sends temporal Y to -Y and exchanges the two xi slices, preserving this domain. F3's threshold inclusion gives (c3); the other indicator invariances are exact. A direct quotient count verifies the kernel normalization: the ring measure for one class is `(c_F^M/2) J varrho d zeta`, while the slab bilinear form is `(c_F^(2M)/2) J(zeta)varrho(zeta) varrho(Y_3) J(zeta')varrho(zeta')`. Dividing by the two square roots of the ring density leaves precisely c_F^M in k^+. No additional factor two or gauge determinant is missing.

The auxiliary checks F2–F3 (P:322–345) also hold on their stated small-defect domain: the two fibre windings give `1.2 n(theta_delta+2C sqrt(delta))`; neighbouring opposite signs would require `2pi<=2.4n eta+eta`; a negative base face sign contradicts its small defect. These facts supply the required inclusion of good slabs. F3(iii) is only the upper plaquette bound for flat signs; no inverse inclusion with the same radius is being used.


## 5. H3 — HOLDS AFTER CORRECTION

P:415–458; the essential local input is H2, not a mass inferred from global transversality. For mixed faces, `D_1 Z=zeta_b-zeta_b'+D_0^F W_e`; fibre transversality kills the cross term separately on every edge. The fibre gap supplies mu_n for each zeta and W. End-slice weights lose at most one half. Thus H2 gives `sum w_p |D_1 Z|^2 >= (mu_n/2)||Z||^2`. This uses the antiperiodic fibre spectrum C:90–97 and its product version S:321–331. H1's Duhamel estimate has constant one in the stated metric: each matrix norm is |a_i|/2, and four arguments give `sum|a_i|<=2|a|_2`.

All extension constants can be checked by hand. One valid cutoff is `c(s)=1-10t^3+15t^4-6t^5`, `t=(s-1)/3` on [1,4], constant outside. It is C^2, lies in [0,1], and has `|c'|<=5/8`, `|c''|<=2`. Set R=2r. On |a|<=2R, Taylor's bounds for N give

    ||D^2[c(|a|^2/R^2)N]||
      <= |a| + 2|a|^3/R^2 + (4/3)|a|^5/R^4 + |a|^3/(3R^2)
      <= (190/3)R < 128r.

There are at most six incident plaquettes per link, including n=2 with its distinct oriented lattice links. Therefore the extended action Hessian is at least `beta(mu_n/8-768r)>=beta mu_n/16`. Its off-argument blocks are at most `1/4+128r<=1/4+1/48<0.271` by the bare bound mu_n<=2, but the sharper needed figure must be checked: `128r<=mu_n/96<=1/48`. Consequently **the printed inference `1/4+128r<=0.26` at P:446 does not follow at r=mu_n/12288 when n=2**. The sharper cross-block estimate below repairs this step for H4. The convexity conclusion itself and the constants 128, 768 remain valid.

For the Jacobian cutoff put R_J=n sqrt(2) r. After removing the affine Taylor part, `|q_J|<=C_J |xi|^2/2`, `|Dq_J|<=C_J|xi|`, `||D^2q_J||<=C_J`. Its cutoff Hessian is bounded by `C_J(1+5x^2+4x^4)<=85C_J` for x=|xi|/R_J<=2. Its entire support lies in J's invertibility domain: `16n r<=sqrt(mu_n)`, since `n sqrt(mu_n)<=pi` and r<=mu_n/12288. Finally `beta mu_n/16-85C_J>=beta mu_n/32` exactly when `beta>=2720C_J/mu_n`. The Haar term has a convex C^2 extension as printed.

Correction, proved here: specify the quintic c above and replace clause (iii)'s `1/4+128r<=0.26` by `1/4+60r<=0.26`. Indeed the same polynomial has `|c'|<=5/8` and `|c''|<=10/(9sqrt(3))<2/3`. Repeating the displayed product rule with those bounds gives, for |a|<=2R,

    ||D^2(cN)||
      <= |a| + (7/3)(5/8)|a|^3/R^2 + (2/3)(2/3)|a|^5/R^4
      <= (251/9)R = (502/9)r < 60r.

Thus every off-argument block is at most `1/4+60r<=1/4+5/512=133/512<13/50=0.26`. The original 128r estimate may still be used for the global lower bound, so r_cvx, beta_J and all downstream constants stay unchanged. The first incorrect line is P:446: for n=2 and r=mu_2/12288 it asserts `13/48<=13/50`. This corrects an actual arithmetic implication; it does not refute the existence of the required extension.


## 6. H4 — HOLDS with corrected H3(iii)

P:460–469. Weight each entire fibre-transverse space by one scalar. This commutes with its orthogonal projection, with the Jacobian Hessian and with the walls; no componentwise locality inside a fibre is assumed. Symmetrization changes a cross-block H_ij by `(cosh(psi_i-psi_j)-1)H_ij`. There are three other arguments per plaquette and at most six incident plaquettes per link. Using the repaired 0.26 bound, the loss is at most `18(13/50) beta(cosh a-1)`. At a=a_n,

    1/32 - (117/25)/300 = 1/32 - 39/2500
       = 313/20000 > 1/64.

Thus the weighted lower bound is correct, with a small but positive margin. Using the uncorrected `1/4+128r` estimate would not give that margin for n=2.

The rate also admits an elementary check. Put x=mu_n/300<=1/150 and y=sqrt(mu_n)/12.3, so `y^2=(100/15129)mu_n<=200/15129`. From the cosh series, `(2k)!>=2*12^(k-1)` for k>=1, and hence `cosh y-1<=y^2/[2(1-y^2/12)]<=mu_n/300`. Therefore a_n>=sqrt(mu_n)/12.3>=1/(6.2n), without numerical evaluation of arccosh. The estimate a_n<0.12 follows since `cosh(0.12)>=1+0.12^2/2>1+2/300`.


## 7. Theorem A and its assembly — HOLDS AFTER CORRECTION

P:526–556. The correction is H3(iii) above; Theorem A's statement, window and constants do not change. The analytic premise HS0 is kept explicit here and checked below. No all-M result follows.

**Thresholds.** `delta_1=delta_0/(2R(n)^2)` gives `r_1=r_inj`. Since `delta_0<=(4200*61000)^(-2)n^(-32)`, this radius is below `mu_n/12288`, and below F5's radius. `C_J<=60n^4` implies `beta_J<=40800n^6`. The printed beta_0 dominates it. To check the exponential bound, put `a=48n^2/delta_1`. For beta>=4a log(4a), the increasing function `beta-2a log beta` is positive, and beta/2 also exceeds `232n^2/delta_1`. These two bounds give `beta delta_1/8>=6n^2 log beta+29n^2`, which dominates `6n^2 log beta+27n^2+log(6n^2)`. Thus epsilon_1 and M_1 have exactly the stated bounds. Also `2M epsilon_1<=1/(961n^2)` explains 1922 and 31.

**H5 as used here.** Its spectral argument does not assume T^g is positive semidefinite. The strictly positive continuous kernel on compact B has a simple positive eigenvalue Lambda equal to its norm and no eigenvalue -Lambda. Integrating the temporal Y variables makes the open-stack density a product of these kernels; endpoint square-root densities occur once at each end, precisely as in F6. The probability quotient in P:504 follows. The boundary vector 1 has positive overlap with the top vector. This proves the infinite-stack limit. HS and corrected H3–H4 bound its covariances by `C_F exp(-a_n d)` for every even d. For an eigenvector phi off the top vector, choose smooth F with nonzero overlap of F Omega_B with phi. Positivity of each term in the even-power spectral sum forces `|lambda_phi|/Lambda<=exp(-a_n)`. Density removes the differentiability restriction for the spectral conclusion. The prefactor may depend on this test and M; the extracted rate does not. This validates H5 as an implication from HS0, with the H3 repair.

**A1 — HOLDS with that repair.** Each c_4 parity restriction of T^g has one eigenvalue Lambda and the rest bounded above by Lambda exp(-a_n), plus zero. The rest-of-chart subspace contributes zeros; the map in P:549 need only cover the supported chart subspace, not literally every vector in the range if the block has a kernel. Compact-operator min–max gives

    (1-eta)lambda_0 <= Lambda <= (1+eta)lambda_0,
    lambda_2(T|H_+) <= lambda_0[(1+eta)e^(-a_n)+eta].

T>=0 bounds the bottom. For 0<a<=0.12,

    e^(-a/2)-e^(-a)=integral_(a/2)^a e^(-t)dt
       >= (a/2)(1-a) >= 0.44a.

Since `0.44/6.2>2/31`, the claimed interval and gap follow.

**A2 — HOLDS with that repair.** T1's infinite-cylinder limit, followed by the orthogonal projection off Omega within H_+, gives the covariance and the stated product of uncentered L2 norms. No finite-torus covariance is identified with this vacuum matrix element.

**A3 — HOLDS, independently of H3, H4, HS and H5 for its near-vacuum assertion.** F6 gives identical strictly positive blocks in the two parity sectors. T3 gives `||T-T^g||<=eta lambda_0`. Thus their top eigenvalues satisfy

    lambda_1(T|H_-) >= Lambda-eta lambda_0 >= (1-2eta)lambda_0.

It is strictly below lambda_0 by T1's simplicity. Here `eta<=1/(31n)<=1/62`, so

    -log(1-2eta) <= 2eta/(1-2eta) <= 3eta.

This proves the claimed upper bound on the full-space gap, including its beta exponential. The assertion about all remaining odd eigenvalues uses H5 and the H3 repair, exactly as A1 does. The two-state interpretation is a parity/holonomy statement; it is not two vacua of the strictly positive full operator.


## 8. Exact Z_2 model and the Lemma PE correction

**Z2-a — HOLDS AFTER CORRECTION of the quantifiers and normalization convention.** P:141–151. In the strip-flux counting convention, fix the overall normalization by the two-holonomy matrix

    [ E  O ]       E=((1+rho)^M+(1-rho)^M)/2,
    [ O  E ]       O=((1+rho)^M-(1-rho)^M)/2.

Its eigenvalues are the printed `(1+rho)^M` and `(1-rho)^M`. With normalized link Haar they are both multiplied by 2^(-M); the ratio, energy and conclusions are unchanged. This convention must be specified for “exact eigenvalues.” At fixed rho>0 the gap is bounded below uniformly over M>=4 by `4 log((1+rho)/(1-rho))>0`. Therefore P:149–150's literal statement that it is not bounded below uniformly in M at fixed rho is false. Correct statement: no positive lower bound independent of rho (hence of beta when rho=e^(-kappa beta)) holds uniformly over M>=4. This is the quantifier needed by Lemma PE, whose c is absolute. Also the gauge-invariant Hilbert space has dimension two only for this Z_2 model, not for SU(2).

**Z2-b formulas — HOLDS.** P:152–159. The even-parity partition sum is `((1+rho)^N+(1-rho)^N)/2`. Fixing one defect leaves odd parity on N-1 faces; fixing two leaves even parity on N-2. Division gives the two printed probabilities. Subtracting their product gives exactly

    4rho^2 r^(N-2) / [(1+rho)^4(1+r^N)^2].

It is positive and independent of separation for distinct faces. This is a finite-torus parity effect. No SU(2) activity is identified with rho by this computation.

**The inference at P:581 — FAILS.** The exact model does not show that a non-decaying additive term *must* occur in a torus bound. P:156–159 already notes the alternative: a very large C(rho) in a bound `C(rho)e^(-k d)`. For fixed rho, writing q=log(1/r)>0, the factor to be bounded is at most a rho-dependent constant times `exp(kM-qM^2)`, whose supremum in M is finite. The minimum required prefactor can be of order `rho^2 exp(k^2/(4q))` at the optimal even M, hence doubly exponential as beta grows. This refutes “must,” not Theorem B's sufficient additive-error estimate. Replace P:581's last sentence by: “The Z_2 model exhibits a parity contribution; a prefactor uniform in the coupling cannot simply ignore it.”

**Correction of PE's full-sector uniform gap — HOLDS.** This is existing work, not a new result of this check. The earlier source check `gap-s1-check-astra.md:168–189`, cited by P:95–101, already gives the fixed-volume low-temperature Polyakov-loop covariance obstruction. The new A3 strengthens it quantitatively for the actual transfer operator. For fixed n and M=4, beta→infinity is eventually in A's window, while `3sqrt(8 epsilon_1)→0`. Thus no positive absolute c/n can bound the full gauge-invariant gap for all sufficiently large beta and all even M. Neither the Z_2 calculation nor this implication refutes a positive gap depending on beta at a fixed beta, or the separately open flip-even all-M claim.


## 9. T1 and T2 — HOLDS

**T1 (P:232–262).** Each spatial plaquette occurs in two adjacent half-potentials; each time-like plaquette occurs once. Independent temporal Haar integration produces K and hence the trace identities for N>=2 (the task uses even N>=4). Gauge averaging is an orthogonal projection with normalized Haar; convolution by k commutes with it. The factorization `T=e^(-beta V/2) C P e^(-beta V/2)` is exact. The positive-type character expansion of k gives C>=0, including with the spatial centre twist: the twist is entirely in the real multiplication potential. Thus T>=0. The square-integrable continuous kernel makes T compact. Strict kernel positivity implies a nonnegative top eigenfunction is strictly positive, and a real top eigenfunction cannot have both positive and negative parts. Orthogonality then proves simplicity. Symmetries induced by measure-preserving coordinate maps fix its normalized positive eigenfunction, not merely its span. The trace-state limit is justified by `sum lambda_i^N<=lambda_0^(N-2)||T||_HS^2` and the strict spectral separation at fixed n,M,beta. With bounded insertions it converges to the stated vacuum matrix element.

This is the same transfer construction already present in the Sussman–Alpoge outline, GL8 (source lines in Repo search), with the placement of square-root convolution and half-potential interchanged. The present check verifies the spatial-twist specialization; it does not claim a new general transfer theorem.

**T2 (P:264–267).** A spatial mixed plaquette has either zero or two flipped links. In a temporal plaquette the two slice arguments acquire the same central sign, so their signs cancel. Consequently c_4 commutes with V, P, C and T, is a self-adjoint involution, and yields H_+ and H_-. It fixes the positive top vector by T1. No assumption that all gauge-invariant functions are flip-even is used.


## 10. Theorem B — HOLDS AFTER CORRECTION in its H3 input

P:558–573. The statement itself is unchanged. No M_1 restriction is needed for B; the error may instead make it uninformative at large NM. The event E_g is gauge and flip invariant. Its complement has probability p<=NM epsilon_1 by the one-point rectangular BAD bound and the chart inclusion. F5 makes the four flat classes equiprobable with identical coordinate densities; invariance under **both** base flips makes the observable pullbacks identical. This justifies the conditional law nu; dropping that invariance would be wrong for winding observables.

The distance weight on vertices is 1-Lipschitz after dividing by a_n. On each edge use its endpoint average. Adjacent or opposite edge averages on a square differ by at most a_n. On a mixed plaquette, the two vertex weights and the edge weight differ by at most a_n. Therefore the corrected H4 count applies on the torus. Every link on which F depends has both base endpoints in X, so its weight is exactly a_n dist(X,Y); the corresponding weights for G are zero. Orthogonal projection to T_F and the exponential differential both have norm at most one. With the Euclidean product metric on link tangent spaces this gives `||grad F~||<=Lip(F)`, as used. The metric convention is the Riemannian l2 product; using an l1 product would require converting the Lipschitz norm.

Here is a direct check of the possibly delicate 4p constant. Write the two conditional means as a_F=nu(F), b_F=e(F), and likewise for G. Then

    Cov_mu(F,G)-(1-p)Cov_nu(F,G)
       =p[Cov_e(F,G)+(1-p)(b_F-a_F)(b_G-a_G)].

For each variable in [-1,1], `Var_e(F)+(1-p)(b_F-a_F)^2<=E_e[(F-a_F)^2]<=4`. Cauchy–Schwarz for the sum of the covariance and rank-one forms bounds the bracket in absolute value by 4. This proves the displayed B estimate. It supplies a sufficient bound with a parity/error remainder, not the asserted necessity of such a remainder at P:581.


## 11. Lemma CP — HOLDS; its nontrivial-flux rider needs correction

P:622–645. The flat extension of the collar signs is an explicit hypothesis H_r; the proof never obtains it from a plaquette bound. Let q=|gamma|. A plaquette with a free link has every vertex within one base step in l-infinity of gamma. Thus its basepoint lies in gamma^+, giving at most `6n^2 |gamma^+|<=54n^2 q` affected plaquettes. There are at most `6n^2q` free links. Each bad basepoint in gamma selects a different plaquette in A_gamma, so the numerator is at most exp(-beta delta q). These facts do not require gamma to be connected.

For the denominator, extend the collar gauge arbitrarily over gamma and use the hypothesized flat signs on gamma^+. Restrict every free link to its radius-s ball about that reference, s=beta^(-1/2). This has Haar mass at least `(s^3/40)^(6n^2q)`. Every affected plaquette then has defect at most `2max(r,s)^2<=2(r^2+s^2)`, so its Boltzmann weight is at least `exp[-108n^2(beta r^2+1)q]`. Taking the ratio gives exactly the claimed bound since `108+6log40<131`. The two-threshold consequence retains H_r, including its flat-extension clause; delta-good collar data alone do not imply it.

**Flux rider, P:646–648 — HOLDS AFTER CORRECTION.** Replace “no such bound can hold” by: “This proof does not apply without H_r. Under a matched FLUX hypothesis, the conditional event that gamma contains at least one bad point is forced; an all-points-bad bound needs a separate argument.” Forcing at least one bad point is not the event in CP, which asks every point of gamma to be bad. Also the cited FLUX statement is for a filled rectangle, not arbitrary gamma. The rider is not used by Theorems A or B. No bound on flux-odd activities or string tension is proved by this check.


## 12. HS0 — HOLDS; its use is justified below

P:471–475. Here “uniformly convex” means 0<kappa<=Hess Psi; higher bounded derivatives mean orders at least three. The original [Helffer–Sjöstrand 1994 article](https://link.springer.com/article/10.1007/BF02186817) is subscription-only; only its publisher metadata and abstract were available. It was not read in full. The accessible primary source [Carlen, Cordero-Erausquin and Lieb, arXiv:1106.0709v2, section 2](https://arxiv.org/html/1106.0709v2#S2), equations (2.1)–(2.5) and (2.8)–(2.9), supplies the inverse-generator covariance method and gradient commutator. Those passages were read in the PDF text and HTML. They do not by themselves state all of HS0's bounded-derivative conclusions. Helffer's [1993 primary exposition, section 5](https://www.numdam.org/item/SEDP_1992-1993____A12_0.pdf), extracted text pp. XII-14–17, describes the vector equation and exponential weights but explicitly sketches solvability. Its scanned equations were not reliably available through this tool, so they supply no extra analytic premise here.

The missing regularity check can be written directly, instead of invoking an unspecified “second-order analogue.” Use the diffusion

    dX_t = -grad Psi(X_t) dt + sqrt(2) dB_t.

Its drift is globally Lipschitz since Hess Psi is bounded. The integral equation has a unique global solution by Picard iteration on successive finite intervals; linear drift growth prevents explosion. Differentiation in the initial point is differentiation of this same integral equation. Its Markov semigroup has generator L. Using the derivative bounds below, integration by parts gives `d/dt int P_t f dmu=int L P_t f dmu=0` for smooth compactly supported f; Gaussian tails justify the expanding cutoffs. Thus mu is invariant. These are the diffusion/semigroup ingredients also used by the cited primary construction.

Write J_t=DX_t, K_t=D^2X_t and B_j=sup||D^j Psi||. Along each path,

    dJ_t/dt = -Hess Psi(X_t) J_t,              ||J_t||<=e^(-kappa t),
    dK_t/dt = -Hess Psi(X_t) K_t-D^3Psi(X_t)[J_t,J_t],
    ||K_t|| <= (B_3/kappa)e^(-kappa t)(1-e^(-kappa t)).

The last inequality follows by variation of constants, using the norm bound e^(-kappa(t-s)) on the homogeneous propagator. Consequently, for compactly supported smooth g,

    ||D P_t g||_infinity <= ||Dg||_infinity e^(-kappa t),
    ||D^2 P_t g||_infinity
      <= ||D^2g||_infinity e^(-2kappa t)
         +(B_3/kappa)||Dg||_infinity e^(-kappa t).

For C^3 regularity there is also an integrable bound, not an implicit assumption. T_t=D^3X_t solves the homogeneous equation with forcing `-D^4Psi[J,J,J]-3D^3Psi[K,J]`, hence

    ||T_t|| <= [B_4/(2kappa)+3B_3^2/kappa^2] e^(-kappa t).

The chain rule bounds D^3P_tg by

    ||D^3g|| e^(-3kappa t)
      +3(B_3/kappa)||D^2g|| e^(-2kappa t)
      +[B_4/(2kappa)+3B_3^2/kappa^2]||Dg|| e^(-kappa t).

All three derivative bounds are integrable. Couple X_t^x with a stationary solution driven by the same Brownian path. Uniform convexity gives pathwise distance contraction, so

    |P_tg(x)-mu(g)| <= Lip(g)e^(-kappa t)(|x|+int|y|dmu(y)).

The first moment is finite by the quadratic lower bound on Psi. Thus `u=int_0^infinity(P_tg-mu(g))dt` converges locally uniformly, is C^3, and its first two derivatives are globally bounded. Differentiating the integral and using `dP_tg/dt=L P_tg` gives `-Lu=g-mu(g)`. This checks precisely the stronger HS0 formulation consumed by P, with no numerical or computer-assisted step. The ordinary finite-dimensional diffusion calculus is the analytic foundation; no statistical-mechanics decay theorem or spectral gap under examination is assumed.


## 13. Proposition HS and H5 — HOLDS AFTER CORRECTION

**HS (P:477–493).** Add to its general statement: “Each K_i has positive Lebesgue measure in E_i (or first work in its affine hull).” Without this, for example K_i={0} in R, the displayed density has zero normalizer and does not define a probability. The actual K_r factors for r>0 have nonempty interior in T_F or the stated edge space, so no application changes.

For the smooth whole-space case, differentiate HS0's equation to get `(-L+Hess Psi)v=grad G`. Test against `e^(2psi)v`. The scalar diffusion term gives `sum_i e^(2psi_i) int|grad v_i|^2>=0`; the Hessian term is bounded below by kappa' times `||e^psi v||_2^2`. The weight is constant in the integration variables. This gives exactly `||e^psi v||_2<=||e^psi grad G||_2/kappa'` and the printed covariance inequality. Bounded derivatives and Gaussian tails justify integration by parts by smooth expanding spatial cutoffs. The resulting cutoff errors vanish by their inverse-radius factors and integrable Gaussian tails.

Mollification of the potential preserves both Hessian inequalities because they are linear inequalities in the Hessian. For walls, the specific q in P has `q''=2-2/(1+u)^3` on u>=0; q, q' and q'' vanish at u=0. The radial composition is C^2 with bounded nonnegative Hessian. It remains so after restriction to T_F. Its block Hessian commutes with the scalar weight and therefore preserves the weighted lower bound. For a general compact convex K_i one can use `theta_i(x)=int_(sphere) q((v.x-h_K(v))_+)dv`, with q on nonnegative arguments as above. It is C^2, convex, has bounded Hessian, and vanishes exactly on K_i. A separating supporting direction gives positivity outside K_i; a neighbourhood of that direction has positive spherical measure. The one-dimensional sphere is interpreted as its two atoms.

For fixed wall coefficient first mollify, then remove the smoothing. As the wall coefficient tends to infinity, `exp(-Psi-N theta)` is dominated by `exp(-Psi)` and converges to its restriction to K. Positive volume gives a nonzero limiting normalizer. F and G can be replaced by C^1 compactly supported extensions agreeing near the compact K, which justifies dominated convergence also for gradients. This handles the printed general C^1 observables and corners without a boundary sign assumption. In particular the weighted inequality used by A and B is valid after this domain qualification.

**H5 (P:495–512).** HOLDS after the H3 cutoff correction; its spectral argument is checked in section 7. There is no new correction to its constants or spectral conclusion. HS0 supplies the needed smooth analysis and the preceding wall argument supplies the actual product domain. The boundary vector can be any strictly positive vector with nonzero overlap; using 1 in the printed coordinate kernel is valid.


## Disposition and scope

| Statement | Verdict | Qualification |
|---|---|---|
| Rectangular BAD; T3 | HOLDS | Global trace-power estimate; same epsilon |
| F4 | HOLDS | Uses the actual one-fibre uniqueness input |
| F5, J1–J3 | HOLDS | Local determinant and 2^(-c(D)) are correct |
| F6 | HOLDS | Two supported holonomy blocks exchanged by c_4 |
| H3 | HOLDS AFTER CORRECTION | Specify the quintic; replace 128r by 60r in clause (iii) |
| H4 | HOLDS | Uses corrected H3(iii); all constants unchanged |
| Theorem A, A1–A2 | HOLDS AFTER CORRECTION | H3 repair; stated finite window only |
| A3 near-vacuum bound | HOLDS | T3 and F6 suffice; no HS input |
| A3 remaining odd spectrum | HOLDS AFTER CORRECTION | Uses corrected H3 through H5 |
| Z2-a | HOLDS AFTER CORRECTION | Counting-measure normalization; fix beta/rho quantifier |
| Z2-b exact covariance | HOLDS | Model statement only |
| PE full-sector uniform-gap correction | HOLDS | Existing obstruction; quantitative A3 strengthens it |
| Necessity of additive torus term, P:581 | FAILS | A coupling-dependent prefactor can absorb the term |
| T1; T2 | HOLDS | Explicit positive Wilson operator and flip sectors |
| Theorem B | HOLDS AFTER CORRECTION | H3 repair; same rate, prefactor and 4NM epsilon_1 |
| CP | HOLDS | Requires the flat collar-sign extension H_r |
| CP flux rider | HOLDS AFTER CORRECTION | At-least-one event and actual FLUX domain only |
| HS0 | HOLDS | Analytic derivative check above; original 1994 full text unread |
| HS | HOLDS AFTER CORRECTION | Positive-volume factors; application already satisfies it |
| H5 | HOLDS AFTER CORRECTION | H3 repair, HS domain and checked HS0 |

The five correction sites are H3's coefficient, Z2-a's convention/quantifier, P:581's necessity claim, CP's flux rider and HS's general domain. Only H3 changes a numerical step used in the main assembly, and its repair preserves the theorem's printed constants. No claimed finite-window spectral conclusion is refuted. The ordinary full-sector uniform-in-beta gap remains false; this is not a new obstruction to the flip-even target.

Additional source checks: `open-core.md` and `l17c.md` had no matching target/HS label. A narrow five-ref search for `Langevin semigroup|Poisson equation.{0,50}convex|(^|[^[:alnum:]_])HS0([^[:alnum:]_]|$)` completed with no hits; the earlier unbounded-substring HS0 query matched unrelated words and is not used. The local library search, excluding P and this output, also returned no HS0 supplier. Supplemental chunk/obligation searches for Z_2/Z2, local mass, restricted ensemble, centre flip and twisted thin found no matching row. These are recorded searches, not absence theorems.

No computations or tests were used as mathematical evidence. No numerical guide in P was rerun or relied on. The 1994 journal full text was blocked by subscription access; local PDF retrieval also failed on DNS, and local Poppler tools were absent. The accessible primary text and the explicit analytic check above are the actual HS evidence. CA full-index searches were locators only; no new CA theorem or Balaban estimate is imported. No claim is made about odd M, the all-M expansion, order-one coupling, string tension, a continuum limit or an audit status. Only this report was written. It remains local and uncommitted; no external post or push was requested.

RESULT: T3, F4–F6, T1–T2, the exact Z_2 covariance and CP hold; H3's 0.26 step is repaired by the explicit quintic bound 60r, preserving H4, Theorem A's finite window and Theorem B's additive-error bound with their printed constants; A3's near-vacuum bound holds without HS; HS0 and its weighted use pass with the stated domain qualification; the fixed-rho no-uniform-gap wording, the forced-additive-torus-term claim and CP's flux rider require the corrections above. This is research text, not an audit, and grants no status.
