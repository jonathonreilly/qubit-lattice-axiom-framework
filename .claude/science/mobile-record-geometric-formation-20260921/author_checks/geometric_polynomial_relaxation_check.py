"""Author finite matrix/routing controls for the polynomial comparison proof."""
from pathlib import Path
from itertools import combinations
from collections import defaultdict,Counter
from fractions import Fraction
import hashlib,json,math,random
import numpy as np
import sympy as sp
from geometric_general_graph_check import simple_graph,is_connected,relocate

HERE=Path(__file__).resolve().parent;OUT=HERE/'geometric_polynomial_relaxation_checks'
ROWS=[]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def report(name,**data):
    row={'name':name,'pass':True,**data};ROWS.append(row);print(json.dumps(row),flush=True)
def levels(G):
    V=len(G['sites']);K=V//2
    def layer(k):
        return sorted(frozenset(es) for es in combinations(G['edges'],k)
                      if len({u for e in es for u in e})==2*k)
    return layer(K-1),layer(K)
def matrix(G,near,full):
    """Assemble by choosing each proposed graph edge, including no-op proposals."""
    K=len(G['sites'])//2;states=near+full;idx={M:i for i,M in enumerate(states)}
    LB=np.zeros((len(states),len(states)),dtype=int)
    for i,M in enumerate(states):
        owner={u:v for e in M for u,v in (e,e[::-1])}
        for a,b in G['edges']:
            target=None
            if len(M)==K:
                if (a,b) in M:target=M-{(a,b)}
            elif a not in owner and b not in owner:target=M|{(a,b)}
            elif (a in owner)!=(b in owner):
                occupied=a if a in owner else b
                old=tuple(sorted((occupied,owner[occupied])))
                target=M-{old}|{(a,b)}
            if target is not None:
                j=idx[frozenset(target)];assert i!=j
                LB[i,i]+=1;LB[i,j]-=1
    assert np.array_equal(LB,LB.T) and not np.any(LB.sum(axis=1))
    n=len(near);A=-LB[:n,n:];h=A.sum(axis=1)
    assert set(h)<={0,1} and np.all(A.sum(axis=0)==K)
    assert np.array_equal(LB[n:,n:],K*np.eye(len(full),dtype=int))
    LS=LB[:n,:n]-np.diag(h)
    LT=LS+np.diag(h)-A@A.T/K
    assert np.max(abs(LT-(LB[:n,:n]-LB[:n,n:]@LB[n:,:n]/K)))<1e-12
    assert np.max(abs(LT.sum(axis=1)))<1e-12
    # Explicit proposal normalization: off-diagonal proposals are lazy 1/(2m).
    P=np.eye(len(states))-LB/(2*len(G['edges']))
    assert P.min()>=0 and np.min(np.diag(P))>=.5 and np.max(abs(P.sum(axis=1)-1))<1e-12
    return LS,LT,LB,A,h

def route_counts(G,near,full,LS):
    idx={M:i for i,M in enumerate(near)};K=len(G['sites'])//2
    references=defaultdict(set);use=Counter();lengths=[]
    for fnum,F in enumerate(full):
        for e in sorted(F):
            for f in sorted(F):
                M=frozenset(F-{e});target,events=relocate(M,F,e,f,G)
                assert target==F-{f};path=[]
                for a,b,c in events:
                    following=frozenset(M-{tuple(sorted((a,b)))}|{tuple(sorted((b,c)))})
                    i,j=idx[M],idx[following];assert LS[i,j]==-1
                    micro=tuple(sorted((i,j)));path.append(micro)
                    assert (M|{e}==F) or any(near[q]<=F and len(F-near[q])==1 for q in micro)
                    references[micro].add(fnum);use[micro]+=1;M=following
                assert M==target and len(set(path))==len(path) and len(path)<=2*(K-1)
                lengths.append(len(path))
    assert max(map(len,references.values()),default=0)<=2
    assert max(use.values(),default=0)<=2*K*K
    return {'routed_pairs':len(lengths),'max_length':max(lengths,default=0),
            'max_reference_matchings_per_micro_edge':max(map(len,references.values()),default=0),
            'max_micro_edge_path_count':max(use.values(),default=0)}

def positive_gap(L):
    eig=np.linalg.eigvalsh(L);assert abs(eig[0])<1e-9 and eig[1]>1e-9
    return float(eig[1])
