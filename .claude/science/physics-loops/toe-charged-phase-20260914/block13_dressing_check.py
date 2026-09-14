"""Finite falsifiers of loop optimization and defect-path hypotheses."""
import itertools
import numpy as np
from scipy.linalg import eigh,svd,svdvals
from scipy.sparse import kron as skron,eye as seye,csr_matrix
from scipy.sparse.linalg import eigsh

def reduce_cross(phi,psi,dims,keep):
    rest=[i for i in range(len(dims)) if i not in keep]
    d=int(np.prod([dims[i] for i in keep]));perm=keep+rest
    A=phi.reshape(dims).transpose(perm).reshape(d,-1)
    B=psi.reshape(dims).transpose(perm).reshape(d,-1)
    return A@B.conj().T

def polar_partial(T):
    U,s,Vh=svd(T);good=s>1e-12
    return U[:,good]@Vh[good,:]

def root_fidelity(rho,sigma):
    e,Q=eigh(rho);good=e>1e-12;Q=Q[:,good];a=np.sqrt(e[good])
    small=a[:,None]*(Q.conj().T@sigma@Q)*a[None,:]
    return float(np.sqrt(np.maximum(eigh(small,eigvals_only=True),0)).sum())

def optimal_charged_and_dressed():
    rng=np.random.default_rng(91314);rows=[]
    for N in [3,4,5,7]:
      dims=[N*2,2,N];omega=np.exp(2j*np.pi/N)
      G=np.kron(np.diag(omega**np.arange(N)),np.eye(2))
      Vrest=np.roll(np.eye(N),1,axis=0)
      V=np.kron(np.kron(G,np.eye(2)),Vrest)
      psi=rng.normal(size=(N,2,2,N))+1j*rng.normal(size=(N,2,2,N))
      # Exact +1 Gauss fixture: ancillary X-region and Y-region parities agree.
      psi[:,0,1,:]=0;psi[:,1,0,:]=0;psi=psi.ravel();psi/=np.linalg.norm(psi)
      rho=reduce_cross(psi,psi,dims,[0])
      T=sum(omega**(-k)*np.linalg.matrix_power(G,k)@rho@np.linalg.matrix_power(G.conj().T,k) for k in range(N))/N
      A=polar_partial(T).conj().T;alpha=svdvals(T).sum()
      assert np.linalg.norm(G@A@G.conj().T-omega.conjugate()*A,2)<2e-12
      assert abs(np.trace(rho@A)-alpha)<2e-12
      gauge=np.kron(np.eye(N),np.diag([1.,-1.]))
      assert np.linalg.norm(A@gauge-gauge@A,2)<2e-12
      # Independent block formula: Fourier component maps sector r to r+1.
      blocks=sum(svdvals(rho[2*((r+1)%N):2*((r+1)%N)+2,2*r:2*r+2]).sum() for r in range(N))
      assert abs(alpha-blocks)<2e-12
      phi=V@psi;M=reduce_cross(phi,psi,dims,[1]);Q,s,Rh=svd(M)
      R=Rh.conj().T@Q.conj().T;beta=s.sum()
      fullA=np.kron(A,np.eye(2*N));fullR=np.kron(np.kron(np.eye(2*N),R),np.eye(N));B=fullR@V
      assert np.linalg.norm(R.conj().T@R-np.eye(2))<2e-12
      assert np.linalg.norm(R@np.diag([1.,-1.])-np.diag([1.,-1.])@R)<2e-12
      assert abs(np.vdot(psi,B@psi)-beta)<2e-12
      fidelity=root_fidelity(reduce_cross(psi,psi,dims,[0,2]),reduce_cross(phi,phi,dims,[0,2]))
      assert abs(beta-fidelity)<2e-10
      assert np.linalg.norm(fullA@B-omega*B@fullA,2)<3e-12
      assert np.sin(np.pi/N)**2*alpha**2*beta**2<=(1-alpha**2)*(1-beta**2)+2e-12
      rows.append([N,float(alpha),float(beta),fidelity])
    print('OPTIMA N,charged_trace_norm,boundary_overlap,complement_fidelity=',rows)

