---
claim_id: finite_clock_exact_coupled_electric_magnetic_defect_representation_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "On a finite connected complex with vanishing integer H1 and H2, the supplied clock Villain law and integer characters have an exact coupled electric-current and magnetic-coset Gaussian representation with phase and normalization. A four-cube N=3 term has negative real weight. Summing magnetic cosets first gives a strictly positive electric marginal; its spatial interactions remain to be controlled. No fixed-law phase or axiom obstruction follows."
upstream_dependencies: []
runner: scripts/finite_clock_exact_coupled_electric_magnetic_defect_representation_2026_09_15.py
---

# Exact finite-clock coupled electric and magnetic defect law

**Date:** 2026-09-15
**Type:** bounded_theorem
**Status:** proposed_retained

On a finite connected complex with vanishing integer H1 and H2, the supplied clock Villain law and integer characters have an exact coupled electric-current and magnetic-coset Gaussian representation with phase and normalization. A four-cube N=3 term has negative real weight. Summing magnetic cosets first gives a strictly positive electric marginal; its spatial interactions remain to be controlled. No fixed-law phase or axiom obstruction follows.

These proposed analytic results await independent review and formal audit.
No native law, primitive, axiom or physical parameter is selected or changed.

## Status and proof obligations

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: u1_finite_clock_gauge_matter_and_controlled_tame_maxwell_bridge_bounded_theorem_note_2026-09-03
target_blocker_text: "Identify a controlled effective field and the exact coupled-defect law needed for a fixed-clock physical-score theorem."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Control the positive marginalized interaction or retain the mutual phase in a local-carrier expansion with matched boundary and source metrics."
conditional_surface_status: "The supplied finite-volume law, integer topology, boundary kernel and explicit smallness/source conditions in the proof."
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "Self-contained derivation with distinct exact-cochain, Gaussian, Fourier and finite-enumeration challenges, without a phase inference."
```

There are no repository theorem premises. Geometry and probability law are
supplied data. Standard mathematical machinery is derived where used.
The finite executable reads no repository helper or scientific input file.
The exact phase/model match and infinite-volume physical limit remain
separate obligations; neither is inferred from the finite checks.

## 1. Tree gauge and primitive integer curls

Let the finite connected cell complex have E edges,V vertices,P plaquettes.
Assume its integer first and second cohomology vanish, as for a contractible
cubical box. Choose a spanning tree and set its link angles to zero by a
vertex gauge transformation. The remaining r=E-V+1 angles are theta in
(R/2pi Z)^r or in(2pi/N)Z_N^r. The normalized tree gauge quotient is exact
for gauge-invariant observables: every gauge orbit has the same finite
clock size, and the continuous change of variables is an integer torus
automorphism with Haar Jacobian one. The unfixed global vertex gauge
transformation contributes the same constant to every orbit.

Let D be the P by r plaquette-edge incidence matrix after tree columns are
removed. It has full real column rank. Integer H^1=0 implies its columns
are an integer basis of all integer exact plaquette cochains. Integer H^2=0
implies

 K=D Z^r=ker(d_2:Z^P ->Z^(3-cells)),

so K is primitive in Z^P. Put Q=D^T D>0,
P_e=D Q^-1 D^T and P_perp=I-P_e. Every coset[k] in Z^P/K may be represented
by an integer plaquette cochain k. The projected quotient P_perp Z^P is a
full lattice in the complementary real space; it is discrete because P_perp
has rational entries. Its kernel on Z^P is exactly K.

The magnetic charge is m=d_2 k. It is invariant on the coset, obeys d_3m=0,
and identifies the coset under the cohomology assumption. Its squared
Coulomb energy is

 ||P_perp k||^2=<m,(d_2 d_2^T)^+m>,

because P_perp is the real image of d_2^T. Boundary conditions are the
actual finite-cell ones in these matrices; there is no substitution by a
componentwise Dirichlet Green kernel.

## 2. The actual partition function and all integer characters

For integer j in Z^r let

 Z_N(j)=N^-r sum_{theta in(2pi/N)Z_N^r}
      exp[i<j,theta>] prod_p phi_beta((Dtheta)_p),
 phi_beta(u)=sum_{k in Z}exp[-beta(u-2pi k)^2/2].

The normalized observable is Z_N(j)/Z_N(0). Tree-gauge integer characters
correspond to conserved integer edge currents before gauge fixing. In
particular a plaquette Wilson loop has j=D^T e_p.

For any smooth periodic function F(theta), clock sampling equals the sum
of its Fourier coefficients at N Z^r. Applying it with the character gives

 Z_N(j)=sum_{a in Z^r} Z_U(1)(j+Na),

where Z_U(1)(l) is the Haar integral with integer character l. Its Fourier
series converges absolutely for the positive smooth Villain product.
For a fixed coset[k], unfold k+D n into real angles theta-2pi n.
The integer source changes by an integer multiple of2pi and is unchanged.
Completing the square with

 theta=v+2pi Q^-1 D^T k

then gives the exact identity

 Z_N(j)=C_beta sum_{a in Z^r}sum_{[k] in Z^P/K}
  exp[-(1/(2beta))<j+Na,Q^-1(j+Na)>]
  *exp[-2pi^2 beta||P_perp k||^2]
  *exp[2pi i<j+Na,Q^-1D^T k>],                        (1)

 C_beta=(2pi beta)^(-r/2)(det Q)^(-1/2).

The phase is independent of representative: k->k+D n changes its exponent
by2pi i<j+Na,n>, an integer multiple of2pi i. The electric a variables and
magnetic cosets are both retained. The double series is absolutely
convergent because its absolute value factors into two finite-rank Gaussian
lattice sums. This also justifies the final Fourier/unfolding rearrangement
by finite cutoffs and dominated convergence after Gaussian integration.

If an integer matrix R completes[D R] to a unimodular P by P matrix, write
k=R b with b in Z^(P-r). Then(1) is an ordinary pair of integer Gaussian
sums with matrices

 Q_e=Q^-1, Q_m=R^T P_perp R>0, M=Q^-1D^T R,
 phase=exp[2pi i(j+Na)^T M b].                         (2)

Such a completion exists because K is primitive. A particular coordinate
choice need not be spatially local. Gauge/tree choices and completions
must not be mistaken for changes to the physical measure.

## 3. Checks that prevent dropping a defect species or its phase

Setting a=0 gives the continuous U(1) numerator; it is not the finite-clock
law. Setting[k]=0 gives a pure exact-curl/zero-magnetic sector; at fixed
coupling it is not the full law either. The two omissions have different
origins and neither is authorized by the exact identity.

The summands in(1) are not generally nonnegative. On a single four-cube,
r=32-16+1=17,P=24. Symmetry gives(P_e)_pp=17/24 for every plaquette p.
Take j=0,a=D^T e_p and k=3e_p with N=3. The phase is

 exp[2pi i *9*(17/24)]=exp[2pi i*51/8],

whose real part is -1/sqrt(2). The associated energies are
<a,Q^-1a>=17/24 and||P_perp k||^2=9*(7/24).
The magnetic charge d_2(3e_p) is nonzero and satisfies d_3d_2(3e_p)=0.
Both configurations and the negative real weight are exact finite-matrix
facts. Pairing the charge-reversed conjugate term leaves a negative real
pair contribution. Thus a proof treating the two unintegrated gases as an
independent positive product has changed the representation.

This is not a sign obstruction to every positive representation. For each
fixed l=j+Na, the magnetic coset sum is a centered Gaussian lattice
characteristic function in the b coordinates of(2), hence strictly positive
by Poisson summation. Therefore summing the magnetic variables first yields
an exact positive electric marginal. Its effective interaction is the
logarithm of that magnetic characteristic function, evaluated at M^T l.
The matrix M contains the real Green operator and an integer choice of
representatives; its spatial locality is not supplied by positivity.

A convex lemma for a separately supplied closed-charge gas cannot simply
be substituted here:
its closure/boundary kernel differs, and the source map in(2) must be
controlled. An all-source Hessian bound helps only after its metric is
shown to match the electric current metric or a controlled local carrier
norm. Dirac-string/representative invariance does not itself prove such a
norm estimate.

## 4. Finite test design

A single three-cube has r=5,P=6 and one magnetic coordinate. Tree-gauge
clock enumeration requires N^5 states. A primitive row minor of D gives a
unimodular completion by one coordinate plaquette. Compare the direct
clock partition function and plaquette characters with the two Gaussian
sums, including the phase and C_beta. Root-of-unity phase classes make
this finite comparison cheap without changing the identity.

For the single four-cube, calculate Q^-1,P_e,P_perp with exact rational
arithmetic, check all incidence identities, rank, primitivity and the
negative N=3 mixed-phase witness. A complete N^17 clock enumeration is
unnecessary for that exact witness and is not claimed.

Finite cutoffs in the Gaussian sums are finite challenges, not executions
of the infinite series. For the centered electric sum, a useful normalized
tail check follows from the centered lattice-Gaussian MGF bound:

 Pr(max_i|a_i|>A)<=2 sum_i exp[-N^2(A+1)^2/(2beta Q_ii)].

The one-dimensional centered magnetic coordinate of the three-cube has
Pr(|b|>B)<=2 exp[-2pi^2 beta Q_m(B+1)^2]. Absolute double-sum tails may be
bounded by the product of the two positive Gaussian partition sums times
the sum of these two tail probabilities. Nonzero source characters require
a shifted-tail argument or a separately reported cutoff comparison.

## 5. What remains

The identity identifies the actual coupled defect problem. A successful
fixed-order proof must control its positive marginalized interaction or
retain the mutual phase in a convergent construction. It must then prove
the physical-score covariance and higher connected correlation limit, or
an equivalent photon observable theorem. The two-species representation
and its negative individual terms do not refute a Coulomb phase and do not
force an axiom change. They make the next proof obligation concrete.


## 6. Context and finite evidence


The finite checks use exact integer incidence, spanning-tree quotients,
primitive minors and unimodular completions. Ten direct/dual three-cube
comparisons cover N=2,3,5 and beta=0.2,0.5,1,2, with at most3125clock states.
A shifted-cutoff comparison and charge-N alias are separate controls. The
four-cube witness uses exact rational matrices and exact phase -sqrt(2)/2;
no N^17 enumeration is claimed. At N=2,beta=0.2, dropping the phase changes
the three-cube plaquette numerator by approximately0.04355. Complete
magnetic sums remain positive, consistently with the Poisson proof.


## 7. No-Go Discipline Gate

### N1 — Materially distinct attempted inferences

| Honesty | Inference attempted | Finding |
|---|---|---|
| ATTEMPTED | Clock sampling equals its continuous-angle term | The aliases j+Na remain; an exact charge-N control checks their necessity. |
| ATTEMPTED | The magnetic zero coset suffices at fixed coupling | Direct finite sums retain nonzero cosets; a zero-sector reduction needs a separate estimate. |
| ATTEMPTED | The mutual phase can be discarded | Direct three-cube numerators change and an exact four-cube conjugate pair has negative real contribution. |
| ATTEMPTED | Negative summands forbid a positive representation | Full magnetic summation is strictly positive by Poisson summation; the positive marginal is explicit. |
| ATTEMPTED | An integer representative change alters the physical law | It changes the phase by an integer multiple of2pi and leaves magnetic energy fixed. |
| ATTEMPTED | Positive marginal implies spatial locality | The source map includes a Green matrix and an integer section; local-carrier or current-metric bounds remain open. |

No route is ruled out by prior retained authority. These are checks of
particular inference steps, not independent physical walls.

### N2 — Dependency accounting

The analytic steps compose one proof and are not independent phase
evidence. Positivity, convexity, source control and physical-model matching
have separate stated hypotheses. The implications among native-law
selection, the fixed-N=3 Hamiltonian phase and charged matter remain unknown.
No negative control establishes an axiom obstruction.

### N3 — Hidden assumptions

The exact charge domain, cohomology, boundary kernel and source class are
specified before the derivation. The compact-support and finite-complex
boundary conditions are not interchanged. Explicit smallness inequalities
are retained where convexity is asserted. Finite cutoffs do not execute
infinite Gaussian or cluster sums. No physical Gaussian limit, ordinary
uniform spectral gap or score identification is silently inferred.

### N4 — Residual matching

Exact cochain and rational-matrix checks use the same incidence conventions
as their stated examples. Direct/dual or image/Poisson calculations compare
the same finite quantity with its normalization and phase retained. Scalar
theta and graph examples are inference controls, not simulations of the
full four-dimensional clock phase. A separately supplied closed-charge
kernel is not used as a substitute for the actual coupled-defect law.

### N5 — Resolution

Substantive per_element,per_site,per_mode,per_block and lattice_wide lines
are printed by the runner. Finite cochains, matrices and numerical sums
are executed. General integer filling, infinite cluster/quotient sums and
all-volume conclusions are checked and not executed; their written proofs
carry them, pending independent review. PASS counts are not proof.

### N6 — Partial closure paths

A positive effective field and a positive marginalized representation each
provide a possible next starting point under their respective hypotheses.
A matched boundary and local source-carrier estimate, a direct score
argument or a construction retaining mutual phases remain possible.
No registry is changed or approved primitive declared incapable.

### N7 — Steelman

The strongest objection is that a finite identity or a convexity theorem
for a supplied gas does not establish a fixed-clock photon phase. This is
correct. Spatial source control, boundary matching and physical-score
connected correlations remain open. Negative individual terms do not
forbid positive representations, and a marked carrier counterexample does
not refute an author's main theorem or preclude cancellations after full
unmarked resummation. These limits restrict the claim, not the exact
finite calculations or the theorem under its stated hypotheses.

### N8 — Cross-cycle comparison

Earlier growing-coupling constructions could suppress entire defect
sectors under their stated scaling. Fixed laws cannot inherit that
suppression by notation alone. The image-noise and Ward-residual results
remain relevant observable distinctions. No earlier unsuccessful candidate
is promoted to a phase exclusion or an axiom wall.

## 8. Personal review status

All work and checks were performed personally without subagents.
Independent proof review, formal audit and main landing remain pending.
The next step is: Control the positive marginalized interaction or retain the mutual phase in a local-carrier expansion with matched boundary and source metrics.
