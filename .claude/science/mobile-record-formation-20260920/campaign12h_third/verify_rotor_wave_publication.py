"""Portable read-only identity checks; no scientific verdict or execution."""
from pathlib import Path
from hashlib import sha256
import json

def main():
    here=Path(__file__).resolve().parent
    root=here.parents[3]
    manifest=json.loads((here/'PUBLICATION_UNIT_ROTOR_WAVES.json').read_text())
    seen=set()
    for row in manifest['artifacts']:
        relative=Path(row['path'])
        assert not relative.is_absolute() and '..' not in relative.parts
        assert row['path'] not in seen
        seen.add(row['path'])
        data=(root/relative).read_bytes()
        assert len(data)==row['bytes'] and sha256(data).hexdigest()==row['sha256'],row['path']
    assert len(seen)==manifest['artifact_count']
    omitted={row['source_path']:row for row in manifest['omitted_external_sources']}
    inherited=json.loads((here/'PUBLICATION_UNIT_LOCAL_FIELD.json').read_text())
    omitted.update({row['original_path']:row for row in inherited['omitted_external_sources']})
    checked={}
    excluded={}
    def walk(x):
        if isinstance(x,dict):
            if isinstance(x.get('path'),str) and isinstance(x.get('sha256'),str):
                original=x['path']
                if original in omitted:
                    assert x['sha256']==omitted[original]['sha256']
                    excluded[original]=x['sha256']
                else:
                    marker='/.claude/science/'
                    if marker not in original:
                        raise ValueError('Unmapped binding: '+original)
                    relative=Path('.claude/science')/original.split(marker,1)[1]
                    data=(root/relative).read_bytes()
                    assert sha256(data).hexdigest()==x['sha256'],original
                    if 'bytes' in x:assert len(data)==x['bytes']
                    checked[str(relative)]=x['sha256']
            for value in x.values():walk(value)
        elif isinstance(x,list):
            for value in x:walk(value)
    for name in ['LARGE_SPIN_RECORD_AUTHOR_SEAL.json','WEAK_FIELD_WAVEPACKET_AUTHOR_SEAL.json',
                 'large_spin_rotor_independent/PRE_COMPARISON_SEAL.json',
                 'large_spin_rotor_independent/FINAL_SEAL.json',
                 'weak_field_waves_independent/PRE_COMPARISON_SEAL.json',
                 'weak_field_waves_independent/FINAL_SEAL.json']:
        walk(json.loads((here/name).read_text()))
    print(json.dumps({'byte_identical_artifacts':len(seen),
                      'selected_seal_unique_local_bindings':len(checked),
                      'explicitly_omitted_external_bindings':len(excluded),
                      'status':'Identity verification only; no scientific verdict.'},indent=2))
if __name__=='__main__':main()
