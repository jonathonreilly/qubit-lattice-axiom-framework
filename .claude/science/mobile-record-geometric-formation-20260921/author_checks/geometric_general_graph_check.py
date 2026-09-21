"""Author constructive paths versus exhaustive near-perfect slide graphs."""
from pathlib import Path
from collections import deque,Counter
from itertools import combinations
import hashlib,json,random,time
from geometric_partner_formation_check import graph,prepare,enumerate_matchings,edge,partners,records_from,apply_record_event,read_matching

HERE=Path(__file__).resolve().parent;OUT=HERE/'geometric_general_graph_checks';OUT.mkdir(exist_ok=True)
ROWS=[]
def report(name,**data):
    row={'name':name,'pass':True,**data};ROWS.append(row);print(json.dumps(row),flush=True)
def simple_graph(n,edges):
    E={edge(a,b) for a,b in edges};adj=[set() for _ in range(n)]
    for a,b in E:assert a!=b;adj[a].add(b);adj[b].add(a)
    return {'sites':list(range(n)),'edges':sorted(E),'edge_set':E,'neighbors':adj,'faces':[]}
def is_connected(G):
    seen={0};todo=[0]
    while todo:
        for v in G['neighbors'][todo.pop()]-seen:seen.add(v);todo.append(v)
    return len(seen)==len(G['sites'])
def move(M,e,G):
    a,b,c=e;p=partners(M)
    assert p.get(a)==b and c not in p and c in G['neighbors'][b]
    out=frozenset((M-{edge(a,b)})|{edge(b,c)})
    assert len(partners(out))==2*len(out) and all(q in G['edge_set'] for q in out)
    return out
def complete_virtually(M,P,G):
    p=partners(M);hole=next(u for u in range(len(G['sites'])) if u not in p)
    diff=M^P;adj=[[] for _ in G['sites']]
    for a,b in diff:adj[a].append(b);adj[b].append(a)
    path=[hole]
    while True:
        options=[v for v in adj[path[-1]] if len(path)==1 or v!=path[-2]]
        if not options:break
        assert len(options)==1 and options[0] not in path;path.append(options[0])
    assert len(path)%2==0 and path[-1] not in p
    events=[]
    for j in range(0,len(path)-2,2):
        e=(path[j+2],path[j+1],path[j]);M=move(M,e,G);events.append(e)
    missing=edge(path[-2],path[-1]);F=frozenset(M|{missing})
    assert len(partners(F))==len(G['sites']) and len(events)<=len(G['sites'])//2-1
    return M,F,missing,events
def relocate(M,F,missing,target,G):
    assert M==F-{missing};owner={v:e for e in F for v in e}
    prior={missing:None};queue=deque([missing])
    while target not in prior and queue:
        e=queue.popleft()
        for a in e:
            for b in sorted(G['neighbors'][a]):
                f=owner[b]
                if f not in prior:prior[f]=(e,a,b);queue.append(f)
    assert target in prior
    path=[];current=target
    while prior[current] is not None:
        e,a,b=prior[current];path.append((e,current,a,b));current=e
    events=[]
    for e,f,a,b in reversed(path):
        ap=next(v for v in e if v!=a);bp=next(v for v in f if v!=b)
        for event in [(bp,b,a),(b,a,ap)]:M=move(M,event,G);events.append(event)
        assert M==F-{f}
    assert M==F-{target} and len(events)<=2*(len(F)-1)
    return M,events
def connect(M,T,P,G):
    initial=M;M,F,missing,events=complete_virtually(M,P,G)
    tnear,TF,tmissing,tail=complete_virtually(T,P,G)
    target_partner=partners(TF);cycles=0
    while F!=TF:
        adj=[set() for _ in G['sites']]
        for a,b in F^TF:adj[a].add(b);adj[b].add(a)
        first=next(v for v,a in enumerate(adj) if a);C={first};todo=[first]
        while todo:
            u=todo.pop();assert len(adj[u])==2
            for v in adj[u]-C:C.add(v);todo.append(v)
        chosen=min(e for e in F if set(e)<=C)
        M,es=relocate(M,F,missing,chosen,G);events.extend(es)
        anchor,head=chosen;count=0;oldF=F
        while target_partner[head]!=anchor:
            mid=target_partner[head];nxt=partners(M)[mid]
            event=(nxt,mid,head);M=move(M,event,G);events.append(event);head=nxt;count+=1
        missing=edge(head,anchor);F=frozenset(M|{missing});cycles+=1
        assert count==len(C)//2-1
        assert F==frozenset((oldF-{e for e in oldF if set(e)<=C})|{e for e in TF if set(e)<=C})
    M,es=relocate(M,F,missing,tmissing,G);events.extend(es);assert M==tnear
    for a,b,c in reversed(tail):
        event=(c,b,a);M=move(M,event,G);events.append(event)
    assert M==T
    replay=initial
    for e in events:replay=move(replay,e,G)
    assert replay==T
    for a,b,c in reversed(events):replay=move(replay,(c,b,a),G)
    assert replay==initial
    K=len(P);assert len(events)<=K*K+4*K
    return events,cycles
def near_components(near,G):
    left=set(near);parts=[];channels=0
    while left:
        seed=next(iter(left));seen={seed};todo=[seed]
        while todo:
            M=todo.pop();p=partners(M)
            for b,a in p.items():
                for c in G['neighbors'][b]-set(p):
                    target=frozenset((M-{edge(a,b)})|{edge(b,c)});assert target in left or target in seen;channels+=1
                    if target not in seen:seen.add(target);todo.append(target)
        parts.append(seen);left-=seen
    return parts,channels

