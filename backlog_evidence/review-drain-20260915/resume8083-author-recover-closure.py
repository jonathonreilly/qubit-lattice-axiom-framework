import json,subprocess,hashlib,gzip
from pathlib import Path
R=Path('/private/tmp/review-drain-20260915');W=R/'resume-author8083';commit='932e27f7180f9975456de1ee6874de331afc6b98'
rows=json.loads((R/'resume8083-author-relevant-closure-selection.json').read_text())['rows']
sources=json.loads((R/'resume8083-pinned-source-read-map.json').read_text())
for x in sources:rows.append(dict(x,role='reviewed producer or arithmetic source',available=None))
raw=subprocess.check_output(['git','ls-tree','-r','-z',commit],cwd=W);tree={}
for x in raw.split(b'\0'):
 if not x:continue
 m,p=x.split(b'\t',1);mode,typ,oid=m.decode().split();tree[p.decode()]=(mode,oid)
bytail={}
for p in tree:
 if '/native-' in p:
  tail=p[p.rfind('/native-')+1:];bytail.setdefault(tail,[]).append(p)
dest=Path('docs/work_history/repo/review_feedback/pr8079-8083-scientific-recovery');(W/dest/'objects').mkdir(parents=True,exist_ok=True)
proc=subprocess.Popen(['git','cat-file','--batch'],cwd=W,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
def blob(oid):
 proc.stdin.write((oid+'\n').encode());proc.stdin.flush();h=proc.stdout.readline().split();assert h[1]==b'blob';b=proc.stdout.read(int(h[2]));assert proc.stdout.read(1)==b'\n';return b
out=[];missing=[]
for x in rows:
 h=x['sha256'];available=x.get('available');b=None;provenance=None
 if available and (W/available).is_file():
  v=(W/available).read_bytes();b=gzip.decompress(v) if available.endswith('.gz') else v
  if hashlib.sha256(b).hexdigest()!=h:b=None
  else:provenance={'reused':available}
 if b is None:
  tail=x['original'].split('/toe-24h-probes-20260908/')[-1];candidates=[x['path']] if x.get('path') in tree else bytail.get(tail,[])
  for p in candidates:
   mode,oid=tree[p];v=blob(oid)
   if hashlib.sha256(v).hexdigest()==h:b=v;provenance={'commit':commit,'path':p,'mode':mode,'blob':oid};break
 if b is None:missing.append(x);continue
 if provenance.get('reused'):storage=provenance['reused']
 else:
  storage=str(dest/'objects'/f'{h}.gz');target=W/storage
  if not target.exists():target.write_bytes(gzip.compress(b,mtime=0))
 assert hashlib.sha256(gzip.decompress((W/storage).read_bytes()) if storage.endswith('.gz') else (W/storage).read_bytes()).hexdigest()==h
 out.append({'original':x['original'],'sha256':h,'role':x['role'],'storage':storage,'provenance':provenance})
proc.stdin.close();proc.wait()
report={'boundary':'Exact relevant saved arithmetic and source recovery; no numerical re-execution or new certificate.','rows':out,'missing':missing}
(R/'resume8083-author-scoped-recovery.json').write_text(json.dumps(report,indent=2)+'\n')
(W/dest/'manifest.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'recovered':len(out),'missing':len(missing)}))
