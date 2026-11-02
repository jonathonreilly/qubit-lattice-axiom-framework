"""Independent actual S4' central-link SU(2) slice; diagnostic, not interval proof.

Uses Gaussian Legendre integration in theta and scaled Bessel functions, distinct
from the author's arbitrary-precision coordinate-pair quadratures. The eight
incidences are separately established by review_source_history_geometry.py.
"""
import json,time,math
from fractions import Fraction as F
import numpy as np
from scipy.special import roots_legendre,ive
import mpmath as mp

start=time.monotonic();checks={};controls={};data={}
def req(n,p):checks[n]=bool(p);assert p,n
def neg(n,p):controls[n]=bool(p);assert p,n
mp.mp.dps=65
ps=np.array([4/27,1/9]+[10/81]*6)
req('eight_actual_contour_masses_sum_one',sum([F(4,27),F(1,9)]+[F(10,81)]*6)==1)

def Hseries(x):
    x=mp.mpf(x);v=mp.mpf(1);s=v;k=0
    while True:
        k+=1;v*=x*x/(4*k*(k+1));s+=v
        if abs(v)<abs(s)*mp.mpf('1e-62'):return s
        assert k<2000

def haarH(x):return mp.quad(lambda th:mp.exp(x*mp.cos(th))*mp.sin(th)**2*2/mp.pi,[0,mp.pi/2,mp.pi])
errs=[]
for x in [0,.2,2,11,30]:
    v=Hseries(x);q=haarH(mp.mpf(x));err=abs(v/q-1);errs.append(str(err))
    req('haar_series_'+str(x),err<mp.mpf('1e-58'))
    if x: req('bessel_series_'+str(x),abs(v/(2*mp.besseli(1,x)/x)-1)<mp.mpf('1e-58'))
data['normalizer_relative_errors']=errs
neg('omit_haar_normalizer_detected',abs(float(Hseries(2))-1)>.1)

def logH(x):return np.log(2*ive(1,x)/x)+x
for x in [.01,1,7,30,60]:req('scaled_bessel_vs_moment_series_'+str(x),abs(float(mp.log(Hseries(x)))-float(logH(x)))<2e-13)

def logdensity(theta,u,kappa,epsilon=0j,normal=True,probs=ps):
    q=np.cos(theta);result=-6*u*(1-q)*(1+epsilon)
    for p in probs:
        a=1-p*(1-q);radius=np.sqrt(a*a+p*p*(1-q*q));t=kappa*u
        result=result-t*a-(logH(t*radius) if normal else -t)
    return result

def integ(a,b,u,kappa,n=200,epsilon=0j,normal=True,probs=ps):
    x,w=roots_legendre(n);theta=a+(x+1)*(b-a)/2
    logf=logdensity(theta,u,kappa,epsilon,normal,probs)
    shift=float(np.max(logf.real));ans=np.sum(w*np.sin(theta)**2*np.exp(logf-shift))*(b-a)/math.pi
    return ans,shift

def probgood(u,kappa,eps1=.5,n=200,normal=True,probs=ps,wrong_cut=False):
    th0=eps1 if wrong_cut else 2*math.asin(eps1/2)
    z0,s0=integ(0,th0,u,kappa,n,normal=normal,probs=probs)
    z1,s1=integ(th0,math.pi,u,kappa,n,normal=normal,probs=probs)
    logodds=math.log(z0.real/z1.real)+s0-s1
    return logodds-math.log1p(math.exp(logodds))

logs=[]
for u in [1,3,6]:
    aa=probgood(u,10,n=160);bb=probgood(u,10,n=320)
    req('quadrature_refinement_'+str(u),abs(aa-bb)<2e-11)
    req('conditional_good_suppressed_'+str(u),bb<-10*u)
    logs.append({'u':u,'log_P_good':bb,'difference_160_320':abs(aa-bb)})
data['conditional_frustrated_slice']=logs
neg('normalizer_removal_changes_actual_slice',abs(probgood(3,10,normal=False)-probgood(3,10))>1)
neg('linearized_cut_changes_actual_slice',abs(probgood(3,10,wrong_cut=True)-probgood(3,10))>.01)
neg('replace_actual_incidence_by_equal_eighths_changes_slice',abs(probgood(3,10,probs=np.array([.125]*8))-probgood(3,10))>1e-5)

# A finite complex-source integral, retaining normalized kernels.
epsilon=.001+.002j;u=3;th0=2*math.asin(.25)
z0,s0=integ(th0,math.pi,u,10,n=320)
ze,se=integ(th0,math.pi,u,10,n=320,epsilon=epsilon)
ratio=ze/z0*math.exp(se-s0)
bound=math.expm1(12*u*abs(epsilon))
req('complex_source_integral_positive_baseline_bound',abs(ratio-1)<=bound)
req('complex_source_nonconstant',abs(ratio-1)>.001)
data['complex_source_ratio']=[ratio.real,ratio.imag]
data['complex_source_bound']=bound

# Elementary SU(2) cap bound; rho=2sin(theta/2), Haar radial mass.
for radius in [1e-3,.01,.1,.3,.8,1]:
    th=2*mp.asin(mp.mpf(radius)/2)
    mass=(th-mp.sin(th)*mp.cos(th))/mp.pi
    req('su2_haar_cap_lower_'+str(radius),mass>=mp.mpf(radius)**3/(6*mp.pi))
req('frustration_positive_rate_109_over_20',F(10)*(2-F(1,10)**2/2-F(1,2)**2)-12==F(109,20))
neg('weak_kappa_cannot_use_positive_rate',F(1)*(2-F(1,10)**2/2-F(1,2)**2)-12<0)

# H28's pointwise coarse-complex estimate, in genuinely noncommuting matrices.
I=np.eye(2,dtype=complex);sx=np.array([[0,1],[1,0]],complex);sz=np.diag([1,-1]).astype(complex)
def adj(A):return A.conj().T
def tracepair(V,M):return np.trace(np.linalg.inv(V)@M+adj(M)@V)/4
for th in [.1,.8,2.2]:
    U=math.cos(th)*I+1j*math.sin(th)*sx;M=.8*I+.2*U;W=-I
    for z in [.01+.02j,-.05+.03j]:
        V=W@np.diag([np.exp(z),np.exp(-z)])
        delta=tracepair(V,M)-tracepair(W,M)
        req('complex_coarse_bound_'+str((th,z)),abs(delta)<=math.expm1(abs(z))+1e-14)
        neg('replace_inverse_by_adjoint_is_nonholomorphic_'+str((th,z)),abs(tracepair(V,M)-np.trace(adj(V)@M+adj(M)@V)/4)>1e-7)
data['scope']='Conditional one-link SU(2), real fixed coarse -I; finite quadrature evidence only. No unconditional tail, full-cube integral, or sea bound.'
print(json.dumps({'checks':checks,'negative_controls':controls,'data':data,'elapsed_seconds':time.monotonic()-start},indent=2))
