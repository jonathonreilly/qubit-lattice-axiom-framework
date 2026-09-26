#!/usr/bin/env python3
"""Independent finite controls for the stated smooth-winding entropy proof."""
from __future__ import annotations
import datetime, hashlib, itertools, json, math, platform
from pathlib import Path
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent
R=s.Rational
eye=s.eye(3); es=[]; bs=[]
for i in range(3):
    for sign in (1,-1): es.append(sign*eye[:,i]);bs.append(s.zeros(3,1))
for v in itertools.product((-1,1),repeat=3):es.append(s.zeros(3,1));bs.append(s.Matrix(v))

def Kmat(n):
    return s.Matrix(14,14,lambda a,b:n.dot(es[a].cross(bs[b])+es[b].cross(bs[a])))

def jac(p,n,gamma=R(2,3)):
    K=Kmat(n);v=K*p;M=(p.T*v)[0]
    return gamma*(s.diag(*[x-M for x in v])+s.diag(*p)*K-2*p*v.T)

def entropy_cycle():
    # The complete N=8, -e1 owner-route cycle has four distinct physical anchors.
    states=np.indices((14,)*4,dtype=np.int64).reshape(4,-1).T
    count=len(states);powers=14**np.arange(3,-1,-1,dtype=np.int64)
    K=np.asarray(Kmat(-eye[:,0]),dtype=np.int64)
    swaps=[];numerators=[];balance=np.zeros(count,dtype=np.int64)
    for u in range(4):
        w=(u+1)%4;l=(u-1)%4;r=(u+2)%4
        h=K[states[:,l],states[:,u]]+K[states[:,u],states[:,r]]-K[states[:,l],states[:,w]]-K[states[:,w],states[:,r]]
        rate_num=15+h # gamma=2/3,k0=5/2: rate=(15+h)/12.
        exchanged=states.copy();exchanged[:,[u,w]]=exchanged[:,[w,u]]
        index=exchanged@powers
        swaps.append(index);numerators.append(rate_num)
        balance-=rate_num;np.add.at(balance,index,rate_num)
        assert np.array_equal(rate_num+rate_num[index],np.full(count,30))
    assert np.all(balance==0)
    raw=1+((states@np.array([1,3,5,7]))%29)**2
    f=raw/raw.mean();mu=f/count;g=np.sqrt(f);D=0.;hdot=0.;mudot=np.zeros(count)
    for index,num in zip(swaps,numerators):
        rates=num/12
        D+=.5*np.mean((g[index]-g)**2)
        hdot+=8*np.mean(f*rates*(np.log(f[index])-np.log(f)))
        flow=8*mu*rates;mudot-=flow;np.add.at(mudot,index,flow)
    rstar=11/12
    assert hdot <= -2*8*rstar*D+1e-12
    assert abs(mudot.sum())<1e-13
    assert abs(hdot-np.dot(mudot,np.log(f)))<1e-12
    # Genuine inhomogeneous product reference and arbitrary tangent time derivative.
    p=np.array([[1+(5*a+7*u)%19 for a in range(14)] for u in range(4)],float)
    p/=p.sum(axis=1)[:,None]
    pdot=np.zeros_like(p)
    for u in range(4):pdot[u,u]=.001;pdot[u,(u+5)%14]=-.001
    lognu=sum(np.log(p[u,states[:,u]]) for u in range(4))
    lognudot=sum(pdot[u,states[:,u]]/p[u,states[:,u]] for u in range(4))
    direct=np.dot(mudot,np.log(mu)-lognu)-np.dot(mu,lognudot)
    applied=0.
    for index,num in zip(swaps,numerators):applied+=8*np.dot(mu,(num/12)*(lognu[index]-lognu))
    decomposed=hdot-applied-np.dot(mu,lognudot)
    assert abs(direct-decomposed)<2e-12
    # Conditional means use the uniform law within each count sector, not mu.
    sector_code=np.sort(states,axis=1)@powers
    _,sector,size=np.unique(sector_code,return_inverse=True,return_counts=True)
    mean_g=np.bincount(sector,weights=g)/size
    condvar=np.mean((g-mean_g[sector])**2)
    observable=(numerators[0]/12)*((states[:,0]==2).astype(float)-(states[:,1]==2).astype(float))
    mean_v=np.bincount(sector,weights=observable)/size
    V=observable-mean_v[sector]
    lhs=abs(np.dot(mu,V)); bound=2*np.max(np.abs(V))*math.sqrt(condvar)
    assert lhs<=bound+1e-14 and condvar<=D/2+1e-14
    # Incorrect grand-canonical centering would fail: a count-only density has zero swap energy.
    n0=(states==0).sum(axis=1);fv=(1+n0)/(1+n0).mean();Vwrong=n0/4-1/14
    wrong=float(np.mean(fv*Vwrong))
    assert abs(wrong-13/252)<1e-14
    assert all(np.array_equal(fv[index],fv) for index in swaps)
    return {'states':count,'directed_route_channels':4,'integer_uniform_stationarity_residual':0,
      'rates_min_max':[min(int(num.min()) for num in numerators)/12,max(int(num.max()) for num in numerators)/12],
      'rstar':rstar,'bare_dirichlet':D,'entropy_derivative_Euler_N8':hdot,'upper_bound_minus_2NrstarD':-2*8*rstar*D,
      'inhomogeneous_relative_entropy_decomposition_residual':abs(direct-decomposed),
      'conditional_sector_count':len(size),'conditional_V_expectation_abs':lhs,'conditional_CS_bound':bound,
      'conditional_variance_sqrtf':condvar,'ring_Poincare_bound_D_over_2':D/2,
      'wrong_grandcanonical_centering_countercontrol':{'swap_dirichlet':0,'nonzero_expectation':'13/252'},
      'scope':'One complete four-anchor physical route cycle and the actual fourteen labels/rates; not the complete three-dimensional finite generator.'}

