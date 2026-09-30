# Common-time quadratic-weighted microscopic source components

Author analytic discovery lemma, awaiting focused check. Keep CONTRACT's actual compensated finite-spin law, bare Omega, original resolved/coherent marks, physical Gauss sector, fixed delta,kappa,K>0 and epsilon²S(S+1)=delta/K. This is a component estimate in the exact original process, not a replacement process or an observed grade refinement. It uses the checked DEFECT normal form, the quadratic-weight algebra in INITIAL_LAYER_WEIGHTED_LEMMA section1, and the independently checked FIRST_FIELD_MOMENT. It does not use a common-time weighted hole bound, fast gap or local source-cluster assumption.

## Fixed local physical weight and statement

Fix a finite-radius link set E_a translated with center a, and put

    Psi_a=(1+sum_(e in E_a)|E_e|)².

The source/diagnostic weight is not a changed microscopic energy or measured field. Fix one original mark mu at a. With the exact finite-depth normal-form circuit Y, define

    sigma=Y rho_micro Y*,  J_mu=Y j_mu Y*,
    Psi_tilde,a=Y Psi_a Y*,
    J_mu,+=sum_(r>0) J_mu,r,
    Lambda_a,mu= kappa epsilon^-2 J_mu* Psi_tilde,a J_mu,
    R_a,mu=(1-P_W)Lambda_a,mu.                         (S1)

Here P_W is onsite W-grade averaging and J_mu,r are its exact grade components. J_mu,+ keeps all interference AMONG its positive grades and all coherent signs within the one original label mu. The actual jump remains J_mu. Neither J_mu,+ nor any individual grade is a separate observed outcome. Lambda is EXACTLY the physical weighted original post-mark potential expressed in rotated coordinates.

For every fixed T and geometry there are finite C_T,epsilon0 independent of S,L,a such that

    sup_(t<=T) kappa epsilon^-2
        Tr[sigma(t) J_mu,+* Psi_tilde,a J_mu,+]
                           <= C_T epsilon² S <= C_T' epsilon,   (S2)

and

    sup_(t<=T) |integral_0^t Tr[sigma(s)R_a,mu]ds|
                           <= C_T S(epsilon³+T epsilon²)
                           <= C_T'(epsilon²+T epsilon).         (S3)

The first is a positive component bound; the second controls the SIGNED integral of the ENTIRE off-grade physical weighted potential, including weight-conjugation cross terms. A finite sum of monitored center/mark terms has its explicit linear cardinality cost. No estimate of integral |Tr sigma R| or of a trajectory-conditioned hazard is claimed.

## 1. Uniform local quadratic moment from the actual first moment

For any fixed set Z of links let Q_Z=1+sum_Z |E_e| and Xi_Z=1+sum_Z E_e². The checked first-field result gives each physical first moment uniformly bounded on[0,T]. The local conjugation proof there also gives

    ||Y |E_e|Y* - |E_e||| <= C epsilon,

uniformly in spin and volume, from the field-displacement Schur norm and the bounded cone of that single link. This elementary bound alone suffices here (the sharper physical return in that proof is also available). Thus every ROTATED first moment is bounded uniformly on[0,T], without assuming colored-circuit translation symmetry. On the finite spin box,

    E_e² <= S |E_e|,
    Q_Z² <= (1+|Z|S) Q_Z,

so, for S>=1,

    sup_(t<=T) Tr[sigma(t)Xi_Z] + Tr[sigma(t)Q_Z²]
                                         <= C_(Z,T) S.         (S4)

A bounded enlargement of Z changes only this constant. This is precisely where coupling spin to epsilon is useful. It is an upper bound growing like S; no second-moment uniform integrability or rotor second moment is inferred.

## 2. Quadratic form closure, retaining the physical post-mark weight

Use the physical charge/field basis and the section1 displacement norms s_p with fixed p>=4. Normalized hops and diagonal normalized electric compensation have uniform s_p. Finite products, grade projection/homological inverse, and exact local circuit conjugations have the same uniform analytic coefficient bounds on each bounded cone. All statements include boundary-blocked spin paths with their actual zero amplitudes.

For a bounded-cone coefficient A, inserting a finite quadratic field weight gives the form bound

    A* Q_Z² A <= C s_p(A)² Xi_(Z enlarged by supp A),            (S5)

