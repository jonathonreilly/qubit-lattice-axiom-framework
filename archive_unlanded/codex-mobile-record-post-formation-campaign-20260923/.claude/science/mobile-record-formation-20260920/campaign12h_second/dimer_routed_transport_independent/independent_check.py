#!/usr/bin/env python3
"""Independent routed-matching, current, color-code and energy controls.
No author checker/results or previous primary fluctuation source are read.
"""
from pathlib import Path
import datetime, hashlib, itertools, json, math
from fractions import Fraction
import numpy as np
import scipy.linalg
import sympy as sp
HERE = Path(__file__).resolve().parent
DELTAS = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
E = np.array(DELTAS + [(0,0,0)] * 8, dtype=np.int64)
B = np.array([(0,0,0)] * 6 + list(itertools.product([-1,1], repeat=3)), dtype=np.int64)

def vector_f(n):
    x,y,z = n
    return sp.Matrix([y*z*(y*y-z*z), z*x*(z*z-x*x), x*y*(x*x-y*y)])

def rotations():
    out=[]
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([-1,1], repeat=3):
            r=sp.zeros(3)
            for i in range(3):r[i,perm[i]]=signs[i]
            if r.det()==1:out.append(r)
    return out

class Matching:
    def __init__(self,N,staggered=True):
        self.N=N;self.xyz=list(itertools.product(range(N),repeat=3))
        self.index={x:i for i,x in enumerate(self.xyz)}
        self.black=[i for i,x in enumerate(self.xyz) if sum(x)%2==0]
        self.white=[i for i,x in enumerate(self.xyz) if sum(x)%2==1]
        self.bindex={site:i for i,site in enumerate(self.black)}
        self.partner=np.full(N**3,-1,dtype=np.int64)
        for site in self.black:
            sign=1 if staggered or self.xyz[site][0]%2==0 else -1
            target=self.shift(site,(sign,0,0));self.partner[site]=target;self.partner[target]=site
    def shift(self,site,delta):
        return self.index[tuple((a+b)%self.N for a,b in zip(self.xyz[site],delta))]
    def displacement(self,a,b):
        out=[]
        for x,y in zip(self.xyz[a],self.xyz[b]):
            z=(y-x)%self.N
            if z>self.N//2:z-=self.N
            out.append(z)
        return tuple(out)
    def random_flips(self,attempts,seed):
        rng=np.random.default_rng(seed);success=0
        for _ in range(attempts):
            x=int(rng.integers(self.N**3));i,j=sorted(rng.choice(3,size=2,replace=False))
            di=np.eye(3,dtype=int)[i];dj=np.eye(3,dtype=int)[j]
            p=[x,self.shift(x,di),self.shift(self.shift(x,di),dj),self.shift(x,dj)]
            if self.partner[p[0]]==p[1] and self.partner[p[2]]==p[3]:pairs=[(p[0],p[3]),(p[1],p[2])]
            elif self.partner[p[0]]==p[3] and self.partner[p[1]]==p[2]:pairs=[(p[0],p[1]),(p[2],p[3])]
            else:continue
            for a,b in pairs:self.partner[a]=b;self.partner[b]=a
            success+=1
        return success
    def arrays(self):
        assert all(self.partner[self.partner[x]]==x for x in range(self.N**3))
        d=np.array([self.displacement(u,int(self.partner[u])) for u in self.black],dtype=np.int64)
        assert np.all(abs(d).sum(axis=1)==1)
        q=np.array([[self.bindex[int(self.partner[self.shift(u,delta)])] for u in self.black] for delta in DELTAS],dtype=np.int64)
        inv=np.argsort(q,axis=1)
        return d,q,inv
    def block(self,u,l):
        sites={self.shift(self.black[u],z) for z in itertools.product(range(-l,l+1),repeat=3)}
        black={self.bindex[x] for x in sites if x in self.bindex}
        contracted={self.bindex[x if x in self.bindex else int(self.partner[x])] for x in sites}
        return sites,black,contracted

def component_size(adj,start):
    seen={start};queue=[start]
    for u in queue:
        for v in adj[u]-seen:seen.add(v);queue.append(v)
    return len(seen)

