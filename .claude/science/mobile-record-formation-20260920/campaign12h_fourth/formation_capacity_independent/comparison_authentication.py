from pathlib import Path
import hashlib
import json
from datetime import datetime, timezone

HERE = Path(__file__).resolve().parent
AUTHOR = HERE.parent/'formation_capacity_author'

def bind(path):
    raw = path.read_bytes()
    return dict(path=str(path),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())

def verify(entry):
    actual = bind(Path(entry['path']))
    assert actual['bytes']==entry['bytes'] and actual['sha256']==entry['sha256'], entry['path']
    return actual

pre_path = HERE/'PRE_COMPARISON_SEAL.json'
pre_id = bind(pre_path)
assert pre_id['sha256']=='85c7668c76e47cc472f7b04b380f27f267ab7a3323f39b87b722223286bf45e4'
pre = json.loads(pre_path.read_text())
for entry in pre['sources']+pre['artifacts']: verify(entry)
author_path = AUTHOR/'AUTHOR_SEAL.json'
author_id = bind(author_path)
assert author_id['sha256']=='bffa8a7045bb3b787c09e7ab20ca7650662d83d403976fd6a958daa8094b3288'
author = json.loads(author_path.read_text())
for entry in author['sources']+author['artifacts']: verify(entry)
main = json.loads((AUTHOR/'ANALYTIC_DRAFT_SEAL.json').read_text())
extension = json.loads((AUTHOR/'REACTIVATION_DRAFT_SEAL.json').read_text())
for entry in [main['artifact'],*main['sources'],*extension['artifacts']]: verify(entry)
run = json.loads((AUTHOR/'CAPACITY_CONTROL_RUN_RECEIPT.json').read_text())
verify(run['runner'])
assert run['exit_code']==0 and run['command'][1]==run['runner']['path']
assert (AUTHOR/'CAPACITY_CONTROL.stderr.log').read_bytes()==b''
data = json.loads((AUTHOR/'CAPACITY_CONTROL_RESULTS.json').read_text())
assert data['source_sha256']==run['runner']['sha256']
decoder = json.JSONDecoder()
stream = (AUTHOR/'CAPACITY_CONTROL.stdout.log').read_text()
objects = []
while stream.strip():
    stream=stream.lstrip()
    obj,n=decoder.raw_decode(stream)
    objects.append(obj)
    stream=stream[n:]
assert len(objects)==2
assert objects[0]=={k:v for k,v in data.items() if k!='periodic_stationary_controls'}
assert objects[1]=={'stationary_summaries':[
    {k:v for k,v in row.items() if k not in ('charge_word','integer_Gauss_field')}
    for row in data['periodic_stationary_controls']]}
assert sum(r['complete_Gauss_matter_words'] for r in data['finite_number_balance'])==195
assert sum(r['jump_columns_checked'] for r in data['finite_number_balance'])==3510
assert sum(r['legal_jump_outputs'] for r in data['finite_number_balance'])==532

bindings = [author_id,*author['sources'],*author['artifacts']]
result = dict(created_utc=datetime.now(timezone.utc).isoformat(),
    preserved_PRE=pre_id, PRE_bindings_reauthenticated=len(pre['sources'])+len(pre['artifacts']),
    author_seal=author_id, all_author_bindings_reauthenticated=len(author['sources'])+len(author['artifacts']),
    nested_draft_bindings_reauthenticated=1+len(main['sources'])+len(extension['artifacts']),
    main_draft_created_utc=main['created_utc'], extension_draft_created_utc=extension['created_utc'],
    author_run_receipt_verified=True, author_streams_match_result_exactly=True,
    author_scientific_runner_reexecuted=False,
    author_finite_scope=dict(matter_words=195,jump_columns=3510,nonzero_output_words=532,
        field_scope='One spanning-tree field per matter word; no exhaustive electric scan.'),
    read_scope='Full main argument, reactivation extension, interpretation, runner, seals and receipt; all result summary/channel fields read and all recorded periodic charge/field components independently checked by comparison_reactivation_control.py.',
    bindings=bindings)
(HERE/'COMPARISON_SOURCE_BINDINGS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in [
    'PRE_bindings_reauthenticated','all_author_bindings_reauthenticated',
    'nested_draft_bindings_reauthenticated','main_draft_created_utc',
    'extension_draft_created_utc','author_run_receipt_verified',
    'author_streams_match_result_exactly','author_scientific_runner_reexecuted']},indent=2))
