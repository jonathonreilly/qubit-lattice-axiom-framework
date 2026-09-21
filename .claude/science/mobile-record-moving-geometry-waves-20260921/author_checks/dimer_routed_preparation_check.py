#!/usr/bin/env python3
"""Author exact and finite controls for the explicit color-preparation bound."""
from pathlib import Path
from collections import Counter,deque
from fractions import Fraction as F
import datetime,hashlib,itertools,json,math
import numpy as np
from scipy.linalg import expm
HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()

def swapped(state,a,b):
    x=list(state);x[a],x[b]=x[b],x[a];return tuple(x)

def conditional_controls():
    rows=[]
    for K in range(2,7):
        states=list(itertools.permutations(range(K)));size=len(states)
        rng=np.random.default_rng(202609211950+K)
        values=dict(zip(states,map(int,rng.integers(-23,24,size=size))))
        mean=F(sum(values.values()),size)
        variance=sum((v-mean)**2 for v in values.values())/size
        energies={(i,j):F(sum((values[swapped(x,i,j)]-values[x])**2 for x in states),2*size)
                  for i,j in itertools.combinations(range(K),2)}
        D=sum(energies.values());assert variance<=F(2,K)*D
        average_conditional=average_between=F(0)
        for i in range(K):
            groups={a:[x for x in states if x[i]==a] for a in range(K)}
            means={a:F(sum(values[x] for x in xs),len(xs)) for a,xs in groups.items()}
            inside=sum(sum((values[x]-means[a])**2 for x in xs) for a,xs in groups.items())/size
            between=sum((v-mean)**2 for v in means.values())/K
            assert variance==inside+between
            cross=sum(v for (a,b),v in energies.items() if i in (a,b))
            assert between<=cross/K
            if K>2:
                internal=D-cross;assert inside<=F(2,K-1)*internal
            for a in range(K):
                for b in range(K):
                    targets=[swapped(x,i,x.index(b)) for x in groups[a]]
                    assert len(set(targets))==len(groups[b]) and set(targets)==set(groups[b])
                    difference=F(sum(values[x]-values[y] for x,y in zip(groups[a],targets)),len(targets))
                    assert difference==means[a]-means[b]
            average_conditional+=inside/K;average_between+=between/K
        assert average_conditional+average_between==variance
        rows.append(dict(K=K,permutations=size,variance=str(variance),D_all=str(D),
                         complete_comparison_factor=str(F(2,K)),all_conditional_bijections_verified=True))
    return rows

def shortest_path(K,edges,start,end):
    adj=[[] for _ in range(K)]
    for a,b in sorted(edges):adj[a].append(b);adj[b].append(a)
    previous={start:None};queue=deque([start])
    while queue:
        u=queue.popleft()
        if u==end:break
        for v in adj[u]:
            if v not in previous:previous[v]=u;queue.append(v)
    if end not in previous:return None
    path=[end]
    while path[-1]!=start:path.append(previous[path[-1]])
    return list(reversed(path))

def graph_controls():
    rows=[];routes=graphs=0
    for K in range(2,6):
        all_edges=list(itertools.combinations(range(K),2));count=0;worst_ratio=0.;minimum_slack=float('inf')
        base=tuple(i%3 for i in range(K));states=sorted(set(itertools.permutations(base)));index={x:i for i,x in enumerate(states)}
        def laplacian(edges):
            L=np.zeros((len(states),len(states)),dtype=np.int64)
            for i,x in enumerate(states):
                for a,b in edges:
                    j=index[swapped(x,a,b)];L[i,i]+=1;L[i,j]-=1
            assert np.array_equal(L,L.T) and np.all(L.sum(axis=1)==0)
            return L
        complete=laplacian(all_edges)
        assert np.linalg.eigvalsh(complete.astype(float))[1]>=K/2-1e-10
        for mask in range(1<<len(all_edges)):
            edges={e for i,e in enumerate(all_edges) if mask>>i&1}
            if any(shortest_path(K,edges,0,x) is None for x in range(K)):continue
            paths=[shortest_path(K,edges,a,b) for a,b in all_edges];diam=max(len(p)-1 for p in paths)
            occurrences=Counter()
            for (a,b),path in zip(all_edges,paths):
                forward=list(zip(path[:-1],path[1:]));route=forward+forward[-2::-1]
                assert len(route)==2*len(path)-3<=2*diam-1
                old=tuple(range(K));new=old
                for x,y in route:new=swapped(new,x,y)
                assert new==swapped(old,a,b)
                counts=Counter(tuple(sorted(e)) for e in route);assert max(counts.values())<=2
                occurrences.update(counts);routes+=1
            assert max(occurrences.values())<=K*(K-1)
            L=laplacian(edges);factor=(2*diam-1)*K*(K-1)
            slack=float(np.linalg.eigvalsh((factor*L-complete).astype(float)).min())
            assert slack>-1e-8
            lower=1/(2*(2*diam-1)*(K-1));gap=float(np.linalg.eigvalsh(L.astype(float))[1])
            assert gap>=lower-1e-10
            worst_ratio=max(worst_ratio,lower/gap);minimum_slack=min(minimum_slack,slack);count+=1;graphs+=1
        rows.append(dict(K=K,connected_labeled_graphs=count,color_sector_size=len(states),
                         largest_proved_lower_bound_over_actual_gap=worst_ratio,minimum_comparison_slack=minimum_slack))
    return dict(graphs=graphs,immutable_endpoint_transposition_replays=routes,rows=rows)