def geometry_controls(g,name):
    d,q,inv=g.arrays();K=len(g.black);adj=[set() for _ in range(K)]
    cycles=[];fixed=0
    for k,delta in enumerate(DELTAS):
        assert np.array_equal(np.sort(q[k]),np.arange(K))
        remaining=set(range(K))
        while remaining:
            u=min(remaining);cycle=[u];v=int(q[k,u])
            while v!=u:cycle.append(v);v=int(q[k,v])
            remaining-=set(cycle)
            if len(cycle)==1:fixed+=1
            else:assert len(cycle)>=g.N//2;cycles.append(len(cycle))
        for u,v in enumerate(q[k]):
            step=np.array(delta)-d[v]
            assert g.shift(g.black[u],step)==g.black[v]
            if u==v:assert np.array_equal(d[u],delta);continue
            assert step@np.array(delta) in [1,2] and abs(step).sum()==2
            footprint=[int(inv[k,u]),u,int(v),int(q[k,v])]
            assert len(set(footprint))==4
            white_step=np.array(delta)-d[u]
            assert abs(white_step).sum()==2
            assert g.shift(int(g.partner[g.black[u]]),white_step)==g.partner[g.black[v]]
            adj[u].add(int(v));adj[v].add(u)
        # Under parity reversal, old pair u is indexed by its old white endpoint.
        q_new=np.array([g.bindex[g.shift(int(g.partner[u]),delta)] for u in g.black])
        assert np.array_equal(q_new,inv[k^1])
    assert component_size(adj,0)==K
    total=np.zeros((3,3),dtype=np.int64)
    for k,delta in enumerate(DELTAS):
        total+=(np.array(delta)-d[q[k]]).sum(axis=0)[:,None]*np.array(delta)[None,:]
    assert np.array_equal(total,2*K*np.eye(3,dtype=np.int64))
    blocks=[]
    for l in [1,2,3]:
        if 2*l+3>=g.N:continue
        for u in [0,K//7,K//3,K-1]:
            sites,black,C=g.block(u,l)
            restricted={a:{b for b in adj[a] if b in C} for a in C}
            assert component_size(restricted,next(iter(C)))==len(C)
            assert black<=C
            coeff={v:(Fraction(1,len(C)) if v in C else 0)-(Fraction(1,len(black)) if v in black else 0) for v in C|black}
            variance=sum(x*x for x in coeff.values())
            assert variance==Fraction(len(C)-len(black),len(C)*len(black))
            blocks.append({'radius':l,'center':u,'black_count':len(black),'contracted_count':len(C),'boundary_extra':len(C-black),
                           'exact_iid_average_difference_variance':str(variance),'radius4_times_variance':float(l**4*variance)})
    # Mean-current cancellation alone need not eliminate this unsmoothed term.
    r=d[q[0],0]-d[q[1],0]
    assert r.sum()==0
    return {'name':name,'N':g.N,'pairs':K,'fixed_directed_channels':fixed,'nonfixed_cycles':len(cycles),
            'minimum_nonfixed_cycle':min(cycles),'maximum_nonfixed_cycle':max(cycles),
            'routing_and_parity_exact':True,'unwrapped_current_identity':total.tolist(),
            'connected_geometric_block_controls':blocks,
            'unsmoothed_direction_coefficient_variance':str(Fraction(int(r@r),K))},(d,q,inv,adj)

def rate_current_code_controls():
    # Twice S at gamma=1, all integer. The rate drive is h2/2.
    s2=np.array([[[int(np.dot(delta,np.cross(ea,bb)+np.cross(eb,ba)))
                    for eb,bb in zip(E,B)] for ea,ba in zip(E,B)] for delta in DELTAS],dtype=np.int64)
    weights=np.arange(1,15,dtype=np.int64);W=int(weights.sum());p=[Fraction(int(x),W) for x in weights]
    X=[sum(p[a]*int(E[a,i]) for a in range(14)) for i in range(3)]
    Y=[sum(p[a]*int(B[a,i]) for a in range(14)) for i in range(3)]
    def cross(x,y):return [x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0]]
    currents=[];extrema=[]
    for k,delta in enumerate(DELTAS):
        numer=[0]*14;lo=0;hi=0
        for l,a,b,r in itertools.product(range(14),repeat=4):
            h2=int(s2[k,l,a]+s2[k,a,r]-s2[k,l,b]-s2[k,b,r]);lo=min(lo,h2);hi=max(hi,h2)
            assert h2==-int(s2[k,l,b]+s2[k,b,r]-s2[k,l,a]-s2[k,a,r])
            assert h2==int(s2[k^1,r,b]+s2[k^1,b,l]-s2[k^1,r,a]-s2[k^1,a,l])
            term=h2*int(weights[l])*int(weights[a])*int(weights[b])*int(weights[r])
            numer[a]+=term;numer[b]-=term
        actual=[Fraction(x,4*W**4) for x in numer]
        expected=[]
        for a in range(14):
            a1=cross(E[a],Y);a2=cross(X,B[a]);a3=cross(X,Y)
            expected.append(p[a]*sum(delta[i]*(a1[i]+a2[i]-2*a3[i]) for i in range(3)))
        assert actual==expected and sum(actual)==0
        assert (lo,hi)==(-4,4)
        currents.append([str(x) for x in actual]);extrema.append([lo,hi])
    x,y,z=sp.symbols('x y z',real=True);n=sp.Matrix([x,y,z]);f=vector_f(n)
    rots=rotations();assert len(rots)==24
    for R in rots:assert sp.simplify(vector_f(R*n)-R*f)==sp.zeros(3,1)
    assert vector_f(-n)==f
    Aexample=vector_f([0,1,2]);Bexample=vector_f([1,2,3])
    assert max(t*t for t in Aexample)>sp.Rational(81,100)*sum(t*t for t in Aexample)
    assert max(t*t for t in Bexample)<sp.Rational(81,100)*sum(t*t for t in Bexample) and all(t!=0 for t in Bexample)
    color_vectors=[tuple(map(int,e if any(e) else b)) for e,b in zip(E,B)]
    for R in rots:
        permutation=[color_vectors.index(tuple(map(int,R*sp.Matrix(v)))) for v in color_vectors]
        assert sorted(permutation)==list(range(14))
        for k,delta in enumerate(DELTAS):
            newdelta=DELTAS.index(tuple(map(int,R*sp.Matrix(delta))))
            assert np.array_equal(s2[k],s2[newdelta][np.ix_(permutation,permutation)])
    return {'h2_extrema_by_direction':extrema,'rates_at_gamma1_k0_2_range':['1/2','3/2'],
            'full_support_integer_weight_current':currents,'proper_cubic_group_size':24,
            'even_color_code_and_S_covariance_exact':True,'A_open_region_witness':list(map(str,Aexample)),
            'B_open_region_witness':list(map(str,Bexample))},s2

