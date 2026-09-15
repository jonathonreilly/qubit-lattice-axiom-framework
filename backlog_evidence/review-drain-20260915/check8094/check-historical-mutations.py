import ast,gzip,json,hashlib
from pathlib import Path
root=Path(__file__).resolve().parent; out=[]
for number,var in [(8091,'mutations'),(8092,'CASES'),(8094,'MUTATIONS')]:
 folder=next((root/f'original-{number}'/'.claude/science/physics-loops').iterdir())
 harness=folder/'check_mutations.py';tree=ast.parse(harness.read_text())
 cases=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id==var for t in n.targets))
 primary=next((root/f'original-{number}'/'scripts').glob('*.py'));base=primary.read_text(); rows=[]
 for name,old,new in cases:
  assert base.count(old)==1,(number,name)
  expected=base.replace(old,new).encode()
  if number==8094: target=folder/'mutation_evidence'/name/'source.py.gz';err=target.with_name('stderr.gz')
  else:target=folder/'mutations'/(name+'.source.py.gz');err=folder/'mutations'/(name+'.stderr.gz')
  actual=gzip.decompress(target.read_bytes());stderr=gzip.decompress(err.read_bytes())
  assert actual==expected,(number,name,'wrong variant')
  assert b'AssertionError' in stderr,(number,name,'wrong failure')
  rows.append({'name':name,'source_sha256':hashlib.sha256(actual).hexdigest(),'stderr_sha256':hashlib.sha256(stderr).hexdigest(),'failure':stderr.decode().splitlines()[-1]})
 out.append({'number':number,'count':len(rows),'rows':rows})
print(json.dumps(out,indent=2))
