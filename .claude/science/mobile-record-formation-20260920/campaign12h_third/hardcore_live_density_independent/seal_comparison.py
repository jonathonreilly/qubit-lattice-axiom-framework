"""Authenticate and seal only this bounded post-source comparison packet."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json

HERE = Path(__file__).resolve().parent
BASE = HERE.parent


def row(path):
    path = Path(path).resolve()
    data = path.read_bytes()
    return {'path': str(path), 'bytes': len(data), 'sha256': sha256(data).hexdigest()}


def main():
    prepath = HERE/'PRE_COMPARISON_SEAL.json'
    assert row(prepath)['sha256'] == 'caf8a8632b62fa99bcd9fad95f33aa27be44ed0ecd1b511e09827a825b04a703'
    pre = json.loads(prepath.read_text())
    old = pre['sources'] + pre['artifacts']
    for item in old:
        assert row(item['path']) == item
    seals = {
        'HARDCORE_RECORD_RING_AUTHOR_SEAL.json': 'f48d6ee6d9e013bcc12019164ede7f8593feb93e62cd6076e753573b2126ef26',
        'RECORD_DENSITY_AUTHOR_SEAL.json': '7b57069bb8dce7d13eee4c9301f58f15ac62eaed63fe445b1aee63396aad38bb',
        'HOMOGENEOUS_FIELD_STAR_AUTHOR_SEAL.json': '67624b8eafbc339d4c581165ef01ef366035752bfef1e8404faf34edcf6aceaf',
    }
    sources = []
    for name, digest in seals.items():
        path = BASE/name
        assert row(path)['sha256'] == digest
        contents = json.loads(path.read_text())['artifacts']
        for item in contents:
            assert row(item['path']) == item
        sources.extend(contents)
        sources.append(row(path))
    geometry = row(BASE/'local_gauge_record_cooling_check.py')
    assert geometry['sha256'] == '9faf0f87d0574368feb0f656308308c269d3df922bfff7576a8d6d10182b5552'
    sources.append(geometry)
    assert len({x['path'] for x in sources}) == len(sources)
    result = json.loads((HERE/'COMPARISON_RESULTS.json').read_text())
    receipt = json.loads((HERE/'COMPARISON_CHECK_RECEIPT.json').read_text())
    assert receipt['returncode'] == 0
    assert receipt['script_sha256'] == row(HERE/'comparison_check.py')['sha256']
    assert result['script'] == row(HERE/'comparison_check.py')
    assert (HERE/'COMPARISON_CHECK.stdout').read_bytes() == (HERE/'COMPARISON_RESULTS.json').read_bytes()
    assert (HERE/'COMPARISON_CHECK.stderr').read_bytes() == b''
    for key, file in [('stdout_sha256', 'COMPARISON_CHECK.stdout'), ('stderr_sha256', 'COMPARISON_CHECK.stderr')]:
        assert receipt[key] == row(HERE/file)['sha256']
    boundary = {
        'created_utc': datetime.now(timezone.utc).isoformat(),
        'pre_comparison_seal': row(prepath),
        'post_seal_authorization': 'Parent expressly authorized these three frozen seven-artifact packets after receiving PRE.',
        'read_scope': 'Complete three notes, runners, result JSONs, contexts and receipts. Full logs authenticated byte-identical to read JSONs; stderr empty. Earlier truncated note read repaired by targeted section read.',
        'executed': 'Only independent comparison_check.py; imports only identity-matched own PRE finite_sector_check.py.',
        'not_executed': 'No author runner or original numerical sweep rerun.',
        'reused_dependency': geometry,
        'external_source_limit': 'Contextual literature reading and virtual-multiple-occupancy source not freshly verified and not imported into the proof.',
        'unopened': ['newer one-dimensional transport', 'ramp', 'uniform-local normal form', 'campaign checkpoint', 'campaign registry'],
        'unchanged': 'All prior PRE artifacts and primary author files.',
        'disposition': 'No material mathematical error or necessary scope correction identified in bounded comparison.',
    }
    (HERE/'COMPARISON_READ_BOUNDARY.json').write_text(json.dumps(boundary, indent=2)+'\n')
    names = ['COMPARISON.md', 'comparison_check.py', 'COMPARISON_RESULTS.json',
             'COMPARISON_CHECK.stdout', 'COMPARISON_CHECK.stderr', 'COMPARISON_CHECK_RECEIPT.json',
             'COMPARISON_READ_BOUNDARY.json', 'seal_comparison.py']
    artifacts = [row(HERE/name) for name in names]
    old = old + [row(prepath)]
    final = {'created_utc': datetime.now(timezone.utc).isoformat(),
             'status': 'Bounded post-source scientific comparison complete. No formal audit/publication determination.',
             'reviewed_author_packet_and_reused_dependency': sources,
             'preserved_pre_comparison': old, 'comparison_artifacts': artifacts,
             'counts': {'author_and_dependency': len(sources), 'preserved_pre': len(old),
                        'comparison': len(artifacts), 'total': len(sources)+len(old)+len(artifacts)},
             'findings': [], 'requested_corrections': [],
             'limits': ['No volume-uniform field-dynamics theorem or photon/phase claim.',
                        'Different valid upper-bound constants are not errors.',
                        'Numerical matrix exponentials evaluate finite generators; no exact-roundoff claim.',
                        'Author source-context historical reading claims not independently reenacted.',
                        'Earlier failed attempts remain sealed. No failed execution in this comparison.']}
    (HERE/'FINAL_SEAL.json').write_text(json.dumps(final, indent=2)+'\n')
    for item in sources+old+artifacts:
        assert row(item['path']) == item
    print(json.dumps({'report': row(HERE/'COMPARISON.md'), 'final_seal': row(HERE/'FINAL_SEAL.json'),
                      'counts': final['counts'], 'all_bindings_verify': True}, indent=2))


if __name__ == '__main__':
    main()
