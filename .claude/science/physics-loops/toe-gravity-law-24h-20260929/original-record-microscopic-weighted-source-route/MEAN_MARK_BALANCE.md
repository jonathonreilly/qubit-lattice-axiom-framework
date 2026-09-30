# Uniform microscopic mean balance for each original mark

Author analytic discovery lemma; not independently checked. This common-positive-time statement uses the already checked local normal form, physical rare-hole estimate and coherence-correction mechanism. It does NOT use the new weighted initial-layer theorem as a premise. It concerns unconditional cumulative means of the ACTUAL original marks, not conditional hazards, a substituted birth process, quantum post-mark output convergence, or(W1).

## Statement

Keep CONTRACT's supplied microscopic law, bare Omega, Gauss sector, actual integer spins and epsilon² S(S+1)=delta/K on all even safe tori. For a center a and an ORIGINAL mark mu at a, define the actual local source word on the full carrier

    Bhat_mu = j_mu F_a.                               (M1)

On the W0 subspace this is exactly the supplied leading formation map, with its original normalization and label. Outside that subspace(M1) is merely the displayed physical operator word; no new dynamics using it is evolved. For coherent edge marks, j_mu is the full unnormalized coherent sum, not its separately measured signs.

Let N_(a,mu)([0,t]) count that original mark in the actual microscopic process. There are epsilon0,C<infinity independent of S,L,a such that, for each fixed T,

    sup_(0<=t<=T) | E_micro N_(a,mu)([0,t])
       -kappa integral_0^t Tr[rho_micro(s) Bhat_mu*Bhat_mu]ds |
                    <= C epsilon²(1+T)².             (M2)

The same microscopic rho appears on the right. This is NOT comparison with rho_effective. Constants may depend on the fixed law and mark family; there are only finitely many mark types at each center. Finite monitored regions and deterministic bounded-variation time weights inherit the explicit linear region/variation price stated below. All later births are included in the actual ensemble. No bound on global B count, field moments or a fast loss gap is required for this bounded mean statement.

## 1. Exact original count and complete grade algebra

Use the exact finite-depth order-six circuit Y from the checked DEFECT_LEMMA and sigma=Y rho_micro Y*. Keep the actual transformed original jumps J_mu=Y j_mu Y*. For a fixed translation-covariant original mark type mu, let the sum run over its translated centers and define

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

To see the absent quadratic coefficient without assuming an extra symmetry, each first-order gate coefficient has grades plus/minus1. Every second-order circuit coefficient has only even grades: it is built from the grade-zero supplied compensation, products/commutators of the first-order coefficients, and the order-two homological inverse, which preserves grades. Multiplication or commutation with j of grade minus-one therefore makes the second-order jump coefficient odd-grade. It cannot have grade0. All Taylor bounds are uniform in spin, volume and local dimension by the checked finite circuit construction.

Consequently

    kappa epsilon^-2 sum_a J_(a,mu,0)*J_(a,mu,0)
        =kappa sum_a A_(a,mu)*A_(a,mu)+O_local(epsilon²).
                                                               (M5)

## 2. The other grades and their original cross terms

The checked exact defect estimate(D10) gives, for the ACTUAL sigma from Y Omega,

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

The first commutator has only grades plus/minus1. Let P_X project onto all A factors occupied in its fixed support cone. Then P_X[O,S1]P_X=0. In the actual PHYSICAL state the checked estimate(D1), translation invariance and a union bound give

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

Thus the mixed terms vanish as an operator identity by occupancy, not by dephasing the original mark. Moreover D_mu*D_mu<=||F_a||²||j_mu||²w_a. The checked physical hole bound makes its expectation O(epsilon²(1+t)), uniformly in S and L. Equations(M8)-(M9), integrated in(M7), therefore give the same microscopic-state Bhat expression with error <=C epsilon²(1+T)².

Finally both physical quantities are translation covariant: the actual original count of mark mu and Bhat_(a,mu)*Bhat_(a,mu) translated across A centers. The physical generator and Omega are translation invariant. Thus their averages over n equal the corresponding quantity at EACH a, even though the normal-form coloring need not be translation invariant. This proves(M2). No claim that each individual colored negative-grade rate is translation invariant was used.

## 4. Original time-weighted mean output and exact limits

Let nu_(a,mu) be the expected original counting measure on[0,T], and let b_(a,mu)(s)=kappa Tr[rho_micro(s)Bhat_mu*Bhat_mu]. The cumulative signed difference has the uniform bound(M2). Integration by parts therefore gives, for a deterministic bounded-variation time weight f,

    |integral f dnu_(a,mu)-integral f(s)b_(a,mu)(s)ds|
      <=C epsilon²(1+T)² (|f(T)|+Var f).             (M10)

There is no atom at time0; a convention including f(0) can use the larger supnorm+variation bound. Summing finitely many center/mark weights adds their explicit variation factors. Original labels are never merged or refined. This controls cumulative means and fixed bin means, not total variation of the full timestamp law against arbitrarily rapidly oscillating tests.

Crucially, b(s) is NOT asserted to be the conditional intensity of the microscopic history, nor is rho_micro replaced by an effective state. The theorem alone gives no quantum post-mark map approximation, higher count correlations, field moments or source-cluster tail. It does isolate the actual original leading source word as the unconditional mean consumer on a common positive time interval, uniformly in volume, while respecting bare preparation and shared-output coherence. The supplied carrier and original energy law are unchanged. No numerical run or formal review is claimed for this analytic lemma.
