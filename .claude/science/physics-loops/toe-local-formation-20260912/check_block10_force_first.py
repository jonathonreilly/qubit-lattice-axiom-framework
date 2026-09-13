"""Full force compatibility and an exact finite second-order solution."""
import itertools,json,time,hashlib,signal
from pathlib import Path
import sympy as s
AUDIT_TIMEOUT_SEC=180
signal.alarm(AUDIT_TIMEOUT_SEC);started=time.monotonic();checks=[]
def check(name,condition):
    if not condition:raise AssertionError(name)
    checks.append(name)
P,A,B,O=s.symbols('P A B O',real=True)
path=Path(__file__).with_name('BLOCK10_FORCE_FIRST.json');data=json.loads(path.read_text());sym={'P':P,'A':A,'B':B}
force=s.Matrix([s.sympify(x,locals=sym) for x in data['force']])
g=B-A;gm=A-P;energy=g*g+gm*gm;lap_phi2=B*B+P*P-2*A*A
expected=s.zeros(15,1);expected[0]=3*energy/4;expected[1]=expected[3]=lap_phi2-energy/4;expected[7]=g*g/2
check('all_fifteen_force_stencils',all(s.expand(x)==0 for x in force-expected))
source=s.zeros(15,1)
for mask,weight in [(8,1),(4,-1),(2,-1),(1,3)]:source[mask-1]=weight*g*g/2
res=(source-force).applyfunc(s.expand)
check('hyper_projection_zero',res[14]==0)
for axis in range(4):
    bit=1<<(3-axis)
    div=sum(res[mask-1].subs({P:O,A:P,B:A},simultaneous=True)-res[mask-1] for mask in range(1,16) if mask&8 and mask&bit)
    check('all_period_gauge_divergence_'+str(axis),s.expand(div)==0)
# Every constant-metric projection is an explicit telescoping quadratic flux.
fluxes={}
for a,b in [(j,j) for j in range(4)]+list(itertools.combinations(range(4),2)):
    ba,bb=1<<(3-a),1<<(3-b)
    polynomial=s.expand(sum((1 if a==b else 2)*res[mask-1] for mask in range(1,16) if mask&ba and mask&bb))
    poly=s.Poly(polynomial,P,A,B);cp=poly.coeff_monomial(P*P);cb=poly.coeff_monomial(B*B);cpa=poly.coeff_monomial(P*A)
    flux=lambda x,y:cp*x*x-cb*y*y+cpa*x*y
    check('all_period_constant_metric_'+str(a)+str(b),s.expand(polynomial-flux(P,A)+flux(A,B))==0)
    fluxes[str((a,b))]=str(flux(P,A))

# Assemble the 3x15 real-space Hessian from the displayed independent rational table.
L=3;fields=[s.Integer(-1),s.Integer(-1),s.Integer(2)]
Q0=s.Matrix([[0,0,0,0,0,3,0,-6,0,0],[0,-3,3,0,6,-6,0,3,0,0],[0,3,-2,0,-6,3,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,6,-6,0,-6,6,0,0,3,-6],[3,-6,3,0,6,-6,3,6,-6,3],[0,0,0,0,0,3,-2,-6,3,0],[-6,3,0,0,0,6,-6,-6,6,0],[0,0,0,0,3,-6,3,6,-3,0],[0,0,0,0,-6,3,0,0,0,0]])/48
Q=s.zeros(15*L);pairs=list(itertools.combinations(range(5),2))
for n in range(L):
    for perm in itertools.permutations(range(4)):
        maps=[]
        for i,j in pairs:
            mask=sum(1<<(3-a) for a in perm[i:j]);anchor=(n+int(0 in perm[:i]))%L
            maps.append(15*anchor+mask-1)
        for i in range(10):
            for j in range(10):Q[maps[i],maps[j]]+=Q0[i,j]
v=s.zeros(15*L,1);J1=s.zeros(15*L,1);J2=s.zeros(15*L,1);N=s.zeros(15*L,1)
for n in range(L):
    sub={P:fields[(n-1)%L],A:fields[n],B:fields[(n+1)%L]}
    J1[15*n]=sub[B]-2*sub[A]+sub[P]
    J2[15*n:15*(n+1),0]=source.subs(sub)
    N[15*n:15*(n+1),0]=force.subs(sub)
    for mask in range(1,16):
        count=mask.bit_count();nt=mask&1;last=fields[(n+int(bool(mask&8)))%L]
        v[15*n+mask-1]=(2*nt-count)*(fields[n]+last)
check('finite_linear_source_equation',Q*v==J1)
check('finite_full_rank',Q.rank()==24)
solution,parameters=Q.gauss_jordan_solve(J2-N)
w=solution.subs({x:0 for x in parameters})
check('finite_exact_second_order_solution',Q*w+N==J2)
check('nonzero_source_correction_needed',N!=s.zeros(15*L,1))
wrong=J2.copy();wrong[7]=0
check('one_longitudinal_stress_removed_rejected',(Q.row_join(wrong-N)).rank()>Q.rank())
# A closed representative uses one inverse Laplacian and no generic matrix solve.
Lap=s.zeros(L)
for n in range(L):Lap[n,n]=2;Lap[n,(n-1)%L]-=1;Lap[n,(n+1)%L]-=1
sqg=[(fields[(n+1)%L]-fields[n])**2 for n in range(L)]
h=s.Matrix([sqg[n]-sqg[(n-1)%L] for n in range(L)])
u=(Lap+s.ones(L)/L).inv()*h
check('zero_mean_antiderivative',sum(u)==0 and Lap*u==h)
mean2=sum(x*x for x in fields)/L
closed=s.zeros(15*L,1)
for n in range(L):
    metric=[0,3*u[n]/2,3*u[n]/2,4*(fields[n]**2-mean2)-5*u[n]/2]
    for mask in range(1,16):closed[15*n+mask-1]=sum(metric[a] for a in range(4) if mask&(1<<(3-a)))
check('closed_metric_second_order_solution',Q*closed+N==J2)

out=dict(status='passed',scope='all-period symbolic null projections and one exact finite second-order construction, not all-order existence',checks=checks,count=len(checks),constant_metric_fluxes=fluxes,fields=list(map(str,fields)),linear_tangent=list(map(str,v)),quadratic_force=list(map(str,N)),first_source=list(map(str,J1)),second_source=list(map(str,J2)),closed_second_coefficient=list(map(str,closed)),particular_second_coefficient=list(map(str,w)),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),force_input_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),elapsed_sec=time.monotonic()-started)
Path(__file__).with_name('BLOCK10_FORCE_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(checks=len(checks),elapsed_sec=out['elapsed_sec'])))
signal.alarm(0)
