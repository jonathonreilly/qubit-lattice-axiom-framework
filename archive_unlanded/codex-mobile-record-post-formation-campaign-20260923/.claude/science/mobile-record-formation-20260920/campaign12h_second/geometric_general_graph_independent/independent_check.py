#!/usr/bin/env python3
"""Independent near-perfect matching enumeration and constructive marked slide proof.
Does not import the author checker or read its outputs. No production data access.
"""
from pathlib import Path
from collections import deque,Counter
import datetime,hashlib,itertools,json,random,sys,time
import sympy as sp
EVIDENCE=Path(__file__).resolve().parent
SRC=EVIDENCE.parent
OUT=EVIDENCE
NOTE_SHA='70af6469a0e81cbb592ae710eaac07a61912d9754bc98d277ffbf5023301a959'

def edge(a,b):return (a,b) if a<b else (b,a)
def canonical(m):return tuple(sorted(m))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(name,obj): (OUT/name).write_text(json.dumps(obj,indent=2,allow_nan=False)+'\n')
def neighbors(n,edges):
    a=[set() for _ in range(n)]
    for u,v in edges:a[u].add(v);a[v].add(u)
    return a

def connected(n,edges):
    adj=neighbors(n,edges);seen={0};stack=[0]
    while stack:
        for v in adj[stack.pop()]-seen:seen.add(v);stack.append(v)
    return len(seen)==n

def is_bipartite(n,edges):
    a=neighbors(n,edges);colors={}
    for root in range(n):
        if root in colors:continue
        colors[root]=0;queue=[root]
        for u in queue:
            for v in a[u]:
                if v not in colors:colors[v]=1-colors[u];queue.append(v)
                elif colors[v]==colors[u]:return False
    return True

def matchings(n,edges,k):
    adj=neighbors(n,edges)
    def rec(left,need):
        if need==0:yield ();return
        if len(left)<2*need:return
        a=min(left);rest=left-{a}
        if len(rest)>=2*need:yield from rec(rest,need)
        for b in sorted(adj[a]&rest):
            for tail in rec(rest-{b},need-1):yield canonical((edge(a,b),*tail))
    return tuple(sorted(rec(set(range(n)),k)))

def partner(n,m):
    ans=[-1]*n
    for u,v in m:assert ans[u]<0 and ans[v]<0;ans[u]=v;ans[v]=u
    return ans

def actions(n,adj,m):
    p=partner(n,m);out=[]
    for a in range(n):
        if p[a]>=0:continue
        for b in sorted(adj[a]):
            c=p[b]
            if c>=0:out.append(((a,b,c),canonical((set(m)-{edge(b,c)})|{edge(a,b)})))
    assert len({target for op,target in out})==len(out)
    return out

def slide_geometry(m,op):
    a,b,c=op;return canonical((set(m)-{edge(b,c)})|{edge(a,b)})

def prepare(n,adj,m,reference):
    diff=set(m)^set(reference);a=neighbors(n,diff);p=partner(n,m);holes=[u for u in range(n) if p[u]<0]
    path=[holes[0]];prev=-1
    while path[-1]!=holes[1]:
        options=a[path[-1]]-{prev};assert len(options)==1
        nxt=next(iter(options));prev=path[-1];path.append(nxt)
    assert len(path)%2==0
    state=m;ops=[]
    for j in range(0,len(path)-2,2):
        op=tuple(path[j:j+3]);assert op[0] in [u for u in range(n) if partner(n,state)[u]<0]
        assert edge(op[1],op[2]) in state and op[1] in adj[op[0]]
        state=slide_geometry(state,op);ops.append(op)
    missing=edge(path[-2],path[-1]);full=canonical((*state,missing))
    assert len(full)==n//2 and all(v>=0 for v in partner(n,full))
    assert len(ops)<=n//2-1
    return state,full,missing,ops