def sector_gaps():
    # Bare four-cycle swaps: count-type relabeling reduces every fourteen-color sector to these partitions.
    answer=[]
    for partition in [(4,),(3,1),(2,2),(2,1,1),(1,1,1,1)]:
        base=[i for i,n in enumerate(partition) for _ in range(n)]
        states=sorted(set(itertools.permutations(base)));index={v:i for i,v in enumerate(states)}
        Q=s.zeros(len(states))
        for row,v in enumerate(states):
            for u in range(4):
                w=(u+1)%4;changed=list(v);changed[u],changed[w]=changed[w],changed[u]
                col=index[tuple(changed)];Q[row,col]+=1;Q[row,row]-=1
        ev=(-Q).eigenvals();nonzero=[a for a in ev if a!=0]
        gap=min(nonzero) if nonzero else None
        assert ev[0]==1
        if gap is not None:assert gap==2
        answer.append({'count_partition':partition,'arrangements':len(states),'gap':None if gap is None else str(gap),
                       'exact_eigenvalue_multiplicities':{str(k):v for k,v in ev.items()}})
    return answer

def geometry():
    G=np.array([[-2,-1,-1],[0,1,0],[0,0,1]],dtype=int)
    assert round(np.linalg.det(G))==-2
    rows=[]
    routes=[(1,0,0),(0,1,0),(0,0,1),(1,-1,0),(1,0,-1)]
    for N,ell in [(24,2),(40,4),(48,5),(80,9)]:
        assert N>8*ell
        indices=list(itertools.product(range(ell),repeat=3));m=ell**3
        block={tuple((G@np.array(r))%N) for r in indices}
        assert len(block)==m
        differences={tuple((G@np.array(r))%N) for r in itertools.product(range(1-ell,ell),repeat=3)}
        assert len(differences)==(2*ell-1)**3
        bond_counts=[]
        for i in range(3):
            target=tuple(G[:,i]%N)
            count=0
            for w in block:
                shift=(-np.array(w))%N
                shifted={tuple((np.array(b)+shift)%N) for b in block}
                if (0,0,0) in shifted and target in shifted:count+=1
            assert count==(ell-1)*ell**2<=m
            bond_counts.append(count)
        internal=[]
        for a in routes:
            a=np.array(a);valid=0
            for r in indices:
                r=np.array(r)
                if all(np.all((r+t*a>=0)&(r+t*a<ell)) for t in (-1,0,1,2)):valid+=1
            assert 1-valid/m<=6/ell
            internal.append(valid)
        rows.append({'N':N,'ell':ell,'m':m,'overlap_degree':len(differences)-1,'available_colors_8m':8*m,
                     'bond_multiplicities':bond_counts,'internal_four_context_anchors':internal})
    return rows

