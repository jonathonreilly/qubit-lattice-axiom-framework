# Repo search

Target: FINISH row 926, checking row 923 at
`2956aee33aa52095e906d00fef81d05b5fb21b04`.

Terms searched on `origin/main`, `pr/10114`, `pr/10133`, `pr/10134`,
`pr/10141`: `THERM-DI-pin`, `gap-thermpin`, `gauge.Higgs model`,
`Hellmann.Feynman`, word-bounded `Proca`, `Bonati`, `closing level`,
`log.?36`. The first unbounded `Proca` query also matched “reciprocal”;
those hits are irrelevant. The task-specific prior digest is absent.
The November 8 prior digest was read; its targets are RG geometry,
reference laws and source bounds, not the present pin-rate check.

| Ref searched | Revision recorded in this check |
|---|---|
| origin/main | `4d88da5504d356762deb6b1a1c2695336af9fb81` |
| pr/10114 | `f76f6c649cff7dffbab664d8976e680e8f287fe9` |
| pr/10133 | `89faef229ff6e6bde42baad15ed8270c2f4087d8` |
| pr/10134 | `1e70c7211a2cdbc39001e619f1dd89db45e25851` |
| pr/10141 | `c73ad7b177d94f89ff37b77386936e3d52b48b05` |

The completed narrow global pass (head 70, below its cap) returned no
`THERM-DI-pin`, `gap-thermpin`, `gauge.Higgs model`, word-bounded
`Proca`, `0911.1721` or `closing level` match. Its log-36 hits concerned
unrelated scalar thresholds. The broader Hellmann–Feynman pass was capped;
it is only a locator. A further pass over the mass-gap, soft-route and
YM4D snapshot folders on all five refs located the thermal-continuity
statement below and unrelated geometric transports. No absence claim
rests on either capped output or a substring match.

| Relevant hit and range actually read | Exact statement and closeness |
|---|---|
| `origin/main:docs/NATIVE_GAUGE_TRANSFER_BLOCK_HELLMANN_MONOTONICITY_RUNG_EIGHT_BOUNDED_NOTE_2026-06-12.md:90–125` | For `T=E D E`, `T'=(JT+TJ)/2+E D' E`; a simple eigenvalue has logarithmic derivative `<v,T'v>/lambda`, with J contribution `<v,Jv>`. Same product-rule method on a finite block; not the pinned full SU(2) spectrum. Reused as prior method. |
| `origin/main:archive_unlanded/codex__gauge-perron-variational-proof-2026-04-25/docs/GAUGE_VACUUM_PLAQUETTE_PERRON_VARIATIONAL_ENVELOPE_THEOREM_NOTE_2026-04-25.md:290–320` | Symmetric insertion `exp(sB/2) T exp(sB/2)` differentiates its simple Perron logarithm to `<psi,B psi>`. Same half-weight algebra, a different source/transfer. It supplies no excited thermal rate. |
| `origin/main:research/mass-gap/library/gap-u-astra.md:313–336` | A finite-box rate K_B implies level transport and real-time VIR_K; a uniform summable eigenvalue tail gives joint continuity of the thermal sum and its t derivative for t>=4. Related finite-box regularity, explicitly not a box-uniform pin rate. |
| Local `gap-exit-max.md:466–497` | Identifies the fixed-length Higgs pin and proves HL/HL2 given V and DC*. Same model and exact starting bound; reused, not re-attacked. |
| Local `gap-thermdi-astra.md:96–217,313–382`, `gap-thermdi-check-opus.md:35–62` | Supplies P2, (P), the full-trace seed, characteristic consumer, and the all-flux endpoint. These are the same inputs; row 923's intermediate-h and CL deductions are what is checked here. |
| Local `gap-fw-gauss-opus.md:29–35,55–58,89–95`, `gap-fw-gauss-check-astra.md:282–314` | Gives oscillator thermal factors, the derivative `1/(2 sinh omega)`, and three Proca towers on a free spatial box. Same Gaussian method with different spatial boundary; the factor two is already explicit there. No pin-cost theorem there is being redone. |

