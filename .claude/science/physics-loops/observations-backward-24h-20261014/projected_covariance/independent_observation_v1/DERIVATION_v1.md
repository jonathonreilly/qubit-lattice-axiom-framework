# Independent projection and measurement derivation

This derivation was written without reading any root-authored `projected_covariance` working file. It checks the physical supplier and coordinate conventions, not a candidate gravity theory. Its statements are conditional geometry and measurement statements; no fit or observed derivative history is supplied.

## 1. Dictionary and assumptions

Set c=1. Use the physical metric to which the source, observer, and photons couple,

`ds^2 = a^2[-(1+2 Psi)d eta^2 + (1-2 Phi)dx.dx]`,

and define `S=Phi+Psi`, `Phi_W=S/2`, `chi=eta_0-eta`, `N=ln a`, and `mathcalH=a H`. Take a>0 and H nonzero wherever V, alpha or the time-derivative inverses are used. Both potentials and S are dimensionless. A dimensional potential in SI must be divided by c squared before entering this metric. A different sign convention for the spatial potential changes the name of the Weyl combination, not the geometry below.

Assumptions used for the lensing calculation: spatially flat FLRW background; small scalar metric perturbations; the Born ray and linear shear approximation; a supplied background distance-redshift relation; no unmodelled vector/tensor, lens-lens, post-Born, or source/observer corrections. No Poisson equation, no equality `Phi=Psi`, no particular growth factor, and no gravity field equation are needed for the sum-potential relation.

For the velocity calculation, explicitly choose a scalar U by `v_phys=grad_x U/a`, with the spatial gradient at fixed cosmic time. Equivalently, when the covariant spatial four-velocity convention is `u_i=partial_i v_J`, U is v_J to this perturbative order. Then `V=H U` and `v_phys=alpha grad_x V`, where `alpha=1/(a H)`. V is dimensionless and alpha has dimensions of length. If a candidate defines its velocity potential with the opposite gradient sign, every scalar-velocity cross spectrum below changes sign; velocity auto spectra do not. This dictionary is a convention, not a velocity measurement.

## 2. Flat-Born inversion, with its domain

The transverse projection of the perturbed null geodesic equation is `delta x_perp''=-grad_perp S` along the background ray. The transverse parts of `Gamma^i_00` and `Gamma^i_jk n_j n_k` give the gradients of Psi and Phi respectively; terms proportional to the ray direction drop out. Integrating with the observer direction fixed gives the angular lensing potential

`varphi(chi_s,n)=integral_0^chi_s d chi [(chi_s-chi)/(chi_s chi)] S(eta_0-chi,chi n)`.

The lens map is `beta=theta-grad_Omega varphi`. Thus the tracefree angular Hessian of varphi gives the shear. Define the light-cone restriction `S_LC(chi,n)=S(eta_0-chi,chi n)` and

`D_chi = partial_chi [chi^2 partial_chi]`.

Differentiating the integral with respect to **source distance**, keeping n fixed, first gives

`partial_chi_s varphi = chi_s^(-2) integral_0^chi_s S_LC(t,n) dt`.

Consequently

`D_chi varphi = S_LC`, or equivalently `chi partial_chi^2(chi varphi)=S_LC`.

The result is S, not S/2. Taylor's single-potential convention has `S=2 Phi`, hence his inverse for Phi has an additional one-half. This factor must also be squared if both covariance legs are expressed as Phi_W instead of S.

Regularity must justify the integral and differentiation. For the observable smooth angular multipoles with ell>=2, regularity at the observer gives the appropriate vanishing radial behaviour. One can instead work strictly inside a source-distance interval and keep the lower-bound foreground terms explicit. Foreground material below that interval contributes `A(n)+B(n)/chi` to varphi and is annihilated by D_chi. Thus local inversion inside a continuously sampled interval does not require pretending that all foreground structure is separately reconstructed. Gaps, a finite set of source bins, and the lack of sources beyond the survey limit still prevent an arbitrary continuous radial reconstruction.

On a full sphere, with the usual complex spin-2 shear convention,

`gamma_E,ellm(chi_s)=L_ell varphi_ellm(chi_s)`,