def tangent_cancellation():
    p=s.Matrix([R(i,105) for i in range(1,15)]);H=s.diag(*[1/x for x in p]);ones=s.ones(14,1)
    derivatives=[(s.eye(14)[:,a]-s.eye(14)[:,b])/d for a,b,d in [(0,7,11),(2,10,13),(5,12,17)]]
    As=[jac(p,eye[:,i]) for i in range(3)]
    pt=-sum((A*z for A,z in zip(As,derivatives)),s.zeros(14,1))
    coefficient=H*pt+sum((A.T*H*z for A,z in zip(As,derivatives)),s.zeros(14,1))
    assert len(set(coefficient))==1
    assert coefficient[0]!=0
    # A constant ambient remainder is harmless only on mass-zero variations.
    z=s.eye(14)[:,1]-s.eye(14)[:,9]
    assert (coefficient.T*z)[0]==0
    n=eye[:,0];A=As[0];K=Kmat(n);v=K*p;M=(p.T*v)[0];logp=p.applyfunc(s.log);eta=(p.T*logp)[0]
    F=R(2,3)*(p.multiply_elementwise(v)-p*M)
    gradq=R(2,3)*((logp+ones).multiply_elementwise(v-M*ones)+K*p.multiply_elementwise(logp)-(2*eta+1)*v)
    rhs=(derivatives[0].T*H*F)[0]
    lhs=(derivatives[0].T*(H*F+A.T*logp-gradq))[0]
    assert s.expand(lhs-rhs)==0
    return {'coefficient_is_constant_ambient_vector':str(coefficient[0]),'mass_zero_pairing':0,
            'constant_spatial_term_entropy_divergence_residual':0,
            'countercontrol':'The ambient coefficient is nonzero; requiring its componentwise vanishing would be an incorrect stronger cancellation.'}

def exponential_and_canonical():
    m=s.symbols('m',positive=True);alpha=R(1,224);chi=8*m
    assert s.simplify(2*alpha*chi-m/14)==0
    tail_integral=1+R(28,14)/(R(1,7)-R(1,14));assert tail_integral==29
    # Independent, nonidentically distributed categorical observations, exact rational probabilities.
    laws=[(R(1,2),R(1,3),R(1,6)),(R(1,5),R(1,2),R(3,10)),
          (R(2,7),R(3,7),R(2,7)),(R(1,4),R(1,4),R(1,2))]
    mean=sum((s.Matrix(p) for p in laws),s.zeros(3,1))/4
    expectation=0.;mass=R(0)
    for labels in itertools.product(range(3),repeat=4):
        probability=s.prod(laws[i][a] for i,a in enumerate(labels));mass+=probability
        counts=s.Matrix([labels.count(i) for i in range(3)])/4
        Y=4*sum((counts[i]-mean[i])**2 for i in range(3))
        expectation+=float(probability)*math.exp(float(Y/14))
    assert mass==1 and expectation<29
    # Hypergeometric four-site current against product law, with all boundary cases retained.
    K=Kmat(-eye[:,0]);rows=[]
    for counts in [(5,3),(1,7),(8,0)]:
        m0=sum(counts);chosen=(2,6);pop=[a for a,k in zip(chosen,counts) for _ in range(k)]
        total=0.;samples=0
        for positions in itertools.permutations(range(m0),4):
            l,a,b,r=[pop[i] for i in positions]
            hk=K[l,a]+K[a,r]-K[l,b]-K[b,r]
            total+=float((15+hk)/12)*(int(a==2)-int(b==2));samples+=1
        hyper=total/samples
        p=s.zeros(14,1)
        for a,k in zip(chosen,counts):p[a]=R(k,m0)
        sv=(R(2,3)/2*K)*(2*p)
        product=R(1,2)*(p.multiply_elementwise(sv)-p*(p.T*sv)[0])[2]
        failed=1-math.prod((m0-i)/m0 for i in range(4))
        assert failed<=6/m0
        assert abs(hyper-float(product))<=2*(19/12)*failed+1e-13
        rows.append({'counts':counts,'hypergeometric_current':hyper,'product_current':str(product),
                     'coupling_failure_probability':failed,'union_bound':6/m0})
    return {'alpha':'1/224','chi':'8m','Holder_exponent':'m/14','integrated_tail_bound':29,
            'nonidentical_four_draws_exponential_moment':expectation,'canonical_boundary_controls':rows}

def main():
    result={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'scope':'New independent finite controls for the complete supplied proof, before author smooth-time checker/results.',
            'versions':{'python':platform.python_version(),'numpy':np.__version__,'sympy':s.__version__}}
    for name,fn in [('entropy_cycle',entropy_cycle),('all_four_cycle_count_sector_gaps',sector_gaps),
                    ('finite_torus_block_geometry',geometry),('tangent_entropy_cancellation',tangent_cancellation),
                    ('product_exponential_and_canonical_bounds',exponential_and_canonical)]:
        result[name]=fn();print(name+' complete',flush=True)
    result['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    def encode(v):
        if isinstance(v,s.Integer):return int(v)
        if isinstance(v,s.Basic):return str(v)
        if isinstance(v,np.generic):return v.item()
        raise TypeError(type(v).__name__)
    with (HERE/'INDEPENDENT_RESULTS.json').open('x') as f:json.dump(result,f,indent=2,default=encode);f.write('\n')
    print('all independent groups complete',flush=True)

if __name__=='__main__':main()
