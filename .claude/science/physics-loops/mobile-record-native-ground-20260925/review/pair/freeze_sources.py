#!/usr/bin/env python3
from datetime import datetime,timezone
from pathlib import Path
import hashlib,json,subprocess
HERE=Path(__file__).resolve().parent;BASE=HERE.parent
PUB=BASE/'input-energy-power-publication';REV='60c5f194d940a7bbaf1cdd545296e31d74a02f1a'
specs=[('docs/LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md','local_pair.md','7c5bc10d0ca1127c2a1ef6f5cf9269caf6e8f023a09a061c2da0d8e033e35a7a'),
 ('docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md','common_limit.md','c63db3296e5705c57693c2deb109e506f336fae4848d3ab0926d13a98929802b')]
rows=[]
for rel,name,digest in specs:
 raw=(PUB/rel).read_bytes();assert hashlib.sha256(raw).hexdigest()==digest
 run=subprocess.run(['git','-C',str(PUB),'show',REV+':'+rel],capture_output=True)
 assert run.returncode==0 and not run.stderr and run.stdout==raw
 dest=HERE/'sources'/name;dest.parent.mkdir(parents=True,exist_ok=True)
 with dest.open('xb') as out:out.write(raw)
 rows.append(dict(origin=str(PUB/rel),frozen_path=str(dest.relative_to(HERE)),bytes=len(raw),sha256=digest,
  revision=REV,exact_git_object=True,complete_git_stdout_retained=str(dest.relative_to(HERE))))
for rel,name,digest in [('AGENTS.md','AGENTS.md','9bea097b409610ed70f55f53349ce206b6df7e62c63205d7775bac9b3d10dde6'),
 ('docs/ai_methodology/SCIENCE_WORKFLOW.md','workflow.md','d74718214335d4feae4b40d75720482ca93bd1560a3c35174e7bf875b5b59cc4')]:
 origin=BASE/'campaign-working'/rel;raw=origin.read_bytes();assert hashlib.sha256(raw).hexdigest()==digest
 dest=HERE/'sources'/name
 with dest.open('xb') as out:out.write(raw)
 rows.append(dict(origin=str(origin),frozen_path=str(dest.relative_to(HERE)),bytes=len(raw),sha256=digest,
  role='Unchanged previously read applicable procedure; no new scientific premise'))
data=dict(created_utc=datetime.now(timezone.utc).isoformat(),phase='blind independent PRE',
 sources=rows,scientific_parent_count=2,author_sources_read=False,other_active_packets_read=False,
 source_revision=REV,conditional_imports_unaudited=True)
with (HERE/'SOURCE_PINS.json').open('x') as out:json.dump(data,out,indent=2);out.write('\n')
print(json.dumps(data,indent=2))
