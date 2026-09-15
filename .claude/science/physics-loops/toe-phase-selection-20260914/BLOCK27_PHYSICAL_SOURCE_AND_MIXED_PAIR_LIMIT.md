# Physical source matching and the first mixed-defect coefficient

Personal proof development,2026-09-15. This is a finite-order component
expansion result being checked, NOT convergence of the complete expansion,
a fixed-clock Gaussian theorem, or an independently reviewed claim.

## 1. The full physical characteristic source in the coupled representation

On a contractible free cubic complex, let D=d_1,B=d_2, G_j=H_j^-1,
P=D G_1 D*, Q=B*G_3 B=I-P. For integer conserved electric a and closed
magnetic q, choose the same integer filling n(q) as PR8133. Set

    p_a=N D G_1 a,       y_q=B*G_3 q=Q n(q).

The source-free coupled weight at revision
f8e7219b5e79bcb271bb3c1df635ecdeeb57dbe8 is

    W(a,q)=exp[-||p_a||^2/(2beta)-2pi^2 beta||y_q||^2]
             exp[2pi i N<n(q),D G_1a>].

For the physical lifted field X=sqrt(beta)(D theta-2pi k), the exact
characteristic identity in the same variables is

    E exp(i<h,X>)
      =exp[-<h,Ph>/2]
         {sum_{a,q} W(a,q)
               exp[-<p_a,h>/sqrt(beta)-2pi i sqrt(beta)<y_q,h>]
          \over sum_{a,q} W(a,q)}.                        (1.1)

One direct derivation inserts the clock comb sum_a exp(iN<a,theta>)
before unfolding the Haar link integral. Write theta=t+2pi G_1D*n(q)
in the non-flat directions. Then the lifted flux is D t-2pi Q n(q),
the comb contributes the displayed positive-sign mixed phase, and the
Gaussian t integral with exponent i<N a+sqrt(beta)D*h,t> gives

    -||p_a||^2/(2beta)-<p_a,h>/sqrt(beta)-<h,Ph>/2.

The remaining magnetic source has the minus sign in(1.1). Flat gauge
directions enforce conservation; all normalizing constants cancel.
Gaussian decay makes the finite-dimensional sums with any fixed h
absolutely convergent. Changing both a and q to their negatives reverses
both source signs and gives the same characteristic function, but reversing
only one source sign while keeping W fixed generally changes it.

Thus the component sources used in the parity probe are

    s_e=i u_j(h),  u_j(h)=N<d_1G_1j,h>/sqrt(beta),
    s_m=-v_q(h),   v_q(h)=2pi sqrt(beta)<Q n(q),h>.        (1.2)

These are respectively imaginary and real. They are not two arbitrary real
character sources and the coupled terms are still not a positive joint law.

## 2. Exact first mixed coefficient for two component shapes

For one electric component and one magnetic component let their self-
activities be z,w, their mixed phase be theta, and abbreviate u=u_j(h),
v=v_q(h). The coefficient of zw in the logarithm of the normalized source
sum in(1.1) is exactly

    4[(cos(theta)-1)(cosh(u)cos(v)-1)
          -sin(theta)sinh(u)sin(v)].                    (2.1)

It follows by substituting(1.2) into the four-sign sum and subtracting the
source-free coefficient. The quadratic part is

    2(cos(theta)-1)(u^2-v^2)-4sin(theta)u v.             (2.2)

The single-electric coefficient is2(cosh(u)-1), and the single-magnetic
coefficient is2(cos(v)-1). This sign check is consistent with the electric
sector reducing the exact covariance and the magnetic sector adding a
coexact fluctuation to the Haar Gaussian part. It is a coefficient check,
not a sign theorem for the fully interacting covariance.

## 3. Translation-invariant elementary-loop coefficient

Now define a precise infinite-lattice coefficient using all translates and
orientations of the elementary electric loop j_p=D*e_p and magnetic loop
q_p=B e_p. Here P,Q are the bounded infinite-volume Hodge projections.
Their self-activities are constants

    z_0=exp[-N^2/(4beta)],   w_0=exp[-pi^2 beta],

because P(p,p)=Q(p,p)=1/2. Introduce separate formal multipliers lambda_e,
lambda_m for THESE elementary components. The calculation concerns their
mixed coefficient. It neither claims they are the unique least-energy
charges nor replaces the full charge gas by elementary loops.

