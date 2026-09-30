# Actual continuous local histories: compactness, first moments and bounded limiting intensities

Root author proof, not yet independently checked. This is a consumer of checked actual gain matching; it changes no microscopic law, observed mark or state. It is outside the frozen microscopic-output milestone currently under source review. Contract a48d3077 fixes the supplied compensated law, bare Omega, positive couplings, coupled spin family, safe tori, finite horizon T and finite original mark set J. All unobserved events remain unrestricted. Write N_mu(t) and N(t)=sum_J N_mu(t) for the ACTUAL counts.

## 1. Actual finite histories and the uniform current inequality

At each finite volume/spin the Hamiltonian preserves total matter-record number and each birth adds two. Hence the total number of all births is at most floor(|B|/2), although this cap diverges with volume. Each observed history is a finite ordered list of its original marks and continuous times. The finite-dimensional GKSL construction gives its exact positive unnormalized quantum density: between observed events propagate by the trace-decreasing generator retaining all unobserved gains and all losses, and insert the original observed gain at each time. Sum all finite words and integrate their ordered time simplexes. This constructs a positive operator-valued history measure; it is not a trace-class diagonal on a nonatomic L2 space. Its quantum marginal is exactly rho_epsilon(t).

The proof below first uses finite registers only. A register may encode any finite deterministic bin partition and any capped prefix/count function of the original observed history. At each event, use its deterministic classical update on the diagonal register blocks and the original quantum gain. At overflow continue the same gain and full loss; never kill a jump because the counter is full. Unobserved gains leave the register unchanged. This exact bookkeeping dilation has quantum marginal rho_epsilon(t), regardless of cap or partition size.

For mu in J let L_mu=sqrt(kappa)epsilon^-1 j_mu and B_mu=sqrt(kappa)j_mu F_a on the physical spin carrier. Checked G2 states, for every positive extension eta(t) of the SAME rho_epsilon(t),

  sum_mu int_0^T ||L_mu eta L_mu* - B_mu eta B_mu*||_1 dt
       <= e_epsilon,              e_epsilon=C_(J,T)epsilon.       (1)

Its proof uses a squared amplitude depending only on the physical marginal; its constant is independent of the register dimension, cap, partition and time dependence of the extension. No evolving B-process is used. Fix uniform spin-independent bounds lambda_mu>=||B_mu||² and Lambda=sum lambda_mu. Safe choices are36kappa per resolved mark and72kappa per coherent edge mark, from ||F_a||<=6 and original ||j||<=1 or sqrt(2). These are coarse bounds, not actual selected rates.

Let f_mu(t,r) be any deterministic measurable [0,1]-valued function of time and the pre-event finite register. The exact original intensity identity and (1), with the corresponding diagonal contraction, imply

 E int_0^T sum_mu f_mu(t,R_(t-)) dN_mu(t)
   <= int_0^T sum_mu lambda_mu E f_mu(t,R_(t-)) dt +e_epsilon.   (2)

One can restrict to any time interval by setting f=0 outside it. There is ONE error e_epsilon for the complete time integral, not one error per bin. For a common f the right side is Lambda int E f+e_epsilon. At finite volume every current identity is legitimate because rates and total event counts are finite. The same bound holds for any bounded finite history-cylinder test encoded by the register. General continuous-history tests will be reached after taking a limit; no finite-epsilon conditional intensity bound is asserted.

Separately the checked actual D3 estimate gives a constant D_T, independent of epsilon, spin and volume, such that

 E N((s,t]) <= D_T(t-s),       0<=s<=t<=T.                     (3)

This is an UNCONDITIONAL mean intensity bound. It permits large conditional bursts and cannot replace (2). In particular K_T=D_T T bounds E N(T).

## 2. Uncapped first moments are asymptotically uniformly integrable

For integer M>=1 use the register0,...,M, with M absorbing, to encode the event N(t-)>=M. The pathwise identity

 (N(T)-M)_+ = int_0^T 1_(N(t-)>=M) dN(t)

counts all actual later events, including register self-loops at M. Apply (2), then the elementary Markov bound P(N(t)>=M)<=K_T/M:

 E (N(T)-M)_+ <= Lambda T K_T/M + e_epsilon,
 E [N(T)1_(N(T)>2M)] <= 2Lambda T K_T/M +2e_epsilon.           (4)

Thus lim_M->infinity limsup_(epsilon->0,L arbitrary) of the last expectation is zero. Along EVERY sequence epsilon_n->0 and arbitrary allowed L_n, the actual counts are uniformly integrable: for any tolerance, first discard a finite prefix so sup of the remaining e_epsilon is small, choose M for the uniform first term, and then enlarge M to control the finitely many prefix variables. Every finite-prefix variable is integrable (indeed bounded by its finite-volume global cap). This is more than bounded means, and does not assume a volume-uniform global event cap.

No higher finite-epsilon count moment follows from (4). Rare counts can still spoil second-moment uniform integrability. All first-moment passages below use exactly (4).

