# Independent positive coefficient errors in one common-product program cell

New author derivation requiring a distinct check. The exact supplied cell admits an explicit NONZERO independent relative coefficient box at a declared finite horizon whenever the nominal complete bound has positive slack. Evaluating the perturbation on the dressed code replaces a crude detuning-size coefficient O(D1) by O(b). It does not eliminate the effect of independent endpoint compensation errors: those can produce an exact relative occupied-state shift of order epsilon b, much larger than the desired coupling a=2b²/D0.

This is a one-cell complete-output theorem with a common literal input and actual phases. It neither supplies native positive blocks nor proves network robustness. ROOT requested an independent-block error interface and highlighted the cancellation issue; that suggestion is exposure, not evidence for the result.

## 1. Nominal model and the independent box

Take the supplied six-qubit geometry, program patterns000/111 and FULL positive Q convention of739e99c4. Fix b>0,D1>D0>2b and a=2b²/D0. Use the same literal isometry J: arbitrary endpoint state tensor vacant mediator, with the three equal program contents supplied. All four endpoint occupations, coherent legal program superpositions and passive references are allowed.

Resolve the positive mediator block into its two orthogonal projectors. The actual Hamiltonian is

 H_tilde=Q_(b_L)(u,m)+Q_(b_R)(m,v)
       +c_u(I-n_u)+c_v(I-n_v)
       +[d_0 P0_(c_m)+d_1 P1_(c_m)]n_m
       +a_u P0_(c_u)n_u+a_v P0_(c_v)n_v.              (1)

There are eight positive scalar coefficients b_L,b_R,c_u,c_v,d_0,d_1,a_u,a_v. For a SINGLE common relative tolerance 0<=epsilon<1, allow them independently to lie in

 b_L,b_R,c_u,c_v in b[1-epsilon,1+epsilon],
 d_p in (D_p-2b)[1-epsilon,1+epsilon], p=0,1,
 a_u,a_v in a[1-epsilon,1+epsilon].                   (2)

No correlation among these eight deviations is imposed. Each block shape, occupation frame, absence of other couplings and positive-program interpretation remains exact. This is not a block-shape, hopping-phase, program-bit-flip or preparation-error model. All coefficients stay strictly positive for epsilon<1.

Both program occupations and total head number remain conserved. For legal p, exact expansion gives

 H_tilde,p=C_tilde I
      +h_u,p n_u+h_m,p n_m+h_v,p n_v
      -b_L X_h,um-b_R X_h,mv,
 C_tilde=c_u+c_v,
 h_u,p=b_L-c_u+a_u(1-p),
 h_v,p=b_R-c_v+a_v(1-p),
 h_m,p=b_L+b_R+d_p.                                 (3)

C_tilde is the ACTUAL vacuum energy. It is common to both legal programs and all head occupations as a scalar term. The remaining potentials are not global phases. They can be negative after this scalar is extracted without violating positivity of(1). No endpoint compensation or mediator detuning is secretly retuned after the errors.

Let H be the nominal source739 Hamiltonian and H_c=H-2bI. Let A_c=P0 tensor a Rminus be its desired logical generator, with disabled identity, and Rminus=(n_L+n_R-X_h,LR)/2. Targets considered separately are

 actual-phase: exp(-it C_tilde) J exp(-it A_c),
 fixed nominal-phase: exp(-i2bt) J exp(-it A_c).       (4)

Both use the SAME nominal logical operation, common literal injection and full outputs. No input- or program-dependent phase fit is allowed. Rminus includes double-occupation energy1.

## 2. Nominal dressed isometry as a proof device

For each nominal program use the exact dressed injection Jd_p of739, and combine them into Jd. Its exact relation is

 H_c Jd=Jd[A_c-P1 tensor epsilon_off Rplus],
 epsilon_off=4b²/[sqrt(D1²+8b²)+D1],
 Rplus=(n_L+n_R+X_h,LR)/2.

Set r0=sqrt(2)b/D0,r1=sqrt(2)b/(D1+epsilon_off), alpha_p=(1+r_p²)^(-1/2), beta_p=r_p alpha_p, and

 kappa_code=||Jd-J||=sqrt(2-2alpha0)<=r0.             (5)

This is the full endpoint four-state code distance. It is not the sharper isolated propagator leakage2beta0. The dressed states are used only in the proof; actual preparation is still J.

A crucial full-domain identity is

                 ||n_m Jd_p||=beta_p.                (6)

