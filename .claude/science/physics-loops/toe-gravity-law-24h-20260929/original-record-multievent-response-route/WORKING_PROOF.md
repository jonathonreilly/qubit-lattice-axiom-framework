# Working proof: marked tangent lift, source score and unresolved response

This is the complete analytic derivation for the new route. It is provisional pending focused checking. The original supplied model, finite-spin carrier, bare preparation, exact D_epsilon and original marks are unchanged. In particular none of the comparison families below is substituted for the actual microscopic law.

## A. Local factorization of the full dark/bright test corner

Use the checked signed-feedback notation. G=sum_mu g_mu, g_mu=j_mu*j_mu, P=ker G, A_mu=[j_mu,F], d_mu=[F*,j_mu], Z_+=[G,F], Z_-=Z_+*, R=[Z_-,Z_+]. Set

    Z_(mu,+)=[g_mu,F], Z_(mu,-)=Z_(mu,+)*,
    Btilde=sum_mu(A_mu*M_mu A_mu-d_mu*M_mu d_mu),
    E=R-Btilde.                                          (A1)

The chosen M_mu is precisely the bounded local diagonal pullback in the earlier complete proof, 0<=M_mu<=10. On P,

    M_mu A_mu P=j_mu G F P,
    M_mu d_mu P=-j_mu G F*P,
    A_mu P=j_mu F P, d_mu P=-j_mu F*P.                    (A2)

No input inverse of a small spin shift is used. All formulas hold for an entire original coherent-edge j as one operator, or for the original resolved family separately.

Direct expansion, BEFORE compressing the left side, gives

 R P=(F*G²F-FG²F*-GF*GF+GFGF*)P,
 Btilde P=(F*G²F-FG²F*
              -sum_mu j_mu*F*j_mu GF+sum_mu j_mu*Fj_mu GF*)P.

Therefore

    E P=sum_mu j_mu*(d_mu Z_+-A_mu Z_-)P.                (A3)

The apparent global products in(A3) can be made local. Choose a fixed cone C_mu containing j_mu,A_mu,d_mu,Z_(mu,+/-),M_mu. Declare mu~nu when these cones overlap, including mu itself. This is a symmetric bounded-degree relation, independent of spin and volume. Define

    v_mu=sum_(nu:mu~nu)(d_mu Z_(nu,+)-A_mu Z_(nu,-)),
    K=sum_mu j_mu*v_mu.                                 (A4)

For a disjoint pair of cones, all corresponding operators commute, while

    j_mu*d_mu P=Z_(mu,-)P,
    j_mu*A_mu P=Z_(mu,+)P.

The omitted ordered term(mu,nu) in(A3) equals
Z_(nu,+)Z_(mu,-)P-Z_(nu,-)Z_(mu,+)P. It cancels EXACTLY against the term(nu,mu). Thus

    E P=K P,  P E=P K*,  P K=K*P=0.                    (A5)

Every v_mu is now a bounded LOCAL operator, with uniform local norm and range. Its W grade is-1, its Ntot increment is+2, and it preserves Gauss. In particular it annihilates an input with every A site filled in its own cone. The construction retains all charge paths and their interference. No global record cap, static B mask or spin-boundary inverse appears.

For the complete polarized original-mark dissipator, write C_(j,l) for the derivative of D[j+lambda l]^* at zero, including the original append U_mu. Since j_mu P=0, its two gains vanish under P on both sides, but its two losses retain the test corner. Formula(A5) gives, for every full neutral joint test O,

 P sum_mu C_(j_mu,i v_mu)(O)P
                   =(i/2)P[E,O]P.                     (A6)

In detail its loss is -(i/2){K-K*,O}; under P it becomes
(i/2)P(K*O-OK)P. This equals the right side by(A5). In particular this formula does NOT discard dark/bright test corners. Those corners are what(A6) represents.

## B. A genuine local tangent based at the exact D_epsilon

Write its actual nonpositive jumps as

    L_(mu,r)=sqrt(kappa) epsilon^-1 J_(mu,r), r<=0,

and its full neutral Hamiltonian as H_diag. The hidden r branches are part of this mathematical diagnostic generator; only the ORIGINAL mu is appended. They are not observed grades and are not substituted for the coherent microscopic jump.

Define a differentiable local GKSL comparison family, based EXACTLY at D_epsilon, by

 L_(mu,0;lambda)=exp(i lambda M_mu)L_(mu,0),
 L_(mu,-2;lambda)=exp(-i lambda M_mu)L_(mu,-2),
 L_(mu,-1;lambda)=L_(mu,-1)+i lambda sqrt(kappa)epsilon v_mu,
 L_(mu,r;lambda)=L_(mu,r) otherwise,
 H_lambda=H_diag+(kappa lambda/2)Btilde.                  (B1)

