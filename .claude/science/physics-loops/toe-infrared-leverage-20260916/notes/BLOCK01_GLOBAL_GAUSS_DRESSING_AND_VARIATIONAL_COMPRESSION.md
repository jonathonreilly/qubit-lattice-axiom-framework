# Global Gauss dressing and its Coulomb variational compression

**Author theorem proposal; personally derived and checked, not independently reviewed or audited.** Supplied-model mathematics, 2026-09-16. This is a variational compression, not a dynamical elimination or a fixed-coupling phase theorem.

## Statement

Let the complete free cubic complex be [0,L]^3, L>=1, with V=(L+1)^3 vertices. Use unit electric/magnetic weights, integer electric rotors, two charge species with m onsite modes, and a supplied Hamiltonian

    calH = (g^2/2) sum_e E_e^2
           + g^(-2) sum_p [1-cos(theta_p)]
           + sum_(e,s)[c_(x,s)^dagger T_(e,s) U_e^s c_(y,s)+adjoint]
           + H_on,
    D E=Q, Q_x=N_(x,+)-N_(x,-), sum_x Q_x=0.

D is tail-minus-head incidence, e=(x,y), s=+1,-1. H_on commutes with each Q_x. Assume ||T_(e,s)||_*<=t_*; the norm is the nuclear norm. The neutral matter space includes every configuration with zero total charge; no local or block neutrality is imposed.

Put C for edge-to-face curl, A=(C*C)^(1/2), K=A^+, Delta0=DD*, and

    eta_e=exp[-g^2 K_ee/4],
    E_var=tr(A)/4+g^(-2)sum_p[1-exp(-g^2 (C K C*)_pp/4)].

There is an explicitly constructed isometry V_g from that entire neutral matter space into the exact Gauss space. For 0<g<=1/10, define

    t=pi^2/(2sqrt(12)g^2), epsilon=8*10^15 exp(-t).

The proposed uniform result is

    V_g* calH V_g = E_var I + H_m(eta_e T_(e,s))
                   +(g^2/2) Q.Delta0^+Q + R,
    ||R|| <= (10+4t_*) V epsilon/g^2.                (1)

H_m here includes the same H_on. All quantities in (1) are finite-volume operators or numbers, and g may remain fixed as L grows. The error is extensive, with a small coefficient. It is not a volume-independent total error.

Also K_ee<=14 and tr Delta0^+<=(7/4)V uniformly. The construction is independent of an arbitrary spanning-tree representative. It does not select this Hamiltonian from the framework axioms.

## 1. Integer topology and the isometry

Let S=ker D=range C*, P its orthogonal projection, Lambda=S intersect Z^E. The cube has no positive-degree real or integer cohomology. Lambda is saturated: if an integer vector multiplied by a nonzero integer belongs to ker D, it already belongs to ker D. Thus Z^E/Lambda is free, every integer functional on Lambda extends to Z^E, and

    Lambda*=P Z^E.

The map Pz -> Cz is bijective onto C Z^E=ker B intersect Z^P, where B is face-to-cube coboundary. Injectivity uses ker C=range D* and S perpendicular to that space. Surjectivity follows by definition; the equality with all integer closed face cochains follows from integer contractibility. The interval product chain homotopy supplies this integer exactness without a division.

For an integer Q with zero sum, choose E0 in Z^E with DE0=Q, for example by routing along a tree. Define

    e_Q=D*Delta0^+ Q, a_Q=P E0=E0-e_Q,
    Z_g(a)=sum_(n in Lambda+a) exp[-g^2 n.K n],
    psi_Q(E)=Z_g(a_Q)^(-1/2)
             exp[-g^2 (E-e_Q).K(E-e_Q)/2], DE=Q.      (2)

Changing E0 changes a_Q by Lambda and only reindexes the sum. K is positive on S, so every sum converges and psi_Q is normalized. It satisfies exact Gauss law. In an occupation basis b, set

    V_g|b>=|b> tensor psi_(Q(b)).                     (3)

