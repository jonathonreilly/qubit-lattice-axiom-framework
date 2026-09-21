"""Author exact clock/counting controls; no reconstruction of Taggi's theorem."""
from pathlib import Path
from functools import lru_cache
from itertools import product
import hashlib,json
import sympy as s
from geometric_partner_formation_check import graph,prepare,enumerate_matchings,channels,partners

HERE=Path(__file__).resolve().parent;OUT=HERE/'geometric_last_pair_clock_checks';OUT.mkdir(exist_ok=True)
ROWS=[]
def report(name,**data):
    row={'name':name,'pass':True,**data};ROWS.append(row);print(json.dumps(row),flush=True)

def scalar_and_laplace():
    b,z=s.symbols('beta s',positive=True)
    S=s.Matrix([[-1,1,0],[1,-3,2],[0,2,-2]])
    H=s.diag(1,0,1);A=s.Matrix([[1,0],[0,0],[0,1]]);one=s.ones(3,1)
    U=(-S+b*(H+z*s.eye(3))).inv()*(b*A)
    expected=s.Rational(1,2)*s.Rational(2,3)/(s.Rational(2,3)+z)
    assert all(s.simplify(s.limit(x,b,0)-expected)==0 for x in U)
    T=(-S+b*H).inv()*one;M2=(-S+b*H).inv()*(2*T)
    assert [s.limit(b*t,b,0) for t in T]==[s.Rational(3,2)]*3
    assert [s.limit(b*b*t,b,0) for t in M2]==[s.Rational(9,2)]*3
    # A general-chain growing-system countercontrol: shrinking beta alone
    # does not force uniform selection when conservative relaxation shrinks faster.
    n=s.Symbol('n',positive=True);epsilon=1/n**2;rate=1/n
    slow=s.Matrix([[-epsilon,epsilon],[epsilon,-epsilon]])
    hit=(-slow+rate*s.eye(2)).inv()*(rate*s.eye(2))
    assert s.simplify(hit[0,0]-(n+1)/(n+2))==0 and s.limit(hit[0,0],n,s.oo)==1
    # The single near-perfect state is separately exponential, without a Q gap.
    assert s.simplify(b/(b+z*b)-1/(1+z))==0
    report('symbolic_laplace_exit_independence_mean_second_moment_and_countercontrols',
           uniform_exit_probability='1/2',rate='2/3',mean_limit='3/2',second_moment_limit='9/2',
           simultaneous_limit_countercontrol='two-state family: beta=1/n, exchange=1/n^2, initial exit probability (n+1)/(n+2)->1; not a cubic-torus assertion')

def cube_full_operator():
    G=prepare(graph((2,2,2)));states=enumerate_matchings(G)
    near=[M for M in states if len(M)==3];full=[M for M in states if len(M)==4]
    I={M:i for i,M in enumerate(near)};n=len(near)
    S=s.zeros(n);H=s.zeros(n)
    for M,i in I.items():
        for target,r,e in channels(M,G,0,1,0):S[i,I[target]]+=r;S[i,i]-=r
        H[i,i]=len(channels(M,G,1,0,0))
    one=s.ones(n,1);P=one*one.T/n;Q=s.eye(n)-P;h=H*one;p=(one.T*h)[0]/n;q=h-p*one
    assert p==s.Rational(9,11) and n==44 and len(full)==9
    L=-S;R0=Q*(L+P).inv()*Q;C0=(q.T*R0*q)[0]/n
    records=[]
    for beta in [s.Rational(1),s.Rational(1,10),s.Rational(1,100)]:
        R=Q*(L+beta*Q*H*Q+P).inv()*Q;C=(q.T*R*q)[0]/n
        denominator=p-beta*C;assert denominator>0 and C>=0
        T=(one-beta*R*q)/(beta*denominator)
        assert (L+beta*H)*T==one
        mean=(one.T*T)[0]/n;assert mean>=1/(beta*p)
        deviation=max(abs(beta*t-1/p) for t in T)
        records.append({'beta':str(beta),'mean_from_uniform':str(mean),'maximum_scaled_mean_error':str(deviation)})
    # Check the symbolic 3-state mean against every full 44-state equation.
    b=s.Symbol('beta',positive=True)
    def columnar_completion(M):
        births=channels(M,G,1,0,0)
        if not births:return None
        target=births[0][0]
        axes={next(j for j in range(3) if G['sites'][a][j]!=G['sites'][c][j]) for a,c in target}
        return len(axes)==1
    fA=(3*b+22)/(3*b*(b+6));fB=(4*b+22)/(3*b*(b+6));fC=fB+s.Rational(1,6)
    values=s.Matrix([fC if columnar_completion(M) is None else fA if columnar_completion(M) else fB for M in near])
    assert all(s.cancel(x)==0 for x in (L+b*H)*values-one)
    assert all(s.limit(b*x,b,0)==s.Rational(11,9) for x in values)
    correction=C0/(p*p)*one-R0*q/p
    for i,x in enumerate(values):assert s.simplify(s.limit(x-1/(b*p),b,0)-correction[i])==0
    report('unlumped_cube_schur_mean_and_every_state_symbolic_clock',near_states=44,perfect_states=9,
           hazard_probability=str(p),scaled_mean_limit='11/9',integrated_hazard_covariance=str(C0),
           exact_mean_types=[str(fA),str(fB),str(s.factor(fC))],rows=records)

