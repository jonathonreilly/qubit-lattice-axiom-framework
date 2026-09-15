from pathlib import Path
PACK=Path(__file__).parent
ROOT=Path('/Users/jonreilly/Documents/Codex/toe-coupled-defect-convexity-20260915')
SPECS=[
 dict(block=15,note='CARRIER_PRESERVING_CLOSED_INTEGER_CHARGE_GAS_CONVEXIFICATION_BOUNDED_THEOREM_NOTE_2026-09-15.md',runner='carrier_preserving_closed_integer_charge_gas_convexification_2026_09_15.py',draft='BLOCK15_CARRIER_CONVEXIFICATION_DERIVATION.md',check='block15_carrier_check.py',title='Carrier-preserving convexification of a supplied closed-charge gas',
 scope='For the explicitly supplied compactly supported closed integer p-form gas with componentwise Dirichlet Green kernel, a Gaussian split and carrier-preserving cluster bound give a positive effective field, uniform gradient Hessian bounds, explicit sufficient convexity constants and all-real-source curvature control. Exact cochain examples distinguish cluster carriers from cancelled net-charge support. The gas is not identified with the full finite-clock gauge law.',
 next='Match the gauge kernel, boundary and local source carriers before applying the convex-field estimate to a physical score.'),
 dict(block=16,note='FINITE_CLOCK_EXACT_COUPLED_ELECTRIC_MAGNETIC_DEFECT_REPRESENTATION_BOUNDED_THEOREM_NOTE_2026-09-15.md',runner='finite_clock_exact_coupled_electric_magnetic_defect_representation_2026_09_15.py',draft='BLOCK16_EXACT_TWO_DEFECT_GAS_DERIVATION.md',check='block16_two_gas_check.py',title='Exact finite-clock coupled electric and magnetic defect law',
 scope='On a finite connected complex with vanishing integer H1 and H2, the supplied clock Villain law and integer characters have an exact coupled electric-current and magnetic-coset Gaussian representation with phase and normalization. A four-cube N=3 term has negative real weight. Summing magnetic cosets first gives a strictly positive electric marginal; its spatial interactions remain to be controlled. No fixed-law phase or axiom obstruction follows.',
 next='Control the positive marginalized interaction or retain the mutual phase in a local-carrier expansion with matched boundary and source metrics.')
]
CONTEXT15='''
The standard Gaussian-split and polymer strategy is described in
[Dario-Wu2023, section3](https://pauldario.pages.math.cnrs.fr/webpage-of-paul-dario/Villain3D__short_version_.pdf)
and [Bauerschmidt2016, sections4.3 and5.5](https://cims.nyu.edu/~bauerschmidt/teaching/math253x/spin.pdf).
Read scope: Dario-Wu pages14-36 and introductory pages1-5; Bauerschmidt
PDFpages35-40 and47-52, printed33-38 and45-50. Neither full long source is
claimed read. No rotator theorem is imported as a finite-clock gauge phase.

Six finite families cover exact sparse cancellation cochains in3D and4D,
hard-core graph indices, Eulerian and sufficient-constant checks, scalar
theta/Poisson Hessians with multiprecision finite differences, Gaussian
precision matrices, and nine source-curvature quadratures. The scalar
theta examples are algebraic controls, not clock phases. No novelty is
claimed for cluster expansion or the variance/convexity machinery.
'''
CONTEXT16='''
The finite checks use exact integer incidence, spanning-tree quotients,
primitive minors and unimodular completions. Ten direct/dual three-cube
comparisons cover N=2,3,5 and beta=0.2,0.5,1,2, with at most3125clock states.
A shifted-cutoff comparison and charge-N alias are separate controls. The
four-cube witness uses exact rational matrices and exact phase -sqrt(2)/2;
no N^17 enumeration is claimed. At N=2,beta=0.2, dropping the phase changes
the three-cube plaquette numerator by approximately0.04355. Complete
magnetic sums remain positive, consistently with the Poisson proof.
'''
ROUTES15=[
('Connected cluster implies connected net Fourier charge','Six exact transverse cochain examples have a connected carrier and two net components; the marked order-two coefficient is nonzero.'),
('Net charge mass controls all derivative supports','Net mass stays8 while total mass grows as4R+4; the proof reserves total individual charge mass.'),
('Positive theta implies convex effective action','Positive scalar theta controls have negative effective curvature at weak parameters; the explicit Hessian condition is retained.'),
('A logarithmic mixture derivative has no covariance term','Gaussian quadrature detects a nonnegative and nonzero variance term; the source bound includes it.'),
('A gradient lower bound supplies a volume-uniform ordinary gap','The Dirichlet Laplacian smallest eigenvalue depends on box size; only the gradient metric is controlled.'),
('The supplied closed-charge kernel is already the full clock law','Boundary, source and both defect species still need to match; the application is not asserted.')]
ROUTES16=[
('Clock sampling equals its continuous-angle term','The aliases j+Na remain; an exact charge-N control checks their necessity.'),
('The magnetic zero coset suffices at fixed coupling','Direct finite sums retain nonzero cosets; a zero-sector reduction needs a separate estimate.'),
('The mutual phase can be discarded','Direct three-cube numerators change and an exact four-cube conjugate pair has negative real contribution.'),
('Negative summands forbid a positive representation','Full magnetic summation is strictly positive by Poisson summation; the positive marginal is explicit.'),
('An integer representative change alters the physical law','It changes the phase by an integer multiple of2pi and leaves magnetic energy fixed.'),
('Positive marginal implies spatial locality','The source map includes a Green matrix and an integer section; local-carrier or current-metric bounds remain open.')]
FENCE=chr(96)*3