def strip_incidence(L):
    vertices=list(itertools.product(range(L+1),range(2)))
    edges=[((i,y),(i+1,y)) for y in range(2) for i in range(L)]
    edges += [((i,0),(i,1)) for i in range(L+1)]
    ids={e:i for i,e in enumerate(edges)};D=np.zeros((len(vertices),len(edges)),dtype=int)
    for k,(a,b) in enumerate(edges):D[vertices.index(a),k]=-1;D[vertices.index(b),k]=1
    F=np.zeros((len(edges),L),dtype=int)
    for i in range(L):
      for a,b,sign in [((i,0),(i+1,0),1),((i+1,0),(i+1,1),1),((i,1),(i+1,1),-1),((i,0),(i,1),-1)]:F[ids[a,b],i]=sign
    assert not np.any(D@F)
    return D,F

def pauli_sites(L,sparse=False):
    X=np.array([[0.,1.],[1.,0.]]);Z=np.diag([1.,-1.]);I=np.eye(2)
    def op(i,M):
      a=csr_matrix([[1.]]) if sparse else np.ones((1,1))
      for k in range(L):a=skron(a,csr_matrix(M if k==i else I),format='csr') if sparse else np.kron(a,M if k==i else I)
      return a
    return [op(i,X) for i in range(L)],[op(i,Z) for i in range(L)]

def gauge_strip_reduction():
    rows=[];t=.9;K=.43
    for L in [1,2,3,4]:
      D,F=strip_incidence(L);m=F.shape[0]
      states=np.array(list(itertools.product(range(2),repeat=L)));currents=states@F.T%2
      enumerated={tuple(e) for e in itertools.product(range(2),repeat=m) if not np.any(D@e%2)}
      assert enumerated==set(map(tuple,currents)) and len(enumerated)==2**L
      j=F@np.ones(L,dtype=int);assert np.count_nonzero(j)==2*L+2
      X,Z=pauli_sites(L);I=np.eye(2**L)
      for s in [0.,.23,.5,1.]:
        diag=2*t*np.sum(1-np.cos(np.pi*(currents+s*j)),axis=1)+K*L
        microscopic=np.diag(diag)
        for i in range(L):
          for a,n in enumerate(states):
            nxt=n.copy();nxt[i]^=1;b=sum(int(x)*2**(L-1-k) for k,x in enumerate(nxt));microscopic[b,a]-=K
        ising=(2*t*m+K*L)*I-2*t*sum((Z[i]@Z[i+1] for i in range(L-1)),np.zeros_like(I))-2*t*np.cos(np.pi*s)*(2*sum(Z)+Z[0]+Z[-1])-K*sum(X)
        err=np.max(abs(microscopic-ising));assert err<1e-12
      rows.append([L,m,len(enumerated)])
    print('GAUSS STRIP L,links,physical_dimension=',rows)