`L_ell = (1/2) sqrt[(ell-1)ell(ell+1)(ell+2)]`.

For ell>=2 the ideal inverse is `S_LC,ellm=D_chi gamma_E,ellm/L_ell`. The spin-2 operator annihilates ell=0 and ell=1. Shear alone does not determine those angular modes at any source distance. These are angular null modes around the observer, not simply the spatial Fourier mode k=0. Declaring a mean or dipole to vanish is a boundary/statistical convention, not recovery of its realised value.

On a flat patch the tracefree Hessian has the local kernel

`a(chi)+b_1(chi)theta_1+b_2(chi)theta_2+c(chi)(theta_1^2+theta_2^2)/2`.

The last term changes convergence by c while leaving linear shear zero. Constant and linear terms change neither shear nor convergence. This patch statement must not be confused with a complete-sphere harmonic decomposition. A mask introduces additional boundary and E/B mixing issues. Reduced shear `g=gamma/(1-kappa)` has its own mass-sheet ambiguity; treating g as gamma is the explicitly weak, first-order approximation. Magnification can add convergence information only with its own source-population calibration.

## 3. Windowed fields and two-point projection

For a calibrated source sample i, let `n_i(chi_s)` be its normalized **true-distance** distribution after the observed-redshift selection and the conditional redshift-error distribution have been applied. Then

`W_i^L(chi)=integral_chi^infinity n_i(chi_s)(chi_s-chi)/(chi_s chi) d chi_s`,

`gamma^i_E,ellm=L_ell integral d chi W_i^L(chi) S_LC,ellm(chi)`.

A finite collection of these kernels supplies weighted integrals, not arbitrarily many point values of S. A nonsingular continuum inverse is a stronger idealization than a finite tomographic measurement. The true-distance distribution and chi(z) are part of the calibration/model, not obtained automatically from the shear.

Define the unequal-time spectra by

`<A(k,N1) B*(k',N2)>=(2 pi)^3 delta_D(k-k') P_AB(k;N1,N2)`.

Assume statistical homogeneity and isotropy of the underlying spatial fields at each pair of times, with the parity-even scalar sector. A common transfer function is not assumed. Angular integration of a plane wave gives the following light-cone shell covariances:

`C_ell^SS(chi1,chi2)=(2/pi) integral dk k^2 j_ell(k chi1) j_ell(k chi2) P_SS(k;N1,N2)`,

`C_ell^Su(chi1,chi2)=(2/pi) integral dk k^2 j_ell(k chi1) alpha2 k j_ell'(k chi2) P_SV(k;N1,N2)`,

`C_ell^uu(chi1,chi2)=(2/pi) integral dk k^2 alpha1 alpha2 k^2 j_ell'(k chi1) j_ell'(k chi2) P_VV(k;N1,N2)`.

Here `u=n.v_phys`, `Na=N(eta_0-chi_a)`, and the primes on j are derivatives of its argument. The k factors and the alpha factors are essential. The velocity operation is a **spatial** derivative at the fixed time of its own leg; it does not differentiate the unequal-time spectrum with respect to that time. No extra common-growth premise has been hidden in these kernels.

For example, the binned shear covariance is

`C_ell^(gamma_i gamma_j)=L_ell^2 integral d chi1 d chi2 W_i^L(chi1) W_j^L(chi2) C_ell^SS(chi1,chi2)`.

The shear-radial-velocity cross covariance uses one lensing kernel, one velocity selection kernel, and `C_ell^Su`; the radial-velocity auto covariance uses two velocity kernels and `C_ell^uu`. A mask and angular weights further mix ell,m. A catalogue's density-dependent sampling is not automatically a deterministic, unbiased volume-weighting operation: its selection and tracer weighting must be modelled or corrected.

If continuous source-plane covariances are supplied, sufficiently smooth, and noise/systematic terms have been separated, differentiation can be applied to each lensing leg:

`C_ell^SS = D_1 D_2 C_ell^(gamma_E gamma_E)/L_ell^2`,

`C_ell^Su = D_1 C_ell^(gamma_E u)/L_ell`, for ell>=2.

