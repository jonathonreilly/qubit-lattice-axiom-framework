#!/usr/bin/env python3
"""Read-only source reconstruction and static runner inspection; zero mathematics."""
import argparse
import ast
import gzip
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def digest(data):
    return hashlib.sha256(data).hexdigest()


def check(condition, message):
    if not condition:
        raise AssertionError(message)


def pin(data, row, label):
    check(len(data) == row['bytes'], 'length: ' + label)
    check(digest(data) == row['sha256'], 'hash: ' + label)


def inspect(payload, origins):
    spec = json.loads((ROOT / 'INPUTS.json').read_text())
    packet = spec['packet']
    manifest_path = packet + '/IDENTITY_INPUTS.json'
    manifest_bytes = (payload / manifest_path).read_bytes()
    manifest = json.loads(manifest_bytes)
    helper = (payload / spec['helper']).read_bytes()
    tree = ast.parse(helper)
    constants = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id in {
                    'AUDIT_TIMEOUT_SEC', 'AUDIT_INPUT_PATHS', 'MANIFEST_PATH', 'MANIFEST_SHA256'}:
                    constants[target.id] = ast.literal_eval(node.value)
    check(constants['AUDIT_TIMEOUT_SEC'] == 60, 'declared timeout')
    check(constants['MANIFEST_PATH'] == manifest_path, 'manifest path')
    check(constants['MANIFEST_SHA256'] == digest(manifest_bytes), 'manifest fixed identity')
    inputs = sorted(list(manifest['files']) + [manifest_path])
    check(constants['AUDIT_INPUT_PATHS'] == inputs, 'complete literal input declaration')
    expected_helper = (ROOT / 'templates/identity_runner.py.in').read_text().replace(
        '@AUDIT_INPUT_PATHS@', repr(inputs)).replace('@MANIFEST_PATH@', repr(manifest_path)).replace(
        '@MANIFEST_SHA256@', repr(digest(manifest_bytes))).encode()
    check(helper == expected_helper, 'whole helper reproduction; not executed')
    external = manifest['external_scientific_paths']
    check(external == [spec['parent']['repo_path']], 'sole external mathematical input')
    expected_files = (set(manifest['files']) - set(external)) | {manifest_path, spec['helper']}
    actual_files = {str(p.relative_to(payload)) for p in payload.rglob('*') if p.is_file()}
    check(actual_files == expected_files, 'exact payload footprint')
    content = {}
    for relative in sorted(actual_files):
        p = payload / relative
        check(not p.is_symlink() and p.resolve().is_relative_to(payload), 'regular contained payload file')
        content[relative] = p.read_bytes()
        if relative in manifest['files']:
            pin(content[relative], manifest['files'][relative], relative)

    note = content[spec['note']]
    bodymap = json.loads(content[packet + '/BODY_MAP.json'])
    cores = {}
    for row in bodymap['bodies']:
        b = note[row['byte_start_0']:row['byte_end_exclusive']]
        pin(b, row, row['id'])
        check(note.count(b) == 1, 'unique body')
        check(b.endswith(b'\n') and not b.endswith(b'\n\n'), 'one-LF body EOF')
        check(len(b.splitlines()) == row['source_lines'], 'source line count')
        check(note[:row['byte_start_0']].count(b'\n') + 1 == row['line_start_1'], 'first line')
        check(note[:row['byte_end_exclusive']].count(b'\n') == row['line_end_1'], 'last line')
        cores[row['id']] = b
    fragments = []
    for row in bodymap['fragments']:
        b = content[row['path']]
        pin(b, row, row['path'])
        check(b == (ROOT / 'templates' / Path(row['path']).name).read_bytes(), 'current framing source')
        fragments.append(b)
    check(note == fragments[0] + cores['generic'] + fragments[1] + cores['sharper'] +
          fragments[2] + cores['chain'] + fragments[3], 'full body/framing assembly')
    check(note.count(b'](SIMULTANEOUS_MULTI_PORT_THREE_PAULI_BOUNDED_THEOREM_NOTE_2026-10-14.md)') == 1,
          'one explicit mathematical parent link')
    check(note.count(b'](') == 1, 'actual citation count; no hidden raw-proof links')

    archive = json.loads(content[packet + '/SOURCE_ARCHIVE.json'])
    unpacked = {}
    for key, row in archive['objects'].items():
        compressed = content[row['path']]
        pin(compressed, row['stored'], row['path'])
        b = gzip.decompress(compressed)
        pin(b, row, key)
        check(digest(b) == key, 'object filename/content identity')
        check(all(core not in b for core in cores.values()), 'complete core duplicated in an object')
        unpacked[key] = b
    records = {}
    for row in archive['records']:
        pieces = []
        for item in row['parts']:
            check(item['kind'] in ('object', 'core'), 'known recipe kind')
            pieces.append(unpacked[item['sha256']] if item['kind'] == 'object' else cores[item['id']])
        b = b''.join(pieces)
        pin(b, row, row['alias'])
        check(row['alias'] not in records, 'unique logical alias')
        check(len(b.splitlines()) == row['line_count'], 'logical line count')
        records[row['alias']] = b
        if origins:
            p = Path(row['original'])
            check(p.is_file() and not p.is_symlink(), 'source origin regular file')
            check(p.read_bytes() == b, 'exact live origin: ' + row['original'])
    group_counts = {}
    inner_counts = {}
    for group in archive['groups']:
        prefix = 'assemblies/' + group['id'] + '/'
        frozen = records[prefix + group['seal']]
        check(digest(frozen) == group['seal_sha256'], 'frozen assembly identity')
        old_seal = json.loads(frozen)
        rows = old_seal['members']
        expected = {r['path'] for r in rows} | {group['seal']}
        found = {p[len(prefix):] for p in records if p.startswith(prefix)}
        check(found == expected and len(found) == group['complete_files'], 'whole assembly closure')
        for r in rows:
            pin(records[prefix + r['path']], r, 'frozen ' + r['path'])
        if origins:
            oldroot = Path(group['root'])
            actual = {str(p.relative_to(oldroot)) for p in oldroot.rglob('*') if p.is_file()}
            check(actual == expected, 'live old assembly member set')
        entries = json.loads(records[prefix + 'archive/ALIASES.json'])['aliases']
        for row in entries:
            b = records[prefix + row['file']]
            if row['storage'] == 'embedded_proof_body':
                b = b[row['byte_start_0']:row['byte_end_exclusive']]
            else:
                check(row['storage'] == 'object', 'known legacy inner storage')
            pin(b, row, 'inner ' + row['alias'])
        group_counts[group['id']] = len(found)
        inner_counts[group['id']] = len(entries)
    parent = records['external/mathematical_parent/canonical_note.md']
    pin(parent, spec['parent'], 'canonical parent archive')
    pin(parent, manifest['files'][external[0]], 'external canonical declared input')
    row = bodymap['parent']
    raw = parent[row['byte_start_0']:row['byte_end_exclusive']]
    check(digest(raw) == row['raw_sha256'] and parent.count(raw) == 1, 'canonical raw-be8 extraction')
    check(raw == records['external/mathematical_parent/raw_be8.md'], 'exact raw parent source')
    graph = json.loads(content[packet + '/GRAPH_PROPOSAL.json'])
    check(len(graph['external_edges']) == 1 and graph['external_edges'][0]['to'] == row['claim_id'],
          'proposed external edge identity')
    binding = json.loads(content[packet + '/PUBLICATION_BINDINGS.json'])
    check(binding['integration_authorized'] is False and binding['driver_bound_root_acceptance'] is None,
          'no self-authorized integration')
    if origins:
        check(Path(row['path']).read_bytes() == parent, 'current live canonical body')
    return {'status': 'source_components_verified', 'mathematical_predicates': 0,
            'source_group_counts': group_counts, 'inner_alias_counts': inner_counts,
            'archive_records': len(records), 'unique_objects': len(unpacked),
            'payload_files': len(actual_files), 'declared_primary_inputs': len(inputs),
            'primary_runner_executed': False, 'archived_science_executed': False,
            'live_origins_compared': len(records) if origins else 0,
            'note_sha256': digest(note), 'primary_runner_sha256': digest(helper),
            'whole_primary_source_reproduced_and_ast_parsed': True}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--payload', default=str(ROOT / 'payload'))
    parser.add_argument('--origins', action='store_true', help='also compare every declared original source')
    args = parser.parse_args()
    print(json.dumps(inspect(Path(args.payload).resolve(), args.origins), indent=2, sort_keys=True))
