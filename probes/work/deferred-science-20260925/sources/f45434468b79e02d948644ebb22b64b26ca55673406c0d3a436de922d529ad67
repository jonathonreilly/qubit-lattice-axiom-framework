#!/usr/bin/env python3
"""Freeze the released author packet and verify the unchanged sealed PRE."""
from datetime import datetime,timezone
from pathlib import Path
import hashlib,json,subprocess
HERE=Path(__file__).resolve().parent;BASE=HERE.parent
AUTHOR=BASE/'native-one-pair-spectrum-personal'
REV='60c5f194d940a7bbaf1cdd545296e31d74a02f1a'
sha=lambda raw:hashlib.sha256(raw).hexdigest()
pre_path=HERE/'PRE_SEAL.json';pre=json.loads(pre_path.read_text())
assert sha(pre_path.read_bytes())=='bed28ea9c81afb7822d0ddeeb552260e3e0547b6f387c9edb8dbd6aec83ee25b'
for row in pre['members']:
    raw=(HERE/row['path']).read_bytes()
    assert sha(raw)==row['sha256'] and len(raw)==row['bytes']
sealraw=(AUTHOR/'AUTHOR_SEAL.json').read_bytes()
assert sha(sealraw)=='69a754ada477506f4437705dbb49e8ebe93b3c230185b7376b3b8d6bfb18dc6d'
author=json.loads(sealraw);rows=[]
dest=HERE/'post_sources/author';dest.mkdir(parents=True,exist_ok=True)
for name,expected in author['files'].items():
    raw=(AUTHOR/name).read_bytes()
    assert sha(raw)==expected['sha256'] and len(raw)==expected['bytes']
    target=dest/name
    with target.open('xb') as out:out.write(raw)
    rows.append(dict(origin=str(AUTHOR/name),frozen_path=str(target.relative_to(HERE)),**expected,
                     role='Released author source/evidence; not an independent control'))
with (dest/'AUTHOR_SEAL.json').open('xb') as out:out.write(sealraw)
rows.append(dict(origin=str(AUTHOR/'AUTHOR_SEAL.json'),frozen_path='post_sources/author/AUTHOR_SEAL.json',
                 bytes=len(sealraw),sha256=sha(sealraw),role='Released author seal'))
assert author['files']['NATIVE_ONE_PAIR_SPECTRAL_EDGE_ROOT.md']['sha256']=='e177784652f4c6fafb344ddc72ac20144ebabb9b063e009a1a8618529f8ef922'
process=BASE/'THIRTY_THIRD_PRE_ROOT_VERIFICATION.json';raw=process.read_bytes()
assert sha(raw)=='fe54a392a2dc48669da07e302ab561d3e9d8d91e8be5515f23ad36ff684ca234'
with (HERE/'post_sources/ROOT_PRE_VERIFICATION.json').open('xb') as out:out.write(raw)
rows.append(dict(origin=str(process),frozen_path='post_sources/ROOT_PRE_VERIFICATION.json',
                 bytes=len(raw),sha256=sha(raw),role='Root process evidence; not independent authority'))
procedure=HERE/'post_sources/procedure';procedure.mkdir(exist_ok=True)
repo=BASE/'campaign-working'
names=['docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md',
       'docs/ai_methodology/skills/physics-claim-reviewer/SKILL.md',
       'docs/ai_methodology/skills/physics-loop/references/proof-search-governance.md',
       'docs/ai_methodology/skills/review-loop/SKILL.md']
for index,name in enumerate(names):
    p=subprocess.run(['git','show',REV+':'+name],cwd=repo,capture_output=True,check=True)
    assert not p.stderr
    target=procedure/(str(index)+'_'+Path(name).name)
    with target.open('xb') as out:out.write(p.stdout)
    rows.append(dict(origin=str(repo/name),revision=REV,git_path=name,
        frozen_path=str(target.relative_to(HERE)),bytes=len(p.stdout),sha256=sha(p.stdout),
        live_matches_exact_revision=(repo/name).read_bytes()==p.stdout,role='Procedure only'))
installed=Path('/Users/jonreilly/.codex/skills/physics-claim-reviewer/SKILL.md')
assert installed.read_bytes()==(procedure/'1_SKILL.md').read_bytes()
for source in json.loads((HERE/'SOURCE_PINS.json').read_text())['sources']:
    assert sha(Path(source['origin']).read_bytes())==source['sha256']
data=dict(created_utc=datetime.now(timezone.utc).isoformat(),phase='Released-source POST',
    author_member_count=len(author['files']),sources=rows,
    PRE_seal_sha256=sha(pre_path.read_bytes()),all_PRE_members_reverified=len(pre['members']),
    scientific_parents_unchanged=True,author_programs_executed_or_imported=False,
    restricted_other_packets_read=False,
    procedure_scope='Physics claim/proof and artifact comparison only. Owner unchanged model/effort, no delegation, no audit/publication mutation override broader workflow defaults.')
with (HERE/'POST_SOURCE_PINS.json').open('x') as out:json.dump(data,out,indent=2);out.write('\n')
print(json.dumps(data,indent=2))
