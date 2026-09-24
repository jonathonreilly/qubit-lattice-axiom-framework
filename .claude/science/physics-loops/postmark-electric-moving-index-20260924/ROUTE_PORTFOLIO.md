# Route portfolio

An earlier ten-worker review selected the fixed-time scalar/readout target. The 2026-09-24 next-route review covered ten distinct approaches: seven isolated worker reports and three exact checks performed by the author after the platform thread cap prevented further agent threads. Route choice is not review of the resulting theorem. Execution is being performed personally.

The main exercise reframing is to stop treating every fixed kernel entry as the target. Strong convergence of the prepared state reduces the readout to one scalar quadratic form. A weighted Jacobi perturbation estimate closes the prepared-state tail at rate (O(S^{-2})); the remaining problem is the scalar long-time phase.

| Route | Mathematical object and mechanism | Result or first decisive check | Status / strength |
|---|---|---|---|
| Single-profile scalar reduction | One-vector strong convergence and \(\|B_S\|\le1\) | Actual readout differs from \(1/3+(2/3)\operatorname{Re}q_S\) by at most (1.50\times10^4/S^2) | Proved conditional reduction; removes state-tail uncertainty |
| Fixed-index kernel decay | Entries of (e^{-itCN_S}Ve^{itCN_S}) | Decay of every fixed entry implies (q_S\to0) | Active sufficient route; stronger than target; one bad entry does not prove a readout wall |
| Bulk Bloch/WKB with crossing matching | 15-cell symbol, two mod-three resonant pairs, central layer, stationary phase | Local symbol and crossing matrices derived; next is a global quantization or propagation estimate | Active; terminal obligation target-equivalent |
| Spectral commutator / near-resonance split | Invert \(\mathrm{ad}_{N_S}\) away from resonant eigenvalue pairs | Exact diagonal/off-diagonal split added; dense pinching cross-check error (1.1\times10^{-17}) | Active; no uniform near-resonant bound yet |
| Translation-invariant reference | Fourier/Bessel kernel and stationary phase | Exact reference entries are (O(S^{-1})) at fixed nonzero time | Reference estimate is proved; transfer to finite spin at \(\theta\asymp S^2\) is still open |
| Endpoint eigenfunction cap | Buffered row-sum bound and weighted resolvent decay | Exponential leakage for eigenvalues \(\lambda\ge\epsilon\) | Proved partial barrier; low-energy endpoint sector and full scalar remain |
| Actual-readout separated subsequence | Certified subsequence of (S\mapsto\langle O\rangle_{S,1/4}) | Needs exact or interval-certified nonzero separation | Unexplored; finite scans are only exploratory |
| Derive supplied dynamics from axioms | Construct a native bridge from four axioms to hop map and preparation | Requires separate premise/physical-identification theorem | Separate upstream question; no axiom update supported |
| Exact five-site Fourier/differential route | Five component generating function for (N_S) | Exact differential representation; constant internal commutant is scalar | Equivalent until a nonconstant intertwiner yields phase control |
| Operator-norm phase sensitivity | Change (N_S) by (O(S^{-2})) while keeping coarse spectral data | Spectral rounding can force a revival in a comparison operator | Prunes norm-only inference, not the supplied-model target |
| Reversible Markov representation | Full generator written as an imaginary-time reversible-chain kernel | Exact rates; three-residue lumpability fails | Equivalent until a pointwise complex-kernel estimate is proved |
| Global transfer and action | Discrete WKB for the slowly varying Jacobi matrix | Principal action is (5 pi (2-sqrt(lambda))); primitive five-site roots remove the 15-fold readout-collision interpretation | Support only; global quantization and overlap estimates remain |
| Five-site Schur/Weyl pencil | Eliminate four sites between anchors in the resolvent and retain the two-energy period-three insertion | Root derived the 4x4 cell determinant recurrence, exact reduced anchor link, weighted two-energy overlap, and identity-character divided-difference metric; S=1,2,3,5 finite reconstructions agree to below 5e-14 | Exact representation established off cell-resolvent poles; pole/residue control and phase cancellation remain target-equivalent and open |
| Arithmetic weighted sums | Exact spectral phases with actual overlap weights | Moment law, Abel-sum criterion, and certified interior curvature swings at a tested spin; author diagnostic evaluates actual weights/aliases for S=24,48,96 | Open; actual weighted lag sums and aliases are jointly uncontrolled |
| Independent random phases | Replace deterministic phases by independent Haar phases | Variance concentrates around the diagonal ensemble | Failed inference for the exact phase sequence; randomization is not supplied |
| Exact residue symmetry | Test whether the observable commutes with the generator | ([G_S,O])_{0,1}=-C+4-2/C\ne0) for integer spins (S>=1) | Conservation shortcut rejected; no broader target no-go |
| Five-site cross-fiber character geometry | Resolve (N_S) into primitive 5-cell Bloch fibers; track (V) between fibers | Exact Casimir family, four crossing compressions and slopes, principal action, fiber shift by (4 pi/3), and two nondegenerate stationary points are derived in the local bounded-theorem block | Local support complete; full slow-transport estimate remains target-equivalent |

