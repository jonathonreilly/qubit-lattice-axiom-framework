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
ref='refs/heads/'+branch
remote=lambda:cmd('git','ls-remote','--heads','origin',ref).split()[0]
assert remote()==head,'Original recovery branch moved or missing'
reason=(out/a.report).read_text()
assert 'preserve' in reason.lower() and ('rejected' in reason.lower() or 'deferred' in reason.lower()),'Explicit partial-salvage closure reason required'
receipt={'pr':number,'original_head':head,'branch':branch,'landing':r['candidate_commit'],'source_verified_at':remote_source_commit,'lease_deleted':False,'recovery_branch_preserved':True,'reason_report':a.report}
rp=out/f'partial-closure-{number}.json';assert not rp.exists()
body=f'Reviewed positive source salvage landed on main at {r["candidate_commit"]}. Full disposition and reason: https://github.com/{repo}/blob/ai/execution/{reportpath}\n\n'+reason+'\nThe original head branch is preserved for the unlanded conclusions. This is source review, not an independent audit verdict.\n'
comment=out/f'partial-closure-{number}-comment.md';assert not comment.exists();comment.write_text(body)
fresh=view(number);assert fresh['state']=='OPEN' and fresh['headRefOid']==head and fresh['headRefName']==branch
assert remote()==head
cmd('gh','pr','comment',str(number),'--repo',repo,'--body-file',str(comment))
fresh=view(number);assert fresh['state']=='OPEN' and fresh['headRefOid']==head and fresh['headRefName']==branch
assert remote()==head
cmd('gh','pr','close',str(number),'--repo',repo)
receipt['closed']=view(number);assert receipt['closed']['state']=='CLOSED' and receipt['closed']['headRefOid']==head
assert remote()==head
rp.write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({'pr':number,'state':'CLOSED','recovery_branch_preserved':True}))
