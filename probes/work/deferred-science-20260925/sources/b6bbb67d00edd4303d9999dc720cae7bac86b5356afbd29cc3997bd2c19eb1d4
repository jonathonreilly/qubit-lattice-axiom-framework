"""One-time clean publication construction; no scientific source edits."""
from pathlib import Path
import hashlib,json,re,subprocess

E=Path(__file__).resolve().parent;R=E/'formation-response-publication';A=E/'formation-response-sum-personal'
base='60c5f194d940a7bbaf1cdd545296e31d74a02f1a'
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip()==base
assert subprocess.check_output(['git','status','--porcelain'],cwd=R)==b''
packet='.claude/science/physics-loops/mobile-record-formation-response-20260925'
note='docs/ORIGINAL_FORMATION_AND_FIELD_RESPONSE_BUDGET_BOUNDED_THEOREM_NOTE_2026-09-25.md'
runner='scripts/original_formation_and_field_response_budget_2026_09_25.py'
runtime=packet+'/runtime/response_sum_controls.py';out='outputs/formation_response_20260925'
parents=['docs/LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md',
 'docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md',
 'docs/FORMATION_BALANCE_AND_UNSATURATED_DARK_STATES_BOUNDED_THEOREM_NOTE_2026-09-24.md']
expected=['7c5bc10d0ca1127c2a1ef6f5cf9269caf6e8f023a09a061c2da0d8e033e35a7a','c63db3296e5705c57693c2deb109e506f336fae4848d3ab0926d13a98929802b','2ae8d264eaff3ab47ecf4ec41fa21178ff444546bcc2e36d885d092732e30516']
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for rel,digest in zip(parents,expected):assert sha(R/rel)==digest
assert sha(A/'FORMATION_AND_WILSON_RESPONSE_BUDGET_ROOT.md')=='229ec44bb80c1450fbba8b45d6a586a489edebd21aab8fc0db9f43ab74401eaa'
assert sha(A/'response_sum_controls.py')=='dfd21b49faefe51eaedf1a70c75671a9aaf9b58a20cbbed276259148328bdfc5'
cid=Path(note).stem.lower()
header='---\nclaim_id: '+cid+'\nclaim_type: bounded_theorem\nclaim_scope: "Exact conditional common-law aggregate impulse-response/count budget with full matter dynamics and the original formation instrument; no measured probe identification, photon lifetime or microscopic derivative transfer."\nupstream_dependencies:\n'
for rel in parents:header+='  - '+Path(rel).stem.lower()+'\n'
header+='runner: '+runner+'\n---\n\n'
front='''**Type:** bounded_theorem
**Status:** conditional mathematics with scoped independent PRE/POST checks; no retained audit status.

# Original formation and the field-response budget

In the supplied common matter/rotor model, each original formation event reduces
a particular aggregate field-response strength by the same amount. Summing both
Wilson-loop quadrature impulse responses over every elementary cubic plaquette
gives a bounded response operator proportional to the number of vacant B sites.
Exact number balance then fixes its complete preparation-time change from the
original formation count. The normalized relation cancels the supplied electric
coefficient K. This is a joint restriction on precisely defined model
observables, with their experimental identification still open.

The response strength is the initial-lag slope of an impulse experiment made
at each actual preparation time. The state at that time includes all prior
births and subsequent matter/field evolution. A statement at arbitrary finite
preparation time does not determine a finite-lag propagation kernel, stationary
frequency spectrum, photon attenuation or microscopic derivative limit.

The root personally derived the argument and primitive controls below, before
reading a separate sealed PRE reconstruction. Released-source POST found no
required mathematical repair. The author's sufficient fourth-electric-moment
domain and its preservation proof are retained unchanged. The independent PRE
also gives a stronger moment-free response result by a bounded strong-quotient
argument, a positive quadrature-response matrix and an explicit stationary
unsaturated example with nonzero response. Those additions remain separately
attributed in the complete review report; this publication's root response
proof does not rely on them. The bounded count identity itself already holds
for every normal initial state in the root argument.

Loop-family conventions matter: the cubic coefficients use ordinary elementary
plaquettes. On L=4, counting every graph four-cycle would add winding cycles
and change the coefficient. All terms of the full Hamiltonian remain present
regardless of the selected response-loop family. The degree-three cube uses
its own coefficient and is not a surrogate for a degree-six torus.

The earlier initial electric-noise and Wilson-acceleration calculations are
prior photon-bridge results, not new conclusions of this unit. Native probe,
state, scale and readout identification, and uniform control for transferring
an initial-lag derivative from finite microscopic resources, remain open.

## Complete personal argument

'''
old='Personal conditional root candidate, 25 September 2026. No independent\nconfirmation is claimed here.'
new='Personally derived conditional result, 25 September 2026. Separate scoped\nPRE and POST checks are complete; no retained audit status.'
source=(A/'FORMATION_AND_WILSON_RESPONSE_BUDGET_ROOT.md').read_text();assert source.count(old)==1
body=re.sub(r'^(#{1,6}) ',lambda m:'#'*(len(m[1])+2)+' ',source.replace(old,new),flags=re.M)
footer='''
## Reproduction, sources and review scope

The primary runner executes an exact copy of the sealed personal integer
program in a temporary directory. The full scientific output and both streams
are retained, and the original sealed writer is never run in its source
directory. Geometry, electric second differences and actual primitive birth
columns are controls for the displayed proof; they are not a finite-time
simulation, a microscopic response experiment or a comparison with data.

The evidence packet retains the personal seal, separate independent PRE and
POST, their controls and full source/exposure records. A final released-source
publication correspondence check is distinct from the blind PRE; no extra
independence is inferred from a source-hash or cache match. Failed routes and
the author's switch from exploratory second moments to a sufficient fourth
moment remain recoverable. No audit verdict or merge is part of this unit.

The three direct parents are:

'''
for rel,label in zip(parents,['Original local-pair instrument and magnetic dynamics','Full compensated common matter/field law','Formation number balance and unsaturated dark states']):
    footer+='- ['+label+']('+Path(rel).name+').\n'
