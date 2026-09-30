# Neutral dissipative functional and linear event-field gain

Current supporting proof owned by the canonical microscopic-output note. All notation, law, preparation, original mark conventions and uniformity quantifiers are fixed there. This is part of the same bounded theorem, not a separately adopted premise. Constants denoted C may change between displays and depend only on the fixed supports, couplings, horizon and circuit order indicated. Equation prefixes distinguish the components.

## Complete neutral dissipative functional

## Statement and physical-coordinate boundary

Let eta(t) be the exact joint microscopic state with a fixed finite original capped/binned history register (and, if desired, fixed passive reference factors). Its system marginal is the actual rho_micro from bare Omega. Put sigma(t)=Y eta(t)Y*, extending the circuit by identity on the register/reference. Let O be any bounded Hermitian observable on a fixed finite quantum support X and this register, with

    [W,O]=0,  ||O||<=1.

The register is classical, so tests may be taken block diagonal by conditional expectation. The commutator condition means every block has W grade zero. It does NOT require O to commute with each vacancy separately. For a monitored mark, write U_(mu,t)^* for the actual deterministic classical history update on observable blocks. On unmonitored marks it is the identity. Define the EXACT original rotated dissipator and the comparison functional

 D'_epsilon* O =kappa epsilon^-2 sum_mu
     [J_mu* U_(mu,t)^*(O) J_mu -{J_mu*J_mu,O}/2],

 D_B* O =kappa sum_mu
     [Bhat_mu* U_(mu,t)^*(O) Bhat_mu
                            -{Bhat_mu*Bhat_mu,O}/2],
 J_mu=Y j_mu Y*,  Bhat_mu=j_mu F_a.                         (N1)