def graph_cases():
    cases=[]
    edges=list(combinations(range(4),2))
    for mask in range(1<<len(edges)):
        G=simple_graph(4,[e for j,e in enumerate(edges) if mask>>j&1])
        if is_connected(G) and levels(G)[1]:cases.append((f'all_four_{mask}',G))
    for V in [6,8,10]:
        cases.append((f'path_{V}',simple_graph(V,[(j,j+1) for j in range(V-1)])))
        cases.append((f'cycle_{V}',simple_graph(V,[(j,(j+1)%V) for j in range(V)])))
    cases.append(('complete_six',simple_graph(6,combinations(range(6),2))))
    cases.append(('odd_barbell',simple_graph(6,[(0,1),(1,2),(2,0),(3,4),(4,5),(5,3),(2,3)])))
    cases.append(('cube',simple_graph(8,[(u,u^(1<<j)) for u in range(8) for j in range(3)])))
    rng=random.Random(2109211610)
    for V in [6,8]:
        for rep in range(40):
            E={(2*j,2*j+1) for j in range(V//2)}
            for j in range(1,V//2):
                i=rng.randrange(j);E.add(tuple(sorted((2*i+rng.randrange(2),2*j+rng.randrange(2)))))
            E.update(e for e in combinations(range(V),2) if rng.random()<.23)
            cases.append((f'random_{V}_{rep}',simple_graph(V,E)))
    return cases

def comparison_controls():
    rows=[];rng=np.random.default_rng(2109211611)
    for name,G in graph_cases():
        near,full=levels(G);K=len(G['sites'])//2;n=len(near);Z=len(full);m=len(G['edges'])
        LS,LT,LB,A,h=matrix(G,near,full);paths=route_counts(G,near,full,LS)
        C=1+2*K*(K-1);gs,gt,gb=map(positive_gap,[LS,LT,LB])
        assert gt+1e-10>=gb and gs+1e-10>=gt/C
        assert np.linalg.eigvalsh(C*LS-LT).min()>-1e-9
        bound=1/(256*m*(n/Z)**4*C);assert gs+1e-12>=bound
        for _ in range(4):
            x=rng.normal(size=n);harmonic=A.T@x/K;y=np.concatenate([x,harmonic])
            assert abs(y@LB@y/(n+Z)-n/(n+Z)*(x@LT@x/n))<1e-10
            assert np.var(y)+1e-12>=n/(n+Z)*np.var(x)
        rows.append({'case':name,'vertices':2*K,'edges':m,'near':n,'full':Z,
                     'slide_gap':gs,'trace_gap':gt,'Broder_gap':gb,'lower_bound':bound,**paths})
    report('trace_schur_complement_record_preserving_routes_and_gap_comparison',graphs=len(rows),
           routed_pairs=sum(r['routed_pairs'] for r in rows),rows=rows)

def exact_small_controls():
    rows=[]
    cases=[('path4',simple_graph(4,[(0,1),(1,2),(2,3)])),
           ('cycle4',simple_graph(4,[(0,1),(1,2),(2,3),(3,0)])),
           ('cycle6',simple_graph(6,[(i,(i+1)%6) for i in range(6)])),
           ('K4',simple_graph(4,combinations(range(4),2))),
           ('odd_barbell',simple_graph(6,[(0,1),(1,2),(2,0),(3,4),(4,5),(5,3),(2,3)]))]
    for name,G in cases:
        near,full=levels(G);LS,LT,LB,A,h=matrix(G,near,full);K=len(G['sites'])//2
        n,Z,m=len(near),len(full),len(G['edges']);B=sp.Matrix(LB);S=sp.Matrix(LS);AA=sp.Matrix(A)
        T=B[:n,:n]-B[:n,n:]*(B[n:,n:].inv())*B[n:,:n]
        assert T==S+sp.diag(*map(int,h))-AA*AA.T/K
        # Independent cut enumeration verifies the imported normalization on these graphs.
        size=n+Z;conductance=Fraction(1)
        for count in range(1,size//2+1):
            for subset in combinations(range(size),count):
                cut=sum(int(-LB[i,j]) for i in subset for j in range(size) if j not in subset)
                conductance=min(conductance,Fraction(cut,2*m*count))
        imported=Fraction(1,16*m)*Fraction(Z,n)**2;assert conductance>=imported
        beta=sp.Rational(1,13);p=sp.Rational(K*Z,n);H=sp.diag(*map(int,h))
        U=(S+beta*H).inv()*beta*AA
        assert U*sp.ones(Z,1)==sp.ones(n,1) and min(U)>=0
        mean=(S+beta*H).inv()*sp.ones(n,1)
        assert (sp.ones(1,n)*H*mean)[0]/n==1/beta
        rows.append({'case':name,'conductance':str(conductance),'imported_lower_bound':str(imported),
                     'hazard_mean':str(p),'uniform_exit_error_max':str(max(abs(x-sp.Rational(1,Z)) for x in U)),
                     'mean_clock_stationary':str(sum(mean)/n)})
    report('exact_rational_trace_conductance_and_killed_matrix_controls',rows=rows)

def killing_bounds():
    rows=[]
    for name,G in graph_cases():
        if name not in ['all_four_63','cycle_6','cube','odd_barbell','path_10']:continue
        near,full=levels(G);LS,LT,LB,A,h=matrix(G,near,full)
        rows.extend(killing_one(name,LS,A,h))
    # Tiny hazard fraction need not appear in the TV bound denominator.
    for n in [12,40,100]:
        L=np.zeros((n,n))
        for i in range(n-1):L[i,i]+=1;L[i+1,i+1]+=1;L[i,i+1]-=1;L[i+1,i]-=1
        A=np.zeros((n,2));A[0,0]=1;A[-1,1]=1
        rows.extend(killing_one(f'path_chain_rare_hazard_{n}',L,A,A.sum(axis=1)))
    report('uniform_exit_joint_clock_and_mean_bounds',rows=rows)

def killing_one(name,L,A,h):
    n,Z=A.shape;g=positive_gap(L);T=(1+math.log(n))/g;p=float(h.mean());H=np.diag(h)
    J=np.ones((n,n))/n;green=np.linalg.inv(L+J)-J
    assert np.max(np.sum(abs(green),axis=1))<=T+1e-8
    Q=np.eye(n)-J;q=h-p;Qa=Q@A
    def centered(beta,lam):
        # Exact constant/centered Schur decomposition avoids inverting the
        # tiny killed eigenvalue with a full unscaled floating-point solve.
        B=L+beta*(Q@H@Q+lam*p*Q)+J
        ra=np.linalg.solve(B,Qa);rq=np.linalg.solve(B,q)
        C=float(q@rq/n);den=p*(1+lam)-beta*C;assert den>0
        c=(A.mean(axis=0)-beta*(h@ra/n))/den
        U=c[None,:]+beta*ra-beta*rq[:,None]*c[None,:]
        assert np.max(abs((L+beta*(H+lam*p*np.eye(n)))@U-beta*A))<1e-11
        return U,rq,den
    rows=[]
    for r in [1e-4,.01,.1,1,10]:
        beta=r/T;U,rq,den=centered(beta,0)
        assert np.max(abs(U.sum(axis=1)-1))<1e-7 and U.min()>-1e-12
        direct=np.linalg.solve(L+beta*H,beta*A)
        direct_error=float(np.max(abs(direct-U)))
        tv=float(np.max(np.sum(abs(U-1/Z),axis=1)/2));assert tv<=min(1,2*r)+1e-8
        scaled_mean=p*(1-beta*rq)/den;mean_error=float(max(abs(scaled_mean-1)))
        assert np.max(abs((L+beta*H)@scaled_mean-beta*p))<1e-11
        if 2*r<1:assert mean_error<=2*r/(1-2*r)+1e-8
        joint_max=0.
        for lam in [0,.25,1,3]:
            transform,_,_=centered(beta,lam)
            delta=transform-1/(Z*(1+lam))
            # The largest absolute subset sum when the signed row need not sum to zero.
            err=float(max(np.maximum(delta,0).sum(axis=1).max(),np.maximum(-delta,0).sum(axis=1).max()))
            bound=r*(1+lam*p)*(1+1/(1+lam));assert err<=bound+1e-8
            joint_max=max(joint_max,err)
        rows.append({'case':name,'states':n,'targets':Z,'p':p,'gap':g,'beta_times_T':r,
                     'exit_TV':tv,'relative_mean_error':mean_error,'max_joint_subset_transform_error':joint_max,
                     'unscaled_direct_solve_discrepancy':direct_error})
    return rows

def symbolic_volume_bound():
    K,d,kappa=sp.symbols('K d kappa',positive=True)
    C=1+2*K*(K-1);general=kappa/(256*(2*d*K)*(K*K/(2*d))**4*C)
    assert sp.simplify(general-kappa*d**3/(32*K**9*C))==0
    assert sp.simplify(2*K*K-C)==2*K-1
    for kk in range(2,65):assert 1+2*kk*(kk-1)<=2*kk*kk
    report('torus_counting_substitution_and_polynomial_exponent',
           exact_before_C_bound=str(sp.factor(general)),relaxation_bound='kappa*d^3/(64*K^11)',
           mixing_integral_bound='64*K^11*(1+2*d*K*log(2))/(kappa*d^3)',
           sufficient_schedule='(beta/kappa)*K^12 -> 0',literature_theorems_are_imports=True)

def main():
    OUT.mkdir(exist_ok=False)
    comparison_controls();exact_small_controls();killing_bounds();symbolic_volume_bound()
    sources=[Path(__file__),HERE/'GEOMETRIC_POLYNOMIAL_RELAXATION_AND_FORMATION.md',
             HERE/'GEOMETRIC_TWO_VACANCY_GENERAL_GRAPH.md',HERE/'geometric_general_graph_check.py']
    result={'scope':'Author exact/numerical finite controls for a conditional proof; not independent review or a proof by finite enumeration.',
            'rows':ROWS,'sources_sha256':{p.name:sha(p) for p in sources}}
    (OUT/'RESULTS.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'groups':len(ROWS),'sources_sha256':result['sources_sha256']},indent=2))
if __name__=='__main__':main()
