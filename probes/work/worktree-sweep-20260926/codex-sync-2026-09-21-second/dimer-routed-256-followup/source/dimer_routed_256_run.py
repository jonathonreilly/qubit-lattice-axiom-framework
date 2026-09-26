#!/usr/bin/env python3
"""Execute exactly the frozen sixteen-history N=256 follow-up."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor,as_completed
import datetime,hashlib,json,subprocess,sys,time

sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def identity(p):p=Path(p);return dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p))
def save(p,x):Path(p).write_text(json.dumps(x,indent=2,allow_nan=False)+'\n')
def main():
    root=Path(sys.argv[1]).resolve();manifest_path=root/'MANIFEST.json';manifest=json.loads(manifest_path.read_text())
    assert not (root/'DISPATCH.json').exists(),'Existing dispatch requires explicit recovery rather than overwrite'
    snapshot=root/'frozen_sources';snapshot.mkdir()
    copies=[]
    for key in ['protocol','construction','source','setup','binary']:
        row=manifest[key];p=Path(row['path']);assert identity(p)==row
        if key!='binary':
            target=snapshot/p.name;target.write_bytes(p.read_bytes());copies.append(dict(role=key,original=row,snapshot=identity(target)))
    for row in manifest['geometry']:assert identity(row['file']['path'])==row['file']
    dispatch=dict(started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),manifest=identity(manifest_path),
                  wrapper=identity(__file__),concurrency=2,jobs=len(manifest['jobs']),source_snapshots=copies,
                  hard_deadline_utc='2026-09-22T00:25:55+00:00',order='Descending N, then declared geometry and replicate; all declared jobs retained.')
    save(root/'DISPATCH.json',dispatch)
    deadline=datetime.datetime.fromisoformat(dispatch['hard_deadline_utc']).timestamp()
    jobs=sorted(manifest['jobs'],key=lambda x:(-x['N'],x['kind'],x['replicate']))
    def execute(job):
        path=Path(job['output']);assert not path.exists() and not Path(str(path)+'.state').exists()
        seconds=deadline-time.time()
        if seconds<=0: return dict(job=job,status='not_started_deadline')
        start=time.time()
        try:
            proc=subprocess.run(job['command'],capture_output=True,timeout=seconds)
            stdout=proc.stdout;stderr=proc.stderr;code=proc.returncode
        except subprocess.TimeoutExpired as e:
            stdout=e.stdout or b'';stderr=(e.stderr or b'')+b'\nCampaign hard deadline reached.\n';code=-999
        Path(str(path)+'.stdout').write_bytes(stdout);Path(str(path)+'.stderr').write_bytes(stderr)
        row=dict(job=job,started_unix=start,seconds=time.time()-start,returncode=code,
                 stdout_sha256=hashlib.sha256(stdout).hexdigest(),stderr_sha256=hashlib.sha256(stderr).hexdigest())
        outputs=[]
        for p in [path,Path(str(path)+'.state'),Path(str(path)+'.stdout'),Path(str(path)+'.stderr')]:
            if p.exists():outputs.append(identity(p))
        row['outputs']=outputs
        if code==0:
            value=json.loads(path.read_text())
            assert value['mode']=='production' and value['N']==job['N'] and value['seed']==job['seed']
            assert value['key_permutation_verified'] and value['counts_verified'] and not stderr
            assert [x['t'] for x in value['snapshots']]==[0,7/16,7/8,21/16,7/4]
            row.update(status='complete_verified_receipt',attempts=value['attempts'],accepted=value['accepted'],wall_seconds=value['wall_seconds'])
        else:row['status']='failed'
        receipt=Path(str(path)+'.receipt.json');save(receipt,row)
        return dict(N=job['N'],kind=job['kind'],replicate=job['replicate'],seed=job['seed'],status=row['status'],receipt=identity(receipt))
    results=[]
    with ThreadPoolExecutor(max_workers=2) as pool:
        futures={pool.submit(execute,job):job for job in jobs}
        for future in as_completed(futures):
            job=futures[future]
            try:row=future.result()
            except Exception as e:row=dict(N=job['N'],kind=job['kind'],replicate=job['replicate'],seed=job['seed'],status='wrapper_failure',error=repr(e))
            results.append(row)
            if len(results)%2==0 or row['status']!='complete_verified_receipt':
                print(json.dumps(dict(completed=len(results),total=len(jobs),latest={k:v for k,v in row.items() if k!='receipt'})),flush=True)
                save(root/'PROGRESS.json',dict(completed=len(results),total=len(jobs),results=results))
    assert identity(manifest['binary']['path'])==manifest['binary']
    statuses={s:sum(x['status']==s for x in results) for s in sorted({x['status'] for x in results})}
    summary=dict(completed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),manifest=identity(manifest_path),
                 dispatch=identity(root/'DISPATCH.json'),statuses=statuses,rows=sorted(results,key=lambda x:(x['N'],x['kind'],x['replicate'])))
    save(root/'SUMMARY.json',summary);print(json.dumps(dict(statuses=statuses,summary=identity(root/'SUMMARY.json')),indent=2),flush=True)
    return 0 if statuses=={'complete_verified_receipt':16} else 1
if __name__=='__main__':raise SystemExit(main())
