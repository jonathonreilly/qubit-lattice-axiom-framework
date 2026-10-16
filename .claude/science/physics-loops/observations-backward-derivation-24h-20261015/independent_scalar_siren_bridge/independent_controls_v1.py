"""Independent synthetic scalar-siren controls; no author imports or raw data."""
import sys, json, math, hashlib
from pathlib import Path
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp, quad
HERE=Path(__file__).resolve().parent
checks=[]; rows=[]
def ck(name, ok, **detail):
    checks.append(dict(name=name,passed=bool(ok),**detail))
def exact(name, expr):
    val=sp.simplify(expr);ck(name,val==0,expression=str(val))
# Non-axis-aligned rational null direction and TT polarization.
n=sp.Matrix([sp.Rational(2,3),sp.Rational(1,3),sp.Rational(2,3)])
p=sp.Matrix([sp.Rational(2,3),-sp.Rational(2,3),-sp.Rational(1,3)])
q=sp.Matrix([sp.Rational(1,3),sp.Rational(2,3),-sp.Rational(2,3)])
g=sp.diag(-1,1,1,1);k=sp.Matrix([-1,*n]);b=sp.Matrix(sp.symbols('b0:4'))
T=b*k.T+k*b.T-g*(b.T*g*k)[0]
for label,screen in [('plus',p*p.T-q*q.T),('cross',p*q.T+q*p.T)]:
    e=sp.zeros(4);e[1:4,1:4]=screen
    exact('TT arbitrary-gradient '+label,sp.trace(e.T*T))
    exact('TT transverse '+label,(e*k).dot(e*k))
    exact('TT trace '+label,sp.trace(e*g))
F,Fs,om=sp.symbols('F Fs om',positive=True)
exact('canonical kinetic coefficient',Fs*(2*om+3)/(4*F**2)-(Fs*om/(2*F**2)+3*Fs/(4*F**2)))
O=sp.symbols('O',positive=True);exact('four-dimensional current weight',O**4*O**(-2)-O**2)
t,mu,r,w=sp.symbols('t mu r w',positive=True);v=sp.Matrix([r*sp.cos(w*t),r*sp.sin(w*t),0]);I=mu*(v*v.T-sp.eye(3)*r*r/3)
I3=I.diff(t,3);exact('circular quadrupole contraction',sp.trigsimp(sum(I3[i,j]**2 for i in range(3)for j in range(3)))-32*mu**2*r**4*w**6)
GT,Gc,M,eta=sp.symbols('GT Gc M eta',positive=True)
E=-mu*(Gc*M)**sp.Rational(2,3)*w**sp.Rational(2,3)/2
PT=sp.Rational(32,5)*GT*mu**2*(Gc*M)**sp.Rational(4,3)*w**sp.Rational(10,3)
exact('Gc distinct source balance',-(1+eta)*PT/sp.diff(E,w)-sp.Rational(96,5)*GT*mu*(Gc*M)**sp.Rational(2,3)*w**sp.Rational(11,3)*(1+eta))
K,rho,DL,a,eta0,beta,wref=sp.symbols('K rho DL a eta0 beta wref',positive=True)
loss=eta0+beta*(w/wref)**sp.Rational(-2,3)
H=4*K*w**sp.Rational(2,3)*sp.sqrt(rho)/DL;wdot=sp.Rational(96,5)*K*w**sp.Rational(11,3)*(1+loss)
exact('distance ratio',sp.Rational(5,24)*wdot/(H*w**3)-DL*(1+loss)/sp.sqrt(rho))
exact('constant plus dipole chirp ambiguity',wdot.subs({K:K/a,eta0:a*(1+eta0)-1,beta:a*beta},simultaneous=True)-wdot)
exact('amplitude ambiguity',H.subs({K:K/a,rho:a*a*rho},simultaneous=True)-H)
x=sp.symbols('x',real=True);S=10*x**3-15*x**4+6*x**5;B=64*x**3*(1-x)**3
exact('S prime squared integral',sp.integrate(sp.diff(S,x)**2,(x,0,1))-sp.Rational(10,7))
# A separate correlated-endpoint family, checking conservative interval mapping.
qlo,qhi,elo,ehi,xslo,xshi,xolo,xohi=.8,1.1,.1,.4,-.2,.3,.05,.2
lower=2*math.log(qlo)+2*math.log1p(elo)-xshi+xolo
upper=2*math.log(qhi)+2*math.log1p(ehi)-xslo+xohi
vals=[]
for z in np.linspace(0,1,41):
    qq=qlo+(qhi-qlo)*z; ee=ehi-(ehi-elo)*z*z; xs=xslo+(xshi-xslo)*z; xo=xohi-(xohi-xolo)*z
    vals.append(2*math.log(qq)+2*math.log1p(ee)-xs+xo)
ck('correlated registration conservative box',min(vals)>=lower and max(vals)<=upper,lower=lower,upper=upper,actual_min=min(vals),actual_max=max(vals))
# Physical flux-coordinate generator, distinct from transformed-u author ODE.
def profile(x,a,b,scale=1.):
    S=10*x**3-15*x**4+6*x**5;Sp=30*x*x*(1-x)**2;Spp=60*x*(1-x)*(1-2*x)
    B=64*x**3*(1-x)**3;Bp=192*x*x*(1-x)**2*(1-2*x);Bpp=384*x*(1-x)*((1-2*x)**2-x*(1-x))
    den=1+b*B; FF=scale*np.exp(a*S)*den*den
    LLp=a*Sp+2*b*Bp/den
    Q=a*Spp/2+a*a*Sp*Sp/4+(a*b*Sp*Bp+b*Bpp)/den
    return FF,LLp,Q

