# Positive global source moments from the actual microscopic law

Candidate analytic lemma for focused checking. This controls the actual unconditional microscopic process from bare Omega, with both original instruments treated separately. It does not assume a local cluster tail or the desired microscopic-to-effective comparison. K_def below is a matter count, distinct from the fixed electric coupling K.

## Statement

Let n=|A| on an even cubic torus, K_def=W+N_B, and fix delta,kappa>0 and theta>0. There are epsilon_theta>0 and C_theta<infinity, independent of spin and volume, such that the ACTUAL microscopic state satisfies

    Tr[exp(theta K_def) rho_micro(t)]
            <=exp[C_theta n(t+epsilon^2)], t>=0,       (G1)

whenever0<epsilon<=epsilon_theta. The stated joint law epsilon^2 S(S+1)=delta/K may then be imposed. Constants need not be uniform in theta or couplings and no practical values are claimed. The same conclusion, with possibly different constants, holds in the exact local unitary frame constructed below. No electric moment hypothesis is required for this bounded matter count.

Original births obey [N,j]=2j, [W,j]=-j and therefore

    K_def=N-n+2W,  [K_def,j]=0.                         (G2)

In the actual marked process N=n+2R, with R the total number of original births, on each number block. Since2R=N_B-W<=K_def,

    E exp(2theta R(t))<=exp[C_theta n(t+epsilon^2)].    (G3)

This is a bound on the original count distribution with every later birth retained, not a Poisson approximation or a statement about conditional hazards. It is global, not a local exponential-clustering assertion.

## 1. Uniform local frame through third order

The actual normalized spin shifts, compensation terms and bare jumps have uniform local norms, supports and overlap counts. In particular the compensation is a bounded local polynomial including its exact diagonal spin correction and Q_a gate. The local finite-color normal-form construction used in the independently checked defect lemma applies through order three. Its needed mechanism is restated here.

For a local coefficient A, phase-average against the onsite integer W to extract its grade-zero part, and set I_W(A)=sum_(r!=0)A_r/r. This operation preserves support and has norm<=pi||A||/2. For Hermitian off-grade A, I_W(A) is anti-Hermitian and [I_W(A),W]=-A. Color the bounded-overlap supports, exponentiate generators at order epsilon^r on disjoint supports within each color, and process r=1,2,3. Ordering corrections enter only later coefficients and remain in bounded cones. Complex-parameter Taylor estimates on those finite cones give a uniform local remainder. Every word preserves N and Gauss; every retained diagonal coefficient is termwise W-preserving. Parity under epsilon->-epsilon and (-1)^W makes odd diagonal Hamiltonian coefficients vanish.

The resulting EXACT unitary Y_epsilon is a finite-depth local circuit, with each gate within O(epsilon) of identity uniformly in spin, and

    H_Y=delta epsilon^-4 W+delta epsilon^-2 D2+R_H,
    [D2,W]=[D2,N]=0,  ||R_H||_local<=c_H,
    J_(m,Y)=j_m+epsilon j_(1,m)+epsilon^2 R_(m,J).       (G4)

R_H and each R_(m,J) have bounded support/cone and uniform local strengths for sufficiently small epsilon. The order-one Hamiltonian remainder is retained in full. No global condition epsilon||T||<<1 is imposed. Although Y need not be close to I globally, its depth, support sizes and per-gate norm estimates are uniform.

Its first derivative is S1=-F+F^*, hence j_(1,m)=[S1,j_m]. It has W grades0,-2 and raises N by two. Bare j has grade-1. Define the LOCAL anti-Hermitian terms

    X_m=j_m^*j_(1,m)-j_(1,m)^*j_m,  X=sum_m X_m.

Each X_m preserves N and has only W grades+1,-1. Its support is fixed, its norm uniformly bounded, and the sum has bounded incident strength. It is not a measured jump-grade decomposition.

## 2. Exact cancellation for the count algebra

For every bounded f(K_def), bare j commutes with f. Directly expanding both recycling and the anti-commutator loss gives

    D_cross(j,j1)^*f
      =j^* f j1+j1^* f j
           -{j^*j1+j1^*j,f}/2
      =[f,j^*j1-j1^*j]/2.                              (G5)

