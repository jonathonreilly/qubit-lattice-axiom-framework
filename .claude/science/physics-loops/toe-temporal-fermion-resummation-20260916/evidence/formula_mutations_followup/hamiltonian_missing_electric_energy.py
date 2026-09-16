#!/usr/bin/env python3
"""Actual clock gauge histories versus a charged Fock transfer and Hamiltonian.

The free two-site graph has no magnetic plaquette. Four invariant half-filled
two-component sectors realize the original four-component paired boundary
amplitude. This is a finite diagnostic, not a phase or thermal-trace test.
"""
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_FILES=[]
import hashlib,itertools,json,math,time
from pathlib import Path
import numpy as np
from scipy.linalg import eigh
from scipy.optimize import brentq
from scipy.sparse import csr_matrix,diags,eye,kron
from scipy.sparse.linalg import expm_multiply

OCC=list(itertools.combinations(range(4),2))
STATES=[sum(1<<j for j in s) for s in OCC]
OMEGA=STATES.index((1<<2)+(1<<3))
LOCAL_N=np.array([sum(j in [0,2] for j in s) for s in OCC])
CHARGE=(LOCAL_N[:,None,None,None]+LOCAL_N[None,:,None,None]
        -LOCAL_N[None,None,:,None]-LOCAL_N[None,None,None,:]).reshape(-1)
VAC=np.zeros(6**4,complex);VAC[np.ravel_multi_index((OMEGA,)*4,(6,)*4)]=1

def fock(h):
    out=np.zeros((6,6),complex);index={s:j for j,s in enumerate(STATES)}
    for col,s in enumerate(STATES):
        for j in range(4):
            if not(s>>j)&1:continue
            a=s^(1<<j);sgn=(-1)**((s&((1<<j)-1)).bit_count())
            for i in range(4):
                if (a>>i)&1:continue
                row=index[a|(1<<i)]
                out[row,col]+=sgn*(-1)**((a&((1<<i)-1)).bit_count())*h[i,j]
    return out

def one_particle(mu,kappa,theta):
    g0=np.diag([1.,-1.]);g1=np.array([[0,1],[1,0]],complex)
    U=np.array([[0,np.exp(1j*theta)],[0,0]],complex)
    K=kappa*(np.kron(U,(np.eye(2)+g1)/2)+np.kron(U.conj().T,(np.eye(2)-g1)/2))
    G=np.kron(np.eye(2),g0);h=G@(mu*np.eye(4)-K);order=[0,2,1,3]
    h=h[np.ix_(order,order)];assert np.linalg.norm(h-h.conj().T)<1e-13
    return h

def slice_fock(delta,mu,kappa,theta=0.):
    h=one_particle(mu,kappa,theta);G=np.diag([1.,1.,-1.,-1.]);W=np.eye(4)+delta*G@h
    A=W[:2,:2];B=W[:2,2:];D=W[2:,2:];R=np.linalg.inv(D)
    X=np.block([[A+B@R@B.conj().T,B@R],[R@B.conj().T,R]])
    Y=np.linalg.inv(X)
    out=np.array([[np.linalg.det(Y[np.ix_(a,b)]) for b in OCC] for a in OCC])
    out*=np.linalg.det(A)/(1+mu*delta)**4
    assert np.linalg.norm(out-out.conj().T)<2e-13
    return out

def four_tensor_action(A,v):
    x=v.reshape((6,)*4)
    for axis,M in enumerate([A,A,A.conj(),A.conj()]):
        x=np.moveaxis(np.tensordot(M,x,axes=(1,axis)),0,axis)
    return x.reshape(-1)

def variance(c):
    if c<1:
        d=math.pi**2/c
        return .5/c-math.pi**2/c**2*variance(d)
    k=np.arange(-max(1,math.ceil(math.sqrt(44/c))),max(1,math.ceil(math.sqrt(44/c)))+1)
    w=np.exp(-c*k*k)
    return float(np.dot(w,k*k)/w.sum())

def calibration(delta,N,g):
    target=delta*g*g*N*N/(4*math.pi**2)
    logc=brentq(lambda z:math.log(variance(math.exp(z)))-math.log(target),-10,6,xtol=1e-13)
    c=math.exp(logc);K=max(2,math.ceil(math.sqrt(44/c)));k=np.arange(-K,K+1);w=np.exp(-c*k*k);w/=w.sum()
    assert abs(variance(c)/target-1)<2e-11
    def lam(r):
        r=np.asarray(r);return 1-2*np.sum(w*np.sin(math.pi*r[...,None]*k/N)**2,axis=-1)
    return c,lam

def physical_boundary(delta,N,Nt,mu,kappa,g):
    F=slice_fock(delta,mu,kappa);vals,u=eigh(F);assert min(vals)>0
    half=(u*np.sqrt(vals))@u.conj().T
    c,lam=calibration(delta,N,g);electric=lam(CHARGE)
    assert min(electric)>0 and max(electric)<=1+1e-13
    v=four_tensor_action(half,VAC);state=v.copy()
    for _ in range(Nt-1):state=four_tensor_action(half,electric*four_tensor_action(half,state))
    amplitude=np.vdot(v,state)
    assert abs(amplitude.imag)<2e-12 and amplitude.real>0
    wrong=VAC.copy()
    for _ in range(Nt-1):wrong=four_tensor_action(half,electric*four_tensor_action(half,wrong))
    return float(amplitude.real),float(np.vdot(VAC,wrong).real),c

