# Independent Jordan-history action reconstruction, v1

This is the complete frozen independent proof and control report, prepared before opening root's action-selection draft or new implementation. The only repository science source read was the complete supplied action note copied under SUPPLIED_ACTION_NOTE_v1.md. The parent supplied the research question; root retains scientific authorship. This is a focused mathematical check, not a formal audit or an empirical test.


This derivation uses the complete supplied action in EXPONENTIAL_SCALAR_FUTURE_CONFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-13.md, read in full (241 lines), SHA256 39a0dd9e107edba23adbfe8cf070f8f279190c40c651dc905af9d59911cad000. Its immutable copy is SUPPLIED_ACTION_NOTE_v1.md. The action is a candidate premise, not a derived law. No root action_selection draft, new production code, observations or external source was opened. The parent supplied the reconstruction question; root remains author. No formal audit verdict is given.

## 1. Notation and the exact Jordan action

The source calls 1+s*E “F.” To avoid collision, call that dimensionless denominator P here and reserve F=Q/C for the physical Jordan curvature coefficient, of dimension mass squared. Let g=C*ghat, with signature (-+++), and keep the source's action normalization:

    S = integral sqrt(-ghat) [Q Rhat/2 - Q K_AB dphi^A.dphi^B
                            - 2 Q Hv^2 U] + S_m[g,matter].

There is no 1/2 on the source K term. Q=Q0(1+k) is constant for a fixed candidate. Conformal transformation and one integration by parts give

    S = integral sqrt(-g) [F R/2 - G_AB dphi^A.dphi^B/2 - V] + S_m[g,matter],
    G_AB = 2F K_AB - (3/(2F)) F_,A F_,B,
    V = 2 Hv^2 F^2 U/Q.

In particular the Ricci transformation contributes +3(dF)^2/(4F) to the Jordan Lagrangian. This sign and the factor2 multiplying K are consequential. On a genuinely one-field branch parametrized by F,

    S_J = integral sqrt(-g) [F R/2 - Z(F)(dF)^2/2 - V(F)] + S_m[g,matter].

This is a classical minimally coupled physical-fluid model. A homogeneous trajectory of a three-field theory can supply an effective on-trajectory kinetic quantity, but it is not automatically a consistent one-field truncation.

## 2. Background reconstruction with known curvature

Use physical Jordan cosmic time t, scale factor a_J, H=adot_J/a_J, and chi=K_curv/a_J^2, with chidot=-2H*chi. K_curv is the spatial curvature constant in a fixed scale-factor convention; knowing its sign alone is not knowing the numerical chi(t). Use dimensionful physical densities rho,p in one fixed natural-unit system. If normalized densities are provided instead, their common density unit must be supplied explicitly.

The two independent metric equations are

    3F(H^2+chi) = rho + Z Fdot^2/2 + V - 3H Fdot,
    -2F(Hdot-chi) = rho+p + Z Fdot^2 + Fddot - H Fdot.

On an interval with F>0 and Fdot != 0, define

    T_rec = -2F(Hdot-chi) - (rho+p) - Fddot + H Fdot,
    Z_rec(F(t)) = T_rec/Fdot^2,
    V_rec(F(t)) = 3F(H^2+chi) - rho - T_rec/2 + 3H Fdot
                = F(3H^2+Hdot+2chi) -(rho-p)/2
                  +(5/2)H Fdot + Fddot/2.

A strictly monotone F makes these single-valued functions on the traversed interval. For a classical scalar equation, sufficient regularity is F in C3, H in C2, rho,p in C1, together with compatible curvature and conservation. We need only enough smoothness for Z_rec and V_rec to be differentiable along the history; noisy numerical histories need an additional derivative/error treatment. No such measured functions or error bounds are supplied in this task.

This reconstruction determines two on-trajectory functions conditional on the one-field action class and the given physical inputs. It does not uniquely specify functions outside the traversed F interval, a three-field completion, higher-derivative terms, or a fundamental action selected by observation.

## 3. Scalar-equation sufficiency and its exact limits

Variation of the one-field action gives

    Z*(Fddot+3H Fdot) + Z_F*Fdot^2/2 + V_F
       - 3(Hdot+2H^2+chi) = 0.                         (S)

Let E0 be the left side of the first metric equation after bringing everything left, and E2 be

    E2=-2F(Hdot-chi)-(rho+p)-Z Fdot^2-Fddot+H Fdot.

With matter conservation rhodot+3H(rho+p)=0,

    Edot0 + 3H E2 = -Fdot*(left side of S).

Thus exact satisfaction of both metric equations, conservation and Fdot!=0 implies the scalar equation. This is a proof of sufficiency for a specified one-field model on the interval, not an extra independent fitted constraint. Without conservation an extra term -[rhodot+3H(rho+p)] appears on the right. At a constant-F interval the identity loses the scalar equation entirely.

