#!/usr/bin/env python3
"""Independent signed-fiber, integer singlet-column and local-spin controls.

No author code is imported. Spin operators are assembled as permutations of
fixed-magnetization bit strings; cover columns are integer signed supports.
"""
from pathlib import Path
from itertools import product, combinations, permutations
from math import comb, factorial
import json
import numpy as np
import sympy as s

OUT=Path(__file__).resolve().parent

def geometry(shape):
    coords=list(product(*[range(n) for n in shape]));idx={x:i for i,x in enumerate(coords)}
    edges=[];faces=[];d=len(shape)
    for x in coords:
        for i in range(d):
            if x[i]+1<shape[i]:
                y=list(x);y[i]+=1;edges.append(tuple(sorted((idx[x],idx[tuple(y)]))))
        for i,j in combinations(range(d),2):
            if x[i]+1<shape[i] and x[j]+1<shape[j]:
                y=list(x);y[i]+=1;z=y.copy();z[j]+=1;w=list(x);w[j]+=1
                faces.append((idx[x],idx[tuple(y)],idx[tuple(z)],idx[tuple(w)]))
    black={i for i,x in enumerate(coords) if sum(x)%2==0}
    return coords,edges,faces,black

def matchings(V,edges):
    neighbors={v:[] for v in range(V)}
    for a,b in edges:neighbors[a].append(b);neighbors[b].append(a)
    def rec(left):
        if not left:yield ();return
        a=min(left)
        for b in neighbors[a]:
            if b in left:
                for rem in rec(left-{a,b}):yield tuple(sorted(((min(a,b),max(a,b)),)+rem))
    return sorted(rec(set(range(V))))

def spins(V,k):return [sum(1<<i for i in c) for c in combinations(range(V),k)]

