#!/usr/bin/env python3
"""Copy seven explicit immediate freezes, without recursively chasing citations.

Metadata only. Existing files are never overwritten; scientific source is not
imported or executed. Historical publication seal is an identity record only.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
N = ROOT.parent

SETS = [
    ('sparse_author', 'local_conserving_sparse_compiler_candidate', '1fd6b69f78b2b9e270e1dc4655ef9c6da9c6d4290a3e2867ebfac42fc23ac0c9'),
    ('sparse_exposed_review', 'local_conserving_sparse_compiler_exposed_check', '54c2e39507456f530ae87534d58ed24412b5de0bfe1669f7ba6600781ae55fe9'),
    ('sparse_root_decision', 'local_conserving_sparse_compiler_root_review', 'd8774291d4919e586499a97faafb0e1579a91f1e2e342b876b9b4557645a750e'),
    ('control_parent_decision', 'local_conserving_control_root_review', 'b67a8bd687aadaf81df66e5cf6bb0c866c8647bebf4ab8eb7b6e29c94a3a899a'),
    ('emitted_fixture', 'local_conserving_sparse_compiler_fixture', '2b62a1ba9241999824241c41f191674c3a66c0829185e5bc6ea76052fcc40582'),
    ('fixture_exposed_review', 'local_conserving_sparse_fixture_exposed_check', '415bcee1e080367afb77363df79b9e41163c349bcdf44e70710b31dd5137350e'),
    ('fixture_root_decision', 'local_conserving_sparse_fixture_root_review', 'cc442a55dcfc4dc45243161562acd0c87bc0b962ddfaab894743af1444768e93'),
]
BODIES = [
    ('sparse_derivation', 'sparse_author/DERIVATION.md', '6b1e1ecd6afcf53dd05411493c18ceb9db258fcc279dc3c24072a516a5a76c3b'),
    ('sparse_analytical_review', 'sparse_exposed_review/REVIEW.md', '2af89ecefd2d682259e967cc96ef1f5965c37500de4d3cc9261cb39d50254a2a'),
    ('sparse_qualifications', 'sparse_root_decision/FINAL_QUALIFICATIONS.md', '83b913c6b47ee8625cc15914759886e642515d02f284dc84a6b92d8e3ed54d3e'),
    ('runtime_qualifications', 'control_parent_decision/FINAL_QUALIFICATIONS.md', '9fb1514db57464c15de3156916922f405e80e3dc56b6d7624d2e9531b011f305'),
    ('fixture_report', 'emitted_fixture/REVIEW.md', 'c9e99e725b3efd8dabbf551c315e983113129de0ed12d5f9028c207f93fe9649'),
    ('fixture_exposed_review', 'fixture_exposed_review/REVIEW.md', 'c1f7a257fbb824d868c3ca25c7ba9fc8d7504f2e532ca83b8851427afdae305d'),
    ('fixture_qualifications', 'fixture_root_decision/FINAL_QUALIFICATIONS.md', 'e2bf8af1a8c90068c33d833604717762cb1207e008ad52b3c330986cd470a4bc'),
]
HISTORY = [
    ('root_local_conserving_sparse_publication_review/REVIEW.md', 'history/original_publication_review/REVIEW.md', 'f334c5b529760b132eb87ebf40aa1cebdd741226a893420cc20a48aced020b0e'),
    ('root_local_conserving_sparse_publication_review/REVIEW.json', 'history/original_publication_review/REVIEW.json', 'a33ef4f684fc567544a36da12d87a69588de29b10fc6815b6f1a26801b6e19fc'),
    ('local_conserving_sparse_publication_draft/FREEZE.json', 'history/original_publication_FREEZE.json', '0903d917f7fffcde78c432acfe7ba11dae9c7bfd917c9f08f09a50293db67b72'),
]

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def write_new(path, raw):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('xb') as f:
        f.write(raw)

def copy_checked(original, packet, expected):
    assert original.is_file() and not original.is_symlink()
    raw = original.read_bytes()
    assert len(raw) == expected['bytes'] and sha(raw) == expected['sha256'], original
    write_new(ROOT / packet, raw)
    assert (ROOT / packet).read_bytes() == raw
    return {'original_path': str(original), 'packet_path': packet,
            'bytes': len(raw), 'sha256': sha(raw)}

def main():
    rows, closures = [], []
    for alias, name, expected in SETS:
        original_root = N / name
        seal_raw = (original_root / 'FREEZE.json').read_bytes()
        assert sha(seal_raw) == expected, name
        seal = json.loads(seal_raw)
        members = seal.get('members', seal.get('files'))
        assert isinstance(members, list)
        local_members = []
        for entry in members:
            path = Path(entry['path'])
            rel = path.relative_to(original_root) if path.is_absolute() else path
            assert not rel.is_absolute() and '..' not in rel.parts
            packet = str(Path('source') / alias / rel)
            rows.append(copy_checked(original_root / rel, packet, entry))
            local_members.append(str(rel))
        assert len(set(local_members)) == len(local_members)
        seal_packet = str(Path('source') / alias / 'FREEZE.json')
        rows.append(copy_checked(original_root / 'FREEZE.json', seal_packet,
                                 {'bytes': len(seal_raw), 'sha256': expected}))
        closures.append({'name': alias, 'original_root': str(original_root),
                         'packet_root': 'source/' + alias,
                         'freeze': {'packet_path': seal_packet, 'bytes': len(seal_raw), 'sha256': expected},
                         'member_count': len(members)})
    history = []
    for original, packet, expected in HISTORY:
        raw = (N / original).read_bytes()
        history.append(copy_checked(N / original, packet, {'bytes': len(raw), 'sha256': expected}))
    by_path = {row['packet_path']: row for row in rows}
    bodies = []
    for name, rel, expected in BODIES:
        row = by_path['source/' + rel]
        assert row['sha256'] == expected
        bodies.append({'body_id': name, **row})
    capture = {'created_utc': datetime.now(timezone.utc).isoformat(),
               'kind': 'bounded_selected_source_closure', 'scientific_executions': 0,
               'closures': closures, 'source_closure': rows, 'history_records': history,
               'source_files': len(rows), 'source_bytes': sum(r['bytes'] for r in rows),
               'history_scope': 'Three identity/review records only. Original publication member closure is NOT copied or recursively chased.'}
    write_new(ROOT / 'SOURCE_CAPTURE.json', (json.dumps(capture, indent=2) + '\n').encode())
    write_new(ROOT / 'BODY_RECOVERY_MAP.json', (json.dumps({'immutable_bodies': bodies}, indent=2) + '\n').encode())
    lines = ['# Complete immutable bodies', '', 'Every link below is a complete byte-identical body, not an excerpt. Later decisions control current scope; historical pending statements remain literal.', '', '| Body | Packet copy | SHA256 |', '|---|---|---|']
    for row in bodies:
        lines.append(f"| {row['body_id']} | [{row['packet_path']}]({row['packet_path']}) | `{row['sha256']}` |")
    lines += ['', 'The JSON map also records every original absolute path and byte count. `SOURCE_MANIFEST.json` maps all selected source and evidence members. `history/original_publication_FREEZE.json` records the old seal only; its prior archive is not copied. No canonical parent has been invented.', '']
    write_new(ROOT / 'BODY_RECOVERY_MAP.md', '\n'.join(lines).encode())
    print(json.dumps({'source_files': capture['source_files'], 'source_bytes': capture['source_bytes'],
                      'immediate_closures': len(closures), 'immutable_bodies': len(bodies),
                      'history_records': len(history), 'scientific_executions': 0}, indent=2))

if __name__ == '__main__':
    main()
