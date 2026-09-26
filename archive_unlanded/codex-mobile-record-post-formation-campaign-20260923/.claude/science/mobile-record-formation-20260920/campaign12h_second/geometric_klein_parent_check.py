#!/usr/bin/env python3
"""Exploratory exact finite-cube parent and local perturbation controls."""
from pathlib import Path
import datetime,hashlib,importlib.util,itertools,json,math
import numpy as np
import sympy as s
HERE=Path(__file__).resolve().parent
src=HERE/'geometric_singlet_fiber_check.py'
spec=importlib.util.spec_from_file_location('singlet',src);v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()

def permutation_matrix(n,permutation):
    # Bit site x is position n-1-x, matching the tensor product convention.
    P=s.zeros(2**n)
    for z in range(2**n):
        target=sum(((z>>(n-1-x))&1)<<(n-1-permutation[x]) for x in range(n))
        P[target,z]=1
    assert P.T*P==s.eye(2**n)
    return P

def maxspin_projector(n,star):
    P=s.zeros(2**n);outside=[x for x in range(n) if x not in star]
    sectors={}
    for z in range(2**n):
        key=(tuple((z>>(n-1-x))&1 for x in outside),sum((z>>(n-1-x))&1 for x in star))
        sectors.setdefault(key,[]).append(z)
    for (_,weight),indices in sectors.items():
        assert len(indices)==math.comb(len(star),weight)
        for i in indices:
            for j in indices:P[i,j]=s.Rational(1,len(indices))
    assert P==P.T and P*P==P
    return P

def main():
    out=HERE/'geometric_klein_parent_checks';out.mkdir(exist_ok=False)
    n=8;dim=2**n
    edges={(a,b) for a,b in itertools.combinations(range(n),2) if (a^b) in [1,2,4]}
    loops=[]
    for i,j in itertools.combinations([1,2,4],2):
        for a in range(n):
            if a&i==0 and a&j==0:loops.append((a,a^i,a^i^j,a^j))
    black={0,3,5,6};matchings=v.q.m.matchings(n,edges,n//2)
    D=s.Matrix.hstack(*[v.vb_column(n,M,black) for M in matchings]);G=D.T*D
    assert len(matchings)==9 and G.rank()==9
    stars=[{x}|{y for e in edges if x in e for y in e if y!=x} for x in range(n)]
    terms=[maxspin_projector(n,star) for star in stars]
    H=sum(terms,s.zeros(dim));assert H*D==s.zeros(dim,len(matchings))
    assert all(T*D==s.zeros(dim,len(matchings)) for T in terms)
    sector_rows=[];null_vectors=[]
    for k in range(n+1):
        indices=[z for z in range(dim) if z.bit_count()==k]
        block=H.extract(indices,indices);kernel=block.nullspace()
        for col in kernel:
            full=s.zeros(dim,1)
            for i,z in enumerate(indices):full[z]=col[i]
            null_vectors.append(full)
        eigen=np.linalg.eigvalsh(np.asarray(block,dtype=float));nz=eigen[eigen>1e-10]
        sector_rows.append(dict(down_spins=k,dimension=len(indices),exact_nullity=len(kernel),
                               smallest_positive_eigenvalue=float(nz[0]) if len(nz) else None))
    Q=s.Matrix.hstack(*null_vectors);P0=Q*(Q.T*Q).inv()*Q.T
    PV=D*G.inv()*D.T
    assert P0*D==D and H*P0==s.zeros(dim)
    extra=s.simplify(P0-PV);assert extra*extra==extra and extra.T==extra
    # S_total^2 = 3n/4 + sum_{x<y}(Swap_xy - I/2).
    S2=s.Rational(3*n,4)*s.eye(dim);NN=s.zeros(dim)
    for x,y in itertools.combinations(range(n),2):
        perm=list(range(n));perm[x],perm[y]=perm[y],perm[x]
        SW=permutation_matrix(n,perm)
        S2+=SW-s.eye(dim)/2
        if (x,y) in edges:NN+=SW
    assert S2*D==s.zeros(dim,len(matchings))
    # Obtain spin content of the complete parent kernel from exact magnetization
    # multiplicities: multiplicity(spin s)=dim(M=s)-dim(M=s+1).
    dims={abs(n//2-row['down_spins']):row['exact_nullity'] for row in sector_rows if row['down_spins']<=n//2}
    spin_mult={str(j):dims.get(j,0)-dims.get(j+1,0) for j in range(n//2+1)}
    ring=s.zeros(dim)
    for loop in loops:
        perm=list(range(n))
        for i,x in enumerate(loop):perm[x]=loop[(i+1)%4]
        R=permutation_matrix(n,perm);ring+=R+R.T
    perturb=[]
    for name,W in [('nearest_neighbor_swap_sum',NN),('unconditional_plaquette_ring_sum',ring)]:
        action=W*D;projected=s.simplify(G.inv()*D.T*action)
        leakage=s.simplify(action-D*projected)
        assert G*projected==projected.T*G
        outside=s.simplify((s.eye(dim)-P0)*action)
        extra_action=s.simplify(extra*action)
        perturb.append(dict(operator=name,coefficient_matrix=str(projected),
          Gram_Hermitian=True,ordinary_symmetric=projected==projected.T,
          leakage_rank=leakage.rank(),squared_Frobenius_leakage=str(s.trace(leakage.T*leakage)),
          outside_parent_kernel_rank=outside.rank(),extra_parent_groundspace_rank=extra_action.rank(),
          leakage_scope='Finite cube only; projection is algebraic and not a local effective-Hamiltonian theorem.'))
    data=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
      sources_sha256={Path(__file__).name:sha(__file__),src.name:sha(src),
        'geometric_quantum_lift_check.py':sha(HERE/'geometric_quantum_lift_check.py'),
        'geometric_corridor_transport_check.py':sha(HERE/'geometric_corridor_transport_check.py')},
      graph='Eight-vertex simple cube, degree three; not a degree-six infinite cubic lattice.',
      stars=[sorted(x) for x in stars],VB_dimension=D.cols,parent_kernel_dimension=Q.cols,
      all_VB_columns_annihilated_by_each_star=True,magnetization_sectors=sector_rows,
      kernel_spin_multiplicities=spin_mult,extra_groundspace_dimension=str(s.trace(extra)),
      perturbations=perturb,
      scope='Exploratory author exact finite controls. No thermodynamic spectral gap, complete cubic-lattice groundspace, physical preparation or photon claim.')
    (out/'RESULTS.json').write_text(json.dumps(data,indent=2)+'\n');print(json.dumps(data,indent=2))

if __name__=='__main__':main()
