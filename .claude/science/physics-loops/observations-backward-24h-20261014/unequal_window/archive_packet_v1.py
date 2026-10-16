"""Freeze M16 history; exclude external paper assets and interpreter bytecode."""
from pathlib import Path
import gzip,json,hashlib
P=Path(__file__).parent
ARCHIVE='WORK_HISTORY_v1.json.gz'; INDEX='EVIDENCE_MAP_v1.json'
plain=[
 'WORKING_v4.md','NO_GO_DISCIPLINE_CHECKLIST.md','CONFORMANCE_v1.md','REVIEW_RECORD_v1.md',
 'CHECKPOINT_v3.json','PRIOR_SEARCH_v1.json','REPO_CONTEXT_v1.json',
 'CANONICAL_EXECUTION_v3.json','CANONICAL_NOTATION_REPAIR_v1.json',
 'CANONICAL_SELECTION_REPAIR_v1.json','GEOMETRY_EXECUTION_FAILURE_v2.json',
 'FORMATTING_REPAIR_v1.json','M16_SOURCE_PREFLIGHT_v1.json',
 'mutations_v1/REPORT_v1.json','run_mutations_v1.py','archive_packet_v1.py',
 'independent_geometry_v1/INDEPENDENT_DERIVATION_v1.md',
 'independent_geometry_v1/AUTHOR_CORRESPONDENCE_v1.md',
 'independent_geometry_v1/CANONICAL_REVIEW_v1.md',
 'independent_weak_v1/WEAK_PAIR_REVIEW_v1.md',
 'independent_weak_v1/CANONICAL_WEAK_PAIR_REVIEW_v1.md',
 'independent_observation_v1/REPORT_v1.md',
 'independent_observation_v1/PAIR_FUNCTIONAL_DERIVATION_v1.md',
 'independent_observation_v1/M16_CANONICAL_SOURCE_COMPARISON_v1.md',
 'independent_observation_v1/M16_CLUSTER_CAP_v1.md',
]
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
blob=json.dumps({'scope':'Root and focused independent M16 history; synthetic calculations only, no observation arrays','members':members},ensure_ascii=False,sort_keys=True).encode()
(P/ARCHIVE).write_bytes(gzip.compress(blob,mtime=0))
index={'scope':'Immutable source/history path map; selected plain files are convenient identical views, not independent evidence',
 'archive':{'path':ARCHIVE,'sha256':hashlib.sha256((P/ARCHIVE).read_bytes()).hexdigest(),'bytes':(P/ARCHIVE).stat().st_size},
 'members':[{k:m[k] for k in ['path','sha256','bytes']} for m in members],
 'plain_files':plain,'omitted':omitted,
 'recovery':'Read gzip JSON members; verify SHA256 of UTF-8 content before writing to a separate directory using checked relative paths. Refuse overwrites and path traversal.'}
(P/INDEX).write_text(json.dumps(index,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'members':len(members),'plain':len(plain),'omitted':len(omitted),'archive_bytes':index['archive']['bytes']}))