The local filename search also found witness-moment Proca comparisons,
brainstorm Hellmann–Feynman proposals, and status echoes. They supply no
additional rate. In particular `gap-brainstorm-max.md:334,445,484` names
NOCRIT-HF as a missing uniform logarithmic gap-derivative bound; it is a
proposal, not the requested check. The exact target searches in
`open-registry.md`, `open-core.md` and `l17c.md` found no competing owner
for row 926. The upstream work above remains with its existing owners.

**Outline/account lookup.** Read the SA-index README, then chunk-02
neighbouring rows 80–102. SA 2195–2240 proves GL3 and its Bessel series;
SA 2313–2336 constructs the positive gauge-averaged transfer and GL8.
Those exact source ranges were read and are credited below. Searches
of chunk files, `obligations.md` and `ca-full/` for the pin/Higgs,
Proca, Hellmann–Feynman, closing-level and thermal labels found no
direct target. Unrelated “pinned” polymer and “Feynman” covariance
matches were not imported. This is a search result, not a claim that
the full account lacks every equivalent result. No CA proof is
re-derived or assigned new status. The SA source revision `31a47c543775`
is the user's supplied provenance; the on-disk SA directory is not a
Git checkout, so its revision could not be independently queried.

## Provenance and scope

OpenAI Codex, gpt-6-astra, xhigh (requested checker configuration).
Research-text check, not an audit; grants no scientific status. Only this
file is written. No numerical run is used to discharge any statement.
The source is `library/gap-thermpin-opus.md`, lines 1–165, read in full.
Line numbers below refer to that pinned source unless qualified otherwise.

Source SHA-256:
`85e7ea434b2be506b09cfaf431273ed5ecb2f12145244c48d57efc252e8a983b`.
Verdicts distinguish mathematical implications from GUIDE premises.
Tadeusz Balaban's estimates are not used in this check. No original
Balaban paper was obtained or read. The primary Bonati paper was read
online because the author's uncommitted download was absent here.

Checkpoint: all requested statements checked. The surviving SU(2)
obligation is still a box-uniform integrable relative rate. The operator
and absolute-bound exclusions do not dispose of that obligation. Next
decision for the lead: correct row 923 before using those exclusions or
the Gaussian constant. No source, registry, FINISH row or status file
was edited; the check is saved locally, uncommitted and unpushed.

## 1. Model identification and exact transfer factors

**HOLDS — lines 27–34, 48, 50, 52–54, 71–74, 77–79; P1/P2 identity clauses.**
All positively oriented links are pinned, including temporal links. With
normalized Haar measure, introduce one SU(2) matrix phi at each vertex and
change variables to `V_xy = phi_x^* U_xy phi_y`. The plaquette traces are
unchanged, each hopping trace becomes `tr V_xy`, and the remaining phi
integral is one. Thus the measures agree exactly. Bonati's Wilson action
adds the harmless constant `beta N_p` to the negative exponent convention
used here. Their hopping coefficient is `h = kappa`. This identification
already occurs in `gap-exit-max.md:466–480`; credit that prior construction.

The one-link factor is also prior work, not new to row 923. Ethan Sussman
and Levent Alpoge, with Claude and Codex as authors of their text, prove
GL3 at SA 2197–2231. Their coefficient includes `exp(-beta)`. Removing
that scalar and replacing beta by h gives exactly

\[
 a_j(h)=\frac{2}{h}I_{2j+1}(h),\qquad
 \partial_h\log a_j=\frac{I_{2j+2}(h)}{I_{2j+1}(h)}+\frac{2j}{h}.
\]

