import json,pathlib,hashlib,subprocess,gzip
r=pathlib.Path('/private/tmp/review-drain-20260915'); w=r/'drain-author-slot'
sha=lambda b:hashlib.sha256(b).hexdigest()
git=lambda *a:subprocess.check_output(['git','-C',str(w),*a])
read=lambda n:json.loads((r/n).read_text())
d=read('drain8175-author-unit-draft-v1.json'); f=read('drain8175-source-freeze-v2.json'); h=read('drain8175-author-source-handoff-v1.json')
assert git('rev-parse','HEAD').decode().strip()==d['source']['base']=='3dca18ddd0082dc23bb12c7ca38939b901c28736'
assert git('write-tree').decode().strip()==d['source']['tree']=='7a01b258c1130dd2cd97dbd2d204395135fc1481'
assert not git('diff','--name-only')
paths=git('diff','--cached','--name-only','-z').decode().strip('\0').split('\0')
assert set(paths)=={x['path'] for x in f['source']} and len(paths)==34
checked=[]
for x in f['source']:
 p=x['path']; b=(w/p).read_bytes(); assert sha(b)==x['sha256']; assert git('show',':'+p)==b
 mode,blob,stage=git('ls-files','-s','--',p).decode().split('\t')[0].split(); assert mode==x['mode'] and stage=='0'
 checked.append(dict(x,blob=blob,bytes=len(b)))
for group,rows in d['inputs'].items():
 for x in rows: assert sha((w/x['path']).read_bytes())==x['sha256']; assert sha(git('show',':'+x['path']))==x['sha256']
for x in h['original_dispositions']:
 b=gzip.decompress((w/x['recovery']['path']).read_bytes()); assert sha(b)==x['original_sha256']; assert b==git('show','798f661da7140ff6f73c5e4f4984d80b67b3447a:'+x['original_path']); assert sha((w/x['recovery']['path']).read_bytes())==x['recovery']['sha256']
assert len(h['original_dispositions'])==28
refs={}
for n in ['author-unit-draft-v1.json','author-cheap-v1.json','source-freeze-v2.json','author-source-handoff-v1.json','capture-v1.py','mutation-capture-v1.py','capture-plan-v1.json','adapter-verification-v1.json','early-review-v2.json']:
 p=r/('drain8175-'+n);refs[str(p)]=sha(p.read_bytes())
for n in ['capture-v1.py','mutation-capture-v1.py']: compile((r/('drain8175-'+n)).read_text(),n,'exec')
assert read('drain8175-author-cheap-v1.json')['record_sha256']==refs[str(r/'drain8175-author-unit-draft-v1.json')]
assert read('drain8175-author-cheap-v1.json')['mechanical_status']=='ok'
out={'verified':True,'base':d['source']['base'],'tree':d['source']['tree'],'source':checked,'inputs':d['inputs'],'references':refs,'original_dispositions_count':28}
(r/'check8175/cold_identity_v1.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'verified':True,'source_count':34,'refs':refs},indent=2))