For each lambda this is a legitimate finite-volume GKSL generator. All operators preserve the actual Gauss sector and charge, each jump raises Ntot by two, and the Hamiltonian preserves Ntot and W. All same-grade terms of D_epsilon are in its base. A change of jump in(B1) always carries the SAME original mu, preserving coherent signs inside that mark.

Let dot D denote its generator derivative at lambda=0. The phase terms, their Hamiltonian, and(A6) imply

    P dot D(O)P=(2delta/kappa)P T(O)P+P Err_epsilon(O)P,
    ||Err_epsilon||_local<=C epsilon.                   (B2)

To check the power, J_0/epsilon=A+O_local(epsilon), J_-2/epsilon=d+O_local(epsilon), whereas J_-1=j+O_local(epsilon²). The cross product of L_-1 and its variation in(B1) is kappa C_(J_-1,i v), so that error is O_local(epsilon²). The phase errors cost O_local(epsilon), conservatively. Its Hamiltonian derivative is exactly kappa Btilde/2. Combining it with(A6) restores R, not merely P R P. The physical coefficient epsilon²T is therefore its tangent at lambda=epsilon² kappa/(2delta), with an O_local(epsilon³) coefficient error on the dark input compression.

This is a LOCAL-INTERACTION norm assertion. For fixed local quantum and fixed monitored-register support it gives the usual finite incidence norm bound. It is not an operator-norm error independent of volume on arbitrary expanding backward tests. The family is a tangent representation; a finite value of lambda also contains quadratic and higher terms not assigned to the microscopic law. Away from the dark input compression, it is not asserted that dot D equals T.

## C. A common original-mark phase gauge and an actual source-score bound

Multiply EVERY jump in(B1), for every hidden grade and the SAME original mu, by exp(-10i lambda). This scalar phase does not change its GKSL generator or any original marked CP map. On a full original history it multiplies its Kraus amplitude by the scalar exp(-10i lambda times the number of marks), which disappears in that history's quantum gain. It does not change the relative coherent sign amplitudes. This is a freedom in a mathematical dilation, not a new readout or a field-dependent phase chosen from hidden quantum data.

The resulting tangent jumps at zero are

 dot Lhat_(mu,0)= i(M_mu-10)L_(mu,0),
 dot Lhat_(mu,-2)=-i(M_mu+10)L_(mu,-2),
 dot Lhat_(mu,-1)=i sqrt(kappa)epsilon v_mu-10i L_(mu,-1),
 dot Lhat_(mu,r)=-10i L_(mu,r) for the other r<=0.       (C1)

For the ACTUAL normal-form microscopic state sigma(s), with bare Omega preparation and all later original births, define the positive local diagnostic score

    s_mu(s)=sum_(r<=0)Tr[sigma(s) dot Lhat_(mu,r)*dot Lhat_(mu,r)].

For sufficiently small epsilon, all integer spins in the source domain, and 0<T<=1,

    integral_0^T s_mu(s)ds <=C(T²+epsilon²),             (C2)

with C independent of volume, spin, center and original mark type. Constants depend on the fixed supplied couplings and circuit. The coupled spin scaling may be imposed. The inequality holds for every positive joint extension with the same actual sigma marginal, without a conditional hole assumption. Its grade sum is a positive mathematical score, NOT a probability of newly observed grade events.

Here is the source-bound proof. The checked original count estimate and physical number identity give

    <N_B>_rho=2 E R_marks+<W>_rho.

Physical translation covariance and the checked count/defect estimates therefore imply, for each physical B site and T<=1,

    <n_b>_rho(s)<=C(s+epsilon²).

The finite-depth local projection inequality
Y*n_b Y<=2n_b+C epsilon² I gives the same order in sigma. It uses ||[n_b,Y]||<=C epsilon, not global closeness of Y to identity. The analogous argument gives local rotated <w_a><=C epsilon². The complete checked first-field theorem, including its colored-coordinate return, gives

    <|E_e|>_sigma(s)<=C(s+s²)+C epsilon².                (C3)

No postselected or hole-weighted field moment is used.

