# Scalar reconstruction from metric histories and conditional photon records

Claim type: bounded_theorem

Root-authored conditional mathematical development, 2026-10-16.

```yaml
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "focus on deriving the remaining assumptions rather than supplying them"
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
conditional_surface_status: "Local compatibility from ideal metric histories, and fixed-background scalar observability from calibrated lensing/redshift fields, within a supplied canonical conformal-dust class."
hypothetical_axiom_status: "The action, species, flat background and universal matter metric are conditional premises, not derived framework axioms."
admitted_observation_status: "No empirical input admitted; all computational fixtures and noise diagnostics are constructed."
claim_type_reason: "Two explicitly separated local reconstruction statements with regularity, rank, background and calibration hypotheses."
audit_required_before_effective_retained: true
bare_retained_allowed: false
next_trace_action: "Test joint background and measurement identification without supplying either potential slip or an unregistered scalar environment."
```

Primary runner: [scalar_metric_inverse.py](../scripts/scalar_metric_inverse.py).
Its imported helpers contain the source geometry, original-equation forward
controls, coefficient inverse, gain, photon-map and boundary calculations.
The primary reads no observational data. Its output and cache bind the note
and complete imported mathematical source. Historical independent proofs and
failed attempts are preserved separately; they are not substituted for a
fresh computation or treated as framework authority.

## Observation question and exact targets

Measured shapes and redshifts are photon and matter records. They are not
automatically the two spacetime metric potentials used in many inverse
calculations. This note separates the following two targets before any proof.

1. **Metric-history compatibility.** In the action and regular chart below,
   smooth, registered matter-time expansion and two metric potentials with a
   rank-five local design determine the coupling magnitude, scalar speed
   product and fixed-bare-density curvature; the displayed residuals are
   necessary and sufficient for a local background and linear scalar/dust
   solution, up to the stated scale and field-coordinate freedoms.
2. **Fixed-background observability.** For one fixed compatible background
   with nonzero coupling and scalar speed and positive dust, ideal registered
   Weyl potential and corrected radial redshift determine the actual matter
   potential difference J locally on an open spherical annulus, even retaining
   local metric integration kernels. An explicit scalar reconstruction is
   given in the narrower equal-Einstein-potential sector with a fixed velocity
   potential convention. The field equations constrain the kinematic transport
   boundary; its value is not chosen by hand.

These statements cannot be composed into an unconditional reconstruction from
photon records: the second uses a fixed background, while the first uses both
potentials. Uniqueness across different candidate backgrounds/actions remains
open. Neither statement identifies actual observational inputs, selects the
fundamental action or proves a theory of everything.

