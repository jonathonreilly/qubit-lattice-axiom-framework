#!/usr/bin/env python3
"""Narrow provenance and exact-text check; no mathematical computation replay."""
from pathlib import Path
import difflib
import hashlib
import json

HERE = Path(__file__).resolve().parent
REVIEW = HERE.parent
AUTHOR = REVIEW.parent
ARCHIVE = AUTHOR / 'gauge_source_history/before_invariant_subspace_qualification'
NAME = 'COLLECTIVE_RECORD_CIRCULATION_RELEASES_GAUGE_TRAP.md'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(row, path=None):
    path = Path(row['path']) if path is None else path
    assert path.stat().st_size == row['bytes']
    assert sha(path) == row['sha256']


def binding(path):
    return dict(path=str(path), bytes=path.stat().st_size, sha256=sha(path))


def main():
    previous = REVIEW / 'FINAL_COMPARISON_SEAL.json'
    assert sha(previous) == 'cfba4d9c42dd2be9c2bc3c9f516f13a88c6dad5611125c1b751f01cd867744a2'
    pre = REVIEW / 'PRE_COMPARISON_SEAL.json'
    assert sha(pre) == 'bb7539d6463e71fe402ee5738a40ecff09ba52ec4fc0879f2f271fbce981553e'
    old_seal = ARCHIVE / 'GAUGE_RECORD_AUTHOR_PRECOMPARISON_SEAL.json'
    assert sha(old_seal) == '41c3ccff2f341887b71c1ef5ab7d3055f6288eaea97095c89e577273ec4bc9bc'
    mapping_path = ARCHIVE / 'SOURCE_PATH_MAPPING.json'
    mapping = json.loads(mapping_path.read_text())
    assert len(mapping) == 19
    by_original = {r['original']['path']: r for r in mapping}
    assert len(by_original) == 19
    for row in mapping:
        verify(row['archived'])
        assert row['original']['bytes'] == row['archived']['bytes']
        assert row['original']['sha256'] == row['archived']['sha256']
    frozen = json.loads(old_seal.read_text())
    assert len(frozen['artifacts']) == 18
    for row in frozen['artifacts']:
        mapped = by_original[row['path']]
        assert mapped['original'] == row
        verify(row, Path(mapped['archived']['path']))
    previous_data = json.loads(previous.read_text())
    for row in previous_data['artifacts']:
        verify(row)
    for row in previous_data['sources']:
        archived = by_original.get(row['path'])
        verify(row, Path(archived['archived']['path']) if archived else None)
    corrected = AUTHOR / 'GAUGE_RECORD_AUTHOR_CORRECTED_SEAL.json'
    assert sha(corrected) == 'aff064625c5c987e7a45c0d6a25b7b9c9f05025ea148cc14f224adc3855a6bef'
    current = json.loads(corrected.read_text())
    for key in ('frozen_seal', 'historical_path_mapping', 'comparison_seal', 'delta'):
        verify(current[key])
    for row in current['artifacts']:
        verify(row)
    assert len(current['artifacts']) == 18
    old_rows = {r['path']: r for r in frozen['artifacts']}
    new_rows = {r['path']: r for r in current['artifacts']}
    assert old_rows.keys() == new_rows.keys()
    changed = [path for path in old_rows if old_rows[path] != new_rows[path]]
    assert changed == [str(AUTHOR / NAME)]
    old = (ARCHIVE / NAME).read_text()
    new = (AUTHOR / NAME).read_text()
    assert sha(ARCHIVE / NAME) == '66be07b03dcd19dceb6c989e83f23267de16c00299c897d09df1c21aff65f2ed'
    assert sha(AUTHOR / NAME) == 'a8fff88d18ea74660636171d8c4db861f9b0cb77cfeee0b427a5f4e034398fa5'
    removed = ('Hamiltonian to the trapped state: that Hamiltonian annihilates it. Deriving\n'
               'an effective cycle from a larger microscopic model would require new\n')
    inserted = ('Hamiltonian to the trapped state: the earlier dynamics cannot leave the\n'
                'closed fixed-charge saturated matching sector. Hopping and elementary\n'
                'plaquette terms annihilate this basis vector, while diagonal energies and\n'
                'larger contractible field loops may act inside that sector. Deriving an\n'
                'effective cycle from a larger microscopic model would require new\n')
    assert old.count(removed) == new.count(inserted) == 1
    assert old.replace(removed, inserted) == new
    assert new.replace(inserted, removed) == old
    actual_diff = ''.join(difflib.unified_diff(
        old.splitlines(keepends=True), new.splitlines(keepends=True),
        fromfile='frozen/' + NAME, tofile='corrected/' + NAME))
    assert actual_diff == (AUTHOR / 'GAUGE_RECORD_F1_CORRECTION.diff').read_text()
    inputs = {str(p): binding(p) for p in (
        previous, pre, REVIEW / 'COMPARISON.md', REVIEW / 'REPORT.md',
        corrected, mapping_path, AUTHOR / 'GAUGE_RECORD_F1_CORRECTION.diff')}
    for row in mapping:
        path = Path(row['archived']['path']); inputs[str(path)] = binding(path)
    for row in current['artifacts']:
        path = Path(row['path']); inputs[str(path)] = binding(path)
    for key in ('frozen_seal', 'historical_path_mapping', 'comparison_seal', 'delta'):
        path = Path(current[key]['path']); inputs[str(path)] = binding(path)
    result = {
        'scope': 'Only the accepted F1 paragraph and preserved/final source identities; no mathematics rerun.',
        'finding': 'F1 resolved in the corrected source; no new claim introduced by this paragraph.',
        'old_note': binding(ARCHIVE / NAME),
        'corrected_note': binding(AUTHOR / NAME),
        'corrected_author_seal': binding(corrected),
        'archive_rows_authenticated': len(mapping),
        'prior_independent_artifacts_unchanged': len(previous_data['artifacts']),
        'prior_source_bindings_authenticated_using_archives': len(previous_data['sources']),
        'corrected_author_artifacts_authenticated': len(current['artifacts']),
        'unchanged_author_artifacts': len(current['artifacts']) - 1,
        'exact_single_replacement_and_inverse_recovery': True,
        'recorded_unified_diff_exact': True,
        'removed_text': removed,
        'inserted_text': inserted,
        'source_bindings': list(inputs.values()),
        'limitations': 'Earlier scoped scientific conclusions are reused; no broader source review, new frontier access, audit or publication determination.'
    }
    (HERE / 'CORRECTION_ACK.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k:v for k,v in result.items() if k != 'source_bindings'}, indent=2))


if __name__ == '__main__':
    main()