For a fixed cone containing M_mu,A_mu and their local halo, let P_ref fill all its A sites and empty all its B sites. Let p_bad=1-P_ref. It is bounded by the sum of the local w_a and n_b. At a reference input A_mu=j_mu F_a: the original birth follows an outward hop to one of the OTHER five neighbors. Immediately before that birth the only local hole is a and it has five vacant B neighbors. The exact spin bare loss is

    M_mu=10-(2/[S(S+1)])sum_(five eligible links) E_e²   (C4)

on each such path's output preimage. The fields in this sum are the input fields: the helper link just shifted is no longer an eligible vacant-B link. All spin boundary zeros are retained. For either original instrument the coherent amplitudes are finite sums of these actual paths, with uniformly bounded row and column multiplicity. Because |M-10|<=10, E²<=S|E|, and there are at most ten paths per input for one coherent mark, Schur/Cauchy estimates give

 [(M_mu-10)A_mu]*[(M_mu-10)A_mu]
       <=C p_bad+C/(S+1) sum_(e in cone)|E_e|.           (C5)

One may obtain this by first splitting the input into P_ref and its complement, at cost a factor two. On the complement ||(M-10)A|| is uniformly bounded. On P_ref, each squared path coefficient is at most20/(S+1) times the displayed first-field sum; the finite row/column counts price all coherent interference. No equality of amplitudes for different paths and no division by a boundary weight is assumed. The local extension of M is chosen as in the earlier proof, so(C4) lies in its unclipped range and is unchanged by its extension off the two dark path ranges.

Since L_0=sqrt(kappa)(A+O_local(epsilon)), (C3)-(C5) show its score integral is at most C(T²+epsilon² T). For r=-2, d has grade-2 and annihilates the locally all-A-filled input. Thus d*d<=C sum_(local a)w_a. With L_-2=sqrt(kappa)(d+O_local(epsilon)), its score costs C epsilon² T. The same grade support applies to the LOCAL v_mu from(A4); its own epsilon-prefactor in(C1) is harmless.

For r=-1 use the fully checked LOCAL original-gain budget, not a division of a colored global average:

    integral ||j_mu sigma^(1/2)||_2²<=C epsilon4,
    J_(mu,-1)=j_mu+O_local(epsilon²).

Hence integral||L_(mu,-1)sigma^(1/2)||_2²<=C epsilon². Squared triangle bounds its full coherent combination with epsilon v_mu in(C1) by C epsilon². Every other negative grade starts at J_r=O_local(epsilon²), and the number of grades per original cone is fixed; their total costs C epsilon² T. These steps prove(C2). The estimate includes the initial dressed layer and every later birth. It is not pointwise in time for the fast bare-j contribution.

For any nonnegative fixed spatial weights w_mu, summation gives

    integral sum_mu w_mu s_mu <=C(T²+epsilon²)sum_mu w_mu. (C6)

In particular a prescribed summable weight has a uniform-volume source bound. This is an actual microscopic source statement. It does not assert a bound on the reciprocal-weighted future response. No new numerical experiment is needed for the finite-path/operator proof.

## D. Complete many-event dilation: the surviving connection

For a differentiable finite-volume GKSL family with the same original mark labels, set

    A=sum_l L_l* dot L_l,
    Gamma=Im A-dot H,   Ndot=sum_l dot L_l*dot L_l.       (D1)

Here l includes any unobserved Kraus branches already present in that specified diagnostic, and Im A=(A-A*)/(2i). These expressions retain the complete loss derivative. To check the sign, infinitesimal no-event and event Kraus maps give

    V* dot V=i Gamma dt+o(dt),
    dot V*dot V=Ndot dt+o(dt).

The no-event derivative is -i dot H-(A+A*)/2; adding the event overlap A leaves i(Im A-dot H). For(B1) BEFORE the scalar original-mark gauge,

    Gamma=(kappa/2)(Btilde+K+K*)+O_local(epsilon),
    Gamma P=(kappa/2)R P+O_local(epsilon).              (D2)

Thus the connection retains HALF the complete R, including its full test corner. Post-event phases plus the REQUIRED Hamiltonian are not a centered martingale. After(C1), the exact connection is

    Gamma_hat=Gamma-10 sum_(mu,r<=0)L_(mu,r)*L_(mu,r).   (D3)

The sum in(D3) is EXACT. In particular the same-grade J_-1-j=O(epsilon²) correction can create an O(1) contribution after epsilon^-2 multiplication. It must not be replaced by just the bare G. The small score(C2) does not remove this connection or prove a small current. On the bare zero-field Omega, the leading reference values are R Omega=600N Omega and sum A_mu*A_mu Omega=60N Omega. The remaining scalar phase can be centered, but a scalar centering does not remove general later quantum fluctuations. This is a scope check, not a new proof of the already known instantaneous-zero identity.

