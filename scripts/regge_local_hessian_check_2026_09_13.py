"""Rational simplex geometry and a fixed all-phase Laurent identity.

No input files are read except this module's own bytes for an integrity hash.
"""
from __future__ import annotations
import itertools,json,time,hashlib
from pathlib import Path
from types import SimpleNamespace
import sympy as s
AUDIT_TIMEOUT_SEC = 180

def run():
    started=time.monotonic()
    R=s.Rational
    pairs=list(itertools.combinations(range(5),2))
    q=s.symbols('q:10'); qdict=dict(zip(pairs,q))
    def edge(a,b):
        return s.S.Zero if a==b else qdict[tuple(sorted((a,b)))]
    H=s.zeros(4)
    for a in range(1,5):
        H[a-1,a-1]=edge(a-1,a)
        for b in range(a+1,5):
            H[a-1,b-1]=H[b-1,a-1]=R(1,2)*(edge(a,b-1)+edge(a-1,b)-edge(a,b)-edge(a-1,b-1))
    normals=[s.Matrix([-1,0,0,0]),s.Matrix([1,-1,0,0]),s.Matrix([0,1,-1,0]),s.Matrix([0,0,1,-1]),s.Matrix([0,0,0,1])]
    assert sum(normals,s.zeros(4,1))==s.zeros(4,1)
    local=s.S.Zero; schlaefli=s.S.Zero
    for i,j in pairs:
        ni,nj=normals[i],normals[j]
        a,b,c=(ni.dot(ni),ni.dot(nj),nj.dot(nj))
        N=ni.row_join(nj); P=s.eye(4)-N*(N.T*N).inv()*N.T
        W=(ni.T*H*nj)[0]-b*R(1,2)*((ni.T*H*ni)[0]/a+(nj.T*H*nj)[0]/c)
        schlaefli-=W/2
        local+=s.trace(P*H)*W/4
    assert s.expand(schlaefli)==0
    local=s.expand(local)
    Q0=s.hessian(local,q)/2
    assert Q0==Q0.T
    assert all(x.is_Rational for x in Q0)


    w=s.symbols('w0:4',nonzero=True); z=[x*x for x in w]
    sets=[frozenset(a for a,b in enumerate(v) if b) for v in itertools.product((0,1),repeat=4) if any(v)]
    idx={A:i for i,A in enumerate(sets)}
    def mon(anchor):
        return s.prod(z[i] for i in anchor)
    Q=s.zeros(15)
    for perm in itertools.permutations(range(4)):
        maps=[]
        for a,b in pairs:
            maps.append((idx[frozenset(perm[a:b])],frozenset(perm[:a])))
        for i,(ci,ai) in enumerate(maps):
            for j,(cj,aj) in enumerate(maps):
                if Q0[i,j]:Q[ci,cj]+=Q0[i,j]*mon(aj)/mon(ai)
    Q=Q.applyfunc(s.expand)


    C=s.zeros(4,15)
    for i,A in enumerate(itertools.combinations(range(4),3)):
        C[i,idx[frozenset(A)]]=1
        for a,b in itertools.combinations(A,2):
            c=next(x for x in A if x not in (a,b))
            C[i,idx[frozenset((a,b))]]-=(1+z[c])/2
        for a in A:
            b,c=[x for x in A if x!=a]
            C[i,idx[frozenset((a,))]]+=(z[b]+z[c])/2

    def minus(expr):return expr.xreplace({x:1/x for x in w})
    Cm=C.applyfunc(minus)
    E=[]
    for A in sets:
        h=s.zeros(4)
        for a in range(4):h[a,a]=int(A==frozenset((a,)))
        for a,b in itertools.combinations(range(4),2):
            value=(int(A==frozenset((a,b)))-int(A==frozenset((a,)))-int(A==frozenset((b,))))/(2*w[a]*w[b])
            h[a,b]=h[b,a]=value
        E.append(h)
    p=s.Matrix([(x-1/x)/s.I for x in w]); lap=s.expand(p.dot(p))
    F=s.zeros(15)
    for a,Ha in enumerate(E):
        left=Ha.applyfunc(minus)
        for b,Hb in enumerate(E):
            F[a,b]=s.expand(-R(1,4)*(lap*s.trace(left*Hb)-2*(left*p).dot(Hb*p)+s.trace(left)*(p.T*Hb*p)[0]+s.trace(Hb)*(p.T*left*p)[0]-lap*s.trace(left)*s.trace(Hb)))
    proposed=(F-Cm.T*C/2).applyfunc(s.expand)
    res=(Q-proposed).applyfunc(s.expand)
    fail=[(i,j,str(res[i,j])) for i in range(15) for j in range(15) if res[i,j]!=0]

    assert not fail,fail[:3]

    G=s.zeros(15,4)
    for A in sets:
        for a in A:G[idx[A],a]=2*(mon(A)-1)
    assert (Q*G).applyfunc(s.expand)==s.zeros(15,4)
    assert (C*G).applyfunc(s.expand)==s.zeros(4,4)
    assert Q[:,idx[frozenset(range(4))]]==s.zeros(15,1)
    body=[idx[frozenset(A)] for A in itertools.combinations(range(4),3)]
    assert Q.extract(body,body)==-s.eye(4)/2
    assert (Q.extract(body,list(range(15)))+C/2).applyfunc(s.expand)==s.zeros(4,15)
    wrong_body=(Q-F).applyfunc(s.expand)
    assert any(x!=0 for x in wrong_body)
    wrong_sign=(Q+proposed).applyfunc(s.expand)
    assert any(x!=0 for x in wrong_sign)
    # An identity component phase is a distinct, wrong metric map.
    # The full signed coefficient comparison is already independent of this construction.
    wrong_E=[h.copy() for h in E]
    for h in wrong_E:
        for a,b in itertools.combinations(range(4),2):h[a,b]=h[b,a]=s.expand(h[a,b]*w[a]*w[b])
    wrong_gauge=[]
    for c in range(4):
        T=sum((wrong_E[i]*G[i,c] for i in range(15)),s.zeros(4))
        u=s.zeros(4,1);u[c]=w[c]
        wrong_gauge.append((T-s.I*(p*u.T+u*p.T)).applyfunc(s.expand))
    assert any(any(x!=0 for x in T) for T in wrong_gauge)

    out={'status':'exact_coefficient_identity_passed','scope':'one fixed 4D unit path triangulation, all nonzero Laurent phases; no physical gravity claim',
         'local_pairs':pairs,'local_hessian':[[str(Q0[i,j]) for j in range(10)] for i in range(10)],
         'permutations':24,'matrix_entries':225,'nonzero_geometry_entries':sum(x!=0 for x in Q),
         'residual_entries':len(fail),'max_laurent_terms':max(len(s.Add.make_args(x)) for x in Q),
         'checks':['barycentric_normal_sum','local_schlaefli','rational_local_hessian','full_laurent_identity','exact_vertex_gauge','body_constraint_gauge','hyperdiagonal_zero','body_block','body_rows','missing_body_rejected','orientation_reversed_rejected','wrong_metric_phase_rejected'],
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'elapsed_sec':time.monotonic()-started}

    return out, SimpleNamespace(Q=Q,w=w,z=z,p=p,sets=sets,E=E,C=C,G=G,idx=idx,minus=minus)
