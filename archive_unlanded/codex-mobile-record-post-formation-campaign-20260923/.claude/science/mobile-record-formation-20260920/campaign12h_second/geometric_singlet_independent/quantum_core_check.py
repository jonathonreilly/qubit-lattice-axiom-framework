#!/usr/bin/env python3
"""Independent exact operational-moment and channel controls.

The finite orbit ensembles control algebra and symmetries. They are not
numerical quadratures of the source's continuous color-conditioned law.
"""
from pathlib import Path
from itertools import product,permutations,combinations
from fractions import Fraction
import json,math
import sympy as s

OUT=Path(__file__).resolve().parent
I=s.I;half=s.Rational(1,2)
pauli=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1)]
singlet=s.Matrix([0,1,-1,0])/s.sqrt(2)
magic=s.Matrix.hstack(singlet,*[s.kronecker_product(x,s.eye(2))*singlet for x in pauli])

def clean(A):return A.applyfunc(s.simplify)
def f(n):
    x,y,z=n;return s.Matrix([y*z*(y*y-z*z),z*x*(z*z-x*x),x*y*(x*x-y*y)])
def physical_pair(n):
    sigma=sum((n[i]*pauli[i] for i in range(3)),s.zeros(2))
    return s.kronecker_product((s.eye(2)+sigma)/2,(s.eye(2)-sigma)/2)
def moment_density(mu,M):
    return s.Matrix.vstack(s.Matrix.hstack(s.ones(1),mu.T),s.Matrix.hstack(mu,M))/2
def principal_psd(A):
    for size in range(1,A.rows+1):
        for selected in combinations(range(A.rows),size):assert s.simplify(A.extract(selected,selected).det())>=0

