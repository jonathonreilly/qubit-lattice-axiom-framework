# A candidate local autonomous supplier with volume-independent resource density

Author proof candidate. Not independently checked, formally reviewed, audited or retained. No new calculation is asserted in this report. The supplied law and apparatus inputs are those bound in PRE_FREEZE. The fixed-volume autonomous source and thermodynamic original-process sources are provisional reviewed open-branch premises, not main authority or adopted foundations. All reused exact source formulas are restated at their needed scope below.

## 1. Target, topology and assumptions

Fix supplied positive K,delta,kappa, a finite T>0, a finite output region X, finite original-mark centers F, and finitely many passive observation times including0,T. Fix either the original resolved edge/sign instrument or the unnormalized coherent-per-edge instrument. For every positive local process and mean-energy/ledger tolerance, the proposed construction has finite constants R,n,s,M,k0,Kc, independent of torus side L, and a positive time-independent enlarged-cell Hamiltonian H_AUT,L on each even cubic torus L>=24. Its source begins in the ORIGINAL Omega product, its clocks in specified independent phase packets and all flags/copies blank.

The intended approximation is the trace norm of the joint finite-F binned original-history and X quantum output under the prescribed passive grid tests, with an optional external reference carried unchanged. It is local in X,F; no fixed global trace-error tolerance over every mark on an arbitrarily large torus is asserted. Uniform per-center original source-energy approximation and a clock/interaction energy ledger are also claimed below. Every original later birth remains in the target. Apparatus dimensions, local coupling bounds, encoded range and initial energy per center may depend strongly on accuracy,T,X,F but not on L.

The actual source carrier is A:C² and B:C³ with six incoming integer rotors. Gauss is div E=q-1_A, Omega is plus on A, empty on B and zero field. On the A-occupied carrier,

 h=K D+sum_(unordered dist2 a,c) A_ac,
 D=sum_(a->b)(1-n_b)E_ab(E_ab-q_a),
 A_ac=-2delta(F_c F_a P)* (F_c F_a P),
 B_ab,sigma=P j_ab,sigma F_a P,
 B_ab,coh=B_ab,+ + B_ab,-.

F_a moves the existing A charge q to an empty B neighbor d and shifts E_ad by -q. The elementary j creates sigma,-sigma at empty a,b and shifts E_ab by sigma. Full words begin/end in P and preserve Gauss. A whole A_ac or B is compressed for a field box; its internal F steps are never separately clipped. The supplied source has all later-sector bounds

 ||A_ac||<=288delta, ||A_a||<=2592delta=v0,
 A_a=(1/2)sum_c A_ac,
 Gamma_a=kappa sum_(original m at a) B_m*B_m,
 ||Gamma_a||<=g0=80kappa.

The quantum realization, GKSL interpretation, couplings, time, source preparation, local completions and readout remain supplied hypotheses. No native one-M2-per-site or selected physical clock is inferred.

## 2. Dimension-independent local influence, with domains explicit

First consider only finite-dimensional cells. For any observable O, including a spatially amplified external reference, define c_x(O)=sup_(unitary U_x)||[O,U_x]||. Twirling the factors of a finite set Z gives a normal conditional expectation E_Z onto their commutant, with

 ||O-E_Z O||<=sum_(z in Z)c_z(O).

This follows by integrating O-U_z O U_z* one factor at a time and telescoping; the other twirls are contractions. If C_Z is a local unital CP map supported on Z, equal to identity on the exterior, and d_Z=||C_Z-I||_cb, then (C_Z-I)E_Z=0. For x outside Z, locality and contraction give c_x(C_ZO)<=c_x(O). For x in Z,

 c_x(C_ZO)<=c_x(O)+2d_Z sum_(z in Z)c_z(O).             (2.1)

Thus its influence is bounded by the nonnegative matrix I+2d_Z 1_Z1_Z^T. A disjoint color layer with support size<=sigma increases row and column sums by at most1+2sigma max d_Z. For a metric weight exp(mu distance), multiply this increment by exp(mu d), where d bounds support diameter. Products are bounded by the exponential of the sum of these local increments, independently of total volume and cell dimension.

For a local difference map E supported on Z, with E acting as zero on the exterior algebra and cb norm e, the same twirl gives

 ||E(O)||<=e sum_(z in Z)c_z(O).                       (2.2)