The positive series in SA 2225–2231 gives
`a_j(h) ~ h^(2j)/(2^(2j)(2j+1)!)`. In particular `a_0(0)=1`
and all other coefficients vanish. On each vertex-group isotypic space,
the Q_h eigenvalue is the product of these factors. For beta,h>0 the
commuting factors C_beta and Q_h are positive and injective; sandwiching
by the bounded invertible M_h preserves both properties. “Positive
definite” means injective positivity, not a positive lower spectral bound.

For a normalized simple eigenvector f_j, the product rule gives

\[
 T_h'=\tfrac12(V_sT_h+T_hV_s)+M_hC_\beta Q_h'M_h.
\]

Taking its diagonal matrix element proves the stated Hellmann–Feynman
formula, and hence `E_j'=w_0-w_j`. The long-time differentiated trace
gives `w_0=4|B|v_(h,infinity)`. At crossings, diagonalize the derivative
on the finite-multiplicity eigenspace or differentiate its trace. The
Boltzmann factors then give (P-R) with the displayed sign. At real t,
`v_(h,t)` must mean the spectral score; there is no fractional-slice torus.

**HOLDS AFTER CORRECTION — line 75, correction 91, and line 109's charged-level premise.**
The correction at line 91 removes the asserted charge-labelled energy
bound but must also remove “its d_h E < 0” and “never the cost”. The
coefficient asymptotics describe Q_h, not eigenbranches of M_h C_beta Q_h
M_h. Those eigenvectors need not have fixed vertex charges. No sign for
every such level over the pin path follows. Keep only the coefficient
asymptotics and the exact criterion `E_j'>0 iff w_j<w_0`.

## 2. Operator exclusion

**HOLDS — line 81's trace identity and sufficient operator bound.**
On finite spectral subspaces the diagonal of H_h' is the level derivative
(with the derivative block at a crossing). Passing to the differentiated
trace gives the pinching formula. Its vacuum diagonal is zero. Therefore
`Q H_h' Q <= c H_h` implies (P-R), provided the stated form and trace
domains exist. This does not assert boundedness of H_h'.

**FAILS — line 81's assertion “cannot hold ... whenever the vacuum moves”,
and its SU(2) use at lines 128, 150, 165.**
The n-copy example proves a statement about n independent copies, not
about every volume family with a moving vacuum. A local counterexample
to that universal inference is

\[
 H_b(h)=H_1(h)\otimes I+\sum_{i=2}^{b^3}|1\rangle_i\langle1|,
 \quad H_1(h)=R(h)|1\rangle\langle1|R(h)^*,
\]

where R is a plane rotation. The vacuum moves. Every nonzero energy is
at least one and `||H_b'||=1`, independently of b. Thus
`Q H_b' Q <= Q <= H_b`, with c=1 in every box. Moving one site alone
already disproves the asserted implication. Alternatively
`H_b=I-|Omega_b(h)><Omega_b(h)|` has `QH_b'Q=0` even when every factor
of its product vacuum moves; that second example is not a local Hamiltonian.

The source's narrower product calculation is correct. For an n-fold sum
of the SAME moving two-level Hamiltonian, choose each of the last n-1
factors proportional to `omega+epsilon chi`, epsilon=(n-1)^(-1/2),
and put an excited vector in the first factor. Their total energy tends
to `e_1+e`; the cross term in the derivative is
`2a sqrt(n-1)/(1+1/(n-1))`, with all diagonal contributions bounded.
Thus no uniform c exists for that product family. No tensorization or
analogous lower bound has been proved for the actual interacting SU(2)
family. Correct replacement: this example defeats a GENERAL inference
from a moving vacuum; it does not exclude the SU(2) operator route.

## 3. Convexity and the absolute-bound argument

**HOLDS — lines 83–85.** The second t derivative of X is the thermal
variance of E. Hence U=-X' decreases and
`U(t) >= integral_t^(t+1) U(r) dr = X(t)-X(t+1) >= U(t+1)`.
Since c is nonnegative, (P-int) is sufficient at integer t. It does not
by itself supply the real-time characteristic inequality.

