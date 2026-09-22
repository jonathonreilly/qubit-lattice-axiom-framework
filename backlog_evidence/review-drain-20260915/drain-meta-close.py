from pathlib import Path
import json,hashlib,subprocess
r=Path('/private/tmp/review-drain-20260915');w=r/'planning-resume';repo='jonathonreilly/qubit-lattice-axiom-framework'
def run(*a):return subprocess.check_output(a,cwd=w,text=True).strip()
def view(n):return json.loads(run('gh','pr','view',str(n),'--repo',repo,'--json','number,state,headRefOid,headRefName,closedAt'))
report=r/'drain-meta-independent-review-v2.json';assert hashlib.sha256(report.read_bytes()).hexdigest()=='f5ad113ae9280aa12c13ba38627056d233602ddda76d7e5d52f7219b4e08cd98';x=json.loads(report.read_text());pub=json.loads((r/'drain-meta-history-publication.json').read_text())
run('git','fetch','-q','origin','+refs/heads/ai/execution:refs/remotes/origin/ai/execution');remote=run('git','rev-parse','origin/ai/execution')
reportrel='backlog_evidence/review-drain-20260915/'+report.name
assert subprocess.check_output(['git','show',remote+':'+reportrel],cwd=w)==report.read_bytes()
reasons={8179:'The decision record treats a supplied sequential formation model as the axiom itself and promotes broader exclusion and classification conclusions beyond the reviewed source. It contains no unique source repair to land.',8555:'The source-versus-carrier recommendation extrapolates selected capture models; its reported proofs and numerical inputs belong to separate source PRs or scratch work. Its useful corrections are preserved as history and remain obligations of those source reviews.',8572:'The record labels proposed clock, ledger, species and amplitude-model choices as decided while relying on unreviewed sibling claims and additional proposed premises. Its short algebraic identities already belong to the separate source PRs; this summary supplies no unique missing implementation or graph repair.'}
for u in x['units']:
 n=u['number'];head=u['headRefOid'];branch=u['headRefName'];receipt={'pr':n,'reviewed_head':head,'branch':branch,'review_sha256':hashlib.sha256(report.read_bytes()).hexdigest(),'history_commit':remote,'branch_deleted':False}
 def save():
  p=r/f'drain-meta-close-{n}.json';p.write_text(json.dumps(receipt,indent=2)+'\n')
 for e in pub['manifest']['files']:
  if e['pr']==n:assert hashlib.sha256(subprocess.check_output(['git','show',remote+':'+e['execution_path']],cwd=w)).hexdigest()==e['sha256']
 p=view(n)
 if p['state']!='OPEN' or p['headRefOid']!=head:receipt['state']='left_unchanged_head_or_state_moved';receipt['observed']=p;save();continue
 assert run('git','ls-remote','--heads','origin','refs/heads/'+branch).split()[0]==head
 body='Closing after independent review: rejected for canonical main landing. '+reasons[n]+'\n\nComplete exact decision/handoff/state history is preserved at https://github.com/'+repo+'/tree/ai/execution/backlog_evidence/review-drain-20260915/meta-decision-history/pr'+str(n)+'. Original branch retained. Scientific source PRs remain separate open reviews; this closure does not reject their useful bounded results or adopt any proposed clause.\n\nReview and full dispositions: https://github.com/'+repo+'/blob/ai/execution/'+reportrel+'\n'
 f=r/f'drain-meta-close-{n}-comment.md';assert not f.exists();f.write_text(body)
 run('gh','pr','comment',str(n),'--repo',repo,'--body-file',str(f));p=view(n)
 if p['state']!='OPEN' or p['headRefOid']!=head:receipt['state']='left_open_head_moved_after_comment';receipt['observed']=p;save();continue
 assert run('git','ls-remote','--heads','origin','refs/heads/'+branch).split()[0]==head
 run('gh','pr','close',str(n),'--repo',repo);after=view(n)
 if after['headRefOid']!=head:
  run('gh','pr','reopen',str(n),'--repo',repo);receipt['state']='reopened_changed_head';receipt['observed']=view(n);save();continue
 assert after['state']=='CLOSED';assert run('git','ls-remote','--heads','origin','refs/heads/'+branch).split()[0]==head
 receipt['state']='CLOSED';receipt['closed']=after;receipt['recovery_branch_verified']=True;save();print(n,'CLOSED branch preserved',flush=True)
