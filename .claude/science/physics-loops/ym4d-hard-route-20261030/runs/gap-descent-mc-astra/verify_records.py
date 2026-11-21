"""Raw archive integrity plus a separate 2x2-complex-matrix geometry check.
Run serially after sampling. No check discharges a scientific statement.
"""
import hashlib
import gzip
import json
from pathlib import Path
import sys
import numpy as np
from analyze import memory_gate
HERE=Path(__file__).resolve().parent
scratch=Path(sys.argv[1])
m=json.loads((HERE/'manifest.json').read_text());rows=[]
assert hashlib.sha256((HERE/'su2.cpp').read_bytes()).hexdigest()==m['source_sha256']
extra=json.loads((HERE/'extra_manifest.json').read_text())
assert extra['source_sha256']==m['source_sha256']
for j in m['jobs']+extra['jobs']:
    tag=f"L{j['L']}_b{j['beta']:.1f}_{j['mult']}_c{j['chain']}"
    r=json.loads((HERE/(tag+'.json')).read_text());p=HERE/(tag+'.npz')
    z=np.load(p);a=z['records']
    assert hashlib.sha256(p.read_bytes()).hexdigest()==r['archive_sha256']
    assert hashlib.sha256(a.tobytes()).hexdigest()==r['raw_sha256']
    assert a.shape==(j['n'],54*j['L']+24) and np.isfinite(a).all()
    assert np.max(np.abs(a))<=1.00001
    if j['mult']=='anchor':
        spin=z['spin'];assert spin.shape==(j['n'],j['L']//2+1) and np.isfinite(spin).all()
        assert np.max(np.abs(spin))<=1.00001 and np.max(np.abs(spin[:,0]-1))<1e-6
    rows.append(dict(tag=tag,records=len(a),complete=True))
    memory_gate()
checks=[]
for tag in ('L8_b2.4_1_c1','L12_b2.5_8_c1','L12_b2.4_face_c1','L16_b2.5_1_c1'):
    L=int(tag.split('_')[0][1:]);V=L**4
    q=np.fromfile(scratch/(tag+'.cfg'),dtype='<f8').reshape(V,4,4)
    # Homomorphism q -> q0 I - i q_j sigma_j for the +cross convention.
    U=np.empty((V,4,2,2),complex)
    U[:,:,0,0]=q[:,:,0]-1j*q[:,:,3];U[:,:,1,1]=q[:,:,0]+1j*q[:,:,3]
    U[:,:,0,1]=-q[:,:,2]-1j*q[:,:,1];U[:,:,1,0]=q[:,:,2]-1j*q[:,:,1]
    x=np.arange(V);neigh=np.empty((V,4),int)
    for d in range(4):
        st=L**d;c=(x//st)%L;neigh[:,d]=x+np.where(c==L-1,-(L-1)*st,st)
    def rect(mu,nu,r,s):
        y=x.copy();z=np.broadcast_to(np.eye(2,dtype=complex),(V,2,2)).copy()
        for d,n,sign in ((mu,r,1),(nu,s,1),(mu,r,-1),(nu,s,-1)):
            for _ in range(n):
                if sign>0:z=z@U[y,d];y=neigh[y,d]
                else:
                    st=L**d;c=(y//st)%L;y=y+np.where(c==0,(L-1)*st,-st)
                    z=z@U[y,d].conj().transpose(0,2,1)
        return np.trace(z,axis1=1,axis2=2).real.mean()/2
    exact=np.array([rect(mu,nu,r,s) for mu in range(4) for nu in range(mu+1,4) for r,s in ((1,1),(1,2),(2,1),(2,2))])
    saved=np.load(HERE/(tag+'.npz'))['records'][-1,48*L:48*L+24]
    error=float(np.max(np.abs(exact-saved)));assert error<4e-8
    checks.append(dict(tag=tag,matrix_loop_max_error=error,unitarity_max_error=float(np.max(np.abs((q*q).sum(axis=2)-1)))))
    memory_gate()
o4=[]
for beta in (2.3,2.4,2.5):
    for L in (8,12,128):
        for chain in (0,1):
            tag=f'o4_L{L}_b{beta:.1f}_c{chain}'
            p=HERE/(tag+'.csv.gz');r=json.loads((HERE/(tag+'.json')).read_text())
            assert hashlib.sha256(p.read_bytes()).hexdigest()==r['archive_sha256']
            raw=gzip.decompress(p.read_bytes())
            assert hashlib.sha256(raw).hexdigest()==r['sha256']
            assert len(raw.splitlines())==8193
            assert hashlib.sha256((HERE/'o4_control.cpp').read_bytes()).hexdigest()==r['source_sha256']
            assert r['su2_sha256']==m['source_sha256']
            a=np.loadtxt(p,delimiter=',',skiprows=1)
            columns=3+L//2+1+(L//2+1 if L<=12 else 0)
            assert a.shape==(8192,columns) and np.isfinite(a).all()
            assert np.max(np.abs(a[:,0]))<=1.00001 and np.min(a[:,1:3])>=0
            assert np.max(np.abs(a[:,3:]))<=1.00001
            o4.append(dict(tag=tag,records=8192,complete=True))
            memory_gate()
repair=json.loads((HERE/'serial_reproduction.json').read_text())
old=json.loads((HERE/repair['original_receipt']).read_text())
current=json.loads((HERE/(repair['tag']+'.json')).read_text())
assert old['raw_sha256']==current['raw_sha256']==repair['raw_sha256']
assert current['serial_reproduction'] is True
out=dict(archives=rows,o4_archives=o4,matrix_checks=checks,source_hash_matches=True,
    finite_and_bounded_records=True,serial_reproduction_matches=True)
(HERE/'record_verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(archives=len(rows),o4_archives=len(o4),matrix_checks=checks,source_hash_matches=True)))
