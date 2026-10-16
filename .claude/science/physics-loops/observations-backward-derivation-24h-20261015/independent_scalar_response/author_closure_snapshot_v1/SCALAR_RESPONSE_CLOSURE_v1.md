# Constraint preservation and matter-clock response

Root's post-exposure derivation/check. The focused checker independently
supplied the full constraint-preservation identity and a finite rolling-dust
example. Root read that proof/code, then personally rederived the identities
below. This supplement is not part of root's42pre-exposure controls or the
checker's27pre-exposure controls. No data or empirical validation is involved.

Use the notation of SCALAR_RESPONSE_DERIVATION_v1.md, with pi=dot(u),
delta=delta(rho)/rho and dust potential U=-theta/K2. The retained first-order
system is

    dot(H)=-(r+v^2)/(2M^2), dot(v)=-3Hv-Fforce,
    dot(r)=(alpha v-3H)r, dot(Fforce)=mu v-3H alpha r,
    dot(K2)=-2H K2,
    dot(P)=(v u-r U)/(2M^2)-H P,
    dot(U)=-P-alpha u-alpha v U,
    dot(delta)=3dot(P)+K2 U,
    dot(u)=pi,
    dot(pi)=-3H pi-(K2+mu)u-alpha r delta
                  +4v dot(P)-2Fforce P.

Differentiate the momentum equation and insert these rates. Using
Fforce=V_phi+alpha r gives the spatial trace equation

    ddot(P)+4Hdot(P)+(2dot(H)+3H^2)P
      =[v pi-v^2 P-V_phi u]/(2M^2).

Define the energy-constraint residual after substituting momentum by

    E=-2M^2 K2 P-3H(vu-rU)-r delta-v pi+v^2 P-Fforce u.

Direct differentiation gives dot(E)+3H E=0. Therefore an initially zero E
is preserved by this linear initial-value system. This is conditional
constraint propagation, not proof that a reconstructed response history
arbitrarily chosen from observations satisfies all equations. It also does
not choose the initial scalar, dust, metric or velocity perturbations.

For the exact matter-time form let x=phi'/M, b=M alpha, h=aJ'/aJ and
w=u/M. Set ell=h-bx=H_E/A. The relation dot=A d/dtau implies

    ddot(u)=A^2 u''+A^2 b x u'.

The extra time-conversion acceleration cancels the -alpha v term in
the eliminated equation's Einstein damping. Consequently

    w''+3ell w'+(kJ^2+d_eff)w
      =[6b ell+4x]P'
       +[2b kJ^2+6b ell^2-b x^2
                      +2(x'+3hx-2bx^2)]P,             (C1)

where d_eff=kappa+b x'+3b h x-2b^2 x^2. Damping is3ell,
not3h. No quasistatic or high-wave-number limit is involved. This equation
still carries the original initial-mode freedom and matter/metric constraints.

If a common-background mode's potentials were independently reconstructed,
P=(PsiJ+PhiJ)/2 and J=(PsiJ-PhiJ)/2=bw. On a chart with b!=0,
w=J/b can be inserted into (C1) retaining derivatives of both J and b.
This gives a necessary differential relation among actual reconstructed
potential functions and candidate background histories. It avoids first
assigning a fitted pole to kappa. It neither derives b from one ratio nor
completes the observational inversion: the background equations, source and
velocity constraints, derivative uncertainty and common mode/time registration
must also be enforced. This joint equation-level inverse is the next route.

The independent numerical example integrates the original equations on a
stipulated background, with Hamiltonian-consistent initial density. Its v
changes sign between t=.25 and .30 in reference units, so it checks response
equations that remain regular there; it is not one monotonic chart of the
matter-clock inverse. Large slip ratios close to P=0 are not precise signals.
At the well-separated initial k=.5 example, the ratio -1.68 differs from the
naive static value about0.0787. This is a synthetic counterexample to an exact
identification, not an observed discrepancy, stability result or selected
physical cosmology. Original source/result hashes are retained separately.
