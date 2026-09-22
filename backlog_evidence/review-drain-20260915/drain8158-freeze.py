import pathlib,subprocess,json,hashlib
r=pathlib.Path('/private/tmp/review-drain-20260915');w=r/'review-meta-slot';out=[]
def cmd(*a):return subprocess.check_output(a)
for n in [8158]:
 meta=json.loads(cmd('gh','pr','view',str(n),'--repo','jonathonreilly/qubit-lattice-axiom-framework','--json','number,title,headRefOid,baseRefOid,headRefName,baseRefName'))
 (r/f'drain8158-pr{n}-metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
 receipt=cmd('python3',str(w/'docs/ai_methodology/skills/review-loop/scripts/review_workspace.py'),'fetch-head','--repo',str(w),'--repository','jonathonreilly/qubit-lattice-axiom-framework','--number',str(n),'--expected',meta['headRefOid'])
 (r/f'drain8158-pr{n}-fetch.json').write_bytes(receipt)
 base=cmd('git','-C',str(w),'merge-base',meta['baseRefOid'],meta['headRefOid']).decode().strip();meta['delta_base']=base
 patch=cmd('git','-C',str(w),'diff','--binary',base,meta['headRefOid']);(r/f'drain8158-pr{n}-original.patch').write_bytes(patch);meta['patch_sha256']=hashlib.sha256(patch).hexdigest();rows=[]
 for path in cmd('git','-C',str(w),'diff','--name-only',base,meta['headRefOid']).decode().splitlines():
  line=cmd('git','-C',str(w),'ls-tree',meta['headRefOid'],'--',path).decode().strip()
  if not line: rows.append({'path':path,'deleted':True});continue
  mode,kind,blobpath=line.split(None,2);blob=blobpath.split('\t')[0];b=cmd('git','-C',str(w),'show',meta['headRefOid']+':'+path);p=r/'drain8158-originals'/str(n)/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b);rows.append(dict(path=path,mode=mode,blob=blob,sha256=hashlib.sha256(b).hexdigest(),size=len(b)))
 meta['original_paths']=rows;out.append(meta)
(r/'drain8158-original-inventory.json').write_text(json.dumps(out,indent=2)+'\n')
print([(u['number'],u['title'],len(u['original_paths']))for u in out])
