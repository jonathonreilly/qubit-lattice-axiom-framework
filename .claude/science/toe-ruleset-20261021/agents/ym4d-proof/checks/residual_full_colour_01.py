#!/usr/bin/env python3
"""Exact neutral-domain controls. No predecessor helper is imported."""
import itertools, json
import sympy as s
checks=[]
def check(name, predicate, detail=None):
    ok=bool(predicate)
    checks.append({'name':name,'passed':ok,'detail':str(detail) if detail is not None else None})
    if not ok:
        print(json.dumps({'checks':checks,'failed':name},indent=2))
        raise AssertionError(name)
def zero(M): return all(s.simplify(x)==0 for x in M)
def incidence(n):
    d=s.zeros(n)
    for j in range(n): d[j,j]=-1; d[j,(j+1)%n]=1
    return d
def constproj(n): return s.ones(n)/n

d=incidence(9); dc=incidence(3); D=d.T*d; Dc=dc.T*dc
roots=[0,3,6]; interior=[j for j in range(9) if j not in roots]
J=s.eye(9)[:,roots]; I=s.eye(9)[:,interior]; A=I.T*D*I; B=I.T*D*J
L=J-I*A.inv()*B; S=J.T*D*L; Pc=constproj(3); Pf=constproj(9)
Sp=(S+Pc).inv()-Pc
Q=s.eye(9)-D*L*Sp*Sp*L.T*D
check('harmonic trace and equation',zero(J.T*L-s.eye(3)) and zero(D*L-J*S))
check('harmonic constant lift',zero(L*s.ones(3,1)-s.ones(9,1)))
check('coarse Schur constant kernel',S.rank()==2 and zero(S*s.ones(3,1)))
check('retained root mean',zero(Q-(I*I.T+J*Pc*J.T)) and Q[0,3]==s.Rational(1,3),Q[0,3])
cofactor_D=9*D[:8,:8].det(); ranklift_D=(D+Pf).det()
cofactor_S=3*S[:2,:2].det(); ranklift_S=(S+Pc).det()
check('scalar pseudodeterminants two definitions',cofactor_D==ranklift_D and cofactor_S==ranklift_S, [cofactor_D,cofactor_S])
check('scalar Schur Gram factor',ranklift_D==3*A.det()*ranklift_S,[ranklift_D,A.det(),ranklift_S])
check('wrong omitted scalar Gram rejected',ranklift_D!=A.det()*ranklift_S)
M=s.zeros(3,9)
for c in range(3):
    for j in range(3): M[c,3*c+j]=1
check('actual cycle root covariance',zero(M*d-dc*J.T))
C=s.Rational(5,12)*s.eye(3); Rc=(s.eye(3)+dc.T*C*dc).inv(); Rhalf=Pc+s.Rational(2,3)*(s.eye(3)-Pc)
check('rational profile square root',zero(Rhalf*Rhalf-Rc))
F=I*I.T*d.T+J*(Pc*J.T*d.T+Rhalf*dc.T*M); Fnaive=I*I.T*d.T+J*Rhalf*dc.T*M
G=F*d; Gn=Fnaive*d
check('completed ghost common constants',zero(G*s.ones(9,1)) and zero(G.T*s.ones(9,1)) and G.rank()==8)
detG=(G+Pf).det(); detGn=(Gn+Pf).det(); detDc=(Dc+Pc).det()
check('completed ghost Gram factor',detG==3*A.det()*detDc*Rhalf.det(),[detG,detGn])
check('wrong root mean deletion rejected',detGn!=detG and not zero(Gn.T*s.ones(9,1)))
QF=F.T*F; QN=Fnaive.T*Fnaive
check('neutral normalized gauge determinant',s.factor((QF+Pf).det()*ranklift_D/detG**2)==1)
check('inconsistent naive quotient rejected',s.factor((QN+Pf).det()*ranklift_D/detGn**2)==3)

