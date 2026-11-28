# Root rates, local variances and the second-variation sum

Author repair at `0b13f39d269f19602ed3fee11fc146989029a8bb`, OpenAI/gpt-6-astra/max, 2026-11-01. Scope: finding 1 and the variance issue in `../gates/excess-codex-6c0d4e1c9.md`. No numerical computation, independent review or audit. Constants C(L) below may also depend on the explicitly fixed weight rate and input norm bounds, but are free of position, coupling x, depth and torus volume. No assertion here establishes the input regularity of the AN3 curve.

## 1. First tests and the precise conditional statement

**Discharged diagnostic.** If F_y=Ad(R(t))F_z with R spatially constant, then

    Ad(R^-1) Fdot_y = Fdot_z + [Omega,F_z],    Omega=R^-1 Rdot.

Consequently a pure gauge curve stationary at z but moving at y may have Fdot_z=0 and Var(Fdot_y)>0. Discarding Omega is invalid. Neither variance invariance under a fixed rotation nor Stokes in z's rooted gauge bounds this independent relative-root rate by Fdot_z. The proof below retains it and uses link variations. This is an algebraic diagnostic, not a computation on an AN3 curve.

Let s_j=L^(j-k) and d_j(c,b) be distance in **top-cell units** from a level-j site to the fixed top bond b. Fix nu>0 and let kappa be the variation kernel's available rate. To make all weight uses explicit, take 7nu<=kappa/4 and put

    P_j=exp(-nu d_j),    V_j^wt=exp(3nu d_j),    J_j=exp(7nu d_j).

The superscript distinguishes the weight V_j^wt from a connection V_j. Cover neighbourhoods of a fixed number of level-j blocks and compatible down-averages change these weights by bounded factors. These factors are included in the input constants. On a torus use minimum distance and retain cover multiplicities in local sums. A shell count gives `sum_c P_j(c)<=C_nu s_j^-4`, independently of volume. The target weight W_j is a compatible down-average of W_k=exp(g), with g(b)=0 and |grad_top g|<=nu; in particular W_j<=C_nu exp(nu d_j).

Read the old (A1)--(A4) in the following precise form:

- **(A1-r):** `sum P_j |theta_j|^4<=C s_j^4 f^4` and `sum V_j^wt (|delta theta_j|^2+|delta^2 theta_j|^2)<=C_A(L)`, at every level. All fields stay in the fixed small-flux chart. These are curvature and response hypotheses, not a consequence of this lemma.
- **(A2-r):** `sum J_j (|h_j|^4+|h_j^(2)|^4)<=C_A(L)` at every level, in the chain gauge. Because J_j>=1, this also bounds the unweighted suprema of h_j,h_j^(2). The derivative part of A1-r similarly bounds the suprema of its variations.
- **(A3-r):** the absolute second derivative of `E_0(W_0)-E_k(W_k)` is at most C_A(L), with W fixed in time.
- **(A4-r):** for 1<=j<=k, `I^grad_j(V_j;P_j^+)<=C_A(L) qbar^(k-j) B`, with 0<qbar<1 and a volume-independent B. It is enough to use the corrected COMP-g for P and a bounded local top input, which has B<=C_nu(f^2+f^3). This input remains conditional on TOP-W. No fine-level gradient estimate is assumed.

These use only profile rates already allowed by the former A1,A2 if their words “for W=e^g” include both signs and the indicated local enlargements. They explicitly reduce the **output** weight rate to kappa/28. If only one decaying weight is available, the growing response bounds above are additional unproved conditions; weighted l^p nesting cannot replace them. The original unrestricted output at rate kappa/4 is not asserted by this repair.

**Lemma EX2-r (implication).** For the actual chain curve of Section 5.1 of the part, under A1-r--A4-r in the explicit contour-free gauge specified in Section 4,

    sum_(j<k) sum_(y,q) W_(j+1)(y) L^4 Var_(chi_y)(Fdot^j_y) <= C(L),
    sum_(m=0)^k sum_(c at k-m) W_(k-m)(c) sum_e |grad_e delta theta_c|^2 <= C(L).

More explicitly the constant can depend on C_A(L), nu, fixed local geometry and `sqrt(B)/(1-sqrt(qbar))`, and is free of x,depth,volume and b. The root of F^j_y is the chain's frame at y at each t: its comb transport satisfies T_y(y,t)=1 identically. There is no freely chosen time-dependent rotation at that root.

