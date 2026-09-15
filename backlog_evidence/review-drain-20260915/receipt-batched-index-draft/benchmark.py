from pathlib import Path
import tempfile,subprocess,time,json,hashlib,gzip,importlib.util
p=Path(__file__).with_name('review_receipt.py');spec=importlib.util.spec_from_file_location('candidate',p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
with tempfile.TemporaryDirectory() as tmp:
 repo=Path(tmp).resolve();subprocess.run(['git','init','-q',str(repo)],check=True);names=[]
 for i in range(1024):
  name=f'object-{i:04d}.gz';(repo/name).write_bytes(gzip.compress((f'archived source {i}\n'*20).encode(),mtime=0));names.append(name)
 subprocess.run(['git','-C',str(repo),'add','.'],check=True);tree=subprocess.check_output(['git','-C',str(repo),'write-tree'],text=True).strip();start=time.perf_counter()
 for name in names:assert m.git(repo,'show',':'+name)==m.repo_file(repo,name).read_bytes()
 old=time.perf_counter()-start;start=time.perf_counter();m.verify_index_bytes(repo,names,'mismatch');new=time.perf_counter()-start;assert subprocess.check_output(['git','-C',str(repo),'write-tree'],text=True).strip()==tree
 result={'scope':'Synthetic same-byte stage0 archival fixture only; not whole-preflight or production speed claim','objects':len(names),'git_object_tree':tree,'old_exact_git_show_seconds':old,'new_exact_batched_seconds':new,'old_git_processes':len(names),'new_git_processes':16,'speed_ratio_for_this_comparison':old/new,'candidate_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'git_version':subprocess.check_output(['git','--version'],text=True).strip()};out=p.parent.parent/'receipt-batched-index-benchmark.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
