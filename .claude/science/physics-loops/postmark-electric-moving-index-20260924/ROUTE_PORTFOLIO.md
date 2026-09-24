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

Mathematical sectors searched or queued: discrete and matrix-valued WKB; stationary phase and exponential sums; Jacobi operators and orthogonal polynomials; commutator equations; spectral measures and harmonic analysis; operator/Fourier methods; semiclassical propagation and matrix-valued Egorov; finite-group character selection; endpoint weighted forms; exact Schur complements; imaginary-time Markov kernels. Number-theoretic revival analysis is useful only when tied to the actual eigenphase and overlap weights. No route supplies an axiom update: the supplied dynamics and output remain imported premises.