The follow-on author probe of the weighted lag/alias criterion reproduces the
finite cosine-character scalar directly from the spectral double sum and
positive-lag pairing to errors below (3.1\times10^{-15}). At (S=24,48,96),
the twice-positive-lag per-block Abel bounds are approximately 96.97, 213.99,
and 475.73. Near-alias lag-weight mass for a 0.01-radian first-difference
window is approximately 0.0117, 0.0137, and 0.0193. These are float64 finite
diagnostics; their scale says the elementary triangle/Abel estimate is not a
useful closure bound at these sizes, but they establish no asymptotic failure
or target discrepancy. The exact two-energy Schur probe at
`outputs/postmark_moving_index_2026_09_24/attempt_logs/schur_weyl_two_energy_probe.py`
now verifies the four-site determinant recurrence and reduced off-diagonal
symbolically, and checks the weighted overlap and identity-metric formulas on
four finite spins. It reduces the coordinate dimension from `10S-3` to `2S`
away from eliminated-block poles; it does not bound the selected-time phase
sum or prove the actual readout limit. A focused follow-up review now selects
direct deterministic cancellation in the prepared-weighted phase sum. Pole-safe
reconstruction is a support tool only: eliminated-block poles are coordinate
singularities, and a normalized-overlap contraction yields no phase bound.

## Follow-up route decision after the ten-route review

| Route | Mathematical object and first discriminator | Result | Status / strength |
|---|---|---|---|
| Pole-neighborhood excision | Prepared spectral mass near the deleted-anchor compression spectrum, normalized by adjacent full-spectrum spacing | Corrected finite scan at S=16,...,512 has 1.0–2.1% mass at relative radius 0.01; at S=512, 1.34% mass versus 1.58% of modes. The minimum ratio reaches 1.59e-6 | Counting-like finite diagnostic; no uniform mass theorem or phase bound |
| Actual-generator readout correction | Eigensystem of H_S=C N_S with exact G_S phase exp[-it(E^2/C^2-E)] | Dense expm agrees to <=1.2e-15 at S=1,2,3,5; actual O readouts at S=8,16,32,64,128,256,512 remain finite and fluctuate around 1/3 | Corrected finite evidence only; no asymptotic separation or limit |
| Deterministic weighted cancellation | Exact positive-lag decomposition of q_S using prepared coefficients, character matrix elements, and phase C(lambda_k-lambda_j)/4 | Full-lag bins at S=96,192,384,512 reproduce the direct scalar to <=2e-13. The sum of individual lag magnitudes is 0.389,0.378,0.372,0.372 while the signed positive-lag real sum oscillates -0.0141,+0.00470,+0.0118,+0.00620. No sampled single lag dominates; the aggregate Abel bound rises to 1386 at S=512 | Selected campaign: derive joint weighted cancellation over the two spectral indices; fixed-lag and one-lag triangle estimates do not close |
| Discrete spectral-phase alias census | One-index slopes alpha_j=C(lambda_(j+1)-lambda_j)/4 and fixed-lag derivatives alpha_(j+h)-alpha_j | At S=96,192,384,512 there are 4,7,13,17 distinct one-index alias integers; prepared mass within 0.01 rad of an individual alias stays about 0.0043--0.0048. The all-lag L1 weight within 0.01 rad of a lag-derivative alias is 0.0193,0.0260,0.0371,0.0424. Lag reconstruction matches direct evolution within 1.3e-13 | This exposes the missing uniform estimate: branch interpolation, phase-accurate quantization, overlap weights, and summation of every reciprocal alias are unresolved; the finite census is not a decay bound |
| Larger actual-readout sample | Direct finite-spin eigendecomposition of G_S=N_S^2-CN_S at t=1/4 | For S=512,640,768,896,1024, the period-three observable is 0.341669,0.337053,0.337260,0.336208,0.328571; generator factorization agrees at <=6.4e-13 in state/readout checks | Float64 finite samples only; neither convergence to 1/3 nor separated limiting subsequences follows |
| Principal Weyl spectral measure | Fixed moments of the exact tridiagonal N_S from local closed walks and the five-site frozen symbol | Author proof gives weak convergence to density 1/(4 sqrt(lambda)) on (0,4), CDF sqrt(lambda)/2, quantiles 4 rho^2, and normalized phase profile theta/S^2 -> rho^2 | Bounded conditional support theorem; no adjacent gaps or phase modulo 2pi, so the O(S) alias weights remain open |

