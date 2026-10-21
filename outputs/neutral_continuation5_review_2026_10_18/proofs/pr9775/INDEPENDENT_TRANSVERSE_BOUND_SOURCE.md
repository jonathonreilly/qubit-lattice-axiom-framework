<!-- Original PR9775 source SHA256 60170168589f255903d8733316db61813d727ee9e5fd81be2a50da2f58340065. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# Independent transverse-momentum T-junction check

The stated leading N=4 coefficient construction, normalized bound state, and first nonzero original-source overlap are consistent. This is an exact leading K1 fiber result, not a full microscopic pole theorem.

## Native fiber geometry

For two spins in one longitudinal layer, either spin can hop transversely. In a normalized unordered-pair/even-relative-coordinate representation, the two translations contribute phases exp(+/-iQ_a/2), giving relative hopping -2cos(Q_a/2). The origin is excluded because the two spins cannot occupy the same site. For an adjacent-column interval, changing either longitudinal endpoint likewise gives -2cos(Q_z/2) on the x-oriented ray. The y-oriented ray has the opposite native YY sign; a length-alternating gauge makes its hopping negative without changing its length-one root.

At Q=(0,pi,0), these values are horizontal hopping -2, vertical hopping zero, and ray hopping of magnitude2. The inversion-even y=+/-1 host rows combine into one full horizontal chain rooted at |y>=(|ey>+|-ey>)/sqrt(2), with a third semi-infinite lead supplied by the adjacent-y interval ray. All three root-to-lead links have magnitude2; there is no sqrt(2) enhancement because the orientation/root basis and each inversion-paired lead state are normalized consistently.

The y=0 host, with the origin removed, becomes a half-line in the inversion-even space. Joining its x-adjacent root to the x interval ray gives a full chain. Other nonzero-y rows are free horizontal chains. Nonadjacent longer intervals remain frozen at K1. Thus the complete K1 continuum lies in [-4,4], with frozen eigenvalue0, while the y junction may have discrete eigenvalues outside it.

## Exact junction eigenstate

Gauge all three junction leads to hopping -2. Write root amplitude v0 and the amplitude on lead n>=1 as v0 r^n. The bulk equation gives E=-2(r+r^-1), while the root gives E=-6r. Hence r=1/sqrt(2) and E=-3sqrt(2). Normalization is

1=v0^2[1+3 sum_(n>=1)r^(2n)]=4v0^2,

so v0=1/2. This lies strictly below -4 by 3sqrt(2)-4. The positive partner is obtained by bipartite staggering. The lower mode is an isolated simple state in this inversion-even coefficient fiber.

## Original readout normalization and exact darkness

For C_Q normalized per physical volume, the first dressed pair source receives the sum of the two column phases. The same native energy denominator that gave the zero-momentum source yields

j_Q=-lambda[a|x>-b|y>],
a=cos(Qx/2), b=cos(Qy/2),

at Qz=0. At a=b=1 this equals the previously checked -sqrt(2)lambda d. At a=1,b=0 the source lies solely in the disjoint x-chain component, whereas the bound state lies in the y junction. Its leading-source overlap is exactly zero at this momentum.

## Small-b overlap coefficient

Hold a=1 and perturb b away from zero. The y-row bound-state amplitude at horizontal coordinate +/-n is v0 r^n. Vertical host hopping -2b couples each of these to the x-row state at separation n; the two inversion-related row contributions give the source -4b v0 r^n for n>=1. There is no direct b-dependent ray hopping.

Use coordinate j=n-1>=0 on the host side of the full x chain, with its root at j=0 and the interval-ray continuation at j<0. At E=-3sqrt(2), the full-chain Green kernel from the root is

G_(0,j)=-r^|j|/sqrt(2).

The first-order root amplitude is therefore

v_x=sum_(j>=0) G_(0,j)[-4b v0 r^(j+1)]
   =(4b v0 r/sqrt(2))/(1-r^2)=4b v0.

The perturbation maps the unperturbed junction state out of its component, so its first energy shift and its first-order y-root amplitude correction vanish; v_y=v0+O(b^2). Combining the altered eigenvector with the altered original source gives

<bound_b|j_Q>=-lambda[4b v0-b v0]+O(lambda b^2)
            =-3lambda b/2+O(lambda b^2),

up to the arbitrary eigenvector sign. The leading squared overlap is 9lambda^2 b^2/4. Both the state-mixing term and the explicit source term are necessary; keeping only one gives the wrong coefficient.

The perturbation is bounded in operator norm, so the isolated K1 eigenvalue persists for a sufficiently small real b neighborhood by standard isolated-spectrum perturbation theory. This supports the expansion within the coefficient model; it does not require fitting a dispersion. No assertion about a large b interval or the full native higher-order spectrum is made here. Higher dressed-source terms can matter when b is taken to zero together with lambda, so the displayed leading source scaling must retain its order-of-limits qualification.

## Scope

This is constructive: the complete leading compact K1 fiber has an isolated bound state, and the actual specified readout couples to its continuation at nearby momenta. It is not a selected scalar field, an empirical detector bridge, or proof of a microscopic isolated line after higher wall sectors and higher coefficients are restored. The exact symmetry-point darkness remains a useful distinction from the nearby nonzero overlap.
