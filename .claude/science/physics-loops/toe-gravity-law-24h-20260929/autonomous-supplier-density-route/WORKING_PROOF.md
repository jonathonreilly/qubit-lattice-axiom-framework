# Working proof: spatially local stability and the resource order

Candidate derivation. No independent check or new computation yet. This supplements the frozen contract; it is not a completed theorem.

## 1. A dimension-independent influence estimate for bounded channels

In a finite tensor graph define c_x(O)=sup_(unitary U_x)||[O,U_x]||. For a local normal unital CP map C_Z, supported on Z and equal to identity on its exterior, write d_Z=||C_Z-I||_cb. Twirl over the finite-dimensional factors in Z to obtain a conditional expectation E_Z onto their commutant. Then

 ||O-E_Z O||<=sum_(z in Z)c_z(O),
 (C_Z-I)E_Z=0.

(The Haar average is valid after the finite field box and finite record cap; ancillas can be left untouched.) If x is outside Z, contraction and commutation give c_x(C_Z O)<=c_x(O). If x is in Z, the triangle inequality gives

 c_x(C_Z O)<=c_x(O)+2d_Z sum_(z in Z)c_z(O).

Thus one channel updates the nonnegative influence vector by at most I+2d_Z 1_Z 1_Z^T. For a disjoint color layer with |Z|<=sigma, the row-sum increase is at most1+2sigma max d_Z. For channels with d_Z<=c tau, chi color layers per bin and n bins, this is bounded by exp(2sigma chi c T). The spatially weighted row sum is similarly bounded after multiplying by exp(mu diam Z). This is independent of volume, local matrix dimension and tau. Initially c_x(O_X)<=2||O||1_X(x).

For an individual channel difference D_Z with D_Z(I)=0 and exterior identity cancellation, ||D_Z O||<=||D_Z||_cb sum_(z in Z)c_z(O). Summing local differences against the propagated influence matrix therefore uses incident local strengths rather than a total-volume norm. The same estimate localizes a circuit by omitting distant maps: the weighted influence row sum contributes exp(-mu buffer radius). This gives a direct elementary route to a volume-uniform collision comparison.

Continuous local Hamiltonian evolution follows by arbitrarily fine local-unitary splitting and the same estimate (or the corresponding integral Gronwall recursion). A local unitary time step has cb deviation<=2dt||H_Z||. Its path matrix has bounded weighted row growth controlled by4sigma exp(mu d) times the incident local Hamiltonian strength integrated over time. Onsite free clock Hamiltonians can instead be removed exactly by a tensor-product interaction picture, so their huge norm does not enter propagation. This last operation is also valid for infinite analysis clocks, where bounded interaction-picture coefficients are norm-continuous after choosing finite Fourier degree.

For local Hamiltonian differences, Duhamel uses the reference evolved observable inside the commutator and only conjugates by the perturbed unitary outside it. Therefore only the REFERENCE influence kernel is needed. This is critical for random clock offsets: their per-center expected integrated perturbation can be summed against a deterministic summable kernel without taking a global good-clock event.

## 2. Original colored collisions and record placement

At field box R, each original center collision C_a is trace preserving and has

 C_a=I+tau Diss_a+E_a, ||E_a||_cb<=tau² g0²,
 ||C_a-I||_cb<=3g0 tau, g0=80kappa, tau g0<=1/2.

Its exact center semigroup differs by at most7g0²tau², including every multiple-event term. Same-color stars are disjoint. The star-overlap graph has maximum degree18, so chi=19 colors suffice for every finite torus. Every magnetic word is compressed WHOLE, and the original coherent edge sum is never sign-dephased.