Only boundedly many terms matter: those whose physical cone meets X and all marks centered in the fixed monitored F. Terms disjoint from both cancel their complete gains and losses. Let b count interior bin boundaries. Uniformly over the indicated test unit ball, all safe volumes and all spins,

 sup_(t<=T) |integral_0^t Tr[sigma(s)(D'_epsilon*O-D_B*O)]ds|
                 <=C_(X,F)[epsilon(1+T)²+epsilon³(1+b)].      (N2)

The constant is independent of cap/reference dimensions; couplings and fixed circuit geometry are permitted. One may replace sigma by eta ONLY on the comparison D_B side, at the additional smaller error C epsilon²(1+T)². Equivalently,

 integral Tr[eta D_micro*(Y* O Y)]
                   =integral Tr[eta D_B*O]+O_(X,F,T,b)(epsilon). (N3)

The microscopic side acts on the DRESSED test Y*OY. No equality with D_micro*O on an undressed test is asserted. Nor does(N2) identify the fast Hamiltonian, the whole quantum generator, an independently evolved effective state or a field-weighted response. It is an integrated signed functional of the complete dissipative part in exact normal-form coordinates.

## 1. Local graded support and the actual pointwise hole bound

For a finite A set U let P_U=prod_(a in U)n_a, Q_U=I-P_U. The physical per-site defect estimate and the squared circuit return give

    Tr[sigma(t)Q_U]<=C_U epsilon²(1+t).                       (N4)

The circuit return is w_aY=Yw_a+[w_a,Y] with ||[w_a,Y]||<=C epsilon; the local conjugation difference supplies that norm without making the global commutator a local operator. The joint register/reference cannot change(N4), since its marginal is the actual system state.

Two elementary domain facts will be used repeatedly. If a local V has NEGATIVE W grade and U contains its physical A support, then V P_U=0: a nonnegative local hole number cannot be lowered below zero. If O has grade zero and its physical support is also contained in U, then [O,P_U]=0. Indeed [W,O]=0 reduces to commutation with W on O's finite support, so O preserves its zero-hole eigenspace and its orthogonal complement. This remains true for every register block and after the classical update. It is not valid for a general grade-changing test, which is why the domain in(N2) is explicit.

All local jump grade components have fixed cones and finitely many grades, independent of spin and volume. Their expansion is

    J_-1=j+O_local(epsilon²),
    J_0=epsilon A+O_local(epsilon³),
    J_-2=O_local(epsilon),
    J_r=O_local(epsilon²) for r>0
                       and other negative r,
    A=Bhat-D,  D=F_a j.                                     (N5)

The grade-zero remainder order uses the proved circuit parity. The complete coherent mark is expanded as one operator; no sign/grade label is observed.

## 2. The leading negative-grade anticommutator needs two different bounds

Take V=J_(mu,-1) at one relevant original mark. The proved local rotated bare-loss budget(G9) and the first line of(N5), squared, give

    integral_0^T a_mu(s)ds<=C epsilon^4(1+T),
    a_mu(s)=Tr[sigma(s)V*V].                                (N6)

Its localization was proved through the translation-covariant PHYSICAL truncation ell=j-epsilon j1 before dividing by volume. No translation covariance of sigma or the colored exact J_-1 is being assumed here.

The complete registered gain obeys

    |Tr[sigma V*U_mu^*(O)V]|<=||O|| a_mu.

For a loss term choose U containing both supports. Since V=V Q_U and O commutes with Q_U,

 |Tr[sigma V*V O]|
   <= ||V sigma^(1/2)||_2 ||V O sigma^(1/2)||_2
   <= sqrt(a_mu) ||V|| ||O|| sqrt(Tr[sigma Q_U]).             (N7)

The other anticommutator half has the same bound by taking adjoints. This step adds the essential local-hole factor missing from a naive operator-norm multiplication of the gain error. Combining(N4),(N6) by Cauchy--Schwarz in time,

 epsilon^-2 integral_0^T |Tr[sigma D[V]*O]|ds
   <=C epsilon²(1+T)
        +C epsilon^-2 sqrt(epsilon^4(1+T)
                                  epsilon²(T+T²))
   <=C epsilon(1+T)².                                     (N8)

This is an ABSOLUTE integral bound on each grade-minus-one dissipator's tested expectation, including its loss. It is still a diagnostic grade component, not an observed channel.

For grade -2, ||J_-2||=O(epsilon), and V P_U=0. Both gain and loss are supported on Q_U on both input sides because O preserves P_U. Their entire expectation is bounded by C epsilon² Tr sigma Q_U. After epsilon^-2 and integration this costs O(epsilon²(T+T²)). Other negative grades are smaller by(N5). Every positive-grade square has operator norm O(epsilon^4), so its complete microscopic dissipator costs O(epsilon²T) without a hole assumption. There are only finitely many grades and relevant marks.

## 3. Neutral jump and the same actual source word

From(N5), the grade-zero dissipator after multiplication by epsilon^-2 differs from D[A]* by local norm O(epsilon²). The exact physical occupancy blocks are

    Bhat=n_a Bhat n_a,
    D=w_a D w_a,
    A=Bhat-D,
    Bhat*D=D*Bhat=0,
    A*A=Bhat*Bhat+D*D.                                    (N9)

For arbitrary O the gain cross terms need not vanish. They are kept here. On an enlarged all-A-filled projector P_U, Bhat and every grade-zero O block preserve P_U, while D annihilates P_U on both sides. Therefore each of

    Bhat*U_mu^*(O)D,  D*U_mu^*(O)Bhat,
    D*U_mu^*(O)D,  {D*D,O}

is supported on Q_U on BOTH sides. Their bounded norms and(N4) show

    |Tr[sigma(D[A]*O-D[Bhat]*O)]|
                                    <=C epsilon²(1+t).     (N10)

This uses the neutral test domain, not dephasing of the actual coherent mark. Summed/integrated with the neutral Taylor remainder, it contributes O(epsilon²(1+T)²).

## 4. Restore the full offgrade map, including all recycling

For neutral O, onsite grade averaging is the EXACT diagnostic identity

    P_W D'_epsilon*O
                =kappa epsilon^-2 sum_(mu,r)D[J_mu,r]*O.    (N11)

Its difference from the full original dissipator is

    R_O=(1-P_W)D'_epsilon*O.

The bare term has grade zero; the first full polarized jump map has grades +/-1. Thus R_O has local strength O_(X,F)(epsilon^-1||O||), including all higher exact cross terms. Classical updates carry grade zero. All monitored centers F remain in the anchor even if outside X, and exact gain/loss cancellation removes the other disjoint terms.

Use the COMPLETE original joint adjoint generator in the corrector, not a generator with the grade components separated:

    L'^*=i delta epsilon^-4[W,.]+B_epsilon,
    B_epsilon=epsilon^-2 B2+O_local(epsilon^-1),
    K1=(i epsilon^4/delta)I_W R_O,
    K2=(i epsilon^4/delta)I_W(1-P_W)B_epsilon K1.

Then exactly

    L'^*(K1+K2)=-R_O+P_W B_epsilon K1+B_epsilon K2.

K1,K2 have local norms O(epsilon³),O(epsilon^5), uniformly on the test unit ball. The putative epsilon residual vanishes because B2 preserves grades. The remaining local norm is O(epsilon²). Finite support incidence and complete register Kraus-column bounds are independent of register/reference dimension. Integrating within each bin and accounting for corrector changes at its b boundaries yields

 |integral_0^t Tr[sigma(s)R_O(s)]ds|
                   <=C_(X,F)||O||[epsilon³(1+b)+T epsilon²]. (N12)

The same original coherent recycling and both losses act on the corrections. This is a signed integral estimate for R_O, not an assertion that its absolute instantaneous norm is small. The exact joint state is required here; arbitrary time-varying extensions of its marginal would not automatically obey this generator identity.

Equations(N8),(N10)-(N12), summed over the finite relevant mark set, prove(N2). None uses the fast Hamiltonian's absorption or tries to bound the entire generator norm uniformly.

## 5. Physical return and exclusions

The comparison D_B*O is a bounded grade-zero local/register observable with fixed anchor X union F, on each fixed bin. Its first circuit conjugation correction has grades +/-1 and vanishing all-A-filled diagonal block. The physical rare-hole estimate therefore gives the proved sharper expectation return

 |Tr[sigma D_B*O]-Tr[eta D_B*O]|
                        <=C epsilon²(1+sqrt(1+t)).          (N13)

The original register does not require conditional moment bounds: its joint hole trace is its system marginal's trace. Integrate(N13) and use exact covariance of the microscopic dissipator under Y to obtain(N3). Crucially, small ||Y*OY-O|| does not justify applying the epsilon^-2 microscopic dissipator to their difference as though it were small. The dressed-test qualification in(N3) cannot be dropped.

The bound is uniform over the bounded NEUTRAL local/register test unit ball. It controls the complete dissipative contribution in the exact normal form, including the previously problematic negative-grade anticommutator via(N7). It supplies no bound on the fast D2-vacancy Hamiltonian commutator, on hole-weighted quadratic electric coefficients, or on the full quantum evolution. Grade-changing tests, field-weighted norms, growing support/time variation and continuous-timestamp process total variation need separate estimates. Supplied carrier, compensation, preparation and original energy law remain imports.

## Linear post-event field weight

This targets a specific source-sensitive norm on a common physical horizon, weaker than the open quadratic hole/energy consumers. Fix a finite set Z of physical links in the post-event output and put

    Q_Z=1+sum_(e in Z)|E_e|.

Q_Z is a diagnostic linear field weight, not the microscopic Hamiltonian or a replacement energy ledger. Let eta(t) be any positive extension of the SAME actual microscopic state rho(t). Its history register may be the actual finite original capped/binned register. At a fixed original mark write

    L=sqrt(kappa) epsilon^-1 j_mu,
    B=sqrt(kappa) Bhat_mu,
    E=L-B.

The actual and comparison gains are G_L=L eta L*, G_B=B eta B*. Each is an unnormalized original-mark quantum current. Both output quantum supports remain inside the actual spin box. The following estimates are uniform in safe volume and spin under epsilon²S(S+1)=delta/K, on every fixed horizon T:

    integral_0^T Tr[Q_Z G_L(t)]dt <=C_(Z,mu,T),                (W1lin)

    integral_0^T ||Q_Z^(1/2)[G_L(t)-G_B(t)]Q_Z^(1/2)||_1 dt
                                      <=C_(Z,mu,T) sqrt(epsilon). (W2lin)

The same original register append may be applied, since it commutes with the physical Q_Z and contracts the trace norm. Fixed finite mark sets retain their labels in a direct sum, with the finite sum of constants. No arbitrary field-changing CP postprocessing is claimed to preserve this weighted bound.

## 1. Squared weighted error, with its complete spin price

The proved nonnegative gain-amplitude estimate gives

    I_err=integral_0^T ||E eta(t)^(1/2)||_2²dt
                                      <=C epsilon²(1+T)².

It depends only on eta's actual system marginal. On the output spin box,

    0<=Q_Z<=(1+|Z|S)I.

Since E is the difference of two actual finite-spin source maps, its output also lies in that box. Therefore

 I_err,Q=integral_0^T ||Q_Z^(1/2)E eta(t)^(1/2)||_2²dt
                 <=(1+|Z|S) I_err <=C_(Z,T) epsilon.          (W3lin)

The last step uses S epsilon<=sqrt(delta/K) and epsilon<=epsilon0. This is a finite-spin norm price applied to a CHECKED squared error, not an assertion of a rotor norm for Q_Z or a weighted preparation assumption. It retains the full original coherent j_mu inside E.

## 2. Source word's field activity in the actual state

Each branch of Bhat=j_mu F_a contains two legal unit field shifts and the original hard-core matter factors; normalized spin amplitudes have magnitude at most one. Pulling Q_Z through a branch changes its diagonal value by at most two on the affected links. The branch is a conditional partial permutation, hence its weighted square is bounded by Q_Z+2 on its input. A finite Cauchy estimate for the source's actual sum of paths/signs consequently gives the operator form bound

    B* Q_Z B <=C_(mu,Z) [1+sum_(e in Z union supp B)|E_e|].    (W4lin)

No branch is observed or decohered; this is only an upper bound on the complete original word. Adding its finite support on the right is harmless and covers all orientation/charge conventions and intermediate shifts. Forbidden spin-boundary paths have their actual zero coefficient and obey the same bound.

The first-field argument in the normal-form and moments appendix applies to each physical link of the ACTUAL unconditioned marginal, including all later births. Thus

    I_B,Q=integral_0^T Tr[Q_Z G_B(t)]dt<=C_(Z,mu,T).            (W5lin)

The register/reference extension does not require conditional field bounds. Combining L=B+E by squared triangle now gives

    I_L,Q<=2 I_B,Q+2 I_err,Q<=C_(Z,mu,T),

which is(W1lin) for the original physical gain itself, not a substituted source process.

## 3. Weighted gain-current difference and actual event-field tails

The exact gain difference factors as

    G_L-G_B=E eta L*+B eta E*.

After inserting Q_Z^(1/2) on both sides, Hilbert-Schmidt Holder and Cauchy--Schwarz in time yield

 integral ||Q_Z^(1/2)(G_L-G_B)Q_Z^(1/2)||_1
       <=sqrt(I_err,Q)[sqrt(I_L,Q)+sqrt(I_B,Q)].

Equations(W3lin)-(W5lin) prove(W2lin). Both the comparison state and history correlations are the exact actual ones throughout. The result is an averaged integrated post-event current norm, not a pointwise conditional intensity or a whole-process comparison.

There is also a uniform tail statement for the ORIGINAL gain mass. With P_R the projection that every link in Z has |E_e|<=R,

 integral Tr[(I-P_R)G_L]dt <=C_(Z,mu,T)/R.                     (W6lin)

Indeed I-P_R<=Q_Z/R for R>=1. The actual original mean-count bound gives integral Tr G_L<=C_T, and the gentle positive-operator estimate followed by time Cauchy gives

 integral ||G_L-P_R G_L P_R||_1dt<=C_(Z,mu,T)/sqrt(R).         (W7lin)

These statements concern the real quantum payload at original events, including events after register overflow. They show uniform field tightness of that unnormalized gain measure. They do NOT imply uniform integrability of the Q_Z-weighted gain itself: a first-moment bound alone does not control integral Tr[Q_Z 1_(Q_Z>R)G_L] uniformly. No such stronger tail was used above.

## Quadratic boundary and remaining consumer

For Q_Z², the same naive output norm price is O(S²); multiplying the proved O(epsilon²) squared amplitude error then gives only O(1). The source comparison activity has at best O(S) from the current first-field input. Thus this proof does not extend(W2lin) to a vanishing quadratic-weighted norm, and it does not bound the held-hole quantity epsilon^-2 Tr[rho w_a (1+sum_(e in a fixed local link set)|E_e|)^2]. The dark weighted holding, actual energy uniform integrability and full microscopic-to-effective evolution remain open. The new uniform linear post-event moment and weighted same-state gain comparison narrow that source obligation without changing the original records or energy law.
