"""Integrate the read wrapper while retaining all four mathematical bodies."""
from pathlib import Path
import datetime
import hashlib
import json
import shutil

N=Path(__file__).resolve().parents[1]
W=N.parent/'correlation_worktree'
D=N/'two_body_integration'
F=W/'outputs/two_body_autonomous_halt_2026_10_17_inputs'
Q=W/'.claude/science/physics-loops/toe-two-body-autonomous-halt-20261017'
Q.mkdir(parents=True,exist_ok=True)
draft=N/'two_body_publication_draft'
name='TWO_BODY_AUTONOMOUS_HALT_BOUNDED_THEOREM_NOTE_2026-10-17.md'
raw=(draft/'docs'/name).read_bytes()
assert hashlib.sha256(raw).hexdigest()=='665758ecf7cc80378ae14ce863b6421f250c0c602f4f98baccf777a70d08835d'
old=(draft/'WRAPPER.md').read_bytes()
assert raw.startswith(old)
wrapper=old.decode()
changes=[]
def change(a,b):
    global wrapper
    assert wrapper.count(a)==1,(a,wrapper.count(a))
    wrapper=wrapper.replace(a,b,1)
    changes.append({'old':a,'new':b})

change('wrapper_root_approval: pending\ncanonical_execution: pending\npublication: pending_and_separate_from_source_acceptance',
       'wrapper_root_approval: separately_recorded\ncanonical_execution: separately_recorded\npublication: separate_from_source_acceptance')
change('independently prepared common product packet.',
       'independently prepared common clock packet, in product with the old input and source vacuum.')
change('''Can an escaping one-head clock perform the fixed old-pair operation with
positive nearest-neighbor two-body added blocks and leave no persistent
added old interaction in the source vacuum? The supplied ladder below gives
a conditional affirmative construction with a certified nonzero calibration
ceiling and explicit packet errors.''',
'''The supplied positive nearest-neighbor two-body ladder implements the fixed
old-pair operation by reflection of an escaping one-head clock, with a
certified nonzero calibration ceiling and explicit complete-output packet
errors. Its source vacuum leaves no persistent added old interaction.''')
change('''Claim type: bounded theorem. The actual source surface is conditional support,
with no retained audit.''',
'''Claim type: `bounded_theorem`. Source-status request: `proposed_retained`.
The actual source surface is `conditional-support`, with no retained audit.''')
change('''This proposed wrapper, canonical execution and publication remain pending.
The source map records original evidence locations and proposed portable
destinations; root must supply actual integration records before publication.

The proposed primary program is scripts/two_body_autonomous_halt_2026_10_17.py,
with a direct import of scripts/two_body_autonomous_halt_check_2026_10_17.py.
The intended output is outputs/two_body_autonomous_halt_2026_10_17.json.
These are planned canonical paths, not a claim that this drafting task created,
ran or approved those programs. The companion publication record belongs in
.claude/science/physics-loops/toe-two-body-autonomous-halt-20261017/.''',
'''The [source decision](../outputs/two_body_autonomous_halt_2026_10_17_inputs/root/SOURCE_ACCEPTANCE.json)
and [qualification](../outputs/two_body_autonomous_halt_2026_10_17_inputs/root/QUALIFICATION.md)
are separate from wrapper review, portable execution and publication. Their
actual integration outcomes are recorded in the
[review history](../.claude/science/physics-loops/toe-two-body-autonomous-halt-20261017/REVIEW_HISTORY.md)
and [publication checks](../.claude/science/physics-loops/toe-two-body-autonomous-halt-20261017/PUBLISH_CHECKS.json).

**Primary runner:** `scripts/two_body_autonomous_halt_2026_10_17.py`.
The root-owned [primary](../scripts/two_body_autonomous_halt_2026_10_17.py)
directly imports the separately written
[check module](../scripts/two_body_autonomous_halt_check_2026_10_17.py).
The [result](../outputs/two_body_autonomous_halt_2026_10_17.json),
[point witnesses](../outputs/two_body_autonomous_halt_2026_10_17_point_witnesses.json)
and [cache](../logs/runner-cache/two_body_autonomous_halt_2026_10_17.txt)
are evidence only for their actual recorded execution and freshness in the
[execution record](../.claude/science/physics-loops/toe-two-body-autonomous-halt-20261017/CANONICAL_EXECUTION.json).
The [source manifest](../.claude/science/physics-loops/toe-two-body-autonomous-halt-20261017/SOURCE_MANIFEST.json)
binds the unchanged mathematical bodies, and the
[artifact manifest](../outputs/two_body_autonomous_halt_2026_10_17_inputs/ARTIFACT_MANIFEST.json)
binds the historical evidence. Historical absolute paths label original runs;
the portable programs consume repository-local declared inputs.''')
change('''old input and any passive reference, as constructed in the concrete source.
Let''',
'''old input and any passive reference, as constructed in the concrete source.
The readiness is a product across old input, source vacuum and clock; the
one-head clock vector need not be a product across its individual qubits.
Let''')
change('''This fixed calibration ceiling remains in every packet estimate.''',
'''Here R(k0) denotes four logical columns at the same kinetic momentum but
old-dependent total energies 2+s+epsilon(k0); it is not a single-energy
four-open-channel scattering matrix. This fixed calibration ceiling remains
in every packet estimate.''')
change('''The later concrete review has SHA256''',
'''The later [concrete review](../outputs/two_body_autonomous_halt_2026_10_17_inputs/frozen_sources/two_body_interval_review/REVIEW.md)
has SHA256''')
change('''This draft does not infer a merge or synchronization into its source tree.
No editable prompt, physical axiom, audit result, repository file or Git state
was changed by the drafting task.''',
'''The [current-main scope](../outputs/two_body_autonomous_halt_2026_10_17_inputs/integration/current_main_scope.json)
records ten unchanged instruction sources and the unchanged original target
body followed by portable-provenance prose. No science was merged into this
branch, and no audit verdict was adopted. Historical process snapshots in
the evidence pack are immutable records; editable prompts and physical
axioms are unchanged.''')
change('''A new regular child PR,
with its own wrapper review and execution, is the proposed packaging route;
the previous PR is not rewritten.''',
'''This milestone is packaged on a child branch of PR9659 with its own
wrapper review and execution; the previous result is unchanged. The
[portability review](../outputs/two_body_autonomous_halt_2026_10_17_inputs/portability/REPORT.md)
checks the complete code adaptation without relabeling the original runs.
Full combined-current-main pipeline, strict lint and changed-evidence checks
remain shared landing gates under conformance section12; independent retained
audit is separate. No landing is authorized or claimed here.''')

