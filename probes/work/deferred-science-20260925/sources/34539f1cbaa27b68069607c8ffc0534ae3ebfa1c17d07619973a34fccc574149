#!/usr/bin/env python3
from datetime import datetime,timezone
import hashlib,json
from pathlib import Path

HERE=Path(__file__).resolve().parent
BASE=HERE.parent
ROWS=[
 ('campaign-working/docs/LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md','local_pair.md','7c5bc10d0ca1127c2a1ef6f5cf9269caf6e8f023a09a061c2da0d8e033e35a7a','supplied full-P local H4 and original mark'),
 ('campaign-working/docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md','common_limit.md','c63db3296e5705c57693c2deb109e506f336fae4848d3ab0926d13a98929802b','supplied full electric form, Hamiltonian and GKLS model'),
 ('campaign-working/docs/WEAK_FIELD_WAVE_PACKETS_FROM_MOBILE_RECORD_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md','weak_packets.md','651fa7cfd816ca5df8c401959458b7590c2f6ec706af437ef3ce31accb7d3ccf','normalized compact packets; transverse quotient and zero electric winding'),
 ('prepared-observation-publication/docs/ORIGINAL_RECORD_CALIBRATION_AND_PREPARED_MATTER_PROBE_BOUNDED_THEOREM_NOTE_2026-09-24.md','prepared_note.md','14ed0194fefd18eeee711e733bb76c75ce4a88832b01bc55dc41e6e058ba612b','section B exact J_- preparation and C.2 alternatives; other observation claims not imported'),
 ('prepared-matter-probe-independent/PRE.md','prior_PRE.md','5c5ef65435d4165048048fb3b3d7e8abc9ce86ef5e69d2a20024c9d767f15589','explicit prior independent background'),
 ('prepared-matter-probe-independent/PRE_SEAL.json','prior_PRE_SEAL.json','5c72901c7a027ba7f00685ce39abe206a2ae0b8a73098ab35e7f0b72324f177c','prior evidence identity'),
 ('prepared-matter-probe-independent/POST.md','prior_POST.md','f93f56c8b39bdc79329d964bd0170ceae97876bb366733d492bc58b6edb4ecee','explicit prior released-source comparison background'),
 ('prepared-matter-probe-independent/POST_SEAL.json','prior_POST_SEAL.json','dca495a9a8d810740b3048f38e6709584df74d4d707de593f19426defcae0af1','prior evidence identity'),
 ('campaign-working/docs/ai_methodology/SCIENCE_WORKFLOW.md','workflow.md','d74718214335d4feae4b40d75720482ca93bd1560a3c35174e7bf875b5b59cc4','previously read unchanged procedure'),
 ('campaign-working/AGENTS.md','AGENTS.md','9bea097b409610ed70f55f53349ce206b6df7e62c63205d7775bac9b3d10dde6','previously read unchanged procedure'),
]
out=[]
for origin,rel,expected,role in ROWS:
 src=BASE/origin;raw=src.read_bytes();digest=hashlib.sha256(raw).hexdigest();assert digest==expected,(origin,digest)
 dst=HERE/'sources'/rel;dst.parent.mkdir(exist_ok=True)
 with dst.open('xb') as f:f.write(raw)
 out.append(dict(origin=str(src),frozen_path=str(dst.relative_to(HERE)),sha256=digest,bytes=len(raw),role=role))
pins=dict(created_utc=datetime.now(timezone.utc).isoformat(),phase='blind independent PRE',sources=out,
          original_main_revision='0e6ad8285096ed668816f18caaa6fbbfbd9c50e8',
          forbidden_packets_read=False,author_code_imported_or_run=False)
with (HERE/'SOURCE_PINS.json').open('x') as f:json.dump(pins,f,indent=2);f.write('\n')
print(json.dumps(pins,indent=2))
