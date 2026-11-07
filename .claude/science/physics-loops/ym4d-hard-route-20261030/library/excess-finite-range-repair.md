# Finite-range inverse and the trial chain

Author repair at `0b13f39d269f19602ed3fee11fc146989029a8bb`, OpenAI/gpt-6-astra/max, 2026-11-01. Scope: finding 2 of `../gates/excess-codex-6c0d4e1c9.md`. No numerical computation or independent review. The construction and abelian kernels are those of `../parts/hard-core--excess.md`, Section 2. All distances below are in parent cells, using the infinity norm. Constants called absolute may depend on dimension, SU(2), the fixed comb and spline profiles and fixed weight-rate ceiling, but not on L, position, depth, volume or coupling x. C(L) may additionally depend on L.

## 1. First falsifier and the actual derivative

**Discharged diagnostic.** For the shift (S_R u)(n)=u(n+R) on n>=0, `(I-q S_R)^-1 = sum_{n>=0} q^n S_R^n`. A unit quadratic source mR cells away contributes q^m. Dividing this by q^(2mR) diverges as q decreases to zero for m>=1, R>=1. Thus the old squared flux convolution cannot be inferred from finite range. This is an exact algebraic test, not a numeric run or a counterexample to the lift.

Write B(V)=T_0'(V) for the block-frame construction *before* the fibre correction and

    Psi_V(Y)(c) = log( M B(e^Y V)(c) V(c)^-1 ),    m=Psi_V(0).

Here Y is a left Lie-algebra increment on each parent bond. The following locality bounds are for this map, not an assumed nearest-neighbour matrix. To bound its support, trace its operations: a parent comb G_y reads Pi(y) of radius 5; a tensor kernel reads at most four parent cells in each coordinate; a transition reads the two adjacent combs; phi reads one block's contours; M reads the two endpoint blocks and the joining straight lines. Endpoints can add one cell. Their sum is less than 32. Enlarge to the radius a_0=32 to include the coordinate-strip plaquettes that reconstruct these links. Thus m(c), B on a fine bond, and the entries in a row of D Psi read only a fixed finite set of parent bonds and plaquettes. Using R=2a_0+4=68 is a conservative derivative range; no optimal radius or the old radius six is asserted. On a torus these are cover supports, with occurrences retained before identifying periodic variables.

For completeness, the analytic norm meant by `I+O(C(L)f)` is the **row sum of operator norms of the 3 by 3 real blocks**:

    sum_c' ||D Psi_V(Y)_(c,c') - delta_(c,c') I|| <= B_L (f+||Y||_infinity),
    D Psi_V(Y)_(c,c') - delta_(c,c') I = 0 if d(c,c')>R,                 (FR)
    |m(c)| <= B_L sum_(d(z,c)<=a_0) F(z)^2,    ||m||_infinity <= B_L f^2,

where F(z) is the maximum of the parent plaquette norms at z and f=sup F. B_L has absorbed the finite number of source sites.

**Derivation of (FR), discharged for the construction of Section 2.2.** On the enlarged finite rectangle choose a parent comb gauge. Each link logarithm is bounded by C(L)f: an ordered strip reconstruction expresses its holonomy as finitely many transported plaquette holonomies, and the product-angle bound gives this estimate. The same reconstruction makes all the operations defining B and M finite compositions of products, exponentials and logarithms on a fixed small chart. Their first two derivatives are bounded there by finite constants depending on L; this is a bound in all input link coordinates, including directions not preserving curvature or a gauge slice. At a locally flat connection a gauge on this rectangle makes the connection trivial. At the trivial connection the tensor identities give Q_path T_1=I and T_1 d'=d T_0. Linear transition terms are therefore exact gradients. The contour term in Q is phi(y)-phi(y'), and the block gauge e^-phi removes precisely this term. Consequently `D(M B)=I` on **every parent link increment** at a flat connection. Gauge covariance conjugates this identity by isometries at any locally flat background. Subtracting the flat first derivative, the bounded second derivative and the C(L)f distance in the comb chart give (FR). Differentiating the comb itself costs another finite C(L), not an inverse power of f; it is a finite product of links. Replacing V by e^Y V adds C(L)||Y|| to its local distance and flux. Taylor's formula for the residual, whose constant and linear terms vanish, gives the quadratic bound on m. Summing the finitely many derivative entries gives the row norm stated above. Identifying cover occurrences on a small torus can only decrease this row-sum bound. No global trivialisation is used.

## 2. Inversion on squared flux

**Discharged.** Choose f_0(L) so that on ||Y||<=2B_L f^2 the right side of (FR) is at most q=B'_L f<=q_*<1/4. The map Y-Psi(Y) maps this ball into itself and contracts, since its value at zero is -m. Its fixed point is unique in the ball. The mean value formula gives

    (I+E)Y=-m,    E=int_0^1 (D Psi(tY)-I) dt.

E has range R and absolute row sum at most q. In the Neumann series an entry of E^n is zero at distance greater than nR and has norm at most q^n. Hence

    |(I+E)^-1_(c,c')| <= q^ceil(d(c,c')/R)/(1-q),
    |Y(c)| <= C(L) sum_z k_q(c-z) F(z)^2,
    k_q(z) := q^floor((|z|_infinity-a_0)_+/R).                         (INV)

