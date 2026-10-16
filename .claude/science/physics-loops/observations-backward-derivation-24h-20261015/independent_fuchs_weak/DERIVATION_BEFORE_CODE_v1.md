# Independent derivation and frozen synthetic controls

Only the note and development plan have been read. No author runner/results or
raw Fuchs trace has been accessed. This proof and these fixtures are frozen
before implementing the independent checks.

With q=x-X, the harmonic matrix for (q,X) is

    [[D, -m omega^2], [-Z, P]],
    D=Z-m omega^2, Z=k+i omega c, P=K-M omega^2+i omega C.

The force vector is (m g_t+f, M g_p+f_p-f). Cramer's rule gives determinant
Delta=DP-m omega^2 Z and exactly equation (2). The internal force's numerator
is P-m omega^2, whereas a force on the test body with reaction elsewhere has
numerator P. Dividing source response by the former gives equation (3), only
if both Delta and P-m omega^2 are nonzero. At m=1,M=3,omega=1,K=4,C=0,k=2,
c=1/5, one has P=1 and Delta=-1: the system is nonsingular but its internal
calibration response is zero. This is a decisive excluded antiresonance.

For a free support, P=-M omega^2. Uniform external acceleration cancels the
particular relative drive; it does not remove homogeneous motion. If g_p=0,
the relative displacement is m g_t/[D+(m/M)Z]. Near D=0, a small m/M need not
make its difference from the fixed-support response small. This is not a claim
that every calibrated ratio has that enhancement: internal calibration in this
free-support case gives f_equiv=m(g_t-g_p)/(1+m/M).

Dividing the first mechanical equation by m gives
g_t=q''+(c/m)q'+(k/m)q+X''-f/m. Thus equation (4), as written, applies when
the calibration force is off, or when its contribution is included in the
defined drive. For any chosen smooth drive, solving this identity for X'' and
integrating twice leaves the stated missing-channel ambiguity. It does not
identify a physical support obeying an independently known second equation.

For a complex physical solution q_c=z exp(i Omega t), differentiating twice
gives the displayed constant-carrier equation without a rotating-wave
approximation. Multiply by w and integrate: integral(w z')=-D_w and
integral(w z'')=E_w because w and w' vanish at both endpoints. Hence

    [E-(gamma+2iOmega)D+(omega0^2-Omega^2+i gamma Omega)C]/(2iOmega)
        = R-aB-i nu C = b U,

where a=-gamma/2 and nu=(omega0^2-Omega^2)/(2Omega). No initial coefficient
is needed. Homogeneous solutions change the moments but obey the same
identity. For a varying carrier Omega(t), the demodulated operator acquires
i Omega'(t) z, and integration after dividing by Omega(t) has additional
coefficient derivatives. Simply substituting a variable carrier is not exact.

Full real column rank of (B,iC,U,iU) gives at most one exact coefficient vector
if the equations are consistent, and a unique unconstrained least-squares
minimizer otherwise. It neither guarantees consistency nor a physical damping
sign, positive omega0 squared or finite-noise precision. For z=A exp(i sigma t)
and u=exp(i sigma t), compact windows give D=-i sigma C, E=-sigma^2 C and
B=(1+sigma/Omega)C. Every row is a complex multiple of one fixed row, so the
real rank is at most two; if any U is nonzero, its U,iU columns give rank two.

The first-order omission has an exact residual at the true coefficients:

    -D-aC-i nu C-bU = i E/(2Omega)+i a D/Omega.

It must not be called the exact demodulation equation. For full histories, a
common time-invariant convolution commutes with the constant-coefficient
operator. Distinct filters generally give a frequency-dependent input/output
ratio; a proportional-filter exception can be absorbed into b. Finite-record
initial filter state adds other transients. A contribution exp(-t/tau) has
nonzero weak residual unless that exponent happens to be a homogeneous root
of the oscillator operator. Compact endpoints do not remove such a term.

Frozen controls, with synthetic inputs only:

1. Exact symbolic 2x2 solve, free-support uniform-drive cancellation, external
   versus internal calibration numerator, and the nonzero-Delta antiresonance
   above. Near-pole example: m=1,M=1000,k=1,omega=1,c=.001,K=C=0,g_t=1,g_p=0;
   distinguish uncalibrated displacement error from the calibrated ratio.
2. Symbolic constant/variable-carrier transformations and the adjoint identity.
   Use w(s)=140s^3(1-s)^3, verify unit integral and endpoint conditions.
   Set Omega=5,gamma=2,omega0^2=49,b=(3+2i)/7 and
   z(t)=1+2i+(2-i)t+(1+3i)t^2+(2+i)t^3/5. Manufacture u directly from the
   second-order operator divided by 2iOmega b. Windows [j,j+1], j=0,1,2,3,
   permit exact rational polynomial moment integration and real-rank recovery.
   Explicitly preserve nonzero first-order residuals.
3. Add arbitrary homogeneous amplitudes multiplying
   exp[(-1-5i+4sqrt(3)i)t] and exp[(-1-5i-4sqrt(3)i)t]. Use amplitude pairs
   (0,0), (2+i,-1+2i), (100+30i,-80+20i), with unchanged u. Independently
   integrate the moments by 64-node Gauss quadrature, tolerance 2e-10 relative
   plus 1e-11 absolute for weak residuals. Do not fit/subtract those amplitudes.
4. Monochromatic case sigma=2,A=2+i on the same windows: exact rank-two
   factorization and numerical real rank. Compare both raw and column-scaled
   singular values for the manufactured full-rank and rank-deficient cases.
5. Common two-tap filter Hf(t)=[f(t)+f(t-1/3)]/2 preserves the polynomial
   manufactured equation exactly. Differing delays at frequencies 1 and 3
   with delay pi/4 have unequal gain ratios, so a single b cannot absorb them
   at the fixed physical oscillator parameters. A filter-state term
   exp(-5t/2) gives a nonzero compact-window weak residual at the same mode
   parameters. None of these examples identifies a real instrument filter.

All owned runs will be bytecode-disabled and externally bounded at 120 seconds.
Actual stdout/stderr and failures will be retained before repair. Independent
outputs will be frozen before author code/results access. No raw trace, wiring
assignment, support model, covariance, force map or scalar strength is inferred.