Reconstructing scalar-tensor actions is established prior art: Boisseau et al.,
[gr-qc/0001066v1](https://arxiv.org/abs/gr-qc/0001066v1), and Tsujikawa,
[astro-ph/0508542v2](https://arxiv.org/abs/astro-ph/0508542v2), use expansion
and perturbation information under their stated premises. Density-minimum
tomography is another known route, illustrated by Brax et al.,
[1203.4812v2](https://arxiv.org/abs/1203.4812v2). No priority claim is made
for inverse reconstruction or the reductions here. The calculation retains
scalar acceleration, dust response and the original constraints; it does not
insert minimum tracking, a potential profile or a preferred initial state.

## Premises and obligation graph

| Obligation | Treatment here | Surviving condition |
| --- | --- | --- |
| Action and species | Written explicitly; equations derived and checked | The class itself is supplied |
| Clock/frame conversion and density convention | Derived below | Universal conformal matter coupling and a registered clock |
| Metric coefficient extraction | Rank-five linear inverse and residuals | Exact smooth inputs, adequate rank and spatial registration |
| Local background/action construction | Proof using Einstein constraints, dust transport and original scalar equation | Positive dust, nonzero scalar motion/coupling, local field interval |
| Full linear physical compatibility | Original constraints, scalar equation, dust equations and trace | Linear scalar sector; no extra anisotropic stress/species |
| Photon-to-Weyl and redshift map | First-order Born/null calculation | Calibration, distance, endpoints, masks and source registration |
| Transport boundary elimination | Spherical compatibility proof | One fixed compatible homogeneous background and same-dust tracers |
| Practical inversion and action selection | Open | Derivative errors, bias, unknown background, scales and new observations |

Use smooth real functions on connected open charts; smoothness is a sufficient
condition, not a minimal regularity claim. Fourier formulas concern common
nonzero registered comoving modes. Their local spatial versions use the actual
Laplacian, not an assigned shell wave number. No finite-data or stability
conclusion follows merely from ideal rank or uniqueness.

## Action, clocks and complete linear equations

Adopt

    S = integral sqrt(-gE)[M^2 RE/2 - (partial phi)^2/2 - V(phi)]
        - sum m integral A(phi) dsE,
    M>0, A>0, gJ=A^2 gE.

There is one canonical scalar and universally conformal pressureless matter,
with a flat homogeneous background. Einstein time is t, matter background
proper time is tau, d tau=A dt, and a=aJ=A aE. Set

    alpha=A_phi/A, b=M alpha, v=dot(phi), x=phi'/M,
    h=a'/a, q=bx, ell=h-q, H_E=A ell,
    rho = bare proper Einstein particle density,
    rE=A rho, R=rE/(M^2 A^2),
    mu=V_phiphi+rho A_phiphi at fixed bare rho,
    kappa=mu/A^2, F=V_phi+rho A_phi,
    Fbar=F/(M A^2)=-x'-3hx+2qx.

A dot denotes d/dt; a prime denotes d/dtau. The lapse-retaining homogeneous
action gives Friedmann, Raychaudhuri, scalar evolution and particle transport:

    3M^2 H_E^2=v^2/2+V+rE,
    -2M^2 dot(H_E)=v^2+rE,
    dot(v)+3H_E v+F=0,
    dot(rho)+3H_E rho=0.

In the nonzero Fourier sector, let the Einstein metric potentials coincide
and equal P; let u=delta(phi),
delta=delta(rho)/rho and U be the comoving particle velocity potential. For
K2=k_com^2/aE^2, direct linearization gives

    dot(P)+H_E P=(v u-rE U)/(2M^2),
    -2M^2 K2 P-6M^2 H_E(dot(P)+H_E P)
        =rE delta+v dot(u)-v^2 P+F u,
    ddot(u)+3H_E dot(u)+(K2+mu)u
        =-alpha rE delta+4v dot(P)-2F P,
    dot(U)=-P-alpha u-alpha v U,
    dot(delta)=3dot(P)+K2 U.                         (linear system)

For generic local spatial patches, no anisotropic stress alone leaves a
traceless-Hessian kernel in the Einstein potential difference. The displayed
linear system and explicit inverse formulas use its zero sector and the fixed
spatially integrated momentum/velocity convention. Nonzero Fourier modes or
full-sky l>=2 projections remove these kernels; an arbitrary masked patch
does not. The broader uniqueness argument below retains them explicitly.

The density variation includes rho A_phi u. Omitting it would replace the
force F in the Hamiltonian by V_phi incorrectly. The covariant scalar wave
operator retains the lapse-force and metric-time terms; a fitted spatial
response denominator is therefore not simply mu.

For completeness, let E be the Hamiltonian residual after substituting
momentum:

    E=-2M^2 K2 P-3H_E(vu-rE U)-rE delta-v dot(u)+v^2P-Fu.

The background identity dot(F)=mu v-3H_E alpha rE and the displayed system
give dot(E)+3H_E E=0. Differentiated momentum gives the spatial Einstein
pressure equation with scalar pressure v dot(u)-v^2P-V_phi u. Thus a
Hamiltonian-consistent initial linear solution preserves all constraints;
arbitrary functions fitted to a reduced equation need not do so.

The conformal metric gives PsiJ=P+alpha u and PhiJ=P-alpha u. Define
J=(PsiJ-PhiJ)/2=bw with w=u/M. Put kJ2=k_com^2/a^2 and Z=A U. Then

    P'+ell P=(xw-RZ)/2,
    R delta=-2kJ2 P-6ell(P'+ell P)-xw'+x^2P-Fbar w,
    w''+(3h-2q)w'+(kJ2+kappa)w
        =-bR delta+4xP'-2Fbar P,
    Z'=-P-J, delta'=3P'+kJ2 Z.                     (matter equations)

The physical matter-frame contrast is deltaJ=delta-3J, so
deltaJ'=3PhiJ'+kJ2 Z. Z is a comoving potential; its equation has already
absorbed the Hubble/coupling drag. The peculiar velocity is grad(Z/a).

## Metric-history inverse and local action construction

Eliminate delta from the scalar equation using the Hamiltonian constraint.
With L=b'/b one obtains

    J''+kJ2 J=-cD J'-cJ J+d P'+e kJ2 P+f P,
    cD=3ell-2L,
    cJ=kappa+b x'+3bhx-2q^2+L^2-L'-3ell L,
    d=6b^2 ell+4q, e=2b^2,
    f=6b^2 ell^2+2b x'+6hq-5q^2.                   (coefficient relation)

At each epoch form rows [-J',-J,P',kJ2 P,P] and right-hand side J''+kJ2 J.
Rank five and exact membership in the column space give a unique common
coefficient vector. Extra rows test its residual. Five rows alone supply a
solvable linear system, not physical compatibility. Common kJ2 makes two
columns dependent; failure of this rank condition is not a general no-go for
other nonlinear or integrated inverse methods.

From the extracted coefficients and their registered derivatives set

    B=e/2>0, L=B'/(2B), q=h-(cD+2L)/3,
    b=s sqrt(B), x=q/b, s=+1 or -1 constant,
    kappa=cJ-q'-3hq+2q^2-2qL-L^2+L'+3hL.

Require q!=0 and

    d=6B(h-q)+4q,
    f=6B(h-q)^2+2(q'-qL)+6hq-5q^2,
    R=2q'-2h'-2hq+(2-1/B)q^2>0,
    R'+(3h-2q)R=0,
    x''+3hx'+(3h'+kappa-2q'+6hq-4q^2)x-3b(h-q)R=0.

There is no division by 4-6B; B=2/3 is regular on this chart. The extraction
derives b and kappa conditionally from the ideal metric histories rather than
supplying them as independent scalar-response functions.

For positive A0 and field origin phi0 construct

    A=A0 exp(integral q d tau), phi=phi0+M integral x d tau,
    dt=d tau/A, aE=a/A, rE=M^2 A^2R, rho=rE/A,
    V=M^2 A^2[3(h-q)^2-x^2/2-R].

Nonzero x gives local single-valued A(phi),V(phi). The two Einstein
background constraints hold by construction; R transport makes rho aE^3
constant. Differentiating Friedmann with these facts yields the **original**
scalar equation because v!=0. It does not leave an arbitrary scalar-force
constant. Differentiating that force and using the last compatibility equation
recovers the fixed-bare-density curvature kappa.

For each mode reconstruct w=J/b and Z,delta from the matter constraints above.
Require Z'+P+J=0 and delta'-3P'-kJ2 Z=0. Substitution of the reconstructed
delta into the original scalar equation gives precisely the coefficient
relation. Momentum/Hamiltonian hold by construction and the pressure equation
follows as above. This proves the stated local necessity and sufficiency,
including every residual and regularity condition; it is not nonlinear or
multi-species sufficiency.

Initial perturbation values at a reference time are then reconstructed from
these histories. Their cosmological origin, probability law and unobserved
prehistory are not derived. A0, phi0 and field orientation remain free. Changing
A0 by lambda rescales rE,V by lambda^2 and rho by lambda while preserving the
listed matter-time potentials and background quantities at fixed registered
matter-time units. R and kappa have units of inverse time squared, while
h, q and x have units of inverse time; they are not dimensionless unless
explicitly normalized by reference scales. In
particular M^2/A^2 is not absolutely calibrated. No off-trajectory action
extension, globally bounded potential or stable perturbation history follows.

## Pressure trace and a restricted common-gain extension

The independently originated pressure-trace reduction was personally
rederived by root and is attributed in the preserved review evidence. In
matter time the spatial Einstein equation is

    2P''+2(q+4ell)P'+(4ell'+4qell+6ell^2+x^2)P
        -xw'+(Fbar-bR)w=0.

Using J=bw and G=x/b gives

    2P''+8hP'+(4h'+6h^2)P=At P'+Ct P+G J'+Ft J,
    At=6q, Ct=4q'+8hq-2q^2-qG,
    Ft=G'+3(h-q)G-2h'+2q'-2hq+2q^2.

Rank-four rows (P',P,J',J) determine At,Ct,G,Ft. This equation is local;
coeval angular positions can replace Fourier rows when the actual local
design has rank four. Scalar KG, dust continuity, spatial derivatives and
background constraints remain additional physical tests.

Suppose, additionally, both potentials share a positive homogeneous
matter-time gain g(tau); write sG=g'/g and use tildes for recorded coefficients.
The scalar equation gives B=etilde/2. The trace's coefficient of Jtilde'
is unchanged: Etilde=G. Hence

    q=B Etilde, sG=[3(h-q)-2L-cDtilde]/2,
    cJ=cJtilde+cDtilde sG+sG^2+sG', f=ftilde+dtilde sG.

The trace transforms as Atilde=At+4sG,
Ctilde=Ct-At sG-2sG^2+2sG'+8hsG and Ftilde=Ft-GsG. These are extra checks.
After recovering g/g0, divide both channels by it and enforce all original
residuals. Rank five implies rank four for the trace column subset. This
extension remains regular at B=2/3, but leaves g0 and A0. It does not recover
arbitrary transfer functions or a detector gain varying with reception time.

## Which photon records supply which inputs

In conformal time eta, d tau=a d eta, write
dsJ^2=a^2[-(1+2PsiJ)d eta^2+(1-2PhiJ)dx^2]. An observer at the origin receives
a photon from outward direction n and radius r at eta=u; the background ray
has eta=u-r. For the calibrated first-order Born potential

    psi(u,r,n)=2 integral_0^r [(r-s)/(rs)] P(u-s,sn) ds,
    Pcone=(1/2) partial_r[r^2 partial_r psi].

The radial inverse is known prior art, for example Taylor,
[astro-ph/0111605v1](https://arxiv.org/abs/astro-ph/0111605v1).
It differentiates at fixed u. Interior integration contributions c0+c1/r are
annihilated locally; an observer-origin integral still requires its appropriate
regular/subtracted definition. Full-sky shear obeys
gamma_lm=(1/2)sqrt[(l+2)!/(l-2)!] psi_lm for l>=2 and has l=0,1 null modes.
Shear alone does not calibrate those modes or supply J. Masks and source
calibration add unresolved information.

For any field Fhat(u,r,n)=F(eta=u-r,rn), put D=partial_r+partial_u. Then

    partial_eta=partial_u, partial_r at fixed eta=D,
    Delta F = [D^2+2D/r+DeltaOmega/r^2] Fhat,
    F'=a^-1 Fhat_u,
    F''=a^-2[Fhat_uu-Hc Fhat_u], Hc=a_eta/a=ah.

An open repeated-cone strip gives local spacetime neighborhoods, not global
coeval Fourier histories. A whole radial interval [r0,r1] shares coeval times
only in the open interval (u0-r0,u1-r1). Local angular shells do not need that
whole-volume condition. A single cone leaves normal time jets undetermined
in the unrestricted metric class; that is not a same-action counterexample.

A reception-time multiplier g(u) commutes with the radial inverse but becomes
g(eta+r) on a coeval slice. Consequently

    Delta(gF)=g Delta F+2g_u partial_r|eta F+(g_uu+2g_u/r)F.

It cannot silently be substituted for the homogeneous gain of the previous
section. Distance/time registration and derivative-error control remain
premises even when an exact differential inverse exists.

Using outward n and photon direction -n, the measured energy ratio yields

    epsilon=Psi_o-Psi_s+n dot(v_s-v_o)
              -2 integral_0^r partial_eta P(u-s,sn) ds.

This follows from d ln(-p_0)/d eta=partial_eta(Psi+Phi) along the ray and
E=(-p_0)(1-Psi+n dot v)/a. Actual event times matter: at fixed coordinate
endpoints delta eta_s=2 integral_0^r P ds, so comparison with the background
ratio a(u)/a(u-r) adds -Hc_s delta eta_s. Endpoint proper-clock factors and
emitter time mapping also enter a drift derivative. Redshift drift is not
peculiar acceleration alone. The signs and endpoint structure were compared
with Challinor and Lewis, [1105.5292v2](https://arxiv.org/abs/1105.5292v2),
pages 3–4, and Bessa et al., [2306.13911v3](https://arxiv.org/abs/2306.13911v3),
sections 2 and 3.2; their fitted cosmologies and number-count models are not
inputs to this derivation.

Correcting the integrated and observer terms with the same registered fields
defines Rz=-Psi+v_r. For irrotational same-dust velocity v=grad Vv, Euler gives
Vv_eta+Hc Vv=-Psi after fixing the spatially constant convention. Thus

    (partial_r+2partial_u+Hc) Vhat=Rz,
    (partial_r+2partial_u+Hc) Psi=-(partial_u+Hc)Rz.

The characteristic c=u-2r gives
a(c+r)Vhat(c+2r,r)=B(c,n)+integral a(c+s)Rz(c+2s,s) ds.
Kinematics alone leaves B. Its homogeneous family
delta Vhat=a^-1 F(u-2r,n), delta Psi=-a^-1 F_c is valid on an interior annulus;
it is not generally smooth through the observer and is not automatically a
solution of the scalar/Einstein equations. Setting B=0 would supply a boundary.

## Removing that boundary for one fixed compatible background

Fix the compatible homogeneous background, with a,R>0 and b,x nonzero.
All derivatives below are at fixed matter time or fixed comoving position,
on an open product chart with r>0. The corrected redshift tracer must be the
same pressureless matter; bias or extra forces would change the equations.
Retain the calibrated P,Rz inputs and angular sector. The following explicit
formula uses the equal-Einstein-potential sector and integrated conventions
of the displayed original system. Set

    nu=-b'/b-Ft/G,
    S=[2P''+(8h-6q)P'+(4h'+6h^2-Ct)P]/x,
    HP=(6b ell+4x)P'-2b a^-2 Delta P
                   +(6b ell^2-bx^2-2Fbar)P.

The trace, scalar and momentum/redshift relations imply

    w'=nu w+S,
    (Delta-Lambda)w=g,
    Lambda=a^2[nu'+nu^2+3ell nu+kappa-bFbar],
    g=a^2[S'+(nu+3ell)S-HP],
    (partial_r-C)w=f,
    C=aRb/x,
    f=(aR/x)(Rz+P)+(2/x)partial_r(P'+ell P).

C and Lambda depend only on time. The spherical commutator is
[Delta,partial_r]w=2w_r/r^2+2DeltaOmega w/r^3. Apply Delta-Lambda to the
radial equation and subtract (partial_r-C) times the elliptic equation.
Eliminating derivatives gives the exact local identity

    D0 w=N0, D0=Lambda-C^2-C/r,
    N0=(r/2)[(Delta-Lambda)f-(partial_r-C)g]
          -g+Cf+f_r+f/r.

Thus w=N0/D0 wherever D0!=0. At a positive root of D0, its radial derivative
C/r^2 is nonzero; compatible smooth inputs have N0=0 and
w=(partial_r N0)/(partial_r D0). Differentiating D0 w=N0 and using w_r=Cw+f also gives a single expression
throughout the annulus, including D0=0:

    w=(r^2/C)[partial_r N0-C N0-D0 f].

It uses another derivative rather than a D0 denominator. This is an exact
necessary candidate, not a noise-stability guarantee. All reduced and original
residuals must still be tested; arbitrary records need not have a solution.

For two solutions with the same fixed background, P and Rz, their difference
has f=g=0 and hence D0 delta w=0. Because C!=0, D0 vanishes at at most one
radius at each time and on no open radial interval. The difference is zero
off that radius, and continuity makes it zero there too. This proves local
uniqueness without imposing decay, real Fourier wave numbers, an origin
boundary or an initial perturbation spectrum. The constraints then determine
the dust perturbations up to the already fixed homogeneous velocity convention.
This explicit formula applies in any recovered full-sky l>=2 sector, or the
stated equal-potential sector; it does not fill missing angular modes or
remove mask leakage. It does not establish uniqueness of w in the broader
local system with metric integration kernels.

### Uniqueness of the actual slip with local metric kernels retained

The focused checker independently identified this necessary qualification and
proved a stronger J-uniqueness statement; root personally rederived it. Write
PsiE=P+chi, PhiE=P-chi and J=chi+bw. No anisotropic stress gives

    (partial_i partial_j-delta_ij Delta/3)chi=0,
    chi=c0(tau)+c_i(tau)X_i+c2(tau)|X|^2.

The polynomial form follows by compatibility of the equal diagonal and zero
off-diagonal Hessian entries. Call this spatial space P2. It is closed under
time derivatives and the Laplacian. Time-only momentum/Euler integration
functions also belong to P2 and are retained here.

For the difference of two full solutions with the same P,Rz, those data vanish.
Put G=x/b, Cb=R/G, lambda=aCb!=0. Unintegrated momentum, Euler and Hamiltonian
imply w=(R/x)Z+pi_w, J=Cb Z+pi_J, Z'=-Cb Z+pi_t and

    delta=nu_b Z+pi_delta, nu_b=6h-4q+2x'/x+Cb,
    Z_r-lambda Z=S_b, (Delta+Q_b)Z=T_b,
    Q_b=a^2(nu_b'-Cb nu_b), S_b,T_b in P2.

Each pi lies in P2. The second spatial equation follows from bare dust
continuity; no scalar-wave or pressure equation is dropped from existence
requirements. At fixed time write S_b=s2 r^2+s1(n)r+s0, where s1=s_vec dot n.
The radial equation gives Z=Zp+exp(lambda r)f(n), with

    Zp=-s2 r^2/lambda-(2s2/lambda^2+s1/lambda)r
         -(2s2/lambda^3+s1/lambda^2+s0/lambda).

Multiplying the Helmholtz equation by r^2 leaves a polynomial of degree at
most four plus exp(lambda r) times
[(lambda^2+Q_b)r^2+2lambda r]f+DeltaOmega f. Five radial derivatives remove
the ordinary polynomial. The remaining r^2 and r coefficients combine to
2lambda^6 f=0, including lambda^2+Q_b=0. Hence f=0. The remaining negative
powers -4s2/(lambda^2 r)+2s1/(lambda^2 r^2) force s2=s1=0 on an open angular
patch. Z is spatially constant and the actual data difference obeys
J=Z_r/a=0.

Thus J is unique even with the local kernel retained. This proves neither
uniqueness of every scalar representation mode nor the preceding explicit w
formula in that larger system. The argument uses an open time/radial/angular
neighborhood; a single ray, cone or isolated samples do not supply it.
Existence still requires all original equations, including the chi terms.

The strongest missing lemma is now explicit: jointly identify a compatible
background and its calibrated primitive inputs, and establish controlled
errors, without supplying J or that background. Fixed-background uniqueness
does not prove uniqueness between distinct actions or backgrounds.

## Constructed checks, conditioning and retained limitations

One full-action fixture is M=1, aE=t, phi=ln t, A=exp(phi)=t,
rho=t^-3, V=(3/2)exp(-2phi), tau=t^2/2. Here b=1,
x=1/(2tau), R=1/(4tau^2), kappa=7/(4tau^2), C=1 and Lambda=15.
The boundary formula has D0=14-1/r; the compatible exceptional radius is
r=1/14. Regular spherical l=2 Helmholtz modes test the full source formula
and its derivative limit. The annular candidate tau^(-3/2) exp(r)Y20 passes
the homogeneous trace and radial equations but fails the scalar elliptic
identity by -2(7r^2-r+3)/r^2 times itself. This is one explicitly rejected
candidate, not a no-go for network or scalar theories generally.

The spherical geometry is load-bearing. In this same background,

    Z=tau^(-1/2) exp(z+sqrt(14)X), P=0,
    w=J=Z/(2tau), delta=5Z/(2tau)

satisfies every original linear field equation and the **planar** zero-redshift
condition -J+Z_z/a=0. Its true observer-centered radial redshift is nonzero on
an open angular patch. This independent witness, personally substituted by
root, excludes replacing the spherical direction by a plane-parallel one in
this theorem. It is local constructed mathematics, without a claim about
cosmic normalizability or stability.

In the same exact background there are growing modes P=t^(2m), w=Y(m)P,

    Y=(8m^2+12m+3)/(2m+3), z=m(m+1),
    k^2=4z(8z+9)/(3-8z).

Their original scalar, Einstein and dust equations are checked. Four trace
rows (m,1,mY,Y) have determinant
96 product_{i<j}(m_j-m_i)/product_i(2m_i+3), nonzero for distinct regular m.
Yet the growing m values approach a common limit at high k. Fixed wave-number
ratios therefore give a determinant decaying as k^-12. In the frozen
normalization at k0=1000, the synthetic trace and scalar condition numbers
are about 6e20 and 1.6e21. Double precision does not resolve their smallest
singular values reliably; an 80-digit calculation is reported. These are
properties of constructed modes, not survey forecasts or observed cosmology.

For exact y=D theta, perturbations D+E and y+eta obey the elementary
least-squares bound (||eta||+||E||||theta||)/(sigma_min(D)-||E||), when
||E||<sigma_min(D). Units and row/column normalization must be fixed. Small
potential errors do not control their higher derivatives. The synthetic
central-difference lensing inverse has

    Var(P)=r^2 sigma^2(dr^2+3r^2)/(2 dr^4),
    Var(P_uu)=6 Var(P)/du^4

for independent additive input noise and the declared stencil. The preserved
finite-grid experiment illustrates amplification with no smoothing or tuning;
it supplies no measured noise level, likelihood or coverage guarantee.

Surviving imports include action/species/flatness and linearization, absolute
normalization, common coordinates and clocks, calibrated potential/redshift
extraction, same-matter tracer response, rank and derivative error control.
b=0, x=0, R=0 and rank loss need other charts. No full nonlinear stability,
initial-state origin, global bounded history or cross-environment action
uniqueness has been established. No new observational array was accessed.

## Review and reproducibility boundary

The calculation is personally authored. Focused independent proofs precede
exposure to their corresponding new root sources; later correspondence,
unchanged replay and canonical packaging checks are labeled separately.
The pressure-trace discovery, local-kernel uniqueness strengthening and
planar null witness are attributed to focused checkers; root rederived and
integrated them. The explicit w commutator formula was root-derived; its
version without the isolated D0 denominator was integrated after exposure
to the independently obtained Z reconstruction. Both implementations use Python/SymPy, not
independent computer algebra systems. Counts and exact source bindings live
in the source-bound review receipts rather than being pooled as experiments.

The first numerical diagnostic attempts failed at a matrix index and then a
JSON boolean conversion. Their source, failure receipts and narrow repairs
remain preserved. An independent check corrected the kinematic transport's
observer-regularity scope; the revised statement is annular. All current
claims remain conditional, and historical failures are not relabeled as
successful controls. Source mutations and portable replays are separate
validation tasks, not new observations.

Shared integrated-main pipeline, strict lint and changed-evidence validation
are pending hard conditions before landing. No formal audit verdict or
effective framework status is asserted by this author-side packet.
