#!/usr/bin/env python3
"""Freeze released POST inputs without executing author code or changing PRE."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import subprocess

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
AUTHOR = BASE / 'ground-formation-incompatibility-personal'
REPO = BASE / 'campaign-working'
REV = '60c5f194d940a7bbaf1cdd545296e31d74a02f1a'
sha = lambda raw: hashlib.sha256(raw).hexdigest()
expected_seal = '24e2131d01c9e47b9d8c684486e726ab753d7cab1962566baee13fbd5fead572'
raw = (AUTHOR / 'AUTHOR_SEAL.json').read_bytes()
assert sha(raw) == expected_seal
author_seal = json.loads(raw)
assert len(author_seal['members']) == 9
dest = HERE / 'post_sources' / 'author'
dest.mkdir(parents=True, exist_ok=False)
rows = []


def copy(origin, frozen, expected=None, role='Released author source/evidence'):
    raw = origin.read_bytes()
    if expected is not None:
        assert sha(raw) == expected
    frozen.parent.mkdir(parents=True, exist_ok=True)
    with frozen.open('xb') as out:
        out.write(raw)
    rows.append(dict(origin=str(origin), frozen_path=str(frozen.relative_to(HERE)),
                     bytes=len(raw), sha256=sha(raw), role=role))


copy(AUTHOR / 'AUTHOR_SEAL.json', dest / 'AUTHOR_SEAL.json', expected_seal)
for member in author_seal['members']:
    path = AUTHOR / member['path']
    assert path.stat().st_size == member['bytes']
    copy(path, dest / member['path'], member['sha256'])
assert sha((dest / 'GROUND_ENERGY_AND_ORIGINAL_FORMATION_ROOT.md').read_bytes()) == 'efd15929c31fb137219efb571b99fd0bc3641410f1ea857339fdde65d9128a81'
author_pins = json.loads((dest / 'SOURCE_PINS.json').read_text())
origin_checks = []
pre_pins = json.loads((HERE / 'SOURCE_PINS.json').read_text())
pre_sources = {row['origin']: row for row in pre_pins['sources']}
for row in author_pins['sources']:
    origin = Path(row['path'])
    raw = origin.read_bytes()
    assert len(raw) == row['bytes'] and sha(raw) == row['sha256']
    if str(origin) in pre_sources:
        prior = pre_sources[str(origin)]
        assert raw == (HERE / prior['frozen_path']).read_bytes()
        frozen = prior['frozen_path']
    else:
        # The sole extra author reference is a named, source-refresh receipt,
        # not a science packet or campaign checkpoint.
        assert origin.name == 'GROUND_FORMATION_MAIN_REFRESH_0331.json'
        frozen_path = HERE / 'post_sources' / origin.name
        copy(origin, frozen_path, row['sha256'], 'Author source-refresh receipt; process evidence only')
        frozen = str(frozen_path.relative_to(HERE))
    origin_checks.append(dict(origin=str(origin), frozen_path=frozen,
                              sha256=row['sha256'], bytes=row['bytes']))

# Read/freeze only the selected methodology at the same explicitly pinned
# revision; no fetch, current checkpoint, scientific scope expansion or model change.
procedure_paths = [
    'docs/ai_methodology/skills/physics-claim-reviewer/SKILL.md',
    'docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md',
    'docs/ai_methodology/skills/review-loop/SKILL.md',
    'docs/ai_methodology/skills/physics-loop/references/proof-search-governance.md']
procedures = []
for name in procedure_paths:
    raw = subprocess.check_output(['git', 'show', REV + ':' + name], cwd=REPO)
    assert raw == (REPO / name).read_bytes()
    if name.endswith('physics-claim-reviewer/SKILL.md'):
        assert raw == Path('/Users/jonreilly/.codex/skills/physics-claim-reviewer/SKILL.md').read_bytes()
    out_path = HERE / 'post_sources' / 'procedures' / name.removeprefix('docs/ai_methodology/skills/')
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open('xb') as out:
        out.write(raw)
    procedures.append(dict(origin='git:' + REV + ':' + name,
                           frozen_path=str(out_path.relative_to(HERE)), bytes=len(raw), sha256=sha(raw)))

pre_raw = (HERE / 'PRE_SEAL.json').read_bytes()
assert sha(pre_raw) == '108fa39b7d3f86f2b9fd825307da6861dd8548bf9295a3415024a72dd19c4f51'
pre_seal = json.loads(pre_raw)
for row in pre_seal['members']:
    raw = (HERE / row['path']).read_bytes()
    assert len(raw) == row['bytes'] and sha(raw) == row['sha256']
result = dict(created_utc=datetime.now(timezone.utc).isoformat(), phase='Released-source POST',
              author_members=len(author_seal['members']), author_sources=rows,
              author_source_origins=origin_checks, procedure_sources=procedures,
              procedures_revision=REV,
              procedural_scope='Scoped mathematical/source review only; no full review-loop, branch action, new scientific source, audit, model change or delegation',
              preserved_PRE_seal_sha256=sha(pre_raw), preserved_PRE_members=len(pre_seal['members']),
              author_program_execution_or_import=False,
              forbidden_packets_read=False)
with (HERE / 'POST_SOURCE_PINS.json').open('x') as out:
    json.dump(result, out, indent=2)
    out.write('\n')
print(json.dumps(result, indent=2))
