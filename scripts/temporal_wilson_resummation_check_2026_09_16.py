#!/usr/bin/env python3
"""Exact finite Wilson matrices versus temporal runs and rectangle currents.
All numerical comparisons are floating checks of supplied finite systems.
"""
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=['docs/TEMPORAL_WILSON_RESUMMATION_PHYSICAL_CURL_BOUNDED_THEOREM_NOTE_2026-09-16.md']
AUDIT_MEMORY_MB=768
EXPECTED_INPUT_SHA256={'docs/TEMPORAL_WILSON_RESUMMATION_PHYSICAL_CURL_BOUNDED_THEOREM_NOTE_2026-09-16.md': '49892f9e45362c1a5dc2fb627d0d2976cccff0f82a1f11415bbe6ff73b589a07'}
import hashlib,itertools,json,math,time
from pathlib import Path
import numpy as np
from scipy.linalg import block_diag


def clifford():
    sx=np.array([[0,1],[1,0]],complex);sy=np.array([[0,-1j],[1j,0]]);sz=np.diag([1.,-1.]);I=np.eye(2)
    g=[np.kron(sz,I),np.kron(sx,sx),np.kron(sx,sy),np.kron(sx,sz)]
    for i,j in itertools.product(range(4),repeat=2):
        assert np.linalg.norm(g[i]@g[j]+g[j]@g[i]-2*(i==j)*np.eye(4))<1e-14
    return g,[[(np.eye(4)+s*a)/2 for s in [1,-1]] for a in g]


def spin_checks():
    g,p=clifford();rows=[]
    for i,s,e,t in itertools.product(range(1,4),range(2),range(2),range(2)):
        op=p[0][s]@p[i][e]@p[0][t];norm=np.linalg.norm(op,2)
        assert abs(norm-.5)<1e-14
    for i,s,e in itertools.product(range(1,4),range(2),range(2)):
        tr=np.trace(p[0][s]@p[i][e]@p[0][1-s]@p[i][1-e]);assert abs(tr+.5)<1e-14
        rows.append({'axis':i,'temporal_sign':s,'spatial_sign':e,'rectangle_spin_trace':float(tr.real)})
    return rows


def lattice(shape,delta,mu,kappa,seed):
    coords=list(itertools.product(*(range(n) for n in shape)));idx={x:i for i,x in enumerate(coords)};ns=len(coords);rng=np.random.default_rng(seed)
    shifts=[];angles={}
    for axis in range(4):
        U=np.zeros((ns,ns),complex)
        for x in coords:
            y=list(x);y[axis]+=1;y=tuple(y)
            if y in idx:
                theta=float(rng.normal(scale=.4));angles[axis,x]=theta;U[idx[x],idx[y]]=np.exp(1j*theta)
        shifts.append(U)
    _,p=clifford();I=np.eye(4*ns);M=mu+1/delta;x=1/(1+mu*delta)
    temp=np.kron(shifts[0],p[0][0])+np.kron(shifts[0].conj().T,p[0][1]);D0=M*I-temp/delta
    K=sum((kappa*(np.kron(shifts[i],p[i][0])+np.kron(shifts[i].conj().T,p[i][1])) for i in range(1,4)),np.zeros_like(I,dtype=complex))
    R=np.linalg.inv(D0);direct=np.zeros_like(R);U0pow=np.eye(ns,dtype=complex)
    for r in range(shape[0]):
        direct+=delta*x**(r+1)*(np.kron(U0pow,p[0][0])+np.kron(U0pow.conj().T,p[0][1]));U0pow=U0pow@shifts[0]
    err=float(np.linalg.norm(R-direct));assert err<3e-13
    assert np.linalg.norm(R,2)<=1/mu*(1+1e-13)
    log0=np.linalg.slogdet(D0)[1];assert abs(log0-4*ns*math.log(M))<3e-11
    A=R@K;D=D0-K;exact=2*(np.linalg.slogdet(D)[1]-log0)
    terms=[];power=np.eye(4*ns);partial=0.;b=(mu-6*kappa)/4;mu_b=mu-b*math.exp(b/mu);q=6*kappa/mu_b
    assert mu>6*kappa and delta<=1/mu and q<1
    for ell in range(1,15):
        power=power@A;blocks=np.array([np.trace(power[4*j:4*j+4,4*j:4*j+4]) for j in range(ns)])
        term=-2*float(blocks.sum().real)/ell;partial+=term
        if ell>=2:
            upper=4*delta*mu_b*q**ell/ell
            assert np.max(abs(2*blocks/ell))<=upper*(1+1e-12)
        terms.append({'spatial_hops':ell,'trace_log_term':term,'partial_log_determinant':partial})
    qop=3*kappa/mu;tail=2*4*ns*qop**15/(15*(1-qop))
    assert abs(partial-exact)<tail+3e-11
    rectangle=0.;count=0
    for site in coords:
        t=site[0]
        for axis in range(1,4):
            y=list(site);y[axis]+=1;y=tuple(y)
            if y not in idx:continue
            for r in range(1,shape[0]-t):
                later=(t+r,*site[1:]);phase=angles[axis,later]-angles[axis,site]
                for s in range(t,t+r):
                    a=(s,*site[1:]);bb=(s,*y[1:]);phase+=angles[0,a]-angles[0,bb]
                w=delta*x**(r+1);rectangle+=2*kappa*kappa*w*w*math.cos(phase);count+=1
    second=terms[1]['trace_log_term'];assert abs(second-rectangle)<3e-13
    # A continuous gauge shift must preserve the paired determinant exactly.
    chi=rng.normal(size=ns);S=np.diag(np.repeat(np.exp(1j*chi),4));shifted=S.conj().T@D@S
    assert abs(np.linalg.slogdet(shifted)[1]-np.linalg.slogdet(D)[1])<3e-11
    return {'shape':shape,'delta':delta,'mu':mu,'kappa':kappa,'dimension':4*ns,'inverse_run_error':err,'exact_paired_log_ratio':float(exact),'series_error':abs(partial-exact),'operator_tail_bound':tail,'second_order_trace':second,'rectangle_sum':rectangle,'rectangle_count':count,'trace_terms':terms}


