#!/usr/bin/env python3
"""Selective independent trace/congestion/Green/killing checks; no author imports.

Reuses only the earlier sealed independent matching/marked-slide implementation.
All matrix equalities designated exact use SymPy rationals. Eigenvalues and
logarithmic upper bounds are numerical controls, not substitutes for proofs.
"""
from pathlib import Path
from collections import Counter, defaultdict
import datetime, hashlib, importlib.util, itertools, json, math, sys, time
import numpy as np
import sympy as sp

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
RAW = HERE.parent
PREVIOUS = RAW / 'geometric_general_graph_independent/independent_check.py'
spec = importlib.util.spec_from_file_location('sealed_matching_control', PREVIOUS)
old = importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)

def dump(name, value):
    (HERE/name).write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def assemble(vertices, edges):
    edges = set(tuple(sorted(e)) for e in edges)
    K = vertices//2
    near = old.matchings(vertices, edges, K-1)
    full = old.matchings(vertices, edges, K)
    assert full and old.connected(vertices, edges)
    graph = old.slide_graph(vertices, edges, near)
    assert len(old.distances(graph, 0)) == len(near)
    n, Z = len(near), len(full)
    L = sp.zeros(n)
    for u, ns in enumerate(graph):
        L[u,u] = len(ns)
        for v in ns: L[u,v] = -1
    A = sp.Matrix([[int(set(M)<set(F)) for F in full] for M in near])
    h = A*sp.ones(Z,1)
    assert set(h) <= {0,1} and A.T*sp.ones(n,1) == K*sp.ones(Z,1)
    H = sp.diag(*h)
    B = (L+H).row_join(-A).col_join((-A.T).row_join(K*sp.eye(Z)))
    T = L+H-A*A.T/K
    assert B*sp.ones(n+Z,1) == sp.zeros(n+Z,1)
    assert T*sp.ones(n,1) == sp.zeros(n,1)
    assert T == B[:n,:n]-B[:n,n:]*B[n:,n:].inv()*B[n:,:n]
    # Independently assemble the uniform-edge, one-half-lazy proposal chain.
    states = near+full
    indices = {M:i for i,M in enumerate(states)}
    P = sp.zeros(n+Z)
    for u, M in enumerate(states):
        partners = old.partner(vertices,M)
        P[u,u] += sp.Rational(1,2)
        for a,b in sorted(edges):
            target = M
            if len(M)==K and (a,b) in M:
                target=old.canonical(set(M)-{(a,b)})
            elif len(M)==K-1:
                if partners[a]<0 and partners[b]<0:
                    target=old.canonical((*M,(a,b)))
                elif (partners[a]<0) != (partners[b]<0):
                    vacant, occupied = (a,b) if partners[a]<0 else (b,a)
                    target=old.canonical((set(M)-{old.edge(occupied,partners[occupied])})|{(a,b)})
            P[u,indices[target]] += sp.Rational(1,2*len(edges))
    assert P == sp.eye(n+Z)-B/(2*len(edges))
    return {'vertices':vertices,'edges':edges,'K':K,'near':near,'full':full,'graph':graph,
            'n':n,'Z':Z,'L':L,'A':A,'h':h,'H':H,'B':B,'T':T,'P':P}

