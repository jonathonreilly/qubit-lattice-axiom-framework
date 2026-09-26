#!/usr/bin/env python3
"""Independent all-stage corridor, connectivity, injection and matrix checks.
Only imports the earlier sealed independent matching enumerator/slide actions.
No new author checker or outputs are accessed.
"""
from pathlib import Path
from collections import deque,Counter,defaultdict
import datetime,hashlib,importlib.util,itertools,json,math,sys,time
import numpy as np
import sympy as sp
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent;RAW=HERE.parent
PRIOR=RAW/'geometric_general_graph_independent/independent_check.py'
spec=importlib.util.spec_from_file_location('previous_independent_matching',PRIOR)
old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
edge=old.edge;canon=old.canonical
def save(name,data):(HERE/name).write_text(json.dumps(data,indent=2,allow_nan=False)+'\n')
def identity(p):
    p=Path(p);return {'path':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}

class Marked:
    def __init__(self,V,adj,M):
        self.V=V;self.adj=adj;self.M=M;self.j=len(M);self.labels=[-1]*V;self.ops=[]
        for i,(u,v) in enumerate(M):self.labels[u]=2*i;self.labels[v]=2*i+1
        self.verify()
    def verify(self):
        assert len(self.M)==self.j
        p=old.partner(self.V,self.M)
        assert sorted(x for x in self.labels if x>=0)==list(range(2*self.j))
        for u in range(self.V):
            if p[u]<0:assert self.labels[u]<0
            else:assert p[u] in self.adj[u] and self.labels[u]^self.labels[p[u]]==1
    def slide(self,op):
        a,b,c=op;p=old.partner(self.V,self.M)
        assert len({a,b,c})==3 and p[a]<0 and p[b]==c and b in self.adj[a]
        before=self.labels.copy();self.labels[a]=before[b];self.labels[b]=before[c];self.labels[c]=-1
        self.M=canon((set(self.M)-{edge(b,c)})|{edge(a,b)});self.ops.append(op);self.verify()
        for r in range(2*self.j):
            u=before.index(r);v=self.labels.index(r);assert u==v or v in self.adj[u]

def corridor(V,edges,T,e,f):
    """BFS in quotient; move an oriented pair backwards along each empty run."""
    adj=old.neighbors(V,edges);covered={u for q in T for u in q}
    nodes=list(T)+[(u,) for u in range(V) if u not in covered]
    index={u:i for i,node in enumerate(nodes) for u in node};start=nodes.index(e);goal=nodes.index(f)
    parent={start:None};bridges={};queue=deque([start])
    while queue and goal not in parent:
        q=queue.popleft()
        for u in nodes[q]:
            for v in sorted(adj[u]):
                r=index[v]
                if r not in parent:parent[r]=q;bridges[r]=(u,v);queue.append(r)
    assert goal in parent
    path=[goal]
    while path[-1]!=start:path.append(parent[path[-1]])
    path.reverse();matched=[i for i,q in enumerate(path) if len(nodes[q])==2]
    state=Marked(V,adj,canon(set(T)-{e}));original_labels=state.labels.copy();sequence=[state.M]
    for left,right in zip(matched,matched[1:]):
        # Physical path begins at the outgoing endpoint of the absent edge.
        a=bridges[path[left+1]][0];aprime=next(u for u in nodes[path[left]] if u!=a)
        route=[a]+[bridges[path[t]][1] for t in range(left+1,right+1)]
        b=route[-1];bprime=next(u for u in nodes[path[right]] if u!=b)
        moving=(b,bprime)
        for vacancy in reversed(route[:-1]):
            state.slide((vacancy,*moving));sequence.append(state.M);moving=(vacancy,moving[0])
        state.slide((aprime,*moving));sequence.append(state.M)
        assert state.M==canon(set(T)-{nodes[path[right]]})
    assert state.M==canon(set(T)-{f})
    assert len(state.ops)<=V-2 and len(sequence)==len(set(sequence))
    ops=state.ops.copy();destination=state.M
    for a,b,c in reversed(ops):state.slide((c,b,a))
    assert state.M==canon(set(T)-{e}) and state.labels==original_labels
    return {'ops':ops,'states':sequence,'destination':destination,'length':len(ops),'quotient_path':[nodes[q] for q in path]}

