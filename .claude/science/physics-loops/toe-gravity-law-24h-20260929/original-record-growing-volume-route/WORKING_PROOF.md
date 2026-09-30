# Quantitative global comparison on a growing-volume window

Author proof, provisional pending focused independent reconstruction. Selected science fb5da8dd5ac1b001b0c619070f27e5b7f8fe4be7; selected procedure7146fe17a76de41badcaca3c3c7cac6d11eb2a00. No physical-law or native-axiom selection is asserted.

## 1. Exact statement and comparison space

Take an even cubic torus with safe L>=64 and n=|A|=L³/2. The supplied microscopic physical carrier has qutrit charges q=0,+1,-1, integer-spin S links, Gauss div E=q-1_A, W=sum_A(1-n_a), and bare Omega (all A plus, B empty, E=0). Use exactly

    H=delta epsilon^-4 h(epsilon),
    h(z)=W+z T+z² C_S,
    T=-sum_a(F_a+F_a†),
    C_S=sum_a(F_a†F_a-D_a,S+D_a,infinity) Q_a,
    L_mu=sqrt(kappa) epsilon^-1 j_mu,
    epsilon² S(S+1)=delta/K.                                  (1)

Q_a is the actual product of all other A occupations within graph distance2. Each original mark is either a resolved j_(a,b,+/-), or the ORIGINAL unnormalized coherent sum j_++j_-; the two instruments are alternatives. No hidden sign resolution is performed. Delta,kappa,K are fixed positive constants. All Hamiltonian terms preserve total matter occupation Ntot, and every original mark raises Ntot by two. The carrier/law/clock/GKSL interpretation/preparation are supplied premises.

Let P=1_(W=0). The TRUE canonical finite-spin target on P has

    h_eff,S=delta epsilon^-2 H2,S+delta H4,S,
    H2,S=C0-M=D/[S(S+1)],
    H4,S=M²-(M C0+C0 M)/2+A† C1 A-Z†Z/2,
    A=Pi1 T P, M=A†A, Z=Pi2 T Pi1 A,
    B_mu,S=-P j_mu Pi1 T P.                                  (2)

Thus delta epsilon^-2 H2,S=K D exactly. Its jumps are sqrt(kappa) B_mu,S. This is the landed positive-overlap convention, not a new choice of block gauge.

Embed spin link boxes in the physical rotor carrier and P in the full qutrit carrier. The rotor target is exactly

    h_eff,infinity=K D+delta H4,infinity,
    H4,infinity=-2 sum_(unordered dist(a,c)=2) (F_c F_a P)†(F_c F_a P),
    jumps sqrt(kappa) B_mu,infinity.                          (3)

For every finite T there are finite constants c0,C_T, independent of n,S and of the chosen original register, such that if epsilon n²<=c0, then

    sup_(0<=t<=T) ||rho_micro,S(t)-rho_eff,S(t)||_1
       <= C_T [epsilon n³+epsilon² n⁶],                       (4)

and, from Omega,

    sup_(0<=t<=T) ||rho_eff,S(t)-rho_eff,infinity(t)||_1
       <= C_T n⁶/[S(S+1)].                                  (5)

The same bounds hold jointly with any finite original marked register: all centers may be observed, labels and their order retained, time bins arbitrary, and overflow caps arbitrary. Constants do not grow with the register dimension, cap or number of bins. Section7 extends the statement to the complete finite-volume original timestamp instrument plus final quantum output, in its integrated trace norm. Conditional normalized states on rare individual histories are not claimed close.

Combining (1),(4),(5), if epsilon n³->0, the complete comparison error tends to zero. In particular n=o(S^(1/3)) is sufficient. These are sufficient, nonoptimal powers. The theorem does not claim arbitrary-volume uniform local approximation.

## 2. Why this is not the existing fixed-graph conclusion

The complete landed compensation target proof supplies the exact coefficients (2), fixed-graph uniform-S O(epsilon) approximation, and finite-register compatibility, but leaves its graph constants implicit. The landed common-field note supplies strong spin/rotor convergence at each fixed graph. The landed pair-form note supplies (3) and an extensive rotor magnetic norm. None provides (4)-(5) with an explicit joint volume power.

The current matched PR9412 gives actual microscopic local output compactness and moments but explicitly leaves the target Hamiltonian identification open. PR9399 constructs the effective thermodynamic target, not microscopic approximation. The earlier uniform-local-ring source uses a dressed preparation, different spin-half law and a vanishing formation rate. It does not address (1). No proposal theorem is needed below; the proof uses the actual landed coefficients and elementary operator estimates.