For observed centers it is cleaner to prove consistency first with an original-word append space: the no-event map leaves the word untouched and each gain appends its original label. This map remains within O(tau) of identity in cb norm; a reset of an arbitrary record factor would not have this property. Only a finite observed region is anchored. A count cap and overflow flag may be used after pricing the exact target count tail. The apparatus itself uses fresh finite flags and copies at each bin; its known classical interpretation reproduces the append map on their ready inputs. Source registers at unobserved centers may be traced after their last ideal pulse. All original later births remain.

The influence estimate above gives uniform-in-tau localization of both the colored discrete map and the bounded field-box Lindblad process. Choose a common finite spatial patch for a prescribed finite output/instrument tolerance; then the elementary finite-patch global Trotter/collision bound tends to zero as tau does. Because that patch is chosen with a uniform influence estimate before tau, this proves local consistency without a circular volume/tau choice. Multi-time passive flag copies only enlarge the fixed observed anchor and telescope a finite number of errors.

## 3. Uniform prepared rotor-to-field-box transfer

PR9399 does not claim an uncontrolled exchange of box and volume limits. Both the full rotor and each full-word field-box process have the same connected-support and bounded non-electric coefficient constants. Their diagonal electric terms commute. The small-time spatial localization majorant is uniform over R and over the whole unit ball of the local observable algebra. Its finite-subdivision all-time extension is also uniform in R and dimension.

First choose a common finite spatial patch around X and observed F for the prescribed horizon and tolerance. Both full and box finite-volume outputs differ from their patch outputs by the same uniform locality error. On that fixed patch, use the original prepared-input weighted Dyson coefficient argument: all initial fields vanish, every complete magnetic/loss insertion changes the radial field by at most4 and every original jump by at most2. Finite-order coefficients agree for R large enough, and the finite-patch factorial majorant controls the tail at every finite horizon. This gives uniform local trace/instrument approximation from Omega on all large tori. It is a two-stage proof, not a claim that the original global cutoff formula was volume uniform.

Local quadratic energy expectations use the independent local moment bounds for BOTH original and field-box processes. First truncate the local energy form spectrally with a fourth or higher moment tail, then use local trace comparison, then remove that observable truncation. The Hamiltonian energy assignment in the apparatus is the actual whole-word compressed source energy; scalar positivity shifts cancel from energy increments.

## 4. Scheduled pulses, then ideal clock randomness

Set fixed chi color slots per bin and triangle width s<=tau/(8chi+4), with all centers of one color pulsed simultaneously. Each pulse has area1, height1/s, and its local positive logarithm has norm<=2pi. For the deterministic program the time integral of the uniform incident interaction strength is bounded by a constant times chi n, independently of s. Free source terms add only their fixed field-box incident norm times T. The influence exponential can therefore be chosen BEFORE s.

Omitting free source evolution only during the pulses and shifting the small guard intervals produces an integrated local perturbation O(n chi s) times the source local norm. Duhamel with the deterministic-program influence estimate proves that the local error tends to zero with s. Global serialization of all centers and its N-dependent pulse width are unnecessary.

Choose positive Fejer polynomials f of degree M. A deterministic smoothing error is bounded per center by2pi n rho1. For ideal translation clocks, the characteristic formula makes the reduced source/flag process an average over the initial coordinate offsets. At a good clock |y_a|<=sigma, the pulse-train integrated mismatch is at most2n sigma/s before the2pi norm factor. At a bad clock it is at most2n (the pulse train is positive and has total area n over a full circle). Its expected mismatch is at most C n(sigma/s+theta). A finite sum over color classes bounds the expected incident mismatch integrated in time. Applying Duhamel against the deterministic reference kernel and averaging gives a volume-independent local error. No global probability Ntheta is used, and bad clock configurations are not assigned a uniform propagation speed.

The same argument covers clock-independent passive record copies at finitely many grid times, using the finite enlarged observed anchor. This remains a candidate argument until the precise channel/instrument formulation and read-energy allowance are written in the final proof.

## 5. Finite clocks after all program parameters are fixed

