# Original amplitude, gain and bounded-history balances

Current supporting proof owned by the canonical microscopic-output note. All notation, law, preparation, original mark conventions and uniformity quantifiers are fixed there. This is part of the same bounded theorem, not a separately adopted premise. Constants denoted C may change between displays and depend only on the fixed supports, couplings, horizon and circuit order indicated. Equation prefixes distinguish the components.

## Cumulative original mark means

## Statement

Keep the canonical note's supplied microscopic law, bare Omega, Gauss sector, actual integer spins and epsilon² S(S+1)=delta/K on all even safe tori. For a center a and an ORIGINAL mark mu at a, define the actual local source word on the full carrier

    Bhat_mu = j_mu F_a.                               (M1)

On the W0 subspace this is exactly the supplied leading formation map, with its original normalization and label. Outside that subspace(M1) is merely the displayed physical operator word; no new dynamics using it is evolved. For coherent edge marks, j_mu is the full unnormalized coherent sum, not its separately measured signs.

Let N_(a,mu)([0,t]) count that original mark in the actual microscopic process. There are epsilon0,C<infinity independent of S,L,a such that, for each fixed T,

    sup_(0<=t<=T) | E_micro N_(a,mu)([0,t])
       -kappa integral_0^t Tr[rho_micro(s) Bhat_mu*Bhat_mu]ds |
                    <= C epsilon²(1+T)².             (M2)

The same microscopic rho appears on the right. This is NOT comparison with rho_effective. Constants may depend on the fixed law and mark family; there are only finitely many mark types at each center. Finite monitored regions and deterministic bounded-variation time weights inherit the explicit linear region/variation price stated below. All later births are included in the actual ensemble. No bound on global B count, field moments or a fast loss gap is required for this bounded mean statement.

## 1. Exact original count and complete grade algebra

Use the exact finite-depth order-six circuit Y from the normal-form and moments appendix and sigma=Y rho_micro Y*. Keep the actual transformed original jumps J_mu=Y j_mu Y*. For a fixed translation-covariant original mark type mu, let the sum run over its translated centers and define

    Lambda_mu=kappa epsilon^-2 sum_a J_(a,mu)*J_(a,mu).

The exact counting-intensity identity is

    sum_a E N_(a,mu)([0,t])=integral_0^t<Lambda_mu>_sigma ds.

Onsite averaging gives the exact diagnostic decomposition

    P_W Lambda_mu=kappa epsilon^-2 sum_(a,r)
                                     J_(a,mu,r)*J_(a,mu,r).

This is a matrix identity inside the proof, not a measured splitting of the original jump. In particular all same-mark grade cross terms are still in Lambda_mu-P_W Lambda_mu.

The first circuit derivative is S1=-F+F*, so

    J_mu=j_mu+epsilon j1_mu+O_local(epsilon²),
    j1_mu=[-F+F*,j_mu],
    A_mu=(j1_mu)_(grade0)=j_mu F_a-F_a j_mu.           (M3)

For c!=a, [F_c,j_mu]=0: on a shared B factor both operators create a record and their two products vanish; on different B factors they commute. Their electric factors belong to different oriented links. Thus(M3) uses the complete F, not a dropped neighboring term.

The grade-zero component has the sharper Taylor expansion

    J_(mu,0)=epsilon A_mu+O_local(epsilon³).          (M4)

To see the absent quadratic coefficient without assuming an extra symmetry, each first-order gate coefficient has grades plus/minus1. Every second-order circuit coefficient has only even grades: it is built from the grade-zero supplied compensation, products/commutators of the first-order coefficients, and the order-two homological inverse, which preserves grades. Multiplication or commutation with j of grade minus-one therefore makes the second-order jump coefficient odd-grade. It cannot have grade0. All Taylor bounds are uniform in spin, volume and local dimension by the proved finite circuit construction.

Consequently

    kappa epsilon^-2 sum_a J_(a,mu,0)*J_(a,mu,0)
        =kappa sum_a A_(a,mu)*A_(a,mu)+O_local(epsilon²).
                                                               (M5)