The quantitative variation of the landed fixed-graph argument is an exact P/Q Hamiltonian Sylvester correction for the full off-diagonal dissipative loss. It uses the gap between the entire perturbed W0 band and its complement. It does NOT assume a gap, observability, absorption, static B masks or finite-excitation response within the fast sector. It therefore has a different cost and domain from the earlier local response attempts.

## 3. Dimension-independent canonical ground rotation

The actual source gives uniformly in S

    ||T||<=12n, ||C_S||<=48n,
    number of original marks <=12n, ||j_mu||<=2,
    ||B_mu,S||<=12.                                         (6)

The last bound uses the actual local identity B_mu=P j_mu F_a P; the much weaker generic global bound is not substituted. It also holds for rotor B. All arguments below may be amplified by an arbitrary spectator/register Hilbert space.

For |z|<=r_n=(2048n)^-1, the perturbation has norm

    ||zT+z² C_S|| <1/128.

On |zeta|=1/2 the unperturbed resolvent of W has norm<=2 and the perturbed resolvent norm<3. Define only the ground Riesz projection

    P(z)=(2pi i)^-1 integral_(|zeta|=1/2) (zeta-h(z))^-1 dzeta.

The resolvent identity gives ||P(z)-P||<=3||zT+z²C_S||<3/128. Put

    S(z)=P(z)P+(I-P(z))(I-P),
    U(z)=S(z)[I-(P(z)-P)²]^-1/2.                            (7)

Use the norm-convergent inverse-square-root series. This is analytic, U(0)=I, and U,U^-1 have norm<2 on that disk. For real z, P(z) is orthogonal, S†S=I-(P(z)-P)², U is unitary and maps P to P(z). It block-diagonalizes h only relative to P,Q=I-P. No sum over n+1 excited clusters is used. Its ground column is exactly

    U(z)P=P(z)P[P P(z)P]^-1/2,

the same positive-overlap column as the source's all-cluster rotation. Consequently its ground Hamiltonian has exactly the coefficients (2), regardless of the different extension on Q.

Let h_P(z)=P U(z)^-1 h(z) U(z)P. The contour formula for h(z)P(z) bounds h_P(z) by3, independently of ||W||=n. This is important: bounding h(z) naively would add a spurious volume factor. Xi=(-1)^W gives h(-z)=Xi h(z)Xi, U(-z)=Xi U(z)Xi and Xi P=P, so h_P is even. The source's explicit graph-coordinate/orthonormalization calculation then yields

    h_P(z)=z² H2,S+z⁴ H4,S+O(z⁶ n⁶).

Cauchy on the above disk gives, for epsilon<=r_n/2,

    ||h_P(epsilon)-epsilon²H2,S-epsilon⁴H4,S||
       <=4*2048⁶ epsilon⁶ n⁶.                             (8)

The exact derivative is U'(0)P=-Pi1 T P. Because j_mu P=0,

    U^-1 j_mu U P=epsilon B_mu,S+R_mu,
    ||R_mu||<=c_j epsilon² n², c_j=16*2048².             (9)

Indeed the analytic function U^-1 j U P has norm<=8 on the disk, and its Taylor tail starts at order2. Also ||U-I||<=c_U epsilon n for a universal c_U (8192 suffices by the same series bound).

Choose c0<=min(1/4096,1/c_j). Then epsilon n²<=c0 guarantees all preceding conditions and, writing J_mu=U†j_mu U,

    p_mu=P J_mu P, r_mu=Q J_mu P,
    ||p_mu||<=13epsilon, ||r_mu||<=c_j epsilon²n².        (10)

The spectra of the exact rotated physical Hamiltonian H_d=delta epsilon^-4 U†hU have separated P,Q blocks. Weyl's elementary spectral enclosure for real h gives

    inf spec H_Q - sup spec H_P >=g,
    g>=delta/(2epsilon⁴).                               (11)

This is a band separation for small global perturbation epsilon n; it is not a dissipative gap. All spin spaces here are finite dimensional. The estimates do not depend on their dimension.

## 4. Exact loss correction and quantitative full-process comparison

Work first without a register. Let G be the fully rotated original GKSL generator with H_d and jumps sqrt(kappa)epsilon^-1 J_mu. Define a CPTP reference generator on P using the EXACT H_P and jumps sqrt(kappa)epsilon^-1 p_mu; call it L_P. Let E embed P densities. The residual G E-E L_P has:

- cross gains kappa epsilon^-2 sum(r_mu rho p_mu†+p_mu rho r_mu†);
- Q gains kappa epsilon^-2 sum r_mu rho r_mu†;
- P loss leakage -(kappa/(2epsilon²)) sum{r_mu†r_mu,rho};
- the complete off-diagonal loss A_loss rho+rho A_loss†, where

    A_loss=-(kappa/(2epsilon²)) sum Q J_mu†J_mu P.        (12)

No term in J_mu†J_mu has been replaced by a leading-grade approximation. In particular (12) is O(epsilon^-1 n) and cannot be discarded. Equations (6),(10) give

    ||A_loss||<=156 kappa epsilon^-1 n.                 (13)

For any Q<-P operator A, define the exact Sylvester inverse

    R_H(A)=integral_0^infinity e^-tH_Q A e^tH_P dt.

Although each factor may individually contain a scalar growth, their product norm is bounded by e^-gt||A||, so this is a norm-convergent integral and ||R_H||<=g^-1. Direct differentiation gives H_Q R_H(A)-R_H(A)H_P=A. Define

    X=-i R_H(A_loss), K(rho)=Xrho+rho X†.

Then

    ||X||<=312(kappa/delta) epsilon³n,
    G_H K-K L_(P,H)=-(A_loss rho+rho A_loss†).            (14)

The sign follows from -i(H_QX-XH_P)=-A_loss. This cancels the full loss rather than only its leading coefficient. The huge exact P Hamiltonian also cancels inside (14); no bound proportional to its norm is paid.

The uncanceled gains and P leakage have induced trace norm at most

    312 kappa c_j epsilon n³+24 kappa c_j² epsilon²n⁵
       <=336 kappa c_j epsilon n³.                     (15)

This uses c_j epsilon n²<=1. The full dissipator has induced trace norm<=96 kappa epsilon^-2 n; the reference dissipator has norm<=4056 kappa n. Therefore

    ||G(E+K)-(E+K)L_P||_(1->1)
      <=336 kappa c_j epsilon n³
        +59904(kappa²/delta)epsilon n²
        +2530944(kappa²/delta)epsilon³n².               (16)

These are deliberately loose explicit constants, not fitted values. Hamiltonian signs and all cross gains have already been included. No positivity of K is used.

Duhamel between the genuine CPTP full and reference propagators bounds the difference on Hermitian densities by T times (16) plus the two ||K|| endpoints. The rotated bare input differs from E rho0 by at most2||U-I||, and transforming the final state back costs another2||U-I||. Thus the full microscopic process is within C_T epsilon n³ of the exact compressed reference for every P-supported initial density, uniformly in S. No actual-state small-hole estimate was used.

Finally compare the exact reference to (2). By (8), its Hamiltonian discrepancy is at most 4*2048⁶ delta epsilon²n⁶. By (9), its scaled jump p_mu/epsilon differs from B_mu,S by at most c_j epsilon n². Both jumps have norm<=13. The inequality

    ||D[A]-D[B]||_(1->1)<=2(||A||+||B||)||A-B||

bounds the total dissipator discrepancy by 600 kappa c_j epsilon n³. CPTP Duhamel proves (4). No fast-sector absorption estimate has entered.

## 5. Polynomial total-field displacement under the actual rotor target

Set Q_f=1+sum_alllinks |E_e| on the physical rotor P space. This is a weight, distinct from Q=I-P above. The exact K D commutes with Q_f, including all occupation masks after births. The landed pair decomposition gives

    sum_pairs ||delta H4,pair|| <=38880 delta n,
    sum_mu ||sqrt(kappa)B_mu||² <=1728 kappa n.           (17)

Each pair word changes Q_f by at most4; each B changes it by at most2. The bound counts full words and does not truncate a virtual hop.

Here is the operator estimate needed for polynomial, rather than exponential-in-n, moments. If bounded A has integer Q_f bandwidth s, decompose it into the 2s+1 Fourier bands A_d, [Q_f,A_d]=d A_d, ||A_d||<=||A||. Put a=(p-1)/2 for integer p>=1. On an allowed q->q+d transition,

    |(q+d)^p-q^p|/[q(q+d)]^a
       <=p s(1+s)^a,

since both integers are>=1 and their ratio is at most1+s. Thus

    ||Q_f^-a [Q_f^p,A] Q_f^-a||
       <=(2s+1)p s(1+s)^a ||A||.                       (18)

Also ||Q_f^a A Q_f^-a||<=(2s+1)(1+s)^a||A||. Using

    D[B]^*(Q_f^p)=(B†[Q_f^p,B]+[B†,Q_f^p]B)/2

gives its weighted quadratic-form bound by

    (2s+1)² p s(1+s)^(p-1) ||B||² Q_f^(p-1).           (19)

