"""Author exact controls for finite-volume slow-birth selection.

This checks geometric matchings, not ergodicity of immutable marked records.
The connectivity algorithm implements the proof; exhaustive slide-graph BFS
and harmonic residuals are separate controls, not an independent review.
"""
from pathlib import Path
from itertools import product, combinations, permutations
from collections import deque, Counter
import hashlib, json, random
import sympy as sp
from geometric_partner_formation_check import graph, prepare, enumerate_matchings, channels, edge, partners

HERE=Path(__file__).resolve().parent
OUT=HERE/'geometric_rare_birth_checks'
OUT.mkdir(exist_ok=True)
ROWS=[]

def report(name, **data):
    row={'name':name, 'pass':True, **data}
    ROWS.append(row)
    print(json.dumps(row), flush=True)

def validate(M,G):
    p=partners(M)
    assert len(p)==2*len(M) and all(e in G['edge_set'] for e in M)
    assert len(M)*2==len(G['neighbors'])-2
    return p

def slide(M,event,G):
    a,b,c=event
    p=validate(M,G)
    assert p.get(a)==b and c not in p and c in G['neighbors'][b]
    result=frozenset((M-{edge(a,b)})|{edge(b,c)})
    validate(result,G)
    return result

def hole_path(M,G,side,targets):
    """Shortest alternating path, expressed as actual record-slide events."""
    p=validate(M,G)
    head=next(iter(side-set(p)))
    previous={head:None}
    queue=deque([head])
    found=None
    while queue:
        u=queue.popleft()
        if u in targets:
            found=u
            break
        for mid in sorted(G['neighbors'][u]):
            if mid not in p:
                continue
            v=p[mid]
            if v not in previous:
                previous[v]=(u,mid)
                queue.append(v)
    assert found is not None, 'strict Hall reachability failed'
    events=[]
    while previous[found] is not None:
        old,mid=previous[found]
        events.append((found,mid,old))
        found=old
    events.reverse()
    return events

def transform(M,target,G,L):
    """Align two holes, then flip each symmetric-difference cycle by a lollipop."""
    initial=M
    R=set(range(len(G['neighbors'])))-L
    target_p=validate(target,G)
    events=[]
    def execute(e):
        nonlocal M
        M=slide(M,e,G)
        events.append(e)
    for side in [L,R]:
        goal=side-set(target_p)
        assert len(goal)==1
        for e in hole_path(M,G,side,goal):
            execute(e)
    assert set(partners(M))==set(target_p)
    cycles=0
    while M!=target:
        adj={u:set() for u in range(len(G['neighbors']))}
        for a,b in M^target:
            adj[a].add(b);adj[b].add(a)
        first=min(u for u,v in adj.items() if v)
        C={first};stack=[first]
        while stack:
            u=stack.pop()
            assert len(adj[u])==2
            for v in adj[u]-C:
                C.add(v);stack.append(v)
        old=M
        entrance=hole_path(M,G,L,C&L)
        assert entrance and all(v not in C for e in entrance[:-1] for v in e)
        assert entrance[-1][0] in C and entrance[-1][1] in C and entrance[-1][2] not in C
        for e in entrance:
            execute(e)
        head=entrance[-1][0]
        while head in C:
            mid=target_p[head]
            nxt=partners(M)[mid]
            execute((nxt,mid,head))
            head=nxt
        assert head==entrance[-1][2]
        for a,b,c in reversed(entrance[:-1]):
            execute((c,b,a))
        outside=lambda mm:frozenset(e for e in mm if not set(e)<=C)
        assert outside(M)==outside(old)
        assert {e for e in M if set(e)<=C}=={e for e in target if set(e)<=C}
        assert set(partners(M))==set(target_p)
        cycles+=1
    # Full replay plus inverse supports ensure that the actual legal sequence
    # did not merely change an abstract alternating-cycle incidence vector.
    replay=initial
    for e in events:replay=slide(replay,e,G)
    assert replay==target
    for a,b,c in reversed(events):replay=slide(replay,(c,b,a),G)
    assert replay==initial
    return events,cycles

def bipartite_graph(rows):
    K=len(rows)
    neighbors=[set() for _ in range(2*K)]
    edges=[]
    for a,row in enumerate(rows):
        for b in row:
            neighbors[a].add(K+b);neighbors[K+b].add(a);edges.append((a,K+b))
    return {'neighbors':neighbors,'edges':edges,'edge_set':set(edges),'sites':list(range(2*K)),'faces':[]}