For an optional tail discriminator set p_m(t)=P(N(t)>=m), p_0=1. The exact first-hitting identity uses the capped indicator N(t-)=m-1, so (2) gives

 p_m(t)<=Lambda int_0^t p_(m-1)(s)ds+e_epsilon.

Iteration yields p_m(t)<=(Lambda t)^m/m!+e_epsilon sum_(j=0)^(m-1)(Lambda t)^j/j!. This is a tail bound, not a Poisson law and not a moment bound at finite epsilon.

## 3. Close events and deterministic endpoints

Partition[0,T] into intervals of length at most2d. In each bin reset a finite seen-event bit; once set, keep it until the next boundary. For the whole partition use f(t)=1 if the bit was already set before the current event. The left side of(2) is sum_bins E(N_bin-1)_+. By(3), at time t in a bin with left endpoint a,

 P(bit set at t-)<=D_T(t-a).

Integration over all bins costs at most D_T d T. Therefore

 P(some bin has at least two observed events)
    <= Lambda D_T d T+e_epsilon.                             (5)

Use two length2d grids with offsets0 and d, clipped at0,T. Any two events less than d apart lie together in a bin of at least one grid. Endpoint equalities can be handled by half-open convention; finite epsilon has no deterministic-time atoms because its bounded finite-volume intensities integrate over Lebesgue time. A union bound proves

 P(two distinct observed events are less than d apart)
    <=2Lambda D_T T d+2e_epsilon.                            (6)

Also(3) bounds probability of any event in a deterministic interval by its length times D_T. This includes shrinking neighborhoods of0,T and any fixed interior time. No independence of marks, renewal property, Poisson replacement or conditional hazard estimate was used. All same-mark coherent amplitudes remain in their original gain.

## 4. Continuous event-list limits

Let H_T be the disjoint union over m>=0 and ordered mark words in J^m of the compact simplexes0<=t1<=...<=tm<=T. Each component includes coincident times for closure; give different lengths/mark words separated component distance and use the maximum time displacement within a component (bounded to at most1). Finite unions with m<=M are compact. Markov's bound on N(T) therefore makes the actual history laws tight. A diagonal subsequence over lengths/mark words and continuous functions on their compact time simplexes constructs a probability limit; count tail bounds prevent loss of total mass.

For each d>0 the event of a pair with gap<d is relatively open on every simplex. The elementary open-set weak-convergence inequality and(6) bound the limiting probability by2Lambda D_T T d. Send d down to zero. The limiting history almost surely has no simultaneous events. The same reasoning with(3) removes events at every specified deterministic time, including0 andT. This is an atom-free time marginal assertion, not a zero probability for every random event time.

The limit has finite length almost surely. By(4), first moments of the count and any count dominated by N(T) pass through this convergence, including counts on deterministic intervals whose endpoints have zero limiting event probability. Thus actual expected local counts converge to those of this same limiting history along the subsequence.

On sets with a bounded number of jumps, distinct interior event times and a fixed mark word, convergence of event lists yields convergence of multivariate counting paths under piecewise-linear time changes matching the ordered jump times; the maximal displacement tends to zero and the transformed paths coincide. The reverse implication follows by locating the unit jumps. Hence the subsequences also converge in this usual time-change topology for finite-jump count paths. No uniform-time path convergence is claimed across displaced jumps. Total variation on exact continuous timestamps is not proved.

## 5. The limiting natural-filtration intensities are bounded

Fix a history-law subsequential limit P. For deterministic s<t and a bounded nonnegative cylinder H of the history through s, encode H in a capped finite bin/prefix register. Apply(2) with f_mu=H on(s,t] and other marks zero:

 E_epsilon[H(N_mu(t)-N_mu(s))]
       <=lambda_mu(t-s) E_epsilon H+e_epsilon ||H||_infty.    (7)

Initially take cylinders with bin boundaries at fixed times and bounded functions of their capped original words. The limiting law has no boundary atoms or simultaneous events; these cylinder tests are continuous except on null sets in the event-list representation. The count-weighted left side passes by(4), while the bounded right side passes by weak convergence. Monotone-class extension from these generating history cylinders gives

 E_P[H(N_mu(t)-N_mu(s))]<=lambda_mu(t-s) E_P H               (8)

for every bounded nonnegative natural-filtration F_s-measurable H. The same argument works for any finite sum of such predictable rectangles, with its original coefficients; equivalently first apply(2) to the combined [0,1]-valued finite step test to keep one error. Monotone convergence extends domination to the predictable sigma algebra.

More explicitly define its finite measure nu_mu(A)=E_P int1_A dN_mu on predictable sets. Equation(8) and the generating-rectangle extension give nu_mu<=lambda_mu(P tensor dt). Radon-Nikodym on this sigma algebra provides a predictable function a_mu(t,h) with0<=a_mu<=lambda_mu almost everywhere and

 E_P int f dN_mu =E_P int f a_mu dt

for all bounded predictable f. Taking f=H1_(s,t] shows N_mu(t)-int_0^t a_mu du is a martingale. This construction uses the limiting law only. It does not assert that the finite-epsilon microscopic conditional intensity is bounded or converges pointwise, and does not identify a_mu with any autonomous effective state.

