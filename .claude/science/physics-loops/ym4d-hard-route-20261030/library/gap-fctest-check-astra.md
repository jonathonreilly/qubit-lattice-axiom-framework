## Repo search

Target-specific prior digest is absent. The November 8 repository digest
concerns other targets; its transfer-operator pointer is reused below.

Searched `origin/main`, `pr/10114`, `pr/10133`, `pr/10134`, `pr/10141` in
`/Users/jonreilly/Projects/Physics`, using the requested bounded `git grep`
over Markdown and TeX. Ref revisions were respectively
`3e13676f02af206100abfb2875521904e8f53cda`,
`f76f6c649cff7dffbab664d8976e680e8f287fe9`,
`89faef229ff6e6bde42baad15ed8270c2f4087d8`,
`1e70c7211a2cdbc39001e619f1dd89db45e25851`, and
`c73ad7b177d94f89ff37b77386936e3d52b48b05`.

Terms: `gap-fctest|LSI-vac|fisher.{0,25}contract|gradient.{0,25}contract|vacuum slice chain`
(head 80; cap not reached, no exact target hit). Follow-up:
`one.plaquette.{0,40}(chain|transfer)|frozen.slice|MASS_GAP_LOCAL_BLOCK|hypercontract.{0,25}(vacuum|slice)`
(head 65; cap reached, discovery only). Relevant source comparisons:

| Hit | Exact statement and closeness |
|---|---|
| PR 10114, `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md:34–42,68–149` | Defines `T=A K A`, `T psi=lambda_0 psi`, and the vacuum law `psi^2 dU`; distinguishes it from transition-normalizer measure `A psi dU`. Its one-link convolution satisfies `kbar_B W_C=r_f^b W_C`. Same transfer frame and useful character normalization; it does not check row 946 or supply Fisher contraction at beta 2.3. Credit this earlier Astra construction. |
| PR 10134, this lane's `parts/upper-chain.md:1416–1423` | The entropy/Fisher route is recorded as gaining nothing over the regular-part cross-ratio when rare wells remain. Different RG conditional laws and target; no prior result for this test. |
| `origin/main:research/mass-gap/library/gap-transfer-check.md`, `gap-limit-astra.md`, and prior digests | Search hits point back to the same finite-transfer construction. They are retrieval pointers, not new independent suppliers. |

Other hits concern Gaussian Wick contractions, nonlinear background-field
iterations, or a frozen algebraic word slice. They do not identify the
vacuum Fisher ratio. The bounded search is not an absence theorem.
A follow-up, capped at 40 lines, with
`gap-fctest|LSI-vac|vacuum slice chain|Fisher.information contraction`
returned no lines on all five refs.
The registry has no hit for `fctest`, `lsivac`, `(FC)`, `Fisher`, or
`slice chain`. FINISH assigns this check to row 948 and the proof attack
to row 947. This report does not take over that attack.

The SA index README, chunk 02:85–108 and obligations:54–76 were read before
SA 2195–2245 and 2313–2335. GL3 gives
`c_l=(2 exp(-beta)/beta) I_(2l+1)(beta)`; GL8 gives the positive
gauge-averaged transfer and `Z_s(0)=Tr L^s`. Both are indexed as proved in
detail. These are Sussman–Alpoge's results, with Claude and Codex credited
as authors of their text. The scalar `exp(-beta)` cancels in normalized
transitions. Neither passage is the present Monte Carlo check. Index
searches for log-Sobolev, hypercontractivity, Fisher and gradient
contraction returned no hit. Exact-term searches for log-Sobolev,
Monte Carlo and Fisher information in CA-I/II/III also returned no hit;
this does not assert absence under other terminology. Source files are
the supplied copies at `31a47c543775`; their directory has no readable
Git HEAD. No Balaban estimate is needed or imported here.

Provenance: Codex, configured gpt-6-astra/xhigh; checkout
`f1c3de09bbfdbdb048a26fe47593eb5caceb64d6`; 2026-11-14.
This is row 948, a research-text check of row 946, not an audit or status grant.
Numerical evidence is GUIDE only and cannot discharge a proof obligation.

