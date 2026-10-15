# Shear and radial velocity: a light-cone covariance constraint

Working direct-author derivation, 2026-10-15. Status: open pending independent
checks. Intended type: bounded_theorem; trace: upstream_support/supports.
This is not yet a measured-data test or an action/state selection result.

## Target and allowed premises

The M14 momentum inverse requires equal-time potential covariances and their
derivatives. Its exact full rolling equations were independently checked at
commit f3637a4eba3fb18690fe6a2b03d9455c60cc6363. Here the new target is to
eliminate the velocity-potential reconstruction and the unobservable shear
monopole/dipole, using directly radial velocities and shear tomography.
The landed initial-state covariance note already proves generic transfer
feasibility; that result is not this target. Main bbada1fe and planning
3a4b2c66 are unchanged; source and search records are adjacent.

Explicit conditions: flat smooth expanding FLRW physical background, linear
scalar perturbations, the M14 canonical-scalar/conformal-dust dynamics,
irrotational proper peculiar velocity, finite smooth real homogeneous isotropic
equal-time covariance functions, calibrated distance/time and velocities,
full-sky continuum source-distance shear in the first-order Born approximation,
and signal covariances separated from additive/calibration/selection errors.
These conditions are not inferred from the axioms or asserted for ACT/BOSS.
No Gaussianity, single growing seed, common transfer, selected scalar initial
state, velocity-potential boundary condition or potential power spectrum is
prescribed. Initial amplitudes and scalar waves remain free.

Alternative routes: (i) Fourier deprojection needs finite-volume completion;
(ii) direct potential integration needs a radial boundary term;
(iii) local differential elimination may avoid both; (iv) transverse proper
motions could supply additional velocity components; (v) full forward window
likelihood avoids exact deprojection but still needs instrument kernels.
Only (iii) is developed here. No exclusion of the other routes is claimed.

## 1. Kinematics on an equal-distance shell

N=ln(a), H=H_J, V=H v_J, S=Phi_J+Psi_J, and u=n.grad(v_J)/a are used.
Coordinates are comoving; c=1. Put chi=chi(N)>0, chi_N=-1/(a H),
r=|chi n1-chi n2|=chi sqrt(2(1-mu)), and restrict 0<r<2chi.
For C_AB(N,r)=E[A(x1)B(x2)], rotational invariance makes scalar cross
covariances symmetric. At fixed N, differentiating the separation gives

    C_Su = r/(2 a H chi) * partial_r C_SV,
    a^2 H^2 C_uu = alpha partial_r^2 C_VV
                       -(1-alpha) partial_r C_VV/r,
    alpha=r^2/(4 chi^2).

The second formula follows from minus the separation Hessian of C_VV:
n1.rhat=r/(2chi), n2.rhat=-r/(2chi), n1.n2=1-2alpha.
Define D=partial_r/r, K=r partial_r, and E=alpha(K+2)-1. Thus

    d = 2 a H chi C_Su/r^2 = D C_SV,
    U = a^2 H^2 C_uu = E D C_VV.

The homogeneous equation E f=0 has f proportional to
r^(-2) exp(-2chi^2/r^2). Smoothness at zero alone therefore does not fix the
radial integration constant. This is an operator-kernel observation, not a
claim that arbitrary such changes are globally admissible PSD spectra.

For observed angular functions, the equal-time derivative at fixed comoving
separation is

    partial_N|r = partial_N|mu + 2(1-mu)(chi_N/chi) partial_mu.

Changing distance at fixed angle is not that derivative. Define
g=-2chi_N/chi. Then E_N=g(E+1) as operators at fixed r.

## 2. Eliminate the unmeasured radial potential

Let P=(K+2)K(K-2)(K-4), with every factor acting on what follows it.
At each N define the following six processed signal functions:

    A  = P E^2 D C_SS;         A1 = P E^2 D (partial_N C_SS),
    B  = P E^2 d;              B1 = P E^2 (partial_N d),
    C  = P E U;                C1 = P[E partial_N U-g(E+1)U].