The second inequality follows by summing over the initial source support of radius a_0; its finite multiplicity goes into C(L). This is a kernel on **squared flux**. Later local curvature operations enlarge a_0 by another fixed radius; below use a=3a_0+2R for all such operations. There is no division by q in making this enlargement. At f=0 the solution is Y=0; define 0^0=1 in the dominating kernels.

The same proof with source v gives the inverse estimate for D Psi(Y) itself at every Y in this ball. Gauge covariance of the solution follows from covariance of Psi and uniqueness of its fixed point. Thus T(V)=B(e^Y V) is an exact parent-gauge-covariant right inverse of M.

Let K_q=k_q/sum_z k_q, now with radius a, be a probability kernel on the cover, and periodise it by summing all lifts on a torus. The normalising factor is between 1 and an absolute constant. For every fixed p>=0 and rate nu_0>=0 choose q_* with q_* exp(nu_0 R)<1. Shells a+nR <= |z| < a+(n+1)R contain at most C(a+(n+1)R+1)^4 sites, so

    sum_z (1+|z|)^p exp(nu_0 |z|) K_q(z) <= M_p,
    sum_z exp(nu |z|) K_q(z) <= exp(C nu),  0<=nu<=nu_0.              (MOM)

The last line uses exp(nu r)-1 <= nu r exp(nu_0 r) and mass one. M_p,C are free of f,L,depth and volume after this choice of q_*. These are cover moments; minimum torus-distance moments are no larger. This avoids a fixed factor greater than one at each level of a weighted iteration.

Define B_y=(K_q*F^2)(y). The local curvature error of the exact lift, including the change V to e^Y V and conversion between neighbouring block frames, is at most C(L)B_y. This follows from (INV), finite support of those operations, and the enlarged a. Constant normalising factors are absorbed in C(L). This replaces every old `Theta-tilde_y^2`; a square root B_y^1/2 is permissible, the old fast convolution is not.

## 3. Weighted T1--T3

**Discharged.** For orientation weights define P_a W(y)=max_(q,|z-y|<=a) W^q(z) and

    W^+(y) = max( P_a W(y), (K_q*P_a W)(y) ).

When a few successive local enlargements occur, enlarge the fixed a once, or take the corresponding finite convolution of K_q. It has the same type of moments. In particular W=1 gives W^+=1 and a scalar log-Lipschitz weight of rate nu gives W^+<=exp(C nu)W. The same holds for orientation weights obtained by compatible down-averaging of one scalar top profile, with the local rate at that level. A spatial Lipschitz bound on each of several unrelated orientation weights alone would not imply this comparison. For arbitrary weights the definition, rather than any Lipschitz comparison, is used. Down-averages retain the definition in Section 1.7 of the part.

Jensen and transposition of the symmetric kernel give, for p>=2,

    B_y^(p/2) <= (K_q*F^p)(y),
    sum W B^(3/2) <= sum W^+ F^3,
    sum W B^2 <= f sum W^+ F^3,
    sum W B^3 <= f^3 sum W^+ F^3.                                  (J)

Also F(y)B_y <= F(y)^3/3+2B_y^(3/2)/3. Fixed local maxima of F or of its gradients cost only the fixed number of neighbouring parents, independent of L. These inequalities prove all the needed nonlinear weighted estimates without putting a fast kernel inside a square.

