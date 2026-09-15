# Matching the mixed coefficient to the original free-box source

Personal proof candidate,2026-09-15. This closes a specific boundary
identification left open in the preceding all-component calculation. It
does not prove convergence of the complete activity expansion. The result
is an ITERATED limit of a derivative at zero activity, not a Gaussian
limit of the physical clock law at activity1. Independent review is pending.

## 1. The exact finite-volume quantity

Let Lambda_L be centered, increasing free four-dimensional cubic complexes.
All cells, including boundary cells, have the counting inner product. Put

    D_L=d_1,L, B_L=d_2,L,
    P_L=D_L H_1,L^-1 D_L*, Q_L=B_L* H_3,L^-1 B_L=I_L-P_L.

Write g=N/sqrt(beta), b=2pi sqrt(beta), c=g b=2pi N. For a conserved
integer electric current j and a closed integer magnetic three-form q,
let c_e(j),c_m(q) count connected nonzero support components. The support
graphs join edges at a vertex, or three-cells at a four-cell, respectively.
These counts include multiplicities within one component in its values,
not as extra components. Set c_e(0)=c_m(0)=0.

Choose a component-additive integer magnetic filling n(q), B_L n(q)=q.
The exact source sum from the physical clock-comb/unfolding identity is

    Z_L(h;lambda_e,lambda_m)
      =sum_(j,q) lambda_e^c_e(j) lambda_m^c_m(q)
         exp[-g^2<j,H_1,L^-1 j>/2-b^2<q,H_3,L^-1 q>/2]
         exp[i c<n(q),D_L H_1,L^-1 j>]
         exp[-g<D_L H_1,L^-1 j,h>-i b<Q_L n(q),h>].     (1.1)

At lambda_e=lambda_m=1 the normalized physical characteristic function is

    E exp(i<h,X_L>)=exp[-<h,P_L h>/2] Z_L(h;1,1)/Z_L(0;1,1),
    X_L=sqrt(beta)(D_L theta-2pi k).

For each fixed finite L and h, the Gaussian self-energies make all integer
sums absolutely convergent. Component counts are bounded by the numbers
of cells, so Z_L is a polynomial in the two activities, with convergent
coefficients. Also Z_L(h;0,0)=1. Thus its analytic logarithm is defined in
some neighborhood of(0,0). No volume-uniform neighborhood is claimed.
Nor is(1.1) asserted to be a positive probability family at arbitrary
activities; the intermediate electric-magnetic weights are complex.

Define the source-normalized log coefficient

    T_L(h)=partial_lambda_e partial_lambda_m
       [log Z_L(h;lambda_e,lambda_m)-log Z_L(0;lambda_e,lambda_m)]_(0,0).
                                                               (1.2)

There is no division by volume in(1.2). This is the coefficient of the
logarithm of a generating function, not the ordinary pressure density.
Opposite orientations give exactly

    T_L(h)=4 int [cos(theta)-1][cosh(U)cos(V)-1] dnu_e,L dnu_m,L
             -4 int sin(theta)sinh(U)sin(V) dnu_e,L dnu_m,L,
    theta=c<n,P_L S>, U=g<S,P_L h>, V=b<n,Q_L h>.        (1.3)

Here nu_e,L,nu_m,L are the marked component measures from the preceding
note: both orientations have weight1/2, marks have normalized weight, and
self-activities are included in the measures. The factor4 in(1.3) is the
orientation sum, not an additional activity. The two species have no mutual
hard core. The same-species hard core does not enter this mixed coefficient.

## 2. Strong convergence of the actual free-boundary projections

Extend a finite two-form by zero to the full lattice. In this paragraph
P_L means the resulting orthogonal projection on the infinite ell^2 space,
and I_L is the projection onto the cells of Lambda_L. Then

    P_L -> P,  Q_L=I_L-P_L -> Q=I-P STRONGLY on ell^2.  (2.1)

Proof. First let f have finite support. The vectors u_L=P_L f have norm
at most||f||. Every subsequence has a weakly convergent subsubsequence.
For any fixed compact three-form a and one-form v, all relevant cells are
eventually interior, so the finite Hodge identities give

    <d_2* a,u_L>=0,
    <d_1 v,u_L-f>=0.

Every weak limit u consequently satisfies d_2 u=0 and d_1*(u-f)=0 on the
full lattice. At every nonzero Fourier momentum, these identities uniquely
give uhat(k)=P(k)fhat(k). The zero momentum has measure zero, and there
is no nonzero harmonic ell^2 two-form on Z^4. Thus u=Pf. Uniqueness of all
weak subsequential limits gives u_L weakly convergent to Pf.

Because P_L is an orthogonal projection even after extension by zero,

    ||u_L||^2=<f,u_L> -> <f,Pf>=||Pf||^2.

