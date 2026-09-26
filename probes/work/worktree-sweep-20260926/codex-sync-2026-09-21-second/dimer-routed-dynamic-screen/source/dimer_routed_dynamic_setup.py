#!/usr/bin/env python3
"""Freeze geometric inputs and run preproduction decoder/DFT controls."""
from pathlib import Path
import datetime,hashlib,json,platform,subprocess,sys,time
import numpy as np

HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,x):Path(p).write_text(json.dumps(x,indent=2,allow_nan=False)+'\n')
def identity(p):p=Path(p);return dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p))
def execute(command,prefix):
    start=time.time();proc=subprocess.run(list(map(str,command)),capture_output=True)
    Path(str(prefix)+'.stdout').write_bytes(proc.stdout);Path(str(prefix)+'.stderr').write_bytes(proc.stderr)
    receipt=dict(command=list(map(str,command)),started_unix=start,seconds=time.time()-start,exit_code=proc.returncode,
                 stdout_sha256=hashlib.sha256(proc.stdout).hexdigest(),stderr_sha256=hashlib.sha256(proc.stderr).hexdigest())
    save(str(prefix)+'.receipt.json',receipt)
    assert proc.returncode==0,(command,proc.stderr.decode());assert not proc.stderr
    return json.loads(proc.stdout),receipt