## 2. The other grades and their original cross terms

The proved exact defect estimate(D10) gives, for the ACTUAL sigma from Y Omega,

    integral_0^t <D_minus>_sigma ds
                    <=C epsilon² n(1+t),
    D_minus=kappa epsilon^-2 sum_(all marks,r<0)
                            (-r)J_(mu,r)*J_(mu,r).

The integrated negative-grade contribution to P_W Lambda_mu is bounded by this because every -r>=1 and the omitted mark types are positive summands. Positive-grade amplitudes start at epsilon², so their integrated contribution is <=C epsilon² n t. These bounds require neither a gap nor a grade-resolved observed process.

For completeness handle the ENTIRE remaining same-mark cross potential

    R_mu=(1-P_W)Lambda_mu.

It is a Hermitian local interaction sum of strength O(epsilon^-1): the bare loss has grade0 and the first mixed coefficient has grades plus/minus1. Write the exact generator as L'* =i delta epsilon^-4[W,.]+B_epsilon, with B_epsilon=epsilon^-2 B2+O_local(epsilon^-1) and B2 grade-preserving. Define

    K1=(i epsilon^4/delta)I_W R_mu,
    K2=(i epsilon^4/delta)I_W(1-P_W)B_epsilon K1.

Then K1,K2 have local strengths O(epsilon³),O(epsilon^5), and EXACTLY

    L'*(K1+K2)=-R_mu+P_W B_epsilon K1+B_epsilon K2.

The apparent order-epsilon term vanishes since P_W B2 K1=0. The residual has local strength O(epsilon²). Summing bounded-incidence terms, rather than multiplying extensive norms, gives

    |integral_0^t<R_mu>_sigma ds|
                  <=C n(epsilon³+t epsilon²).        (M6)

All gains and losses remain in B_epsilon acting on K1,K2; this is not an estimate for the cross loss evolved by itself. Arbitrary same-mark interference is included in R_mu, including its bounded-order higher coefficients.

Combine(M5)-(M6) and the nonnegative grade estimates:

    | n^-1 sum_a E N_(a,mu)([0,t])
       -(kappa/n)integral_0^t sum_a<A_(a,mu)*A_(a,mu)>_sigma ds |
                  <=C epsilon²(1+t).                (M7)

## 3. Return to the actual physical state and source word

For any bounded grade-zero local O with uniformly bounded support and norm, local Taylor expansion gives

    Y* O Y=O+epsilon[O,S1]+epsilon² R_O,
    ||R_O||<=C_O.

The first commutator has only grades plus/minus1. Let P_X project onto all A factors occupied in its fixed support cone. Then P_X[O,S1]P_X=0. In the actual PHYSICAL state the proved estimate(D1), translation invariance and a union bound give

    Tr[rho_micro(t)(1-P_X)]<=C_X epsilon²(1+t).

For any bounded A with P_X A P_X=0, Cauchy--Schwarz on its P_X/Q_X blocks gives

    |Tr[rho A]|<=||A||(2 sqrt(Tr[rho Q_X])+Tr[rho Q_X])
                <=3||A|| sqrt(Tr[rho Q_X]).

It follows that, for 0<=t<=T,

    |Tr[sigma(t)O]-Tr[rho_micro(t)O]|
                    <=C_O epsilon²(1+sqrt(1+t)),     (M8)

The last inequality uses Tr[rho Q_X]<=1 as well as its hole bound, so the constant in(M8) need not grow with T. No unweighted assumption about the rotated initial state is made; sigma is always the exact Y rho Y*.

Apply this to O=A_mu*A_mu. The local A occupancy blocks in(M3) are orthogonal:

    Bhat_mu=j_mu F_a=n_a Bhat_mu n_a,
    D_mu=F_a j_mu=w_a D_mu w_a,
    A_mu=Bhat_mu-D_mu,
    A_mu*A_mu=Bhat_mu*Bhat_mu+D_mu*D_mu.              (M9)

