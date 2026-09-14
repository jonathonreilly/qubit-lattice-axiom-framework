"""Personal finite challenges for the entire positive-mixture construction.

Exact rational expansion is compared with direct Fejer Fourier coefficients.
This checks small graphs, not the uniform lattice theorem.
"""
from collections import defaultdict
from fractions import Fraction as F
import itertools
import json
import math
from pathlib import Path
import numpy as np


def canonical(rho):
    rho=tuple(rho)
    for value in rho:
        if value:
            return tuple(-x for x in rho) if value<0 else rho
    raise AssertionError('a nonempty disjoint merge cannot vanish')


def support(rho):
    return {i for i,x in enumerate(rho) if x}


def adjacent(a,b,neighbors):
    return any(j in neighbors[i] for i in support(a) for j in support(b))


def children(items,i,j):
    ra,ka,pa=items[i];rb,kb,pb=items[j]
    assert support(ra).isdisjoint(support(rb))
    rest=[item for index,item in enumerate(items) if index not in (i,j)]
    return [
        (F(1,3),rest+[(ra,3*ka,pa+1)]),
        (F(1,3),rest+[(rb,3*kb,pb+1)]),
        (F(1,6),rest+[(canonical(a-b for a,b in zip(ra,rb)),3*ka*kb,pa+pb+1)]),
        (F(1,6),rest+[(canonical(a+b for a,b in zip(ra,rb)),3*ka*kb,pa+pb+1)]),
    ]


def expand(items,neighbors,weight=F(1)):
    for i in range(len(items)):
        for j in range(i+1,len(items)):
            if adjacent(items[i][0],items[j][0],neighbors):
                for factor,new in children(items,i,j):
                    yield from expand(new,neighbors,weight*factor)
                return
    yield weight,items


def fejer_mixture(h,edge_count):
    weights=[2*F(h+1-k,h+1)/int(4*k*k) for k in range(1,h+1)]
    weights=[1-sum(weights)]+weights
    assert min(weights)>0 and sum(weights)==1
    for choices in itertools.product(range(h+1),repeat=edge_count):
        weight=math.prod(weights[k] for k in choices)
        items=[]
        for e,k in enumerate(choices):
            if k:
                rho=[0]*edge_count;rho[e]=k
                items.append((tuple(rho),4*k*k,0))
        yield weight,items


def square_test(h):
    # Counterclockwise boundary on four canonically oriented square edges.
    d=np.array([1,1,-1,-1],dtype=int)
    neighbors={i:set(range(4)) for i in range(4)}
    leaves=[];coefficients=defaultdict(F);count=0
    for outer,items in fejer_mixture(h,4):
        for inner,final in expand(items,neighbors):
            count+=1;weight=outer*inner
            assert len(final)<=1
            for rho,K,power in final:
                S=support(rho)
                assert power<=len(set.union(*(neighbors[i] for i in S)))-1
                assert K==3**power*math.prod(4*rho[i]**2 for i in S)
            leaves.append((weight,final))
            if final:
                rho,K,power=final[0]
                # Independent gauge constraint: incidence at each vertex.
                grad=np.array([[-1,1,0,0],[0,-1,1,0],[0,0,1,-1],[-1,0,0,1]])
                closed=np.array(rho)@grad
                if not np.any(closed):
                    assert np.array_equal(rho,rho[0]*d)
                    coefficients[rho[0]]+=weight*K
    assert sum(w for w,_ in leaves)==1
    expected={k:2*F(h+1-k,h+1)**4 for k in range(1,h+1)}
    assert dict(coefficients)==expected,(coefficients,expected)
    rng=np.random.default_rng(1427+h)
    maxerr=0.
    for phase in rng.uniform(-np.pi,np.pi,(17,4)):
        direct=math.prod(1+2*sum(float(F(h+1-k,h+1))*math.cos(k*x) for k in range(1,h+1)) for x in phase)
        expanded=sum(float(weight)*math.prod(1+K*math.cos(np.dot(rho,phase)) for rho,K,_ in items) for weight,items in leaves)
        maxerr=max(maxerr,abs(expanded-direct))
        assert abs(expanded-direct)<2e-11
    beta=.55;curvature_min=float('inf');largest_activity=0.;max_gaussian_error=0.
    for flux in np.linspace(-np.pi,np.pi,43):
        direct=1+sum(float(v)*math.exp(-2*np.pi*np.pi*beta*k*k)*math.cos(k*flux) for k,v in expected.items())
        transformed=0.
        for weight,items in leaves:
            if not items:
                transformed+=float(weight);continue
            rho,K,_=items[0]
            if np.any(np.array(rho)@grad):
                transformed+=float(weight);continue
            k=rho[0]
            # Rank-one square Q=d^T d. One selected edge kills the
            # renormalized frequency completely; the external phase stays.
            Q=np.outer(d,d);u=np.array([rho[0],0,0,0],dtype=float)
            assert np.array_equal(np.array(rho)-Q@u,np.zeros(4))
            z=K*math.exp(-2*np.pi*np.pi*beta*k*k)
            assert 0<z<.5
            largest_activity=max(largest_activity,z)
            value=1+z*math.cos(k*flux)
            first=-z*k*math.sin(k*flux);second=-z*k*k*math.cos(k*flux)
            curvature=second/value-(first/value)**2
            assert curvature>=-z/(1-z)*k*k-1e-12
            curvature_min=min(curvature_min,curvature)
            transformed+=float(weight)*value
        max_gaussian_error=max(max_gaussian_error,abs(direct-transformed))
        assert abs(direct-transformed)<2e-11
    return dict(fejer_order=h,positive_mixture_leaves=count,
                exact_closed_coefficients={str(k):str(v) for k,v in coefficients.items()},
                product_identity_max_error=maxerr,gaussian_identity_max_error=max_gaussian_error,
                largest_damped_factor_activity=largest_activity,
                smallest_sampled_component_curvature=curvature_min,
                initial_component_can_be_negative=(1+4*math.cos(math.pi)<0))