For completeness the exact finite-volume trajectory calculus does not require an uncontrolled infinite series. Every jump in(B1) raises Ntot by two, and its Hamiltonian preserves it. Thus a fixed initial number block has at most a finite number of events. The terminal/no-event and ordered original-event amplitudes form a finite-order continuous-time Dyson isometry. Differentiate this isometry; equivalently take the infinitesimal Kraus identities above and then their bounded finite-volume limit. One may first retain the complete original history, whose fixed-mark append is an isometry, and then apply the specified caps, bins or quantum readouts as CP postprocessing. All original append operations and coherent signs are retained. No extra grade is read out.

Let psi_s be the full baseline trajectory dilation vector, z_s its parameter derivative. Then

 d||z_s||²/ds=<Ndot>_s+2 Re<z_s,i Gamma psi_s>,
 d<psi_s,z_s>/ds=i<Gamma>_s.                            (D4)

Choosing a scalar phase with derivative c(s)=<Gamma>_s centers the second identity. The centered tangent q(s) consequently satisfies

    q'(s)<=<Ndot>_s+2 sqrt(q(s)) sqrt(Var_s Gamma),
    sqrt(q(T))<=sqrt(integral_0^T<Ndot>_s ds)
                       +integral_0^T sqrt(Var_s Gamma)ds. (D5)

The last inequality follows by comparison with [sqrt(integral<Ndot>)+integral sqrt(Var Gamma)]², with a positive regularizer at zero if necessary. Output trace-norm sensitivity is at most2sqrt(q). For mixed inputs purify with an untouched reference; all identities remain valid. The scalar phase may depend on that declared input. This is a source-specific bound, not an unsupported input-uniform diamond estimate.

The expectations in(D4)-(D5) are in the FORWARD BASELINE FAMILY state. For(B1) that state follows D_epsilon. The actual source estimate(C2) is in sigma following L'. Inserting(C2) into(D5) would silently identify those different states. It is NOT done. Even with a valid forward identification, the centered connection variance would still need a bound. A bad upper bound on that variance is not evidence of divergence of the actual response.

A related finite-event-count bound explains the reach of the old first-event mechanism. For a PURE post-phase family L_l(lambda)=exp(i s_l lambda M_l)L_l and dot H=(sum s_l L_l*M_l L_l)/2, ||M_l||<=m, with at most r future events, the first-event bound iterates to

    ||partial_lambda V^T||<=2mr,
    ||partial_lambda Phi^T||_diamond<=4mr, all T.       (D6)

Indeed factor the full trajectory isometry into its first-event isometry followed, on each event branch, by the remaining r-1-event isometry. Differentiate the product. The first term costs2m; the second costs at most the previous bound times a first-event probability amplitude<=1. Induction starts at r=0, where the parameter perturbation vanishes. This allows arbitrary Hamiltonians preserving the number grading and arbitrary reference systems. It does not cover the extra v variation by fiat. From bare Omega the global maximum r=N/2 grows with volume. Therefore(D6) is a finite-volume control, not the sought local response theorem and not a new physical preparation.

## E. A genuinely actual-state retarded identity and its consumer

One can use(C2) without identifying forward states. For any Hermitian joint test O, define the ORIGINAL-mark gradient

    nabla_l O=U_mu(O)L_l-L_l O.

The complete generator derivative satisfies exactly

 dot D(O)=sum_l[dot L_l* nabla_l O+(nabla_l O)*dot L_l]
                                                   -i[Gamma,O]. (E1)

Expansion verifies all gains and both losses. The same formula holds after the original-mark phase gauge. For the ACTUAL sigma and any bounded neutral exact-D backward test O_s, ||O_s||<=1, positive fixed weights w_mu give

 |integral Tr[sigma dot D(O_s)]ds|
 <=2 sqrt( Noise_w(sigma) Energy_(w^-1)(sigma,O) )
             +|integral Tr[sigma(-i[Gamma_hat,O_s])]ds|, (E2)

where Noise_w is precisely(C6) and

 Energy_(w^-1)=integral sum_(mu,r<=0) w_mu^-1
                    Tr[sigma(nabla_(mu,r)O_s)*(nabla_(mu,r)O_s)]ds. (E3)

