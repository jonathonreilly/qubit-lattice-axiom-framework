"""Declared fixed-rate follow-up, with per-run geometry/FFT reconstruction.

Large lossless states live outside the source repository. No sampling rule
is modified here. All whole-realization statistics remain postprocessing.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor,as_completed
import argparse,datetime,hashlib,json,subprocess,time,traceback
import numpy as np

HERE=Path(__file__).resolve().parent
DEADLINE=datetime.datetime(2026,9,22,0,25,55,tzinfo=datetime.timezone.utc)
def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for block in iter(lambda:f.read(1<<20),b''):h.update(block)
    return h.hexdigest()
def now():return datetime.datetime.now(datetime.timezone.utc)

def verify_state(prefix,d):
    path=Path(str(prefix)+'.state.txt');N=d['N'];V=N**3
    with path.open() as f:headers=[next(f).rstrip('\n'),next(f).rstrip('\n')]
    assert headers==[f'N {N}','site partner identity births_at_site']
    rawhash=sha(path);a=np.loadtxt(path,skiprows=2,dtype=np.int32)
    assert a.shape==(V,4) and np.array_equal(a[:,0],np.arange(V))
    p=a[:,1];rid=a[:,2];births=a[:,3]
    assert d['full'] and np.all(p>=0) and np.all(p<V)
    assert np.array_equal(p[p],np.arange(V)) and np.array_equal(np.sort(rid),np.arange(V))
    assert np.all((rid^rid[p])==1) and int(births.sum())==V==2*d['birth_events']
    assert int(np.maximum(births-1,0).sum())==d['site_reuses'] and int(births.max())==d['max_site_births']
    assert np.all(births>=0) and births.max()<65536
    x=np.indices((N,N,N),dtype=np.int32).reshape(3,-1).T
    delta=(x[p]-x)%N
    assert np.all(np.minimum(delta,N-delta).sum(axis=1)==1)
    sigma=1-2*(x.sum(axis=1)%2);ni=np.zeros((V,3),dtype=np.int8)
    for i in range(3):
        y=x.copy();y[:,i]=(y[:,i]+1)%N;v=(y[:,0]*N+y[:,1])*N+y[:,2];ni[:,i]=(p==v)
    counts=ni.sum(axis=0);assert counts.tolist()==d['orientation_counts'] and np.all(counts%2==0)
    sixB=(sigma[:,None]*(6*ni-1)).reshape(N,N,N,3)
    div=sum(sixB[...,i]-np.roll(sixB[...,i],1,axis=i) for i in range(3))
    assert np.max(abs(div))==0
    wind=[]
    for i in range(3):
        planes=np.bincount(x[:,i],weights=sigma*ni[:,i],minlength=N)
        assert np.all(planes==planes[0]);wind.append(int(planes[0]))
    assert wind==d['winding']
    transform=np.fft.fftn(sixB/6.0,axes=(0,1,2),norm='ortho')
    error=0.;gauss=0.;shells={};individual=[]
    for item in d['modes']:
        ell=np.asarray(item['ell']);field=transform[tuple(ell%N)]
        normal=1-np.exp(-2j*np.pi*ell/N);q=normal@field
        longitudinal=abs(q)**2/np.vdot(normal,normal).real
        power=float(np.vdot(field,field).real);ST=float((power-longitudinal)/2)
        difference=max(abs(ST-item['transverse_per_polarization']),abs(power-item['power']))
        error=max(error,float(difference));gauss=max(gauss,float(abs(q)))
        assert difference<1e-8 and abs(q)<1e-9
        shells.setdefault(int(ell@ell),[]).append(ST)
        individual.append({'ell':ell.tolist(),'power':power,'transverse_per_polarization':ST})
    assert {k:len(v) for k,v in shells.items()}=={1:3,2:6,3:4,4:3}
    compact=Path(str(prefix)+'.state.npz')
    np.savez_compressed(compact,partner=p,identity=rid,births_at_site=births.astype(np.uint16))
    with np.load(compact,allow_pickle=False) as archive:
        assert np.array_equal(archive['partner'],p)
        assert np.array_equal(archive['identity'],rid)
        assert np.array_equal(archive['births_at_site'],births)
    certificate={'ASCII_sha256':rawhash,'ASCII_headers':headers,'ASCII_site_column':f'integers0..{V-1}',
                 'archive':compact.name,'archive_sha256':sha(compact),'archive_bytes':compact.stat().st_size,
                 'lossless_arrays_reopened_and_equal':True,'max_FFT_power_difference':error,
                 'max_FFT_Gauss_residual':gauss,'integer_Gauss_max_abs':0,
                 'shells':{str(k):float(np.mean(v)) for k,v in shells.items()},
                 'modes':individual,'winding_power_per_component':sum(w*w for w in wind)/(3*N),
                 'site_reuse_fraction':float(np.count_nonzero(births>1)/V)}
    Path(str(prefix)+'.verification.json').write_text(json.dumps(certificate,indent=2)+'\n')
    path.unlink() # Only the just-created redundant file, after lossless comparison.
    return certificate

def main():
    ap=argparse.ArgumentParser();ap.add_argument('executable',type=Path);ap.add_argument('output',type=Path)
    ap.add_argument('--pilot',action='store_true');args=ap.parse_args()
    exe=args.executable.resolve();out=args.output.resolve();out.mkdir(parents=True,exist_ok=False)
    if args.pilot:cases=[(N,b,210000000+10000*N+1000*j+999) for N in [4,16,32] for j,b in enumerate([.1,1,10])]
    else:cases=[(N,b,210000000+10000*N+1000*j+r) for N in [16,32,64,128] for j,b in enumerate([.1,1,10]) for r in range(1,(64 if N==128 else 256)+1)]
    assert len(set(s for N,b,s in cases))==len(cases)
    assert args.pilot or len(cases)==2496
    source=HERE/'geometric_partner_growth.cpp';protocol=HERE/'GEOMETRIC_FIXED_RATE_FOLLOWUP_PROTOCOL.md'
    manifest={'created_utc':now().isoformat(),'deadline_utc':DEADLINE.isoformat(),'pilot':args.pilot,
              'source_sha256':sha(source),'binary_sha256':sha(exe),'wrapper_sha256':sha(Path(__file__)),
              'protocol_sha256':sha(protocol),'cases':cases,'workers':2,'event_cap':1000000000,
              'projection_only':True,'kappa':1,'nu':0}
    assert manifest['source_sha256']=='5e24d66b068740dd58dd8aeb9d88f6cfc90238105b7266563bc37ecc2532b716'
    assert manifest['binary_sha256']=='ffc3e77cf1793b5acb6fdb792563ee13db11ed73a698b2652dbff79300b4f10d'
    (out/'MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
    def run(case):
        N,beta,seed=case;name=f'N{N}_b{beta}_s{seed}';prefix=out/name
        if now()>=DEADLINE:return {'name':name,'case':case,'status':'not_started_deadline'}
        cmd=[str(exe),str(N),str(seed),str(beta),'1','1000000000',str(prefix),'1' if args.pilot and N==4 else '0']
        started=time.monotonic();proc=subprocess.run(cmd,text=True,capture_output=True);wall=time.monotonic()-started
        Path(str(prefix)+'.stdout').write_text(proc.stdout);Path(str(prefix)+'.stderr').write_text(proc.stderr)
        receipt={'case':case,'command':cmd,'exit_code':proc.returncode,'process_wall_seconds':wall,'finished_utc':now().isoformat()}
        status='failed';verification=None;d={};failure=None
        if proc.returncode==0:
            d=json.loads(Path(str(prefix)+'.json').read_text())
            if d['full']:
                try:verification=verify_state(prefix,d);status='full_verified'
                except Exception as error:
                    failure=repr(error);status='verification_failed'
                    Path(str(prefix)+'.verification.stderr').write_text(traceback.format_exc())
            else:status='event_cap_censored'
        receipt.update(status=status,verification_error=failure,files={})
        for suffix in ['.csv','.json','.state.txt','.state.npz','.verification.json','.verification.stderr','.stdout','.stderr']:
            f=Path(str(prefix)+suffix)
            if f.exists():receipt['files'][f.name]=sha(f)
        Path(str(prefix)+'.receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
        fields={k:d[k] for k in ['N','beta','seed','time','events','slide_events','site_reuses','max_site_births','winding'] if k in d}
        answer={'name':name,'case':case,'status':status,'process_wall_seconds':wall,'total_wall_seconds':time.monotonic()-started,**fields}
        if verification:answer.update({k:verification[k] for k in ['shells','winding_power_per_component','max_FFT_power_difference','max_FFT_Gauss_residual','archive_bytes','site_reuse_fraction']})
        if failure:answer['verification_error']=failure
        return answer
    results=[]
    with ThreadPoolExecutor(max_workers=2) as pool:
        futures={pool.submit(run,case):case for case in cases}
        for future in as_completed(futures):
            try:row=future.result()
            except Exception as error:row={'case':futures[future],'status':'wrapper_exception','error':repr(error),'traceback':traceback.format_exc()}
            results.append(row);print(json.dumps(row),flush=True)
            if len(results)%32==0:
                (out/'PROGRESS.json').write_text(json.dumps({'completed':len(results),'declared':len(cases),'status_counts':{s:sum(r['status']==s for r in results) for s in sorted(set(r['status'] for r in results))},'updated_utc':now().isoformat()},indent=2)+'\n')
    assert sha(source)==manifest['source_sha256'] and sha(exe)==manifest['binary_sha256']
    summary={'manifest':manifest,'results':sorted(results,key=lambda r:r['case']),
             'all_full_verified':all(r['status']=='full_verified' for r in results),
             'total_process_seconds':sum(r.get('process_wall_seconds',0) for r in results),
             'status_counts':{s:sum(r['status']==s for r in results) for s in sorted(set(r['status'] for r in results))}}
    (out/'SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps({k:summary[k] for k in ['all_full_verified','total_process_seconds','status_counts']}),flush=True)
    if any(r['status'] in ['failed','verification_failed','wrapper_exception'] for r in results):raise SystemExit(1)

if __name__=='__main__':main()
