"""Exact transfer formulas versus direct Villain kernels and finite generators."""
from pathlib import Path
from itertools import product
import json, math
import numpy as np
import mpmath as mp
from scipy.linalg import expm,eigh

result={};rows=[]
def theta(x):return 1+2*sum(x**(q*q) for q in range(1,30))
def eigenQ(N,x):
    angle=2*np.pi*np.arange(N)/N
    return (1+2*sum(x**(q*q)*np.cos(q*angle) for q in range(1,30)))/theta(x)
def spatial(phi,y):return (1+2*sum(y**(q*q)*np.cos(q*phi) for q in range(1,30)))/theta(y)
for N in [2,3,5,9,17]:
    X=np.roll(np.eye(N),1,axis=0);H0=2*np.eye(N)-X-X.T
    for delta in [.1,.025,.00625,.0015625]:
        t=.7;x=delta*t;beta=N*N/(2*np.pi*np.pi)*math.log(1/x)
        # Direct periodized real Gaussian evaluated on each group element.
        ang=2*np.pi*np.arange(N)/N;n=np.arange(-20,21)
        prob=np.exp(-beta*(ang[:,None]+2*np.pi*n)**2/2).sum(axis=1);prob/=prob.sum()
        Q=sum(prob[r]*np.linalg.matrix_power(X,r) for r in range(N))
        lam=eigenQ(N,x);assert lam.min()>0
        assert np.max(abs(np.sort(np.linalg.eigvalsh(Q))-np.sort(lam)))<1e-13
        error=float(np.linalg.norm(Q-(np.eye(N)-x*H0),2))
        R=2*x**4/(1-x**5);bound=8*x*x+(4*x+2)*R
        assert error<=bound+1e-14
        generator=-np.log(lam)/delta
        target=2*t*(1-np.cos(ang));ge=float(np.max(abs(generator-target)))
        deficit=4*x+2*R;generator_bound=(bound+deficit**2/(2*(1-deficit)))/delta
        assert deficit<1 and ge<=generator_bound+1e-12
        rows.append({'N':N,'delta':delta,'temporal_beta':beta,'generator_error':ge,'transfer_linear_error':error,'proved_linear_error_bound':bound})
    last=[r['generator_error'] for r in rows if r['N']==N]
    assert all(b<a for a,b in zip(last,last[1:]))
result['temporal_direct_kernel']=rows
# Uniform spatial-potential check, with high-resolution angles used only to
# challenge the analytic uniform bound (not to prove it).
sp=[]
for delta in [.1,.025,.00625,.0015625]:
    K=1.3;y=delta*K/2;phi=np.linspace(-np.pi,np.pi,2049)
    B=spatial(phi,y);assert B.min()>0 and B.max()<=1+1e-14
    error=float(np.max(abs(-np.log(B)/delta-K*(1-np.cos(phi)))))
    R=2*y**4/(1-y**5);linear=8*y*y+(4*y+2)*R;deficit=4*y+2*R
    bound=(linear+deficit**2/(2*(1-deficit)))/delta
    assert deficit<1 and error<=bound+1e-12
    sp.append({'delta':delta,'spatial_beta':1/(2*math.log(1/y)),'generator_sup_grid_error':error})
assert all(b['generator_sup_grid_error']<a['generator_sup_grid_error'] for a,b in zip(sp,sp[1:]))
result['spatial_villain_generator']=sp
# Fixed one-plaquette physical Gauss sector. Electric labels have the same
# oriented flux on all four edges, so Q restricted to the sector is lambda^4.
pr=[]
for N in [3,5,9]:
    ang=2*np.pi*np.arange(N)/N;F=np.exp(1j*np.outer(np.arange(N),ang))/np.sqrt(N)
    t=.7;K=1.3
    HB=F.conj().T@np.diag(K*(1-np.cos(ang)))@F
    HE=np.diag(8*t*(1-np.cos(ang)));H=HE+HB
    exact=expm(-.8*H)
    for delta in [.1,.025,.00625]:
        half=F.conj().T@np.diag(np.sqrt(spatial(ang,delta*K/2)))@F
        T=half@np.diag(eigenQ(N,delta*t)**4)@half
        eig,U=eigh(T);assert eig.min()>0 and eig.max()<=1+1e-12
        generator=(U*(-np.log(eig)/delta))@U.conj().T
        ge=float(np.linalg.norm(generator-H,2))
        steps=round(.8/delta);evolved=(U*(eig**steps))@U.conj().T
        error=float(np.linalg.norm(evolved-exact,2))
        pr.append({'N':N,'delta':delta,'generator_error':ge,'semigroup_time':.8,'semigroup_error':error,'minimum_transfer_eigenvalue':float(eig.min())})
    rr=[r for r in pr if r['N']==N]
    assert all(b['generator_error']<a['generator_error'] and b['semigroup_error']<a['semigroup_error'] for a,b in zip(rr,rr[1:]))
