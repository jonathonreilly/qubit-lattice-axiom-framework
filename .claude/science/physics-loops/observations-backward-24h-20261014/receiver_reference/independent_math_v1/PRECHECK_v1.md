# Independent carrier/receiver-reference mathematics precheck v1

This precheck is derived from the announced task premises before opening any M10 author proof or implementation. The parent supplied the candidate formulas; independence means a separate proof and implementation, not blindness to those targets. Root remains the scientific author. No observation, raw product, receiver metadata or author source is used. All quantities below are conditional model quantities in the declared voltage/code and time units, not a supplied physical calibration or noise budget.

## 1. Exact finite-vector uncertainty

Assume N>=1, known finite real sample times t_n, finite z in C^N, u_f,n=exp(2pi i f t_n), and unrestricted complex amplitude c. Use the Euclidean Hermitian convention A(f)=u_f^*z, S=z^*z and ||u_f||^2=N. Orthogonal projection gives

`||z-c u_f||^2 = E(f)+N|c-A(f)/N|^2`,
`E(f)=S-|A(f)|^2/N >= 0`.

This follows by expanding the Hermitian norm and completing the square, not by assuming the fitted residual is noise. For a supplied deterministic bound ||eta||<=B with B>=0, the exact joint feasible set is

`{(f,c): E(f)<=B^2 and |c-A(f)/N|<=sqrt((B^2-E(f))/N)}`.

Thus f is feasible exactly when E(f)<=B^2, provided c=0 is allowed. For B^2<S this is equivalent to |A(f)|>=sqrt(N(S-B^2)); for B^2>=S every frequency is feasible by c=0. If an additional premise requires a nonzero carrier, the edge case B^2=S and A(f)=0 admits only c=0 and must be excluded; when B^2>S a sufficiently small nonzero c exists at every frequency. If N=1, E(f)=0 for every f regardless of the recorded value. Empty data N=0 do not permit this formula. Repeated times and exact sampling aliases can produce multiple feasible frequencies even with B=0.

At a fixed feasible f, the amplitude magnitudes form exactly `[max(0,|A|/N-rho), |A|/N+rho]`, rho=sqrt((B^2-E)/N). If rho<|A|/N, nonzero phases lie in the closed arc of half-angle arcsin(rho/(|A|/N)) around arg A. If rho>|A|/N all phases occur. When rho=|A|/N>0 the disk touches zero: nonzero phases lie in the open half-circle, with endpoints approached only as amplitude tends to zero. If both vanish, the only amplitude is zero and its phase is undefined. A supplied lower amplitude bound or stochastic likelihood changes the model and cannot be silently inserted.

For any true pair (f_*,c_*), eta=z-c_*u_{f_*}. The fitted residual at that same frequency is exactly `||P_perp eta||^2`, while `||eta||^2=E(f_*)+N|c_*-A(f_*)/N|^2`. It is therefore a lower bound on the discrepancy norm squared, not an upper bound. Parallel error can be arbitrarily large while E=0. Without B or another quantitative restriction on discrepancy, every frequency with every chosen amplitude can explain the same finite z by defining eta=z-cu_f. Even finite observed voltage does not impose a finite uniform noise bound when c is unrestricted.

Concrete error witness: at times (0,1), take z=(1,1). The fitted model f=0,c=1 has residual zero. The alternative true carrier f=1/2,c=1 has samples (1,-1) and eta=(0,2), with norm squared 4. Its optimized residual is 2. Assigning B from the best fitted residual, B=0, would exclude this possible true carrier. No physical conclusion follows from the preferred fit without an independently supplied error model.

## 2. Arbitrary constant-modulus waveforms and ADC centers

Let r_n=|z_n|, R=sum r_n. Allow independent phases q_n=a exp(i theta_n) with one a>=0. For each n, the reverse triangle inequality gives |z_n-q_n|^2>=(r_n-a)^2, with equality by aligning q_n with z_n (any phase at z_n=0). Minimizing the sum over a gives a=R/N and

