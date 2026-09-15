import importlib.util,json
from pathlib import Path
root=Path('/private/tmp/review-drain-20260915/receipt-support-fix')
s=importlib.util.spec_from_file_location('fixture',root/'docs/audit/scripts/tests/test_review_receipt.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
results=[]
for case in ['schema2_empty','duplicate_support','helper_pin','cache_still_required']:
 t=m.ReceiptTests();t.setUp()
 try:
  if case=='schema2_empty':t.record.update(schema_version=2,supporting_proofs=[])
  elif case=='helper_pin':
   t.write('scripts/helper.py','AUDIT_TIMEOUT_SEC=30\nAUDIT_INPUT_PATHS=("docs/PROOF.md",)\ndef run(): return 1\n');t.record['inputs']['helpers']=t.bind(['scripts/helper.py']);t.supporting_proof_fixture(pinned=False)
  else:t.supporting_proof_fixture()
  if case=='duplicate_support':t.record['supporting_proofs'].append(dict(t.record['supporting_proofs'][0]))
  status,r=t.check(cache=case=='cache_still_required')
  expected=1 if case in ['duplicate_support','cache_still_required'] else 0
  assert status==expected,(case,r)
  results.append({'case':case,'status':status,'result':r})
 finally:t.doCleanups()
Path('/private/tmp/review-drain-20260915/receipt-support-independent-controls.json').write_text(json.dumps(results,indent=2)+'\n');print([(x['case'],x['status']) for x in results])
