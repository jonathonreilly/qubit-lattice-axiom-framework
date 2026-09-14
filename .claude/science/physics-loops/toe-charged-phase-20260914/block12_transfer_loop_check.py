"""Exact finite-source/loop-algebra checks, not a thermodynamic phase test."""
import itertools
import numpy as np
from scipy.linalg import eigh

def two_plaquette_transfer():
    rows=[]
    # Two squares sharing one edge: 3 private boundary edges each, 1 shared.
    # Independent link increments push forward to the two plaquette curls.
    incidence=np.array([[1,1,1,0,0,0,1],[0,0,0,1,1,1,-1]],dtype=int)
    for N in [2,3,5]:
      bt=.73;bs=.81;theta=2*np.pi*np.arange(N)/N
      w=np.exp(bt*np.cos(theta));w/=w.sum()
      p=np.zeros((N,N))
      for z in itertools.product(range(N),repeat=7):
        z=np.array(z);r=incidence@z%N;p[tuple(r)]+=np.prod(w[z])
      lam=np.fft.fft(w).real
      eigen=np.array([[lam[q]**3*lam[r]**3*lam[(q-r)%N] for r in range(N)] for q in range(N)])
      predicted=np.fft.ifft2(eigen).real
      assert np.max(abs(p-predicted))<1e-13
      flux=np.array(list(itertools.product(range(N),repeat=2)));dim=N*N
      index={tuple(x):i for i,x in enumerate(flux)}
      K=np.array([[p[tuple((a-b)%N)] for b in flux] for a in flux])
      M=np.exp(bs*np.cos(2*np.pi*flux/N).sum(axis=1));root=np.sqrt(M)
      T=root[:,None]*K*root[None,:]
      assert eigh(T,eigvals_only=True)[0]>0
      for dv in [np.array([1,0]),np.array([1,-1])]:
        dest=np.array([index[tuple((a+dv)%N)] for a in flux])
        D=np.eye(dim)[dest].T
        B=D*root[None,:]/root[:,None]
        W=np.diag(np.exp(2j*np.pi*flux[:,0]/N));omega=np.exp(2j*np.pi*dv[0]/N)
        assert np.max(abs(W@D-omega*D@W))<1e-13
        assert np.max(abs(D.T@D-np.eye(dim)))<1e-13
        A=bs*np.sum(abs(np.sin(np.pi*dv/N)))
        for n in [2,3]:
          Tn=np.linalg.matrix_power(T,n);Z=np.trace(Tn)
          d=np.trace(Tn@D)/Z;b=np.trace(Tn@B)/Z
          # Direct temporally twisted path sum: start a, end a+dv,
          # and weight M once on each of the n intermediate/start slices.
          raw=0.;unitary=0.
          for a in range(dim):
            end=dest[a]
            for middle in itertools.product(range(dim),repeat=n-1):
              vertices=(a,)+middle+(end,)
              weight=np.prod([M[vertices[k]]*K[vertices[k],vertices[k+1]] for k in range(n)])
              raw+=weight;unitary+=weight*np.sqrt(M[end]/M[a])
          assert abs(raw/Z-b)<2e-12 and abs(unitary/Z-d)<2e-12
          assert np.exp(-A)*b<=d+1e-13 and d<=np.exp(A)*b+1e-13
          rows.append([N,dv.tolist(),n,float(d),float(b),float(A)])
    print('TRANSFER N,curl_v,slices,unitary_D,raw_seam_B,A=',rows)

def algebra_countercheck():
    out=[]
    for N in [3,5,7]:
      U=np.diag(np.exp(2j*np.pi*np.arange(N)/N));V=np.roll(np.eye(N),1,axis=0)
      omega=np.exp(2j*np.pi/N)
      assert np.max(abs(U@V-omega*V@U))<1e-13
      for L in [1,3,9]:
        a=.1*np.exp(-.31*L);b=.1*np.exp(-.47*L)
        rho=(np.eye(N)+a*(U+U.conj().T)+b*(V+V.T))/N
        val,Q=eigh(rho);assert val[0]>0 and abs(np.trace(rho)-1)<1e-13
        av=np.trace(rho@U);bv=np.trace(rho@V)
        assert abs(av-a)<1e-13 and abs(bv-b)<1e-13
        err=max(abs(np.trace(rho@U@V)-av*bv),abs(np.trace(rho@V@U)-av*bv))
        assert abs(1-omega)*abs(av*bv)<=2*err+1e-13
        psi=sum(np.sqrt(val[j])*np.kron(Q[:,j],np.eye(N)[:,j]) for j in range(N))
        H=np.eye(N*N)-np.outer(psi,psi.conj());energy=eigh(H,eigvals_only=True)
        assert abs(energy[0])<1e-13 and abs(energy[1]-1)<1e-13
        out.append([N,L,float(a),float(b),float(err),float(energy[1]-energy[0])])
    print('ALGEBRA ONLY N,L,a,b,connected_error,gap=',out)

if __name__=='__main__':
    for f in [two_plaquette_transfer,algebra_countercheck]:
        f();print('PASS',f.__name__,flush=True)
