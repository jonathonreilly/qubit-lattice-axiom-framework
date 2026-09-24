"""Compact matrix-band packet control, separate from a full cubic Gauss model."""

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('scripts/charged_band_packet_check.py',)
from pathlib import Path
from itertools import combinations
from datetime import datetime,timezone
import hashlib,json,math
import sympy as s
import numpy as np
from scipy.sparse import coo_matrix,eye
from scipy.sparse.linalg import expm_multiply

HERE=Path(__file__).resolve().parent
words=[tuple(1 if i in up else -1 for i in range(4)) for up in combinations(range(4),2)]
index={q:i for i,q in enumerate(words)}
edges=[(0,1),(1,2),(2,3),(3,0)]
D=len(words)
def symbolic():
    H0=s.zeros(D);H1=s.zeros(D)
    for e,(a,b) in enumerate(edges):
        for col,q in enumerate(words):
            target=list(q);target[a],target[b]=target[b],target[a]
            row=index[tuple(target)]
            H0[row,col]-=2
            if e==0 and q[a]!=q[b]:H1[row,col]+=4*s.I*q[a]
    u=s.ones(D,1)/s.sqrt(D);P=u*u.T
    deriv=-(H0+8*s.eye(D)+P).inv()*H1*u
    assert s.simplify((u.T*deriv)[0])==0
    norm=s.simplify((s.conjugate(deriv.T)*deriv)[0])
    return {'dimension':D,'band_Hessian':'4/3','u_prime_norm_squared':str(norm)},float(norm)

def cutoff(x):
    z=np.clip((np.abs(x)-.7)/.3,0,1)
    return 1-10*z**3+15*z**4-6*z**5

def run(h,unorm,extra=0,grid=8192):
    theta=2*np.pi*(np.arange(grid)/grid-.5)
    chi=cutoff(theta)
    u0=np.ones(D)/np.sqrt(D)
    u=np.tile(u0,(grid,1)).astype(complex)
    # Pointwise exact matter matrix; use no Hessian Taylor coefficients here.
    for k in np.flatnonzero(chi):
        ham=np.zeros((D,D),dtype=complex)
        for e,(a,b) in enumerate(edges):
            R=np.zeros((D,D),dtype=complex)
            for col,q in enumerate(words):
                target=list(q);target[a],target[b]=target[b],target[a]
                phase=(q[a]-q[b])*theta[k] if e==0 else 0.
                R[index[tuple(target)],col]=np.exp(-1j*phase)
            ham-=R+R.conj().T
        vals,vec=np.linalg.eigh(ham);v=vec[:,0]
        overlap=np.vdot(u0,v)
        assert abs(overlap)>.5
        u[k]=v*np.exp(-1j*np.angle(overlap))
    alpha=math.sqrt(2/3)
    x=theta/math.sqrt(h)
    psi0=(alpha/np.pi)**.25*np.exp(-alpha*x*x/2)
    psi1=math.sqrt(2*alpha)*x*psi0
    mmax=math.ceil(12/math.sqrt(h))+extra
    mm=np.arange(-mmax,mmax+1);nm=len(mm)
    def coeff(psi):
        f=(h**(-.25)*chi*psi)[:,None]*u
        transformed=np.fft.fft(f,axis=0)/grid
        return (np.sqrt(2*np.pi)*np.where(mm%2==0,1.,-1.)[:,None]*
                transformed[mm%grid]).reshape(-1)
    c0=coeff(psi0);c1=coeff(psi1)
    norm=np.linalg.norm((c0+c1)/np.sqrt(2))
    initial=(c0+c1)/(math.sqrt(2)*norm)
    row=[];col=[];data=[]
    for k,m in enumerate(mm):
        for qi,q in enumerate(words):
            source=k*D+qi
            row.append(source);col.append(source);data.append(h*m*m+8/h)
            for e,(a,b) in enumerate(edges):
                target=list(q);target[a],target[b]=target[b],target[a]
                qtarget=index[tuple(target)]
                shift=-(q[a]-q[b]) if e==0 else 0
                destk=k+shift
                if 0<=destk<nm:
                    row.append(destk*D+qtarget);col.append(source);data.append(-2/h)
    ham=coo_matrix((data,(row,col)),shape=(nm*D,nm*D)).tocsr()
    assert np.max(np.abs((ham-ham.T).data),initial=0)<1e-12
    res0=np.linalg.norm(ham@c0-alpha*c0)
    res1=np.linalg.norm(ham@c1-3*alpha*c1)
    predicted=[math.sqrt(2*alpha*unorm),math.sqrt(6*alpha*unorm)]
    times=[]
    for t in (.2,1.):
        actual=expm_multiply(-1j*t*ham,initial)
        target=(np.exp(-1j*alpha*t)*c0+np.exp(-3j*alpha*t)*c1)/(math.sqrt(2)*norm)
        err=float(np.linalg.norm(actual-target))
        bound=t*(res0+res1)/(math.sqrt(2)*norm)
        assert err<=bound+1e-10
        times.append({'time':t,'state_norm_error':err,'Duhamel_bound':float(bound),
                      'unitarity_error':abs(float(np.linalg.norm(actual))-1)})
    return {'h':h,'electric_cutoff':mmax,'grid':grid,'full_dimension':nm*D,
            'packet_norm':float(norm),'residuals':[float(res0),float(res1)],
            'residuals_over_sqrt_h':[float(res0/math.sqrt(h)),float(res1/math.sqrt(h))],
            'predicted_leading_residuals_over_sqrt_h':predicted,'times':times}

def main():
    exact,unorm=symbolic()
    rows=[run(h,unorm) for h in [1/32,1/64,1/128,1/256]]
    assert max(abs(x/y-1) for x,y in zip(rows[-1]['residuals_over_sqrt_h'],
                 rows[-1]['predicted_leading_residuals_over_sqrt_h']))<.06
    refined=run(1/128,unorm,extra=60,grid=16384)
    errors=[abs(a['state_norm_error']-b['state_norm_error'])
            for a,b in zip(rows[2]['times'],refined['times'])]
    assert max(errors)<1e-9
    source=Path(__file__).read_bytes()
    out={'created_utc':datetime.now(timezone.utc).isoformat(),
         'source':{'path':str(Path(__file__).resolve()),'bytes':len(source),'sha256':hashlib.sha256(source).hexdigest()},
         'model':'One compact coordinate, four records at fixed total charge zero on a cycle; theta only on edge 0, phi=0. K=h,J=1/h; scalar -8/h removed.',
         'scope':'A matrix-band residual and compact-state normalization control, not a literal full cubic Gauss or thermodynamic phase simulation.',
         'exact_band_control':exact,'harmonic_frequency':2*math.sqrt(2/3),
         'rows':rows,'refinement':refined,'refinement_state_error_changes':errors}
    text=json.dumps(out,indent=2)+'\n';(HERE/'CHARGED_BAND_PACKET_RESULTS.json').write_text(text);print(text,end='')
if __name__=='__main__':main()
