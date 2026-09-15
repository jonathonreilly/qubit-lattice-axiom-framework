from pathlib import Path
import json,hashlib,subprocess
r=Path('/private/tmp/review-drain-20260915'); w=r/'author-slot-one'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
git=lambda *a:subprocess.check_output(['git','-C',str(w),*a],text=True).strip()
old=json.loads((r/'8087-unit-v1-preexecution.json').read_text()); report=json.loads((r/'review-8087-preexecution.json').read_text())
base='0641ef197a36124872e898265b0d7fc16422b051';tree='fc6fec82fd4c7f3792951f78e0013a55ee2b79da'
assert git('rev-parse','HEAD')==base and git('write-tree')==tree
assert set(git('diff','--cached','--name-only',base).splitlines())=={x['path'] for x in old['source']['paths']}
for x in old['source']['paths']:
 assert sha(w/x['path'])==x['sha256']
 assert hashlib.sha256(subprocess.check_output(['git','-C',str(w),'show',':'+x['path']])).hexdigest()==x['sha256']
changes=[]
for category,rows in old['inputs'].items():
 for row in rows:
  new=sha(w/row['path'])
  if new!=row['sha256']:
   assert category=='context' and row['path'].endswith(('references/UNIT_RECEIPT.md','scripts/review_receipt.py'))
   changes.append({'path':row['path'],'old_sha256':row['sha256'],'new_sha256':new})
   row['sha256']=new
assert len(changes)==2
report.update(source_tree=tree,confirmation_base=base,methodology_context_transition={'previous_base':old['source']['base'],'new_base':base,'changes':changes,'scope':'Read exact landed diff. Registered current premise authority resolution only; no scientific source, runtime, parent, threshold, cap, or acceptance criterion changed. Original preexecution report and failed mechanical preflight remain immutable. No science execution yet.','prior_report_sha256':sha(r/'review-8087-preexecution.json')})
newreport=r/'review-8087-preexecution-fixed-method.json'; assert not newreport.exists();newreport.write_text(json.dumps(report,indent=2)+'\n')
ref={'path':str(newreport),'sha256':sha(newreport)}
old['unit_id']='pr8087-preexecution-fixed-method';old['source'].update(base=base,commit=base,tree=tree)
old['reviewer']['report']=ref
old['reviewer']['references'] += [{'path':str(r/p),'sha256':sha(r/p)} for p in ['8087-unit-v1-preexecution.json','8087-preexecution-preflight.json','8087-author-replay-fixed-method.json']]
for c in old['constituents']:c['dispositions']=dict(ref,json_pointer='/original_dispositions')
for n in old['non_science_notes']:n['review_reference']=ref
out=r/'8087-unit-v1-preexecution-fixed-method.json';assert not out.exists();out.write_text(json.dumps(old,indent=2)+'\n')
print(json.dumps({'tree':tree,'record':str(out),'record_sha256':sha(out),'report_sha256':sha(newreport),'changed_context':changes},indent=2))