**HOLDS — line 87 as a reading of HL2 with its named inputs.**
`gap-exit-max.md:483–497` supplies the field lower bound, weighted row
sum and box-comparison bound quoted here. Its distance is d_n=n/2-5/2.
This check uses HL2 conditionally on its stated Theorem V and Lemma DC*;
it does not redo those separately owned proofs.

**HOLDS AFTER CORRECTION — line 89's quotient calculation.** If BOTH
displayed numerator and denominator bounds hold, division gives exactly
the displayed exponential majorant. For a prefactor bounded above and
below independently of b, that particular majorant is uniform on
`4<=t<=b/24` precisely when `m_1>=m_2`. This is a limitation of that
majorant, not a necessary condition for the actual ratio to be bounded.

The parenthesis does not supply its denominator hypothesis. A variational
upper bound `E_j<=m_2` alone gives neither a positive lower bound on E_j
nor control of the normalization. The actual formula is

\[
 U(t)=\frac{\sum_{j>0}E_j e^{-tE_j}}{1+S(t)}.
\]

If N_1 levels also obey `E_j>=m_->0`, they give only
`U>=m_- N_1 exp(-m_2 t)/(1+S)`. A bound on S or a separate extensive
lower bound is still needed. Also, negative level derivatives can cancel
in the numerator. No theorem excluding all absolute-bound methods follows.

**FAILS as a proved SU(2) exclusion — lines 89, 128, 150, 165's log 36 claim.**
The algebraic GUIDE comparison is

\[
 \log(h/\beta)-\log((h-6\beta)/(36\beta))
 =\log36+\log\frac{h}{h-6\beta}\longrightarrow\log36.
\]

But its two exponents are not proved numerator/denominator bounds for
the same SU(2) thermal ratio. HL2 compares two symmetric tori over a
distance `d_n=n/2-5/2`; it supplies no `exp(-m_1 t)` cylinder estimate
with that same m_1. The other exponent is a Gaussian guide, not an
SU(2) variational estimate. Keep the displayed difference as GUIDE only.
The assertion that these methods are excluded for SU(2), or that a ratio
expansion is the only possible proof, is not established.

## 4. Transported seed and closing-level lemma

**HOLDS — line 55 and Lemma CL, lines 104–105; P1's transport clause and P3.**
These are implications from the stated full-trace seed and (P-R), with
the same positive transfer in each axis. They do not prove either a
rate or a closing SU(2) level. Here is the domain and constant check.

Put `M=exp(I)`, `a=ceil(Mn)`, `b=24a`. The supplied seed is
`X_(h_0)(n;(4n)^3)<=64 delta_n`. Lemma E' enlarges each side from
4n to b with factor `b/(4n-n)=8a/n<=8(M+1)`. Hence

\[
 X_{h_0}(n;b^3)\le[8(M+1)]^3\,64\delta_n.
\]

For an endpoint h, set `I_h=integral_h^(h_0)c(q)dq<=I`.
In forward parameter s=h_0-h the inequality is `X_s+c t X_t<=0`.
The characteristic ending at t=a starts at `a exp(-I_h)>=n`.
All its times lie in `[n,a]`, inside the required `[4,b/24]`.
Monotonicity of X in t proves the same bound at that endpoint h,
uniformly in h, using the fixed full-path M. Since
`delta_n=4608 beta n^4 2^(1-d_n)/(d_n-1)->0`, the right side vanishes.
If `E_1(h(a))<=kappa/(24a)` for every sufficiently large integer a,
then the left side is at least `log(1+exp(-kappa/24))>0` along
`a=ceil(Mn)`. This is the contradiction. No limit at fixed b as
`t->infinity` was used, and no levelwise rate was assumed.