## 2. The local variance estimate missing from A4

**Discharged local lemma.** Let D_y be a coordinate box containing the support of chi_y, the rooted comb paths and the strips between adjacent paths, of diameter C L at level j. For each orientation let F_y(z)=Ad(T_yz)theta(z). Then

    L^4 Var_(chi_y)(F_y)
      <= C(L) [sum_(D_y,e,q) |grad_e theta_q|^2 + n_y^2],
    n_y=sum_(plaquettes in D_y)|theta|^2.                         (VP)

Here and below the finite cover occurrences, not identified transports, are used. To prove it, connect two sites of D_y by coordinate edges. For any vector field A, the telescoping sum and Cauchy--Schwarz give `|A(z)-A(w)|^2<=C L sum_edges_on_path |Delta A|^2`. Apply this to the exact identity `Var_chi A=(1/2)sum_(z,w) chi(z)chi(w)|A(z)-A(w)|^2`. Since D_y has finitely many sites depending only on L, this proves the required box Poincare inequality, with no claim of a sharp coefficient. It is also valid for a probability measure with zero weights at some sites.

The adjacent comb transport differs from T_yz U_e(z) by the holonomy of a loop filled by coordinate strips in D_y. The product-angle inequality bounds its distance from identity by `C(L)n_y^1/2`. Therefore

    |Delta_e F_y(z)| <= |grad_e theta(z)|+C(L)n_y^1/2 |theta(z+e)|.

Squaring and summing proves VP. Finite overlap and local weight comparison then give

    V_j(P):=sum_(y,q) P_(j+1)(y)L^4 Var_(chi_y)(F_y)
        <= C(L) [I^grad_j(V_j;P_j^+) + sum P_j^+ |theta_j|^4].     (VP-W)

This is an upper variance bound from gradients; it does not reverse EX-loc. A4-r gives, for j>=1,

    V_j(P)<=C(L)[qbar^(k-j) B+s_j^4 f^4].

For the single fine endpoint j=0 use Var<=second moment and the mass estimate:

    V_0(P)<=C(L) E_0(P_0^+)
       <=C(L)(sum P_0^+ |theta_0|^4)^(1/2)(sum P_0^+)^(1/2)
       <=C(L,nu) f^2.

Consequently `sum_(j<k) sqrt(V_j(P))<=C(L,nu)[f+sqrt(B)/(1-sqrt(qbar))+f^2]`, with no depth or volume factor. This handles the fine endpoint absent from the hole-filling proof.

## 3. Every root change keeps its rate

**Discharged local lemma.** Fix neighbouring roots y,z and a common enlarged box. Write their transport comparison as

    T_y(w) T_z(w)^-1 = R_yz exp(lambda(w)),    R_yz=T_y(z),
    lambda(z)=0,    |lambda(w)|<=C(L)n^1/2.

The last inequality follows from the coordinate-strip fillings. R_yz is the actual chain transport on the root-to-root comb path, not a separately adjustable frame. Differentiating that finite product of links gives

    |Omega_yz|=|R_yz^-1 Rdot_yz| <= C(L) H_1(y,z),
    H_1(y,z)=sum_(bonds in common box) |h_j|.                     (ROOT)

This retains exactly the constant term excluded by the former proof. In z's rooted axial gauge, the loop exp(lambda(w)) is a finite product of reconstructed links. Strip reconstruction expresses each link in that gauge as an analytic function of the rooted plaquette holonomies, with bounded first derivatives on the small chart. Thus

    |d exp(lambda)/dt| <= C(L) N_d^1/2,
    N_d=sum_(common box) |Fdot_z|^2.

After conjugating by the spatially constant R_yz, differentiation gives

    Ad(R_yz^-1)Fdot_y = Fdot_z+[Omega_yz,F_z]+error,
    ||error||_(L^2(chi)) <= C(L)[(n N_d)^1/2+|Omega_yz| n].        (FC)

Here the three errors are respectively `(Ad(exp lambda)-I)Fdot_z`, the derivative of exp(lambda) acting on F_z, and `[Omega,(Ad(exp lambda)-I)F_z]`. This proves the displayed bound directly. In particular

    sigma(Fdot_y) <= sigma(Fdot_z)+2|Omega_yz|sigma(F_z)
                         +C(L)[(n N_d)^1/2+|Omega_yz|n].

