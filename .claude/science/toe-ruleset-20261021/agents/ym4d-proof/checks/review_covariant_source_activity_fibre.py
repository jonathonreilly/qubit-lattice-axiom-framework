"""Independent SU(2) fibre of the normalized paired kernel and full Haar 3-form.
Spectator HS coordinates are fixed. This is neither the full coupled integral
nor a certification of the extremely restrictive sufficient SA12 constants.
"""
import json,os,re,resource,subprocess,time
import mpmath as m
START=time.monotonic();resources=[];checks=[];m.mp.dps=65
THREADS=['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS']
def guard(where):
 p=subprocess.run(['/usr/bin/memory_pressure','-Q'],capture_output=True,text=True,timeout=5);r=re.search(r'System-wide memory free percentage:\s*(\d+)%',p.stdout);assert p.returncode==0 and r
 v={'where':where,'rss':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'free':int(r.group(1)),'load':list(os.getloadavg()),'nice':os.getpriority(os.PRIO_PROCESS,0),'elapsed':time.monotonic()-START,'threads':{k:os.environ.get(k) for k in THREADS}};resources.append(v);assert v['rss']<2e9 and v['free']>=50 and max(v['load'])<20 and v['nice']>=10 and v['elapsed']<60 and set(v['threads'].values())=={'1'}
def gate(name,condition,detail=None):
 checks.append({'name':name,'passed':bool(condition),'detail':str(detail) if detail is not None else None});assert condition,name
def err(x,y):return abs(x-y)/max(1,abs(y))
def tr(A):return A[0,0]+A[1,1]
def maxabs(A):return max(abs(A[i,j]) for i in range(A.rows) for j in range(A.cols))
guard('start');alpha=m.mpf('.43');b=m.mpf('.07');u=m.mpf(17);kap=m.mpf('1.1');t=u*kap;p=m.mpf('1.15');eps=m.mpc('.014','.009');f=m.mpf(1)/27
I=m.eye(2);sx=m.matrix([[0,1],[1,0]]);sy=m.matrix([[0,-1j],[1j,0]])
V0=m.cos(alpha)*I+1j*m.sin(alpha)*sx;V1=m.cos(b)*I+1j*m.sin(b)*sy;V=[V0,V1,I,I]
P=V0*V1*V0**-1*V1**-1;q=m.re(tr(P)/2);ss=m.sqrt(1-q*q);nmat=(P-q*I)/(1j*ss)
gate('nonzero coarse curvature',ss>m.mpf('.01'),ss)
gate('full colour generator',maxabs(nmat*nmat-I)<m.mpf('1e-55'))
def ea(a):return m.cos(a)*I+1j*m.sin(a)*nmat
edge=(1,1,0,0)
def shift(x,mu,step=1):return tuple((v+(step if j==mu else 0))%6 for j,v in enumerate(x))
def link(x,mu,a):
 U=V[mu] if x[mu]%3==1 else I
 return ea(a)*U if mu==0 and x==edge else U
def plaquette(x,nu,a):return link(x,0,a)*link(shift(x,0),nu,a)*link(shift(x,nu),0,a)**-1*link(x,nu,a)**-1
def W(a):return 1-q*m.cos(a)+ss*m.sin(a)
def z0(z):return 2*m.besseli(1,z)/z if z else m.mpf(1)
def radius(a):return m.sqrt(1-2*f*(1-f)*(1-m.cos(a)))
def haarlog(a):return 2*m.log(m.sin(a)/a) if a else m.mpf(0)
def ell(a,e):return u*(5*(1-m.cos(a))+(1+e)*W(a))+m.log(z0(t*radius(a)))-t*(1-f+f*m.cos(a))-haarlog(a)
def haar_normalizer_direct(a):
 M=((1-f)*I+f*ea(a))*V0;Mrel=M*V0**-1
 a0=tr(Mrel)/2;a1=tr(nmat*Mrel)/(2j)
 def shc(z):return m.sinh(z)/z if z else m.mpf(1)
 # Exact angular integration over S^2 of normalized S^3 Haar.
 return 2/m.pi*m.quad(lambda theta:m.sin(theta)**2*m.exp(t*a0*m.cos(theta))*shc(t*a1*m.sin(theta)),[0,m.pi/2,m.pi])
for a in [m.mpf(0),m.mpf('.03'),m.mpf('-.12'),m.mpc('.045','.018'),m.mpc('-.08','.011')]:
 direct=sum(1-tr(plaquette(x,nu,a))/2 for nu in [1,2,3] for x in [edge,shift(edge,nu,-1)])
 gate('actual six plaquettes '+str(a),err(direct,5*(1-m.cos(a))+W(a))<m.mpf('1e-25'))
 nz=haar_normalizer_direct(a);gate('actual normalized Haar kernel '+str(a),err(nz,z0(t*radius(a)))<m.mpf('1e-25'),err(nz,z0(t*radius(a))))
