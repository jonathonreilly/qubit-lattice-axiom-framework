"""Finite algebra challenges for the proposed clock covariance route."""
import itertools
import json
from pathlib import Path
import numpy as np
from scipy.linalg import eigh


def close(a,b,tol=2e-10):
    e=float(np.max(np.abs(np.asarray(a)-np.asarray(b))))
    assert e<tol,(e,tol)
    return e


def residue_moments(beta,N):
    k=np.arange(-70,71)
    w=np.exp(-k*k/(2*beta))
    z=np.array([w[k%N==r].sum() for r in range(N)])
    first=np.array([(k*w)[k%N==r].sum() for r in range(N)])
    second=np.array([(k*k*w)[k%N==r].sum() for r in range(N)])
    return z,first,second


def cube_duality():
    rows=[]
    d=6
    for N,beta in [(2,.7),(3,1.1),(4,.8),(5,1.7),(8,2.6)]:
        bd=N*N/(4*np.pi*np.pi*beta)
        z,f,s=residue_moments(beta,N)
        Z=(z**d).sum()
        diag=(s*z**(d-1)).sum()/Z
        off=(f*f*z**(d-2)).sum()/Z
        C=np.full((d,d),off);np.fill_diagonal(C,diag)
        # Dual lattice consists of vectors whose coordinate sum is 0 mod N.
        # Character filtering is independent of the primal residue-sector sum.
        k=np.arange(-70,71);w=np.exp(-k*k/(2*bd))
        phase=np.exp(2j*np.pi*np.arange(N)[:,None]*k[None,:]/N)
        a=phase@w;b=phase@(k*w);c=phase@(k*k*w)
        Zd=np.mean(a**d)
        dd=np.mean(c*a**(d-1))/Zd
        od=np.mean(b*b*a**(d-2))/Zd
        close([Zd.imag,dd.imag,od.imag],[0,0,0])
        D=np.full((d,d),od.real);np.fill_diagonal(D,dd.real)
        err=close(C/beta+D/bd,np.eye(d))
        covolume=N**(d-1)
        partition_rhs=(2*np.pi*beta)**(d/2)*Zd.real/covolume
        close(Z,partition_rhs)
        assert np.linalg.eigvalsh(C).min()>0
        assert np.linalg.eigvalsh(D).min()>0
        assert np.max(np.abs(C/beta-D/bd-np.eye(d)))>.1
        rows.append(dict(N=N,beta=beta,beta_dual=bd,primal_partition=float(Z),
                         dual_partition=float(Zd.real),covariance_identity_error=err,
                         primal_covariance_eigenvalues=np.linalg.eigvalsh(C).tolist()))
    return rows


def cochain_box(shape):
    vertices=list(itertools.product(*(range(s) for s in shape)))
    vid={v:i for i,v in enumerate(vertices)}
    edges=[]
    for x in vertices:
        for a in range(len(shape)):
            if x[a]+1<shape[a]:edges.append((x,a))
    eid={e:i for i,e in enumerate(edges)}
    grad=np.zeros((len(edges),len(vertices)))
    for i,(x,a) in enumerate(edges):
        y=list(x);y[a]+=1;y=tuple(y)
        grad[i,vid[y]]=1;grad[i,vid[x]]=-1
    faces=[]
    for x in vertices:
        for a,b in itertools.combinations(range(len(shape)),2):
            if x[a]+1<shape[a] and x[b]+1<shape[b]:faces.append((x,a,b))
    curl=np.zeros((len(faces),len(edges)))
    for i,(x,a,b) in enumerate(faces):
        xa=list(x);xa[a]+=1;xa=tuple(xa)
        xb=list(x);xb[b]+=1;xb=tuple(xb)
        for e,sgn in [((x,a),1),((xa,b),1),((xb,a),-1),((x,b),-1)]:curl[i,eid[e]]=sgn
    close(curl@grad,0)
    return edges,faces,grad,curl