One must not remove the second term. Small-chart n is bounded by a fixed C(L); its squared errors are bounded by `C(L)(n N_d+H_1^2 n)`.

The weighted root contribution is summable using A2, not a curvature-only rate bound:

    sum_y W(y)L^4 |Omega_yz|^2 <|F_z|^2>_chi
       <= C(L) sum_y W(y) H_1(y,z)^2 n_y
       <= C(L)(sum V^wt H_1^4)^(1/2)(sum P n_y^2)^(1/2)
       <= C(L) s_j^2 f^2.                                      (ROOT-W)

The middle inequality is valid because `W<=C(P V^wt)^1/2`; finite overlap gives `sum P n_y^2<=C(L)sum P^+|theta_j|^4`. The fourth moment of a finite path sum is bounded by path length cubed times the sum of fourth powers, so A2-r supplies the other factor. There are only finitely many frame comparisons per parent and `sum_(j<k)s_j^2<=1/(L^2-1)`. Coarse-root contour comparisons use s_(j+1), whose sum is still bounded by `1/(1-L^-2)`. Thus *each* kind of root change is paid, with C(L) and no depth loss.

## 4. Differentiating the variance identity in consistent frames

Fix the explicit chart choice in `block-poincare-energy-package.md`, Theorem 7 Step 1: N_j(V)=g^[j](V).M_j(V), where g_y^[j](V)=exp(-Phi_y^[j] X), X=log(V V_j(0)^-1), and Phi^[j] is frozen at the base point. The definition N^(n)=N_(n-1) composed with ... composed with N_0 gives V_(j+1)=g^[j](V_j).M(V_j) exactly. Thus C_j(y,t)=g^[j](V_j(t))^-1 is a one-level contour conversion. In the identity V_W use

    theta'_y=Ad(C_j(y,t)) theta_(j+1)(y,t).

F^j_y itself is rooted in the level-j chain frame with T_y(y,t)=1. This separates the root convention from the parent contour conversion. The rate of C_j, and its second derivative, are bounded by C(L) times finite path sums of h_j and of h_j^(2),h_j^2, respectively: Phi is a finite linear contour functional with orthogonal base transports, and differentiating exp(Phi X) on the small chart gives these bounds. In particular it is **not** an accumulated rotation from the top of the chain. Its differentiated theta' obeys the same bounds used below, with another C(L). This proves the needed one-level relation and rate bounds for that chart choice; A1-r,A2-r must refer to its curve, not to an unspecified gauge with arbitrary higher time derivatives.

Put alpha=T^-1 Tdot, beta=alpha-dot. Then exactly

    Fdot=Ad(T)(delta theta+[alpha,theta]),
    Fddot=Ad(T)(delta^2 theta+2[alpha,delta theta]
                              +[beta,theta]+[alpha,[alpha,theta]]).

For the fixed local paths, `|alpha|<=C(L)H_1` and `|beta|<=C(L)H_2`, where H_2 is the sum of |h^(2)|+|h|^2. A1-r,A2-r imply

    sum_y V^wt(y)L^4 <|Fdot|^2+|Fddot|^2>_chi <= C(L),            (G)

and the same with local unweighted sums replacing averages. Here are the nontrivial products, with weights shown: `sum V^wt H_2^2 |theta|^2` for the h^(2) term is bounded by `(sum J |h^(2)|^4)^(1/2)(sum P|theta|^4)^(1/2)`, since `(V^wt)^2/P=J`. The h^2 term is handled in the same way after using the unweighted sup of h, supplied by J>=1. `sum V^wt H_1^2 |delta theta|^2` is bounded by sup H_1^2 times the A1-r second moment. The same reasoning bounds the double commutator. It also bounds sup |Fdot|, sup |Fddot|, and hence all local N_d,N_dd moments of order at least one with weight V^wt. This avoids the invalid rule l^4(W)<=l^2(W) for an arbitrary decaying W.

Let R_y=2<theta'_y,r_y>-|r_y|^2. With weights fixed in time, the exact telescoping identity gives

    2 sum_j sum_y W L^4 Var(Fdot)
       = Yddot-2 sum_j sum_y W L^4 Cov(F,Fddot)+sum_j sum_y W Rddot. (D-r)

For the covariance use W^2/P<=C V^wt, VP-W and G:

    |sum_y W L^4 Cov(F,Fddot)| <= C sqrt(V_j(P)).

