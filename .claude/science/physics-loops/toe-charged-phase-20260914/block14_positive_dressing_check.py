"""Personal finite falsifiers for positive orbit dressings; no phase computation."""
import itertools
import numpy as np
from scipy.linalg import eigh
from scipy.special import logsumexp


def ratio(f):
    N=f.shape[0];om=np.exp(2j*np.pi/N)
    return sum(om**(-k)*np.roll(f,-k,axis=0) for k in range(N))/sum(np.roll(f,-k,axis=0) for k in range(N))


def posterior_identities():
    rng=np.random.default_rng(39171)
    for N in (2,3,4,5,7):
        om=np.exp(2j*np.pi/N);char=om**np.arange(N)
        for scale in (.05,.8,3.):
            mu=np.exp(scale*rng.normal(size=(N,13)));mu/=mu.sum()
            f=np.exp(scale*rng.normal(size=(N,13)))
            A=ratio(f);Amu=ratio(mu)
            assert np.max(abs(A))<=1+1e-12
            assert np.max(abs(np.roll(A,1,axis=0)-om**(-1)*A))<1e-12
            mass=mu.sum(axis=0);p=mu/mass;q=f/f.sum(axis=0)
            u=char@p;w=char@q
            r=float(mass@abs(u)**2);alpha=float(mass@abs(u))
            assert abs(np.sum(mu*Amu)-r)<1e-12
            assert alpha**2<=r+1e-12 and r<=alpha+1e-12
            z=np.conj(u)/np.where(abs(u)>1e-15,abs(u),1)
            Aopt=char[:,None]*z[None,:]
            assert abs(np.sum(mu*Aopt)-alpha)<1e-12
            got=np.sum(mu*A);expected=np.sum(mass*u*np.conj(w))
            assert abs(got-expected)<1e-12
            eps=abs(p-q).sum(axis=0);E2=float(mass@eps**2)
            assert got.real>=r-np.sqrt(r*E2)-1e-12
            KL=np.sum(p*np.log(p/q),axis=0)
            assert E2<=2*float(mass@KL)+1e-12
            assert np.max(abs(ratio(f*np.exp(rng.normal(size=13)))-A))<1e-12
    print('posterior_identities: exact charge, norm, optimum, matched second moment, robustness and orbit normalization checked')


def cycle_partition():
    for N in (2,3,5):
        om=np.exp(2j*np.pi/N)
        for P in (3,4):
            spins=np.array(list(itertools.product(range(N),repeat=P-1)))
            spins=np.column_stack([np.zeros(len(spins),dtype=int),spins])
            diff=np.roll(spins,-1,axis=1)-spins
            for kappa in (.3,1.4):
                weight=np.exp(kappa*np.cos(2*np.pi*np.arange(N)/N))
                wh=np.fft.fft(weight)/N
                assert wh[1].real>0 and abs(wh[1].imag)<1e-12 and wh[1].real<wh[0].real
                f=[]
                for h in range(N):
                    a=np.zeros(P,dtype=int);a[0]=h
                    direct=N*np.prod(weight[(diff+a)%N],axis=1).sum()
                    fourier=N**P*np.sum(wh**P*om**(np.arange(N)*h))
                    assert abs(direct-fourier)<1e-9*direct
                    f.append(direct)
                A=ratio(np.array(f)[:,None])[:,0]
                expected=(wh[1]/wh[0])**P*om**np.arange(N)
                assert np.max(abs(A-expected))<1e-12
    print('cycle_partition: direct site-spin sums equal Fourier currents and exact extra perimeter attenuation')


def two_plaquette_auxiliary():
    edges=[(0,1),(1,2),(3,4),(4,5),(0,3),(1,4),(2,5)]
    F=np.array([[1,0,-1,0,-1,1,0],[0,1,0,-1,0,-1,1]])
    rng=np.random.default_rng(431)
    for N in (2,3,5):
        om=np.exp(2j*np.pi/N);kappa=.7;w=np.exp(kappa*np.cos(2*np.pi*np.arange(N)/N));wh=np.fft.fft(w)/N
        spins=np.array(list(itertools.product(range(N),repeat=5)));spins=np.column_stack([np.zeros(len(spins),dtype=int),spins]);diff=np.column_stack([spins[:,y]-spins[:,x] for x,y in edges])
        def direct(a):return N*np.prod(w[(diff+a)%N],axis=1).sum()
        for _ in range(6):
            a=rng.integers(N,size=7);b=(F@a)%N;gau=rng.integers(N,size=6);grad=np.array([gau[y]-gau[x] for x,y in edges])
            assert np.max(abs(F@grad))==0
            lhs=direct(a);rhs=N**6*sum(wh[q1]**3*wh[q2]**3*wh[(q1-q2)%N]*om**(q1*b[0]+q2*b[1]) for q1 in range(N) for q2 in range(N))
            assert abs(lhs-rhs)<1e-10*lhs
            assert abs(direct(a+grad)-lhs)<1e-10*lhs
    print('two_plaquette_auxiliary: direct six-site spin sums, gauge transformations, and closed-current partition formula agree')