def selected_link_integration():
    edges,faces,g,d=cochain_box((5,2,2,2))
    Q=d.T@d
    val,vec=eigh(Q);mask=val>1e-9
    V=(vec[:,mask]/val[mask])@vec[:,mask].T
    targets=[((0,0,0,0),1,2),((3,0,0,0),1,2)]
    rho=np.array([2*np.pi*d[faces.index(f)] for f in targets])
    close(rho@g,0)
    colors=np.array([a*8+sum((x[b]%2)*2**j for j,b in enumerate(c for c in range(4) if c!=a)) for x,a in edges])
    selected=[];tilde=[];cost=[]
    for r in rho:
        scores=np.array([np.sum(r[colors==c]**2) for c in range(32)])
        c=int(np.argmax(scores));inds=np.where((colors==c)&(r!=0))[0]
        assert np.sum(r[inds]**2)>=np.sum(r*r)/32
        close(Q[np.ix_(inds,inds)],np.diag(np.diag(Q)[inds]))
        u=np.zeros(len(edges));u[inds]=r[inds]/np.diag(Q)[inds]
        rt=r-Q@u
        close(rt[inds],0);close(rt@g,0)
        selected.extend(inds.tolist());tilde.append(rt);cost.append(float(r@u))
    close(Q[np.ix_(selected,selected)],np.diag(np.diag(Q)[selected]))
    tilde=np.array(tilde);cost=np.array(cost)
    beta=.17
    K=np.array([.2,.35]);z=K*np.exp(-beta*cost/2)
    rng=np.random.default_rng(210914)
    a=rng.normal(size=len(edges));phase=rho@a
    def integral(freq,amp,ph):
        total=0j
        for signs in itertools.product((-1,0,1),repeat=len(freq)):
            signs=np.array(signs);r=signs@freq
            coefficient=np.prod(np.where(signs==0,1.,amp/2))
            total+=coefficient*np.exp(-beta*(r@V@r)/2+1j*(signs@ph))
        assert abs(total.imag)<1e-12
        return float(total.real)
    original=integral(rho,K,phase)
    transformed=integral(tilde,z,phase)
    err=close(original,transformed)
    wrong_factor=integral(tilde,K*np.exp(-beta*cost),phase)
    wrong_phase=integral(tilde,z,tilde@a)
    assert abs(original-wrong_factor)>1e-4
    assert abs(original-wrong_phase)>1e-4
    return dict(edges=len(edges),plaquettes=len(faces),rank=int(mask.sum()),
                selected_links=selected,source_integral=original,
                transformed_integral=transformed,error=err,
                wrong_double_damping_error=abs(original-wrong_factor),
                wrong_phase_current_error=abs(original-wrong_phase))


def phase_curvature():
    rng=np.random.default_rng(7)
    worst=0.;rows=[]
    for count in (1,3,5):
        z=rng.uniform(.03,.35,count)
        freq=rng.normal(size=(count,2))
        slope=rng.normal(size=count)
        phase0=rng.uniform(-np.pi,np.pi,count)
        C=float(np.sum(z/(1-z)*slope**2))
        terms=[]
        for sig in itertools.product((-1,0,1),repeat=count):
            sig=np.array(sig);f=sig@freq
            weight=np.prod(np.where(sig==0,1.,z/2))*np.exp(-f@f/2)
            terms.append((weight,float(sig@phase0),float(sig@slope)))
        minimum=float('inf')
        for t in np.linspace(-10,10,201):
            I=sum(w*np.cos(p+t*s) for w,p,s in terms)
            first=sum(-w*s*np.sin(p+t*s) for w,p,s in terms)
            second=sum(-w*s*s*np.cos(p+t*s) for w,p,s in terms)
            assert I>0
            curvature=second/I-(first/I)**2
            assert curvature>=-C-1e-11
            minimum=min(minimum,curvature)
        rows.append(dict(currents=count,lower_curvature_bound=-C,smallest_sampled=minimum))
    # A negative mixture coefficient invalidates the log-sum step even when
    # the resulting function is positive everywhere.
    z=.005;c=.99;t=np.pi
    I=1-c*(1+z*np.cos(t));first=c*z*np.sin(t);second=c*z*np.cos(t)
    curvature=second/I-(first/I)**2
    assert I>0 and curvature < -z/(1-z)
    # Pointwise derivative bound remains valid close to z=1.
    for z in (.05,.5,.8,.99):
        x=np.linspace(-np.pi,np.pi,1001)
        second=-(z*np.cos(x)+z*z)/(1+z*np.cos(x))**2
        assert np.max(np.abs(second))<=z/(1-z)+1e-8
    return dict(positive_phase_integrals=rows,negative_mixture_counterexample_curvature=float(curvature))


def affine_closed_cosets():
    rows=[]
    for beta in (1.7,2.6,5.):
        vals=[]
        for shift in np.linspace(0,1,101):
            x=np.arange(-40,41)+shift
            w=np.exp(-6*x*x/(2*beta));w/=w.sum()
            mean=x@w;var=(x*x)@w-mean*mean
            vals.append(6*var/beta)
        rows.append(dict(beta=beta,smallest_closed_covariance_ratio=min(vals),
                         largest_closed_covariance_ratio=max(vals)))
    return rows


if __name__=='__main__':
    result=dict(status='personal_finite_identity_checks_pass',
                lattice_duality=cube_duality(),
                local_gaussian_integration=selected_link_integration(),
                phase_curvature=phase_curvature(),affine_cosets=affine_closed_cosets(),
                limits='The finite identities do not prove uniform phase representation, boundary control, thermodynamic covariance bounds or a fixed-clock phase.')
    Path(__file__).with_name('BLOCK7_DUAL_COVARIANCE_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