def ancestry_test():
    # Test arbitrary graph histories, including retention after earlier
    # mergers. This challenges the bound in terms of FINAL support rather
    # than the whole initial component. It is stronger than a total-size bound.
    rng=np.random.default_rng(4127);cases=0;largest_power=0
    for size in (7,13,23):
        for trial in range(500):
            graph={i:{i} for i in range(size)}
            for i,j in itertools.combinations(range(size),2):
                if rng.uniform()<.13:
                    graph[i].add(j);graph[j].add(i)
            initial=rng.integers(1,4,size)
            items=[]
            for i,k in enumerate(initial):
                r=[0]*size;r[i]=int(k);items.append((tuple(r),4*int(k)**2,0))
            while True:
                pairs=[(i,j) for i,j in itertools.combinations(range(len(items)),2) if adjacent(items[i][0],items[j][0],graph)]
                if not pairs:break
                i,j=pairs[int(rng.integers(len(pairs)))];choice=int(rng.integers(4))
                _,items=children(items,i,j)[choice]
            seen=set()
            for rho,K,power in items:
                S=support(rho);assert seen.isdisjoint(S);seen|=S
                neighbor_union=set.union(*(graph[i] for i in S))
                assert power<=len(neighbor_union)-1,(S,power,neighbor_union)
                assert K==3**power*math.prod(4*rho[i]**2 for i in S)
                largest_power=max(largest_power,power)
            for a,b in itertools.combinations(items,2):assert not adjacent(a[0],b[0],graph)
            cases+=1
    return dict(random_graph_branch_histories=cases,largest_amplitude_power=largest_power,
                qualification='Random finite histories supplement the explicit ancestry proof; they do not establish it.')


def affine_source_test():
    records=[]
    for beta in (.13,.4,.8,1.6):
        for shift in (0.,.17,.41,.5):
            x=np.arange(-60,61)+shift;weight=np.exp(-x*x/(2*beta));Z=weight.sum()
            mean=x@weight/Z;variance=x*x@weight/Z-mean*mean
            k=np.arange(-60,61);damping=np.exp(-2*np.pi*np.pi*beta*k*k)
            phase=np.exp(2j*np.pi*k*shift)
            theta=(damping@phase).real
            first=((2j*np.pi*k*damping)@phase).real
            second=((-4*np.pi*np.pi*k*k*damping)@phase).real
            curvature=second/theta-(first/theta)**2
            expected=beta+beta*beta*curvature
            assert abs(Z-np.sqrt(2*np.pi*beta)*theta)<1e-12
            assert abs(variance-expected)<1e-12
            records.append(dict(beta=beta,shift=shift,variance=float(variance),theta_source_variance=float(expected)))
    witness=next(r for r in records if r['beta']==.13 and r['shift']==.5)
    assert witness['variance']>1.9*witness['beta']
    return dict(source_identities=records,shifted_covariance_exceeds_beta=witness,
                qualification='The centered covariance upper bound does not extend to arbitrary affine cosets.')


def composite_annihilator_test():
    rows=[]
    matrices=[np.array([[2]]),np.array([[2,0,1],[0,3,2]]),np.array([[2,4],[4,8]])]
    for N in (2,4,6):
        for D in matrices:
            m,n=D.shape
            points=list(itertools.product(range(N),repeat=m))
            kernel=[x for x in points if np.all(D.T@np.array(x)%N==0)]
            image={tuple((D@np.array(v))%N) for v in itertools.product(range(N),repeat=n)}
            annihilator={x for x in points if all(np.dot(x,y)%N==0 for y in kernel)}
            assert image==annihilator
            rows.append(dict(N=N,matrix=D.tolist(),kernel_size=len(kernel),image_size=len(image)))
    assert rows[0]['matrix']==[[2]] and rows[0]['image_size']==1
    return rows


if __name__=='__main__':
    result=dict(status='personal_finite_ensemble_checks_pass',square=[square_test(h) for h in (1,2)],
                ancestry=ancestry_test(),affine_source=affine_source_test(),
                composite_annihilators=composite_annihilator_test(),
                limits='Finite exact checks of the ensemble construction, not a universal phase proof or an independent review.')
    Path(__file__).with_name('BLOCK7_ENSEMBLE_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
