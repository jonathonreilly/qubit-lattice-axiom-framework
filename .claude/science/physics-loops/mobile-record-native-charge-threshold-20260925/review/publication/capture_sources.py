"""Copy only released inputs into this new packet; never alter source paths."""
from __future__ import annotations
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

EXT = Path('/Users/jonreilly/Documents/Codex/physics-sync-2026-09-24-fifth')
HERE = Path(__file__).resolve().parent
PUB = EXT / 'native-charge-threshold-publication'
AUTHOR = EXT / 'native-charge-identification-personal'
PRIOR = EXT / 'native-charge-identification-independent'

def digest(body):
    return hashlib.sha256(body).hexdigest()

def stat_record(path):
    s = path.stat()
    return {k: getattr(s, 'st_' + k) for k in ('mode', 'dev', 'ino', 'size', 'mtime_ns', 'ctime_ns')}

def main():
    pending = {}
    def add(path, label, relative, expected=None):
        path = Path(path)
        if path in pending:
            if expected is not None:
                old = pending[path]['expected_sha256']
                assert old is None or old == expected
                pending[path]['expected_sha256'] = expected
            return
        pending[path] = {'role': label, 'snapshot': 'frozen/' + label + '/' + relative,
                         'expected_sha256': expected}
    frozen_path = EXT / 'NATIVE_CHARGE_THRESHOLD_FROZEN_SOURCES.json'
    frozen = json.loads(frozen_path.read_bytes())
    for rel, sha in frozen['files_sha256'].items():
        add(PUB / rel, 'publication', rel, sha)
    for rel in (
        'NATIVE_CHARGE_THRESHOLD_FROZEN_SOURCES.json',
        'NATIVE_CHARGE_THRESHOLD_PUBLICATION_WORKING_SOURCES.json',
        'NATIVE_CHARGE_THRESHOLD_PRIMARY_EXECUTION.json',
        'NATIVE_CHARGE_THRESHOLD_PRIMARY_ROOT_REVIEW.json',
        'build_native_charge_threshold_publication.py',
        'FORTIETH_PRE_ROOT_REVIEW.json', 'FORTIETH_POST_ROOT_REVIEW.json',
    ):
        add(EXT / rel, 'process', rel)
    add(PUB / 'scripts/runner_cache.py', 'tooling', 'runner_cache.py')
    seals = [
        (AUTHOR, 'author', 'AUTHOR_SEAL.json', '08dd5ec99ddeccfb7f70a50e216cd40e3cf8ab954cbda6fca27fbbfcaecad83a'),
        (PRIOR, 'prior_checker', 'PRE_SEAL.json', 'c8287bdc28f8c38368b4130c306c285270037e4b8b4e54614d97c25c14869e07'),
        (PRIOR, 'prior_checker', 'POST_SEAL.json', '1df6721dded12cd248c17448f94f538b18007d547703c567a573e260e17517df'),
    ]
    for base, label, name, sha in seals:
        body = (base / name).read_bytes()
        assert digest(body) == sha, (name, digest(body), sha)
        add(base / name, label, name, sha)
        for member in json.loads(body)['members']:
            rel = member['path']
            assert not Path(rel).is_absolute() and '..' not in Path(rel).parts
            add(base / rel, label, rel, member['sha256'])
    assert not (HERE / 'SOURCE_PINS.json').exists(), 'Do not overwrite any prior capture'
    rows = []
    for origin, item in pending.items():
        before = stat_record(origin)
        body = origin.read_bytes()
        after = stat_record(origin)
        assert before == after, str(origin)
        sha = digest(body)
        assert item['expected_sha256'] is None or item['expected_sha256'] == sha, str(origin)
        destination = HERE / item['snapshot']
        assert destination.is_relative_to(HERE / 'frozen') and not destination.exists()
        destination.parent.mkdir(parents=True, exist_ok=True)
        with destination.open('xb') as stream:
            stream.write(body)
        rows.append(dict(item, origin=str(origin), sha256=sha, bytes=len(body), original_stat=before))
    result = {
        'captured_utc': datetime.now(timezone.utc).isoformat(),
        'scope': 'Released-source publication40 correspondence; newly exposed reviewer; no scientific source executed or imported.',
        'originals_modified': False,
        'stat_scope': 'Mode, device, inode, size, mtime_ns, ctime_ns; access times are not changed explicitly or used as content evidence.',
        'member_count': len(rows), 'members': rows,
    }
    with (HERE / 'SOURCE_PINS.json').open('x') as stream:
        json.dump(result, stream, indent=2); stream.write('\n')
    print(json.dumps({'captured_files': len(rows), 'roles': {r: sum(x['role'] == r for x in rows) for r in sorted({x['role'] for x in rows})}, 'source_pins_sha256': digest((HERE / 'SOURCE_PINS.json').read_bytes())}, indent=2))

if __name__ == '__main__':
    main()
