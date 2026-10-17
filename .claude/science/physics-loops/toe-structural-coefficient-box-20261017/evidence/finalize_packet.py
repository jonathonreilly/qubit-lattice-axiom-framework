"""Archive compact publication evidence outside the canonical input closure."""
from pathlib import Path
import hashlib
import gzip
import json
import shutil

D=Path(__file__).resolve().parent
W=D.parents[1]/'correlation_worktree'
Q=W/'.claude/science/physics-loops/toe-structural-coefficient-box-20261017'
E=Q/'evidence';E.mkdir(exist_ok=False)
names=['PRE_RUN_PLAN.md','METADATA_ADAPTATION.json','WHITESPACE_ADAPTATION.json',
       'PR9662_VERIFICATION.json','pr9662_inventory.json','canonical.stdout','canonical.stderr',
       'GRAPH_EXECUTIONS.json','GRAPH_VERIFICATION.json','GRAPH_RETRY_PLAN.json',
       'graph_build.stdout','graph_build.stderr','graph_manifest.stdout','graph_manifest.stderr',
       'adapt_metadata.py','prepare_records.py','mutations.py','run_canonical.py','graph_check.py',
       'focused_verify.py','finalize_packet.py','NOTE_REFRESH.json','refresh_wrapper.py',
       'CANONICAL_REPEAT_COMPARISON.json']
for name in names: shutil.copyfile(D/name,E/name)
shutil.copytree(D/'mutations',E/'mutations')
for script in (E/'mutations').glob('*/mutated.py'):
    # Preserve executed bytes, including historical trailing spaces, without
    # introducing whitespace defects in new text diffs. Raw copies remain in D.
    (script.parent/'mutated.py.gz').write_bytes(gzip.compress(script.read_bytes(),mtime=0))
    script.unlink()
shutil.copytree(D/'graph_attempt_1',E/'graph_attempt_1')
shutil.copytree(D/'canonical_attempt_1',E/'canonical_attempt_1')
shutil.copyfile(D/'CANONICAL_EXECUTION.json',Q/'CANONICAL_EXECUTION.json')
execution=json.loads((D/'CANONICAL_EXECUTION.json').read_text())
graph=json.loads((D/'GRAPH_VERIFICATION.json').read_text())
root_review=Q/'ROOT_WRAPPER_REVIEW.json'
assert hashlib.sha256(root_review.read_bytes()).hexdigest()=='9f943f6d46cc3621082f84bfc7be5e843955398a601c42a8adaf8a05e2b3f738'
for name in ('CLAIM_STATUS_CERTIFICATE.md','REVIEW_HISTORY.md','HANDOFF.md'):
    path=Q/name
    text=path.read_text()
    if name=='CLAIM_STATUS_CERTIFICATE.md':
        text=text.replace('Root review of the final publication wrapper\nand implementation remains pending; source acceptance alone does not approve\nthis wrapper.', 'Root has approved the final publication wrapper and implementation for\nregular conditional publication, subject to focused packet/staging checks,\nin [its separate record](ROOT_WRAPPER_REVIEW.json). This is no landing approval.')
    elif name=='REVIEW_HISTORY.md':
        text=text.replace('Root review of the final wrapper and implementation is pending.',
                          'Root approved the final wrapper and implementation for conditional\npublication, subject to focused packet/staging checks, in\n[its separate record](ROOT_WRAPPER_REVIEW.json).')
    else:
        text=text.replace('Root must independently read the final wrapper, primary and\nevidence before choosing publication.',
                          'Root has read and approved the final wrapper and primary in\n[its separate record](ROOT_WRAPPER_REVIEW.json), subject to focused\npacket/staging checks before publication.')
    path.write_text(text)