`min_constant_modulus ||z-q||^2 = S-R^2/N`.

The minimum is nonnegative by Cauchy-Schwarz. A single complex constant-amplitude tone is a subset of these arbitrary-phase waveforms, so its residual has the same necessary lower bound; equality for arbitrary phases does not establish a tone fit.

For integer centers x_n+i y_n, define `C_n=ceil(sqrt(x_n^2+y_n^2))` exactly using integer arithmetic and C=sum C_n. Since C>=R>=0,

`||z-q||^2 >= max(0, S-C^2/N)`.

An upper approximation to R is required here. A floor radius can create a false exclusion. Integer rounding must be exact; binary floating square roots near large perfect squares are not certificates.

Under the additional ideal *closed* Cartesian cell premise `Q_n=[x_n-1,x_n+1]+i[y_n-1,y_n+1]`, every q in the product cells has ||z-q||^2<=2N. Consequently `N*S-C^2>2*N^2` is a sufficient exact exclusion of every constant-modulus waveform in those cells. The strict sign is necessary: equality of the exact center minimum with 2N can occur for a waveform at cell corners. The result also safely excludes half-open cells because they are subsets of the closed boxes; feasibility or equality for the closed enlargement is not sufficient for a particular half-open quantizer convention. Saturated/clipped or nonideal cells are not assumed to have this shape.

A useful boundary example is z=(1+i,3+3i). The common closed-cell voltage 2+2i lies in both cells and has center residual squared 4=2N. This prevents replacing a strict exclusion by a non-strict one. A strong exclusion example is z=(1+i,9+9i): S=164, C=15, N*S-C^2=103>8. The exact arbitrary-phase center minimum is 64.

This is a statement about total analog voltage under the assumed cell law. A receiver carrier plus additive thermal/electronic/mixing error need not have constant total modulus. Rejecting a noiseless constant-modulus voltage is not rejecting an underlying carrier, not a physical noise upper bound, and not a scalar/gravity observation.

## 3. Exact closed-cell amplitude and phase feasibility

For an individual closed square, the exact range of attainable magnitudes is the closed interval [ell_n,h_n], where

`ell_n^2=max(|x_n|-1,0)^2+max(|y_n|-1,0)^2`,
`h_n^2=(|x_n|+1)^2+(|y_n|+1)^2`.

The lower and upper extrema follow by independent coordinate minimization/maximization. The continuous norm maps the connected compact square to an interval, so no intermediate magnitude is missing. Therefore a waveform of arbitrary phases but common modulus exists in the product closed cells iff `max ell_n <= min h_n`, equivalently `max ell_n^2 <= min h_n^2`. The requested strict reverse inequality is not merely sufficient: it is exactly the failure condition for this enlarged waveform class. N=1 always has a nonempty amplitude interval, and origin-containing cells simply have ell=0. This criterion is exact for the closed boxes, but its success still does not establish a tone or a carrier calibration.

At a fixed f the exact noiseless tone criterion is `intersection_n (conj(u_f,n) Q_n) != empty` in the complex c-plane. These are rotated closed squares, so this is a finite convex feasibility problem. Quarter-turn phases leave their axes aligned, giving an exact rational rectangle-intersection fixture. With z=(3+3i,-3-3i), the amplitude intervals agree; f=0 cannot fit any common c in the cells, but f=1/2 at times (0,1) can. This separates the amplitude-only test from phase coherence.

If a separately supplied physical discrepancy ball of radius B is admitted and analog values are only known to be in the cells, the exact fixed-f condition becomes

`min_c sum_n dist(c u_f,n, Q_n)^2 <= B^2`.

The scalar c objective is continuous, convex and coercive for N>=1 with bounded nonempty cells, so its minimum exists. This statement introduces no selected realization inside a cell as known truth; it is an existential feasible set under supplied premises. The simple necessary center condition is `E(f) <= (B+sqrt(2N))^2`, from triangle inequality, not generally an equivalence.

