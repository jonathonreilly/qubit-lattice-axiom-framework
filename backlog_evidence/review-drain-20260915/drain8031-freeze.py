import subprocess,json,pathlib,hashlib
r='/private/tmp/review-drain-20260915/integration-resume'; root=pathlib.Path('/private/tmp/review-drain-20260915'); out=root/'drain8031-originals';out.mkdir(exist_ok=True)
def g(*a):return subprocess.check_output(['git','-C',r,*a])
h='3756b77ab56aa397a7113082783c1c491d8d96ea';b='3dee7c038c60dd9aaddbcc186207f165367cc274'; m=g('merge-base',b,h).decode().strip(); rows=[]
for p in g('diff','--name-only',m,h).decode().splitlines():
 data=g('show',h+':'+p);dest=out/p;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data);dest.chmod(0o444)
 tree=g('ls-tree',h,'--',p).decode().split(); rows.append(dict(path=p,mode=tree[0],blob=tree[2],sha256=hashlib.sha256(data).hexdigest(),size=len(data),recovery=str(dest)))
delta=g('diff','--binary',m,h);(root/'drain8031-original.delta').write_bytes(delta)
(root/'drain8031-original-manifest.json').write_text(json.dumps(dict(head=h,base=b,merge_base=m,main='631d6b36cd1e9b860763ebcad36e40a2bbe7439c',delta_sha256=hashlib.sha256(delta).hexdigest(),files=rows),indent=2)+'\n')
print(len(rows),m)
