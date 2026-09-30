# Local original gain matching from the actual negative-grade budget

Author analytic discovery lemma, awaiting independent reconstruction. This proof uses the checked DEFECT(D1)-(D10), the original source algebra in MEAN_MARK_BALANCE, and the same finite local circuit. It does not use ORIGINAL_REGISTER_BALANCE, time compactness, a field moment, the weighted source-component lemma, a fast gap or a source-cluster hypothesis. The actual supplied compensated spin law, physical Gauss sector, bare Omega, all later births and both ORIGINAL mark families separately are unchanged. No grade is observed or substituted for a mark.

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

The checked D10 is

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

This does not require a two-hole probability estimate; the checked one-hole union bound suffices. From the actual PHYSICAL D1,

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

Gain matching is stronger than the earlier signed mean identity in output topology but has the weaker O(epsilon) error order. It is compatible with the separately checked O(epsilon²) cumulative mean result. It does NOT control the complete anticommutator loss: multiplying a state-weighted amplitude error by an operator with norm O(epsilon^-1) can lose the smallness. Nor does it remove the fast Hamiltonian or identify its effective fourth-order response. A no-event/whole-process comparison therefore still needs the complete coherent loss/Hamiltonian cancellation or another valid passive-response argument.

The proof gives no quadratic-field-weighted version of(G1)-(G2). Inserting an S² operator-norm price again loses smallness, and unconditional first-field tightness cannot supply a hole-weighted tail. Persistent dark occupation and its field/source weighting remain the hard residuals. No source-selected foundation, altered energy law, formal review, numerical execution or new apparatus claim is made.
