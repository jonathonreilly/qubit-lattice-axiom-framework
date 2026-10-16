"""One-time metadata seal of this source-exposed analytical review."""
from pathlib import Path
import datetime, hashlib, json
OUT=Path(__file__).resolve().parent
FINAL=OUT/'FREEZE.json'
def sha(data): return hashlib.sha256(data).hexdigest()
def utc(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
if FINAL.exists(): raise RuntimeError('Already frozen; refusing another seal.')
inventory=json.loads((OUT/'SOURCE_IDENTITIES.json').read_text())
assert len(inventory['sources'])==4 and inventory['scientific_executions']==0
for item in inventory['sources']:
 data=(OUT/item['capture']).read_bytes()
 assert data==Path(item['source']).read_bytes()
 assert len(data)==item['bytes'] and sha(data)==item['sha256']
checkpoint=dict(completed_utc=utc(),status='complete exposed analytical review; root acceptance pending',
                sketch_sha256='43fc957f7c1937091d8755365eb4da550fc171cc02083f0c74d034901a9c3340',
                scientific_executions=0,scientific_replays=0,current_sources_verified=4,
                conclusion='Full original C and vacuum E are restored at the declared endpoint within the complete trace budget, conditionally on the new complement amplitude range and inherited premises.',
                qualifications=['Coefficient u in[0,2] is an additional physical-control premise.',
                                'Separate positive source generator from its unitary; scalar cancellation is a full-unitary endpoint identity.',
                                'Use the actual runtime output phase in F_out inverse and retain all actual reserves.',
                                'Uniform target certificate and incident bound must precede duration/program selection.',
                                'All D/C/R correlations and full-space errors remain included; initial independent vacuum E is paid once.',
                                'Endpoint recovery and a finite trace telescope do not supply autonomous halt, infinite reuse or physical drive resources.'],
                analytic_failed_alternative='Using F_phi inverse without runtime phase update leaves E at trace distance2 sqrt(1-cos(omega*t/2)^(2N)) in the one-source endpoint comparison.',
                other_author_recovery_files_read=False,editable_prompt_files_changed=[],canonical_or_git_actions=False)
(OUT/'CHECKPOINT.json').write_text(json.dumps(checkpoint,indent=2)+'\n')
members=[]
for path in sorted(OUT.rglob('*')):
 if path.is_symlink(): raise RuntimeError(f'Symlink in packet: {path}')
 if path.is_file() and path!=FINAL:
  data=path.read_bytes()
  members.append(dict(path=str(path.relative_to(OUT)),bytes=len(data),sha256=sha(data)))
freeze=dict(frozen_utc=utc(),kind='final exposed analytical recovery review',scientific_executions=0,
            member_count=len(members),files=members,
            scope='All local packet files except this root FREEZE.json; exact selected source snapshots, not transitive historical archive validation.')
FINAL.write_text(json.dumps(freeze,indent=2)+'\n')
for item in members:
 data=(OUT/item['path']).read_bytes()
 assert len(data)==item['bytes'] and sha(data)==item['sha256']
print(json.dumps(dict(status='sealed; member hashes verified',members=len(members),
                      review_bytes=(OUT/'REVIEW.md').stat().st_size,
                      review_sha256=sha((OUT/'REVIEW.md').read_bytes()),
                      freeze_bytes=FINAL.stat().st_size,freeze_sha256=sha(FINAL.read_bytes()),
                      scientific_executions=0)))
