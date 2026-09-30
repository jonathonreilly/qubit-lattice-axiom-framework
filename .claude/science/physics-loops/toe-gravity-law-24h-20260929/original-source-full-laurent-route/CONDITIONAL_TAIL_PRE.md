# Independent conditional-tail derivation before root proof exposure

Frozen before opening source-consumer-direction/CONDITIONAL_POLYNOMIAL_TAIL.md or its freeze. Root's task/three-step mechanism and now its completion brief are exposed; no blank-slate claim. I authored/reconstructed preceding actual-source inputs. No code/scientific computation, external action or new source hypothesis is verified here. This is conditional fixed-volume finite-fiber mathematics, not actual microscopic residence.

## Contract

Let d be fixed, H(theta)=H(theta)* a finite Laurent matrix with norm<=M on the physical phase torus, and 0<=G<=gI fixed with g>0. Fix delta,kappa,T0>0. Let S_theta(t)=exp[t(-i delta H(theta)-kappa G/2)], O=[G;GH;...;GH^(d-1)], and N=ker O. Assume the EXTRA generic formal-source containment already discussed, so every supplied formal source column T_mu has Pi_N T_mu=0 almost everywhere. Let r>0 be the GENERIC MAXIMAL rank of O, and q one actually nonzero r-by-r Laurent minor. A smaller nonzero minor would NOT control the least positive singular value when the generic rank is larger. Rank zero is trivial under formal containment: all formal sources must vanish.

A positive physical trace-class source sigma can be written sum_l |v_l><v_l|, with fiber intensity w(theta)=sum_l||v_l(theta)||^2. Assume explicitly ess sup w<=W and Pi_N(theta)v_l(theta)=0 almost everywhere. This is not identifying sigma with a trace-class multiplication operator on a nonatomic phase space. The actual original-history source is not asserted to satisfy this bound.

## 1. Uniform finite-time Gram comparison