def strong_zero_mode():
    rows=[]
    for L in [2,3,5,8]:
      X,Z=pauli_sites(L);I=np.eye(2**L);P=np.linalg.multi_dot(X) if L>2 else X[0]@X[1]
      for g in [.2,.55,.8]:
        J=1.3;h=J*g;H=-J*sum((Z[i]@Z[i+1] for i in range(L-1)),np.zeros_like(I))-h*sum(X)
        c=np.sqrt((1-g*g)/(1-g**(2*L)));Gamma=np.zeros_like(I);prefix=I.copy()
        for i in range(L):Gamma+=c*g**i*prefix@Z[i];prefix=prefix@X[i]
        assert np.max(abs(Gamma@Gamma-I))<2e-13
        assert np.max(abs(Gamma@P+P@Gamma))<2e-13
        error=np.linalg.norm(H@Gamma-Gamma@H,2);bound=2*J*c*g**L
        assert abs(error-bound)<2e-12
        # Resolve exact parity blocks: an unrestricted eigensolver mixes the
        # exponentially close pair by roundoff divided by the small gap.
        half=2**(L-1);plus=np.zeros((2**L,half));minus=plus.copy()
        for k in range(half):
          plus[k,k]=plus[-1-k,k]=1/np.sqrt(2)
          minus[k,k]=1/np.sqrt(2);minus[-1-k,k]=-1/np.sqrt(2)
        ep,Qp=eigh(plus.T@H@plus);em=eigh(minus.T@H@minus,eigvals_only=True)
        ground=ep[0];gap=min(em[0],ep[1])-ground;psi=plus@Qp[:,0];trial=Gamma@psi
        assert np.linalg.norm(H@psi-ground*psi)<2e-12
        assert abs(np.vdot(psi,trial))<2e-13
        ray=float(np.vdot(trial,H@trial)-ground);assert gap<=ray+2e-12 and ray<=bound+2e-12
        # Free-Majorana spectrum is an independent 2L-dimensional route.
        C=np.diag(np.full(L,h))+np.diag(np.full(L-1,J),-1)
        freegap=2*svdvals(C)[-1];assert abs(gap-freegap)<3e-12
        rows.append([L,g,float(gap),bound])
    # Large strips require no exponentially large Hilbert matrix.
    for L in [16,32,64,128]:
      g=.8;J=1.3;C=np.diag(np.full(L,J*g))+np.diag(np.full(L-1,J),-1)
      gap=2*svdvals(C)[-1];bound=2*J*np.sqrt((1-g*g)/(1-g**(2*L)))*g**L
      assert gap<=bound+3e-15;rows.append([L,g,float(gap),bound])
    print('DEFECT GAP L,g,exact_gap,zero_mode_upper_bound=',rows)

def defect_paths_and_commutator():
    rows=[]
    for N in [3,5,7]:
      theta=2*np.pi/N;omega=np.exp(1j*theta);U=np.diag(omega**np.arange(N));V=np.roll(np.eye(N),1,axis=0)
      I=np.eye(N);t=1.2;K=.83
      def HE(s):return t*(2*I-np.exp(1j*s*theta)*V-np.exp(-1j*s*theta)*V.T)+K*(I-(U+U.conj().T)/2)
      def HB(s):return t*(2*I-V-V.T)+K*(I-(np.exp(-1j*s*theta)*U+np.exp(1j*s*theta)*U.conj().T)/2)
      assert np.max(abs(HE(1)-U@HE(0)@U.conj().T))<1e-12
      assert np.max(abs(HB(1)-V@HB(0)@V.T))<1e-12
      for s in [0.,.25,.5,.8,1.]:
        derivative=t*(-1j*theta*np.exp(1j*s*theta)*V+1j*theta*np.exp(-1j*s*theta)*V.T)
        assert np.max(abs(derivative@V-V@derivative))<1e-13
        assert np.max(abs(V@HE(s)@V.T-HE(s)-(V@HE(0)@V.T-HE(0))))<1e-12
      gaps=[min(np.diff(eigh(H(s),eigvals_only=True))[:1]) for H in [HE,HB] for s in np.linspace(0,1,51)]
      assert min(gaps)>.01
      # No separation: both one-site paths stay gapped on this checked grid.
      # Also isolate the electric-flow neutrality term in the algebra bound.
      SE=U;SB=I;A=SE.conj().T@U;B=SB.conj().T@V
      residual=np.linalg.norm(A@B-omega*B@A,2)
      missing=np.linalg.norm(U@SB-SB@U,2)+np.linalg.norm(SE@SB-SB@SE,2)
      needed=np.linalg.norm(SE@V-V@SE,2)
      assert residual>missing+.1 and residual<=missing+needed+1e-12
      rows.append([N,float(min(gaps)),float(residual),float(needed)])
    print('PATH FIXTURES N,min_grid_gap,twisted_residual,required_neutrality_error=',rows)

if __name__=='__main__':
    for f in [optimal_charged_and_dressed,gauge_strip_reduction,strong_zero_mode,defect_paths_and_commutator]:
        f();print('PASS',f.__name__,flush=True)