Thus the mixed terms vanish as an operator identity by occupancy, not by dephasing the original mark. Moreover D_mu*D_mu<=||F_a||²||j_mu||²w_a. The proved physical hole bound makes its expectation O(epsilon²(1+t)), uniformly in S and L. Equations(M8)-(M9), integrated in(M7), therefore give the same microscopic-state Bhat expression with error <=C epsilon²(1+T)².

Finally both physical quantities are translation covariant: the actual original count of mark mu and Bhat_(a,mu)*Bhat_(a,mu) translated across A centers. The physical generator and Omega are translation invariant. Thus their averages over n equal the corresponding quantity at EACH a, even though the normal-form coloring need not be translation invariant. This proves(M2). No claim that each individual colored negative-grade rate is translation invariant was used.

## 4. Original time-weighted mean output and exact limits

Let nu_(a,mu) be the expected original counting measure on[0,T], and let b_(a,mu)(s)=kappa Tr[rho_micro(s)Bhat_mu*Bhat_mu]. The cumulative signed difference has the uniform bound(M2). Integration by parts therefore gives, for a deterministic bounded-variation time weight f,

    |integral f dnu_(a,mu)-integral f(s)b_(a,mu)(s)ds|
      <=C epsilon²(1+T)² (|f(T)|+Var f).             (M10)

There is no atom at time0; a convention including f(0) can use the larger supnorm+variation bound. Summing finitely many center/mark weights adds their explicit variation factors. Original labels are never merged or refined. This controls cumulative means and fixed bin means, not total variation of the full timestamp law against arbitrarily rapidly oscillating tests.

Crucially, b(s) is NOT asserted to be the conditional intensity of the microscopic history, nor is rho_micro replaced by an effective state. The theorem alone gives no quantum post-mark map approximation, higher count correlations, field moments or source-cluster tail. It does isolate the actual original leading source word as the unconditional mean consumer on a common positive time interval, uniformly in volume, while respecting bare preparation and shared-output coherence. The supplied carrier and original energy law are unchanged.

## Local amplitude and original quantum gain

## 1. Statements and exact norms

Fix one original mark type mu and one center a. Let rho(t) be the ACTUAL unmonitored microscopic ensemble, sigma(t)=Y rho(t)Y* its exact normal-form coordinates, and

    Bhat_(a,mu)=j_(a,mu) F_a,
    L_(a,mu)=sqrt(kappa) epsilon^-1 j_(a,mu),
    B_(a,mu)=sqrt(kappa) Bhat_(a,mu).

For every fixed T there are finite constants independent of safe torus volume, spin and center, with the declared coupled scaling allowed, such that

 integral_0^T ||(epsilon^-1 j_(a,mu)-Bhat_(a,mu))
                                      rho(t)^(1/2)||_2² dt
                                      <=C epsilon²(1+T)².       (G1)

This is an integral of a NONNEGATIVE squared amplitude difference, not just a signed mean-count identity. The Hilbert-Schmidt norm is on the actual finite microscopic carrier. The original coherent edge mark uses its entire unnormalized j_++j_- and the corresponding entire Bhat; its signs are not separately measured.

Let eta(t) be ANY positive trace-one extension of the same actual rho(t), for example its exact original capped/binned history with arbitrary reference factors. The extension may vary with t; it need only have marginal rho(t). Then

 integral_0^T || L_mu eta(t)L_mu* - B_mu eta(t)B_mu* ||_1 dt
                                      <=C epsilon(1+T)².       (G2)

Operators in(G2) act as identity on the extension. The same bound holds after the original history append map or any fixed trace-nonincreasing completely positive output postprocessing. Summing a fixed finite set of original marks/centers costs its cardinality. Thus(G2) compares the actual original quantum GAIN current with the Bhat gain evaluated in the SAME joint state and with the SAME output label. It does not compare two independently evolved laws. This unnormalized current can have total trace equal to a mean event count, not one.

A second consequence is a local rotated dark-occupation estimate. Let

    v_a=sum_(b~a)(1-n_b)

