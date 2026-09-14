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
          raw=0.;unitary=0.;raw_a=np.zeros(dim);unitary_a=np.zeros(dim)
          for a in range(dim):
            end=dest[a]
            for middle in itertools.product(range(dim),repeat=n-1):
              vertices=(a,)+middle+(end,)
              weight=np.prod([M[vertices[k]]*K[vertices[k],vertices[k+1]] for k in range(n)])
              raw+=weight;unitary+=weight*np.sqrt(M[end]/M[a])
              raw_a[a]+=weight;unitary_a[a]+=weight*np.sqrt(M[end]/M[a])
          assert abs(raw/Z-b)<2e-12 and abs(unitary/Z-d)<2e-12
          # A fixed starting flux breaks charge-conjugation cancellation in
          # the fully summed trace and checks the actual sourced insertion.
          assert np.max(abs(raw_a/Z-np.diag(Tn@B)/Z))<2e-12
          assert np.max(abs(unitary_a/Z-np.diag(Tn@D)/Z))<2e-12
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


"""Personal finite checks of a conditional gap/perimeter estimate."""
from collections import defaultdict
import itertools
import numpy as np
from scipy.linalg import eigh
from scipy.integrate import quad

def add(p,i,n=1):
    q=list(p);q[i]+=n;return tuple(q)
def plaquette(p,i,j):
    return [(p,i,1),(add(p,i),j,1),(add(p,j),i,-1),(p,j,-1)]

def linked_clock_geometry():
    rows=[]
    for L in [1,2,3,5,8,12]:
      j=defaultdict(int)
      for x in range(-L,L):
        j[((x,-L,0),0)]+=1;j[((x,L,0),0)]-=1
      for y in range(-L,L):
        j[((L,y,0),1)]+=1;j[((-L,y,0),1)]-=1
      v={((x,0,z),1):1 for x in range(0,2*L) for z in range(-L+1,L+1)}
      div=defaultdict(int)
      for (p,i),m in j.items():div[p]-=m;div[add(p,i)]+=m
      assert not any(div.values())
      assert sum(m*v.get(e,0) for e,m in j.items())==1
      candidates=set()
      for p,i in v:
        for k in range(3):
          if k!=i:
            a,b=sorted([i,k]);candidates.add((p,a,b));candidates.add((add(p,k,-1),a,b))
      curl={}
      for p,i,k in candidates:
        m=sum(s*v.get((q,d),0) for q,d,s in plaquette(p,i,k))
        if m:curl[p,i,k]=m
      assert len(curl)==8*L and all(abs(x)==1 for x in curl.values())
      support=set((q,d) for (p,i,k),m in curl.items() for q,d,s in plaquette(p,i,k))
      def center(e):
        p,i=e;q=2*np.array(p);q[i]+=1;return q
      C=np.array([center(e) for e in j]);Y=np.array([center(e) for e in support])
      distance=np.min(np.abs(C[:,None,:]-Y[None,:,:]).sum(axis=2))/2
      assert distance>=max(0,L-1)
      # d^2=0 on every cube adjacent to the nonzero curl, exact integers.
      cubes=set()
      for p,i,k in curl:
        h=3-i-k;cubes.add(p);cubes.add(add(p,h,-1))
      def cv(p,i,k):return curl.get((p,i,k),0)
      for p in cubes:
        dd=cv(add(p,0),1,2)-cv(p,1,2)-cv(add(p,1),0,2)+cv(p,0,2)+cv(add(p,2),0,1)-cv(p,0,1)
        assert dd==0
      rows.append([L,len(j),len(v),len(curl),float(distance)])
    print('GEOMETRY L,Wilson_edges,membrane_edges,defect_plaquettes,distance=',rows)

