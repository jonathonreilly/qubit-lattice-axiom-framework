#!/usr/bin/env python3
"""Exact finite-law and oriented-geometry challenges to the sparse-loop example.

No Hamiltonian measure is sampled. The all-volume and limiting statements are
carried by the written counterexample, not by these finite calculations.
"""
AUDIT_TIMEOUT_SEC=120
from collections import Counter,defaultdict
from fractions import Fraction as F
from itertools import combinations,permutations,product
from pathlib import Path
import hashlib,json,math,time


def shift(x,mu):
    y=list(x);y[mu]+=1;return tuple(y)


def boundary_face(x,axes,coefficient=1):
    i,j=axes
    return {(shift(x,i),j):coefficient,(x,j):-coefficient,
            (shift(x,j),i):-coefficient,(x,i):coefficient}


def divergence(edges):
    out=defaultdict(int)
    for (x,mu),value in edges.items():out[shift(x,mu)]+=value;out[x]-=value
    return {x:v for x,v in out.items() if v}


def face_vertices(x,axes):
    i,j=axes
    return {x,shift(x,i),shift(x,j),shift(shift(x,i),j)}


def geometry_checks():
    marks=[]
    for axes in combinations(range(4),2):
        other=[i for i in range(4) if i not in axes]
        for offsets in product((1,2),repeat=2):
            base=[1]*4
            for mu,value in zip(other,offsets):base[mu]=value
            for sign in (-1,1):marks.append((tuple(base),axes,sign))
    assert len(marks)==48
    symcases=0
    for perm in permutations(range(4)):
        for signs in product((-1,1),repeat=4):
            transform=lambda x:tuple(x[perm[a]] if signs[a]>0 else 3-x[perm[a]] for a in range(4))
            for base,axes,coefficient in marks:
                edges=boundary_face(base,axes,coefficient);mapped=defaultdict(int)
                for (x,mu),value in edges.items():
                    a,b=transform(x),transform(shift(x,mu));nu=next(i for i in range(4) if a[i]!=b[i])
                    if b[nu]>a[nu]:mapped[(a,nu)]+=value
                    else:mapped[(b,nu)]-=value
                vertices={transform(x) for x in face_vertices(base,axes)}
                newaxes=tuple(i for i in range(4) if len({x[i] for x in vertices})==2)
                newbase=tuple(min(x[i] for x in vertices) for i in range(4))
                expected=boundary_face(newbase,newaxes,1)
                sign=next(iter(mapped.values()))/next(expected[k] for k in mapped)
                assert sign in (-1,1)
                assert dict(mapped)=={k:int(sign)*v for k,v in expected.items()}
                assert (newbase,newaxes,int(sign)) in marks
                assert not divergence(mapped)
                symcases+=1
    # Choose various planes/offsets in adjacent blocks and inspect actual supports.
    allvertices=[];alledges=defaultdict(int);boxbounds=[]
    for index,r in enumerate(product(range(2),repeat=4)):
        base,axes,sign=marks[(index*7)%len(marks)]
        x=tuple(4*r[i]+base[i] for i in range(4))
        vertices=face_vertices(x,axes);allvertices.append(vertices)
        for e,val in boundary_face(x,axes,sign).items():alledges[e]+=val
        boxbounds.append([(min(v[i] for v in vertices)-1,max(v[i] for v in vertices)+1) for i in range(4)])
    assert not divergence(alledges)
    assert max(abs(v) for v in alledges.values())==1
    for i,j in combinations(range(len(allvertices)),2):
        assert min(max(abs(x[k]-y[k]) for k in range(4)) for x in allvertices[i] for y in allvertices[j])>=3
        assert any(boxbounds[i][k][1]<boxbounds[j][k][0] or boxbounds[j][k][1]<boxbounds[i][k][0] for k in range(4))
    return dict(single_block_marks=len(marks),hyperoctahedral_maps=384,oriented_cases=symcases,
                neighboring_blocks=len(allvertices),bad_vertices=sum(map(len,allvertices)),
                current_edges=len(alledges),maximum_current=1)


