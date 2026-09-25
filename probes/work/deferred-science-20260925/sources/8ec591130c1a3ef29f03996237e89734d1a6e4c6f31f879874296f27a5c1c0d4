#!/usr/bin/env python3
"""PRE46 one-time sealing WRITER. No scientific rerun or outside mutation."""
from datetime import datetime, timezone
from pathlib import Path
import difflib, hashlib, json

BASE=Path(__file__).resolve().parent
TARGET=BASE/'PRE_SEAL.json'
assert not TARGET.exists()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def identity(p):
    st=p.stat()
    return dict(sha256=sha(p),bytes=st.st_size,mode=st.st_mode,mtime_ns=st.st_mtime_ns)

sources=load(BASE/'SOURCE_PINS.json')['sources']
assert len(sources)==6
for row in sources:
    assert sha(Path(row['origin']))==sha(BASE/row['snapshot'])==row['sha256']
receipt=load(BASE/'verification_attempt01/EXECUTION.json')
assert receipt['exit_code']==0 and receipt['all_byte_stat_unchanged']
assert receipt['observed_before']==receipt['observed_after'] and len(receipt['observed_before'])==27
assert receipt['source_sha256']==sha(BASE/'verify_readonly.py')==sha(BASE/'verification_attempt01/source.py')
assert receipt['stdout_sha256']==sha(BASE/'verification_attempt01/stdout.json')
assert receipt['stderr_sha256']==sha(BASE/'verification_attempt01/stderr.txt')
assert (BASE/'verification_attempt01/stderr.txt').read_bytes()==b''
result=load(BASE/'verification_attempt01/stdout.json')
assert result['status']=='All read-only PRE46 evidence checks passed'
assert result['magnetic_terms_checked']==553 and result['dissipative_terms_checked']==217
assert result['primitive_branch_rows_checked']==140
repair=load(BASE/'PRE_WORDING_REPAIR.json')
old=BASE/repair['preserved_before'];current=BASE/'PRE.md'
assert sha(old)==repair['before_sha256'] and sha(current)==repair['after_sha256']
assert old.read_text().count(repair['old_phrase'])==1
assert old.read_text().replace(repair['old_phrase'],repair['new_phrase'])==current.read_text()
expected_diff=''.join(difflib.unified_diff(old.read_text().splitlines(keepends=True),current.read_text().splitlines(keepends=True),fromfile='PRE before wording correction',tofile='PRE corrected'))
assert (BASE/'PRE_WORDING_REPAIR.diff').read_text()==expected_diff
for path, previous in receipt['observed_after'].items():
    if Path(path)==current:
        assert previous['sha256']==sha(old) and previous['bytes']==old.stat().st_size
    else:
        assert identity(Path(path))==previous
for folder, program in (('primitive_attempt01','charge_current_control.py'),('fourier_attempt01','fourier_charge_control.py')):
    p=BASE/folder;r=load(p/'EXECUTION.json')
    assert r['exit_code']==0 and r['source_unchanged']
    assert r['source_sha256']==sha(BASE/program)==sha(p/'source.py')
    assert r['stdout_sha256']==sha(p/'stdout.json') and r['stderr_sha256']==sha(p/'stderr.txt')
    assert (p/'stderr.txt').read_bytes()==b''
members=[]
for p in sorted(BASE.rglob('*')):
    if p.is_file():
        assert not p.is_symlink()
        members.append(dict(path=str(p.relative_to(BASE)),sha256=sha(p),bytes=p.stat().st_size))
seal=dict(phase='Blind independent PRE46 before author46 disclosure',sealed_utc=datetime.now(timezone.utc).isoformat(),
          report='PRE.md',report_sha256=sha(current),members=members,source_origins=sources,
          verifier=dict(code='verify_readonly.py',execution='verification_attempt01/EXECUTION.json',
                        stdout_sha256=receipt['stdout_sha256'],elapsed_seconds=receipt['elapsed_seconds'],
                        observed_files_unchanged_during_execution=27,exit_code=0,empty_stderr=True),
          preserved_preseal_wording_repair=dict(record='PRE_WORDING_REPAIR.json',history=repair['preserved_before'],
                                               equations_or_controls_changed=False),
          exposure=dict(prior42_static_law_knowledge_disclosed=True,author46_read=False,
                        forbidden_packets_read=False,prior_or_author_program_import_or_execution=False,
                        delegation=False,publication_or_audit_mutation=False),
          scope='Bounded current continuity and minimum-sector initial connected charge moments in the supplied finite common law; no stationary spectrum, physical units, microscopic derivative or volume-uniform transfer')
with TARGET.open('x') as f:f.write(json.dumps(seal,indent=2,sort_keys=True)+'\n')
for row in members:(BASE/row['path']).chmod(0o444)
TARGET.chmod(0o444)
for row in members:assert sha(BASE/row['path'])==row['sha256']
print(json.dumps(dict(report_sha256=seal['report_sha256'],seal_sha256=sha(TARGET),members=len(members),source_origins=len(sources)),indent=2))
