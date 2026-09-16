# New route: uniform real-time electric two-point propagation

2026-09-16 UTC. ACTIVE, UNPROVED. Complete/preserve the Block04 mixed-state
milestone first. This is a substantive new obligation: equal-time/form
convergence alone does not establish real-time dynamics.

The exact electric equation may bypass the problematic magnetic equation.
With dimensionless G=calH-E_ground and J_l=-partial_(theta_l)calH_m,

    i[calH,P]=-S^*Z+g W_E^(1/2)J,
    [calH,P(u)]=i Z(Su)-i g J(W_E^(1/2)u).

On a ground vector (or as Hilbert--Schmidt vectors with rho^1/2),

    G P(u)rho^1/2-P(Omega u)rho^1/2
       =-Q(Omega u)rho^1/2-i g J(W_E^(1/2)u)rho^1/2,

because M^*Omega=S. Check the signs explicitly. Block02 plus Fourier trace
positivity bounds the Q term by C sqrt(delta) sup||u_hat||. Each current
link is bounded, giving the second term <=Cg||u||_1. This is **norm
convergence of generator action on one-field ground vectors**, stronger
than merely convergence of energy forms. It may suffice for real-time
electric two-point functions.

For u_t=exp(-it Omega)u, apply Duhamel to
exp(-itG)P(u)rho^1/2 versus P(u_t)rho^1/2. The only new uniformity issue is
the l1 norm of u_t in the current bound. There is a plausible elementary
route: the matrix symbol Omega(k) is smooth off0, O(|k|) at0 and has second
derivatives O(1/|k|), hence belongs to H^2(T^3). Fourier Cauchy--Schwarz
then implies absolute summability of its kernel, since
sum_(x in Z^3)(1+|x|^2)^-2<infinity. Finite-volume kernels are periodizations
and have no larger l1 norm. The convolution Banach-algebra exponential
gives ||exp(-it Omega_L)u||_1<=exp(K|t|)||u||_1 uniformly in L.

If all of that is checked, the Duhamel error on bounded time intervals is
C_T(sqrt(delta)+g), and equal-time covariance convergence supplies the
free electric Wightman two-point function along arbitrary joint g0,Linf.
This would establish a real-time two-point bridge, NOT full nonlinear
Weyl dynamics or the fixed-g phase.

Do not silently generalize to all fields/polynomials. The magnetic equation
contains symmetrized cos(theta)P and its L2 remainder needs more than a
second-moment estimate. A toy coupling to an unseen high-energy oscillator
can preserve a Gaussian equal-time vacuum and first energy forms while
changing limiting dynamics; this is why the norm residual above matters.

Possible magnetic recovery: choose transverse smear and use the approximate
ground annihilation relation to identify its created vector with an electric
smear, plus Z_perp small. M multipliers are bounded on Fourier sup, but may
not preserve l1 at zero, so do not assume that route uniform without a new
smear argument. Purely electric local probes already give a nontrivial
propagation result.

## More detailed route, still to write and check

For the l1 kernel, avoid differentiating individual eigenvectors. Let
A(k)=S(k)^*S(k), tau=tr A, p=[tau^2-tr(A^2)]/2, and Pi its rank-two range
projection. For k!=0,

    Omega(k)=[A(k)+sqrt(p(k)) Pi(k)]/sqrt(tau(k)+2sqrt(p(k))).

The null vector is W_E^-1/2 d(k), d_i=exp(ik_i)-1; its normalized outer
product gives I-Pi. Positivity of fixed weights makes both nonzero
eigenvalues comparable to |k|^2 near0. Thus p~|k|^4, tau~|k|^2,
Pi derivatives order j scale |k|^-j, and Omega derivatives through order2
scale |k|^(1-j). This proves H^2 without a degeneracy assumption. Weak
second derivatives have no point delta because the shrinking boundary
integrals vanish. Periodization of the absolutely summable Fourier kernel
is exact, since its Fourier series converges uniformly to Omega.

