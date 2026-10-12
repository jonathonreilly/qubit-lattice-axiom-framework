"""Read-only reconstruction of the administrative delivery layer; no science."""
from pathlib import Path
import gzip
import hashlib
import json

P = Path(__file__).resolve().parent
W = P.parents[3]
sha = lambda b: hashlib.sha256(b).hexdigest()


def need(ok, text):
    if not ok:
        raise RuntimeError(text)


def path(relative):
    need(relative and not Path(relative).is_absolute() and '..' not in Path(relative).parts, 'Unsafe packet path')
    p = P / relative
    need(p.is_file() and not p.is_symlink() and p.resolve().is_relative_to(P.resolve()), 'Missing regular packet payload: '+relative)
    return p


def main():
    evidence = json.loads(path('DELIVERY_EVIDENCE_MAP.json').read_text())
    source_map = json.loads(path('DELIVERY_SOURCE_MAP.json').read_text())
    need(evidence['schema'] == 'deduplicated_complete_own_evidence_v2', 'Unknown archive schema')
    originals, hashes, targets = {}, set(), set()
    for row in evidence['objects']:
        need(row['sha256'] not in hashes and row['preserved'] not in targets, 'Duplicate object identity or target')
        hashes.add(row['sha256'])
        targets.add(row['preserved'])
        packed = path(row['preserved']).read_bytes()
        need(sha(packed) == row['compressed_sha256'], 'Compressed evidence identity changed')
        data = gzip.decompress(packed)
        need(sha(data) == row['sha256'] and len(data) == row['bytes'], 'Evidence identity changed')
        need(row['originals'] and len(row['originals']) == len(set(row['originals'])), 'Empty/duplicate aliases')
        need(row['storage'] in {'existing_source_evidence', 'delivery_object'}, 'Unknown storage type')
        prefix = 'evidence/' if row['storage'] == 'existing_source_evidence' else 'delivery_evidence/objects/'
        need(row['preserved'].startswith(prefix), 'Object storage escape')
        for original in row['originals']:
            need(original not in originals, 'Duplicate original alias')
            originals[original] = (row, data)
        need(len(row['packed_originals']) == len(set(row['packed_originals'])), 'Duplicate packed aliases')
        for original in row['packed_originals']:
            need(original not in originals, 'Duplicate packed original alias')
            originals[original] = ({'bytes':len(packed),'sha256':sha(packed)}, packed)
    actual = {str(p.relative_to(P)) for p in (P/'delivery_evidence').rglob('*') if p.is_file()}
    expected = {r['preserved'] for r in evidence['objects'] if r['storage'] == 'delivery_object'}
    need(actual == expected, 'Delivery object membership changed')
    need(source_map['mathematical_changes'] == [], 'Unexpected mathematical change')
    edits = source_map['metadata_edits']
    need(len({e['target'] for e in edits}) == len(edits), 'Duplicate metadata target')
    for edit in edits:
        need(edit['category'] == 'administrative_delivery_metadata' and edit['mathematical_changes'] == [], 'Non-administrative edit')
        if edit['kind'] == 'replace':
            need(edit['before_origin'] in originals, 'Absent original metadata')
            need(originals[edit['before_origin']][0]['sha256'] == edit['before_sha256'], 'Old metadata identity changed')
        else:
            need(edit['kind'] == 'new' and edit['before_origin'] is None and edit['before_sha256'] is None, 'Unmapped metadata creation')
        need(edit['after_template'] in originals, 'Absent complete delivery template')
        row, full_after = originals[edit['after_template']]
        need(row['sha256'] == edit['after_sha256'] and row['bytes'] == edit['after_bytes'], 'Template pin changed')
        need(path(edit['target']).read_bytes() == full_after, 'Metadata differs from full reviewed template')
    for row in source_map['unchanged_source_files']:
        p = W / row['path']
        need(p.is_file() and not p.is_symlink() and p.resolve().is_relative_to(W.resolve()), 'Invalid unchanged source')
        need(sha(p.read_bytes()) == row['sha256'] and p.stat().st_size == row['bytes'], 'Original science/source-map bytes changed')
    old_manifest = source_map['generated_manifest_replacement']
    need(old_manifest['target'] == 'SOURCE_IDENTITIES.json' and old_manifest['category'] == 'administrative_manifest_refresh'
         and old_manifest['mathematical_changes'] == [], 'Unexpected manifest transformation')
    need(old_manifest['before_origin'] in originals and originals[old_manifest['before_origin']][0]['sha256'] == old_manifest['before_sha256'], 'Original manifest is not preserved')
    need(source_map['frozen_helper_origin'] in originals and raw_helper() == originals[source_map['frozen_helper_origin']][1], 'Delivery helper differs from its complete reviewed source')
    need(len(source_map['fixed_evidence_maps']) == 2, 'Expected two unchanged evidence maps')
    for row in source_map['fixed_evidence_maps']:
        data = (W/row['path']).read_bytes()
        need(len(data) == row['bytes'] and sha(data) == row['sha256'], 'A declared evidence-map input changed')
    patch = source_map['old_packet_manifest_patch']
    need(patch['before_origin'] in originals and originals[patch['before_origin']][0]['sha256'] == patch['before_sha256'], 'Old five-note manifest before bytes missing')
    need(patch['after_template'] in originals and originals[patch['after_template']][0]['sha256'] == patch['after_sha256'], 'Old five-note manifest repair specimen missing')
    old_bytes = originals[patch['before_origin']][1]
    new_bytes = originals[patch['after_template']][1]
    need((W/patch['target']).read_bytes() == new_bytes and patch['mathematical_changes'] == [], 'Old manifest differs from exact mapped repair')
    before, after = json.loads(old_bytes), json.loads(new_bytes)
    need({k:v for k,v in before.items() if k!='files'} == {k:v for k,v in after.items() if k!='files'}, 'Old manifest metadata changed')
    changes = {r['path']:r for r in patch['changes']}
    need(len(changes) == 5 and len(before['files']) == len(after['files']), 'Old manifest repair membership changed')
    for old, new in zip(before['files'],after['files'],strict=True):
        need(old['path'] == new['path'], 'Old manifest reordered')
        if old['path'] in changes:
            need(old == changes[old['path']]['before'] and new == changes[old['path']]['after'], 'Wrong cache record replacement')
        else:
            need(old == new, 'Unrelated old manifest record changed')
    manifest = json.loads(path('SOURCE_IDENTITIES.json').read_text())
    need(manifest['schema'] == 'complete_massive_delivery_payload_v1', 'Unexpected payload manifest schema')
    records = manifest['files']
    need(len(records) == len({r['path'] for r in records}), 'Duplicate final payload path')
    packet_prefix = str(P.relative_to(W)) + '/'
    permitted = set(source_map['outside_packet_payload_paths'])
    for row in records:
        relative = row['path']
        need(relative.startswith(packet_prefix) or relative in permitted, 'Out-of-scope manifest member')
        p = W / relative
        need(p.is_file() and not p.is_symlink() and p.resolve().is_relative_to(W.resolve()), 'Invalid final payload')
        data = p.read_bytes()
        need(len(data) == row['bytes'] and sha(data) == row['sha256'], 'Final payload identity changed: '+relative)
    actual_paths = {str(p.relative_to(W)) for p in P.rglob('*') if p.is_file() and p != P/'SOURCE_IDENTITIES.json'} | permitted
    need(actual_paths == {r['path'] for r in records}, 'Final payload membership changed')
    print(json.dumps({'delivery_objects': len(hashes), 'original_aliases': len(originals), 'metadata_edits': len(edits), 'payload_files_except_manifest': len(records), 'mathematical_changes': [], 'science_executed': False}))


def raw_helper():
    return Path(__file__).read_bytes()


if __name__ == '__main__':
    main()
