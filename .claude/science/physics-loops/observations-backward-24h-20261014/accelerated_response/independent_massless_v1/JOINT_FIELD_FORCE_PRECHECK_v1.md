# Independent joint direct-field/force derivation before author access

Reviewer `/root/inertial_response_check`. No accelerated-response author draft
or code has been read. The pure-force derivation/oracles were frozen and their
18 new checks completed before this joint extension was written. Root remains
the author of the actual physical one-way count model; none is supplied here.

Consider finitely many prescribed C2 strictly subluminal paths x_j(s), with
bounded acceleration on intervals containing the real compact coefficients
c_j in L2 and W_j in H1. For one common real free massless scalar h, set

    L = sum_j integral [c_j(s) h(s,x_j(s))
                         + W_j(s).a_h(s,x_j(s))] ds,
    a_h=-(1-|u_j|^2)(grad h+u_j partial_s h).

The laboratory energy norm is ||h||_E^2=2E. A necessary domain qualification is
stated first, because force and direct-field functionals behave differently.

## Constant background and the energy space

The norm result below applies to the completion of compactly supported smooth
initial data under dot H1(R3) x L2(R3), with the dot-H1 Sobolev representative
in L6 and a fixed constant background. On that space, the field is anchored and
there is no arbitrary additive zero-energy constant in the data.

If instead one permits all classical finite-gradient-energy fields plus an
arbitrary constant h0, then adding h0 leaves laboratory energy and force
unchanged, while L changes by

    h0 sum_j integral c_j(s) ds.

Thus no energy-only bound exists on that unrestricted class when this total
coefficient is nonzero. Either the background must be fixed or the displayed
total coefficient must vanish, so the functional descends to the quotient by
constants. This qualification was identified independently and sent to root
before reading any author material. It is not retired by the Fourier formula.

## Exact signed amplitude

For each n on S2 and path j let

    d_j=1-n.u_j>0, A_j=1-|u_j|^2,
    tau_j=s-n.x_j(s), B_j=A_j(n-u_j)/d_j,
    C_{j,n}(tau_j(s))=c_j(s)/d_j(s),
    H_{j,n}(tau_j(s))=B_j(s).W_j(s).

C is compact L2; H is compact H1. Extend each by zero outside its own arrival
interval, using the same global tau coordinate for every path. With the Fourier
convention fhat(k)=integral f(tau)exp(-ik tau)d tau, the original laboratory
positive-frequency coefficient of this path is

    integral [c_j - i k A_j(n-u_j).W_j]
                 exp[-ik(s-n.x_j(s))] ds
      = Chat_{j,n}(k) - i k Hhat_{j,n}(k)
      = Fourier[C_{j,n} - partial_tau H_{j,n}](k).

The relative sign is MINUS. The last step uses
Fourier[partial_tau H]=i k Hhat with the vanishing endpoint traces. A second
way to see it is to integrate B.W times partial_tau exp(-ik tau) by parts.
Adding separate field and force norms loses this sign and the cross term.

Write D_n=sum_j(C_{j,n}-partial_tau H_{j,n}). Real Fourier pairing and the
laboratory norm give the exact dual norm

    G_total = 1/(2pi)^3 integral_S2 integral_0^infinity |Dhat_n(k)|^2 dk dOmega
            = 1/(8pi^2) integral_S2 integral |D_n(tau)|^2 d tau dOmega.

The sharp bound is |L|^2 <= 2E G_total in the anchored energy completion.
The mixed Gram of two such functionals replaces |D|^2 by their product.
Reality supplies the half-line Parseval factor pi, not an extra factor two.
This is a common-field Gram; independent fields would require their own direct
sum energy space rather than deleting the common-field cross terms by choice.

For a single path, define R_n=partial_s(B_n.W). The exact local formula is

    G = 1/(8pi^2) integral ds integral_S2 [c(s)-R_n(s)]^2/d_n(s) dOmega.

This requires only the existing C2 path and L2/H1 coefficient regularity; no
derivative of c and no jerk appear. It includes both the field/force interference
and the acceleration terms in R. It is a continuous functional of the stated
data; pointwise traces need not exist for every energy-space field.

## Independent analytic sign and normalization oracles

For a stationary path the odd angular field-force cross term vanishes and

    G = integral [c^2/(2pi) + |W'|^2/(6pi)] ds.

For a nonzero constant velocity u=beta e, define ell=log((1+beta)/(1-beta)) and
A=1-beta^2. The coefficient of c^2 and the vector coefficient in the cross term
are

    K(beta)=ell/(4pi beta),
    S(beta)=A(2beta-ell)/(4pi beta^2) e,
    g_s = K c^2 - 2c S.W' + W'^T T(beta) W'.

Here T is the previously frozen inertial tensor. S points opposite u and has
small-beta limit -u/(6pi); K tends to 1/(2pi). These independently integrated
angular coefficients detect a sign error which the stationary same-path case
cannot detect.

At an instantaneous rest event u=0 with acceleration v, direct angular
polynomial integration instead gives

    g_s = c^2/(2pi) + 2c(v.W)/(3pi) + |W'|^2/(6pi)
          + (|v|^2 |W|^2 + 7(v.W)^2)/(30pi).

The W'-W term and c-W' term vanish at this instant, but the c-acceleration-W
term does not. In the pure-force plateau counterexample, take c equal to the
smooth velocity derivative on the moving plateau, with zero outside. The
original laboratory coefficient integral [c-i k A(n-u).W] exp(-ik tau) provides
a separate finite-frequency oracle for the sign-sensitive exact square.

## Cross paths

All cross terms must be evaluated after each path is pushed into the common
arrival coordinate. Coincident paths with opposite (c,W) give exact zero even
though their individual norms are positive. For distinct stationary paths
x_a=0, x_b=r e1, take c_a=w, W_a=0, c_b=0 and W_b=e1 w. Then

    D_n(tau)=w(tau)-n_1 w'(tau+n_1 r),
    G=1/(8pi^2) integral_S2 integral |D_n|^2 d tau dOmega.

The cross term generally does not vanish. An independent laboratory-frequency
representation is

    Dhat_n(k)=what(k)[1-i k n_1 exp(i k n_1 r)].

The two forms can be tested separately using exact piecewise polynomial time
integration and direct frequency integration. They demonstrate why neither an
equal-laboratory-time cross product nor the sum of individual norms is exact.

For a finite number N of paths the norm is finite. The triangle bound
sqrt(G_total)<=sum_j sqrt(G_j), or G_total<=N sum_j G_j, is safe but usually
nonsharp. A clock contribution alone obeys
G_clock<=||c||_2^2/[2pi(1-b)] on |u|<=b<1; it can be combined with the earlier
force bound by the triangle inequality, retaining all actual cross terms in
the exact formula.

No result here supplies a physical field energy, clock calibration, background
choice or count model. No massive acceleration result follows: the nonzero-mass
phase is not k times a single arrival coordinate, so the Parseval reduction used
above must not be reused for mu>0 without a new proof.
