# Independent check: cost of a particle-relative flat environment

Reviewed `/tmp/environment_cost_derivation.md` against `NATIVE_DRESSED_PATCH_PROOF.md` and `EXTENDED_ENVIRONMENT_PROOF.md`. The coefficient inequality and the stated radius upper exponent are supported, with the spectral-support and dressing qualifications below. No repository files were changed.

## Exact coefficient geometry

Take a nonwrapping m by m square S of logical column sites on the transverse torus, m>=3 and R>m+2. There are 2m(m-1) internal edges and (m-1)^2 internal plaquettes. Exactly 4m edges cross its boundary. The plaquettes intersecting S have lower-left coordinates in an (m+1) by (m+1) set; subtracting internal plaquettes gives 4m boundary-crossing plaquettes. Thus for K=-5 sum E-4 sum P, the omitted boundary operator satisfies ||B||<=5(4m)+4(4m)=36m.

For any internal horizontal edge, select an internal plaquette meeting exactly one endpoint: if the edge starts before the last internal x coordinate, choose the plaquette extending beyond its right endpoint; otherwise choose one extending beyond its left endpoint. Choose an available internal y side, including at the square boundary. The vertical-edge argument is the rotated version. m>=3 is essential; the analogous assertion fails for a 2 by 2 square. Thus every internal edge anticommutes with some internal plaquette and Q_S E Q_S=0. I independently enumerated the coordinates for m=3,...,8; both boundary counts and all anticommutations passed.

On the all-positive internal-flux subspace, K_S has compressed value -4(m-1)^2. The all-X product trial has expectation -10m(m-1), so e_S<=-10m(m-1) and the flat-subspace cost above e_S is at least D_m=6m^2-2m-4. This does not require identifying the ground state of the open square.

Write K=K_S+K_out+B. Product ground states of the disjoint S/outside Hamiltonians imply e<=e_S+e_out+||B||. Every state has outside expectation at least e_out. Combining upper and lower boundary errors gives the stated 2||B||<=72m penalty, regardless of entanglement across the boundary.

## Approximate flatness and conditional states

For epsilon=tr rho(1-Q_S), Cauchy-Schwarz bounds the two off-diagonal blocks of E by 2sqrt(epsilon(1-epsilon)); the complementary diagonal block is bounded by epsilon. Since Q_S E Q_S=0 and ||E||=1, the looser bound used in the draft, |<E>|<=2sqrt(epsilon)+epsilon, is valid. The plaquette lower bound does not require approximate flatness. Therefore

<K>-e >=6m^2-2m-4-72m
 -10m(m-1)[2sqrt(epsilon)+epsilon].

For a background-valued position state, I tensor K is diagonal in the particle position label. Apply the same inequality to the normalized conditional background density at each position, using the translated square, and average. Concavity of sqrt gives precisely the claimed replacement by the mean failure probability epsilon. Zero-probability positions can be omitted. This works for mixed states and arbitrary position-background entanglement; it assumes neither classical signs nor a factorized environment.

## Transfer to the actual heavy states

The required state premise is support in the actual isolated two-wall spectral cluster with energy within O(J lambda^(5/2)) of its bottom. A small mean energy without that spectral-support premise does not justify projection to N=2. Apply the established equivariant SW map and N=2 projection before defining the relative patch event. As the cited proof explains, projected energy control uses the approximate eigenvalue equation and bounded cluster width, not a bare global-H norm times state error.

In the exactly odd physical-Z sector the half block is absent. Otherwise the earlier O(lambda^(3/2)) bound on half weight permits conditional normalization to the singleton block. More explicitly, Hb-Eb is nonnegative and both kinetic blocks are bounded below by -4J lambda for sufficiently small lambda (the half bound is -6J lambda^2). Thus the total weighted expectation of Hb-Eb is O(J lambda^(5/2)); dividing its singleton contribution by a probability tending to one preserves that order. One must not use the singleton D2 identity on the half block itself.

With Hb=c(lambda,R)I+J lambda^4 K/128+E_rem and ||E_rem||=O(J lambda^5 R^2), R~lambda^-1, its minimum differs from c+J lambda^4 e/128 by O(J lambda^3). Hence the conditional singleton state satisfies

<K>-e <= C lambda^(-3/2)+O(lambda^(-1)).

This estimate includes the two appearances of the background remainder and the previously controlled heavy projection errors. The bounded patch projector transfers back to the actual state without an m^2 multiplier. It is an SW-dressed measurement, not an identification with the undressed microscopic local projector.

## Radius consequence and limits

If the particle-relative m-square is all-flat with probability 1-epsilon and epsilon=o(1), the coefficient of m^2 in the lower bound tends to six and is positive for sufficiently small lambda. Combining the two inequalities yields m^2=O(lambda^(-3/2))+O(m), and therefore m=O(lambda^(-3/4)). In particular m~lambda^-q with q>3/4 and epsilon tending to zero is excluded within the stated box regime.

This bounds a high-probability *jointly* flat patch radius. It does not locate a domain wall, give a lower radius at this exponent, or constrain center-of-mass extent. The previously derived joint-flat lower scales q<3/8 and this upper exponent 3/4 are different bounds with a gap between them, not a radius selection. No clustering, gap inside K, empirical source identification, or new interaction is needed for the coefficient cost inequality.