Telescoping two circuits and using contraction therefore sums local defects against a finite influence kernel, not against total volume. Omitting interactions outside a spatial buffer gains an exponential distance factor from its weighted kernel. The initial influence vector of O_X is bounded by2||O||1_X. All estimates remain uniform over the entire observable unit ball and its matrix amplifications.

Local Hamiltonian propagators satisfy the analogous bounds by finite-volume Lie-product approximation into local unitary steps. Such a step has cb deviation<=2dt||H_Z||. Time-dependent bounded coefficients are treated by step approximation followed by their finite-volume integral equation. One may use a deliberately loose growth exponent4sigma exp(mu d) times the sum, over a fixed finite coloring, of the integrated maximal local coefficient norm in each color. Both forward and backward orders have the same bound. The finite coloring depends only on support/incidence, not on volume or local dimension.

For two Hamiltonian programs, Duhamel places the reference-evolved observable inside each local commutator and only a norm-preserving perturbed unitary outside. Its difference is therefore controlled by the REFERENCE influence kernel and the integrated local perturbation. The perturbation need not have the same propagation constant. This fact will price random clock offsets without a global good-clock event.

An unbounded onsite free clock term is NOT handled by an infinite-dimensional Haar average. Remove it in its product interaction picture. First prove the resulting locality estimate for arbitrary finite Fourier compressions, where the above argument applies and the interaction norms/geometry are uniform. At fixed finite spatial volume, exact clock-prefix Dyson convergence from the prepared finite band gives vector-norm convergence as that compression tends to infinity. Local trace norm then converges. Passing the uniform spatial-boundary estimate through that fixed-volume limit supplies precisely the prepared-state ideal-clock locality used below. No whole-space operator-norm clock convergence or normal infinite Haar measure is claimed.

## 3. Uniform prepared rotor field-box approximation

The previously checked thermodynamic proof gives common-small-time locality by a connected adjoint series in the electric interaction picture. Each center coefficient is bounded in cb norm by lambda=5184delta+160kappa, has support in a radius4 ball of129 cells, and annihilates observables on disjoint supports. A length-j string on x cells has at most16641^j(q)_j choices, q=max(1,ceil(x/129)), and enlarges radius by at most8j. Its tail is

 R_(q,m)(z)=sum_(j>m)binom(j+q-1,j)z^j,
 z=16641lambda t<1.

The one-step commuting electric halo only enlarges the initial anchor by one. This argument applies to every full-word product box |E|<=R with the SAME constants: the electric terms still commute and the bounded whole-word norms and exact losses are unchanged or smaller. Finite-region mark instruments anchor all monitored gains in X union F, keep every loss and unobserved gain, and have the same spatial majorant with a finite larger anchor. Their monitored label-number tail is bounded by (80kappa|F|T)^j/j!.

At all finite times, subdivide into finitely many intervals where the majorant converges. Approximate each local CP evolution by a finite-region CP map, then use contraction and a successively enlarged finite region. The required regions and error bounds are uniform in R and dimension. This is the fully checked finite-subdivision construction, not point-norm continuity of the rotor electric group.

Consequently, for a prescribed finite-output/instrument tolerance, first choose a finite spatial patch large enough to localize BOTH the full rotor process and every boxed process uniformly over R and torus volume. On this fixed patch, remove the field box by the prepared-input Dyson argument: Omega has zero fields; a complete magnetic/loss multiplier shifts the radial total field by at most4, a jump by at most2, and every finite-order coefficient agrees once R exceeds all its internal prefixes. The bounded-perturbation factorial majorant on this finite patch controls its tail at every finite T. Passive clock-independent record copies do not change the field prefixes or total simplex volume. This proves local trace/instrument convergence from Omega uniformly in volume as R grows. On small tori a metric buffer may contain the entire torus; its cardinality is still bounded by the common cubic-ball overcount, so the same resource bound applies.

For local source energy, use the actual uniform moment estimate for Q_S=1+sum_(links in S)|E|. If u=p/2 and b_u(s)=(2s+1)(1+s)^u, then in both full and boxed source processes

 Tr(Q_S^p rho(t))<=exp(C_p(S)t),
 C_p(S)=2b_(p/2)(4)V_S+[b_(p/2)(2)^2+b_(p/2)(4)]G_S.