For a full multi-field model, the analogous identity only sets the velocity-contracted scalar equation to zero. It does not enforce every transverse equation. A curve fitted through multi-field configuration space is not automatically a consistent reduced action.

## 4. Candidate radial kinetic geometry and two-epoch identification

The supplied candidate has

    0<k<1/3,
    a=(1-k)(1+3k)/4, alpha=sqrt(a), s=(1+k)/[k(1-3k)],
    E=exp(2alpha u), P=1+sE, J=1+(1-3a)sE,
    K_u=J/P^2, C=(1+s)E/P, Q=Q0(1+k).

Define positive constants

    A=Q/(1+s), B=sQ/(1+s), Q=A+B,
    F=B+A exp(-2alpha u), F_u=-2alpha(F-B).

The finite field chart is F>B; its asymptotic endpoint B is not a finite u. Inverting gives

    u= -log((F-B)/A)/(2alpha),
    P=F/(F-B),
    K_u=(F-3aB)(F-B)/F^2.

At x=y=0, and also kinematically for any constant transverse coordinates,

    Z0(F)=2F K_u/F_u^2 - 3/(2F)
         = beta/(F-B),
    beta=(1-3a)/(2a)=1/(2a)-3/2.

Since 1/4<a<1/3, the candidate demands 0<beta<1/2. In this branch Z0>0; the more general scalar-tensor non-ghost condition would only require Z+3/(2F)>0, so positive Z must not be imposed as a universal reconstruction law.

For distinct epochs F1!=F2 with positive finite Z1,Z2 and distinct reciprocals,

    beta=(F2-F1)/(1/Z2-1/Z1),
    B=F1-beta/Z1.

Equivalently 1/Z must be affine in F with slope 1/beta>2 and negative intercept -B/beta. Every further epoch tests this same line. Two points fix the parameters, not the functional form; a third point or a whole interval can reject it. A zero slope, the wrong sign, beta outside (0,1/2), B<=0, or an observed F<=B fails this radial candidate on the stated input assumptions. Exact endpoints k=0 or1/3 are outside the supplied model and must not be silently admitted as fits.

Within the supplied k branch,

    a=1/(2beta+3),
    k=[1-2sqrt(1-3a)]/3,
    s=(1+k)/[k(1-3k)],
    Q=B(1+s)/s,
    Q0=Q/(1+k), A=B/s.

The other quadratic root for k lies outside the supplied interval; selecting the allowed root uses the candidate's explicit domain. Thus the radial kinetic function identifies k and the normalization Q0 conditionally on absolutely normalized F,rho,p and the given action convention. If Q0 has already been supplied independently, this becomes a consistency check against it instead of a new free fit. Kinetic geometry alone does not infer actual x=y=0.

## 5. Radial potential, scale and coefficient identification

On x=y=0 the supplied potential is

    U0 = 3/2 + 3s(E-1)^2/(2P^2) + nu(1+s)u^2/(2P^2).

Substitute the inverse map above into V=2 Hv^2 F^2 U0/Q. The result is

    V0(F) = (Hv^2/Q) [3F^2 + 3s(F-Q)^2
              + nu(1+s)(F-B)^2 log^2((F-B)/A)/(4a)].

After k,Q,A,B are fixed by the kinetic shape, define

    L0(F)=3[F^2+s(F-Q)^2]/Q,
    L1(F)=(1+s)(F-B)^2 log^2((F-B)/A)/(4aQ).

Then V_rec=theta0*L0+theta1*L1, with theta0=Hv^2>0 and theta1=Hv^2*nu>0. Two rows with determinant L0(F1)L1(F2)-L0(F2)L1(F1) nonzero identify both coefficients. Further epochs check the same coefficients; fitting two rows is not an independent observation test. Recover Hv=sqrt(theta0)>0 and nu=theta1/theta0>0. If convergence under the older confinement theorem is also requested, its separate nu<=6a condition must be checked; that upper bound is not a premise of every action in this class.

At F=Q, L1=0 and V(Q)=3Q Hv^2. This point can fix Hv^2 from a supplied exact potential value but contains no information about nu by itself. Two arbitrary epochs can have proportional rows; their distinct F values alone are not a rank guarantee for the potential fit. On a genuine open F interval the two analytic basis functions are not proportional (L0 is strictly positive, L1 has a zero at Q), so exact knowledge on that interval identifies their coefficients. This is an identifiability statement, not numerical conditioning or observed precision.

Dimensions provide a useful check: [F]=[Q]=[B]=mass^2, [Z]=mass^-2, beta dimensionless, [V]=mass^4, [L0]=[L1]=mass^2 and [theta0]=[theta1]=mass^2. An overall rescaling F,rho,p by a common positive lambda rescales Z by 1/lambda, V by lambda and Q0 by lambda; the inferred beta,k and time-scale Hv are unchanged. Therefore this procedure does not derive an absolute gravitational unit. An actual measurement identifying F with a local gravity observable remains a separate environment/range/calibration bridge.

