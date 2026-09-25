"""One-shot new POST43 binder/sealer; no author or scientific program rerun."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import ast
import json

HERE=Path(__file__).resolve().parent


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def identity(path):
    raw=path.read_bytes()
    return dict(path=str(path.relative_to(HERE)),sha256=sha256(raw).hexdigest(),bytes=len(raw))


def observed(path):
    st=path.stat()
    raw=path.read_bytes()
    return dict(path=str(path),sha256=sha256(raw).hexdigest(),bytes=len(raw),
                dev=st.st_dev,ino=st.st_ino,mode=st.st_mode,
                mtime_ns=st.st_mtime_ns,ctime_ns=st.st_ctime_ns,nlink=st.st_nlink)


def write(name,obj):
    with (HERE/name).open('x') as f:
        json.dump(obj,f,indent=2);f.write('\n')


assert not (HERE/'POST_SEAL.json').exists()
prior=json.loads((HERE/'POST_PRESERVATION_BEFORE.json').read_text())
prior_paths={Path(row['path']) for row in prior['files']}
assert len(prior_paths)==43
for row in prior['files']:
    assert observed(Path(row['path']))==row
pins=json.loads((HERE/'POST_SOURCE_PINS.json').read_text())
assert len(pins['author_sources'])==12
for row in pins['author_sources']:
    assert observed(Path(row['origin']))==row['observed_origin']
    frozen=HERE/row['frozen_path']
    assert digest(frozen)==row['sha256'] and frozen.stat().st_size==row['bytes']
for row in pins['reused_unchanged_parent_and_procedure_pins']:
    assert digest(HERE/row['frozen_path'])==row['sha256']
    if not row['origin'].startswith('git:'):
        assert digest(Path(row['origin']))==row['sha256']

executions=[]
for label in ('post_freeze','post_comparison','post_typesetting'):
    path=HERE/(label+'.execution.json')
    receipt=json.loads(path.read_text())
    script=Path(receipt['command'][2])
    assert script.parent==HERE and script.name.startswith('post_')
    assert digest(script)==receipt['source_sha256']
    assert digest(HERE/'post_record.py')==receipt['recorder_sha256']
    assert receipt['exit_code']==0 and receipt['elapsed_seconds']>0
    for suffix,log in receipt['outputs'].items():
        data=(HERE/log['path']).read_bytes()
        assert sha256(data).hexdigest()==log['sha256'] and len(data)==log['bytes']
        if suffix=='stderr.txt':assert data==b''
    console=HERE/(label+'.console.txt')
    if console.exists():
        expected=(json.dumps(receipt,indent=2)+'\n').encode()
        expected+=(HERE/receipt['outputs']['stdout.txt']['path']).read_bytes()
        assert console.read_bytes()==expected
        assert (HERE/(label+'.console.stderr.txt')).read_bytes()==b''
    executions.append(dict(receipt=identity(path),script=identity(script),exit_code=0,
                           complete_log_bindings=True,console_checked=console.exists()))

comparison=json.loads((HERE/'post_comparison.stdout.txt').read_text())
assert comparison['complete_author_pair_rows_checked']==175
assert comparison['complete_author_matching_paths_checked']==4
assert comparison['full_matched_dense_Gauss_states_checked']==20
assert comparison['preserved_PRIOR_files']==43
assert comparison['source_sha256']==digest(HERE/'post_compare_read_only.py')
assert comparison['author_scientific_programs_imported_or_executed'] is False
typeset=json.loads((HERE/'post_typesetting.stdout.txt').read_text())
assert typeset['before_sha256']==digest(HERE/typeset['preserved_draft'])
assert typeset['after_sha256']==digest(HERE/'POST.md')
assert (HERE/'post_freeze.stdout.txt').read_bytes()==(HERE/'POST_SOURCE_PINS.json').read_bytes()
tree=ast.parse((HERE/'post_compare_read_only.py').read_text())
for node in ast.walk(tree):
    if isinstance(node,ast.Call):
        if isinstance(node.func,ast.Name):
            assert node.func.id not in {'exec','eval','compile','open','__import__'}
        if isinstance(node.func,ast.Attribute):
            assert node.func.attr not in {'write','write_text','write_bytes','mkdir','unlink','rename','chmod','open','run','Popen'}
assert not list(HERE.rglob('*.pyc'))

write('POST_PRESERVATION_AFTER.json',dict(
    at_utc=datetime.now(timezone.utc).isoformat(),all_43_files_exact=True,
    stat_scope=prior['stat_scope'],files=[observed(Path(row['path'])) for row in prior['files']]))
bindings=dict(
    at_utc=datetime.now(timezone.utc).isoformat(),
    scope='POST43 final source/log/preservation binding only; no science rerun',
    report=identity(HERE/'POST.md'),source_pins=identity(HERE/'POST_SOURCE_PINS.json'),
    prior_PRE_report=identity(HERE/'PRE.md'),prior_PRE_seal=identity(HERE/'PRE_SEAL.json'),
    author_seal=identity(HERE/'post_sources/author/AUTHOR_SEAL.json'),
    author_members=11,author_origins_unchanged=True,prior_43_files_exact=True,
    preserved_before=identity(HERE/'POST_PRESERVATION_BEFORE.json'),
    preserved_after=identity(HERE/'POST_PRESERVATION_AFTER.json'),
    executions=executions,comparison_result=identity(HERE/'post_comparison.stdout.txt'),
    read_only_comparator=identity(HERE/'post_compare_read_only.py'),
    readonly_comparator_AST_write_execution_guard=True,
    full_relevant_target_rows=175,full_matched_paths=4,full_matched_dense_states=20,
    failed_POST_executions=0,
    editorial_math_repair=dict(receipt=identity(HERE/'post_typesetting.stdout.txt'),
                                prior_draft=identity(HERE/typeset['preserved_draft'])),
    author_programs_imported_or_executed=False,old_sealed_writers_executed=False,
    forbidden_external_source_references_followed=False,
    delegation_model_change_publication_audit_or_merge=False)
write('POST_FINAL_BINDINGS.json',bindings)
members=[]
for path in sorted(HERE.rglob('*')):
    if not path.is_file() or path in prior_paths:continue
    assert path.name not in ('POST_SEAL.json','POST_SEAL_RECEIPT.json')
    relative=path.relative_to(HERE)
    assert str(relative).startswith(('post_','POST'))
    members.append(identity(path))
seal=dict(
    sealed_at_utc=datetime.now(timezone.utc).isoformat(),
    phase='Released-source independent POST43 correspondence',
    report=identity(HERE/'POST.md'),source_pins=identity(HERE/'POST_SOURCE_PINS.json'),
    prior_PRE_seal_sha256=digest(HERE/'PRE_SEAL.json'),
    author_seal_sha256=pins['author_seal_sha256'],
    member_count=len(members),members=members,
    exclusion='All original PRE files; POST seal and later receipt cannot self-hash',
    immutable_new_files='New POST members and seal set to mode 0444; original files never chmodded',
    stop_condition='Report sealed hashes and stop; no audit or publication action')
write('POST_SEAL.json',seal)
for row in members:
    assert identity(HERE/row['path'])==row
for row in members:
    (HERE/row['path']).chmod(0o444)
(HERE/'POST_SEAL.json').chmod(0o444)
for row in prior['files']:assert observed(Path(row['path']))==row
for row in pins['author_sources']:assert observed(Path(row['origin']))==row['observed_origin']
receipt=dict(
    at_utc=datetime.now(timezone.utc).isoformat(),member_count=len(members),
    report=identity(HERE/'POST.md'),seal=identity(HERE/'POST_SEAL.json'),
    source_pins=identity(HERE/'POST_SOURCE_PINS.json'),
    all_new_member_hashes_verified=True,all_43_PRE_files_bytes_stat_unchanged=True,
    all_12_author_origins_bytes_stat_unchanged=True,
    new_member_permissions_0444=all((HERE/row['path']).stat().st_mode&0o777==0o444 for row in members),
    outside_own_manifest=True)
write('POST_SEAL_RECEIPT.json',receipt)
(HERE/'POST_SEAL_RECEIPT.json').chmod(0o444)
print(json.dumps(receipt,indent=2))