def moment_checks():
    assert clean(magic.H*magic)==s.eye(4)
    n=s.Matrix([s.Rational(2,3),s.Rational(1,3),s.Rational(2,3)])
    assert n.dot(n)==1
    assert clean(magic.H*physical_pair(n)*magic-moment_density(n,n*n.T))==s.zeros(4)
    x,y,z=s.symbols('x y z',real=True);v=s.Matrix([x,y,z]);rotations=[]
    for perm in permutations(range(3)):
        for signs in product([-1,1],repeat=3):
            R=s.zeros(3)
            for i in range(3):R[i,perm[i]]=signs[i]
            if R.det()==1:
                assert (f(R*v)-R*f(v)).applyfunc(s.expand)==s.zeros(3,1)
                rotations.append(R)
    assert len(rotations)==24 and f(-v)==f(v)
    Rx=s.Matrix([[1,0,0],[0,0,-1],[0,1,0]])
    Ry=s.diag(-1,1,-1);cycle=s.Matrix([[0,1,0],[0,0,1],[1,0,0]])
    oppositeB=s.Matrix([[0,-1,0],[-1,0,0],[0,0,-1]])
    assert all(R.det()==1 for R in [Rx,Ry,cycle,oppositeB])
    a,c=s.symbols('a c',real=True);MA=s.diag(a,(1-a)/2,(1-a)/2)
    MB=(s.Rational(1,3)-c)*s.eye(3)+c*s.ones(3)
    assert Rx*MA*Rx.T==MA and Ry*MA*Ry.T==MA
    assert cycle*MB*cycle.T==MB and oppositeB*MB*oppositeB.T==MB
    unknowns=s.symbols('m00 m11 m22 m01 m02 m12')
    M=s.Matrix([[unknowns[0],unknowns[3],unknowns[4]],[unknowns[3],unknowns[1],unknowns[5]],[unknowns[4],unknowns[5],unknowns[2]]])
    stabdim=[]
    for R in [Rx,cycle]:
        mat,_=s.linear_eq_to_matrix(list(R*M*R.T-M),unknowns)
        stabdim.append(6-mat.rank())
    assert stabdim==[2,2]
    nA=s.Matrix([1,8,4])/9;nB=s.Matrix([1,-2,3])/s.sqrt(14)
    assert nA.dot(nA)==nB.dot(nB)==1
    fa,fb=f(nA),f(nB)
    assert fa[0]>0 and fa[0]**2>s.Rational(81,100)*fa.dot(fa)
    assert all(q>0 for q in fb) and max(q*q for q in fb)<s.Rational(81,100)*fb.dot(fb)
    epsilon=s.Rational(2,5);delta=s.Matrix([0,1,0]);orbit_rows=[];second=[]
    for name,point,R,opposite,order in [('A+x',nA,Rx,Ry,4),('B111',nB,cycle,oppositeB,3)]:
        points=[sign*(R**i)*point for sign in [-1,1] for i in range(order)]
        assert sum(points,s.zeros(3,1))==s.zeros(3,1)
        M=clean(sum((p*p.T for p in points),s.zeros(3))/len(points))
        rho=sum(((1+epsilon*p.dot(delta))*physical_pair(p) for p in points),s.zeros(4))/len(points)
        opp=[opposite*p for p in points]
        rho_opp=sum(((1+epsilon*p.dot(delta))*physical_pair(p) for p in opp),s.zeros(4))/len(opp)
        assert clean(rho-rho_opp)==s.zeros(4)
        assert clean(magic.H*rho*magic-moment_density(epsilon*M*delta,M))==s.zeros(4)
        assert clean(sum(((1+epsilon*p.dot(delta))*p for p in points),s.zeros(3,1))/len(points))==epsilon*M*delta
        rho0=sum((physical_pair(p) for p in points),s.zeros(4))/len(points)
        principal_psd(s.eye(4)/2-rho0)
        principal_psd(clean((1+abs(epsilon))*rho0-rho))
        assert s.simplify(rho.det())>0
        second.append(M)
        orbit_rows.append(dict(color=name,points=len(points),second_moment=[[str(q) for q in M.row(i)] for i in range(3)],
            tilted_first_moment=list(map(str,epsilon*M*delta)),pair_density_determinant=str(s.simplify(rho.det())),
            exact_opposite_density_equality=True))
    # These concrete second moments furnish a generic moment-map control.
    # The actual continuous-law values are not inferred from the finite orbits.
    aval=second[0][0,0];cval=second[1][0,1]
    labels=[];matrices=[];field=[]
    for axis in range(3):
        for sign in [-1,1]:
            vector=s.zeros(3,1);vector[axis]=sign
            M=(1-aval)/2*s.eye(3);M[axis,axis]=aval
            labels.append(('A',tuple(vector)));matrices.append(M);field.append(s.Matrix.vstack(vector,s.zeros(3,1)))
    for b in product([-1,1],repeat=3):
        vector=s.Matrix(b);labels.append(('B',b));matrices.append((s.Rational(1,3)-cval)*s.eye(3)+cval*vector*vector.T)
        field.append(s.Matrix.vstack(s.zeros(3,1),vector))
    moment=s.Matrix.hstack(*[s.Matrix([M[0,0],M[1,1],M[2,2],M[0,1],M[0,2],M[1,2]]) for M in matrices])
    F=s.Matrix.hstack(*field);odd=[];used=set()
    for i,(kind,b) in enumerate(labels):
        if i in used:continue
        j=labels.index((kind,tuple(-x for x in b)));used|={i,j}
        e=s.zeros(14,1);e[i]=1;e[j]=-1;odd.append(e)
    odd=s.Matrix.hstack(*odd);assert odd.cols==7 and moment*odd==s.zeros(6,7)
    assert (F*odd).rank()==6
    tangent=s.Matrix.hstack(*[moment[:,i]-moment[:,13] for i in range(13)])
    assert tangent.rank()==5
    contrast=s.Matrix([s.Rational(1,6)]*6+[-s.Rational(1,8)]*8)
    assert moment*contrast==s.zeros(6,1)
    return dict(proper_cubic_covariance_rotations=24,stabilizer_symmetric_matrix_dimensions=stabdim,
        exact_open_class_witnesses={'A+x':[str(q) for q in nA],'B111':[str(q) for q in nB]},
        epsilon=str(epsilon),delta=list(delta),finite_even_orbit_controls=orbit_rows,
        exact_odd_population_kernel_dimension=7,vector_field_rank_on_odd_space=6,
        tangent_rank_in_this_finite_ensemble_control=5,even_orbit_mass_contrast_also_in_kernel=True,
        scope='Actual continuous-ensemble equality follows from parity and proper-cubic stabilizers analytically. Finite orbit moments test the algebra, not the continuous moment values or a late-time correlated key ensemble.')

def square_columns():
    covers=[[(0,1),(3,2)],[(0,2),(3,1)]];D=s.zeros(16,2)
    for col,M in enumerate(covers):
        for bits in product([0,1],repeat=2):
            mask=0
            for bit,(black,white) in zip(bits,M):mask|=(bit<<black)|((1-bit)<<white)
            D[mask,col]=s.Rational((-1)**sum(bits),2)
    return D

