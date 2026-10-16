"""Freeze M17 history; exclude external paper assets and interpreter bytecode."""
from pathlib import Path
import gzip,json,hashlib
P=Path(__file__).parent
ARCHIVE='WORK_HISTORY_v1.json.gz'; INDEX='EVIDENCE_MAP_v1.json'
plain=json.loads((P/"PLAIN_FILES_v1.json").read_text())
assert not (P/ARCHIVE).exists() and not (P/INDEX).exists()
assert all((P/x).is_file() for x in plain)
members=[];omitted=[]
for f in sorted(P.rglob('*')):
 if not f.is_file():continue
 name=f.relative_to(P).as_posix();data=f.read_bytes()
 row={'path':name,'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)}
 if any(x in f.relative_to(P).parts for x in ['primary_sources','page_renders']) or f.suffix.casefold() in ['.pdf','.png','.jpeg','.jpg','.webp']:
  omitted.append({**row,'reason':'External complete paper/text/render stays local; source version, identity and reading scope retained'});continue
 if '__pycache__' in f.parts or f.suffix=='.pyc':
  omitted.append({**row,'reason':'Generated interpreter bytecode; source retained'});continue
 members.append({**row,'encoding':'utf-8','content':data.decode('utf-8')})
blob=json.dumps({'scope':'Root and focused independent M17 history; synthetic calculations only, no observation arrays','members':members},ensure_ascii=False,sort_keys=True).encode()
(P/ARCHIVE).write_bytes(gzip.compress(blob,mtime=0))
index={'scope':'Immutable source/history path map; selected plain files are convenient identical views, not independent evidence',
 'archive':{'path':ARCHIVE,'sha256':hashlib.sha256((P/ARCHIVE).read_bytes()).hexdigest(),'bytes':(P/ARCHIVE).stat().st_size},
 'members':[{k:m[k] for k in ['path','sha256','bytes']} for m in members],
 'plain_files':plain,'omitted':omitted,
 'recovery':'Read gzip JSON members; verify SHA256 of UTF-8 content before writing to a separate directory using checked relative paths. Refuse overwrites and path traversal.'}
(P/INDEX).write_text(json.dumps(index,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'members':len(members),'plain':len(plain),'omitted':len(omitted),'archive_bytes':index['archive']['bytes']}))
