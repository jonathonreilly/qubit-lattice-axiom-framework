# Hostile review of the bounded MGX author unit

Date: 2026-10-29. **One narrow binding source-domain correction is required.**
The conditional covariance, transport and spectral arguments are supported;
the actual crossover and continuum physical mass gap remain UNDECIDED.

This is a fresh delegated reviewer context, with the inherited model and
reasoning configuration unchanged. It is same-family review (Codex reviewing
Codex), not cross-family replication. I did not author MGX. The raw note and
its sources, including earlier reviews, were available during this review;
this is not a blinded experiment. Independence below consists of rebuilding
the decisive mathematics, including a different covariance proof, rather
than adopting previous review labels or diagnostic counts.

## Frozen source and authority boundary

- Reviewed `MGX.md`, all 387 lines, SHA256
  `979953ced67ed7a3f115dd6e81565cc04321ab12c0a5118cd7b6d4d39b07c9a2`.
  This matches `checks/mgx_author_freeze.sha256` and the identical recovery
  copy `checks/mgx_author_v1.md`.
- All 16 entries in `checks/mgx_sources.sha256` matched their actual bytes.
  The source baseline is `f401d825dcdaac36b13f0aee885f16099d066abb`.
- Governing skill and proof-search reference were read at the explicitly
  supplied cached-main revision `01589af3faf806b736c42dc2f3bd625e9edead9f`.
  Remote freshness was not independently established. Repository `AGENTS.md`,
  `SCIENCE_WORKFLOW.md`, both briefs and `PROCESS_LIGHT.md` were read.
  Cached execution instructions supplied no scientific premise or status.
- This is the requested author-unit readiness review only. No Git, PR,
  ledger, audit, retained-status or integration action is authorized by it.
  `LAND` would mean readiness of this bounded note, not an actual landing or
  a physical-gap result. My only written output is this report.

## Binding finding and item verdicts

**F1 — Source integrability needs its domain, MGX lines 121–127.** Equation
(4) introduces source insertions without a boundedness or exponential-moment
condition, then asserts that the source-weighted integrals exist whenever the
kernel does. Compactness and normalization of the kernel are insufficient for
arbitrary insertions. A positive compact-group density can have an unbounded
L2 insertion with no positive exponential moment. For example, near the
identity of SU(2), radial Haar volume scales as `r^2 dr`; an insertion `1/r`
has finite second moment locally, whereas its positive exponential does not
have a finite integral. The same example can use a plaquette holonomy and
therefore be gauge invariant. The kernel `K=1` does not repair this.

**Binding fix:** qualify the setup of (4) by *bounded local finite-cutoff
insertions F_i and finite source parameters J_i*, or state the required
exponential-integrability hypothesis explicitly. The bounded version is
already the exact domain in `MASS_GAP_CONSTRUCTION_ASTRA.md:393–397`.
This correction does not require strengthening the L2 hypotheses used by
the covariance identity and section 5, which do not require exponential
moments. No change to the overall UNDECIDED conclusion is requested.

| Item and frozen MGX lines | Verdict | Fix or preserved boundary |
|---|---|---|
| Target, dense observable family, same hierarchy and endpoint, 18–63 | Supported within the supplied Wilson model and fixed-spacing scope | None. Keep MG0–MG5 open and the SU(N) group restriction explicit. |
| Action normalization, flow window and endpoint comparison, 65–117 | Supported as a normalization identity and conditional flow comparison | None. Keep the final-output exception and formal one-loop continuation qualifications. |
| Exact coarse/source weights, 119–135 | HOLD for the overbroad integrability assertion | Apply F1. Existence/locality of the actual all-field coarse action remains a separate producer obligation. |
| Zero-Hessian control and full source conditioning, 136–170 | Supported | None. The example is not an actual RG output or a reflection-positive countermodel. Both terms of total covariance remain indispensable. |
| Weighted interaction/covariance criterion, 172–248 | Supported conditional finite-volume theorem | None. Its all-field weighted row condition is an unproved input for the actual S4' output. |
| Complete transport, onset/window and fixed-time limit, 250–307 | Supported conditional implication | None. The localized conditional means, conditional remainder, MG0 matching and MG4 nontriviality are genuine open hypotheses. |
| Direct physical transfer and physical-rate conversion, 309–345 | Supported conditional implication and exact diagnostic | None. The diagonal alternative still needs common physical-time matching; an auxiliary stochastic gap cannot be substituted. |
| Final decisions, scientific scope and attribution, 347–387 | Supported | None beyond F1. No GO, universal obstruction, infrared producer, continuum existence or physical-gap theorem has been established. |

## Independent mathematical checks