All N derivatives here hold r fixed, including those of the factors a,H,chi
inside d,U. A1,B1,C1 are input derivative functionals, not ordinary derivatives
of A,B,C. E and P do not commute; the displayed order is part of the claim.

For Q=P E^2 D, these equal (Q C_SS,Q C_SV,Q C_VV) and
(Q partial_N C_SS,Q partial_N C_SV,Q partial_N C_VV). The nontrivial identity is

    E^2 D partial_N C_VV
      = E partial_N U - g(E+1)U,

obtained by differentiating U=E D C_VV before applying E. It does not solve
the radial ODE or set its homogeneous solution to zero.

## 3. Shear tomography and angular null modes

In the stated flat first-order Born convention, define the lensing potential

    psi(s,n)=integral_0^s (s-chi)/(s chi) S(N(chi),chi n) dchi.

The shear spin-2 harmonic is gamma_lm=0.5 sqrt((l+2)!/(l-2)!) psi_lm for l>=2.
Its scalar reconstruction has no information about l=0,1. Nevertheless,

    S_lm(s)=partial_s[s^2 partial_s psi_lm(s)], l>=2.

This radial derivative follows the past light cone; it is not partial_N S
at a fixed point. The subsequent equal-time covariance derivative is supplied
by the shell geometry in section1. Differentiating two source arguments of a
shear covariance is required for C_SS; one for a shear/velocity covariance.

An isotropic covariance after removing l=0,1 differs by A0(N)+A2(N)r^2.
Consequently C_SS has that ambiguity, d has a_-2(N)/r^2+a_0(N), and U has
b_0(N)+b_2(N)r^2. Since E^2(1)=8alpha^2-4alpha+1 and
E^2(r^-2)=r^-2, P annihilates every resulting ambiguity in A,B,C,A1,B1,C1.
The same result holds if low multipoles are also removed from radial velocities.
No angular null coefficient is selected or inferred. Masks or other missing
multipoles need a new operator; they are not covered by this full-sky result.

## 4. Necessary coefficient constraint

For the supplied M14 dynamics put x=F_N/F, y=x/q, h=H_N/H,
J=3 exp(-3N)/(H/H0)^2 and m=J R. The physical fields obey

    S_N-y V_N = a0 S+c0 V,
    a0=(y-x-2)/2, c0=-h y-m.

Multiplication by S-yV at separated points and symmetrization, with y held
as a coefficient, yields

    (C_SS,N-2y C_SV,N+y^2 C_VV,N)/2
       =a0 C_SS+(c0-a0 y)C_SV-c0 y C_VV.

Because all coefficients depend on N only, Q preserves this identity. Thus
the six processed shear/radial-velocity functions supply the row

    [A/2, -A/2-B1+(h-1)B, C1/2+B/2-h C, B, -C]
      dot [x,y,y^2,m-xy/2,my] = -A1/2-A.

At a regular epoch, five linearly independent separation/weight rows identify
the lifted vector, followed by its two monomial consistency tests. This is a
sufficient rank condition, not a guarantee that a measured survey has rank,
not a minimum-data theorem, and not full-history compatibility. Zero roll and
other M14 inverse-domain restrictions still apply. Q is not positivity
preserving; A,B,C are processed correlations, not a PSD covariance matrix.

## 5. Open checks and actual observation boundary

Need independent geometry/operator proof, exact noncommutation/null controls,
nonzero-rank admissible homogeneous ensembles, full rolling synthetic forward
comparison, and a weak finite-window form. High radial derivatives may make
this pointwise construction impractical. No stability bound for a survey is
asserted. A finite collection of source/redshift bins does not by itself supply
the continuum differentiable inputs. Lens bias, intrinsic alignments, velocity
distance calibration, masking, noise and nonlinear/lensing corrections remain
explicit measurement obligations. No new data are admitted and no empirical
fit is performed. The supplied action, absolute normalization, environment and
realized history remain unselected.
