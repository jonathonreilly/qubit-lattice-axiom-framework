"""Exact support geometry and rational finite-time bound arithmetic; no simulation."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from pathlib import Path
import hashlib,json,time

def geometry(L):
    @lru_cache(None)
    def neighbors(x):
        out=[]
        for i in range(3):
            for d in (-1,1):
                y=list(x);y[i]=(y[i]+d)%L;out.append(tuple(y))
        assert len(set(out))==6
        return tuple(sorted(out))
    @lru_cache(None)
    def star(a):
        assert sum(a)%2==0
        return frozenset([('s',*a),*[('s',*b) for b in neighbors(a)],
                          *[('e',*a,*b) for b in neighbors(a)]])
    @lru_cache(None)
    def partners(a):
        return frozenset(c for b in neighbors(a) for c in neighbors(b) if c!=a)
    def centers(X):
        result=set()
        for v in X:
            x=v[1:4]
            if v[0]=='e' or sum(x)%2==0:result.add(x)
            else:result.update(neighbors(x))
        return result
    def groups(X):
        a=centers(X);out={('f',x) for x in a}
        for x in a:
            for y in partners(x):out.add(('h',*sorted((x,y))))
        return out
    def support(g):
        return star(g[1]) if g[0]=='f' else star(g[1])|star(g[2])
    def Dhalo(X):
        out=set(X)
        for v in X:
            x=v[1:4]
            if v[0]=='e':edges=[(x,v[4:7])]
            elif sum(x)%2==0:edges=[(x,b) for b in neighbors(x)]
            else:edges=[(a,x) for a in neighbors(x)]
            for a,b in edges:out.update([('s',*a),('s',*b),('e',*a,*b)])
        return out
    return neighbors,star,partners,groups,support,Dhalo

def counts(G):
    return dict(formation=sum(g[0]=='f' for g in G),magnetic=sum(g[0]=='h' for g in G))

def strength(G):
    c=counts(G);return (5184*c['magnetic'],600*c['formation'])

def multiply(p,q):
    return [F(p[0]*q[0]),F(p[0]*q[1]+p[1]*q[0]),F(p[1]*q[1])]

def main():
    t=time.monotonic();rows=[]
    for L in [4,6,8,12,16,20]:
        neighbors,star,partners,groups,support,Dhalo=geometry(L)
        a=(0,0,0);b=(1,0,0);SA={('s',*a)};SB={('s',*b)}
        sets={'A':SA,'B':SB,'AB':SA|SB};out={}
        exhaustive=None
        if L<=8:
            A=[x for x in product(range(L),repeat=3) if sum(x)%2==0]
            exhaustive={('f',x) for x in A}
            for x in A:
                for y in A:
                    if x<y and set(neighbors(x))&set(neighbors(y)):exhaustive.add(('h',x,y))
            c=counts(exhaustive)
            assert c['formation']==L**3//2
            assert c['magnetic']==(15*L**3//4 if L==4 else 9*L**3//2)
        for name,S in sets.items():
            G=groups(S);X1=set(S)
            for g in G:
                assert support(g)&S
                assert len(support(g))<=25
                X1.update(support(g))
            X2=Dhalo(X1);G2=groups(X2)
            assert len(X1)<=4651*len(S) and len(X2)<=19*len(X1)
            assert counts(G)['formation']<=6*len(S)
            assert counts(G)['magnetic']<=180*len(S)
            if exhaustive is not None:
                assert G=={g for g in exhaustive if support(g)&S}
                assert G2=={g for g in exhaustive if support(g)&X2}
            out[name]=dict(S=sorted(S),X1=sorted(X1),X2=sorted(X2),
                groups=sorted(G),halo_groups=sorted(G2),counts=counts(G),
                halo_counts=counts(G2),J_coefficients=strength(G),
                J_halo_coefficients=strength(G2),
                exhaustive_global_comparison=exhaustive is not None)
        # Complex covariance is proved analytically. These two real site tests
        # exercise its diagonal and negative neighboring covariance coefficients.
        tests=[{a:F(1)},{b:F(1)}];means=[];N=[]
        edges=set()
        for x in [a,b]:
            edges.update((x,y) if sum(x)%2==0 else (y,x) for y in neighbors(x))
        for f in tests:
            means.append(10*sum(f.get(y,F(0))-f.get(x,F(0)) for x,y in edges))
            N.append([20*sum((f.get(y,F(0))-f.get(x,F(0)))*(g.get(y,F(0))-g.get(x,F(0))) for x,y in edges) for g in tests])
        assert means==[-60,60] and N==[[120,-20],[-20,120]]
        M={}
        for label,first,second,bprod in [('AA','A','A',4),('BB','B','B',1),('AB','A','B',2)]:
            Slabel=first if first==second else 'AB';r=out[Slabel]
            p=multiply(r['J_coefficients'],r['J_halo_coefficients'])
            q=multiply(out[first]['J_coefficients'],out[second]['J_coefficients'])
            M[label]=[bprod*(x/2+y) for x,y in zip(p,q)]
        MAB=sum(M['AB']);MBB=sum(M['BB']);T=min(F(120)/(60*MAB+11*MBB),F(60)/MBB)
        error=T*(MAB+MBB/6)/(120-T*MBB)
        assert 120-T*MBB>0 and error<=F(1,60)
        rows.append(dict(L=L,sets=out,means_in_kappa=means,covariance_in_kappa=N,
            M_polynomial_order=['delta_squared','delta_kappa','kappa_squared'],M=M,
            illustrative_delta_kappa_equal_one=dict(max_time_for_bound_one_over_sixty=T,
                decimal_time=float(T),denominator=120-T*MBB,ratio_error_bound=error),
            scope='Exact geometry and rational conservative bound arithmetic; not a time-evolution simulation or laboratory calibration.'))
    # Local neighborhoods eventually stop wrapping. This checks the displayed
    # volume comparison; no theorem for arbitrary L is inferred from this grid.
    for key in ['A','B','AB']:
        assert rows[-1]['sets'][key]['counts']==rows[-2]['sets'][key]['counts']
        assert rows[-1]['sets'][key]['halo_counts']==rows[-2]['sets'][key]['halo_counts']
    result=dict(program_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        graphs=rows,elapsed_seconds=time.monotonic()-t,status='all exact assertions passed')
    print(json.dumps(result,indent=2,default=lambda x:str(x) if isinstance(x,F) else x))

if __name__=='__main__':main()
