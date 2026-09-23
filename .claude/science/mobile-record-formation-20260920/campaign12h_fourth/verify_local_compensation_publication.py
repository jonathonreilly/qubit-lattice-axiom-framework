"""Portable read-only content verification of the local-compensation research unit."""
from pathlib import Path
from hashlib import sha256
import json

def main():
    here=Path(__file__).resolve().parent
    root=here.parents[3]
    manifest=json.loads((here/'PUBLICATION_UNIT_LOCAL_COMPENSATION.json').read_text())
    original=Path(manifest['original_source_root'])
    seen=set()
    for row in manifest['artifacts']:
        rel=Path(row['path'])
        assert not rel.is_absolute() and '..' not in rel.parts and str(rel) not in seen
        data=(root/rel).read_bytes()
        assert len(data)==row['bytes'] and sha256(data).hexdigest()==row['sha256'],str(rel)
        seen.add(str(rel))
    assert len(seen)==manifest['artifact_count']
    bindings={}
    def walk(value):
        if isinstance(value,dict):
            if isinstance(value.get('path'),str) and isinstance(value.get('sha256'),str):
                rel=Path(value['path']).relative_to(original)
                assert '..' not in rel.parts
                data=(root/rel).read_bytes()
                assert sha256(data).hexdigest()==value['sha256'],str(rel)
                if 'bytes' in value:assert len(data)==value['bytes'],str(rel)
                bindings[str(rel)]=value['sha256']
            for item in value.values():walk(item)
        elif isinstance(value,list):
            for item in value:walk(item)
    for name,expected in manifest['selected_identity_records'].items():
        path=here/name
        assert sha256(path.read_bytes()).hexdigest()==expected,name
        walk(json.loads(path.read_text()))
    print(json.dumps({'byte_identical_selected_artifacts':len(seen),
                      'selected_record_unique_local_bindings':len(bindings),
                      'base_commit':manifest['base_commit'],
                      'status':'Identity verification only; selective scientific review is documented separately.'},indent=2))

if __name__=='__main__':main()