The limit's total a is at mostLambda. Stopping N at level M and applying the preceding identity to its bounded exponential increment gives, for z>=1,

 E_P z^(N(t) wedge M)
   <=1+Lambda(z-1)int_0^t E_P z^(N(s) wedge M)ds
   <=exp[Lambda t(z-1)].

Send M upward by monotone convergence. Every limiting count has this exponential-moment upper bound. It is not equality with Poisson and does not transfer higher moments from the microscopic sequence without their own uniform-integrability proof.

## 6. Terminal quantum payloads, with weak timestamp topology

Fix a finite physical output region X at a fixed horizon T. Embed its spin fields by zero extension in the common local rotor carrier. The exact original instrument is a positive trace-class-valued measure Q_epsilon on H_T; Tr Q_epsilon is the actual history probability. Its quantum marginal is rho_epsilon,X(T). Existing first-field control implies, for the finite-rank cutoff P_R retaining all local matter factors and |E_e|<=R,

 int Tr[(1-P_R)Q_epsilon(dh)]<=C_X,T/R.                       (9)

The diagonal cutoff rank is finite for every R. No tail conditioning on a rare history is assumed. For an actual history density eta(h), purification or two Hilbert-Schmidt factorizations give the integrated gentle bound

 int ||eta(h)-P_R eta(h)P_R||_1 dh <=2sqrt(C_X,T/R).           (10)

Here dh denotes the exact count/mark/simplex dominating measure at that finite volume; the bound depends only on(9), so it survives changes of that representation. It also follows for arbitrary positive operator-valued measures by first taking their finite scalar trace measure.

At fixed R, all matrix-entry measures of P_R Q_epsilon P_R have total variation dominated by its positive trace measure, by positivity and Cauchy. Tightness on H_T and finite matrix dimension permit a further weak subsequence. Diagonalize over integer R. The estimates(10) make these finite-rank limits Cauchy in integrated trace variation as R grows; compatibility gives a positive trace-class-valued limiting measure Q, of trace one, whose scalar trace is the SAME classical P. This may alternatively be constructed from matrix-entry Radon-Nikodym densities against P; positivity of every finite compression and the trace bound give a positive trace-class density almost everywhere.

Precisely, along that subsequence,

 int Tr[A(h)Q_epsilon(dh)] -> int Tr[A(h)Q(dh)]              (11)

for every bounded operator-norm-continuous A:H_T->B(H_X). To justify the whole test class, first restrict to a compact bounded-count event set and finite R. Finite-dimensional matrix measures converge weakly there; tightness handles the discarded event tail and(10) the quantum tail. No uniform norm continuity in electric energy is needed.

For a fixed finite time partition and capped original word readout, the inverse images of register values have boundary only at deterministic bin times (and coincident endpoints). These are P-null. The finite-rank matrix measures therefore converge on each such event, and(10) promotes this to trace norm of its quantum payload. Summing over the finite register gives the earlier finite-bin/cap instrument limits, now as marginals of Q. Removing the cap is permitted in the UNCONDITIONAL binned cq trace norm because overflow trace is bounded by K_T/M on both sequence and limit. This does not imply continuous-timestamp trace variation or normalized postselected-state convergence.

Only a terminal quantum output is claimed in(11). Noncommuting multi-time quantum measurements would change the instrument and need their own contract. No classical trajectory of quantum fields, full conditional quantum filter, no-event generator or unique process law is identified by this compactness argument. The scalar limit can have bounded predictable intensity while its dynamics and physical selection remain unresolved.

## 7. Scope and what is actually gained

For every epsilon_n->0 with arbitrary allowed volume/spin growth, actual original finite-region continuous histories have convergent subsequences in event-time topology. Limits are simple, have no deterministic-time atoms, preserve actual first count moments, and admit natural-filtration intensities bounded by the supplied uniform B-operator constants. Terminal local quantum payloads admit compatible positive trace-class-valued history limits in weak timestamp topology. These conclusions use actual microscopic gains in the same recorded state; no record proxy or different law was matched to data.

The full microscopic quantum generator, unique limiting history, spatial boundary independence, higher microscopic count moments, quadratic energy/W1, unbounded conditioned electric tails and physical law/clock selection remain open. The source is an optional compensated qutrit/spin model, not a consequence of native M2 axioms. The result gives no axiom inconsistency or completed TOE.

Closest actual main prior: LOCAL_BACKGROUND_AND_UNRESTRICTED_ORIGINAL_RECORD_COUNTS... was fully read; it uses bounded effective hazards and fixed-volume microscopic finite-bin-then-mesh transfer. The photon readout parent's entire relevant section C was read and has the same fixed-graph/ordered-limit boundary. Existing campaign PR9399 has a complete effective timestamp instrument; its state is not used here. The new mechanism is the register-dimension-independent ACTUAL G2 error together with positive tail-event projections and current bookkeeping. No broad mathematical novelty claim is made for the compactness or Radon-Nikodym steps.

No new numerical science computation was run. The proof and exact input identities are the evidence; finite simulations would not prove its joint-volume quantifiers. This root candidate must receive a focused independent reconstruction before it is reused or packaged.