(Q/'PUBLICATION_REVIEW.md').write_text('''# Publication implementation review

This is a source-exposed packaging check, not an independent science verdict.
The author theorem, separate physical-bit review and root qualification were
already accepted for conditional reuse. The complete new wrapper, primary
and helper were read for code/prose drift. The embedded theorem is verified
byte-identical; complete calculation ASTs are compared to frozen source
bodies, with only the recorded resource dictionaries excepted. All source
coefficients, equations and scientific assertions are unchanged.

The wrapper preserves exact prescribed block forms, darkness, K and J,
the same supplied finite ready vector, literal old aging, both old energy
sectors, complete old/source/clock/passive-reference outputs and actual nu.
It distinguishes the ten-variable actual-scalar result from the nine-variable
fixed-nu corollary. The positive vacuum-leakage discriminator is explicitly
outside the coefficient box. The huge clock costs, finite-clock horizon,
original calibration residual and larger source/contact loads remain visible.
The independent reviewer was source-exposed and same-model; this implementer
also has prior source authorship and review exposure.

The primary's direct helper import is explicit. Both calculations execute in
one process with CPU60 and external wall60; the nested original limits are
now historical. The helper's legacy `author_program_executed: false` field
describes what that helper itself calls: it does not import or execute the
author program. The outer primary does execute both portable calculations,
as its scope and shared-process metadata state. The nested author's
`independent_review: false` likewise labels that calculation's scope.

Input hashes are reported for the full declared closure and independently
bound by the canonical cache authority's pre/post execution identity. The
canonical output slot is initialized before the first identity capture;
the second run uses that existing slot. Publication receipts are kept outside
the declared closure. After root's two publication-only note edits, the first
canonical result/cache/receipt were archived and a second canonical run was
performed under the same limits. Every scientific field agrees exactly;
only the note input hash and elapsed-time fields differ. No canonical note,
program or declared input changed after the latest successful run.

Eight single-change copied-code mutations failed at their named scientific
assertions: coefficient radius, inverse ceiling, omitted closed-tail
variation, vacuum darkness, signed surface recurrence, noncommuting product
order, common phase and finite-clock horizon. No checksum failure counts.
Subsequent blank-line cleanup preserves both complete module ASTs, and its
record explains reuse without another mutation run. These discriminators do
not prove the infinite-operator argument or broaden its accepted scope.
The portable mutated programs are lossless gzip copies of the exact executed
bytes; decompression hashes are checked against their original receipts.

The canonical runner exited0 in '''+str(execution['elapsed_sec'])+''' seconds,
with157 helper assertions and no stderr. Its exact extra reflection bound is
approximately0.00020268904500846948; the complete supplied-readiness and
finite-clock bounds are approximately0.011147623271512414 and
0.012147623271512415. Decimals are display only; exact rationals govern.
No grid, quadrature, fit, time evolution or large clock allocation ran.

The first citation-graph attempt exceeded the initial60-second cap; its
source, streams and failure receipt are preserved. One explicitly declared
180-second retry completed, then the manifest writer ran sequentially. The
only topology change is the structural note and its edge to the prior
two-body theorem. Existing nodes and dependency entries are unchanged. The
later note metadata and root-record link change preserves every graph
extraction field except the note hash, checked with the actual builder's
functions. The original generated graph keeps its actual earlier note hash
as validation residue; the topology manifest remains correct. No second
successful graph build or manual generated-hash refresh is claimed.

Deterministic readiness, vocabulary, input freshness, helper discovery,
compilation, links and topology outcomes are recorded in
[PUBLISH_CHECKS.json](PUBLISH_CHECKS.json). They do not substitute for root
review or the shared integrated-main landing gates. Root's separate
[wrapper review](ROOT_WRAPPER_REVIEW.json) now approves regular conditional
publication subject to the focused packet/staging checks; it gives no
retained status or landing approval.
No staged change, commit, push, PR, audit verdict, prompt, axiom or shared
recovery-checkpoint edit was made by this implementation task.
''')
print(json.dumps({'archived_evidence_files':sum(p.is_file() for p in E.rglob('*')),'canonical_elapsed_seconds':execution['elapsed_sec'],'graph_added':graph['added']},indent=2))
