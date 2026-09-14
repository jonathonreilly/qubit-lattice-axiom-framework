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

if __name__=='__main__':
    for f in [linked_clock_geometry,filter_spectral_and_algebra]:
        f();print('PASS',f.__name__,flush=True)