def two_plaquette_ground():
    rows=[]
    for N in (2,3,5,7):
        om=np.exp(2j*np.pi/N);bs=list(itertools.product(range(N),repeat=2));index={b:i for i,b in enumerate(bs)}
        def shift(v):
            out=np.zeros((N*N,N*N))
            for i,b in enumerate(bs):out[index[tuple((b[k]+v[k])%N for k in range(2))],i]=1
            return out
        I=np.eye(N*N);S1=shift((1,0));S2=shift((0,1));S12=shift((1,-1))
        electric=3*(2*I-S1-S1.T)+3*(2*I-S2-S2.T)+(2*I-S12-S12.T)
        magnetic=np.diag([2-np.cos(2*np.pi*b[0]/N)-np.cos(2*np.pi*b[1]/N) for b in bs])
        for K in (.25,1.,4.):
            ev,vec=eigh(electric+K*magnetic);psi=vec[:,0]
            if psi.sum()<0:psi=-psi
            assert psi.min()>0 and ev[1]>ev[0]
            mu=(psi**2).reshape(N,N);mass=mu.sum(axis=0);p=mu/mass
            u=(om**np.arange(N))@p;r=float(mass@abs(u)**2);alpha=float(mass@abs(u))
            bare=abs(np.sum(mu*om**np.arange(N)[:,None]))
            assert abs(np.sum(mu*ratio(mu))-r)<1e-12
            assert alpha+1e-12>=bare
            # An auxiliary graph partition has three outer edges per face and one shared edge.
            kappa=1.2;w=np.exp(kappa*np.cos(2*np.pi*np.arange(N)/N));wh=np.fft.fft(w)/N
            f=np.array([N**6*sum(wh[q1]**3*wh[q2]**3*wh[(q1-q2)%N]*om**(q1*b1+q2*b2) for q1 in range(N) for q2 in range(N)) for b1,b2 in bs]).reshape(N,N)
            assert np.max(abs(f.imag))<1e-8 and f.real.min()>0
            A=ratio(f.real);assert np.max(abs(A))<=1+1e-12
            assert abs(np.sum(mu*A))<=alpha+1e-12
            rows.append((N,K,float(bare),alpha,r,float(np.sum(mu*A).real)))
    print('two_plaquette_ground: actual finite physical clock flux Hamiltonian; (N,K,bare,diagonal_optimum,matched,auxiliary)')
    for row in rows:print(row)


def fidelity_wrong_direction():
    plus=np.array([1,1])/np.sqrt(2);minus=np.array([1,-1])/np.sqrt(2)
    quantum=abs(np.vdot(plus,minus));classical=np.sum(abs(plus)*abs(minus))
    assert quantum<1e-14 and abs(classical-1)<1e-14
    print('fidelity_wrong_direction: identical coordinate probabilities can have orthogonal quantum states; no classical lower bound on quantum fidelity')


def psdpower(M,power):
    ev,U=eigh((M+M.conj().T)/2)
    vals=np.zeros_like(ev);keep=ev>1e-12
    vals[keep]=ev[keep]**power
    return (U*vals)@U.conj().T


def quantum_ratio(F,V,N):
    om=np.exp(2j*np.pi/N);orbit=[np.linalg.matrix_power(V,k)@F@np.linalg.matrix_power(V.conj().T,k) for k in range(N)]
    tau=sum(orbit)/N;T=sum(om**(-k)*orbit[k] for k in range(N))/N
    inv=psdpower(tau,-.5);A=inv@T.conj().T@inv
    return A,tau,T


