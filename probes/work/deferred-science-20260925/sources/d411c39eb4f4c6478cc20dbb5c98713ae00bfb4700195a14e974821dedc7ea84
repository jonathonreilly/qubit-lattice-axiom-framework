"""One-time author46 evidence writer/sealer; no scientific execution."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
D=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert not (D/'AUTHOR_SEAL.json').exists() and not (D/'ROOT_READ_RECEIPT.json').exists()
for row in json.loads((D/'SOURCE_PINS.json').read_text())['sources']:assert sha(Path(row['origin']))==row['sha256']
for path in ['attempt01/EXECUTION.json','ROOT_READONLY_EXECUTION.json']:
 r=json.loads((D/path).read_text());assert r['exit_code']==0
assert (D/'attempt01/stderr.txt').read_bytes()==(D/'ROOT_READONLY.stderr.txt').read_bytes()==b''
assert sha(D/'CHARGE_CURRENT_AND_INITIAL_COVARIANCE_ROOT.md')=='b8bec7cc03e7af401aae097445ae24faecd45dcffd8e0273300f16d17d455c1d'
r=dict(at=datetime.now(timezone.utc).isoformat(),author_note_sha256=sha(D/'CHARGE_CURRENT_AND_INITIAL_COVARIANCE_ROOT.md'),
 complete_working_and_final_argument_read=True,complete_all_new_code_read=True,full_final_note_diff_read=True,
 all_five_compact_mean_covariance_and_current_groups_read=True,all_8480_raw_rows_mechanically_checked=True,
 all_raw_vectors_manually_read=False,primary_result_sha256=sha(D/'attempt01/stdout.json'),
 readonly_result_sha256=sha(D/'ROOT_READONLY.stdout.json'),failed_scientific_attempts=[],
 independence='Personal derivation and personal data reconstruction, not independent confirmation. Root42 PRE/POST already known. No independent45 argument read.',
 observation='Existing bounded charge-current/covariance consequence before fitting, conditional on supplied model and initial matter. No measured finite-frequency noise or empirical identification.')
(D/'ROOT_READ_RECEIPT.json').write_text(json.dumps(r,indent=2)+'\n')
members=[]
for p in sorted(D.rglob('*')):
 if p.is_file():
  assert not p.is_symlink() and '__pycache__' not in p.parts
  members.append(dict(path=str(p.relative_to(D)),sha256=sha(p),bytes=p.stat().st_size))
s=dict(at=datetime.now(timezone.utc).isoformat(),phase='Personal author46 before independent46 request or disclosure',
 note='CHARGE_CURRENT_AND_INITIAL_COVARIANCE_ROOT.md',note_sha256=sha(D/'CHARGE_CURRENT_AND_INITIAL_COVARIANCE_ROOT.md'),
 members=members,source_pins_sha256=sha(D/'SOURCE_PINS.json'),independent_confirmation=False,
 scope='Supplied original matter/field generator, bounded charge continuity and initial normal-state charge covariance derivative; no finite-time spectrum, physical calibration or audit status.')
(D/'AUTHOR_SEAL.json').write_text(json.dumps(s,indent=2)+'\n')
for row in members:(D/row['path']).chmod(0o444)
(D/'AUTHOR_SEAL.json').chmod(0o444)
for row in members:assert sha(D/row['path'])==row['sha256']
print(json.dumps(dict(note_sha256=s['note_sha256'],seal_sha256=sha(D/'AUTHOR_SEAL.json'),members=len(members)),indent=2))
