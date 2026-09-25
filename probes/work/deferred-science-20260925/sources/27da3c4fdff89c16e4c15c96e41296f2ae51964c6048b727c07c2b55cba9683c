"""Original local primitive/Gauss algebra and a separate three-state timing toy."""
from collections import Counter, deque, defaultdict
from fractions import Fraction
from itertools import product
from pathlib import Path
import json, math, time
import numpy as np
from scipy.linalg import expm


def primitive_control():
    side=6
    vertices=list(product(range(side),repeat=3))
    is_a=lambda v:sum(v)%2==0
    def neighbors(v):
        for axis in range(3):
            for sign in (-1,1):
                w=list(v);w[axis]=(w[axis]+sign)%side;yield tuple(w)
    def edge(x,y):
        return (x,y) if is_a(x) else (y,x)
    def key(flow):
        return tuple(sorted((a,b,int(v)) for (a,b),v in flow.items() if v))
    def divergence(flow):
        out=Counter()
        for (x,y),v in flow.items():out[x]+=v;out[y]-=v
        return {x:v for x,v in out.items() if v}
    def path(start,end):
        before={start:None};q=deque([start])
        while end not in before:
            x=q.popleft()
            for y in neighbors(x):
                if y not in before:before[y]=x;q.append(y)
        route=[end]
        while route[-1]!=start:route.append(before[route[-1]])
        return route[::-1]
    a=(0,0,0);d=(1,1,0);h=(2,2,0)
    c=(1,0,0);e=(0,1,0);b=(5,0,0)
    fixed=[(0,5,0),(0,0,1),(0,0,5)]
    common=Counter();routes=[]
    for start,end in [(d,fixed[0]),(h,fixed[1]),(h,fixed[2])]:
        route=path(start,end);routes.append(route)
        for x,y in zip(route,route[1:]):common[edge(x,y)]+=(-1 if is_a(x) else 1)
    expected={d:-1,h:-2,**{v:1 for v in fixed}}
    assert divergence(common)==expected
    loop=Counter({(a,c):1,(d,c):-1,(d,e):1,(a,e):-1})
    baseline={v:1 for v in vertices if is_a(v)}
    def gauss(charges,flow):
        delta={v:charges.get(v,0)-baseline.get(v,0) for v in vertices}
        delta={v:q for v,q in delta.items() if q}
        assert divergence(flow)==delta
    rows=[];outputs_by_sign={}
    for sigma in (-1,1):
        outputs=[]
        for occupied,empty,phase in [(c,e,1),(e,c,-1)]:
            initial=baseline.copy();initial[d]=initial[h]=-1
            for v in fixed+[occupied]:initial[v]=1
            incoming=common.copy();incoming[d,occupied]-=1
            gauss(initial,incoming)
            retained=[];blocked_birth=0
            for destination in neighbors(a):
                if initial.get(destination,0):continue
                after=initial.copy();charge=after.pop(a);after[destination]=charge
                flow=incoming.copy();flow[a,destination]-=charge
                if after.get(b,0):blocked_birth+=1;continue
                assert not after.get(a,0)
                after[a]=sigma;after[b]=-sigma;flow[a,b]+=sigma
                gauss(after,flow)
                retained.append((tuple(sorted(after.items())),key(flow),phase))
            assert len(retained)==1 and blocked_birth==1
            outputs+=retained
            for winding in range(-2,3):
                shifted=incoming.copy()
                for link,value in loop.items():shifted[link]+=winding*value
                gauss(initial,shifted)
            rows.append(dict(sigma=sigma,initial_occupied_variable=occupied,
                             initial_records=len(initial),output_records=len(dict(retained[0][0])),
                             retained_paths=1,outward_to_birth_site_rejected=1,
                             physical_flux_cases_checked=5))
        assert outputs[0][0]==outputs[1][0]
        coefficients=Counter()
        for left,right in product(outputs,repeat=2):
            fleft=Counter({(x,y):v for x,y,v in left[1]})
            fright=Counter({(x,y):v for x,y,v in right[1]})
            diff=Counter(fright)
            for link,value in fleft.items():diff[link]-=value
            coefficients[key(diff)]+=Fraction(left[2]*right[2],2)
        negative=Counter({link:-value for link,value in loop.items()})
        assert coefficients==Counter({():Fraction(1),key(loop):Fraction(-1,2),key(negative):Fraction(-1,2)})
        outputs_by_sign[str(sigma)]=dict(identity='1',cycle='-1/2',inverse_cycle='-1/2',
                                       dephased_identity='1',dephased_cycle='0')
    return dict(scope='Exact original selected primitive on the side-six cubic graph; no full Hamiltonian propagation.',
                common_flow=key(common),common_flow_paths=routes,rows=rows,
                effects=outputs_by_sign,gauss_checks='both charged branches and every listed loop flux satisfy div E=q-1_A')


def timing_probability(g,b,one,order):
    q,w=np.polynomial.hermite.hermgauss(order)
    dark=np.array([1.,-1.])/math.sqrt(2)
    h=np.diag([1.,-1.])/(g*g)
    values=[]
    for x in q:
        angle=math.sqrt(2)*g*x
        jump=np.array([np.exp(.5j*angle),np.exp(-.5j*angle)])
        loss=np.outer(jump.conj(),jump)
        final=expm(b*(-1j*h-.5*loss))@dark
        probability=1-float(np.vdot(final,final).real)
        values.append(probability*(2*x*x if one else 1.))
    return float(np.dot(w,values)/math.sqrt(math.pi))


def timing_control():
    rows=[];max_refinement=0.
    for g in (.4,.2,.1,.05,.025):
        for exponent in (3.5,2.):
            b=g**exponent
            vals=[]
            for one in (False,True):
                coarse=timing_probability(g,b,one,24)
                fine=timing_probability(g,b,one,32)
                max_refinement=max(max_refinement,abs(coarse-fine)/(b*g*g))
                assert abs(coarse-fine)<2e-13
                vals.append(fine)
            assert vals[1]>vals[0]
            rows.append(dict(g=g,window_exponent=exponent,window=b,
                             vacuum_probability=vals[0],one_probability=vals[1],
                             vacuum_over_b_g2=vals[0]/(b*g*g),
                             one_over_b_g2=vals[1]/(b*g*g),
                             excess_over_b_g2=(vals[1]-vals[0])/(b*g*g)))
    small=rows[-2]
    assert abs(small['vacuum_over_b_g2']-.5)<.025
    assert abs(small['excess_over_b_g2']-1)<.003
    assert rows[-1]['vacuum_over_b_g2']>100
    return dict(scope='Separate two coherent input states and one absorbing state at each Gaussian angle. '
                      'kappa=tau=1, matter splitting g^-2, one selected jump and its full loss. '
                      'No cubic electric term, Gauss constraint, other original channels or microscopic limit in this timing toy.',
                rows=rows,maximum_scaled_quadrature_refinement=max_refinement,
                no_uniform_optimal_window_claim=True)


def main():
    t=time.perf_counter()
    data=dict(primitive=primitive_control(),separate_timing=timing_control(),
              elapsed_seconds=time.perf_counter()-t,
              evidence_limit='Primitive algebra and separate finite timing model only, not an empirical detector.')
    print(json.dumps(data,indent=2,allow_nan=False))


if __name__=='__main__':main()
