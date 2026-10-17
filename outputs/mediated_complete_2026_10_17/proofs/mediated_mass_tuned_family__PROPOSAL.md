# Fixed coefficients tuning the limiting linear-energy source

Status: ROOT author conditional construction requiring distinct checking. This tunes only the limiting selected-channel linear-energy source. It is not a full loaded inverse, prepared pulse, runtime or native supplier theorem. It is an alternative to the bare-ratio family, not a consequence of that family's gamma identities.

Use the corrected port replacement of mediated_critical_source_interface/PROPOSAL.md d2b7b435f6813847a0b293d5584a3aa5af844a02be09a95b768adc4ea4f963e3. Its original distinct review bda0710050f4154b190220419a1240c52adc04b15d0dfdb1a8e3ed27c22e6a7f supports unchanged mediator identities conditional on exactly that correction; scoped correction recheck remains pending. Here J_m denotes the mediator strong bond, distinct from the calibrated old-processor J. Fix 0<q<J_m, r=q/J_m, d_infty=1/(J_m^2-q^2), and C=3sqrt(3)j J_m d_infty>0. Choose J_m+q<2j. This alone does not impose any gamma correlations.

## Limiting linear masses and target equations

Set u=gamma1^2 d_infty, v=gamma2^2 d_infty, w=gamma3^2 d_infty. With n1=n2=2m-1,n3=m, the limiting source mass coefficients are

    Z0=1+u, Z1=1+u+v, Z2=1+v+w.

The selected zero-energy hopping magnitudes are gamma1^2/J_m r^(2m-2), gamma2^2/J_m r^(2m-2), gamma3^2/J_m r^(m-1). After the source-only linear-mass congruence the limiting effective magnitudes are

    A1_m=[u/(d_infty J_m sqrt(Z0 Z1))] r^(2m-2),
    A2_m=[v/(d_infty J_m sqrt(Z1 Z2))] r^(2m-2),
    K_m=[w/(d_infty J_m sqrt(Z2))] r^(m-1).

The critical conditions A2_m^2=8 A1_m^2 and K_m^2=3j sqrt(3) A1_m hold for EVERY integer m if and only if the fixed coefficients obey

    v^2(1+u)=8u^2(1+v+w),
    w^2 sqrt((1+u)(1+u+v))=C u(1+v+w).             (1)

These equations include the energy-dependent diagonal normalization that the earlier bare-ratio family omitted. The background port still has its self-energy s3(z); it is not removed or normalized by the source-only congruence. Consequently(1) alone does not tune the full coupled apparatus.

## Positive fixed solutions for arbitrarily small supplied scale

Write u=epsilon^2, v=epsilon^2 V, w=epsilon W, with epsilon>0. Define

    F1(V,W,epsilon)=V^2(1+epsilon^2)
                      -8(1+epsilon^2 V+epsilon W),
    F2(V,W,epsilon)=W^2 sqrt((1+epsilon^2)
                          (1+epsilon^2(1+V)))
                      -C(1+epsilon^2 V+epsilon W).

These functions are real analytic near (sqrt(8),sqrt(C),0), vanish there, and their Jacobian in (V,W) at that point is diag(2sqrt(8),2sqrt(C)), invertible. The analytic implicit function theorem therefore gives unique local positive analytic V(epsilon),W(epsilon) for sufficiently small |epsilon|. For epsilon>0 the corresponding fixed coefficients

    gamma1=epsilon/sqrt(d_infty),
    gamma2=epsilon sqrt(V(epsilon))/sqrt(d_infty),
    gamma3=sqrt(epsilon W(epsilon)/d_infty)

solve(1), and all tend to zero as epsilon tends to zero. Thus a sufficiently small positive epsilon meets the finite installation inequalities gamma3<=j, gamma1+gamma2<=2j, gamma2+gamma3<=2j and J_m+gamma_l<=2j. It can also meet gamma_l<=(J_m-q)/4 if desired. No length m enters these coefficients. Existence of the positive solution is local; no global uniqueness or numerical choice is claimed.