The tensor bounds (K), with the corrected local error, give

    |theta_p| <= L^-2 (|theta'(y)|+C max_near |grad' theta'|)+C(L)B_y,
    |grad theta_p| <= C_6 L^-3 max_near |grad' theta'|+C(L)B_y.        (T1-r)

The comparison of flat and covariant differences adds a product of two local parent fluxes, already covered by B_y. C_6 and C are absolute. For the variance identity use the constant L^-2 theta'(y) as a trial mean. The leading squared difference sums to an absolute multiple of I^grad(V;W^+); errors give C(L) sum W B^2. The LE remainder is bounded by C(L) times the locally enlarged B; its pairing with theta' is cubic by (J) and Young. This proves

    e(TV;W) <= C_1 I^grad(V;W^+) + C(L)cub(V;W^+).                 (T2-r)

Squaring the second bound in (T1-r) and counting L^4 fine sites per parent gives the absolute coefficient C_2 L^-2. Its squared error is bounded by f cub using (J). Cubing the first bound gives C L^-2 cub plus C(L)f^3 cub. Shrink f_0(L) until C(L)f_0(L)^3<=L^-2. Thus

    I^grad(TV;W^down) <= C_2 L^-2 I^grad(V;W^+) + C(L)f cub(V;W^+),
    cub(TV;W^down) <= C_3 L^-2 cub(V;W^+).                         (T3-r)

C_1,C_2,C_3,C_6 are absolute upper bounds, not the old numerical estimates of near-optimal constants. Enlarging them once does not put any C(L) in front of a leading linear term. No numerical value of L_0 is certified.

## 4. TOP-1, constants and class membership

**Discharged trial estimate; implication for A_k using item (o).** Put x_m=L^(2m) flux(Vtilde_(k-m)), d_m=L^(2m) sup|grad theta(Vtilde_(k-m))|. Since B<=f^2, (T1-r) gives

    d_(m+1) <= (C_6/L)d_m+B_L L^(-2m)x_m^2,
    x_(m+1) <= x_m+C d_m+B_L L^(-2m)x_m^2,    x_0=f, d_0<=2f.

Choose L>=2C_6. Summing the first recurrence bounds sum d_m by 2d_0+2B_L sum L^(-2m)x_m^2. Inserting this in the second and bootstrapping x_m<=C_7 f, with C_7=2(1+4C), closes for a positive f_1(L). Hence flux(Vtilde_(k-m))<=C_7 L^(-2m)f uniformly in depth.

Choose L first so that alpha=C_2/L^2<=1/2 and beta=C_3/L^2<=1/2. Then choose f_1(L)<=f_0(L)/C_7 for the preceding bootstrap, keeping every input to a lift in its domain. For a_m=I^grad(Vtilde_(k-m)), c_m=cub(Vtilde_(k-m)), (T3-r) implies

    c_m<=beta^m c_0,
    sum_(m=0)^k a_m <= 2a_0+C(L)c_0.

Indeed sum a_(m+1)<=alpha sum a_m+C(L)sum f_m c_m; the latter sum is at most C(L)c_0. Sum (T2-r) and telescope the compatible energies:

    E_0(Utilde)-E_k(V) <= 2C_1 I^grad_k(V)+C(L)cub(V).              (TOP-tr)

This is free of x,depth,volume and sector; 2C_1 is absolute. Weighted trial estimates follow with a finite factor exp(C sum_m nu L^-m), using (MOM). No factor is repeated without its scale-dependent nu.

**Which class?** The deterministic, unlabelled kernel is certain only for child flux <=T; the formula domain is D_k={flux<=T_2}, T_2=C_p C_a T. These are distinct. For every input in D_k the trial's levels strictly below k have flux <=T (even T/4 if desired) provided

    T_2<=f_1(L),    C_7 C_p C_a/L^2<=1    (respectively <=1/4).     (CLASS)

The second condition is made in the choice of L when C_p,C_a are the fixed geometric constants of the consumer's threshold convention. If they depend on L, (CLASS) must instead be checked as an inequality; shrinking a_* cannot change their ratio. For inputs with flux<=T, it suffices that L^2>=C_7. The terminal prescribed V need only be in D_k: it is not a child on which a rough label is sampled in constructing its preimage. Thus (CLASS) gives a class chain in exactly the sense needed for the unlabelled fibre comparison, not merely a bound C_7 T at each level.

After L, shrink a_* so T_2=C_p C_a a_*/L^2<=f_1(L) and the existing chart thresholds. This precedes x_* and uses no x. Given item (o)'s identification of the classical branch value with the infimum on such chains, A_k(V)<=A_0(Utilde)<=E_0(Utilde) in the matching Wilson/quadratic normalisation. This is the conditional first inequality of TOP-1. Item (o) remains an imported sketch, not proved by this lift.

## 5. Boundary of this repair

**Gap for TOP-W.** (TOP-tr) is a weighted bound for the *trial*. Minimality at W=1 does not compare weighted energies. Section 3 of the part tries to obtain this from a relative logarithm H between the actual minimum U and Utilde. Theorem F inverts the tangent constrained Hessian at U. Equal nonlinear coarse images give `Q^o H=O(H^2)`, not `Q^o H=0`; and `G in ker Q^o_U` need not be tangent at Utilde. Thus applying that inverse to J(G)=D A(Utilde)[G] requires a quantitative nonlinear fibre chart and its weighted error estimates. Item (o)'s qualitative sketch does not supply them.

The exact missing estimate at that step is, in the consumer's top-scale Eps norm and with a gauge fixing the parent data (eta=L^-n, Utilde^g_b=exp(eta H_b)U_b, H in su(2)),

    sum_B W(B)||H||_Eps(B)^2
      <= C [Yhat_tr(W^+) + sum_B W(B) f_B^4],                      (H-W)

uniformly in n,volume,x and sector, together with a representative/chart for which H represents Utilde relative to U and the nonlinear constraint residual is absorbed. C must be absolute if C_T is to be chosen before L, as in the consumer's constants list. A C(L) estimate suffices only for a correspondingly relabelled C_T(L) and fixed-L geometric rate. F's linear inverse bound alone is not a derivation of (H-W). The further transport comparison of hierarchical frames in Step (3) also remains an explicit condition; the old written C(L)^2 there cannot silently be renamed an absolute C_T.

No claim of impossibility: a weighted nonlinear fibre-chart proof might establish these estimates. This is the first unresolved step in applying the corrected trial to TOP-W. Dependent statements in the part are therefore conditional on this comparison, rather than asserted as consequences of the tail repair.
