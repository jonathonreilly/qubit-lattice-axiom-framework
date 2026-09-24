#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,shutil,datetime
HERE=Path(__file__).resolve().parent;D=HERE.parent;RAW=D.parents[3]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
items=[
 ('fast_band_tail_author/ROTOR_CUBE_FAST_ENERGY_STRONG_DECAY_WITHOUT_UNIFORM_DECAY.md','9d73530905763400ce31f66188c5eb9c5c1a0336e0c444bbe4f1c23c0c19fc7a','supplied full physical direct-integral theorem'),
 ('fast_band_tail_author/AUTHOR_SEAL.json','646d5a33082c0d44a8af5a25a22b61da9b8ca89275651f80458c2a9c7f7f02e6','supplied prior author seal'),
 ('fast_band_tail_author/EXACT_TAIL_RESULTS.json','9761680bde05c651c01a421e80b8aeac358ae9b24da717cc7b0b05d48d186a0b','supplied exact physical/cycle/rank/first-mark certificate'),
 ('fast_band_tail_author/exact_tail_control.py','7fb623f63f1d0eeef7b51c619e3f9cd8165e7810eb254f876846c79afcc468b8','read prior certificate implementation; never imported'),
 ('fast_band_tail_independent/PRE_ROTOR_FAST_BAND_TAIL.md','4fac5d28f39bfe747f50c2a8ca083353a92f6a58bddaf46456127d9770d0e5de','released independent prior reconstruction; its current POST not read'),
 ('fast_band_energy_author/ACTUAL_CUBE_BIRTH_ENERGY_ON_THE_FAST_TIME_SCALE.md','f71515321246fd2900b1ca801eb12e816b0a7ab2a1d8f820ae75bb87e28df02a','separate compact-time microscopic interpretation premise'),
 ('fast_band_energy_independent/FINAL_SEAL.json','5824c37555272e57a1b5b0b1214bcb5441a86dd9362f18bb157bbeec960a4ef5','completed compact-time comparison identity/scope only'),
]
rows=[]
for alias,expected,role in items:
 p=D/alias;assert sha(p)==expected,(alias,sha(p));out=HERE/'sources'/alias;out.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,out)
 rows.append({'source_alias':alias,'snapshot':str(out.relative_to(HERE)),'sha256':expected,'bytes':out.stat().st_size,'role':role})
# Reuse previously verified instruction snapshots, not current campaign state.
prior=D/'autonomous_clock_independent/sources/instructions'
for name in ['repository_AGENTS.md','planning_AGENTS.md','SCIENCE_WORKFLOW.md']:
 p=prior/name;out=HERE/'sources/instructions'/name;out.parent.mkdir(exist_ok=True);shutil.copyfile(p,out)
 rows.append({'source_alias':'verified_prior_instruction_snapshot/'+name,'snapshot':str(out.relative_to(HERE)),'sha256':sha(out),'bytes':out.stat().st_size,'role':'reused governing instruction identity'})
extras=[(Path('/Users/jonreilly/.codex/skills/no-go-discipline/SKILL.md'),'no-go-discipline_SKILL.md'),(Path('/Users/jonreilly/.codex/skills/physics-claim-reviewer/SKILL.md'),'physics-claim-reviewer_SKILL_read_only.md'),(Path('/Users/jonreilly/.codex/skills/physics-loop/references/proof-search-governance.md'),'proof-search-governance.md'),(RAW/'docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md','SKILL_FRESHNESS_CHECK.md')]
for p,name in extras:
 out=HERE/'sources/instructions'/name;shutil.copyfile(p,out)
 rows.append({'source_alias':str(p),'snapshot':str(out.relative_to(HERE)),'sha256':sha(out),'bytes':out.stat().st_size,'role':'local identified methodology snapshot; no science authority'})
(HERE/'SOURCE_BINDINGS.json').write_text(json.dumps({'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sources':rows,'forbidden_source_access':False,'boundary':'No new rate-author files, campaign CHECKPOINT, external personal directories or peer current POST contents read. A path-only inventory briefly listed released predecessor folders; those POST contents were not opened.','portability':'Scientific source aliases and hashes are authoritative; historical instruction snapshots may be omitted from a public projection with explicit provenance omissions.','methodology_freshness':'Identified installed local skill/reference snapshot used; no network fetch or workflow/landing action authorized. Physics-claim-reviewer was inspected for applicability, not invoked as a landing workflow.'},indent=2)+'\n')
print(json.dumps({'source_count':len(rows),'all_requested_hashes_authenticated':True},indent=2))
