# Working derivation: temporal runs before spatial loops

Author working proposal, not yet a checked theorem. The initial target is a physical-time-density and curl-response bound uniform in the time step. It does not by itself identify a Hamiltonian state or establish a compact phase.

## Supplied operator

Use a free spatial three-cube and open time vertices t=0,...,M_t-1 with spacing delta. Spatial lattice spacing is the fixed unit. Let gamma_0,...,gamma_3 be Hermitian4-by-4 Euclidean Clifford matrices and P_mu,+/-=(I+/-gamma_mu)/2. Covariant forward shifts U_mu carry unit U(1) link phases, with zero beyond the open boundary. The finite-clock case is restriction of those phases to roots of unity.

For spatial hopping kappa>0 and mass m>0 put mu=m+3kappa and

    D_delta=D_0-K_s,
    D_0=(mu+delta^-1)I-delta^-1(P_0,+U_0+P_0,-U_0*),
    K_s=kappa sum_(i=1)^3(P_i,+U_i+P_i,-U_i*).

All these are supplied model data. Because the two temporal spin projections are orthogonal, the temporal shift combination has norm at most1. Each spatial axial combination also has norm at most1. Hence ||D_0^-1||<=1/mu and ||K_s||<=3kappa, so the operator trace-log series converges for every m>0, uniformly in delta in its norm ratio. The local absolute loop bound below needs the stronger mu>6kappa, equivalently m>3kappa.

Set M=mu+delta^-1 and x=(1+mu delta)^-1. On the open time interval the inverse is exactly

    R=D_0^-1=sum_(r>=0) w_r[P_0,+U_0^r+P_0,-(U_0*)^r],
    w_r=M^-1 x^r=delta x^(r+1).

Terms beyond the interval vanish. At r=0 the projections sum to I; this is not a double copy of the identity. In the gamma_0 eigenbasis D_0 is triangular in time, so det D_0=M^(4 |Lambda|), independent of gauge links. Work with

    L_delta(theta)=log|det(D_delta D_0^-1)|^2
      =-2 Re sum_(ell>=1) Tr[(R K_s)^ell]/ell.

This is a log of the positive paired determinant. It is not a positive measure on its signed Fourier currents.

## Spin factor and time closure

A word with ell spatial hops consists of ell temporal runs of nonnegative lengths r_j and signs sigma_j, interspersed with spatial projectors P_(i_j),epsilon_j. A closed traced word satisfies spatial closure and

    sum_j sigma_j r_j=0.

Anticommutation of gamma_0 with each gamma_i gives

    ||P_0,sigma P_i,epsilon P_0,tau||=1/2

for either same or opposite temporal signs. By inserting the first rank2 temporal projection at the end of the trace,

    |tr_spin(P_0,sigma1 P_i1,epsilon1 ... P_0,sigmaell P_iell,epsilonell)|
       <=2^(1-ell).

The sum over2^ell temporal sign words cancels the apparent exponential factor2 per run. There are at most6^ell spatial directed words at a given root.

For fixed signs the closure determines r_ell uniquely from the other ell-1 run lengths, when that value is nonnegative. Dropping the remaining boundary and closure restrictions and using sup_r w_r<=delta yields

    sum_(r>=0,time-closed) product_j w_(r_j)
      <=delta mu^(-(ell-1)).

This is the missing time-step factor. Independently summing all ell run lengths would lose it and give an erroneous root density proportional to delta^-1.

## Exponential physical-time and spatial localization

Restrict0<delta<=1/mu. Choose b>0 with

    mu_b=mu-b exp(b/mu)>6kappa.

This is possible whenever mu>6kappa; for example b=(mu-6kappa)/4 works since exp(1/4)<4/3. Since exp(b delta)-1<=b exp(b/mu)delta,

    sum_(r>=0)w_r exp(b delta r)<=1/mu_b,
    sup_(r>=0)w_r exp(b delta r)<=delta.

Let S=delta sum_j r_j. For any alpha>=0 with q=6kappa exp(alpha)/mu_b<1, the absolute coefficient sum rooted at one spacetime vertex, weighted by exp(alpha ell+bS), is at most

    4 delta mu_b sum_(ell>=2) q^ell/ell.             (W.1)

