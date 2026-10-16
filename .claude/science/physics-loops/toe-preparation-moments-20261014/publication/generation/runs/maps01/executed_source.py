#!/usr/bin/env python3
"""Emit exact whole-source, function/global and framing maps. No code execution."""
import ast
import difflib
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def identity(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def units(data):
    lines = data.splitlines(keepends=True)
    offsets = [0]
    for line in lines:
        offsets.append(offsets[-1] + len(line))
    tree = ast.parse(data)
    rows = []

    def walk(nodes, prefix=''):
        for node in nodes:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                first = min([node.lineno] + [d.lineno for d in node.decorator_list])
                block = b''.join(lines[first - 1:node.end_lineno])
                rows.append(dict(identity(block), name=prefix + node.name,
                                 start_line_1=first, end_line_1=node.end_lineno,
                                 byte_start_0=offsets[first - 1],
                                 byte_end_exclusive=offsets[node.end_lineno],
                                 ast_sha256=hashlib.sha256(ast.dump(node, include_attributes=False).encode()).hexdigest()))
                walk(node.body, prefix + node.name + '.')
            elif hasattr(node, 'body') and isinstance(node.body, list):
                walk(node.body, prefix)
    walk(tree.body)
    module = []
    for i, node in enumerate(tree.body):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            continue
        raw = b''.join(lines[node.lineno - 1:node.end_lineno])
        names = []
        if isinstance(node, ast.Assign):
            names = [x.id for x in node.targets if isinstance(x, ast.Name)]
        module.append(dict(identity(raw), index=i, kind=type(node).__name__, names=names,
                           start_line_1=node.lineno, end_line_1=node.end_lineno,
                           byte_start_0=offsets[node.lineno - 1],
                           byte_end_exclusive=offsets[node.end_lineno]))
    return rows, module


def save(relative, data):
    path = ROOT / 'review_maps' / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise ValueError('refuse map overwrite: ' + str(path))
    path.write_bytes(data)


def run():
    config = json.loads((ROOT / 'INPUTS.json').read_text())
    sharper = Path(next(g['root'] for g in config['groups'] if g['id'] == 'sharper'))
    baseline_helper = Path(next(p['path'] for p in config['external_files']
                                if p['alias'] == 'procedural_baseline/simultaneous_multi_port_identity_2026_10_14.py'))
    pairs = [
        ('builder', sharper / 'ASSEMBLE_SOURCE_ONLY.py', ROOT / 'BUILD_COMPONENTS.py'),
        ('source_checker', sharper / 'CHECK_SOURCE_ONLY.py', ROOT / 'CHECK_COMPONENTS.py'),
        ('primary_helper', baseline_helper, ROOT / 'payload' / config['helper']),
        ('recorder', sharper / 'record_run.py', ROOT / 'record_run.py'),
        ('builder_current_delta', ROOT / 'history/wrapper_v1/BUILD_COMPONENTS.py', ROOT / 'BUILD_COMPONENTS.py'),
        ('wrapper_repair', None, ROOT / 'REPAIR_WRAPPER.py'),
        ('history_checker', None, ROOT / 'CHECK_HISTORY.py'),
        ('review_mapper', None, ROOT / 'MAKE_REVIEW_MAPS.py'),
        ('freezer', None, ROOT / 'FREEZE_COMPONENTS.py')]
    program_maps = []
    for label, previous, current in pairs:
        new = current.read_bytes()
        old = previous.read_bytes() if previous else b''
        oldunits, oldglobals = units(old)
        newunits, newglobals = units(new)
        oldnames = {r['name']: r for r in oldunits}
        classified = []
        changed = []
        for row in newunits:
            prior = oldnames.get(row['name'])
            state = 'byte_identical' if prior and prior['sha256'] == row['sha256'] else ('changed' if prior else 'new')
            classified.append(dict(row, comparison=state, previous=prior))
            if state != 'byte_identical':
                changed.append(b'\n# ' + row['name'].encode() + b'\n' +
                               new[row['byte_start_0']:row['byte_end_exclusive']])
        diff = ''.join(difflib.unified_diff(old.decode().splitlines(True), new.decode().splitlines(True),
                                           fromfile=str(previous or '/dev/null'), tofile=str(current))).encode()
        save(label + '/complete.diff', diff)
        save(label + '/whole_changed_functions.txt', b''.join(changed))
        newmodule = b''.join(b'\n# module statement ' + str(r['index']).encode() + b'\n' +
                             new[r['byte_start_0']:r['byte_end_exclusive']] for r in newglobals)
        save(label + '/complete_new_module_statements.txt', newmodule)
        program_maps.append({'label': label, 'previous': dict(identity(old), path=str(previous)) if previous else None,
                             'current': dict(identity(new), path=str(current)),
                             'whole_file_byte_identical': previous is not None and old == new,
                             'functions': classified, 'previous_module_statements': oldglobals,
                             'current_module_statements': newglobals,
                             'removed_functions': [r for r in oldunits if r['name'] not in {x['name'] for x in newunits}],
                             'complete_diff': 'review_maps/' + label + '/complete.diff',
                             'complete_diff_identity': identity(diff)})
    framing = []
    current = (ROOT / 'templates/note_header.md').read_bytes()
    for group in config['groups']:
        oldpath = Path(group['root']) / 'wrappers/note_prefix.md'
        old = oldpath.read_bytes()
        diff = ''.join(difflib.unified_diff(old.decode().splitlines(True), current.decode().splitlines(True),
                                           fromfile=str(oldpath), tofile='templates/note_header.md')).encode()
        path = 'framing/' + group['id'] + '_wrapper_to_current.diff'
        save(path, diff)
        framing.append({'prior': dict(identity(old), path=str(oldpath)),
                        'current': dict(identity(current), path='templates/note_header.md'),
                        'diff': dict(identity(diff), path='review_maps/' + path),
                        'raw_proof_change': False})
    bodymap = json.loads((ROOT / 'payload' / config['packet'] / 'BODY_MAP.json').read_text())
    mapdata = {'scope': 'source maps only; maps do not authorize integration or establish mathematics',
               'programs': program_maps, 'framing': framing,
               'body_map': bodymap, 'new_math_predicates': 0,
               'new_current_sidecars': [str(p.relative_to(ROOT)) for p in sorted((ROOT / 'packet_text').glob('*'))]}
    save('PROGRAM_AND_FRAMING_MAP.json', (json.dumps(mapdata, indent=2, sort_keys=True) + '\n').encode())
    footprint = [{'path': str(p.relative_to(ROOT / 'payload')), **identity(p.read_bytes())}
                 for p in sorted((ROOT / 'payload').rglob('*')) if p.is_file()]
    save('EXPECTED_PAYLOAD.json', (json.dumps({'files': footprint, 'count': len(footprint),
         'stage_only_after_root_acceptance': True, 'graph_and_cache_not_in_this_footprint': True},
         indent=2, sort_keys=True) + '\n').encode())
    print(json.dumps({'program_comparisons': len(program_maps), 'framing_comparisons': len(framing),
                      'payload_files': len(footprint), 'raw_proof_changes': 0,
                      'mathematical_predicates': 0, 'source_executed_for_mapping': False}, indent=2))


if __name__ == '__main__':
    run()