Once R,tau,s,M,k0 have been chosen, the STATIC apparatus coupling has uniform incident norm bounded by a fixed multiple of2pi/s, independent of clock cutoff. Use its ordinary local propagation estimate to choose a finite spatial buffer around the observed source/flag/interaction-energy cells. Onsite source/clock free Hamiltonians do not enlarge the support bounds; finite source electric terms can be included in the bounded local strength.

Inside this fixed buffer, the ideal and compressed clock Dyson coefficients agree through order r whenever Kc>=k0+Mr. Every insertion changes one clock momentum by at most M. The finite-patch interaction norm is at most2pi times its number of A centers divided by s, known before Kc. The two high-order tails are bounded by4 sum_(j>r)(v_patch T)^j/j! in trace norm. Choose r and then Kc. No parameter chosen afterward changes the interaction norm or the required spatial buffer. All clock parameters are uniform in the full torus volume.

## 6. Endpoint density and ledger candidate

With sigma<s, each ideal clock marginal at a grid endpoint has local bad-position probability theta. Positivity and the endpoint triangle zeros yield

 0<=<V_a><=2pi[n rho_inf+theta/s].

A local joint finite-clock comparison adds at most(2pi/s)delta_clock for the compressed V_a. Parameters can make this bound arbitrarily small after s is fixed. The initial mean clock energy per A center is omega Kc, and its maximum is2omega Kc; finite flags and copies have zero supplied free spectrum. The source shift2592delta per center and all couplings are included in the positive total Hamiltonian.

At every finite torus the exact closed-run identity is

 -Delta<E_clock>/N=Delta<E_source>/N+Delta<V>/N.

Uniform per-center source approximation and endpoint interaction bounds would make this a genuine original energy-density supplier statement. A performed grid read need not commute with V; its energy exchange must be bounded separately from the same local positive pulse estimate. No stationary/catalytic resource or branchwise work law is inferred. This section is still provisional pending the complete process/read formulation and independent checking.


## 7. Infinite analysis clocks and finite observed words: domain clarification

The elementary twirling proof above is used only on finite-dimensional local factors. It must not invoke a nonexistent normal Haar average on the full infinite-dimensional clock unitary group. To transfer its locality bound to the IDEAL analysis-clock experiment from the prepared finite band, first use arbitrarily large finite Fourier compressions on a fixed finite spatial torus. Their free clock terms are onsite and their interaction norms/geometry are uniform in the compression size. The finite-dimensional influence bounds therefore hold uniformly. At fixed spatial volume, the exact clock-prefix/Dyson argument gives convergence in vector norm from the prepared band as the Fourier cutoff tends to infinity (also with the finitely many passive clock-independent copies). Partial trace gives trace-norm convergence of the local outputs. Pass the uniform boundary-comparison inequality through that fixed-volume limit. This establishes precisely the prepared-state ideal-clock locality needed for the resource construction; it does not assert norm convergence of clock propagators on their whole Hilbert space.

For a finite word cap, use a classical append-with-overflow CP channel on the observed record factor. Its gain can be represented by Kraus operators L_m tensor |append_m(w)><w| for every word w; the sum of their adjoint products is the original Gamma tensor I. The no-event Kraus keeps the word untouched. Thus the near-identity/cb bounds remain determined by Gamma even though this extension dephases preexisting coherent word states on a gain. Original histories are classical, so the extension changes no claimed input/output. Overflow coarsens only the record and never stops later source jumps. The target probability of overflow is bounded by the original finite-F rate tail, and any apparatus overflow discrepancy is covered by the same finite-region instrument comparison.

Binning retains original labels. If a desired binned observable also keeps the relative temporal order of different observed-center marks inside a fine bin, the deterministic color sweep disagrees only when there are at least two observed events in that bin; the original source bound prices their total probability by a constant times(80kappa|F|)^2 T tau. This bound is local in F, not a false statement that the entire large lattice has at most one event per bin. All unobserved later events remain in the source evolution.
