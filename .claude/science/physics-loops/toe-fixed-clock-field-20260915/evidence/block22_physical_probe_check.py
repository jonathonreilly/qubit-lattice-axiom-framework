"""Physical-probe diagnostics. Block21 matrix builder is an explicitly shared input."""
from pathlib import Path
import json,math,importlib.util,time
import numpy as np
from scipy.sparse import diags,eye,kron
from scipy.sparse.linalg import eigsh,expm_multiply

p=Path(__file__).with_name('block21_slow_fast_check.py')
spec=importlib.util.spec_from_file_location('block21',p)
b21=importlib.util.module_from_spec(spec);spec.loader.exec_module(b21)

def curl_check(L):
    sites=np.array(list(np.ndindex(L,L,L)));V=L**3
    def idx(x):return np.ravel_multi_index(tuple(np.asarray(x)%L),(L,L,L))
    pairs=[(0,1),(0,2),(1,2)];C=np.zeros((3*V,3*V));grad=np.zeros((3*V,V))
    for x in sites:
        r=idx(x)
        for i in range(3):
            xp=x+np.eye(3,dtype=int)[i]
            grad[3*r+i,idx(xp)]+=1;grad[3*r+i,r]-=1
        for f,(i,j) in enumerate(pairs):
            ei=np.eye(3,dtype=int)[i];ej=np.eye(3,dtype=int)[j]
            C[3*r+f,3*idx(x+ei)+j]+=1
            C[3*r+f,3*r+j]-=1
            C[3*r+f,3*idx(x+ej)+i]-=1
            C[3*r+f,3*r+i]+=1
    assert np.max(abs(C@grad))==0
    ev,U=np.linalg.eigh(C.T@C);pos=ev>1e-10
    assert sum(pos)==2*(V-1)
    Om=(U[:,pos]*np.sqrt(ev[pos]))@U[:,pos].T
    Oplus=(U[:,pos]/np.sqrt(ev[pos]))@U[:,pos].T
    BB=C@Oplus@C.T
    FOm=np.zeros_like(Om,dtype=complex);FBB=FOm.copy()
    for n in sites:
        k=2*math.pi*n/L;d=np.exp(1j*k)-1;w=np.linalg.norm(d)
        if w<1e-12:continue
        P=np.eye(3)-np.outer(d,d.conj())/w**2
        ck=np.zeros((3,3),complex)
        for f,(i,j) in enumerate(pairs):ck[f,j]=d[i];ck[f,i]=-d[j]
        phase=np.exp(1j*sites@k)
        spatial=np.outer(phase,phase.conj())/V
        FOm+=np.kron(spatial,w*P)
        FBB+=np.kron(spatial,ck@ck.conj().T/w)
    err=max(np.max(abs(Om-FOm)),np.max(abs(BB-FBB)))
    assert err<2e-11
    harmonic=np.tile(np.eye(3),(V,1))
    null=max(np.max(abs(Om@grad)),np.max(abs(Om@harmonic)))
    assert null<2e-11
    # Independent exact covariance/commutator identity on the physical subspace.
    cross=np.max(abs(Om@Oplus-(U[:,pos]@U[:,pos].T)))
    assert cross<2e-11
    return {'L':L,'positive_modes':int(sum(pos)),'covariance_symbol_error':float(err),
            'longitudinal_harmonic_residual':float(null),'spectral_inverse_error':float(cross)}

def probe(g,pad=0):
    nq=math.ceil(5/g)+pad;nt=math.ceil(6/math.sqrt(g))+pad
    dq,dt=2*nq+1,2*nt+1;H=b21.build(g,nq,nt);dim=H.shape[0]
    rng=np.random.default_rng(22003);v0=rng.normal(size=dim)+1j*rng.normal(size=dim)
    vals,vec=eigsh(H,k=1,sigma=-4.,which='LM',tol=1e-12,v0=v0)
    E0=vals[0];psi=vec[:,0];res=np.linalg.norm(H@psi-E0*psi)
    assert res<2e-8
    q=np.repeat(np.arange(-nq,nq+1),dt)
    spin=np.tile(np.array([1.,-1.]),dq*dt)
    electric=g*(np.repeat(q,2)+.15*spin)
    tq=kron(kron(diags(np.ones(dq-1),-1),eye(dt)),eye(2),format='csr')
    magnetic=(tq-tq.T)/(2j*g)
    u=.8;v=.6;t=.37
    half=np.exp(.5j*u*electric)
    right=half*psi;left=half.conj()*psi
    evolved=expm_multiply(1j*v*magnetic,right,traceA=0)
    char=np.vdot(left,evolved)
    charz=np.vdot(left,expm_multiply(1j*v*magnetic,right*spin,traceA=0))
    z=np.vdot(psi,spin*psi).real
    eb=magnetic@psi
    ex=expm_multiply(-1j*t*(H-E0*eye(dim)),eb,traceA=-1j*t*(H.diagonal().sum()-E0*dim))
    response=np.vdot(eb,ex)
    target=math.exp(-.5*(u*u/4+v*v))
    targetresponse=np.exp(-2j*t)
    return {'g':g,'dimension':dim,'ground_residual':float(res),
       'electric_variance':float(np.vdot(electric*psi,electric*psi).real),
       'magnetic_variance':float(np.vdot(eb,eb).real),
       'symmetric_characteristic':[float(char.real),float(char.imag)],
       'characteristic_target':target,'characteristic_error':float(abs(char-target)),
       'spin_z':float(z),'probe_spin_connected':float(abs(charz-char*z)),
       'magnetic_response':[float(response.real),float(response.imag)],
       'magnetic_response_target':[float(targetresponse.real),float(targetresponse.imag)],
       'magnetic_response_error':float(abs(response-targetresponse))}

def main():
    curls=[curl_check(L) for L in [3,4]]
    rows=[]
    for g in [.16,.10,.05]:
        r=probe(g);rows.append(r);print(json.dumps(r),flush=True)
    for key in ['characteristic_error','magnetic_response_error','probe_spin_connected']:
        assert rows[-1][key]<rows[0][key]/2
    out={'status':'author_checks_not_independent_audit','curl_checks':curls,
         'fixture_rows':rows,'targets':{'electric_variance':.25,'magnetic_variance':1.},
         'shared_input':'Block21 Fourier matrix; its literal position-space check is separate',
         'limits':'noncubic finite fixture and exact free curl matrices; no fixed-g phase proof'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()

