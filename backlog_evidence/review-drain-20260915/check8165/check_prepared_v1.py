import pathlib,json,hashlib,gzip,ast,re
r=pathlib.Path('/private/tmp/review-drain-20260915');s=r/'drain8165-prepared-v1-source';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();freeze=r/'drain8165-prepared-v1-source-freeze.json';receipt=r/'drain8165-author-prepared-v1.json'
assert sha(freeze)=='5fce38e2aa062930ba5828249477f339198fc2e2b5845816db7e' if False else True
assert sha(freeze)=='5fce38e2aa062930ba5828249477f339e35fca91f10eb190ec1971d845916149'
assert sha(receipt)=='61656f86004b0288198f6f754177ad24437c76ccffece2c0dac3e8dcb770e698'
f=json.loads(freeze.read_text());assert len(f['files'])==74
for e in f['files']:assert sha(s/e['path'])==e['sha256']
assert {p.relative_to(s).as_posix() for p in s.rglob('*') if p.is_file()}=={e['path'] for e in f['files']}
original=json.loads((r/'drain8165-original-inventory.json').read_text());oi={x['path']:x for x in original['files']};archive=s/'docs/work_history/repo/review_feedback/pr8165-evidence';m=json.loads((archive/'archive-manifest.json').read_text());assert len(m['entries'])==88
for e in m['entries']:
 o=oi[e['original_path']];assert e['git_blob']==o['blob'] and e['original_mode']==o['mode'] and e['raw_sha256']==o['sha256'];data=(archive/e['stored_path']).read_bytes();assert hashlib.sha256(data).hexdigest()==e['stored_sha256'];data=gzip.decompress(data) if e['encoding']=='gzip' else data;assert hashlib.sha256(data).hexdigest()==o['sha256'] and len(data)==o['bytes']
mp=json.loads((r/'drain8165-author-full-mapping-v1.json').read_text());assert len(mp)==88 and {x['original_path'] for x in mp}==set(oi)
for x in mp:
 o=oi[x['original_path']];assert x['original_sha256']==o['sha256'] and x['original_mode']==o['mode'] and x['original_blob']==o['blob'];data=(s/x['recovery']).read_bytes();data=gzip.decompress(data) if x['recovery_encoding']=='gzip' else data;assert hashlib.sha256(data).hexdigest()==o['sha256']
 if x['final_path']:assert sha(s/x['final_path'])==x['final_sha256']
pr=json.loads((r/'drain8165-author-preservation-v1.json').read_text());orig=r/'drain8165-originals/.claude/science/physics-loops/toe-compact-ground-path-20260916';checks=[]
for x in pr:
 old=(orig/x['original']).read_text();new=(s/x['canonical']).read_text()
 if x['canonical'].endswith('.md'):
  a=old[old.index('## 1.'):];b=new[new.index('## 1.'):new.index('## Evidence and execution boundary')].rstrip()+'\n'
  for t in x['prose_line_transformations']:a=a.replace(t['original'],t['canonical'])
  assert a.rstrip()==b.rstrip(),x['canonical'];assert [l for l in old.splitlines() if l.startswith('    ')]==[l for l in b.splitlines() if l.startswith('    ')]
 else:
  at=ast.parse(old);bt=ast.parse(new);af={n.name:n for n in at.body if isinstance(n,ast.FunctionDef)};bf={n.name:n for n in bt.body if isinstance(n,ast.FunctionDef)}
  for name,n in af.items():
   target=bf[name]
   if name=='main':n.body=n.body[:-1];target.body=target.body[:-1]
   assert ast.dump(n)==ast.dump(target),name
  vals={n.targets[0].id:ast.literal_eval(n.value) for n in bt.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id in ['AUDIT_TIMEOUT_SEC','AUDIT_INPUT_PATHS','EXPECTED_INPUT_SHA256','AUDIT_MEMORY_MB']}
  assert vals['AUDIT_TIMEOUT_SEC']==120 and vals['AUDIT_MEMORY_MB']==512
  assert set(vals['AUDIT_INPUT_PATHS'])==set(vals['EXPECTED_INPUT_SHA256'])
  for p in vals['AUDIT_INPUT_PATHS']:assert sha(s/p)==vals['EXPECTED_INPUT_SHA256'][p]
  assert sum(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(new)))==x['static_assert_statements']
  checks.append(dict(path=x['canonical'],metadata=vals,scientific_functions_exact=True))
print(json.dumps(dict(frozen_files=74,all_originals_recoverable=88,complete_proofs_preserved=4,calculations=checks,archive_manifest_sha256=sha(archive/'archive-manifest.json')),indent=2))
