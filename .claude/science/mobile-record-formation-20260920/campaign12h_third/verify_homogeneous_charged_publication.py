"""Read-only portable identity verification for the homogeneous charged unit."""
from pathlib import Path
from hashlib import sha256
import json

def main():
    here=Path(__file__).resolve().parent;root=here.parents[3]
    manifest=json.loads((here/'PUBLICATION_UNIT_HOMOGENEOUS_CHARGED.json').read_text())
    seen=set()
    for row in manifest['artifacts']:
        p=Path(row['path'])
        assert not p.is_absolute() and '..' not in p.parts and row['path'] not in seen
        seen.add(row['path']);data=(root/p).read_bytes()
        assert len(data)==row['bytes'] and sha256(data).hexdigest()==row['sha256'],row['path']
    assert len(seen)==manifest['artifact_count']
    omitted={}
    for name in ['PUBLICATION_UNIT_LOCAL_FIELD.json','PUBLICATION_UNIT_ROTOR_WAVES.json',
                 'PUBLICATION_UNIT_HOMOGENEOUS_CHARGED.json']:
        for row in json.loads((here/name).read_text())['omitted_external_sources']:
            omitted[row.get('source_path',row.get('original_path'))]=row
    checked={};excluded={}
    def walk(x):
        if isinstance(x,dict):
            if isinstance(x.get('path'),str) and isinstance(x.get('sha256'),str):
                old=x['path']
                if old in omitted:
                    assert x['sha256']==omitted[old]['sha256'];excluded[old]=x['sha256']
                else:
                    assert '/.claude/science/' in old,old
                    relative=Path('.claude/science')/old.split('/.claude/science/',1)[1]
                    data=(root/relative).read_bytes()
                    assert sha256(data).hexdigest()==x['sha256'],old
                    if 'bytes' in x:assert len(data)==x['bytes'],old
                    checked[str(relative)]=x['sha256']
            for value in x.values():walk(value)
        elif isinstance(x,list):
            for value in x:walk(value)
    for name in manifest['selected_seals']:walk(json.loads((here/name).read_text()))
    print(json.dumps({'byte_identical_new_artifacts':len(seen),
                      'selected_seal_unique_local_bindings':len(checked),
                      'explicitly_omitted_external_bindings':len(excluded),
                      'status':'Identity verification only; no scientific verdict.'},indent=2))
if __name__=='__main__':main()