def moment_coefficients(L=2):
    sites=list(product(range(L),repeat=4));N=len(sites)
    # Each block sign is a distinct monomial in four families of independent signs.
    masks=[sum(1<<(nu*L+x[nu]) for nu in range(3)) for x in sites]
    coefficients=Counter()
    for a,b,c,d in product(range(N),repeat=4):
        if masks[a]^masks[b]^masks[c]^masks[d]==0:
            coefficients[len({a,b,c,d})]+=1
    expected={1:N,2:3*N*(N-1),4:(3*L*L-2*L)**4-3*N*N+2*N}
    assert dict(coefficients)==expected
    # A truly independent sign per block has no four-distinct contribution.
    independent=Counter()
    for a,b,c,d in product(range(N),repeat=4):
        if (1<<a)^(1<<b)^(1<<c)^(1<<d)==0:independent[len({a,b,c,d})]+=1
    assert independent[4]==0 and coefficients[4]>0
    return sites,masks,dict(coefficients),dict(independent)


def binomial_fourth(nplus,nminus,rho):
    result=F(0)
    for a in range(nplus+1):
        pa=math.comb(nplus,a)*rho**a*(1-rho)**(nplus-a)
        for b in range(nminus+1):
            pb=math.comb(nminus,b)*rho**b*(1-rho)**(nminus-b)
            result+=pa*pb*(a-b)**4
    return result


def exact_moment_checks():
    L=2;sites,masks,coeff,independent=moment_coefficients(L);N=len(sites)
    sign_sum_counts=Counter()
    for assignment in range(1<<(4*L)):
        values=[(-1)**((assignment&mask).bit_count()) for mask in masks]
        sign_sum_counts[sum(values)]+=1
    assert sum(sign_sum_counts.values())==2**(4*L)
    rows=[]
    for rho in (F(1,12),F(1,600),F(1,1200)):
        enumerated=F(0)
        for total,count in sign_sum_counts.items():
            enumerated+=F(count,2**(4*L))*binomial_fourth((N+total)//2,(N-total)//2,rho)
        normalized=enumerated/N**2
        polynomial=sum(F(value)*rho**degree for degree,value in coeff.items())/N**2
        formula=rho/N+3*rho*rho*(1-F(1,N))+rho**4*((3-F(2,L))**4-3+F(2,N))
        assert normalized==polynomial==formula
        cumulant=formula-3*rho*rho
        limit=78*rho**4
        assert limit>0
        rows.append(dict(rho=str(rho),fourth_moment=str(formula),fourth_cumulant=str(cumulant),
                         limiting_fourth_cumulant=str(limit)))
    return dict(L=L,sites=N,environment_assignments=2**(4*L),
                sign_sum_counts=dict(sign_sum_counts),ordered_tuple_coefficients=coeff,
                independent_sign_coefficients=independent,exact_moments=rows)


def analytic_scaling_checks():
    rows=[]
    for rho in (F(1,12),F(1,600)):
        for L in (2,8,32,128):
            N=L**4
            fourth=rho/N+3*rho*rho*(1-F(1,N))+rho**4*((3-F(2,L))**4-3+F(2,N))
            cumulant=fourth-3*rho*rho
            limit=78*rho**4
            rows.append(dict(rho=str(rho),L=L,variance=str(rho),source_l3_cubed=str(F(1,L*L)),
                             fourth_cumulant=str(cumulant),limit=str(limit),
                             # This is the proved lower bound, not a sampled MGF.
                             log_MGF_lower_at_t1=float(rho*L*L)-4*L*math.log(2)))
    return rows


def main():
    start=time.monotonic()
    out=dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope=__doc__,
             geometry=geometry_checks(),moments=exact_moment_checks(),scaling=analytic_scaling_checks(),
             status='PERSONAL_CHECKS_COMPLETED')
    out['elapsed_seconds']=time.monotonic()-start
    print(json.dumps(out,indent=2,sort_keys=True))


if __name__=='__main__':main()
