"""Finish publication metadata before canonical execution; keep historical copies fixed."""
from pathlib import Path
import ast
import datetime
import hashlib
import json
import shutil

D=Path(__file__).resolve().parent
W=D.parents[1]/'correlation_worktree'
Q=W/'.claude/science/physics-loops/toe-structural-coefficient-box-20261017'
def digest(raw): return {'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
def pin(p): return {'path':str(p.relative_to(W)),**digest(p.read_bytes())}
def write(p,x): p.write_text(json.dumps(x,indent=2)+'\n')

# Wrapping introduced whitespace-only blank lines. Fix before the canonical
# run. Mutation evidence remains reusable because complete module ASTs are
# identical before/after this formatting operation, including all assertions.
backup=D/'pre_whitespace_adaptation'; backup.mkdir(exist_ok=False)
format_rows=[]
for name in ('structural_coefficient_box_2026_10_17.py','structural_coefficient_box_check_2026_10_17.py'):
    p=W/'scripts'/name; old=p.read_bytes()
    (backup/name).write_bytes(old)
    text=old.decode(); cleaned='\n'.join(line.rstrip() for line in text.splitlines())+'\n'
    old_ast=ast.dump(ast.parse(text),include_attributes=False)
    new_ast=ast.dump(ast.parse(cleaned),include_attributes=False)
    assert old_ast==new_ast
    p.write_text(cleaned)
    format_rows.append({'path':str(p.relative_to(W)),'before':digest(old),'after':digest(p.read_bytes()),
                        'complete_module_ast_unchanged':True,'ast_sha256':hashlib.sha256(old_ast.encode()).hexdigest(),
                        'removed_trailing_space_lines':[i for i,l in enumerate(text.splitlines(),1) if l.rstrip()!=l]})
write(D/'WHITESPACE_ADAPTATION.json',{'scope':'Formatting only; prior mutation evidence applies to the identical complete module ASTs. Frozen source copies untouched.','files':format_rows})
m=json.loads((D/'METADATA_ADAPTATION.json').read_text())
m['canonical_primary']=pin(W/'scripts/structural_coefficient_box_2026_10_17.py')
m['canonical_helper']=pin(W/'scripts/structural_coefficient_box_check_2026_10_17.py')
m['later_whitespace_adaptation']='WHITESPACE_ADAPTATION.json records AST-identical formatting; mutation tests predate only this whitespace normalization.'
write(D/'METADATA_ADAPTATION.json',m)
s=json.loads((Q/'SOURCE_MANIFEST.json').read_text())
s.update(canonical_primary=m['canonical_primary'],canonical_helper=m['canonical_helper'],
         whitespace_adaptation='evidence/WHITESPACE_ADAPTATION.json')
write(Q/'SOURCE_MANIFEST.json',s)

inventory=json.loads((D/'pr9662_inventory.json').read_text())
assert inventory['headRefOid']=='3f641f336a1ab6ea36f37b3ccfbbbe5269241fc7'
assert len(inventory['files'])==len({f['path'] for f in inventory['files']})==45
write(D/'PR9662_VERIFICATION.json',{'checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
      'authority':'Read-only gh pr view against actual Git origin jonathonreilly/qubit-lattice-axiom-framework',
      'number':9662,'head':inventory['headRefOid'],'base':inventory['baseRefOid'],'file_count':len(inventory['files']),
      'raw_response':digest((D/'pr9662_inventory.json').read_bytes()),
      'coverage':'Complete returned PR body and45-path inventory read; no scientific source review of that unrelated PR.',
      'scope':'Supplied Pauli-stabilizer classification and charge motion. Not a premise of this structural coefficient result. START count45 is confirmed at this observed head.'})

(Q/'TRACE_GATE.md').write_text('''# Trace to the supplied two-body reflection theorem

This bounded theorem gives a nonzero absolute coefficient tolerance for the
supplied autonomous reflection ladder. Its downstream consumer is
[the two-body theorem](../../../../docs/TWO_BODY_AUTONOMOUS_HALT_BOUNDED_THEOREM_NOTE_2026-10-17.md).
The trace is upstream support: exact positive block forms, a dark source
vacuum, old K, uniform clock J, nominal calibration and supplied finite
readiness remain premises. This result does not supply a native apparatus,
an emitter preparation, general noise tolerance or retained status.

The new uniform resolvent comparison adds less than 0.000203 to the prior
complete-output estimate. Actual physical nu is used in the ten-variable
comparison. Holding nominal nu fixes one coefficient and leaves the stated
nine-variable corollary. Finite clock size limits the time domain.

The complete frozen argument, reused premise closure, separate source
review and conditional root acceptance are linked from the
[canonical note](../../../../docs/STRUCTURAL_COEFFICIENT_BOX_BOUNDED_THEOREM_NOTE_2026-10-17.md).
The publication implementation verifies transport and deterministic evidence;
it supplies no new independent science verdict.
''')
(Q/'CLAIM_STATUS_CERTIFICATE.md').write_text('''# Claim-status certificate

The proposed claim type is `bounded_theorem`; the actual surface is
`conditional-support`, with trace `upstream_support`. Conditional source
acceptance is recorded in the immutable source archive. The complete-output
bounds are below 0.0112 for every t>=2*10^13 on the infinite blank clock and
below 0.0122 only through t=4*10^13 on the stated finite clock. These depend
on exact prescribed block forms and the same independently supplied ready
vector. The comparator retains literal old aging and actual scalar phase.

No bare retained status or physical provenance is claimed. Independent
retained audit, integrated-main pipeline, strict lint and changed-evidence
gates remain later obligations. Root review of the final publication wrapper
and implementation remains pending; source acceptance alone does not approve
this wrapper. No audit verdict or editable prompt is written by this packet.

Actual finite execution and focused checks are recorded in
[PUBLISH_CHECKS.json](PUBLISH_CHECKS.json). A later author commit, push or PR
is outside this implementation task.
''')
(Q/'REVIEW_HISTORY.md').write_text('''# Source and publication review record

Root source acceptance
`ec522e7c0a20ac95c47e3c8b87af9fdc683e135e54269afd251ba97e5cb207c5`
qualifies the complete frozen coefficient argument conditionally. Independent
source report
`7ec59622c9acaf321bc2363839a8631f81c5b1b75e78a99a03c7500366b4f5f8`
is source-exposed, same-model checking through a separately written
physical-bit, signed-recurrence and noncommuting implementation. The original
author child pin is explicitly post-execution; the independent source
execution is launch-pinned. Neither historical receipt is rewritten.

The publication implementer previously authored the stationary source and
worked on the generic bridge review and two-body packaging. This is shared
model/source exposure, not another independent scientific review. The
root-qualified source mathematics is reused here. Full canonical wrapper and
both calculation bodies were read; their transport, exact body bytes and
metadata adaptation were checked separately from the inherited science.

The portable calculation ASTs differ from the frozen bodies only in two
resource-report dictionaries. Historical limits remain labeled historical;
both portable calculations share CPU60/wall60. A later blank-line whitespace
cleanup preserves complete module ASTs, so the eight scientific mutation
results remain applicable without repeating them. Exact changes, source pins
and actual streams are in [the metadata record](evidence/METADATA_ADAPTATION.json),
[whitespace record](evidence/WHITESPACE_ADAPTATION.json) and
[mutation results](evidence/mutations/RESULTS.json).

Root review of the final wrapper and implementation is pending. Canonical
execution, focused checks, combined-main gates and publication are separate
events; no retained audit or full landing approval is implied.
''')
(Q/'HANDOFF.md').write_text('''# Publication handoff

This packet is prepared on `physics-loop/toe-structural-coefficient-box-20261017`
above parent HEAD `0e8375354c42963234cc4b15b14ab6bb553c713d` (PR9661).
The implementation task leaves every path unstaged and creates no commit,
push or PR. Root must independently read the final wrapper, primary and
evidence before choosing publication. If PR9661 remains open, it must land
first or join the actual integrated landing delta.

The exact argument is preserved inside the canonical note. The47 historical
artifacts are immutable declared data. The50 primary inputs include that
closure, its manifest, the canonical note and directly imported helper.
Publication receipts are outside that input closure to avoid circular cache
freshness. Any later change to the primary, note or a declared input requires
a new canonical run; a receipt edit is not a substitute.

See [actual publication checks](PUBLISH_CHECKS.json),
[canonical execution](CANONICAL_EXECUTION.json),
[source manifest](SOURCE_MANIFEST.json) and
[publication evidence map](PUBLICATION_EVIDENCE.json).
The adjacent PR9662 body and full45-file inventory were read at its pinned
head; its distinct stabilizer scope is not imported.

The generated citation_graph.json is validation residue. Only the intended
citation_graph_manifest.json topology delta belongs in the publication set.
Full integrated-current-main pipeline, strict lint and changed-evidence
checks are later shared gates under review-loop conformance section12.
Independent retained audit remains separate. No prompts, axioms, policy,
audit verdict or shared recovery checkpoint changed in this task.
''')
print(json.dumps({'format_ast_unchanged':True,'pr9662_files':45,'canonical_primary':m['canonical_primary'],'canonical_helper':m['canonical_helper']},indent=2))