be the number of empty neighboring B factors, an operator diagonal in the physical occupation basis. Then, under epsilon²S(S+1)=delta/K,

 epsilon^-2 integral_0^T Tr[sigma(t) w_a v_a]dt
                                  <=C epsilon²(S+1)(1+T)
                                  <=C' epsilon(1+T).           (G3)

This refers to the exact ROTATED diagnostic hole sector. It is not the physical birth count, which is typically order one. It does not control fields, dark holding populations, or the inverse lifetime of a dark configuration.

## 2. First obtain a global squared budget in exact rotated coordinates

The proved D10 is

 integral_0^T <D_minus>_sigma dt <=C epsilon² n(1+T),
 D_minus=kappa epsilon^-2 sum_(all original marks,r<0)
                                     (-r)J_mu,r*J_mu,r,
 J_mu=Y j_mu Y*,  n=|A|.

Every term is nonnegative. Selecting grade -1 and the chosen translated mark type gives

 integral_0^T sum_a Tr[sigma J_(a,mu,-1)*J_(a,mu,-1)]dt
                                      <=C epsilon^4 n(1+T).    (G4)

Fixed positive kappa is absorbed in C. The first transformed-jump coefficient

    j1_mu=[S1,j_mu],   S1=-F+F*,

has only grades0,-2. Hence

    ||J_(a,mu,-1)-j_(a,mu)||<=C epsilon²,

uniformly in spin and volume, by the exact bounded-cone circuit expansion and its grade projection. The vector inequality ||(A+B)psi||²<=2||Apsi||²+2||Bpsi||², applied to the density square root, therefore gives

 integral_0^T sum_a ||j_(a,mu) sigma(t)^(1/2)||_2² dt
                                      <=C epsilon^4 n(1+T).    (G5)

This is a global estimate so far. It is not divided by n using a nonexistent translation symmetry of sigma or of the colored grade components.

## 3. Translation-covariant physical truncation localizes the budget

The EXACT physical pullback of the bare rotated j is

    K_(a,mu)=Y* j_(a,mu)Y
            =ell_(a,mu)+epsilon² R_(a,mu),
    ell_(a,mu)=j_(a,mu)-epsilon j1_(a,mu),
    ||R_(a,mu)||<=C.                                         (G6)

The remainder has a bounded cone, but is allowed to depend on the coloring. Only the local conjugation expansion is used; no global norm estimate for Y-I occurs. The first derivative S1 and thus ell are translation covariant under the physical torus translations, independently of that coloring.

Unitary invariance identifies ||K_mu rho^(1/2)||_2=||j_mu sigma^(1/2)||_2. Applying the same squared inequality in(G6), summing centers and using(G5), yields

 integral_0^T sum_a ||ell_(a,mu) rho(t)^(1/2)||_2² dt
                                      <=C epsilon^4 n(1+T).    (G7)

Now both rho and ell are PHYSICAL and translation covariant. Divide(G7) by n to obtain, for EACH center,

 integral_0^T ||ell_(a,mu)rho(t)^(1/2)||_2² dt
                                      <=C epsilon^4(1+T).      (G8)

This localization is the essential step. Returning once more through(G6) also gives the genuinely local rotated estimate

 integral_0^T ||j_(a,mu)sigma(t)^(1/2)||_2² dt
                                      <=C epsilon^4(1+T),      (G9)

without asserting that sigma is translation invariant. The argument works for every one of the finitely many original mark types and all centers, with a common enlarged constant.

## 4. The full first coefficient differs from Bhat only on input holes

Keep the COMPLETE first derivative, not just its grade-zero part:

    j1_mu=j_mu F_a-F_a j_mu+[F*,j_mu]
           =Bhat_mu+Rhole_mu,
    Rhole_mu=-F_a j_mu+[F*,j_mu].                             (G10)

For c!=a, [F_c,j_mu]=0 by the actual hard-core shared-B creation rule, with disjoint oriented link factors; this is why the outward part reduces to F_a. The inward commutator [F*,j_mu] has grade -2 and bounded finite support: only overlapping stars contribute. A local grade -2 operator annihilates the all-A-occupied input on its support, since it cannot reduce a nonnegative local hole number below zero. The other term F_a j_mu has the right input vacancy factor w_a. Thus, on a fixed neighborhood U of a,

    Rhole_mu P_U=0,   P_U=prod_(c in U cap A)n_c,
    Rhole_mu*Rhole_mu <=C (I-P_U).                            (G11)

