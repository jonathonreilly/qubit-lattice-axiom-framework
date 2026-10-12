#!/usr/bin/env python3
"""Read-only, complete byte reconstruction. Never imports a scientific helper."""
from pathlib import Path
import gzip
import hashlib
import json

P = Path(__file__).resolve().parent
W = P.parents[3]
sha = lambda data: hashlib.sha256(data).hexdigest()
read = lambda name: json.loads((P / name).read_bytes())


def need(test, message):
    if not test:
        raise RuntimeError(message)


def main():
    originals = {}
    maps = ['EVIDENCE_MAP.json']
    maps += [x for x in ['PREPARATION_EVIDENCE_MAP.json', 'VALIDATION_EVIDENCE_MAP.json'] if (P/x).exists()]
    for name in maps:
        seen = set()
        for row in read(name)['objects']:
            packed = (P/row['preserved']).read_bytes()
            data = gzip.decompress(packed)
            need(sha(packed) == row['compressed_sha256'] and sha(data) == row['sha256'] and len(data) == row['bytes'], 'Archive mismatch: '+name)
            need(row['sha256'] not in seen, 'Duplicate payload record: '+name)
            seen.add(row['sha256'])
            for original in row['originals']:
                need(original not in originals or originals[original] == data, 'Ambiguous original alias')
                originals[original] = data
    mapping = read('PUBLICATION_EDITS.json')
    need(mapping['mathematical_changes'] == [], 'Mathematical edit appeared')
    for row in mapping['outputs']:
        if row.get('kind') == 'whole_source_orchestration':
            data = (P/'RUNNER_TEMPLATE.py').read_bytes()
            need(sha(data) == row['template_sha256'], 'Template changed')
            text = data.decode()
            for before, after in row['literal_substitutions'].items():
                need(text.count(before) == 1, 'Template anchor mismatch')
                text = text.replace(before, after, 1)
        else:
            data = originals[row['source_path']]
            need(sha(data) == row['source_sha256'] and len(data) == row['source_bytes'], 'Frozen note identity mismatch')
            text = data.decode()
            for edit in row['edits']:
                need(text.count(edit['before']) == edit['occurrences'], 'Literal publication anchor mismatch')
                text = text.replace(edit['before'], edit['after'], edit['occurrences'])
            text += row['appended_text']
        actual = (W/row['publication_path']).read_bytes()
        need(text.encode() == actual and sha(actual) == row['publication_sha256'] and len(actual) == row['publication_bytes'], 'Complete publication reconstruction differs: '+row['publication_path'])
        need(row['mathematical_changes'] == [], 'Source map declares mathematical changes')
    for row in mapping['runtime_resources']:
        actual = (P/row['packet_path']).read_bytes()
        need(actual == originals[row['original']] and sha(actual) == row['sha256'] and len(actual) == row['bytes'], 'Whole helper changed')
    print(json.dumps({'status':'complete_byte_reconstruction_verified', 'original_aliases':len(originals), 'publication_outputs':len(mapping['outputs']), 'complete_runtime_resources':len(mapping['runtime_resources']), 'maps':maps, 'mathematical_changes':[]}))


if __name__ == '__main__':
    main()
