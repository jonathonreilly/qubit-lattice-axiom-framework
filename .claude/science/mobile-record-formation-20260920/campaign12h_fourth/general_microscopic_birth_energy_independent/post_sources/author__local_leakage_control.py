#!/usr/bin/env python3
"""Fresh primitive path control for actual rotated-jump coefficients.
Author calculation, not independent evidence. Every edge is oriented A to B.
"""
from pathlib import Path
from collections import defaultdict
import json,math
import sympy as sy
HERE=Path(__file__).resolve().parent

def graph(kind,degree=3):
    if kind=='cube':
        A=(0,3,5,6);nv=8
        edges=tuple((a,b) for a in A for b in range(nv) if (a^b).bit_count()==1)
    elif kind=='ring':
        A=(0,2,4);nv=6;edges=tuple((a,b) for a in A for b in ((a-1)%6,(a+1)%6))
    else:
        A=(0,);nv=degree+1;edges=tuple((0,b) for b in range(1,nv))
    return A,nv,edges

def initial(kind,n=0,degree=3):
    A,nv,edges=graph(kind,degree);q=tuple(int(x in A) for x in range(nv));f=[0]*len(edges)
    if kind=='cube':
        for edge,val in { (0,1):n,(3,1):-n,(3,2):n,(0,2):-n }.items():f[edges.index(edge)]=val
    elif kind=='ring':
        for k,(a,b) in enumerate(edges):f[k]=n if b==(a+1)%6 else -n
    state=(q,tuple(f));assert gauss(state,A,edges)
    return A,edges,state

def gauss(state,A,edges):
    q,f=state;div=[0]*len(q)
    for (a,b),e in zip(edges,f):div[a]+=e;div[b]-=e
    return all(div[x]==q[x]-int(x in A) for x in range(len(q)))

def weight(e,shift,S):
    if S is None:return 1.
    if abs(e+shift)>S:return 0.
    return math.sqrt(max(0.,1-e*(e+shift)/(S*(S+1))))

def F(v,A,edges,S,center=None):
    out=defaultdict(float)
    for (q,f),amp in v.items():
        for k,(a,b) in enumerate(edges):
            if center is not None and a!=center:continue
            if not q[a] or q[b]:continue
            shift=-q[a];w=weight(f[k],shift,S)
            if not w:continue
            qq,ff=list(q),list(f);qq[b]=qq[a];qq[a]=0;ff[k]+=shift
            state=(tuple(qq),tuple(ff));assert gauss(state,A,edges)
            out[state]+=amp*w
    return {q:x for q,x in out.items() if abs(x)>1e-14}

def j(v,A,edges,S,k,sign):
    out=defaultdict(float);a,b=edges[k]
    for (q,f),amp in v.items():
        if q[a] or q[b]:continue
        for r in ((1,-1) if sign==0 else (sign,)):
            w=weight(f[k],r,S)
            if not w:continue
            qq,ff=list(q),list(f);qq[a]=r;qq[b]=-r;ff[k]+=r
            state=(tuple(qq),tuple(ff));assert gauss(state,A,edges)
            out[state]+=amp*w
    return {q:x for q,x in out.items() if abs(x)>1e-14}

def norm(v):return sum(abs(x)**2 for x in v.values())
def subtract(a,b,scale=1.):return {q:a.get(q,0)-scale*b.get(q,0) for q in set(a)|set(b)}
def D(state,A,edges):
    q,f=state
    return sum(e*(e-q[a]) for (a,b),e in zip(edges,f) if q[a] and not q[b])
def E2(state):return sum(e*e for e in state[1])