These return covariances of light-cone shell fields in the observable angular subspace. They do not return individual spatial Fourier amplitudes, the velocity-potential spectrum, or fixed-k time derivatives without further inversion. Recovering a spatial spectrum from a correlation function ordinarily needs the full separation range, or an explicitly finite basis/window model; finite angular and radial extent does not provide that range automatically.

In matrix language, a calibrated linear measurement has `C_obs=K C K^dagger+N`, with additional intrinsic-alignment/calibration terms and cross terms unless they are demonstrably absent. Differentiation or inversion acts on the noise covariance too. A time derivative also has `K' C K^dagger+K C K'^dagger+N'`; differentiating observed bands while ignoring their evolving kernels does not isolate C'. No Gaussian likelihood is needed for these second-moment identities.

## 4. What radial velocities can and cannot substitute for

Under the scalar-flow convention above,

`u=alpha partial_chi^spatial V`,

whereas `d V_LC/d chi=partial_chi^spatial V-partial_eta V`.

Thus integrating observed u along the ray without a time-evolution term is generally not a reconstruction of V on that ray. On a single, simultaneous three-dimensional domain an irrotational velocity can instead be integrated radially, subject to its angular integration functions and boundary/regularity conditions. The same statement is not automatically valid on an evolving light cone. Non-potential tangential motions are also not supplied by radial data alone.

For two positions `x_a=chi_a n_a`, set `s=x2-x1`, `s=|s|`, `mu=n1.n2`, and `p_a=n_a.s_hat`. Statistical isotropy of a parity-even vector field gives

`<v_1i v_2j>=Psi_perp delta_ij+(Psi_parallel-Psi_perp)s_hat_i s_hat_j`,

so

`<u1 u2>=mu Psi_perp+p1 p2(Psi_parallel-Psi_perp)`.

For a scalar potential, with `xi_VV=<V1 V2>` and spatial derivatives at fixed N1,N2,

`Psi_perp=-alpha1 alpha2 xi_VV,s/s`,

`Psi_parallel=-alpha1 alpha2 xi_VV,ss`.

Similarly `<S1 u2>=alpha2 p2 xi_SV,s`. These signs follow by differentiating with respect to x1 and x2, which have opposite effects on the separation vector. The notation here separates sightlines from separation directions; it is not a literal reuse of the overloaded unit-vector notation printed around Wang Eqs. (4)-(5).

Wang's two pair statistics have expectation `psi1=A Psi_parallel+(1-A)Psi_perp` and `psi2=B Psi_parallel+(1-B)Psi_perp` under their common correlation/selection approximation. Their algebraic inverse requires `A-B!=0`. Different sightline geometries can supply the two combinations; sufficiently narrow separation/time bins and an appropriate sampling model are also required.

There is a useful exact restriction on an infinitesimally thin equal-time shell. If `chi1=chi2=chi`, then `p1=-s/(2chi)`, `p2=s/(2chi)` and `mu=1-s^2/(2chi^2)`. At a fixed s all pairs therefore have the same geometric coefficients: the two-statistic design has A=B wherever those ratios are defined. In this ideal shell alone they are not two independent measurements of an arbitrary vector covariance.

In the scalar-flow case the same-shell quantities reduce to

`<S1 u2>=alpha s xi_SV,s/(2chi)`,

`<u1 u2>=alpha^2 [s^2 xi_VV,ss/(4chi^2)-(1-s^2/(4chi^2)) xi_VV,s/s]`.

The potential-flow relation `Psi_parallel=d(s Psi_perp)/ds` can be used as an additional spatial differential constraint. Recovering xi_VV then becomes a differential inverse with its boundary, regularity, zero-mode and spectral-positivity conditions to be stated and checked. This review does not claim that all such inverses are impossible or that regularity alone proves uniqueness. Adding other radii supplies new geometric leverage but also different emission times; an exact treatment must retain that evolution rather than silently treating the catalogue as one time slice.

## 5. Time derivatives versus changing radius

For an unfiltered scalar covariance under homogeneity/isotropy, write

`C_LC(chi1,chi2,mu)=xi_AB(N1,N2;s)`,

`s^2=chi1^2+chi2^2-2chi1 chi2 mu` and `dN/dchi=-mathcalH`.

The exact chain rule is

