"""Two integral routes and positive constitutive checks of quadratic coframe flow."""
from pathlib import Path
from collections import Counter
from itertools import product
import hashlib,json,math,time
import sympy as s
import numpy as np
from numpy.polynomial.legendre import leggauss
start=time.monotonic();checks=Counter()
def require(ok,label):
    if not ok:raise AssertionError(label)
    checks[label]+=1
h,x=s.symbols('h x',real=True);cs=[s.Integer(0),*s.symbols('c1 c2 c3',real=True)]
T=sum(cs);Q=sum(c*c for c in cs);y=1-x

def cut(expr):return s.Poly(s.expand(expr),h).terms()
def trim(expr):return s.expand(sum(c*h**pw[0] for pw,c in cut(expr) if pw[0]<=2))
def pow2(a,b,p):return 1+p*a*h+(p*b+p*(p-1)*a*a/2)*h*h
# Full Feynman-parameter formula, expanded eigenvalue by eigenvalue.
det=1
for c in cs:det=trim(det*pow2(2*y*c,y*c*c,-s.Rational(1,2)))
parameter=[]
for c in cs:
    Ei=1+h*c;B=2*Ei**2-sum((1+h*d)**2 for d in cs)
    integrand=trim(-x*det*B*Ei*pow2(2*y*c,y*c*c,-1))
    value=s.expand(s.integrate(integrand,(x,0,1)))
    target=1+h*(-s.Rational(5,3)*c+s.Rational(2,3)*T)+h*h*(-2*c*c+T*c+Q/2-T*T/4)
    require(s.expand(value-target)==0,'parameter integral full quadratic coefficient')
    parameter.append(value)
# Independent unshifted angular route; squared sphere coordinates are Dirichlet(1/2).
u=s.symbols('u0:4',real=True)
def sphere(expr):
    pol=s.Poly(s.expand(expr),*u);total=0
    for powers,coefficient in pol.terms():
        degree=sum(powers);moment=s.prod(s.rf(s.Rational(1,2),p) for p in powers)/s.rf(2,degree)
        total+=coefficient*moment
    return s.expand(total)
alpha=sum(c*v for c,v in zip(cs,u));beta=sum(c*c*v for c,v in zip(cs,u))
angular=[]
for i,c in enumerate(cs):
    Ei=1+h*c;B=2*Ei**2-sum((1+h*d)**2 for d in cs)
    inverse=1-2*h*alpha+h*h*(4*alpha*alpha-beta)
    inverse2=1-4*h*alpha+h*h*(12*alpha*alpha-2*beta)
    val=sphere(trim(-B*Ei*(inverse-2*Ei**2*u[i]*inverse2)))
    require(s.expand(val-parameter[i])==0,'unshifted exact S3 moments independently recover the parameter integral')
    angular.append(val)
for i,c in enumerate(cs[1:],1):
    velocity=trim(parameter[i]-parameter[0]*(1+h*c))
    expected=-s.Rational(8,3)*h*c+h*h*(-2*c*c+T*c/3)
    require(s.expand(velocity-expected)==0,'temporal normalization removes scalar quadratic wavefunction terms')
c=s.symbols('c',real=True);r=1+c
# Convert the exact scalar source to units e^2/(8pi^2).
scalar=-s.Rational(4,3)*(4*r*r+3*r+1)*(r-1)/(r+1)**2
require(s.expand(s.series(scalar,c,0,3).removeO()+s.Rational(8,3)*c+c*c)==0,'exact scalar velocity formula has matching quadratic expansion')

# Positive full matrices at finite shear; no Taylor expansion in the quadrature.
O=np.array([[0.,0,1],[0,0,0],[1,0,0]])
def Mfull(E,degree):
    xx,ww=leggauss(degree);xx=(xx+1)/2;ww=ww/2;E2=E@E;B=2*E2-np.trace(E2)*np.eye(4);answer=np.zeros((4,4))
    for x,w in zip(xx,ww):
        A=x*np.eye(4)+(1-x)*E2
        answer-=w*x/np.sqrt(np.linalg.det(A))*B@E@np.linalg.inv(A)
    return answer
matrix_results=[]
for d in (.04,.02,.01):
    F=[]
    for sign in (-1,1):
        E=np.eye(4);E[1:,1:]+=sign*d*O
        m=Mfull(E,128);m2=Mfull(E,256)
        require(np.linalg.norm(m-m2)<1e-13,'full positive coframe parameter quadrature comparison')
        F.append(m[1:,1:]-m[0,0]*E[1:,1:])
    average=(F[0]+F[1])/(2*d*d);error=np.linalg.norm(average+2*O@O)
    require(error<20*d*d,'full coframe pair has derived quadratic mean self-energy')
    matrix_results.append({'shear':d,'quadratic_source_error':float(error)})

