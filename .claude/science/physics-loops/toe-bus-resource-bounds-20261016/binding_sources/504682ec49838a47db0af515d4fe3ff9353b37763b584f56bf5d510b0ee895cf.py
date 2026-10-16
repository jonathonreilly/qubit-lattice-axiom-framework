"""Preserve a failed argument check and record actual unchanged-source review."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
N=Path('/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023');D=N/'publication_integration/bus_resource';W=N.parent/'correlation_worktree'
def read(p):return json.loads(p.read_text())
def pin(p):
 b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def same(p,r):assert all(pin(p)[k]==r[k] for k in ('bytes','sha256')),str(p)
f=D/'actions/cache';e=read(f/'EXECUTION.json');launch=read(f/'LAUNCH.json')
assert e['exit_code']==1 and launch['phase']=='cache'
assert launch['argv'][-2:]==['--canonical-review-sha','REPLACE']
for key in ('launch','stdout','stderr'):same(Path(e[key]['path']),e[key])
assert (f/'stdout').read_bytes()==b''
assert "assert pin(path)['sha256']==args.canonical_review_sha" in (f/'stderr').read_text()
assert not (D/'BOUND_CANONICAL.json').exists() and not (D/'runs/primary_separate_streams').exists()
pre=read(D/'PREPARED.json')
for name,row in pre['canonical_files'].items():same(W/name,row)
original=D/'ACTUAL_ROOT_CANONICAL_REVIEW.json';review=read(original)
same(W/'scripts/bus_resource_bounds_2026_10_16.py',review['prebinding_primary'])
assert review['root_read_complete'] is True
captured={p.name:dict(original=pin(p),utf8=p.read_text()) for p in sorted(f.iterdir()) if p.is_file()}
target=D/'failed_actions/cache_01_wrong_argument';assert not target.exists();target.parent.mkdir(parents=True,exist_ok=True)
f.rename(target)
for name,row in captured.items():same(target/name,row['original'])
review.update(utc=datetime.now(timezone.utc).isoformat(),previous_canonical_review=pin(original),
 previous_cache_failure=dict(reason='Root mistakenly supplied literal REPLACE as the canonical-review hash. The exact-hash guard refused before binding or child execution; all prepared source identities remained unchanged.',
 actual_failed_files=captured,preserved_directory=str(target),recovery='Original failed action directory moved intact to failed_actions/cache_01_wrong_argument; no receipt or source overwritten. Retry will use the actual newly recorded contract hash with unchanged frozen integration code.'),
 actual_next_step='Bind this separately recorded unchanged-source recovery review using its actual contract hash, then run guarded cache and remaining phases. Seven successful phases alone are not the complete execution history.')
out=D/'ACTUAL_ROOT_CANONICAL_RECOVERY_REVIEW.json';assert not out.exists();out.write_text(json.dumps(review,indent=2)+'\n')
print(json.dumps({'review':pin(out)},indent=2))
