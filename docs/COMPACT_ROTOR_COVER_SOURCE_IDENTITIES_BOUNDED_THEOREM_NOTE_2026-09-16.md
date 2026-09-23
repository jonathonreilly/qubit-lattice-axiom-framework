---
claim_id: compact_rotor_cover_source_identities_bounded_theorem_note_2026-09-16
claim_type: bounded_theorem
runner: scripts/compact_rotor_cover_source_check_2026_09_16.py
claim_scope: "Exact finite-graph compact cover and normalized source identities for the supplied rotor Hamiltonian, with full thermal trace and all windings."
upstream_dependencies: []
---

# Exact compact cover, normalized sources and the winding-mixture terms

**Type:** bounded_theorem

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

Exact finite-graph compact cover and normalized source identities for the supplied rotor Hamiltonian, with full thermal trace and all windings. The complete proof is self-contained below. No result from PR8165 or PR8166 is a mathematical premise. The Hamiltonian, coupling, thermal state and source class are supplied, not selected from framework axioms. No audit verdict is asserted.

## 1. Kernel and Haar normalization

Let C be spatial cubic curl on a fixed finite graph with E links and P
plaquettes, and let

    H=-(g^2/2)Delta+g^(-2)sum_p[1-cos(Ctheta)_p], g>0.

Compact link coordinates have period2pi and normalized Haar measure
 dtheta/(2pi)^E. The real covering-space kernel, with respect to Lebesgue
measure, is exactly

    k_T(x,y)=(2pi g^2 T)^(-E/2)
       exp[-||y-x||^2/(2g^2T)-F_T(x,y)/g^2],              (1)

where, writing b for independent standard real Brownian bridges on[0,T],

    F_T(x,y)=-g^2 log E_b exp[-g^(-2)integral_0^T
        sum_p[1-cos(C[(1-s/T)x+(s/T)y+g b(s)])_p] ds].

The bridge definition is complete here and imports no sibling derivative
estimate. In particular0<=F_T<=2PT. Simultaneous integer shifts of both endpoints leave k_T
unchanged. The compact Haar kernel is

    K_T(theta,phi)=(2pi)^E sum_(ell in Z^E)
                                  k_T(theta,phi+2pi ell). (2)

The factor(2pi)^E is required because k_T uses Lebesgue measure whereas
K_T uses normalized Haar measure. All winding labels remain present.

## 2. Exact trace in unwrapped coordinates

Let beta=MT, with integer M>=1, and Q=[-pi,pi)^E. Expand the finite trace
using M compact kernels and(2). There is one Haar factor for every
integration variable and one compensating factor from every kernel, so

    Z_beta=Tr exp(-beta H)
      =sum_(ell_0,...,ell_(M-1)) integral_(Q^M)
            product_n k_T(theta_n,theta_(n+1)+2pi ell_n)
            dtheta_0...dtheta_(M-1), theta_M=theta_0.      (3)

Put m_0=0, m_(n+1)=m_n+ell_n, and a_n=theta_n+2pi m_n.
The integer map from the ell_n to(m_1,...,m_M) is bijective. For each
intermediate time, the translates Q+2pi m_n tile real link space once
up to measure-zero boundaries. Simultaneous endpoint periodicity in(1)
then gives

    Z_beta=sum_(w in Z^E) integral_(a_0 in Q)
        integral_(a_1,...,a_(M-1) in R^E)
        product_(n=0)^(M-1) k_T(a_n,a_(n+1))
        da_0...da_(M-1),   a_M=a_0+2pi w.                (4)

The initial fundamental cell and the final winding w are both essential.
Integrating a_0 over all real links as well would count constant integer
shifts infinitely many times. Requiring a_M=a_0 would discard temporal
winding sectors. Quotienting continuous gauge/null directions in the real
comparison law is not this compact integer quotient.

The identity is valid for every finite graph and g,T>0. It has no
thermodynamic or zero-temperature limiting assumption. It also does not
replace finite thermal traces by Gauss-projected traces; any physical
sector identification in the ground-state limit remains separate.

## 3. Periodic observables and background sources are different

For a bounded periodic path or endpoint observable X, its actual MGF is

    E exp(tX)=Z_X(t)/Z_beta,

where the integrand in(4) is multiplied by exp[tX(a mod2pi)]. This is
an exact normalized observable insertion. For example at coarse times,

    X_h=(T/g) sum_(n,p) h_n,p principal[(Ca_n)_p]

