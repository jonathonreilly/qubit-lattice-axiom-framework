# Linear energy mass changes the naive critical ratios

Status: ROOT author calculation, requiring a distinct check. This is a local Taylor-interface diagnostic, not a dynamical theorem or a no-go claim. It uses the stationary three-mediator proposal at SHA256 2972451d77aae751d5cf64c7022468e372d078a5bfda36b7a9c7b8477036596e, whose distinct check is pending.

Write c_l=gamma_l^2 d_(n_l)>0. The exact diagonal self-energy expansions are s_l(z)=-c_l z+O(z^3), while t_l(z)=t_l(0)+O(z^2). Retain the fixed-port sign gauge and let a_l=|t_l(0)|. On the first three source coordinates, the coefficient of z in the eliminated equation is the positive diagonal matrix

    Z_s=diag(Z0,Z1,Z2),
    Z0=1+c1, Z1=1+c1+c2, Z2=1+c2+c3.

The three-source block at linear order is z Z_s plus the canonical positive off-diagonal entries in E-H. Congruence by Z_s^(-1/2), leaving all background coordinates unchanged, puts this linear coefficient into identity form. The resulting reference hoppings are

    a1_eff=a1/sqrt(Z0 Z1),
    a2_eff=a2/sqrt(Z1 Z2),
    kappa_eff=a3/sqrt(Z2).

The background port still carries its additional diagonal coefficient c3 z. It cannot be discarded by this source-only congruence. Normalizing that port too would alter every old contact to it; it is not a free reexpression of the original background Green function.

For the proposed n1=n2=2m-1 and gamma2/gamma1=8^(1/4), one has c2=sqrt(8)c1 exactly. Since c3>0,

    (a2_eff/a1_eff)^2=8 Z0/Z2 < 8.

Thus exact critical ratios at z=0 do not by themselves reproduce the critically tuned linear-energy source polynomial. This strict discrepancy holds for every m and every nonzero supplied gamma1. It is a statement about the exact Taylor coefficients, not an approximation error caused by truncating a numerical series.

At fixed positive J,q,gamma_l and increasing m, d_n tends to 1/(J^2-q^2). Hence the ratio tends to

    8 [1+gamma1^2/(J^2-q^2)] /
      [1+(gamma2^2+gamma3^2)/(J^2-q^2)] < 8.

The relative linear-mass discrepancy does not vanish merely because the induced hoppings become geometrically small. Its absolute size can be reduced by separately small gamma_l/(J-q), but that is an additional supplied scale and incurs its own preparation/resource tradeoff.

This calculation does not invalidate the bandcenter stationary identities. It identifies the next necessary interface: either control the noncritical pulse and charged mass/preparation corrections directly, or choose new correlations to tune the renormalized coefficients and port response. Neither route is excluded here. A changed effective target requires its own physical phase and normalization; the full nonlinear Schur functions, loaded poles, product-seed spectral weight and mediator output coordinates remain unproved. The congruence is algebraic, not an isometric embedding or a proof of a dressed input state.

Exposure: ROOT suggested the previous integer lengths and algebraic bare ratios, read the complete new proposal and its isolated ancestor, and derived this diagnostic separately. No independent-check claim, spectrum execution, parameter sweep, canonical publication, physical-axiom or prompt change is made.