guard('direct geometry and group normalizer')
h2=1/(4*m.sqrt(2)*m.pi**2);hline=m.sqrt(2)*h2
haar_mass=h2*4*m.pi*m.quad(lambda r:r*r*(m.sin(r/m.sqrt(2))/(r/m.sqrt(2)))**2 if r else 0,[0,m.sqrt(2)*m.pi])
gate('normalized full three-colour Haar constant',abs(haar_mass-1)<m.mpf('1e-25'),haar_mass)
cN=m.besseli(2,t)/m.besseli(1,t);h_expected=u*(5+q)+t*f-t*cN*f*(1-f)+m.mpf(2)/3
h_actual=m.diff(lambda a:ell(a,0),0,2)
gate('finite-u full density Hessian',err(h_actual,h_expected)<m.mpf('1e-25'),h_actual-h_expected)
gate('HS Haar coefficient N^2/(6u)',abs((m.mpf(2)/3)/u-m.mpf(4)/(6*u))<m.mpf('1e-60'))
guess=-ss/(5+q)
a0=m.findroot(lambda a:m.diff(lambda z:ell(z,0),a),(guess,guess+m.mpf('.005')),tol=m.mpf('1e-58'),maxsteps=30)
a1=m.findroot(lambda a:m.diff(lambda z:ell(z,eps),a),(a0,a0+m.mpf('.001')),tol=m.mpf('1e-58'),maxsteps=30)
k0=m.diff(lambda a:ell(a,0),a0,2);k1=m.diff(lambda a:ell(a,eps),a1,2);c0=1/m.sqrt(k0);c1=1/m.sqrt(k1)
res=max(abs(m.diff(lambda z:ell(z,0),a0)),abs(m.diff(lambda z:ell(z,eps),a1)))
gate('actual real and source-complex critical residuals',res<m.mpf('1e-30'),res)
gate('complex symmetric covariance branch',abs(c1*c1*k1-1)<m.mpf('1e-55') and m.re(c1)>0)
missing_norm=m.diff(lambda z:ell(z,0)-m.log(z0(t*radius(z))),a0)
missing_haar=m.diff(lambda z:ell(z,0)+haarlog(z),a0)
gate('omitting normalizer changes actual critical equation',abs(missing_norm)>m.mpf('1e-10'),missing_norm)
gate('omitting Haar changes actual critical equation',abs(missing_haar)>m.mpf('1e-10'),missing_haar)
guard('critical equations')
nodes={}
for count in [32,48,96]:
 X,weights=m.gauss_quadrature(count,'legendre');nodes[count]=list(zip(X,weights));guard('nodes '+str(count))
def quad(fun,lo,hi,count=48):
 middle=(lo+hi)/2;half=(hi-lo)/2
 return half*sum(weight*fun(middle+half*x) for x,weight in nodes[count])
fixed=hline*quad(lambda a:m.exp(-ell(a,eps)),a0-c0*p,a0+c0*p,96)
zp=m.erf(p/m.sqrt(2));vac=eps*u*W(a0)
def rem(w):return ell(a0+c0*w,0)-ell(a0,0)-w*w/2
def src(w):return eps*u*(W(a0+c0*w)-W(a0))
def expectation(with_linear=True):
 def ff(w):
  dsrc=src(w)
  if not with_linear:dsrc-=eps*u*c0*(q*m.sin(a0)+ss*m.cos(a0))*w
  return m.exp(-w*w/2-rem(w)-dsrc)/(m.sqrt(2*m.pi)*zp)
 return quad(ff,-p,p)
pref=hline*c0*m.sqrt(2*m.pi)*zp*m.exp(-ell(a0,0)-vac)
factored=pref*expectation();gate('fixed real Haar fibre exact Gaussian factorization',err(factored,fixed)<m.mpf('1e-25'),err(factored,fixed))
gate('source vacuum omission rejected',err(factored*m.exp(vac),fixed)>m.mpf('1e-10'),err(factored*m.exp(vac),fixed))
without_linear=pref*expectation(False);gate('canonical linear source omission rejected',err(without_linear,fixed)>m.mpf('1e-10'),err(without_linear,fixed))
gate('Haar constant omission rejected',err(factored/hline,fixed)>m.mpf('1e-10'))
gate('covariance Jacobian omission rejected',err(factored/c0,fixed)>m.mpf('1e-10'))
guard('fixed real integration set')
d=a1-a0;e=c1-c0
calls=0
def contour(s):
 bs=a0+s*d;cs=c0+s*e
 return hline*cs*quad(lambda w:m.exp(-ell(bs+cs*w,eps)),-p,p)
def flux(s):
 global calls
 bs=a0+s*d;cs=c0+s*e;value=contour(s)
 numerator=hline*(m.exp(-ell(bs+cs*p,eps))*(d+e*p)-m.exp(-ell(bs-cs*p,eps))*(d-e*p))
 calls+=1
 if calls%8==0:guard('flux '+str(calls))
 return numerator/value
I0=contour(0);I1=contour(1);integrated=quad(flux,0,1,32);ratio_log=m.log(I1/I0)
gate('source-complex normalized contour return',abs(integrated-ratio_log)<m.mpf('1e-25'),integrated-ratio_log)
gate('contour start is exact fixed sector',err(I0,fixed)<m.mpf('1e-25'))
gate('nontrivial full face correction',abs(ratio_log)>m.mpf('1e-10'),ratio_log)
guard('completion')
print(json.dumps({'checks':checks,'parameters':{k:str(v) for k,v in {'alpha':alpha,'b':b,'u':u,'kappa':kap,'p':p,'epsilon':eps,'affected_word_fraction':f}.items()},'dps':m.mp.dps,'critical':{'a0':str(a0),'a1':str(a1),'k0':str(k0),'k1':str(k1),'residual':str(res)},'fixed_integral':str(fixed),'factored_integral':str(factored),'normalized_flux':str(integrated),'log_contour_ratio':str(ratio_log),'resources':resources,'scope':'Actual SU(2) full-Haar density fibre; all-volume/support and full coupled claims rest on the analytic proof, not this finite check.'},indent=2))