Vacuum and antisymmetric one-head code columns have zero mediator occupancy. The symmetric one-head dressed column has mediator amplitude beta_p. The double-head dressed column has mediator component beta_p times(|110>+|011>)/sqrt(2), which lies in a different number sector. These columns are orthogonal, so their operator norm is beta_p, not a sum over input columns. In addition

              D0 beta0<sqrt(2)b,
              D1 beta1<sqrt(2)b.                     (7)

The same controlled-sector calculation works with arbitrary reference entanglement. It does not require the ACTUAL perturbed dressed code to exist, share the nominal eigenvalues or be invariant.

## 3. Perturbation action, with independent cancellations paid

Write Delta_c=(H_tilde-C_tilde I)-H_c. On program p define endpoint potential errors e_u,p=h_u,p-a(1-p), e_v,p=h_v,p-a(1-p), mediator error e_m,p=h_m,p-D_p, and hopping deviations delta b_L,b_R. Equation(2) gives

 |e_u,p|,|e_v,p|<=2epsilon b+epsilon a(1-p),
 |e_m,p|<=epsilon[2b+(D_p-2b)]=epsilon D_p,
 |delta b_L|,|delta b_R|<=epsilon b.                 (8)

Thus the two endpoint occupation terms acting on Jd cost at most4epsilon b+2epsilon a, using ||n_u||=||n_v||=1. This includes double occupation. Each hopping X_h has full norm1, so the two hopping perturbations cost at most2epsilon b. Equations(6)--(7) bound the mediator term on the dressed code by sqrt(2)epsilon b even if D1 is large. Combining the orthogonal legal program sectors by a maximum yields

       ||Delta_c Jd||<=epsilon B_act,
       B_act=(6+sqrt(2))b+2a.                       (9)

No commutation of Delta_c with Jd or the nominal source Hamiltonian is assumed. This is a bound on the entire dressed four-state input, not just its selected one-head column. It retains independent b_L,b_R and endpoint compensation errors. Its improvement over ||Delta_c||=O(epsilon D1) follows from the EXACT small mediator amplitude of the nominal dressed code, not from an unsupported perturbation of a multiple pole.

The actual Hamiltonian residual against the desired nominal logical generator is consequently

 (H_tilde-C_tilde I)Jd-Jd A_c
       =Delta_c Jd-Jd(P1 tensor epsilon_off Rplus).

Its norm is at most epsilon B_act+epsilon_off. Rectangular Duhamel and the two endpoint replacements Jd to J prove, for every real t,

 ||exp(-it H_tilde)J-exp(-it C_tilde)J exp(-it A_c)||
 <=min{2,2kappa_code+|t|(epsilon_off+epsilon B_act)}.  (10)

This is full physical output, including mediator and program registers and all endpoint occupations. An all-enabled restricted program removes epsilon_off but is not needed for(10). No spectral assumption on H_tilde is required beyond self-adjointness; large-time usefulness still depends on the stated bound. The estimate is linear in horizon but uses the dressed residual coefficient rather than full T||DeltaH||.

## 4. Unknown phase and one explicit nonzero box

Because |C_tilde-2b|<=2epsilon b, comparison with the SAME fixed nominal-phase target costs the separate exact scalar distance2|sin[t(C_tilde-2b)/2]|. Therefore

 fixed-phase error <=min{2,2kappa_code+|t|[
                      epsilon_off+epsilon B_fix]},
 B_fix=(8+sqrt(2))b+2a.                             (11)

Knowing the actual scalar permits(10), while ignorance does not permit silently fitting it away. For the channel associated with the entire cell the common scalar is irrelevant; this does not remove the relative occupied-state errors in(8). Program-dependent detuning/onsite errors cannot be absorbed into C_tilde: their terms vanish on vacuum and differ on occupied inputs.

For any chosen nominal b,D0,D1 and horizon T>0 with positive slack

 0<eta<2,
 mu=eta-2kappa_code-T epsilon_off>0,

one explicit sufficient independent box is

 epsilon_* = min{1/2, mu/(2 T B_fix)}.              (12)

All actual tuples in(2) with epsilon<=epsilon_* then satisfy fixed-phase error at most eta-mu/2<eta on |t|<=T. The certified actual-phase upper envelope is no larger; no ordering of exact errors to the two distinct targets is asserted. Equation(12) is a derived single analytic box, not a search or optimized bound. It is nonzero for every nominal finite tuple with the declared slack. If that slack is absent, this particular certificate gives no nonzero box; it is not a physical impossibility statement.

