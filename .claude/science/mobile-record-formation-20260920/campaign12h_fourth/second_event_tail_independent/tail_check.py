"""Independent continuation of the sealed exact ring clock.

No fourth-campaign author source imported or read.  New calculations use the
two-coordinate no-event matrix, angular weights, and rates from our own PRE.
Numerical tail integrals corroborate, rather than prove, the asymptotics.
"""
from pathlib import Path
import cmath, hashlib, json, math
import numpy as np
import sympy as sp
import mpmath as mp
from scipy.integrate import quad
from scipy.linalg import expm

D=Path(__file__).resolve().parent
k,w,s=sp.symbols('k w s',positive=True)
M=sp.Matrix([[-4*k,0,-2*w],[0,0,2*w],[w,-w,-2*k]])
initial=sp.Matrix([1,0,0])
laplace=sp.factor((sp.Matrix([[1,1,0]])*(s*sp.eye(3)-M).inv()*initial)[0])
expected=(s*s+2*k*s+4*w*w)/((s+2*k)*(s*s+4*k*s+4*w*w))
assert sp.simplify(laplace-expected)==0
moments={}
for p in range(1,5):
    moments[p]=sp.factor(p*(-1)**(p-1)*sp.diff(laplace,s,p-1).subs(s,0))
assert moments[1]==1/(2*k)
assert sp.simplify(moments[2]-(1/(2*k*k)+1/(2*w*w)))==0
leading={p:sp.simplify(sp.limit(w**(2*p-2)*moments[p],w,0)) for p in (2,3,4)}
for p,v in leading.items():assert sp.simplify(v-sp.factorial(p)*k**(p-2)/4)==0

def f(omega,kappa,time):
    """Stable exact adjacent-state survival, including large time and omega=0."""
    omega=abs(float(omega))
    if omega==0:return math.exp(-4*kappa*time)
    if omega<kappa and math.sqrt(kappa*kappa-omega*omega)*time>20:
        q=math.sqrt(kappa*kappa-omega*omega)
        u=math.exp(-omega*omega*time/(kappa+q));v=math.exp(-(kappa+q)*time)
        A=(-omega*omega*u/(kappa+q)+(kappa+q)*v)/(2*q)
        B=omega*(u-v)/(2*q)
        return A*A+B*B
    q=cmath.sqrt(kappa*kappa-omega*omega)
    F=time if abs(q)<1e-14 else cmath.sinh(q*time)/q
    A=cmath.cosh(q*time)-kappa*F
    return math.exp(-2*kappa*time)*(abs(A)**2+omega*omega*abs(F)**2)

def fiber(theta,a,kappa,time,coherent=False):
    ans=.5*math.exp(-4*kappa*time)
    for j in range(6):
        alpha=(4*theta+2*math.pi*j)/6
        weight=(1+math.cos(theta-alpha))/6 if coherent else 1/6
        for sign in (-1,1):
            s2=max(0.,4+sign*4*math.cos(alpha/2))
            ans+=.25*weight*f(a*math.sqrt(s2),kappa,time)
    return ans

def uniform_laplace(lam,a,kappa):
    if a==0:return 1/(lam+4*kappa)
    A=lam*(lam+4*kappa)
    correction=kappa*lam/((lam+2*kappa)*math.sqrt(A*(A+32*a*a)))
    return .5/(lam+4*kappa)+.5/(lam+2*kappa)-correction

def uniform_survival(a,kappa,time):
    if a==0:return math.exp(-4*kappa*time),0.
    O=math.sqrt(8)*abs(a)
    cut=min(math.pi/2,8*math.sqrt(kappa)/(O*math.sqrt(max(time,1e-100))))
    val1,err1=quad(lambda x:f(O*math.sin(x),kappa,time),0,cut,epsabs=1e-14,epsrel=3e-11)
    val2,err2=quad(lambda x:f(O*math.sin(x),kappa,time),cut,math.pi/2,epsabs=1e-14,epsrel=3e-11)
    return .5*math.exp(-4*kappa*time)+(val1+val2)/math.pi,(err1+err2)/math.pi

matrix_rows=[]
for kap in (.7,1.3):
    for om in (0.,1e-5,.2,kap,1.7,9.):
        K=np.array([[-2*kap,1j*om],[1j*om,0]],complex)
        for time in (.01,.9,8.,100.):
            actual=float(np.linalg.norm(expm(time*K)@np.array([1,0]))**2)
            stable=f(om,kap,time)
            assert abs(actual-stable)<2e-13,(kap,om,time,actual,stable)
            matrix_rows.append({'kappa':kap,'omega':om,'time':time,'matrix':actual,'formula':stable,'error':abs(actual-stable)})

