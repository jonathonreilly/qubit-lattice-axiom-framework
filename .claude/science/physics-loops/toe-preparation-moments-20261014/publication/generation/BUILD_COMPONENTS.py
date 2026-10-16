#!/usr/bin/env python3
"""Build source-only components; never import or execute archived science."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parent
SCHEMA = 'preparation-moment-components-v1'
FRAGMENTS = ['note_header.md', 'between_generic_sharper.md',
             'between_sharper_chain.md', 'note_footer.md']
VERIFY_EXISTING = False
WRITTEN = set()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def info(data):
    return {'bytes': len(data), 'sha256': sha(data)}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def safe(path):
    q = PurePosixPath(path)
    require(not q.is_absolute() and '..' not in q.parts and str(q) == path,
            'unsafe relative path: ' + path)
    return path


def read_pin(pin):
    p = Path(pin['path'])
    require(p.is_file() and not p.is_symlink(), 'missing/nonregular source: ' + str(p))
    data = p.read_bytes()
    require(sha(data) == pin['sha256'], 'source hash drift: ' + str(p))
    if 'bytes' in pin:
        require(len(data) == pin['bytes'], 'source length drift: ' + str(p))
    return data


def encode_json(value):
    return (json.dumps(value, indent=2, sort_keys=True) + '\n').encode()


def write(out, relative, data):
    p = out / safe(relative)
    require(relative not in WRITTEN, 'duplicate generated path: ' + relative)
    WRITTEN.add(relative)
    if VERIFY_EXISTING:
        require(p.is_file() and not p.is_symlink() and p.read_bytes() == data,
                'reproduction mismatch: ' + relative)
        return
    p.parent.mkdir(parents=True, exist_ok=True)
    require(not p.exists(), 'refuse overwrite: ' + str(p))
    p.write_bytes(data)


def checked_group(group):
    root = Path(group['root'])
    seal = root / group['seal']
    raw = read_pin({'path': str(seal), 'sha256': group['seal_sha256']})
    spec = json.loads(raw)
    rows = spec['members']
    expected = {safe(r['path']): r for r in rows}
    require(len(expected) == len(rows), 'duplicate frozen member')
    expected[group['seal']] = info(raw)
    actual = {str(p.relative_to(root)): p for p in root.rglob('*') if p.is_file()}
    require(set(expected) == set(actual), 'frozen member set drift: ' + group['id'])
    require(len(actual) == group['complete_files'], 'frozen member count drift')
    result = []
    for relative in sorted(expected):
        p = actual[relative]
        b = read_pin(dict(expected[relative], path=str(p)))
        result.append((relative, str(p), b))
    return result


def build(output):
    config = json.loads((ROOT / 'INPUTS.json').read_text())
    require(output.parent.resolve().is_relative_to(ROOT), 'output must stay under component root')
    if VERIFY_EXISTING:
        require(output.is_dir(), 'existing reproduction target missing')
    else:
        require(not output.exists(), 'output already exists; preserve attempts, choose a new name')
        output.mkdir(parents=True)
    packet = config['packet']
    bodies = {c['id']: read_pin(c) for c in config['cores']}
    for key, b in bodies.items():
        require(b.endswith(b'\n') and not b.endswith(b'\n\n'), key + ': expected one-LF EOF')
    fragments = [(ROOT / 'templates' / name).read_bytes() for name in FRAGMENTS]
    note = fragments[0]
    maps = []
    for i, core in enumerate(config['cores']):
        b = bodies[core['id']]
        start = len(note)
        note += b
        maps.append(dict(core, byte_start_0=start, byte_end_exclusive=len(note),
                         line_start_1=note[:start].count(b'\n') + 1,
                         line_end_1=note.count(b'\n'), source_lines=len(b.splitlines()),
                         terminal_lf_count=1, transformation='none'))
        note += fragments[i + 1]
    require(all(note.count(b) == 1 for b in bodies.values()), 'body not unique in note')
    write(output, config['note'], note)
    for name, b in zip(FRAGMENTS, fragments):
        write(output, packet + '/framing/' + name, b)

    objects = {}
    records = []
    logical = {}

    def object_part(b):
        key = sha(b)
        if key not in objects:
            packed = gzip.compress(b, mtime=0)
            relative = packet + '/objects/' + key + '.gz'
            write(output, relative, packed)
            objects[key] = dict(info(b), path=relative, stored=info(packed), codec='gzip')
        return {'kind': 'object', 'sha256': key}

    def add_record(alias, original, b):
        require(alias not in logical, 'duplicate archive alias: ' + alias)
        parts = []
        at = 0
        while at < len(b):
            matches = [(b.find(core, at), key) for key, core in bodies.items()]
            matches = [(pos, key) for pos, key in matches if pos >= 0]
            if not matches:
                parts.append(object_part(b[at:])); break
            pos, key = min(matches)
            if pos > at:
                parts.append(object_part(b[at:pos]))
            parts.append({'kind': 'core', 'id': key})
            at = pos + len(bodies[key])
        if not b:
            parts.append(object_part(b''))
        row = dict(info(b), alias=alias, original=original, parts=parts,
                   line_count=len(b.splitlines()))
        records.append(row)
        logical[alias] = b

    for group in config['groups']:
        for relative, original, b in checked_group(group):
            add_record('assemblies/' + group['id'] + '/' + relative, original, b)
    for item in config['external_files']:
        add_record('external/' + item['alias'], item['path'], read_pin(item))
    parent = config['parent']
    parent_bytes = read_pin(parent)
    parent_raw = read_pin({'path': parent['raw_path'], 'sha256': parent['raw_sha256']})
    require(parent_bytes.count(parent_raw) == 1, 'parent raw body not unique')
    parent_start = parent_bytes.index(parent_raw)
    add_record('external/mathematical_parent/canonical_note.md', parent['path'], parent_bytes)
    for core in config['cores']:
        add_record('cores/' + core['id'], core['path'], bodies[core['id']])
    for item in config['generation_history']:
        add_record(item['alias'], item['path'], read_pin(item))

    inner_count = 0
    for group in config['groups']:
        base = 'assemblies/' + group['id'] + '/'
        entries = json.loads(logical[base + 'archive/ALIASES.json'])['aliases']
        for item in entries:
            b = logical[base + safe(item['file'])]
            if item['storage'] == 'embedded_proof_body':
                b = b[item['byte_start_0']:item['byte_end_exclusive']]
            else:
                require(item['storage'] == 'object', 'unsupported inner storage')
            require(info(b) == {'bytes': item['bytes'], 'sha256': item['sha256']},
                    'inner alias drift: ' + item['alias'])
            inner_count += 1

    archive = {'schema': SCHEMA, 'records': records, 'objects': objects,
               'groups': config['groups'], 'inner_aliases_checked': inner_count,
               'scope': 'complete three accepted assembly packages and explicit external file list; no recursive campaign import',
               'mathematical_predicates': 0}
    write(output, packet + '/SOURCE_ARCHIVE.json', encode_json(archive))
    bodymap = {'schema': SCHEMA, 'note': dict(info(note), path=config['note']), 'bodies': maps,
               'fragments': [dict(info(b), path=packet + '/framing/' + name)
                             for name, b in zip(FRAGMENTS, fragments)],
               'parent': dict(parent, byte_start_0=parent_start,
                              byte_end_exclusive=parent_start + len(parent_raw),
                              line_start_1=parent_bytes[:parent_start].count(b'\n') + 1,
                              line_end_1=parent_bytes[:parent_start + len(parent_raw)].count(b'\n'))}
    write(output, packet + '/BODY_MAP.json', encode_json(bodymap))
    branch = json.loads(logical['external/renewal_binding/bootstrap/BRANCH.json'])
    bindings = {'schema': SCHEMA, 'observed_branch': branch, 'main_guard': config['main'],
                'instruction_guard': config['instructions'],
                'renewed_campaign_end_utc': '2026-10-15T21:43:09Z',
                'parent_canonical': bodymap['parent'],
                'integration_authorized': False, 'driver_bound_root_acceptance': None,
                'current_component_root_review': None, 'current_primary_execution': None,
                'current_regular_pr': None,
                'scope': 'recorded observations only; root runtime freshness and integration review remain required'}
    write(output, packet + '/PUBLICATION_BINDINGS.json', encode_json(bindings))
    graph = {'new_claim': config['claim_id'], 'new_note': config['note'],
             'external_edges': [{'from': config['claim_id'], 'to': parent['claim_id'],
                                 'citation': Path(parent['repo_path']).name,
                                 'role': 'mathematical theorem import'}],
             'internal_prerequisite': 'complete chain79d appendix',
             'context_only_no_edge': ['archived local-defect comparison c163',
                                     'parent method attribution', 'Git ancestry'],
             'existing_graph_objects': 'all complete nodes and edges must be preserved during root integration',
             'graph_executed': False}
    write(output, packet + '/GRAPH_PROPOSAL.json', encode_json(graph))
    for source in sorted((ROOT / 'packet_text').glob('*')):
        require(source.is_file() and not source.is_symlink(), 'packet text must be regular files')
        write(output, packet + '/' + source.name, source.read_bytes())

    files = {relative: info((output / relative).read_bytes()) for relative in sorted(WRITTEN)}
    files[parent['repo_path']] = info(parent_bytes)
    manifest = {'schema': SCHEMA, 'claim_id': config['claim_id'], 'note': config['note'],
                'packet': packet, 'helper': config['helper'], 'files': files,
                'external_scientific_paths': [parent['repo_path']],
                'integrity_paths': sorted(set(files) - {parent['repo_path']}),
                'mathematical_predicates': 0, 'science_executed': False,
                'core_sha256': {c['id']: c['sha256'] for c in config['cores']}}
    manifest_path = packet + '/IDENTITY_INPUTS.json'
    manifest_bytes = encode_json(manifest)
    write(output, manifest_path, manifest_bytes)
    inputs = sorted(list(files) + [manifest_path])
    template = (ROOT / 'templates/identity_runner.py.in').read_text()
    helper = template.replace('@AUDIT_INPUT_PATHS@', repr(inputs)).replace(
        '@MANIFEST_PATH@', repr(manifest_path)).replace('@MANIFEST_SHA256@', repr(sha(manifest_bytes)))
    require('@AUDIT_' not in helper and '@MANIFEST_' not in helper, 'unresolved helper token')
    write(output, config['helper'], helper.encode())
    require(WRITTEN == {str(p.relative_to(output)) for p in output.rglob('*') if p.is_file()},
            'unexpected output member')
    summary = {'schema': SCHEMA, 'output': str(output), 'note': info(note),
               'mode': 'read_only_reproduction' if VERIFY_EXISTING else 'build_new',
               'helper': info(helper.encode()), 'manifest': info(manifest_bytes),
               'archive_records': len(records), 'archive_objects': len(objects),
               'inner_aliases_checked': inner_count, 'source_group_counts':
               {g['id']: g['complete_files'] for g in config['groups']},
               'core_occurrences_in_note': {key: note.count(b) for key, b in bodies.items()},
               'external_math_parents': 1, 'mathematical_predicates': 0,
               'proposed_helper_executed': False, 'archived_science_executed': False}
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', default=str(ROOT / 'payload'))
    parser.add_argument('--verify-existing', action='store_true',
                        help='recompute expected bytes and compare without writing the payload')
    args = parser.parse_args()
    VERIFY_EXISTING = args.verify_existing
    build(Path(args.output).resolve())