# Harmonic graph with counting-normalized four-dimensional M=ell^-1.
ell=s.Integer(3); m=1/ell; a,r=s.symbols('a r',real=True); c=1+a*a+a*r+2*r*r
JH=c*s.Matrix([[m*m,-m],[-m,1]])
nh=s.Matrix([1,m]); Ph=nh*nh.T/(nh.dot(nh))
pdetH=s.factor((JH+Ph).det())
Z=c*m*m; X=c
check('harmonic graph rank and null',JH.det()==0 and zero(JH*nh))
check('coarse elimination harmonic Gram',s.factor(pdetH-X*(1+m*m))==0)
check('fine elimination harmonic Gram',s.factor(pdetH-Z*(1+m**-2))==0)
check('wrong harmonic norm exchange rejected',s.factor(pdetH-X*(1+m**-2))!=0)
# The harmonic contribution to G_perp is 1/2 log Z + 1/2 log C.
ratio=s.factor(Z/c)
check('harmonic normalized constant',ratio==ell**-2,ratio)
check('harmonic mixed derivatives cancel',s.diff(s.log(ratio),a,r)==0 and s.diff(s.log(ratio),a,2)==0)
check('individual harmonic derivatives nonzero',s.diff(s.log(c),a,r).subs({a:0,r:0})==1)

# Actual four-dimensional mesh, with its exact q=0 prescription.
mesh=list(itertools.product((0,1,2),repeat=4)); loop=s.Rational(0)
for q in mesh:
    comp=[0 if x==0 else 3 for x in q]; lam=sum(comp)
    if lam: loop+=s.Rational(comp[0]+comp[1],lam)
loop/=81
check('neutral Wilson loop finite zero fibre',loop==s.Rational(40,81),loop)
for N in (2,3,4):
    basis=s.zeros(N,N-1)
    for j in range(N-1): basis[j,j]=1; basis[N-1,j]=-1
    metric=(basis.T*basis)/N
    colour=basis*metric.inv()*basis.T
    check('Cartan completeness N='+str(N),zero(colour-(N*s.eye(N)-s.ones(N))))
    beta=-(N-1)*loop/2
    check('nonzero finite Wilson coefficient N='+str(N),beta==-(N-1)*s.Rational(1,4)*(1-s.Rational(1,81)) and beta!=0,beta)

# Actual normalized SU(2) action from contour average, not FC2 as input.
t,z,delta=s.symbols('t z delta',real=True)
phi=s.sqrt((5+4*s.cos(3*t*z))/9)-(2*s.cos(t*(z+delta))+s.cos(t*(2*z-delta)))/3
poly=s.expand(s.series(phi,t,0,6).removeO())
expected=t*t*delta*delta/2+t**4*(delta*z**3/3-delta*delta*z*z/2-delta**4/24)
check('actual normalized contour quartic',s.expand(poly-expected)==0,poly)
check('neutral cubic zero',poly.coeff(t,3)==0)
check('polar correction retained',poly.coeff(t,4).coeff(delta,2).coeff(z,2)==-s.Rational(1,2))
check('wrong constant polar metric rejected',s.expand(poly-(expected+t**4*delta**2*z**2/2))!=0)

x,v,b3=s.symbols('x v b3')
E=x*x-x*v+v*v/2-x**4/24-x*x*v*v/4+v**4/7
xjet=v/2+b3*v**3
station=s.series(s.diff(E,x).subs(x,xjet),v,0,5).removeO()
b3val=s.solve(station.coeff(v,3),b3)[0]
value=s.series(E.subs(x,xjet.subs(b3,b3val)),v,0,6).removeO().expand()
quartic=s.expand((-x**4/24-x*x*v*v/4+v**4/7).subs(x,v/2)).coeff(v,4)
check('stationary quartic direct substitution',value.coeff(v,4)==quartic and b3val!=0,[b3val,quartic])
check('wrong removed neutral quartic rejected',quartic!=0)
print(json.dumps({'scope':'exact finite neutral-domain, quartic and harmonic controls; no thermodynamic or depth-uniform verdict','passed':sum(c['passed'] for c in checks),'total':len(checks),'checks':checks},indent=2))
