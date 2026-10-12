"""Read-only independent validation of the author's sealed evidence package."""
from pathlib import Path
import hashlib,json,sys,difflib,datetime
root=Path(__file__).resolve().parent
E=root.parent/'dyadic_route_readiness/dyadic_even_refinement'
out=root/'author_evidence_validation.json'
checks=[]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def check(name,ok,**detail):checks.append(dict(name=name,ok=bool(ok),**detail))
def read(name):return json.loads((E/name).read_text())
manifest=read('final_manifest.json')
check('final_manifest_anchor',sha(E/'final_manifest.json')=='e25e34e5200340a92cd2d60949eec7b4b698708fc43b533711666111e7bdbe4e')
fail=[]
for path,spec in manifest['files'].items():
    p=Path(path)
    if not p.is_file() or sha(p)!=spec['sha256'] or p.stat().st_size!=spec['bytes']:fail.append(path)
check('all_final_manifest_files',not fail,count=len(manifest['files']),failed_paths=fail)
excluded={'final_manifest.json','final_receipt.json'}
actual={str(p) for p in E.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.name not in excluded}
actual.add(manifest['main_note'])
check('final_manifest_complete_inventory',actual==set(manifest['files']),missing=sorted(actual-set(manifest['files'])),extra=sorted(set(manifest['files'])-actual),stated_exclusions=manifest['exclusions'])

historical=read('execution_manifest.json');repro=read('reproduction_manifest.json');recovery=read('EXECUTED_INPUT_RECOVERY.json')
check('execution_manifest_anchor',sha(E/'execution_manifest.json')=='dfe56a005e018555d7d93b522d195042b94c74ff8aff67f53783d1cf7276a35f')
check('reproduction_manifest_anchor',sha(E/'reproduction_manifest.json')=='e3fb00cfd543ecb7b09624b4fc366df1dd5cd3a6f41d198d7071434365fa4ad2')
recover={r['historical_path']:r for r in recovery}
check('all_historical_input_bytes_recoverable',set(recover)==set(historical['files']) and all(r['sha256']==historical['files'][p] and sha(r['recovery_path'])==r['sha256'] for p,r in recover.items()),count=len(recover))
check('reproduction_manifest_current_inputs',all(sha(p)==h for p,h in repro['files'].items()),count=len(repro['files']))
check('reproduction_inputs_exact_recovery',repro['files']=={r['recovery_path']:r['sha256'] for r in recovery})

core=E/'frozen/DYADIC_EVEN_REFINEMENT_PROBE.md';executed=E/'frozen/EXECUTED_ARGUMENT.md';final=Path(manifest['main_note'])
check('final_argument_is_append_only',final.read_bytes().startswith(executed.read_bytes()),executed_hash=sha(executed),final_hash=sha(final))
for before,after,diffname,old,new in [(core,executed,'POSTFREEZE_PREEXEC.diff','frozen_argument','preexecution_argument'),(executed,final,'FINAL_EVIDENCE_APPENDIX.diff','executed_argument','final_argument')]:
    computed=''.join(difflib.unified_diff(before.read_text().splitlines(keepends=True),after.read_text().splitlines(keepends=True),fromfile=old,tofile=new))
    check('exact_diff_'+diffname,computed==(E/diffname).read_text())

jobs={'exact_baseline_v2':0,'state_baseline_v2':0,'mutant_missing_normalization':1,'mutant_tensor_shortcut':1,'mutant_missing_state_formfactor':1}
rows=[];receipts=[];outcomes={}
for name,rc in jobs.items():
    for layer in ('inner','outer'):
        path=E/'runs'/f'{name}_{layer}.receipt.json';r=json.loads(path.read_text())
        check('receipt_'+name+'_'+layer,r['returncode']==rc and not r['timeout'] and r['source_unchanged'] and r['source_before']==r['source_after']==historical['files'] and r['actual_manifest_sha256']==sha(E/'execution_manifest.json') and r['expected_manifest_sha256']==sha(E/'execution_manifest.json') and r['timeout_seconds']==(60 if layer=='inner' else 70) and all(sha(r[k])==r[k+'_sha256'] for k in ('stdout','stderr')) and Path(r['stderr']).read_bytes()==b'',returncode=r['returncode'],seconds=r['elapsed_seconds'])
        receipts.append({'name':name,'layer':layer,'path':str(path),'sha256':sha(path),'start_utc':r['start_utc'],'end_utc':r['end_utc'],'elapsed_seconds':r['elapsed_seconds'],'returncode':r['returncode']})
    stdout=E/'runs'/f'{name}_inner.stdout.txt'
    these=[];summary=None
    for lineno,line in enumerate(stdout.read_text().splitlines(),1):
        if not line.startswith('{'):continue
        item=json.loads(line)
        if 'name' in item:
            these.append(item);rows.append({'run':name,'stdout':str(stdout),'line':lineno,'row':item})
        if 'summary' in item:summary=item['summary']
    failures=[x['name'] for x in these if not x['pass']]
    expected_summary={'rows':len(these),'pass':len(these)-len(failures),'fail':len(failures),'failed':failures}
    check('rows_'+name,all(type(x['pass']) is bool for x in these) and len(set(x['name'] for x in these))==len(these) and summary==expected_summary)
    outcomes[name]={'rows':len(these),'failures':failures,'survivors':[x['name'] for x in these if x['pass']]}
check('all_row_inventory_entries',rows==read('row_inventory.json'),count=len(rows))
check('all_receipt_inventory_entries',receipts==read('verified_execution_receipts.json'),count=len(receipts))
disp=read('result_disposition.json')
check('failure_survivor_inventory',all(disp[n]['failed_names']==o['failures'] and disp[n]['surviving_names']==o['survivors'] and disp[n]['summary']['rows']==o['rows'] for n,o in outcomes.items()))
totals={'baseline_rows':sum(o['rows'] for n,o in outcomes.items() if n.endswith('baseline_v2')),'baseline_failed':sum(len(o['failures']) for n,o in outcomes.items() if n.endswith('baseline_v2')),'mutant_rows':sum(o['rows'] for n,o in outcomes.items() if n.startswith('mutant')),'mutant_failed':sum(len(o['failures']) for n,o in outcomes.items() if n.startswith('mutant')),'mutant_surviving':sum(len(o['survivors']) for n,o in outcomes.items() if n.startswith('mutant'))}
summary=read('summary.json')
check('reported_totals',all(summary[k]==v for k,v in totals.items()),**totals)
invalid=read('INVALID_INITIAL_RECORDING.json')
check('invalid_record_files_preserved',all(sha(p)==h for p,h in invalid['retained_files'].items()),count=len(invalid['retained_files']),classification=invalid['status'])

for label in ['missing_normalization','tensor_shortcut','missing_state_formfactor']:
    a=(E/'candidate.py').read_text();b=(E/'variants'/f'{label}.py').read_text()
    changes=[l for l in difflib.unified_diff(a.splitlines(),b.splitlines()) if l.startswith(('+','-')) and not l.startswith(('+++','---'))]
    check('variant_one_material_change_'+label,len(changes)==2,changes=changes)

data={'verified_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks':checks,'all_checks_hold':all(c['ok'] for c in checks),'outcomes':outcomes,'totals':totals,'rows':rows}
out.write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps({'all_checks_hold':data['all_checks_hold'],'checks':len(checks),'failed':[c for c in checks if not c['ok']],'totals':totals,'report':str(out)},indent=2))
sys.exit(0 if data['all_checks_hold'] else 1)
