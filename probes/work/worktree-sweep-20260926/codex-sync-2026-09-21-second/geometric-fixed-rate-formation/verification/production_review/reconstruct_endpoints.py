#!/usr/bin/env python3
"""Read only the preselected NPZ arrays; no author observable outputs/imports."""
from pathlib import Path
import datetime,hashlib,json,math,time
import numpy as np
HERE=Path(__file__).resolve().parent
def file_identity(path):
    path=Path(path);h=hashlib.sha256()
    with path.open('rb') as handle:
        for b in iter(lambda:handle.read(1<<20),b''):h.update(b)
    return {'path':str(path),'bytes':path.stat().st_size,'sha256':h.hexdigest()}
def save(name,data): (HERE/name).write_text(json.dumps(data,indent=2,allow_nan=False)+'\n')
def reconstruct(row,modes):
    path=Path(row['archive']);N=row['N'];V=N**3
    with np.load(path,allow_pickle=False) as archive:
        assert set(archive.files)=={'partner','identity','births_at_site'}
        p=archive['partner'];rid=archive['identity'];birth=archive['births_at_site']
    assert p.shape==rid.shape==birth.shape==(V,)
    assert p.dtype==rid.dtype==np.dtype('int32') and birth.dtype==np.dtype('uint16')
    assert all(a.flags.c_contiguous for a in [p,rid,birth])
    index=np.arange(V,dtype=np.int64)
    assert np.all((0<=p)&(p<V)) and np.all(p!=index)
    assert np.array_equal(p[p],index)
    assert np.all((0<=rid)&(rid<V)) and np.all(np.bincount(rid,minlength=V)==1)
    assert np.all(np.bitwise_xor(rid,rid[p])==1)
    coords=[index//(N*N),(index//N)%N,index%N]
    distance=np.zeros(V,dtype=np.int16)
    for c in coords:
        diff=(c[p]-c)%N;distance+=np.minimum(diff,N-diff).astype(np.int16)
    assert np.all(distance==1)
    assert int(birth.sum(dtype=np.uint64))==V
    histogram=np.bincount(birth.astype(np.int64))
    reuse=sum((count-1)*int(number) for count,number in enumerate(histogram) if count>1)
    fraction=float(np.count_nonzero(birth>1)/V)
    sigma=(1-2*((coords[0]+coords[1]+coords[2])%2)).astype(np.int8)
    positive=[]
    for axis,stride in enumerate([N*N,N,1]):
        target=index+stride*(((coords[axis]+1)%N)-coords[axis])
        positive.append((p==target).astype(np.int8))
    counts=[int(q.sum()) for q in positive]
    assert sum(counts)==V//2 and all(c%2==0 for c in counts)
    Q=np.stack([sigma*(6*q-1) for q in positive],axis=1).reshape(N,N,N,3)
    divergence=np.zeros((N,N,N),dtype=np.int16)
    for axis in range(3):divergence+=Q[...,axis]-np.roll(Q[...,axis],1,axis=axis)
    assert not np.any(divergence)
    planes=[];winds=[]
    for axis in range(3):
        q=(sigma*positive[axis]).reshape(N,N,N)
        other_axes=tuple(i for i in range(3) if i!=axis)
        flux=q.sum(axis=other_axes,dtype=np.int64)
        assert np.all(flux==flux[0]);wind=int(flux[0]);winds.append(wind);planes.append(flux.tolist())
        assert int(Q[...,axis].sum(dtype=np.int64))==6*N*wind
    # Direct separable DFT: precontract only the needed z-frequencies, then y,x.
    phases={k:np.exp((-2j*np.pi*k/N)*np.arange(N)) for k in range(-2,3)}
    zpartials={k:np.einsum('z,xyzi->xyi',phases[k],Q,optimize=True) for k in sorted({m[2] for m in modes})}
    yzpartials={}
    mode_rows=[];shells={k:[] for k in [1,2,3,4]}
    for ell in modes:
        xk,yk,zk=ell
        if (yk,zk) not in yzpartials:
            yzpartials[yk,zk]=np.einsum('y,xyi->xi',phases[yk],zpartials[zk],optimize=True)
        z=np.einsum('x,xi->i',phases[xk],yzpartials[yk,zk],optimize=True)/(6*math.sqrt(V))
        d=1-np.exp(-2j*np.pi*np.asarray(ell)/N)
        charge=sum(d[i]*z[i] for i in range(3))
        power=math.fsum(float(abs(w)**2) for w in z)
        longitudinal=float(abs(charge)**2/math.fsum(float(abs(w)**2) for w in d))
        transverse=(power-longitudinal)/2
        assert abs(charge)<1e-9 and transverse>=-1e-14
        square=sum(k*k for k in ell);shells[square].append(transverse)
        mode_rows.append({'ell':ell,'field_real':[float(w.real) for w in z],'field_imag':[float(w.imag) for w in z],
                          'power':power,'longitudinal':longitudinal,'transverse_per_polarization':transverse,'gauss_residual':float(abs(charge))})
    assert {k:len(v) for k,v in shells.items()}=={1:3,2:6,3:4,4:3}
    # Reconstruct the original ASCII byte stream in memory-bounded chunks.
    ah=hashlib.sha256();ah.update(f'N {N}\nsite partner identity births_at_site\n'.encode())
    for start in range(0,V,16384):
        ah.update(''.join(f'{u} {int(p[u])} {int(rid[u])} {int(birth[u])}\n' for u in range(start,min(V,start+16384))).encode())
    return {'selection':row,'archive':file_identity(path),'array_sha256':{name:hashlib.sha256(memoryview(a)).hexdigest() for name,a in [('partner',p),('identity',rid),('births_at_site',birth)]},
            'ASCII_reconstruction_sha256':ah.hexdigest(),'sites':V,'record_ids_permutation':True,'reciprocal_NN_antipodal_ID_pairing':True,
            'birth_budget':int(birth.sum(dtype=np.uint64)),'birth_histogram':histogram.tolist(),'site_reuses':reuse,'max_site_births':int(birth.max()),
            'site_reuse_fraction':fraction,'orientation_counts':counts,'integer_Gauss_max_abs':int(np.max(abs(divergence))),
            'plane_fluxes':planes,'winding':winds,'winding_power_per_component':sum(w*w for w in winds)/(3*N),
            'modes':mode_rows,'shells':{str(k):math.fsum(v)/len(v) for k,v in shells.items()},
            'axis_mode_square':math.fsum(x*x for x in shells[1])/3}

if __name__=='__main__':
    assert not (HERE/'ENDPOINT_RECONSTRUCTION.json').exists()
    selection=json.loads((HERE/'SELECTION.json').read_text())
    declared=json.loads((HERE/'SELECTION_SEAL.json').read_text())
    for row in declared['artifacts']:
        assert file_identity(row['path'])==row
    start=time.monotonic();rows=[]
    for row in selection['selected_endpoints']:
        rows.append(reconstruct(row,selection['declared_modes']))
        print('reconstructed',row['name'],'endpoint',len(rows),'of',len(selection['selected_endpoints']),flush=True)
    save('ENDPOINT_RECONSTRUCTION.json',{'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'read_boundary':'Only preselected NPZ physical arrays opened; stored summaries, certificates and observable tables remain unread.',
        'method':'Integer reconstruction and direct separable DFT, without author helper imports.','rows':rows,'elapsed_seconds':time.monotonic()-start,
        'checker':file_identity(Path(__file__))})
    print('All24 endpoints reconstructed; stored output comparison not yet performed.',flush=True)