Distinct b are orthogonal regardless of their gauge-state overlap; hence (3) is an isometry. The gauge vectors have Gaussian tails and lie in the domain of every electric polynomial on each finite box, so all compressed matrix elements used below are defined.

## 2. Poisson form and the square-root kernel

Poisson summation on the Euclidean space S gives

    Z_g(a)=c_g Theta_g(a),
    Theta_g(a)=sum_(eta in Lambda*)
       exp[-pi^2 eta.A eta/g^2] exp[2pi i eta.a],      (4)

where c_g>0 is independent of a. Let H2=CC*+B*B. Tensoring interval complexes shows H2>0 and ||H2||<=12: every positive-degree tensor component has at least one edge interval Laplacian, whose spectrum is positive, while each coordinate contributes at most four.

For q=Cz, eta=Pz, the singular-value decomposition of C gives

    eta.A eta=q.H2^(-1/2)q.                          (5)

Indeed on range C the eigenvalue of H2 is the square of the corresponding singular value of C, while eta=C*(CC*)^+q. Equation (5) is a square-root Coulomb kernel; substituting H2^-1 would be a different trial state.

We next prove a derivative bound on an extension of log Theta that is uniform over all real a in S, not just a=0.

## 3. Local integer fillings, including free boundaries

A closed integer face cochain splits uniquely into connected closed components under adjacency by a common cube. Every cube closure equation involves mutually adjacent faces, so each support component is itself closed. The adjacency degree is at most ten.

For each connected component gamma, write s=||gamma||_1. There is an odd choice of integer edge filling z_gamma satisfying

    C z_gamma=gamma, ||z_gamma||_infinity<=3s,

supported in a clipped cube of side at most 6s. Here is the boundary argument. Dualize gamma to a relative one-cycle, with dual boundary chains set to zero. Its connected support fits in a clipped cube of side at most s+2. Away from the physical boundary, contract the interval product to a corner; projection to the corner annihilates positive-degree cycles. If it meets boundary faces without an opposite pair, contract along one such normal to that boundary face. Other boundary faces are preserved and the chosen face is zero in the relative complex.

If the support reaches an opposite pair, use the whole physical cube: cubic geometry then implies L<=s+2. In each relative interval let h(v) be the path from the left boundary to an interior vertex v. The identity boundary h=I on vertices gives the projection I-h boundary on edges onto the full interval generator. The tensor homotopy

    H=h_1+P_1 h_2+P_1 P_2 h_3

has the usual degree signs and satisfies boundary H+H boundary=I-P_1 P_2 P_3. The product projection is supported only in degree three, so it vanishes on the one-cycle. Each input cell contributes coefficient at most one to a specified output in each coordinate term, giving the bound 3s. Dualizing back gives the stated loose support bound. More specifically, every filled edge is within s+4<=5s in base-cell distance of each face in the connected carrier; in the opposite-face case the whole cube already has side at most s+2. For a connected cluster the same argument uses its total mass and connected union, retaining that5S anchor radius after summing its fillings. Choosing one filling for each sign pair and negating it makes the rule odd. This argument uses cubic boxes; arbitrary thin rectangles are not included.

For q=sum gamma define z(q)=sum z_gamma. On S,

    z(q).a=eta.a,

because any two fillings differ by an exact edge form, orthogonal to S. Off S this chosen source is an extension and is not claimed independent of the filling convention.

## 4. Positive cluster extension and uniform derivatives

Set c0=1/(2sqrt(12)). Split (5) using a centered face Gaussian phi of covariance

    (H2^(-1/2)-c0 I)/(2g^2)>0.

With t=pi^2 c0/g^2, the theta function on S equals E_phi Xi(C*phi+a). Here Xi(u) is the exact hard-core sum of connected closed-face polymers with activities

    z_gamma(u)=exp[-t||gamma||_2^2] exp[2pi i z_gamma.u].

