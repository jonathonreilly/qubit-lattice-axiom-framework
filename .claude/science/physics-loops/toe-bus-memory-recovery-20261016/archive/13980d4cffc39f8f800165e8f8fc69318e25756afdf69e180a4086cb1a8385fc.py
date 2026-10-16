"""Seal this review after metadata-only source and receipt verification."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

O = Path(__file__).resolve().parent
def digest(data):
    return hashlib.sha256(data).hexdigest()
def identify(path):
    data = path.read_bytes()
    return dict(bytes=len(data), sha256=digest(data))
def require(path, row):
    actual = identify(path)
    if actual != {k: row[k] for k in ('bytes', 'sha256')}:
        raise ValueError(f'Identity mismatch: {path}')

if (O/'FREEZE.json').exists():
    raise RuntimeError('Refusing to alter an existing freeze')
sources = json.loads((O/'SOURCE_IDENTITIES.json').read_text())
for row in sources['sources']:
    require(Path(row['source']), row)
    if 'capture' in row:
        require(O/row['capture'], row)
author_root = Path(next(r['source'] for r in sources['sources'] if r['key']=='author_freeze')).parent
for row in sources['author_freeze_members_verified']:
    require(author_root/row['path'], row)
receipt = json.loads((O/'metadata_capture/EXECUTION.json').read_text())
if receipt['exit_code'] != 0 or receipt['scientific_execution'] is not False or receipt['source_unchanged_after_run'] is not True:
    raise ValueError('Metadata receipt scope/result mismatch')
data = (O/receipt['source_at_launch']).read_bytes()
if len(data) != receipt['source_bytes'] or digest(data) != receipt['source_sha256'] or data != (O/'capture_sources.py').read_bytes():
    raise ValueError('Metadata source-at-launch mismatch')
if digest((O/'run_metadata_capture.py').read_bytes()) != receipt['launcher_sha256']:
    raise ValueError('Metadata launcher mismatch')
for stream in ('stdout', 'stderr'):
    require(O/receipt[stream]['path'], receipt[stream])
members = [dict(path=str(p.relative_to(O)), **identify(p)) for p in sorted(O.rglob('*')) if p.is_file()]
record = dict(schema='bounded-source-exposed-review-freeze-v1', frozen_utc=datetime.now(timezone.utc).isoformat(),
    directory=str(O), disposition='Scoped analytical check survives with explicit inherited and new physical/endpoint qualifications; root acceptance pending.',
    exposure='Same-model source-exposed review; prior root sketch known; no new root review files read.',
    scientific_executions=0, metadata_execution='metadata_capture/EXECUTION.json',
    source_identity_count=len(sources['sources']), captured_source_count=sum('capture' in x for x in sources['sources']),
    author_freeze_member_count=len(sources['author_freeze_members_verified']), member_count=len(members), members=members,
    verification='Every live source and captured source identity, four author freeze members, actual metadata receipt/source/launcher/full streams verified immediately before sealing.',
    mutation_scope='Only this assigned review directory; no prior freeze, author, canonical, Git, publication, audit, cache, graph, lock, prompt or axiom mutations.')
freeze = O/'FREEZE.json'
freeze.write_text(json.dumps(record, indent=2)+'\n')
for row in members:
    require(O/row['path'], row)
print(json.dumps(dict(freeze=str(freeze), **identify(freeze), member_count=len(members), review=identify(O/'REVIEW.md'), scientific_executions=0), indent=2))