Weak convergence plus norm convergence gives strong convergence. Density
of compactly supported forms and||P_L||<=1 extend the conclusion to all
ell^2 sources. Since I_L tends strongly to I, the assertion for Q_L follows.
This proof does not replace a free kernel by a Dirichlet kernel, differentiate
a Green-function asymptotic, or presume convergence of its absolute row sum.
The finite zero extension itself need not be globally closed; only the
identities against eventually interior test forms are used.

In particular, for a fixed finite component fill S or n,

    ||P_L S||^2 -> ||PS||^2,  ||Q_L n||^2 -> ||Qn||^2,
    <n,P_L S> -> <n,PS>.                                (2.2)

## 3. Uniform component moments at the boundary

Use the same infinite-lattice filling rule whenever a component's local
bounding box is interior. Near the physical boundary, use the relative
cubical contraction from the free-filling note at PR8133 revision
f8e7219b5e79bcb271bb3c1df635ecdeeb57dbe8. Its proposed integer homotopy
supplies support in a clipped cube of side at most6m and coefficient
norm at most4m, for component mass m. The proof contracts onto a boundary
face when only non-opposite boundary faces are met; if opposite faces are
met, m controls the whole cubic side, and the product relative interval
homotopy applies. This finite-boundary filling premise remains provisional.

It is unnecessary to infer the infinite-lattice4m^2 mass bound at a free
boundary. The stated support and coefficient bounds give the looser bound

    ||fill||_1 <= A m^5, A=24*7^4=57624.               (3.1)

Indeed there are at most6(6m+1)^4 two-cells, each of magnitude at most4m.
The infinite4m^2 bound is also covered by(3.1). Choose the rules odd and
average their384 signed-cubic pushforwards as normalized marks. For a fixed
bulk component these marks stabilize to the chosen infinite-lattice marks.

The degree14 connected-support count remains valid up to the boundary:
at mass m and a specified component cell, there are at most2*393^(m-1)
integer components. A component whose fill meets a fixed two-cell can be
anchored in at most C_anchor m^4 cells, C_anchor=4*25^4. The previous
radius12m bound covers the clipped boxes and dual-cell offsets.
H_p,L<=16I gives the same half-weight estimates

    sqrt(w_e,L)<=exp[-t_e m], t_e=g^2/64,
    sqrt(w_m,L)<=exp[-t_m m], t_m=pi^2 beta/16.

Consequently the half-weight anchored moments obey, uniformly in L,

    M_L^(1/2)(r)
      <=[2 C_anchor A^r/393] sum_(m>=1)
                    m^(5r+4)[393 exp(-t)]^m.           (3.2)

The same series restricted to m>M bounds the mass tail and tends to0 as
M tends to infinity. All these moments are finite under

    beta>=16, N^2/beta>=512.                            (3.3)

These are coefficient bounds, not a proof of a phase throughout(3.3).

For any fixed finite list of bulk components, their fillings eventually
stabilize and(2.2) gives convergence of their weights. The uniform moment
tails control components meeting a fixed finite set with arbitrarily large
mass, including components whose boundary remains far away. This is the
local convergence property of the measures used below.

## 4. Continuous cosine functionals and bounded operators

For either species write, with its current finite or infinite measure,

    F_L(z)=int [cos(c<s,z>)-1] dnu_L(s),
    H_L(z,y)=int [cos(c<s,z>)-1] cos(b<s,y>) dnu_L(s).