def decode_geometry(path):
    data=Path(path).read_bytes();assert data[:8]==b'DRPAIR01'
    N=int(np.frombuffer(data,dtype='<u4',count=1,offset=8)[0]);V=N**3;K=V//2
    p=np.frombuffer(data,dtype='<u4',offset=12).copy();assert len(p)==V and np.all(p<V)
    ar=np.arange(V,dtype=np.int64);assert np.array_equal(p[p],ar)
    xyz=np.stack(np.unravel_index(ar,(N,N,N)),axis=1).astype(np.int32)
    disp=(xyz[p]-xyz+N//2)%N-N//2;assert np.all(np.sum(abs(disp),axis=1)==1)
    black=np.flatnonzero(xyz.sum(axis=1)%2==0);white=p[black]
    owner=np.full(V,-1,dtype=np.int64);owner[white]=np.arange(K)
    channels=0;minimum_progress=2
    for delta in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
        d=np.array(delta,dtype=int);target=(xyz[black]+d)%N
        site=np.ravel_multi_index(tuple(target.T),(N,N,N));q=owner[site]
        assert np.array_equal(np.sort(q),np.arange(K))
        step=d-disp[black[q]]
        assert np.array_equal((xyz[black]+step)%N,xyz[black[q]])
        moving=q!=np.arange(K);progress=step[moving]@d
        assert np.all((progress>=1)&(progress<=2))
        if len(progress):minimum_progress=min(minimum_progress,int(progress.min()))
        inv=np.argsort(q);assert np.all(inv[moving]!=q[q[moving]])
        channels+=int(moving.sum())
    assert channels==5*K
    return N,p,black,xyz[black],dict(N=N,pairs=K,channels=channels,minimum_forward_progress=minimum_progress,
                                     matching_and_route_permutations_verified=True,source=identity(path))

def features():
    e=np.array([(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]+[(0,0,0)]*8)
    b=np.array([(0,0,0)]*6+[(x,y,z) for x in [-1,1] for y in [-1,1] for z in [-1,1]])
    return np.hstack((e,b))
def dft(colors,xyz,N):
    out=[]
    for j in range(3):
        phase=np.exp(-2j*np.pi*xyz[:,j]/N)
        totals=np.bincount(colors,weights=phase.real,minlength=14)+1j*np.bincount(colors,weights=phase.imag,minlength=14)
        out.append(totals@features()/np.sqrt(len(colors)))
    return np.array(out)

MASK=(1<<64)-1
def rng_first_colors(seed,count):
    state=[]
    for _ in range(4):
        seed=(seed+0x9e3779b97f4a7c15)&MASK;z=seed
        z=((z^(z>>30))*0xbf58476d1ce4e5b9)&MASK;z=((z^(z>>27))*0x94d049bb133111eb)&MASK
        state.append(z^(z>>31))
    rot=lambda x,k:((x<<k)|(x>>(64-k)))&MASK
    answer=[]
    while len(answer)<count:
        result=(rot((state[1]*5)&MASK,7)*9)&MASK;t=(state[1]<<17)&MASK
        state[2]^=state[0];state[3]^=state[1];state[1]^=state[2];state[0]^=state[3];state[2]^=t;state[3]=rot(state[3],45)
        if result>=((1<<64)%14):answer.append(result%14)
    return np.array(answer,dtype=np.uint8)

def check_state(result_path,geometry):
    result=json.loads(Path(result_path).read_text());N,p,black,xyz=geometry[:4];K=len(black)
    raw=Path(str(result_path)+'.state').read_bytes();assert raw[:8]==b'DRSTATE1'
    assert int(np.frombuffer(raw,dtype='<u4',count=1,offset=8)[0])==N
    keys=np.frombuffer(raw,dtype='<u4',count=K,offset=12);colors=np.frombuffer(raw,dtype=np.uint8,offset=12+4*K)
    assert len(colors)==K and np.all(colors<14);assert np.array_equal(np.sort(keys),np.arange(K))
    assert np.array_equal(colors[:32],rng_first_colors(result['seed'],32))
    assert np.array_equal(np.bincount(colors,minlength=14),result['color_counts'])
    assert np.array_equal(np.bincount(colors[keys],minlength=14),result['color_counts'])
    errors=[]
    for i,arr in [(0,colors),(-1,colors[keys])]:
        expected=dft(arr,xyz,N);stored=np.array(result['snapshots'][i]['fields']);stored=stored[:,:,0]+1j*stored[:,:,1]
        error=float(np.max(abs(stored-expected)));assert error<1e-8;errors.append(error)
    assert result['key_permutation_verified'] and result['counts_verified']
    return dict(N=N,seed=result['seed'],initial_and_final_DFT_errors=errors,
                initial_32_color_RNG_replay=True,whole_state_permutation_and_counts=True,
                output=identity(result_path),state=identity(str(result_path)+'.state'))

def main():
    root=Path(sys.argv[1]).resolve();binary=Path(sys.argv[2]).resolve();root.mkdir(exist_ok=False)
    (root/'geometry').mkdir();(root/'validation').mkdir();(root/'histories').mkdir()
    assert sys.byteorder=='little'
    geometry_rows=[];decoded={}
    for N in [16,32,64,128]:
        for kind in ['winding','irregular']:
            path=root/'geometry'/f'N{N}_{kind}.bin';seed=29121000+N+(1000 if kind=='irregular' else 0)
            output,receipt=execute([binary,'geometry',N,kind,seed,path],root/'geometry'/f'N{N}_{kind}')
            data=decode_geometry(path)
            if kind=='irregular':assert output['accepted_flips']>0
            geometry_rows.append(dict(N=N,kind=kind,seed=seed,file=identity(path),generator=output,
                                      independent_decoder=data[-1],command_receipt=receipt))
            if N in [16,128]:decoded[(N,kind)]=data
            print('geometry verified',N,kind,flush=True)
    validations=[];benchmarks=[]
    for N,kind,rep in [(16,'winding',r) for r in range(4)]+[(16,'irregular',r) for r in range(4)]+[(128,'irregular',0)]:
        seed=202609218000+100*N+rep;path=root/'validation'/f'N{N}_{kind}_{rep}.json'
        geom=root/'geometry'/f'N{N}_{kind}.bin'
        output,receipt=execute([binary,'validate',geom,seed,path],path)
        validations.append(check_state(path,decoded[(N,kind)]))
        benchmarks.append(dict(N=N,kind=kind,seed=seed,attempts=output['attempts'],seconds=output['wall_seconds']))
        print('state/DFT/RNG verified',N,kind,rep,flush=True)
    jobs=[]
    for size_index,(N,reps) in enumerate([(16,256),(32,128),(64,64),(128,32)]):
        for kind_index,kind in enumerate(['winding','irregular']):
            for rep in range(reps):
                seed=202609211810+100000*size_index+10000*kind_index+rep
                path=root/'histories'/f'N{N}_{kind}_r{rep+1:03}.json'
                jobs.append(dict(N=N,kind=kind,replicate=rep+1,seed=seed,output=str(path),
                                 command=[str(binary),'run',str(root/'geometry'/f'N{N}_{kind}.bin'),str(seed),str(path)]))
    assert len(jobs)==960 and len({x['seed'] for x in jobs})==960
    manifest=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  protocol=identity(HERE/'DIMER_ROUTED_DYNAMIC_SCREEN_PROTOCOL.md'),
                  construction=identity(HERE/'DIMER_ROUTED_RECORD_TRANSPORT.md'),
                  source=identity(HERE/'dimer_routed_dynamics.cpp'),setup=identity(__file__),binary=identity(binary),
                  platform=dict(system=platform.platform(),python=sys.version),geometry=geometry_rows,
                  validation=validations,benchmarks=benchmarks,jobs=jobs,
                  scope='Frozen before production dispatch. Decoder/initial RNG/final states/DFTs checked; no full random-clock trajectory replay claimed.')
    save(root/'MANIFEST.json',manifest)
    save(HERE/'DIMER_ROUTED_DYNAMIC_SETUP_RECEIPT.json',dict(manifest=identity(root/'MANIFEST.json'),
         geometry_count=len(geometry_rows),validation_count=len(validations),histories=len(jobs),benchmarks=benchmarks,
         max_DFT_error=max(max(x['initial_and_final_DFT_errors']) for x in validations),
         production_dispatched=False))
    print(json.dumps(dict(manifest=identity(root/'MANIFEST.json'),histories=len(jobs),benchmarks=benchmarks),indent=2))

if __name__=='__main__':main()