Write c=2pi N, g=N/sqrt(beta), b=2pi sqrt(beta), and define real kernels

    C(p,p')=cos[c P(p,p')]-1,
    S(p,p')=sin[c P(p,p')],
    R(p,p')=S(p,p')-c P(p,p').

Projection gives sum_{p'}|P(p,p')|^2=1/2 and |P(p,p')|<=1/2. Hence

    sup_p sum_{p'} |C(p,p')|<=c^2/4,
    sup_p sum_{p'} |R(p,p')|<=c^3/24.                   (3.1)

The same bounds hold for columns. C,R are absolutely summable matrix
convolutions, while S=cP+R is a bounded signed operator. Set

    A_N=sum_{p'} C(p,p').

Cubic symmetry makes this independent of p, including its orientation;
symmetry of P makes the column sum the same. It is finite and nonpositive.
It is strictly negative for N>=1: equality would require every N P(p,p')
to be an integer. Since a square-summable row tends to zero, that would
make the row finitely supported, contrary to its noncontinuous Fourier
multiplier. Thus -pi^2 N^2<=A_N<0.

For a real two-form test h, put U=gPh, V=bQh. The summed quadratic
coefficient from(2.2), including the self-activities, is

    z_0 w_0 {2 A_N [g^2||Ph||^2-b^2||Qh||^2]
                  -4 g b <Ph,S Qh>}.                  (3.2)

The non-absolutely-summable part of the mixed term cancels EXACTLY in the
physical source:

    <Ph,c P Qh>=0,
    <Ph,S Qh>=<Ph,R Qh>.                               (3.3)

This is the source match that the general component-source calculation
alone could not supply. It is not valid for arbitrary independent sources.

## 4. The remaining mixed quadratic term vanishes on macroscopic tests

Use plaquette midpoint coordinates when taking Fourier transforms. The
absolutely summable kernel R has a continuous Fourier matrix Rhat(k).
Signed coordinate reflections act diagonally on the six two-form
orientations at k=0. For two distinct orientations, a reflection flips
exactly one of their signs, forcing the corresponding entry of Rhat(0)
to vanish. Coordinate permutations equate all six diagonal entries.
Entrywise sine is odd, so R has exactly this signed covariance. Therefore

    Rhat(0)=r_N I_6                                    (4.1)

for a real finite r_N. Coordinate shifts incurred by reflections have
phase1 at k=0; using midpoint coordinates does not change(4.1).

Since P(k)Q(k)=0,

    ||P(k)Rhat(k)Q(k)||
       <=||Rhat(k)-r_N I|| ->0 as k->0.                 (4.2)

Take smooth compactly supported continuum tests f and the standard sampled
plaquette source h_a(p)=a^2 f(a midpoint(p)) in four dimensions. Its ell^2
norm is bounded and its Fourier mass concentrates near0. Thus(4.2) and
boundedness give

    <P h_a,R Q h_a> ->0.                               (4.3)

The ordinary Hodge-symbol limit gives ||P h_a||^2 ->||P_cont f||_2^2 and
likewise for Q. The limiting quadratic mixed coefficient is consequently

    2 z_0 w_0 A_N
       [g^2||P_cont f||_2^2-b^2||Q_cont f||_2^2].        (4.4)

No rate of continuity for Rhat and no fitted large-distance decay are used.

## 5. Higher source powers in THIS coefficient disappear

Poisson summation for a smooth compactly supported f gives
||hhat_a||_{L^1(T^4)}=O(a^2). Because the Hodge multipliers have norm<=1,

    ||Ph_a||_infinity+||Qh_a||_infinity=O(a^2),
    ||Ph_a||_2+||Qh_a||_2=O(1).

Thus their fourth-power sums are O(a^4). Taylor's theorem, the row/column
bounds for C, and 2u^2v^2<=u^4+v^4 bound the difference between the first
term of(2.1), summed over components, and its quadratic part by O(a^4).

For the second term use S as a signed bounded operator, not an absolute
kernel. With U=gPh_a,V=bQh_a,

    ||sinh(U)-U||_2=O(a^4),
    ||sin(V)-V||_2=O(a^4).

Consequently <sinh(U),S sin(V)>-<U,S V>=O(a^4).
The normalized elementary mixed coefficient therefore has the purely
quadratic macroscopic limit(4.4), for every fixed beta>0 and finite N>=1.

This is a statement about a specified first mixed component coefficient
defined by these convergent/operator sums. Identifying it with a uniform
thermodynamic derivative of the full clock pressure requires an activity
analyticity/limit theorem that has NOT been proved here. Summing all orders
at the physical activity values remains the main open step. In particular,
finite-order Gaussian behavior is not a Gaussian limit of the full law.

## 6. Finite checks and a preserved arithmetic blind spot

The source identity was compared with independent clock-angle/image sums
on a single three-cube, at N=2,3,4 and two nonprojected sources each. The
six residuals are below1.2e-15. The electric-current and magnetic sums used
cutoffs5 and6; the direct image sum used cutoff6. These finite sums are not
certified interval bounds for their omitted Gaussian tails. Omitting the
electric source disagrees in every case. Reversing both source signs agrees,
as required by simultaneous charge conjugation.

The first checker incorrectly required the single-source sign change to
disagree also at N=3. It did not: that case has an exact extra arithmetic
symmetry. For this particular three-cube, B is a six-entry row with
BB*=6, and

    M_N={m in Z^6: Bm=0 modulo N},
    T=I-B*B/3=P-Q.

If3 divides N, then Bm/3 is integer for every m in M_N. Thus Tm is again
integer, BTm=-Bm, and T is an orthogonal involution preserving M_N.
The centered Gaussian image law consequently has an independent Hodge
sign-reversal symmetry. A source-sign probe at N=3 cannot distinguish the
two formulas. This is a finite-carrier arithmetic fact, not a four-dimensional
phase claim.

The failed checker bytes and failure values are preserved under review/.
The final checker retains N=3 as a symmetry control, checks the lattice
reflection on integer generators for N=3,6, and uses N=2,4 as discriminating
source-sign cases. Their relative-sign errors range from1.1e-5 to1.4e-3;
the threshold was not loosened to accept an error in the source identity.

All six two-form orientations were also checked on periodic tori of
length8,12,16,24. Their row-square sum equals(1-L^-4)/2, explicitly retaining
the finite harmonic difference. The sums A_N agree across orientations;
Rhat(0) is scalar; and P(k)Q(k)=0. At N=3 the finite A_N values approach
approximately-35.5905 in these samples. This is diagnostic only, with no
certified infinite-volume error or fitted convergence rate. Independent
review, the full-component extension, and the all-order/source/state
estimates remain open regardless of these checks.