This does not require a two-hole probability estimate; the proved one-hole union bound suffices. From the actual PHYSICAL D1,

    ||Rhole_mu rho(t)^(1/2)||_2² <=C epsilon²(1+t).            (G12)

Since j_mu-epsilon Bhat_mu=ell_mu+epsilon Rhole_mu, equations(G8),(G12), integrated and combined by the squared inequality, give

 integral_0^T ||(j_mu-epsilon Bhat_mu)rho(t)^(1/2)||_2²dt
                                      <=C epsilon^4(1+T)².

Dividing by epsilon² proves(G1). The estimate includes the initial layer rather than excluding it: at Omega, j_mu vanishes while Bhat_mu does not, so no pointwise-in-time amplitude assertion is possible. The integrated nonnegative budget is what remains small.

## 5. Original quantum gain, labels and extensions

For any extension eta with physical marginal rho,

 ||(L_mu-B_mu)eta^(1/2)||_2²
               =Tr[rho(L_mu-B_mu)*(L_mu-B_mu)].

Thus(G1) gives the same integral bound for EVERY such extension, without a conditional or postselected hole assumption. Put E_mu=L_mu-B_mu. The exact difference factors as

    L_mu eta L_mu* - B_mu eta B_mu*
                   =E_mu eta L_mu*+B_mu eta E_mu*.

Hilbert-Schmidt/trace-norm Holder therefore bounds its trace norm by

    ||E_mu eta^(1/2)||_2
       (||L_mu eta^(1/2)||_2+||B_mu eta^(1/2)||_2).

The integral of the first factor squared is <=C epsilon²(1+T)². The actual original count bound D3 controls integral ||L_mu eta^(1/2)||_2² by C(T+T²); uniform ||Bhat_mu|| bounds the corresponding B integral by CT. Cauchy--Schwarz in time proves(G2), with the stated larger polynomial envelope. For a finite mark set, use Cauchy--Schwarz on mark times time, or sum the per-mark bound. The direct sum over ORIGINAL mark labels has trace norm equal to that sum.

An actual deterministic classical append is a completely positive trace-preserving map on the joint gain output. Such maps contract the trace norm of Hermitian differences; any declared trace-nonincreasing CP readout has the same property. The original gains therefore retain their labels, all same-mark sign coherence, and their conditional quantum payload inside the compared joint current. No separate process using Bhat is silently substituted. This is an averaged integrated gain-current bound; it does not assert equality of finite-epsilon conditional hazards or a convergence theorem for an entire timestamp law.

## 6. Local darkness with exact spin-boundary loss

Sum(G9) over the ORIGINAL marks at a. For either instrument their total bare loss is exactly

    sum_(mu at a)j_mu*j_mu
      =2 sum_(b~a)w_a(1-n_b)
                       [1-E_(ab)²/(S(S+1))].                (G13)

For the resolved instrument this is the sum of the two normalized sign-shift squared amplitudes 1-E(E+1)/Cspin and 1-E(E-1)/Cspin. For the coherent edge instrument the same total follows because the two final A charges are orthogonal; the signs remain one observed label. Orientation reversal changes which sign has which shift but not this sum. At a spin boundary one of the paths is blocked with its actual zero amplitude, and the other contributes 2/(S+1). Consequently

    sum_mu j_mu*j_mu >= [2/(S+1)] w_a v_a.

Combining with(G9) proves(G3). The slowing at high field is paid explicitly by S+1 rather than replaced by a rotor constant. This shows that the rescaled integrated rotated-hole occupation outside the locally full-B dark set vanishes even under the coupled spin scaling. It gives no such estimate inside that dark set and no static-cluster or all-state absorption theorem.

## What remains unresolved