def closure_checks():
    mu=3.;out=[]
    for delta in [.2,.05,.01]:
        x=1/(1+mu*delta);b=.2;mu_b=mu-b*math.exp(b/mu)
        for ell in [2,3,4]:
            signs=[1]*(ell-1)+[-1];R=math.ceil(24/(-math.log(x)))
            # For this sign word the final length is exactly the sum of the rest.
            # The closed sum is geometric in each of the ell-1 free lengths.
            closed=(delta*x)**ell/(1-x*x*math.exp(2*b*delta))**(ell-1)
            bound=delta*mu_b**(-(ell-1));assert closed<=bound
            independent=(1/mu)**ell
            out.append({'delta':delta,'spatial_hops':ell,'weighted_closed_sum':closed,'closed_bound':bound,'unconstrained_time_sum':independent,'ratio_unconstrained_to_unweighted_closed':independent/((delta*x)**ell/(1-x*x)**(ell-1))})
    return out


def continuum_rectangle():
    mu=6.;kappa=.5;F=.4;limit=-kappa*kappa*F*F/(mu*(4*mu*mu+F*F));hess=-kappa*kappa/(2*mu**3);rows=[]
    for j in range(9):
        delta=1/(mu*2**j);x=1/(1+mu*delta);z=x*x;a=2*math.sin(F*delta/2)**2
        total=-z*(1+z)*a/((1-z)*((1-z)**2+2*z*a))
        value=2*kappa*kappa*delta*x*x*total
        curvature=-2*kappa*kappa*delta**3*x*x*z*(1+z)/(1-z)**3
        rows.append({'delta':delta,'finite_time_density':value,'continuum_density':limit,'relative_error':abs(value/limit-1),'finite_curvature':curvature,'continuum_curvature':hess})
    assert rows[-1]['relative_error']<.01
    assert abs(rows[-1]['finite_curvature']/hess-1)<.01
    assert rows[-1]['relative_error']<rows[0]['relative_error']/50
    return rows


def run():
    start=time.time();spin=spin_checks();matrices=[lattice((3,2,2,2),.1,6.,.5,271),lattice((5,2,1,1),.05,6.,.5,314)]
    _emit({'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'spin_checks':spin,'finite_matrices':matrices,'time_closure':closure_checks(),'continuum_rectangle':continuum_rectangle(),'seconds':time.time()-start})




def _check_inputs():
    root = Path(__file__).resolve().parents[1]
    for name in AUDIT_INPUT_PATHS:
        actual = hashlib.sha256((root / name).read_bytes()).hexdigest()
        if actual != EXPECTED_INPUT_SHA256[name]:
            raise RuntimeError("input identity mismatch: " + name)

def _emit(report):
    report["input_sha256"] = dict(EXPECTED_INPUT_SHA256)
    report["completed_diagnostic_families"] = 1
    output = Path(__file__).resolve().parents[1] / "logs" / "runner-cache" / (Path(__file__).stem + ".json")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    print("TOTAL: PASS=1 FAIL=0")
    print('per_element: finite Wilson matrices, temporal-run inverses and rectangle traces.')
    print('per_site: two fixed free spatial shapes and open temporal boundaries.')
    print('per_mode: Clifford sandwich and gauge conjugation controls; no physical spectrum.')
    print('per_block: closed-time sums and leading rectangle continuum diagnostic.')
    print('lattice_wide: finite diagnostics only; general uniform bounds use the supplied-model proof.')

if __name__=='__main__':
    _check_inputs()
    run()