def header(s):
 return f'''---
claim_id: {s['note'][:-3].lower()}
claim_type: bounded_theorem
claim_scope: "{s['scope']}"
upstream_dependencies: []
runner: scripts/{s['runner']}
---

# {s['title']}

**Date:** 2026-09-15
**Type:** bounded_theorem
**Status:** proposed_retained

{s['scope']}

These proposed analytic results await independent review and formal audit.
No native law, primitive, axiom or physical parameter is selected or changed.

## Status and proof obligations

{FENCE}yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: u1_finite_clock_gauge_matter_and_controlled_tame_maxwell_bridge_bounded_theorem_note_2026-09-03
target_blocker_text: "Identify a controlled effective field and the exact coupled-defect law needed for a fixed-clock physical-score theorem."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "{s['next']}"
conditional_surface_status: "The supplied finite-volume law, integer topology, boundary kernel and explicit smallness/source conditions in the proof."
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "Self-contained derivation with distinct exact-cochain, Gaussian, Fourier and finite-enumeration challenges, without a phase inference."
{FENCE}

There are no repository theorem premises. Geometry and probability law are
supplied data. Standard mathematical machinery is derived where used.
The finite executable reads no repository helper or scientific input file.
The exact phase/model match and infinite-volume physical limit remain
separate obligations; neither is inferred from the finite checks.

'''

def appendix(s):
 routes=ROUTES15 if s['block']==15 else ROUTES16
 rows='\n'.join('| ATTEMPTED | '+a+' | '+b+' |' for a,b in routes)
 start=9 if s['block']==15 else 6
 return f'''

## {start}. Context and finite evidence

{CONTEXT15 if s['block']==15 else CONTEXT16}

## {start+1}. No-Go Discipline Gate

### N1 — Materially distinct attempted inferences

| Honesty | Inference attempted | Finding |
|---|---|---|
{rows}

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

## {start+2}. Personal review status

All work and checks were performed personally without subagents.
Independent proof review, formal audit and main landing remain pending.
The next step is: {s['next']}
'''

for s in SPECS:
 body=(PACK/s['draft']).read_text();body=body[body.index('## 1.'):]
 if s['block']==16:
  body=body.replace('The block15 convex closed-charge lemma cannot simply be substituted here:','A convex lemma for a separately supplied closed-charge gas cannot simply\nbe substituted here:')
 source=header(s)+body+appendix(s);(ROOT/'docs'/s['note']).write_text(source)
 r=(PACK/s['check']).read_text().replace('from pathlib import Path','AUDIT_TIMEOUT_SEC = 180\nfrom pathlib import Path',1)
 r=r[:r.index("if __name__=='__main__':")]
 if s['block']==15:
  lines=[
   ('per_element','executed exact exterior derivatives and closure in six carrier-cancellation examples in3D and4D.'),
   ('per_site','executed positive theta kernels, Poisson Hessians and multiprecision action differences; positive kernels can coexist with negative effective curvature.'),
   ('per_mode','executed finite Gaussian covariance splits and precision series, plus Eulerian moment-tail polynomial identities.'),
   ('per_block','executed hard-core graph indices and source Gaussian quadratures with the positive source-variance term retained.'),
   ('lattice_wide','checked and not executed: infinite rooted cluster sums, arbitrary integer fillings and volume-uniform convexity rely on the written analytic hypotheses.')]
 else:
  lines=[
   ('per_element','executed integer boundary-of-boundary identities and exact rational curl projections on single three- and four-cubes.'),
   ('per_site','executed exact tree gauge counts and direct finite-clock sums up to3125states with the supplied Villain weight.'),
   ('per_mode','executed electric aliases, integer representative shifts and an exact negative mixed phase at N=3 on the four-cube.'),
   ('per_block','executed ten direct/dual three-cube comparisons, a shifted-cutoff comparison and positive complete magnetic phase-class sums.'),
   ('lattice_wide','checked and not executed: the general coupled-defect identity and positive marginal follow from the written proof; fixed-law phase control remains open.')]
 r+="if __name__=='__main__':\n rows=run()\n print(json.dumps(rows,indent=2))\n"
 r+=''.join(' print('+repr(k+': '+v)+')\n' for k,v in lines)
 (ROOT/'scripts'/s['runner']).write_text(r)
 print(s['block'],'source',len(source.splitlines()),'runner',len(r.splitlines()))
