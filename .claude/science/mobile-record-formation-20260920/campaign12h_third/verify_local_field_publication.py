"""Read-only portable byte verification of the selected publication unit.

This is provenance bookkeeping, not an independent scientific check.
"""
from pathlib import Path
from hashlib import sha256
import json


def main():
    here = Path(__file__).resolve().parent
    root = here.parents[3]
    manifest = json.loads((here/'PUBLICATION_UNIT_LOCAL_FIELD.json').read_text())
    paths = set()
    failures = []
    for row in manifest['artifacts']:
        relative = Path(row['path'])
        if relative.is_absolute() or '..' in relative.parts or row['path'] in paths:
            raise ValueError('Unsafe or duplicate artifact path: '+row['path'])
        paths.add(row['path'])
        target = root/relative
        if not target.is_file():
            failures.append({'path':row['path'],'error':'missing'})
            continue
        data = target.read_bytes()
        if len(data) != row['bytes'] or sha256(data).hexdigest() != row['sha256']:
            failures.append({'path':row['path'],'error':'source identity mismatch'})
    if len(paths) != manifest['artifact_count']:
        raise ValueError('Manifest artifact count mismatch')
    print(json.dumps({'verified_artifacts':len(paths)-len(failures),
                      'failures':failures,
                      'omitted_primary_sources':len(manifest['omitted_external_sources']),
                      'status':'Byte identities only; no scientific verdict.'},indent=2))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