## Finding and statement verdicts

Read row 946 in full, row 941:73–120 and 293–455, and all three Python
sources in `guide/lane946/`. The row 946 note hash is
`044c6ea12941a45d00e82002772344216bd43d3ca5e71aa0d98fa69c53536814`.

The overall conclusion **HOLDS AFTER CORRECTION**: no reported run
produced a refutation. The code targets a finite open-cylinder ratio.
The exact transfer/gradient identities hold. The claimed universal
downward bias fails. Sampling errors, vacuum convergence and physical
interpretations need the narrower wording below. No proof input is supplied.

Line references in this table refer to `gap-fctest-opus.md` at the pinned
commit. A GUIDE verdict covers the stated model and available arithmetic.

| Statement / lines | Verdict | Scope or required correction |
|---|---|---|
| Definitions of the vacuum law, P and ambient metric, 48–57 | HOLDS | Match row 941 (A1)–(A3); the tangent norm is the unit-quaternion sphere norm. |
| `(FC)_theta => (GC)_theta`; exact R(f)>=1 refutes theta<1, 58–61,395 | HOLDS | For a nonconstant smooth gauge-invariant f on the same box, use g=1+epsilon f>0 and divide by epsilon squared. |
| Cut flip and winding-line parity, 65–66 | HOLDS | Every spatial plaquette meets the cut evenly; each once-winding line meets it once. |
| Small-box versus seed-box distinction, 68–75 | HOLDS AFTER CORRECTION | No small-box measurement establishes or refutes the seed-box inequality. A finite-cylinder threshold crossing also needs vacuum-error control. |
| E1, endpoint weights and nu_K convergence, 79–85 | HOLDS | Finite compact SU(2) graph; full endpoint spatial action; asymptotic rate has a box-dependent constant and no supplied numerical error bound. |
| E2, conditional independence, 86 | HOLDS | Open halves are independent under the equilibrium law given the middle slice. |
| E3, transport and conditional law, 87–91 | HOLDS | Matches `slices_su2`, including inverse placement on the backward temporal links. |
| E4, finite-cylinder score and R_K limit, 92–97 | HOLDS AFTER CORRECTION | The identity and limit hold; “without bias except” omits covariance, ratio and equilibration errors. |
| Inner chain needs no burn-in, 99–102 | HOLDS AFTER CORRECTION | True if the starting outer configuration is an equilibrium sample. A 200-sweep cold start does not prove that premise. |
| Independent-half product removes same-half squared-noise bias, 103–106 | HOLDS | Conditional independence removes that particular additive variance term. |
| `(1-O(tau/n))^2` scalar/downward bias, 106–108 | FAILS | Cross-lag covariances need not be proportional to the true covariance; explicit failure below. |
| Wilson-loop gradients and Gram denominators, 109–111 | HOLDS | Distinct links; shared-link terms retained for sums, and for the cube product by the product rule. |
| Jackknife formula, 112 | HOLDS | Correct delete-one-chain standard-error formula; it is not an exact coverage or bias bound. Original arrays are absent. |
| Autocorrelations reported for every base observable and outer S, 113–114 | FAILS | Code records selected first-location series and only outer lag 1, not those claimed integrated times. |
| Free-photon spectral reference and hand flux sum, 115–119,161–169 | HOLDS AFTER CORRECTION | Correct vacuum formula; decimals are rounded. The sampled open cylinder has the finite-K correction below and requires removal/quotienting of zero modes. |
| One-plaquette reduction and reference computation, 120–123,181–189 | HOLDS AFTER CORRECTION | Correct character normalization and metric cancellation. Quadrature and finite character/Ritz truncations are numerical approximations, not exact infinite-space theta_GC. |
| Observable definitions, 126–131 | HOLDS | All requested families are implemented; “one plane” in the zero-momentum sum means one orientation across the entire spatial slice. |
| Pass/fail criteria, 124,133–138 | HOLDS AFTER CORRECTION | Correctly applied to printed estimates as a GUIDE screen; not a rigorous refutation rule for the vacuum target. Historical preregistration is not independently verified. |
| Sampler, transport, gradient and denominator self-tests, 143–159,176–179 | HOLDS | Saved self-test log passes and code exercises these identities. Static mathematical checks below support the implementations. |
| C1/C2 calibration PASS arithmetic, 191–212,326–328 | HOLDS | All recorded tests meet the written tolerance, using recorded errors. “A few percent” describes plaquette/mode central values, not every nonlinear calibration. |
| b1, b5 and cube tables, 218–278 | HOLDS | Match JSON and run logs. These are finite-cylinder estimates with reported statistical errors. Cube was simulated, not solved exactly. |
| K=6 versus 8 and n=300 versus 600, 280–303 | HOLDS AFTER CORRECTION | All differences are within 1.5 combined reported errors. Only side 4, beta 2.3 was tested; neither zero bias nor a 0.7% bias bound follows. |
| Side-6 table and trends, 305–324 | HOLDS AFTER CORRECTION | Numbers match. Local plaquette ratios rise 17–21%; replace “neither family shows growth” by “no estimate approaches 1.” |
| Variational matrices and population span supremum, 332–337 | HOLDS AFTER CORRECTION | Correct Gram/Rayleigh construction; empirical maximization is a noisy estimate, not a certified variational lower bound. Its numerator is not unbiased. |
| Variational and beta-3.5 figures, 339–358 | HOLDS | Match saved JSON/logs as reported GUIDE figures. Missing arrays prevent independent matrix/error recomputation. |
| Serial timing and memory summary, 360–362 | HOLDS AFTER CORRECTION | Stage logs show serial runs across 30m53s, peak printed RSS 1.142 GB. Lock acquisition, `nice` and free-memory assertions have no saved receipt here. |
| Result tables and NOT REFUTED, 366–389,399–400,436 | HOLDS AFTER CORRECTION | No reported crossing; call the quantities estimates of R_K, with the statistical/systematic limits below. |
| “No thin-vortex double well”; local scale controls contraction, 401 | FAILS | A few low Rayleigh ratios cannot exclude a slow observable or a rare well. Preserve only the measured comparisons. |
| Winding-line trends identify small-box physics, 402,414–416 | HOLDS AFTER CORRECTION | The trends hold for the tested functions; flux-energy and large-box explanations remain hypotheses. No gap or theta=e^(-2E_1) identification was measured. |
| Seed-box (FC)/(GC) remain OPEN; row 947's refutation switch is not triggered, 403–419 | HOLDS | This report does not reassess or prove row 947's inequality. |
| Reproduction paths and credit, 421–434 | HOLDS AFTER CORRECTION | Source scripts and JSON/logs are present; raw `.npz` files are not. Definitions and inherited transfer/character work retain the credits above. |