# The sum of the coherent cosine terms cancels on each pi/2 orbit of theta.
uniform_rows=[]
for a in (0.,.4,2.,11.):
    kap=.7
    for time in (.1,1.,10.):
        direct=[]
        for coh in (False,True):
            val,err=quad(lambda theta:fiber(theta,a,kap,time,coh)/(2*math.pi),0,2*math.pi,
                         points=[math.pi/2,math.pi,3*math.pi/2],epsabs=2e-12,epsrel=2e-11,limit=500)
            direct.append(val)
        one,err=uniform_survival(a,kap,time)
        assert max(abs(x-one) for x in direct)<2e-10
        uniform_rows.append({'a':a,'kappa':kap,'time':time,'resolved_full_angle':direct[0],
                             'coherent_full_angle':direct[1],'arcsine_integral':one,'quad_error_estimate':err})

laplace_rows=[]
for a in (.3,2.,10.):
    for lam in (.001,.13,2.,11.):
        kap=.7;O=math.sqrt(8)*a
        def one(x):
            om=O*math.sin(x)
            return (lam*lam+2*kap*lam+4*om*om)/((lam+2*kap)*(lam*lam+4*kap*lam+4*om*om))
        value=.5/(lam+4*kap)+quad(one,0,math.pi/2,epsabs=1e-13,epsrel=1e-12)[0]/math.pi
        predicted=uniform_laplace(lam,a,kap)
        assert abs(value-predicted)<1e-12
        laplace_rows.append({'a':a,'kappa':kap,'Laplace_parameter':lam,'angular_integral':value,'closed_formula':predicted})

a=2.;kap=.7
C=1/(32*abs(a)*math.sqrt(2*math.pi*kap))
tail_rows=[]
for time in (10.,100.,1000.,10000.,100000.):
    value,error=uniform_survival(a,kap,time)
    tail_rows.append({'time':time,'survival':value,'t_to_3_over_2_times_survival':time**1.5*value,
                      'predicted_coefficient':C,'relative_coefficient_error':abs(time**1.5*value/C-1),
                      'quad_error_estimate':error})
assert tail_rows[-1]['relative_coefficient_error']<1e-4

# Exact second-moment angular criteria and useful normalizable controls.
# g=2 sin^2(2 theta) is the density of a two-circulation superposition.
theta=sp.symbols('theta',real=True)
second_base=sp.Rational(5,16)/k**2
second_regularized=second_base+sp.Rational(3,4)/sp.symbols('a',nonzero=True,real=True)**2
def singular_sum(theta,coherent):
    ans=0.
    for j in range(6):
        alpha=(4*theta+2*math.pi*j)/6
        b=(1+math.cos(theta-alpha))/6 if coherent else 1/6
        ans+=b/math.sin(alpha/2)**2
    return ans
second_rows=[]
for coh in (False,True):
    correction=0.;errors=0.
    for l,r in zip(np.linspace(0,2*math.pi,5)[:-1],np.linspace(0,2*math.pi,5)[1:]):
        value,error=quad(lambda th:2*math.sin(2*th)**2*singular_sum(th,coh)/(2*math.pi),l,r,epsabs=1e-12)
        correction+=value;errors+=error
    value=5/(16*kap*kap)+correction/(16*a*a)
    expected=5/(16*kap*kap)+3/(4*a*a)
    assert abs(value-expected)<2e-12
    second_rows.append({'coherent':coh,'density':'2 sin^2(2 theta)','weighted_cosecant_sum_integral':correction,
                        'second_moment':value,'exact_formula_value':expected,'quad_error_estimate':errors})

# A band around pi produces different powers for resolved/coherent first marks.
width=.3;gpi=math.pi/width
def band_survival(time,coh):
    cut=min(width,8*math.sqrt(kap)/(abs(a)*(math.sqrt(2)/3)*math.sqrt(time)))
    integrand=lambda x:(fiber(math.pi+x,a,kap,time,coh)+fiber(math.pi-x,a,kap,time,coh))/(2*width)
    v1,e1=quad(integrand,0,cut,epsabs=2e-17,epsrel=2e-8,limit=300)
    v2,e2=quad(integrand,cut,width,epsabs=2e-17,epsrel=2e-8,limit=300)
    return v1+v2,e1+e2
band_rows=[]
for time in (100.,1000.,10000.):
    for coh in (False,True):
        power=2.5 if coh else 1.5
        coefficient=(3*gpi*math.sqrt(kap)/(1024*math.sqrt(2*math.pi)*abs(a)**3)
                     if coh else gpi/(128*abs(a)*math.sqrt(2*math.pi*kap)))
        value,error=band_survival(time,coh)
        band_rows.append({'coherent':coh,'time':time,'survival':value,'power':power,
                          'scaled_survival':time**power*value,'predicted_coefficient':coefficient,
                          'relative_coefficient_error':abs(time**power*value/coefficient-1),'quad_error_estimate':error})
