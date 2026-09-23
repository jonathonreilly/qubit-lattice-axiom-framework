"""Portable read-only identity verification of the selected post-formation rotor unit."""
from pathlib import Path
from hashlib import sha256
import json

def main():
    here=Path(__file__).resolve().parent
    root=here.parents[3]
    manifest=json.loads((here/'PUBLICATION_UNIT_POST_FORMATION_ROTOR.json').read_text())
    seen=set()
    for row in manifest['artifacts']:
        rel=Path(row['path'])
        assert not rel.is_absolute() and '..' not in rel.parts and str(rel) not in seen
        data=(root/rel).read_bytes()
        assert len(data)==row['bytes'] and sha256(data).hexdigest()==row['sha256'],str(rel)
        seen.add(str(rel))
    assert len(seen)==manifest['artifact_count']
    bindings={}
    def check(path,digest,size=None):
        data=path.read_bytes()
        assert sha256(data).hexdigest()==digest,str(path)
        if size is not None:assert len(data)==size,str(path)
        bindings[str(path.relative_to(root))]=digest
    def walk(value):
        if isinstance(value,dict):
            if isinstance(value.get('path'),str) and isinstance(value.get('sha256'),str):
                old=value['path']
                assert '/.claude/science/' in old,old
                path=root/'.claude/science'/old.split('/.claude/science/',1)[1]
                check(path,value['sha256'],value.get('bytes'))
            for item in value.values():walk(item)
        elif isinstance(value,list):
            for item in value:walk(item)
    for name,expected in manifest['selected_seals'].items():
        path=here/name
        check(path,expected)
        seal=json.loads(path.read_text())
        walk(seal)
        for relative,digest in seal.get('files',{}).items():
            check(path.parent/relative,digest)
        for relative,digest in seal.get('dependencies',{}).items():
            check(here.parent/relative,digest)
    print(json.dumps({'byte_identical_selected_artifacts':len(seen),
                      'selected_seal_unique_local_bindings':len(bindings),
                      'base_commit':manifest['base_commit'],
                      'status':'Source identity verification only; scientific scope is in the README and source-bound comparisons.'},indent=2))

if __name__=='__main__':main()
