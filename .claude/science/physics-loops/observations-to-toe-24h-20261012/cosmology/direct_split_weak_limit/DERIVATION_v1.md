# Weak split-family limit and the unresolved fast mode

Parent /root authors this block. It explains an exposed numerical pattern; it
is not an independent observational test or a proof that failed finite-k
histories converge. The supplied action remains the curvature/fluid candidate.
Take b=k, a=(1-k)(1+3k)/4, s=(1+k)/(k(1-3k)), k decreasing to zero.
Use the same fixed physical calibration and gas distribution as IC. Then
R(k)=R0/(1+k), R0=3 rho_unit/(2 rho_vacuum); H_v is fixed.

## Pointwise action limit

On bounded coordinate sets with u=k^2 v and bounded v, the kinetic metric and
potential have the following limits, with D0=1+2(x^2+y^2)/3:

    K_u/k -> 1/4, K_x/k -> 4/(9D0), K_y/k -> 1/(3D0),
    (U-3/2)/k -> Vbar=x^2/2+y^2/3,
    alpha_B/k -> 1/2, C_B -> 1,
    U_u/k -> v x^2 - x^2 - 2y^2/3,
    k U_uu -> x^2.

At u=0, U=3/2+k(x^2/2+y^2/3) exactly. The limits follow by
substitution in the original Weyl expressions. Differentiating before taking
the limit is necessary: setting u=0 in U first would erase U_uu. Taylor
remainders are pointwise uniform on fixed compact x,y,v sets because the
rational prefactors have a regular positive-denominator expansion at k=0
and their exponential arguments are O(k^2). This is a limit of coefficients,
not a compactness or convergence proof for solutions over the 24-e-fold path.

If u=O(k^2), p_u=O(k), and x,y,p_x,p_y stay bounded on a fixed time interval,
the scalar energy is O(k), C_B=1+O(k^3), alpha_B p_u=O(k^2), and

    H_J^2/H_v^2 -> H_GR^2 = 1+2R0 rho_J/3,
    h_GR = d ln H_GR/dN_J = -R0(rho_J+P_J)/H_GR^2,
    G_N/G_ref -> 1.

These conditional implications follow from the Friedmann constraint and
matter conservation; they do not show the stated bounds hold for the actual
finite-k initial data. Large but finite early scalar amplitudes are allowed
pointwise; constants in asymptotic estimates may depend on their bounds.

## Regular limiting transverse dynamics

Under the same branch assumptions and sufficiently regular transverse limit,
dividing the x,y equations by k gives a four-dimensional candidate limiting
system in the physical e-fold N_J. Let gbar_x=4/(9D0), gbar_y=1/(3D0),
Tbar=gbar_x p_x^2+gbar_y p_y^2. Its equations are

    phi_i'=p_i,
    p_i'=-(3+h_GR)p_i-C_i/gbar_i-(partial_i Vbar)/(gbar_i H_GR^2),
    C_i=p_i sum_j(partial_j gbar_i)p_j
        -1/2 sum_j(partial_i gbar_j)p_j^2, i,j in {x,y}.

The gas and dust density determine H_GR, not the transverse scalar energy in
this zero-coupling limit. The potential gradients are x and 2y/3. The finite
field metric remains curved after division by k; replacing it by a flat metric
would give different dynamics. Integration uses the same temperature clock:
dN_J/dL=1/cT, and the same rescalings x=sx X, y=sy Y with
sx=sqrt(R0 rho_di) exp(-3N_J/2), sy=sqrt(R0 rho_gas_initial) exp(-2N_J).
Initial X=Y=1, vx=-3/2, vy=-2 are supplied, not selected dynamically.

## Fast mode: do not discard its inertia

The leading transverse solution alone does not determine u. The positive
potential-curvature contribution to the u e-fold frequency is, for x!=0,

    omega_N^2 ~ U_uu/(K_u H_GR^2)
              ~ 4x^2/(k^2 H_GR^2).

This is a leading coefficient, not a full coupled mode eigenvalue. Terms from
the rolling background, fluids and metric perturbations are not all included.
For an oscillation u=k^2 v with frequency O(1/k), p_u=O(k) but p_u'=O(1).
Consequently K_u p_u' is O(k), the same order as the force; no algebraic
constraint follows merely from small u or small scalar energy.

Only under an additional zero-inertia/quasistatic assumption would one set

    v_bal x^2 = x^2+2y^2/3-R0 tau_J/2-H_GR^2 Tbar/2.

We report this balance diagnostic without substituting it into a finite-k
history or presenting it as a proven slow manifold. It becomes singular where
x=0; it is not used there. Initial data u=p_u=0 generally do not meet it when
thermal traces are present. Preserving the fast mode is necessary to interpret
the incomplete stiff-history checks honestly.

## Frozen computation and inference scope

Check the action coefficient limits symbolically at u=0 and by independent
80-digit evaluations at u=k^2 v for fixed generic points, keeping all inputs
bound. Compare curved-metric acceleration against independently differentiated
lowered momenta. Integrate the regular limiting system using DOP853 and a
refined run, and compare with an independent BDF route if available. Freeze
relative/absolute integration tolerances (2e-10/2e-12, then2e-11/2e-13), maximum
L steps .04/.02, 241 reported samples, and a 3e-6 scaled-state refinement bound.
This bound concerns only the new regular limiting system.

Compare its stored scaled states with the previously completed finite-k split
histories at k=1e-5 and1e-6. Report their differences descriptively with no pass
threshold for finite-k convergence. Retain early thermal transients and late
transverse differences rather than selecting matching intervals. Report the
leading frequency scale and formal zero-inertia diagnostic at all sample rows.
No new observation, parameter fit, holdout or empirical acceptance is claimed.
Successful limiting dynamics cannot replace the original finite-k timeouts,
prove initial-condition selection, establish a quantum limit as K shrinks,
or complete cosmological/solar/environmental matching.