The factor4 includes the paired determinant and the rank2 spin trace. The spatial graph is bipartite, so one-hop loops cannot close; summing all ell>=2 is a harmless enlargement. A nontrivial temporal rectangle already has ell=2 spatial hops, unlike the original unresummed four-edge count. Summing roots converts delta times the number of time vertices into the physical duration. The estimate is independent of spatial volume and time length as a bound per root/time density, not as a bound on the total extensive action.

## Candidate local curl extension

For a closed word rooted at(x_0,t_0), project each spatial hop to time t_0 with a temporal plaquette strip. The remaining spatial closed walk at t_0 can be filled by an integer coordinate contraction toward x_0. All strips and the spatial fill stay inside the visited coordinate bounding box and the open physical box. The spatial fill has plaquette l1 mass at most3ell^2. The temporal strip mass, weighted by delta, is at most ell S. Thus a chosen translation-covariant integer filling n_gamma has physical area

    A_gamma=sum_spatial|n_p|+delta sum_temporal|n_p|
       <=3ell^2+ell S.                              (W.2)

Use physical curl variables F_ij=(C theta)_ij and F_0i=delta^-1(C theta)_0i, and norm ||h||_(p,phys)^p=delta sum_p |h_p|^p, summed over all plaquette orientations. Define the real-source extension of each loop phase by

    Phi_gamma(F)=sum_spatial n_p F_p
                      +delta sum_temporal n_p F_p.

It agrees with its actual Wilson-loop phase when F is the physical curl. Adding integer2pi images to the unscaled plaquette curls changes that phase by an integer multiple of2pi and does not alter the exponential. The off-carrier extension depends on the fixed filling convention.

For a fixed translated shape, Young's convolution inequality gives
||Phi_gamma(h)||_(p,root,phys)<=A_gamma ||h||_(p,plaquette,phys).
Summing translations of the absolute coefficients gives a Hessian Schur bound and, for k=2,3, the candidate derivative estimate

    |D^k L_ext(F)[h_1,...,h_k]|
      <=epsilon_k product_j ||h_j||_(k,phys),        (W.3)

where, with q_b=6kappa/mu_b,

    epsilon_k=4 mu_b 2^(k-1)
       sum_(ell>=2) q_b^ell/ell
        [3^k ell^(2k)+k! b^-k ell^k].               (W.4)

This follows from A^k<=2^(k-1)[3^k ell^(2k)+ell^k S^k] and S^k<=k! b^-k exp(bS), followed by(W.1) at alpha0. The constants are finite and tend to zero as mu->infinity with kappa fixed. The extension remains real because the series takes real parts; it does not require positive individual loop coefficients.

The translation counting and source normalization in(W.2)-(W.4) need a cold proof check. In particular this is a bound in the physical-time weighted norms. Rewriting in counting-norm variables Omega=sqrt(delta)F introduces a delta^-1/2 third-derivative coefficient. That conversion must not be erased when matching a separate Gaussian remainder theorem.

## First temporal rectangle prediction to test

For one positively oriented spatial edge and open times t<t+r delta, the ell2 contribution is predicted to be

    L_2=2kappa^2 sum_(edge,t,r>=1) w_r^2 cos Phi_(edge,t,r),

where Phi is the rectangle holonomy, equal in temporal gauge to theta_i(t)-theta_i(t+r delta) up to an irrelevant sign. At equal times the reverse spatial projectors multiply to zero. The nonzero temporal directions are opposite, with spin trace-1/2. The factor2 above still needs explicit determinant/trace verification.

After subtracting its zero-field constant, the proposed continuum-time limit on a fixed finite duration is

    2kappa^2 sum_edges integral_(0<t<s<T)
         exp[-2mu(s-t)] [cos(integral_t^s F_0i)-1] dt ds.

For a constant temporal curl in the long-time density this becomes

    -kappa^2 F^2/[mu(4mu^2+F^2)],

with small-field quadratic coefficient-kappa^2/(4mu^3). This is only the first spatial-hop contribution. No all-order photon response or charge running is inferred from it.

## Remaining model boundaries

Open time boundaries remove temporal winding/Polyakov terms; antiperiodic finite-temperature time requires a separate treatment. The continuous-time one-particle expression suggested by multiplying the Dirac operator by gamma_0 is gamma_0(mu-K_s), but a Hamiltonian boundary-state/source match has not yet been derived. The paired determinant represents supplied massive fermions and does not include the gapless Weyl problem. Finally the proper spatial Villain Hamiltonian matching is inverse-logarithmic in the time step, so an isotropic compact phase theorem cannot simply consume(W.3).
