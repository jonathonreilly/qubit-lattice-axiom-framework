"""New recovery capture. Reads originals; writes only this new evidence directory."""
from pathlib import Path
import datetime, hashlib, json, shutil, stat, subprocess

HERE = Path(__file__).resolve().parent
OUTER = HERE.parent
WORK = OUTER / 'local-charge-observation-publication'
FROZEN = OUTER / 'LOCAL_CHARGE_OBSERVATION_FROZEN_SOURCES.json'
BASE = '60c5f194d940a7bbaf1cdd545296e31d74a02f1a'

def digest(raw): return hashlib.sha256(raw).hexdigest()
def signature(p):
    s = p.stat()
    return dict(sha256=digest(p.read_bytes()), bytes=s.st_size, mode=stat.S_IMODE(s.st_mode),
                mtime_ns=s.st_mtime_ns, ctime_ns=s.st_ctime_ns, inode=s.st_ino)
def git(*args):
    p = subprocess.run(['git', '-C', str(WORK), *args], capture_output=True, check=True)
    return p.stdout
def write_json(name, obj):
    p = HERE / name
    with p.open('x') as f: json.dump(obj, f, indent=2, sort_keys=True); f.write('\n')

freeze = json.loads(FROZEN.read_text())
selected = {FROZEN}
selected.update(WORK / p for p in freeze['files_sha256'])
extra_work = ['AGENTS.md', 'docs/ai_methodology/SCIENCE_WORKFLOW.md',
              'docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md',
              'docs/ai_methodology/skills/physics-claim-reviewer/SKILL.md',
              'docs/ai_methodology/skills/review-loop/SKILL.md',
              'docs/ai_methodology/skills/physics-loop/references/proof-search-governance.md',
              'scripts/runner_cache.py', 'docs/audit/scripts/write_citation_graph_manifest.py']
selected.update(WORK / p for p in extra_work)
old_dirs = ['native-charge-current-noise-personal','native-charge-current-noise-independent',
            'native-charge-current-noise-qualified','native-charge-finite-time-personal',
            'native-charge-finite-time-independent','local-charge-observation-publication-history']
for name in old_dirs:
    selected.update(p for p in (OUTER / name).rglob('*') if p.is_file())
for p in OUTER.iterdir():
    if p.is_file() and (p.name.startswith(('LOCAL_CHARGE_OBSERVATION','FORTY_SIXTH','FORTY_SEVENTH'))
                       or p.name in ['build_local_charge_observation_publication.py',
                                     'verify_local_charge_observation_publication.py',
                                     'qualify_forty_sixth_current_wording.py']):
        selected.add(p)

rows = []
for p in sorted(selected):
    if p.is_symlink(): raise RuntimeError('Unexpected symlink: ' + str(p))
    before = signature(p)
    rel = p.relative_to(OUTER)
    target = HERE / 'sources' / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open('xb') as f: f.write(p.read_bytes())
    after = signature(p)
    assert before == after and digest(target.read_bytes()) == before['sha256'], str(p)
    rows.append(dict(original=str(p), snapshot=str(target.relative_to(HERE)), **before))

checks = {p: signature(WORK/p)['sha256'] == h for p,h in freeze['files_sha256'].items()}
assert all(checks.values())
identity = dict(captured_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                requested_base=BASE, head=git('rev-parse','HEAD').decode().strip(),
                branch=git('branch','--show-current').decode().strip(),
                origin_main=git('rev-parse','origin/main').decode().strip(),
                instruction_ref=git('rev-parse','origin/ai/execution').decode().strip(),
                status=git('status','--porcelain=v1','--untracked-files=all').decode(),
                frozen_manifest_sha256=digest(FROZEN.read_bytes()),
                frozen_file_checks=checks,
                network_refresh_performed=False,
                scope='New released-source recovery review; no original-reviewer final approval or new blinded derivation.')
assert identity['head'] == BASE and identity['branch'] == freeze['branch']
write_json('SOURCE_PINS.json', dict(captured_utc=identity['captured_utc'], members=rows))
write_json('GIT_IDENTITY.json', identity)
(HERE/'BASE_GRAPH.json').write_bytes(git('show', BASE+':docs/audit/data/citation_graph_manifest.json'))
(HERE/'PUBLICATION_TRACKED.diff').write_bytes(git('diff',BASE,'--','docs/audit/data/citation_graph_manifest.json'))
(HERE/'AI_EXECUTION_AGENTS.md').write_bytes(git('show','origin/ai/execution:AGENTS.md'))
parents = {}
for rel in freeze['parent_paths']:
    base_bytes = git('show', BASE+':'+rel)
    parents[rel] = dict(base_sha256=digest(base_bytes), current_sha256=digest((WORK/rel).read_bytes()),
                        unchanged=base_bytes == (WORK/rel).read_bytes())
assert all(v['unchanged'] for v in parents.values())
write_json('PARENT_BASE_IDENTITY.json', parents)
print(json.dumps(dict(captured_files=len(rows), bytes=sum(r['bytes'] for r in rows),
                      frozen_files=len(checks), frozen_match=all(checks.values()),
                      unchanged_parents=len(parents), branch=identity['branch'], head=identity['head'])))
