# Independent scalar principal cone and tidal readout

Pre-author-exposure derivation. Inputs are solely the neutral assignment: signature(-+++), X=-gE^{mu nu}phi_mu phi_nu/2>0, action M²RE/2+P(phi,X), positive smooth conformal A, regular rolling homogeneous background, and the specified no-linear-anisotropic-stress nonzero spatial scalar sector. No new root kinetic note/code or other checker's derivation has been read. This is conditional mathematics, not empirical identification or a novelty claim.

## 1. Principal symbol from variation, and an alternate quadratic-action route

Varying phi and integrating once gives div(P_X grad phi)+P_phi plus the conformal matter trace source. The trace source contains no second phi derivatives for ordinary nondifferential conformal matter coupling. Expanding the divergence, the scalar second-derivative coefficient is

    G^{mu nu}=P_X gE^{mu nu}-P_XX grad^mu phi grad^nu phi.

The scalar principal covector condition is G^{mu nu}xi_mu xi_nu=0. Lower-order terms contain P_phi, P_Xphi, background gradients, mass and matter sources. In a local homogeneous Einstein-frame orthonormal rest chart, dot(phi)=v, 2X=v², so

    G^{00}=-(P_X+2X P_XX)=-K,   G^{ij}=P_X delta^{ij}.
    K omega_E²-P_X |k_E|²=0,  c_s²=P_X/K.

Independent derivation: expand X about phi=v t with perturbation pi. Then delta X=v pi_dot+[(pi_dot)²-|grad pi|²]/2. The quadratic derivative Lagrangian is [K(pi_dot)²-P_X|grad pi|²]/2, reproducing the same symbol without using the expanded equation. Background variation affects only lower-order/WKB transport terms.

Strict healthy scalar hyperbolicity in this rest chart requires K>0 and P_X>0. X>0 alone does not imply either. K=0 is a degenerate kinetic equation; P_X=0 gives a degenerate spatial principal part. Both negative coefficients can leave a real ratio but give a ghost relative to the positive gravitational kinetic convention. No upper bound c_s<=1 follows from the stated action alone. The Einstein metric principal sector has its separate tensor null cone; using it as the scalar cone would impose an extra condition.

At a point, physical rods/time for gJ=A²gE scale alike: omega_J=omega_E/A and k_J=k_E/A. Hence their ratio and c_s are unchanged. This is an exact conformal relation between local cones, not a claim that A is constant globally. On an evolving background extracting this principal cone from finite waves requires wavelengths/periods short against background/coefficient scales, correct mode selection and controlled lower-order contributions. Standard Einstein equations have second metric derivatives while their P stress has at most first phi derivatives; the scalar equation has first metric derivatives through the connection. Thus the coupled principal system does not identify the scalar and tensor cones merely because gravity is present. Matter derivative couplings or extra propagating sectors require their own principal-system analysis.

## 2. Linear conformal potentials before any metric-potential neglect

In a common conformal-time Newtonian scalar gauge write

    dsE²=aE²[-(1+2PsiE)deta²+(1-2PhiE)dx²].

For nonzero spatial modes with zero total linear anisotropic stress, the traceless Einstein equation gives PsiE=PhiE=U. This needs the specified sector; it is not valid for arbitrary matter stress. With s=delta ln A in this same gauge and aJ=Abar aE, linear conformal multiplication gives exactly

    PsiJ=U+s,  PhiJ=U-s,  s=(PsiJ-PhiJ)/2.

No assumption U=0 is used. For a rolling background delta phi and s alone are slicing-dependent; these equations refer to Newtonian-gauge perturbations, or equivalently their corresponding gauge-invariant completions. The physical Bardeen potentials are the corresponding gauge-invariant readout variables. A homogeneous/time-redefinition mode cannot be recovered by importing a nonzero-k inverse.

This slip can in principle isolate s independently of U if BOTH physical potentials have been reconstructed under a calibrated measurement map. Ordinary lensing measures their sum, which is 2U here, so lensing alone cancels s rather than measuring it. A channel proportional to only one potential or one transverse tidal component is likewise insufficient without more information.

## 3. Direct curvature calculation and tidal inversion

Fix curvature convention

    R_{0i0j}=1/2(h_{0j,i0}+h_{i0,0j}-h_{00,ij}-h_{ij,00})