def density_controls():
    K=5;Q=np.zeros((K,K));clockwise=2.;counterclockwise=.5
    for i in range(K):Q[i,(i+1)%K]+=clockwise;Q[i,(i-1)%K]+=counterclockwise;Q[i,i]-=clockwise+counterclockwise
    assert np.all(Q.sum(axis=0)==0) and np.all(Q.sum(axis=1)==0) and not np.array_equal(Q,Q.T)
    S=(Q+Q.T)/2;r=(clockwise+counterclockwise)/2;D=2;g=r/(2*(2*D-1)*(K-1))
    assert np.linalg.eigvalsh(-S)[1]>=g
    rows=[]
    for t in [.05,.5,2.,10.]:
        initial=np.zeros(K);initial[0]=1;prob=expm(t*Q.T)@initial
        chi=math.sqrt(float(np.mean((K*prob-1)**2)));bound=math.sqrt(K-1)*math.exp(-g*t)
        tv=float(abs(prob-1/K).sum()/2)
        assert chi<=bound+1e-12 and tv<=chi/2+1e-12
        rows.append(dict(t=t,centered_L2=chi,L2_bound=bound,total_variation=tv))
    # Exact count-sector mixture equals the product law, with a nonuniform p.
    p=[F(1,2),F(1,3),F(1,6)];states=list(itertools.product(range(3),repeat=5));sectors=Counter(tuple(x.count(a) for a in range(3)) for x in states)
    total=F(0)
    for x in states:
        counts=tuple(x.count(a) for a in range(3));multiplicity=math.factorial(5)//math.prod(math.factorial(c) for c in counts)
        assert multiplicity==sectors[counts]
        count_law=multiplicity*math.prod(pa**c for pa,c in zip(p,counts))
        probability=count_law/multiplicity;assert probability==math.prod(p[a] for a in x);total+=probability
    assert total==1
    schedule=[]
    for N in [8,16,32,64,128,256]:
        K=N**3//2;k0=1.1;g=k0/(4*(3*N-1)*(K-1));eps=N**-4
        t=(K*math.log(14)/2+math.log(1/(2*eps)))/g
        # Logarithms avoid overflow in the deliberately enormous uniform bound.
        assert abs((-math.log(2)+K*math.log(14)/2-g*t)-math.log(eps))<1e-8
        schedule.append(dict(N=N,pairs=K,epsilon=eps,gap_lower_bound=g,sufficient_post_completion_time=t))
    return dict(nonreversible_density_rows=rows,count_mixture_states=len(states),all_sector_weights_exact=True,schedule=schedule)

def main():
    out=HERE/'dimer_routed_preparation_checks';out.mkdir(exist_ok=False)
    files=[Path(__file__),HERE/'DIMER_ROUTED_POLYNOMIAL_COLOR_PREPARATION.md',HERE/'DIMER_ROUTED_RECORD_TRANSPORT.md']
    sources={p.name:sha(p) for p in files};rows=[]
    for name,fn in [('conditional_permutation_bound',conditional_controls),('physical_graph_comparison',graph_controls),('nonreversible_preparation',density_controls)]:
        value=fn();rows.append(dict(group=name,passed=True,detail=value));print(json.dumps(dict(group=name,passed=True)),flush=True)
        (out/(name+'.json')).write_text(json.dumps(value,indent=2)+'\n')
    assert sources=={p.name:sha(p) for p in files}
    report=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),sources_sha256=sources,groups=rows,
      scope='Author finite controls for an all-volume proof; not a mixing-exponent fit, native rate derivation or independent audit.')
    (out/'RESULTS.json').write_text(json.dumps(report,indent=2)+'\n');print('PASS: three complete color-preparation groups',flush=True)
if __name__=='__main__':main()