V_S and G_S sum only original bounded magnetic and jump strengths meeting the finite link set S, hence are independent of volume and box. This follows by weighted spectral-difference bands and exact cancellation of disjoint gain/loss; the electric part commutes with Q_S. A local quadratic form O satisfying ||O psi||<=C||Q_S²psi|| has spectral-tail expectation at most2C Tr(Q_S^4 rho)/r² after truncation to Q_S<=r. First choose r, then a local trace tolerance, then the field box R. This proves a uniform local source-energy comparison without inferring moments from trace norm. The original local assignment is h_a=K D_a+A_a; summing it gives h exactly.

## 4. Bounded-color original collisions

At the chosen field box R, use h_R and complete compressed B_m. Shift h_+=h_R+v0 N I>=0. The source local norm is bounded, for example by e_R=12K(1+R)²+v0 per center, and each center support lies in a radius3 ball. Thus all local influence constants are finite and independent of volume.

Refine the prescribed finite observation grid into bins tau_k with max tau_k tending to zero and each prescribed time an exact bin boundary. Subdividing each original interval nearly equally ensures min tau_k>=max tau_k/2 once the refinement is fine. Require g0 max tau_k<=1/2. At each center/bin define

 K_a0=sqrt(I-tau_k Gamma_a,R),
 K_am=sqrt(tau_k kappa) B_m,R.

Their exact instrument is CPTP. Its cb deviation from identity on an original-word append space is at most3g0 tau_k; its difference from the exact center Lindblad exponential is at most7g0²tau_k². These estimates follow from the scalar square-root remainder and the exponential remainder with norm2g0, and retain original multiple-event terms in the comparison.

Observed word registers may be made finite with an overflow label. To define a near-identity extension on their complete algebra, use jump Kraus L_m tensor |append_m(w)><w| for every classical word w, while the no-event Kraus keeps the word. Their adjoint products still sum to Gamma tensor I. Overflow coarsens only observed data; the source continues to evolve and jump. Original histories are classical, so this extension changes no claimed input. Its overflow probability is priced by the original finite-F count tail and the instrument comparison. It does not reset an arbitrary record factor at every step.

The overlap graph of A stars has degree18, so19 colors suffice. Same-color stars and their local records are disjoint. Apply one color layer after another in each bin, then exact free evolution exp(-i tau_k h_R). Equation(2.1), with d<=3g0 tau_k, yields a spatial influence bound depending on sum tau_k=T and19 colors, independent of the refinement. Both this circuit and the bounded boxed Lindblad evolution can therefore be localized to a COMMON finite patch before choosing the mesh. On that patch the ordinary finite-dimensional collision/Trotter bound is O(T max tau_k) with a finite patch-dependent constant. This proves uniform local consistency of the colored program as the mesh shrinks. No total-volume event bound or empty exterior is used.

The physical apparatus uses one fresh finite flag F_ak and copy E_ak per center/bin, of dimension13 resolved or7 coherent. With R_a psi=(sqrt(tau_k kappa)B_m psi)_m, the Julia unitary

 U_flag=[[sqrt(I-R_a*R_a),-R_a*],[R_a,sqrt(I-R_aR_a*)]]

has exactly the required ready column. Conjugating U_flag tensor I by the local modular copy makes U_ak preserve the matched span{|m,m>}. A positive logarithm0<=G_ak<=2pi can be chosen within these same local invariant blocks. It preserves Gauss and the matched record code. At each ideal completed pulse, tracing E gives the ORIGINAL instrument. In the coherent case only the original edge is copied, never its two signs.

A fine bin can contain multiple continuous observed marks. If their within-bin temporal order is retained in the requested output, arbitrary deterministic tie ordering differs only on the multiple-observed-mark event. Its total probability is bounded by a constant times(80kappa|F|)^2 T max tau_k. Unobserved events everywhere else are not restricted by this local estimate.

## 5. Scheduled pulses without a volume-dependent sweep

Use one common color-slot program at every center of a color. Let chi=19 and choose s<=min tau_k/(8chi+4). In each bin place successive disjoint triangles of width2s, area1 and height1/s, with guard neighborhoods around every bin boundary. All same-color G_ak are disjoint and commute. The triangle program produces their exact layer when h_R is omitted during its pulses.

The deterministic program has a finite integrated local strength independent of s: its clock-control part is bounded by a constant times2pi chi n, where n is the number of bins. This is because the integral of every pulse is1 and the maximum over finitely many colors is bounded by their sum. The free source contributes a fixed local strength times T. Let C_prog be any of the explicit finite influence constants from section2 for this integrated budget and the finite number of passive grid copies. C_prog can be fixed BEFORE s.