Equal-time characteristic convergence alone does not justify moments. For a
real possibly nonlocal smear f, P(f)=[Q(f)+Q(f)^*]/2. Let eta=||Q(f)||_rho.
The exact commutator expectation is

    c= rho[Q(f),Q(f)^*]
      =2 f.Omega.f + O(g^2 ||f||_2^2).

Also ||Q(f)^*||_rho^2=eta^2+c and
|rho Q(f)^2|<=eta sqrt(eta^2+c). Consequently

    rho P(f)^2=(1/2)f.Omega.f+O_B(sqrt(delta)+g^2)

uniformly for ||f||_2 and sup||f_hat|| bounded by B. Complex smears follow
by polarization, using that the electric components commute. This yields
the needed moment limit and controls nonlocal-smear approximation.

With u_t=exp(-it Omega_L)u, the Q residual is bounded by
w0 sqrt(delta) sup||u_hat|| since the Fourier exponential is unitary. The
current residual is <=Cg exp(K|t|)||u||_1. Therefore bounded-time Duhamel
should give norm error C_T(sqrt(delta)+g). For real local u,v,

    rho[P(u,t)P(v)] -> (1/2)u.Omega exp(-it Omega).v

in dimensionless time; physical time replaces t by t/a.

Magnetic recovery is plausible WITHOUT an l1 bound for M. On ground vectors,

    Z(v) = -i P(Mv) +i Q(Mv)+Z_perp(v)

up to equality as applied to the vector. The last two terms have norm
O(sqrt(delta)). The bounded Fourier symbol f(k)=M(k)v_hat(k) may be
discontinuous at0, but can be approximated in L2 by Fejer trigonometric
polynomials f_n with uniformly bounded Fourier sup and real-position
coefficients. The electric moment estimate above bounds the limsup norm of
P(Mv-f_n) by [int (Mv-f_n)^* Omega (Mv-f_n)/2]^(1/2), which tends to zero.
At each fixed n the electric dynamic theorem applies. Take the joint g,L
limit first, then n->infinity. Unitarity controls the approximation error
uniformly in time. This would give all local gauge two-point functions,
with one-particle vector label zeta=u-i Mv and covariance
(1/2) zeta_1^* Omega exp(-it Omega) zeta_2. Check orientations and complex
conjugation. This still does not prove nonlinear field dynamics.

## Separate promising matter-dynamics route

For a rooted auxiliary CAR generator a_x=U(p_x)^q c_x, the electric
commutator has g^2 E times its fixed finite path plus a g^2 scalar. Since
P=g sqrt(e)E has uniformly bounded local second moments, its ground-vector
norm is O(g). The matter commutator is the free hopping equation plus fixed
fundamental-loop defects; Block01 makes those O(g) in ground norm. Thus

    [calH,a_x]rho^1/2 +sum_y h_xy a_y rho^1/2 =O(g)

for each fixed x/root path, and adjoints similarly. For finite CAR
polynomials, reorder P past bounded dressings; commutators add O(g) bounded
terms, so the generator residual may remain O(g). This gives a different
route to real-time fermion correlations, not through energy-form convergence.

Free finite-range CAR evolution has rapidly decaying spatial tails. To avoid
uncontrolled wrapping loops, approximate its evolving smears on a fixed
large ball, use the O(g) residual there, take the joint g,L limit, then let
the ball grow. The derivative truncation error is small uniformly on bounded
times by the finite-range matrix exponential. For arbitrary fixed products,
free CAR norm continuity gives the same approximation. On ground vectors
G j(B)rho^1/2=[calH,j(B)]rho^1/2, suggesting an intertwiner with free CAR
vacuum evolution. Then extend to time-ordered bounded matter words by
bounded multiplication and finite-polynomial approximation. Only neutral
physical words are the final claim; charged rooted CAR is a proof device.
Do not combine this automatically with unbounded mixed gauge/matter
multi-time products, which can require higher moments.