## 6. Transverse motion changes equalities to necessary inequalities

The supplied K is diagonal and K_u is independent of x,y. C and hence F depend only on u. The full Jordan homogeneous kinetic energy combination is

    T_rec = Z0(F) Fdot^2 + 2F[K_x xdot^2 + K_y ydot^2].

For 0<k<1/3 and finite fields, K_x,K_y are positive because

    K_x=(1+s)4k/(9PD), K_y=(1+s)k/(3PD),
    D=1+2(1+k)(x^2+y^2)/3>0.

Thus when Fdot!=0,

    Z_rec >= beta/(F-B),
    (F-B) Z_rec >= beta.

Equality means both transverse velocities vanish at that instant; it does not identify the coordinate values. The exact affine inverse-kinetic relation is no longer required if transverse motion is admitted. The inequality alone cannot determine a unique k,Q0 or certify a full solution; transverse dynamics and the same potential still constrain the motion.

Similarly the extra potential is

    V_tr=(Hv^2 k F^2/Q)[x^2 r^px +(2/3)y^2 r^py] >=0,
    r=(F-B)/A,
    px=(1-k)/(2a), py=(1+k)/(2a).

Consequently V_rec>=V0(F) is a necessary condition for the full candidate. These kinetic/potential inequalities are coupled through the same coordinates, velocities and their equations; they are not independent free positive nuisance functions and are not sufficient for existence.

A particularly important distinction: x=x0,y=y0 constant makes the kinetic equality hold even for nonzero x0,y0, and such constants would add the positive terms just displayed to V. However, they are not actual full candidate solutions unless x0=y0=0. In the Einstein frame, Gamma^x_uu=Gamma^y_uu=0 because K_u has no x,y dependence, and there is no transverse matter force because C depends only on u. With both transverse velocities zero, their scalar equations require

    U_x=k*x0*exp(-lambda_x*u)=0,
    U_y=(2k/3)*y0*exp(-lambda_y*u)=0.

For k,Hv>0 and finite u this forces x0=y0=0. Therefore x=y=0 with zero transverse velocities is a consistent truncation, but it must be justified using those equations, not inferred from kinetic reconstruction alone. If one transverse coordinate is constant while another moves, connection forces can enter; the statement above assumes both are constant.

## 7. Constant-F plateaus and failure witnesses

For a constant F=F* on an open interval, the one-field/x=y=0 branch requires

    -2F*(Hdot-chi)=rho+p,
    V*=3F*(H^2+chi)-rho.

Conservation then makes V* constant. Z(F*) is unprobed because its kinetic term vanishes. Independently, the scalar equation requires

    V_F(F*)=R/2=3(Hdot+2H^2+chi),
    2F*V_F(F*)-4V*=rho-3p.

Because the left side is constant, the matter trace must be constant on such a one-field plateau. Radiation plus a constant vacuum term is compatible; arbitrary time-dependent dust trace is not. The metric equations alone do not supply this condition.

Exact failure witness: F*=2, H=1, chi=rho=p=0, and potential V(F)=6 constant satisfy both metric equations and conservation. The scalar equation equals -6 and fails. Thus invoking Bianchi alone at a plateau would accept a false solution. Replacing V locally by 6+6(F-2) repairs this particular scalar equation; its kinetic coefficient is still unconstrained by the background plateau.

For the actual candidate at its vacuum F*=Q, x=y=0, V(Q)=3Q Hv^2 and V_F(Q)=6Hv^2 for every allowed k and nu. Vacuum de Sitter H=Hv therefore yields the same F,H history for a continuum of k and nu if Q0 is adjusted to Q/(1+k). The plateau does not select them. The nu basis and its first derivative both vanish at F=Q. An independently fixed Q0 would constrain this degeneracy but is an additional normalization input.

With transverse motion on a constant-u/F plateau, T_rec can instead equal 2F[K_x xdot^2+K_y ydot^2]>=0. Such a history is not representable by a finite Z(F) Fdot^2 and need not obey the single-field plateau conclusions; the full independent scalar equations must be checked. At isolated zeros of Fdot, division is invalid, but a previously reconstructed regular model may extend the scalar equation by continuity. Neither a regular extension nor a plateau equation should be asserted solely from a 0/0 expression.

## 8. What is and is not eliminated

Exact metric histories, absolute F(t), conserved physical matter and known curvature can reconstruct an action along a monotone one-field history. Inside the already supplied candidate family, its radial kinetic shape can conditionally identify k,Q0 and its potential basis can identify Hv,nu when the stated rank/domain gates hold. This removes arbitrary choices only after those suppliers and that model class have been supplied and tested.

