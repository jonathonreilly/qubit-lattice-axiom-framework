#!/usr/bin/env python3
"""Verify exact complete pre-repair payload recovery without copying its unchanged content."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def run():
    spec = json.loads((ROOT / 'INPUTS.json').read_text())
    out = ROOT / 'payload'
    record = json.loads((ROOT / 'history/wrapper_v1/PAYLOAD_RECONSTRUCTION.json').read_text())
    current_map = json.loads((out / spec['packet'] / 'BODY_MAP.json').read_text())
    note = (out / spec['note']).read_bytes()
    cores = {r['id']: note[r['byte_start_0']:r['byte_end_exclusive']]
             for r in current_map['bodies']}
    expected = set()
    for item in record['previous_files']:
        recipe = item['recipe']
        if recipe['kind'] == 'current_payload':
            data = (out / recipe['path']).read_bytes()
        elif recipe['kind'] == 'historical_file':
            data = (ROOT / recipe['path']).read_bytes()
        elif recipe['kind'] == 'old_framing_current_cores':
            data = (ROOT / recipe['header']).read_bytes()
            for core, fragment in zip(recipe['body_ids'], recipe['tail_fragments']):
                data += cores[core] + (out / fragment).read_bytes()
        else:
            raise ValueError('unknown prior payload recipe')
        assert len(data) == item['bytes'] and hashlib.sha256(data).hexdigest() == item['sha256'], item['path']
        assert item['path'] not in expected
        expected.add(item['path'])
    actual = {str(p.relative_to(out)) for p in out.rglob('*') if p.is_file()}
    assert expected == actual
    print(json.dumps({'status': 'complete_prior_payload_reconstructed',
                      'files': len(expected), 'new_raw_proof_copies': 0,
                      'mathematical_predicates': 0, 'science_or_primary_executed': False}, indent=2))


if __name__ == '__main__':
    run()
