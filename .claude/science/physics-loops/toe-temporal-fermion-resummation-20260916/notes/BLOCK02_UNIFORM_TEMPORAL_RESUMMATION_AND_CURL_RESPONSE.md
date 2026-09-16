# Temporal Wilson resummation with physical curl bounds uniform in time step

Author theorem proposal, 2026-09-16. Current surface status `conditional-support`; no independent review or audit. The model is a supplied paired massive Wilson determinant on a free spatial cube times an open time interval. The result addresses the temporal-run resummation left open in main's compact determinant/current note. It is not a compact-gauge phase theorem or a derived native matter law.

## 1. Model and statement

Spatial lattice spacing is the unit. Let Lambda_s be any finite free cubic box in Z^3, and let the time vertices be0,...,M_t-1, separated by delta>0. Write Lambda for their product and T_delta=delta M_t. Boundary shifts are zero outside the box. Let gamma_mu be Hermitian4-by-4 Euclidean Clifford matrices, and P_mu,+/-=(I+/-gamma_mu)/2. The covariant forward shifts U_mu have unit complex phases and otherwise the usual oriented nearest-neighbor entries. Finite cyclic links are the restriction to Nth roots of unity, with no lower bound on N required for this estimate.

Supply kappa>0 and m>3kappa, and put mu=m+3kappa>6kappa. Set

    D=D_0-K_s,
    D_0=(mu+delta^-1)I-delta^-1(P_0,+U_0+P_0,-U_0*),
    K_s=kappa sum_(i=1)^3(P_i,+U_i+P_i,-U_i*),
    L_delta(theta)=log|det(D D_0^-1)|^2.              (1)

Fix b>0 such that mu_b=mu-b exp(b/mu)>6kappa, and assume0<delta<=1/mu. One permitted choice is b=(mu-6kappa)/4. Define q_b=6kappa/mu_b<1.

There is a real local-loop extension L_ext(F) of(1) from physical plaquette curls to arbitrary real plaquette variables, where temporal curls are divided by delta and spatial curls are not. It has bounds independent of the number of spatial sites, the number of time slices and delta:

    |L_delta| <= 4 T_delta |Lambda_s| mu_b
                         sum_(ell>=2)q_b^ell/ell,   (2)

and, for k=2,3,

    |D^k L_ext(F)[h_1,...,h_k]|
       <=epsilon_k product_j ||h_j||_(k,phys),       (3)
    ||h||_(p,phys)^p=delta sum_plaquettes |h_p|^p,

with an explicit finite sufficient constant

    epsilon_k=4 mu_b 2^(k-1) sum_(ell>=2)q_b^ell/ell
          [3^k ell^(2k)+k! b^-k ell^k].              (4)

The Hessian also has an entrywise Schur envelope in this physical metric with norm at most epsilon_2. Derivatives are controlled for all real F, including off the physical curl carrier. For fixed kappa, the constants in(4) tend to zero as mu->infinity. Section7 records a sharper heavy-mass order. The extension is defined by a chosen local filling convention; only its values on physical curls are canonical.

## 2. Exact temporal inverse and determinant normalization

Let M=mu+delta^-1 and x=(1+mu delta)^-1. Orthogonality of P_0,+ and P_0,- gives

    R=D_0^-1=sum_(r>=0)w_r[P_0,+U_0^r+P_0,-(U_0*)^r],
    w_r=M^-1 x^r=delta x^(r+1).                     (5)

The sum is finite on the open time interval. At r=0 the two terms sum to M^-1 I. Each temporal spin sector is triangular in time, so det D_0=M^(4|Lambda|), independently of the temporal gauge links.

The temporal shift combination has norm at most1, since its two spin blocks are U_0 and U_0*. Thus ||R||<=1/mu. Each spatial axial combination has the same norm bound and ||K_s||<=3kappa. It follows that ||R K_s||<=3kappa/mu<1. The finite-matrix logarithm therefore gives exactly

    L_delta=-2 Re sum_(ell>=1)Tr[(R K_s)^ell]/ell.    (6)

The operator norm argument in fact only requires m>0. It establishes the identity, not yet the local absolute estimates used below. No choice of logarithm of a possibly signed determinant is needed: twice the real part gives the logarithm of its squared modulus.

## 3. The spin gain and the closed-time gain

Expand each factor R in(6) into temporal runs and each K_s into directed spatial hops. A traced word has ell spatial steps, ell temporal signs sigma_j and ell lengths r_j>=0. Its spatial walk is closed and

    sum_j sigma_j r_j=0.                            (7)

The gauge coefficient is a unit-modulus Wilson-loop phase. Its remaining spin trace contains alternating P_0,sigma and P_i,epsilon. Anticommutation of gamma_0 and gamma_i gives, for every choice of signs,

    ||P_0,sigma P_i,epsilon P_0,tau||=1/2.           (8)