def graph_laplacian(V,edges,states):
    adj=old.neighbors(V,edges);where={M:i for i,M in enumerate(states)};L=sp.zeros(len(states));graph=[]
    for i,M in enumerate(states):
        neighbors={where[target] for op,target in old.actions(V,adj,M)};graph.append(neighbors)
        L[i,i]=len(neighbors)
        for z in neighbors:L[i,z]=-1
    assert L==L.T and L*sp.ones(len(states),1)==sp.zeros(len(states),1)
    return L,graph

def augmenting_components(V,M,P):
    diff=set(M)^set(P);adj=old.neighbors(V,diff);remaining={u for e in diff for u in e};paths=[]
    while remaining:
        u=min(remaining);component={u};queue=[u]
        for v in queue:
            for w in adj[v]-component:component.add(w);queue.append(w)
        remaining-=component
        endpoints=[v for v in component if len(adj[v])==1]
        if endpoints:
            assert len(endpoints)==2
            paths.append(frozenset(e for e in diff if e[0] in component))
    assert len(paths)==V//2-len(M)
    return paths

def injection_check(V,layers):
    K=V//2;counts=[]
    for j in range(K):
        images={}
        for M in layers[j]:
            for P in layers[K]:
                for Q in augmenting_components(V,M,P):
                    U=canon(set(M)^Q);W=canon(set(P)^Q)
                    assert U in layers[j+1] and W in layers[K-1]
                    key=(U,W);preimage=(M,P,tuple(sorted(Q)))
                    assert key not in images;images[key]=preimage
                    holes=[v for v,q in enumerate(old.partner(V,W)) if q<0]
                    diff=set(U)^set(W);adj=old.neighbors(V,diff);seen={holes[0]};queue=[holes[0]]
                    for v in queue:
                        for z in adj[v]-seen:seen.add(z);queue.append(z)
                    assert holes[1] in seen
                    recovered={e for e in diff if e[0] in seen}
                    assert recovered==Q and canon(set(U)^recovered)==M and canon(set(W)^recovered)==P
        domain=(K-j)*len(layers[j])*len(layers[K]);codomain=len(layers[j+1])*len(layers[K-1])
        assert len(images)==domain<=codomain
        counts.append({'j':j,'domain':domain,'codomain':codomain})
    R=sp.Rational(len(layers[K-1]),len(layers[K]));C=sum(sp.Rational(len(layers[j]),(j+1)*len(layers[j+1])) for j in range(K));H=sum(sp.Rational(1,i) for i in range(1,K+1))
    assert R/K<=C<=2*R*H/(K+1)
    return {'injective_maps':counts,'C_exact':str(C),'lower_exact':str(R/K),'upper_exact':str(2*R*H/(K+1))}

def exchange_laplacian(states):
    L=sp.zeros(len(states))
    for i,M in enumerate(states):
        for z in range(i):
            if len(set(M)^set(states[z]))==2:
                L[i,i]+=1;L[z,z]+=1;L[i,z]-=1;L[z,i]-=1
    return L