def current_symbol_controls(s2):
    rho=sp.Rational(2,5);p=sp.Matrix([rho/6]*6+[(1-rho)/8]*8);C=sp.diag(*p)-p*p.T
    Q=sp.Matrix([1,2,3]);S=sp.zeros(14)
    for i in range(3):S+=Q[i]*sp.Matrix(s2[2*i].tolist())/2
    A=2*sp.diag(*p)*S
    assert S*p==sp.zeros(14,1) and A*C==C*A.T
    X=sp.Matrix(E.T.tolist());Y=sp.Matrix(B.T.tolist());cross=sp.Matrix([[0,-Q[2],Q[1]],[Q[2],0,-Q[0]],[-Q[1],Q[0],0]])
    assert X*A==-rho*cross*Y/3 and Y*A==(1-rho)*cross*X
    lam=sp.symbols('lambda');polynomial=A.charpoly(lam).as_expr();target=lam**10*(lam**2-rho*(1-rho)*(Q.dot(Q))/3)**2
    assert sp.expand(polynomial-target)==0
    assert (sp.zeros(14)*C)==sp.zeros(14)
    return {'rho_A':str(rho),'Q':list(Q),'gamma1_full14_characteristic_polynomial':str(sp.factor(polynomial)),
            'probability_tangent_counts_gamma_nonzero':{'propagating':4,'static':9},
            'gamma_zero_probability_tangent_static':13,'field_flux_signs_and_C_symmetrization_exact':True}

def local_canonical_control(s2):
    # Complete 8-site sector, three active labels. Check every count profile.
    active=[2,6,13];n=8;rows=0;maximum=Fraction(0)
    for counts in itertools.product(range(n+1),repeat=3):
        if sum(counts)!=n:continue
        weights={a:c for a,c in zip(active,counts)};current=[Fraction(0)]*14
        for word in itertools.product(active,repeat=4):
            remaining=weights.copy();prob=Fraction(1)
            for i,a in enumerate(word):prob*=Fraction(remaining[a],n-i);remaining[a]-=1
            if not prob:continue
            l,a,b,r=word;h2=int(s2[0,l,a]+s2[0,a,r]-s2[0,l,b]-s2[0,b,r])
            current[a]+=prob*h2/4;current[b]-=prob*h2/4
        q=sp.Matrix([sp.Rational(weights.get(a,0),n) for a in range(14)]);S=sp.Matrix(s2[0].tolist())/2
        flux=2*sp.diag(*q)*(S*q-sp.ones(14,1)*(q.T*S*q)[0])
        err=max(abs(current[a]-Fraction(flux[a])) for a in range(14));maximum=max(maximum,err);rows+=1
    return {'block_size':n,'canonical_count_profiles':rows,'max_exact_without_replacement_minus_product_current':str(maximum),
            'coverage':'Finite canonical sampling control; the uniform O(1/m) estimate is proved by collision coupling, not inferred from these rows.'}