For equal temporal signs, the sandwich is P_0,sigma/2. For unequal signs it is epsilon P_0,sigma gamma_i P_0,tau/2, whose nonzero singular values are1/2 because gamma_i is a unitary map between the two temporal spin subspaces. Inserting the initial rank2 projection at the end of the trace proves the bound2^(1-ell) on its absolute value.

There are2^ell temporal sign words. Their number cancels the corresponding factor in the spin estimate. At each root there are at most6^ell directed spatial words. The zero-length temporal-run representations are included in this count; they sum algebraically to the identity and are not discarded.

For fixed signs, equation(7) determines r_ell from r_1,...,r_(ell-1), if the determined value is a nonnegative integer. Dropping that last admissibility condition and all boundary conditions only enlarges an absolute sum. Since

    sum_(r>=0)w_r=1/mu,  sup_r w_r<=delta,

the sum of temporal weights of closed words is at most delta mu^(-(ell-1)). This factor delta is essential. Counting all ell temporal runs independently would lose it.

For the exponential weight S=delta sum_j r_j, the condition delta<=1/mu gives

    sum_(r>=0)w_r exp(b delta r)
      =delta/[1+mu delta-exp(b delta)]<=1/mu_b,
    sup_(r>=0)w_r exp(b delta r)<=delta.             (9)

Indeed exp(b delta)-1<=b exp(b/mu)delta<mu delta. Combining(6)-(9) yields, for every root z and alpha>=0 such that q=6kappa exp(alpha)/mu_b<1,

    sum_(words rooted at z)|a_gamma| exp(alpha ell+bS)
          <=4delta mu_b sum_(ell>=2)q^ell/ell.       (10)

Here a_gamma is the coefficient before the unit loop phase, including the paired-determinant factor and1/ell. One spatial hop cannot close. The estimate does not assert that coefficients are positive. Summing roots proves(2). Since alpha can be chosen strictly positive, the loop expansion is exponentially localized in spatial length and physical temporal length, uniformly in delta.

## 4. A boundary-compatible physical-area filling

Treat a loop word as an integer1-cycle in the rectangular spacetime cell complex, based at(x_0,t_0). Project it to the spatial slice at t_0. Each spatial hop at time t_j is connected to its projected hop by a temporal plaquette strip. The boundary of the sum of strips is the original cycle minus its spatial projection: vertical edges cancel at consecutive endpoints, including repeated visits. Equivalently this is the interval chain homotopy between the identity and projection to t_0. The sum of strip lengths, weighted by delta, is at most

    sum_(spatial hops j)|t_j-t_0|<=ell S.            (11)

All those strips remain between visited times and inside the physical time interval.

The projected closed spatial walk has length at most ell and lies in a coordinate box of side at most ell containing x_0. Contract that box to x_0 one coordinate at a time. The integer prism chain homotopy sends each input edge through at most3ell plaquettes: each of the three coordinate displacements is at most ell, and degenerate parallel prisms contribute zero. Applied to the ell-edge cycle it produces an integer spatial2-chain with boundary that cycle and l1 norm at most3ell^2. The contraction stays in the coordinate box, so it remains inside any free spatial cube containing the original path.

Combining the spatial fill and strips gives n_gamma with boundary equal to the loop and

    A_gamma=sum_spatial|n_gamma,p|
                +delta sum_temporal|n_gamma,p|
       <=3ell^2+ell S.                              (12)

Choose this coordinate order once. The rule commutes with allowed lattice translations; full rotation symmetry is not needed for the bound. It is an integer rule, so

    Phi_gamma(F)=sum_spatial n_gamma,p F_p
                       +delta sum_temporal n_gamma,p F_p       (13)

equals the actual link phase when F_ij=(Ctheta)_ij and F_0i=delta^-1(Ctheta)_0i. Adding2pi integer images to the unscaled curls does not change exp(iPhi). Thus the same extension can be evaluated on Villain image fields with these physical-time conventions. It neither changes their probability law nor makes a signed current expansion positive.

## 5. Uniform derivative bounds and the metric factors

Define L_ext by replacing each loop phase in(6) by exp[iPhi_gamma(F)] and keeping the real part. Absolute convergence follows from(10). For a fixed word shape translated over roots, Phi is a finite convolution from orientation-indexed plaquette fields to scalar root fields. Its kernel l1 norm is A_gamma, including the factor delta on temporal plaquettes. Extending the finite-box field by zero and allowing all root translations, Young's inequality gives

    ||Phi_gamma(h)||_(p,root,phys)
      <=A_gamma ||h||_(p,plaquette,phys).            (14)

The restriction to roots for which the loop and its fill lie in the box only decreases an absolute sum. Since all root coefficients for a fixed shape are translates with the same magnitude, Holder's inequality and(14) give

    sum_roots |a_gamma| product_(j=1)^k|Phi_gamma(h_j)|
      <=delta^-1 |a_gamma| A_gamma^k
                                    product_j||h_j||_(k,phys). (15)

