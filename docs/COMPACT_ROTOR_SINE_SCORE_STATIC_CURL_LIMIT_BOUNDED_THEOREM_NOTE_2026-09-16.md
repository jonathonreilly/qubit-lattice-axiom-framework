---
claim_id: compact_rotor_sine_score_static_curl_limit_bounded_theorem_note_2026-09-16
claim_type: bounded_theorem
runner: scripts/compact_rotor_sine_score_check_2026_09_16.py
claim_scope: "Actual compact sine-source MGF bound and conditional static exact-curl Gaussian limit at fixed g and finite beta, with explicit deterministic contact concentration or supplied spatial ergodicity."
upstream_dependencies: []
---

# Actual compact sine scores: exponential control and a static curl limit

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

Actual compact sine-source MGF bound and conditional static exact-curl Gaussian limit at fixed g and finite beta, with explicit deterministic contact concentration or supplied spatial ergodicity. The complete proof is self-contained below. No result from PR8165 or PR8166 is a mathematical premise. The Hamiltonian, coupling, thermal state and source class are supplied, not selected from framework axioms. No audit verdict is asserted.

## 1. Supplied law and observables

On a finite spatial graph, let C be its oriented plaquette/link incidence and

    H=-(g^2/2)Delta+g^(-2)sum_p(1-cos B_p), B=Ctheta,
    g>0, beta>0.

Use normalized compact Haar measure and the full thermal trace. Its positive
Feynman-Kac law is the free compact Brownian loop measure, reweighted by the
bounded cosine potential. It is not a zero-winding path measure. No physical
Gauss projection is inserted in the thermal trace in this note.

For real deterministic plaquette sources h_p(s), define

    X_h=(1/g)integral_0^beta sum_p h_p(s) sin B_p(s) ds,
    H2=integral_0^beta sum_p |h_p(s)|^2 ds.

The first assertion, valid at every finite graph, is

    E exp(t X_h)<=exp(t^2 H2/2), for every real t.          (1)

Initially take bounded measurable sources; approximation extends to L2
sources on this finite space-time domain. This is a bound on an actual
observable MGF. It is not a background-source partition ratio incorrectly
called an MGF, and does not replace principal flux by sine without notice.

## 2. Positive electric expansion and the amplitude-phase bound

For nonnegative deterministic c_p(s) and real phases phi_p(s), write Z[c,phi]
for the thermal path integral with exponent

    -beta P/g^2+g^(-2)integral sum_p c_p(s)cos(B_p(s)-phi_p(s)) ds.

The constant remains -beta P/g^2 for every c. In the integer electric basis,
the kinetic semigroup is positive diagonal. Each cosine term raises or lowers
the electric vector by the actual integer plaquette boundary C_p, with
coefficient c_p/(2g^2) and a phase of modulus one. The time-ordered Dyson
expansion of its trace is a sum over closed electric walks. Removing all
phases leaves a nonnegative weight for every such walk. Consequently

    0<Z[c,phi]<=Z[c,0].                                   (2)

For bounded c, absolute convergence follows either from the bounded
perturbation expansion of the trace-class kinetic semigroup, or by bounding
the k-th positive insertion contribution by the free heat trace times
(g^(-2)integral sum c)^k/k!. Thus the triangle inequality is applicable to
the infinite electric sum and the ordered integrals. The same statement
holds for piecewise measurable time dependence by approximation. Equation
(2) is a standard positive-character/diamagnetic argument, not new machinery.

Pointwise in space-time,

    cos B+g t h sin B=R cos(B-phi),
    R=sqrt(1+g^2 t^2 h^2), phi=arctan(g t h).

Therefore the MGF is exactly Z[R,phi]/Z[1,0]. Use (2), then compare the
two positive coordinate-path integrands using cos B<=1:

    E exp(t X_h)
      <=Z[R,0]/Z[1,0]
      <=exp[g^(-2)integral sum_p(R_p-1)]
      <=exp(t^2 H2/2).