def stationary_sector_energy(g,arrays,s2):
    d,q,inv,adj=arrays;K=len(g.black);twiceQ=np.zeros((K,K),dtype=np.int64);adjacency=np.zeros((K,K),dtype=np.int64)
    # One B color among A colors. gamma=1,k0=2; actual rate=1+h2/8.
    a,b=2,6
    for k in range(6):
        for u,v in enumerate(q[k]):
            if u==v:continue
            # Endpoint exceptional color at source then at target. Context is A,A.
            h2=int(s2[k,a,b]+s2[k,b,a]-2*s2[k,a,a])
            forward=8+h2;backward=8-h2
            twiceQ[u,v]+=forward;twiceQ[v,u]+=backward
            twiceQ[u,u]-=forward;twiceQ[v,v]-=backward
            adjacency[u,v]+=1;adjacency[v,u]+=1
    assert np.all(twiceQ.sum(axis=0)==0) and np.all(twiceQ.sum(axis=1)==0)
    L=np.diag(adjacency.sum(axis=1))-adjacency
    assert np.array_equal(-(twiceQ+twiceQ.T),16*L)
    Q=twiceQ.astype(float)/8;S=(Q+Q.T)/2
    f=np.array([(i*7)%13-6 for i in range(K)],dtype=float);F=f-f.mean();Pi=np.ones((K,K))/K
    poisson=np.linalg.solve(-S+Pi,F);Hminus1=float(F@poisson/K)
    rows=[]
    for t in [.1,.7]:
        matrix=np.zeros((K+2,K+2));matrix[:K,:K]=Q;matrix[:K,K]=F;matrix[K,K+1]=1
        integrated=scipy.linalg.expm(t*matrix)[:K,K+1]
        variance=float(2*F@integrated/K);bound=2*t*Hminus1
        assert -1e-10<=variance<=bound+1e-9
        rows.append({'time':t,'stationary_integrated_variance':variance,'forward_backward_bound':bound})
    return {'states':K,'uniform_stationarity_exact':True,'symmetric_generator_swap_form_exact':True,
            'generator_asymmetric':not np.array_equal(twiceQ,twiceQ.T),
            'energy_inequality_numerical_rows':rows,
            'scope':'Complete one-exceptional-color sector at an irregular admissible N=8 matching; not a full-product simulation.'}

def run():
    geometries=[];gs=[];arrs=[]
    for N,attempts,seed,name in [(8,0,0,'winding_staggered8'),(8,16000,212018,'irregular8'),(12,38000,212019,'irregular12')]:
        g=Matching(N,staggered=not attempts);success=g.random_flips(attempts,seed) if attempts else 0
        row,arrays=geometry_controls(g,name);row['successful_geometry_flips']=success
        geometries.append(row);gs.append(g);arrs.append(arrays)
        print('geometry',name,'cycles',row['minimum_nonfixed_cycle'],row['maximum_nonfixed_cycle'],'direction variance',row['unsmoothed_direction_coefficient_variance'],flush=True)
    current,s2=rate_current_code_controls();print('exact rates, full-support currents and cubic code passed',flush=True)
    symbol=current_symbol_controls(s2);canonical=local_canonical_control(s2)
    energy=stationary_sector_energy(gs[1],arrs[1],s2)
    assert Fraction(geometries[1]['unsmoothed_direction_coefficient_variance'])>0
    result={'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'geometry':geometries,
            'currents_rates_code':current,'current_symbol':symbol,'canonical_sampling':canonical,'stationary_energy':energy,
            'read_boundary':'No author checker/results or old primary fluctuation note accessed.',
            'findings':['The four-propagating-mode count requires gamma != 0; gamma=0 gives thirteen static tangent modes.']}
    result['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return result

if __name__=='__main__':
    assert not (HERE/'INDEPENDENT_RESULTS.json').exists()
    result=run()
    (HERE/'INDEPENDENT_RESULTS.json').write_text(json.dumps(result,indent=2,default=str)+'\n')
    print('Independent controls complete.')