def columns(V,covers,black):
    basis=spins(V,V//2);row={b:i for i,b in enumerate(basis)};D=s.zeros(len(basis),len(covers))
    for j,M in enumerate(covers):
        for bits in product([0,1],repeat=V//2):
            mask=0
            for bit,(a,b) in zip(bits,M):
                if a not in black:a,b=b,a
                mask|=(bit<<a)|((1-bit)<<b)
            D[row[mask],j]=(-1)**sum(bits)
    return basis,row,D

def overlay_loops(V,M,P):
    neighbors=[set() for _ in range(V)]
    for a,b in M+P:neighbors[a].add(b);neighbors[b].add(a)
    left=set(range(V));n=0
    while left:
        stack=[left.pop()];n+=1
        while stack:
            current=stack.pop()
            for v in neighbors[current]&left:left.remove(v);stack.append(v)
    return n

def spin_permutation(V,cycle):
    mapping=list(range(V))
    for a,b in zip(cycle,cycle[1:]+cycle[:1]):mapping[a]=b
    return mapping

def action_on_columns(D,basis,row,perms):
    result=s.zeros(*D.shape)
    for perm in perms:
        for r,mask in enumerate(basis):
            moved=sum(((mask>>a)&1)<<b for a,b in enumerate(perm));target=row[moved]
            for j in range(D.cols):result[target,j]+=D[r,j]
    return result

def qdm(covers,faces):
    idx={M:i for i,M in enumerate(covers)};A=s.zeros(len(covers));F=s.zeros(len(covers))
    for j,M in enumerate(covers):
        m=set(M)
        for face in faces:
            a,b,c,d=face;first={tuple(sorted(e)) for e in [(a,b),(c,d)]};second={tuple(sorted(e)) for e in [(b,c),(d,a)]}
            old,new=(first,second) if first<=m else (second,first)
            if old<=m:
                P=tuple(sorted((m-old)|new));A[idx[P],j]+=1;F[j,j]+=1
    assert A==A.T
    return A,F

def local_graph_control(name,shape):
    coords,edges,faces,black=geometry(shape);V=len(coords);K=V//2;covers=matchings(V,edges)
    basis,row,D=columns(V,covers,black);Gint=D.T*D;G=Gint/2**K
    assert Gint.rank()==len(covers)
    assert G==s.Matrix([[s.Rational(2)**(overlay_loops(V,M,P)-K) for P in covers] for M in covers])
    inverse=Gint.inv(method='DM');A,F=qdm(covers,faces)
    tc=G*A-A*G;vc=G*F-F*G
    constraints=s.Matrix.hstack(s.Matrix(list(vc)),s.Matrix(list(-tc)))
    Wnn=action_on_columns(D,basis,row,[spin_permutation(V,list(e)) for e in edges])
    perms=[]
    for face in faces:perms.extend([spin_permutation(V,list(face)),spin_permutation(V,list(reversed(face)))])
    Wring=action_on_columns(D,basis,row,perms)
    Snn=D.T*Wnn;Sring=D.T*Wring
    Rnn=Wnn.T*Wnn-Snn.T*inverse*Snn
    Rring=Wring.T*Wring-Sring.T*inverse*Sring
    Rcross=Wnn.T*Wring-Snn.T*inverse*Sring
    a=s.trace(Rnn)/2**K;b=s.trace(Rcross)/2**K;c=s.trace(Rring)/2**K
    alpha=-b/a if a else None;minimum=c-b*b/a if a else c
    if name=='square':
        assert constraints.rank()==0 and a==b==c==0
        # Singlet-edge readout from its physical swap definition.
        swap=action_on_columns(D,basis,row,[spin_permutation(V,list(edges[0]))])
        Pedge=(D-swap)/2;plus=D*s.ones(D.cols,1)
        coherent=(plus.T*((D-swap)*s.ones(D.cols,1)/2))[0]/(plus.T*plus)[0]
        incoherent=s.trace(D.T*Pedge)/(D.cols*2**K)
        occupation=sum(edges[0] in M for M in covers)/len(covers)
        assert coherent==s.Rational(3,4) and incoherent==s.Rational(5,8) and occupation==.5
    if name=='ladder6':
        assert constraints.rank()==1 and vc/2-tc==s.zeros(len(covers))
        H=F/2-A;lift=D*H*inverse*D.T
        assert lift==lift.T and lift*D==D*H
        assert alpha==-1 and minimum==0
    if name=='cube':
        assert constraints.rank()==2 and alpha==-2 and minimum==0
        assert (a,b,c)==(5,10,20) and Rnn.rank()==Rring.rank()==1
    if name=='ladder8':
        assert alpha==-s.Rational(21,23) and minimum==s.Rational(33,46)
        assert a-2*b+c==s.Rational(3,4)
    if name=='patch12':
        assert len(covers)==32 and alpha==-s.Rational(29041,21729)
        assert minimum==s.Rational(348331597,3911220)
        assert (a,c)==(s.Rational(7243,120),s.Rational(1575,8))
        assert (Rnn.rank(),Rring.rank())==(24,27)
    result=dict(name=name,shape=shape,vertices=V,edges=len(edges),plaquettes=len(faces),covers=len(covers),spin_sector_dimension=len(basis),
        exact_cover_Gram_rank=Gint.rank(),qdm_metric_constraint_rank=constraints.rank(),
        nn_leakage_rank=Rnn.rank(),ring_leakage_rank=Rring.rank(),
        nn_leakage_norm_squared=str(a),cross_leakage_inner_product=str(b),ring_leakage_norm_squared=str(c),
        optimal_nn_coefficient=None if alpha is None else str(alpha),minimal_combination_leakage_squared=str(minimum),
        computation='Integer singlet columns in the zero-magnetization basis, exact rational small Gram inverse; no author matrices imported.')
    if name=='square':result['edge_readout']={'coherent':str(coherent),'incoherent':str(incoherent),'classical_matching_occupation':'1/2'}
    return result,dict(V=V,edges=edges,faces=faces,black=black,covers=covers,basis=basis,row=row,D=D,Wnn=Wnn,Wring=Wring,inverse=inverse)

def signed_fibers(data):
    V=data['V'];K=V//2;black=data['black'];covers=data['covers'];row=data['row'];D=data['D']
    frames=[(s.Matrix([s.Rational(3,5),4*s.I/5]),s.Matrix([4*s.I/5,s.Rational(3,5)])),
            (s.Matrix([s.Rational(5,13),s.Rational(12,13)]),s.Matrix([-s.Rational(12,13),s.Rational(5,13)])),
            (s.Matrix([s.Rational(1,3)+2*s.I/3,s.Rational(2,3)]),s.Matrix([-s.Rational(2,3),s.Rational(1,3)-2*s.I/3]))]
    for u,v in frames:assert s.simplify(s.Matrix.hstack(u,v).det())==1 and s.simplify((u.H*u)[0])==1 and s.simplify((u.H*v)[0])==0
    all_fibers={};phase=s.I
    for j,M in enumerate(covers):
        fiber=[];total=s.zeros(2**V,1);phased=s.zeros(2**V,1)
        for assignment in permutations(range(K)):
            for signs in product([0,1],repeat=K):
                record=[None]*V;vectors=[None]*V;sgn=(-1)**sum(signs)
                for key,flip,(a,b) in zip(assignment,signs,M):
                    if a not in black:a,b=b,a
                    u,v=frames[key];vectors[a]=[u,v][flip];vectors[b]=[v,u][flip]
                    record[a]=(key,flip);record[b]=(key,1-flip)
                vec=vectors[-1]
                for t in reversed(vectors[:-1]):vec=s.kronecker_product(vec,t)
                total+=sgn*vec;phased+=sgn*phase*vec
                fiber.append((tuple(record),sgn))
        assert len(set(r for r,sgn in fiber))==2**K*factorial(K)
        target=s.zeros(2**V,1)
        for mask,r in row.items():target[mask]=factorial(K)*D[r,j]
        assert (total-target).applyfunc(s.simplify)==s.zeros(2**V,1)
        assert (phased-phase*target).applyfunc(s.simplify)==s.zeros(2**V,1)
        all_fibers[M]=dict(fiber)
    rotations=0
    for M,fiber in all_fibers.items():
        for face in data['faces']:
            old={e for e in M if set(e)<=set(face)}
            if len(old)!=2:continue
            for cycle in [face,tuple(reversed(face))]:
                perm=spin_permutation(V,list(cycle));P=tuple(sorted(tuple(sorted((perm[a],perm[b]))) for a,b in M));seen=set()
                for record,sgn in fiber.items():
                    target=[None]*V
                    for a,b in enumerate(perm):target[b]=record[a]
                    target=tuple(target);seen.add(target)
                    assert all_fibers[P][target]==sgn
                assert seen==set(all_fibers[P]);rotations+=1
    return dict(vertices=V,covers=len(covers),marked_states=sum(map(len,all_fibers.values())),signed_rotation_bijections=rotations,
        exact_product_frame_sum_factor=factorial(K),normalized_intertwiner_factor=f'sqrt({factorial(K)})',
        representative_phase_is_common=True)

def cube_parent(data):
    V=data['V'];stars=[tuple(sorted({v}|{b if a==v else a for a,b in data['edges'] if a==v or b==v})) for v in range(V)]
    assert all(len(star)==4 for star in stars)
    rows=[];globalgap=None;zero_sector=None
    for k in range(V+1):
        basis=spins(V,k);idx={mask:i for i,mask in enumerate(basis)};H=s.zeros(len(basis))
        for star in stars:
            maskstar=sum(1<<v for v in star);P=s.zeros(len(basis))
            for col,mask in enumerate(basis):
                weight=(mask&maskstar).bit_count();outside=mask&~maskstar
                for chosen in combinations(star,weight):
                    target=outside|sum(1<<v for v in chosen);P[idx[target],col]+=s.Rational(1,comb(4,weight))
            assert P==P.T and P*P==P
            if k==V//2:assert P*data['D']==s.zeros(len(basis),len(data['covers']))
            H+=P
        assert all((12*x).q==1 for x in H)
        nullity=len(basis)-H.rank()
        eig=np.linalg.eigvalsh(np.array(H.tolist(),dtype=float));positive=eig[eig>1e-9]
        gap=float(positive.min()) if len(positive) else None
        if gap is not None:globalgap=gap if globalgap is None else min(globalgap,gap)
        rows.append(dict(number_down=k,dimension=len(basis),exact_kernel_dimension=nullity,finite_numerical_positive_gap=gap))
        if k==4:zero_sector=H
    assert [r['exact_kernel_dimension'] for r in rows]==[0,0,0,3,13,3,0,0,0]
    Z=s.Matrix.hstack(*zero_sector.nullspace())
    D=data['D'];inv=data['inverse']
    for W in [data['Wnn'],data['Wring']]:
        leakage=W-D*inv*D.T*W
        assert Z.T*leakage==s.zeros(Z.cols,W.cols)
    assert 0.61257<globalgap<0.61258
    return dict(stars=len(stars),star_size=4,exact_parent_kernel_dimension=sum(r['exact_kernel_dimension'] for r in rows),
        exact_cover_span_dimension=len(data['covers']),kernel_su2_multiplicities={'spin0':10,'spin1':3},
        magnetization_sectors=rows,finite_numerical_gap=globalgap,
        nn_and_ring_leakage_orthogonal_to_entire_parent_kernel=True,
        scope='Finite open cube. No assertion about infinite-volume gap or equality of ground space with cover span.')

if __name__=='__main__':
    target=OUT/'SINGLET_LOCAL_RESULTS.json';assert not target.exists()
    results={'local_graphs':[],'signed_fibers':[]}
    for name,shape in [('square',(2,2)),('ladder6',(2,3)),('cube',(2,2,2)),('ladder8',(2,4)),('patch12',(2,2,3))]:
        result,data=local_graph_control(name,shape);results['local_graphs'].append(result);print(json.dumps(result),flush=True)
        if name in ['square','ladder6']:
            result=signed_fibers(data);results['signed_fibers'].append(result);print('Signed fibers '+json.dumps(result),flush=True)
        if name=='cube':
            results['cube_parent']=cube_parent(data);print('Cube parent '+json.dumps(results['cube_parent']),flush=True)
    target.write_text(json.dumps(results,indent=2)+'\n')
