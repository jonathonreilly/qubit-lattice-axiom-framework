import pathlib,json,hashlib,subprocess
R=pathlib.Path('/private/tmp/review-drain-20260915');sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();H=lambda b:hashlib.sha256(b).hexdigest()
def git(*a):return subprocess.check_output(['git',*a])
main='3dca18ddd0082dc23bb12c7ca38939b901c28736';source='26d741ce87521f08ef4b12d5395d4c0431e7eafa';prospective='00545238571bc27fc92574dacfd414ec54af8a04'
f=json.loads((R/'drain8173-author-final-freeze.json').read_text());review=json.loads((R/'drain8173-final-review.json').read_text());unit=json.loads((R/'drain8173-unit-final.json').read_text());col=json.loads((R/'train87-collected-units.json').read_text())
assert sha(R/'drain8173-unit-final.json')=='c83c559ec0b724aad8d3e1ffdb74be0a5d91171837fe04c59bd48b6b531621a0';assert sha(R/'drain8173-final-review.json')=='821daa433aaee116b5e36a98b036f777b40ba9f96a84c0f4f8fd100a6e09c3d7'
assert git('rev-parse',source+'^{tree}').decode().strip()==review['source_tree']==f['tree'];assert col['units'][0]['source_paths']==f['source_paths']
for e in review['source_paths']:
 p=e['path'];assert H(git('show',source+':'+p))==e['sha256'];info=git('ls-tree',source,'--',p).decode().split();assert info[0]==e['mode'] and info[2]==e['blob']
checked={};absent=[]
for p,h in f['inputs'].items():
 q=subprocess.run(['git','show',main+':'+p],capture_output=True)
 if q.returncode:
  assert p in f['source_paths'];absent.append(p)
 else:assert H(q.stdout)==h;checked[p]=h
# Prospective PR8172 owned paths already reviewed: compare every added/changed path to actual main.
paths=git('diff','--name-only','6332b12b59c83c5b08cc7b4ad90898cb6666050d',prospective).decode().splitlines();diff=[];equal=[]
for p in paths:
 a=git('show',prospective+':'+p);b=git('show',main+':'+p)
 if a!=b:diff.append(p)
 else:equal.append(p)
assert diff==['docs/audit/data/citation_graph_manifest.json'],diff
print(json.dumps(dict(main=main,source_commit=source,source_tree=f['tree'],source_paths=f['source_paths'],unchanged_main_inputs=checked,own_new_inputs_absent_on_main=absent,prospective_tree=prospective,prospective_source_identical_paths=equal,prospective_differences=diff,science_reruns=0),indent=2))