def exact_conductance(P):
    size=P.rows
    best=None
    for count in range(1,size//2+1):
        for sub in itertools.combinations(range(size),count):
            left=set(sub)
            flux=sum(P[u,v] for u in left for v in range(size) if v not in left)/count
            if best is None or flux<best: best=flux
    return best

def route_check(data):
    n,K=data['n'],data['K']
    adj=old.neighbors(data['vertices'],data['edges'])
    where={M:i for i,M in enumerate(data['near'])}
    references=defaultdict(set); loads=Counter(); lengths=Counter(); routed=0
    sample_two=None
    for F in data['full']:
        for e,f in itertools.permutations(F,2):
            start=old.canonical(set(F)-{e})
            tracker=old.Tracked(data['vertices'],adj,start)
            old.transport(tracker,F,e,f)
            assert tracker.m==old.canonical(set(F)-{f})
            sequence=[where[start]];state=start
            for op in tracker.ops:
                state=old.slide_geometry(state,op);sequence.append(where[state])
            microedges=[tuple(sorted(q)) for q in zip(sequence,sequence[1:])]
            assert len(microedges)==len(set(microedges))
            assert len(sequence)==len(set(sequence))
            assert len(microedges)<=2*(K-1)
            for q in microedges:
                assert q[1] in data['graph'][q[0]]
                references[q].add(F);loads[q]+=1
            lengths[len(microedges)]+=1;routed+=1
    for q,fs in references.items():
        assert len(fs)<=2
        assert loads[q]<=2*K*K
        # The two candidate references are recovered only from endpoint holes.
        candidates=set()
        for endpoint in q:
            M=data['near'][endpoint]
            holes=[x for x,p in enumerate(old.partner(data['vertices'],M)) if p<0]
            e=tuple(holes)
            if e in data['edges']: candidates.add(old.canonical((*M,e)))
        assert fs<=candidates
        if len(fs)==2 and sample_two is None:
            sample_two={'microedge':[data['near'][q[0]],data['near'][q[1]]],
                        'reference_perfect_matchings':sorted(fs),'path_load':loads[q]}
    return {'routes':routed,'length_histogram':dict(sorted(lengths.items())),
            'max_reference_count':max(map(len,references.values()),default=0),
            'max_ordered_path_load':max(loads.values(),default=0),
            'load_bound':2*K*K,'two_reference_witness':sample_two}

def positive_gap(matrix):
    vals=np.linalg.eigvalsh(np.array(matrix,dtype=float))
    assert abs(vals[0])<1e-9 and vals[1]>1e-9
    return float(vals[1])

def matrix_checks(data):
    n,Z,K=data['n'],data['Z'],data['K']
    L,T,B=data['L'],data['T'],data['B']
    Pi=sp.ones(n)/n
    Green=(L+Pi).inv()-Pi
    assert L*Green==sp.eye(n)-Pi and Green*sp.ones(n,1)==sp.zeros(n,1)
    gap=positive_gap(L);gt=positive_gap(T);gb=positive_gap(B)
    C=1+2*K*(K-1)
    assert gt+1e-10>=gb and C*gap+1e-10>=gt
    least=float(np.linalg.eigvalsh(np.array(C*L-T,dtype=float))[0])
    assert least>=-1e-9
    R=sp.Rational(n,Z)
    lower=sp.Rational(1,256*len(data['edges'])*R**4*C)
    assert gap>=float(lower)
    green_norm=max(sum(abs(Green[i,j]) for j in range(n)) for i in range(n))
    TG=(1+math.log(n))/gap
    assert float(green_norm)<=TG+1e-10
    harmonic=data['A'].T/K
    for shift in [0,3]:
        f=sp.Matrix([((i+shift)**2%13)-4 for i in range(n)])
        ext=f.col_join(harmonic*f)
        assert (ext.T*B*ext)[0]/(n+Z)==(f.T*T*f)[0]/(n+Z)
        variance_full=(ext.dot(ext)/(n+Z)-(sum(ext)/(n+Z))**2)
        variance_near=(f.dot(f)/n-(sum(f)/n)**2)
        assert variance_full>=sp.Rational(n,n+Z)*variance_near
    conductance=None
    if n+Z<=12:
        conductance=exact_conductance(data['P'])
        assert conductance>=sp.Rational(1,16*len(data['edges'])*R**2)
        assert gb/(2*len(data['edges']))+1e-12>=float(conductance**2/2)
    return {'gap_slide':gap,'gap_trace':gt,'gap_broder':gb,
            'claimed_gap_lower':str(lower),'trace_form_comparison_min_eigenvalue':least,
            'centered_Green_exact_infinity_norm':str(green_norm),'TG':TG,
            'conductance_exact':str(conductance) if conductance is not None else None},Green,TG

def killing_checks(data,Green,TG):
    n,Z=data['n'],data['Z'];L,H,A=data['L'],data['H'],data['A']
    p=sp.Rational(sum(data['h']),n)
    rows=[]
    for beta in [sp.Rational(1,10000),sp.Rational(1,300),sp.Rational(1,10),sp.Integer(1)]:
        exit_matrix=(L+beta*H).inv()*(beta*A)
        assert exit_matrix*sp.ones(Z,1)==sp.ones(n,1)
        assert min(exit_matrix)>=0
        tv=max(sum(abs(exit_matrix[i,j]-sp.Rational(1,Z)) for j in range(Z))/2 for i in range(n))
        assert float(tv)<=min(1,2*float(beta)*TG)+1e-12
        z=beta*p*(L+beta*H).inv()*sp.ones(n,1)
        assert sum(data['h'][i]*z[i] for i in range(n))/n==p
        err=max(abs(x-1) for x in z)
        mean_bound=None
        if 2*float(beta)*TG<1:
            mean_bound=2*float(beta)*TG/(1-2*float(beta)*TG)
            assert float(err)<=mean_bound+1e-12
        transform_errors={}
        # Exhaust all full-geometry events when Z is small.
        for lam in [sp.Rational(1,2),sp.Integer(2)]:
            U=(L+beta*(H+lam*p*sp.eye(n))).inv()*(beta*A)
            bound=float(beta)*TG*(1+float(lam*p))*(1+1/(1+float(lam)))
            largest=sp.Integer(0)
            for mask in range(1<<Z):
                D=[j for j in range(Z) if mask>>j&1]
                for i in range(n):
                    value=abs(sum(U[i,j] for j in D)-sp.Rational(len(D),Z)/(1+lam))
                    largest=max(largest,value)
            assert float(largest)<=bound+1e-12
            transform_errors[str(lam)]=str(largest)
        rows.append({'beta':str(beta),'max_exit_TV_exact':str(tv),'scaled_mean_error_exact':str(err),
                     'mean_bound':mean_bound,'joint_event_Laplace_errors_exact':transform_errors})
    if p==1:
        beta,lam=sp.symbols('beta lam',positive=True)
        assert (L+beta*H)*sp.ones(n,1)==beta*sp.ones(n,1)
        # Constant hazard -> exact exponential clock from every entrance law.
        assert (L+beta*(H+lam*sp.eye(n)))*(sp.ones(n,1)/(1+lam))==beta*sp.ones(n,1)
    return {'p':str(p),'checks':rows,'constant_hazard_exact_clock':p==1}

def run():
    graphs={
        'path4':(4,[(0,1),(1,2),(2,3)]),
        'cycle4':(4,[(0,1),(1,2),(2,3),(0,3)]),
        'diamond':(4,[(0,1),(0,2),(1,2),(0,3),(1,3)]),
        'complete4':(4,list(itertools.combinations(range(4),2))),
        'path6':(6,[(i,i+1) for i in range(5)]),
        'cycle6':(6,[(i,(i+1)%6) for i in range(6)]),
        'triangles_with_bridge':(6,[(0,1),(1,2),(0,2),(3,4),(4,5),(3,5),(2,3)]),
        'K33':(6,[(i,j) for i in range(3) for j in range(3,6)]),
        'squares_with_bridge':(8,[(0,1),(1,2),(2,3),(0,3),(4,5),(5,6),(6,7),(4,7),(3,4)]),
        'cube':(8,[(x,x^(1<<i)) for x in range(8) for i in range(3) if x<(x^(1<<i))]),
        'complete6':(6,list(itertools.combinations(range(6),2))),
    }
    output=[];two_reference=[]
    for name,(v,edges) in graphs.items():
        data=assemble(v,edges)
        route=route_check(data)
        matrices,green,TG=matrix_checks(data)
        killing=killing_checks(data,green,TG) if data['n']<=18 and data['Z']<=6 else None
        if route['two_reference_witness']: two_reference.append(name)
        # A false trace that omits self-return subtraction loses zero row sums.
        wrong=data['L']+data['H']-(data['A']*data['A'].T-sp.diag(*data['h']))/data['K']
        assert wrong*sp.ones(data['n'],1)==data['h']/data['K']
        row={'name':name,'vertices':v,'edges':sorted(data['edges']),'near':data['n'],'full':data['Z'],
             'bipartite':old.is_bipartite(v,data['edges']),'route':route,'matrices':matrices,'killing':killing}
        output.append(row)
        print(name,json.dumps({'near':data['n'],'full':data['Z'],'routes':route['routes'],'gap':matrices['gap_slide']}),flush=True)
    assert two_reference, 'A one-reference congestion claim should be falsified by these fixtures'
    K,d=sp.symbols('K d',positive=True)
    denominator=sp.simplify(256*(2*d*K)*(K**2/(2*d))**4*(2*K**2))
    assert denominator==64*K**11/d**3
    return {'status':'all independent controls passed','graphs':output,
            'two_reference_countercontrols':two_reference,
            'torus_gap_denominator_exact':str(denominator),
            'statement_limits':['Eigenvalues and logarithmic bound comparisons are floating controls; matrix identities and displayed rational killing values are exact.',
                                'Published conductance and monomer theorems are imported, not reproved.',
                                'No author checker/results or production trajectories accessed.']}

if __name__=='__main__':
    started=time.monotonic()
    result=run();result.update(elapsed_seconds=time.monotonic()-started,
        checker_sha256=sha(__file__),reused_independent_checker_sha256=sha(PREVIOUS),
        completed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
    dump('INDEPENDENT_RESULTS.json',result)
    print('complete',json.dumps({'graphs':len(result['graphs']),'seconds':result['elapsed_seconds']}),flush=True)