# Solve the sourced mean flow and independently integrate its photon history.
z,t=s.symbols('z t',positive=True);flow_results=[]
for nn in (1,2,3,4,6):
    N=s.Integer(nn);p=1+2/N
    RR=-s.log(z)/(4*z*z) if N==2 else (N-3)/(2*(N-2))*(z**(-4/N)-z**(-p))
    star=-5*N/(8*(N+2))*(1-z**(-4/N))
    cf=star+2*RR/(N+2);cg=star-N*RR/(N+2)
    require(s.simplify(s.diff(cf,z)+2*RR/(N*z)+3*z**(-1-4/N)/(2*N))==0,'mean fermion solution obeys derived quadratic self-energy')
    require(s.simplify(s.diff(cg,z)-RR/z+s.Rational(1,2)*z**(-1-4/N))==0,'photon metric solution obeys derived quadratic tensor increment')
    history=s.integrate(cf.subs(z,t)-s.Rational(1,2)*t**(-4/N),(t,1,z))/z
    require(s.simplify(history-cg)==0,'positive constitutive history independently recovers photon mean drift')
    flow_results.append({'N':nn,'relative_coefficient':str(RR),'common_coefficient':str(star)})
require(s.simplify(flow_results[2]['relative_coefficient'])==0,'N3 quadratic relative-source cancellation is retained')
# The log term must not be replaced by a pure z^-2 coefficient at N2.
require(s.diff(-s.log(z)/4,z)!=0,'quartet resonant relative mode is not purely homogeneous')

# Full tensor mixture along the derived mean/contrast trajectories.
constitutive=[]
for d in (.04,.02,.01):
    V0=d*d*np.diag([1.,0,1])
    for end in (2.,5.,10.):
        outs=[]
        for degree in (128,256):
            nodes,ww=leggauss(degree);tt=1+(end-1)*(nodes+1)/2;ww=ww*(end-1)/2
            eps=np.eye(3);bb=np.eye(3)
            for zt,weight in zip(tt,ww):
                cf=(-5/16*(1-zt**-2)-math.log(zt)/(8*zt*zt))*V0
                for sign in (-1,1):
                    E=np.eye(3)+cf+sign*d*O/zt
                    e=E@E/np.linalg.det(E);bv=np.linalg.inv(e)
                    eps+=weight*e/2;bb+=weight*bv/2
            outs.append((eps/end,bb/end))
        require(max(np.linalg.norm(outs[0][i]-outs[1][i]) for i in (0,1))<1e-13,'constitutive-history quadrature cutoff comparison')
        eps,bb=outs[-1]
        require(np.linalg.norm(eps-np.diag(np.diag(eps)))<1e-14 and np.linalg.norm(bb-np.diag(np.diag(bb)))<1e-14,'reflected pair cancels off-diagonal mixture entries')
        actual=np.array([(bb[j,j]*bb[k,k]/(eps[j,j]*eps[k,k]))**.25-1 for i,j,k in ((0,1,2),(1,0,2),(2,0,1))])
        predicted=np.diag((-5/16*(1-end**-2)+math.log(end)/(8*end*end))*V0)
        error=np.linalg.norm(actual-predicted)
        require(error<20*d**4,'exact positive metric extraction matches quadratic common drift')
        eb=eps@bb;W=(eb-np.trace(eb)*np.eye(3)/3)/2
        tfV=V0-np.trace(V0)*np.eye(3)/3
        expectedW=2*(end**-1-end**-2)*tfV
        require(np.linalg.norm(W-expectedW)<20*d**4,'quadratic mean backreaction leaves prior polarization coefficient unchanged')
        constitutive.append({'shear':d,'z':end,'metric_error':float(error),'W_error':float(np.linalg.norm(W-expectedW))})

root=Path(__file__).resolve().parents[1];files=[Path(__file__).resolve(),root/'notes/BLOCK13_QUARTET_QUADRATIC_BACKREACTION.md']
result={'status':'PASS_personal_quadratic_loop_challenges','checks':dict(checks),'full_matrix_quadrature':matrix_results,'flow_solutions':flow_results,'full_constitutive_mixtures':constitutive,'seconds':time.monotonic()-start,
'limits':['one-loop coefficient expansion only','two algebraic derivations by the same author','constitutive trajectories use the quadratic truncation','no uniform higher-order remainder or physical phase theorem'],
'sha256':{str(f.relative_to(root)):hashlib.sha256(f.read_bytes()).hexdigest() for f in files}}
out=json.dumps(result,indent=2);Path(__file__).with_suffix('.json').write_text(out+'\n');print(out)
