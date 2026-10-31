"""Independent exact algebra, stationary jets, and d=4 Bloch controls.
No author helper is imported. Analytic proofs are in the paired review report.
"""
import sys, itertools, json, datetime
import sympy as s
import numpy as np
from scipy.linalg import eigvalsh

print('UTC', datetime.datetime.now(datetime.timezone.utc).isoformat())
print('versions', sys.version, 'sympy',s.__version__,'numpy',np.__version__)
checks=[]
def gate(name, ok, detail=None):
    ok=bool(ok); checks.append(ok)
    print(('PASS' if ok else 'FAIL'),name, '' if detail is None else detail, flush=True)

def zd(M): return all(s.simplify(v)==0 for v in M)
D=s.Matrix([1,2,1]); C=s.Matrix([[3,1,0],[1,4,1],[0,1,2]])
B=s.Matrix([[2,1],[-1,0],[0,-1]])
Ci=C.inv(method='DM'); Pi=Ci-Ci*D*(D.T*Ci*D).inv()*D.T*Ci
X=Pi+D*D.T
M=s.Matrix([[1,2,0,1],[0,1,-1,2],[2,0,1,-1]])
H=s.Matrix([[5,1,0,1],[1,4,1,0],[0,1,3,1],[1,0,1,4]])
G=s.diag(0,0,0,4); Z=H+M.T*Pi*M+G; Y=-M.T*Pi
Sch=Z-Y*X.inv()*Y.T
CE=(B.T*C*B).det(method='bareiss')/(B.T*B).det(method='bareiss')
gate('off-shell Schur cancellation',zd(Sch-H-G))
gate('Wilson block genuinely nontransverse',H*s.Matrix([0,0,0,1]) != s.zeros(4,1))
gate('ghost/Gram determinant cancellation',s.factor(X.det()*CE-(D.T*D)[0])==0)
gate('zero-residual determinant product',s.factor(X.det()*Sch.det()*CE/((D.T*D)[0]*(H+G).det()))==1)
mutPi=Ci;mutX=mutPi+D*D.T
mutSch=H+M.T*mutPi*M+G-M.T*mutPi*mutX.inv()*mutPi*M
gate('full inverse in place of transverse inverse rejected',not zd(mutSch-H-G))
t=s.symbols('t');A=s.Matrix([[4,1],[1,3]]);Cg=s.Matrix([[3,1],[1,2]]);Bg=s.Matrix([[1,2],[-1,1]]);O=s.zeros(2)
W=A.row_join(t*Bg).col_join((t*Bg.T).row_join(Cg))
Jbad=A.row_join(t*Bg).row_join(t*Bg).col_join((t*Bg.T).row_join(Cg).row_join(O)).col_join((t*Bg.T).row_join(O).row_join(Cg))
Jcorr=A.row_join(O).row_join(t*Bg).col_join(O.row_join(Cg).row_join(O)).col_join((t*Bg.T).row_join(O).row_join(Cg))
target=s.expand(Cg.det()*W.det(method='bareiss'))
gate('multidimensional corrected block',s.expand(Jcorr.det(method='bareiss')-target)==0)
delta=s.expand(Jbad.det(method='bareiss')-target)
gate('duplicated off-shell coupling rejected',delta!=0,str(delta))
pred=-s.trace(A.inv()*Bg*Cg.inv()*Bg.T)/2
coef=s.diff(s.log(Jbad.det())-s.log(target),t,2).subs(t,0)/4
gate('half-log duplicated-block coefficient',s.simplify(coef-pred)==0,str(coef))

# Independent perpendicular-first integral reduction, not Feynman parameters.
a,b=s.symbols('a b', positive=True)
J=s.pi/(2*(a+b)) # integral_0^inf u^2/((u^2+a^2)(u^2+b^2)) du by partial fractions
rad=s.simplify(-s.diff(J,b)/(2*b)-a*s.diff(J,a,b)/(4*b))
gate('perpendicular radial integral',s.simplify(rad-s.pi/(4*(a+b)**3))==0)
u=s.symbols('u', nonnegative=True);tau=s.symbols('tau',positive=True)
outer=s.integrate((tau+2*u)**-3,(u,0,s.oo));long=tau/tau**3+2*outer
core=s.simplify(s.pi**2*long/3)
gate('transverse core by perpendicular integration',s.simplify(core-s.pi**2/(2*tau**2))==0,str(core))
gate('wrong core factor rejected',s.simplify(core-s.pi**2/(4*tau**2))!=0)
R=s.symbols('R', positive=True)
bubble=s.pi**2+2*s.pi**2*s.log(R/tau)
vector=s.diff(bubble,tau)/2
gate('degree-five convolution derivative',s.simplify(vector+s.pi**2/tau)==0,str(vector))
gate('separate pole equal to dimension rejected',s.integrate(u**(-1),(u,s.Symbol('eps',positive=True),1)).has(s.log))
omega=s.Matrix([s.Rational(3,5),s.Rational(4,5)]);At=s.eye(2)-omega*omega.T
gate('direction-dependent Ward log mutation survives Ward',At!=s.zeros(2) and zd(At*omega))

