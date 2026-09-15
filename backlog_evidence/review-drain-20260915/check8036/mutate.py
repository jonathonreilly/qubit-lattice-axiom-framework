from pathlib import Path
import subprocess,json,hashlib
O=Path('/private/tmp/review-drain-20260915/check8036');R=O.parent/'unit8036';h='6067254e3bca867aa6e737f7aa2bb6078e5d622d'
rows=json.loads(subprocess.check_output(['git','-C',str(R),'show',h+':.claude/science/physics-loops/native-product-gibbs-20260908/MUTATION_RECORD.json']));result=[]
for i,row in enumerate(rows):
 name=row.get('source','native_product_gibbs_encoded_2026_09_08.py');source=(R/'scripts'/name).read_text();assert hashlib.sha256(source.encode()).hexdigest()==row['source_sha256'];assert row['old'] in source
 p=O/'mutants'/str(i)/'scripts'/name;p.parent.mkdir(parents=True);p.write_text(source.replace(row['old'],row['new'],1));run=subprocess.run(['python3',str(p)],capture_output=True,text=True,timeout=60)
 assert run.returncode!=0
 predicate=row.get('expected_failure','full_success_spectral_target');assert predicate in run.stderr,(i,run.stderr)
 result.append(dict(mutation=row.get('name',row.get('mutation')),exit=run.returncode,predicate=predicate,stderr=run.stderr))
(O/'mutations.json').write_text(json.dumps(result,indent=2));print('PASS10mutations failed intended predicates')