## 1. Probability law and code-to-definition check

Write `b=exp(-V/2)` and `h_j=T^j b`. `Lat4` includes each spatial
plaquette at every time, endpoints included. Integrating temporal links
inserts gauge projections. Thus the middle density and transported
forward conditional are exactly

```math
\nu_K(dx)=\frac{h_K(x)^2\,dx}{\int h_K^2\,dx},\qquad
\pi_x^{(K)}(dw)=\frac{T_0(x,w)h_{K-1}(w)}{h_K(x)}\,dw.
```

The backward law agrees by time reflection. Freezing x disconnects the
two open halves. Haar invariance under the endpoint gauge transformation
gives the transported w of E3. All x-dependence in its normalized law is
`exp(beta <x,w>)`; the factor `exp(-V(x)/2)` cancels. Differentiating
the normalized integral proves A3 for P_K. The code projects w at x
before accumulating and multiplies the two covariances by beta squared.
There is no missing potential derivative, factor of two, or gauge volume.

Strict positivity of the finite-box transfer gives its simple positive
Perron vector. Applying the smooth kernel after spectral convergence
also gives convergence of the derivatives needed for R_K. Symmetries
of b restrict its excited overlaps to the invariant, centre-even sector.
This justifies the asymptotic limit, not a quantified error at K=6.
P_K need not preserve nu_K at finite K. Calling it the stationary vacuum
chain is therefore an actual measure identification error.

