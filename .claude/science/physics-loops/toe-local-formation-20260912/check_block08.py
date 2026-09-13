"""Small independent geometry and Taylor checks for hyperdiagonal compatibility."""
import itertools,json,hashlib,time,signal
from pathlib import Path
import sympy as s
import mpmath as mp
AUDIT_TIMEOUT_SEC=180
signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError('180-second budget')))
signal.alarm(AUDIT_TIMEOUT_SEC)
started=time.monotonic(); checks=[]
def check(name,cond):
    if not cond:raise AssertionError(name)
    checks.append(name)
lam=s.Symbol('lam',real=True)
th1=s.acos(s.sqrt((4-lam**2)/(2*(8-lam**2))))
th2=s.acos(-2*lam/(8-lam**2))
A1=s.sqrt(s.Rational(3,4)-lam**2/16);A2=s.sqrt(1-lam**2/16)
d1=2*s.pi-6*th1;d2=2*s.pi-4*th2
fp=-lam*(8*d1/A1+6*d2/A2)/16
check('first_deficit_series',s.simplify(s.series(d1,lam,0,4).removeO()+s.sqrt(3)*lam**2/8)==0)
check('second_deficit_series',s.simplify(s.series(d2,lam,0,5).removeO()+lam+13*lam**3/96)==0)
check('action_derivative_series',s.simplify(s.series(fp,lam,0,5).removeO()-3*lam**2/8-lam**3/8-lam**4/16)==0)
check('wrong_cubic_sign_rejected',s.simplify(s.diff(fp,lam,2).subs(lam,0))==s.Rational(3,4))
print('exact Taylor coefficients checked',flush=True)

# Local normals independently compared with literal hinge triangle Gram determinants.
X=[s.Matrix([int(i<j) for i in range(4)]) for j in range(5)]
n=[s.Matrix([-1,0,0,0]),s.Matrix([1,-1,0,0]),s.Matrix([0,1,-1,0]),s.Matrix([0,0,1,-1]),s.Matrix([0,0,0,1])]
for i,j in itertools.combinations(range(5),2):
    hinge=[a for a in range(5) if a not in (i,j)]
    U=(X[hinge[1]]-X[hinge[0]]).row_join(X[hinge[2]]-X[hinge[0]])
    check('hinge_normal_area_'+str(i)+str(j),(U.T*U).det()==n[i].dot(n[i])*n[j].dot(n[j])-n[i].dot(n[j])**2)
    check('hinge_normal_plane_'+str(i)+str(j),U.T*n[i]==s.zeros(2,1) and U.T*n[j]==s.zeros(2,1))

# Cross coefficient by a separate incidence census of the six 2+2 splits.
B=s.zeros(4);hs={}
for a,b in itertools.combinations(range(4),2):
    hs[a,b]=s.Symbol('h'+str(a)+str(b));B[a,b]=B[b,a]=hs[a,b]
cs=0
for A in itertools.combinations(range(4),2):
    u=s.Matrix([int(a in A) for a in range(4)]);v=s.ones(4,1)-u
    cs+=2*(u.T*B*v)[0]
check('uniform_shear_mixed_coefficient',s.expand(cs-8*sum(hs.values()))==0)

mp.mp.dps=65
verts=[mp.matrix([int(i<j) for i in range(4)]) for j in range(5)]
perms=list(itertools.permutations(range(4)))
sets=[tuple(i for i,x in enumerate(v) if x) for v in itertools.product((0,1),repeat=4) if any(v)]
full=tuple(range(4))
def dot(M,a,b):return (a.T*M*b)[0]
def flat_metric(shear):
    M=mp.eye(4);M[0,1]=M[1,0]=shear;return M