combined=wrapper.encode()+raw[len(old):]
(W/'docs'/name).write_bytes(combined)
families=[('generic','finite_channel_wavepacket_bridge/THEOREM_V2.md'),
          ('interval','two_body_interval_bridge/CANDIDATE.md'),
          ('stationary_history','dark_source_two_body_halt/ROUTE.md'),
          ('selected_coefficients','dark_source_two_body_halt/old_cap_search/RESULT.md')]
bodies=[]
for label,rel in families:
    p=N/rel;b=p.read_bytes();assert combined.count(b)==1,rel
    at=combined.index(b)
    bodies.append({'label':label,'source':str((F/'frozen_sources'/rel).relative_to(W)),
                   'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),
                   'body_byte_start_inclusive':at,'body_byte_end_exclusive':at+len(b)})
manifest={'note':{'path':'docs/'+name,'bytes':len(combined),'sha256':hashlib.sha256(combined).hexdigest()},
          'unchanged_bodies':bodies,'draft_note_sha256':hashlib.sha256(raw).hexdigest(),
          'draft_wrapper_sha256':hashlib.sha256(old).hexdigest(),
          'wrapper_refinements':changes,'source_base':'c86e61caf46c848fe8cee57ecbea6e6fdad7a4bc',
          'publication_parent':'f5f5eda7427453aac726b394381c965f9e28ac03',
          'current_main_instruction_revision':'2bb6c1a54721e70512922fb10d4495adf8ea3042',
          'root_source_acceptance_sha256':'fba41e11ee5e282800547e7571ab520abddeda1d9d3947d7095b9dfbf6fbc4fb',
          'scope':'Complete mathematical bodies unchanged. Root read the full wrapper and refined only framing, exact product/energy-column meanings, paths and separate integration-status references. Actual execution/publication remain independently recorded.'}
(Q/'SOURCE_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
(D/'WRAPPER_REVIEW.json').write_text(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'root_wrapper_source_correspondence_approved':True,'note':manifest['note'],
    'source_bodies_checked':len(bodies),'complete_wrapper_read':True,
    'source_acceptance_separate':True,'canonical_execution_at_decision':None,
    'retained_audit':False,'editable_prompt_files_changed':[]},indent=2)+'\n')

artifact=json.loads((F/'ARTIFACT_MANIFEST.json').read_text())
selected=[(D/'SOURCE_ACCEPTANCE.json','root/SOURCE_ACCEPTANCE.json'),
          (D/'QUALIFICATION.md','root/QUALIFICATION.md'),
          (D/'WRAPPER_REVIEW.json','root/WRAPPER_REVIEW.json'),
          (D/'CODE_ADAPTATION.json','integration/CODE_ADAPTATION.json'),
          (D/'main_refresh/SCOPE.json','integration/current_main_scope.json'),
          (draft/'DRAFT_CHECK.json','integration/DRAFT_CHECK.json'),
          (draft/'WRAPPER.md','integration/DRAFT_WRAPPER.md')]
selected += [(x,'portability/'+x.name) for x in (N/'two_body_interval_review/portability').iterdir()
             if x.is_file() and x.suffix!='.pyc']
for src,rel in selected:
    dst=F/rel;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dst)
    b=dst.read_bytes();artifact['files'][rel]={'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
(F/'ARTIFACT_MANIFEST.json').write_text(json.dumps(artifact,indent=2)+'\n')
print(json.dumps({'note':manifest['note'],'unchanged_bodies':len(bodies),
                  'wrapper_refinements':len(changes),'artifact_entries':len(artifact['files'])},indent=2))