at linear order about a local Minkowski metric. For h00=-2PsiJ, hij=-2PhiJ deltaij, h0i=0,

    R_{0i0j}=partial_i partial_j PsiJ+deltaij partial_0² PhiJ.

A globally opposite Riemann convention flips both calibrated measured amplitudes and must be treated consistently. Let a single Fourier component be exp[i(k z-omega t)] in physical local coordinates, with k and omega real and nonzero. Let T denote either scalar transverse component (or the transverse average after tensor separation), and L the longitudinal component. Then

    T=-omega²(U-s),
    L=-k²(U+s)-omega²(U-s).

Solve, retaining U:

    PhiJ=-T/omega², PsiJ=-(L-T)/k²,
    s=1/2[T/omega²-(L-T)/k²],
    U=-1/2[T/omega²+(L-T)/k²].

The 2x2 map from (U,s) to (T,L) has determinant 2 omega² k². Therefore the two phase-resolved, relatively calibrated amplitudes isolate s in this frozen operator precisely away from omega k=0. At omega²=k², T-L/2=k²s: the common Einstein potential cancels, but the equality omega²=k² must not be inserted just because tensors or photons are luminal.

The conformal-potential relation is exact at first perturbative order on the supplied background. The displayed Riemann/plane-wave inversion is exact for the frozen flat-background linear operator. It is NOT an exact FLRW finite-frequency curvature formula. Evolving-frame tetrads, background curvature, observer motion, scale-factor derivatives and variation of A add terms of orders H omega and H² (and analogous background rates) relative to the wave's omega² or k² terms. Their subtraction or an asymptotic hierarchy is a separate physical requirement. Direct geodesic-deviation curvature readout, propagation direction, k, omega, scalar/tensor separation, source registration and complex relative calibration are supplied measurement conditions. Squared amplitudes without relative phase do not implement this complex linear inverse.

## 4. Identification failures that survive the algebraic map

Even perfect tidal inversion of s is not by itself identification of the free scalar principal cone. At alpha=d ln A/dphi=0, s=alpha delta phi vanishes at linear order regardless of the scalar principal speed; a constant A is an exact permitted blind example. If alpha is nonzero but unknown, s is locally proportional to the scalar perturbation and shares its leading eikonal phase, but its amplitude does not calibrate delta phi. A vanishing alpha or rapidly varying readout invalidates naive mode tracking. A mixture of scalar eigenmodes, driven matter response or an externally forced metric perturbation is not automatically a freely propagating scalar branch.

A concrete finite-frequency ambiguity is the stable frozen scalar equation pi_tt-c_s² pi_zz+m_eff² pi=0. At one measured nonzero k, omega²=c_s² k²+m_eff². The same luminal-looking omega=k can come from c_s²=1,m_eff=0 or c_s²=1/2,m_eff²=k²/2. Both allow the same nonzero s amplitude after preparation/coupling adjustment, and the tidal map itself supplies no mass measurement. This is a frozen-mode counterexample to inference of the principal coefficient from one phase speed; it does not assert two globally matched cosmologies. With arbitrary forcing even a chosen finite dispersion curve is not sufficient absent branch/source assumptions. The strongest supported conclusion is an explicit remaining physical identification obligation, not a universal no-go theorem.

Conversely a demonstrated asymptotic scalar cone with c_s=1, X>0 and nondegenerate P_X implies P_XX=0 on the probed background points. It does not identify P=X-V, fix field normalization or determine an off-trajectory action. P=F(phi)X-V(phi) with F>0 is luminal; appropriate local field redefinition changes its normalization and conformal coupling. Terms proportional to [X-X0(phi)]³ leave the action's two-jet along X=X0(phi) unchanged but change off-trajectory nonlinear dynamics. Cone/readout data therefore constrain combinations inside a supplied class, not the full action.

## Predeclared exact controls

Before code: independently expand a polynomial P to quadratic derivative order; build linear Riemann directly from the metric perturbation; invert the two-channel matrix for arbitrary U,s,k,omega; include nonzero-U and nonluminal numerical rational witnesses; demonstrate zero-k/zero-frequency rank loss, zero-coupling blindness, lensing cancellation, finite-mass ambiguity, conformal speed invariance and a noncanonical luminal kinetic family. No author result will be used as an expected value. Runs will be bytecode-disabled and bounded by120seconds. Actual failures will remain preserved.