is periodic in every compact link. If m_n=(Ca_n-principal(Ca_n))/(2pi),
then on any chosen real chart,

    X_h=(T/g)sum h_n,p(Ca_n)_p
                       -(2pi T/g)sum h_n,p m_n,p.         (5)

Dropping the integer term changes the observable. Equation (5) retains
that term in the exact definition.
A heat-kernel score or a sine score would be another observable and must
be identified explicitly rather than substituted for principal flux.

A background magnetic source h_n(s) instead replaces the path potential
by V(Ctheta(s)+g h_n(s)). It changes each bridge factor in(4) to the
corresponding source-dependent positive kernel. The trace becomes a
time-ordered product if the source depends on time. The same cover
identity holds, since the added source does not destroy link periodicity.

The logarithm of this background-source partition function is generally
not the MGF of X_h. Differentiating its nonlinear potential also produces
local second and third derivative terms. Calling it a field MGF would
lose those terms.

## 4. The normalized mixture derivative identities

Let nu denote the source-independent integration/summation measure in(4),
including the Gaussian prefactors. For any finite collection of real
background-source parameters h, write its dimensionless action as S_h
and let

    Z(h)=integral exp(-S_h) dnu,
    Phi(h)=-log Z(h),
    <A>_h=Z(h)^(-1) integral A exp(-S_h)dnu.

The exact source derivatives are

    Phi_a=<S_a>,
    Phi_ab=<S_ab>-Cov(S_a,S_b),
    Phi_abc=<S_abc>
       -Cov(S_ab,S_c)-Cov(S_ac,S_b)-Cov(S_bc,S_a)
       +Cum3(S_a,S_b,S_c).                               (6)

Here the expectation includes every endpoint and every winding label.
Within-bridge cumulants already belong to the derivatives of F_T;
(6) still has the additional mixture covariances and cumulant. A bound
on each lift's third derivative only bounds the first term in the last
line. It cannot silently dispose of the other four terms.

At a fixed finite graph, differentiation is legitimate: the cosine
potential and its first three background derivatives are bounded on
bounded source sets, and the free compact heat trace is finite. The
positive bridge integrals are bounded below by exp(-2PT/g^2), so their
log derivatives have finite bounds at that graph. This justifies(6);
it does not assert that the resulting estimates are uniform in volume.

One may decompose the original configuration space into contour or chart
labels independent of the external source before differentiating. If the
labels or domains are instead defined from source-shifted fields, their
source dependence must also be accounted for. A field-dependent choice
of lift is not automatically a unit-Jacobian global chart of multiplicity1.

## 5. A free-circle check on the missing mixture terms

For one free rotor, consider the compact kernel as a function of endpoint
difference z. Its physical action, ignoring a z-independent normalization,
is

    A(z)=-g^2 log sum_(n in Z)
                           exp[-(z+2pi n)^2/(2g^2T)].     (7)

