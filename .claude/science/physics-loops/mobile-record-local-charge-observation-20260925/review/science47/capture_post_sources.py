"""Snapshot only the released author47 generation and its seven explicit source pins."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json

HERE = Path(__file__).resolve().parent
AUTHOR = HERE.parent / 'native-charge-finite-time-personal'


def ident(path):
    s = path.stat()
    return {'sha256': sha256(path.read_bytes()).hexdigest(), 'bytes': s.st_size,
            'mode': s.st_mode, 'dev': s.st_dev, 'ino': s.st_ino,
            'mtime_ns': s.st_mtime_ns, 'ctime_ns': s.st_ctime_ns, 'nlink': s.st_nlink}


def main():
    assert not (HERE / 'POST_SOURCE_PINS.json').exists()
    pre = json.loads((HERE / 'PRE_SEAL.json').read_text())
    originals = []
    for row in pre['members']:
        path = HERE / row['path']
        now = ident(path)
        assert now['sha256'] == row['sha256'] and now['bytes'] == row['bytes']
        originals.append({'path': str(path), **now})
    for name in ('PRE_SEAL.json', 'PRE_SEAL_RECEIPT.json'):
        originals.append({'path': str(HERE / name), **ident(HERE / name)})
    assert len(originals) == 41
    seal = json.loads((AUTHOR / 'AUTHOR_SEAL.json').read_text())
    assert ident(AUTHOR / 'AUTHOR_SEAL.json')['sha256'] == '1f2cb7ce4c8e8b5491a2e35aae215f7e0533d6119343074173ef13dc877d8ba8'
    assert len(seal['members']) == 17
    records = []

    def capture(path, rel, expected, role):
        before = ident(path)
        assert before['sha256'] == expected, str(path)
        target = HERE / 'post_sources' / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open('xb') as stream:
            stream.write(path.read_bytes())
        assert ident(path) == before
        records.append({'origin': str(path), 'snapshot': str(target.relative_to(HERE)),
                        'role': role, **before})

    capture(AUTHOR / 'AUTHOR_SEAL.json', Path('author47/AUTHOR_SEAL.json'),
            '1f2cb7ce4c8e8b5491a2e35aae215f7e0533d6119343074173ef13dc877d8ba8', 'Released author47 seal')
    for row in seal['members']:
        path = AUTHOR / row['path']
        assert path.stat().st_size == row['bytes']
        capture(path, Path('author47') / row['path'], row['sha256'], 'Released author47 member; inspected, never executed')
    for i, row in enumerate(json.loads((AUTHOR / 'SOURCE_PINS.json').read_text())['sources']):
        path = Path(row['path'])
        allowed = path.name in (
            'LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md',
            'LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md',
            'FORMATION_BALANCE_AND_UNSATURATED_DARK_STATES_BOUNDED_THEOREM_NOTE_2026-09-24.md',
            'CHARGE_CURRENT_AND_INITIAL_COVARIANCE_ROOT.md', 'AUTHOR_SEAL.json', 'AGENTS.md', 'SCIENCE_WORKFLOW.md')
        assert allowed
        role = 'Explicit source46 note/seal only; no other46 member followed' if path.parent.name == 'native-charge-current-noise-personal' else 'Unchanged common-model parent or procedure identity'
        capture(path, Path('bound_sources') / (str(i) + '_' + path.name), row['sha256'], role)
    with (HERE / 'POST_PRE_PRESERVATION_BEFORE.json').open('x') as stream:
        json.dump({'files': originals, 'stat_scope': 'Bytes and stable file stats; access time excluded.'}, stream, indent=2); stream.write('\n')
    result = {'at_utc': datetime.now(timezone.utc).isoformat(), 'sources': records,
              'author47_seal_sha256': ident(AUTHOR / 'AUTHOR_SEAL.json')['sha256'],
              'author47_members': 17, 'preserved_PRE_files': len(originals),
              'PRE_seal_sha256': ident(HERE / 'PRE_SEAL.json')['sha256'],
              'exposure': 'Complete released47 proof/code/history plus complete bound46 note and46 seal; no46 controls or other members opened.',
              'forbidden_sources_read': [], 'author_programs_executed_or_imported': []}
    with (HERE / 'POST_SOURCE_PINS.json').open('x') as stream:
        json.dump(result, stream, indent=2); stream.write('\n')
    print(json.dumps({'source_records': len(records), 'author47_members': 17,
                      'preserved_PRE_files': len(originals), 'pins_sha256': ident(HERE / 'POST_SOURCE_PINS.json')['sha256'],
                      'all_expected_source_bytes_verified': True}, indent=2))


if __name__ == '__main__':
    main()