Gain matching is stronger than the earlier signed mean identity in output topology but has the weaker O(epsilon) error order. It is compatible with the separately proved O(epsilon²) cumulative mean result. It does NOT control the complete anticommutator loss on arbitrary tests: multiplying a state-weighted amplitude error by an operator with norm O(epsilon^-1) can lose the smallness. Nor does it remove the fast Hamiltonian or identify its effective fourth-order response. A no-event/whole-process comparison therefore still needs the complete coherent loss/Hamiltonian cancellation or another valid passive-response argument.

The proof gives no quadratic-field-weighted version of(G1)-(G2). Inserting an S² operator-norm price again loses smallness, and unconditional first-field tightness cannot supply a hole-weighted tail. Persistent dark occupation and its field/source weighting remain the hard residuals. No source-selected foundation, altered energy law, formal review, numerical execution or new apparatus claim is made.

## Bounded original-history balance

## 1. Exact output and target identity

Fix a finite set F of monitored A centers, finitely many time-bin intervals on[0,T], and a count cap M. The classical register Z records the original labels with their bin tags and within-history order. On overflow it retains an absorbing flag, while the system continues to evolve. Either the original resolved instrument or the original unnormalized coherent-edge instrument is used separately. Write eta(t) for the EXACT joint microscopic quantum/register state, and g for any real bounded function of the register, including its overflow outcome. Let T_(mu,t)g(z)=g(append_(mu,bin(t))(z)) be the true register update for a monitored original mark mu. At overflow this is g(overflow). All update maps have norm one on the classical supnorm algebra.

For mu at a define the same full-carrier physical source word as in the proved mean theorem,

    Bhat_mu=j_mu F_a,
    Delta_(mu,t)g=T_(mu,t)g-g.

No dynamics using Bhat is evolved. Let b be the number of fixed bin boundaries in the interior of[0,T]. There are C_F,epsilon0 independent of spin, safe torus volume, cap M and g such that

 sup_(0<=t<=T) | E g(Z_t)-g(empty)
       -kappa integral_0^t sum_(mu centered in F)
          Tr[eta(s)(Bhat_mu*Bhat_mu tensor Delta_(mu,s)g)]ds |
 <= C_F ||g||_infinity
          [epsilon²(1+T)²+epsilon³(1+b)].                       (R1)

Constants depend on the fixed couplings, finite pattern geometry and original mark family; the finite-color construction is the same proved one. Coupled spin/epsilon scaling is allowed, but no field estimate is needed. All later births and every original same-mark coherent contribution are present. The formula concerns bounded functions of the entire recorded capped word, rather than just its count or final bin.

Equivalently, for each mu let the positive register measure

    nu_mu(s;z)=Tr_system[eta_z(s) Bhat_mu*Bhat_mu].

The classical register marginal tau obeys the approximate integrated vector identity

 ||tau(t)-tau(0)-kappa integral_0^t
           sum_mu (append_(mu,s)*-I)nu_mu(s)ds||_(ell1)
 <= C_F [epsilon²(1+T)²+epsilon³(1+b)].                       (R2)

Trace/supnorm duality in this FINITE classical space gives(R2) from the uniform bound(R1). This is a same-joint-state identity. In general nu_mu is correlated with the quantum state and the recorded past, so(R2) is not a closed classical generator and does not identify a microscopic conditional hazard. It does not replace eta by an effective state or assert a quantum post-mark map comparison.

## 2. Copying every translated monitored pattern for the proof

The defect estimate for negative-grade loss is global, and the normal-form coloring need not preserve translations. A single monitored register cannot justify dividing a colored local loss estimate by volume. We avoid that mistake as follows.

On one finite torus attach, as mathematical bookkeeping, a register Z_x for EVERY A-sublattice translation x of the fixed pattern F. Each reads the SAME physical original event history restricted to x+F, with labels expressed in that translated pattern's coordinates. These registers have their exact joint correlations; they are not independent samples or new physical apparatus. The full original finite-volume marked process supplies this joint classical extension directly. It leaves the system marginal unchanged. A physical mark at a updates exactly those pattern registers for which a lies in x+F, at most |F| of them. Other registers are left untouched. The deterministic simultaneous update has a complete Kraus column with sum V_z*V_z=I. Consequently the physical grade-loss sum in this enlarged classical extension is still D_minus tensor I, with no multiplicity in the actual jump law.