The constant b here is just the displayed fixed source frequency. Uniform
moments and Holder give

    |F_L(z)-F_L(z')|
      <=c^2 M_L(2)(||z||_2+||z'||_2)||z-z'||_2/2.      (4.1)

The same bound controls changes of z in H_L. Changes in y obey

    |H_L(z,y)-H_L(z,y')|
      <=b c^2 M_L(3)||z||_3^2||y-y'||_3/2.             (4.2)

This follows by bounding the three factors of a rank-one form and using
the anchored third-moment Holder inequality. For compact z,y, only fills
meeting the support of z contribute. Local convergence and(3.2) therefore
give convergence of F_L and H_L. Equations(4.1)-(4.2), with||z||_3<=||z||_2,
extend it to strongly convergent ell^2 arguments.

Put x_L=P_L h,y_L=Q_L h for a fixed compact h. They converge strongly to
x=Ph,y=Qh. Define continuous scalar functions at their removable zeros:

    alpha(U)=(cosh U-1)/U^2, alpha(0)=1/2,
    eta(V)=(cos V-1)/V^2, eta(0)=-1/2,
    A_e(U)=sinh U/U, A_e(0)=1,
    A_m(V)=sin V/V, A_m(0)=1.

The source-energy bound remains valid in each finite box:

    w_e,L exp(|U|)<=exp(||h||_2^2) sqrt(w_e,L).         (4.3)

Let C=cos(theta)-1 and R=sin(theta)-theta. Define

    E_L^h=int S tensor S alpha(U) cos(V) C dnu_e,L dnu_m,L,
    M_L^h=int n tensor n eta(V) C dnu_e,L dnu_m,L,
    R_L^h=int S tensor n A_e(U) A_m(V) R dnu_e,L dnu_m,L.

The Schur estimates in the preceding coefficient note and(4.3) give
volume-uniform operator bounds, for||h||_2<=H:

    ||E_L^h|| <=exp(H^2)c^2 M_m,L(2) M_e,L^(1/2)(4)/4,
    ||M_L^h|| <=c^2 M_e,L(2) M_m,L(4)/4,
    ||R_L^h|| <=exp(H^2)c^3 M_e,L^(1/2)(4) M_m,L(4)/6. (4.4)

For fixed matrix indices i,j, the E_L^h entry has an outer fill meeting
i,j. Its inner magnetic integral is H_m,L(P_L S,y_L), which converges
by(2.1),(4.1)-(4.2). The outer coefficient converges by(2.2), and its
mass tail is controlled by the half-weight fourth moment. The M_L^h entry
uses F_e,L(P_L n) and the same argument. For R_L^h, both fills meet fixed
indices. The estimate

    |R|<=c^3||S||_1^3||n||_1^3/6

and(4.3) give a product of anchored fourth-moment majorants. Pointwise
convergence of every fixed component pair and its phase then gives entrywise
convergence. Uniform operator bounds extend this entrywise convergence to
weak operator convergence of all three matrices. Strong convergence of
x_L,y_L is sufficient when these operators are inserted in scalar products;
strong convergence of the coefficient operators is not assumed.

## 5. The signed linear kernel also converges

Set

    J_e,L(x_L)=int S sinh(g<S,x_L>) dnu_e,L,
    J_m,L(y_L)=int n sin(b<n,y_L>) dnu_m,L.

These vectors converge strongly in ell^2 to their infinite-lattice versions.
Here is a direct truncation argument. Restrict first to component mass m<=M.
Carriers then have uniformly bounded mass and support radius. The restricted
map is uniformly Lipschitz on bounded ell^2 sets, by a bounded rank-one
Hessian. For a compact argument, local convergence gives convergence in a
fixed finite coordinate neighborhood. Approximation by compact arguments
therefore gives strong convergence for x_L->x and y_L->y at this fixed M.

The omitted electric tail is at most, in ell^2 norm,

    g exp(H^2) M_e,L^(1/2)(2;m>M)||x_L||_2,

by |sinh U|<=|U|exp(|U|),(4.3), and the absolute-frame Schur bound.
The magnetic tail is bounded by b M_m,L(2;m>M)||y_L||_2. Equation(3.2)
makes both tails tend to0 uniformly in L. This proves the stated strong
convergence, without an absolute row estimate for P_L.

Using sin(theta)=c<n,P_L S>+R, equation(1.3) becomes exactly

    T_L(h)=4g^2<x_L,E_L^h x_L>+4b^2<y_L,M_L^h y_L>
       -4c<J_e,L(x_L),P_L J_m,L(y_L)>
       -4g b<x_L,R_L^h y_L>.                           (5.1)

All terms have limits by sections2,4,5. The limit equals the signed
infinite-lattice definition in the preceding note. In particular this
identifies its prescribed conditional summation with the actual exhaustion
through these finite free cubic boxes:

    lim_(L->infinity) T_L(h)=T_infinity(h)              (5.2)

for every compact real h under(3.3). This does not assert independence of
arbitrary orders of conditionally convergent component cutoffs.

## 6. The iterated macroscopic limit and the remaining gap

For smooth compactly supported continuum two-forms f, take
h_a(p)=a^2 f(a midpoint(p)). At each fixed a this has finite support.
Combining(5.2) with the arbitrary-component coefficient theorem gives

    lim_(a->0) lim_(L->infinity) T_L(h_a)
       =2g^2 a_e||P_cont f||_2^2-2b^2 a_m||Q_cont f||_2^2, (6.1)

where a_e,a_m are the finite negative diagonal constants specified there.
The inner limit is taken before the macroscopic scaling limit. No uniform
rate in a is obtained here, so an arbitrary simultaneous choice L=L(a)
with aL(a)->infinity is not silently substituted into(6.1).

This is a proposed exact identification of one activity coefficient for
the original source. It uses the provisional free-boundary filling lemma
and the preceding all-component bounds, all still awaiting independent
review. No nonzero activity radius uniform in L, exchange of an infinite
activity series with scaling, or evaluation at physical activities1 is
proved. Those remain the actual all-order/phase problem.
