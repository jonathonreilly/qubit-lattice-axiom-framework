"""Full nonlinear area-deficit forces against the exact second-order construction."""
import itertools,json,time,hashlib,signal
from pathlib import Path
import mpmath as mp
import block10_distance_geometry as geometry
AUDIT_TIMEOUT_SEC=180
signal.alarm(AUDIT_TIMEOUT_SEC);mp.mp.dps=65;started=time.monotonic();checks=[]
def check(name,condition):
    if not condition:raise AssertionError(name)
    checks.append(name)
base=Path(__file__).parent;data=json.loads((base/'BLOCK10_FORCE_CHECKS.json').read_text());L=3
parse=lambda values:[mp.mpf(x.split('/')[0])/mp.mpf(x.split('/')[1]) if '/' in x else mp.mpf(x) for x in values]
v=parse(data['linear_tangent']);w=parse(data['closed_second_coefficient']);J1=parse(data['first_source']);J2=parse(data['second_source']);N=parse(data['quadratic_force'])
flat=[mp.mpf(mask.bit_count()) for n in range(L) for mask in range(1,16)]
def mask(vertex):return sum((1<<(3-i))*vertex[i] for i in range(4))
def get_q(values,n):
    def q(v,w):
        st=tuple(w[i]-v[i] for i in range(4));anchor=(n+v[0])%L
        return values[15*anchor+mask(st)-1]
    return q

def full_force(values):
    deficits={(n,u,w):2*mp.pi for n in range(L) for _,u,w in geometry.triangles}
    for n in range(L):
        q=get_q(values,n)
        for vertices in geometry.paths:
            G=geometry.simplex_data(vertices,q)
            for i,j in itertools.combinations(range(5),2):
                hh=[a for a in range(5) if a not in (i,j)];origin=vertices[hh[0]]
                u=tuple(vertices[hh[1]][a]-origin[a] for a in range(4));w=tuple(vertices[hh[2]][a]-origin[a] for a in range(4))
                _,theta=geometry.hinge_data(G,i,j)
                deficits[((n+origin[0])%L,u,w)]-=theta
    force=[mp.mpf(0)]*(15*L)
    for (n,u,w),deficit in deficits.items():
        sub=tuple(w[i]-u[i] for i in range(4))
        indices=[15*n+mask(u)-1,15*((n+u[0])%L)+mask(sub)-1,15*n+mask(w)-1]
        qa,qb,qc=[values[i] for i in indices];area=mp.sqrt(geometry.area_sq(qa,qb,qc))
        for index,derivative in zip(indices,[qb+qc-qa,qa+qc-qb,qa+qb-qc]):force[index]+=derivative*deficit/(16*area)
    return force

check('flat_all_forces',max(map(abs,full_force(flat)))<mp.mpf('1e-59'))
steps=[mp.mpf('0.001'),mp.mpf('0.0005')];linear=[];quadratic=[];rows=[]
for ep in steps:
    plus=full_force([q+ep*a for q,a in zip(flat,v)]);minus=full_force([q-ep*a for q,a in zip(flat,v)])
    linear.append([(a-b)/(2*ep) for a,b in zip(plus,minus)])
    quadratic.append([(a+b)/(2*ep**2) for a,b in zip(plus,minus)])
lin=[(4*b-a)/3 for a,b in zip(*linear)];quad=[(4*b-a)/3 for a,b in zip(*quadratic)]
lin_err=max(abs(a-b) for a,b in zip(lin,J1));quad_err=max(abs(a-b) for a,b in zip(quad,N))
check('all45_linear_forces',lin_err<mp.mpf('1e-8'))
check('all45_quadratic_forces',quad_err<mp.mpf('1e-7'))
check('all_nonaxis_quadratic_forces_zero',max(abs(quad[15*n+mask-1]) for n in range(L) for mask in range(1,16) if mask not in (1,2,4,8))<mp.mpf('1e-7'))
print('linear/quadratic max errors',mp.nstr(lin_err,8),mp.nstr(quad_err,8),flush=True)

corrected=[];uncorrected=[]
for ep in [mp.mpf('0.002'),mp.mpf('0.001'),mp.mpf('0.0005')]:
    values=[q+ep*a+ep**2*b for q,a,b in zip(flat,v,w)]
    actual=full_force(values)
    error=max(abs(f-ep*a-ep**2*b) for f,a,b in zip(actual,J1,J2))
    wrong=max(abs(f-ep*a) for f,a in zip(actual,J1))
    corrected.append(error);uncorrected.append(wrong)
    rows.append(dict(epsilon=str(ep),corrected_residual=str(error),corrected_over_epsilon_cubed=str(error/ep**3),temporal_only_residual=str(wrong)))
for i in range(2):
    ratio=corrected[i]/corrected[i+1]
    check('corrected_cubic_residual_scaling_'+str(i),7<ratio<9)
    wrongratio=uncorrected[i]/uncorrected[i+1]
    check('uncompleted_quadratic_residual_scaling_'+str(i),mp.mpf('3.8')<wrongratio<mp.mpf('4.2'))

out=dict(status='passed',scope='all45 exact-stencil coefficients checked against separate nonlinear distance-Gram forces; finite-step diagnostics do not prove the asymptotic theorem',checks=checks,count=len(checks),linear_max_error=str(lin_err),quadratic_max_error=str(quad_err),residual_rows=rows,precision_digits=mp.mp.dps,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),helper_sha256=hashlib.sha256((base/'block10_distance_geometry.py').read_bytes()).hexdigest(),force_input_sha256=hashlib.sha256((base/'BLOCK10_FORCE_CHECKS.json').read_bytes()).hexdigest(),elapsed_sec=time.monotonic()-started)
(base/'BLOCK10_NONLINEAR_FORCE_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(checks=len(checks),rows=rows,elapsed_sec=out['elapsed_sec'])))
signal.alarm(0)