The delta^-1 in this formula converts the counting root sum to the physical-time measure. It is cancelled by the closed-time factor delta in(10), rather than omitted.

Now A^k<=2^(k-1)[3^k ell^(2k)+ell^k S^k] and S^k<=k! b^-k exp(bS). Applying(10) at alpha0 proves(3)-(4). All differentiated phases have modulus1 for real F; this is why the bounds are uniform over the full real extension. Weighted absolute convergence of the derivative series justifies termwise differentiation and gives C^k regularity for each finite k by the same argument.

The Hessian envelope can also be written entrywise. Let c_gamma,p be the coefficient of F_p in(13), and sum

    B_(p,q)=sum_(shapes,roots)|a_gamma| |c_gamma,p c_gamma,q|.

For each p, translation counting gives sum_q B_(p,q)<=sum_shapes |a_gamma| A_gamma^2<=delta epsilon_2. Symmetry gives the same column bound. Therefore delta^-1 B is a Schur envelope of norm at most epsilon_2 for the Hessian in the physical metric. This is stronger than an estimate of a single finite-direction derivative.

No norm conversion is implicit. If Omega=sqrt(delta)F is instead used with the counting ellp norm, the Hessian bound stays epsilon_2, while the third derivative coefficient becomes epsilon_3 delta^-1/2. A later anisotropic Gaussian argument must match these source and measure conventions explicitly.

## 6. Exact leading temporal rectangle and its limit

At ell2 the spatial word traverses one edge and returns. If both temporal runs have zero length, the two reverse spatial projectors multiply to zero. Otherwise their lengths agree and their temporal signs are opposite. The spin trace is

    tr(P_0,sigma P_i,epsilon P_0,-sigma P_i,-epsilon)=-1/2.

Counting the two edge directions and the two time orderings in(6) gives exactly

    L_2(theta)=2kappa^2 sum_(positive spatial edges e)
                    sum_(t,r>=1, t+r<M_t) w_r^2 cos Phi_(e,t,r). (16)

The finite matrix program checks this coefficient and sign by direct traces of(RK_s)^2, independently of the rectangle sum.

For a smooth temporal field history and fixed duration, w_r^2=delta^2(1+mu delta)^(-2r-2). Riemann sums, dominated by an integrable exponential on the finite time triangle, give after subtracting the zero-field constant

    L_2(F)-L_2(0) ->2kappa^2 sum_e integral_(0<t<s<T)
        exp[-2mu(s-t)] [cos(integral_t^s F_0i)-1] dt ds.         (17)

The assertion is for bounded continuous physical curl histories on each edge; the rectangle phase is their integral. It does not infer convergence for arbitrary time-dependent lattice gauge samples from smoothness of an unrelated field.

For a constant curl F and then the large-duration density, dominated integration gives

    lim_(T->infinity)(L_2(F)-L_2(0))/T
       =-kappa^2 F^2/[mu(4mu^2+F^2)].               (18)

Its quadratic coefficient is-kappa^2/(4mu^3). This is a finite response of the leading spatial-hop contribution. It is not an all-order charge-renormalization formula or a photon pole.

## 7. Optional sharper heavy-mass order

For ell2 the projected spatial cycle cancels exactly. Its fill is the single temporal rectangle, whose physical area is S/2. Odd spatial lengths cannot close on the free cubic graph. Consequently the following improved constant can replace(4):

    epsilon_k^sharp=4mu_b [ (q_b^2/2) k!/(2^k b^k)
      +2^(k-1) sum_(even ell>=4)q_b^ell/ell
                   (3^k ell^(2k)+k!b^-k ell^k) ].   (19)

The proof uses exactly the same weighted absolute sum, retaining these two geometric facts. With b=(mu-6kappa)/4 and fixed kappa, (19) gives epsilon_2^sharp=O(mu^-3), and epsilon_3^sharp=O(mu^-3). The latter order allows the spatial plaquette contribution at ell4. No optimized numerical mass threshold is asserted.

## 8. Scope and remaining joins

This closes a supplied-model uniform-time estimate under an explicit heavy-mass condition. It supplies an extensive action-density bound and an absolute local curl extension; neither implies nonnegative Fourier currents or an independently verified phase. The bounds apply pointwise to both continuous and finite-cyclic gauge links before any gauge averaging.

Open time boundaries are essential to the exact triangular normalization and to the absence of winding loops. Antiperiodic finite-temperature time requires a separate winding analysis. The formal continuous-time one-particle expression gamma_0(mu-K_s) is Hermitian, but a fermionic boundary-state/transfer/source identification remains to be derived. The inverse-logarithmic spatial Villain matching of the previous campaign also remains distinct from an isotropic fixed-beta phase theorem. Gapless matter, a fixed-payload photon phase, native-law selection and any axiom-forcing contradiction are not established.