def cell_action(mu,shear=mp.mpf('0')):
    G=flat_metric(shear)
    area_sum=mp.mpf('0')
    for W in sets:
        for U in sets:
            if set(U)<set(W):
                u=mp.matrix([int(i in U) for i in range(4)])
                v=mp.matrix([int(i in W)-int(i in U) for i in range(4)])
                qa,qb=dot(G,u,u),dot(G,v,v)
                qc=dot(G,u+v,u+v)+(mu if W==full else 0)
                area_sum+=mp.sqrt((2*qa*qb+2*qa*qc+2*qb*qc-qa**2-qb**2-qc**2)/16)
    angle_sum=mp.mpf('0')
    for perm in perms:
        M=mp.matrix([[G[perm[a],perm[b]] for b in range(4)] for a in range(4)])
        M[0,3]+=mu/2;M[3,0]+=mu/2
        for a,b in itertools.combinations(range(5),2):
            h=[i for i in range(5) if i not in (a,b)]
            u,v=verts[h[1]]-verts[h[0]],verts[h[2]]-verts[h[0]]
            legs=[verts[a]-verts[h[0]],verts[b]-verts[h[0]]]
            D=mp.matrix([[dot(M,u,u),dot(M,u,v)],[dot(M,v,u),dot(M,v,v)]])
            inv=D**-1
            def projected(i,j):
                ai=mp.matrix([dot(M,u,legs[i]),dot(M,v,legs[i])])
                aj=mp.matrix([dot(M,u,legs[j]),dot(M,v,legs[j])])
                return dot(M,legs[i],legs[j])-(ai.T*inv*aj)[0]
            cosine=projected(0,1)/mp.sqrt(projected(0,0)*projected(1,1))
            theta=mp.acos(cosine)
            angle_sum+=mp.sqrt(mp.det(D))*theta/2
    return 2*mp.pi*area_sum-angle_sum

def derivative(mu):
    t1=mp.acos(mp.sqrt((4-mu**2)/(2*(8-mu**2))))
    t2=mp.acos(-2*mu/(8-mu**2))
    return -mu*(8*(2*mp.pi-6*t1)/mp.sqrt(mp.mpf(3)/4-mu**2/16)+6*(2*mp.pi-4*t2)/mp.sqrt(1-mu**2/16))/16
base=cell_action(mp.mpf(0))
check('literal_flat_cell_action',abs(base)<mp.mpf('1e-60'))
rows=[]
for mu in [mp.mpf('0.2'),mp.mpf('-0.2')]:
    actual=cell_action(mu)-base
    integral=mp.quad(derivative,[0,mu])
    error=abs(actual-integral)
    check('nonlinear_action_integral_'+str(mu),error<mp.mpf('1e-58'))
    rows.append({'mu':str(mu),'literal_action':str(actual),'integrated_derivative':str(integral),'error':str(error)})
    print('literal action versus derivative',mu,mp.nstr(error,5),flush=True)

coeff=[]
for shear_ratio,target in [(0,mp.mpf(1)/8),(1,mp.mpf(3)/8),(-1,-mp.mpf(1)/8)]:
    estimates=[]
    for step in [mp.mpf('0.002'),mp.mpf('0.001')]:
        plus=cell_action(step,shear_ratio*step)
        minus=cell_action(-step,-shear_ratio*step)
        estimates.append((plus-minus)/(2*step**3))
    richardson=(4*estimates[1]-estimates[0])/3
    check('uniform_shear_cubic_'+str(shear_ratio),abs(richardson-target)<mp.mpf('1e-9'))
    coeff.append({'shear_ratio':shear_ratio,'expected':str(target),'two_step_extrapolate':str(richardson),'error':str(abs(richardson-target))})
    print('cubic ray',shear_ratio,mp.nstr(richardson,18),flush=True)

out={'scope':'one exact local family and constant-metric/hyperdiagonal tangents; no general curved-tangent or physical instability theorem',
     'status':'passed','checks':checks,'count':len(checks),'nonlinear_comparisons':rows,
     'cubic_ray_diagnostics':coeff,'numerical_limit':'high precision and finite-step extrapolation support the separately derived exact coefficients; no interval remainder certificate',
     'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'elapsed_sec':time.monotonic()-started}
Path(__file__).with_name('BLOCK08_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'checks':len(checks),'elapsed_sec':out['elapsed_sec']}))
signal.alarm(0)