Thus the first factor on the right is now bounded in the ACTUAL source by
C(T²+epsilon²)sum w_mu. This discharges a specific previously unsupported source-score input. It neither declares(E3) bounded nor absorbs the connected Hamiltonian current. The physical epsilon²T coefficient multiplies the tangent estimate by epsilon² kappa/(2delta), and(B2)'s dark-input/local-error qualifications also remain.

Even the unweighted energy has the exact actual-state identity

 integral<Gamma_D(O_s)>_sigma ds
       =<O_T²>_sigma(T)-<O_0²>_sigma(0)
                         -integral<(L'^*-D)(O_s²)>_sigma ds, (E4)

between history boundaries, with their true boundary terms retained on concatenation. Its last term is not zero because sigma does not evolve under D. A reciprocal spatial weight in(E3) asks for additional information still; an unweighted endpoint bound would not automatically provide it. The current in(E2) likewise retains(D3) and all full-test cross terms. A scalar state phase or conservation of instantaneous mark intensities cannot remove it.

This leaves a precise two-part response consumer: a reciprocal-weighted original noise-gradient estimate at the epsilon scaling needed in(E2), and the actual connected current of Gamma_hat (or a cancellation controlling their sum). The local source score is no longer an extra hypothesis. The response/current conditions themselves are not proved here, nor called weaker than the entire target without qualification. The dark-input error and higher local correctors still need their expanding-test prices.

## F. The exact slow quotient, and why it is not the missing local theorem

There is a limited positive physical-time application available directly from the exact definitions. P0=1_(W=0) is invariant for D_epsilon: all negative grades annihilate it, J_0 preserves it, and H_diag preserves W. The supplied compensation gives

    P0 H2 P0=sum_a(D_(a,infinity)-D_(a,S))P0,             (F1)

an actual diagonal commuting local interaction. On this quotient the remaining neutral Hamiltonian has uniformly bounded local strength at physical order one, as do J_0/epsilon. Conjugating by the large diagonal part in(F1) enlarges a local cone only by one fixed interaction halo, because all its terms commute. The conjugated bounded terms retain their norms uniformly in time, spin and epsilon.

An ordinary connected local Dyson expansion therefore gives, on a sufficiently small fixed physical interval and a fixed local joint test O, a bound

    ||T_0 U_0^*(t)O||<=C_(O,T),                         (F2)

independent of volume and spin. Here U_0 is the EXACT diagnostic quotient and T_0 its complete feedback restriction, including original marks. One explicit justification is to count only connected ordered interactions in the bounded diagonal interaction picture: the number of choices at the next step is bounded by a constant times the current support size, giving a factorial times a polynomial; the time-ordered factorial cancels and leaves a convergent geometric series for a fixed positive small T. One additional local T insertion changes only that polynomial and constant. This is the same already supplied local-interaction method, used on the exact quotient, not a new uniform theorem about the full fast carrier.

T also preserves this state block: d P0=0, A has grade0, and R is neutral. Therefore compression of any full retarded test to P0 is exactly U_0^*(t)(P0 O P0); incoming observable gains from other sectors do not change this compression identity. From(F2),

    |epsilon² integral Tr[sigma(s)P0 T(O_s)P0]ds|
                                                     <=C_(O,T) epsilon². (F3)

No effective-state expectation replaces sigma in(F3). This is an application to one GLOBAL invariant diagnostic block. A small local hole density does not imply a large global P0 weight at growing volume. It gives no local-hole-free buffer theorem or influence bound against outside holes. Thus(F3) is a bounded known-method consumer, not the new solution to unsaturated/multiple-hole physical transport. That obligation is deliberately left separate from the new tangent and source-score lemmas.

## G. Evidence, prior boundaries and terminal status

The genuinely new high-fanout candidates are the bounded local corner factorization(A4)-(A6), its complete exact-D tangent(B1)-(B2), and the actual source-score theorem(C2). They have full analytic derivations from the bound current sources. Their mechanism is different from finite-k absorption, held-hole electric residence, global count tilts and the prior first-event theorem. No new computation or numerical extrapolation was used. The general dilation algebra and source-input estimates are proved here; the old scalar-phase obstruction and saturated predual resonance are credited earlier results rather than rerun as discoveries.

Four failures are retained explicitly: jump-rate invariance does not make the complete tangent a martingale; finite event count costs volume from Omega; a source score in sigma cannot be inserted into a D-forward channel formula; and the global W0 quotient is not a local buffer assertion. The exact full response/current consumer in(E2)-(E4) remains. No arbitrary state or separately prepared gas is offered as a counterexample to the actual law. No formal review, audit, source landing, primitive adoption or whole-limit conclusion is made.
