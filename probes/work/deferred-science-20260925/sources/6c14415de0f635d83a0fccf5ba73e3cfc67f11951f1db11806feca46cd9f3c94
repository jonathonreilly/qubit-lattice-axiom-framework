from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, subprocess

ROOT=Path(__file__).resolve().parent
AUTHOR=ROOT.parent/'prepared-matter-probe-personal'
REPO=ROOT.parent/'campaign-working'
MAIN='0e6ad8285096ed668816f18caaa6fbbfbd9c50e8'
OUT=ROOT/'post_sources'
def sha(data): return hashlib.sha256(data).hexdigest()
def keep(name,data,**metadata):
    target=OUT/name
    target.parent.mkdir(parents=True,exist_ok=True)
    if target.exists(): assert target.read_bytes()==data
    else: target.write_bytes(data)
    row=dict(frozen_path=str(target.relative_to(ROOT)),bytes=len(data),sha256=sha(data),**metadata)
    pins.append(row);print(json.dumps(row,sort_keys=True))

preseal=ROOT/'PRE_SEAL.json'
assert sha(preseal.read_bytes())=='5c72901c7a027ba7f00685ce39abe206a2ae0b8a73098ab35e7f0b72324f177c'
pre=json.loads(preseal.read_text())
for member in pre['members']:
    data=(ROOT/member['path']).read_bytes()
    assert len(data)==member['bytes'] and sha(data)==member['sha256']

pins=[]
sealdata=(AUTHOR/'AUTHOR_SEAL.json').read_bytes()
assert sha(sealdata)=='99a14ba42c0936a52cf4037428168eadc8021651dddc5b718332b4bf8b97fe33'
authorseal=json.loads(sealdata)
assert len(authorseal['files'])==7
keep('author/AUTHOR_SEAL.json',sealdata,path=str(AUTHOR/'AUTHOR_SEAL.json'),role='released author seal')
for name,member in authorseal['files'].items():
    data=(AUTHOR/name).read_bytes()
    assert len(data)==member['bytes'] and sha(data)==member['sha256']
    keep('author/'+name,data,path=str(AUTHOR/name),role='released author evidence; not independent execution')
assert sha((AUTHOR/'PREPARED_MATTER_INTERFERENCE_PROBE_ROOT.md').read_bytes())=='ab3c1883b032e571efdeb52330d7665c262f70e3f303b3236f32f89accbcd7bf'

git_sources=[
 ('bounded_target.md',MAIN,'docs/BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET_BOUNDED_THEOREM_NOTE_2026-09-24.md',
  'f6cbeb6e0ddaa7d5a7ede3d3f3c2b7f5b22d58adeba8ef84f8aabc10599fb0f9','conditional main register premise'),
 ('public_original_readout.md','04dcf088de81990632d869142f30a59e881a8f31',
  'docs/ORIGINAL_FORMATION_RECORD_PHOTON_READOUT_AND_MICROSCOPIC_FINITE_BINS_BOUNDED_THEOREM_NOTE_2026-09-24.md',None,
  'explicitly released public parent; section C used for register reasoning'),
 ('procedure/physics-claim-reviewer.md',MAIN,'docs/ai_methodology/skills/physics-claim-reviewer/SKILL.md',None,'procedural'),
 ('procedure/skill-freshness.md',MAIN,'docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md',None,'procedural'),
 ('procedure/proof-search-governance.md',MAIN,'docs/ai_methodology/skills/physics-loop/references/proof-search-governance.md',None,'procedural'),
]
for name,commit,path,expected,role in git_sources:
    data=subprocess.check_output(['git','show',commit+':'+path],cwd=REPO)
    if expected: assert sha(data)==expected
    keep(name,data,repository=str(REPO),commit=commit,path=path,role=role)
installed=Path('/Users/jonreilly/.codex/skills/physics-claim-reviewer/SKILL.md')
assert installed.read_bytes()==(OUT/'procedure/physics-claim-reviewer.md').read_bytes()

# Existing PRE copies remain the source for the unchanged four main parents.
reused=[]
for source in json.loads((ROOT/'SOURCE_PINS.json').read_text())['sources']:
    if source['frozen_path'] in ['sources/local_compensation.md','sources/local_pair_form.md',
                                 'sources/electric_magnetic.md','sources/weak_field_packets.md']:
        path=ROOT/source['frozen_path']
        assert sha(path.read_bytes())==source['sha256']
        reused.append(source)

result=dict(phase='released-source POST',created_utc=datetime.now(timezone.utc).isoformat(),
            sources=pins,reused_unchanged_PRE_sources=reused,
            preserved_PRE_seal_sha256=sha(preseal.read_bytes()),preserved_PRE_members=len(pre['members']),
            author_seal_member_count=7,installed_reviewer_matches_pinned_source=True,
            author_SOURCE_PINS_private_entries_followed=False,
            no_author_code_executed=True,no_other_active_checker_packets_read=True)
(ROOT/'POST_SOURCE_PINS.json').write_text(json.dumps(result,indent=2)+'\n')
print('TOTAL frozen',len(pins),'new input records; four unchanged PRE science inputs reused;',len(pre['members']),'PRE members unchanged')