`fct.py:202–276` has the correct SU(2) update for a nonzero staple A=kV:
`U=X V^*` gives `Re(UA)=k X_0`. In the large-alpha rejection sampler,
the proposed s=(1-X_0)/2 has density proportional to
`sqrt(s) exp(-2 alpha s)`; acceptance `sqrt(1-s)` produces the Haar
factor `sqrt(1-X_0^2)`. The small-alpha branch rejects directly from Haar.
Overrelaxation `U -> V^* U^* V^*` preserves Haar and `Re(UA)`.
No two links in a colour share a plaquette, so the simultaneous updates
preserve the conditional Wilson law. This establishes the invariant law
of the update, not finite-time equilibration from the cold start.
An exactly zero staple is an unhandled corner: replacing k by 1e-300
leaves V=0, producing a zero quaternion before normalization. This is
a null event for these continuous equilibrium laws and is not evidence
of a defect in the saved runs; a general-purpose sampler should use
a direct Haar draw there.

For a loop with distinct links, differentiating one link gives a tangent
vector of squared norm `1-c^2`, c its normalized real trace.
`loop_grads` retains the appropriate conjugation for reversed links.
`ObsSU2.den` retains shared-link cross terms for the square/plane sums;
distinct winding lines have disjoint links. The cube observable uses the
product rule, including all shared-link contributions. `score_rows`
forms each linear combination before its half-product, as required.
The frozen slice is a view, but `tab_frz` never updates it; the code
also checks bitwise equality. These checks cover the requested A3 bridge.

## 2. The finite-sample bias claim fails

For a fixed x assume stationary conditional samples. Let
`C=Cov(a_0,F_0)` and `D_n=n^(-2) sum_(i,j) Cov(a_i,F_j)`.
The implemented covariance in `Acc.cov`, with denominator n, obeys

```math
E\widehat C=C-D_n,\qquad
E[\widehat C^F\!\cdot\widehat C^B]=
(C-D_n^F)\cdot(C-D_n^B).
```

Even if the two sampling schedules agree, the answer is `|C-D_n|^2`.
The difference from `|C|^2` is `-2<C,D_n>+|D_n|^2`, with no fixed sign.
Different colour orders in the two halves do not improve that assertion.

A two-sample counterexample is checkable by hand. Take independent
stationary signs X,Y. Resample X independently each step; retain Y with
probability 3/4 and flip it with probability 1/4. The product chain is
reversible with uniform law. Set `a=X+Y`, `F=X-Y`. Then
`C=1-1=0`, while both lag-one cross-covariances are `-1/2`.
For n=2, `D_2=(-1/2-1/2)/4=-1/4`, so `E C_hat=1/4`.
Two independent copies give `E[C_hat^F C_hat^B]=1/16>0=C^2`.
This refutes the asserted statistical inference from independence and
stationarity. It is not a counterexample to Wilson (FC), nor evidence
that the particular SU(2) estimates have upward bias.

For iid samples only, `D_n=C/n` and the factor is exactly `(1-1/n)^2`.
At n=300 this would be about 0.99334. The measured autocorrelation of
one f, or of one product a*f, does not determine the required signed
cross-lag sum for every score coordinate and observable. A ratio of
sample means also has finite-sample bias. Delete “without bias”, the
universal downward sign, and the claimed 0.7% SU(2) bound.

## 3. Calibrations and recorded arithmetic

