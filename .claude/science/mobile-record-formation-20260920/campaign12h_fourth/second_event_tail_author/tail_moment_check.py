"""Exact moment identities and long-time controls for the frozen rotor block law."""
from pathlib import Path
import hashlib,json,math
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.linalg import expm

D=Path(__file__).resolve().parent
source=D.parent/'second_event_independent/REPORT.md'
assert hashlib.sha256(source.read_bytes()).hexdigest()=='39e2b04f9140f10db8d8bbd178a086902d9b09f6854b0e317a663071bacf4582'
k,w=sp.symbols('k w',positive=True,real=True)
K=sp.Matrix([[-2*k,sp.I*w],[sp.I*w,0]])
X=sp.Matrix([[1/(2*k),-sp.I/(2*w)],[sp.I/(2*w),1/(2*k)+k/w**2]])
Y=sp.Matrix([[(k*k+w*w)/(2*k*k*w*w),-sp.I*(2*k*k+w*w)/(2*k*w**3)],
             [sp.I*(2*k*k+w*w)/(2*k*w**3),(4*k**4+k*k*w*w+w**4)/(2*k*k*w**4)]])
assert (K.conjugate().T*X+X*K+sp.eye(2)).applyfunc(sp.simplify)==sp.zeros(2)
assert (K.conjugate().T*Y+Y*K+2*X).applyfunc(sp.simplify)==sp.zeros(2)

def stable_two_level(omega,kappa,t):
    omega=abs(omega)
    if abs(omega-kappa)<=1e-12*kappa:
        return math.exp(-2*kappa*t)*((1-kappa*t)**2+(kappa*t)**2)
    if omega>kappa:
        nu=math.sqrt((omega-kappa)*(omega+kappa))
        r=kappa/nu
        return math.exp(-2*kappa*t)*(1-r*math.sin(2*nu*t)+2*r*r*math.sin(nu*t)**2)
    w=math.sqrt((kappa-omega)*(kappa+omega))
    slow=math.exp(-omega*omega*t/(kappa+w))
    fast=math.exp(-(kappa+w)*t)
    difference=slow*(-math.expm1(-2*w*t))
    adjacent=fast-omega*omega*difference/(2*w*(kappa+w))
    opposite=omega*difference/(2*w)
    return adjacent*adjacent+opposite*opposite

def ring(theta,a,kappa,t,coherent):
    answer=.5*math.exp(-4*kappa*t)
    for j in range(6):
        alpha=(4*theta+2*math.pi*j)/6
        b=(1+math.cos(theta-alpha))/6 if coherent else 1/6
        # Trigonometric factors avoid subtracting nearly equal cosines.
        for singular in (2*math.sqrt(2)*abs(math.cos(alpha/4)),
                         2*math.sqrt(2)*abs(math.sin(alpha/4))):
            answer+=.25*b*stable_two_level(a*singular,kappa,t)
    return answer

controls=[]
for omega in (0.,1e-8,.013,.6,.9,.9000001,1.,7.,100.):
    for t in (0.,.17,1.2,18.):
        kappa=.9
        generator=np.array([[-2*kappa,1j*omega],[1j*omega,0]],complex)
        observed=float(np.linalg.norm(expm(t*generator)@np.array([1.,0.]))**2)
        predicted=stable_two_level(omega,kappa,t)
        error=abs(observed-predicted)
        assert error<2e-10,(omega,t,error)
        controls.append({'omega':omega,'t':t,'matrix_norm':observed,'stable_formula':predicted,'absolute_error':error})

a=4.2;kappa=.9
tail=[]
for label,sign in [('one_flux',0),('neighbor_plus',1),('neighbor_minus',-1)]:
    for coherent in (False,True):
        coefficient=0.
        for j in range(4):
            center=j*math.pi/2
            g=1+sign*math.cos(center)
            b=(1+math.cos(center))/6 if coherent else 1/6
            coefficient+=3*g*b/(64*math.sqrt(2*math.pi*kappa)*abs(a))
        for t in (100.,1000.,10000.,100000.):
            width=math.sqrt(kappa)/(abs(a)*math.sqrt(2)/3*math.sqrt(t))
            value=error=0.
            for j in range(4):
                center=j*math.pi/2
                cuts=sorted(set([0.]+[v*width for v in (-8,-3,-1,1,3,8) if abs(v*width)<math.pi/4]))
                def integrand(x):
                    theta=center+x
                    return t**1.5*(1+sign*math.cos(theta))*ring(theta,a,kappa,t,coherent)/(2*math.pi)
                part,err=quad(integrand,-math.pi/4,math.pi/4,points=cuts,epsabs=1e-11,epsrel=1e-9,limit=200)
                value+=part;error+=err
            assert abs(value-coefficient)/coefficient<.015
            tail.append({'field':label,'coherent':coherent,'t':t,'scaled_survival_t_power_3_over_2':value,
                         'analytic_coefficient':coefficient,'relative_difference':(value-coefficient)/coefficient,
                         'quadrature_error_estimate':error})

moment_cuts=[]
for cut in (.2,.1,.05,.01,.002):
    integral=0.
    for j in range(4):
        left=j*math.pi/2+cut;right=(j+1)*math.pi/2-cut
        def integrand(theta):
            total=sum((1/6)/math.sin((4*theta+2*math.pi*j)/12)**2 for j in range(6))
            return total/(16*a*a*2*math.pi)
        value,err=quad(integrand,left,right,epsabs=1e-10,epsrel=1e-10)
        integral+=value
    exact=3/(4*math.pi*a*a*math.tan(2*cut))
    assert abs(integral-exact)<1e-9
    moment_cuts.append({'angular_excision_radius':cut,'second_moment_positive_singular_part':integral,
                        'exact_cut_formula':exact,'radius_times_singular_part':cut*integral,
                        'limiting_cut_coefficient':3/(8*math.pi*a*a)})
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'dependency_report_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
     'symbolic_mean_matrix':str(X),'symbolic_second_moment_matrix':str(Y),
     'two_state_controls':controls,'long_time_quadrature':tail,'excision_moment_controls':moment_cuts,
     'scope':'Controls corroborate the source-bound moment and asymptotic proof; finite quadrature is not proof of an infinite second moment.'}
p=D/'TAIL_AND_MOMENT_RESULTS.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