It does not derive measured F from local G, select an initial state, demonstrate that observed data are smooth enough for the required derivatives, guarantee full three-field equations from a contracted identity, determine off-trajectory functions, exclude all alternative actions, or identify a unique TOE. New observations have not been opened or claimed. Calibration points, exposed development checks and any future independent observational test must remain distinct. Failed parameter/domain/compatibility gates must be preserved rather than absorbed into a chosen state or a fitted selector.

## 9. Open-interval equality and conditional uniqueness

Combining the two independently derived statements in Section6 gives a stronger precise implication. If a full solution of the same supplied candidate parameters obeys Z_rec=beta/(F-B) on an open interval with Fdot!=0, positivity makes xdot=ydot=0 throughout that interval. The transverse coordinates are then constant there. Their independent scalar equations, because K_u has no transverse dependence and C depends only on u, force x=y=0. Thus the zero-transverse branch follows from exact kinetic equality on an interval plus the full candidate equations. Equality at a single epoch only fixes velocities and is insufficient. This statement uses the same candidate parameters on both sides; it does not exclude another parameter choice with transverse motion or select this family among all scalar-tensor actions.

## 10. Independent controls actually executed

The source independent_reconstruction_controls_v1.py was frozen before execution. It uses SymPy1.14.0 for exact algebra and the Python standard library for three ordinary floating chart round trips. It imports no author module, reads no observations and uses no simulation or fitted data. Execution under Python3.12.8 exited zero in approximately0.753seconds. All42 recorded controls passed:39 exact and3 floating controls. Stderr was empty. There was no failed independent execution, repaired independent fixture or discarded independent attempt in this block. Failures of false mathematical shortcuts are explicitly successful counterexample controls.

The exact controls check the F derivative and the factor-two/conformal sign in the Jordan kinetic term; the independent identity 1/(2FZ+3)=a/J from the source coupling; the metric/scalar/conservation identity; the expanded potential including curvature and5/2 coefficient; three full analytic histories including a curved radiation example with decreasing F and healthy Einstein kinetic term despite negative Jordan Z; an explicit conservation violation; four exact two-epoch k,Q0 reconstructions plus incompatible third rows; six identifiability-domain failures; full potential normalization, vacuum value/slope and two-coefficient/third-row reconstruction; transverse positivity and nonzero-coordinate forces; a plateau metric-only failure and its separate scalar slope; candidate vacuum parameter degeneracy; and the absolute-normalization scaling.

The three floating controls independently round trip original exponential-chart values through the derived F inverse. They are ordinary deterministic arithmetic controls, not high-precision integrations or rigorous numerical enclosures. In particular this work does not certify recovery from cancellation-dominated histories. A high condition number or differentiation error can defeat practical inference despite exact identifiability. The generic exact histories are manufactured solutions of their reconstructed one-field models; they are not claimed to be solutions of the restricted revised candidate unless expressly stated. The negative-Z example intentionally demonstrates that the candidate's Z>0 restriction is not universal scalar-tensor physics.

The supplied action still fixes the convention and model family. The source contains the original no-half K normalization, positive domain and two supplied scales. No measured H,F,rho,p, curvature history or environmental mapping was supplied here. Exact input identities, mathematical derivations and synthetic controls cannot substitute for those observations.

## 11. Exposure chronology and retained identities

The independent precheck was frozen at2026-10-15T11:27:48.649364+00:00, before any root action-selection draft/code access. Its SHA256 is8838cf6e29c77e7804b93c61637ce4d75ba3949b50ddd3794b42923352b29141. The independent control source was frozen at2026-10-15T11:31:34.849865+00:00, SHA256 c043596f9cf7c76c7b67eaf2745ee246c2c1950a3b247c52a6fafb1fabb63979. Full results are CONTROL_RESULTS_v1.json, SHA256 c860bf5331c7f03f5d317a9b7ec41d54c4a57c5bed01ffbb8125efb12b48f0bf.

After the independent proof/code were already frozen, the parent described its own case9 numerical failure and conditioning diagnosis in a coordination message, and highlighted the open-interval equality consequence. No corresponding author file, result or source was opened, and no independent fixture was changed in response. Those reported author numbers are not independently substantiated in this report. This disclosure prevents confusing the shared problem/exposure history with an answer-blind experiment. The complete mathematical open-interval implication is recorded explicitly in Section9 from the already derived positivity and transverse equations.

PRECHECK_FREEZE_v1.json, CONTROL_SOURCE_FREEZE_v1.json and CONTROL_EXECUTION_v1.json retain the ordering and exact command/runtime identities. The companion INDEPENDENT_MATH_IDENTITY_v1.json pins all independent files and the supplied action copy. Later author-source comparisons must be separate immutable supplements. No root source, git/index/branch, graph, cache, PR, campaign state, lock or process was changed.