def channel_checks():
    D=square_columns();G=D.H*D;assert G==s.Matrix([[1,half],[half,1]])
    kraus=[]
    for j in range(2):
        L=s.zeros(16,2);L[:,j]=D[:,j];kraus.append(L)
    assert sum((L.H*L for L in kraus),s.zeros(2))==s.eye(2)
    off=s.Matrix([[0,1],[0,0]])
    assert sum((L*off*L.H for L in kraus),s.zeros(16))==s.zeros(16)
    plus=s.ones(2,1)/s.sqrt(2);coherent=D*plus;coherent/=s.sqrt((coherent.H*coherent)[0])
    mixture=sum((L*plus*plus.H*L.H for L in kraus),s.zeros(16))
    difference=clean(mixture-coherent*coherent.H)
    distance=sum(abs(v)*m for v,m in difference.eigenvals().items())/2;assert distance==s.Rational(1,4)
    lam=s.Rational(3,2);success=D/s.sqrt(lam)
    failure=s.sqrt(s.Rational(2,3))*s.Matrix([[1,-1],[-1,1]])/2
    assert clean(success.H*success+failure.H*failure)==s.eye(2)
    assert clean(plus.H*success.H*success*plus)[0]==1
    assert all((success.H*success)[j,j]==s.Rational(2,3) for j in range(2))
    marker=s.Matrix.hstack(s.kronecker_product(D[:,0],s.Matrix([1,0])),s.kronecker_product(D[:,1],s.Matrix([0,1])))
    assert marker.H*marker==s.eye(2)
    singular=s.Matrix([[1,1],[1,1]]);minus=s.Matrix([1,-1])/s.sqrt(2)
    assert (minus.H*singular*minus)[0]==0 and (plus.H*singular*plus)[0]==2
    products=[]
    for P in [1,2,3,4]:
        GP=G
        for _ in range(P-1):GP=s.kronecker_product(GP,G)
        rowsum=s.Rational(3,2)**P
        assert GP*s.ones(2**P,1)==rowsum*s.ones(2**P,1)
        assert max(GP.eigenvals())==rowsum
        products.append(dict(plaquettes=P,dimension=2**P,lambda_max=str(rowsum),basis_success=str(1/rowsum),coherent_uniform_success='1'))
    return dict(square_Gram=[[str(q) for q in G.row(i)] for i in range(2)],
        exact_channel_offdiagonal_zero=True,square_coherent_vs_mixture_trace_distance=str(distance),
        scalar_success_basis_probability='2/3',scalar_success_uniform_probability='1',
        orthogonal_marker_isometry=True,singular_Gram_zero_success_control=True,square_products=products)

def torus_tile_control():
    N=8;coords=list(product(range(N),repeat=3));index={x:i for i,x in enumerate(coords)};tiles=[]
    for z in range(N):
        for x in range(0,N,2):
            for y in range(0,N,2):tiles.append([index[(x,y,z)],index[(x+1,y,z)],index[(x+1,y+1,z)],index[(x,y+1,z)]])
    assert sorted(v for tile in tiles for v in tile)==list(range(N**3))
    P=len(tiles);K=N**3//2;assert P==K//2
    choices=[[0]*P,[1]*P,[i%2 for i in range(P)]];matchings=[]
    for bits in choices:
        M=[]
        for tile,bit in zip(tiles,bits):
            a,b,c,d=tile;M.extend([(a,b),(c,d)] if bit==0 else [(b,c),(d,a)])
        assert sorted(v for e in M for v in e)==list(range(N**3));matchings.append(M)
    comparisons=[]
    for i,j in combinations(range(len(choices)),2):
        adj=[set() for _ in range(N**3)]
        for a,b in matchings[i]+matchings[j]:adj[a].add(b);adj[b].add(a)
        unvisited=set(range(N**3));components=0
        while unvisited:
            stack=[unvisited.pop()];components+=1
            while stack:
                for v in adj[stack.pop()]&unvisited:unvisited.remove(v);stack.append(v)
        hd=sum(a!=b for a,b in zip(choices[i],choices[j]));assert components==K-hd
        comparisons.append(dict(pair=[i,j],different_tiles=hd,overlay_components=components,exact_overlap=str(Fraction(1,2**hd))))
    return dict(N=N,sites=N**3,plaquettes=P,matching_pairs_checked=comparisons,
        guaranteed_Gram_eigenvalue=str(Fraction(3,2)**P),basis_success_upper_bound=str(Fraction(2,3)**P),
        scope='Combinatorial overlap checks of three actual torus matchings; the entire exponential-size principal matrix is not enumerated.')

if __name__=='__main__':
    p=OUT/'QUANTUM_CORE_RESULTS.json';assert not p.exists()
    result={'operational_moments':moment_checks()};print('Operational moments and symmetry complete',flush=True)
    result['channels']=channel_checks();print('Channel and coherent-filter controls complete',flush=True)
    result['torus_tiles']=torus_tile_control();print('Actual torus tiled subset complete',flush=True)
    p.write_text(json.dumps(result,indent=2,default=str)+'\n')
