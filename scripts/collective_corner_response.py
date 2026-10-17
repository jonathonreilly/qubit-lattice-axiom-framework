#!/usr/bin/env python3
"""Finite full-band response of a supplied corner model; no autonomous scalar asserted."""
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=['data/collective_corner_response/candidate.json']
import itertools,json
from pathlib import Path
import numpy as np
from scipy.special import expit
ROOT=Path(__file__).resolve().parents[1]
def read_model():
    d=json.loads((ROOT/AUDIT_INPUT_PATHS[0]).read_text())
    dec=lambda a:np.array(a['real'])+1j*np.array(a['imag'])
    return np.array(d['shifts']),dec(d['blocks']),dec(d['mass_matrix']),d['chemical_potential_development_value']
def hamiltonian(k,sh,bl):
    return np.einsum('s,sij->ij',np.exp(1j*(sh@k)),bl)
def sample(N,shift,sh,bl,M):
    grid=2*np.pi/N*(np.array(list(itertools.product(range(N),repeat=3)))+shift)
    h=np.array([hamiltonian(k,sh,bl) for k in grid]);hq=np.array([hamiltonian(k+np.pi,sh,bl) for k in grid])
    e,U=np.linalg.eigh(h);eo,Uo=np.linalg.eigh(hq)
    B=Uo.conj().transpose(0,2,1)@M@U
    return h,hq,e,eo,B

def response(e,eo,B,mu,T):
    de=eo[:,:,None]-e[:,None,:]
    f=expit((mu-e)/T);fo=expit((mu-eo)/T)
    deg=abs(de)<1e-9
    D=np.divide(f[:,None,:]-fo[:,:,None],de,out=np.zeros_like(de),where=~deg)
    fm=expit((mu-(eo[:,:,None]+e[:,None,:])/2)/T)
    D[deg]=(fm*(1-fm)/T)[deg]
    w=abs(B)**2/len(e)
    iso=float(np.sum(D*w));eqdeg=float(np.sum(D*w*deg))
    iw={str(om):float(np.sum(D*w*np.divide(de**2,de**2+om**2,out=np.zeros_like(de),where=~deg))) for om in [.001,.01,.05,.1,.5]}
    return dict(isothermal=iso,degenerate=eqdeg,collisionless_static=iso-eqdeg,imaginary_frequency=iw,density=float(np.mean(f.sum(axis=1))),node_states=int(np.sum(abs(e-mu)<1e-8)))

def main():
    sh,bl,M,mu=read_model();checks={}
    def check(n,c):
        checks[n]=bool(c)
        if not c:raise AssertionError(n)
    check('mass matrix Hermitian',np.allclose(M,M.conj().T,atol=1e-12))
    check('source normalization',abs(np.max(abs(M))-1)<1e-12)
    check('hopping Hermitian pairs',all(np.allclose(bl[i].conj().T,bl[np.where((sh==-s).all(axis=1))[0][0]],atol=1e-12) for i,s in enumerate(sh)))
    rows=[]
    for N in [4,8,12]:
      for shift in [0.,.5]:
        h,hq,e,eo,B=sample(N,shift,sh,bl,M)
        for T in [.1,.03,.01]:
            row=dict(N=N,shift=shift,T=T,mu=mu,**response(e,eo,B,mu,T));rows.append(row)
            check(f'positive response {N} {shift} {T}',row['isothermal']>=row['collisionless_static']>=0)
            vals=list(row['imaginary_frequency'].values())
            check(f'Euclidean monotone {N} {shift} {T}',all(a>=b>=0 for a,b in zip([row['collisionless_static']]+vals,vals)))
    # Folded full free-energy second derivative: counts each k,k+Q pair twice, divide by2.
    N=4;T=.03;h,hq,e,eo,B=sample(N,0.,sh,bl,M)
    chi=response(e,eo,B,mu,T)['isothermal']
    def omega(m):
        z=np.zeros((len(h),24,24),complex)
        z[:,:12,:12]=h;z[:,12:,12:]=hq;z[:,:12,12:]=m*M;z[:,12:,:12]=m*M
        E=np.linalg.eigvalsh(z)
        return -T*np.logaddexp(0,(mu-E)/T).sum()/(2*len(h))
    fd={str(eps):float(-(omega(eps)-2*omega(0)+omega(-eps))/eps**2) for eps in [.001,.0003,.0001]}
    check('full grand potential derivative',abs(fd['0.0001']-chi)<1e-5)
    check('staggered source has zero linear expectation',abs((omega(.0001)-omega(-.0001))/.0002)<1e-8)
    # Actual finite real-space Hamiltonian gives a different assembly path.
    sites=list(itertools.product(range(4),repeat=3));idx={s:i for i,s in enumerate(sites)};hr=np.zeros((768,768),complex);mr=np.zeros_like(hr)
    for s,i in idx.items():
        for shift,block in zip(sh,bl):
            j=idx[tuple((np.array(s)+shift)%4)];hr[12*j:12*j+12,12*i:12*i+12]+=block
        mr[12*i:12*i+12,12*i:12*i+12]=(-1)**sum(s)*M
    er,Ur=np.linalg.eigh(hr);Br=Ur.conj().T@mr@Ur
    rr=response(er[None,:],er[None,:],Br[None,:,:],mu,T)
    check('real space versus Bloch normalization',abs(rr['isothermal']/64-chi)<1e-10)
    # Four node states and applied-source vertex, not a canonical Yukawa coupling.
    k=np.pi/2*np.array([1,-1,1]);ek,uk=np.linalg.eigh(hamiltonian(k,sh,bl));eq,uq=np.linalg.eigh(hamiltonian(k+np.pi,sh,bl));vertex=uq[:,:2].conj().T@M@uk[:,:2]
    sv=np.linalg.svd(vertex,compute_uv=False)
    check('paired source vertex',np.ptp(sv)<1e-10 and sv.min()>0)
    nodecurie=float(4*sv[0]**2/(4*T*N**3))
    # Formula for these4 states only; other exactly degenerate states can also contribute.
    check('node Curie contribution bounded by total',nodecurie<=rows[1]['degenerate']+1e-10)
    out={'scope':'Supplied free model and grand canonical development states. Finite response, not a self-generated collective scalar.','empirical_data_used':False,'response_rows':rows,'finite_difference':fd,'realspace_isothermal':rr['isothermal']/64,'source_vertex_singular_values':sv.tolist(),'node_curie_at_L4_T003':nodecurie,'conditional_static_mean_field_threshold_L12_shift_half_T003':1/rows[16]['isothermal'],'checks':checks}
    p=ROOT/'outputs/collective_corner_response/result.json';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'checks':len(checks),'passed':sum(checks.values()),'L4_T003_chi':chi,'vertex':sv.tolist(),'status':'conditional-support','physical_scalar_derived':False}))
if __name__=='__main__':main()
