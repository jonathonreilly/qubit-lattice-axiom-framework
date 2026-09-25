from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent / 'campaign-working'
REV = '60c5f194d940a7bbaf1cdd545296e31d74a02f1a'
PARENTS = {
    'LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS': '7c5bc10d0ca1127c2a1ef6f5cf9269caf6e8f023a09a061c2da0d8e033e35a7a',
    'LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT': 'c63db3296e5705c57693c2deb109e506f336fae4848d3ab0926d13a98929802b',
    'FORMATION_BALANCE_AND_UNSATURATED_DARK_STATES': '2ae8d264eaff3ab47ecf4ec41fa21178ff444546bcc2e36d885d092732e30516',
}


def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args])


def observation(path):
    s = path.stat()
    return {'sha256': sha256(path.read_bytes()).hexdigest(), 'bytes': s.st_size,
            'mode': s.st_mode, 'dev': s.st_dev, 'ino': s.st_ino,
            'mtime_ns': s.st_mtime_ns, 'ctime_ns': s.st_ctime_ns, 'nlink': s.st_nlink}


def main():
    (HERE / 'sources').mkdir()
    rows = []
    for stem, expected in PARENTS.items():
        rel = 'docs/' + stem + '_BOUNDED_THEOREM_NOTE_2026-09-24.md'
        path = ROOT / rel
        raw = path.read_bytes()
        pinned = git('show', REV + ':' + rel)
        assert raw == pinned and sha256(raw).hexdigest() == expected
        target = HERE / 'sources' / path.name
        target.write_bytes(raw)
        rows.append({'origin': str(path), 'snapshot': str(target.relative_to(HERE)),
                     'role': 'Only authorized scientific parent', 'git_revision': REV,
                     'git_path': rel, **observation(path)})
    procedural = ['AGENTS.md', 'docs/ai_methodology/SCIENCE_WORKFLOW.md',
                  'docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md']
    for rel in procedural:
        path = ROOT / rel
        target = HERE / 'sources' / ('procedure_' + path.name)
        raw = path.read_bytes()
        target.write_bytes(raw)
        rows.append({'origin': str(path), 'snapshot': str(target.relative_to(HERE)),
                     'role': 'Procedure only; no scientific premise', **observation(path)})
    for ref, rel, dest in [
        ('origin/ai/execution', 'AGENTS.md', 'ai_execution_AGENTS.md'),
        ('origin/main', 'docs/ai_methodology/skills/physics-claim-reviewer/SKILL.md', 'physics_claim_reviewer_SKILL.md'),
        ('origin/main', 'docs/ai_methodology/skills/physics-loop/references/proof-search-governance.md', 'proof_search_governance.md'),
    ]:
        raw = git('show', ref + ':' + rel)
        (HERE / 'sources' / dest).write_bytes(raw)
        rows.append({'git_repository': str(ROOT), 'git_revision': git('rev-parse', ref).decode().strip(),
                     'git_path': rel, 'snapshot': 'sources/' + dest,
                     'sha256': sha256(raw).hexdigest(), 'bytes': len(raw),
                     'role': 'Procedure only; read existing refs, no fetch or mutation'})
    result = {'at_utc': datetime.now(timezone.utc).isoformat(), 'sources': rows,
              'scientific_revision': REV, 'observed_origin_main': git('rev-parse', 'origin/main').decode().strip(),
              'prior_exposure': 'Earlier42/43 PRE/POST and final publication comparison are disclosed historical exposure; no prior scientific code reused.',
              'forbidden_packets_read': [], 'scientific_programs_imported': []}
    (HERE / 'SOURCE_PINS.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