def calculation(kind,n=0,S=None,degree=3):
    A,edges,state=initial(kind,n,degree);v={state:1.};fv=F(v,A,edges,S);z=F(fv,A,edges,S)
    allrows=[];totals={}
    for instrument in ('resolved','coherent'):
        rsum=rate=ddrift=e2drift=0.;selected=None;maxresidual=0.
        for k,(a,b) in enumerate(edges):
            for sign in ((1,-1) if instrument=='resolved' else (0,)):
                B=j(fv,A,edges,S,k,sign)
                # R = jZ/2 - F B; independently evaluate the local expression.
                jz={q:x/2 for q,x in j(z,A,edges,S,k,sign).items()}
                R=subtract(jz,F(B,A,edges,S));local={q:-x for q,x in F(B,A,edges,S,center=a).items()}
                residual=norm(subtract(R,local));maxresidual=max(maxresidual,residual)
                assert residual<2e-24
                bn,rn=norm(B),norm(R);rate+=bn;rsum+=rn
                ddrift+=sum(abs(x)**2*(D(q,A,edges)-D(state,A,edges)) for q,x in B.items())
                e2drift+=sum(abs(x)**2*(E2(q)-E2(state)) for q,x in B.items())
                if k==0 and sign in (1,0):
                    selected={'mark':[a,b,sign],'B_squared_norm':bn,'R_squared_norm':rn,'blocked':bn<1e-14,'high_band_moment_coefficient':rn/bn if bn>1e-14 else None,
                              'conditional_D':sum(abs(x)**2*D(q,A,edges) for q,x in B.items())/bn if bn>1e-14 else None,
                              'conditional_E2':sum(abs(x)**2*E2(q) for q,x in B.items())/bn if bn>1e-14 else None}
        totals[instrument]={'total_dimensionless_rate':rate,'total_R_squared_norm':rsum,'D_drift':ddrift,'E2_drift':e2drift,'max_local_identity_squared_residual':maxresidual,'selected_first_edge':selected}
    assert abs(totals['resolved']['total_R_squared_norm']-totals['coherent']['total_R_squared_norm'])<2e-11
    if kind=='ring':assert totals['resolved']['total_R_squared_norm']<2e-24
    if S is None:
        degree_by_a={a:sum(x==a for x,b in edges) for a in A}
        expected=sum(3*d*(d-1)*(d-2) for d in degree_by_a.values())
        assert totals['resolved']['total_R_squared_norm']==expected
    if kind=='cube' and S is not None:
        C=S*(S+1);u=n*n/C
        expectedR=72-72*u+36*u*u+12*u/C
        expectedD=-32*n*n*(3-3*u+u*u)-16*n*n/C
        expectedRate=48-32*u+8*u*u
        expectedE2=96-128*u+48*u*u
        for t in totals.values():
            assert abs(t['total_R_squared_norm']-expectedR)<3e-10
            assert abs(t['D_drift']-expectedD)<3e-10*max(1,abs(expectedD))
            assert abs(t['total_dimensionless_rate']-expectedRate)<3e-10
            assert abs(t['E2_drift']-expectedE2)<3e-10*max(1,abs(expectedE2))
        a=1-n*(n+1)/C;selected=totals['resolved']['selected_first_edge']
        assert abs(selected['B_squared_norm']-a*(1+a))<1e-12
        assert abs(selected['R_squared_norm']-4*a*a)<1e-12
        if not selected['blocked']:
            assert abs(selected['conditional_D']-2*n*n/(1+a))<2e-10*max(1,n*n)
            expectedE=4*n*n+2+2*n*(2*a+1)/(1+a)
            assert abs(selected['conditional_E2']-expectedE)<2e-10*max(1,n*n)
            totalmean=selected['conditional_D']/C+selected['high_band_moment_coefficient']
            assert abs(totalmean-(2-2*n/C/(1+a)))<2e-11
    return {'graph':kind,'degree_for_star':degree if kind=='star' else None,'n':n,'S':S,'initial_D':D(state,A,edges),'initial_E2':E2(state),'instruments':totals}

if __name__=='__main__':
    u,v=sy.symbols('u v',real=True);a=1-u-v;b=1-u+v
    per=sy.expand(6*(a*a+b*b+a*b));assert sy.expand(per-18*(1-u)**2-6*v*v)==0
    f=72-168*u+132*u*u-32*u**3
    assert sy.diff(f,u)==sy.expand(-24*(4*u-7)*(u-1)) and f.subs(u,1)==4
    n,C=sy.symbols('n C',real=True,nonzero=True)
    es=[n,-n,0];ms=[1-e*(e-1)/C for e in es];ps=[1-e*(e+1)/C for e in es]
    localE2=sum(ms[o]*(ps[j]*(2-2*es[o]+2*es[j])+ms[j]*(2-2*es[o]-2*es[j]))
                for j in range(3) for o in range(3) if j!=o)
    cubeE2=sy.expand(2*localE2+48)
    assert sy.expand(cubeE2-(96-128*n*n/C+48*n**4/C**2))==0
    rows=[calculation('star',degree=d) for d in (1,2,3,4,5)]
    rows+=[calculation(kind,n=n) for kind in ('cube','ring') for n in (0,1,7)]
    rows+=[calculation(kind,n=n,S=S) for kind in ('cube','ring') for S in (1,2,5,20,100) for n in sorted(set((-S,0,1,S//2,S)))]
    result={'fresh_primitives':'A-to-B oriented normalized spin shifts and hard-core matter; no imported campaign builder',
            'exact_symbolic_flux_identity':str(per),'lambda0_limiting_power_polynomial':str(f),
            'exact_symbolic_cube_E2_drift':str(cubeE2),
            'rows':rows,'all_assertions_passed':True,
            'limits':'Rotated-jump coefficient and slow-energy drift controls; actual full-H moment theorem requires the canonical low-band perturbation argument, not these paths alone.'}
    (HERE/'LOCAL_LEAKAGE_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'all_assertions_passed':True,'cases':len(rows),'cube_rotor_R_squared_sum':rows[5]['instruments']['resolved']['total_R_squared_norm'],'degree_two_rotor_coefficient':rows[8]['instruments']['resolved']['total_R_squared_norm'],'symbolic_per_affected_A':str(per)},indent=2))