A physical incident-load cap can be imposed simultaneously. For each of the nominal combined mediator blocks, the perturbed norm is max(d_0,d_1)<=(1+epsilon)(D1-2b); it is not necessary to add their norms when they are implemented as one block with independent positive eigen-coefficients. Every other block norm likewise grows by at most1+epsilon. Hence every incident sum is at most1+epsilon times its nominal value. If the nominal maximum incident sum D1+2b is at most2Lambda/3, then epsilon_*<=1/2 guarantees actual incident loads<=Lambda. Under a convention counting the two mediator projectors separately, the nominal incident sum must instead include BOTH; this alternate accounting is not covered by reusing D1+2b.

The cell has six qubits and the same supports. It has eight scalar projector/bond coefficients, or seven listed blocks when the two mediator-program projectors are combined. The independent coefficient box is meaningful in either convention, but physical load bookkeeping must match the implementation. No new preparation, sensor, control sequence or external calibration operation is supplied by the proof.

## 5. Gate-time scales and an exact sensitivity diagnostic

At T_gate=pi/a=pi D0/(2b²), the nominal certificate is

 2kappa_code+T_gate epsilon_off
          <2sqrt(2)b/D0+pi D0/D1.

The new fixed-phase perturbation term has explicit ceiling

 epsilon T_gate B_fix
   =pi epsilon[(8+sqrt(2))D0/(2b)+2].              (13)

The actual-phase expression replaces8+sqrt(2) by6+sqrt(2). Thus at positive nominal slack the sufficient relative tolerance is of order eta*b/D0; if the nominal mixing ratio b/D0 itself is chosen proportional to eta, this route gives a relative box of order eta², with declared constants and exact tuning before errors. This is a sufficient one-cell scaling, not a necessary hardware law. Large disabled D1 is no longer in the perturbation coefficient. Small effective exchange a, however, still makes independent strong endpoint compensation errors consequential.

There is a direct exact example explaining that remaining sensitivity. Keep ALL coefficients nominal except c_u=c_v=b(1+epsilon), a permitted tuple of the independent box. Then C_tilde=2b+2epsilon b and the centered endpoint diagonals in program p are a(1-p)-epsilon b. Reflection symmetry survives, so the physical one-head antisymmetric state A=(|100>-|001>)/sqrt(2) remains an EXACT eigenvector, with centered energy a(1-p)-epsilon b. It is also a literal-code vector with no mediator component. Relative to the actual-phase target(4), its vector discrepancy is exactly

                         2|sin(epsilon b t/2)|.    (14)

This is not caused by a large mediator population or by an unknown common scalar. Vacuum has exactly the actual C_tilde phase and no such centered error. Consequently vacuum/antisymmetric coherence detects the relative shift as well; a common rephasing of the entire target cannot make both columns agree. The example concerns this explicitly allowed error direction and fixed target, not a necessary tolerance theorem for arbitrary architectures or a proof of failure at every error value/time.

It also shows why nominal cancellation of endpoint terms is not maintained under independent positive block errors. Their deviations are of order epsilon b, rather than epsilon a. A refined mediator-only error model might permit a better scale, but that would not be the independent eight-coefficient box considered here. No such unproved improvement is claimed.

## 6. Scope, exposure and next check

This result allows independent positive scalar deviations from the exact nominal correlation at a bounded horizon, while retaining the common literal preparation and every physical output. It does not remove the need to supply nominal roles, occupation basis, positive block shapes, conserved program contents, their initialization, finite strength or original isolation. Errors on program/projector directions, unwanted extra couplings, arbitrary environment contacts and state-preparation errors require other estimates. There is no transfer to the old emitted-packet apparatus, no network robustness theorem, native supplier, capture/reset or finite permanent halt conclusion.

Primary exact source739e99c44feb30f0bdc569d804f0e643ff993ab556056e1b6820f7012a9de088 and its distinct check809a2083527cf942e6a6e879a6211600c9f144938915a43dbcf56d5680858fb6 were completely read in the preceding coherent tasks. Sector sourcea94697cf9dd3c0b62a38b97a3cc64640b7d3eac41d48f625e1595ec7d857dd76 is my separate authored work; its restricted-domain N-independent conclusion is not a premise for this FULL single-cell four-state calculation. My prior cell/attachment authorship and network check are shared exposure, not independent evidence for this new tolerance proof.

The load-bearing new steps are(6)--(11), the phase separation, simultaneous load/box condition(12), and the exact antisymmetric diagnostic(14). A distinct checker should reconstruct these before integration. ROOT proposed the question and warned about independent endpoint cancellation errors. No desired numerical tolerance was assumed, no parameter sweep or symbolic/numerical scientific program was run, and no numerical operating point was selected.

Only this proposal was written. No canonical/W/Git/PR/checkpoint/prompt/model change or delegation occurred. No retained or publication status is assigned.
