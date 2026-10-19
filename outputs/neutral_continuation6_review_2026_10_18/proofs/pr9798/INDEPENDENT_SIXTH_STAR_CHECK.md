<!-- Original PR9798 source SHA256 2d242ec2f19c850121afbc7d738e33f372867f7f259d28a39fe49c43cc961bb4. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# Conditional sixth-order four-ray star check

PASS for the specified star operator. Native graph closure, coefficients, source identification and any transfer to the full microscopic Hamiltonian remain separate premises.

Set t>0, w=v/t>=0 and x=E/t. There are two zero-onsite rays and two rays of onsite -v; the central onsite is zero. All central and outward hoppings are -t at momentum zero.

## Upper isolated eigenvalue

For x>2 the decaying ratios are

 r_h=-(x-sqrt(x^2-4))/2,
 r_l=-(x+w-sqrt((x+w)^2-4))/2.

The center equation is x=-2r_h-2r_l, equivalently

 sqrt(x^2-4)+sqrt((x+w)^2-4)=x+w.

The Schur complement E-2t^2 g(E)-2t^2 g(E+v), with g(z)=(z-sqrt(z^2-4t^2))/(2t^2) above the bands, is strictly increasing, negative at E=2t and positive at infinity. Thus exactly one upper isolated eigenvalue exists for every finite w>=0.

Squaring yields the polynomial

 3x^4+8wx^3+(4w^2-16)x^2-32wx-16w^2=0.

Keep the unsquared equation and x>2 to discard extraneous roots. At w=8/7 the polynomial is

 147x^4+448x^3-528x^2-1792x-1024=0.

A 40-digit interval-arithmetic sign check of the unsquared equation certifies

 2.11447531630064 < x < 2.11447531630066.

The upper band edge is 2t, giving gap approximately 0.11447531630065 t. Since the two ray continua overlap for w=8/7, there is no intervening spectral gap in which an extra bound eigenvalue could hide. The antisymmetric ray combinations are free half-lines and add no exterior eigenvalues.

## Lower eigenvalue criterion

Below the lower edge E=-v-2t use the negative-energy Weyl branch. The same strictly increasing Schur complement has edge value

 2t-sqrt(v^2+4vt).

A lower isolated eigenvalue exists exactly when

 0<=v/t<2sqrt(2)-2.

At equality the limiting solution is at the low-ray edge and is not square summable. At v/t=8/7 the edge value is negative, so there is no lower bound state. Thus this model has precisely one isolated eigenvalue, above its continuum, at the stated native ratio.

## Normalization and source weight

Choose the normalized bound state with positive center amplitude sqrt(Z). Its amplitude at site n>=1 of each ray is sqrt(Z) r_a^n, where

 Z=[1+2r_h^2/(1-r_h^2)+2r_l^2/(1-r_l^2)]^(-1).

Numerically at w=8/7,

 r_h=-0.71408832358710, r_l=-0.34314933456322,
 Z=0.29869300450170.

For the unnormalized specified source s=|low1,first>+|low2,first>, the bound-state spectral weight is

 |<bound|s>|^2=4Z r_l^2=0.14068615643049.

For the unit-normalized source s/sqrt(2), the overlap probability is half this number, approximately 0.07034307821524. This distinction matters: the source sum has norm squared two. The normalized bound state has been used in both statements.

## Finite momentum and curvature

Write t=2gamma. For high x/y rays set c_hx=a_hx=t cos(qx/2), c_hy=a_hy=t cos(qy/2). For the low x ray set outward a_lx=t cos(qx) and contact c_lx=t cos(qy/2); for low y interchange x and y. Onsites remain 0 and -v as specified in the question. Near zero all hoppings are positive in these conventions before their Hamiltonian minus signs.

Define g_a(z)=(z-sqrt(z^2-4a^2))/(2a^2) above the corresponding band. The exact upper eigenvalue equation is

 E=sum_high c_a^2 g_(a_a)(E)+sum_low c_a^2 g_(a_a)(E+v).

The isolated simple q=0 eigenvalue persists analytically for sufficiently small real q. The continuum is the union of the four intervals onsite_a+[-2|a_a|,2|a_a|]. This is an analytic perturbation of a bounded operator with a nonzero spectral gap, so ordinary eigenvalue derivatives are controlled here.

Feynman–Hellmann gives contact derivative -2Z r_a and outward-hopping derivative -2Z r_a^3/(1-r_a^2) at zero. Hence

 E(q)=t x+t C(qx^2+qy^2)+O(t|q|^4),
 C=Z[r_h/(4(1-r_h^2))+r_l/4+r_l^3/(1-r_l^2)]
   =-0.14810976156651 approximately.

The Hessian entries are therefore -0.29621952313301 t, with zero mixed derivative at zero. This upper bound branch is locally a maximum in both transverse momentum directions, not a positive-curvature low-energy minimum. This curvature assumes exactly the given momentum-dependent hoppings and momentum-independent onsites; any native onsite dispersion would have to be added separately.

For a finite-q source with the same two unit coefficients on first low sites, set rho_a=-a_a g_(a_a)(E-onsite_a). Its first-site amplitude is -c_a g_(a_a)(E-onsite_a) times the center amplitude. Normalization gives

 Z(q)^(-1)=1+sum_a c_a^2 g_a(E-onsite_a)^2/(1-rho_a^2),
 W_s(q)=Z(q)[c_lx g_lx(E+v)+c_ly g_ly(E+v)]^2.

A different physical Fourier source may carry additional phases or coefficients; its native identification is not proved by the star solution.