Dropping free source evolution during the pulse windows, and moving the short initial guards to the end of each bin to match the stated free step, costs an integrated local source perturbation bounded by a fixed multiple of n chi s e_R. Duhamel and the local influence estimate therefore give a local process error tending to zero with s. This is the local version of the finite-volume pulse/free comparison. It does not use the static supremum1/s to choose the deterministic-program cone; that would create a false circular resource estimate.

Replace each triangle by its positive degree-M Fejer convolution f_ak on a circle of length Lc=4T. Its integral is1, norm<=1/s, variation<=2/s, and the pulse sum at a center is<=1/s. Explicit coefficients are

 fhat_j=(1-|j|/(M+1)) exp(-ij omega t_ak) sinc²(j omega s/2)/Lc,
 omega=2pi/Lc, |j|<=M.

The bounds

 rho1<=Lc[1+log(M+1)]/[(M+1)s],
 rhoinf<=Lc[1+log(M+1)]/[2(M+1)s²]

control its L1 and supremum error. Local Duhamel prices smoothing by C_prog times a fixed geometric factor times n rho1. The integrated local strength of the smoothed reference is still bounded by the same pulse-area budget, independent of M.

## 6. Ideal translation clocks and local jitter averaging

The analysis model has one circle clock per A center, P=-i d/dx, initial band

 beta(x)=[Lc(2k0+1)]^-1/2 sum_(m=-k0)^k0 exp(im omega x),
 Pr(|x|circle>sigma)<=theta:=Lc²/[4(2k0+1)sigma²].

Its finite-volume Hamiltonian is h_++sum_a P_a+sum_ak f_ak(X_a)G_ak. The interaction is bounded at each finite volume, so this is self-adjoint by bounded perturbation. Its exact characteristic formula gives, after tracing clocks, an average of source/record programs with coefficients f_ak(t+y_a), weighted by product |beta(y_a)|². This remains true as a CP process with passive clock-independent copies inserted at the prescribed times. Conditional clock marginals need not remain product; only the unconditional characteristic representation is used.

For one good clock |y_a|<=sigma, total variation gives integrated pulse mismatch<=2n sigma/s. For a bad clock, positivity and the circle-area normalization give the bound2n. Multiplying by ||G||<=2pi and averaging gives an integrated perturbation per center bounded by4pi n(sigma/s+theta).

Duhamel compares each random program with the deterministic smoothed reference. The norm-preserving perturbed propagators occur outside its commutator, while the deterministic reference influence kernel occurs inside. Average the local perturbation against that kernel. A finite color sum bounds the integrated expected incident strength; its constants do not depend on volume. Thus the local jitter error is at most C_prog times a finite geometric factor times n(sigma/s+theta). This avoids a global Ntheta probability and requires no uniform velocity for all bad-offset programs. The same bound, with a fixed additional influence factor, covers the finitely many passive local grid tests.

## 7. Positive finite clocks and noncircular resource selection

Implement the clock band |m|<=Kc with

 H_Ca=omega sum_(m=-Kc)^Kc(m+Kc)|m><m|>=0,
 F_ak=Pi_Kc f_ak(X_a)Pi_Kc>=0,
 V_K=sum_ak F_ak G_ak,
 H_AUT=h_++sum_a H_Ca+V_K>=0.

Compression is ordinary Toeplitz compression, not a cyclic Fourier shift. Per center0<=sum_k F_ak G_ak<=2pi/s, uniformly in Kc and volume. Free clock energies are onsite; remove them in the product interaction picture. The static interaction therefore has fixed local strength controlled by e_R and2pi/s, independently of Kc.

After R,mesh,s,M,k0 are fixed, choose a finite spatial buffer using section2 for the static apparatus, around all observed source/record cells and around a representative local interaction-energy star. Its size is independent of Kc and total volume. The corresponding ideal prepared-clock locality follows by the finite-compression limit explained in section2. Inside this fixed patch let v_patch<=2pi N_patch/s bound its interaction norm. Starting in the product band k0, every interaction insertion changes one clock momentum by at most M, even with the source h_R present in the free picture. Every word and prefix through r agrees exactly in the ideal and finite clocks if Kc>=k0+Mr. Thus their finite-patch trace/instrument error is at most

 4 sum_(j>r)(v_patch T)^j/j!.

The same bound holds with passive clock-independent copies: total ordered simplex volume is still T^j/j!. Choose r and then Kc. Later increasing Kc changes only onsite free norms, so it does not invalidate the spatial buffer. This is the decisive noncircular clock-resource order.