This is an identity only on the f(K_def) algebra; the full cross dissipator is not declared Hamiltonian. At the original scaling its contribution is (kappa/(2epsilon))[f,X].

Set

    S_loss=(i kappa/(2delta)) I_W(X).

I_W(X) is Hermitian because X is anti-Hermitian, so S_loss is anti-Hermitian. Also [S_loss,W]=-i kappa X/(2delta). Implement Z_epsilon as a finite-color product of the local exp(epsilon^3 S_loss,local), and set V=Z Y. Its first relevant Hamiltonian change is

    H_V=H_Y+delta epsilon^-1[S_loss,W]+O_local(1).

All ordering corrections from these new gates begin at physical order epsilon^2; conjugation of D2 contributes order epsilon, and all are bounded local remainders. The leading j and epsilon j1 coefficients in(G4) are unchanged. For f(K_def),

    i[delta epsilon^-1[S_loss,W],f]
                    =-(kappa/(2epsilon))[f,X].          (G6)

Thus(G5) is canceled, with the displayed sign. The epsilon^-4 penalty, epsilon^-2 D2 Hamiltonian and epsilon^-2 bare dissipators all annihilate f(K_def) exactly. The remaining action is of physical order one in local strength, not order epsilon^-1 or epsilon^-2. Labels and coherent edge maps are unchanged; V is only an exact mathematical coordinate frame.

## 3. A positive operator inequality at arbitrary volume

Write Q_theta=exp(theta K_def) and let L_V^* be the exact transformed adjoint generator. Since K_def is a sum of commuting onsite matter counts, conjugating any local term by Q_theta^(+/-1/2) keeps its support and multiplies its norm by at most exp(theta s/2), where s is the number of matter-count factors in that support. It has no dependence on the dimension of the electric factors.

After the exact cancellations(G5)-(G6), each term of

    B_theta=Q_theta^(-1/2)(L_V^* Q_theta)Q_theta^(-1/2)

is a bounded local remainder with uniformly bounded norm. For Hamiltonian terms this follows by writing the normalized commutator as i(Q^-1/2 H Q^1/2-Q^1/2 H Q^-1/2). For a jump product, use the same local conjugations in gain and loss. Taylor remainders in(G4) remain bounded after these conjugations because their support/cone is fixed. Summing the bounded number of center terms per A site gives a finite b_theta such that

    B_theta<=b_theta n I,
    L_V^* Q_theta<=b_theta n Q_theta.                  (G7)

There is no additive corrector of size epsilon^3 n being assumed small. Q_theta itself is strictly positive at every volume. Positivity of the transformed state and Gronwall give

    Tr(Q_theta rho_V(t))<=exp(b_theta n t)
                                      Tr(Q_theta rho_V(0)). (G8)

At each finite spin/volume this is an ordinary bounded-generator inequality. It is also valid for the separately supplied finite-volume rotor version, since W,T,C,j and Q_theta are bounded there. No unbounded electric multiplication operator occurs in this lemma. Uniformity is supplied by the local estimates, not by a growing-volume semigroup assumption.

## 4. The small-gate inequality that prices bare preparation