def scatter(M,k,Fl=1.,Fr=1.):
    incoming=np.array([1,1j*k*Fl]); reflected=np.array([1,-1j*k*Fl]);outgoing=np.exp(1j*k)*np.array([1,1j*k*Fr])
    rr,tt=np.linalg.solve(np.column_stack((M@reflected,-outgoing)),-M@incoming)
    return rr,tt

def physical(a,b,k,scale=1.):
    def fun(x,y):
        F=profile(x,a,b,scale)[0];J=np.array([[0,1/F],[-k*k*F,0]])
        return (J@y.reshape((2,2))).reshape(-1)
    sol=solve_ivp(fun,[0,1],np.eye(2).reshape(-1),method='Radau',rtol=3e-11,atol=3e-13,dense_output=True)
    if not sol.success:raise RuntimeError(sol.message)
    MM=sol.y[:,-1].reshape((2,2));Fl=scale;Fr=scale*np.exp(a);rr,th=scatter(MM,k,Fl,Fr)
    return sol,rr,th,MM

def layers(a,b,k,count):
    dx=1/count;xx=(np.arange(count)+.5)*dx;Q=profile(xx,a,b)[2];lam=k*k-Q
    z=np.sqrt(lam.astype(complex))*dx;co=np.cos(z).real;si=(dx*np.sinc(z/np.pi)).real
    A=np.eye(2)
    for c,s,l in zip(co,si,lam):A=np.array([[c,s],[-l*s,c]])@A
    return scatter(A,k)

def cpair(z):return [float(z.real),float(z.imag)]
for a,b in [(.45,.30),(-.55,-.20),(0.,.65)]:
    denom=1+min(b,0);Jupper=abs(a)*15/8+a*a*5/14+(abs(a*b)*15/4+abs(b)*768/(25*math.sqrt(5)))/denom
    Jnumeric=quad(lambda xx:abs(profile(xx,a,b)[2]),0,1,epsabs=2e-10,epsrel=2e-10,limit=200)[0]
    ck('analytic J enclosure '+str((a,b)),Jnumeric<=Jupper,J=Jnumeric,upper=Jupper)
    for k in [1.7,4.3,13.,37.]:
        sol,rr,th,MM=physical(a,b,k);tt=th*math.exp(a/2)
        r2,t2=layers(a,b,k,2048);r8,t8=layers(a,b,k,8192)
        err=max(abs(r8-rr),abs(t8-tt));coarse=max(abs(r2-rr),abs(t2-tt))
        ck('independent layer/flux ODE '+str((a,b,k)),err<8e-7,error=err,coarse_error=coarse)
        ck('layer refinement '+str((a,b,k)),err<coarse*.2 or coarse<2e-10,fine=err,coarse=coarse)
        flux=abs(rr)**2+math.exp(a)*abs(th)**2
        ck('physical weighted flux '+str((a,b,k)),abs(flux-1)<3e-8,error=abs(flux-1),unweighted_flux=abs(rr)**2+abs(th)**2)
        ck('real transfer determinant '+str((a,b,k)),abs(np.linalg.det(MM)-1)<3e-8,error=abs(np.linalg.det(MM)-1))
        m=Jupper*math.exp(Jupper/k)/(2*k)
        ck('conservative scattering bounds '+str((a,b,k)),abs(tt-1)<=m+1e-9 and abs(rr)<=min(m,1)+1e-9 and abs(tt)>=1/math.sqrt(1+m*m)-1e-9,m=m)
        right=np.exp(1j*k)*np.array([math.exp(-a/2),1j*k*math.exp(a/2)])
        init=np.linalg.solve(MM,right)
        def fplus(xx):return math.sqrt(profile(xx,a,b)[0])*(sol.sol(xx).reshape((2,2))@init)[0]
        probes=[]
        for xx in [.09,.41,.78]:
            fun=lambda yy:math.sin(k*(yy-xx))/k*profile(yy,a,b)[2]*fplus(yy)
            integral=quad(lambda yy:fun(yy).real,xx,1,epsabs=2e-9,epsrel=2e-9,limit=200)[0]+1j*quad(lambda yy:fun(yy).imag,xx,1,epsabs=2e-9,epsrel=2e-9,limit=200)[0]
            probes.append(abs(fplus(xx)-np.exp(1j*k*xx)-integral))
        ck('Volterra independent quadrature '+str((a,b,k)),max(probes)<2e-8,errors=probes)
        rows.append(dict(a=a,b=b,k=k,r=cpair(rr),t_u=cpair(tt),t_h=cpair(th),layer_error=err,flux_error=abs(flux-1),volterra_error=max(probes),Jupper=Jupper,Jnumeric=Jnumeric,m=m))
        if k==4.3:
            _,rs,ts,_=physical(a,b,k,5.75)
            ck('global F scale '+str((a,b,k)),max(abs(rs-rr),abs(ts-th))<2e-8,error=max(abs(rs-rr),abs(ts-th)))
for k in [.4,3.7,20.]:
    _,rr,tt,_=physical(0,0,k)
    ck('constant profile '+str(k),abs(rr)<1e-8 and abs(tt-1)<1e-8,r=cpair(rr),t=cpair(tt))
result={'scope':'Independent exact algebra plus synthetic physical-flux Radau versus constant-Q layers and Volterra quadrature; no empirical test','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'passed':sum(c['passed']for c in checks),'failed':sum(not c['passed']for c in checks),'checks':checks,'scattering_rows':rows}
(HERE/'INDEPENDENT_RESULTS_v1.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':result['passed'],'failed':result['failed'],'max_layer_error':max(r['layer_error']for r in rows),'max_flux_error':max(r['flux_error']for r in rows),'max_volterra_error':max(r['volterra_error']for r in rows)}))
sys.exit(bool(result['failed']))
