#!/usr/bin/env python3
"""Independent top-current derivative and exact cube controls.
Imports only this review's own, already preserved Cell implementation.
"""
import itertools,json,time
import numpy as np
from review_bottom_curvature_independent import Cell, CHECKS,check,equality,detect,maxabs,phi

def source_from_cubic(cell,p,q,va,vb):
    p=np.asarray(p,complex);q=np.asarray(q,complex);k=p+q
    a,fa,ra=cell.lift(p,va);b,fb,rb=cell.lift(q,vb)
    Bp=cell.mixedB(cell.P,p,q,a,b)
    words=cell.mixedB(cell.M,p,q,a,b);B=np.zeros(4,complex);np.add.at(B,cell.softdirs,words*cell.softscale)
    top=np.zeros(4,complex)
    for mu in range(4):
        datum=np.eye(4)[mu];cc,fc,rc=cell.lift(-k,datum)
        Bbc=cell.mixedB(cell.P,q,-k,b,cc);Bca=cell.mixedB(cell.P,-k,p,cc,a)
        Sbc=cell.mixedB(cell.M,q,-k,b,cc);Sca=cell.mixedB(cell.M,-k,p,cc,a)
        top[mu]=np.sum(fa*Bbc+fb*Bca+fc*Bp)-cell.kappa*(
            np.sum(ra[cell.softdirs]*Sbc+rb[cell.softdirs]*Sca)*cell.softscale+np.dot(rc,B))
    W=cell.mixedDBdual(cell.P,p,q,a,b,fa,fb)
    M=cell.mixedDBdual(cell.M,p,q,a,b,ra[cell.softdirs],rb[cell.softdirs])*cell.softscale
    op=cell.operators(k);S=op['Qdual']@top-W+cell.kappa*M;R=op['d3']@Bp
    N=op['d2']@S+op['d3dual']@R
    phase=np.exp(-1j*(cell.coords@k)/cell.L)/cell.V
    average=lambda v:np.einsum('u,ud->d',phase,v.reshape(cell.V,-1))
    return dict(qtop=top,S=S,R=R,N=N,lowN=average(N),avg=average,op=op,W=W,M=M)

def current_controls():
    c=Cell();va=np.array([.6,-.2,.35,.1]);vb=np.array([-.15,.5,.25,-.4])
    p=np.array([.31,-.18,.21,.09])+1j*np.array([.004,-.006,.003,.005]);records=[]
    for sign in [-1,1]:
        wp=np.array([.0,.024+.004j,.013-.002j,-.008+.001j]);wp[0]=sign*np.sqrt(-np.sum(wp[1:]**2));k=6*np.arcsin(wp/6)
        source=source_from_cubic(c,p,k-p,va,vb)
        # Only now solve the second stationary coefficient.
        direct=c.evaluate(p,k-p,va,vb)
        err=equality('cubic_current_sheet_'+str(sign),source['qtop'],direct['qcur'])
        check('independent_null_numerator_'+str(sign),maxabs(source['lowN']),2e-9*(1+maxabs(source['S'])))
        equality('independent_source_'+str(sign),source['S'],direct['S'])
        op=source['op']
        for name,delta in [('Wilson_DB',op['d2']@source['W']),('soft_DB',-c.kappa*op['d2']@source['M']),('Bianchi',-op['d3dual']@source['R'])]:
            detect('independent_omit_'+name+'_'+str(sign),maxabs(source['avg'](delta)),maxabs(source['lowN']))
        records.append(dict(sheet=sign,current_error=err,low_numerator=maxabs(source['lowN']),low_curvature=maxabs(direct['lowPsi']),complex_theta=True))
    w=np.array([.014j,.014,0,0],complex);radius=.071;nodes=32;acc=np.zeros(6,complex)
    for j in range(nodes):
        z=radius*np.exp(2j*np.pi*j/nodes);ww=w.copy();ww[0]=z;k=6*np.arcsin(ww/6)
        source=source_from_cubic(c,p,k-p,va,vb)
        acc+=c.L**4*source['lowN']*z/((z*z+np.sum(ww[1:]**2))*(z-w[0]))/nodes
    k=6*np.arcsin(w/6);direct=c.evaluate(p,k-p,va,vb)
    err=equality('independent_cubic_Cauchy',acc/c.L**2,direct['lowPsi'],2e-8)
    return dict(sheets=records,cauchy_error=err,cauchy_nodes=nodes,radius=radius)

def cube_controls():
    # Exact integer SU(2) coefficient arithmetic on one cube, no periodic solve.
    verts=list(itertools.product(range(2),repeat=3));edges=[]
    for x in verts:
        for mu in range(3):
            if x[mu]==0: edges.append((x,mu))
    edgeindex={e:i for i,e in enumerate(edges)}
    def path(start,steps):
        x=list(start);out=[]
        for mu,s in steps:
            if s<0:x[mu]-=1
            out.append((edgeindex[(tuple(x),mu)],s))
            if s>0:x[mu]+=1
        return out
    faces=[];signs=[]
    for normal in range(3):
        pair=[j for j in range(3) if j!=normal]
        for side in [0,1]:
            x=[0,0,0];x[normal]=side;mu,nu=pair
            faces.append(path(x,[(mu,1),(nu,1),(mu,-1),(nu,-1)]))
            signs.append((-1)**normal*(2*side-1))
    def curl(a):return np.array([sum(s*a[i] for i,s in word) for word in faces])
    def B(a):
        out=[]
        for word in faces:
            v=[s*a[i] for i,s in word]
            out.append(sum((np.cross(v[i],v[j]) for i in range(4) for j in range(i+1,4)),start=np.zeros(3,dtype=np.int64)))
        return np.array(out)
    def div3(F):return sum((s*f for s,f in zip(signs,F)),start=np.zeros(3,dtype=np.int64))
    rng=np.random.default_rng(7241);reports=[]
    for trial in range(8):
        a=rng.integers(-4,5,size=(12,3),dtype=np.int64);lam={}
        for x in verts:
            steps=[(mu,1) for mu in range(3) if x[mu]]
            lam[x]=sum((s*a[i] for i,s in path((0,0,0),steps)),start=np.zeros(3,dtype=np.int64))
        grad=[];C=[]
        for x,mu in edges:
            y=list(x);y[mu]+=1;y=tuple(y);grad.append(lam[y]-lam[x]);C.append(np.cross(lam[x],lam[y]))
        grad=np.array(grad);C=np.array(C);rem=a-grad
        check('cube_gradient_BCH_'+str(trial),maxabs(B(grad)-curl(C)),0)
        check('cube_pure_gradient_Bianchi_'+str(trial),maxabs(div3(B(grad))),0)
        mixed=B(a)-B(grad)-B(rem)
        check('cube_factorization_'+str(trial),maxabs(div3(B(a))-div3(mixed+B(rem))),0)
        reports.append(dict(trial=trial,pure_gradient_curl=maxabs(curl(grad)),curvature=maxabs(curl(a)),mixed_Bianchi=maxabs(div3(mixed)),remainder_Bianchi=maxabs(div3(B(rem)))))
    detect('cube_mixed_af_needed',max(r['mixed_Bianchi'] for r in reports),0)
    return reports

def main():
    start=time.monotonic();res=dict(current=current_controls(),cube=cube_controls())
    print(json.dumps(dict(result=res,checks=CHECKS,passed=sum(c['passed'] for c in CHECKS),total=len(CHECKS),seconds=time.monotonic()-start),indent=2))
    raise SystemExit(0 if all(c['passed'] for c in CHECKS) else 1)
if __name__=='__main__':main()
