"""Challenge common-metric native frame construction and physical support."""
from pathlib import Path
from itertools import product
from collections import deque
import hashlib,json,math,time
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent


def run():
    start=time.monotonic();checks=[]
    def check(name,ok,**details):
        assert bool(ok),(name,details)
        checks.append(dict(name=name,**details))
    def eq(name,a,b):
        z=a-b
        vals=list(z) if isinstance(z,s.MatrixBase) else [z]
        check(name,all(s.trigsimp(s.expand_complex(x))==0 for x in vals))
    k=s.symbols('kx ky kz',real=True)
    theta=s.symbols('theta',real=True)
    zeta=s.cos(theta);v=s.sin(theta)
    F=s.Matrix(3,3,s.symbols('f0:9',real=True))
    F0=s.diag(1,1,v);ff=F-F0
    b=zeta-s.cos(k[2]);r=2-s.cos(k[0])-s.cos(k[1])
    d=s.Matrix([s.sin(k[0]),s.sin(k[1]),r+b])
    vertices=s.Matrix([[s.sin(k[0]),s.sin(k[1]),b*s.sin(k[2])/v**2],
                       [s.sin(k[0]),s.sin(k[1]),b*s.sin(k[2])/v**2],
                       [s.sin(k[2])*s.sin(k[0])/v,s.sin(k[2])*s.sin(k[1])/v,b/v]])
    deformed=d+s.Matrix([sum(ff[a,j]*vertices[a,j] for j in range(3)) for a in range(3)])
    naive=F*s.Matrix([s.sin(k[0]),s.sin(k[1]),b/v])+s.Matrix([0,0,r])
    for w in(-1,1):
        sub={k[0]:0,k[1]:0,k[2]:w*theta}
        R=s.diag(1,1,w)
        eq('all_frame_values_preserve_node_'+str(w),deformed.subs(sub),s.zeros(3,1))
        eq('exact_common_frame_tangent_'+str(w),deformed.jacobian(k).subs(sub),R*F)
        eq('exact_naive_frame_tangent_'+str(w),naive.jacobian(k).subs(sub),F*R)
        eq('common_principal_metric_'+str(w),(R*F).T*(R*F),F.T*F)
    t=s.symbols('t',real=True)
    shear=s.Matrix([[1,0,t],[0,1,0],[t,0,v]])
    gp=shear.T*shear
    gm=s.diag(1,1,-1)*gp*s.diag(1,1,-1)
    eq('naive_metric_shear_difference',gp[0,2]-gm[0,2],2*t*(1+v))
    check('shear_witness_is_nonzero',(gp[0,2]-gm[0,2]).subs({t:s.Rational(1,10),theta:s.pi/3})!=0)

    # Separate finite Laurent coefficient construction, as actual directed
    # hopping displacements rather than differentiating the supplied vertices.
    def vec(j,n=1):
        q=[0,0,0];q[j]=n;return tuple(q)
    def sincoeff(j,scale=1,step=1):
        return {vec(j,step):scale/(2*s.I),vec(j,-step):-scale/(2*s.I)}
    laurent={}
    for a in range(3):
        for j in range(3):
            if a<2 and j<2: co=sincoeff(j)
            elif a<2:
                co=sincoeff(2,zeta/v**2)
                co.update(sincoeff(2,-1/(2*v**2),2))
            elif j<2:
                co={}
                for sj,sz in product((-1,1),repeat=2):
                    q=[0,0,sz];q[j]=sj
                    co[tuple(q)]=-sj*sz/(4*v)
            else:
                co={(0,0,0):zeta/v,vec(2):-1/(2*v),vec(2,-1):-1/(2*v)}
            laurent[a,j]=co
            for w in(-1,1):
                zero=sum(c*s.exp(s.I*q[2]*w*theta) for q,c in co.items())
                eq('Laurent_node_'+str((a,j,w)),zero,0)
                for ell in range(3):
                    jet=sum(s.I*q[ell]*c*s.exp(s.I*q[2]*w*theta) for q,c in co.items())
                    eq('Laurent_jet_'+str((a,j,w,ell)),jet,(w if a==2 else 1)*int(j==ell))

    # Literal shortest protected paths on open virtual boxes, including thin
    # x boxes where detours at a boundary must use the other direction.
    sig=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
    routed=0;maxlen=0
    for shape in((3,3,3),(1,3,3),(2,2,3)):
        cells=list(product(*(range(n) for n in shape)))
        cellset=set(cells)
        nodes={(2*x[0]+rr,x[1],x[2]) for x in cells for rr in(0,1)}
        def protected(a,b):
            if a[1]!=b[1]:
                tail=min(a,b)
                return (tail[0]+tail[1])%2==0
            return True
        def path(a,b):
            todo=deque([(a,0)]);seen={a}
            while todo:
                here,dist=todo.popleft()
                if here==b:return dist
                if dist==4:continue
                for j,sgn in product(range(3),(-1,1)):
                    there=list(here);there[j]+=sgn;there=tuple(there)
                    if there in nodes and there not in seen and protected(here,there):
                        seen.add(there);todo.append((there,dist+1))
            return None
        for (a,j),co in laurent.items():
            for displacement in co:
                for x in cells:
                    target=tuple(x[i]+displacement[i] for i in range(3))
                    if target not in cellset:continue
                    for r0,r1 in product((0,1),repeat=2):
                        if sig[a][r0,r1]==0:continue
                        p0=(2*x[0]+r0,x[1],x[2]);p1=(2*target[0]+r1,target[1],target[2])
                        length=path(p0,p1)
                        check('protected_frame_hopping_'+str(routed),length is not None and length<=4,
                              shape=shape,length=length)
                        maxlen=max(maxlen,length);routed+=1
    check('four_edge_route_is_exercised',maxlen==4)

    # The proof's global relative bound is challenged away from the nodes,
    # near each node and at trigonometric corners, for three fixed zetas.
    rng=np.random.default_rng(60613)
    fixed=rng.normal(size=(3,3));fixed=(fixed+fixed.T)/2;fixed/=np.linalg.norm(fixed)
    reports=[]
    for zz in(.5,.8,.99):
        vv=math.sqrt(1-zz*zz);star=math.acos(zz)
        deltaF=fixed*vv**2/(4*math.sqrt(10))
        sample=rng.uniform(-math.pi,math.pi,(600,3))
        corners=np.array(list(product((0.,math.pi),repeat=3)))
        near_nodes=np.vstack([np.array([0,0,w*star])+1e-4*rng.normal(size=(30,3)) for w in(-1,1)])
        sample=np.vstack([sample,corners,near_nodes])
        sx,sy,sz=np.sin(sample).T;cx,cy,cz=np.cos(sample).T
        dd=np.array([sx,sy,2+zz-cx-cy-cz]).T
        norm=np.linalg.norm(dd,axis=1)
        vertex=np.empty((len(sample),3,3))
        vertex[:,0,:]=vertex[:,1,:]=np.array([sx,sy,(zz-cz)*sz/vv**2]).T
        vertex[:,2,:]=np.array([sz*sx/vv,sz*sy/vv,(zz-cz)/vv]).T
        perturb=np.einsum('aj,naj->na',deltaF,vertex)
        error=np.linalg.norm(perturb,axis=1)
        check('global_relative_bound_challenge_'+str(zz),np.max(error/norm)<.25,
              max_ratio=float(np.max(error/norm)),proved_upper=.25)
        check('two_node_preservation_lower_bound_challenge_'+str(zz),
              np.min(np.linalg.norm(dd+perturb,axis=1)/norm)>.75)
        reports.append(dict(zeta=zz,samples=len(sample),max_relative=float(np.max(error/norm))))
    out=dict(status='PASS',checks=len(checks),details=checks,routed_hoppings=routed,max_path_length=maxlen,
             numerical_challenges=reports,elapsed_seconds=time.monotonic()-start,
             source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             scope='Exact symbolic node/metric identities and literal finite protected routes; global preservation is the analytical relative-bound theorem, not inferred from samples.')
    (HERE/'BLOCK06_FRAME_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='details'},indent=2))

if __name__=='__main__':run()