def two_level_check(V,edges,j,layers):
    k=j+1;near=layers[j];upper=layers[k];n,q=len(near),len(upper)
    L,graph=graph_laplacian(V,edges,near);assert len(old.distances(graph,0))==n
    A=sp.Matrix([[int(set(M)<set(T)) for T in upper] for M in near]);h=A*sp.ones(q,1);H=sp.diag(*h)
    assert A.T*sp.ones(n,1)==k*sp.ones(q,1)
    lower_exchange=exchange_laplacian(near);upper_exchange=exchange_laplacian(upper)
    U=k*H-A*A.T
    assert lower_exchange==L+U
    LB=(lower_exchange+H).row_join(-A).col_join((-A.T).row_join(upper_exchange+k*sp.eye(q)))
    extend=sp.eye(n).col_join(A.T/k)
    cross=H-A*A.T/k
    assert cross==U/k
    upper_energy=A*upper_exchange*A.T/(k*k)
    compressed=extend.T*LB*extend
    assert compressed==L+U+U/k+upper_energy
    upper_psd=float(np.linalg.eigvalsh(np.array(2*len(edges)*U/k-upper_energy,dtype=float))[0]);assert upper_psd>-1e-8
    C=1+(V-2)*(len(edges)+len(edges)**2)*(k-1)*(k+1+2*len(edges))
    psd=float(np.linalg.eigvalsh(np.array(C*L-compressed,dtype=float))[0]);assert psd>-1e-7
    gs=float(np.linalg.eigvalsh(np.array(L,dtype=float))[1]);gb=float(np.linalg.eigvalsh(np.array(LB,dtype=float))[1]);assert gs>=gb/C-1e-10
    p=sp.Rational(sum(h),n);B=(1+math.log(n))/gs
    route_refs=defaultdict(set);loads=Counter();paths=0;maxlen=0;where={M:i for i,M in enumerate(near)}
    for T in upper:
        for e,f in itertools.combinations(T,2):
            route=corridor(V,edges,T,e,f);maxlen=max(maxlen,route['length']);paths+=1
            micro=[tuple(sorted((where[a],where[b]))) for a,b in zip(route['states'],route['states'][1:])]
            assert len(micro)==len(set(micro))
            for key in micro:route_refs[key].add(T);loads[key]+=1
    ref_bound=2*(len(edges)+len(edges)**2);load_bound=(len(edges)+len(edges)**2)*k*(k-1)
    assert max(map(len,route_refs.values()),default=0)<=ref_bound and max(loads.values(),default=0)<=load_bound
    exact_killing=[]
    if n<=12:
        Pi=sp.ones(n)/n;G=(L+Pi).inv()-Pi
        assert L*G==sp.eye(n)-Pi
        for beta in [sp.Rational(1,1000),sp.Rational(1,7)]:
            R=(L+beta*H).inv();exit=beta*R*A
            assert exit*sp.ones(q,1)==sp.ones(n,1) and min(exit)>=0
            tv=max(sum(abs(exit[i,t]-sp.Rational(1,q)) for t in range(q))/2 for i in range(n));assert float(tv)<=min(1,2*float(beta)*len(edges)*B)+1e-10
            z=beta*p*R*sp.ones(n,1);err=max(abs(x-1) for x in z)
            delta=float(beta)*len(edges)*B
            if delta<.5:assert float(err)<=2*delta/(1-2*delta)+1e-10
            for lam in [sp.Rational(1,2),sp.Integer(2)]:
                T=(L+beta*(H+lam*p*sp.eye(n))).inv()*beta*A
                diff=T-sp.ones(n,q)/(q*(1+lam))
                event_err=max(max(sum(max(x,0) for x in diff[i,:]),sum(max(-x,0) for x in diff[i,:])) for i in range(n))
                assert float(event_err)<=float(beta)*B*(len(edges)+float(lam*p))*(1+1/(1+float(lam)))+1e-10
            exact_killing.append({'beta':str(beta),'TV_exact':str(tv),'mean_error_exact':str(err)})
    return {'j':j,'lower_states':n,'upper_states':q,'hazard_range':[int(min(h)),int(max(h))],'p_exact':str(p),
            'slide_gap':gs,'auxiliary_gap':gb,'comparison_C':C,'compressed_comparison_min_eigenvalue':psd,'upper_energy_comparison_min_eigenvalue':upper_psd,
            'parent_routes':paths,'maximum_route_length':maxlen,'maximum_reference_count':max(map(len,route_refs.values()),default=0),'maximum_route_load':max(loads.values(),default=0),'exact_killing_controls':exact_killing}