# Two-source mixed stationary polynomial: exact coefficient recursion then substitution.
x1,x2,b1,b2=s.symbols('x1 x2 b1 b2'); xs=s.Matrix([x1,x2]);bs=s.Matrix([b1,b2]);vs=[x1,x2,b1,b2]
HH=s.Matrix([[3,1],[1,2]]);CC=s.Matrix([[-1,2],[1,-1]]);KK=s.Matrix([[5,1],[1,4]])
F2=(xs.T*HH*xs)[0]/2+(xs.T*CC*bs)[0]+(bs.T*KK*bs)[0]/2
F3=(x1+2*x2+b1-b2)**3/s.Integer(6)+(x1-b2)**2*b1/s.Integer(5)+x2*b1*b2/s.Integer(7)
F4=(x1-x2+2*b1+b2)**4/s.Integer(24)+x1*x2*b1*b2/s.Integer(11)
F=F2+F3+F4

def homogeneous(poly,deg):
    return s.Add(*[c*b1**m[0]*b2**m[1] for m,c in s.Poly(s.expand(poly),b1,b2).terms() if sum(m)==deg])
linear=-HH.inv()*CC*bs;xx=linear
for degree in (2,3):
    residual=s.Matrix([homogeneous(s.diff(F,x).subs(dict(zip(xs,xx)),simultaneous=True),degree) for x in xs])
    xx=xx-HH.inv()*residual
subst=dict(zip(xs,xx));eff=s.expand(F.subs(subst,simultaneous=True));eff=sum(homogeneous(eff,j) for j in range(2,5))
for j in (1,2,3):
    gate('stationarity degree '+str(j),all(homogeneous(s.diff(F,x).subs(subst,simultaneous=True),j)==0 for x in xs))

def deriv(poly,dirs,variables):
    for d in dirs:poly=sum(d[i]*s.diff(poly,z) for i,z in enumerate(variables))
    return s.expand(poly).subs({z:0 for z in variables})
dirs=[s.Matrix([1,0]),s.Matrix([0,1]),s.Matrix([1,1]),s.Matrix([2,1])]
Zeta=(-HH.inv()*CC).col_join(s.eye(2));zs=[Zeta*v for v in dirs]
E2=deriv(eff,dirs[:2],[b1,b2]);E3=deriv(eff,dirs[:3],[b1,b2]);E4=deriv(eff,dirs,[b1,b2])
gate('fully polarized quadratic jet',s.simplify(E2-deriv(F,zs[:2],vs))==0,str(E2))
gate('fully polarized cubic jet with mixed source vertices',s.simplify(E3-deriv(F,zs[:3],vs))==0,str(E3))
def cc(i,j):return s.Matrix([deriv(s.diff(F,x),[zs[i],zs[j]],vs) for x in xs])
exchanges=[(cc(i,j).T*HH.inv()*cc(k,l))[0] for (i,j,k,l) in [(0,1,2,3),(0,2,1,3),(0,3,1,2)]]
direct=deriv(F,zs,vs);exchange=sum(exchanges)
gate('fully polarized quartic jet',s.simplify(E4-direct+exchange)==0,{'E4':str(E4),'exchanges':[str(x) for x in exchanges]})
for i,value in enumerate(exchanges):gate('omitted quartic pairing '+str(i)+' rejected',value!=0 and E4!=direct-exchange+value)
gate('wrong quartic exchange sign rejected',exchange!=0 and E4!=direct+exchange)

# Actual d=4 order-averaged S4-prime contour map at depth one, L=3.
dim=4;L=3;offs=list(itertools.product(range(-1,2),repeat=dim));index={z:i for i,z in enumerate(offs)};root=index[(0,)*dim];n=len(offs)
orders=list(itertools.permutations(range(dim)))
def shift(z,mu,sgn=1):
    v=list(z);v[mu]+=sgn;return tuple(v)