First U_H(t)=exp(-i delta Ht). Each scalar component f(t) of sqrt(G)U_H(t)v obeys the order-d scalar ODE from the characteristic polynomial of -i delta H. Its coefficient vector lies in a compact polydisk determined by d and delta M. In companion coordinates (f,f',...,f^(d-1)), the output pair (e_1*,C_a) is observable for EVERY coefficient vector a: e_1*C_a^j=e_(j+1)* for j<d. Thus

    K(a)=integral_0^T0 exp(tC_a*)e_1 e_1*exp(tC_a) dt

is positive definite for every a, continuous on that compact polydisk, and has a common strictly positive least eigenvalue c0. This is a genuine uniform bound even at repeated roots/rank changes. Summing scalar components yields

 integral_0^T0 ||sqrt(G)U_H(t)v||^2 dt
    >= c0 sum_(j<d) delta^(2j)||sqrt(G)H^jv||^2
    >= (c0 min_(j<d)delta^(2j)/g)||Ov||^2.

No inverse eigenvalue separation of H is used.

For the actual damped S, Duhamel gives f_U=f_S+(kappa/2)K_volterra f_S, where the kernel is sqrt(G)U_H(t-s)sqrt(G), of norm<=g. Young's inequality on [0,T0] gives ||f_U||_L2 <=(1+kappa g T0/2)||f_S||_L2. Therefore the true loss Gram

    W_T0=integral_0^T0 S(t)*G S(t)dt >= c O*O,
    c=c0 min_(j<d)delta^(2j)/[g(1+kappa g T0/2)^2]>0.

This avoids needing to compare noncommuting damped derivative jets directly. Such a comparison is also triangular: G Z^j=(-i delta)^j G H^j+sum_(b<j)C_jb G H^b, by choosing the rightmost G in each remaining word. The coefficients are uniformly bounded at fixed d,M,g,delta,kappa.

## 2. Minor and contraction

Set L_O=g[summation_(j<d) M^(2j)]^(1/2), or any strictly positive larger uniform norm bound for O. At q!=0 the rank is exactly r. Exterior-power singular-value bounds give

    sigma_r(O)>=|q|/L_O^(r-1),
    O*O >= |q|^2/L_O^(2r-2) (I-Pi_N).

N and its complement reduce H and G, hence S. The exact loss identity is

    ||S(T0)v||^2=||v||^2-kappa<v,W_T0 v>.

On N-perpendicular this gives contraction by 1-a|q|^2. Choose a>0 no larger than kappa c/L_O^(2r-2) and no larger than 1/[2 sup|q|^2]. Iterating fixed intervals T0, and using contractivity for the remaining interval, gives

    ||S(t)(I-Pi_N)||^2 <= C exp(-b t |q(theta)|^2)

with fixed positive C,b depending on the declared finite data. Nothing is volume uniform. The phase-zero set of q is null and irrelevant to the stated phase-integrated estimate. Generic containment can also be seen to hold wherever q!=0: all augmented (r+1)-minors vanish identically once the generic ranks agree.

## 3. Elementary Laurent sublevel estimate

Let D_q be the sum of coordinate exponent widths of q after extracting a Laurent monomial. If D_q=0, q is a nonzero monomial, whose modulus is a nonzero CONSTANT on the physical torus; this gives an exponential bound directly. It need not be a constant polynomial before that extraction.

For D_q>0, an elementary induction gives

    Haar{|q|<=eta} <= C_q eta^(1/D_q),  0<eta<=1.

Univariate step: for a polynomial p of degree<=D having some coefficient of modulus>=a, factor p=c product(z-r_j). The maximum coefficient is at most 2^D |c| product max(1,|r_j|). If |p(e^it)|<=eta, at least one normalized factor |e^it-r_j|/max(1,|r_j|) is <=2(eta/a)^(1/D). Each such circle sublevel has measure<=C times this radius, uniformly in the root (larger radii are handled by the trivial bound1). Thus measure<=C_D(eta/a)^(1/D).

For the induction, expand in one variable of positive width D and choose a nonzero coefficient c(y). If its own remaining width-sum is E>0, induction bounds the bad coefficient set by C a^(1/E). On its complement the univariate estimate is C_D(eta/a)^(1/D). Taking a=eta^(E/(D+E)) gives exponent1/(D+E), at least as strong as1/D_q. If E=0, that coefficient has constant nonzero modulus after its monomial factor, and the univariate bound gives exponent1/D. A variable of width zero can be omitted. Constants depend on the actual polynomial; no generic independent physical path parameters are invoked.

Layer integration, not a fixed crude split, then gives for alpha=1/D_q

 integral exp(-bt|q|^2)dtheta
    <= C_q Gamma(1+alpha/2)(bt)^(-alpha/2)

for large t, with a harmless enlarged constant for (1+t)^(-alpha/2) at all t. Indeed the layer identity integrates 2bt s exp(-bt s^2) times Haar{|q|<=s}; extend the sublevel bound to s>=1 by increasing its constant.

## 4. Conditional conclusion and limits

The physical trace identity is

 Tr[S(t)sigma S(t)*]=integral sum_l||S_theta(t)v_l(theta)||^2 dtheta
    <= C W (1+t)^(-1/(2D_q))

when D_q>0, and exponential decay for nonzero constant-modulus q. It uses the assumed absence of dark source mass and the assumed bounded fiber intensity. It does not discard phase coherences; the identity follows from rank-one decomposition and decomposability of S.

This supplies a polynomial upper tail only under those additional assumptions. For D_q>=1 the displayed exponent<=1/2 is not integrable, so it does not prove finite mean residence, much less an electric weighted time integral or quadratic uniform integrability. No actual source intensity regularity, full containment, uniform volume scaling, finite-spin transfer or microscopic forcing bound has been established here. No flaw was found in the conditional mechanism with these precise qualifications.
