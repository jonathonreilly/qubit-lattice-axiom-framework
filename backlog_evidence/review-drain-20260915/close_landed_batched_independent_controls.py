from pathlib import Path
import tempfile,subprocess,hashlib,re,json
r=Path(__file__).parent;s=(r/'close_landed_batched.py').read_text();block=s[s.index('remote_source_commit='):s.index("reportpath='")];n=0
with tempfile.TemporaryDirectory() as d:
 p=Path(d)
 def git(*a):return subprocess.check_output(['git',*a],cwd=p,text=True).strip()
 subprocess.run(['git','init','-q',d],check=True);git('config','user.email','test@example.com');git('config','user.name','test')
 names=['a','unicodé\nname','empty'];contents=[b'a\0b\n',b'xyz',b'']
 for name,data in zip(names,contents):(p/name).write_bytes(data)
 git('add','.');git('commit','-qm','frozen');sha=git('rev-parse','HEAD');git('update-ref','refs/remotes/origin/main',sha)
 (p/'a').write_bytes(b'index differs');git('add','a')
 rec={'source_owners':names,'inputs':{k:hashlib.sha256(v).hexdigest() for k,v in zip(names,contents)}}
 class Runner:
  def __init__(self,output=None):self.output=output;self.calls=[]
  def run(self,args,**kw):
   self.calls.append((args,kw));assert all(x.startswith((sha+':').encode()) for x in kw['input'].split(b'\0')[:-1])
   if self.output is not None:return self.output
   return subprocess.run(args,cwd=p,**kw)
 def run(runner,record=rec):exec(block,{'root':p,'r':record,'git':git,'subprocess':runner,'hashlib':hashlib,'re':re})
 good=Runner();run(good);n+=1;assert len(good.calls)==1
 from types import SimpleNamespace as R
 def fail(data,rc=0):
  global n
  try:run(Runner(R(stdout=data,stderr=b'failure',returncode=rc)))
  except AssertionError:n+=1
  else:raise AssertionError('negative control survived')
 for data in [b'',b'bad\n',b'0'*40+b' tree 1\nx\n',b'0'*40+b' blob 3\na\n',b'0'*40+b' blob 1\nz\n']:fail(data)
 raw=subprocess.run(['git','cat-file','--batch','-z'],cwd=p,input=b''.join((sha+':'+k).encode()+b'\0' for k in names),capture_output=True).stdout
 fail(raw+b'extra');fail(raw,1)
 # Missing current-main source must fail even when present in index/worktree.
 (p/'only-index').write_bytes(b'x');git('add','only-index');bad={'source_owners':['only-index'],'inputs':{'only-index':hashlib.sha256(b'x').hexdigest()}}
 try:run(Runner(),bad)
 except AssertionError:n+=1
 else:raise AssertionError('index-only accepted')
 # Chunk count bound, preserving every repeated request rather than caching.
 repeated={'source_owners':['a']*129,'inputs':rec['inputs']};rr=Runner();run(rr,repeated);assert [len(x[1]['input'].split(b'\0'))-1 for x in rr.calls]==[64,64,1];n+=1
out={'controls_passed':n,'scope':'Extracted local block only; no GitHub/network/closure action','source_sha256':hashlib.sha256(s.encode()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()};(r/'close_landed_batched-independent-controls.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
