#!/usr/bin/env python3
"""Exact exploratory singlet-fiber lift, overlap, and Hamiltonian controls."""
from pathlib import Path
import hashlib,importlib.util,itertools,json,math
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent
src=HERE/'geometric_quantum_lift_check.py'
spec=importlib.util.spec_from_file_location('quantum_lift',src);q=importlib.util.module_from_spec(spec);spec.loader.exec_module(q)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()

def vb_column(n,M,black):
    result=[]
    for bits in itertools.product([0,1],repeat=n):
        value=1
        for e in M:
            b,w=e if e[0] in black else e[::-1]
            if bits[b]==bits[w]:value=0;break
            value*=1 if bits[b]==0 else -1
        result.append(value)
    return s.Matrix(result)/s.sqrt(2**(n//2))

def components(n,edges):
    adj=[set() for _ in range(n)]
    for u,v in edges:adj[u].add(v);adj[v].add(u)
    unseen=set(range(n));count=0
    while unseen:
        count+=1;u=min(unseen);seen={u};todo=[u]
        for v in todo:
            for z in adj[v]-seen:seen.add(z);todo.append(z)
        unseen-=seen
    return count

def main():
    out=HERE/'geometric_singlet_fiber_checks';out.mkdir(exist_ok=False)
    cube_edges={(a,b) for a,b in itertools.combinations(range(8),2) if (a^b) in [1,2,4]}
    cube_loops=[]
    for i,j in itertools.combinations([1,2,4],2):
        for a in range(8):
            if a&i==0 and a&j==0:cube_loops.append((a,a^i,a^i^j,a^j))
    cases=[('square',4,{(0,1),(1,2),(2,3),(0,3)},[(0,1,2,3)],{0,2}),
           ('ladder6',6,{(0,1),(1,2),(3,4),(4,5),(0,3),(1,4),(2,5)},[(0,1,4,3),(1,2,5,4)],{0,2,4}),
           ('cube8',8,cube_edges,cube_loops,{0,3,5,6})]
    z=[s.Matrix([1,0]),s.Matrix([0,1])]
    x=[s.Matrix([1,1])/s.sqrt(2),s.Matrix([-1,1])/s.sqrt(2)]
    y=[s.Matrix([1,s.I])/s.sqrt(2),s.Matrix([s.I,1])/s.sqrt(2)]
    rows=[];built={};v=s.symbols('v',real=True)
    for name,n,edges,loops,black in cases:
        full,states,geom,H2,degree,HQ2,Dq,T=q.build(n,edges,loops);K=n//2;F=2**K*math.factorial(K)
        sign=np.array([math.prod(1 if eta[b]%2==0 else -1 for b in black) for eta in states],dtype=np.int64)
        signed_T=sign[:,None]*T
        assert np.array_equal(H2@signed_T,signed_T@HQ2)
        assert np.array_equal(signed_T.T@signed_T,F*np.eye(len(full),dtype=np.int64))
        D=s.Matrix.hstack(*[vb_column(n,M,black) for M in full]);G=s.simplify(D.T*D)
        expected=s.Matrix([[s.Rational(2)**(components(n,set(M)|set(P))-K) for P in full] for M in full])
        assert G==expected
        H=s.Matrix(HQ2)/2+v*s.diag(*map(int,Dq));comm=G*H-H*G
        conditions=[s.factor(a) for a in comm if a!=0]
        solutions=s.linsolve(conditions,[v]) if conditions else s.S.Reals
        if n<=6:
            V=s.Matrix.hstack(*[q.product(z+x+y if n==6 else z+x,eta) for eta in states])
            A=s.Matrix(signed_T)/s.sqrt(F)
            assert s.simplify(V*A-s.sqrt(math.factorial(K))*D)==s.zeros(2**n,len(full))
        row=dict(graph=name,matchings=len(full),fiber=F,signed_integer_intertwiner=True,
                 VB_rank=D.rank(),loop_Gram_formula=True,Gram=str(G),
                 v_solutions_at_t_one=str(solutions),independent_commutator_equations=sorted(set(map(str,conditions))))
        if name=='ladder6':
            assert solutions==s.FiniteSet(s.Tuple(s.Rational(1,2)))
            HH=H.subs(v,s.Rational(1,2));physical=s.simplify(D*HH*G.inv()*D.T)
            assert physical==physical.T and physical*D==D*HH
            row['positive_tuned_ladder_Hermitian_lift']=True
        built[name]=(D,G,H,full);rows.append(row)
    # One fixed-edge singlet projector distinguishes geometry, mixture and RVB.
    D,G,H,full=built['square'];n=4;bits=list(itertools.product([0,1],repeat=n));P=s.zeros(16)
    for i,state in enumerate(bits):
        flipped=list(state);flipped[0],flipped[1]=flipped[1],flipped[0]
        P[i,i]+=s.Rational(1,2);P[bits.index(tuple(flipped)),i]-=s.Rational(1,2)
    assert P==P.T and P*P==P
    summed=D*s.ones(len(full),1);norm=(summed.T*summed)[0]
    coherent=s.simplify((summed.T*P*summed)[0]/norm)
    mixed=s.simplify(s.trace(D.T*P*D)/len(full))
    occupation=s.Rational(sum((0,1) in M for M in full),len(full))
    assert (norm,coherent,mixed,occupation)==(3,s.Rational(3,4),s.Rational(5,8),s.Rational(1,2))
    # Uniform antipodal classical preparation is an explicit separable mixture.
    rho=s.zeros(4)
    for spinors in [z,x,y]:
        for a,b in [spinors,spinors[::-1]]:
            vector=s.kronecker_product(a,b);rho+=vector*vector.conjugate().T/6
    singlet=s.Matrix([0,1,-1,0])/s.sqrt(2);fidelity=s.simplify((singlet.T*rho*singlet)[0])
    assert fidelity==s.Rational(1,2)
    assert rho.eigenvals()=={s.Rational(1,2):1,s.Rational(1,6):3}
    result=dict(sources_sha256={Path(__file__).name:sha(__file__),src.name:sha(src)},
                rows=rows,square_readout=dict(RVB_norm_squared=str(norm),RVB_singlet_projector=str(coherent),
                  incoherent_singlet_cover_mixture=str(mixed),classical_uniform_geometric_occupation=str(occupation)),
                antipodal_classical_mixture=dict(density_matrix=str(rho),singlet_fidelity=str(fidelity),
                  explicit_separable_six_product_decomposition=True),
                scope='Exploratory conditional coherent antisymmetric sector. No native preparation, local physical Hamiltonian, geometric measurement, or photon theorem.')
    (out/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

if __name__=='__main__':main()