**HOLDS — line 136's endpoint extension for the compact pinned model.**
At each fixed box, `Q_h->P` in norm and `T_h->T_0` in trace norm.
The latter implies operator-norm convergence and convergence of the
ordered positive eigenvalues. The first two nonzero eigenvalues at h=0
therefore give continuous E_1. An endpoint bound `E_1(0)<=kappa/b`
with kappa>0 supplies some h(b)>0 with `E_1(h(b))<=2kappa/b`.
There is no requirement that h(b) be uniform in b. CL applies.

**HOLDS AFTER CORRECTION — line 106's applications.** A tunnelling
doublet with `E_1<=C exp(-sigma b^3)` implies the CL hypothesis for
all large boxes; that implication is elementary. The existence of such
a doublet for this model is an additional premise, beyond detecting a
first-order thermodynamic line. Neither its transfer-gap bound nor a
critical dynamical exponent is proved here. A critical point alone does
not supply the specific `E_1<=kappa/b` hypothesis. Label both as
conditional applications, not refutations obtained from Monte Carlo alone.

## 5. Seed shift

**HOLDS — line 124 and P5, conditional on the same HL2 inputs.**
The pointwise absolute bound in HL2 permits moving the lower endpoint
of the integral to any `h_0'>=78 beta`. It does not require monotonicity
of the signed difference `e_n-e_(2n)`. With `d=d_n>1`, direct integration
gives

\[
 \int_{78\beta}^\infty 2\left(\frac{36\beta}{q-6\beta}\right)^d dq
 =72\beta\frac{2^{1-d}}{d-1}.
\]

Multiplication by `4(2n)^4=64 n^4` gives `4608 beta n^4`, as claimed.
The limiting constant cancels between the two volumes. Theorem D(a,b)
then bounds `X(n;(2n)^3)` by delta_n; three applications of E', each
with factor `4n/(2n-n)=4`, give `X(n;(4n)^3)<=64 delta_n`.
All three ingredients are existing results, credited in the source;
this verifies their composition, not a new high-pin seed theorem.

## 6. Gaussian (Proca) calculation

**HOLDS AFTER CORRECTION — lines 117–118, normalization only.**
For `U=exp(i A.sigma/2)`, the displayed quadratic action is correct.
In the convention `S_2=(1/2)<A,precision A>`, its precision is K/4,
so its covariance is `4 K^{-1}`. The stated matrix inversion is correct
for the rescaled K. Fourier phases are removed by using bond midpoints.
Its longitudinal eigenvalue is h, and its three transverse eigenvalues
are `h+beta phat^2`. The pole and its rank-three residue are correct:

\[
 4\sinh^2(\omega(p)/2)=h/\beta+q^2,
 \qquad q^2=\sum_{i=1}^3 4\sin^2(p_i/2).
\]

**HOLDS — line 119's Fock spectrum for h>0.** Prior work already gives
the oscillator trace and derivative `d omega/d(m^2)=1/(2 sinh omega)`
in Claude Opus's `gap-fw-gauss-opus.md:29–35,55–58`; its massive
Proca reduction is at 89–95, with the determinant argument in Codex's
`gap-fw-gauss-check-astra.md:282–314`. Those concern spatial free walls.
The following checks the periodic spatial specialization and keeps its
zero momentum; it is no new general Proca or oscillator theorem.
For one colour and spatial momentum, split the spatial field into two
components perpendicular to q and one parallel component. Integrating
the temporal component gives the time-difference coefficient and the
on-site coefficient

| Oscillator | A (difference) | B (on-site) |
|---|---:|---:|
| Two transverse components | beta | h+beta q^2 |
| One longitudinal component | beta h/(h+beta q^2) | h |

The action of each real oscillator is
`sum_t [A(x_(t+1)-x_t)^2+B x_t^2]/8`. At q=0 all three components
have A=beta, B=h. In every case `B/A=h/beta+q^2`. The Gaussian integration
determinant contributes only a scalar per slice, which cancels in
`T/lambda_0`.