result['gauss_sector_noncommuting_transfer']=pr
# The wrong fixed-N rotor scaling: use log1p on an explicitly summed spectral
# deficit, preserving exponentially small values that double precision loses.
mp.mp.dps=90;freeze=[];N=5;b=mp.mpf(1)
for delta in [mp.mpf('0.1'),mp.mpf('0.05'),mp.mpf('0.02'),mp.mpf('0.005'),mp.mpf('0.001')]:
    x=mp.exp(-2*mp.pi**2*b/(N*N*delta));den=1+2*sum(x**(q*q) for q in range(1,20))
    energies=[]
    for k in range(N):
        deficit=2*sum(x**(q*q)*(1-mp.cos(2*mp.pi*q*k/N)) for q in range(1,20))/den
        energies.append(-mp.log1p(-deficit)/delta)
    maxh=max(energies);assert maxh>0
    freeze.append({'delta':str(delta),'log10_generator_norm':str(mp.log10(maxh))})
assert all(mp.mpf(v['log10_generator_norm'])<mp.mpf(u['log10_generator_norm']) for u,v in zip(freeze,freeze[1:]))
result['fixed_N_rotor_scaling_freezes']=freeze
# Distinct absolute path and operator bounds for anisotropic r=1 Wilson.
sx=np.array([[0,1],[1,0]],complex);sy=np.array([[0,-1j],[1j,0]],complex);sz=np.diag([1,-1])
gam=[np.kron(sx,s) for s in [sx,sy,sz]]+[np.kron(sy,np.eye(2))]
vs=list(product(range(2),range(2),range(2),range(3)));ix={v:i for i,v in enumerate(vs)}
rng=np.random.default_rng(8108);Us=[]
for mu,L in enumerate([2,2,2,3]):
    U=np.zeros((len(vs),len(vs)),complex)
    for x in vs:
        y=list(x);y[mu]=(y[mu]+1)%L
        U[ix[x],ix[tuple(y)]]=np.exp(1j*rng.uniform(-np.pi,np.pi))
    assert np.linalg.norm(U.conj().T@U-np.eye(len(vs)))<1e-13;Us.append(U)
wilson=[]
for delta in [1.,.25,.0625]:
    weights=[1,1,1,1/delta];m0=.7;mass=m0+sum(weights);K=np.zeros((4*len(vs),4*len(vs)),complex)
    for w,g,U in zip(weights,gam,Us):
        axial=-w*(np.kron((np.eye(4)-g)/2,U)+np.kron((np.eye(4)+g)/2,U.conj().T))
        assert abs(np.linalg.norm(axial,2)-w)<1e-12;K+=axial
    D=mass*np.eye(len(K))+K
    coercive=(D+D.conj().T)/2
    assert np.linalg.eigvalsh(coercive).min()>=m0-1e-12
    assert np.linalg.svd(D,compute_uv=False).min()>=m0-1e-12
    actual=float(np.linalg.norm(K,2)/mass);improved=sum(weights)/mass;count=2*sum(weights)/mass
    assert actual<=improved+1e-12 and improved<1
    wilson.append({'delta':delta,'mass_diagonal':mass,'path_count_ratio':count,'operator_ratio_bound':improved,'actual_operator_ratio':actual,'minimum_singular_value':float(np.linalg.svd(D,compute_uv=False).min())})
result['anisotropic_Wilson_bound_distinction']=wilson
print(json.dumps(result,indent=2),flush=True)
Path(__file__).with_name('BLOCK3_TRANSFER_SCALING_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
