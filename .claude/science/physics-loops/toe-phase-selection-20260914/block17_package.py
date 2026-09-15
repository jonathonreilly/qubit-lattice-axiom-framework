from pathlib import Path
PACK=Path(__file__).parent
ROOT=Path('/Users/jonreilly/Documents/Codex/toe-coupled-defect-convexity-20260915')
ns={'__file__':str(PACK/'block15_16_package.py')};text=(PACK/'block15_16_package.py').read_text();exec(compile(text[:text.index('for s in SPECS:')],'<package-helpers>','exec'),ns)
s=dict(block=17,note='FREE_CUBIC_MAGNETIC_LOCAL_FILLINGS_AND_POSITIVE_ELECTRIC_CURRENT_CONVEX_EXTENSION_BOUNDED_THEOREM_NOTE_2026-09-15.md',runner='free_cubic_magnetic_local_fillings_and_positive_electric_current_convex_extension_2026_09_15.py',title='Local magnetic fillings and the exact positive electric-current extension',
scope='For the supplied finite-clock Villain law on free four-dimensional cubic boxes, a boundary-compatible local integer filling extends the provisional carrier theorem to the actual magnetic Hodge kernel. Its locally marked source has uniform curvature bounds. At the stated sufficient smallness, summing magnetic defects gives an exact positive electric-current marginal with a uniformly convex real extension in the Coulomb current metric. The integer marginal retains both defects; no fixed-clock photon limit follows.',
next='Independently review the boundary/source bridge and then control the integer-current infrared limit, preserving the current lattice and physical-score observables.')
deps=['carrier_preserving_closed_integer_charge_gas_convexification_bounded_theorem_note_2026-09-15','finite_clock_exact_coupled_electric_magnetic_defect_representation_bounded_theorem_note_2026-09-15']
header=ns['header'](s).replace('upstream_dependencies: []','upstream_dependencies:\n'+''.join('  - '+x+'\n' for x in deps).rstrip())
header=header.replace('There are no repository theorem premises. Geometry and probability law are\nsupplied data. Standard mathematical machinery is derived where used.','The two explicit provisional premises are the carrier theorem and exact\ncoupled-defect identity included in this PR. Both await independent review.\nThe new proof below supplies the boundary and local-source bridge.')
header=header.replace('The exact phase/model match and infinite-volume physical limit remain\nseparate obligations; neither is inferred from the finite checks.','The thermodynamic phase and physical-score limit remain separate\nobligations; neither is inferred from the finite checks.')
header+='''
| Premise | Revision status and precise use |
|---|---|
| [Carrier theorem](CARRIER_PRESERVING_CLOSED_INTEGER_CHARGE_GAS_CONVEXIFICATION_BOUNDED_THEOREM_NOTE_2026-09-15.md) | Same-PR provisional source; rooted mass bound, explicit constants and finite-dimensional variance estimate |
| [Coupled-defect law](FINITE_CLOCK_EXACT_COUPLED_ELECTRIC_MAGNETIC_DEFECT_REPRESENTATION_BOUNDED_THEOREM_NOTE_2026-09-15.md) | Same-PR provisional source; exact integer-current/magnetic-coset identity and source normalization |
| Cubic boundary filling and actual Hodge kernel | Derived in section1 and matched in section2 here |
| Positive electric marginal and convex extension | Derived in sections3-4; the extension away from integer currents depends on the fixed filling convention |
| Fixed-order photon law and matter | Open; no Gaussian limit is inferred from convexity |

'''
body=(PACK/'BLOCK17_LOCAL_SOURCE_AND_POSITIVE_ELECTRIC_EXTENSION_DERIVATION.md').read_text()
body=body[body.index('## 1.'):].replace('block15','the carrier theorem').replace('block16','the coupled-defect theorem').replace('The the coupled-defect theorem','The coupled-defect theorem')
appendix='''
## 6. Finite evidence and negative-claim discipline

Four finite families check absolute, one-face-relative and full-relative
integer tensor homotopies; top-degree and anisotropic boundary controls;
actual three/four-cube Hodge spectra and source-energy identities; and
fifteen real-current Hessians for the exact one-mode magnetic quotient
of a single three-cube, compared with multiprecision finite differences.
That last finite quotient is a chain-rule control and does not execute the
uniform p<d filling theorem or a four-dimensional phase.

### N1 — Materially distinct attempted inferences

| Honesty | Inference attempted | Outcome |
|---|---|---|
| ATTEMPTED | Use an absolute contraction for every boundary carrier | The proof and exact tensor checks keep absolute, one-face-relative and full-relative homotopies distinct. |
| ATTEMPTED | Include top-degree charges under the same local support bound | Unit-mass top-degree interval charges require increasingly long fills;1<=p<d is retained. |
| ATTEMPTED | Replace cubic domains by arbitrary thin rectangles | A mass2 boundary-crossing carrier in a thin rectangle has an increasingly large least fill. |
| ATTEMPTED | Demand representative invariance for all real currents | Integer currents have phase ratio1; a half-current control has ratio-1. The real extension is explicitly constructed and convention-dependent. |
| ATTEMPTED | Differentiate the source normalization without its variance | The all-source bound retains the nonnegative variance term and the resulting denominator1-beta epsilon. |
| ATTEMPTED | Infer a photon limit from a convex extension of integer weights | The actual measure remains on the current lattice; its infrared correlations are an additional obligation. |

No route is ruled out by prior retained authority. These are distinct
assumption checks, not independent physical walls.

### N2 — Dependencies

This source composes two explicit provisional proofs. The boundary lemma
and source bridge are new obligations checked here; their use does not
retroactively give either premise independent retained status. Relations
to native formation, the N=3 penalty Hamiltonian and matter remain unknown.
The extension's metric convexity is not a theorem about current quantization.

### N3 — Hidden assumptions

Domains are free cubic boxes,1<=p<d, with the actual cubical Hodge kernel
and integer cohomology. Odd component fillings are fixed once. The source
extension for real currents is defined by those fillings; only integer
values have the original representative invariance. All smallness
conditions are explicit. The physical law has not acquired continuous
current variables or a new primitive.

### N4 — Residual matching

Relative homotopies test the same integer interval tensor construction.
Hodge matrices and source norms use the actual finite-cube incidence.
The exact three-cube scalar magnetic quotient checks a finite extension's
normalization and Hessian, not the universal cubic filling proof.
The positive marginal sums every magnetic charge and keeps the exact
electric current lattice; no negative mixed term is simply discarded.

### N5 — Resolution

The runner prints substantive per_element,per_site,per_mode,per_block and
lattice_wide evidence. The finite homotopies, rational source relations
and finite-difference Hessians are executed. General local fillings,
infinite cluster sums, all-box convexity and a physical infrared limit
are checked and not executed; the written proof carries the first three,
while the infrared limit remains open.

### N6 — Partial paths

The exact integer-current marginal and its controlled real extension
provide a specific next target. Its current lattice, source interaction
and physical-score correlations still require an infrared analysis.
A direct score argument remains possible. No axiom or primitive is
changed or declared inadequate by these bounds.

### N7 — Steelman

The main criticism is that a smooth convex extension is not the same as
a Gaussian scaling limit of an integer-current measure. This is correct,
even when the Hessian is close to its Coulomb quadratic form. Pointwise
weight bounds can accumulate volume-dependent normalization differences.
The construction supplies the exact integer marginal and a controlled
extension; it does not supply missing photon dispersion, charged matter
or a native probability law.

### N8 — Cross-cycle comparison

The carrier theorem's original Dirichlet kernel was narrower than the
actual magnetic law. This note explicitly proves the cubic-boundary and
Hodge-kernel bridge. The exact coupled-defect identity still has negative
individual mixed terms; complete magnetic summation gives the positive
marginal used here. Growing-coupling limits and fixed-law image-noise/Ward
distinctions retain their stated scope and are not promoted to phase proofs.

## 7. Personal review status

The derivation and all finite checks were performed personally without
subagents. Independent review and formal audit of all three linked sources
remain pending. The next step is the integer-current infrared theorem
and its match to physical-score observables.
'''
(ROOT/'docs'/s['note']).write_text(header+body+appendix)
r=(PACK/'block17_local_source_check.py').read_text().replace('from pathlib import Path','AUDIT_TIMEOUT_SEC = 180\nfrom pathlib import Path',1)
r=r[:r.index("if __name__=='__main__':")]
r+="if __name__=='__main__':\n rows=run()\n print(json.dumps(rows,indent=2))\n"
lines=[
('per_element','executed exact integer interval/tensor homotopies with absolute, one-face-relative and full-relative boundaries.'),
('per_site','executed top-degree unit-charge and thin-rectangle mass2 controls whose least fillings grow beyond a fixed local carrier.'),
('per_mode','executed exact three/four-cube Hodge spectra, conserved-current source norms and integer versus half-current phase shifts.'),
('per_block','executed fifteen exact one-mode magnetic quotient Hessians and multiprecision finite differences for real electric-current extensions.'),
('lattice_wide','checked and not executed: cubic local filling, source-curvature and exact positive-marginal convexity rely on the stated proofs; the integer-current infrared limit remains open.')]
r+=''.join(' print('+repr(k+': '+v)+')\n' for k,v in lines)
(ROOT/'scripts'/s['runner']).write_text(r)
print('source',len((header+body+appendix).splitlines()),'runner',len(r.splitlines()))