def permanent(A):
    A=tuple(tuple(row) for row in A);n=len(A)
    @lru_cache(None)
    def rec(i,used):
        if i==n:return 1
        return sum(rec(i+1,used|(1<<j)) for j in range(n) if A[i][j] and not (used>>j)&1)
    return rec(0,0)

def counting_controls():
    rows=[]
    for shape,periodic in [((2,2,2),False),((4,4,1),True)]:
        # Build adjacency directly: a unit-length singleton coordinate has
        # no self edge. The second case is the ordinary 4x4 square torus.
        sites=list(product(*(range(n) for n in shape)));idx={x:i for i,x in enumerate(sites)}
        L=[u for u,x in enumerate(sites) if sum(x)%2==0];R=[u for u,x in enumerate(sites) if sum(x)%2==1]
        neighbor=[set() for x in sites]
        for u,x in enumerate(sites):
            for axis,N in enumerate(shape):
                if N==1:continue
                for direction in [-1,1]:
                    y=list(x);y[axis]+=direction
                    if periodic:y[axis]%=N
                    elif not 0<=y[axis]<N:continue
                    neighbor[u].add(idx[tuple(y)])
        degree=len(neighbor[0]);assert all(len(v)==degree for v in neighbor)
        A=[[int(v in neighbor[u]) for v in R] for u in L];Z=permanent(A);K=len(L)
        minors=[]
        for i in range(K):
            minors.append([permanent([[A[ii][jj] for jj in range(K) if jj!=j] for ii in range(K) if ii!=i]) for j in range(K)])
        chi=s.Rational(sum(minors[0]),Z);Omega=sum(map(sum,minors))
        assert Omega==K*Z*chi and all(s.Rational(minors[0][j],Z)==s.Rational(1,degree) for j,v in enumerate(R) if v in neighbor[L[0]])
        assert sum(minors[i][j] for i in range(K) for j in range(K) if A[i][j])==K*Z
        if shape==(2,2,2):assert (Z,Omega,chi)==(9,44,s.Rational(11,9))
        rows.append({'shape':shape,'periodic':periodic,'degree':degree,'perfect_matchings':Z,
                     'near_perfect_matchings':Omega,'chi':str(chi),'p':str(1/chi),
                     'origin_monomer_ratios':[str(s.Rational(x,Z)) for x in minors[0]]})
    report('independent_permanent_minors_and_monomer_counting_identity',rows=rows,
           boundary='The cube is an abstract degree3 graph and the square torus is2D; neither is a numerical verification of the imported d>2 theorem.')

def main():
    scalar_and_laplace();cube_full_operator();counting_controls()
    sources=[Path(__file__),HERE/'GEOMETRIC_LAST_PAIR_CLOCK_AND_MONOMERS.md',HERE/'GEOMETRIC_RARE_BIRTH_UNIFORM_SELECTION.md',HERE/'geometric_partner_formation_check.py']
    result={'scope':'author exact controls; no proof verification of external equilibrium theorem; independent review pending',
            'rows':ROWS,'sources_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}}
    (OUT/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'groups':len(ROWS),'sources_sha256':result['sources_sha256']},indent=2))

if __name__=='__main__':main()