assert not (R/note).exists();(R/note).write_text(header+front+body+footer)
(R/runtime).parent.mkdir(parents=True);(R/runtime).write_bytes((A/'response_sum_controls.py').read_bytes())
template=(E/'microscopic-energy-budget-publication/scripts/microscopic_ground_energy_and_formation_budget_2026_09_25.py').read_text()
tail=template[template.index('from pathlib import Path'):]
for oldtext,newtext in [('microscopic-energy-budget-','formation-response-'),('microscopic_control.','response_control.'),
 ('SPIN_ENERGY_CONTROL_RESULTS.json','RESPONSE_SUM_RESULTS.json'),('MICROSCOPIC_ENERGY_BUDGET_PUBLIC_RESULTS.json','FORMATION_RESPONSE_PUBLIC_RESULTS.json'),
 ('Fresh reuse of exact root cycle controls for the microscopic transfer; no numerical cubic residence theorem or new independent check.','Fresh reuse of exact root geometry, Gauss, electric-identity and original-birth controls; no dynamical simulation, measured probe or new independent check.')]:
    assert oldtext in tail;tail=tail.replace(oldtext,newtext)
wrapper='#!/usr/bin/env python3\n"""Fresh exact-source original-formation response controls."""\nAUDIT_TIMEOUT_SEC = 120\nAUDIT_INPUT_PATHS = '+repr(tuple([note,*parents,runtime]))+'\nOUTPUT_DIRECTORY = '+repr(out)+'\nRUNTIME = '+repr(runtime)+'\n'+tail
(R/runner).write_text(wrapper)
manifest={'base_revision':base,'base_branch':'main','branch':'codex/mobile-record-formation-response-budget-20260925',
 'packet':packet,'note':note,'runner':runner,'runtime':[runtime],'output_directory':out,'parent_paths':parents,
 'cache':'logs/runner-cache/original_formation_and_field_response_budget_2026_09_25.txt',
 'result':out+'/FORMATION_RESPONSE_PUBLIC_RESULTS.json','source_note':str(A/'FORMATION_AND_WILSON_RESPONSE_BUDGET_ROOT.md'),
 'presentation_replacements':[{'old':old,'new':new}],'heading_level_increment':2,
 'source_files_sha256':{rel:sha(R/rel) for rel in [note,runner,runtime,*parents]}}
with (E/'FORMATION_RESPONSE_PUBLICATION_WORKING_SOURCES.json').open('x') as stream:json.dump(manifest,stream,indent=2);stream.write('\n')
print(json.dumps(manifest,indent=2))