Use the extensive test

    G=sum_x g(Z_x),  n=|A|.

The generator is linear, so each term retains the one-register anchor x+F. A finite number of generator actions, grade projections or homological inverses enlarges only its quantum neighborhood and bounded incidence. The support/mark counts depend on F and the fixed circuit order, not n or M. Complete gain/loss cancellation removes unmonitored terms disjoint from that anchor; terms updating its register must all be kept, including those outside its current quantum support. Cross-map norms are bounded by the Kraus-column/supnorm contraction, independently of the potentially huge copied-register dimension.

Only AFTER returning observables to physical coordinates will translation covariance be used. The physical law, bare Omega and blank copied-register preparation are translation covariant, with translations permuting the register indices. This is enough to divide both physical sides by n. No covariance of Y, sigma or its grade-resolved rates is assumed.

## 3. Exact original generator and diagnostic grades

Extend the proved circuit Y by identity on every register. Put sigma_joint=Y eta_all Y* and J_mu=Y j_mu Y*. At any time within a bin the EXACT original registered generator acts on G as

    Lambda_G=L'^*G
       =kappa epsilon^-2 sum_(physical mu) J_mu*J_mu tensor d_mu,
    d_mu=sum_(x: center(mu) in x+F) Delta_(mu,t)g(Z_x).          (R3)

The tensor notation means the commuting quantum coefficient and displayed classical function. In particular ||d_mu||<=2|F| ||g||. Hamiltonian terms vanish on G. All same-mark coherence is still inside J_mu*J_mu. Grade averaging is a diagnostic matrix identity,

    P_W Lambda_G=kappa epsilon^-2 sum_(mu,r)
                                   J_mu,r*J_mu,r tensor d_mu.  (R4)

It is not a recorded grade split.

For r<0, positivity and |d_mu|<=2|F| ||g|| give

 | integral_0^t <negative part of(R4)> ds |
 <=2|F| ||g|| integral_0^t <D_minus> ds
 <=C_F ||g|| epsilon² n(1+t).                                (R5)

The system marginal of sigma_joint is exactly the original rotated marginal, so the proved D10 applies. There is no conditional rare-hole or conditional loss assumption. Each positive-grade J_mu,r starts at epsilon² in the uniform local expansion; their contribution in(R4) is bounded by C_F ||g|| epsilon² n t.

The complete grade-zero coefficient satisfies, as proved in the mean theorem,

    J_mu,0=epsilon A_mu+O_local(epsilon³),
    A_mu=j_mu F_a-F_a j_mu.                                  (R6)

The absent quadratic grade-zero coefficient follows from W-grade parity of the first two circuit orders. Neighboring F_c with c!=a commute with j_mu: if they share a B factor both products have two record creations there and vanish, while otherwise their local factors commute. The grade0 first coefficient is therefore the complete displayed word. Coherent signs remain inside j_mu. Uniform column norms give

 kappa epsilon^-2 sum_mu J_mu,0*J_mu,0 tensor d_mu
       = kappa sum_mu A_mu*A_mu tensor d_mu
                                           +O_local,F(epsilon² ||g||).

Its extensive norm error is <=C_F n epsilon²||g||.

## 4. Entire off-grade potential with every register update

Let R_G=(1-P_W)Lambda_G. It is an exact Hermitian interaction sum of local strength O_F(epsilon^-1||g||). The bare potential j_mu*j_mu has grade0, and the leading mixed jump coefficient has grades +/-1. Higher same-mark cross terms are retained in R_G. The exact registered adjoint generator is

    L'^*=i delta epsilon^-4[W,.]+B_epsilon,
    B_epsilon=epsilon^-2 B2+O_local,F(epsilon^-1),

