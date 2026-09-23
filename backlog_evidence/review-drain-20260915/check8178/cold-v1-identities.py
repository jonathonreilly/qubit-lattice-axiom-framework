from pathlib import Path
import json,hashlib,subprocess
R=Path('/private/tmp/review-drain-20260915');W=R/'review-draft-slot';sh=lambda b:hashlib.sha256(b).hexdigest();git=lambda *a:subprocess.check_output(['git','-C',str(W),*a]);rp=R/'drain8178-author-unit-draft-staged-v1.json';assert sh(rp.read_bytes())=='fa502ce48627a80fff2e30ef50c248a44be4f4f1b1afa7c04e4924bc953e1bc6';d=json.loads(rp.read_text());h=json.loads((R/'drain8178-author-handoff-v2.json').read_text());base=d['source']['base'];tree=d['source']['tree'];actual=git('rev-parse','origin/main').decode().strip();assert actual==base=='f947216c6ec62d6c663b9c73ef180b1f4f8b622f';assert git('rev-parse','HEAD').decode().strip()==base
ids={}
for e in d['source']['paths']+sum(d['inputs'].values(),[]):
 p=e['path'];assert p not in ids or ids[p]==e['sha256'];ids[p]=e['sha256'];assert sh((W/p).read_bytes())==e['sha256'];assert sh(git('show',tree+':'+p))==e['sha256']
for e in h['source_files']:assert ids[e['path']]==e['sha256']
assert not git('diff','--name-only');assert git('diff','--cached','--name-only',tree)==b''
rows=git('diff','--name-status','--no-renames',base,tree).decode().splitlines();assert len(rows)==43 and all(x.startswith('A\t') for x in rows);assert {x.split('\t')[1] for x in rows}=={e['path'] for e in h['source_files']}
# Existing main is untouched; all candidate delta is new independently reviewed files.
old='eadad252feffba1891b5b774822da85b92842578';advance=git('diff','--name-only',old,base).decode().splitlines();overlap=sorted(set(advance)&set(ids));assert set(overlap)=={'docs/ai_methodology/skills/review-loop/references/FIXES_AND_REPORTING.md','docs/ai_methodology/skills/review-loop/references/OPERATIONS.md','docs/ai_methodology/skills/review-loop/references/REVIEW_UNITS.md','docs/ai_methodology/skills/review-loop/references/UNIT_RECEIPT.md','docs/audit/scripts/build_citation_graph.py','scripts/audit_packet_script_deps.py'}
for e in d['reviewer']['references']:assert sh(Path(e['path']).read_bytes())==e['sha256']
cheap=R/'drain8178-author-cheap-staged-v2.json';c=json.loads(cheap.read_text());assert c['record_sha256']==sh(rp.read_bytes()) and c['tree']==tree and c['mechanical_status']=='ok' and not c['cache_checked']
# No basename conflict excluding established README exception.
tracked=git('ls-tree','-r','--name-only',base,'docs').decode().splitlines();names={Path(p).name for p in tracked}
newdocs=[e['path'] for e in h['source_files'] if e['path'].startswith('docs/') and e['path'].endswith('.md') and Path(e['path']).name not in ['README.md','SKILL.md']];assert len({Path(p).name for p in newdocs})==len(newdocs) and not any(Path(p).name in names for p in newdocs)
res=dict(status='identity/current-main preservation read-only verification',base=base,tree=tree,reviewed_main=actual,source_paths=43,unique_bound_paths=len(ids),candidate_changes=rows,current_main_advance_paths=advance,relevant_advance_paths=overlap,current_main_preserved=True,basename_collisions=[],science_executions=0,gate_executions=0)
(R/'check8178/cold-v1-identities.json').open('x').write(json.dumps(res,indent=2)+'\n');print('verified',len(ids),'bound paths',len(advance),'main advance paths')
