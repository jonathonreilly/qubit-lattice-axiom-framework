"""Finite transfer-kernel diagnostics for the additional actions in arXiv2505.00079v2."""
import itertools
import numpy as np
from scipy.linalg import eigh,expm
from fractions import Fraction


def z4_single_link():
    for beta,beta2 in ((1.514,-.393),(1.4,-.407),(1.6,-.379)):
        r=np.arange(4);w=np.exp(beta*np.cos(np.pi*r/2)+beta2*np.cos(np.pi*r));lam=np.fft.fft(w).real/4
        expected=np.array([(np.exp(beta2)*np.cosh(beta)+np.exp(-beta2))/2,np.exp(beta2)*np.sinh(beta)/2,(np.exp(beta2)*np.cosh(beta)-np.exp(-beta2))/2,np.exp(beta2)*np.sinh(beta)/2])
        assert np.max(abs(lam-expected))<1e-12
        packet={'beta':beta,'beta2':beta2,'lambda':lam.tolist(),'positive_kernel':bool(lam.min()>0)}
        if lam.min()>0:
            energy=-np.log(lam/lam[0]);t1=energy[2]/4;t2=(energy[1]-2*t1)/4
            H=np.fft.ifft(np.fft.fft(np.eye(4),axis=0)*energy[:,None],axis=0).real
            # Rebuild in the actual coordinate basis independently.
            X=np.roll(np.eye(4),1,axis=0);direct=t1*(2*np.eye(4)-X-X.T)+t2*(2*np.eye(4)-X@X-(X@X).T)
            assert np.max(abs(H-direct))<1e-12
            assert expm(-.001*H)[0,2]<0
            packet.update(energies=energy.tolist(),t1=float(t1),t2=float(t2),offdiag_two_step=float(H[0,2]))
        print('z4_link',packet)
    edges=[(0,1),(1,2),(3,4),(4,5),(0,3),(1,4),(2,5)]
    D=np.zeros((6,7),int)
    for l,(x,y) in enumerate(edges):D[x,l]=-1;D[y,l]=1
    F=np.array([[1,0,-1,0,-1,1,0],[0,1,0,-1,0,-1,1]])
    j=(F.T@np.array([1,3]))%4;assert np.all((D@j)%4==0)
    coeff=[Fraction(17,12),Fraction(1,3),Fraction(-7,12),Fraction(1,3)]
    eigen=Fraction(1)
    for q in j:eigen*=coeff[q]
    assert eigen==Fraction(-7,8748)
    print('exact_physical_negative_transfer',j.tolist(),str(eigen))


def monopole_prism():
    for N in (3,):
        F=np.array([[1,0,-1,0,-1,1,0],[0,1,0,-1,0,-1,1]])
        delta=np.array(list(itertools.product(range(N),repeat=7)))
        def principal(a):return (a+N//2)%N-N//2
        pd=principal(delta);fd=(F@delta.T).T%N;lift=(F@pd.T).T
        bs=np.array(list(itertools.product(range(N),repeat=2)));pb=principal(bs)
        for beta in (.1,.265,.5114,1.,2.):
            temporal=np.exp(beta*np.cos(2*np.pi*delta/N).sum(axis=1))
            for mu in (0.,.3,1.,3.,10.):
                K=np.zeros((N*N,N*N))
                for i,b in enumerate(bs):
                    for j,bp in enumerate(bs):
                        keep=np.all(fd==(bp-b)%N,axis=1)
                        monop=(pb[j]-pb[i]-lift[keep])/N
                        assert np.max(abs(monop-np.rint(monop)))<1e-12
                        K[i,j]=np.sum(temporal[keep]*np.exp(-mu*np.sum(monop**2,axis=1)))
                assert np.linalg.norm(K-K.T)<1e-9*np.linalg.norm(K)
                eig=eigh(K,eigvals_only=True);print('z3_two_plaquette_prism',beta,mu,float(eig[0]/eig[-1]))
    print('These finite kernels do not establish positivity on arbitrary spatial complexes or an infrared phase.')


if __name__=='__main__':z4_single_link();monopole_prism()
