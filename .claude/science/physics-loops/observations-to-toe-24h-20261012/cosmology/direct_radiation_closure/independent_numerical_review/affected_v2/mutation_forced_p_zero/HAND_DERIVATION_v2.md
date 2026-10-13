# Direct radiation consistency and reconstruction — unexecuted derivation

Parent calculation, written before symbolic/numeric execution. This is a
candidate calculation pending checks, not a certified negative claim or
empirical success. The existing dust potential is tested with its parameters
unchanged. A separate radiation-aware potential, if successful, is a new
model-development construction, not a prediction of that earlier potential.

Use the same action R-2(du)^2-2(dchi)^2-4V, A=exp(sqrt(a)u), a>0, G_*>0.
Add an ideal positive radiation fluid with p=rho/3 and separately conserved
Einstein radiation density. Write S=4pi G_*rho_m, R=4pi G_*rho_r and L=V_L.
Here S and R have dimensions H^2. A=1 on the proposed u=0 trajectory.
Radiation couples through the metric; its vanishing trace gives no direct
scalar source. The supplied photon statistics and massless dispersion, plus
adiabatic conservation, are explicit thermodynamic premises. No photons,
initial entropy, baryon abundance or neutrino distribution are derived.

Observed CMB temperature is a development input. Fixsen2009 Table2 gives a
combined determination 2.72548+/-0.00057K; it is not solely the paper's new
WMAP/FIRAS differential fit, which is2.7260+/-0.0013K. NASA's posted monopole
spectrum uses an explicitly supplied2.725K baseline plus earlier residuals;
it cannot independently validate that baseline. Do not treat its published
per-bin errors as a full independent covariance likelihood.

## Test the unchanged dust potential

Existing V=L+S(chi)[(u-sqrt(a))^2+eta u^2]/2 has
S=c sinh^2[k(chi-chi_c)], c=L/(1+a), k^2=3(1+a)/(2a), left branch.
The u=0 equation forces matter density to equal the same function S.
Conservation then forces Sdot=-3HS and Rdot=-4HR, hence R=b S^(4/3), b>0.
Writing Hbar^2=2[(1+a)S+L]/3 and B=(2+a)S+2L,
S_chi=-3Hbar sqrt(S/a) and chidot=(H/Hbar)sqrt(aS).
Friedmann therefore forces F=H^2=Hbar^2[1+2R/B]. Its derivative and
Raychaudhuri must agree:

  Hdot_from_F=-(3S/2) F_S-2R F_R,
  Hdot_Ray=-S-4R/3-aS F/Hbar^2,
  Hdot_from_F-Hdot_Ray=2aRS[(2+a)S-L]/(3B^2).

If this identity is confirmed, it is nonzero on a positive-density open
interval except at one isolated S. It concerns ONLY the exact u=0 trajectory
of this unchanged potential with positive conserved radiation. It does not
exclude approximate solutions, drifting u, another potential, variable
coupling, extra fields, curvature or another thermodynamic history. It is not
an observed exclusion of the full two-field family.

## A separately reconstructed radiation-aware potential

Choose positive b,L and a>0; R(S)=b S^(4/3), W=S+4R/3,
C=(1+a)(S+R)+L and Hbar^2=2C/3. Specify

  chidot=sqrt(aW), Sdot=-3Hbar S,
  dS/dchi=-3Hbar S/sqrt(aW),
  U(S)=L+(a/2)S+(a/3)R.

The coordinate chi(S) is given by the monotone integral and is locally
invertible for S>0. These statements define one background from an exposed
expansion target, not a uniqueness theorem. On u=0, put

  V(u,chi)=U(S(chi))-sqrt(a)S(chi)u+M(S(chi))u^2/2.

Friedmann, Raychaudhuri, matter/radiation conservation and both scalar
background equations should then hold exactly. In particular V_u=-sqrt(a)S
cancels the matter source, while
chidotdot=-a Hbar(3S+16R/3)/(2 chidot) and
U_chi=-a Hbar(3S/2+4R/3)/chidot give the chi equation.

For curvature let F_Scoord=(dS/dchi)^2=6 C S^2/(aW) and use total S
derivatives along R=bS^(4/3). Then

  U_chichi=F_Scoord U_SS+(F_Scoord)_S U_S/2.

Both U_S=a(1/2+4R/(9S)) and U_SS=4aR/(27S^2) are positive.
The derivative of F_Scoord is positive: with r=R/S its numerator is
C_S S(3+4r)+C(3+8r/3), all positive. Thus U_chichi>0 for S>0.
Choose the new transverse function

  M=a F_Scoord/U_chichi+a S^2/U.

The bare potential Hessian on the trajectory has entries
(M,-sqrt(a)S_chi; -sqrt(a)S_chi,U_chichi), positive diagonal and determinant
(aS^2/U) U_chichi>0. Completing the square gives
V>=U-aS^2/(2M)>=U/2>0, for all real u and S>0. These are potential
properties only, not a proof of cosmological stability, attraction, physical
screening, quantum consistency or initial-condition selection.

The continuum limits are test targets, not yet checked results:
chi'/sqrt(a) tends sqrt(2/(1+a)) in radiation domination and
sqrt(3/(2(1+a))) in dust domination, where prime=d/dlog(scale).
Consequently U has leading radiation exponential slope
sqrt(8(1+a)/a) versus dust slope sqrt(6(1+a)/a).
At future vacuum chi approaches a finite chi_c. With
q=(chi_c-chi)*3H_vac/(2sqrt(a)), the handwritten endpoint series is
S=q^2-(4b/5)q^(8/3)+... and U=L+(a/2)q^2-(ab/15)q^(8/3)+... .
This suggests C2 but non-C3 endpoint behavior. It must be checked before
claiming any smooth extension. Do not silently call the potential analytic
on a domain that includes chi_c.

## Numerically useful exact coordinate

Set x=lnS. The canonical coordinate satisfies dchi/dx=-sqrt(g(x)) with
 g=aW/(9Hbar^2)>0. A noncanonical representation has kinetic term
(du)^2+g(x)(dx)^2 and the same potential as above. It is a field coordinate
change on S>0, not another physical degree of freedom. Gamma=g_x/(2g).
For state(u,x,w=u',p=x',lm=ln sigma_m,lr=ln sigma_r), define

  H^2=2(sigma_m+sigma_r+V)/(3-w^2-g p^2),
  h=H'/H=-(sigma_m+4sigma_r/3)/H^2-w^2-g p^2,
  u'=w, x'=p,
  w'=-(3+h)w-(V_u+sqrt(a)sigma_m)/H^2,
  p'=-(3+h)p-Gamma p^2-V_x/(g H^2),
  lm'=-3+sqrt(a)w, lr'=-4.

The exact trajectory has u=w=0,p=-3,sigma_m=S,sigma_r=R. Any numeric
use must check denominator positivity and coordinate conditioning.