The first derivatives check the direction of the correction: F1'=2sqrt(8)V'(0)-8sqrt(C)=0 and F2'=2sqrt(C)W'(0)-C sqrt(C)=0. Hence

    V'(0)=sqrt(2C), W'(0)=C/2.

The coefficients are exact correlated supplied values. Analytic existence is not an implementation algorithm, native mechanism or tolerance guarantee, and it does not justify measuring them to unlimited precision for free.

## Explicit finite-length discrepancy of the linear model

The exact finite-length diagonal coefficients are

    u_m=u(1-r^(4m-2)), v_m=v(1-r^(4m-2)),
    w_m=w(1-r^(2m)).

Put Z0m=1+u_m, Z1m=1+u_m+v_m, Z2m=1+v_m+w_m. All are at least1. Define delta_m=(u+v+w)r^(2m). Since 4m-2>=2m for m>=1, each |Zim-Zi|<=delta_m. The zero-energy hopping numerators remain the same as above; only the true finite masses differ from their limits.

For x>=1, the derivative of log x is at most1. Thus

    |log(Zim/Zi)|<=delta_m.

Let A1_actual,A2_actual,K_actual denote the same zero-energy hopping magnitudes divided by the exact finite mass factors. The limiting equations(1) imply

    |log[(A2_actual^2/A1_actual^2)/8]|
       =|log(Z0m/Z0)-log(Z2m/Z2)|<=2delta_m,

    |log[K_actual^2/(3j sqrt(3)A1_actual)]|
       =|.5log(Z0m/Z0)+.5log(Z1m/Z1)
                                      -log(Z2m/Z2)|<=2delta_m.

Therefore each displayed normalized ratio differs from1 in absolute value by at most exp(2delta_m)-1. These are exact finite-length estimates on the linear-mass-normalized coefficients; they do not assert equality at finite m.

Writing lambda_m=sqrt(3)A1_m=Lambda r^(2m-2), with the fixed positive Lambda=sqrt(3)u/[d_infty J_m sqrt(Z0 Z1)], gives

    delta_m=(u+v+w) r^2 lambda_m/Lambda.

Thus the relative linear-mass tuning discrepancy vanishes at least linearly with this geometrically small lambda_m at fixed supplied coefficients. This corrects the earlier bare-ratio family's nonzero limiting mismatch. It does not establish a complete error estimate: the constants can depend on the chosen fixed epsilon,J_m,q,j, and the discrete lambda family is not continuously tunable.

## What still prevents a physical output transfer

The exact finite-energy hoppings and diagonal remainders are not these linear coefficients. Their checked local envelopes are proportional to n_l z^2/(J_m-q)^2 at leading relative hopping order and gamma_l^2 |z|^3/[(J_m-q)^3(J_m-q-|z|)] for the diagonal remainder. They must be kept over an explicitly chosen shrinking resonant region and its tails; a fixed-band uniform approximation need not improve with m.

The port self-energy, complementary channels and actual noncommuting background kernel still need their ordered inverse. Bare-product preparation still has a finite dressed-witness allowance controlled by gamma1/sqrt(J_m^2-q^2), not by m alone. The endpoint coefficient congruence is not a physical isometry or a free correlated seed. Mediator occupancy, output phase including (-1)^m, actual spectral regularity, full apparatus outputs and finite receiver resources are not proved here. A viable next step is a loaded resolvent/pulse estimate using the corrected linear tuning and the separately checked local product-seed witness, rather than importing the old nominal theorem.

Exposure: ROOT authored the linear-mass diagnostic51b3461c and this alternative construction after examining the stationary proposal and its distinct correction. The analytic theorem and its hypotheses are given explicitly above; no independent-check claim is made. No numerical root solve, spectrum, dynamics, sweep, canonical publication, axiom or editable prompt change occurred.
