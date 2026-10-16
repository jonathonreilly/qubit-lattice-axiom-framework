# Independent derivation before reading author implementation

Radial flux: for s,t>=0 choose r=sqrt(s+t), cos(theta)=sqrt(s/(s+t)) when s+t>0. Then f(s+t)=f(s)+f(t), and zero case is immediate. For b>=a, f(b)-f(a)=f(b-a)>=0. Thus rational lower/upper approximations squeeze f(x) to x*f(1). Finite positive flux excludes pathological additive functions, c=0 is the trivial case. A single pi/4 identity permits q(r)=r^2*h(log_2(r^2)) for positive period-one h and r>0, so does not select a unique quadratic law. This is selection by universal splitter conservation, not a derivation of that physical premise.

Real transport: H(H) identity and rotations acting on the two arm vectors give outputs (R0u +/- R1u)/2. The real dot product of the rotated unit vectors is cos(phi0-phi1). Norm squares yield (1+/-cos(delta))/2 and sum to one. This is ordinary real wave algebra with specified junction and phase transport; calling its norm flux uses the previous functional premises and unit calibration.

Counters: t=r+p in [0,2), other pre-count sum=2-t in (0,2]. Strict condition 2-t>1 is t<1, complementary to t>=1. New r=t-floor(t) lies in [0,1), and other residue equals 1-r. Summing r_t=r_(t-1)+p_t-Z_t yields N=sum p+r_initial-r_final. Difference magnitude <1. For constant p this is floor(r_initial+n*p), no ensemble needed.

At half flux, r advances mod one by 1/2, and threshold decisions swap exactly on each subsequent trial. At r=0 or 1/2 this remains true because the specified strict/weak ties allocate one click. Every even n count equals n/2 for all initial residues. Any initial ensemble then has variance zero. This is not iid Bernoulli behavior.

Initialization necessity: events p>=a=1-r0 and p<b=r1 partition all p in [0,1] iff a=b on the stated residue domains. If b>a, their overlap [a,b) produces doubles; if b<a, [b,a) produces no count. Independent continuous uniform residues give independent click probabilities p and 1-p, so double and zero each p*(1-p). These are ensemble comparison assumptions.

General floor counters telescope each channel with bounded final residues, hence mean total count minus mean incident flux vanishes at long times. Exactly one count per trial cannot persist with a different constant total flux; this claim needs counters emitting floor(residue+increment) if increment exceeds one, not a single-output clipped detector.

Loss process: write a=eta0,b=eta1 and m=(1-a)*(1-b). Starting after a retained zero, the next underlying port is one. First retained one has probability b*sum m^k=b/(1-m); first retained zero has probability (1-b)*a/(1-m). Starting after one gives zero a/(1-m) and one (1-a)*b/(1-m). D=1-m. Stationary balance pi0*b=pi1*a gives pi0=a/(a+b). Other eigenvalue 1-(a+b)/D=-ab/D. For any stationary two-state chain, conditional centered binary expectation is multiplied by this eigenvalue, so normalized lag-one covariance equals it. Need stationary retained-stream initialization for covariance identification, but not for transition probabilities.

Even n underlying trials have exactly n/2 zero clicks; independent retention gives Binomial(n/2,a), mean na/2 and variance na(1-a)/2. Independent half-Bernoulli underlying outcomes thinned independently instead give Binomial(n,a/2), variance n(a/2)(1-a/2). Subtraction yields n*a^2/4. IID uniform reset residues each trial would yield P(click0)=p and independent outcomes for fixed settings, but would be a new reset/noise law with renewed complementary preparation.

No mathematical discrepancy found at this pre-code stage. Source labels all key transport, preparation, threshold, initial-state and loss assumptions. Physical calibration, lattice realization and genuine stochastic-process reproduction remain open.
