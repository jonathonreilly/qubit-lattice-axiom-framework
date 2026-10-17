from pathlib import Path
import datetime,hashlib,json,importlib.util,sys
sys.dont_write_bytecode=True
N=Path('/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023')
B=N/'local_conserving_sparse_qualified_publication_draft'
R=N/'root_local_conserving_sparse_qualified_publication_review'
def pin(p):
    p=Path(p);b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def verify(p,row):
    a=pin(p);assert a['bytes']==row['bytes'] and a['sha256']==row['sha256'],str(p)
assert pin(B/'FREEZE.json')['sha256']=='8f59a94d8583f02f04b1df7824a47496de789e12d8a4094affc54a38da0b954c'
assert pin(B/'verify_provenance.py')['sha256']=='cd890636262655c771d56dde5273dc8993adafdb2408dd784fbeb611255d97c7'
sp=importlib.util.spec_from_file_location('qualified_sparse_source_metadata',B/'verify_provenance.py')
m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
result=m.verify(B)
assert result['exact_final_inventory_checked'] and result['source_files']==131
manifest=json.loads((B/'SOURCE_MANIFEST.json').read_text())
for row in manifest['source_closure']+manifest['history_records']:
    verify(row['original_path'],row)
    assert Path(row['original_path']).read_bytes()==(B/row['packet_path']).read_bytes()
assert sum(row['bytes'] for row in manifest['source_closure'])==10367578
receipt=json.loads((B/'runs/metadata_checks/EXECUTION.json').read_text())
for key in ['source','launcher']:verify(receipt[key]['path'],receipt[key])
assert Path(receipt['source']['path']).read_bytes()==(B/'verify_provenance.py').read_bytes()
assert Path(receipt['launcher']['path']).read_bytes()==(B/'run_metadata_checks.py').read_bytes()
for row in receipt['inputs_at_launch']:
    for key in ['original','snapshot']:verify(row[key]['path'],row[key])
    assert row['original']['sha256']==row['snapshot']['sha256']
assert receipt['cwd']==str(B) and len(receipt['invocations'])==2
for inv,expected in zip(receipt['invocations'],[2,0]):
    assert inv['exit_code']==expected and inv['expected_exit']==expected
    assert inv['argv'][2]==receipt['source']['path'] and inv['cwd']==str(B)
    for key in ['stdout','stderr']:verify(inv[key]['path'],inv[key])
    assert inv['stderr']['bytes']==0
    out=json.loads(Path(inv['stdout']['path']).read_text())
    assert out['status']==('UNBOUND' if expected==2 else 'SOURCE_CLOSURE_VERIFIED')
    assert out['exact_final_inventory_checked'] is False and out['scientific_executions']==0
R.mkdir(exist_ok=False)
review='''# Root review of the qualified sparse publication source

Approved for source integration under the existing mathematical and fixture qualifications. This is review of the new wrapper and exact source packet, not a retained audit or approval of a future canonical diff.

Root read the complete current theorem wrapper, PR description, exposure statement, body map, metadata report, README and checkpoint, together with all five packaging/validator scripts. Previously reviewed full arguments, qualifications and actual scientific sources are reused at unchanged identities. Seven full bodies and seven immediate source freezes remain recoverable. All 131 source files (10,367,578 bytes), three bounded historical records and the complete final inventory were refreshed. The validator only checks metadata and defaults to UNBOUND. Its actual source-only and default receipts, source captures, launchers, input snapshots and full streams match the recorded exits 0 and 2; their preseal inventory flag correctly remains false. This root run separately verifies the final exhaustive inventory.

The current wrapper accurately distinguishes the fixed-q laboratory L^4 count from classical compilation complexity. It retains the complete block/complement contract, determinant phase, clean-ancilla isometry, strict path/full-SWAP permission, actual positive reserve/scalar, numerical cancellation requests, guard/post-off timing, initial-plus-final energy allowance and same-F storage. The nominal added cap includes Delta. Physical readiness, all-site access and timing remain supplied. It does not identify a microscopic controller or an autonomous halt.

The later fixture acceptance is incorporated additively. One complex128 emitted propagation, one structural route inspection and floating saved-array reanalysis are distinct evidence. The wrapper does not claim independent circuit replay, interval certification, pulse integration, q>1 coverage, a general executable compiler or useful small reservoir error at L=1. The determinant-omission negative control remains explicit. The earlier preexec failure and unknown cause, and the original publication's unsnapshotted preliminary metadata, remain historical limitations rather than repaired evidence.

The packet's exposure text refers to its supplied old captured instruction revision. This is historical source provenance, not current repository authority. Actual canonical integration must use the root's current instruction/ref binding and actual landed/open parent identities, with a fresh exact wrapper/code/staging review. The old 0903 publication packet and its old a33 review stay unchanged and do not approve these new bytes. All current source packet canonical/base/publication fields remain null. No scientific replay, Git action, retained status, physical-axiom or editable-prompt change was performed by this review.
'''
(R/'REVIEW.md').write_text(review)
r=dict(kind='root_qualified_sparse_publication_source_review',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),disposition='QUALIFIED_SOURCE_INTEGRATION_APPROVED_CANONICAL_CHECKS_PENDING',root_read_complete=True,source_freeze=pin(B/'FREEZE.json'),source_note=pin(B/'THEOREM_NOTE.md'),source_manifest=pin(B/'SOURCE_MANIFEST.json'),source_validator=pin(B/'verify_provenance.py'),metadata_receipt=pin(B/'runs/metadata_checks/EXECUTION.json'),source_files=131,history_records=3,immutable_bodies=7,metadata_verification=result,review=pin(R/'REVIEW.md'),actual_canonical_acceptance=None,actual_git_base=None,publication=None,retained_audit=False,scientific_executions=0,editable_prompt_files_changed=[])
(R/'REVIEW.json').write_text(json.dumps(r,indent=2)+'\n')
(R/'FREEZE.json').write_text(json.dumps(dict(kind='root_qualified_sparse_publication_source_review_freeze',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),members=[pin(R/'REVIEW.md'),pin(R/'REVIEW.json')]),indent=2)+'\n')
print(json.dumps(dict(review=pin(R/'REVIEW.json'),freeze=pin(R/'FREEZE.json'),metadata=result)))