def connected(G):
    seen={0};todo=[0]
    while todo:
        u=todo.pop()
        for v in G['neighbors'][u]-seen:seen.add(v);todo.append(v)
    return len(seen)==len(G['neighbors'])

def near_matchings(G,L):
    K=len(L)
    left=sorted(L)
    def visit(j,used,M):
        if len(M)>K-1 or len(M)+K-j<K-1:return
        if j==K:
            if len(M)==K-1:yield frozenset(M)
            return
        a=left[j]
        yield from visit(j+1,used,M)
        for b in sorted(G['neighbors'][a]-used):
            yield from visit(j+1,used|{b},M+[edge(a,b)])
    return list(visit(0,set(),[]))

def bfs_component(G,states):
    pool=set(states);seen={states[0]};queue=deque(seen);count=0
    while queue:
        M=queue.popleft();p=partners(M)
        for b,a in p.items():
            for c in G['neighbors'][b]-set(p):
                t=frozenset((M-{edge(a,b)})|{edge(b,c)})
                assert t in pool
                count+=1
                if t not in seen:seen.add(t);queue.append(t)
    assert seen==pool
    return count

def exhaustive_small_graphs():
    totals=Counter();worst=0;cycle_flips=0
    for K in range(1,5):
        for k in range(1,K+1):
            for rows in product(list(combinations(range(K),k)),repeat=K):
                if any(sum(j in row for row in rows)!=k for j in range(K)):continue
                G=bipartite_graph(rows)
                if not connected(G):continue
                L=set(range(K));states=near_matchings(G,L)
                assert states
                count=bfs_component(G,states)
                for M in states:
                    events,cycles=transform(M,states[0],G,L)
                    worst=max(worst,len(events));cycle_flips+=cycles
                totals['graphs']+=1;totals['near_states']+=len(states);totals['directed_slide_channels']+=count
    report('all_connected_regular_bipartite_graphs_up_to_four_vertices_per_side',**totals,
           longest_constructed_transform=worst,cycles_flipped=cycle_flips)

