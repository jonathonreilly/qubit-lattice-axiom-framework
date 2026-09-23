from pathlib import Path
import json,hashlib,difflib,subprocess
r=Path('/private/tmp/review-drain-20260915');w=r/'author-draft-slot'
p=json.loads((r/'drain8030-author-prepared-v1.json').read_text());f=w/p['note'];old=f.read_text()
needle='Equivalently, a demonstrably nonzero propagation speed bounded by this LR parameter could not coexist with a bounded gap in this uniformly weak scaling window.'
replacement='The original propagation/bounded-gap noncoexistence certification is also explicitly deferred under N1. The preceding quantitative implication is retained with its stated hypotheses; it is not promoted here into a certified negative classification.'
assert old.count(needle)==1
new=old.replace(needle,replacement)
marker='## Accepted scope and deferred certification\n'
record='''## No-Go Discipline Gate: DEFERRED N1–N8 applicability record

Both the separated-field exclusion certification and the propagation/bounded-gap noncoexistence certification remain **DEFERRED**. The following applicability record identifies existing mathematics and controls; it does not declare a negative-claim PASS or claim five independent failed in-domain routes.

| Item | Applicability and evidence boundary |
| --- | --- |
| N1 — alternative routes | DEFERRED: the required route coverage is not established. Uniform versus pointwise clustering, pairwise smearing versus applying a support-union prefactor, wrong exponential-series degree, clock direction, the extra actual-gap upper premise, and contact/repeated-plaquette/FDD scope are inference controls, not five failed in-domain mechanisms. |
| N2 — independence of the obstruction | DEFERRED: equation (1) explicitly imports a uniform clustering estimate for the selected state in one sufficiently small fixed window. No claim that this premise is independent of every proposed alternative mechanism is certified. |
| N3 — hidden assumptions | DEFERRED: support sizes, operator norms, positive separation, coefficient budgets, supplied mesh and clock, and the additional actual-gap upper bound are explicit hypotheses. Removing them has not been exhausted. |
| N4 — residual matching | DEFERRED: the positive contact FDD is retained, with overlapping/contact supports distinct from positively separated supports. It does not furnish a physical dynamical limit or certify the residual alternatives exhaustively. |
| N5 — resolution and execution | DEFERRED for negative certification. The scaling program specifies exact series-degree, weighted-budget and clock-ratio arithmetic and adverse checks; uniformity and support-union applicability are analytical checks in the proof. The contact program specifies moment normalization, 27 actual plaquette link sets, repeated-plaquette adversity, and Taylor/logarithm constants and mesh exponent. Its per-element, per-site, per-mode and per-block classes refer only to those finite fixtures; lattice-wide labels do not mean the clustering theorem or FDD limit was executed. These unchanged programs have historical evidence; no new capture has been performed for this draft. Scaling TOTAL18 includes one resource predicate; contact TOTAL13 has a separate resource guard. |
| N6 — partial closure | DEFERRED: the retained bounds and constructive Haar FDD require no new axiom. Changing norm/support assumptions, coupling window, dynamics or the supplied time/mesh relationship would require a separately justified statement, not a convention silently inserted here. |
| N7 — strongest alternative | DEFERRED: the actual contact FDD is a constructive alternative to conflating all statistical limits with separated-field dynamics. It does not exhaust alternatives involving changed hypotheses or interacting/dynamical limits. |
| N8 — prior-cycle consistency | DEFERRED: complete original arguments, controls and failures remain in the exact recovery archive. Their repetition or historical review does not establish the missing current route coverage. |

'''
assert new.count(marker)==1;new=new.replace(marker,record+marker)
new=new.replace('The original separated-field negative classification remains procedurally deferred;', 'The original separated-field and propagation/bounded-gap noncoexistence certifications remain procedurally deferred;')
# Independent byte checks: all original indented mathematical lines and the exact implication remain.
assert [x for x in old.splitlines() if x.startswith(' ')]==[x for x in new.splitlines() if x.startswith(' ')]
imp='Second, for this LR upper parameter even to remain at least some fixed V_0>0, (3) forces G_ell>=V_0/(16e u_* ell), hence a diverging actual gap lower bound.'
assert imp in old and imp in new
for item in p['files']:assert hashlib.sha256((w/item['path']).read_bytes()).hexdigest()==item['sha256']
f.write_text(new)
patch=r/'drain8030-author-corrections-v2.patch';assert not patch.exists();patch.write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='prepared-v1/'+p['note'],tofile='prepared-v2/'+p['note'])))
for item in p['files']:item['sha256']=hashlib.sha256((w/item['path']).read_bytes()).hexdigest()
p['version']=2;p['supersedes']='drain8030-author-prepared-v1.json';p['affected_review']='drain8030-early-affected-review-v1.json';p['scope_repairs']=['A1: explicitly deferred propagation/bounded-gap noncoexistence certification, preceding inequality byte-identical','A2: honest DEFERRED N1–N8 record; named finite/analytical controls, no quota PASS'];p['deferred_scope']='Separated-field and propagation/bounded-gap noncoexistence negative certifications remain deferred under unmet N1.';p['v2_validation']={'indented_math_lines_byte_identical':True,'preceding_conditional_inequality_byte_identical':True,'runner_bytes_unchanged':True,'new_execution':False,'empty_evidence_placeholders_created':False}
assert not subprocess.check_output(['git','diff','--name-only'],cwd=w).strip();assert not subprocess.check_output(['git','diff','--cached','--name-only'],cwd=w).strip()
out=r/'drain8030-author-prepared-v2.json';assert not out.exists();out.write_text(json.dumps(p,indent=2)+'\n');print(hashlib.sha256(out.read_bytes()).hexdigest())