Polymers are incompatible when their supports meet or share a cube. Component decomposition proves the equality with the full charge sum. Gaussian integration can first be done with finite charge cutoffs; exp(-t||q||^2) supplies absolute convergence for removing them.

For completeness define

    r=exp(-t/2), u_t=2r/(1-r^3),
    R_t=e u_t/(1-100e u_t).

Connected supports of size n containing a fixed face number at most 10^(2(n-1)), by a deterministic tree traversal. Integer nonzero labels at half strength sum to at most u_t^n. Consequently the rooted half-strength sum, with the usual exp(n) weight, is at most R_t. If 11R_t<=1, the sum of half-strength polymers incompatible with gamma, times exp of their support sizes, is at most |supp gamma|.

The hard-core connected coefficient is the alternating sum of connected spanning subgraphs of the incompatibility graph. Its absolute value is bounded by the number of spanning trees: ordering graph edges and applying the greedy spanning-tree algorithm partitions connected graphs into tree-indexed intervals, each with alternating sum of magnitude at most one. The rooted-tree recursion and the preceding incompatibility inequality therefore bound the absolute logarithm-cluster sum containing a fixed face by R_t at half strength.

For a cluster of total integer mass S, restoring full strength supplies exp(-tS/2), even if its net charge cancels. Thus the full-strength absolute mass-S cluster sum rooted at a fixed face is <=R_t exp(-tS/2). All estimates are uniform for real u. Opposite charge clusters conjugate each other. The absolutely convergent connected expansion U(u) obeys Xi(u)=exp U(u)>0, by its power-series identity continued from zero activities to unit activities. No positivity of individual Fourier terms is assumed.

The combined filling z_C has sup norm <=3S and lies in a cube of side <=6S. The loose bounds

    ||z_C||_2^2 <= C0 S^5, C0=15552,
    number of possible root faces within its anchor radius <= C1 S^3,
    C1=10648,

follow by counting edge cells and the radius 5S containing each possible anchor. Differentiating a cluster phase once and twice, then summing anchors, gives

    sup_u ||grad U||_infinity
      <=6pi C1 R_t sum_(S>=1) S^4 exp(-tS/2),
    sup_u ||U''||_(2->2)
      <=4pi^2 C0 C1 R_t sum_(S>=1) S^8 exp(-tS/2).    (6)

For the second inequality use |z_C.h|^2<=C0 S^5 sum_(e in filling box)|h_e|^2 before summing anchors. This proves the operator bound without assuming a local inverse Coulomb projector. Derivatives of any fixed further order exist by reserving more cluster mass, so differentiating finite-dimensional integrals below is legitimate.

For t>=128, R_t<=6r and sum S^j r^S<=2 j! r for j<=8, from the Eulerian generating formula j!r/(1-r)^(j+1). Therefore both quantities in (6) are bounded by

    epsilon0=4*10^15 exp(-t).                         (7)

For example the second prefactor is less than
40*C0*C1*6*2*8!=3,204,911,569,305,600 <4*10^15. These are conservative analytic constants, not fitted phase thresholds. All cluster conditions above hold at t>=128.

## 5. Integrating the auxiliary Gaussian at every real source

The edge variable u=C*phi has covariance

    T=(A-c0 A^2)/(2g^2)

on S and kernel S-perpendicular. It is positive on S and ||T||<=sqrt(12)/(2g^2)=(12/pi^2)t<2t. Define on all real edge a

    F_ext(a)=log E_(u~Gaussian(T)) exp U(u+a).          (8)