**Normalization and controlled interval.** With Hermitian generators
`tr(T^a T^b)=delta_ab/2`, expansion of a plaquette gives
`1-Re tr(U_p)/N = a^4 sum_a(F^a_mu,nu)^2/(4N)+o(a^4)` for each unoriented
plane. Summing planes converts this to coefficient `beta_W/(8N)` in front
of `integral F^a_mu,nu F^a_mu,nu`, hence `beta_W=2N/g_std^2` for the
displayed standard continuum convention. FLOW instead defines the Wilson
coefficient as `u=1/g_flow^2`. Thus the endpoint really requires
`g_flow^2>=32` and `g_std^2>=64N`; the local-block `g_K` cannot silently be
identified with `g_flow`.

The standard one-loop premise gives `du/d log(mu)=4N b_0`, hence
`b=11N^2/(12 pi^2)` with the stated `b_0`. This coefficient is a named
premise here, not a new loop calculation. From
`u_(k+1)=u_k-b_k-rho_k`, summation and the uniform remainder bound produce
(2). The proof uses only inputs through `n-1`; its separate tuning theorem
keeps the output through `K` weak as well. Shrinking gamma to at most one
is legitimate and gives `u_k>=1` on those guaranteed tuned nodes. The
logarithmic continuation reaches a formal finite length ratio, but extending
its validity to `u=1/32` is not licensed by this estimate. I checked these
statements against FLOW's definitions and argument, not its historical
status headlines.

**Endpoint constants and physical scope.** The raw local-block construction
retains `A k P_gauge A`, its actual Perron factor and all spatial plaquettes.
The half-slab row is `14 beta`; the physical output comparison gives
`Q=12 beta+beta^2/(1-14 beta)` and input defect `beta`, hence
`r=beta/(1-Q)`. At `beta=1/32`,
`Q=3/8+1/576=217/576`, so `r=18/359`. These increase through the stated
positive interval. They are physical one-step constants only after the
actual slab/Doob comparison, not because the auxiliary heat-bath process
has a gap.

I also checked the raw finite-energy witness and infinite-volume injectivity
premises consumed by MGX: the witness uses operator positivity for the
rank-one comparison, then separately uses the nonnegative exterior kernel;
the finite-block Haar variance is `1/4` for SU(2) and `1/(2N^2)` otherwise.
The injectivity supplement uses bounded finite-boundary tilts, local Haar
domination to transport null sets, a countable exhaustion, nonzero Wilson
Fourier multipliers, and L1 martingale convergence. It does not infer
injectivity from finite-volume injectivity alone. Consequently the asserted
fixed-spacing logarithmic Hamiltonian and nonzero finite-energy sector are
consistent with the raw source. None of these arguments removes the
regulator or restores continuum rotations.

**Projection and source controls.** Since `s_p` starts at degree two,
`c s_p^2` has zero Hessian. The four center-valued plaquette assignments give
`0,4c,4c,0`, with mixed difference magnitude `8c`. Thus a marginal Hessian
cannot control all-field interactions. For square-integrable fine sources,
conditional expectation is an orthogonal projection in L2: decomposing each
source into its conditional mean and orthogonal residual makes the cross
terms vanish and gives (5), with the second term the conditional residual
inner product. For bounded sources, differentiating
`Z(J)/Z(0)=integral mu_c(dV) E[exp(sum J_i F_i)|V]` gives the same two
terms. At `K=1` the coarse means are constants and the entire fine connected
correlation remains in the conditional term/source-only logarithm. This
checks both direction and normalization of the source transport.

**A different derivation of the weighted covariance estimate.** I rebuilt
the real covariance bound by a source tilt and finite random-scan coupling,
rather than integrating the author's heat-bath covariance identity:

1. For normalized densities whose log ratio has range `L`, write the density
   ratio between `m` and `M`. Convexity bounds its positive deviation by
   `(M-1)(1-m)/(M-m)`; setting `M/m=exp(L)` and maximizing gives
   `(exp(L/2)-1)/(exp(L/2)+1)=tanh(L/4)`. Therefore the actual single-site
   influences are bounded by (6), including all normalizers.
2. Tilt the full law by `exp(h g)` for bounded real `g`. Its single-site
   conditional defect relative to the original law is at most
   `b_i(h)=|h| delta_i g/4`. Couple successive random single-coordinate
   updates of the two laws by maximal conditional couplings. Both marginals
   stay at their respective Gibbs laws. If there are `M` coordinates, the
   disagreement probabilities satisfy
   `p_(k+1)<=[(1-1/M)I+C/M] p_k+b/M`. The matrix has row sum strictly less
   than one, so iteration gives the limiting bound `p<=D b`, with
   `D=(I-C)^(-1)`. Telescoping a real local function over differing
   coordinates gives `|mu_h f-mu f|<=sum_ij delta_i f D_ij b_j(h)`.
3. Differentiate at `h=0` (boundedness justifies this) to obtain
   `|Cov(f,g)|<=(1/4) sum_ij delta_i f D_ij delta_j g`. This independently
   recovers the author's normalization, orientation and factor.