with a finite geometry-dependent constant. Indeed each matrix path changes Q_Z by at most its field displacement; weighted row and column sums, Schur's test, and 2|E_e E_f|<=E_e²+E_f² give (S5). The same row argument bounds a general Hermitian quadratic-weighted coefficient by +/- C Xi on its cone. Products, complete local adjoint generator actions and I_W preserve that class, with their coefficient's stated epsilon order. Only terms whose supports meet the current cone act; disjoint complete gains and losses cancel. No extensive operator norm is multiplied by another extensive norm.

The exact conjugated weight has the quadratic expansion

    Psi_tilde,a=Psi_a+epsilon Psi1_a+O_quad(epsilon²),

where Psi1_a=[S1,Psi_a], S1=-F+F*, has grades +/-1. This formula holds in the just stated quadratic form class, not in an unweighted norm uniform in S. It follows either by the convergent local gate series in displacement norms or by conjugating each field factor separately. In particular Psi_tilde,a is positive and has majorant C Xi on a fixed enlarged cone.

The original transformed jump has J_mu,+ = O_(s_p)(epsilon²), since j has grade -1 and its first derivative has only grades0,-2. Inserting its squared order in (S5) proves

    J_mu,+* Psi_tilde,a J_mu,+ <= C epsilon^4 Xi_Z.

Together with(S4) and the microscopic kappa epsilon^-2 prefactor this proves(S2). No source paths or coherent same-label signs have been discarded.

## 3. Entire off-grade potential, with all weight and jump cross terms

At order epsilon^-2, Lambda has coefficient kappa j_mu*Psi_a j_mu, which has grade0. At order epsilon^-1 its coefficient includes BOTH mixed jump terms and the weight derivative:

    kappa(j1_mu*Psi_a j_mu+j_mu*Psi_a j1_mu
                         +j_mu*Psi1_a j_mu).

All have grades +/-1. Thus R=(1-P_W)Lambda has local quadratic strength O(epsilon^-1), including its exact higher terms. This leading-order assertion is not obtained by holding the post-mark weight fixed while conjugating only jumps.

Write the EXACT original rotated adjoint generator as

    L'* = i delta epsilon^-4[W,.]+ B_epsilon,
    B_epsilon=epsilon^-2 B2+O_local(epsilon^-1),

where B2 preserves W grades. Define

    K1=(i epsilon^4/delta) I_W R,
    K2=(i epsilon^4/delta) I_W(1-P_W)B_epsilon K1.                (S6)

K1,K2 are Hermitian bounded-cone quadratic-weighted operators of orders epsilon³ and epsilon^5. The exact identity is

    L'*(K1+K2)=-R+P_W B_epsilon K1+B_epsilon K2.                (S7)

The possible epsilon term in P_W B_epsilon K1 vanishes because B2 preserves grades and K1 is off-grade. The residual in(S7) therefore has quadratic strength O(epsilon²). The bounded number of local actions gives one fixed cone Z' with

    |<K1+K2>_sigma(t)| <= C epsilon³ <Xi_Z'>_sigma(t),
    |<P_W B_epsilon K1+B_epsilon K2>_sigma(t)|
                                   <= C epsilon² <Xi_Z'>_sigma(t).

All jump recycling and loss terms are kept in these actions. Integrating(S7) in the exact sigma, using both endpoints and(S4), proves(S3). The finite-spin law is finite dimensional at every stage, so no unbounded generator domain or interchange of infinite-volume limits is being silently asserted. Every constant is independent of volume, and the estimates therefore survive along arbitrary safe-volume/spin sequences. Coupling gives epsilon S<=sqrt(delta/K), yielding the final orders in(S2)-(S3).

## Exact remaining consumer and limits

The grade-diagonal part P_W Lambda is NOT asserted to equal sum_r J_mu,r*Psi_tilde,a J_mu,r: the transformed physical weight itself has off-grades. Balanced weight/jump cross terms remain. Nor do(S2)-(S3) control the diagonal negative-grade holding activity, or the hole-supported block F_a j_mu with its quadratic post-mark weight. Unweighted loss integrability(D10) and unweighted field tightness do not bound their product. The target W1, or an appropriate source-sensitive integrated weighted replacement C1, remains open.

This proves a common-time vanishing estimate for specific components that previously cost O(1) under the crude norm Psi=O(S²). It does not prove that the entire original weighted mark process converges, that a physical grade can be observed, or that the same-state leading formation word can be evolved as a substitute law. No new computation is needed for this analytic lemma; the separately corrected finite algebra control concerns the earlier mean/first-field inputs only.
