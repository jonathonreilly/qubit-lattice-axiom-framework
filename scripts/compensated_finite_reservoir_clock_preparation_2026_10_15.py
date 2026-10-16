#!/usr/bin/env python3
"""Source-integrity primary; no scientific code or archived run executes."""
from pathlib import Path, PurePosixPath
import hashlib
import json

REPO = Path(__file__).resolve().parents[1]
PACKET = '.claude/science/physics-loops/toe-compensated-finite-reservoir-clock-preparation-20261015'
NOTE = 'docs/COMPENSATED_FINITE_RESERVOIR_CLOCK_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-15.md'
PARENT = 'docs/FINITE_RESERVOIR_BOUNDARY_CLOCK_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-15.md'
MANIFEST_PATH = PACKET + '/INPUT_MANIFEST.json'
MANIFEST_SHA = 'c3de89ed6b753cf7266e6c33dfec4258103f14256268b891b748db315a3ac77b'
AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = ('.claude/science/physics-loops/toe-compensated-finite-reservoir-clock-preparation-20261015/ACTUAL_BINDING.json', '.claude/science/physics-loops/toe-compensated-finite-reservoir-clock-preparation-20261015/AUTHOR_EXPOSURE.md', '.claude/science/physics-loops/toe-compensated-finite-reservoir-clock-preparation-20261015/AUTHOR_FAILURE_LEDGER.md', '.claude/science/physics-loops/toe-compensated-finite-reservoir-clock-preparation-20261015/BODY_MAP.json', '.claude/science/physics-loops/toe-compensated-finite-reservoir-clock-preparation-20261015/DEPENDENCIES.json', '.claude/science/physics-loops/toe-compensated-finite-reservoir-clock-preparation-20261015/EXPOSURE_AND_LIMITS.md', '.claude/science/physics-loops/toe-compensated-finite-reservoir-clock-preparation-20261015/PUBLICATION_STATE.json', '.claude/science/physics-loops/toe-compensated-finite-reservoir-clock-preparation-20261015/ROOT_ACCEPTANCE.md', '.claude/science/physics-loops/toe-compensated-finite-reservoir-clock-preparation-20261015/SOURCE_MANIFEST.json', '.claude/science/physics-loops/toe-compensated-finite-reservoir-clock-preparation-20261015/SOURCE_REVIEW.md', 'docs/COMPENSATED_FINITE_RESERVOIR_CLOCK_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'docs/FINITE_RESERVOIR_BOUNDARY_CLOCK_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-15.md', '.claude/science/physics-loops/toe-compensated-finite-reservoir-clock-preparation-20261015/INPUT_MANIFEST.json')

def require(condition, message):
    if not condition:
        raise ValueError(message)

def digest(data):
    return hashlib.sha256(data).hexdigest()

def same(data, row, label):
    require(len(data) == row['bytes'] and digest(data) == row['sha256'], label)

def main():
    manifest_raw = (REPO / MANIFEST_PATH).read_bytes()
    require(digest(manifest_raw) == MANIFEST_SHA, 'input manifest identity')
    manifest = json.loads(manifest_raw)
    require(manifest['schema'] == 'compensated-preparation-inputs-v1', 'manifest schema')
    members = manifest['members']
    require(len(AUDIT_INPUT_PATHS) == len(set(AUDIT_INPUT_PATHS)), 'duplicate inputs')
    require(set(AUDIT_INPUT_PATHS) == set(members) | {MANIFEST_PATH}, 'input closure')
    data = {}
    for name, row in members.items():
        path = PurePosixPath(name)
        require(not path.is_absolute() and '..' not in path.parts, 'relative input path')
        data[name] = (REPO / name).read_bytes()
        same(data[name], row, 'input identity: ' + name)

    sources = json.loads(data[PACKET + '/SOURCE_MANIFEST.json'])
    mapping = json.loads(data[PACKET + '/BODY_MAP.json'])
    note = data[NOTE]
    for name in ('candidate', 'channel_refinement'):
        row = mapping[name]
        body = note[row['start']:row['end']]
        same(body, row, 'complete embedded body: ' + name)
        require(note.count(body) == 1, 'unique embedded body: ' + name)
    require(mapping['candidate']['end'] == len(note), 'complete candidate reaches EOF')
    report = data[PACKET + '/SOURCE_REVIEW.md']
    section = mapping['channel_refinement']
    require(report[section['source_start']:section['source_end']] ==
            note[section['start']:section['end']], 'verbatim attributed refinement')
    same(report, sources['sources']['source_review'], 'source review identity')
    same(data[PACKET + '/ROOT_ACCEPTANCE.md'],
         sources['sources']['root_acceptance'], 'root acceptance identity')

    parent = sources['sources']['mathematical_parent']
    same(data[PARENT], parent, 'finite-reservoir canonical parent')
    parent_body = mapping['parent_raw_body']
    body = data[PARENT][parent_body['start']:parent_body['end']]
    same(body, parent_body, 'complete parent proof interval')
    require(data[PARENT].count(body) == 1, 'unique parent proof interval')
    dependencies = json.loads(data[PACKET + '/DEPENDENCIES.json'])
    require(dependencies['direct_mathematical_parents'] == [PARENT], 'sole mathematical parent')
    require(dependencies['memory_resource_note_is_dependency'] is False, 'comparison is not premise')
    state = json.loads(data[PACKET + '/PUBLICATION_STATE.json'])
    require(state['kind'] == 'dated_source_proposal_not_actual_binding', 'honest proposal state')
    require(state['root_source_acceptance'] is True, 'source acceptance')
    for field in ('canonical_binding', 'primary_execution', 'cache_execution',
                  'graph_execution', 'publication_action', 'retained_audit'):
        require(state[field] is None, 'proposal must not fabricate ' + field)

    binding = json.loads(data[PACKET + '/ACTUAL_BINDING.json'])
    require(binding['kind'] == 'actual_canonical_source_binding', 'actual binding kind')
    same(note, binding['canonical_note'], 'actual note binding')
    same(data[PARENT], binding['mathematical_parent'], 'actual parent binding')

    print(json.dumps({'result': 'source_integrity_verified',
        'scope': 'Exact source/body/parent identities only; mathematics and physical supply are not executed.',
        'scientific_programs_run': 0, 'historical_runs_replayed': 0,
        'publication_or_retained_status_certified': False}, sort_keys=True))
    print('per_element: arbitrary old/clock input and passive reference; full transferred reservoir retained')
    print('per_site: supplied positive onsite/nearest-neighbour compensators, full SWAP and entry controls')
    print('per_mode: full-sector turn-on and entry-specific turn-off; channel refinement preserves phase distinction')
    print('per_block: actual free-K aging, scalars, covariance, work, slew and calibration remain charged')
    print('lattice_wide: finite conditional driven preparation; native supply, autonomy and recycling remain open')

if __name__ == '__main__':
    main()