Here is a direct spectral check, without importing a Fock assertion.
The one-oscillator kernel is proportional to
`exp[-alpha(x^2+y^2)+gamma xy]`, with
`alpha=(2A+B)/16`, `gamma=A/4`. Let
`rho=sqrt(alpha^2-gamma^2/4)>0`. Gaussian integration shows that
`f_0(x)=exp(-rho x^2)` is its top eigenfunction. Conjugation by f_0,
followed by division by its eigenvalue, gives a Gaussian Markov operator
with conditional mean `r x`, where
`r=gamma/[2(alpha+rho)]`. It maps a polynomial of degree k to a
polynomial with leading coefficient multiplied by r^k. Self-adjointness
and Gram–Schmidt in the invariant Gaussian measure therefore give
orthogonal polynomial eigenfunctions with eigenvalues r^k. They are
complete: a function orthogonal to every polynomial has zero Gaussian
Laplace transform near zero, hence zero Fourier transform and is zero.
Finally `(r+r^(-1))/2=2alpha/gamma=1+B/(2A)`, so `r=exp(-omega)`.
Tensoring the real Fourier modes gives exactly
`E=sum n_(p,s,c) omega(p)`, with nine oscillators per spatial site.

**HOLDS AFTER CORRECTION — lines 120–121, P4 and the Gaussian RESULT clause.**
The first failing equality is line 120:
`sinh(omega) d omega = d(h/beta)`. It must be

\[
 2\sinh\omega\,d\omega=d(h/\beta),\qquad
 \partial_h\omega=\frac{1}{2\beta\sinh\omega},\qquad
 c_*^G(h)=\frac{1}{2\beta\omega_0\sinh\omega_0}.
\]

The function `omega sinh omega` strictly increases for omega>0.
Every nonvacuum Fock level consequently has `E'/E<=c_*^G`, which
implies (P-R) for every real t>0 and every box. The zero-momentum
one-quantum level attains this levelwise bound. Taking t to infinity
at a fixed box also shows sharpness among rates valid at all times.
Its integrated cost is

\[
 \int_{h_1}^{h_0}c_*^G(h)dh
 =\log\frac{\omega_0(h_0)}{\omega_0(h_1)}.
\]

The printed rate is twice c_*^G. It remains a valid upper bound, but
its integral is TWICE the printed logarithm; it cannot attain the gap
comparison with equality. The corrected sharp cost has the claimed
divergence `-(1/2)log(h_1/beta)+O(1)` as h_1 tends to zero. The printed
rate instead has divergence `-log(h_1/beta)+O(1)`.

Independent hand test: choose `h/beta=1/2`. Then `omega_0=log 2` and
`sinh omega_0=3/4`. Differentiating `2 cosh omega_0=2+h/beta` gives
`omega_0'=2/(3 beta)`, whereas line 120 gives `4/(3 beta)`.
This exact test needs no floating-point values. The decimal costs in
line 121 are only guides to the corrected logarithm, not evidence for
the original rate/cost pair; their printed decimal rounding was not rerun.

**HOLDS AFTER CORRECTION — line 122's integer-time statement.**
It is a necessary low-temperature asymptotic, not a sufficient rate at
all integer times. For one oscillator,

