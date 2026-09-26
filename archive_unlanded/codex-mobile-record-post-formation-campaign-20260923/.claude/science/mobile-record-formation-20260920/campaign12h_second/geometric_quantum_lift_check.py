#!/usr/bin/env python3
"""Exploratory exact controls for coherent permutations and literal qubit Gram compatibility."""
from pathlib import Path
import hashlib,importlib.util,itertools,json
import numpy as np
import sympy as s
HERE=Path(__file__).resolve().parent
src=HERE/'geometric_corridor_transport_check.py'
spec=importlib.util.spec_from_file_location('matching',src);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()

def build(n,edges,loops):
    full=m.matchings(n,edges,n//2);K=n//2;states=[];geometries=[]
    for q,M in enumerate(full):
        for labels in itertools.permutations(range(K)):
            for mask in range(1<<K):
                state=[-1]*n
                for e,pair in zip(sorted(M),labels):
                    bit=(mask>>pair)&1;state[e[0]]=2*pair+bit;state[e[1]]=2*pair+1-bit
                states.append(tuple(state));geometries.append(q)
    assert len(states)==len(set(states))==len(full)*s.factorial(K)*2**K
    index={eta:i for i,eta in enumerate(states)}
    moves=[];degree=np.zeros(len(states),dtype=int)
    Hkin=np.zeros((len(states),len(states)),dtype=np.int64)
    HQkin=np.zeros((len(full),len(full)),dtype=np.int64);Dq=np.zeros(len(full),dtype=int)
    for q,M in enumerate(full):
        for p in loops:
            first={m.edge(p[i],p[(i+1)%len(p)]) for i in range(0,len(p),2)}
            second={m.edge(p[i],p[(i+1)%len(p)]) for i in range(1,len(p),2)}
            if not (first<=M or second<=M):continue
            target=(M-first)|second if first<=M else (M-second)|first
            qtarget=full.index(frozenset(target));HQkin[q,qtarget]-=2;Dq[q]+=1
    for i,eta in enumerate(states):
        q=geometries[i];M=full[q];local=[]
        for p in loops:
            first={m.edge(p[j],p[(j+1)%len(p)]) for j in range(0,len(p),2)}
            second={m.edge(p[j],p[(j+1)%len(p)]) for j in range(1,len(p),2)}
            if not (first<=M or second<=M):continue
            degree[i]+=1
            for sign in [1,-1]:
                new=list(eta)
                for k,x in enumerate(p):new[p[(k+sign)%len(p)]]=eta[x]
                target=tuple(new);j=index[target];Hkin[i,j]-=1;local.append(j)
                assert all((new.index(label)==x or m.edge(x,new.index(label)) in edges) for x,label in enumerate(eta))
                assert geometries[j]!=q
        moves.append(local)
    assert np.array_equal(Hkin,Hkin.T)
    assert np.array_equal(degree,np.asarray(Dq)[geometries])
    # Twice the Hamiltonian with t=1 and arbitrary v: indicator lift gives an
    # integer identity, so no square-root normalization tolerance is needed.
    T=np.eye(len(full),dtype=np.int64)[geometries]
    assert np.array_equal(Hkin@T,T@HQkin)
    assert np.array_equal((degree[:,None]*T),T@np.diag(Dq))
    return full,states,geometries,Hkin,degree,HQkin,Dq,T

def product(spinors,state):
    result=s.Matrix([1])
    for label in state:result=s.kronecker_product(result,spinors[label])
    return result

def main():
    out=HERE/'geometric_quantum_lift_checks';out.mkdir(exist_ok=False)
    root2=s.sqrt(2);z=[s.Matrix([1,0]),s.Matrix([0,1])]
    x=[s.Matrix([1,1])/root2,s.Matrix([-1,1])/root2]
    y=[s.Matrix([1,s.I])/root2,s.Matrix([s.I,1])/root2]
    square=(4,{(0,1),(1,2),(2,3),(0,3)},[(0,1,2,3)])
    ladder=(6,{(0,1),(1,2),(3,4),(4,5),(0,3),(1,4),(2,5)},[(0,1,4,3),(1,2,5,4)])
    cube_edges={(a,b) for a,b in itertools.combinations(range(8),2) if (a^b) in [1,2,4]}
    cube_loops=[]
    for i,j in itertools.combinations([1,2,4],2):
        for a in range(8):
            if a&i==0 and a&j==0:cube_loops.append((a,a^i,a^i^j,a^j))
    rows=[];built={}
    for name,args in [('square',square),('ladder6',ladder),('cube8',(8,cube_edges,cube_loops))]:
        data=build(*args);built[name]=data
        full,states,geometries,H,D,Hq,Dq,T=data
        rows.append(dict(graph=name,unmarked_states=len(full),fiber_size=len(states)//len(full),
                         marked_states=len(states),literal_qubit_dimension=2**args[0],
                         local_channels=int(D.sum()*2),integer_intertwiner_verified=True))
    # One four-cycle of distinguishable configurations: exact propagator.
    tau=s.symbols('tau',real=True)
    R=s.zeros(4)
    for i in range(4):R[(i+1)%4,i]=1
    H=-(R+R.T)/2
    U=s.simplify(s.exp(-s.I*tau*H))
    basis=s.Matrix([1,0,0,0]);coherent=s.Matrix([1,0,1,0])/root2
    odd=s.diag(0,1,0,1)
    p_basis=s.simplify(s.expand_complex(((U*basis).conjugate().T*odd*(U*basis))[0]))
    p_coherent=s.simplify(s.expand_complex(((U*coherent).conjugate().T*odd*(U*coherent))[0]))
    assert s.simplify(p_basis-s.sin(tau)**2/2)==0
    assert s.simplify(p_coherent-s.sin(tau)**2)==0
    square_probability=dict(definite_or_incoherent_same_geometry=str(p_basis),
                            coherent_uniform_fiber=str(p_coherent),
                            QDM=str(s.sin(tau)**2),at_pi_over_2=['1/2','1','1'])

    full,states,geometries,H2,D,HQ2,DQ,T=built['square']
    V=s.Matrix.hstack(*[product(z+x,eta) for eta in states]);G=V.conjugate().T*V
    Ufiber=s.Matrix(T)/s.sqrt(8)
    coherent_Gram=s.simplify(Ufiber.T*G*Ufiber)
    assert coherent_Gram==s.ones(2)
    Hstate=(0,1,2,3);Vstate=(2,1,0,3)
    assert geometries[states.index(Hstate)]!=geometries[states.index(Vstate)]
    overlap=s.simplify(G[states.index(Hstate),states.index(Vstate)])
    assert overlap==s.Rational(1,2)
    # Nonorthogonal keys: coherent geometric columns can be independent, but
    # remain nonorthogonal. This distinguishes a particular collapse example
    # from a universal assertion that the coherent span always collapses.
    u=[s.Matrix([s.Rational(3,5),s.Rational(4,5)]),
       s.Matrix([-s.Rational(4,5),s.Rational(3,5)])]
    Vgeneric=s.Matrix.hstack(*[product(z+u,eta) for eta in states])
    Gram_generic=s.simplify(Ufiber.T*Vgeneric.T*Vgeneric*Ufiber)
    assert Gram_generic==s.Matrix([[s.Rational(674,625),1],[1,s.Rational(674,625)]])
    physical_square=dict(marked_Gram_rank=G.rank(),marked_states=len(states),
                         coherent_Gram_orthogonal_key_axes=str(coherent_Gram),
                         coherent_Gram_generic_key_axes=str(Gram_generic),
                         different_geometry_overlap=str(overlap),
                         states=[Hstate,Vstate])

    # A necessary condition for any Hermitian H_phys satisfying H_phys V=V H:
    # [V^*V,H]=0. Evaluate an exact nonzero entry, with full numeric matrix
    # search used only to choose a witness before exact arithmetic verification.
    full,states,geometries,H2,D,HQ2,DQ,T=built['ladder6']
    V=s.Matrix.hstack(*[product(z+x+y,eta) for eta in states])
    G=s.simplify(V.conjugate().T*V);Gn=np.asarray(G,dtype=complex)
    witnesses=[]
    for v in [s.Rational(0),s.Rational(1),s.Rational(2,3)]:
        H=s.Matrix(H2)/2+v*s.diag(*map(int,D))
        Hn=np.asarray(H,dtype=complex);comm=Gn@Hn-Hn@Gn
        i,j=np.unravel_index(np.argmax(abs(comm)),comm.shape)
        exact=s.simplify((G.row(i)*H.col(j)-H.row(i)*G.col(j))[0])
        assert exact!=0 and abs(complex(exact)-comm[i,j])<1e-12
        witnesses.append(dict(v=str(v),row=int(i),column=int(j),source_state=states[i],target_state=states[j],
                              exact_Gram_commutator=str(exact),numeric_max_abs=float(abs(comm[i,j]))))
    report=dict(scope='Exploratory conditional orthogonal configuration lift and countercontrols for a literal tensor-qubit realization. No photon, ground-state preparation or axiomatic quantum dynamics theorem.',
                sources_sha256={Path(__file__).name:sha(Path(__file__)),src.name:sha(src)},
                lifts=rows,square_probability=square_probability,physical_square=physical_square,
                ladder_Gram_compatibility_witnesses=witnesses,
                literature_used_in_calculation=False)
    (out/'RESULTS.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()

