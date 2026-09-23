#!/usr/bin/env python3
"""Analytic third log-determinant variation versus separate finite differences.

Physical duration is held fixed as time resolution increases. These finite
directions test the C3 formula, not the general all-direction estimate.
"""
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_FILES=['docs/TEMPORAL_WILSON_RESUMMATION_PHYSICAL_CURL_BOUNDED_THEOREM_NOTE_2026-09-16.md']
AUDIT_MEMORY_MB=768
EXPECTED_INPUT_SHA256={'docs/TEMPORAL_WILSON_RESUMMATION_PHYSICAL_CURL_BOUNDED_THEOREM_NOTE_2026-09-16.md': '49892f9e45362c1a5dc2fb627d0d2976cccff0f82a1f11415bbe6ff73b589a07'}
import hashlib,itertools,json,math,time
from pathlib import Path
import numpy as np

def check(Nt):
    delta=.3/Nt;mu=6.;kappa=.5;shape=(Nt,2,2,1)
    coords=list(itertools.product(*(range(s) for s in shape)));index={x:i for i,x in enumerate(coords)}
    sx=np.array([[0,1],[1,0]],complex);sy=np.array([[0,-1j],[1j,0]]);sz=np.diag([1.,-1.]);I=np.eye(2)
    gamma=[np.kron(sz,I),np.kron(sx,sx),np.kron(sx,sy),np.kron(sx,sz)]
    edges=[];ei={}
    for x in coords:
        for a in range(4):
            y=list(x);y[a]+=1;y=tuple(y)
            if y in index:ei[a,x]=len(edges);edges.append((a,x,y))
    rows=[];types=[]
    for x in coords:
        for a,b in itertools.combinations(range(4),2):
            xa=list(x);xa[a]+=1;xa=tuple(xa);xb=list(x);xb[b]+=1;xb=tuple(xb)
            keys=[(a,x),(b,xa),(a,xb),(b,x)]
            if all(k in ei for k in keys):
                row=np.zeros(len(edges))
                for k,s in zip(keys,[1,1,-1,-1]):row[ei[k]]+=s
                rows.append(row/(delta if a==0 else 1));types.append((a,b))
    C=np.array(rows);rng=np.random.default_rng(81073)
    spatial_keys=sorted({(a,x[1:]) for a,x,y in edges if a!=0})
    history={key:rng.normal(size=4) for key in spatial_keys}
    theta=[];direction=[]
    for a,x,y in edges:
        if a==0:theta.append(0.);direction.append(0.)
        else:
            A,B,c,d=history[a,x[1:]];theta.append(A+delta*x[0]*B);direction.append(c+delta*x[0]*d)
    theta=np.array(theta);direction=np.array(direction)
    direction/=(delta*np.sum(abs(C@direction)**3))**(1/3)
    assert abs(delta*np.sum(abs(C@direction)**3)-1)<1e-12
    nd=4*len(coords);D=np.eye(nd,dtype=complex)*(mu+1/delta);forward=[];reverse=[]
    for e,(a,x,y) in enumerate(edges):
        u=slice(4*index[x],4*index[x]+4);v=slice(4*index[y],4*index[y]+4);rate=1/delta if a==0 else kappa
        f=-rate*np.exp(1j*theta[e])*(np.eye(4)+gamma[a])/2
        r=-rate*np.exp(-1j*theta[e])*(np.eye(4)-gamma[a])/2
        D[u,v]=f;D[v,u]=r;forward.append((u,v,f));reverse.append((v,u,r))
    R=np.linalg.inv(D)
    def derivatives(vector):
        a1=np.zeros_like(D);a2=np.zeros_like(D);a3=np.zeros_like(D)
        for e,w in enumerate(vector):
            u,v,f=forward[e];a1[u,v]=1j*w*f;a2[u,v]=-w*w*f;a3[u,v]=-1j*w**3*f
            u,v,r=reverse[e];a1[u,v]=-1j*w*r;a2[u,v]=-w*w*r;a3[u,v]=1j*w**3*r
        A=R@a1;B=R@a2;C3=R@a3
        return 2*np.real(np.trace(A)),2*np.real(np.trace(B-A@A)),2*np.real(np.trace(C3-3*B@A+2*A@A@A))
    first,second,third=derivatives(direction)
    def ratio(h):
        diff=np.zeros_like(D)
        for e,w in enumerate(direction):
            u,v,f=forward[e];diff[u,v]=f*np.expm1(1j*h*w)
            u,v,r=reverse[e];diff[u,v]=r*np.expm1(-1j*h*w)
        return 2*np.linalg.slogdet(np.eye(nd)+R@diff)[1]
    def fd(h):return (ratio(2*h)-2*ratio(h)+2*ratio(-h)-ratio(-2*h))/(2*h**3)
    h=.1;coarse=fd(h);fine=fd(h/2);richardson=(4*fine-coarse)/3
    assert abs(richardson-third)<max(1e-10,.002*abs(third)),(Nt,third,richardson)
    chi=rng.normal(scale=.3,size=len(coords));gauge=np.array([chi[index[y]]-chi[index[x]] for a,x,y in edges])
    assert np.linalg.norm(C@gauge)<1e-12
    gauge_values=derivatives(gauge);assert max(abs(x) for x in gauge_values)<2e-10
    b=(mu-6*kappa)/4;mb=mu-b*math.exp(b/mu);q=6*kappa/mb
    S5=q*(1+26*q+66*q*q+26*q**3+q**4)/(1-q)**6
    S2=q*(1+q)/(1-q)**3;bound=16*mb*(27*(S5-q)+6/b**3*(S2-q))
    assert abs(third)<bound
    return {'time_slices':Nt,'delta':delta,'physical_duration':delta*Nt,'matrix_dimension':nd,'first_variation':float(first),'second_variation':float(second),'third_variation':float(third),'third_difference_coarse':float(coarse),'third_difference_fine':float(fine),'third_difference_richardson':float(richardson),'third_difference_error':float(abs(richardson-third)),'third_variation_bound':bound,'pure_gauge_variations':[float(x) for x in gauge_values]}

def run():
    start=time.time();rows=[check(n) for n in [3,6,12]]
    assert max(abs(r['third_variation']) for r in rows)>1e-7,'The selected directions did not resolve a third variation'
    _emit({'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'fixed_duration_checks':rows,'seconds':time.time()-start})



def _check_inputs():
    root = Path(__file__).resolve().parents[1]
    for name in AUDIT_INPUT_FILES:
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
    print('per_element: analytic third variations versus determinant finite differences.')
    print('per_site: fixed physical duration 0.3 and three time resolutions.')
    print('per_mode: sampled physical curl directions and pure-gauge controls.')
    print('per_block: original Richardson comparison and sufficient general bound.')
    print('lattice_wide: sampled directions only; no exhaustive all-direction numerical proof.')

if __name__=='__main__':
    _check_inputs()
    run()
