"""Read-only portable evidence authentication; not a scientific rerun."""
from pathlib import Path
from hashlib import sha256
import json


def main():
    here = Path(__file__).resolve().parent
    root = here.parents[3]
    manifest = json.loads((here / 'PUBLICATION_UNIT_ENERGY_SELECTION.json').read_text())
    original = Path(manifest['original_source_root'])
    historical = {(r['path'], r['sha256'], r['bytes'])
                  for r in manifest['historical_instruction_snapshots']}
    seen = set()
    for row in manifest['artifacts']:
        rel = Path(row['path'])
        assert not rel.is_absolute() and '..' not in rel.parts and str(rel) not in seen
        data = (root / rel).read_bytes()
        assert len(data) == row['bytes'] and sha256(data).hexdigest() == row['sha256'], str(rel)
        seen.add(str(rel))
    assert len(seen) == manifest['artifact_count']
    bindings = {}
    skipped = set()

    def walk(value):
        if isinstance(value, dict):
            if isinstance(value.get('path'), str) and isinstance(value.get('sha256'), str):
                key = (value['path'], value['sha256'], value.get('bytes'))
                if key in historical:
                    skipped.add(key)
                else:
                    path = Path(value['path'])
                    rel = path.relative_to(original) if path.is_absolute() else path
                    assert '..' not in rel.parts and not rel.is_absolute()
                    data = (root / rel).read_bytes()
                    assert sha256(data).hexdigest() == value['sha256'], str(rel)
                    if 'bytes' in value:
                        assert len(data) == value['bytes'], str(rel)
                    bindings[str(rel)] = value['sha256']
            for item in value.values():
                walk(item)
        elif isinstance(value, list):
            for item in value:
                walk(item)

    for name, expected in manifest['selected_identity_records'].items():
        path = here / name
        assert sha256(path.read_bytes()).hexdigest() == expected, name
        walk(json.loads(path.read_text()))
    assert skipped == historical
    print(json.dumps({'byte_identical_selected_artifacts': len(seen),
                      'selected_record_unique_science_bindings': len(bindings),
                      'historical_instruction_bindings_not_portably_reexecuted': len(skipped),
                      'base_commit': manifest['base_commit'],
                      'status': 'Identity verification only. Historical instruction hashes were authenticated at source and are preserved as provenance, not copied prompts or scientific premises. Selective scientific review is separate.'}, indent=2))


if __name__ == '__main__':
    main()
