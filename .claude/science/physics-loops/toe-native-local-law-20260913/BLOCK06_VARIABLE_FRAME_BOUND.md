# Controlled native approximation for a nonuniform common frame

Analytical author derivation before finite challenges. All frame fields,
scale and couplings in this construction are specified inputs. This bound
provides a continuum approximation on a stated slow subspace, not a
metric-selection theorem or a finite-spacing gravitational symmetry.

## 1. Laurent bounds for the nine vertices

For V(k)=sum_r c_r exp(i k.r) vanishing at k_w, the elementary inequality
|exp(i u)-1-i u|<=u^2/2 gives the global momentum estimate

    |V(k_w+a p)/a-grad V(k_w).p| <= a L_V |p|^2,
    L_V=(1/2)sum_r |c_r| |r|^2.                         (B1)

For the vertices (C1), convenient exact Laurent constants are

    L_aj=1/2,                       a=1,2; j=1,2,
    L_a3=(zeta+2)/(2v^2),            a=1,2,
    L_3j=1/v,                       j=1,2,
    L_33=1/(2v).                                         (B2)

The connection hopping B(k)=sin k3/v obeys

    |B(k_w+a p)-w| <= a |p|/v.                          (B3)

These estimates hold at both nodes. They do not rely on fitting a polynomial
to sampled lattice energies.

## 2. A local polynomial approximation of the spin connection

Let F(x)=F0+f(x), F0=diag(1,1,v). Assume f is a real finite Fourier sum with
frequency support |q|<=B_f. Assume, for all x,

    ||F0^(-1) f(x)||_op <= rho < 1,
    ||F(x)||_op <= M0,
    [sum_i ||partial_i F(x)||_op^2]^(1/2) <= M1.

The stronger small-frame condition (C5), imposed pointwise if desired,
implies invertibility but is not needed separately for the estimates below.
For integer m>=0 define

    Q_m(x)=sum_(n=0)^m [-F0^(-1) f(x)]^n F0^(-1).

The Neumann identity gives

    ||Q_m||_op <= 1/[v(1-rho)],
    ||F^(-1)-Q_m||_op <= rho^(m+1)/[v(1-rho)].          (B4)

Replace the inverse in (P9) by Q_m to obtain the real scalar C_m. Its Fourier
support lies in |q|<=(m+2)B_f. There are six nonzero epsilon entries. For
each, Cauchy-Schwarz in i bounds the directional derivative row by M0 M1,
and the Q column has norm at most ||Q||. Hence

    ||C_m-C||_infinity <= eta_m,
    eta_m=3 M0 M1 rho^(m+1)/[2v(1-rho)].                (B5)

A literal native control stencil may also replace partial_i F by

    D_i^a F(x)=[F(x+a e_i)-F(x-a e_i)]/(2a).

If M3=[sum_i sup_x ||partial_i^3 F(x)||_op^2]^(1/2), central Taylor's
integral remainder gives ||D_i^a F-partial_i F||_infinity <=
a^2 sup||partial_i^3 F||/6. The resulting C_m^a is still a real finite
Fourier sum with the same bandwidth and obeys

    ||C_m^a-C||_infinity <= eta,
    eta=eta_m+a^2 M0 M3/[4v(1-rho)],
    ||C_m^a||_infinity <= c_m,
    c_m=3 M0(M1+a^2 M3/6)/[2v(1-rho)].                 (B6)

The stencil uses the frame at x and nearest coordinate neighbors, and no
matrix inverse or nonlocal solve is needed at a site. This is a bounded local
CONTROL rule for the supplied frame; a physical frame register and its
Hamiltonian still have to be constructed.

## 3. Operator estimate and exact sampling domain

Use the native Fourier convention and envelope coordinate x=-a n from
BLOCK06_DERIVATION.md. For a continuum L2 spinor with Fourier support |p|<=K,
modulation by exp(-i k_w.n) followed by a^(3/2) sampling at -a n is isometric
whenever its support remains within the associated Brillouin window.
Finite Fourier multiplication by a coefficient of bandwidth B increases
support by at most B. Define

    P=K+(m+2)B_f,       a P < acos(zeta).                (B7)

This keeps all intermediate and output bands for the following operator
inside their node window; it also separates the two nodes. Define the
native envelope operator using the EXACT trigonometric symbols

    h_a,m=h0(k_w+a p)/a
          +(1/2)sum_aj {f_aj(x),sigma_a V_aj(k_w+a p)/a}
          +(1/2){C_m^a(x),B(k_w+a p)} I.                (B8)

On this band, modulation/sampling intertwines (B8) exactly with the stated
finite-range lattice hopping operator. There is no projection of a product
onto a smaller computational band in this assertion.

Let h_F,w be the full continuum operator (P12), including exact C(F), and
q_aj=||f_aj||_infinity. The Wilson estimate (D9) and (B1)-(B6) imply

    ||(h_a,m-h_F,w) psi|| <= epsilon_a,m(K) ||psi||,
    epsilon_a,m(K)=delta_a(P)+a P^2 sum_aj q_aj L_aj
                    +c_m a P/v+eta,
    delta_a(P)=a P^2/2+a^2 P^3/6.                        (B9)

Proof: in each anticommutator, the Fourier error acts either before f,
on the K band, or after f, on the K+B_f band. Each half is bounded by
q_aj a L_aj P^2/2. The scalar hopping similarly has two halves bounded
by c_m a P/(2v). The remaining scalar multiplication error is at most eta.
The base symbol error is bounded by delta_a(P). Summing proves (B9).
Although exact C need not have finite Fourier support, its difference from
C_m^a is bounded as a multiplication operator on the full continuum L2
space. Thus (B9) includes that tail; it does not silently identify the exact
continuum output with a band-limited sampled function.

For a real finite Fourier lapse N with bandwidth B_N and sup norm n0,
H[N]={N,h}/2 satisfies the corresponding estimate n0 epsilon_a,m(K+B_N),
with the separation condition enlarged to a[K+B_N+(m+2)B_f]<acos(zeta).
This is an operator bound on the stated input band, not a claim that time
evolution preserves that band indefinitely.

Taking m proportional to log(1/a) for fixed rho<1 makes eta_m=O(a), while
P=O(log(1/a)). Equation (B9) is then O(a log^2(1/a)) at fixed K,B_f and
bounded smooth frame, and the no-alias condition holds for sufficiently
small a. This supplies a convergent sequence of finite-range Hamiltonians:
raising m changes the local polynomial of external frame values, not the
maximum quantum hopping path length. It does not supply a uniform
interacting bound or control long times without an additional propagation
estimate.

## 4. Finite challenge design

Use a positive frame with a nonzero C, such as
F=[[1+t,b sin z,0],[b sin z,1,0],[0,0,v]] for fixed small t,b. Its exact
connection is -v t b cos z/[4(1+t-b^2 sin^2 z)]. Compare the nine genuine
native Laurent multipliers and the central-stencil C_m^a against the exact
continuum differential operator on low Fourier inputs at both nodes.
Include offdiagonal frame entries involving z in a second supplied frame,
so the repaired two-cone shear vertices are actually exercised. Challenge
the inverse remainder and central derivative errors separately. Use the
analytic bound as the theorem; grids and Fourier truncation are diagnostics.
