#!/usr/bin/env python3
"""Source-only POST authentication; no author builder is imported or run."""
from pathlib import Path
import datetime,hashlib,json,shutil
HERE=Path(__file__).resolve().parent
FALLBACK=Path('/Users/jonreilly/Documents/Codex/mobile-record-formation-20260920/.claude/science/mobile-record-formation-20260920/campaign12h_fourth')
BASE=HERE.parent if (HERE.parent/'fast_band_energy_author').is_dir() else FALLBACK
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def check(p,want):
 got=digest(p);assert got==want,(str(p),got,want)
 return {'path':str(p),'bytes':p.stat().st_size,'sha256':got}
def verify(sealroot,sealname,want):
 p=sealroot/sealname;entry=check(p,want);obj=json.loads(p.read_text())
 rows=[check(sealroot/r['path'],r['sha256']) for r in obj['artifacts']]
 return obj,{'seal':entry,'authenticated_artifacts':rows,'count':len(rows)}
pre,precheck=verify(HERE,'PRE_SEAL.json','b17570e736b8a496ae76f71d918087c5c301f3abb05b21733b9204ee3b2239db')
author,authorcheck=verify(BASE/'fast_band_energy_author','AUTHOR_SEAL.json','409ed3831825ab6fd90b9fae16ac074995bacdd2af760727bf7e3a9f3111efc2')
prior,priorcheck=verify(BASE/'general_microscopic_birth_energy_independent','FINAL_COMPARISON_SEAL.json','9e85bfa3c1f20ababdb5e4b368d865a01c3f5f4d1c0f728deff684f0d3ea6596')
check(BASE/'general_microscopic_birth_energy_independent/POST_GENERAL_MICROSCOPIC_COMPARISON.md','6fc6cbfe124668aaeddca9a5c5f2f1b48166cb817b91bbaf3ed79209c5524959')
sourcecheck=[check(BASE/rel,want) for rel,want in author['sources_sha256'].items()]
snapshots=[]
paths=[BASE/'fast_band_energy_author'/r['path'] for r in author['artifacts']]
paths += [BASE/'fast_band_energy_author/AUTHOR_SEAL.json']
paths += [BASE/rel for rel in author['sources_sha256']]
paths += [BASE/'general_microscopic_birth_energy_independent'/s for s in ('POST_GENERAL_MICROSCOPIC_COMPARISON.md','FINAL_COMPARISON_SEAL.json')]
for p in paths:
 rel=p.relative_to(BASE);dest=HERE/'post_sources'/rel;dest.parent.mkdir(parents=True,exist_ok=True)
 if dest.exists():assert dest.read_bytes()==p.read_bytes()
 else:shutil.copyfile(p,dest)
 snapshots.append({'source_relative_to_campaign12h_fourth':str(rel),'snapshot':str(dest.relative_to(HERE)),'sha256':digest(p),'bytes':p.stat().st_size})
result={'authenticated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'PRE_unchanged':precheck,'released_author':authorcheck,'author_bound_sources':sourcecheck,'prior_completed_scoped_comparison':priorcheck,'snapshots':snapshots,'scope':'Hash authentication and immutable local source snapshots; source validity is separately assessed in COMPARISON.md. No audit status is inferred.'}
(HERE/'POST_SOURCE_BINDINGS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps({'PRE_unchanged':precheck['count'],'author_artifacts':authorcheck['count'],'author_sources':len(sourcecheck),'prior_comparison_artifacts':priorcheck['count'],'source_snapshots':len(snapshots),'all_hashes_match':True},indent=2))