and B2 preserves grades because register updates carry no W grade. Define within each fixed bin

    K1=(i epsilon^4/delta) I_W R_G,
    K2=(i epsilon^4/delta) I_W(1-P_W)B_epsilon K1.

Their local strengths are O_F(epsilon³||g||) and O_F(epsilon^5||g||). The exact identity, with complete registered gains AND losses in every action, is

    L'^*(K1+K2)=-R_G+P_W B_epsilon K1+B_epsilon K2.

The apparent epsilon term vanishes by P_W B2 K1=0. The residual has local strength O_F(epsilon²||g||). Summing bounded incidence gives the signed-integral bound

 |integral_0^t <R_G> ds|
 <=C_F n ||g|| [epsilon³(1+b)+t epsilon²].                    (R7)

To check the b factor, integrate separately on the fixed bin intervals. K1,K2 may change when the append label changes, so their endpoint terms have at most b internal jumps plus the two exterior endpoints, each bounded by C_F n epsilon³||g||. The joint registered state itself is continuous there. No derivative of a cumulative mean estimate is being assumed. This is not a bound on the integral of the absolute off-grade activity.

## 5. Return to the physical joint state and original Bhat word

Each summand of the neutral source is a bounded local grade-zero quantum coefficient times a bounded function of one copied register. The circuit acts only on the quantum factor. For such O, its first conjugation correction has grades +/-1 and norm <=C_F||g||; its compression to the fully occupied local A neighborhood vanishes. The actual joint state's hole probability in that neighborhood is the system marginal's proved O(epsilon²(1+t)). Cauchy--Schwarz on the occupied/hole blocks, followed by the explicit epsilon in the circuit expansion, gives

    |<O>_sigma_joint-<O>_eta_all|
                   <=C_F ||g|| epsilon²(1+sqrt(1+t)).          (R8)

This applies to A_mu*A_mu tensor each Delta g. It uses neither a bound on a state conditioned on its history nor colored translation symmetry. Summing the n|F| finite-incidence terms preserves the stated extensive order.

As exact physical occupancy blocks,

    Bhat_mu=j_mu F_a=n_a Bhat_mu n_a,
    D_mu=F_a j_mu=w_a D_mu w_a,
    A_mu=Bhat_mu-D_mu,
    A_mu*A_mu=Bhat_mu*Bhat_mu+D_mu*D_mu.                       (R9)

These identities still hold after multiplying by any classical Delta g. Mixed terms vanish algebraically by A occupancy, not by observing an extra label or dephasing signs. Since D_mu*D_mu<=C w_a, its signed register-weighted expectation has magnitude <=C||g|| times the physical local-hole probability. Thus the integrated difference between the A*A and Bhat*Bhat expressions is <=C_F n||g|| epsilon²(1+T)², including(R8).

Combine the exact Dynkin identity for G with(R4)-(R9). Both remaining sides are now PHYSICAL observables of the copied-register process. Translation covariance of that exact process makes each translated pattern have the same expectation and same source-integral value. Divide by n and discard all registers except the chosen one; their marginal is precisely eta in section1. This proves(R1), uniformly over every bounded g, and hence(R2).

## 6. Limits and consumer

The result identifies a bounded integrated register-generator expression evaluated in the SAME joint microscopic state. It controls history-dependent bounded tests, whereas the earlier mean theorem controlled only unconditional cumulative counts and deterministic time weights. The new proof does not assert that kappa Bhat*Bhat is the true finite-epsilon conditional hazard: the actual source rates vanish initially at Omega while the leading Bhat rates do not. Nor is(R1) a pointwise time derivative or an uncapped unbounded-count identity. Bin-switch errors and all initial-layer corrections are explicit.

The local trajectory and rotor-limit appendix supplies a subsequential local-state limit and the required bounded-word passage. This lemma alone does not supply that convergence, identify the quantum dynamics, or justify a closed classical Markov law. Continuous-timestamp whole-process convergence, positive-time source clustering, quadratic hole-weighted moment and changing-source coherent fast feedback remain separate. The full microscopic Hamiltonian and original energy ledger have not been replaced. The finite controls do not replace this analytic proof.