Apply (18)-(19) to the actual target. For p=4, a valid common overcount is

    L_eff^*(Q_f^4)<=C4 n Q_f³,
    C4=162000(38880 delta+1728 kappa).                   (20)

For m4(t)=Tr Q_f^4 rho_eff,infinity(t), Holder gives m3<=m4^(3/4), hence

    m4(t)^(1/4)<=1+(C4/4)n t.                           (21)

The initial value is exactly1 for Omega. No factorization or probabilistic replacement is made.

For domain justification, first compress COMPLETE bounded magnetic and jump words to finite product field boxes, using the actual compressed jump loss B_R†B_R and the same diagonal D. Equations (18)-(20) survive with unchanged constants, so (21) is uniform in the auxiliary box. At each fixed n, remove that box: in the D interaction picture a length-l Dyson density word from Omega has both legs in Q_f<=1+4l and trace norm bounded by (c_n T)^l/l!. This follows from the bounded full magnetic/dissipator norm and the finite field bandwidth; electric conjugation changes phases only. Fixed words stabilize when the box exceeds their full intermediate field excursion. Polynomial weights remain summable against the factorial. Thus the box limit is the actual full rotor target and preserves all required weighted limits. The box is a proof device, not an imposed field preparation or a different limiting dynamics.

The same proof works after any original register is appended, because the register does not change fields and its append maps are CPTP.

## 6. Quantitative spin/rotor comparison without a field-cap hypothesis

Write C_spin=S(S+1). Embed the spin target by setting its bounded H4,S and B_mu,S to zero outside the full physical spin box, and retain the SAME K D on the entire rotor P space. The box reduces this law, so its restriction from Omega is the actual spin target. On each oriented link the normalized spin amplitude is sqrt(1-E(E+k)/C_spin), when its hop is allowed, and zero when blocked. Against the rotor shift, its pointwise amplitude difference obeys

    |spin amplitude-1| <= (|E|+1)²/C_spin.              (22)

For an allowed hop use 1-sqrt(1-x)<=x, 0<=x<=1. At or outside a forbidden boundary the right side is at least1. This proves a Q_f²-relative bound for the elementary weighted shifts, including the boundary rather than deleting it.

A length-r full operator word consists of such shifts and diagonal charge/occupancy/W projections. Telescope its spin/rotor difference, and commute Q_f² through the remaining finite-band words. A finite bound c_r/C_spin results in norm after right multiplication by Q_f^-2. The global box endpoints cause no dimension factor: (I-P_S)Q_f^-2 has norm<=[S(S+1)]^-1, since outside the box Q_f>=S+2. The same estimates hold for adjoints.

All terms in (2) expand into words of length<=4, with at most50000 n⁴ total absolute coefficient weight: the T l1 weight is<=12n and the compensation l1 weight<=48n; M²,Z†Z/2 cost<=31104n⁴, and the remaining two terms cost<=13824n³. Charge and W projections commute with Q_f. Thus for a universal c,

    ||(H4,S-H4,infinity)Q_f^-2|| <=c n⁴/C_spin,
    ||(B_mu,S-B_mu,infinity)Q_f^-2|| <=c/C_spin.         (23)

This intentionally does not assume a local finite-spin H4 cancellation. The rotor H4 locality is used only in its own moment estimate (17). Each B and its adjoint have bounded norm and bandwidth2; therefore all loss differences inherit the same weighted bound. In particular terms such as (B_S-B_infinity)† B_infinity require commuting Q_f² through B_infinity; they are not bounded by a scalar expectation alone.

For any positive rotor density rho with finite m4, Hilbert-Schmidt Cauchy-Schwarz gives

    ||(L_eff,S-L_eff,infinity)rho||_1
       <= c(delta n⁴+kappa n) C_spin^-1 sqrt(m4).       (24)

The common unbounded electric commutator cancels EXACTLY. Duhamel in its common interaction picture is legitimate by the finite-word weighted limit above; alternatively integrate first in finite boxes and take that fixed-volume limit. Both laws are CPTP. Insert (21) into (24) and integrate over0<=s<=T. Since n>=1,

    error <= C_T n⁶/C_spin,

which proves (5). This is an actual target-state displacement moment estimate, not an assumption about microscopic energy or a postselected source field.

## 7. Complete original marked output

Represent any finite original register by a CPTP append map Phi_mu,t on its diagonal classical density algebra. It can retain the original mark label, its chronological order and any prescribed bin containing t; after an overflow it may continue the quantum law with an absorbing register. The generator's gain is

    kappa epsilon^-2 (Ad_Jmu tensor Phi_mu,t),

