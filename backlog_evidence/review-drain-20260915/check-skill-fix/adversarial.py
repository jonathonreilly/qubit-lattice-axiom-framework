from pathlib import Path
import importlib.util,json,sys
src=Path('/private/tmp/review-drain-20260915/skill-fix/docs/audit/scripts/tests/test_pipeline_manifest_staging.py')
spec=importlib.util.spec_from_file_location('fixture',src);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
results=[]
for name,old,new,test in [('removed-stage','git add -- docs/audit/data/citation_graph_manifest.json',':','test_opt_in_stages_fresh_manifest_before_invariant_only'),('broad-stage','git add -- docs/audit/data/citation_graph_manifest.json','git add -A','test_opt_in_stages_fresh_manifest_before_invariant_only'),('ignored-stage-failure','git add -- docs/audit/data/citation_graph_manifest.json','git add -- docs/audit/data/citation_graph_manifest.json || true','test_failed_staging_stops_before_downstream_work'),('ignored-generator-failure','python3 docs/audit/scripts/write_citation_graph_manifest.py','python3 docs/audit/scripts/write_citation_graph_manifest.py || true','test_failed_generation_never_stages_or_reaches_invariant')]:
 case=m.PipelineManifestStagingTests(test);case.setUp()
 try:
  shell=case.root/'docs/audit/scripts/run_pipeline.sh';text=shell.read_text();assert old in text;shell.write_text(text.replace(old,new,1))
  try:getattr(case,test)()
  except AssertionError as e:results.append(dict(mutation=name,rejected=True,reason=str(e)[:500]))
  else:raise AssertionError('survived:'+name)
 finally:case.doCleanups()
# Existing staged unrelated content stays byte-identical, not merely unstaged dirty data.
case=m.PipelineManifestStagingTests();case.setUp()
try:
 case.git('add','--','unrelated.txt');before=case.git('show',':unrelated.txt');run=case.run_pipeline('--stage-citation-manifest',EXPECT_STAGED='1');assert run.returncode==0;assert case.git('show',':unrelated.txt')==before
 results.append(dict(case='pre-staged unrelated path unchanged',passed=True))
finally:case.doCleanups()
Path('/private/tmp/review-drain-20260915/check-skill-fix/adversarial.json').write_text(json.dumps(results,indent=2));print('PASS:4mutants rejected;pre-staged content preserved')
