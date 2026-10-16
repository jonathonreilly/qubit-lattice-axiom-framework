"""Metadata-only exact-source capture and final freeze; no science replay."""
from pathlib import Path
import hashlib, json
from datetime import datetime, timezone
OUT=Path(__file__).resolve().parent
N=OUT.parent
W=N.parent/'correlation_worktree'
S=OUT/'sources'; S.mkdir(exist_ok=True)
def ident(p):
 p=Path(p); b=p.read_bytes()
 return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def write(name,obj): (OUT/name).write_text(json.dumps(obj,indent=2)+'\n')
sources=[]
def capture(label,path,expected,coverage,role):
 item=ident(path); assert item['sha256']==expected,(str(path),item,expected)
 dst=S/(label+Path(path).suffix); dst.write_bytes(Path(path).read_bytes())
 assert ident(dst)['sha256']==expected
 sources.append({'original':item,'captured':ident(dst),'read_coverage':coverage,'role':role})

capture('bus_note',W/'docs/STRONGLY_REGULAR_BUS_BOUNDED_THEOREM_NOTE_2026-10-15.md',
 '1733b2962df77699f6dcf13538916cc0a9780802ea82a93a8c56c373a717700b',
 'Complete wrapper, complete unchanged author proof and complete exposed review; initial overlong display repaired by targeted ranges 230-296,297-325,325-494,495-681,682-796 and727-752. Prior authored proof coverage reused at unchanged identity.',
 'Conditional bus statement, literal positive blocks, geometry, moments input and exact runtime phase/order.')
capture('bus_acceptance',N/'strongly_regular_bus_root_review/QUALIFIED_ACCEPTANCE.json',
 'cc2e519d8c4de174cc98137a8f9c5e2ae7df6a782adfd93d7389d1eac346c726','Complete current read.','Qualified source acceptance; no retained audit.')
capture('bus_qualifications',N/'strongly_regular_bus_root_review/FINAL_QUALIFICATIONS.md',
 'a182e0074ac9b8ed1d9e9e57627d289754252e2969446099ed502e229bf61880','Complete current read.','Controlling bus domain/effectiveness/supplier qualifications.')
capture('installed_background',W/'docs/INSTALLED_BACKGROUND_AUXILIARY_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-15.md',
 '7d48af3dc97630d1adc21ac6cbce02fe602aeea14d4b81e2edad54944c9cb021',
 'Complete overview28-100; complete generic fast-pulse source/premises/generators/full-reference comparison107-242. Later normalized-success and recurrence proofs not imported or claimed fully read.',
 'Interface comparison: different binary-vacuum consumer, explicit control/readiness supplies. No chain costs transferred.')
capture('installed_readiness',W/'docs/INSTALLED_GENERATOR_PREPARATION_READINESS_BOUNDED_THEOREM_NOTE_2026-10-15.md',
 'cdb42d6682ee56968c20229b2e012a23afc6de75bceab0f42f06bc94b95a4fe6',
 'Complete overview34-146, with34-98 repair after a combined display truncated; complete central energy argument149-260. Other preserved independent derivations and reader composition bodies not imported or claimed fully read.',
 'Interface comparison: supplied expectation for a specific mediator; no bus phase or purity supplier.')
capture('compensated_reservoir',W/'docs/COMPENSATED_FINITE_RESERVOIR_CLOCK_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-15.md',
 'd28bb8d6a39ffcdce60f61fb47414abdcdd00e2cbbbb32013c4f8277b2a72ac8',
 'Complete overview32-141 and complete unchanged central proof228-930 in two untruncated reads. Separate projective-speed refinement142-225 not used or claimed read.',
 'Reused method: positive complements, C-infinity profiles, full SWAP, paid ramps, full-output Duhamel, scalar/work/moment accounting. Boundary-specific constants not transferred.')
capture('finite_reservoir',W/'docs/FINITE_RESERVOIR_BOUNDARY_CLOCK_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-15.md',
 '3560cefa1c9a9e8064a11d2fc683bedd0cab3109905df5bffecdbe1999ad15ad',
 'Complete unchanged central proof104-644; its boundary apparatus values remain context, not bus constants.',
 'Reused full-output reservoir SWAP contract and exact finite-memory information accounting.')
