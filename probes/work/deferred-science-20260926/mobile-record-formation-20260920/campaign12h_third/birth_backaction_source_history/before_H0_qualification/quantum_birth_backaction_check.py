#!/usr/bin/env python3
"""Author checks of coherent record motion with irreversible vacancy filling.

These are supplied quantum models. They do not derive a native clock,
Hamiltonian, Record interpretation, or thermodynamic quantum phase.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,itertools,json
import numpy as np
import sympy as s
from scipy.linalg import expm

HERE=Path(__file__).resolve().parent


def two_block():
    k,b=s.symbols('kappa beta',positive=True,real=True)
    A=s.Matrix([[0,-s.I*k],[-s.I*k,-b/2]])
    # First transient state: record still at birth source. Second: it moved off.
    X=s.Matrix([[2/b+b/(4*k*k),-s.I/(2*k)],[s.I/(2*k),2/b]])
    assert s.simplify(A.conjugate().T*X+X*A)==-s.eye(2)
    mean=X[0,0]
    assert s.simplify(s.diff(mean,b).subs(b,2*s.sqrt(2)*k))==0
    assert s.simplify(mean.subs(b,2*s.sqrt(2)*k))==s.sqrt(2)/k
    # Direct full three-state Lindblad evolution is separate from the no-jump formula.
    diagnostics=[]
    for beta in [s.Rational(1,4),s.Rational(1,1),s.Rational(4,1),s.Rational(16,1)]:
        bf=float(beta)
        H=np.array([[0,1,0],[1,0,0],[0,0,0]],dtype=complex)
        jump=np.zeros((3,3),dtype=complex);jump[2,1]=np.sqrt(bf)
        K=jump.conj().T@jump
        superop=-1j*(np.kron(np.eye(3),H)-np.kron(H.T,np.eye(3)))
        superop+=np.kron(jump.conj(),jump)-.5*(np.kron(np.eye(3),K)+np.kron(K.T,np.eye(3)))
        initial=np.diag([1.,0.,0.]).astype(complex)
        An=np.array([[0,-1j],[-1j,-bf/2]],dtype=complex)
        for t in [0.,.1,1.,4.,12.]:
            rho=(expm(superop*t)@initial.reshape(-1,order='F')).reshape((3,3),order='F')
            transient=expm(An*t)@np.array([1.,0.])
            birth=1-float(np.vdot(transient,transient).real)
            assert abs(np.trace(rho)-1)<1e-12
            assert np.linalg.eigvalsh(rho).min()>-1e-12
            assert abs(rho[2,2].real-birth)<1e-12
            diagnostics.append(dict(beta=str(beta),t=t,birth_probability=birth,
                                    full_Lindblad_birth_probability=float(rho[2,2].real)))
    return dict(exact_mean_first_birth=str(mean),
                minimizing_beta='2*sqrt(2)*kappa',minimum_mean='sqrt(2)/kappa',
                exact_Lyapunov_residual_zero=True,
                comparison='For a classical reversible hop at rate kappa and birth beta, the mean is 1/kappa+2/beta. No physical matching of the two kappa parameters is assumed.',
                diagnostics=diagnostics)


def graph_dark_controls():
    square=s.Matrix([[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]])
    dark=s.Matrix([0,1,0,-1]);assert square*dark==s.zeros(4,1)
    source=s.Matrix([[1,0,0,0]])
    obs=s.Matrix.vstack(*(source*square**j for j in range(4)))
    assert obs.rank()==3
    vertices=list(itertools.product(range(2),repeat=3))
    cube=s.Matrix(8,8,lambda i,j:int(sum(a!=b for a,b in zip(vertices[i],vertices[j]))==1))
    source8=s.zeros(1,8);source8[0,0]=1
    obs8=s.Matrix.vstack(*(source8*cube**j for j in range(8)))
    assert obs8.rank()==4
    return dict(square_source=0,square_dark_vector=list(dark),square_dark_dimension=1,
                square_hole_at_1_dark_overlap='1/2',cube_source=[0,0,0],
                cube_observability_rank=4,cube_dark_dimension=4,
                cube_uniform_hole_eventual_completion_probability='1/2')


def paired_dark_vacancy():
    N=4
    vertices=list(itertools.product(range(N),repeat=3));lookup={p:i for i,p in enumerate(vertices)}
    neighbors=[]
    for p in vertices:
        row=[]
        for axis in range(3):
            for sign in (-1,1):
                q=list(p);q[axis]=(q[axis]+sign)%N;row.append(lookup[tuple(q)])
        assert len(set(row))==6;neighbors.append(row)
    pairs=list(itertools.combinations(range(len(vertices)),2));index={pair:i for i,pair in enumerate(pairs)}
    sin=[0,1,0,-1]
    state=np.array([sin[(vertices[j][0]-vertices[i][0])%N]*sin[(vertices[j][1]-vertices[i][1])%N] for i,j in pairs],dtype=np.int64)
    out=np.zeros(len(pairs),dtype=np.int64)
    birth_supported=[]
    for n,(i,j) in enumerate(pairs):
        if j in neighbors[i]:birth_supported.append(n)
        for k in neighbors[i]:
            if k!=j:out[n]+=state[index[tuple(sorted((k,j)))]]
        for k in neighbors[j]:
            if k!=i:out[n]+=state[index[tuple(sorted((i,k)))]]
    assert np.array_equal(out,4*state)
    assert np.all(state[birth_supported]==0)
    norm=int(state@state);assert norm==512
    h0=lookup[(0,0,0)];h1=lookup[(1,1,1)];witness=index[(h0,h1)]
    assert state[witness]==1
    # Explicit almost-complete matching leaves those separated holes. It is a
    # possible sequence of pair births, not by itself a quantum trajectory proof.
    edges={tuple(sorted((lookup[(x,y,z)],lookup[(x+1,y,z)]))) for x in (0,2) for y in range(N) for z in range(N)}
    path=[(0,0,0),(1,0,0),(1,1,0),(0,1,0),(0,1,1),(1,1,1)]
    for j in (0,2,4):edges.remove(tuple(sorted((lookup[path[j]],lookup[path[j+1]]))))
    for j in (1,3):edges.add(tuple(sorted((lookup[path[j]],lookup[path[j+1]]))))
    used=[x for edge in edges for x in edge]
    assert len(used)==len(set(used))==62 and set(used)==set(range(64))-{h0,h1}
    assert all(j in neighbors[i] for i,j in edges)
    return dict(torus_N=N,sites=64,two_vacancy_basis_size=len(pairs),
                adjacent_vacancy_pairs=len(birth_supported),exact_integer_H_eigenvalue=4,
                exact_eigenvector_residual_zero=True,birth_support_amplitude_exactly_zero=True,
                unnormalized_state='sin(pi*(y_x-x_x)/2) sin(pi*(y_y-x_y)/2)',
                norm_squared=norm,separated_holes=[[0,0,0],[1,1,1]],
                localized_hole_pair_dark_overlap_lower_bound='1/512',
                near_perfect_matching_edges=len(edges),matching=[list(edge) for edge in sorted(edges)],
                scope='Nearest-neighbor coherent hard-core record hopping, identical occupied record label, and pair births only at adjacent vacancies. This supplied occupation model does not impose the previous permanent-partner adjacency rule or derive the formation instrument.')


def main():
    result=dict(created_utc=datetime.now(timezone.utc).isoformat(),
                status='author_exact_model_calculations_independent_check_pending',
                script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                two_block=two_block(),one_vacancy=graph_dark_controls(),paired_vacancy=paired_dark_vacancy(),
                scope='Supplied coherent occupation dynamics and irreversible birth models. Exact finite algebra and declared finite numerical controls; no native axiom law, new quantum-Zeno mechanism, full thermodynamic phase, or TOE completion claim.')
    encoded=json.dumps(result,indent=2,default=int)+'\n';(HERE/'QUANTUM_BIRTH_BACKACTION_RESULTS.json').write_text(encoded);print(encoded,end='')


if __name__=='__main__':main()
