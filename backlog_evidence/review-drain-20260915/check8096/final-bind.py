"""Final independent binding; no runner/preflight execution."""
from pathlib import Path
import json,hashlib,subprocess,sys
r=Path('/private/tmp/review-drain-20260915');w=r/'review-slot-one';sys.path.insert(0,str(w/'scripts'));import runner_cache
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();hb=lambda b:hashlib.sha256(b).hexdigest();git=lambda *a:subprocess.check_output(['git','-C',str(w),*a],text=True).strip()
assert len(sys.argv)==2;tree=sys.argv[1];assert git('write-tree')==tree
record=json.loads((r/'8096-unit-v1-preexecution.json').read_text());report=json.loads((r/'review-8096-preexecution.json').read_text());latest=git('rev-parse','origin/main');base=record['source']['base']
for rows in record['inputs'].values():
 for x in rows:
  assert sha(w/x['path'])==x['sha256']
  exists=subprocess.run(['git','-C',str(w),'cat-file','-e',base+':'+x['path']],capture_output=True).returncode==0
  if exists:assert hb(subprocess.check_output(['git','-C',str(w),'show',latest+':'+x['path']]))==x['sha256'],x['path']
runner=record['notes'][0]['primary_runner'];stem=Path(runner).stem;cache_rel='logs/runner-cache/'+stem+'.txt'
changed=set(git('diff','--cached','--name-only',base).splitlines());assert changed=={x['path'] for x in record['source']['paths']}
for x in record['source']['paths']:
 if x['path']!=cache_rel:assert sha(w/x['path'])==x['sha256']
 x['sha256']=sha(w/x['path']);assert hb(subprocess.check_output(['git','-C',str(w),'show',':'+x['path']]))==x['sha256']
for e in report['archive_entries']:assert (w/e['final_path']).read_bytes()==(r/'check8096/original-8096'/e['original_path']).read_bytes()
rp=r/('8096-execution-'+stem+'.json');receipt=json.loads(rp.read_text());res=receipt['result'];cp=Path(receipt['cache_path'])
assert receipt['preexecution_record_sha256']==sha(r/'8096-unit-v1-preexecution.json')
assert res['status']=='ok' and res['exit_code']==0 and res['stderr']=='' and res['elapsed_sec']<120 and receipt['limit_sec']==120
assert cp.resolve()==(w/cache_rel).resolve() and sha(cp)==receipt['cache_sha256'] and runner_cache.cache_status(runner)=='fresh'
assert res['stdout'] in cp.read_text() and 'TOTAL: PASS=41 FAIL=0' in res['stdout']
old=(r/'check8096/original-8096'/cache_rel).read_text();old_pass=[x for x in old.splitlines() if x.startswith('PASS:')];new_pass=[x for x in res['stdout'].splitlines() if x.startswith('PASS:')]
assert len(old_pass)==38 and len(new_pass)==41 and old_pass==new_pass[:38]
assert [x.split(' ',2)[1] for x in new_pass[38:]]==['translation-lexicographic-counterexample','null-prefix-unweighted-exchange-counterexample','star-positive-leaf-cancellation-through-six']
assert not any(x.startswith('FAIL:') for x in res['stdout'].splitlines())
for prefix in ['per_element:','per_site:','per_mode:','per_block:','lattice_wide:']:assert len([x for x in res['stdout'].splitlines() if x.startswith(prefix)])==1
comparison=r/'8096-reviewer-output-comparison.json';assert not comparison.exists();comparison.write_text(json.dumps(dict(original_completed_checks=38,original_check_lines_exactly_retained=True,added_regression_lines=new_pass[38:],new_total=41,boundary='Original cache was historical after proof correction. One new capture binds corrected source and all three declared inputs; retained old check outcomes do not imply acceptance of the old proof.'),indent=2)+'\n')
refs=[r/'8096-unit-v1-preexecution.json',r/'review-8096-preexecution.json',r/'8096-preexecution-preflight.json',r/'8096-preexecution-preflight-execution.json',rp,r/('8096-execution-'+stem+'-started.json'),r/'8096-author-capture.py',r/'8096-author-capture.log',comparison,r/'check8096/final-bind.py']
for rows in report['original_dispositions'].values():
 for x in rows:
  if x['final_path']==cache_rel:x['final_sha256']=sha(cp);x['disposition']='Fresh canonical cache from one corrected-source capture; original 38-check cache remains recoverable byte-exact at frozen original head and in original reviewer snapshot.'
report.update(status='PASS_WITH_BOUNDED_CLAIMS',final_verdict='PASS WITH BOUNDED CLAIMS',source_tree=tree,source_paths=record['source']['paths'],remaining=[],executions=[dict(runner=runner,total_pass=41,total_fail=0,elapsed_sec=res['elapsed_sec'],timeout_sec=120,cache_sha256=sha(cp))],final_confirmation='Complete original and affected correction read; positive-prefix exchange, six-neighbour classification, lexicographic and framework-scope repairs independently confirmed. All 15 staged paths, ten raw historical files and all source/input hashes bound. One actual 41/0 capture; original 38 check lines unchanged plus three regression controls and five honest N5 statements. Independent reviewer controls separately passed 38/0.',current_main_context=dict(commit=latest,assessment='All inherited authorities, context and tooling inputs match latest main exactly. Other newly landed native/classical geometry packets do not supply a physical formation process or alter this declared finite binary product model; no new axiom or primitive is used.'),references=report['references']+[dict(path=str(p),sha256=sha(p)) for p in refs])
final=r/'review-8096-final.json';assert not final.exists();final.write_text(json.dumps(report,indent=2)+'\n');ref=dict(path=str(final),sha256=sha(final))
record['unit_id']='pr8096-final';record['source']['tree']=tree;record['reviewer']['report']=ref
for c in record['constituents']:c['dispositions']=dict(ref,json_pointer='/original_dispositions/'+c['id'])
for x in record['non_science_notes']:x['review_reference']=ref
record['reviewer']['references'] += [dict(path=str(p),sha256=sha(p)) for p in refs];record['boundary']='Final independent source PASS WITH BOUNDED CLAIMS; final cache preflight, combined integration and audit are separate. No physical formation process or full-axiom nonselection theorem.'
fp=r/'8096-unit-v1-final.json';assert not fp.exists();fp.write_text(json.dumps(record,indent=2)+'\n')
md=r/'review-8096.md';assert not md.exists();md.write_text('# PR8096 independent source review\n\n**PASS WITH BOUNDED CLAIMS** at tree `'+tree+'`.\n\nThe corrected proof distinguishes fixed orders from covariant laws, includes zero-prefix probabilities, and extends the binary classification through all six neighbor slots. Framework-wide conclusions were narrowed to the declared model. All 14 original paths are accounted for; ten historical files remain exact.\n\nIndependent controls passed 38/0. One fresh primary capture passed 41/0 under 120 seconds, preserving all original 38 check outcomes and adding three regressions. Final source/input/cache bindings verified.\n\nReport SHA256: `'+sha(final)+'`. Final v1 SHA256: `'+sha(fp)+'`. Integration and audit remain separate.\n')
print(json.dumps(dict(tree=tree,report_sha256=sha(final),record_sha256=sha(fp),elapsed_seconds=res['elapsed_sec']),indent=2))
