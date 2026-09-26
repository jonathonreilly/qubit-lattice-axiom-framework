"""Independent binary/key/Fourier decoder, with no author Python imports."""
from pathlib import Path
from itertools import product
import struct, hashlib
import numpy as np

FEATURE=np.array([tuple(s if j==i else 0 for j in range(3))+(0,0,0)
                  for i in range(3) for s in [1,-1]]+
                 [(0,0,0)+b for b in product([-1,1],repeat=3)],dtype=np.int64)
DIRECTIONS=FEATURE[:6,:3]
MASK=2**64-1

def identity(path):
    p=Path(path);d=p.read_bytes()
    return {'path':str(p),'bytes':len(d),'sha256':hashlib.sha256(d).hexdigest()}

def seeded_colors(seed,k):
    # Separate integer transcription of splitmix seeding + xoshiro256**;
    # only initial color draws, not Poisson clocks or the dynamic trajectory.
    words=[]
    for step in range(1,5):
        z=(seed+step*0x9e3779b97f4a7c15)&MASK
        z=((z ^ (z>>30))*0xbf58476d1ce4e5b9)&MASK
        z=((z ^ (z>>27))*0x94d049bb133111eb)&MASK
        words.append(z ^ (z>>31))
    def rotate(z,n): return ((z<<n)&MASK) | (z>>(64-n))
    result=np.empty(k,dtype=np.uint8);i=0;rejected=0
    while i<k:
        a,b,c,d=words
        output=(rotate((5*b)&MASK,7)*9)&MASK
        words=[a ^ d ^ b, b ^ c ^ a, c ^ a ^ ((b<<17)&MASK), rotate(d ^ b,45)]
        if output < 2**64%14:
            rejected+=1;continue
        result[i]=output%14;i+=1
    return result,rejected

def decode_geometry(path,check_routes=True):
    data=Path(path).read_bytes();assert data[:8]==b'DRPAIR01'
    n=struct.unpack_from('<I',data,8)[0];v=n**3;k=v//2
    assert n>=8 and n%2==0 and len(data)==12+4*v
    partner=np.frombuffer(data,offset=12,dtype='<u4').astype(np.int64)
    sites=np.arange(v);assert np.all(partner<v) and np.array_equal(partner[partner],sites)
    xyz=np.column_stack((sites//(n*n),(sites//n)%n,sites%n))
    distance=np.minimum((xyz[partner]-xyz)%n,(xyz-xyz[partner])%n)
    assert np.all(distance.sum(axis=1)==1)
    black=sites[(xyz.sum(axis=1)&1)==0];white=partner[black]
    assert len(black)==k and len(np.unique(white))==k
    owner=np.full(v,-1,dtype=np.int64);owner[black]=np.arange(k);owner[white]=np.arange(k)
    rows=[];catalog=[]
    if check_routes:
        d=(xyz[white]-xyz[black]+n//2)%n-n//2
        for j,delta in enumerate(DIRECTIONS):
            target=(xyz[black]+delta)%n;targetid=target[:,0]*n*n+target[:,1]*n+target[:,2]
            q=owner[targetid];assert np.array_equal(np.sort(q),np.arange(k))
            inv=np.empty(k,dtype=np.int64);inv[q]=np.arange(k)
            moving=np.flatnonzero(q!=np.arange(k));right=q[q[moving]]
            footprints=np.column_stack((inv[moving],moving,q[moving],right))
            assert np.all(np.diff(np.sort(footprints,axis=1),axis=1)>0)
            unwrapped=delta-d[q[moving]]
            assert np.all(np.sum(abs(unwrapped),axis=1)==2)
            assert np.all((unwrapped@delta>=1)&(unwrapped@delta<=2))
            assert np.array_equal((xyz[black[moving]]+unwrapped)%n,xyz[black[q[moving]]])
            rows.append({'direction':delta.tolist(),'moving_channels':len(moving)})
            # Only keep all rows for small fixture checks.
            if n<=8:
                catalog.extend((int(l),int(u),int(w),int(r),j//2,1 if j%2==0 else -1)
                               for l,u,w,r in footprints)
        assert sum(x['moving_channels'] for x in rows)==5*k
    return {'N':n,'K':k,'partner':partner,'black':black,'white':white,'xyz':xyz[black],
            'route_summary':rows,'catalog':catalog,'identity':identity(path)}

def read_state(path,n):
    data=Path(path).read_bytes();k=n**3//2
    assert data[:8]==b'DRSTATE1' and struct.unpack_from('<I',data,8)[0]==n
    assert len(data)==12+5*k
    keys=np.frombuffer(data,offset=12,count=k,dtype='<u4').astype(np.int64)
    colors=np.frombuffer(data,offset=12+4*k,count=k,dtype=np.uint8)
    assert np.array_equal(np.sort(keys),np.arange(k)) and np.all(colors<14)
    return keys,colors

def reconstruct_fields(colors,xyz,n):
    # Integer coordinate/color histograms followed by a 1D FFT, unlike the
    # simulator's sitewise complex summation and the author's phase-weighted
    # color bincount. No stored Fourier values are arguments to this function.
    answer=[]
    for axis in range(3):
        hist=np.bincount(xyz[:,axis]*14+colors,minlength=n*14).reshape(n,14)
        profile=hist@FEATURE
        answer.append(np.fft.fft(profile,axis=0)[1]/np.sqrt(len(colors)))
    return np.array(answer)

def as_json_complex(a):return np.stack((a.real,a.imag),axis=-1).tolist()

def verify_physical_keys(geometry,keys):
    k=geometry['K'];record=np.empty(2*k,dtype=np.int64)
    record[geometry['black']]=2*keys;record[geometry['white']]=2*keys+1
    assert np.array_equal(np.sort(record),np.arange(2*k))
    assert np.array_equal(record[geometry['partner']],record ^ 1)
    return {'whole_pair_record_ids':2*k,'all_record_ids_distinct':True,
            'geometric_partner_equals_antipodal_record_partner':True,
            'black_white_record_roles_conserved':True}
