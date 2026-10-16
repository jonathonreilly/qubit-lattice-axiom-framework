# Deriving the weak-source loss term from the same scalar action

Status: exploratory conditional-support; root author. This extends the
source obligation in SCALAR_SIREN_BRIDGE_v1.md. It selects no potential,
normalization or hidden initial state. Standard weak-field scalar radiation
is rederived to identify exactly where the earlier nuisance can be closed.
No compact-binary observation is treated as a weak-body experiment by fiat.

## 1. Local charge follows from minimal matter coupling for weak bodies

Retain the supplied F R/2 scalar action with physical Jordan metric g.
Let F0>0 be a nearly constant environmental value, D0=2omega(F0)+3>0.
Use F_star=F0 solely to simplify the local Einstein-frame conversion. A
weakly self-gravitating point body with constant Jordan rest mass m has

 mE(phi)=m sqrt(F0/F(phi)),
 beta=d log mE/dphi=-1/sqrt(2F0 D0),
 alpha=sqrt(2F0) beta=-1/sqrt(D0).                         (1)

The scalar charge in the canonical equation is q=beta m. Thus the charge
is not an extra chosen parameter in this weak-body limit. Finite binding
energy, screening, composition dependence or an extended body can change
its effective charge; none is removed by(1). Strong-body effective masses
mA^E(phi) instead require their own internal solution. Define
alpha_A=sqrt(2F0) d log mA^E/dphi without claiming it is known.

With GT=1/(8pi F0), canonical scalar exchange contributes
-GT alpha1 alpha2 m1m2 exp(-m_s r)/r. In the leading long-range limit
m_s r<<1, the orbital coefficient is Gc=GT(1+alpha1 alpha2). Corrections
from a finite scalar range must be retained when that limit fails.

## 2. Scalar luminosity from direct multipole expansion

Assume an isolated circular Newtonian orbit, constant effective charges,
nonrelativistic speed v=r Omega<<1 and locally negligible curvature. In the
massless wave zone the canonical retarded field has multipoles

 delta phi=-[Q+n_i dotD_i+n_i n_j ddotQ_ij/2+...]/(4pi R).

The canonical energy flux is R^2 int(d_t delta phi)^2 dOmega. Constancy
of the monopole and circular trace leaves the leading dipole and quadrupole.
The angular integrals int n_i n_j=4pi delta_ij/3 and
int n_i n_j n_k n_l=4pi(delta_ij delta_kl+delta_ik delta_jl
+delta_il delta_jk)/15 give

 P_scalar,dipole=Dddot_i Dddot_i/(12pi),
 P_scalar,quadrupole=Q'''_ij,STF Q'''_ij,STF/(120pi).        (2)

For source masses m1,m2, mu=m1m2/M and a circular relative separation r,

 D=sqrt(4pi GT) mu(alpha1-alpha2) r_vector,
 Q_ij,STF=sqrt(4pi GT) alpha_Q I_ij,
 alpha_Q=(alpha1 m2+alpha2 m1)/M.                         (3)

Combining(2)-(3) with the tensor quadrupole flux derived in the preceding
note gives the leading positive loss fraction

 eta_d=(5/96)(alpha1-alpha2)^2/v^2,
 eta_q=alpha_Q^2/6.                                      (4)

In particular, equal weak-body charges give eta_d=0 but
eta_q=1/(6D0). A vanishing dipole is not a derivation of zero scalar luminosity.
These leading terms do not include post-Newtonian corrections, scalar
monopole evolution, absorption, tidal channels or environmental injection.

## 3. The mass threshold also follows from the action, conditionally

The exact trace/scalar equations yield

 (2omega+3) box F=T+2F V_F-4V-omega_F(partial F)^2.         (5)

In a material vacuum with constant F0, equilibrium requires F0 V_F=2V,
and linearization gives

 m_s^2=2(F0 V_FF-V_F)/(2omega+3).                         (6)

On a flat constant vacuum, a negative value gives growing sufficiently
long-wavelength linear modes. On a curved background, the sign of this local
coefficient alone does not establish a global instability: the geometry,
spectrum and boundary conditions also matter. The flat-space positive-mass
radiation threshold below requires m_s^2>=0. Positive kinetic sign alone
does not guarantee that condition. A material environment adds its own
response to(5).
The local curvature scale R=4V/F must also be small compared with orbital
and wave scales before a flat-space multipole expansion applies.

