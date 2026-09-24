from pathlib import Path
import hashlib,json,urllib.request
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'post_sources/reference';OUT.mkdir(parents=True,exist_ok=True)
url='https://arxiv.org/pdf/1111.4210v2'
p=OUT/'barthel_kliesch_1111.4210v2.pdf'
b=p.read_bytes() if p.exists() else urllib.request.urlopen(url,timeout=60).read()
expected='8ba41b87f829585840fc0f2547d702ab044783b0b1a5997e77cccab589f81c4d'
assert hashlib.sha256(b).hexdigest()==expected
if not p.exists():p.write_bytes(b)
reader=PdfReader(p)
text='\n\n'.join(f'=== PDF page {i+1} ===\n'+(page.extract_text() or '') for i,page in enumerate(reader.pages))
q=OUT/'barthel_kliesch_complete_text.txt';q.write_text(text)
rows=[]
for f in [p,q]:
    item=dict(frozen_path=str(f.relative_to(ROOT)),bytes=f.stat().st_size,sha256=hashlib.sha256(f.read_bytes()).hexdigest(),
              url=url,role='Primary mathematical reference released/cited by root; full extraction frozen; only setting, Theorem 1/proof and propagator appendices used.')
    rows.append(item);print(json.dumps(item,sort_keys=True))
(ROOT/'POST_REFERENCE_PINS.json').write_text(json.dumps(dict(pdf_pages=len(reader.pages),sources=rows),indent=2)+'\n')
print('reference PDF matches root pinned identity; pages',len(reader.pages))