This proves (1). In particular EX_h=0 and Var(X_h)<=H2. The constants are
independent of the number of links and of g. The time measure is physical
time ds, not a counting measure with a silently omitted time step.

For a locally weak limit of these zero-background finite-volume thermal
laws at fixed beta,g, (1) passes for every fixed finite-support source:
the sine path integral is a bounded continuous local functional for smooth
time sources, followed by deterministic time approximation. The bound is
not automatically asserted for every boundary-conditioned Gibbs state or
every ergodic component of a limit. Conditioning need not preserve (2).

## 3. Static curl shifts supply a second exact identity

Now require h=Cu, independent of time. On the finite compact graph,
theta_e(s) -> theta_e(s)+g t u_e preserves every free Brownian loop measure
and its winding sectors. Hence the partition function with magnetic
background g t h is exactly unchanged. Define

    Y_h=integral_0^beta sum_p h_p^2 cos B_p(s) ds,
    H3=beta sum_p |h_p|^3.

Taylor's formula, with its pointwise third-derivative bound, gives

    1=E exp[-t X_h-t^2 Y_h/2+r_h(t)],
    |r_h(t)|<=delta_t:=g |t|^3 H3/6.                     (3)

In particular EX_h=0 and Var(X_h)=EY_h. Differentiation is legitimate
at each finite graph because X_h and Y_h are bounded. The exact identity
also holds in an infinite-volume thermal Gibbs path law for finitely
supported u: its local conditional specification permits the static shift
of those finitely many whole temporal loops. All plaquettes touching the
shifted links, including boundary-crossing plaquettes, must be retained.
The conditional outside paths are unchanged, and the conditional integral
is an ordinary translation of compact loop coordinates.

There is also a useful domination that requires only (3), avoiding the
ergodic-component issue at the end of section 2. Since |Y_h|<=H2,

    E exp(t X_h)<=exp(t^2 H2/2+delta_t)                  (4)

for static curl sources in any such Gibbs path law. To see this, use (3)
with -t and the bounds on its other terms. Although (4) is weaker than (1),
it is sufficient for the diffuse limit below and applies directly to the
chosen Gibbs component. This distinction is kept explicit.

## 4. A quantitative conditional Gaussian limit

Consider a sequence of the above laws and static exact curls h_L. Suppose

    sup_L H2_L<=K<infinity, H3_L ->0,
    Y_(h_L) ->v in L2, with deterministic v.

The exact Ward variance identity shows 0<=v<=K. Write X_L=X_(h_L) and
delta_L=g|t|^3 H3_L/6, with fixed g,t. From (3),

    exp(-delta_L)<=E exp(tX_L-t^2 Y_L/2)<=exp(delta_L).

For y,v in[-K,K], the function exp(-t^2 y/2) has Lipschitz constant
(t^2/2)exp(t^2 K/2). Cauchy-Schwarz and (4) at 2t give

    E[exp(tX_L)|Y_L-v|]
      <=exp(t^2 K+4delta_L)||Y_L-v||_2.

Combining the last two inequalities yields the explicit estimate

    |E exp(tX_L)-exp(t^2 v/2)|
      <=exp(t^2 K/2)[exp(delta_L)-1]
        +(t^2/2)exp(2t^2 K+4delta_L)||Y_L-v||_2.         (5)

Thus the actual sine-score MGFs converge at every fixed real t to that of
N(0,v), and X_L converges in distribution. This is not a finite-volume
numerical fit. It uses an exact change of variables, a deterministic Taylor
remainder, and precisely the stated contact concentration hypothesis.

For finitely many source sequences, assume contact concentration for every
real linear combination. Applying the same proof and Cramer-Wold gives a
joint Gaussian vector. Its covariance is the limit of

    E integral sum_p h_(L,a),p h_(L,b),p cos B_p(s) ds.

No third-cumulant mixing theorem is imported. Conversely, (1) alone would
only give tightness and exponential integrability; it does not imply (5).

## 5. An ergodic thermal state supplies contact concentration