## Personal transfer-phase execution after the ten-worker selection

The selected local-transfer block now has five derived and author-checked
modules in the current worktree. The exact S^-2 local phase, regular O(S)-cell
transport, simple Bragg crossing, central double contacts, and positive
simple-turning-point Airy match have distinct analytic proofs and paired
deterministic runners. They concern the same explicit scalar Jacobi family
and make no physical axiom claim.

| Route | Mechanism and first discriminator | Result | Strength / remaining wall |
|---|---|---|---|
| Regular local phase and product | Exact second-order five-site coefficient convolution plus moving eigenbasis overlap | Exact symbolic trace/phase identities; shifted 15-site product; regular product error O(S^-1) with the Berry connection; canonical caches pass | Bounded on regular compact arcs; no crossing, turn, endpoint, or readout conclusion |
| One simple Bragg root | Shrinking layer rho=S^-2/3 and an outer homological equation with gap proportional to distance | Exact moving-frame phase identity; opposite Berry sign and additive g1 mutations rejected; eight exact finite products decrease in norm error; the tested crossing cell is hyperbolic at every sampled S | Bounded O(S^-1/3) for one simple interior root away from u=0; no energy-uniform result |
| Central double contact | Exact first-order suppression A1(0)=0, quadratic detuning, inner rho=S^-1/2 and outer correction O(1/u) | Exact symbolic vanishing and all four quadratic contact identities; constant off-diagonal mutation rejected; 32 finite exact-transfer products over four energies | Bounded O(S^-1/2) at four fixed energies; not uniform in energy, turning, endpoints, overlaps, or aliases |
| Positive simple turning point | Parabolic Jordan reduction of the exact five-site transfer at k=pi; first discriminator is the signed lower-left slope and its Airy scale | Fixed-window Airy system q''=b_lambda tau q, b_lambda=800 a_lambda/lambda; finite-edge shift is O(S^-1); ordered allowed-side match has outer error C R^-3/2 | Bounded local theorem for compact energies and fixed scaled windows; the finite forbidden tail and boundary-selected branch remain open |
| Forbidden-tail boundary selection — next | Exact finite Jacobi eigenvector on u>a_lambda matched to the positive-turn Airy window | Test whether a cone or Riccati contraction controls the growing Airy coefficient relative to the allowed WKB mode | Highest remaining local-to-global leverage; no theorem or negative result yet |
| Prepared-overlap and joint aliases | Use turning-matched eigenfunctions to derive the period-three overlap weights and sum every reciprocal alias in the actual double sum | Open; finite quadratic and one-lag routes remain insufficient | Still the decisive actual-readout obligation |

The first symbolic phase-identity attempt omitted the fixed-cell similarity
conjugation between the per-site expansion and the principal frame. The exact
runner exposed a nonzero residual; conjugating the five-site first-order
coefficient by D on both sides reduced it to zero. This was a diagnostic
coordinate error caught before relying on the result. The first central route
probe also had an import-root path mistake; no calculation ran until that path
was corrected. Full details and outputs are in the attempt logs.

No axiom update follows from these results. The supplied finite-spin model
and preparation remain conditional inputs, and no actual-readout limit or
separated subsequence has been established.

Mathematical sectors searched or queued: discrete and matrix-valued WKB; stationary phase and exponential sums; Jacobi operators and orthogonal polynomials; commutator equations; spectral measures and harmonic analysis; operator/Fourier methods; semiclassical propagation and matrix-valued Egorov; finite-group character selection; endpoint weighted forms; exact Schur complements; imaginary-time Markov kernels. Number-theoretic revival analysis is useful only when tied to the actual eigenphase and overlap weights. No route supplies an axiom update: the supplied dynamics and output remain imported premises.

## Current-head route selection and source search — 2026-09-24

**Target state:** open after matching-hit review. The target is not the full
fixed-time readout theorem here; this block targets the actual-index local
five-site transfer trace and phase through order `S^-2`, a missing input to
global phase-accurate quantization and overlap transport.

**Source revisions reviewed:** current main
`0e6ad8285096ed668816f18caaa6fbbfbd9c50e8`; parent source/PR head
`c734332ca227c4371f3c188f96227c494b43f533`; phase-accuracy checkpoint
`20251000c51`.

**Statement search on refreshed `origin/main` and relevant candidate heads:**