def cube_harmonic():
    G=prepare(graph((2,2,2)));states=enumerate_matchings(G)
    b=sp.Symbol('b',positive=True)
    transforms=[]
    for perm in permutations(range(3)):
        for flips in product([0,1],repeat=3):
            transforms.append({u:G['index'][tuple(x[perm[i]]^flips[i] for i in range(3))] for u,x in enumerate(G['sites'])})
    def representative(M):
        return min(tuple(sorted(edge(T[a],T[c]) for a,c in M)) for T in transforms)
    rep={M:representative(M) for M in states};orbits=sorted(set(rep.values()));OI={M:i for i,M in enumerate(orbits)}
    Q=sp.zeros(len(orbits));known={}
    for M in states:
        row=[sp.Integer(0)]*len(orbits);i=OI[rep[M]]
        for t,rate,event in channels(M,G,b,1,0):
            j=OI[rep[t]];row[j]+=rate;row[i]-=rate
        if i in known:assert known[i]==row
        else:known[i]=row
    for i,row in known.items():
        for j,q in enumerate(row):Q[i,j]=q
    transient=[i for i,M in enumerate(orbits) if len(M)<4]
    full=[i for i,M in enumerate(orbits) if len(M)==4]
    def columnar(M):
        axes={next(j for j in range(3) if G['sites'][a][j]!=G['sites'][c][j]) for a,c in M}
        return len(axes)==1
    boundary={i:sp.Integer(columnar(orbits[i])) for i in full}
    rhs=sp.Matrix([sum(Q[i,j]*boundary[j] for j in full) for i in transient])
    u=(-Q.extract(transient,transient)).inv()*rhs
    values={**boundary,**{i:sp.factor(u[j]) for j,i in enumerate(transient)}}
    # Check every original state/channel, including full boundary conditions.
    for M in states:
        actual=values[OI[rep[M]]]
        if len(M)==4:assert actual==int(columnar(M))
        else:
            residual=sum(rate*(values[OI[rep[t]]]-actual) for t,rate,e in channels(M,G,b,1,0))
            assert sp.cancel(residual)==0
    expected=(6*b**3+77*b**2+308*b+308)/(7*(b+6)*(3*b**2+19*b+22))
    result=values[OI[()]]
    assert sp.cancel(result-expected)==0
    assert sp.limit(result,b,0)==sp.Rational(1,3)
    assert sp.limit(result,b,sp.oo)==sp.Rational(2,7)
    certificate={'variable':'b=beta/kappa; nu=0', 'orbits':orbits,
                 'generator':[[str(q) for q in row] for row in Q.tolist()],
                 'harmonic_solution':[str(values[i]) for i in range(len(orbits))],
                 'full_state_boundary_and_harmonic_checks':len(states),
                 'empty_columnar_probability':str(result)}
    (OUT/'CUBE_HARMONIC_CERTIFICATE.json').write_text(json.dumps(certificate,indent=2)+'\n')
    report('cube_exact_symbolic_absorption_and_108_state_harmonic_lift',states=len(states),
           probability=str(result),at_one=str(result.subs(b,1)),slow_limit='1/3',fast_limit='2/7')
    # Solve the complete near-perfect killed chain for each full target. This
    # does not use cubic symmetry or the lumped absorption computation above.
    near=[M for M in states if len(M)==3];full_states=[M for M in states if len(M)==4]
    I={M:i for i,M in enumerate(near)};FI={M:i for i,M in enumerate(full_states)}
    S=sp.zeros(len(near));H=sp.zeros(len(near));A=sp.zeros(len(near),len(full_states))
    for M,i in I.items():
        for t,r,e in channels(M,G,0,1,0):S[i,I[t]]+=r;S[i,i]-=r
        births=channels(M,G,1,0,0)
        assert len(births)<=1
        H[i,i]=len(births)
        for t,r,e in births:A[i,FI[t]]=r
    assert S==S.T and all(sum(A[i,j] for i in range(len(near)))==4 for j in range(9))
    assert sum(H.diagonal())==36
    numerical=[]
    for rate in [sp.Rational(1),sp.Rational(1,10),sp.Rational(1,100),sp.Rational(1,1000)]:
        U=(-S+rate*H).inv()*(rate*A)
        assert (-S+rate*H)*U==rate*A and all(sum(row)==1 for row in U.tolist())
        assert all(q>=0 for q in U)
        deviation=max(sum(abs(U[i,j]-sp.Rational(1,9)) for j in range(9))/2 for i in range(len(near)))
        numerical.append({'beta':str(rate),'worst_start_TV':str(deviation),'decimal':float(deviation)})
    assert all(a['decimal']>b['decimal'] for a,b in zip(numerical,numerical[1:]))
    (OUT/'CUBE_KILLED_CHAIN.json').write_text(json.dumps({'near_states':len(near),'full_states':len(full_states),'rows':numerical},indent=2)+'\n')
    report('full_near_perfect_killed_chain_all_targets',near_states=len(near),full_states=len(full_states),rows=numerical)

def periodic_constructive_controls():
    rows=[]
    for N in [4,6,8,12]:
        G=prepare(graph((N,N,N),True));L={i for i,x in enumerate(G['sites']) if sum(x)%2==0}
        def columnar(axis,shift):
            result=set()
            for u,x in enumerate(G['sites']):
                if x[axis]%2==shift:
                    y=list(x);y[axis]=(y[axis]+1)%N;result.add(edge(u,G['index'][tuple(y)]))
            return frozenset(result)
        first=columnar(0,0);target_full=columnar(0,1)
        M=first-{min(first)};target=target_full-{min(target_full)}
        events,cycles=transform(frozenset(M),frozenset(target),G,L)
        rows.append({'N':N,'case':'shifted_columnar_noncontractible_cycles','events':len(events),'cycles':cycles})
        # Orthogonal columnars require contractible-cycle rearrangements too.
        target_full=columnar(1,0);target=frozenset(target_full-{min(target_full)})
        events,cycles=transform(frozenset(M),target,G,L)
        rows.append({'N':N,'case':'orthogonal_columnar','events':len(events),'cycles':cycles})
    report('periodic_constructive_paths_with_noncontractible_cycles',rows=rows)

def main():
    exhaustive_small_graphs()
    cube_harmonic()
    periodic_constructive_controls()
    sources=[Path(__file__),HERE/'GEOMETRIC_RARE_BIRTH_UNIFORM_SELECTION.md',HERE/'geometric_partner_formation_check.py',HERE/'GEOMETRIC_PARTNER_RECORD_FORMATION.md']
    result={'status':'author exact controls; independent review pending; finite graphs and ordered rate limit only',
            'rows':ROWS,'source_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}}
    (OUT/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'complete':True,'groups':len(ROWS),'source_sha256':result['source_sha256']},indent=2))

if __name__=='__main__':main()