Its sum is bounded by Section 2, including j=0. No assertion that A4 itself bounds a variance is used.

For the remainder, in the rooted axial gauge r=Phi(a), with Phi(0)=D Phi(0)=0 and bounded first two derivatives on the local chart. The strip reconstruction gives

    |a|<=C(L)n^1/2,   |adot|<=C(L)N_d^1/2,
    |addot|<=C(L)(N_dd^1/2+N_d),
    |rdot|<=C(L)(n N_d)^1/2,
    |rddot|<=C(L)(N_d+(n N_dd)^1/2+n^1/2 N_d).

Use the **full** expression

    Rddot=2<theta'ddot,r>+4<theta'dot,rdot>+2<theta',rddot>
                                      -2|rdot|^2-2<r,rddot>.

Finite overlap gives `||n^1/2||_(l^4(P))<=C(L)s_j f`. All N_d,N_dd moments needed below are bounded with V^wt by G and the sup bounds. Holder therefore bounds the five groups by sums of

    C(L)s_j^2 f^2,   C(L)s_j f,   C(L)s_(j+1) f,
    C(L)s_j s_(j+1)f^2,   C(L)s_j^2 f^2.

For example theta'ddot n uses l^2(V^wt) and l^2(P); theta'dot sqrt(n N_d) uses l^4(V^wt), l^4(P), l^2(V^wt); theta' N_d uses l^4(P), l^(4/3)(V^wt); and theta' sqrt(n N_dd) uses l^4(P), l^4(P), l^2(V^wt). In each case the product of weight powers dominates W: the smallest exponent is (-nu/4-nu/4+3nu/2)=nu. Higher powers of n are harmless by its small-chart sup bound. Thus

    sum_j |sum_y W Rddot_y| <= C(L) sum_(j<k) s_(j+1) f <= C(L).

A3-r and D-r now prove the first assertion of EX2-r.

## 5. From differentiated variances to gradients

Differentiate TL in one common rooted box. Its linear identities become the same fixed linear functionals on Fdot. Derivatives of its analytic quadratic errors are bounded by `C(L)(n+Theta^2)^1/2 N_d^1/2` in that box. Use FC, including ROOT-W, to change each of the finitely many variance frames back to its own root. The additional errors have squares bounded by `C(L)(n N_d+H_1^2 n)` and their coarse counterparts. Their weighted sums are <=C(L)s_(j+1)^2 f^2: for n N_d use l^2(P) and l^2(V^wt), and for H_1^2 n use ROOT-W.

Finally return from a flat difference in that common gauge to the **covariant difference of delta theta in the chain gauge at t=0**. There are two kinds of error: a connection/transport angle O(C(L)n^1/2) times delta theta, and a transport or contour rate O(C(L)H_1) times theta. The first has weighted square bounded by the same l^4 pairings and sup/second-moment bounds above; the second is exactly ROOT-W, with the corresponding coarse or fine h. None of these rates is discarded on the grounds of gauge invariance. Therefore

    b_(k-j-1)(W) <= C(L) sum_y W L^4 Var(Fdot^j_y)
                                   +C(L)s_(j+1)^2 f^2,  j<k.

The fine b_k is a single term, bounded by C times the weighted l^2 norm of delta theta_0 by the shift triangle inequality and local weight comparison. Summing proves the second assertion of EX2-r. The proof is conditional on A1-r--A4-r in this fixed contour chart and on the stated small-flux domain; its constants are not absolute in L. It establishes summability, **not** a pointwise geometric estimate for b_m or for second derivatives of a composed source.

## 6. What remains for the consumers

The frame and variance defects themselves are repaired at the level of this conditional proof. The unresolved inputs are the stated response estimates for the AN3 curve and, for A4-r via COMP-g, the weighted comparison (H-W), (HC-W) in `excess-finite-range-repair.md`. Growing response weights at rate 7nu and the output-rate restriction are part of the statement, not tacit consequences of one decaying weighted norm.

For the older second-variation route to DS, Cauchy--Schwarz now bounds `sum_m sqrt(b_m b'_m)`; root/transport terms have a factor s_m f and are also summable. This does not give a per-m geometric rate or the full mixed-bond tree norm without its own weighted mixed-variation/source estimate. The pinned `library/sector-values.md` uses a different DS proof through FALL, CRUDE and LAN, explicitly not this lemma. Repairing EX2 does not certify that newer proof.