It agrees with log Theta_g on S. Each finite volume has a proper positive integral. Under epsilon0||T||<1/2, the negative log density on S has Hessian at least (1-epsilon0||T||)T^-1. The finite-dimensional Brascamp-Lieb variance bound therefore applies on S: Var(h)<=E[grad h.(Hess W)^(-1)grad h] for density proportional to exp(-W). The precise form and hypotheses are in equation(1.3) of [Carlen, Cordero-Erausquin and Lieb (2013)](https://www.numdam.org/article/AIHPB_2013__49_1_1_0.pdf), pages1-2, checked here in an orthonormal coordinate system on S. W is smooth, has a positive Hessian, and has an integrable Gaussian tail; DU[h] is bounded and smooth. This is a mathematical inequality, not a physical-model import. Differentiation gives

    grad F_ext=E grad U,
    F_ext''[h,h]=E U''[h,h]+Var(DU[h]).

The variance is at most ||T|| epsilon0^2 ||h||^2/(1-epsilon0||T||): the S-gradient of DU[h] is P U''h and the covariance metric is bounded by T/(1-epsilon0||T||). Consequently

    ||grad F_ext||_infinity<=epsilon0,
    ||F_ext''||_(2->2)<=2epsilon0=epsilon.             (9)

The singular ambient covariance introduces no problem because the Gaussian and convexity argument live on S. At t>=128 the product 2t epsilon0<1/2; it decreases thereafter. For g<=1/10, t>142>128. This proves (9) uniformly over all L and all real affine sectors. No total theta sum is required to be close to one as volume grows.

## 6. Exact overlaps and electric moments

Write F for the restriction of (8) to S. For a link e, t_e=P e, completion of the square in the electric sum gives

    I_Q(e)=sum_E psi_Q(E) psi_(Q+De)(E+e)
      =eta_e exp[F(a_Q+t_e/2)
                 -F(a_Q)/2-F(a_Q+t_e)/2].           (10)

The exponent has absolute value <=epsilon||t_e||^2/8<=epsilon/8, by (9) and the midpoint remainder. Thus |I_Q(e)-eta_e|<=epsilon/4. The same holds for charge-minus hopping with -e.

For d_p=C*e_p in Lambda, periodicity F(a+d_p)=F(a) gives

    <U(d_p)>_Q=exp[-g^2 d_p.K d_p/4]
              exp[F(a_Q+d_p/2)-F(a_Q)].             (11)

Here ||d_p||^2=4, so the second exponent is bounded by epsilon/2 and the multiplicative discrepancy by epsilon (epsilon<1). Replacing normalized sector overlaps by the centered-sector overlap without (9) would be invalid.

Differentiate Z_g(a) in (2). On S, with n=E-e_Q,

    <n>=-A grad F/(2g^2),
    Cov(n)=A/(2g^2)+A F'' A/(4g^4).                  (12)

Since e_Q.n=0 pointwise, the electric energy is exactly

    (g^2/2)<E^2>_Q
      =(g^2/2)Q.Delta0^+Q+tr(A)/4
        +[tr(A F'' A)+|A grad F|^2]/(8g^2).          (13)

The gradient term is essential; a covariance bound alone does not control it. Use the ambient extension gradient in that term, since A projects to S. Bounds (9), tr A^2=4P_faces, ||A||^2<=12 and E_edges<=3V show the absolute last term is at most

    (V/g^2)[(3/2)epsilon+(9/2)epsilon^2].             (14)

## 7. Whole-matter-space compression

For every matter occupation matrix element of a link hop, (10) multiplies its free CAR matrix element. The charge change is independent of the onsite mode labels, so the difference from eta_e times that hop is the free hop times a diagonal charge function of norm <=epsilon/4. The free hopping operator norm is <=||T_(e,s)||_*, by a singular-value decomposition and the CAR norm of a single mode transfer. Adding adjoints and both species gives total norm error <=3t_* V epsilon.

The onsite operator is exact under (3), since it preserves each charge. Magnetic terms are diagonal in the matter occupation basis; (11) bounds their difference by 3V epsilon/g^2. Combining with (14), g<=1 and epsilon<=1 gives (1), with the deliberately enlarged coefficient 10+4t_*. This is an operator estimate over all neutral matter states, including highly inhomogeneous charges. It is not an expectation estimate limited to a Slater trial.

## 8. Uniform one-link and Coulomb trace bounds

The free Hodge edge Laplacian H1=D*D+C*C has interval tensor eigenvalues

    lambda_n=4 sum_i sin^2(pi n_i/[2(L+1)]).

For an edge in direction i, n_i=1,...,L and the other indices are 0,...,L. Every normalized product eigenfunction has squared magnitude <=8/(L+1)^3. On S, H1^(-1/2)=K, and on the orthogonal gradient space it is positive; hence K<=H1^(-1/2). Since sqrt(lambda_n)>=2|n|/(L+1), group indices by max norm j. A shell has at most 3j^2+3j+1 points, and

    K_ee <=4/(L+1)^2 sum_(j=1)^L (3j^2+3j+1)/j
          <=14 L/(L+1)<=14.                         (15)

For the vertex Laplacian all indices include zero, with only the all-zero mode removed. The same lower eigenvalue bound gives

    tr Delta0^+ <=(L+1)^2/4 sum_(j=1)^L
                         (3j^2+3j+1)/j^2
                 <=(7/4)(L+1)^2 L <=(7/4)V.         (16)

These bounds use three spatial dimensions and free cubes. A lower-dimensional infrared limit requires different estimates.

Two conjugate Slater states with equal fixed particle numbers have equal local mean density, hence mean Q=0. For a real vertex multiplier f and covariance 0<=C<=I, the Slater identity gives Var N(f)=tr[C f(1-C)f]<=tr C f^2<=m||f||^2. The two independent sectors therefore have Cov(Q)<=2m I. From (16), their expected Coulomb energy is <=(7m/4)g^2 V. This is a trial-state energy consequence; it makes no assertion about the actual interacting charge covariance.

## 9. What this establishes and what it leaves

The construction supplies exact Gauss law, a whole-space variational matrix and a charge-uniform compact correction estimate. It keeps g fixed while increasing volume. The nonzero Coulomb term remains at fixed g: increasing the number of sites does not by itself remove microscopic interactions.

The isometry selects one gauge vector per matter configuration. The full Hamiltonian can leave its range and excite transverse photons. Nothing above bounds that off-space action by the exponentially small error in (1). Therefore (1) cannot be substituted for a Feshbach Hamiltonian or used to infer the true ground-state phase, gap, dynamical photon propagation or infrared weakening of the effective charge. A genuine fixed-g result still needs control of that dynamical coupling and of the actual state. This is a new global reference construction, not closure of that residual or an axiom obstruction.

## Personal finite challenges

The separate programs in ../evidence use actual integer cochains and an actual charged ring Hamiltonian. They test the fractional kernel, Poisson normalization, translated moments and normalized hopping overlaps by distinct sums; compare independent free-cube spectra; construct the physical Gauss basis; and compare direct Hamiltonian compression with the exact theta formulas. The ring additionally measures off-space action and the variational energy excess over its actual finite ground energy. It demonstrates why tiny compact compression error does not certify a dynamical elimination.

The analytic theorem uses g<=0.1 and arbitrary free cubes. The finite identity challenges deliberately include larger g, where dropping the affine normalization gives visible errors; they do not certify the theorem by sampling its asymptotic regime. Floating cutoff comparisons are not rigorous tail intervals, and no three-dimensional phase is simulated. All checks are by the author and grant no independent review status.

Proof-method provenance: the current-main carrier and free-cube filling proposals at e0ef7cf4633034a8c1e6d57f5812cc4275bf1349 suggested the cluster argument. The needed d=3, p=2 filling, square-root covariance, affine-source estimate and compression are stated and derived here. The prior charged-rotor draft PR8160 is context, not a theorem input to this construction.
