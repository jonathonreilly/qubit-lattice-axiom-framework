# Finite smooth weights for the projected constraint

Direct author /root, working conditional derivation. This complements
WORKING_v1.md; it does not assert that a finite survey provides its inputs.

Use compactly supported smooth w(N,r) strictly inside 0<r<2chi(N), with measure
dN dr. The radial adjoints are

    K*= -K-1,
    P*= (K-1)(K+1)(K+3)(K+5),
    D*w= -partial_r(w/r),
    E*w= -alpha r partial_r w-(alpha+1)w.

Order reverses under adjoints. Put L*w=(E*)^2 P*w and Q*w=D*L*w.
Define the candidate-history coefficients a0=(y-x-2)/2 and c0=-h y-m.
After radial integration by parts and then time integration by parts, the
pointwise necessary constraint has the weak form

    integral [K_SS C_SS+K_Su C_Su+K_uu C_uu] dN dr=0,

with

    K_SS = -0.5 partial_N(Q*w)-a0 Q*w,
    K_Su = (2 a H chi/r^2) [partial_N(y L*w)-(c0-a0 y)L*w],
    K_uu = a^2 H^2 {-partial_N[(y^2/2)E*P*w]
                    -(y^2 g/2)(E*+1)P*w+c0 y E*P*w}.

Every derivative in these kernels acts on the calibrated geometry, proposed
coefficient histories and declared weight, not on a measured correlation.
Time variation of x,y,m and the projection operator is retained. In particular,
replacing a coefficient history by its value at a central redshift is not part
of this formula. The identities remain necessary only; a candidate can pass
these projected constraints yet fail scalar evolution or other observations.

All endpoint terms vanish for compact support. A concrete finite regularity
alternative uses a FIXED rectangle [N0,N1] x [r0,r1] strictly inside the
light-cone domain, enough continuous derivatives, and vanishing w and its
first six radial derivatives at the fixed radial boundaries, with w and all
needed radial derivatives zero on the time boundaries. This alternative does
not cover moving radial integration limits: their time boundary flux need not
vanish when Q*w is nonzero, even if w through derivative six vanishes. For
moving boundaries require the full flux to vanish separately (for example
stronger weight vanishing through derivative seven), or retain its exact term.
The primary compact interior support statement avoids that flux. No physical
boundary condition on V is inserted.

If separately justified pointwise errors obey |delta C_i|<=epsilon_i(N,r),
the candidate residual error is at most

    sum_i integral |K_i| epsilon_i dN dr.

This prices the derived operator; it does not supply epsilon, noise independence,
signal/noise separation or cosmic variance. The high derivative order moved to
weights can still create a very large error amplification.

The correlations C_SS and C_Su refer to the reconstructed l>=2 local Weyl
field. They still require the two-source-argument lensing inversion, and the
fixed-separation derivative construction assumes continuum signal functions.
For actual finite source/velocity bins one must propagate their known windows
before comparison, or prove that the required weak functional is represented
by their window span. The weak form alone does not establish that supplier.
This distinction is particularly important for the diagonal equal-epoch limit
of a two-source covariance. It is not licensed by simply interpolating bins.
