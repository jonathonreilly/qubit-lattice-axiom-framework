#!/usr/bin/env python3
"""Direct paired-determinant Hessian on the quotient by gauge directions.
Uses a different Clifford basis and explicit derivatives, not loop enumeration.
"""
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_FILES=[]
import hashlib,itertools,json,math,time
from pathlib import Path
import numpy as np
from scipy.linalg import eigh


def epsilon2(mu,kappa):
    b=(mu-6*kappa)/4;mu_b=mu-b*math.exp(b/mu);q=6*kappa/mu_b
    assert b>0 and 0<q<1
    S1=lambda z:z/(1-z)**2
    S3=lambda z:z*(1+4*z+z*z)/(1-z)**4
    loose=8*mu_b*(9*(S3(q)-q)+2/b**2*(S1(q)-q))
    z=q*q
    sharp=4*mu_b*(z/(4*b*b)+2*(9*8*(S3(z)-z)+2/b**2*2*(S1(z)-z)))
    assert 0<sharp<loose
    return loose,sharp


def make(shape,delta,mu,kappa,seed):
    sx=np.array([[0,1],[1,0]],complex);sy=np.array([[0,-1j],[1j,0]]);sz=np.diag([1.,-1.]);I=np.eye(2)
    gamma=[np.kron(sx,I),np.kron(sy,sx),np.kron(sy,sy),np.kron(sy,sz)]
    coords=list(itertools.product(*(range(n) for n in shape)));idx={x:i for i,x in enumerate(coords)}
    edges=[];edgeidx={}
    for x in coords:
        for axis in range(4):
            y=list(x);y[axis]+=1;y=tuple(y)
            if y in idx:edgeidx[axis,x]=len(edges);edges.append((axis,x,y))
    ne=len(edges);nv=len(coords);nd=4*nv;rng=np.random.default_rng(seed)
    angles=np.array([rng.normal(scale=.35*(delta if a==0 else 1)) for a,x,y in edges])
    D=np.eye(nd,dtype=complex)*(mu+1/delta);D1=np.zeros((ne,nd,nd),complex);D2=np.zeros_like(D1)
    forward=[];reverse=[];G=np.zeros((ne,nv))
    for e,(axis,x,y) in enumerate(edges):
        rate=1/delta if axis==0 else kappa;p=(np.eye(4)+gamma[axis])/2;pm=(np.eye(4)-gamma[axis])/2
        a=slice(4*idx[x],4*idx[x]+4);bb=slice(4*idx[y],4*idx[y]+4)
        f=-rate*np.exp(1j*angles[e])*p;r=-rate*np.exp(-1j*angles[e])*pm
        D[a,bb]=f;D[bb,a]=r;D1[e,a,bb]=1j*f;D1[e,bb,a]=-1j*r;D2[e,a,bb]=-f;D2[e,bb,a]=-r
        forward.append((a,bb,f));reverse.append((bb,a,r));G[e,idx[y]]=1;G[e,idx[x]]=-1
    rows=[];types=[]
    for x in coords:
        for a,b in itertools.combinations(range(4),2):
            xa=list(x);xa[a]+=1;xa=tuple(xa);xb=list(x);xb[b]+=1;xb=tuple(xb)
            keys=[(a,x),(b,xa),(a,xb),(b,x)]
            if all(key in edgeidx for key in keys):
                row=np.zeros(ne)
                for key,sign in zip(keys,[1,1,1,-1]):row[edgeidx[key]]+=sign
                rows.append(row);types.append((a,b))
    C=np.array(rows);assert np.linalg.norm(C@G)==0
    physical=C.copy()
    for j,(a,b) in enumerate(types):
        if a==0:physical[j]/=delta
    metric=delta*physical.T@physical
    inverse=np.linalg.inv(D);B=np.einsum('ij,ejk->eik',inverse,D1)
    second=np.einsum('ij,eji->e',inverse,D2)
    H=2*np.real(np.diag(second)-np.einsum('eij,fji->ef',B,B))
    assert np.linalg.norm(H-H.T)<2e-12
    gauge_residual=float(np.linalg.norm(H@G));assert gauge_residual<2e-10
    ev,u=eigh(metric);keep=ev>1e-9*max(ev)
    whiten=u[:,keep]/np.sqrt(ev[keep]);quotient=whiten.T@H@whiten
    spectrum=eigh(quotient,eigvals_only=True);actual=float(max(abs(spectrum)))
    loose,sharp=epsilon2(mu,kappa);assert actual<sharp
    # A separate determinant-ratio difference, formed near I to avoid the
    # large gauge-independent temporal normalization in a finite difference.
    direction=rng.normal(size=ne);direction/=np.linalg.norm(physical@direction)*math.sqrt(delta)
    expected=float(direction@H@direction)
    def ratio(step):
        diff=np.zeros_like(D)
        for e in range(ne):
            a,bb,f=forward[e];diff[a,bb]=f*np.expm1(1j*step*direction[e])
            a,bb,r=reverse[e];diff[a,bb]=r*np.expm1(-1j*step*direction[e])
        return 2*np.linalg.slogdet(np.eye(nd)+inverse@diff)[1]
    h=.02;fd=(ratio(h)+ratio(-h))/h**2;half=(ratio(h/2)+ratio(-h/2))/(h/2)**2
    extrap=(4*half-fd)/3;assert abs(extrap-expected)<3e-8
    return {'shape':shape,'delta':delta,'mu':mu,'kappa':kappa,'matrix_dimension':nd,'edges':ne,'plaquettes':len(rows),'curl_rank':int(keep.sum()),'gauge_hessian_residual':gauge_residual,'physical_hessian_spectral_radius':actual,'proved_loose_bound':loose,'proved_refined_bound':sharp,'hessian_direction_value':expected,'determinant_difference_extrapolate':float(extrap),'difference_error':abs(extrap-expected)}


def run():
    start=time.time();rows=[make((3,2,2,2),d,6.,.5,927) for d in [.1,.05,.01]]
    heavy=[]
    for mu in [12.,24.,48.,96.,192.]:
        loose,sharp=epsilon2(mu,.5);heavy.append({'mu':mu,'loose_bound':loose,'refined_bound':sharp,'mu_cubed_times_refined':mu**3*sharp})
    assert heavy[-1]['refined_bound']<heavy[0]['refined_bound']/1000
    print(json.dumps({'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'physical_curl_hessians':rows,'heavy_mass_bounds':heavy,'seconds':time.time()-start},indent=2))


if __name__=='__main__':run()