\[
 X(t)=-\log(1-e^{-t\omega}),\quad
 -\frac{\partial_hX(t)}t=\frac{\omega'}{e^{t\omega}-1},\quad
 D(t)=\log\frac{1-e^{-(t+1)\omega}}{1-e^{-t\omega}}.
\]

The required ratio tends to `omega'/(1-e^(-omega))` as t tends to
infinity, but is strictly larger at finite t. At `omega=log2`, t=4,
it is `(omega'/15)/log(31/30)>2 omega'`, since
`log(31/30)<1/30`. Thus using the leading-term rate as sufficient fails
even for one oscillator. Its integrated asymptotic rate is exactly
`log[(exp(omega(h_0))-1)/(exp(omega(h_1))-1)]`, approximately the
frequency difference when both frequencies are large. The source has
not proved a finite-time (P-int) rate with that cost.

**HOLDS AFTER CORRECTION — lines 121, 137–138's photon endpoint.**
The h>0 oscillator calculation itself proves the divergent cost. At
h=0 a noncompact periodic Maxwell potential has harmonic zero modes;
its unmodified Gaussian integral and normalized vacuum trace are not
the compact endpoint assumed by CL. A claim about its h=0 photon trace
must specify gauge and zero-mode removal. No such endpoint construction
or trace-norm limit is supplied here. Compact U(1) transfer-gap claims
remain conditional on the stated, unproved photon-level premise.

## 7. Bonati et al. and the transition inference

**HOLDS — lines 95–101's reading, as GUIDE and source attribution.**
Read the primary [Bonati, Cossu, D'Elia and Di Giacomo paper, v2](https://arxiv.org/html/0911.1721v2),
equation (1), introduction, sections 2.1–2.3, 2.5–2.6 and Appendix A.
Its normalization matches h=kappa. It reports a crossover at beta=2.5,
correlation length about ten, first-order evidence at 2.775, 2.79 and
2.8, and endpoint fits `2.7266(16)` and `2.7299(36)` in equation (6).
The quoted kappa value at 2.775, large-volume double peaks at 2.8, and
the merging crossover lines match. The introduction attributes the
large-kappa/small-beta analyticity region to Fradkin–Shenker and
Osterwalder–Seiler. This check does not independently verify their papers.

**HOLDS AFTER CORRECTION — lines 102, 106, 157 and 165's extrapolations.**
The endpoint is a fitted estimate with uncertainty, not an exact dividing
value 2.73. The paper supplies neither an all-beta phase-diagram theorem
nor a transfer-spectrum tunnelling bound. Reading the window [2.3,2.6]
as crossover-only is a GUIDE extrapolation. A refutation above the
endpoint additionally requires CL's quantitative finite-box closing-level
premise. A smooth local-observable crossover also supplies no full-trace
rate. The source's “not blocked” must mean only “not ruled out by this
phase-diagram guide”; it cannot mean that transport is established.

## 8. Remaining statements and summary coverage

The following records the remaining substantive lines. Plans, download
logs and authorship claims are provenance, not mathematical statements.

| Source lines | Verdict | Exact scope or correction |
|---|---|---|
| 10 versus 27; 25–46 | HOLDS AFTER CORRECTION | The introductory “spatial links” is corrected by the actual all-link model. The definitions, (R), (G), (CE), seed and restricted-time caveat agree with `gap-thermdi-astra.md:96–217,313–382`. The cancellation and full-flux scope agree with `gap-thermdi-check-opus.md:35–62`. G requires the separately stated all-time domain. |
| 59 | HOLDS | The quoted SEED-FP is the quantified target at `gap-finishline-opus.md:113–123`. A single fixed bare beta does not establish a uniform first-passage family. This is a comparison of the two contracts, not a recheck of the account's continuum construction. |
| 61–67, 135, 137–141 | HOLDS AFTER CORRECTION | CL applies IF the compact-model photon or flux levels satisfy the stated bounds. The freezing locations, transfer splittings, eight nearly degenerate finite-beta levels, and high-pin assertions for every compact group are not proved here. Keep them as GUIDE assumptions; “must fail” means conditional on them and the starting seed. No new verdict on those separately owned inputs. A Langevin gap is not a transfer gap. |
| 108–113, 159's last sentence | HOLDS AFTER CORRECTION | The claimed low-h glue/flux locations assume confinement and the gap being sought. The high-h SU(2) energies are Gaussian guides. Neither excludes closing levels. The cost and box-size estimates are heuristics using an all-time comparison that the restricted-time hypothesis alone does not supply. Keep “analyticity not supplied”; delete any implication that every expansion method is ruled out. |
| 127 | HOLDS AFTER CORRECTION | In the Gaussian model `X=sum_modes -log(1-exp(-t omega))` is extensive, and `S=exp(X)-1`. The dilute-mode estimate `N exp(-t omega)` estimates X (and the one-excitation contribution), not the full S when that number is large. The printed S≈18 cannot justify a full-trace estimate. Many-excitation control is indeed needed. |
| 129–131, 161 | HOLDS AFTER CORRECTION | No SU(2) rate is supplied on any interval. A common wrapping expansion is a proposed sufficient approach, not a proved necessary one or the unique obstruction. A typical mean activity and a plaquette adjacency count do not prove a KP norm bound. “No obstruction in principle” and “technical” are unsupported by a Gaussian pass; remove them. The threshold near 340 beta remains GUIDE. |
| 141's full-flux requirement | HOLDS | At h=0 the full trace includes all flux sectors. The transported seed bounds their sum too. No projection has removed the flux obligation. This is already the point of row 908, not a newly proved confinement result. |
| 142 | HOLDS AFTER CORRECTION | `chi_adj(-U)=chi_adj(U)` proves centre-flip symmetry, and its maximum at ±1 gives the stated Z_2 limiting weights at fixed volume. A transition on this exact path, its location, and a closing level IN THE EVEN TRACE are additional unproved inputs. The adjoint trace pin freezes an entire group-valued frame; an ordinary single adjoint Higgs need not be that model. A named adjoint-Higgs analogy does not identify it. CL cannot be applied to the even sector merely from odd-flux near degeneracy. |
| 144 | HOLDS AFTER CORRECTION | The displayed estimate has row sum at least one only for `6 beta<h<=24 beta`; for `h<=6 beta` its positive field lower bound is unavailable. Failure of this bound does not prove that every worst-case method fails or that every possible proof must be typical-case. |
| 149 (P1) | HOLDS | Model identity, exact (P-R), and intermediate-h transported seed, with the premises in sections 1 and 4 above. |
| 150 (P2) | HOLDS AFTER CORRECTION | Factors, derivatives, pinching, convexity and integer sufficient form hold. The universal operator exclusion FAILS. The absolute-bound exclusion and log 36 must be restricted as in sections 2–3. |
| 151 (P3) | HOLDS | CL and its compact endpoint extension, with the supplied seed. |
| 152 (P4) | HOLDS AFTER CORRECTION | Use `1/(2 beta omega_0 sinh omega_0)` for the stated exact logarithmic cost. The larger printed rate works but costs twice as much. |
| 153 (P5) | HOLDS | Seed shift, with the existing HL2 and trace-algebra premises. |
| 155–163 | HOLDS AFTER CORRECTION | READ/GUIDE/ARGUED retain the limits above. The source's claimed downloads and numeric execution are not independently authenticated. No rate for actual SU(2) is proved by this check. |

No interval rate or first-passage seed has been supplied. The useful
surviving conclusions are the exact identities, the conditional seed
transport and CL, the seed shift, and the corrected Gaussian control.
The main failures are the asserted universal operator exclusion and its
promotion to an SU(2) exclusion, and the claimed proved SU(2) log-36
exclusion. No statement of SU(2) gap closure follows from this report.

RESULT: Model identification, one-link factors, Hellmann–Feynman identities, transported seed, Lemma CL and seed shift HOLD with their stated inputs; the universal operator exclusion FAILS, and the claimed proved SU(2) log-36 exclusion FAILS; Gaussian control HOLDS AFTER CORRECTION to c_*^G=1/(2 beta omega_0 sinh omega_0), retaining the exact logarithmic cost and its divergence; Bonati's endpoint reading HOLDS as GUIDE, but transition-to-CL conclusions require an additional quantitative closing-level premise; THERM-DI-pin for SU(2) remains OPEN, with no interval rate supplied and no status granted.
