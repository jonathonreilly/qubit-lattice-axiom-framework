"""Full mixed constraints, Gaussian transfer and exact polynomial fragments.

Only this source is read for an integrity hash. The transfer calculation does
not import the geometric checker or use its expected coefficient matrix.
"""
from __future__ import annotations
import json,time,hashlib
from pathlib import Path
import sympy as s
AUDIT_TIMEOUT_SEC = 180

def run():
    started=time.monotonic();checks=[]
    def check(name,condition):
        if not condition:raise AssertionError(name)
        checks.append(name)
    r,t=s.symbols('r t',real=True);tau,sigma,a,b1,b2,b3,v1,v2,u,w=s.symbols('tau sigma a b1 b2 b3 v1 v2 u w',real=True)
    H=s.Matrix([[tau/2+u,w,v1,b1],[w,tau/2-u,v2,b2],[v1,v2,sigma,b3],[b1,b2,b3,a]])
    p=s.Matrix([0,0,r,t]);D=r*r+t*t
    F=s.expand(D*s.trace(H*H)-2*(H*p).dot(H*p)+2*s.trace(H)*(p.T*H*p)[0]-D*s.trace(H)**2)
    Ft=2*D*(u*u+w*w);Fv=2*((t*v1-r*b1)**2+(t*v2-r*b2)**2)
    Fs=-D*tau*tau/2-2*tau*(r*r*a+t*t*sigma-2*r*t*b3)
    check('full_mixed_decomposition',s.expand(F-Ft-Fv-Fs)==0)
    check('lapse_equation',s.diff(F,a)==-2*r*r*tau)
    check('first_shift_equation',s.expand(s.diff(F,b1)-4*r*(r*b1-t*v1))==0)
    check('second_shift_equation',s.expand(s.diff(F,b2)-4*r*(r*b2-t*v2))==0)
    check('remaining_scalar_equation',s.expand(s.diff(F,tau).subs(tau,0)+2*(r*r*a+t*t*sigma-2*r*t*b3))==0)
    check('wrong_missing_scalar_cross_rejected',s.expand(F-Ft-Fv+D*tau*tau/2)!=0)
    check('wrong_missing_vector_cross_rejected',s.expand(Fv-2*(t*t*(v1*v1+v2*v2)+r*r*(b1*b1+b2*b2)))!=0)
    eta=s.Matrix(s.symbols('e0:4'))
    HG=H+s.I*(p*eta.T+eta*p.T)
    check('trace_constraint_gauge',s.expand(HG[0,0]+HG[1,1]-tau)==0)
    check('tensor_gauge',HG[0,1]==w and s.expand((HG[0,0]-HG[1,1])/2-u)==0)
    for j in (0,1):
        check('vector_combination_gauge_'+str(j),s.expand(t*HG[j,2]-r*HG[j,3]-(t*H[j,2]-r*H[j,3]))==0)
    check('scalar_combination_gauge',s.expand(r*r*HG[3,3]+t*t*HG[2,2]-2*r*t*HG[2,3]-(r*r*a+t*t*sigma-2*r*t*b3))==0)
    # On the constraint surface the explicit gauge choice kills every non-TT entry.
    HS=H.subs({tau:0,b1:t*v1/r,b2:t*v2/r,a:(2*r*t*b3-t*t*sigma)/(r*r)})
    g3=-sigma/(2*s.I*r)
    g0=-(b3+s.I*t*g3)/(s.I*r)
    g=s.Matrix([-v1/(s.I*r),-v2/(s.I*r),g3,g0])
    fixed=(HS+s.I*(p*g.T+g*p.T)).applyfunc(s.simplify)
    check('explicit_full_constraint_gauge_reduction',fixed==s.Matrix([[u,w,0,0],[w,-u,0,0],[0,0,0,0],[0,0,0,0]]))

    z=s.Symbol('z',positive=True);x,beta=s.symbols('x beta',real=True)
    A=(z+1/z)/2;alpha=(1/z-z)/2
    check('transfer_width_equation',s.simplify(alpha**2-(A*A-1))==0)
    check('transfer_generating_quadratic',s.simplify(2*alpha*z-1+z*z)==0)
    check('transfer_generating_constant',s.simplify(A-z-alpha)==0)
    # The domain is 0<z<1, hence r=(1-z)/sqrt(z)>0; keep that sign explicitly.
    r_from_z=(1-z)/s.sqrt(z)
    check('transfer_trace',s.simplify(s.sqrt(z)/(1-z)-1/r_from_z)==0)
    # A separate Gaussian-moment recurrence checks seven Hermite eigenfunctions.
    z0=s.Rational(1,2);alpha0=s.Rational(3,4);A0=s.Rational(5,4)
    y=s.Symbol('y');mom=[s.S.One,z0*x]
    for n in range(2,7):mom.append(s.expand(z0*x*mom[-1]+(n-1)*z0*mom[-2]))
    for n in range(7):
        poly=s.Poly(s.hermite(n,s.sqrt(alpha0)*y),y)
        expectation=sum(coef*mom[power[0]] for power,coef in poly.terms())
        check('hermite_transfer_eigenfunction_'+str(n),s.expand(expectation-z0**n*s.hermite(n,s.sqrt(alpha0)*x))==0)
    check('continuum_width_substitution_rejected',s.Rational(1,2)!=A0*A0-1)

    phase=s.Symbol('phase',nonzero=True)
    Csum=(1-z*z)/((1-z*phase)*(1-z/phase))/(2*alpha)
    check('covariance_fourier_all_phases',s.cancel(Csum-1/((1-z)**2/z+2-phase-1/phase))==0)

    # Exact finite polynomial fragments in the full oscillator's invariant degree range.
    N=8
    T=s.diag(*[z0**n for n in range(N)])
    X=s.zeros(N)
    for n in range(N-1):X[n,n+1]=X[n+1,n]=s.sqrt(s.Rational(n+1)/(2*alpha0))
    Omega=s.eye(N)[:,0]
    vecs=[T*X*Omega,T**2*(X**2-s.eye(N)/(2*alpha0))*Omega,T*X*T*X**2*Omega]
    V=s.Matrix.hstack(*vecs)
    check('polynomial_fragments_no_cutoff_contact',V[7,:]==s.zeros(1,3))
    site=(V.T*V).applyfunc(s.simplify);link=(V.T*T*V).applyfunc(s.simplify)
    for name,gram in [('site',site),('link',link)]:
        for order in range(1,4):
            for inds in __import__('itertools').combinations(range(3),order):
                check('reflection_'+name+'_'+str(inds),gram.extract(inds,inds).det()>=0)
    wrong=T.copy();wrong[1,1]=-wrong[1,1]
    check('negative_transfer_mode_rejected',((X*Omega).T*wrong*(X*Omega))[0]<0)
    for n in (0,1,2,5):
        check('exact_vacuum_covariance_'+str(n),(Omega.T*X*T**n*X*Omega)[0]==z0**n/(2*alpha0))

    ps=s.symbols('p0:3',real=True);R2=sum(q*q for q in ps)
    num=sum(q*q*(1-q*q/4) for q in ps)
    check('group_velocity_identity',s.expand(num-(R2-sum(q**4 for q in ps)/4))==0)
    check('group_velocity_axis_nyquist',num.subs({ps[0]:2,ps[1]:0,ps[2]:0})==0)

    out={'status':'passed','scope':'exact constraints, Gaussian spectral algebra and finite polynomial fragments; reduced quantization only',
         'checks':checks,'count':len(checks),'transfer_fixture':{'z':'1/2','width':'3/4','r_squared':'1/2','hermite_degrees':list(range(7))},
         'reflection_gram_site':[[str(site[i,j]) for j in range(3)] for i in range(3)],
         'reflection_gram_link':[[str(link[i,j]) for j in range(3)] for i in range(3)],
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'elapsed_sec':time.monotonic()-started}

    return out
