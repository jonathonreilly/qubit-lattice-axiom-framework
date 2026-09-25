"""Seal only this new recovery directory after final read-only source checks."""
from pathlib import Path
import datetime, hashlib, json, stat, subprocess

here=Path(__file__).resolve().parent
work=here.parent/'local-charge-observation-publication'
sha=lambda raw:hashlib.sha256(raw).hexdigest()
read=lambda p:json.loads(p.read_text())
pins=read(here/'SOURCE_PINS.json')['members']
successful=read(here/'COMPARISON02.stdout.json')
expected_changes=successful['concurrent_metadata_changes']
changes=[]
for row in pins:
    p=Path(row['original']);s=p.stat()
    current=dict(sha256=sha(p.read_bytes()),bytes=s.st_size,mode=stat.S_IMODE(s.st_mode),
                 mtime_ns=s.st_mtime_ns,ctime_ns=s.st_ctime_ns,inode=s.st_ino)
    delta={k:dict(before=row[k],after=v) for k,v in current.items() if row[k]!=v}
    if delta:changes.append(dict(path=row['original'],changes=delta))
    assert sha((here/row['snapshot']).read_bytes())==row['sha256']
assert changes==expected_changes
git=lambda *args:subprocess.run(['git','-C',str(work),*args],capture_output=True,check=True).stdout.decode()
identity=read(here/'GIT_IDENTITY.json')
assert git('rev-parse','HEAD').strip()==identity['head']
assert git('branch','--show-current').strip()==identity['branch']
assert git('status','--porcelain=v1','--untracked-files=all')==identity['status']
receipt=read(here/'COMPARISON02.execution.json')
assert receipt['exit_code']==0 and receipt['stderr_bytes']==0
assert sha((here/'compare_read_only.py').read_bytes())==receipt['program_sha256']
assert sha((here/'COMPARISON02.stdout.json').read_bytes())==receipt['stdout_sha256']
assert sha((here/'COMPARISON02.stderr.txt').read_bytes())==receipt['stderr_sha256']
preservation=dict(checked_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  original_bytes_unchanged=len(pins),fully_unchanged=len(pins)-len(changes),
                  previously_partial47_chmod_changes=changes,
                  worktree_head_branch_and_status_unchanged=True,
                  original47_new_report_or_seal_read=False)
with (here/'FINAL_PRESERVATION.json').open('x') as f:json.dump(preservation,f,indent=2,sort_keys=True);f.write('\n')
members=[dict(path=str(p.relative_to(here)),sha256=sha(p.read_bytes()),bytes=p.stat().st_size)
         for p in sorted(here.rglob('*')) if p.is_file()]
seal=dict(sealed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
          scope='NEW released-source recovery review of frozen 46+47 publication; not original-reviewer final approval or new blinded derivation.',
          canonical_note_sha256='087ba77c29a8d44a88aa3bb493d34bd1db64e10115a935a7521ea8895a12359e',
          frozen_manifest_sha256=identity['frozen_manifest_sha256'],
          report_sha256=sha((here/'REPORT.md').read_bytes()),
          comparison_stdout_sha256=receipt['stdout_sha256'],
          disposition='No required mathematical or correspondence repair identified within reviewed scope; no integration, publication or audit approval.',
          original47_new_report_or_seal_read=False,
          members=members,member_count=len(members),file_mode_after_seal='0444')
with (here/'SEAL.json').open('x') as f:json.dump(seal,f,indent=2,sort_keys=True);f.write('\n')
for p in here.rglob('*'):
    if p.is_file():p.chmod(0o444)
for row in seal['members']:
    p=here/row['path'];assert sha(p.read_bytes())==row['sha256'] and p.stat().st_size==row['bytes']
print(json.dumps(dict(report=str(here/'REPORT.md'),report_sha256=seal['report_sha256'],
                     seal=str(here/'SEAL.json'),seal_sha256=sha((here/'SEAL.json').read_bytes()),
                     sealed_members=len(members),original_bytes_unchanged=len(pins),
                     original_files_byte_stat_unchanged=len(pins)-len(changes),
                     preserved_external_metadata_changes=len(changes)),indent=2))