def all_small_graphs():
    totals=Counter();by_size=[];worst=0;began=time.monotonic()
    for n in [2,4,6]:
        edges=list(combinations(range(n),2));counts=Counter()
        for mask in range(1<<len(edges)):
            G=simple_graph(n,[e for i,e in enumerate(edges) if mask>>i&1])
            if not is_connected(G):continue
            states=enumerate_matchings(G);full=[M for M in states if len(M)==n//2]
            if not full:continue
            P=full[0];near=[M for M in states if len(M)==n//2-1]
            components,channels=near_components(near,G);assert len(components)==1
            target=near[0]
            for M in near:
                events,cycles=connect(M,target,P,G);worst=max(worst,len(events));counts['cycle_changes']+=cycles
            counts['graphs']+=1;counts['near_states']+=len(near);counts['directed_slide_channels']+=channels
        by_size.append({'vertices':n,**counts});totals.update(counts)
        print(json.dumps({'progress_vertices':n,'counts':dict(counts),'elapsed_seconds':time.monotonic()-began}),flush=True)
    report('all_connected_labeled_simple_graphs_through_six_vertices_with_a_perfect_matching',rows=by_size,totals=dict(totals),maximum_constructed_path=worst)

def sparse_and_nonbipartite_controls():
    rng=random.Random(2109211550);rows=[]
    for n in [8,10,12,16,24]:
        for rep in range(16):
            P=frozenset((2*i,2*i+1) for i in range(n//2));edges=set(P)
            # Join the contracted matching into a random tree, then add edges;
            # bridges, leaves, odd cycles and irregular degrees are permitted.
            for j in range(1,n//2):
                i=rng.randrange(j);edges.add(edge(2*i+rng.randrange(2),2*j+rng.randrange(2)))
            for a,b in combinations(range(n),2):
                if rng.random()<.07:edges.add((a,b))
            G=simple_graph(n,edges);assert is_connected(G)
            M=frozenset(P-{rng.choice(sorted(P))});T=frozenset(P-{rng.choice(sorted(P))})
            # Obtain unrelated near states by unbiased legal slide steps.
            for side in [0,1]:
                state=M if side==0 else T
                for _ in range(10*n):
                    p=partners(state);es=[(a,b,c) for b,a in p.items() for c in G['neighbors'][b]-set(p)]
                    if es:state=move(state,rng.choice(es),G)
                if side==0:M=state
                else:T=state
            events,cycles=connect(M,T,P,G)
            # Track genuine unchanged rational Bloch keys along the entire path.
            state,births,key=records_from(M,G);old={rid:content for rid,content in state.values()}
            for e in events:key=apply_record_event(state,('slide',*e),G,key,births)
            assert read_matching(state,G)==T and old=={rid:content for rid,content in state.values()}
            rows.append({'vertices':n,'replicate':rep,'edges':len(edges),'events':len(events),'cycle_changes':cycles})
    report('irregular_bridge_and_odd_cycle_examples_with_immutable_content_replay',cases=len(rows),rows=rows)

def periodic_controls():
    rows=[]
    for N in [4,6,8,12]:
        G=prepare(graph((N,N,N),True));P=G['perfect']
        for axis,shift in [(0,1),(1,0)]:
            F=set()
            for u,x in enumerate(G['sites']):
                if x[axis]%2==shift:
                    y=list(x);y[axis]=(y[axis]+1)%N;F.add(edge(u,G['index'][tuple(y)]))
            M=frozenset(P-{min(P)});T=frozenset(F-{min(F)})
            events,cycles=connect(M,T,P,G)
            rows.append({'N':N,'target_axis':axis,'target_shift':shift,'events':len(events),'cycles':cycles})
    report('periodic_contractible_and_winding_cycle_paths',rows=rows)

def disconnected_control():
    edges={(offset+i,offset+(i+1)%4) for offset in [0,4] for i in range(4)}
    G=simple_graph(8,edges);states=enumerate_matchings(G);near=[M for M in states if len(M)==3]
    components,_=near_components(near,G);assert sorted(map(len,components))==[4,4,4,4]
    full={M for M in states if len(M)==4};assert len(full)==4
    exits=[]
    for component in components:
        reachable=set()
        for M in component:
            p=partners(M);holes=[v for v in range(8) if v not in p]
            if edge(*holes) in G['edge_set']:reachable.add(M|{edge(*holes)})
        assert len(reachable)==2;exits.append(len(reachable))
    report('disconnected_two_square_countercontrol',near_states=16,component_sizes=[4]*4,full_matchings=4,reachable_full_counts=exits)

def main():
    all_small_graphs();sparse_and_nonbipartite_controls();periodic_controls();disconnected_control()
    sources=[Path(__file__),HERE/'GEOMETRIC_TWO_VACANCY_GENERAL_GRAPH.md',HERE/'geometric_partner_formation_check.py']
    result={'scope':'Author exact finite controls and constructive path replay; selective independent reconstruction pending; no mixing, phase, wave or operational quantum conclusion.',
            'rows':ROWS,'sources_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}}
    (OUT/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'groups':len(ROWS),'sources_sha256':result['sources_sha256']},indent=2))
if __name__=='__main__':main()
