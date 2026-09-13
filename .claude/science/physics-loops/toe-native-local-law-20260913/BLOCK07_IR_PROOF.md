# Uniform native stress logarithm

Working proof for the real symmetric frequency-even response R5 in
BLOCK07_DERIVATION.md. Fix zeta<1; constants need not be uniform at node
merger. A and B range over a bounded subset of real symmetric matrices.
Take the thermodynamic momentum integral first. Let K=(omega,Dq) and
kappa=|K|. The proposed theorem is

    chi_AB(K)=c_AB+d_AB omega^2+e_AB,ij Q_i Q_j
              -kappa^4 log(1/kappa) T_AB(Khat)/(80 pi^2 v)
              +O(kappa^4),                              (U1)

where T_AB is the four-dimensional transverse-traceless contraction R8.
The local coefficients are the actual native integral's constant and
second derivatives, which exist. This theorem does not assert they have
Einstein values or symmetry. The remainder is uniform over all K directions,
including Q=0 and omega=0. Changing the fixed logarithm scale changes only
the O(kappa^4) term.

## 1. Smooth annulus family with derivative bounds

Choose disjoint ellipsoidal neighborhoods of the two simple zeros. Write
the centered internal momentum there as k=k_w+D^-1 r n, |n|=1. At shifted
momenta and for Q=r eta,

    d(k+/-q/2)/r=R_w(n+/-eta/2)+r b_+/-(r,n,eta),
    u_A(k,q)/r=R_w A n+r a_A(r,n,eta).                   (U2)

The functions b and a extend smoothly, in fact analytically in the radial
parameter, to r=0. This follows by Taylor's integral formula for the finite
trigonometric d and V; their values and first derivatives at the zeros are
the explicit ones in R1's source specification. On |eta|<=1/4 the two
normalized energy norms are bounded below uniformly. Set omega=r xi.

The full R5 integrand, including its minus sign, is therefore r times a
smooth function G(r,n,eta,xi) on the compact set
0<=r<=delta, n in S2, |eta|+|xi|<=1/4. All derivatives needed through order
five in eta,xi, and one additional r derivative, are bounded. At r=0 this
is exactly the linear-cone family. Consequently its m-th external derivative
is bounded by C_m r^(1-m), and its fourth derivative differs from the linear
cone derivative by at most C r^-2. This argument controls all external
directions at once; it does not divide by |Q|.

For r>=8 kappa, Taylor expansion in the external K gives the terms of degree
zero, two and four, with remainder bounded by C kappa^5/r^4. Odd total
degrees vanish: the integrand is even under q->-q and separately under
omega->-omega. This also excludes omega*Q mixed quadratic terms. The native
fourth Taylor term differs from the cone fourth term by C kappa^4/r^2.
After multiplying by r^2 dr both errors integrate to O(kappa^4):

    kappa^5 int_(8kappa)^delta r^-2 dr=O(kappa^4),
    kappa^4 int_(8kappa)^delta 1 dr=O(kappa^4).             (U3)

The cone fourth term has radial dependence r^-3, so its integral supplies
log(delta/(8 kappa)). Its angular polynomial is exactly R6--R7. Restoring
both nodes and the Jacobian 1/v gives R8's coefficient.

## 2. The inner region and lower Taylor coefficients

For sufficiently small neighborhoods, the simple-zero property gives
E_-+E_+ >= c (r+|Q|), including near either shifted zero. The vertices are
bounded by C(r+|Q|). Projectors have norm one almost everywhere, hence

    |Delta J_AB/(Delta^2+omega^2)| <= C (r+|Q|).            (U4)

Undefined projectors exactly at a zero affect a null set. In r<8 kappa the
integral is O(kappa^4), uniformly also when Q=0. The zero-order integrand at
K=0 is O(r); the second external derivatives are O(r^-1) by U2. Their
integrals exist, and their omitted inner-ball contributions, multiplied by
their external Taylor monomials, are respectively O(kappa^4) and
kappa^2 O(kappa^2). They may therefore be extended to the full node balls.
This defines c,d,e in U1 by the native integrals, without fitting them.

## 3. Complement of the nodes and the limit order

On the fixed complement, both shifted energies stay uniformly away from
zero for small K, so the integrand is smooth with bounded derivatives.
Its constant and quadratic terms join the node terms; its fourth term and
remainder are O(kappa^4). Smooth radial partitions can be used instead of
hard balls. The difference lies in a fixed gapped annulus and is analytic
to the needed order, leaving the logarithmic coefficient unchanged.

Finite-volume Kato response tends to the stated integral on any sequence
of compatible gapped momentum grids whose mesh tends to zero. Away from
the finitely many shifted zeros this is ordinary Riemann convergence. Near
them, U4 bounds the possible contribution by the volume times a bounded
continuous envelope; the values at an exactly zero mode may instead be
excluded by a boundary twist. The theorem is about the integral followed
by K->0, and does not assert interchange with a finite-grid infrared limit.

## 4. Lapse mixing and actual limits of the conclusion

A first-order lapse adds sigma.[d_-+d_+]/2 to the vertex. Its node value and
first jet are the same as A=I in U2. Replacing A by A+n I therefore proves
the same logarithm for the seven lapse/strain sources, including mixed terms.
The nonlinear specified lapse law changes contact terms, which are local
for finite-range source couplings; these have no logarithm at quadratic
order. A time-dependent full spacetime frame may also need a temporal spin
connection. This note addresses the real symmetric even-frequency kernel;
it does not identify the parity-odd response or silently assume those
additional geometric contacts vanish.

The four-dimensional projector is an exact tensor statement about this
leading nonanalytic term. It does not make the full lattice Hessian
transverse, remove its local elastic terms, establish full nonlinear
diffeomorphism invariance, or derive the Einstein two-derivative coefficient.
