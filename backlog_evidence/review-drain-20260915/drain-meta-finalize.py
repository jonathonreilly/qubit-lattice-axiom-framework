import json,subprocess,hashlib
from pathlib import Path
R=Path('/private/tmp/review-drain-20260915'); W=R/'review-meta-slot'; base='7475249f415a87db92a611e6157fae600d66f3f4'
def git(*a):return subprocess.check_output(['git','-C',str(W),*a])
def sha(b):return hashlib.sha256(b).hexdigest()
def save(p,j):
 with (R/p).open('x') as f:json.dump(j,f,indent=2);f.write('\n')
inv=json.loads((R/'drain-meta-original-inventory.json').read_text());v2=json.loads((R/'drain-meta-8572-inventory-v2.json').read_text());inv[2].update(headRefOid=v2['head'],delta_base=v2['delta_base'],original_paths=v2['original_paths'])
rows=[]; inherited=[]
for unit in inv:
 n=unit['number'];h=unit['headRefOid'];b=unit['delta_base']
 live=json.loads(subprocess.check_output(['gh','pr','view',str(n),'--repo','jonathonreilly/qubit-lattice-axiom-framework','--json','headRefOid,headRefName,state,updatedAt']))
 assert live['headRefOid']==h and live['state']=='OPEN';save(f'drain-meta-{n}-final-head.json',live)
 assert git('merge-base',base,h).decode().strip()==b
 patch=git('diff','--binary',b,h);(R/f'drain-meta-{n}-verified-final.patch').write_bytes(patch)
 actual=set(git('diff','--name-only',b,h).decode().splitlines());assert actual=={x['path'] for x in unit['original_paths']}
 for p in unit['original_paths']:
  data=git('show',h+':'+p['path']);ls=git('ls-tree',h,'--',p['path']).decode().split();assert ls[0]==p['mode'] and ls[2]==p['blob'] and sha(data)==p['sha256']
  rows.append(dict(p,pr=n,original_revision=h,delta_base=b,disposition='historical_only_reject_main',recovery={'revision':h,'path':p['path'],'sha256':p['sha256'],'proposed_execution_path':f'backlog_evidence/review-drain-20260915/meta-decision-history/pr{n}/'+p['path']},claim_scope='campaign decision/proposal and author-reported sibling findings; not independent source proof or audit authority'))
 unit['verified_patch_sha256']=sha(patch)
 for name in ['HANDOFF.md','STATE.yaml']:
  path='.claude/science/physics-loops/admissibility-induced-law-20260906/'+name
  if path in actual:continue
  try:data=git('show',h+':'+path)
  except subprocess.CalledProcessError:continue
  out=R/f'drain-meta-{n}-inherited-{name}';out.write_bytes(data);ls=git('ls-tree',h,'--',path).decode().split()
  inherited.append(dict(pr=n,original_revision=h,path=path,mode=ls[0],blob=ls[2],sha256=sha(data),bytes=len(data),local_recovery=str(out),disposition='inherited_context_not_new_source'))
ctx=[]
for p in json.loads((R/'drain8137-original-review.json').read_text())['input_bindings'][:6]:
 data=(W/p['path']).read_bytes();assert sha(data)==p['sha256'];ctx.append(dict(p,read_scope='same-session complete authority read reused at exact SHA'))
for p in ['docs/repo/DEFERRED_DECISIONS.md','docs/repo/REVIEW_FEEDBACK_WORKFLOW.md','docs/repo/ACTIVE_REVIEW_QUEUE.md']:
 ctx.append(dict(path=p,sha256=sha((W/p).read_bytes()),read_scope='governance routing/standing defaults; active queue routing and status boundaries'))
report=dict(status='REJECT_MAIN_LANDING_PRESERVE_HISTORICAL_PROVENANCE',reviewer_session='/root/review_8011',current_base=base,units=inv,original_dispositions=rows,inherited_context=inherited,context_inputs=ctx,runtime_scientific_inputs=[],source_changes=[],audit_verdict=None,branches='Preserve all three original branches. Root must recheck live heads immediately before closure.',current_main_loss='No source is proposed for removal or overwrite. Separate source PRs retain independent review obligations; summaries do not import their proofs or grades.',claim_dispositions={'8179':['Blocks01–34 interpretation/threshold/memory/gravity summaries: author history only. Sequential formation is a supplied model, not an axiom selected by this record.','HANDOFF blocks01–05 certificates, closures and later corrigenda: retain complete version as history; no grade inheritance.'], '8555':['Blocks39–52 capture/streaming/count/inertia and force numbers: sibling-model claims, not independent proofs here.','Wind-isotropy/collision correction and variable-magnitude escape: useful exact historical provenance; source PRs own canonical corrections.','HANDOFF and STATE resume instructions/certificates are historical; neither grants present authority.'],'8572':['Rows1–50 clocks, ledger, amplitude, strains, species and mass claims: conditional supplied-model summaries, no adoption of clauses A/B/C.','Fork probe and scratch numerics: proposed research and reported checks, no universal exclusion or GR derivation.','New-head alternating-length/rest-energy correction must be retained at95be2edf; old0659 coverage not substituted.']},salvage={'canonical':'No unique missing implementation, graph repair, or self-contained scientific packet identified in these seven-path deltas. Non-theorem/meta form itself is not rejection reason.','history':'Preserve full exact decision, handoff, state and fork-probe versions with historical/unreviewed README on ai/execution.','elementary_algebra':'For odd bipartite hopping H and diagonal parity epsilon, {H,epsilon}=0 gives (H+m epsilon)^2=H^2+m^2. Chessboard positive phi has phi_x phi_y=1 on nearest-neighbor edges, hence phi H phi=H absent onsite terms. These short identities do not establish the broader physical/uniqueness claims and already point to separate source PRs.'},limitations='No sibling source theorem is accepted or rejected by this meta review; no campaign or primary execution undertaken. External comparisons are not imported as premises. Main landing would require a separately reviewed narrowed source packet, not rebranding historical summaries as proof.')
save('drain-meta-independent-review.json',report)
print(json.dumps({'report_sha256':sha((R/'drain-meta-independent-review.json').read_bytes()),'inherited':inherited},indent=2))