Let A be a local nonnegative integer matter count with spectrum in{0,...,s}, P0 its zero-count projection, and U a unitary with eta=||U-I||. Fix0<theta<theta', put M=exp(theta s), r=exp[-(theta'-theta)] and g=1-r. If eta<=g/(4M), then

    U^* exp(theta A)U
       <=exp[c(theta,theta',s) eta^2] exp(theta' A),
    c=(M-1)+8M^2/g.                                   (G9)

Here is the complete uniform-dimension proof. Normalize the left side by exp(-theta'A/2), obtaining T^*T for T=exp(theta A/2)U exp(-theta'A/2). On P0, unitarity and exp(theta A)-I supported off P0 give its block bound1+(M-1)eta^2. The off-diagonal block has norm<=2M eta, since ||U^*exp(theta A)U-exp(theta A)||<=2M eta. The positive-count diagonal block is at most r+2M eta<=1-g/2. For a vector x+y in the two blocks, bound the cross term by

    4M eta ||x||||y||
       <=(8M^2 eta^2/g)||x||^2+(g/2)||y||^2.

This proves T^*T<=[1+c eta^2]I<=exp(c eta^2)I. The argument allows infinite electric degeneracy of each matter-count block and does not assume a product gauge state.

For a layer of disjoint local gates, apply(G9) on its tensor factors. The untouched factors contribute contractions after the theta' tilt. There are O(n) gates. Across the finite number d of circuit layers, use a fixed sequence theta=theta0<theta1<...<theta_d. Their number and maximal local s are independent of spin and volume. The per-gate eta<=c_gate epsilon gives, for V and also for V^*, constants a_theta and a finite Theta(theta)>theta such that

    V^* Q_theta V <=exp(a_theta n epsilon^2)Q_Theta,
    V Q_theta V^* <=exp(a_theta n epsilon^2)Q_Theta.       (G10)

Different harmless maxima may be absorbed into a_theta. The smallness threshold is the minimum of finitely many gate thresholds and is independent of volume. Gauss restriction preserves the operator inequality. This is why the cost is O(n epsilon^2), not an unjustified global ||V-I|| estimate.

Since K_def Omega=0, the first inequality in(G10) gives

    Tr(Q_theta rho_V(0))<=exp(a_theta n epsilon^2).

For the physical state rho=V^*rho_V V, use the second inequality, apply(G8) at Theta(theta), and price its initial moment in the same way. The result is

    Tr(Q_theta rho(t))
       <=exp[(a_theta+a_Theta)n epsilon^2+b_Theta n t],

which is(G1) after increasing C_theta. Thus the bare preparation, physical count and exact original dynamics are all included.

## 5. A concrete source-weighted consequence, with its limit

Fix theta, choose T<=theta/(4C_theta) and epsilon^2<=theta/(4C_theta). Then(G1) gives, uniformly for t<=T, an exponential suppression of global dense sectors. For the physical projector Pi_dense onto full B and W=2,

    Tr(Pi_dense rho(t))<=exp(-theta n/2-2theta).         (G11)

The same form holds in the V frame. The checked physical hole-density bound independently gives Tr(Pi_dense rho)<=C epsilon^2 n(1+T)/2. Combining the two estimates by dividing volumes at n=(4/theta)log(1/epsilon) yields

    sup_volume,t<=T Tr(Pi_dense rho(t))
                   <=C' epsilon^2[1+log(1/epsilon)].     (G12)

The V-frame hole bound follows from the earlier Y-frame bound and the projection estimate for Z, whose local gate size is O(epsilon^3). Thus(G12) applies to that leading fast coordinate sector as well, with changed constants. For bounded instantaneous state outputs, the gentle projection estimate makes the trace weight of deleting this sector at most twice the square root of(G12). This is not a deletion imposed on the actual process.

The total original birth count is monotone. Equation(G3) also prices actual high-record histories on a short interval. That can suppress late globally dense histories at large volume; it does not justify measuring whether an internal quantum basis sector was ever visited.

None of(G11)-(G12) bounds epsilon^-2 times an integrated fast current by a vanishing quantity, controls effects left by earlier visits, or supplies a LOCAL occupied-island tail inside a much larger system. In particular one cannot replace the total volume n in(G1) by the size of a selected region without a new argument: H2 transports the local count. The local-source M4 obligation remains open.

## Exact control and reuse boundary

check_tilt.py constructs the complete72-state spin-one Gauss tree with one degree-three A star. For both original instruments it verifies the order-three Hamiltonian cancellation, the bare K_def commutation, the functional cross-jump identity for q^K at q=2,3, and the additional-unitary sign. The uncorrected pole has102 nonzero entries; all vanish after the stated correction, while the wrong sign doubles them. Initial tilted coefficients15 and40 equal5(q^2-1). The actual positive-grade second jump coefficient has squared norm18 on Omega, consistent with the three-leaf source geometry. Cost0.55627CPU seconds,35,258,368 peak RSS bytes. These finite exact checks do not establish the uniform circuit, small-gate inequality or moment theorem; those are the analytic arguments above.

This new lemma is not yet independently checked. Its intended reuse is the limited global source-weight consequence, not a shortcut to local clustering, energy moments or the complete microscopic limit. The earlier read-only search overrun is recorded separately in RUN_CONTRACT and is not included in the scientific control cost.
