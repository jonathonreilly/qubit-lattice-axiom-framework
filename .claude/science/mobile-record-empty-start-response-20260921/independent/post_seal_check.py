#!/usr/bin/env python3
"""Narrow post-seal geometry/remainder checks; writes only this directory."""
from fractions import Fraction as F
from itertools import product, combinations
from collections import Counter
from pathlib import Path
from math import prod
from contextlib import redirect_stdout
import hashlib
import io
import json
import runpy

HERE=Path(__file__).resolve().parent
AUTHOR=HERE.parent
EXPECTED={
    'EMPTY_START_DERIVATION.md':'4e34cda1cb85a8b7471c80f22bad5a56d64319b8bb3090fdcdcea0174091ec74',
    'empty_start_geometry.py':'182ce88938e4f7471b6801972bfbc8630b9dc79fd29918d36af3c33399727aec',
    'EMPTY_START_GEOMETRY_RESULTS.json':'52d18fa0fac5f62686421df89e021b17ac2114833e6b6a939a0166289bdf601c',
}


def source_guard():
    for name,digest in EXPECTED.items():
        assert hashlib.sha256((AUTHOR/name).read_bytes()).hexdigest()==digest,name


def primary_reproduction():
    source_guard()
    destination=HERE/'POST_SEAL_PRIMARY_REPRODUCTION.json'
    original=Path.write_text
    def redirect_write(path,data,*args,**kwargs):
        assert path.resolve()==(AUTHOR/'EMPTY_START_GEOMETRY_RESULTS.json').resolve(),str(path)
        return original(destination,data,*args,**kwargs)
    capture=io.StringIO()
    Path.write_text=redirect_write
    try:
        with redirect_stdout(capture):
            runpy.run_path(str(AUTHOR/'empty_start_geometry.py'),run_name='__main__')
    finally:
        Path.write_text=original
    (HERE/'POST_SEAL_PRIMARY_RUN.log').write_text(capture.getvalue())
    assert destination.read_bytes()==(AUTHOR/'EMPTY_START_GEOMETRY_RESULTS.json').read_bytes()
    source_guard()
    return 'Exact runner reproduced; only its result write was redirected; bytes match.'


def torus(side,d):
    vertices=list(product(range(side),repeat=d))
    index={v:i for i,v in enumerate(vertices)}
    adj=[set() for _ in vertices]
    for i,v in enumerate(vertices):
        for a in range(d):
            for step in [-1,1]:
                q=list(v);q[a]=(q[a]+step)%side
                adj[i].add(index[tuple(q)])
    return vertices,adj


def independent_counts(side,d):
    vertices,adj=torus(side,d)
    x=0
    target=(1,)+(0,)*(d-1)
    q=vertices.index(target)
    # Count length-two walks from each hop endpoint, rather than intersecting
    # neighbor sets of every spectator with the endpoint neighbor sets.
    walks=[]
    for endpoint in [x,q]:
        count=Counter()
        for mid in adj[endpoint]:
            for end in adj[mid]:
                count[end]+=1
        walks.append(count)
    by_type=Counter()
    for y in range(len(vertices)):
        if y in [x,q]:
            continue
        typ=int(y in adj[x])+int(y in adj[q])
        by_type[typ]+=(walks[0][y]-walks[1][y])**2
    if side>=6:
        assert by_type[1]==2*(8*d-7)
        assert by_type[0]==2*(8*d*d-14*d+7)
        assert by_type[2]==0
    return {str(k):v for k,v in sorted(by_type.items())}


def axes_W():
    return [[F(3,2) if a==b else F(1,2) if (a^1)==b else F(1)
             for b in range(6)] for a in range(6)]


def formula(W,d):
    h=[[sum(W[a][c]*W[c][b] for c in range(6))-6 for b in range(6)] for a in range(6)]
    return d*sum(h[a][b]**2*(2*(8*d-7)*W[a][b]/(1+W[a][b])+8*d*d-14*d+7)
                 for a,b in product(range(6),repeat=2))


def direct_pair_edge(side,d,W):
    vertices,adj=torus(side,d)
    x=0;q=vertices.index((1,)+(0,)*(d-1))
    def hazard(occupied):
        value=F(0)
        for z in range(len(vertices)):
            if z in occupied:
                continue
            for a in range(6):
                local=F(1)
                for y,b in occupied.items():
                    if y in adj[z]:
                        local*=W[a][b]
                value+=local
        return value
    energy=F(0)
    for y in range(len(vertices)):
        if y in [x,q]:
            continue
        for a,b in product(range(6),repeat=2):
            old={x:a,y:b};new={q:a,y:b}
            u=W[a][b] if y in adj[x] else F(1)
            v=W[a][b] if y in adj[q] else F(1)
            rate=v/(u+v)
            energy+=u*rate*(hazard(new)-hazard(old))**2
    # Translation/axis symmetry gives d edges per site.
    assert d*energy==formula(W,d)
    return str(d*energy)


