"""Independent periodic cubic cochain and transverse-symbol controls."""
from pathlib import Path
from itertools import product
from datetime import datetime, timezone
import hashlib
import json
import numpy as np

HERE=Path(__file__).resolve().parent


def rank_mod(a,p=1009):
    a=np.asarray(a,dtype=np.int64).copy()%p
    nr,nc=a.shape;r=0
    for c in range(nc):
        inds=np.flatnonzero(a[r:,c])
        if not len(inds):continue
        j=r+int(inds[0]);a[[r,j]]=a[[j,r]]
        a[r]=(a[r]*pow(int(a[r,c]),p-2,p))%p
        rows=np.flatnonzero(a[r+1:,c])+r+1
        if len(rows):a[rows]=(a[rows]-a[rows,c,None]*a[r,None,:])%p
        r+=1
        if r==nr:break
    return r


def cubic(n):
    vertices=list(product(range(n),repeat=3));idx={x:i for i,x in enumerate(vertices)}
    edges=[(x,i) for x in vertices for i in range(3)]
    ei={e:j for j,e in enumerate(edges)}
    faces=[(x,i,j) for x in vertices for i in range(3) for j in range(i+1,3)]
    def shift(x,i):
        z=list(x);z[i]=(z[i]+1)%n;return tuple(z)
    d=np.zeros((len(edges),len(vertices)),dtype=np.int64)
    c=np.zeros((len(faces),len(edges)),dtype=np.int64)
    for row,(x,i) in enumerate(edges):
        d[row,idx[x]]=-1;d[row,idx[shift(x,i)]]=1
    for row,(x,i,j) in enumerate(faces):
        c[row,ei[x,i]]=1;c[row,ei[shift(x,i),j]]=1
        c[row,ei[shift(x,j),i]]=-1;c[row,ei[x,j]]=-1
    harmonic=np.array([[int(i==j) for j in range(3)] for x,i in edges],dtype=np.int64)
    assert np.array_equal(c@d,np.zeros((len(faces),len(vertices)),dtype=np.int64))
    assert np.array_equal(c@harmonic,np.zeros((len(faces),3),dtype=np.int64))
    return vertices,edges,faces,d,c,harmonic


def run(n):
    vertices,edges,faces,d,c,harmonic=cubic(n);v=len(vertices)
    rd=rank_mod(d);rc=rank_mod(c);rn=rank_mod(np.column_stack((d,harmonic)))
    assert rd==v-1 and rc==2*v-2 and rn==v+2
    b=c.T@c
    numeric=np.linalg.eigvalsh(b.astype(float))
    expected=[0.]*(v+2)
    for m in product(range(n),repeat=3):
        if m==(0,0,0):continue
        val=4*sum(np.sin(np.pi*mi/n)**2 for mi in m)
        expected.extend([val,val])
    err=float(np.max(np.abs(numeric-np.sort(expected))))
    assert err<1e-10
    modes=[]
    for m in [(0,0,0),(1,0,0),(1,2,-1),(n//2,0,1)]:
        k=2*np.pi*np.array(m)/n;kh=2*np.sin(k/2)
        a=np.array([1+2j,3-1j,-2+.5j])
        q=np.array([np.exp(1j*k@(np.array(x)+np.eye(3)[i]/2))*a[i] for x,i in edges])
        wanta=(kh@kh)*a-kh*(kh@a)
        want=np.array([np.exp(1j*k@(np.array(x)+np.eye(3)[i]/2))*wanta[i] for x,i in edges])
        symbol_error=float(np.max(np.abs(b@q-want)))
        assert symbol_error<1e-10
        # Direct face-centered curl phase, to test orientation as well.
        wantc=np.array([np.exp(1j*k@(np.array(x)+(np.eye(3)[i]+np.eye(3)[j])/2))*
                       1j*(kh[i]*a[j]-kh[j]*a[i]) for x,i,j in faces])
        curl_error=float(np.max(np.abs(c@q-wantc)))
        assert curl_error<1e-10
        modes.append({'mode':m,'lambda':float(kh@kh),'curl_symbol_error':curl_error,
                      'curl_square_symbol_error':symbol_error})
    return {'side':n,'vertices':v,'links':len(edges),'plaquettes':len(faces),
            'prime':1009,'gradient_rank_mod_prime':rd,'curl_rank_mod_prime':rc,
            'gradient_plus_harmonic_rank_mod_prime':rn,
            'exact_real_rank_certificate':'Integer modular lower bound equals the upper bound from the connected gradient and three independent constant directions.',
            'real_coexact_dimension':2*v-2,'full_curl_square_nullity':v+2,
            'full_spectrum_error':err,'largest_eigenvalue':float(numeric[-1]),
            'mode_checks':modes}


def continuum_controls():
    c=1.7;length=2.3;m=np.array([1,2,-1])
    target=c*np.linalg.norm(2*np.pi*m/length);rows=[]
    for n in (12,24,48,96):
        a=length/n;k=2*np.pi*m/n;kh=2*np.sin(k/2)
        omega=c*np.linalg.norm(kh)/a
        project=np.eye(3)-np.outer(kh,kh)/(kh@kh)
        target_project=np.eye(3)-np.outer(m,m)/(m@m)
        rows.append({'side':n,'spacing':a,'omega0':c/(2*a),'frequency':omega,
                     'frequency_error':target-omega,
                     'error_divided_by_spacing_squared':(target-omega)/a**2,
                     'projector_error':float(np.linalg.norm(project-target_project,ord=2))})
    assert all(rows[j+1]['frequency_error']<rows[j]['frequency_error'] for j in range(3))
    return {'physical_side':length,'speed':c,'fixed_mode':m.tolist(),
            'continuum_frequency':target,'rows':rows,
            'scope':'Only a fixed nonzero Fourier mode and fixed physical box; no infinite-volume or phase assertion.'}


out={'created_utc':datetime.now(timezone.utc).isoformat(),'status':'PASS',
     'cubic_controls':[run(n) for n in (3,4,6)],
     'finite_mode_continuum':continuum_controls(),
     'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'limits':'Exact integer incidence identities and rank certificates plus floating spectral controls. The all-size quotient and finite-time bounds are proved in the report, not inferred from these cases.'}
text=json.dumps(out,indent=2)+'\n';(HERE/'INCIDENCE_RESULTS.json').write_text(text);print(text,end='')
