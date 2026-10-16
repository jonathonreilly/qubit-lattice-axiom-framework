# Independent derivation before reading the author runner

Prepared after the complete source note, plan, frozen manifest and dependent
siren note were read, but before opening or executing the source-closure runner.
The preceding timestamp/hash record is `PRE_CODE_SOURCE_BINDING.json`.
This is the independent starting calculation, not a retrospective claim based
on the author's code. The broader siren block remains outside this check.

## Charge and conservative normalization

For `gE=(F/Fstar)gJ`, the physical point-particle action is
`-m integral sqrt(Fstar/F) dsE`. With
`dphi/dF=sqrt(Fstar D/2)/F`, `D=2omega+3`, the local mass derivative is
`beta=-1/sqrt(2 Fstar D)`. At the chosen `Fstar=F0`, `mE=m` and
`q=mE beta=alpha m/sqrt(2F0)`, where `alpha=-1/sqrt(D0)`.

Variation of the canonical scalar action plus the particle action gives
`(box-m_s^2)delta phi=q delta^3(x)` locally. The static solution is
`delta phi=-q exp(-m_s r)/(4pi r)`. The second particle's energy shift is
`-q1 q2 exp(-m_s r)/(4pi r)`, or
`-GT alpha1 alpha2 m1m2 exp(-m_s r)/r`, since `GT=1/(8pi F0)`.
The force contains the additional factor `(1+m_s r)`; the constant orbital
coupling requires the long-range limit. No compact-body charge follows from
this point-particle weak-binding calculation.

## Angular flux and circular moments

The retarded scalar field is minus the retarded source integral divided by
`4pi R`. Its dipole/quadrupole time derivatives therefore have coefficients
`1/(4pi R)` and `1/(8pi R)`. Rotational angular averages give

    average[(n.d)^2] = d.d/3,
    average[(n.S.n)^2] = [(tr S)^2+2 tr(S^2)]/15.

One independent derivation uses a rotationally invariant three-dimensional
Gaussian: its fourth moment is Wick's sum, while its radial fourth moment is
`15/4` for density proportional to `exp(-x.x)`. Dividing the Gaussian tensor
moment by the radial moment yields the angular result without angular
quadrature. With a constant trace, the fluxes become
`Dddot^2/(12pi)` and `Q_STF'''^2/(120pi)`. A changing trace cannot simply be
dropped; it is excluded by the circular, constant-charge source contract.

In the mass center, `x1=m2 r/M`, `x2=-m1 r/M`. Hence
`D=sqrt(4pi GT) mu(alpha1-alpha2)r` and
`Q_STF=sqrt(4pi GT)(alpha1 m2+alpha2 m1)I/M`.
For a circular orbit, `Dddot^2=4pi GT mu^2 DeltaAlpha^2 r^2 Omega^4` and
`I'''^2=32 mu^2 r^4 Omega^6`. Dividing by the tensor flux `GT I'''^2/5`
therefore gives exactly `5 DeltaAlpha^2/(96 v^2)` and `alpha_Q^2/6`.
Equal weak-body charges cancel the dipole but leave `1/(6D0)` quadrupole loss.

## Massive harmonics and frame-dependent units

For a harmonic `exp(-i nu t)`, the radiative multipole field has amplitude
proportional to `k^ell`, while the time-averaged radial flux is
`nu k |amplitude|^2/2`. Relative to a massless harmonic the factor is
`(k/nu)^(2ell+1)=[1-m_s^2/nu^2]^((2ell+1)/2)`.
The circular dipole uses `nu=Omega`, the quadrupole `nu=2Omega`. A decaying
evanescent solution has zero time-averaged outward flux; the threshold limit
also vanishes. This assumes a linear outgoing field, `k r<<1`, and no other
energy channels. It is not a nonlinear screening threshold.

Tracing the metric equation and eliminating curvature from the scalar equation
gives `D box F=T+2F V_F-4V-omega_F (partial F)^2`.
At a material-vacuum constant solution, `F0 V_F=2V`, and linearization gives
`m_J^2=2(F0 V_FF-V_F)/D0`. The Einstein potential is
`U=Fstar^2 V/F^2`. At its stationary point,

    U_phiphi = (Fstar/F0) m_J^2.

The background conformal rescaling of time/length supplies exactly the same
conversion. Choosing `Fstar=F0` makes the numerical masses equal. Off
equilibrium, the omitted terms are

    U_phiphi - (Fstar/F)m_J^2
      = -Fstar (V_F-2V/F)[4/(F D)+D_F/D^2].

Thus equilibrium is essential, including for nonconstant omega. With
`V=F W(x)`, `x=log(F/C)`, the derivatives are
`V_F=W+W_x`, `F V_FF=W_x+W_xx`. The vacuum criterion is `W_x=W` and
`m_J^2=2(W_xx-W)/D`. The cancellation of `C` is real, but a physical radius
scale, an action continuation and registration to the source environment
remain required.

## Metric potentials and compact-body ambiguity

The scalar perturbation for a universal weak source gives
`delta F/F0=2GT M alpha^2 exp(-m_s r)/r`. Multiplying the Einstein weak
metric by `F0/F` produces the stated Jordan time/spatial potentials with
`1+alpha^2` and `1-alpha^2`. Their ratio is
`gamma=(1-alpha^2)/(1+alpha^2)` in the long-range regime. The inverse requires
the same weak-source/environment contract and `gamma>-1`; it is not a
universal transfer rule for compact bodies or finite-range orbital forces.

At fixed conservative product `p`, the effective charges `(a,p/a)` have
`DeltaAlpha^2=(a-p/a)^2` and
`alpha_Q=(a m2+p m1/a)/M`. These are nonconstant functions of `a`; discrete
exchange coincidences do not remove the degeneracy. This is a degeneracy of
effective source parameters, not proof that every pair is realized by a body
solution of one selected action.

The substitution into the dependent siren relation is algebraically
`Dchirp/DL=(1+chi2/(6D0))/sqrt(Fs/Fo)`. It inherits the independently needed
tensor-propagation and source/readout contract. The bridge itself is checked
elsewhere; this calculation does not establish a real source's applicability.

## Scope concern to test independently

The sentence declaring every negative `m_s^2` a constant-background instability
is broader than the flat local calculation warrants. A negative value excludes
the stable positive-mass flat-space threshold, but curvature/boundary conditions
can control the long wavelengths responsible for a tachyonic inference.

A concrete potential counterexample to the unqualified wording is a constant
scalar on AdS4 of radius L with `m_s^2=-2/L^2`. Under the standard reflecting
branch, the reduced scalar radial operator has

    -d^2/dchi^2 + ell(ell+1)/sin^2(chi)

on `0<chi<pi/2`, with vanishing endpoint data; it is nonnegative. This follows
from the general AdS potential
`ell(ell+1)/sin^2(chi)+(m_s^2 L^2+2)/cos^2(chi)`.
The same action class can realize the point with `D0>0` and
`W(u)=(-3/L^2)exp(u)-D0 u^2/(2L^2)`, `u=log(F/F0)`: the equilibrium condition
holds, the curvature is `-12/L^2`, and the scalar mass is `-2/L^2`.
This does not create a positive-mass radiation threshold; it challenges only
an unconditional curved-background instability inference. The safer statement
is explicitly about the flat, constant-coefficient approximation and its
validity scale. The proposed AdS operator will be derived before relying on
this as a finding.
