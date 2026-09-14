"""Working falsifiers only. No fixed-payload photon-phase theorem."""
import numpy as np
from scipy.linalg import eigh
from scipy.special import ive
from math import pi,sqrt,exp,log,asinh,ceil

def tube_and_closed_loop():
    from scipy.integrate import quad
    for u,v in [(1.,1.),(.1,10.),(.001,30.)]:
        G0=1/sqrt(u*(u+4*v));q=(u+2*v-sqrt(u*(u+4*v)))/(2*v)
        for r in [0,1,3,10]:
            z=quad(lambda k:np.cos(r*k)/(u+2*v*(1-np.cos(k))),-pi,pi,epsabs=1e-9)[0]/(2*pi)
            assert abs(z-G0*q**r)<1e-7
        assert abs(G0*(1-q)-(1-u*G0)/(2*v))<1e-12
    # Full anisotropic Gaussian gauge precision at each four-momentum.
    rng=np.random.default_rng(240914);largest=0.
    for bt,bs in [(1,1),(10,.01),(30,1e-6)]:
      for _ in range(20):
        k=rng.uniform(.15,2.9,4);d=np.exp(1j*k)-1;forms=[];weights=[]
        for i in range(4):
          for j in range(i+1,4):
            row=np.zeros(4,complex);row[j]=d[i];row[i]=-d[j];forms.append(row);weights.append(bt if i==0 else bs)
        D=np.array(forms);Q=D.conj().T@np.diag(weights)@D;Qi=np.linalg.pinv(Q,rcond=1e-12)
        observed=(D[0]@Qi@D[0].conj()).real
        ss=np.sum(abs(d[1:])**2);w=abs(d[1])**2/ss;s0=abs(d[0])**2
        predicted=(1-w)*s0/(bt*s0+bs*ss)+w/bt
        largest=max(largest,abs(observed-predicted));assert abs(observed-predicted)<1e-9
        assert observed<=1/bt+1e-10
    print('TUBE full closed temporal-plaquette covariance residual=',largest)

def gaussian_square_completion():
    from scipy.integrate import quad
    beta=2.;n=6;rho=3.
    Z=quad(lambda x:exp(-n*x*x/(2*beta)),-10,10)[0]
    val=quad(lambda x:exp(-n*x*x/(2*beta))*np.cos(rho*x),-10,10)[0]/Z
    assert abs(val-exp(-beta*rho*rho/(2*n)))<1e-13
    assert abs(val-exp(-beta*rho*rho/n))>.1
    print('GAUSSIAN preprint normalization discrepancy=',val,exp(-beta*rho*rho/n))

def blocked_skellam():
    rows=[]
    for N in [16,32,64,128,256,512]:
      c=.25;T=c*N;q=np.arange(N);q=np.where(q>N//2,q-N,q)
      eig=np.exp(-2*T*(1-np.cos(2*pi*q/N)));p=np.fft.ifft(eig).real
      r=np.arange(N);r=np.where(r>N//2,r-N,r)
      direct=sum(ive(abs(r+m*N),2*T) for m in range(-4,5))
      assert np.max(abs(p-direct))<1e-14 and abs(p.sum()-1)<1e-13
      g=sum(np.exp(-(r+m*N)**2/(4*T)) for m in range(-4,5));g/=g.sum()
      tv=.5*np.sum(abs(p-g));a=4*pi*pi*c/N;b=16*c/N;M=N//2
      # Uniform Fourier-error bound; the reflected Gaussian aliases are retained.
      central=(4/3)*c*pi**4/N**3*(3*sqrt(pi)/(4*b**2.5)+8*exp(-2)/b**2)
      alias=2*exp(-a*M*M)/(1-exp(-a*(2*M+1)))+2*exp(-a*N*N)/(1-exp(-3*a*N*N))*(1+sqrt(pi/a))
      B=central+alias
      assert np.max(abs(p-g))<=B/N+1e-14
      R=min(N//2-1,ceil(sqrt(12*c*N*log(N))))
      rate=R*asinh(R/(2*T))-2*T*(sqrt(1+(R/(2*T))**2)-1)
      bound=min(B/2,(2*R+1)*B/(2*N)+exp(-rate)+.5*exp(-R*R/(4*T)))
      assert tv<=bound+1e-13
      rows.append([N,float(tv),float(bound),float(N*tv)])
    print('SKELLAM N, actual_TV, derived_bound, N_TV=',rows)

def coupled_clock_block():
    # Actual single plaquette reduced clock. The coefficient a can be4t for
    # a square's four electric links. Here a=b=1 sets the comparison units.
    rows=[]
    for c in [.1,.3]:
      Omega=2*pi*c*sqrt(2);gamma=2*asinh(Omega/2)
      gap_limit=gamma/Omega;variance_limit=1/sqrt(1+Omega**2/4)
      for N in [32,64,128,256]:
        a=b=1.;T=c*N;theta=2*pi*np.arange(N)/N;theta=np.where(theta>pi,theta-2*pi,theta)
        X=np.roll(np.eye(N),1,axis=0);E=a*(2*np.eye(N)-X-X.T);V=b*(1-np.cos(theta));H=E+np.diag(V)
        en,U=eigh(H);gap=en[1]-en[0]
        ev=np.exp(-T*2*a*(1-np.cos(2*pi*np.arange(N)/N)))
        col=np.fft.ifft(ev).real;PE=np.array([[col[(i-j)%N] for j in range(N)] for i in range(N)])
        w=np.exp(-T*V/2);S=w[:,None]*PE*w[None,:]
        lam,Q=eigh(S);block_gap=log(lam[-1]/lam[-2])/T
        truevar=np.sum(theta**2*abs(U[:,0])**2);blockvar=np.sum(theta**2*abs(Q[:,-1])**2)
        grat=block_gap/gap;vrat=blockvar/truevar
        assert abs(grat-gap_limit)<4/N and abs(vrat-variance_limit)<4/N
        rows.append([c,N,float(grat),gap_limit,float(vrat),variance_limit])
    assert abs(rows[-1][2]-1)>.1
    print('COUPLED c,N,gap_ratio,limit,variance_ratio,limit=',rows)

if __name__=='__main__':
    for f in [gaussian_square_completion,tube_and_closed_loop,blocked_skellam,coupled_clock_block]:
        f();print('PASS',f.__name__,flush=True)