For arbitrary-phase common-modulus waveforms there is an even simpler exact cell-to-waveform distance:

`min_a>=0 sum_n dist(a,[ell_n,h_n])^2`.

At each n, the closest cell point to some freely oriented vector of magnitude a has distance dist(a,[ell_n,h_n]); optimizing phases and cells independently realizes it. This is a one-dimensional convex problem. It can supply a *necessary lower* discrepancy budget under the total-voltage model, never an upper noise bound. For the pair (1+i,9+9i), amplitudes have intervals [0,2sqrt(2)] and [8sqrt(2),10sqrt(2)]. Their exact minimum discrepancy squared is 36 at a=5sqrt(2); an underlying carrier can still be present with error at least 6 in these uncalibrated code units.

## 4. Correlation grid bound and centering qualification

Choose a common time origin tau and define `A_tau(f)=sum z_n exp(-2pi i f(t_n-tau))=exp(2pi i f tau) A(f)`. It has exactly the same magnitude as A. Its derivative exists and satisfies

`|A_tau'(f)| <= L_tau = 2pi sum |t_n-tau| |z_n|`.

Integration over the frequency segment gives `|A_tau(f)-A_tau(g)|<=L_tau|f-g|`; hence `||A(f)|-|A(g)||<=L_tau|f-g|`. The centered constant cannot be applied to the *uncentered complex-valued* A without its phase redefinition. For N=1,t=1,z=1, tau=1 gives L_tau=0, while A(0)=1 and A(1/2)=-1. Their magnitudes agree and A_tau is constant, as required. The common phase factor is essential.

A weighted median of the times with weights |z_n| minimizes this L1-based time-origin bound; using the ordinary mean is valid but need not minimize it. If all weights are zero, A=0 and L=0. If all nonzero weighted times coincide, the centered correlation is constant and every magnitude is frequency-independent.

Let a finite grid cover a *specified* frequency domain K with radius delta: each f in K lies within delta of some grid point. Then

`sup_f_in_K |A(f)| <= min(R, max_grid |A(f_j)|+L_tau delta)`.

For a compact interval with both endpoints in the grid, delta is half the largest grid gap. If endpoints are absent, include their distances to the nearest grid point. A finite grid cannot cover the whole real line with finite delta; one must supply a bounded search band or prove an exact alias period. For arbitrary sample times no period is presumed. A supremum is safer than claiming an attained global maximum on an unbounded or open domain.

To use the bound as a certificate, grid amplitudes, L and delta need exact values or rigorously outward bounds. An ordinary floating FFT, a nominal resolution, a plotted peak, or a finite sampled maximum is not an interval certificate. The triangle cap R can likewise be bounded above by exact ceil radii C; a bound larger than sqrt(N*S) can be conservatively capped there. A valid amplitude upper bound U gives the necessary residual lower bound `max(0,S-U^2/N)` on the covered domain. B must still be supplied independently.

Exact off-grid witness: for times (0,1), z=(1,-1), the grid {0,1} has amplitude zero at both points but f=1/2 has amplitude 2. The centered Lipschitz bound has delta=1/2 and L=2pi, hence upper pi (or the exact triangle cap 2), safely covering that hidden peak. With a narrow noise budget, replacing the continuous maximum by the coarse grid maximum would falsely exclude the carrier.

## Planned independent controls and scope

The accompanying implementation will use Fraction pairs for complex arithmetic, integer ceil square roots and exact quarter-turn sampling. Separate fixtures test conjugation and error orientation, projection decomposition, noisy-truth versus zero fitted residual, zero/nonzero-amplitude boundaries, integer rounding direction, closed-cell equality, amplitude-only versus phase feasibility, and an off-grid false-exclusion witness. The elementary rational bound pi<22/7 may be used only to conservatively enclose the synthetic Lipschitz fixture; no floating FFT is labeled certified. These finite controls support the algebraic argument; they do not prove an empirical error model or calibrate physical volts, frequency clocks, carrier phase, station geometry or scalar response.
