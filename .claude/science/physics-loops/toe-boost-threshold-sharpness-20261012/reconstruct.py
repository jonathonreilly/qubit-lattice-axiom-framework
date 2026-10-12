from pathlib import Path
import gzip, hashlib, json, textwrap
P=Path(__file__).resolve().parent
W=P.parents[3]
sha=lambda b:hashlib.sha256(b).hexdigest()
for row in json.loads((P/'PUBLICATION_EDITS.json').read_text())['outputs']:
    b=gzip.decompress((P/row['preserved_source']).read_bytes())
    assert sha(b)==row['source_sha256']
    t=b.decode()
    for edit in row['edits']:
        assert t.count(edit['before'])==1
        t=t.replace(edit['before'],edit['after'])
    t+=row['appended_text']
    assert t==(W/row['publication_path']).read_text()
    assert sha(t.encode())==row['publication_sha256']
for row in json.loads((P/'PRIMARY_COMPOSITION.json').read_text())['outputs']:
    parts=[]
    for src in row['sources']:
        b=gzip.decompress((P/src['preserved_source']).read_bytes())
        assert sha(b)==src['source_sha256']
        t=b.decode()
        parts.append(t if src['wrapper'] is None else 'def '+src['wrapper']+'():\n'+textwrap.indent(t,'    ')+'\n\n')
    t=row['prefix']+''.join(parts)+row['suffix']
    assert t==(W/row['publication_path']).read_text()
    assert sha(t.encode())==row['publication_sha256']
print('Both full notes and both complete finite controls reconstruct exactly')