def norm_checks(name,n,edges,W):
    adj=[[] for _ in range(n)]
    for x,y in edges:
        adj[x].append(y);adj[y].append(x)
    z=max(map(len,adj))
    umax=max(F(1),max(map(max,W)))
    states=list(product(range(-1,6),repeat=n))
    ids={s:i for i,s in enumerate(states)}
    weights=[prod(W[s[x]][s[y]] for x,y in edges if s[x]>=0 and s[y]>=0)
             for s in states]
    epsilon=F(1,7)
    runs=[]
    for kappa in [F(0),F(2,3)]:
        transitions=[]
        for i,s in enumerate(states):
            row=[]
            for x,y in edges:
                if (s[x]<0)!=(s[y]<0):
                    t=list(s);t[x],t[y]=t[y],t[x];j=ids[tuple(t)]
                    row.append((j,kappa*weights[j]/(weights[i]+weights[j])))
            for x in range(n):
                if s[x]<0:
                    for a in range(6):
                        t=list(s);t[x]=a
                        rate=epsilon*prod(W[a][s[y]] for y in adj[x] if s[y]>=0)
                        row.append((ids[tuple(t)],rate))
            transitions.append(row)
        R=6*epsilon*umax**z+z*kappa
        K=2*(z+1)
        for site in range(n):
            values=[F(s[site]>=0) for s in states]
            bound=F(1)
            data=[]
            for k in range(1,7):
                values=[sum(rate*(values[j]-values[i]) for j,rate in row)
                        for i,row in enumerate(transitions)]
                norm=max(map(abs,values))
                bound*=2*R*(1+(k-1)*K)
                assert norm<=bound,(name,kappa,site,k,norm,bound)
                data.append({'k':k,'actual_norm':str(norm),'claimed_bound':str(bound)})
            runs.append({'kappa':str(kappa),'site':site,'powers':data})
    return {'name':name,'states':len(states),'max_degree':z,'runs':runs}


def main():
    reproduction=primary_reproduction()
    count_cases=[{'side':L,'dimension':d,'counts':independent_counts(L,d)}
                 for L,d in [(6,1),(7,1),(6,2),(7,2),(6,3),(7,3),(6,4),(7,4)]]
    excluded=independent_counts(5,1)
    assert excluded['0']==0 and excluded['1']==2
    v=[2,-1,-1,0,0,0]
    general=[[1+F(v[a]*v[b],10) for b in range(6)] for a in range(6)]
    W=axes_W()
    direct={'cycle6_axes':direct_pair_edge(6,1,W),
            'torus6x6_general':direct_pair_edge(6,2,general)}
    assert formula(W,3)==F(2379,5) and formula(W,3)/60==F(793,100)
    positivity=[]
    for gamma in [F(-1,10),F(0),F(1,10)]:
        matrix=[[1+gamma*v[a]*v[b] for b in range(6)] for a in range(6)]
        assert all(sum(row)==6 for row in matrix)
        assert all(x>0 for row in matrix for x in row)
        value=formula(matrix,3)
        assert (value>0)==(gamma!=0)
        positivity.append({'rank_one_coefficient':str(gamma),'D2_per_site':str(value)})
    norms=[norm_checks('singleton',1,[],W),
           norm_checks('path3',3,[(0,1),(1,2)],W),
           norm_checks('star4',4,[(0,1),(0,2),(0,3)],general)]
    epsilon,kappa,z,u=F(1,7),F(2,3),6,F(3,2)
    R=6*epsilon*u**z+z*kappa;R0=6*epsilon*u**z;K=2*(z+1)
    C=((2*R)**6+(2*R0)**6)*prod(1+j*K for j in range(6))/720
    a=F(793,100)*kappa*epsilon**4
    tmax=a/(2*C)
    assert C*tmax**6==a*tmax**5/2
    out={'status':'all narrow checks passed','primary_reproduction':reproduction,
         'sources_sha256':EXPECTED,'independent_geometry':count_cases,
         'excluded_cycle5_counts':excluded,'direct_birth_hazard_edge_sums':direct,
         'positive_negative_centered_modes':positivity,'generator_norm_checks':norms,
         'norm_inequalities_checked':sum(len(r['powers']) for g in norms for r in g['runs']),
         'one_uniform_window_example':{'epsilon':str(epsilon),'kappa':str(kappa),
             'R_kappa':str(R),'R_0':str(R0),'K':K,'a':str(a),'C':str(C),
             't_max':str(tmax),'t_max_approx':float(tmax)}}
    source_guard()
    (HERE/'POST_SEAL_CHECK_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='generator_norm_checks'},indent=2))


if __name__=='__main__':
    main()
