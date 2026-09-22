import json,subprocess,hashlib
from pathlib import Path
R=Path('/private/tmp/review-drain-20260915');repo=R/'integration-resume';prs=[8138,8139,8141,8142,8146];inv={x['number']:x for x in json.loads((R/'drain-all-inventory-20260922.json').read_text())};skill=repo/'docs/ai_methodology/skills/review-loop/scripts/review_workspace.py'
for pr in prs:
 p=R/f'drain8146-head-{pr}.json';assert not p.exists()
 with p.open('w') as out:subprocess.run(['python3',str(skill),'fetch-head','--repo',str(repo),'--repository','jonathonreilly/qubit-lattice-axiom-framework','--number',str(pr),'--expected',inv[pr]['headRefOid']],stdout=out,check=True)
subprocess.run(['git','fetch','origin','main'],cwd=repo,check=True)
base=subprocess.check_output(['git','rev-parse','origin/main'],cwd=repo,text=True).strip();W=R/'drain-review8146';subprocess.run(['git','worktree','add','--detach',str(W),base],cwd=repo,check=True)
rows=[]
for pr in prs:
 x=inv[pr];head=x['headRefOid'];decl=x['baseRefName'];ref='origin/'+decl
 try:basehead=subprocess.check_output(['git','rev-parse',ref],cwd=repo,text=True).strip()
 except subprocess.CalledProcessError:raise
 mb=subprocess.check_output(['git','merge-base',head,basehead],cwd=repo,text=True).strip();delta=subprocess.check_output(['git','diff','--name-status',mb,head],cwd=repo,text=True);paths=[]
 for line in delta.splitlines():
  status,path=line.split('\t',1);item={'status':status,'path':path}
  if status!='D':
   b=subprocess.check_output(['git','show',head+':'+path],cwd=repo);p=R/'drain8146-originals'/str(pr)/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b);item['sha256']=hashlib.sha256(b).hexdigest()
  paths.append(item)
 patch=subprocess.check_output(['git','diff','--binary',mb,head],cwd=repo);(R/f'drain8146-original-{pr}.patch').write_bytes(patch);rows.append({'pr':pr,'head':head,'declared_base':decl,'base_head':basehead,'merge_base':mb,'paths':paths,'patch_sha256':hashlib.sha256(patch).hexdigest()})
(R/'drain8146-original-inventory.json').write_text(json.dumps({'current_main':base,'constituents':rows},indent=2)+'\n');print(json.dumps({'base':base,'counts':{x['pr']:len(x['paths']) for x in rows}}))
