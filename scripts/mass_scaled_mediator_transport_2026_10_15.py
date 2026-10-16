"""Integrity-only primary. No scientific computation, helper import or replay."""
from pathlib import Path, PurePosixPath
import hashlib
import json

REPO = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 60
NOTE = 'docs/MASS_SCALED_MEDIATOR_TRANSPORT_BOUNDED_THEOREM_NOTE_2026-10-15.md'
PACKET = '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015'
PARENT = 'docs/NEAREST_NEIGHBOR_SHARED_MEDIATOR_PROGRAMMING_BOUNDED_THEOREM_NOTE_2026-10-15.md'
MANIFEST_SHA256 = '6b547bc5f38a31a1794a3a07776955c2cdbddfb91ec44d4239d01ee20d740e36'
AUDIT_INPUT_PATHS = ('.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/ACTUAL_BINDING.json', '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/ARCHIVE_INDEX.json', '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/ARTIFACT_PLAN.md', '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/ASSUMPTIONS_AND_IMPORTS.md', '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/BODY_MAP.json', '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/CLAIM_STATUS_CERTIFICATE.md', '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/DEPENDENCIES.json', '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/EXPOSURE_AND_LIMITS.md', '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/GOAL.md', '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/HANDOFF.md', '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/PR_BODY.md', '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/PR_TITLE.txt', '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/PUBLICATION_STATE.json', '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/REVIEW_HISTORY.md', '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/SOURCE_MANIFEST.json', '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/TRACE_GATE.md', '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/binding_sources/EXTERNAL_9605_SCOPE.json', '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/binding_sources/OPEN_DELTA.json', '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/binding_sources/REFS.json', '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/source_recovery/070ecbfde3e9_ACCEPTANCE.md', '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/source_recovery/12940dac4eec_FINAL_SOURCE_RECHECK.json', '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/source_recovery/16c557054f50_FINAL_FREEZE.json', '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/source_recovery/494b4a1b7eaf_READ_COVERAGE.md', '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/source_recovery/4eac1e235892_stdout', '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/source_recovery/55f84274ea10_close_review.py', '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/source_recovery/5871330e1923_PROPOSAL_FREEZE.json', '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/source_recovery/7032c75133b6_FINAL_FREEZE.json', '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/source_recovery/7d755929ed1d_stdout', '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/source_recovery/8319969f2412_SEAL_RECEIPT.json', '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/source_recovery/96673d1ea60d_SOURCE_CLOSURE.json', '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/source_recovery/9bad8213ab82_LAUNCH.json', '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/source_recovery/9ed1cf096359_recorder_source.py', '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/source_recovery/c7342b78acc2_EXECUTION.json', '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/source_recovery/cbfaec06c0e8_EXECUTION.json', '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/source_recovery/cebbafe2b0b3_child_source.py', '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/source_recovery/e2a84f2ecca1_LAUNCH.json', '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/source_recovery/e37286b1a818_SOURCE_MANIFEST.json', '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/source_recovery/e3b0c44298fc_stderr', '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/source_recovery/f3c8bf07f6f9_child_source.py', '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/source_recovery/fcf66962cfe1_seal_metadata.py', 'docs/MASS_SCALED_MEDIATOR_TRANSPORT_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'docs/NEAREST_NEIGHBOR_SHARED_MEDIATOR_PROGRAMMING_BOUNDED_THEOREM_NOTE_2026-10-15.md', '.claude/science/physics-loops/toe-mass-scaled-mediator-transport-20261015/INPUT_MANIFEST.json')

def digest(data):
    return hashlib.sha256(data).hexdigest()

def safe(path):
    relative = PurePosixPath(path)
    if relative.is_absolute() or '..' in relative.parts:
        raise ValueError('Non-relative or escaping input path')
    resolved = (REPO / path).resolve()
    resolved.relative_to(REPO.resolve())
    return resolved

def require(condition, message):
    if not condition:
        raise ValueError(message)

def read_json(path):
    return json.loads(safe(path).read_bytes())

def interval(container, row):
    raw = container[row['start_byte_inclusive']:row['end_byte_exclusive']]
    require(len(raw) == row['bytes'] and digest(raw) == row['sha256'], 'Body interval identity')
    require(container.count(raw) == 1, 'Body must occur exactly once')
    return raw

def main():
    manifest_path = PACKET + '/INPUT_MANIFEST.json'
    manifest_bytes = safe(manifest_path).read_bytes()
    require(digest(manifest_bytes) == MANIFEST_SHA256, 'Input manifest identity')
    manifest = json.loads(manifest_bytes)
    require(manifest['schema'] == 'source_integrity_inputs_v1', 'Manifest schema')
    rows = manifest['inputs']
    require(len({row['path'] for row in rows}) == len(rows), 'Duplicate manifest paths')
    require(set(AUDIT_INPUT_PATHS) == {row['path'] for row in rows} | {manifest_path}, 'Input path set')
    for row in rows:
        data = safe(row['path']).read_bytes()
        require(len(data) == row['bytes'] and digest(data) == row['sha256'], 'Input identity: ' + row['path'])
    note = safe(NOTE).read_bytes()
    header = note.split(b'---', 2)[1].decode()
    require('canonical_parent_binding_complete: true' in header.splitlines(), 'Root canonical binding required; source proposal is not bound')
    for line in ('claim_type: bounded_theorem', 'actual_current_surface_status: conditional-support',
                 'trace_class: upstream_support', 'audit_required_before_effective_retained: true',
                 'bare_retained_allowed: false',
                 'upstream_dependencies: ["nearest_neighbor_shared_mediator_programming_bounded_theorem_note_2026-10-15"]'):
        require(line in header.splitlines(), 'Required current claim/dependency field: ' + line)
    body_map = read_json(PACKET + '/BODY_MAP.json')
    expected = {'mass_scaled_candidate': '785e56e3f8e667750b1f54da8963274096ac3ddac9fb8c56db3d6460846773e7', 'mass_scaled_review': 'cc5670ba9d6da565d75efb7bf70f7fc5d39f677a129cd2d1b744cc529b7b106e'}
    require(len(body_map['bodies']) == 2 and {row['name'] for row in body_map['bodies']} == set(expected), 'Complete body map')
    for row in body_map['bodies']:
        require(row['container'] == NOTE and row['sha256'] == expected[row['name']], 'Body role and hash')
        interval(note, row)
    dependencies = read_json(PACKET + '/DEPENDENCIES.json')['dependencies']
    require(len(dependencies) == 1, 'Exactly one mathematical parent')
    parent_row = dependencies[0]
    require(parent_row['path'] == PARENT and parent_row['claim_id'] == 'nearest_neighbor_shared_mediator_programming_bounded_theorem_note_2026-10-15', 'Parent role')
    parent = safe(PARENT).read_bytes()
    require(digest(parent) == '68f0ee48bc27f86fabb19f1920cd63f8ea829b716c2fde043fe68001aa6e5649' == parent_row['sha256'] and len(parent) == parent_row['bytes'], 'Canonical parent identity')
    row = body_map['parent_body']
    require(row['container'] == PARENT and row['sha256'] == 'd4ed04f737c418cd951d9c736a81785863e09b0031a3ffaecf2c02233f1f3d25', 'Single-port parent interval role')
    interval(parent, row)
    state = read_json(PACKET + '/PUBLICATION_STATE.json')
    require(state['kind'] == 'dated_source_proposal_not_actual_binding', 'Dated proposal provenance')
    for field in ('canonical_binding', 'primary_execution', 'cache_execution', 'mutation_execution', 'graph_execution', 'publication_action', 'retained_audit'):
        require(state[field] is None, 'Historical outcome must remain null: ' + field)
    require(state['scientific_programs_run'] == 0 and state['historical_programs_replayed'] == 0, 'Historical execution scope')
    require(read_json(PACKET + '/DEPENDENCIES.json')['supplied_controls_are_axioms'] is False,
            'supplied controls are not axioms')
    require(read_json(PACKET + '/DEPENDENCIES.json')['universal_no_go'] is False,
            'positive conditional scope')
    binding = read_json(PACKET + '/ACTUAL_BINDING.json')
    require(binding['kind'] == 'actual_canonical_source_binding', 'actual binding kind')
    bound = binding['canonical_note']
    require(bound['path'] == NOTE and bound['bytes'] == len(note) and bound['sha256'] == digest(note),
            'actual note binding')
    require(binding['raw_bodies'] == body_map['bodies'], 'actual body binding')
    require(binding['canonical_parent'] == dependencies[0], 'actual parent binding')
    require(binding['parent_body'] == body_map['parent_body'], 'actual parent body binding')
    require(binding['base_head'] == '60d0ac6642802cdbdea27c6c2c49d0825cba48cd', 'actual stack head')
    require(binding['base_branch'] == 'physics-loop/toe-shared-mediator-programming-20261015', 'actual stack branch')
    require(binding['planned_feature_branch'] == 'physics-loop/toe-mass-scaled-mediator-transport-20261015', 'actual feature branch')
    observed = binding['parent_pr']
    require(observed['number'] == 9604 and observed['state'] == 'OPEN' and observed['isDraft'] is False
            and observed['headRefOid'] == binding['base_head'] and observed['headRefName'] == binding['base_branch'],
            'observed parent PR binding')
    refresh = read_json(PACKET + '/binding_sources/REFS.json')
    require(binding['origin_main'] == refresh['refs']['origin/main']
            and binding['instruction_revision'] == refresh['refs']['origin/ai/execution']
            and refresh['refs']['HEAD'] == binding['base_head'], 'latest main refresh binding')
    require(binding['retained_audit'] is False and binding['canonical_execution_not_yet_performed'] is True,
            'dated binding execution scope')

    print(json.dumps({'result': 'source_integrity_verified', 'scope': 'identities and body/dependency structure only',
                      'scientific_programs_run': 0, 'historical_programs_replayed': 0,
                      'publication_or_retained_status_certified': False}, sort_keys=True))
    print('per_element: exact bytes and manifest identities only; no physical-element validation')
    print('per_site: source preserves fixed-pair and isolation premises; no new lattice computation')
    print('per_mode: N_X=1 theorem scope retained; no sector or spectral execution')
    print('per_block: two immutable bodies and one mathematical dependency checked')
    print('lattice_wide: no native supplier, global program, scientific execution or retained audit certified')

if __name__ == '__main__':
    main()