Each lifted action A_n(z)=(z+2pi n)^2/(2T) has zero third derivative
and Hessian1/T. Under the normalized winding weights, let d=z+2pi n.
Direct differentiation gives

    A'(z)=<d>/T,
    A''(z)=1/T-Var(d)/(g^2T^2),
    A'''(z)=Cum3(d)/(g^4T^3).                             (8)

At the antipodal point z=pi, the two nearest lifts have displacements
+pi and-pi. For sufficiently small g^2T the compact Hessian is negative,
approaching1/T-pi^2/(g^2T^2), although every lifted Hessian is positive.
Just off that point the third derivative is nonzero, although every
lifted cubic derivative vanishes. This is a direct check of the terms
in(6), not a no-go for uniform bounds at a fixed coupling.

The normalized Haar kernel can independently be evaluated as

    sum_(k in Z) exp[-g^2T k^2/2] exp(i k z)
     =sqrt[2pi/(g^2T)] sum_(n in Z)
                       exp[-(z+2pi n)^2/(2g^2T)].         (9)

High-precision Fourier/image comparisons challenge both the normalization
and the derivative formulas. A finite numerical check does not replace
the exact Poisson/heat-kernel identity.

## 6. An exact static Ward identity and its limited physical content

For a static background h=Cu, translating every compact link by g lambda u
is a unitary change of variables. The sourced Hamiltonian

    H(lambda)=-(g^2/2)Delta+g^(-2)V(Ctheta+g lambda Cu)

is unitarily conjugate to H(0), so its partition function and all energy
levels are independent oflambda. At finite temperature, the path form
of the second derivative gives the exact identity

    Var[ (1/g) integral_0^beta sum_p h_p sin(Ctheta)_p dt ]
       =E integral_0^beta sum_p h_p^2 cos(Ctheta)_p dt.    (10)

It is the cancellation between response covariance and the contact term
in the background-source derivative. It does not say that the magnetic
observable itself has zero fluctuations.

For the nondegenerate finite-graph ground state psi, define

    M_h=g^(-1)sum_p h_p sin(Ctheta)_p,
    R=(H-E0)^(-1) on psi-perp.

Ordinary second-order eigenvalue perturbation yields

    2 <M_h psi,R M_h psi>=<sum_p h_p^2 cos(Ctheta)_p>.     (11)

The finite system has a positive gap, so this expression is well-defined;
no volume-uniform gap is assumed. The double-commutator first moment is

    <M_h psi,(H-E0)M_h psi>
                  =(1/2)E ||C*[h cos(Ctheta)]||^2.        (12)

The factor g cancels between kinetic diffusivity and the gradient of M_h.
The right side contains fluctuations of cos(Ctheta), not just C*h. Thus
(11) does not by itself force a low-momentum spectral gap to vanish.
Replacing(12) by a constant times||C*h||^2 would require an additional
estimate; an earlier proposed local Gram comparison is already known to
fail and is not reused here.

A single compact plaquette, with its correct four-link kinetic metric,
has Hamiltonian 2g^2 n^2+g^(-2)(1-cos phi). It is gapped at fixed g and
satisfies(11) exactly. This finite example is a calibration of the Ward
identity's scope, not a counterexample to a growing-volume photon phase.

## 7. The remaining constructive target

Equations(4)-(6) preserve the compact law and identify precisely where a
comparison must act. The current task is to reorganize that exact measure
into controlled local weights, or derive its response directly, while
retaining both the mixture terms and the intended observable. The normalized activities and their source derivatives remain targets
for a further constructive comparison.

The local Hamiltonian path specification is part of the supplied compact
law. Further comparison work can use that structure. No axiom update is
inferred from the present open target.

The separate sparse-loop construction and its negative implication are
preserved as deferred historical science in the recovery packet. They are
not a live claim of this note.

## Evidence and historical boundary

Primary runner: `scripts/compact_rotor_cover_source_check_2026_09_16.py`. The runner retains all original arithmetic, fixtures, assertions and tolerances. Its 120-second timeout is unchanged; a 768 MiB external process-tree cap is proposed from the finite dense matrices and library overhead, not measured RSS. JSON is written under `logs/runner-cache/`. `TOTAL: PASS=2 FAIL=0` counts the two completed diagnostic families, not dynamic assertions or exhaustive theorem coverage. Static assertion count is separately labelled.

The [exact historical recovery](work_history/repo/review_feedback/pr8167-evidence/README.md) preserves all 116 original paths, modes, blobs and hashes, including the complete sparse construction and calculation, every current/historical mutation, failed side4 adjacency claim and passing-but-insufficient check, and failed Fourier2/3 refinement. The universal sparse-geometry negative implication is deferred with its full proof and branch recovery handle. It is neither a live bounded conclusion nor mathematically refuted by the procedural N1 limitation.

## No-Go Discipline Gate

**N1 — Actual scope.** This note states the positive identities or conditional source theorem above. The separate sparse-law universal negative conclusion is absent from the live claim; formal negative certification is deferred, with no invented five-route coverage.

**N2 — Premises.** The supplied rotor model, full thermal trace and stated source/state conditions are the exact premises. Open extensions are not counted as independent impossibility walls.

**N3 — Imports.** Normalized Haar measure, all windings, Feynman-Kac, electric Dyson expansion and standard differentiation/ergodic tools are explicit. No empirical fit or native model-selection claim is made.

**N4 — Controls.** Free-circle derivatives and gapped finite rotors calibrate the displayed identities at their actual finite domains. The complete sparse-law proof and eighteen current/historical mutation sources and errors remain historical, not present execution evidence.

**N5 — Resolution.** Finite Fourier/image and matrix challenges exercise the specified formulas. No numerical thermodynamic, beta-infinity, principal-flux or photon proof is claimed. Executed certificates state exactly the two diagnostic families completed.

**N6 — Positive content.** Exact compact normalization, contact/mixture identities and the bounded sine-source/static-curl results preserve their complete arguments. A stronger physical-source comparison remains open.

**N7 — State boundary.** Fixed finite temperature and supplied contact concentration or ergodicity are not physical thermal Gauss projection, vacuum selection or a photon pole. No model-wide obstruction is claimed.

**N8 — Reopening.** Further source/state/temperature control can extend these results. The deferred sparse construction remains available in full for an honestly completed future certification.
