"""Independent literal 3D Christoffel/adjoint control, no author imports.

Price: <=30 CPU seconds, <=150 MB. Dense first derivatives only, n=3,5.
The analytic argument, not these floating point samples, is the proof.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS'):
    os.environ[key] = '1'
import json, time, resource, pathlib, datetime, hashlib
resource.setrlimit(resource.RLIMIT_CPU, (30, 35))
import numpy as np

ROOT = pathlib.Path(__file__).resolve().parent
RUNTIME = pathlib.Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
deadline = json.loads((RUNTIME/'DEADLINE.json').read_text())['deadline_epoch']
assert time.time() < deadline and not (RUNTIME/'STOP_REQUESTED.json').exists()
start = time.time()
pairs = [(0,0),(1,1),(2,2),(0,1),(0,2),(1,2)]
a, K, eps = 1.3, .7, 1e-24

def matrix(x, momentum=False):
    y = np.zeros(x.shape[:-1]+(3,3), dtype=x.dtype)
    for t,(i,j) in enumerate(pairs):
        v = x[...,t] / (2 if momentum and i != j else 1)
        y[...,i,j] = y[...,j,i] = v
    return y

def local(g, p, q, r):
    G = matrix(g)
    Q = matrix(q)
    inv = np.linalg.inv(G)
    s = np.sqrt(np.linalg.det(G))
    B = s[...,None,None]*inv
    pi = matrix(p, True)
    tr = np.einsum('...ij,...ji->...',G,pi)
    gp = np.einsum('...ij,...jk->...ik',G,pi)
    T = a/s*(np.einsum('...ij,...ji->...',gp,gp)-.5*tr*tr)
    gam = np.zeros(G.shape[:-2]+(3,3,3),dtype=np.result_type(g,p,q,r))
    for k in range(3):
        for i in range(3):
            for j in range(3):
                for l in range(3):
                    gam[...,k,i,j] += .5*inv[...,k,l]*(Q[...,i,j,l]+Q[...,j,i,l]-Q[...,l,i,j])
    V = np.zeros_like(T,dtype=np.result_type(g,p,q,r))
    for i in range(3):
        for j in range(3):
            for k in range(3):
                V += K*(r[...,k,i,j]*gam[...,k,i,j]-r[...,j,i,j]*gam[...,k,i,k])
                for l in range(3):
                    V -= K*B[...,i,j]*(gam[...,k,k,l]*gam[...,l,i,j]-gam[...,k,j,l]*gam[...,l,i,k])
    return T,V,B,gam

def make_derivative(n):
    xs = 2*np.pi*np.arange(n)/n
    delta = xs[:,None]-xs[None,:]
    D = sum(-2*k/n*np.sin(k*delta) for k in range(1,(n+1)//2))
    def diff(f,j):
        return np.moveaxis(np.tensordot(D,f,axes=(1,j)),0,j)
    return D,diff

def fields(n):
    x,y,z = np.meshgrid(*(2*np.pi*np.arange(n)/n for _ in range(3)),indexing='ij')
    g = np.stack([1+.02*np.cos(x)+.005*np.sin(y+z),1+.014*np.sin(y),1+.018*np.cos(z),
                  .004*np.cos(x+y),.003*np.sin(y-z),.005*np.cos(z+x)],axis=-1)
    p = np.stack([.08+.03*np.sin(x),-.06+.02*np.cos(y+z),.04+.01*np.sin(z),
                  .023*np.cos(x-z),.016*np.sin(y+x),-.018*np.cos(z-y)],axis=-1)
    return g,p

def original_H(g,p,diff):
    q = np.stack([diff(g,j) for j in range(3)],axis=-2)
    dummy = np.zeros(g.shape[:-1]+(3,3,3),dtype=g.dtype)
    T,_,B,gam = local(g,p,q,dummy)
    R = np.zeros_like(B)
    for i in range(3):
        for j in range(3):
            for k in range(3):
                R[...,i,j] += diff(gam[...,k,i,j],k)-diff(gam[...,k,i,k],j)
                for l in range(3):
                    R[...,i,j] += gam[...,k,k,l]*gam[...,l,i,j]-gam[...,k,j,l]*gam[...,l,i,k]
    return np.mean(T-K*np.einsum('...ij,...ij->...',B,R))

def adjoint_gradient(g,p,diff):
    q = np.stack([diff(g,j) for j in range(3)],axis=-2)
    dummy = np.zeros(g.shape[:-1]+(3,3,3))
    B = local(g,p,q,dummy)[2]
    r = np.stack([diff(B,j) for j in range(3)],axis=-3)
    T,V,_,_ = local(g,p,q,r)
    Tg,Vg,Tp = (np.zeros_like(g) for _ in range(3))
    Vq,Vr = np.zeros_like(q),np.zeros_like(r)
    for t in range(6):
        gc = g.astype(complex); gc[...,t] += 1j*eps
        tt,vv,_,_ = local(gc,p,q,r)
        Tg[...,t],Vg[...,t] = tt.imag/eps,vv.imag/eps
        pc = p.astype(complex); pc[...,t] += 1j*eps
        Tp[...,t] = local(g,pc,q,r)[0].imag/eps
    for j in range(3):
        for t in range(6):
            qc = q.astype(complex); qc[...,j,t] += 1j*eps
            Vq[...,j,t] = local(g,p,qc,r)[1].imag/eps
        for u in range(3):
            for v in range(3):
                rc = r.astype(complex); rc[...,j,u,v] += 1j*eps
                Vr[...,j,u,v] = local(g,p,q,rc)[1].imag/eps
    inv = np.linalg.inv(matrix(g)); s = np.sqrt(np.linalg.det(matrix(g)))
    Bg = np.zeros(g.shape[:-1]+(6,3,3))
    for t,(u,v) in enumerate(pairs):
        E = np.zeros((3,3)); E[u,v] = E[v,u] = 1
        trace = np.einsum('...ij,ji->...',inv,E)
        Bg[...,t,:,:] = s[...,None,None]*(.5*trace[...,None,None]*inv-np.einsum('...ij,jk,...kl->...il',inv,E,inv))
    grad_no_r = Tg+Vg-sum(diff(Vq[...,j,:],j) for j in range(3))
    r_adj = np.einsum('...tij,...ij->...t',Bg,sum(diff(Vr[...,j,:,:],j) for j in range(3)))
    grad = grad_no_r-r_adj
    r_wrong = np.einsum('...tij,...kt->...kij',Bg,q)
    false_H = np.mean(T+local(g,p,q,r_wrong)[1])
    pi,G = matrix(p,True),matrix(g)
    tr = np.einsum('...ij,...ji->...',G,pi)
    explicit_Tp = 2*a/s[...,None,None]*(np.einsum('...ij,...jk,...kl->...il',G,pi,G)-.5*G*tr[...,None,None])
    exp6 = np.stack([explicit_Tp[...,i,j] for i,j in pairs],axis=-1)
    diagnostics = {
        'original_vs_augmented_H': float(abs(original_H(g,p,diff)-np.mean(T+V))),
        'explicit_Tp_error': float(np.max(abs(Tp-exp6))),
        'false_chain_rule_r_max_error': float(np.max(abs(r-r_wrong))),
        'false_chain_rule_H_error': float(abs(original_H(g,p,diff)-false_H)),
        'omitted_r_adjoint_max_error': float(np.max(abs(r_adj))),
        'minimum_metric_eigenvalue': float(np.linalg.eigvalsh(G).min())}
    return grad,Tp,diagnostics

output = {'description':'Independent full 3D local partials and literal original-H variation; author code not imported or executed.',
          'couplings':{'a':a,'K':K},'epsilon':eps,'grids':[]}
for n in (3,5):
    assert time.time() < deadline and not (RUNTIME/'STOP_REQUESTED.json').exists()
    D,diff = make_derivative(n)
    g,p = fields(n)
    hg,hp,record = adjoint_gradient(g,p,diff)
    errors=[]
    if n == 3:
        for var,expected in ((0,hg),(1,hp)):
            for index in np.ndindex(g.shape):
                gc,pc = g.astype(complex),p.astype(complex)
                (gc if var==0 else pc)[index] += 1j*eps
                actual = original_H(gc,pc,diff).imag/eps*n**3
                errors.append(float(abs(actual-expected[index])))
        record['checked_coordinate_derivatives'] = len(errors)
    else:
        rng = np.random.default_rng(9302026)
        for _ in range(24):
            dg,dp = rng.standard_normal(g.shape),rng.standard_normal(p.shape)
            actual = original_H(g+1j*eps*dg,p+1j*eps*dp,diff).imag/eps
            expected = np.mean(np.sum(hg*dg+hp*dp,axis=-1))
            errors.append(float(abs(actual-expected)))
        record['checked_dense_tangent_directions'] = len(errors)
    record.update(n=n,sites=n**3,max_gradient_error=max(errors),derivative_skew_error=float(np.max(abs(D+D.T))))
    output['grids'].append(record)
output.update(wall_seconds=time.time()-start,cpu_seconds=time.process_time(),max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
              script_sha256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
(ROOT/'full_variation.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