capture('quantitative_acceptance',N/'quantitative_bias_selection_root_review/QUALIFIED_ACCEPTANCE.json',
 '810d46f26c0883a470c010783fe310e0e0af9ee1a82f025ac32893bf45294fff','Complete current read.','Context only; no preparation premise imported.')
capture('quantitative_qualifications',N/'quantitative_bias_selection_root_review/FINAL_QUALIFICATIONS.md',
 '1aab69f2d3407be3718e91a3b7e61ef0f24426691b69c3d97682de5893106386','Complete current read.','Context/scope boundary only.')

governance=[]
for path,expected in [
 (N/'bootstrap/planning/AGENTS.md','3d409e93abb3b58796a9c10ca6d21ba93b7edc73b8fb24e7364da97c805580a9'),
 (N/'bootstrap/sources/docs/ai_methodology/SCIENCE_WORKFLOW.md','05f3ec8e58ccd7a4d2a87643fb7ed4f12998c6a1d5721e3632a502de8a0ad6ce')]:
 item=ident(path); assert item['sha256']==expected
 governance.append({**item,'coverage':'Complete prior coherent-task read reused at unchanged identity.'})
for path,expected in [
 (N/'bootstrap/sources/docs/ai_methodology/skills/workhorse/SKILL.md','9801055aea637b0e6f765f1558113a9998fe6b4d5a213b0d03d096fe96cb4cdb'),
 (Path('/Users/jonreilly/.codex/skills/physics-claim-reviewer/SKILL.md'),'9d841edd05b9dc4c5145abcfd5352cd45460a1cc57c23c1eabd131590dbb1455')]:
 item=ident(path); assert item['sha256']==expected
 governance.append({**item,'coverage':'Already applied; complete prior coherent-task read reused at unchanged identity.'})

rec=json.loads((OUT/'check_run/EXECUTION.json').read_text())
launch=json.loads((OUT/'check_run/LAUNCH.json').read_text())
assert rec['exit_code']==0 and not rec['timed_out']
for k in ['source_at_launch','launcher_at_launch','stdout','stderr']: assert ident(rec[k]['path'])==rec[k]
for k in launch: assert launch[k]==rec[k]
assert (OUT/'check_release_moments.py').read_bytes()==(OUT/'check_run/executed_source.py').read_bytes()
assert (OUT/'run_check.py').read_bytes()==(OUT/'check_run/launcher_at_launch.py').read_bytes()
initial=json.loads((OUT/'INITIAL_FINDINGS_FREEZE.json').read_text())
assert ident(initial['path'])=={k:initial[k] for k in ['path','bytes','sha256']}
assert initial['utc']<rec['started_utc']

write('SOURCE_MANIFEST.json',{'utc':datetime.now(timezone.utc).isoformat(),'sources':sources,'governance_reused':governance,
 'inventoried_not_used':{'path':str(W/'docs/INSTALLED_LOCAL_CLOCK_RESET_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-15.md'),'sha256':'fa4f38f2097a30b141bae9ae6115ec81e95102c61b94d509536ac81bba8cf0b8','coverage':'Filename, size/hash and headings only; no Markov/reset theorem imported.'},
 'external_web_sources':[],'scientific_executions':1,'old_science_replays':0,'editable_prompt_files_changed':[]})
