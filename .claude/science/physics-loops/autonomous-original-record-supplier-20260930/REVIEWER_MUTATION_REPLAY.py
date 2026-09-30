import ast,json,time,hashlib
from pathlib import Path
p=Path(__file__).parent
repo=p.parents[3]
source=(repo/'scripts/autonomous_local_original_rotor_supplier_2026_09_30.py').read_text()
tree=ast.parse((p/'MUTATIONS.py').read_text())
cases=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='cases' for t in n.targets))
rows=[];start=time.process_time()
for name,fn,args,old,new in cases:
 assert source.count(old)==1
 ns={'__name__':'review_scratch','__file__':str(repo/'scripts/autonomous_local_original_rotor_supplier_2026_09_30.py')}
 exec(compile(source.replace(old,new),name,'exec'),ns)
 try:ns[fn](*args)
 except AssertionError:rows.append({'mutation':name,'rejected_by_mathematical_assertion':True})
 else:raise AssertionError(('survived',name))
result={'primary_sha256':hashlib.sha256(source.encode()).hexdigest(),'replayed_author_mutation_definitions':True,'not_independent_math':True,'mutations':rows,'cpu_seconds':time.process_time()-start}
(p/'REVIEWER_MUTATION_REPLAY_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