For a transverse photon mode with spatial eigenvalue s, completing
the Gaussian square gives `r=exp(-omega)`, `cosh(omega)=1+s/2`.
The derivative of P f for the linear mode is r times that of f; hence
R=r squared. At s=2 and 4 these are `(2-sqrt(3))^2` and
`(3-2 sqrt(2))^2`. The plaquette has momentum weight
`s_1+s_2`. On side 4 each s_i has multiplicities 1,2,1 at 0,2,4.
This gives row 946's displayed `8F(2)+24F(4)+24F(6)+8F(8)` divided
by 256. It independently checks `photon_exact`'s incidence-matrix path.
The exact expression, rather than the rounded 0.016335, is the reference.

The actual finite-cylinder mode has
`r_1=1/(1+s)`, `r_K=1/(2+s-r_(K-1))`. Its exact linear-observable
ratio is r_K squared. For s>=2, r<=r_K<=1/3 and
`0<=r_K-r<=r_1 (1/9)^(K-1)` follows from the recurrence.
At K=6 this bounds the absolute squared-ratio difference by
`2/(9*9^5)<4e-6`. Thus using the vacuum reference is harmless at
the stated 5% calibration floor, but it is not finite-K exactness.
The Gaussian full link measure has gauge/constant zero modes.
This calibration is understood on the curvature quotient: tested
fluxes and differences w-x discard the common zero-mode coordinates.
It does not construct a normalized law for all unfixed link coordinates.

For the single plaquette, GL3 and the four distinct links give
`C chi_n=((2/beta) I_n(beta))^4 chi_n`, without an extra division by n.
The code's `G diag(c_n) G^T` is the character representation of
`exp(beta cos(theta)/2) C exp(beta cos(theta)/2)`.
Differentiating its quotient gives `dP`; the full-link gradient factor
4 cancels between numerator and denominator. Thus the reference model
and normalization agree with row 941. Forty characters, 800 quadrature
nodes and 23 nonconstant Ritz functions are still finite approximations.
Agreement with row 941, which uses the same character method, is
reproduction, not an independent derivation of an exact numerical value.

All JSON ratios equal their stored numerator divided by denominator.
The tables, final-round logs and `logs/summary.md` agree to their printed
precision. The following calculations use the stored errors, not newly
estimated errors; full bookkeeping is `/tmp/ym4d-row948-check/arithmetic.txt`.

| Check | Arithmetic outcome |
|---|---|
| Photon flux / mode 1 / mode 2 relative discrepancies | 0.505%, 1.565%, 1.107%; all PASS the stated tolerance. |
| Single-plaquette c, beta 2.3 / 2.6 | 1.963% / 2.476%; PASS. |
| Nonlinear single-plaquette functions | All PASS, but beta-2.3 tanh(10c) differs by 49.5% and c cubed by 15.4%. Their 3-error relative tolerances are 124.5% and 28.0%. This is weak calibration for those functions. |
| K=8 versus K=6, side 4 beta 2.3 | Largest difference 1.275 combined reported errors (cross-section lines). |
| n=600 versus n=300, same box/coupling | Largest difference 1.446 combined reported errors (zero-momentum plaquettes). |
| Largest R_hat+3 error: b1 / b2 / b3 / b4 / b5 / cube | 0.14537 / 0.16547 / 0.15353 / 0.03290 / 0.21547 / 0.0008912. |
| Variational beta 2.3 / 2.6 | 0.144742 +/- 0.004694; 0.221743 +/- 0.011465. Printed figures agree; original matrix recalculation unavailable. |
| Beta 3.5 cross-section probe | 0.307475 +/- 0.020634, with upper screen 0.36938. |

The calibration distinguishes a missing beta-squared score factor: at
beta 2.3 it would divide the plaquette prediction by 5.29, far outside
its 6.44% tolerance. Its nonlinear checks are much less discriminating.
No original recorded estimate satisfies the proposed refutation threshold.

## 4. Uncertainty, variational scope and interpretation

`jack_ratio` correctly deletes whole independent chains, which avoids
pretending that every inner draw or spatial location is independent.
Correlations between rounds within a chain therefore do not by themselves
invalidate that grouping. It provides a sampling-error estimate given
equilibration; it does not bound common initialization or boundary bias.

