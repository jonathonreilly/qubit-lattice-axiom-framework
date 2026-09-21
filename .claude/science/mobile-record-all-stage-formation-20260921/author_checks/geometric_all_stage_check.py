#!/usr/bin/env python3
"""Author controls for the all-stage conditional proof; not an independent audit."""
from pathlib import Path
from collections import deque
import datetime, hashlib, importlib.util, itertools, json, math, random, sys
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent
PARENT=HERE/'geometric_corridor_transport_check.py'
spec=importlib.util.spec_from_file_location('corridor',PARENT)
c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
edge=c.edge
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()

def components(edges):
    remain=set(edges);answer=[]
    while remain:
        first=min(remain);vertices=set(first);todo=[*first]
        for v in todo:
            for e in sorted(remain):
                if v in e:
                    for u in e:
                        if u not in vertices:vertices.add(u);todo.append(u)
        comp={e for e in remain if set(e)<=vertices};remain-=comp;answer.append(comp)
    return answer

def ordered_path(edges,start=None):
    adj={}
    for a,b in edges:adj.setdefault(a,[]).append(b);adj.setdefault(b,[]).append(a)
    if start is None:start=min(v for v in adj if len(adj[v])==1)
    path=[start];previous=None
    while True:
        nxt=[v for v in adj[path[-1]] if v!=previous]
        if not nxt:break
        assert len(nxt)==1
        previous=path[-1];path.append(nxt[0])
    assert len(path)==len(edges)+1
    return path

def apply(M,op):
    a,b,d=op;assert len({a,b,d})==3
    assert edge(b,d) in M and a not in {v for e in M for v in e}
    return (M-{edge(b,d)})|{edge(a,b)}

def align_to_reference(n,edges,start,P):
    M=start;ops=[]
    def execute(new):
        nonlocal M
        for op in new:
            assert edge(op[0],op[1]) in edges
            M=apply(M,op);ops.append(op)
    for part in components(M^P):
        degree={v:sum(v in e for e in part) for e in part for v in e}
        if not any(d==1 for d in degree.values()):continue
        path=ordered_path(part)
        assert edge(*path[:2]) in P and edge(*path[-2:]) in P
        execute([tuple(path[t:t+3]) for t in range(0,len(path)-2,2)])
    while M-P:
        cycles=components(M^P)
        cycle=next(part for part in cycles if part&M)
        degree={v:sum(v in e for e in cycle) for e in cycle for v in e}
        assert all(d==2 for d in degree.values())
        occupied={v for e in M for v in e}
        h=next(e for e in sorted(P-M) if not occupied.intersection(e))
        e=min(cycle&M);T=M|{h}
        execute(c.transport(n,edges,T,h,e))
        assert M==T-{e}
        path=ordered_path(cycle-{e},e[0])
        assert path[-1]==e[1]
        execute([tuple(path[t:t+3]) for t in range(0,len(path)-2,2)])
    assert M<=P
    target=frozenset(sorted(P)[:len(M)])
    while M!=target:
        h=min(target-M);e=min(M-target);T=M|{h}
        execute(c.transport(n,edges,T,h,e))
    assert M==target
    return target,ops

def marked_replay(n,edges,M,target,ops):
    original=M;labels=[-1]*n
    for i,(a,b) in enumerate(sorted(M)):labels[a],labels[b]=2*i,2*i+1
    initial=labels[:]
    for a,b,d in ops:
        old=labels[:];assert old[a]==-1 and old[b]>=0 and old[d]>=0
        assert edge(a,b) in edges and edge(b,d) in M
        labels[a],labels[b],labels[d]=old[b],old[d],-1
        M=apply(M,(a,b,d))
        assert sorted(v for v in labels if v>=0)==list(range(2*len(M)))
        assert all(labels[u]^labels[v]==1 for u,v in M)
        pos={value:site for site,value in enumerate(labels) if value>=0}
        assert all(pos[value]==site or edge(site,pos[value]) in edges
                   for site,value in enumerate(old) if value>=0)
    assert M==target
    for a,b,d in reversed(ops):
        labels[d],labels[b],labels[a]=labels[b],labels[a],-1
        M=apply(M,(d,b,a))
    assert M==original and labels==initial