For a mode frequency nu>m_s, the outgoing wave number is
k=sqrt(nu^2-m_s^2). The far-field expansion of the outgoing Green function
supplies k^ell for multipole order ell, and its radial energy flux supplies
nu*k. Relative to the massless multipole this is

 chi_ell(nu)=[1-m_s^2/nu^2]^((2ell+1)/2), nu>m_s;
 chi_ell=0 below threshold.                              (7)

The dipole oscillates at Omega and the quadrupole at2Omega, so(4) becomes
eta_d chi_1(Omega)+eta_q chi_2(2Omega). The long-wavelength source expansion
needs k r<<1. Conservative long-range dynamics additionally needs m_s r<<1;
otherwise the constant-Gc energy relation in the preceding note cannot be
used unchanged. This is a local, adiabatic linear massive-field calculation,
not a threshold prediction for a nonlinear screened source.

The static inverse reconstructs omega(x),W(x)=V/F, x=log(F/C), where C is
unknown. Since V_F=W+W_x and F V_FF=W_x+W_xx, a constant-field vacuum point
and its mass satisfy

 W_x=W,   m_s^2=2(W_xx-W)/(2omega+3).                     (8)

The unknown constant C cancels. This supplies a cross-domain consistency
relation without inserting an absolute scalar scale. It does not permit
evaluating the static inverse at its singular constant-F chart. One needs
the action functions and derivatives in an independently reconstructed
neighboring field interval and a valid continuation to the candidate vacuum
point. Registration with the actual radiating environment is still required.

## 4. What can now replace the nuisance term

For two weak, unscreened bodies with the common charge(1), no extra energy
channels, and the stated source/propagation limits, the previous relation is

 D_chirp/DL=[1+chi_2(2Omega)/(6D0)]/sqrt(Fs/Fo).            (9)

Here D0 and m_s can in principle come from the same reconstructed action
functions through(8); they are not arbitrary fitted loss parameters. Source
frequency is Omega=(1+z)Omega_o. The measured endpoint ratio would then
register the constants as log(Cs/Co)=log(Fs/Fo)-xs+xo.
This retires free eta only within the weak-source class and with those inputs.
It does not derive the underlying action class or certify a real source.

There is a second independent weak-field input. In the massless/long-range
limit a static weak mass gives

 g00=-1+2GT M(1+alpha^2)/r,
 gij=deltaij[1+2GT M(1-alpha^2)/r],
 gamma_PPN=(1-alpha^2)/(1+alpha^2).

Thus alpha^2=(1-gamma_PPN)/(1+gamma_PPN), and a physically applicable
same-environment measurement of gamma_PPN would bound eta_q=alpha^2/6
without a selected omega. At finite range the potential ratio contains
alpha^2 exp(-m_s r) instead; orbital force includes further radial derivatives.
Identifying potentials with force coefficients or transferring a Solar-System
bound to compact bodies would add assumptions. No such transfer is made here.

For general compact-body charges, measuring a conservative product
p=alpha1 alpha2 does not by itself determine radiation. For any positive
parameter a, alpha1=a and alpha2=p/a keep p fixed but change both the dipole
and alpha_Q. Masses and source histories being equal do not remove this
charge freedom. A body-structure equation, scalar response measurement or
additional waveform information is required; choosing alpha1=alpha2 would
just restore the assumption we are trying to derive.

## 5. Evidence and status

SCALAR_SOURCE_PLAN_v1.json freezes exact angular, conformal, mass, threshold,
inverse-coordinate and charge-degeneracy controls before execution. Synthetic
parameter cases are mathematical examples, not a fit or an empirical test.
The negative-mass control excludes using the healthy flat-space massive
threshold at those parameters; it is not an exclusion of every curved
background. The equal-product/different-luminosity examples separately
exclude determining radiation from the conservative product alone.

Primary background: Bernard, Blanchet and Trestini,
https://arxiv.org/html/2201.10924, include scalar multipoles and effective
body sensitivities. The elementary leading equations here are computed
directly; their full higher-order waveform is neither imported nor reproduced.
No novelty is claimed for weak-field multipole radiation, PPN relations or
massive-wave thresholds. This remains a support calculation, not another
milestone PR. The next physical task is the extended-body scalar response
and the actual environmental mapping, not supplying a compact-body charge.

Version2 narrows the stability statement after focused review: a negative
local mass coefficient alone is insufficient to diagnose a curved vacuum.
Equations and original174controls are unchanged and still bound to v1.
The original broader sentence is preserved in v1; use v2 for current scope.