and its loss is the unchanged anticommutator of J_mu†J_mu tensor I. For each mu the append maps have induced trace norm1. Splitting them into many Kraus operators does NOT multiply the estimates by the number of stored words.

The rotations and X in section4 act on the quantum factor only. A_loss, the Hamiltonian Sylvester equation and K are independent of the register and of time-bin boundaries. Every remainder gain estimate uses only ||Phi_mu,t||=1; every loss is already exact. The reference dissipator bounds remain unchanged. Thus the same corrected Duhamel identity holds for arbitrary piecewise time-dependent append maps, without differentiating a bin label or restarting the corrector at each boundary. No homogeneous-register assumption is being extended across bins. Sections5-6 also retain these append maps and their contraction bounds, proving the joint finite-register versions of (4)-(5), with no count of bins in the constant.

There are at most floor(n/2) ORIGINAL marks in the complete finite-volume trajectory from Omega: Ntot starts at n, Hamiltonians preserve it, each mark raises it by2, and the qutrit carrier has at most2n occupied sites. The same is true for the true targets. This is an exact all-history conservation law, not a chosen global occupation preparation or a truncation. Thus a cap floor(n/2) retains every event. The normal-form rotation and its corrector also preserve Ntot, although the correction itself need not be positive.

One can consequently pass from binned registers to complete timestamps. At each fixed n,S,T, the bounded-jump construction gives trace-class-valued CP densities on the finite disjoint union of original label lists and ordered time simplexes (and an atom for no events), including every coherent original mark. The rotor construction uses its common electric interaction picture; its bounded jumps give the same strong-predual integrals. The sum of their trace integrals is1. No new Poisson process is substituted.

Choose nested finite time partitions. Store every label and its order even when several marks occupy the same bin. Coarse register outputs are integrals of those exact density functions on the resulting simplex cells. For a difference f of the two output densities, the sum of norms of these cell integrals converges to integral||f||_1. To prove this, approximate the Bochner L1 trace-class function by simple functions on the generating rectangle algebra; conditional cell averaging is contractive and fixes the approximants eventually up to arbitrarily small L1 error. There are finitely many lists at each fixed n. This argument is not pointwise comparison of normalized conditional states.

The uniform finite-bin estimate therefore passes to the integrated trace norm of the complete finite-volume timestamp/quantum output. Any forgetting of labels, binning, partial trace, bounded record payoff or final bounded quantum test is a channel/contraction and inherits the same bound. Arbitrarily rare normalized conditional outputs need separate denominator bounds. No globally ordered infinite-volume history is constructed here.

## 8. Explicit joint scaling, failure modes and exact remaining scope

With epsilon=sqrt(delta/K)/sqrt(S(S+1)), (4)-(5) give

    global marked-output error <=C_T[epsilon n³+epsilon² n⁶]. (25)

Take safe even L(S)=2 floor(S^(1/12)/2) once this exceeds64. Then n=L³/2=O(S^(1/4)), epsilon n³=O(S^-1/4), and epsilon²n⁶=O(S^-1/2). This is an explicit joint growing-volume approximation on every fixed finite physical interval. It is not a qualitative subsequence selected after convergence.

The following alternative approaches were considered and not used:

1. Direct global pricing of the local normal form would require controlling gauge changes and backward-test remainders. It is unnecessary for this restricted volume window; no unproved local response norm is smuggled into (25).
2. Summing all excited Riesz cluster errors naively may introduce an extra n factor. The ground-column rotation and exact Sylvester equation avoid that loss, while retaining the canonical ground coefficient.
3. Bounding rotor field moments by Gronwall C n m4 would give exp(C n T) and a much weaker window. The finite-shift commutator lowers the moment degree and proves the polynomial bound (21).
4. Spin/rotor strong convergence alone gives no explicit n window. The full-word boundary-relative estimate (23) is needed; no field cap or unproved energy coercivity replaces it.

The result leaves arbitrary-volume uniform local microscopic approximation open, including sequences with n comparable to or larger than S^(1/3). It does not identify the full microscopic unbounded energy, prove energy uniform integrability, select a natural preparation or clock, change the original coherent marks, derive the supplied quantum law from M2, or close the TOE lane. It also does not prove any proposed fast residence/gap bound: the spectral inverse used here separates W0 from its complement only while the TOTAL perturbation is small.

No high-fanout downstream use is authorized by this author proof alone. A focused independent source-bound check is required. No numerical spectrum, finite-word control, formal review or audit verdict is claimed in this packet.