def filter_spectral_and_algebra():
    rows=[]
    for N in [3,5,7]:
      U=np.diag(np.exp(2j*np.pi*np.arange(N)/N));V=np.roll(np.eye(N),1,axis=0).astype(complex)
      omega=np.exp(2j*np.pi/N)
      H=1.2*(2*np.eye(N)-V-V.conj().T)+.83*(np.eye(N)-(U+U.conj().T)/2)
      e,Q=eigh(H);Omega=Q[:,0];gap=e[1]-e[0];HV=V@H@V.conj().T
      # Independent exact unitary conjugation dynamics check.
      def evolved(H,O,t):
        q,R=eigh(H);Z=(R*np.exp(1j*t*q))@R.conj().T;return Z@O@Z.conj().T
      for x,y in [(.2,-.3),(.7,.4),(1.1,-.8)]:
        ux=evolved(H,U,x);vy=evolved(H,V,y)
        left=ux@vy-omega*vy@ux
        r=x-y;diff=evolved(H,U,r)-evolved(HV,U,r)
        # Undo the common tau_y and remove the final V.
        uy=evolved(H,diff@V,y)
        assert np.max(abs(left-uy))<2e-13
      u=np.vdot(Omega,U@Omega);v=np.vdot(Omega,V@Omega)
      for c,n in [(2.,1),(2.,3),(np.e,5)]:
        a=c/gap;timescale=n*a;delta=e[:,None]-e[None,:]
        mult=np.sinc(a*delta/np.pi)**n
        A=Q@(mult*(Q.conj().T@U@Q))@Q.conj().T
        B=Q@(mult*(Q.conj().T@V@Q))@Q.conj().T
        eps=c**(-n)
        assert np.linalg.norm((A-u*np.eye(N))@Omega)<=eps+1e-13
        assert np.linalg.norm((A.conj().T-u.conjugate()*np.eye(N))@Omega)<=eps+1e-13
        connected1=abs(np.vdot(Omega,A@B@Omega)-u*v)
        connected2=abs(np.vdot(Omega,B@A@Omega)-u*v)
        eta=np.linalg.norm(A@B-omega*B@A,ord=2)
        assert max(connected1,connected2)<=eps**2+1e-13
        assert abs(1-omega)*abs(u*v)<=eta+2*eps**2+1e-13
        # One-filter alternate proof, with different remainder but same
        # asymptotic gap bound after optimizing n/L.
        eta1=np.linalg.norm(A@V-omega*V@A,ord=2)
        assert abs(1-omega)*abs(u*v)<=eta1+2*eps+1e-13
        rows.append([N,c,n,float(gap),float(eta),float(connected1)])
      # n=2 convolution is triangular; quadrature independently verifies
      # the matrix-element multiplier at representative nonzero gaps.
      a=2/gap
      for E in [gap,2.7*gap,5.1*gap]:
        val=quad(lambda t:(2*a-abs(t))/(4*a*a)*np.cos(E*t),-2*a,2*a,epsabs=1e-12,points=[0])[0]
        assert abs(val-np.sinc(a*E/np.pi)**2)<2e-13
    print('FILTER N,c,n,gap,twisted_error,connected=',rows)


AUDIT_TIMEOUT_SEC = 90

def degenerate_ground_sectors():
    N=3
    Z=np.diag(np.exp(2j*np.pi*np.arange(N)/N));X=np.roll(np.eye(N),1,axis=0)
    h=1.2*(2*np.eye(N)-X-X.T)+.83*(np.eye(N)-(Z+Z.conj().T)/2)
    e,Q=eigh(h);q=Q[:,0];chi=np.array([1.,2.]);chi/=np.linalg.norm(chi)
    H=np.kron(h,np.eye(2));U=np.kron(Z,np.eye(2));V=np.kron(X,np.diag([1.,-1.]))
    Omega=np.kron(q,chi);P0=np.kron(np.outer(q,q.conj()),np.eye(2))
    u=np.vdot(Omega,U@Omega);v=np.vdot(Omega,V@Omega)
    assert np.linalg.norm(P0@U@Omega-u*Omega)<1e-13
    assert np.linalg.norm(P0@U.conj().T@Omega-u.conjugate()*Omega)<1e-13
    assert np.linalg.norm(P0@V@Omega-v*Omega)>.1
    E,R=eigh(H);a=np.e/(e[1]-e[0]);n=4
    A=R@(np.sinc(a*(E[:,None]-E[None,:])/np.pi)**n*(R.conj().T@U@R))@R.conj().T
    omega=np.exp(2j*np.pi/N);eps=np.e**(-n)
    assert max(abs(np.vdot(Omega,A@V@Omega)-u*v),abs(np.vdot(Omega,V@A@Omega)-u*v))<=eps+1e-13
    assert abs(1-omega)*abs(u*v)<=2*eps+np.linalg.norm(A@V-omega*V@A,2)+1e-13
    # Adverse control: filtering does not remove a nonscalar ground-space component.
    Hbad=np.diag([0.,0.,1.]);Ubad=np.array([[0.,1.,0.],[1.,0.,0.],[0.,0.,1.]])
    Obad=np.array([1.,0.,0.]);Abad=np.sinc(np.e*(np.diag(Hbad)[:,None]-np.diag(Hbad)[None,:])/np.pi)**n*Ubad
    assert np.linalg.norm(Abad@Obad)==1 and 1>eps
    print('DEGENERACY: scalar Wilson compression sufficient; nonscalar ground leakage survives filtering.')

if __name__=='__main__':
    for f in [two_plaquette_transfer,algebra_countercheck,linked_clock_geometry,filter_spectral_and_algebra,degenerate_ground_sectors]:
        f();print('PASS',f.__name__,flush=True)
    print('TOTAL: 5 substantive scientific check families passed; author evidence only.')
    print('per_element: exact Weyl phases and independent temporal seam path sums distinguish unitary and weighted insertions.')
    print('per_site: integer link cochains and all boundary plaquette supports establish the linked-loop separation.')
    print('per_mode: spectral sinc multipliers are compared with triangular time quadrature and both ordered correlations.')
    print('per_block: ground-space compression, nonscalar leakage, transfer positivity and the exact twisted dynamical identity are checked.')
    print('lattice_wide: checked and not executed — the asymptotic spectral-gap implication uses the written conditional proof; no infinite-volume clock phase or photon pole is computed.')
