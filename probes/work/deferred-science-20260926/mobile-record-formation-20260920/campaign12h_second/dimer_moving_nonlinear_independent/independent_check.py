#!/usr/bin/env python3
"""Independent owner-block geometry and conditional-entropy controls."""
from __future__ import annotations
import datetime,hashlib,itertools,json,math,platform
from pathlib import Path
from fractions import Fraction as F
import numpy as np
import scipy
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import expm_multiply
import sympy as s

HERE=Path(__file__).resolve().parent
DELTAS=[tuple(sign*int(j==i) for j in range(3)) for i in range(3) for sign in (1,-1)]

class Matching:
    def __init__(self,N):self.N=N;self.changed={};self.flips=0
    def canon(self,x):return tuple(int(a)%self.N for a in x)
    def partner(self,x):
        x=self.canon(x)
        return self.changed.get(x,(x[0]^1,x[1],x[2]))
    def owner(self,x):
        x=self.canon(x)
        return x if sum(x)%2==0 else self.partner(x)
    def disp(self,y,x):
        return np.array([(int(a)-int(b)+self.N//2)%self.N-self.N//2 for a,b in zip(y,x)],dtype=int)
    def d(self,u):return self.disp(self.partner(u),u)
    def q(self,u,delta):return self.owner(np.array(u)+delta)
    def flip(self,z,i,j):
        a=np.eye(3,dtype=int)[i];b=np.eye(3,dtype=int)[j];z=np.array(z)
        v=[self.canon(x) for x in (z,z+a,z+a+b,z+b)]
        if self.partner(v[0])==v[1] and self.partner(v[2])==v[3]:new=[(0,3),(1,2)]
        elif self.partner(v[0])==v[3] and self.partner(v[1])==v[2]:new=[(0,1),(2,3)]
        else:return False
        for x,y in new:self.changed[v[x]]=v[y];self.changed[v[y]]=v[x]
        self.flips+=1;return True
    def make_rough(self,L,attempts=600,seed=418):
        value=seed
        def draw(mod):
            nonlocal value
            value=(1103515245*value+12345)%(2**31)
            return value%mod
        planes=[(0,1),(0,2),(1,2)]
        for _ in range(attempts):
            z=[draw(L+6)-3 for _ in range(3)];i,j=planes[draw(3)];self.flip(z,i,j)
        for u,v in self.changed.items():
            assert self.partner(v)==u and np.sum(np.abs(self.disp(v,u)))==1 and (sum(u)+sum(v))%2==1
    def fixture_hash(self):
        data=json.dumps(sorted((list(k),list(v)) for k,v in self.changed.items()),separators=(',',':')).encode()
        return hashlib.sha256(data).hexdigest()

def origins_containing(M,x,L):
    return {M.canon(np.array(x)-r) for r in itertools.product(range(L),repeat=3)}

def block(M,z,L):
    z=np.array(z);physical=[M.canon(z+r) for r in itertools.product(range(L),repeat=3)]
    return physical,{M.owner(x) for x in physical}

def owner_geometry():
    N,L=180,16;M=Matching(N);M.make_rough(L)
    assert N>10*L and L>=16 and L%2==0
    rows=[];point_counter=None
    for origin in [(0,0,0),(1,2,-1),(-2,-1,3)]:
        physical,B=block(M,origin,L);m=len(B)
        assert L**3//2<=m<=L**3
        graph={u:set() for u in B};internal_edges=0;nonloops=0
        z=np.array(origin)
        for r in itertools.product(range(L),repeat=3):
            x=z+np.array(r)
            for i in range(3):
                if r[i]==L-1:continue
                y=x+np.eye(3,dtype=int)[i];a,b=M.owner(x),M.owner(y);internal_edges+=1
                if a!=b:
                    nonloops+=1;graph[a].add(b);graph[b].add(a)
                    black,white=(M.canon(x),M.canon(y)) if sum(x)%2==0 else (M.canon(y),M.canon(x))
                    delta=M.disp(white,black)
                    assert M.q(black,delta)==M.owner(white)
                    assert {black,M.owner(white)}=={a,b}
        seen={next(iter(B))};todo=list(seen)
        while todo:
            for v in graph[todo.pop()]:
                if v not in seen:seen.add(v);todo.append(v)
        assert seen==B and internal_edges==3*(L-1)*L**2
        T2=np.zeros((3,3),dtype=np.int64);symdiff=[];four_contexts=0
        for delta0 in DELTAS:
            delta=np.array(delta0);image={M.q(u,delta) for u in B};symdiff.append(len(image.symmetric_difference(B)))
            assert len(image)==m
            for u in B:
                v=M.q(u,delta);a=delta-M.d(v);T2+=np.outer(a,delta)
                assert np.array_equal(a,M.disp(v,u))
                if v!=u:
                    l=M.canon(np.array(u)+M.d(u)-delta);r=M.q(v,delta)
                    assert M.q(l,delta)==u and len({l,u,v,r})==4
                    four_contexts+=1
        error=T2-2*m*np.eye(3,dtype=np.int64)
        assert np.max(symdiff)<=18*L**2
        assert np.linalg.norm(error/2)<=54*L**2
        for u in sorted(B):
            Tu2=sum((np.outer(np.array(delta)-M.d(M.q(u,np.array(delta))),np.array(delta)) for delta in DELTAS),np.zeros((3,3),dtype=int))
            if point_counter is None and not np.array_equal(Tu2,2*np.eye(3,dtype=int)):
                point_counter={'anchor':u,'twice_local_tensor':Tu2.tolist()}
        rows.append({'origin':origin,'m':m,'weight':str(F(m,L**3+L**2)),'physical_internal_edges':internal_edges,
                     'contracted_nonloop_edges_with_multiplicity':nonloops,'connected_owner_graph':True,
                     'nonfixed_four_context_checks':four_contexts,'six_route_symmetric_differences':symdiff,
                     'twice_tensor_boundary_error':error.tolist()})
    assert point_counter is not None
    # Exact coverage and physical-edge multiplicities: use actual pairs in several orientations.
    pairs=[];seen_d=set()
    for u in sorted(M.changed):
        if sum(u)%2:continue
        d=tuple(M.d(u))
        if d in seen_d:continue
        seen_d.add(d);v=M.partner(u)
        U=origins_containing(M,u,L);V=origins_containing(M,v,L)
        assert len(U|V)==L**3+L**2 and len(U&V)==L**3-L**2
        pairs.append({'direction':d,'pair_owner_block_coverage':len(U|V),'physical_edge_cube_coverage':len(U&V)})
    assert len(pairs)>=3
    return {'N':N,'L':L,'accepted_fixture_flips':M.flips,'matching_override_sha256':M.fixture_hash(),
            'blocks':rows,'pointwise_tensor_identity_countercontrol':point_counter,'pair_coverage_controls':pairs,
            'overlap_degree_bound':(2*L+3)**3-1,'Holder_color_slots':32*L**3,
            'scope':'Sparse, exactly constructed irregular perfect matching on an N=180 torus; no kinetic simulation or phase screen.'}

def full_small_coverage():
    # Exhaustive translated-cube coverage on a smaller torus; combinatorial identities require no limit.
    N,L=12,4;M=Matching(N);M.make_rough(L,attempts=90,seed=73);w=L**3+L**2
    origins=list(itertools.product(range(N),repeat=3));counts={z:0 for z in origins}
    anchors=[u for u in origins if sum(u)%2==0]
    for u in anchors:
        support=origins_containing(M,u,L)|origins_containing(M,M.partner(u),L)
        assert len(support)==w
        for z in support:counts[z]+=1
    assert sum(counts.values())==len(anchors)*w
    assert min(counts.values())>=L**3//2 and max(counts.values())<=L**3
    # Compare three blocks directly with the complete incidence counting.
    for z in [(0,0,0),(1,2,3),(9,11,10)]:assert len(block(M,z,L)[1])==counts[z]
    return {'N':N,'L':L,'origins':len(origins),'black_anchors':len(anchors),'coverage_per_anchor':w,
            'sum_m_z':sum(counts.values()),'K_times_w':len(anchors)*w,'minimum_m':min(counts.values()),
            'maximum_m':max(counts.values()),'nonconstant_weights':len(set(counts.values()))>1,
            'scope':'Exact small combinatorial control; not a numerical test of the theorem large-block hypothesis L>=16.'}

def actual_square_records():
    positions=[(0,0),(1,0),(1,1),(0,1)];black=[0,2];out=[]
    for name,keys in [('horizontal',[0,1,2,3]),('vertical',[0,3,2,1])]:
        marks=[]
        for step in (1,-1):
            after=[None]*4
            for i,key in enumerate(keys):after[(i+step)%4]=key
            assert sorted(after)==[0,1,2,3]
            for i,key in enumerate(keys):
                j=after.index(key);assert sum(abs(a-b) for a,b in zip(positions[i],positions[j]))==1
            pair_edges=[]
            for color in (0,1):
                a,b=[i for i,k in enumerate(after) if k//2==color]
                assert sum(abs(x-y) for x,y in zip(positions[a],positions[b]))==1
                pair_edges.append(sorted([a,b]))
            mark=[after[i]//2 for i in black]
            marks.append({'step':step,'final_keys':after,'black_colors':mark,'pair_edges':pair_edges})
        assert {tuple(z['black_colors']) for z in marks}=={(0,1),(1,0)}
        out.append({'initial_orientation':name,'initial_keys':keys,'marks':marks})
    return out

def conditional_geometry_entropy():
    q=14;d=q*q;dim=2*d;nu=.6
    a,b=np.divmod(np.arange(d),q);perm=b*q+a
    rows=[];cols=[];data=[]
    for M in (0,1):
        for x in range(d):
            row=M*d+x
            for y in (x,int(perm[x])):rows.append(row);cols.append((1-M)*d+y);data.append(nu)
            rows.append(row);cols.append(row);data.append(-2*nu)
    Q=csr_matrix((data,(rows,cols)),shape=(dim,dim))
    rho=np.array([.75,.25]);f=np.vstack((1+(3*a+5*b)%17,1+((7*a+b)%13)**2)).astype(float)
    f/=f.mean(axis=1)[:,None]
    mu=(rho[:,None]*f/d).ravel();reference=np.repeat(rho/d,d)
    mudot=Q.T@mu;rhodot=2*nu*(rho[::-1]-rho);refdot=np.repeat(rhodot/d,d)
    assert np.max(np.abs(Q.T@reference-refdot))<1e-16
    derivative=float(np.dot(mudot,np.log(mu/reference))-np.dot(mu,refdot/reference))
    KL=0.
    for M in (0,1):
        for permutation in (np.arange(d),perm):
            KL+=nu*rho[M]*np.mean(f[M]*(np.log(f[1-M,permutation])-np.log(f[M])))
    assert abs(derivative-KL)<2e-14 and derivative<0
    def H(state):
        prob=state.reshape(2,d);marginal=prob.sum(axis=1);ans=0.
        for M in (0,1):
            if marginal[M]>0:
                positive=prob[M]>0
                ans+=float(np.dot(prob[M,positive],np.log(prob[M,positive]/(marginal[M]/d))))
        return ans
    histories=[]
    for name,initial in [('nonstationary_positive',mu),('point_mass_geometry',np.concatenate((f[0]/d,np.zeros(d))))]:
        initialH=H(initial);series=[]
        for t in (.1,.5,1.):
            state=expm_multiply(Q.T*t,initial);value=H(state)
            assert value<=initialH+1e-13 and abs(state.sum()-1)<1e-13
            series.append({'t':t,'H0':value,'rho':state.reshape(2,d).sum(axis=1).tolist()})
        histories.append({'initial':name,'initial_H0':initialH,'rows':series})
    # Countercontrol outside the hypotheses: color-dependent occurrence creates conditional information.
    joint=np.array([[1/8,1/4],[3/8,1/4]],float)
    marginal=joint.sum(axis=1);bad=float(np.sum(joint*np.log(joint/(marginal[:,None]/2))))
    assert bad>0
    return {'joint_states':dim,'marked_rotation_rate_each':nu,'rho0':rho.tolist(),'rho_derivative':rhodot.tolist(),
            'uniform_conditional_reference_forward_residual':float(np.max(np.abs(Q.T@reference-refdot))),
            'H0_derivative':derivative,'sum_negative_KLs':KL,'finite_time_contraction':histories,
            'autonomy_countercontrol':{'model':'Start geometry0 and uniform binary color; geometry0->1 rate2 for color0 and rate1 for color1, identity color action. Evaluate t=log2.',
                                      'initial_H0':0,'final_H0':bad,'joint_law':joint.tolist()},
            'scope':'Complete isolated flippable-square geometry/mark projection with two fourteen-color positions. No routed color dynamics is needed to test the new geometric entropy contribution.'}

def canonical_plaquette_and_constants():
    # Nonuniform count sectors, including a constant sector, still have exactly zero swap current mean.
    rows=[]
    for labels in [(0,0,0,1),(0,1,2,3),(0,0,1,1),(0,0,0,0)]:
        arrangements=set(itertools.permutations(labels));total=s.zeros(4,1)
        for v in arrangements:
            total[v[0]]+=1;total[v[2]]-=1
        assert total==s.zeros(4,1)
        rows.append({'count_fixture':labels,'arrangements':len(arrangements),'canonical_indicator_difference':[0]*4})
    L=s.symbols('L',positive=True);alpha=s.Rational(1,1792);chi=32*L**3
    assert s.simplify(2*alpha*chi-L**3/28)==0
    checks=[]
    for LL in (16,18,32,64):
        assert (2*LL+3)**3<32*LL**3
        minimum_m=LL**3//2
        assert 2*alpha*(32*LL**3)==s.Rational(minimum_m,14)
        checks.append({'L':LL,'overlap_slots_needed_bound':(2*LL+3)**3,'chi':32*LL**3,
                       'minimum_m':minimum_m,'largest_centered_exponent':str(2*alpha*(32*LL**3)),
                       'm_over_14':str(s.Rational(minimum_m,14))})
    return {'canonical_zero_drift_controls':rows,'alpha':str(alpha),'checks':checks,
            'mixture_step':'For each M the same exponential upper bound holds; averaging arbitrary rho preserves that bound before taking log. Exact sum omega_z=K controls the deterministic mean-shift term.'}

def main():
    result={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'boundary':'Independent source reconstruction and controls before author moving-nonlinear checker/results.',
            'versions':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'sympy':s.__version__}}
    for name,fn in [('owner_cube_geometry',owner_geometry),('all_origin_small_coverage',full_small_coverage),
                    ('immutable_plaquette_marks',actual_square_records),('nonstationary_conditional_entropy',conditional_geometry_entropy),
                    ('canonical_drift_and_weighted_exponential',canonical_plaquette_and_constants)]:
        result[name]=fn();print(name+' complete',flush=True)
    result['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    def encode(v):
        if isinstance(v,np.generic):return v.item()
        if isinstance(v,s.Integer):return int(v)
        if isinstance(v,s.Basic):return str(v)
        raise TypeError(type(v).__name__)
    with (HERE/'INDEPENDENT_RESULTS.json').open('x') as f:json.dump(result,f,indent=2,default=encode);f.write('\n')
    print('all independent groups complete',flush=True)

if __name__=='__main__':main()