def direct_dirac_weight(angles,delta,mu,kappa):
    sx=np.array([[0,1],[1,0]],complex);sz=np.diag([1.,-1.])
    g0=np.kron(sz,np.eye(2));g1=np.kron(sx,sx);Pp=np.kron(np.eye(2),(np.eye(4)+g0)/2);Pm=np.eye(8)-Pp
    Nt=len(angles);D=np.zeros((8*Nt,8*Nt),complex)
    for t,theta in enumerate(angles):
        U=np.array([[0,np.exp(1j*theta)],[0,0]],complex)
        K=kappa*(np.kron(U,(np.eye(4)+g1)/2)+np.kron(U.conj().T,(np.eye(4)-g1)/2))
        a=slice(8*t,8*(t+1));D[a,a]=(1+mu*delta)*np.eye(8)-delta*K
        if t+1<Nt:D[a,slice(8*(t+1),8*(t+2))]=-Pp
        if t>0:D[a,slice(8*(t-1),8*t)]=-Pm
    return math.exp(2*(np.linalg.slogdet(D)[1]-8*Nt*math.log1p(mu*delta)))

def explicit_paths(mu,kappa,g):
    N=3;Nt=3;delta=.08;c,lam=calibration(delta,N,g);angles=2*math.pi*np.arange(N)/N
    Q=np.array([[np.mean(lam(np.arange(N))*np.cos((angles[a]-angles[b])*np.arange(N))) for b in range(N)] for a in range(N)])
    assert min(Q.reshape(-1))>0 and np.linalg.norm(Q.sum(axis=1)-1)<1e-13
    path_sum=0.;reduction_error=0.
    for labels in itertools.product(range(N),repeat=Nt):
        history=angles[list(labels)];weight=direct_dirac_weight(history,delta,mu,kappa)
        state=np.zeros(6,complex);state[OMEGA]=1
        for theta in history:state=slice_fock(delta,mu,kappa,float(theta))@state
        reduced=abs(state[OMEGA])**4
        reduction_error=max(reduction_error,abs(weight-reduced));assert abs(weight-reduced)<2e-12
        probability=np.prod([Q[labels[t+1],labels[t]] for t in range(Nt-1)])/N
        path_sum+=probability*weight
    physical,missing_endpoints,_=physical_boundary(delta,N,Nt,mu,kappa,g)
    assert abs(path_sum-physical)<3e-12
    assert abs(missing_endpoints-physical)>1e-4
    return {'N':N,'time_slices':Nt,'delta':delta,'histories':N**Nt,'direct_four_component_path_sum':path_sum,'physical_fock_transfer_amplitude':physical,'difference':abs(path_sum-physical),'maximum_spin_reduction_error':reduction_error,'amplitude_without_endpoint_factors':missing_endpoints,'endpoint_error':abs(missing_endpoints-physical),'calibrated_c':c}

def continuum_hamiltonian(mu,kappa,g):
    H=fock(one_particle(mu,kappa,0))+2*mu*np.eye(6)
    full=diags(0*g*g*CHARGE**2,dtype=complex,format='csr')
    for axis,A in enumerate([H,H,H.conj(),H.conj()]):
        piece=csr_matrix([[1.]])
        for i in range(4):piece=kron(piece,csr_matrix(A) if axis==i else eye(6,format='csr'),format='csr')
        full=full+piece
    assert np.linalg.norm((full-full.conj().T).data)<1e-12
    return full

def generator_check(H,mu,kappa,g):
    rng=np.random.default_rng(43270)
    v=rng.normal(size=6**4)+1j*rng.normal(size=6**4);v/=np.linalg.norm(v)
    expected=H@v;rows=[]
    for N in [64,128,256]:
        delta=.001/N**2;F=slice_fock(delta,mu,kappa);ev,u=eigh(F)
        half=(u*np.sqrt(ev))@u.conj().T;c,lam=calibration(delta,N,g)
        actual=four_tensor_action(half,lam(CHARGE)*four_tensor_action(half,v))
        error=float(np.linalg.norm((v-actual)/delta-expected))
        rows.append({'N':N,'delta':delta,'generator_vector_error':error,'hamiltonian_vector_norm':float(np.linalg.norm(expected))})
    assert rows[-1]['generator_vector_error']<.001,rows
    assert rows[-1]['generator_vector_error']<rows[0]['generator_vector_error']/10,rows
    return rows

def run():
    start=time.time();mu=6.;kappa=.5;g=.8;T=.5
    paths=explicit_paths(mu,kappa,g);H=continuum_hamiltonian(mu,kappa,g)
    generators=generator_check(H,mu,kappa,g)
    ref=np.vdot(VAC,expm_multiply(-T*H,VAC));assert abs(ref.imag)<1e-13
    rows=[]
    for power in [1,2,3]:
        values=[]
        # The original slow-path endpoint N=17 missed the declared factor3
        # diagnostic. Retain that failure and resolve farther to N=33.
        for N in ([3,5,9,17,33] if power==1 else [3,5,9,17]):
            Nt=N**power;delta=T/Nt
            value,without,c=physical_boundary(delta,N,Nt,mu,kappa,g)
            values.append({'N':N,'Nt':Nt,'delta':delta,'calibrated_c':c,'actual_boundary_amplitude':value,'continuum_boundary_amplitude':float(ref.real),'absolute_error':abs(value-ref.real)})
        assert values[-1]['absolute_error']<values[0]['absolute_error']/3,values
        rows.append({'joint_path_power':power,'values':values})
    # Even the slow first path is a small finite-time error here; this is not
    # a bound for general graphs or a uniform-volume convergence assertion.
    assert rows[0]['values'][-1]['absolute_error']<.01
    print(json.dumps({'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'physical_invariant_sector_dimension':6**4,'electric_charge_range':[int(min(CHARGE)),int(max(CHARGE))],'exact_finite_path_check':paths,'continuum_hamiltonian_nonzeros':H.nnz,'independent_generator_checks':generators,'joint_refinements':rows,'seconds':time.time()-start},indent=2))

if __name__=='__main__':run()
