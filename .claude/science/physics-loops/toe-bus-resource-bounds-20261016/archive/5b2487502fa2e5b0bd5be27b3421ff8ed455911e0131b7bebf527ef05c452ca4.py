"""One-time metadata seal; contains no scientific computation."""
from pathlib import Path
import hashlib, json, datetime
OUT=Path(__file__).resolve().parent
FINAL=OUT/'FREEZE.json'
def sha(data): return hashlib.sha256(data).hexdigest()
def utc(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
if FINAL.exists(): raise RuntimeError('Already frozen; refusing to overwrite.')
sources=json.loads((OUT/'SOURCE_IDENTITIES.json').read_text())
assert sources['source_count']==3 and sources['scientific_executions']==0
for row in sources['sources']:
 data=(OUT/row['capture']).read_bytes()
 assert data==Path(row['source']).read_bytes()
 assert len(data)==row['bytes'] and sha(data)==row['sha256']
checkpoint=dict(completed_utc=utc(),status='complete exposed analytical check; root acceptance pending',
                reviewed_derivation_sha256='2bfb24cce9760be23d750b3b2a190b3110bc0326c035488aae004d1de7849a74',
                scientific_executions=0,scientific_replays=0,source_identities_reverified=3,
                conclusion='The two requested steps are supported under the stated post-selection margins and qualified parent premises.',
                new_proof='Weighted orthogonal polynomials give ||partial_i J|| <= M_0/w_i, including normalization and QR regularity.',
                precision='Recomputed pole-to-full-A2 sensitivities and phase costs are dominated by equations36-37.',
                qualifications=['Fixed selected nodes, bias and spectral charts; no differentiated discrete selection.',
                                'Late U_T is certified before choosing exact rational M; no log-branch derivative.',
                                'Full-space counterterms, actual reserves and phase costs remain charged.',
                                'Norm-aware arithmetic and all qualified parent/physical premises remain.',
                                'No full parent validation or retained audit.'],
                editable_prompt_files_changed=[],canonical_or_git_changes=False)
(OUT/'CHECKPOINT.json').write_text(json.dumps(checkpoint,indent=2)+'\n')
members=[]
for path in sorted(OUT.rglob('*')):
 if path.is_symlink(): raise RuntimeError(f'Symlink in packet: {path}')
 if path.is_file() and path!=FINAL:
  data=path.read_bytes()
  members.append(dict(path=str(path.relative_to(OUT)),bytes=len(data),sha256=sha(data)))
freeze=dict(frozen_utc=utc(),kind='final scoped exposed analytical review',scientific_executions=0,
            member_count=len(members),files=members,
            scope='All local packet files except this root FREEZE.json; three selected upstream sources only.')
FINAL.write_text(json.dumps(freeze,indent=2)+'\n')
for row in members:
 data=(OUT/row['path']).read_bytes()
 assert len(data)==row['bytes'] and sha(data)==row['sha256']
print(json.dumps(dict(status='frozen; all member hashes verified',member_count=len(members),
                      review_bytes=(OUT/'REVIEW.md').stat().st_size,
                      review_sha256=sha((OUT/'REVIEW.md').read_bytes()),
                      freeze_bytes=FINAL.stat().st_size,freeze_sha256=sha(FINAL.read_bytes()),
                      scientific_executions=0)))