def cycles(n,f,g):
    diff=set(f)^set(g);left=set(v for e in diff for v in e);pf=partner(n,f);pg=partner(n,g);ans=[]
    while left:
        start=min(left);vertices=[start];current=start;which=0
        while True:
            nxt=(pf if which==0 else pg)[current];which^=1
            if nxt==start:break
            assert nxt not in vertices;vertices.append(nxt);current=nxt
        assert len(vertices)>=4 and len(vertices)%2==0
        left-=set(vertices);ans.append(vertices)
    return ans

class Tracked:
    def __init__(self,n,adj,m):
        self.n=n;self.adj=adj;self.m=m;self.labels=[-1]*n;self.ops=[];self.checks=0
        for j,(u,v) in enumerate(m):self.labels[u]=2*j;self.labels[v]=2*j+1
        self.validate()
    def validate(self):
        assert len(self.m)==self.n//2-1
        p=partner(self.n,self.m)
        assert sorted(v for v in self.labels if v>=0)==list(range(self.n-2))
        for u in range(self.n):
            if p[u]<0:assert self.labels[u]<0
            else:assert (self.labels[u]^self.labels[p[u]])==1 and p[u] in self.adj[u]
        self.checks+=1
    def slide(self,op):
        a,b,c=op;p=partner(self.n,self.m)
        assert len({a,b,c})==3 and p[a]<0 and p[b]==c and b in self.adj[a]
        before=self.labels.copy();self.labels[a]=before[b];self.labels[b]=before[c];self.labels[c]=-1
        self.m=slide_geometry(self.m,op);self.ops.append(op);self.validate()
        # Every record which moved did so across exactly one graph edge.
        before_pos={r:i for i,r in enumerate(before) if r>=0};after_pos={r:i for i,r in enumerate(self.labels) if r>=0}
        for r,u in before_pos.items():assert after_pos[r]==u or after_pos[r] in self.adj[u]


