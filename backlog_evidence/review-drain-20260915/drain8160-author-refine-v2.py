from pathlib import Path
import json,hashlib,ast,re,subprocess,difflib,gzip
R=Path('/private/tmp/review-drain-20260915');W=R/'drain-author-slot';p=json.loads((R/'drain8160-author-prepared-v1.json').read_text());O=R/'drain8160-author-originals/.claude/science/physics-loops/toe-interacting-scale-20260916';sha=lambda b:hashlib.sha256(b).hexdigest()
notes=p['notes'];runs=p['runners'];owners=[0,1,1,2,3,4,5]; pins=['mu_F((0,60g/a])+mu_B((0,60g/a]) >= g.','A W_E A=C^* W_B C,','A W_E A=C^* W_B C,','chi\'(t)=-(kappa_L/2)t chi(t)+epsilon(t),','sigma(G B)=sigma(G) omega_F(B).','[calH,P(u)]=i Z(Su)-i g J(W_E^(1/2)u).','(g^2 q^2/2)||W_E^(1/2)p_x||_2^2 a_x.']
patch=[]
for n in notes:
 text=(W/n).read_text();new=text.replace('from another PR','from another source package');(W/n).write_text(new);patch+=list(difflib.unified_diff(text.splitlines(True),new.splitlines(True),fromfile=n,tofile=n))
for i,r in enumerate(runs):
 text=(W/r).read_text();assert pins[i] in (W/notes[owners[i]]).read_text()
 new=text.replace('\nTOL','\nassert '+repr(pins[i])+" in (_REPO / AUDIT_INPUT_PATHS[0]).read_text()\n\nTOL",1);(W/r).write_text(new);ast.parse(new);patch+=list(difflib.unified_diff(text.splitlines(True),new.splitlines(True),fromfile=r,tofile=r))
manifestpath=W/'docs/work_history/review_loop/pr8160/original-manifest.json';m=json.loads(manifestpath.read_text());counts={};funcs=0
for e in m:
 b=gzip.decompress((W/e['stored']).read_bytes());assert sha(b)==e['original_sha256']
 if e['final_path']:
  e['final_sha256']=sha((W/e['final_path']).read_bytes())
  if e['final_path'].endswith('.py'):
   orig=ast.parse(b.decode());cur=ast.parse((W/e['final_path']).read_text());a={n.name:ast.dump(n,include_attributes=False) for n in orig.body if isinstance(n,ast.FunctionDef) and n.name!='main'};c={n.name:ast.dump(n,include_attributes=False) for n in cur.body if isinstance(n,ast.FunctionDef) and n.name!='main'};assert a==c;funcs+=len(a)
   data=json.loads((O/'evidence'/Path(e['original_path']).name).with_suffix('.json').read_text());counts[e['final_path']]=data['checks']
manifestpath.write_text(json.dumps(m,indent=2)+'\n')
(R/'drain8160-author-refinement-v2.patch').write_text(''.join(patch))
p['files']=[{'path':x['path'],'sha256':sha((W/x['path']).read_bytes())} for x in p['files']];p['archive_manifest_sha256']=sha(manifestpath.read_bytes());p['historical_assertion_totals']=counts;p['count_scope']='Original assertion invocation counts, not independent theorem/family counts; main print counts retained and current execution still pending.';p['static_checks'].update(scientific_function_asts_unchanged=funcs,decoded_original_payloads=86,literal_own_proof_pins=7)
f=R/'drain8160-author-prepared-v2.json';assert not f.exists();f.write_text(json.dumps(p,indent=2)+'\n');print(json.dumps({'files':len(p['files']),'scientific_functions_unchanged':funcs,'original_checks':counts,'sha256':sha(f.read_bytes())}))