(OUT/'EXPOSURE.md').write_text('''# Exposure and dependency boundary

This is a same-model exposed continuation. The worker authored the earlier bus and static-bias transfer and reviewed the chain/quantitative extensions. No fresh independent parent validation is claimed. The current preparation papers were read before designing this bus adaptation; their compensation, SWAP, Duhamel, waveform and finite-memory methods are explicitly credited. No native-supplier conclusion is imported from their conditional status.

The exact quantitative-selection acceptance is context only. No padding extension or generic-domain implication is imported. Installed-background and readiness notes are used to compare their actual interface, with partial-source coverage made explicit in SOURCE_MANIFEST.json. Complete compensation and reservoir central arguments were read; unrelated preserved alternative arguments were not silently treated as read.

INITIAL_FINDINGS.md was frozen before constructing the new check. One new exact64-dimensional compression discriminator was written from the algebra and executed. No old scientific code was loaded or run. All streams were read. It checks a concrete missing-off-code-energy risk; it is not bus propagation, physical validation or a family proof.

The physical deliverable is a conditional driven-model interface. Fresh independent pure memory, physically supplied positive complements, phase/timing references, isolation/calibration and any microscopic drive outputs and energy remain conditions. Root owns acceptance; no retained audit or publication is performed.
''')
(OUT/'FAILURES_AND_LIMITS.md').write_text('''# Failures, rejected inferences and verification limits

No scientific execution failed and no scientific rerun occurred. One exact new check completed with exit0, source and launcher fixed at launch, full stdout and empty stderr preserved.

Initial large source displays were truncated: the bus combined canonical display, a combined preparation overview, and a bus-review display. They were not counted as complete coverage by themselves. Required proof intervals were recovered with smaller targeted reads; the last review gap was repaired at727-752. Source coverage lists both completed arguments and bodies not imported.

Rejected inferences are preserved in DERIVATION.md: the different mediator readiness certificate is not a bus preparation theorem; identical installed mean/variance cannot choose among orthogonal coherent phases; symmetric-code compression loses off-code density-counterterm variance; a reduced controller channel does not certify external drive outputs; algebraic compensation does not erase either physical channel's incident load; finite-window success does not imply permanent halt or reuse.

The fresh check uses N=3, one source, two bus sites and one old qubit, dimension64. Its source frequency is an algebra fixture, not a full calibrated strong-spectral routed-bus instance. It verifies operator compressions, complement identity and a source-phase orientation, not pulse evolution or a complete source family. The analytic proof supplies the general statements.

No microscopic driver, fresh-memory supply, cooling, physical energy observable or autonomous schedule was constructed. No claim is made that the existing preparation contracts automatically provide those resources.
''')
(OUT/'CHECKPOINT.md').write_text('''# Current final checkpoint

DERIVATION.md contains a complete conditional preparation/release theorem for the accepted strong-spectral bus. Existing preparation notes do not directly supply this bus's coherent source input. Their paid-compensation method adapts with explicit positive complementary controls, fresh vacuum memory, ordinary-NN matching and phase-referenced local rotations.

The complete modeled comparator retains every old/controller/memory/reference output and has phase C0*A_u+pi*n_S/4. Runtime composition yields e^(-isH) W e^(-i(T+tau)H) at laboratory time T+tau+s, with the bus's source and reserve phases retained. The modeled preparation incident cap is2J_*+g, independent of accuracy; slew and global resources may grow. Release first/second moments include the complete off-code NN source fluctuations, and explicit smaller trace budgets give requested preparation moment accuracy.

One new exact64-dimensional check passed. Its symmetric-code mutant preserves the mean but omits4/352947 of second moment for its chosen fixture. The analytical phase discriminator shows orthogonal sources with identical first two installed moments. Complete source/launcher/streams are in check_run.

Unclosed physical premises: fresh purity and memory isolation, actual complementary interactions and phase/time controls, full-generator and pointwise-load calibration, and a microscopic external driver with its complete retained output and energy budget. No native supplier, permanent halt, reader or reset/reuse follows. This is same-model exposed work and root acceptance remains pending.

All source identities and read coverage are in SOURCE_MANIFEST.json, with exact copies under sources/. FREEZE.json binds all final members. No canonical/Git/PR/cache/graph/lock/prompt/axiom/audit/publication/other-chat state was changed.
''')
write('VERIFICATION.json',{'utc':datetime.now(timezone.utc).isoformat(),'kind':'Metadata-only source identity and receipt verification.',
 'source_captures_verified':len(sources),'scientific_receipt':ident(OUT/'check_run/EXECUTION.json'),
 'source_and_launcher_equal_launch_copies':True,'initial_findings_precede_new_check':True,
 'full_scientific_streams_read':True,'scientific_executions':1,'scientific_failures':0,'scientific_replays':0})
members=[ident(p) for p in sorted(OUT.rglob('*')) if p.is_file() and p.name!='FREEZE.json']
write('FREEZE.json',{'utc':datetime.now(timezone.utc).isoformat(),'status':'Frozen conditional source proposal; root acceptance pending.',
 'scope':'Driven installed-bus preparation and release with explicit remaining physical suppliers; no native or microscopic driver claim.',
 'members':members,'scientific_executions':1,'retained_audit':False,'fresh_independent_parent_validation':False,'editable_prompt_files_changed':[]})
print(json.dumps({'derivation':ident(OUT/'DERIVATION.md'),'freeze':ident(OUT/'FREEZE.json'),'frozen_members':len(members),'source_captures':len(sources)},indent=2))