4. Every path contributing to `C^n` obeys the triangle inequality for time
   distance. Multiplying its edges by their exponential weights and summing
   gives row bound `q_*^n`; the resolvent therefore has weighted row bound
   `1/(1-q_*)`. The four real/imaginary covariances of a complex pair give
   the conservative factor one in (8).

There are six plaquettes incident to each four-dimensional link and three
other links in each. Each mixed Wilson oscillation is at most `4 beta_W`,
so the weighted row is at most `18 beta_W exp(nu)+epsilon_nu`. At the
endpoint, this is `(9/16)exp(nu)+epsilon_nu`, exactly the budget stated in
the note. A periodic time circle must use cyclic distance or a genuinely
safe window; the note explicitly retains that qualification. This estimate
does not require, and does not prove, a coarse physical transfer operator.

**Localization, fixed-time passage and density.** Write
`e_R=D_F exp(-kappa R)`. Replacing the centered conditional means by their
approximants costs at most `M_F e_R+(M_F+e_R)e_R`, bounded by the claimed
`(2M_F+D_F)D_F exp(-kappa R)`. For `R=floor(n/4)`, support separation is at
least `n/2-d_F`, and `exp(-kappa R)<=exp(kappa)exp(-kappa n/4)`.
Combining the three terms yields precisely (9), including its prefactor
and `c=min(nu/2,kappa/4,sigma)`. Positivity of its left side comes from the
matched fine reflected correlation; arbitrary coarse covariance is not
asserted positive.

Fixing an integer `n` first uses the common onset, eventually admissible
window, same-sequence convergence and `eta_a,F(n)->0`. It gives the
continuum bound at `n ell`, after which `n` may grow. For every
`0<=b<c/ell`, the spectral measure then bounds low-energy weight by
`A_F exp[-(c-b ell)n]`, forcing that weight to vanish. Boundedness of the
spectral projection extends this conclusion from the assumed dense
complex span to all of `Omega-perp`; a common rate is essential, whereas
prefactors and onset may depend on F. Nonzero excited space and strong
convergence of finite-energy projections supply finite excited infimum.
No exchange of cutoff removal with a large-time limit occurs.

**Direct transfer conversion.** Since `P` commutes with the vacuum
projection, writing `m=n b_a+s` gives the centered contraction `r_*^n`.
As `n>=t/(a b_a)-1>=t/ell_+-1`, it is at most
`r_*^(-1) exp[log(r_*)t/ell_+]` when `0<r_*<1`. The zero case is handled by
any larger positive contraction bound. The raw norm estimate does not
identify ground-state forms with finite-time-circle traces; the note
correctly leaves that matching as an actual uniform-limit obligation.
Finally `diag(1,exp(-a^2))` has energy `diag(0,a)` at time step a, confirming
that positive cutoff gaps alone do not give a positive limiting threshold.

## Coverage, limits and scientific disposition

The complete target, its review, finite-transfer construction/review,
local-block construction/review and injectivity supplement were read.
FLOW was read at lines 1–237, 392–458 and 4824–4851; the necessary coupling
conventions, hypotheses and flow/tuning proof are within that coverage.
I read AUDIT lines 160–194, the one-loop review's final scope at 353–378,
HANDOFF at 350–400, the crossover prior-art note at 1–42 and 214–252,
and its complete review. The crossover literature screen is context only,
not a transitive proof premise. A truncated aggregate tool response was
replaced by complete, untruncated reads of the affected source ranges.

Primary attribution/scope was checked directly against the
[Balaban publication record](https://scholarship.libraries.rutgers.edu/esploro/outputs/journalArticle/Renormalization-group-approach-to-lattice-gauge/991031665200104646),
[Dimock abstract](https://arxiv.org/abs/1108.1335v2) and
[Shen–Zhu–Zhu abstract](https://arxiv.org/abs/2204.12737v1). Dimock's cited
example is scalar phi4 in three dimensions. Those reads supply attribution,
not an external infrared theorem. No full-paper examination is claimed.

No numerical or symbolic experiment was run; the reported rejection of
`nice` was not bypassed. Historical diagnostic runners were not replayed,
and their PASS counts were not treated as independent evidence. Hashes
and file reading were bookkeeping. No editable prompt, scientific source,
audit file or ledger was changed by this reviewer.

The remaining producer is substantial: an actual all-field interaction
estimate at fixed physical block size plus complete localized fine-source
transport and its conditional remainder, or the direct uniform physical
transfer estimate, on the same nontrivial reconstructed continuum
hierarchy. The former is a stronger sufficient package than a mass gap;
the latter is essentially a gap estimate in transfer language once its
matching hypotheses are supplied. Neither is near closure merely because
its contract has now been stated. F1 is a bounded-note domain repair, not
resolution of any of these scientific obligations.

VERDICT: HOLD