```bash
git fetch origin main:refs/remotes/origin/main
git rev-parse origin/main
git ls-tree -r --name-only origin/main -- docs | rg -i 'postmark.*electric.*(five.site|transfer|phase|quantization)'
git grep -n -i -E 'second.order.{0,40}(five.site|transfer|trace|eigenphase)|((five.site|transfer|trace|eigenphase).{0,40}second.order)|tau_2|τ_2|phase expansion through S.?\^?2' origin/main -- 'docs/POSTMARK_ELECTRIC*' 'scripts/postmark_electric*'
git grep -n -i -E 'second.order.{0,40}(five.site|transfer|trace|eigenphase)|((five.site|transfer|trace|eigenphase).{0,40}second.order)|tau_2|τ_2|phase expansion through S.?\^?2' HEAD -- 'docs/POSTMARK_ELECTRIC*' 'scripts/postmark_electric*'
git grep -n -i -E 'second.order.{0,40}(five.site|transfer|trace|eigenphase)|((five.site|transfer|trace|eigenphase).{0,40}second.order)|tau_2|τ_2|phase expansion through S.?\^?2' origin/physics-loop/postmark-electric-quantization-phase-20260924 -- 'docs/POSTMARK_ELECTRIC*' 'scripts/postmark_electric*'
```

Main has no five-site electric transfer source title; the matching proposal
heads contain the existing five-site coefficient and first-order frozen-band
correction but no `tau_2` or second-order local eigenphase. The prior phase
branch adds a finite phase-accuracy gate only, which has been fast-forwarded
into this campaign at `20251000c51`; it is not duplicated by the new analytic
transfer derivation. Parent PR #9078 and stacked PR #9091 were checked through
their bodies and review records; both are open, non-draft, and have no
independent reviews or comments.

**Ten-worker route decision:** retain the exact fixed-time scalar target;
first derive the regular-arc transfer phase through `S^-2` with a uniform
remainder and exact shifted 15-site regrouping. Then attempt global
quantization and prepared-overlap transport; only after that is the
alias-complete two-index sum a viable decisive target. A one-row terminal
estimate is a useful side lemma but not the main blockage. Axiomatic
underdetermination is not a contradiction and does not warrant revising the
four axioms.

**Promotion Value Gate (prospective):** V1 is the unresolved global phase and
overlap input to `Re(q_S(1/4))`; V2 is the previously absent second-order
actual-index cell trace/phase coefficient, established by the source search
above; V3 requires exact symbolic coefficient identities and a proved compact
uniform remainder, with the global transport gap named; V4 is the new
second-order local phase data needed to attempt `o(S^-2)` eigenvalue control;
V5 is not a one-step variant of the first-order band correction or the Weyl
count, because it expands the determinant-one actual transfer product and
tracks the second coefficient. Final answers depend on source and runner
checks and will be recorded before any PR is opened.

## Current-head route selection at the Airy boundary — 2026-09-24

Ten read-only route reviewers inspected candidate head
2d36bafc9ba85a2cd1e5e588d7892a79aa086903 against main
0e6ad8285096ed668816f18caaa6fbbfbd9c50e8. Seven selected finite-endpoint
selection of the decaying Airy mode first; two selected a direct
prepared-weighted phase/readout estimate; one selected central-detuning
uniformity. No reviewer edited source or ran the selected campaign, and route
agreement is not independent proof validation.

| Lens | Highest-value result | Remaining mathematical obligation |
|---|---|---|
| Exact boundary / forbidden propagation | Terminal row gives an explicit positive seed; strict row dominance suggests backward positivity and monotonicity | Prove induction on every five-residue row and transfer the cone into the Airy projective coordinates |
| Airy/Jordan matching | A nonnegative decreasing Airy solution on the whole forbidden half-line should exclude the growing mode | Derive how the Jordan first coordinate depends on adjacent staggered values; prove normalized limits are nonzero |
| Central layer | Detuning scale is S^-2/3 around the positive turn with no leading order-one mode conversion | Lower priority than endpoint selection; uniform central energies may be excised for qualitative scalar control only |
| Prepared scalar | Observable-aware phase bound weights each pair by the magnitude of c_j c_k V_jk, removing the need for full state-norm accuracy | Must bound macroscopic lags and every reciprocal alias; finite low-lag samples give no asymptotic estimate |
| Axiom boundary | Supplied dynamics and preparation are not fixed by the native axioms | No contradiction and no axiom update; require an explicit model bridge or incompatible axiom-compatible models |

The route review is rank-selection evidence only. The personally executed
campaign must derive the recurrence inequalities and either prove the
branch-selection estimate or record the exact failed passage.