All errors can now be made small in this sequence: local rotor-box error; colored-collision mesh error; triangle/free error; smoothing and local jitter; static-buffer boundary error; clock-band tail. The source observables and original histories are retained through each comparison. Finite composition and contraction sum the errors. For source energy in the boxed system, multiply the final bounded-output trace tolerance by a common local norm bound on h_a,R; the earlier rotor-box energy estimate separately prices the unbounded target. No energy inference is made from trace norm alone.

## 8. Resource density and exact controller ledger

At every observation boundary, every ideal triangle vanishes on the clock-coordinate neighborhood |y_a|<=sigma<s. The ideal clock marginal is translated exactly even after source/record entanglement and unconditioned passive reads. Positivity gives, per center,

 0<=<V_a><=2pi[n rhoinf+theta/s].

A local joint finite-clock trace comparison adds at most(2pi/s)eta_clock. Define

 nu=2pi[n rhoinf+theta/s]+(2pi/s)eta_clock.

After s is fixed, M,k0 and the spatial/clock cutoffs can make nu as small as required, with no dependence on volume. The finite apparatus then has0<=<V_K>/N<=nu at every designated boundary. The same bound holds immediately after an unconditioned local flag read, since it leaves clock marginals unchanged and0<=G_ak<=2pi remains available. A read touching centers F can change mean energy by at most2nu|F|; free source and clock terms commute with that flag read. This is a supplied measurement-apparatus exchange allowance, not zero-cost observation.

For the closed run, exact conservation gives on every finite torus

 -Delta<E_clock>/N=Delta<h_R>/N+Delta<V_K>/N.             (8.1)

The scalar positivity shift cancels. Uniform per-center source-energy approximation and the endpoint bound therefore give, with their chosen tolerances,

 | -Delta<E_clock>/N-Delta<h>_original/N |
 <=source_mean_transfer_error+2nu.                     (8.2)

If actual reads inject total mean energy W_read, add W_read/N to the left clock debit in(8.1); its absolute allowance is the sum of the per-read estimates. No postselected branch is assigned this mean bound. The original source mean increment equals its integrated original source current by the separately checked uniform local-energy balance. No equality of instantaneous pulsed clock-current operators or work distributions is asserted.

The initial clock mean per center is omega Kc, maximum2omega Kc, and variance omega²k0(k0+1)/3. Flags/copies have supplied zero free spectrum, while every coupling is included in V_K. A sufficient initial positive total-energy density bound is e_R+omega Kc+2pi/s. All are finite and independent of L. The chosen parameters may be extremely large; no efficiency claim is made.

Each A cell contains its two-state source, one finite clock and2n flag/copy factors; each B cell contains its qutrit and six(2R+1)-state links. Encode them factorwise in finite qubit blocks, preserving the prepared code and original source/readout factors. With qE=ceil log2(2R+1), qC=ceil log2(2Kc+1), and qF=4 resolved or3 coherent, sufficient qubit counts are

 bA=1+qC+2n qF, bB=2+6qE.

A block side ceil_cuberoot(max(bA,bB)) is independent of full volume. The existing explicit star/magnetic geometry gives finite range at most seven block widths and finite arity determined by these local factors. This is an enlarged-cell engineered realization, not unchanged nearest-neighbor native M2 dynamics. Exact coefficient/preparation choices are inputs; a precision-cost theorem is not additionally claimed here.

## 9. Scope, proof state and the next check

The proof candidate changes the observation topology from an entire fixed-volume history to fixed regional original-record/quantum outputs, while making the apparatus resources uniform in volume. It keeps the actual source carrier/law, Omega, original coherent or resolved maps, and controller/interaction energy accounting. It does not establish a globally fixed trace error over all lattice records, exact continuous timestamps, stationary/catalytic supply, exact flag permanence, microscopic M4, physical clock selection, a gravity source/action identification or a new axiom.

No decisive finite computation has yet been executed for this new packet. The old source-star, Gauss, matched-record, clock-prefix and energy-ledger controls remain input evidence at their frozen hashes, not new runs. The new proof needs a focused independent check of the local influence/collision argument, expected-jitter Duhamel step, rotor-box limit order and resource/ledger composition before downstream reuse. A milestone requires its own self-contained source, primary/cache, conformance, graph acknowledgment and formal source review; this candidate is not a PR receipt.