def transport(tracked,full,missing,target):
    assert tracked.m==canonical(set(full)-{missing})
    if missing==target:return missing
    pf=partner(tracked.n,full);parent={missing:None};bridge={};queue=deque([missing])
    while queue and target not in parent:
        q=queue.popleft()
        for a in q:
            for b in sorted(tracked.adj[a]):
                f=edge(b,pf[b])
                if f not in parent:parent[f]=q;bridge[f]=(a,b);queue.append(f)
    assert target in parent
    route=[];q=target
    while q!=missing:route.append((q,bridge[q]));q=parent[q]
    route.reverse();before=len(tracked.ops)
    for f,(a,b) in route:
        aprime=pf[a];bprime=pf[b]
        assert edge(a,aprime)==missing
        tracked.slide((a,b,bprime));tracked.slide((aprime,a,b));missing=f
        assert tracked.m==canonical(set(full)-{missing})
    assert len(tracked.ops)-before<=2*(tracked.n//2-1)
    return missing


def construct(n,edges,start,target,reference,keep_trace=False):
    adj=neighbors(n,edges);tracked=Tracked(n,adj,start)
    u,full,missing,start_ops=prepare(n,adj,start,reference)
    v,goal_full,goal_missing,target_ops=prepare(n,adj,target,reference)
    for op in start_ops:tracked.slide(op)
    assert tracked.m==u
    cs=cycles(n,full,goal_full)
    for vertices in cs:
        first=edge(vertices[0],vertices[1]);missing=transport(tracked,full,missing,first)
        for j in range(1,len(vertices)//2):tracked.slide(tuple(vertices[2*j-1:2*j+2]))
        cycle_edges={edge(vertices[j],vertices[(j+1)%len(vertices)]) for j in range(len(vertices))}
        full=canonical(set(full)^cycle_edges);missing=edge(vertices[-1],vertices[0])
        assert tracked.m==canonical(set(full)-{missing})
    assert full==goal_full
    missing=transport(tracked,full,missing,goal_missing)
    assert tracked.m==v
    for a,b,c in reversed(target_ops):tracked.slide((c,b,a))
    assert tracked.m==target
    K=n//2;bound=K*K+4*K
    assert len(tracked.ops)<=bound
    assert len(tracked.ops)<=K*K+4*K-4
    result={'length':len(tracked.ops),'bound':bound,'cycles_used':len(cs),'record_invariant_checks':tracked.checks}
    if keep_trace:
        replay=Tracked(n,adj,start);trace=[{'matching':replay.m,'record_positions':replay.labels.copy()}]
        for op in tracked.ops:
            replay.slide(op);trace.append({'slide':op,'matching':replay.m,'record_positions':replay.labels.copy()})
        result.update(start=start,target=target,reference=reference,trace=trace)
    return result


def slide_graph(n,edges,states):
    adj=neighbors(n,edges);where={m:i for i,m in enumerate(states)};a=[]
    for m in states:a.append({where[z] for op,z in actions(n,adj,m)})
    assert all(i in a[j] for i,ns in enumerate(a) for j in ns)
    return a

def distances(a,start):
    d={start:0};queue=deque([start])
    while queue:
        u=queue.popleft()
        for v in a[u]:
            if v not in d:d[v]=d[u]+1;queue.append(v)
    return d

def components(a):
    unseen=set(range(len(a)));sizes=[]
    while unseen:
        seen=set(distances(a,min(unseen)));sizes.append(len(seen));unseen-=seen
    return sorted(sizes)


def graph_check(n,edges,paths=False):
    full=matchings(n,edges,n//2);near=matchings(n,edges,n//2-1);assert full
    graph=slide_graph(n,edges,near);assert len(distances(graph,0))==len(near)
    pcount=0;pred=Counter()
    for m in near:
        pm=partner(n,m);h=[u for u in range(n) if pm[u]<0]
        if edge(*h) in edges:pcount+=1;pred[canonical((*m,edge(*h)))]+=1
    assert set(pred)==set(full) and set(pred.values())=={n//2}
    assert pcount==(n//2)*len(full)
    constructions=[]
    pairs=itertools.product(near,near) if paths and len(near)<=120 else [(near[0],near[-1]),(near[len(near)//2],near[0])]
    for s,t in pairs:constructions.append(construct(n,edges,s,t,full[0]))
    diameter=max(max(distances(graph,i).values()) for i in range(len(near))) if paths else None
    if diameter is not None:assert diameter<=(n//2)**2+4*(n//2)
    return {'n':n,'edges':len(edges),'full_matchings':len(full),'near_matchings':len(near),'bipartite':is_bipartite(n,edges),'exact_slide_diameter':diameter,
            'constructive_paths':len(constructions),'longest_constructed_path':max(c['length'] for c in constructions),'alternating_cycles_used':sum(c['cycles_used'] for c in constructions),
            'eligible_near_states':pcount,'uniform_clock_rate':str(sp.Rational(pcount,len(near)))}


def exhaustive_small():
    summary=[];start=time.monotonic()
    for n in [2,4,6]:
        potential=list(itertools.combinations(range(n),2));counts=Counter();max_path=0;cyc=0
        for mask in range(1<<len(potential)):
            es={e for i,e in enumerate(potential) if mask>>i&1}
            if not connected(n,es):continue
            counts['connected_graphs']+=1
            fs=matchings(n,es,n//2)
            if not fs:continue
            z=graph_check(n,es,paths=False)
            counts['connected_graphs_with_perfect_matching']+=1
            counts['nonbipartite_covered']+=not z['bipartite']
            counts['near_states_checked']+=z['near_matchings']
            counts['constructive_paths_checked']+=z['constructive_paths']
            max_path=max(max_path,z['longest_constructed_path']);cyc+=z['alternating_cycles_used']
        row={'n':n,**dict(counts),'longest_constructed_path':max_path,'alternating_cycles_used':cyc};summary.append(row)
        print('exhaustive',json.dumps(row),flush=True)
    return {'rows':summary,'elapsed_seconds':time.monotonic()-start}


def named_graphs():
    out={}
    def add(name,n,es):out[name]=(n,{edge(*e) for e in es})
    for n in [4,6,8,10]:add(f'path_{n}',n,[(u,u+1) for u in range(n-1)])
    for n in [4,6,8]:add(f'cycle_{n}',n,[(u,(u+1)%n) for u in range(n)])
    add('diamond',4,[(0,1),(0,2),(1,2),(0,3),(1,3)])
    add('two_odd_triangles_with_mandatory_bridge',6,[(0,1),(1,2),(2,0),(3,4),(4,5),(5,3),(2,3)])
    add('two_even_squares_with_never_full_bridge',8,[(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(3,4)])
    add('complete_6',6,itertools.combinations(range(6),2))
    add('two_by_four_grid',8,[(i,i+4) for i in range(4)]+[(u,u+1) for u in [0,1,2,4,5,6]])
    add('petersen',10,[(i,(i+1)%5) for i in range(5)]+[(i,i+5) for i in range(5)]+[(i+5,(i+2)%5+5) for i in range(5)])
    rng=random.Random(44210921)
    for n in [8,10]:
        for j in range(8):
            es={edge(i,i+1) for i in range(0,n,2)}|{edge(i,i+1) for i in range(n-1)}
            for e in itertools.combinations(range(n),2):
                if rng.random()<.21:es.add(e)
            add(f'irregular_seeded_n{n}_{j}',n,es)
    return out


def exact_clock():
    n=4;es={(0,1),(0,2),(1,2),(0,3),(1,3)};near=matchings(n,es,1);full=matchings(n,es,2);adj=slide_graph(n,es,near)
    Q=sp.zeros(len(near));R=sp.zeros(len(near),len(full))
    for i,ns in enumerate(adj):
        for j in ns:Q[i,j]=1
        Q[i,i]=-len(ns)
        holes=[u for u,v in enumerate(partner(n,near[i])) if v<0]
        if edge(*holes) in es:R[i,full.index(canonical((*near[i],edge(*holes))))]=1
    h=R*sp.ones(len(full),1);H=sp.diag(*h);b,s=sp.symbols('beta s',positive=True)
    mean=(b*H-Q).inv()*sp.ones(len(near),1);exit_matrix=(b*H-Q).inv()*b*R
    laplace=(s*b*sp.eye(len(near))-Q+b*H).inv()*b*R
    limits=laplace.applyfunc(lambda x:sp.simplify(sp.limit(x,b,0)))
    assert all(x==2/(5*s+4) for x in limits)
    for i,m in enumerate(near):
        if m==((0,1),):assert sp.simplify(mean[i]-5/(4*b)-sp.Rational(1,4))==0
        else:assert sp.simplify(mean[i]-5/(4*b))==0
        assert sum(exit_matrix[i,:])==1 or sp.simplify(sum(exit_matrix[i,:])-1)==0
        for j in range(2):assert sp.limit(exit_matrix[i,j],b,0)==sp.Rational(1,2)
    # A fixed extra symmetric geometric move must leave the rare limit unchanged.
    Qextra=Q.copy();Qextra[0,4]+=sp.Rational(7,3);Qextra[4,0]+=sp.Rational(7,3);Qextra[0,0]-=sp.Rational(7,3);Qextra[4,4]-=sp.Rational(7,3)
    extra=(b*H-Qextra).inv()*b*R
    assert all(sp.limit(x,b,0)==sp.Rational(1,2) for x in extra)
    return {'graph':'diamond','near_matchings':near,'full_matchings':full,'Q':[[str(x) for x in Q.row(i)] for i in range(len(near))],
            'h':[int(x) for x in h],'mean':list(map(str,mean.applyfunc(sp.factor))),'finite_beta_exit':[[str(sp.factor(x)) for x in exit_matrix.row(i)] for i in range(len(near))],
            'joint_scaled_laplace_limits':[[str(x) for x in limits.row(i)] for i in range(len(near))],
            'beta_one_exit':[[str(x.subs(b,1)) for x in exit_matrix.row(i)] for i in range(len(near))],
            'symmetric_extra_channel_rare_exit_checked':True,'clock_rate':'4/5'}


def countercontrols():
    # Disconnected edge plus square: two full-square choices remain frozen when holes lie on the isolated edge.
    n=6;es={(0,1),(2,3),(3,4),(4,5),(2,5)};near=matchings(n,es,2);full=matchings(n,es,3)
    sizes=components(slide_graph(n,es,near));assert sizes==[1,1,4]
    isolated=[m for m in near if len(actions(n,neighbors(n,es),m))==0];assert len(isolated)==2
    # A connected no-perfect-matching graph cannot have a full birth exit.
    star={(0,1),(0,2),(0,3)};star_near=matchings(4,star,1);assert not matchings(4,star,2)
    assert all(edge(*[u for u,v in enumerate(partner(4,m)) if v<0]) not in star for m in star_near)
    # Marked states of one prescribed pair on P4 have two orientation components.
    path={(0,1),(1,2),(2,3)};states=[(u,v) for e in sorted(path) for u,v in [e,e[::-1]]];where={x:i for i,x in enumerate(states)};adj=neighbors(4,path);matrix=[]
    for R,S in states:
        ns=set()
        for a in set(range(4))-{R,S}:
            if R in adj[a]:ns.add(where[(a,R)])
            if S in adj[a]:ns.add(where[(S,a)])
        matrix.append(ns)
    marked=components(matrix);assert marked==[3,3]
    return {'disconnected_edge_plus_square':{'near_components':sizes,'full_matchings':len(full),'two_singletons_exit_deterministically_to_different_full_states':True},
            'connected_star_without_perfect_matching':{'near_states':len(star_near),'birth_eligible_states':0,'full_matchings':0},
            'path4_marked':{'marked_components':marked,'geometric_components':[3]}}


def main():
    global OUT
    if len(sys.argv)==3 and sys.argv[1]=='--output':
        OUT=Path(sys.argv[2]).resolve();assert OUT.is_relative_to(EVIDENCE) and OUT!=EVIDENCE;OUT.mkdir(parents=True,exist_ok=False)
    elif len(sys.argv)!=1:raise SystemExit('usage: independent_check.py [--output NEW_CHILD_DIRECTORY]')
    elif (OUT/'RESULTS.json').exists():raise SystemExit('preserved results exist; use a new --output directory')
    assert sha(SRC/'GEOMETRIC_TWO_VACANCY_GENERAL_GRAPH.md')==NOTE_SHA
    start=datetime.datetime.now(datetime.timezone.utc).isoformat();exhaustive=exhaustive_small()
    named={};spec=named_graphs()
    for name,(n,es) in spec.items():
        named[name]=graph_check(n,es,paths=True);print('named',name,json.dumps(named[name]),flush=True)
    n,es=spec['two_even_squares_with_never_full_bridge'];F=canonical([(0,1),(2,3),(4,5),(6,7)])
    M=canonical(set(F)-{(4,5)});T=canonical([(0,3),(1,2),(6,7)])
    bridge=construct(n,es,M,T,F,keep_trace=True);assert bridge['cycles_used']==1
    assert any((3,4) in {edge(a,b),edge(b,c)} for a,b,c in [step['slide'] for step in bridge['trace'][1:]])
    save('BRIDGE_EXCURSION.json',bridge)
    clock=exact_clock();save('EXACT_CLOCK.json',clock)
    counters=countercontrols();save('COUNTERCONTROLS.json',counters)
    result={'scope':'Pre-author-checker independent finite geometry and exact killed-chain controls; no production values or mixing comparison read.',
            'started_utc':start,'finished_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_note_sha256':NOTE_SHA,
            'exhaustive_labeled_small_graphs':exhaustive,'named_graphs':named,'named_graph_definitions':{name:{'n':n,'edges':sorted(es)} for name,(n,es) in spec.items()},
            'bridge_cycle_excursion_length':bridge['length'],'diamond_clock_rate':clock['clock_rate'],'countercontrols':counters,'open_findings':[]}
    save('RESULTS.json',result)
    print('COMPLETE',json.dumps({'exhaustive_graphs':sum(x['connected_graphs_with_perfect_matching'] for x in exhaustive['rows']),'named_graphs':len(named),'open_findings':[]}))

if __name__=='__main__':main()