def rep(z):
    of=tuple((v+1)%L-1 for v in z);cell=np.array([(z[i]-of[i])//L for i in range(dim)])
    return of,cell
def ph(p,z):
    of,cell=rep(z);return index[of],np.exp(1j*np.dot(p,cell))
def field_row(p,z,mu):
    i,c=ph(p,z);v=np.zeros(dim*n,dtype=complex);v[dim*i+mu]=c;return v

def path_vector(p,start,end,order):
    z=start;row=np.zeros(dim*n,dtype=complex)
    for mu in order:
        while z[mu]!=end[mu]:
            sg=1 if end[mu]>z[mu] else -1
            if sg==1:row+=field_row(p,z,mu);z=shift(z,mu)
            else:z=shift(z,mu,-1);row-=field_row(p,z,mu)
    assert z==end
    return row

def operators(p):
    grad=np.zeros((dim*n,n),complex);curl=[]
    for z in offs:
        i=index[z]
        for mu in range(dim):
            j,c=ph(p,shift(z,mu));grad[dim*i+mu,j]+=c;grad[dim*i+mu,i]-=1
        for mu in range(dim):
            for nu in range(mu+1,dim):
                curl.append(field_row(p,shift(z,mu),nu)-field_row(p,z,nu)-field_row(p,shift(z,nu),mu)+field_row(p,z,mu))
    Q=np.zeros((dim,dim*n),complex)
    for mu in range(dim):
        end=tuple(L if i==mu else 0 for i in range(dim))
        for y in offs:
            yp=tuple(y[i]+end[i] for i in range(dim))
            for order in orders:
                Q[mu]+=path_vector(p,(0,)*dim,y,order)+path_vector(p,y,yp,(mu,))+path_vector(p,yp,end,tuple(reversed(order)))
    Q/=len(offs)*len(orders)
    return grad,np.array(curl),Q

tree=set()
for z in offs:
    if z==(0,)*dim:continue
    mu=next(i for i,v in enumerate(z) if v)
    parent=shift(z,mu,-1 if z[mu]>0 else 1)
    base=parent if z[mu]>0 else z
    tree.add(dim*index[base]+mu)
keep=[i for i in range(dim*n) if i not in tree]
gate('tree slice dimension',len(tree)==n-1 and len(keep)==dim*n-n+1,{'removed':len(tree),'kept':len(keep)})
points=[(0.,0.,0.,0.),(.37,.81,-.43,.29),(np.pi,0.,0.,0.),(np.pi,np.pi,np.pi,np.pi),(1e-7,0.,0.,0.)]
for p in points:
    grad,curl,Q=operators(np.array(p));dc=np.exp(1j*np.array(p))-1;expected=np.zeros((dim,n),complex);expected[:,root]=dc
    err=float(np.max(np.abs(Q@grad-expected)))
    gate('S4-prime gradient covariance '+str(p),err<2e-12,err)
    Hfull=curl.conj().T@curl+Q.conj().T@Q
    rooted=np.delete(grad,root,axis=1)
    gate('rooted gauge modes '+str(p),np.max(np.abs(Hfull@rooted))<2e-11)
    Hslice=Hfull[np.ix_(keep,keep)];ev=eigvalsh(Hslice)
    gate('positive slice sample '+str(p),ev[0]>1e-8,{'min':float(ev[0]),'max':float(ev[-1])})
    if not any(p):
        bare=(curl.conj().T@curl)[np.ix_(keep,keep)];eb=eigvalsh(bare)
        gate('omitted top mismatch restores four harmonic modes',np.count_nonzero(np.abs(eb)<1e-8)==dim,{'nullity':int(np.count_nonzero(np.abs(eb)<1e-8))})
        ef=eigvalsh(Hfull)
        gate('omitted slice restores gauge modes',np.count_nonzero(np.abs(ef)<1e-8)==n-1,{'nullity':int(np.count_nonzero(np.abs(ef)<1e-8))})

# Two-dimensional product operator: Fourier diagonalization vs exact image formula.
r=.5
for T1,T2 in [(3,4),(4,5),(5,3)]:
    for dx,dy in [(0,0),(1,0),(1,2),(T1-1,T2-1)]:
        ft=sum(np.exp(2j*np.pi*(k*dx/T1+l*dy/T2))/((2.5-2*np.cos(2*np.pi*k/T1))*(2.5-2*np.cos(2*np.pi*l/T2))) for k in range(T1) for l in range(T2))/(T1*T2)
        def per(d,T):return 2/3*(r**(d%T)+r**(T-d%T))/(1-r**T)
        expected=per(dx,T1)*per(dy,T2)
        gate('2D Fourier-image identity '+str((T1,T2,dx,dy)),abs(ft-expected)<2e-14,float(abs(ft-expected)))
    omitted=(2/3)**2
    finite=per(0,T1)*per(0,T2)
    gate('2D omitted images rejected '+str((T1,T2)),abs(finite-omitted)>.01)

print('RESULT',sum(checks),'/',len(checks),'predicates passed')
print('Scope: exact finite algebra and stationary jets; numerical sampled d=4 contour controls; no all-momentum or depth-uniform theorem supplied by sampling.')
assert all(checks)