`finish` records only c at the first plaquette, tanh(10c) there, the first
winding line, and four components of one local product a*c. It does not
record times for smeared observables, plane/line sums, cube monopoles,
each covariance component, or the variational matrices. Outer S has
only a demeaned lag-one statistic with 4–8 rounds, not an integrated
time. For iid rounds, even the ratio of expected adjacent covariance
to variance is `-1/(m-1)` under this centering. Negative recorded lag
one therefore cannot establish absence of a slow component. The code
and saved output support selected diagnostics, not “every series”.

`zmvar.py:35–65,90–123` builds the correct population Gram matrices and
restricts the denominator to its positive numerical range. Exact
population matrices give a lower bound on the full supremum. Empirical
matrices have both covariance bias and noise, and choosing their largest
eigenvalue is adaptive. A delete-one jackknife does not certify a lower
bound or a three-sigma coverage guarantee, especially near degenerate
maxima. This matters to a future claimed crossing; none occurred here.

The reported K/n comparisons concern only b1/b2/b3, all at beta 2.3 on
side 4. The side-6, beta-2.6, cube and variational runs have no such
matched stability pairs. Their errors must not inherit that validation.
The finite-K approximation and 200-sweep cold-start assumption remain
unquantified, although the numerical comparisons are useful GUIDE evidence.

Keep the observed ordering of the tested functions. Delete “no thin-vortex
double well” and “theta ... is available”: no supremum over all f or
positive g was controlled. The strongest measured line modes are
centre-odd small-box probes, but their interpretation through a flux
energy, confinement, or `theta=e^(-2E_1)` is not established by these data.
The recalled glueball value does not enter this check or any verdict.

## 5. Evidence limits and completed checkpoint

All row 946 Python files, JSON outputs and logs were read. No `.npz`
file is present, despite the save calls in both drivers. Consequently
the original jackknife errors, autocorrelation estimates and variational
matrices cannot be independently recalculated here. Preserve the raw
chain sums/matrices and diagnostic series if a threshold crossing is
ever to be assessed. The summary script correctly formats ordinary
run JSON; its default glob would fail on the later variational JSON,
which lacks an `R` member. Pass an explicit list for that summary.
Also, `zmvar.py` imports NumPy/SciPy before `fct` sets thread variables;
a standalone rerun should set those variables in its launch environment.
No saved launch command establishes that detail for the original run.

The criteria are explicit in Step 2. Their claimed registration before
the runs is not independently verified: a bounded commit listing finds
note commits before 08:11Z, but the needed historical blobs are absent.
`git show` at `2383a8744` and `60b2d84fe` attempted lazy retrieval and
failed because github.com could not be resolved. No historical diff
was run. Stage logs independently place C1/C2 at beta 2.3 before b1;
the optional beta-2.6 C2 was run after b5. Criteria were not changed
in this check.

Checkpoint: the text/code/arithmetic check is complete. Numerical reruns
were skipped: the sparse checkout lacks `scripts/lab_ops.py`, and the
required shared lock, located from its main-branch source, is
`/tmp/physics-lab`, outside the permitted scratch folder. Permission for
that narrow exception was requested but had not arrived when this report
was completed. A private replacement lock would not enforce the required
machine-wide exclusion, so none was used. No simulation was launched.

The raw-input hash manifest is `/tmp/ym4d-row948-check/input-sha256.txt`.
Only this report and scratch bookkeeping have changed. The report is
local, uncommitted and unpushed. Source notes, registries and science
status remain untouched. No additional proof or review lane was started.
The next decision belongs to row 947: these data supply no refutation
requiring its conditional change of target.

RESULT: HOLDS AFTER CORRECTION as a GUIDE report: row 946 supplies no refutation of (FC); its open-cylinder score and recorded calibration arithmetic hold, its universal downward-bias claim FAILS, and its finite-K, uncertainty and variational claims require the restrictions above. Vacuum (FC)/(GC) on the seed box remain OPEN; no status is granted.
