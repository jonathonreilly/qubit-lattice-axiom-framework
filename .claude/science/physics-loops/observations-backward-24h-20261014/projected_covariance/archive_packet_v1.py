"""Package immutable M15 history without publishing external full texts or pixels."""
from pathlib import Path
import gzip,json,hashlib
P=Path(__file__).parent
ARCHIVE='WORK_HISTORY_v1.json.gz'; INDEX='EVIDENCE_MAP_v1.json'
plain=[
 'WORKING_v1.md','WEAK_FORM_v2.md','FAILURE_v1.md','FORWARD_PROTOCOL_v1.json',
 'NO_GO_DISCIPLINE_CHECKLIST.md','CONFORMANCE_v1.md','REVIEW_RECORD_v1.md',
 'CHECKPOINT_v1.json','CHECKPOINT_v2.json','PRIOR_SEARCH_v1.json','REPO_CONTEXT_v1.json',
 'PRIMITIVE_IDENTITY_REUSE_v1.json','M15_SOURCE_PREFLIGHT_v1.json',
 'CANONICAL_REPAIR_IDENTITY_v1.json','PROTOCOL_GUARD_CHECK_v1.json','archive_packet_v1.py',
 'independent_geometry_v1/INDEPENDENT_DERIVATION_v1.md',
 'independent_geometry_v1/AUTHOR_CORRESPONDENCE_v1.md',
 'independent_geometry_v1/CANONICAL_REVIEW_v1.md',
 'independent_weak_v1/WEAK_REVIEW_v1.md',
 'independent_weak_v1/CANONICAL_WEAK_REVIEW_v1.md',
 'independent_observation_v1/REPORT_v1.md','independent_observation_v1/DERIVATION_v1.md',
 'independent_observation_v1/POST_EXPOSURE_COMPARISON_v1.md',
 'independent_observation_v1/M15_CANONICAL_SOURCE_COMPARISON_v1.md',
 'independent_observation_v1/M15_CLUSTER_CAP_v1.md',
 'independent_observation_v1/SOURCE_RECORD_v1.json',
 'independent_observation_v1/M15_CANONICAL_IDENTITY_v1.json',
 'MUTATIONS_v1/RESULTS_v1.json',
]
assert not (P/ARCHIVE).exists() and not (P/INDEX).exists()
assert all((P/f).is_file() for f in plain)
members=[];omitted=[]
for f in sorted(P.rglob('*')):
 if not f.is_file():continue
 name=f.relative_to(P).as_posix();data=f.read_bytes()
 row={'path':name,'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)}
 if any(x in f.relative_to(P).parts for x in ['primary_sources','page_renders']):
  omitted.append({**row,'reason':'External full paper/text/render; kept local, source version and reading scope preserved'});continue
 if '__pycache__' in f.parts or f.suffix=='.pyc':
  omitted.append({**row,'reason':'Generated interpreter bytecode; source preserved'});continue
 members.append({**row,'encoding':'utf-8','content':data.decode('utf-8')})
blob=json.dumps({'scope':'Versioned root and independent M15 science/history; no empirical observations','members':members},ensure_ascii=False,sort_keys=True).encode()
(P/ARCHIVE).write_bytes(gzip.compress(blob,mtime=0))
index={'scope':'Exact original-path map; plain copies are convenient views of archived members, not independent evidence',
 'archive':{'path':ARCHIVE,'sha256':hashlib.sha256((P/ARCHIVE).read_bytes()).hexdigest(),'bytes':(P/ARCHIVE).stat().st_size},
 'members':[{k:m[k] for k in ['path','sha256','bytes']} for m in members],
 'plain_files':plain,'omitted':omitted,
 'unpack':'Read gzip JSON members; encode each content as UTF-8 and verify sha256 before writing to a separate destination using the relative path. Refuse overwriting existing science.'}
(P/INDEX).write_text(json.dumps(index,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'members':len(members),'plain':len(plain),'omitted':len(omitted),'archive_bytes':index['archive']['bytes']}))
