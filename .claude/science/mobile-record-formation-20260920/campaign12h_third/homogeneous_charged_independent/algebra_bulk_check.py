"""Exact bulk counts, neutral physical fields, birth algebra and resonant control."""
from collections import Counter, deque
from datetime import datetime, timezone
from fractions import Fraction as F
from hashlib import sha256
from itertools import product, combinations
from pathlib import Path
import json, math
import sympy as sp

HERE=Path(__file__).resolve().parent


def torus(d, side=6):
    vertices=list(product(range(side),repeat=d));idx={x:i for i,x in enumerate(vertices)}
    edges=[];oriented={};adj=[set() for _ in vertices]
    for i,x in enumerate(vertices):
        for mu in range(d):
            y=list(x);y[mu]=(y[mu]+1)%side;j=idx[tuple(y)]
            oriented[(i,j)]=(len(edges),1);oriented[(j,i)]=(len(edges),-1)
            edges.append((i,j));adj[i].add(j);adj[j].add(i)
    checker={i for i,x in enumerate(vertices) if sum(x)%2==0}
    return vertices,idx,edges,oriented,adj,checker


def energy(edges, occupied):
    value=sum((int(x in occupied)+int(y in occupied)-1)**2 for x,y in edges)
    assert value%2==0
    return value//2


def divergence(edges,electric,V):
    result=[0]*V
    for (x,y),m in zip(edges,electric):result[x]+=m;result[y]-=m
    return result