`partial_chi1 C_LC = -mathcalH1 partial_N1 xi + [(chi1-chi2 mu)/s] partial_s xi`,

`partial_mu C_LC = -(chi1 chi2/s) partial_s xi`.

Therefore, in the interior of the accessible triangle domain,

`partial_N1 xi|_(N2,s) = -(1/mathcalH1)[partial_chi1 + (chi1-chi2 mu)/(chi1 chi2) partial_mu] C_LC`,

with the analogous second-leg expression. The domain is `|chi1-chi2| < s < chi1+chi2`, with nonzero radii and the needed derivatives existing. Thus it would be too strong to say that a light cone can never inform a fixed-separation time derivative. Ideal continuous, calibrated **scalar** covariances plus statistical homogeneity/isotropy permit this geometric conversion wherever those derivatives are identifiable. That is not a measurement of the same individual object at two epochs.

On an equal-radius shell at fixed angular separation,

`d C_shell/dN|_mu = (partial_N1+partial_N2)xi|_equal - [s/(mathcalH chi)] partial_s xi`.

The equal-time, fixed-comoving-separation total derivative therefore adds back the spatial term. Equivalently one follows `mu(N)=1-s^2/[2chi(N)^2]`, changing angle to keep s fixed. At fixed ell an angular spectrum also changes its characteristic spatial scale as chi changes; it is not a fixed-k spectrum derivative.

For cross covariances the total equal-time derivative does not by itself separate the two time legs. Auto covariances can have the two legs equal by exchange symmetry, but that does not supply the missing derivative of a different field. A light-cone *partial* derivative with one radius changed is not already the desired single time leg either; the angular correction above is necessary.

These scalar identities cannot be applied blindly to the observed radial-velocity covariance: its p_a, mu, alpha_a and sampling kernels also change. Nor do they restore the shear's missing ell=0,1 covariance. A projected construction must carry its projection and calibration operators, or explicitly supply the unprojected scalar covariance required by the formulas.

## 6. Measurement contract and source comparison

Real input is a set of galaxy shapes, redshifts and calibrated distance indicators, not smooth S,V fields. A usable lensing supplier must specify shear response and additive/multiplicative calibration, point-spread-function correction, intrinsic alignments, angular mask, source sampling, true-distance distributions and redshift errors, smoothing and the full propagated covariance. The inverse's radial second derivatives amplify small-scale noise; choosing a regularization/basis is an additional reconstruction assumption.

A velocity supplier must specify the physical rest frame and observer correction, distance-indicator zero point, background H and chi(z), redshift errors, peculiar-velocity estimator, selection and distance-error bias treatment, tracer/velocity weighting, nonlinear dispersions and correlated calibration errors. At low redshift `u approximately cz-H0 d` illustrates why a distance zero point and H0 affect inferred radial flows. At finite redshift even the first-order Doppler relation uses `(1+z_obs)=(1+z_cos)(1+u/c)` after the appropriate observer correction; relativistic and gravitational terms need a stated treatment. Spectroscopic redshift by itself does not separate background recession and peculiar motion.

The primary comparison is narrow. [Taylor v1](https://arxiv.org/pdf/astro-ph/0111605v1), Eqs. (3)-(5), (9)-(18), supplies the flat-Born radial relation, angular inversion and its single-potential convention. [Heavens v2](https://arxiv.org/pdf/astro-ph/0304151v2), Secs. 2.2-2.5, explicitly includes photometric distance mixing, an angular mask, source weighting and shape noise; its density forecast also assumes a common growth history and Poisson mapping. [Wang et al. v1](https://arxiv.org/pdf/1808.07543v1), Secs. 3-5, supplies the radial pair geometry, geometric denominator and finite-catalogue calibration/variance context. Their subsequent linear-density model, numerical calibrations and cosmological fits are not inputs here. None of those conditional forecast/estimator choices is promoted to an observed continuous covariance or derivative history.

The independent script checks 43 exact projection/geometry identities and discriminates six deliberately incorrect alternatives. Those are internal controls of this derivation; they are not empirical experiments or validation of the root's not-yet-read construction. Source versions, exact reading scope and artifact hashes are recorded separately.