def quantum_orbit_identities():
    rng=np.random.default_rng(71614)
    for N in (2,3,4,5,7):
        d=2*N;om=np.exp(2j*np.pi/N);V=np.diag(np.repeat(om**np.arange(N),2))
        for rank in (1,2,d):
            C=rng.normal(size=(d,rank))+1j*rng.normal(size=(d,rank));rho=C@C.conj().T;rho/=np.trace(rho)
            A,tau,T=quantum_ratio(rho,V,N)
            alpha=np.linalg.svd(T,compute_uv=False).sum();r=np.trace(rho@A)
            rootinv=psdpower(tau,-.25);middle=rootinv@T@rootinv
            assert abs(r-np.linalg.norm(middle,'fro')**2)<2e-10
            assert np.linalg.norm(A,2)<=1+2e-10
            assert np.linalg.norm(V@A@V.conj().T-om**(-1)*A)<2e-10
            assert alpha**2<=r.real+2e-10 and r.real<=alpha+2e-10
            assert abs(r.imag)<2e-10
            # Compare with the separate positive-operator compression, including null supports.
            inv=psdpower(tau,-.5);E=[inv@np.linalg.matrix_power(V,k)@rho@np.linalg.matrix_power(V.conj().T,k)@inv/N for k in range(N)]
            stack=np.vstack([psdpower(e,.5) for e in E]);D=np.kron(np.diag(om**np.arange(N)),np.eye(d))
            assert np.linalg.norm(stack.conj().T@D@stack-A)<2e-7
        # In a shift basis, diagonal input recovers the classical orbit ratio.
        Vshift=np.roll(np.eye(N),1,axis=0);f=np.exp(rng.normal(size=N));A,_,_=quantum_ratio(np.diag(f),Vshift,N)
        assert np.max(abs(np.diag(A)-ratio(f[:,None])[:,0]))<1e-12
    print('quantum_orbit_identities: full-rank and singular inputs, charged contraction, positive-operator compression and alpha squared bounds checked')


def positive_purification_control():
    for r in (2,4,8):
        plus=np.ones((r,r))/r;eye=np.eye(r)/r
        R=np.kron(eye,plus);C=np.kron(plus,eye)
        rho=np.block([[R,np.zeros_like(R)],[np.zeros_like(C),C]])/2
        V=np.kron(np.array([[0,1],[1,0]]),np.eye(r*r));sigma=V@rho@V.T
        A,tau,T=quantum_ratio(rho,V,2)
        # A direct positive purification with exactly the written register assignment.
        M=np.zeros((2*r*r,2*r))
        for i in range(r):
            for j in range(r):M[i*r+j,i]=1/np.sqrt(2*r*r);M[r*r+i*r+j,r+j]=1/np.sqrt(2*r*r)
        assert np.linalg.norm(M@M.T-rho)<1e-12
        cross=M.T@V@M
        F=np.linalg.svd(cross,compute_uv=False).sum()
        root=psdpower(rho,.5);F2=np.trace(psdpower(root@sigma@root,.5)).real
        assert abs(F-1/r)<1e-12 and abs(F2-F)<1e-7
        assert np.max(abs(np.diag(rho)-np.diag(sigma)))<1e-12
        assert abs(np.linalg.svd(T,compute_uv=False).sum()-(1-1/r))<1e-12
        assert np.linalg.norm(np.diag(T))<1e-12
        assert np.trace(rho@A).real>0
    print('positive_purification_control: identical diagonals, exact quantum fidelity 1/r, zero diagonal charged order and full optimum 1-1/r')


def all_charge_collision():
    rng=np.random.default_rng(3381)
    def entropy(rho):
        eig=eigh(rho,eigvals_only=True);eig=eig[eig>1e-12]
        return float(-np.sum(eig*np.log(eig)))
    for N in (2,3,4,5,7):
        om=np.exp(2j*np.pi/N);d=2*N;V=np.diag(np.repeat(om**np.arange(N),2))
        for rank in (1,2,d):
            C=rng.normal(size=(d,rank))+1j*rng.normal(size=(d,rank));rho=C@C.conj().T;rho/=np.trace(rho)
            orb=[np.linalg.matrix_power(V,k)@rho@np.linalg.matrix_power(V.conj().T,k) for k in range(N)];tau=sum(orb)/N;inv=psdpower(tau,-.25)
            vals=[]
            for q in range(N):
                T=sum(om**(-q*k)*orb[k] for k in range(N))/N;vals.append(np.linalg.norm(inv@T@inv,'fro')**2)
            assert abs(vals[0]-1)<1e-10
            R=sum(vals[1:]);total=np.linalg.norm(inv@rho@inv,'fro')**2-1
            D=entropy(tau)-entropy(rho)
            assert abs(R-total)<1e-10 and R<=N-1+1e-10
            assert D>=-1e-10 and D<=np.log1p(R)+1e-10 and D<=np.log(N)+1e-10
    # Order in charge2 of Z4 can be invisible in charge1.
    N=4;V=np.diag(1j**np.arange(N));psi=np.array([1,0,1,0])/np.sqrt(2);rho=np.outer(psi,psi)
    _,tau,T1=quantum_ratio(rho,V,N)
    T2=sum((-1)**k*np.linalg.matrix_power(V,k)@rho@np.linalg.matrix_power(V.conj().T,k) for k in range(N))/N
    assert np.linalg.norm(T1)<1e-12 and np.linalg.norm(T2)>.1
    print('all_charge_collision: Fourier orthogonality, entropy-to-collision bound and a charge1-blind Z4 control checked')