def bulk(d):
    vertices,idx,edges,oriented,adj,checker=torus(d)
    V=len(vertices);M=len(edges);alpha=2*d-1
    assert energy(edges,checker)==0 and len(checker)==V//2
    aedges=[(x,y) if x in checker else (y,x) for x,y in edges]
    counts=Counter();examples={}
    for i,j in combinations(range(M),2):
        x,y=aedges[i];u,v=aedges[j]
        if len({x,y,u,v})<4:
            counts['meeting']+=1;continue
        w=int(v in adj[x])+int(y in adj[u]);counts[str(w)]+=1
        examples.setdefault(w,(i,j))
    assert counts['meeting']==V*d*alpha
    assert counts['2']==V*d*(d-1)
    assert counts['1']==d*V*(alpha*alpha-2*(d-1))
    observed=[]
    for w,(i,j) in sorted(examples.items()):
        x,y=aedges[i];u,v=aedges[j]
        one=checker-{x}|{y};two=checker-{x,u}|{y,v}
        e1=energy(edges,one);e2=energy(edges,two)
        assert e1==alpha and e2==2*alpha-w
        observed.append({'cross_edges':w,'first_energy':e1,'second_energy':e2,
                         'hopped_edges':[list(edges[i]),list(edges[j])]})
    diagonal=(F(M)+2*counts['meeting']-F(2,2*alpha-1)*counts['1']-F(4,2*alpha-2)*counts['2'])/alpha**3
    formula=F(2*d*(alpha*alpha-1),alpha**3*(2*alpha-1))*V
    assert diagonal==formula

    # Neutral charges, paired by disjoint two-edge paths, then a divergence-free
    # electric modification. All assignments are made geometrically, not from
    # the coefficient formula being tested.
    charge=[0]*V;electric=[0]*M
    for x in vertices:
        if sum(x)%2 or x[0]%2:continue
        y=list(x);y[0]=(y[0]+1)%6;y=tuple(y)
        z=list(y);z[1]=(z[1]+1)%6;z=tuple(z)
        charge[idx[x]]=1;charge[idx[z]]=-1
        for p,q in ((idx[x],idx[y]),(idx[y],idx[z])):
            ei,sign=oriented[p,q];electric[ei]+=sign
    # Add a circulation of strength two on an independently chosen plaquette.
    square=[(0,)*d,tuple(1 if i==0 else 0 for i in range(d)),
            tuple(1 if i in (0,1) else 0 for i in range(d)),
            tuple(1 if i==1 else 0 for i in range(d))]
    for x,y in zip(square,square[1:]+square[:1]):
        ei,sign=oriented[idx[x],idx[y]];electric[ei]+=2*sign
    assert divergence(edges,electric,V)==charge
    assert sum(charge)==0 and sum(x*x for x in charge)==V//2
    spin=max(abs(m) for m in electric)+1;cs=spin*(spin+1)
    linear=0;norms=[]
    for (tail,head),m in zip(edges,electric):
        occupied=tail if tail in checker else head
        eta=1 if occupied==tail else -1
        linear+=eta*charge[occupied]*m
        norms.append(1-F(m*m-eta*charge[occupied]*m,cs))
    assert linear==V//2
    E2=sum(m*m for m in electric)
    assert sum(norms)==M-F(E2-V//2,cs)
    return {'dimension':d,'side':6,'volume':V,'edge_count':M,'pair_counts':dict(counts),
            'actual_B_energies':observed,'unit_shift_fourth_diagonal_total':str(diagonal),
            'unit_shift_fourth_diagonal_per_site':str(diagonal/V),
            'physical_second_order':{'spin':spin,'charge_total':sum(charge),
                'number_records':V//2,'electric_square_sum':E2,'charge_linear_sum':linear,
                'sum_squared_first_hop_weights':str(sum(norms))},
            'all_bulk_identities_exact':True}


def resonant_example():
    vertices,idx,edges,oriented,adj,checker=torus(2)
    V=len(vertices);found=None
    for mult in range(1,V):
        if math.gcd(mult,V)!=1:continue
        occ={i for i in range(V) if (mult*i+3)%V < V//2}
        for x in sorted(occ):
            for y in sorted(adj[x]-occ):
                after=occ-{x}|{y}
                if energy(edges,occ)==energy(edges,after):
                    found=(occ,x,y,after,mult);break
            if found:break
        if found:break
    assert found is not None
    occ,x,y,after,mult=found
    charge=[0]*V
    for j,z in enumerate(sorted(occ)):charge[z]=1 if j<len(occ)//2 else -1
    parent={0:None};order=[0];queue=deque([0])
    while queue:
        z=queue.popleft()
        for w in sorted(adj[z]):
            if w not in parent:parent[w]=z;order.append(w);queue.append(w)
    subtree=charge.copy();electric=[0]*len(edges)
    for z in reversed(order[1:]):
        p=parent[z];ei,sign=oriented[z,p]
        electric[ei]=sign*subtree[z];subtree[p]+=subtree[z]
    assert divergence(edges,electric,V)==charge
    assert sum(charge)==0
    spin=max(abs(m) for m in electric)+1
    ei,sign=oriented[x,y];newE=electric.copy();newE[ei]-=sign*charge[x]
    newQ=charge.copy();newQ[y]=newQ[x];newQ[x]=0
    assert divergence(edges,newE,V)==newQ
    assert max(abs(m) for m in newE)<=spin
    assert energy(edges,occ)==energy(edges,after)
    return {'dimension':2,'side':6,'occupation_rule_multiplier':mult,
            'occupied_vertex_indices':sorted(occ),'hop_vertex_indices':[x,y],
            'hop_coordinates':[list(vertices[x]),list(vertices[y])],
            'before_B':energy(edges,occ),'after_B':energy(edges,after),
            'N':len(occ),'charge_total':sum(charge),'spin_with_nonzero_hop':spin,
            'electric_word':electric,'charge_word':charge,
            'consequence':'The full normal form has a nonzero first-order B-resonant hopping term away from the code. A previous O(V0 epsilon^2) full-space velocity cannot be reused without another argument.'}


def birth_algebra():
    output=[]
    q=sp.diag(0,1,-1);vac=sp.diag(1,0,0);I3=sp.eye(3)
    creates=[]
    for pos in (1,2):
        a=sp.zeros(3);a[pos,0]=1;creates.append(a)
    for spin in (1,2,3):
        cs=spin*(spin+1);size=2*spin+1
        E=sp.diag(*range(-spin,spin+1));U=sp.zeros(size)
        for k,m in enumerate(range(-spin,spin)):
            U[k+1,k]=sp.sqrt(1-sp.Rational(m*(m+1),cs))
        vp=sp.kronecker_product(creates[0],creates[1],U)
        vm=sp.kronecker_product(creates[1],creates[0],U.T)
        gx=sp.kronecker_product(I3,I3,E)-sp.kronecker_product(q,I3,sp.eye(size))
        gy=-sp.kronecker_product(I3,I3,E)-sp.kronecker_product(I3,q,sp.eye(size))
        assert gx*vp==vp*gx and gx*vm==vm*gx
        assert gy*vp==vp*gy and gy*vm==vm*gy
        resolved=vp.T*vp+vm.T*vm
        coherent=vp+sp.I*vm
        desired=sp.kronecker_product(vac,vac,2*(sp.eye(size)-E**2/cs))
        assert sp.simplify(resolved-desired)==sp.zeros(9*size)
        assert sp.simplify(coherent.conjugate().T*coherent-desired)==sp.zeros(9*size)
        assert sp.simplify(vp.T*vm)==sp.zeros(9*size)
        output.append({'spin':spin,'dimension':9*size,'Gauss_commutators_zero':True,
                       'resolved_and_one_coherent_jump_loss_equal':True,
                       'loss_on_empty_edge_in_E_order':list(map(str,[desired[i,i] for i in range(size)]))})
    return output


def scaling():
    alpha,cs,K,J=sp.symbols('alpha C K J',positive=True)
    epsilon2=J*alpha*(alpha-1)/(2*K*cs)
    V0=2*K*K*cs*cs/(J*(alpha-1))
    t2=epsilon2*V0*V0
    assert sp.simplify(t2/(alpha*V0*cs)-K)==0
    assert sp.simplify(2*t2*t2/(V0**3*alpha**2*(alpha-1))-J)==0
    return {'epsilon_squared':str(epsilon2),'V0':str(V0),
            'full_space_velocity':'O(V0 epsilon)=O(epsilon^-3), not O(epsilon^-2)',
            'chosen_normal_form_order':'m=3d+6',
            'chosen_birth_rate':'beta0 epsilon^(3d)',
            'remainder_after_cone_power':3,
            'birth_source_after_cone_power':1,
            'code_higher_order_power':2}


def main():
    result={'created_utc':datetime.now(timezone.utc).isoformat(),'status':'PASS',
            'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'bulk':[bulk(d) for d in (2,3)],'resonant_control':resonant_example(),
            'birth_algebra':birth_algebra(),'scaling':scaling(),
            'method':'Independent exact integer/rational counts, complete local operator algebra; no author imports.'}
    data=json.dumps(result,indent=2)+'\n';target=HERE/'ALGEBRA_BULK_RESULTS.json'
    assert not target.exists();target.write_text(data);print(data,end='')


if __name__=='__main__':main()