def levels(n,edges):
    return [c.matchings(n,edges,j) for j in range(n//2+1)]

def graph_cases():
    answer=[]
    for n in [4,6,8,10,12]:
        path={edge(i,i+1) for i in range(n-1)}
        answer.append((f'path_{n}',n,path))
        answer.append((f'cycle_{n}',n,path|{edge(0,n-1)}))
    answer.append(('complete_8',8,set(itertools.combinations(range(8),2))))
    answer.append(('two_k4_bridge',8,set(itertools.combinations(range(4),2))|
                   set(itertools.combinations(range(4,8),2))|{(3,4)}))
    rng=random.Random(9211701)
    for n in [8,10,12]:
        for trial in range(10):
            edges={edge(i,i+1) for i in range(n-1)}
            edges|={e for e in itertools.combinations(range(n),2) if rng.random()<.07}
            answer.append((f'random_{n}_{trial}',n,edges))
    return answer

def connectivity_controls():
    rows=[]
    for name,n,edges in graph_cases():
        states=levels(n,edges);P=states[-1][0];count=longest=0
        for layer in states[:-1]:
            for M in layer:
                target,ops=align_to_reference(n,edges,M,P)
                marked_replay(n,edges,M,target,ops)
                count+=1;longest=max(longest,len(ops))
        rows.append(dict(graph=name,vertices=n,edges=sorted(edges),
                         cardinality_counts=list(map(len,states)),replayed=count,longest_route=longest))
    return dict(pass_=True,graphs=len(rows),marked_paths=sum(r['replayed'] for r in rows),rows=rows)

def injection_for_graph(n,edges):
    layers=levels(n,edges);K=n//2
    if not layers[K]:return None
    Z=len(layers[K]);near=len(layers[K-1]);triples=0
    for j in range(K):
        images=set()
        for M in layers[j]:
            for P in layers[K]:
                paths=[]
                for part in components(M^P):
                    if len(part&P)==len(part&M)+1:paths.append(frozenset(part))
                assert len(paths)==K-j
                for Q in paths:
                    U=M^Q;W=P^Q
                    assert U in layers[j+1] and W in layers[K-1]
                    key=(U,W);assert key not in images;images.add(key)
                    holes=set(range(n))-{v for e in W for v in e}
                    assert len(holes)==2
                    restored=next(part for part in components(U^W)
                                  if holes<={v for e in part for v in e})
                    assert restored==Q and U^Q==M and W^Q==P
                    triples+=1
        assert len(images)==(K-j)*len(layers[j])*Z
        assert len(images)<=len(layers[j+1])*near
    coeff=sum(s.Rational(len(layers[j]),(j+1)*len(layers[j+1])) for j in range(K))
    R=s.Rational(near,Z);bound=2*R*s.harmonic(K)/(K+1)
    assert R/K<=coeff<=bound
    return triples,str(coeff),str(bound)

def counting_controls():
    rows=[];total=0
    for n in [2,4,6]:
        possible=list(itertools.combinations(range(n),2));graphs=triples=0
        for mask in range(1<<len(possible)):
            edges={e for i,e in enumerate(possible) if mask>>i&1}
            if not c.connected(n,edges):continue
            result=injection_for_graph(n,edges)
            if result is None:continue
            graphs+=1;triples+=result[0]
        rows.append(dict(vertices=n,graphs=graphs,injective_triples=triples));total+=triples
        print(json.dumps(dict(group='counting_progress',**rows[-1])),flush=True)
    return dict(pass_=True,graphs=sum(r['graphs'] for r in rows),injective_triples=total,rows=rows)

def matrices(n,edges):
    layers=levels(n,edges);Ls=[];As=[]
    for j,layer in enumerate(layers[:-1]):
        pos={M:i for i,M in enumerate(layer)};upper={M:i for i,M in enumerate(layers[j+1])}
        L=s.zeros(len(layer));A=s.zeros(len(layer),len(upper))
        for M,i in pos.items():
            vacant=set(range(n))-{v for e in M for v in e}
            for u in vacant:
                for v,w in M:
                    for b,d in [(v,w),(w,v)]:
                        if edge(u,b) in edges:
                            T=(M-{edge(b,d)})|{edge(u,b)}
                            t=pos[T];L[i,i]+=1;L[i,t]-=1
            for e in edges:
                if set(e)<=vacant:A[i,upper[M|{e}]]=1
        assert L==L.T and L*s.ones(len(layer),1)==s.zeros(len(layer),1)
        assert list(s.ones(1,len(layer))*A)==[j+1]*len(upper)
        Ls.append(L);As.append(A)
    return layers,Ls,As

def clock_controls():
    cases=[('cycle4',4,{(0,1),(1,2),(2,3),(0,3)}),
           ('paw4',4,{(0,1),(1,2),(0,2),(2,3)}),
           ('cycle6',6,{edge(i,(i+1)%6) for i in range(6)}),
           ('irregular6',6,{(0,1),(1,2),(2,3),(3,4),(4,5),(0,2),(1,4),(2,5)})]
    rows=[]
    for name,n,edges in cases:
        layers,Ls,As=matrices(n,edges);K=n//2
        p=[s.Rational((j+1)*len(layers[j+1]),len(layers[j])) for j in range(K)]
        coefficient=sum(1/v for v in p);svalue=s.Rational(7,5)
        target_transform=s.prod(v/(v+svalue) for v in p)
        for beta in [s.Rational(1),s.Rational(1,100),s.Rational(1,1000000)]:
            t=s.zeros(len(layers[-1]),1);F=s.eye(len(layers[-1]))
            stage_errors=[]
            for j in reversed(range(K)):
                L,A=Ls[j],As[j];dim=L.rows;h=A*s.ones(A.cols,1);H=s.diag(*h)
                killed=L+beta*H;inv=killed.inv()
                t=inv*(s.ones(dim,1)+beta*A*t)
                F=(killed+svalue*beta*s.eye(dim)).inv()*beta*A*F
                exitlaw=inv*beta*A
                assert exitlaw*s.ones(A.cols,1)==s.ones(dim,1)
                stage_errors.append(max(abs(float(v-s.Rational(1,A.cols))) for v in exitlaw))
            mean=float(beta*t[0]);transform=float(sum(F))
            error=abs(mean/float(coefficient)-1)
            joint_error=max(abs(float(v-target_transform/len(layers[-1]))) for v in F)
            if beta==s.Rational(1,1000000):
                assert error<1e-4 and joint_error<1e-4 and max(stage_errors)<1e-4
            rows.append(dict(graph=name,beta=str(beta),p=list(map(str,p)),
                             limiting_mean=str(coefficient),scaled_exact_mean=str(beta*t[0]),
                             mean_relative_error=error,exact_laplace=str(sum(F)),
                             limiting_laplace=str(target_transform),joint_exit_transform_error=joint_error,
                             max_entry_stage_exit_error=max(stage_errors)))
    # Exact symbolic whole-clock limit and mean on the cycle4, no beta truncation.
    name,n,edges=cases[0];layers,Ls,As=matrices(n,edges)
    b=s.symbols('b',positive=True);t=s.zeros(len(layers[-1]),1);F=s.ones(len(layers[-1]),1)
    for L,A in reversed(list(zip(Ls,As))):
        H=s.diag(*(A*s.ones(A.cols,1)));Q=L+b*H
        t=Q.inv()*(s.ones(L.rows,1)+b*A*t)
        F=(Q+svalue*b*s.eye(L.rows)).inv()*b*A*F
    assert s.limit(b*t[0],b,0)==s.Rational(5,4)
    assert s.limit(F[0],b,0)==s.Rational(4,4+svalue)*s.Rational(1,1+svalue)
    return dict(pass_=True,rows=rows,cycle4_symbolic_mean=str(s.factor(b*t[0])),
                cycle4_symbolic_laplace=str(s.factor(F[0])))

def comparison_controls():
    rows=[]
    cases=graph_cases()[:6]+[('complete4',4,set(itertools.combinations(range(4),2))),
                            ('irregular6',6,{(0,1),(1,2),(2,3),(3,4),(4,5),(0,2),(1,4),(2,5)})]
    for name,n,edges in cases:
        layers,Ls,As=matrices(n,edges);m=len(edges)
        for j in range(1,n//2):
            lower=layers[j];upper=layers[j+1];k=j+1;size=len(lower)+len(upper)
            states=lower+upper;B=np.zeros((size,size));D=np.asarray(Ls[j],dtype=float)
            for a,b in itertools.combinations(range(size),2):
                x,y=states[a],states[b]
                legal=(len(x)==len(y) and len(x-y)==len(y-x)==1) or (
                    abs(len(x)-len(y))==1 and (x<=y or y<=x))
                if legal:B[a,a]+=1;B[b,b]+=1;B[a,b]-=1;B[b,a]-=1
            A=np.asarray(As[j],dtype=float)
            extension=np.vstack([np.eye(len(lower)),A.T/k])
            C=1+(n-2)*(m+m*m)*(k-1)*(k+1+2*m)
            slack=C*D-extension.T@B@extension
            residual=float(np.linalg.eigvalsh(slack).min())
            assert residual>-1e-7
            gap=float(np.linalg.eigvalsh(D)[1]);bgap=float(np.linalg.eigvalsh(B)[1])
            assert gap>0 and bgap>0 and gap+1e-10>=bgap/C
            rows.append(dict(graph=name,j=j,lower=len(lower),upper=len(upper),comparison_factor=C,
                             slide_gap=gap,auxiliary_gap=bgap,minimum_energy_slack=residual))
    return dict(pass_=True,rows=rows)

def main():
    out=HERE/'geometric_all_stage_checks';out.mkdir(exist_ok=False)
    sources={p.name:sha(p) for p in [Path(__file__),PARENT,HERE/'GEOMETRIC_ALL_STAGE_FORMATION_CLOCK.md']}
    rows=[]
    for name,fn in [('connectivity',connectivity_controls),('counting',counting_controls),
                    ('clock',clock_controls),('comparison',comparison_controls)]:
        result=fn();result['pass']=result.pop('pass_');rows.append(dict(group=name,**result))
        (out/(name+'.json')).write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps(dict(group=name,passed=True)),flush=True)
    assert sources=={name:sha(HERE/name) for name in sources}
    report=dict(scope='Author exact/finite controls for the candidate all-stage proof. No independent review or all-volume quantitative theorem.',
                sources_sha256=sources,rows=rows,created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
    (out/'RESULTS.json').write_text(json.dumps(report,indent=2)+'\n')
    print('PASS: four complete all-stage control groups',flush=True)

if __name__=='__main__':main()