assert max(x['relative_coefficient_error'] for x in band_rows if x['time']==10000.)<1e-3
band_sum=quad(lambda r:3/(4*math.cos(r/2)**2*math.cos(r)**2)+1/math.cos(r),0,width,
              epsabs=1e-13)[0]/width
band_m2=5/(16*kap*kap)+band_sum/(16*a*a)

# Fractional moments between one and 3/2: positive Laplace integral, plus
# an independently evaluated complex-root moment formula at p=5/4.
fractional=[]
for a0 in (1.,2.,8.,32.):
    for p in (1.25,1.4):
        def regular(lam):
            return kap/((lam+2*kap)*math.sqrt((lam+4*kap)*(lam*(lam+4*kap)+32*a0*a0)))
        low,e1=quad(regular,0,1,weight='alg',wvar=(.5-p,0),epsabs=1e-12,epsrel=1e-11)
        high,e2=quad(lambda lam:regular(lam)*lam**(.5-p),1,np.inf,epsabs=1e-12,epsrel=1e-11)
        pref=p*(p-1)/math.gamma(2-p)
        limiting=math.gamma(p+1)*.5*((4*kap)**(-p)+(2*kap)**(-p))
        moment=limiting+pref*(low+high)
        fractional.append({'a':a0,'p':p,'moment':moment,'fast_limit_moment':limiting,
                           'excess':moment-limiting,'a_times_excess':a0*(moment-limiting),'quad_error_estimate':e1+e2})
mp.mp.dps=55
pp=mp.mpf(5)/4;kk=mp.mpf(7)/10;aa=mp.mpf(2);O=mp.sqrt(8)*aa
def mp_moment(om):
    ww=mp.sqrt(kk*kk-om*om)
    if abs(ww)<mp.mpf('1e-40'):
        return mp.gamma(pp+1)/(2*kk)**pp*(pp*pp-pp+2)/2
    slow=kk*om*om/(2*ww*ww*(kk+ww))
    fast=kk*(kk+ww)/(2*ww*ww)
    return mp.re(mp.gamma(pp+1)*(slow/(2*om*om/(kk+ww))**pp+
                   fast/(2*(kk+ww))**pp-(om*om/(ww*ww))/(2*kk)**pp))
def transformed(u):
    if not u:return 2*mp.gamma(pp+1)*kk**(pp-2)/(4*O**(2*pp-2))
    return 2*u*mp_moment(O*mp.sin(u*u))
critical=mp.sqrt(mp.asin(kk/O))
mp_value=.5*mp.gamma(pp+1)/(4*kk)**pp+mp.quad(transformed,[0,critical,mp.sqrt(mp.pi/2)])/mp.pi
value=next(x['moment'] for x in fractional if x['a']==2. and x['p']==1.25)
assert abs(float(mp_value)-value)<2e-11

# Moment divergence is seen directly in the exact m2 integrand.  This
# cutoff calculation tests normalization, not the analytic divergence proof.
cutoff_rows=[]
for cutoff in (.08,.02,.005):
    integral=0.
    for i in range(4):
        l=i*math.pi/2+cutoff;r=(i+1)*math.pi/2-cutoff
        integral+=quad(lambda x:1/math.sin(2*x)**2/(2*math.pi),l,r,epsabs=1e-11)[0]
    expected=2/math.pi/math.tan(2*cutoff)
    assert abs(integral-expected)<1e-10
    cutoff_rows.append({'angular_cutoff':cutoff,'cosecant_integral':integral,'exact_cutoff_formula':expected,
                        'divergent_m2_contribution':3*integral/(8*a*a)})

out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'model':'Exact unit-rotor eight-site post-first-mark effective clock; a=eta-4 delta, kappa>0.',
     'two_state_survival_Laplace':str(laplace),'two_state_integer_moments':{str(p):str(v) for p,v in moments.items()},
     'small_frequency_leading_moments':{str(p):str(v) for p,v in leading.items()},
     'stable_formula_matrix_controls':matrix_rows,'uniform_density_survival_controls':uniform_rows,
     'closed_Laplace_angular_controls':laplace_rows,'uniform_density_tail':tail_rows,
     'regularized_density_second_moment_formula':str(second_regularized),'regularized_second_moment_controls':second_rows,
     'band_density_controls':band_rows,'band_density_width':width,'band_coherent_second_moment':band_m2,
     'band_coherent_weighted_cosecant_integral':band_sum,
     'fractional_moment_controls':fractional,'fractional_moment_independent_root_integral':str(mp_value),
     'second_moment_cutoff_controls':cutoff_rows,
     'scope':['No tail-author source or new author packet opened.',
              'Quadrature error estimates and finite numeric samples are controls, not proofs of asymptotics.',
              'All integer moments >=2 diverge for single-circulation input when a!=0; at a=0 the law is Exp(4 kappa).',
              'General normalizable densities require the integrability conditions in REPORT.md.']}
target=D/'TAIL_RESULTS.json';assert not target.exists()
target.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
