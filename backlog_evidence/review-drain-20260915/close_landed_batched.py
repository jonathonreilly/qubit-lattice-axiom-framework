"""Exact-head closure after independently reviewed content lands and provenance is remote.
Each call handles one PR. Retargeting base dependents never accepts their science.
"""
import argparse,hashlib,json,subprocess,re
from pathlib import Path
ap=argparse.ArgumentParser();ap.add_argument('label');ap.add_argument('pr');ap.add_argument('--report',required=True);a=ap.parse_args()
root=Path.cwd();out=root.parent;repo='jonathonreilly/qubit-lattice-axiom-framework'
r=json.loads((out/(a.label+'-landing.json')).read_text());assert r['landing_state']=='LANDED';head=r['heads'][a.pr];number=int(a.pr)
def cmd(*args):return subprocess.check_output(args,text=True).strip()
def git(*args):return cmd('git',*args)
def gh(*args):return json.loads(cmd('gh',*args,'--repo',repo))
def view(n):return gh('pr','view',str(n),'--json','number,state,headRefOid,headRefName,baseRefName,isCrossRepository,isDraft,url,closedAt')
def dependents(branch):return gh('pr','list','--state','open','--base',branch,'--limit','1000','--json','number,headRefOid,headRefName,baseRefName,isDraft')
git('fetch','origin','main','ai/execution');git('merge-base','--is-ancestor',r['candidate_commit'],'origin/main')
# Reverify every source against one frozen fetched main commit using bounded raw blobs.
# No persistent cache, identity shortcut, or cross-PR verification reuse.
remote_source_commit=git('rev-parse','origin/main')
paths=iter(r['source_owners']);pending=next(paths,None)
while pending is not None:
 chunk=[];size=0
 while pending is not None and len(chunk)<64:
  length=(root/pending).stat().st_size
  if chunk and size+length>8*1024*1024:break
  chunk.append(pending);size+=length;pending=next(paths,None)
 result=subprocess.run(['git','cat-file','--batch','-z'],input=b''.join((remote_source_commit+':'+p).encode()+b'\0' for p in chunk),capture_output=True)
 assert result.returncode==0,('git cat-file failed',result.stderr)
 data=result.stdout;offset=0
 for p in chunk:
  end=data.find(b'\n',offset);assert end>=offset,('missing blob header',p)
  match=re.fullmatch(rb'(?:[0-9a-f]{40}|[0-9a-f]{64}) blob ([0-9]+)',data[offset:end]);assert match,('missing or non-blob source',p)
  start=end+1;stop=start+int(match[1]);assert stop<len(data) and data[stop:stop+1]==b'\n',('truncated blob',p)
  assert hashlib.sha256(data[start:stop]).hexdigest()==r['inputs'][p],('landed source drift',p)
  offset=stop+1
 assert offset==len(data),'unexpected trailing batch output'
reportpath='backlog_evidence/review-drain-20260915/'+a.report
assert subprocess.check_output(['git','show','origin/ai/execution:'+reportpath])==(out/a.report).read_bytes(),'report not durably remote'
p=view(number);assert p['state']=='OPEN' and p['headRefOid']==head,p
branch=p['headRefName'];assert branch!='main' and not p['isCrossRepository']
other=gh('pr','list','--state','open','--head',branch,'--limit','1000','--json','number');assert [x['number'] for x in other]==[number],other
children=dependents(branch); receipt={'pr':number,'original_head':head,'branch':branch,'landing':r['candidate_commit'],'dependent_base_maintenance':[],'lease_deleted':False}
rp=out/f'closure-{number}.json'
def save():rp.write_text(json.dumps(receipt,indent=2)+'\n')
# Persist immutable head/base identities and original deltas before any retargeting.
for child in children:
 c=view(child['number']);assert c['state']=='OPEN' and c['baseRefName']==branch and c['headRefOid']==child['headRefOid']
 if subprocess.run(['git','cat-file','-e',c['headRefOid']+'^{commit}'],capture_output=True).returncode:
  git('fetch','origin',c['headRefOid'])
  git('cat-file','-e',c['headRefOid']+'^{commit}')
 base=git('merge-base',head,c['headRefOid']);delta=subprocess.check_output(['git','diff','--binary',base+'..'+c['headRefOid']]);dp=out/f'closure-{number}-child-{c["number"]}-original.patch';dp.write_bytes(delta)
 receipt['dependent_base_maintenance'].append({'original':c,'original_merge_base':base,'delta_sha256':hashlib.sha256(delta).hexdigest(),'delta_file':dp.name})
save()
for entry in receipt['dependent_base_maintenance']:
 c=entry['original'];fresh=view(c['number']);assert fresh['headRefOid']==c['headRefOid'] and fresh['state']=='OPEN' and fresh['baseRefName']==branch
 cmd('gh','pr','edit',str(c['number']),'--repo',repo,'--base','main');fresh=view(c['number']);assert fresh['headRefOid']==c['headRefOid'] and fresh['state']=='OPEN' and fresh['baseRefName']=='main';entry['verified']=fresh;save()
assert not dependents(branch),'Open base dependent remains; preserve branch'
body=f'Reviewed source content landed on main at {r["candidate_commit"]}. Independent review and full constituent dispositions: https://github.com/{repo}/blob/ai/execution/{reportpath}\n\nThe exact integrated candidate passed the full pipeline, strict lint, and changed-evidence checks. Regenerated audit outputs were stripped; this is source review, not an independent audit verdict. Original head verified unchanged before closure.'
comment=out/f'closure-{number}-comment.md';comment.write_text(body+'\n');cmd('gh','pr','comment',str(number),'--repo',repo,'--body-file',str(comment))
fresh=view(number);assert fresh['state']=='OPEN' and fresh['headRefOid']==head
assert not dependents(branch)
cmd('git','push','--force-with-lease=refs/heads/'+branch+':'+head,'origin',':refs/heads/'+branch);receipt['lease_deleted']=True;save()
for e in receipt['dependent_base_maintenance']:
 c=e['original'];fresh=view(c['number']);assert fresh['state']=='OPEN' and fresh['baseRefName']=='main' and fresh['headRefOid']==c['headRefOid'];e['post_delete_verified']=fresh
receipt['immediate_state']=view(number);save();print(json.dumps({'pr':number,'lease_deleted':True,'immediate_state':receipt['immediate_state']['state']}))