def composed_clock(V,edges):
    """Symbolic complete growing generator via its exact successive resolvents."""
    K=V//2;layers=[old.matchings(V,edges,j) for j in range(K+1)];beta=sp.symbols('beta',positive=True)
    kernels=[];means=[];rates=[];tilted=[]
    for j in range(K):
        L,_=graph_laplacian(V,edges,layers[j]);A=sp.Matrix([[int(set(M)<set(T)) for T in layers[j+1]] for M in layers[j]])
        h=A*sp.ones(len(layers[j+1]),1);H=sp.diag(*h);p=sp.Rational(sum(h),len(layers[j]));rates.append(p)
        inv=(L+beta*H).inv();kernels.append(beta*inv*A);means.append(inv*sp.ones(len(layers[j]),1))
        s=sp.Rational(j+1,3);tilted.append((L+beta*H+beta*s*sp.eye(len(layers[j]))).inv()*beta*A)
    distribution=sp.ones(1,1);mean=0;transform=sp.ones(1,1);gated=sp.ones(1,1);target=1;gate_target=1
    for j in range(K):
        mean+= (distribution*means[j])[0];distribution=distribution*kernels[j]
        transform=transform*tilted[j]
        gate=sp.diag(*[int(i%2==0) for i in range(len(layers[j+1]))]);gated=gated*tilted[j]*gate
        s=sp.Rational(j+1,3);target*=rates[j]/(rates[j]+s)
        gate_target*=rates[j]/(rates[j]+s)*sp.Rational((len(layers[j+1])+1)//2,len(layers[j+1]))
    mean=sp.factor(beta*mean)
    mean_limit=sp.limit(mean,beta,0,dir='+');C=sum(1/p for p in rates);assert mean_limit==C
    transforms=[sp.factor(x) for x in transform];limits=[sp.limit(x,beta,0,dir='+') for x in transforms]
    assert limits==[sp.factor(target/len(layers[K]))]*len(layers[K])
    gate_value=sp.factor(sum(gated));gate_limit=sp.limit(gate_value,beta,0,dir='+');assert gate_limit==sp.factor(gate_target)
    return {'rates':[str(p) for p in rates],'scaled_total_mean_exact':str(mean),'scaled_total_mean_limit':str(mean_limit),
            'different_stage_tilt_parameters':[str(sp.Rational(j+1,3)) for j in range(K)],
            'joint_clock_and_final_geometry_exact':[str(x) for x in transforms],'joint_limits':[str(x) for x in limits],
            'postbirth_geometry_event_gate':'even enumerator indices at each stage','gated_joint_transform_exact':str(gate_value),'gated_joint_limit':str(gate_limit)}

def run():
    graphs={'path4':(4,[(i,i+1) for i in range(3)]),'cycle4':(4,[(i,(i+1)%4) for i in range(4)]),
        'diamond':(4,[(0,1),(0,2),(1,2),(0,3),(1,3)]),'path6':(6,[(i,i+1) for i in range(5)]),
        'complete6':(6,list(itertools.combinations(range(6),2))),
        'odd_barbell':(6,[(0,1),(1,2),(0,2),(3,4),(4,5),(3,5),(2,3)]),
        'triangle_tail':(6,[(0,1),(1,2),(0,2),(2,3),(3,4),(4,5)]),
        'squares_bridge':(8,[(0,1),(1,2),(2,3),(0,3),(4,5),(5,6),(6,7),(4,7),(3,4)]),
        'cube':(8,[(u,u^(1<<i)) for u in range(8) for i in range(3) if u<(u^(1<<i))]),
        'path10':(10,[(i,i+1) for i in range(9)])}
    results=[]
    for name,(V,es) in graphs.items():
        edges=set(map(lambda e:edge(*e),es));layers=[old.matchings(V,edges,j) for j in range(V//2+1)]
        assert layers[-1] and old.connected(V,edges)
        stages=[two_level_check(V,edges,j,layers) for j in range(1,V//2)]
        count=injection_check(V,layers)
        results.append({'name':name,'V':V,'edges':sorted(edges),'layer_counts':list(map(len,layers)),
                        'all_nonfull_layers_connected':True,'stages':stages,'counting':count})
        print('checked',name,'layers',list(map(len,layers)),'stages',len(stages),flush=True)
    path_edges=set((i,i+1) for i in range(9));witness=corridor(10,path_edges,((0,1),(8,9)),(0,1),(8,9));assert witness['length']==8
    save('EMPTY_CORRIDOR_WITNESS.json',witness)
    clocks={name:composed_clock(*graphs[name]) for name in ['cycle4','diamond','path6']}
    disconnected=[(0,1),(2,3)];states=old.matchings(4,disconnected,1);_,graph=graph_laplacian(4,disconnected,states)
    assert old.components(graph)==[1,1]
    star=[(0,1),(0,2),(0,3)];assert not old.matchings(4,star,2)
    return {'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'graphs':results,'symbolic_stage_composition':clocks,
            'countercontrols':{'disconnected_graph_lower_chain_components':[1,1],'star_no_perfect_matching_no_terminal_birth':True,
                               'full_level_has_no_physical_slides':True},
            'exact_control_status':'Rational matrix identities, symbolic limits, marked path/injection checks exact; spectral/PSD checks numerical.',
            'not_accessed':'New author checker and all new author outputs remain unopened.'}
if __name__=='__main__':
    assert not (HERE/'INDEPENDENT_RESULTS.json').exists()
    result=run();result['checker']=identity(Path(__file__));result['reused_independent_helper']=identity(PRIOR)
    save('INDEPENDENT_RESULTS.json',result);print('independent reconstruction checks complete',flush=True)
