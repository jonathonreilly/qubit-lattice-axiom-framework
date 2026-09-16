#!/usr/bin/env python3
"""Open Wilson determinant, reduced positive transfer, and explicit CAR Fock state.
The general determinant reduction is prior art; this checks our exact conventions.
"""
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_FILES=[]
import hashlib,itertools,json,math,time
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import eigh


def one_particle_parts(mu,kappa):
    sx=np.array([[0,1],[1,0]],complex);sz=np.diag([1.,-1.]);g0=np.kron(sz,np.eye(2));g1=np.kron(sx,sx)
    G=np.kron(np.eye(2),g0);hop=np.array([[0,1],[0,0]],complex)
    forward=np.kron(hop,(np.eye(4)+g1)/2);reverse=np.kron(hop.conj().T,(np.eye(4)-g1)/2)
    order=[0,1,4,5,2,3,6,7]
    def perm(A):return A[np.ix_(order,order)]
    parts=[perm(mu*G),perm(-kappa*G@(forward+reverse)),perm(-1j*kappa*G@(forward-reverse))]
    for a in parts:assert np.linalg.norm(a-a.conj().T)<1e-13
    return parts


def theta(t):return .6*math.sin(2.3*t)+.2*math.cos(5.1*t)


def fock_map(h,states):
    index={s:j for j,s in enumerate(states)};d=len(states);H=np.zeros((d,d),complex)
    for col,state in enumerate(states):
        for j in range(8):
            if not(state>>j)&1:continue
            after=state^(1<<j);s1=(-1)**((state&((1<<j)-1)).bit_count())
            for i in range(8):
                if (after>>i)&1:continue
                final=after|(1<<i);s2=(-1)**((after&((1<<i)-1)).bit_count())
                H[index[final],col]+=s1*s2*h[i,j]
    return H


def exterior(S,occupied):
    d=len(occupied);out=np.empty((d,d),complex)
    for i,a in enumerate(occupied):
        for j,b in enumerate(occupied):out[i,j]=np.linalg.det(S[np.ix_(a,b)])
    return out


def run():
    start=time.time();mu=6.;kappa=.5;T=.5;r=4;n=8
    parts=one_particle_parts(mu,kappa)
    def h(t):return parts[0]+math.cos(theta(t))*parts[1]+math.sin(theta(t))*parts[2]
    occupied=list(itertools.combinations(range(8),4));states=[sum(1<<j for j in row) for row in occupied];omega=states.index(sum(1<<j for j in range(4,8)))
    fparts=[fock_map(a,states) for a in parts];fparts[0]+=mu*r*np.eye(len(states))
    def H(t):return fparts[0]+math.cos(theta(t))*fparts[1]+math.sin(theta(t))*fparts[2]
    psi=np.zeros(len(states),complex);psi[omega]=1
    sol=solve_ivp(lambda t,y:-H(t)@y,(0,T),psi,rtol=2e-11,atol=2e-13)
    assert sol.success;fock_amplitude=sol.y[omega,-1]
    one=solve_ivp(lambda t,y:(-h(t)@y.reshape(n,n)).reshape(-1),(0,T),np.eye(n,dtype=complex).reshape(-1),rtol=2e-11,atol=2e-13)
    assert one.success;S=one.y[:,-1].reshape(n,n);minor_amplitude=math.exp(-mu*r*T)*np.linalg.det(S[r:,r:])
    assert abs(minor_amplitude-fock_amplitude)<3e-10
    Pp=np.diag([1]*r+[0]*r);Pm=np.eye(n)-Pp;G=Pp-Pm
    rows=[];finite_fock=[]
    for Nt in [4,8,16,32,64]:
        delta=T/Nt;big=np.zeros((n*Nt,n*Nt),complex);Xprod=np.eye(n,dtype=complex);chron=np.eye(n,dtype=complex);logA=logD=0.;Xs=[]
        for t in range(Nt):
            a0=G@h(t*delta);block=np.eye(n)+delta*a0
            A=block[:r,:r];B=block[:r,r:];C=block[r:,:r];D=block[r:,r:]
            assert np.linalg.norm(C+B.conj().T)<1e-13
            invD=np.linalg.inv(D);X=np.block([[A+B@invD@B.conj().T,B@invD],[invD@B.conj().T,invD]])
            assert np.linalg.norm(X-X.conj().T)<1e-13 and eigh(X,eigvals_only=True).min()>0
            Xprod=X@Xprod;chron=np.linalg.inv(X)@chron;logA+=np.linalg.slogdet(A)[1];logD+=np.linalg.slogdet(D)[1];Xs.append((X,A))
            sl=slice(n*t,n*(t+1));big[sl,sl]=block
            if t+1<Nt:big[sl,slice(n*(t+1),n*(t+2))]=-Pp
            if t>0:big[sl,slice(n*(t-1),n*t)]=-Pm
        norm=2*r*Nt*math.log1p(mu*delta)
        phase,raw=np.linalg.slogdet(big);assert abs(phase-1)<3e-12
        exact=raw-norm;schur=np.linalg.slogdet(Xprod[:r,:r])[1]-norm
        complementary=logA+np.linalg.slogdet(chron[r:,r:])[1]-norm
        assert abs(exact-schur)<3e-11 and abs(exact-complementary)<3e-11
        canonical=math.exp(logA-norm)*np.linalg.det(chron[r:,r:])
        assert abs(abs(canonical)-math.exp(exact))<3e-11
        comm=float(np.linalg.norm(Xs[0][0]@Xs[-1][0]-Xs[-1][0]@Xs[0][0]));assert comm>1e-9
        if Nt==4:
            state=psi.copy();min_eig=1.
            for X,A in Xs:
                F=math.exp(np.linalg.slogdet(A)[1]-2*r*math.log1p(mu*delta))*exterior(np.linalg.inv(X),occupied)
                min_eig=min(min_eig,float(eigh(F,eigvals_only=True).min()));assert min_eig>0
                state=F@state
            assert abs(state[omega]-canonical)<3e-11
            finite_fock.append({'Nt':Nt,'fock_dimension':len(states),'amplitude_error':float(abs(state[omega]-canonical)),'minimum_slice_transfer_eigenvalue':min_eig})
        rows.append({'Nt':Nt,'delta':delta,'full_matrix_dimension':n*Nt,'normalized_log_determinant':float(exact),'schur_error':abs(exact-schur),'complementary_minor_error':abs(exact-complementary),'noncommuting_slice_norm':comm,'paired_boundary_weight':math.exp(2*exact),'continuum_paired_weight':float(abs(fock_amplitude)**2),'paired_weight_error':abs(math.exp(2*exact)-abs(fock_amplitude)**2),'scalar_log_prefactor':float(logA-norm)})
    assert rows[-1]['paired_weight_error']<rows[0]['paired_weight_error']/5
    assert rows[-1]['paired_weight_error']<.003
    print(json.dumps({'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'continuum_fock_amplitude':[float(fock_amplitude.real),float(fock_amplitude.imag)],'one_particle_vs_fock_amplitude_error':float(abs(minor_amplitude-fock_amplitude)),'finite_fock_check':finite_fock,'joint_open_boundary_checks':rows,'seconds':time.time()-start},indent=2))


if __name__=='__main__':run()
