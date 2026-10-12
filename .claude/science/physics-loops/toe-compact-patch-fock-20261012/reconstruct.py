from pathlib import Path
import gzip, hashlib, json
P = Path(__file__).resolve().parent
W = P.parents[3]
for row in json.loads((P/'PUBLICATION_EDITS.json').read_text())['outputs']:
    b = gzip.decompress((P/row['preserved_source']).read_bytes())
    assert hashlib.sha256(b).hexdigest() == row['source_sha256']
    t = b.decode()
    for edit in row['edits']:
        assert t.count(edit['before']) == 1
        t = t.replace(edit['before'], edit['after'])
    t += row['appended_text']
    assert (W/row['publication_path']).read_text() == t
    assert hashlib.sha256(t.encode()).hexdigest() == row['publication_sha256']
print('Complete Fock note and primary reconstruct exactly from frozen sources and explicit edits')