Let mu be a translation-stationary and translation-ergodic Gibbs path law
on Z^d with finite periodic temporal length beta, for the stated local
rotor specification. Existence or uniqueness of this particular ergodic
state is not proved here. The theorem applies to a supplied state with
these properties, not automatically to a symmetric mixture of phases.

Choose a smooth compactly supported real vector field a on R^d. On positive
lattice links put

    u_(L,i)(x)=L^(1-d/2) a_i(x/L), h_L=C u_L.

This is an exactly finitely supported lattice curl. If
f_ij=partial_i a_j-partial_j a_i, Taylor expansion uniformly on its support
gives h_(L,ij)(x)=L^(-d/2)f_ij(x/L)+O(L^(-d/2-1)). Hence

    H2_L -> beta sum_(i<j) integral f_ij^2,
    H3_L=O(L^(-d/2)) ->0.

Set Z_ij(x)=integral_0^beta cos B_ij(x,s) ds, a bounded stationary spatial
field. The multiparameter mean ergodic theorem gives L2 convergence of
averages on growing translated rectangular boxes to EZ_ij(0). Approximate
the continuous compactly supported weight f_ij^2 by rectangular step
functions; boundedness of Z makes the approximation uniform in L. It follows
that

    Y_(h_L) -> v(a)
      =sum_(i<j) EZ_ij(0) integral f_ij^2, in L2.         (6)

The lattice Taylor error contributes O(L^(-1)) deterministically. No decay
rate for correlations, uniqueness, or mixing stronger than spatial ergodicity
is needed for this contact average. If the state is time-stationary,
EZ_ij(0)=beta E cos B_ij(0,0); isotropy makes these coefficients equal.
Equation (5) therefore proves the Gaussian limit for this restricted family
in the actual compact thermal law. Nondegeneracy requires v(a)>0 and is not
silently inferred merely from ergodicity.

For a nonergodic stationary Gibbs state, the same weighted averages converge
to conditional expectations on the invariant sigma algebra. They need not
be deterministic. This note does not replace the resulting conditional
variance by an unconditional number or assert a Gaussian limit in that case.

## 6. Scope of the source and state theorem

This result uses the supplied Gibbs weight and exact shift identity to
control a particular diffuse sine-source sector. Its scope for a further
compact-to-real magnetic comparison is as follows:

- The score is sin(B)/g, not principal(B)/g or the local integer filling.
  At fixed g, even rare branch events cannot be discarded by a pointwise
  small-field expansion followed by an uncontrolled extensive sum.
- The source is a static spatial curl and the observable integrates over
  the whole finite thermal circle. General time-dependent magnetic sources
  change the kinetic action under a link shift. They are not covered by (3).
- The spatial Gibbs state and its ergodicity are premises in section 5.
  There is no uniform beta->infinity argument here and no physical thermal
  Gauss projection. The vacuum field and electric observable maps remain open.
- A response fixed by a change of variables can occur in gapped systems.
  Even independent compact rotors satisfy the corresponding single-coordinate
  identity and diffuse-score CLT. It supplies no low-energy spectral pole.

These restrictions prevent treating a Ward-sector Gaussian result as a
photon phase. The main remaining question is the nontrivial physical field
sector and its time dependence at fixed g, including normalized compact
weights and the intended source. No framework axiom or primitive is changed.

The separate sparse-loop construction and its negative implication are
preserved as deferred historical science in the recovery packet. They are
not a live claim of this note.

## Evidence and historical boundary

Primary runner: `scripts/compact_rotor_sine_score_check_2026_09_16.py`. The runner retains all original arithmetic, fixtures, assertions and tolerances. Its 120-second timeout is unchanged; a 768 MiB external process-tree cap is proposed from the finite dense matrices and library overhead, not measured RSS. JSON is written under `logs/runner-cache/`. `TOTAL: PASS=2 FAIL=0` counts the two completed diagnostic families, not dynamic assertions or exhaustive theorem coverage. Static assertion count is separately labelled.

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
