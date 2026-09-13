from pathlib import Path
import shutil, json, hashlib, subprocess, gzip
parent=Path('/Users/jonreilly/Documents/Codex/toe-native-local-law-20260913')
cp=parent/'.claude/science/physics-loops/toe-native-local-law-20260913'
wt=Path('/Users/jonreilly/Documents/Codex/toe-gauss-reduced-spectrum-20260913')
packet=wt/'.claude/science/physics-loops/gauss-reduced-weak-coupling-spectrum-20260913'
packet.mkdir(parents=True,exist_ok=True)
note=wt/'docs/EXACT_GAUSS_REDUCTION_AND_FIXED_VOLUME_WEAK_COUPLING_SPECTRUM_BOUNDED_THEOREM_NOTE_2026-09-13.md'
runner=wt/'scripts/exact_gauss_reduction_and_fixed_volume_weak_coupling_spectrum_2026_09_13.py'
front='''---
claim_id: exact_gauss_reduction_and_fixed_volume_weak_coupling_spectrum_bounded_theorem_note_2026-09-13
claim_type: bounded_theorem
claim_scope: "For a supplied finite charged integer-link Hamiltonian on a fixed contractible cubical box, derive exact affine-integer Gauss coordinates and the weak-coupling fixed-index spectral limit. Primitive plaquette generation gives an oscillator plus the supplied fixed-number free CAR Hamiltonian; finite scaled flux cutoff gives a Dirichlet boundary. The theorem does not establish the thermodynamic charged photon/Weyl phase, a common interacting cone, Hamiltonian selection or an axiom update."
upstream_dependencies:
  - native_edge_record_matter_instrument_and_energy_ledger_bounded_theorem_note_2026-09-05
runner: scripts/exact_gauss_reduction_and_fixed_volume_weak_coupling_spectrum_2026_09_13.py
---

# Exact Gauss reduction and a fixed-volume weak-coupling spectrum

**Date:** 2026-09-13
**Type:** bounded_theorem
**Status:** proposed_retained

An exact reduction of Gauss law retains the charged, non-product flux domain.
In a fixed finite contractible box, the low spectrum of the supplied hard-link
Hamiltonian converges, as g tends to zero, to gauge oscillators plus the
supplied free matter spectrum in a fixed total-number sector. A cutoff with
finite gS retains a Dirichlet flux boundary; allowing gS to diverge removes it.
The proof below uses integer generation, quadratic forms and compactness.
Finite spectra challenge its hypotheses and coefficients but do not replace it.

~~~yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact Gauss isometry, positive weighted electric decomposition, fixed-graph spectral form limit and finite-boundary discriminator."
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Obtain a physical low-energy spectral comparator for a charged finite-link candidate, beyond a small plaquette expectation."
source_of_blocker_text: user_goal
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Control volume dependence, harmonic holonomies, interacting charged correlations and compact defects; the thermodynamic phase remains open."
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
~~~

The [minimal framework memo](MINIMAL_AXIOMS_2026-06-29.md) supplies ontology
context. The [edge matter construction](NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md)
and [current integer-link source](THE_FERMION_ON_COMPACT_U1_LINKS_THE_INTEGER_FLUX_SELECTS_THE_STAGGERED_GAUSS_LAW_AND_JOINS_THE_MAXWELL_GERM_BOUNDED_THEOREM_NOTE_2026-09-03.md)
identify comparison domains. The graph, CAR realization, charges, Hamiltonian
time and coefficients remain supplied. This source redeclares its complete
Hamiltonian; no unmerged campaign note is a theorem premise. No axiom, approved
primitive, state formation rule or audit verdict is changed.

Maximal-tree reduction and lattice continuum comparisons are established
mathematical methods. [Horn and Weinstein](https://www.slac.stanford.edu/pubs/slacpubs/2750/slac-pub-2864.pdf),
section 2 and sections 3.2-3.4, provide gauge-Hamiltonian and projected-flow
context. [Nakamura and Tadano](https://arxiv.org/pdf/1903.10656), section 1,
state a norm-resolvent continuum theorem for square-lattice Schrodinger
operators under specified potential and embedding hypotheses. That theorem
is not invoked for the charge-dependent domains and primitive multishifts
here. The fixed-index form argument below supplies its own hypotheses and
does not claim their norm-resolvent rate or a new general continuum principle.

'''
body=(cp/'BLOCK14_DERIVATION.md').read_text().split('\n',1)[1]
end='''

## No-Go Discipline Gate

The negative statements delimit particular regulator, topology and inference
choices. This is a constructive finite-volume theorem with an open phase task,
not a general obstruction to finite-spin photons or the framework.

**N1 — Actual distinct attack routes.**

| Route | Mechanism and disposition | Marker |
|---|---|---|
| Integer cycle and charge coordinates | Exact rooted-tree flows retain all physical states and expose the affine cutoff; a product charge/flux cutoff is generally false. | ATTEMPTED |
| Weighted electric minimization | Orthogonal projection isolates a positive Coulomb kernel, while its fractional longitudinal field leaves an affine integer residual; the full charged potential is unproved. | ATTEMPTED |
| Discrete quadratic forms and compactness | Primitive plaquette generation, confining electric energy and min-max yield fixed-index convergence on a fixed contractible graph. Growing-volume constants remain uncontrolled. | ATTEMPTED |
| Dirichlet oscillator and Gaussian tails | Finite gS retains a demonstrably different vacuum. Increasing gS is a constructive escape within the same regulator family. | ATTEMPTED |
| Integer sublattice and homology countermodels | Doubled shifts preserve two copies; periodic cubes retain three harmonic directions. These disprove extensions obtained by dropping stated hypotheses. | ATTEMPTED |
| Direct physical matrix comparison | Full link-field enumeration and separate CAR matrices challenge the reduction and its signs on a charged cycle. This is a finite check, not a phase proof. | ATTEMPTED |

These are different mathematical objects and obligations. The procedural
route count is not exhaustive proof against unexamined phase constructions.

**N2 — Implication audit.** Let R be the exact reduction, S the fixed-graph
spectral convergence, P the interacting thermodynamic phase, and C the common
interacting cone. R is used to prove S here, but R alone imposes neither a
weak-coupling limit nor primitive magnetic generation. S does not prove P,
as it supplies no uniform growing-volume control. No converse P=>this R or S
is asserted for other encodings. P and C are separate target descriptions
whose logical equivalence or independence has not been established here.
No independent-wall count is assigned to these unresolved relations.

**N3 — Hidden-premise scan.** Contractibility is over the integers; all
elementary plaquettes and positive fixed weights are specified. Total charge
is neutral and the finite matter space is nonempty. Bounded matter couplings,
fixed graph, positive a, unit-amplitude shifts, retained magnetic identity
terms, the g-scaled embedding and the limiting cutoff are explicit. The
four-orbital model is a supplied specialization. Its free Bloch behavior is
not assumed in an open box, and its interacting thermodynamic spectrum is
not inferred. Classical gauge fixing is not a physical preparation gate.

**N4 — Residual matching.** The current integer-link source is used for
conditional construction context, not as an obstruction to every regulator.
Horn/Weinstein supplies method history, not this cutoff-dependent spectral
theorem. Nakamura/Tadano section 1 concerns a different embedding and scalar
square-lattice operator: it is contextual rather than a substituted proof
of the charged moving-domain claim. No historical no-go is imported as a
witness against the full target.

**N5 — Resolution audit.** Per element, exact weighted projections and
integer link displacements are checked. Per site, direct CAR actions and
Gauss neutrality are checked. Per mode, Dirichlet oscillator coefficients,
Gaussian bounds and nonprimitive copies are checked. Per block, open-box
integer generation and the direct charged-cycle matrix are checked.
Lattice wide, the theorem quantifies over each fixed finite contractible
box; a periodic rank comparator is checked. The thermodynamic spectrum,
charged poles and common interacting cone are not tested or established.

**N6 — Partial closure and conventions.** The affine-coordinate isometry
and finite-volume spectral comparator close a supplied-model obligation.
Changing the vacuum energy zero cannot remove the missing Gaussian mass
at fixed finite gS. Allowing gS to diverge is an explicit same-family escape;
finite-spin encodings or other observables can have different requirements.
None of these choices automatically introduces a framework axiom.

**N7 — Steelman.** The strongest positive reading is that exact Gauss
dressing is compatible with a weak-coupling physical spectrum whose finite
levels approach oscillator and matter sums. It motivates, rather than proves,
a stable charged Coulomb phase. A successful uniform correlation/RG argument
or an independent finite-spin construction could settle a broader target
without contradicting the boundary or topology counterexamples.

**N8 — Cross-cycle echo.** Earlier campaign work controlled finite-time
truncation and ground-state plaquette/angle statistics. The new terminal
object is the physical finite-volume spectrum with exact charge dressing.
The remaining phase gap is not counted again as a new axiom deficit.
Periodic holonomies and growing-volume control are the next research targets.

## Author checks and verification limits

The runner independently enumerates all four-link electric fields satisfying
Gauss law and builds separate CAR matrices, then compares the complete charged
Hamiltonian with the cycle-coordinate matrix at S=1,2. This fixture has one
orbital per site, two particles and eta=(0,1,0,1); it is explicitly smaller
than the supplied four-orbital three-dimensional carrier. Open cubical boxes
check exact incidence, rooted-tree cycles and Smith invariants. Weighted
oscillator frequencies are compared against the direct curl matrix, including
the open cube frequencies (2,2,2,sqrt(6),sqrt(6))/a.

The one-plaquette hypergeometric boundary reference is compared with an
independent continuum finite-difference matrix. Finite hard-link charged
spectra approach both the finite-boundary targets and, when gS grows, the
first four full-space oscillator/matter sums. A doubled-shift model retains
two low clusters. Exact symbolic substitution checks the even ODE recurrence.
These finite checks do not certify compactness, arbitrary graph size, a
joint error rate or the thermodynamic phase; those claims stand or fall with
their actual proofs and stated limitations.

Raw exploration, source history, canonical execution and deliberate
wrong-formula checks are preserved in the branch packet. All execution and
source review in this campaign were personal author work. Independent review,
full integrated validation and formal audit remain pending; no retained
status is granted by the author checks.
'''
note.write_text('\n'.join(line.rstrip() for line in (front+body+end).splitlines())+'\n')
shutil.copy2(cp/'check_block14.py',runner)
for name in ['BLOCK14_SEED.md','BLOCK14_DERIVATION.md','block14_spectral_explore.py','BLOCK14_SPECTRAL_EXPLORATION.json','BLOCK14_SPECTRAL.stdout','BLOCK14_SPECTRAL.stderr']:
    if (cp/name).exists(): shutil.copy2(cp/name,packet/name)
shutil.copytree(cp/'BLOCK14_PRIOR_CHECK',packet/'prior_check',dirs_exist_ok=True)
(packet/'LITERATURE_SCOPE.md').write_text('''# Reading scope and method provenance

Horn/Weinstein SLAC-PUB-2864: sections 2 and 3.2-3.4 read in full in the
preceding block; general gauge reduction/projected-flow method context.
Nakamura/Tadano arXiv:1903.10656v1: section 1, assumptions A/B, Theorem 1.1
and corollaries read; section 2.1 and 2.2 displayed and examined for the
Fourier embedding and relative-potential control. The remaining proof was
not read in full. Its norm-resolvent theorem is not imported. The note gives
its own fixed-index form/compactness argument for its different domain.
The cutoff and charge-domain derivation preceded this comparison search.
No novelty of the general maximal-tree or continuum-limit method is claimed.
''')
print(json.dumps(dict(note=str(note),runner=str(runner),packet=str(packet))))