def blocking_gate():
    rng=np.random.default_rng(117)
    X=np.array([[0,1],[1,0]]);m=3;D=2**m
    U=np.zeros((D,D))
    for a in range(D):
        bits=[(a>>(m-1-i))&1 for i in range(m)]
        out=[bits[0]]+[b^bits[0] for b in bits[1:]]
        b=sum(x<<(m-1-i) for i,x in enumerate(out));U[b,a]=1
    Vb=np.kron(np.kron(X,X),X);assert np.linalg.norm(U@np.kron(X,np.eye(4))@U.T-Vb)<1e-12
    Ut=np.kron(U,U);Vf=np.kron(Vb,Vb);Vc=np.kron(X,X)
    def coarse(rho):
        encoded=Ut.T@rho@Ut
        # axes: coarse0, internal0, coarse1, internal1, then bra axes
        a=encoded.reshape(2,4,2,4,2,4,2,4)
        return np.einsum('aibjcidj->abcd',a).reshape(4,4)
    for _ in range(4):
        psi=rng.random(D*D);psi/=np.linalg.norm(psi);rho=np.outer(psi,psi);rhoc=coarse(rho)
        assert abs(np.trace(rhoc)-1)<1e-12 and rhoc.min()>0
        fineX=np.trace(rho.reshape(D,D,D,D),axis1=1,axis2=3)
        coarseX=np.trace(rhoc.reshape(2,2,2,2),axis1=1,axis2=3)
        _,_,Tf=quantum_ratio(fineX,Vb,2);_,_,Tc=quantum_ratio(coarseX,X,2)
        af=np.linalg.svd(Tf,compute_uv=False).sum();ac=np.linalg.svd(Tc,compute_uv=False).sum();assert ac<=af+1e-12
        Mf=np.trace((Vf@rho).reshape(D,D,D,D),axis1=0,axis2=2)
        Mc=np.trace((Vc@rhoc).reshape(2,2,2,2),axis1=0,axis2=2)
        bf=np.linalg.svd(Mf,compute_uv=False).sum();bc=np.linalg.svd(Mc,compute_uv=False).sum();assert bc<=bf+1e-12
        Pplus=np.ones((2,2))/2;Rlift=U@np.kron(Pplus,np.eye(4))@U.T
        bplus=np.trace(Pplus@Mc)
        assert abs(np.trace(np.kron(np.eye(D),Rlift)@Vf@rho)-bplus)<1e-12
        assert bplus<=bc+1e-12 and bc<=2*bplus+1e-12
    mixed=np.eye(4)/4;M=np.trace((Vc@mixed).reshape(2,2,2,2),axis1=0,axis2=2)
    assert np.linalg.norm(M)<1e-12
    print('blocking_gate: exact CNOT membrane pullback, static lower bounds, positive boundary contraction and mixed-state fidelity counterexample checked')


def approximate_blocking_gate():
    X=np.array([[0,1],[1,0]],dtype=complex);Z=np.diag([1.,-1.]);I=np.eye(2)
    rng=np.random.default_rng(181)
    for p in (.001,.03,.2):
        # Schrödinger erasure to |0>, whose adjoint is C -> <0|C|0> I.
        def phi(C):return (1-p)*C+p*C[0,0]*I
        eps=np.linalg.norm(phi(X)-X,2);assert abs(eps-p)<1e-12
        C=phi(Z);Af=(C-X@C@X)/2
        assert np.linalg.norm(Af-C,2)<=np.sqrt(2*eps)+1e-12
        assert np.linalg.norm(X@Af@X+Af)<1e-12
        assert np.linalg.norm(Af,2)<=1+1e-12
        for _ in range(5):
            R=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2));R/=np.linalg.norm(R,2)
            assert np.linalg.norm(phi(R@X)-phi(R)@X,2)<=np.sqrt(2*eps)+1e-12
            assert np.linalg.norm(phi(X@R@X)-X@phi(R)@X,2)<=2*np.sqrt(2*eps)+1e-12
    print('approximate_blocking_gate: noncovariant erasure noise, exact charge reprojection and quantitative multiplicativity penalties checked')


if __name__=='__main__':
    posterior_identities();cycle_partition();two_plaquette_auxiliary();two_plaquette_ground();fidelity_wrong_direction();quantum_orbit_identities();positive_purification_control();all_charge_collision();blocking_gate();approximate_blocking_gate()
    print('Ten finite families passed. No large-region interacting phase, native Born law, or independent review is established.')
