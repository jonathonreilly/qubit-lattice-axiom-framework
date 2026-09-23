#!/usr/bin/env python3
"""Exact physical-cube point-spectrum certificate, independently rebuilt.

No author or previous model builder is imported.  The old independent builder
is used only in a separate optional comparison after this runner is frozen.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
import json, platform, time
import numpy as np
import sympy as sp

VERTICES=tuple(range(8)); A_SITES=frozenset((0,3,5,6))
EDGES=tuple((x,y) for x in VERTICES for y in range(x+1,8) if (x^y).bit_count()==1)
TREE=frozenset(((0,1),(0,2),(0,4),(1,3),(1,5),(2,6),(3,7)))
CHORDS=tuple(e for e in EDGES if e not in TREE)
EDGE_INDEX={e:i for i,e in enumerate(EDGES)}
CHORD_INDEX={e:i for i,e in enumerate(CHORDS)}
ZERO=(0,)*len(CHORDS)


def state_space(level):
    # Exactly two vacancies and one minus record: all other sites are plus.
    return tuple(tuple(0 if v in vacancies else -1 if v==negative else 1
                       for v in VERTICES)
                 for vacancies in combinations(VERTICES,2)
                 if len(A_SITES.intersection(vacancies))==level
                 for negative in VERTICES if negative not in vacancies)


def divergence(field):
    div=[0]*8
    for (x,y),f in zip(EDGES,field):div[x]+=f;div[y]-=f
    return tuple(div)


def gauss_rhs(q):return tuple(q[v]-int(v in A_SITES) for v in VERTICES)


def physical_field(q,chord_values):
    # Exact integer tree solve; root 0.  Tree order is irrelevant.
    field=[0]*12
    for edge,value in zip(CHORDS,chord_values):field[EDGE_INDEX[edge]]=value
    r=[a-b for a,b in zip(gauss_rhs(q),divergence(field))]
    tree_remaining=set(TREE); remaining=set(VERTICES)
    while len(remaining)>1:
        leaf=next(v for v in sorted(remaining) if v!=0 and
                  sum(v in edge for edge in tree_remaining)==1)
        edge=next(e for e in tree_remaining if leaf in e)
        parent=edge[1] if edge[0]==leaf else edge[0]
        sigma=1 if edge[0]==leaf else -1
        value=sigma*r[leaf]
        field[EDGE_INDEX[edge]]=value
        r[parent]+=r[leaf];r[leaf]=0
        tree_remaining.remove(edge);remaining.remove(leaf)
    assert r[0]==0
    assert divergence(field)==gauss_rhs(q)
    return tuple(field)


def legal_hops(q):
    # Locate each vacancy, then each occupied neighbor.  This assembly differs
    # from the exploratory edge/direction loop and retains all 12 field shifts.
    for destination in VERTICES:
        if q[destination]!=0:continue
        for source in VERTICES:
            if q[source]==0 or (source^destination).bit_count()!=1:continue
            charge=q[source];edge=tuple(sorted((source,destination)))
            direction=1 if source<destination else -1
            shift=[0]*12;shift[EDGE_INDEX[edge]]=-direction*charge
            out=list(q);out[destination]=charge;out[source]=0
            yield tuple(out),tuple(shift),-1


def add(x,y):return tuple(a+b for a,b in zip(x,y))
def chord_part(shift):return tuple(shift[EDGE_INDEX[e]] for e in CHORDS)


def exact_hopping(phase,states,excited):
    rows={q:i for i,q in enumerate(excited)}
    mat=sp.zeros(len(excited),len(states))
    for j,q in enumerate(states):
        for out,shift,amplitude in legal_hops(q):
            if out in rows:
                mat[rows[out],j]+=amplitude*phase**sum(chord_part(shift))
    return mat


def h2_paths(states):
    # All ordered legal T hops; retain only the required intermediate/final W.
    final=set(states);paths=defaultdict(int);total=0
    for j,q in enumerate(states):
        for mid,s1,t1 in legal_hops(q):
            assert sum(mid[a]==0 for a in A_SITES)==1
            for out,s2,t2 in legal_hops(mid):
                if out not in final:continue
                paths[(out,q,chord_part(add(s1,s2)))]+=-t1*t2
                total+=1
    return paths,total


def eval_paths(paths,states,phase):
    ix={q:i for i,q in enumerate(states)};mat=sp.zeros(len(states))
    for (out,q,shift),amp in paths.items():mat[ix[out],ix[q]]+=amp*phase**sum(shift)
    return mat


def matmod(M,p,imaginary_root):
    return np.array([[int(sp.re(z))+imaginary_root*int(sp.im(z)) for z in row]
                     for row in M.tolist()],dtype=np.int64)%p


def modular_charpoly(M,p):
    # Faddeev--LeVerrier in F_p; p>dimension so every required division exists.
    n=len(M);ident=np.eye(n,dtype=np.int64);B=ident.copy();coef=[1]
    for k in range(1,n+1):
        MB=M@B%p;c=(-int(np.trace(MB))*pow(k,-1,p))%p
        coef.append(c);B=(MB+c*ident)%p
    assert not np.any(B) # Cayley--Hamilton remainder.
    return coef


def detmod(M,p):
    # Separate Gaussian elimination, for polynomial interpolation checks.
    A=[[int(v)%p for v in row] for row in M];det=1;n=len(A)
    for j in range(n):
        pivot=next((i for i in range(j,n) if A[i][j]),None)
        if pivot is None:return 0
        if pivot!=j:A[j],A[pivot]=A[pivot],A[j];det=-det
        value=A[j][j];det=det*value%p;inv=pow(value,-1,p)
        for i in range(j+1,n):
            factor=A[i][j]*inv%p
            for k in range(j+1,n):A[i][k]=(A[i][k]-factor*A[j][k])%p
            A[i][j]=0
    return det%p


def polynomial_value(coeff,x,p):
    out=0
    for a in coeff:out=(out*x+a)%p
    return out


def main():
    start=time.perf_counter();x=sp.Symbol('lambda')
    bases=[state_space(k) for k in range(3)];P,Q=bases[:2]
    assert list(map(len,bases))==[36,96,36]
    incidence=sp.zeros(8,12)
    for j,(tail,head) in enumerate(EDGES):incidence[tail,j]=1;incidence[head,j]=-1
    tree_minor=incidence.extract(range(1,8),[EDGE_INDEX[e] for e in EDGES if e in TREE])
    assert abs(tree_minor.det())==1
    refs={q:physical_field(q,ZERO) for level in bases for q in level}
    background=tuple(int(v in A_SITES) for v in VERTICES)
    cycle_columns=[physical_field(background,tuple(int(i==j) for i in range(5))) for j in range(5)]
    cycles=sp.Matrix(12,5,lambda i,j:cycle_columns[j][i])
    assert incidence*cycles==sp.zeros(8,5)
    assert cycles.extract([EDGE_INDEX[e] for e in CHORDS],range(5))==sp.eye(5)
    count=0
    for q in P:
        source=refs[q]
        hops=list(legal_hops(q));assert len(hops)==6
        for out,shift,amplitude in hops:
            assert out in Q and amplitude==-1
            target=physical_field(out,chord_part(shift))
            assert add(source,shift)==target
            assert sorted(v for v in q if v)!=sorted([]) # nonempty, then exact invariants.
            assert sorted(v for v in q if v)==sorted(v for v in out if v)
            count+=1
    assert count==216
    paths,ordered_paths=h2_paths(P)
    assert ordered_paths==504
    for q in P:
        row=[(out,shift,amp) for (out,source,shift),amp in paths.items() if source==q]
        assert sum(amp for out,shift,amp in row)==-14
        assert sum(amp for out,shift,amp in row if out==q and shift==ZERO)==-6
        for out,shift,amp in row:
            assert paths[(q,out,tuple(-a for a in shift))]==amp
    full_shift_path_checks=0
    for q in P:
        for mid,s1,_ in legal_hops(q):
            for out,s2,_ in legal_hops(mid):
                if out in P:
                    assert add(refs[q],add(s1,s2))==physical_field(out,chord_part(add(s1,s2)))
                    full_shift_path_checks+=1
    assert full_shift_path_checks==ordered_paths
    polys=[];matrices=[];fiber_results=[]
    for phase in [sp.S.One,sp.I]:
        A=exact_hopping(phase,P,Q);H=-A.conjugate().T*A
        assert H==eval_paths(paths,P,phase)
        assert H==H.conjugate().T and list(H.diagonal())==[-6]*36
        assert all(sp.re(z).is_Integer and sp.im(z).is_Integer for z in H)
        poly=sp.Poly(H.charpoly(x).as_expr(),x,domain=sp.ZZ);assert all(c.is_Integer for c in poly.all_coeffs())
        polys.append(poly);matrices.append(H)
        fiber_results.append({'chord_phase':str(phase),'charpoly_coefficients':[str(v) for v in poly.all_coeffs()],
                              'factorization':str(sp.factor(poly.as_expr())),
                              'matrix_real':[[int(sp.re(z)) for z in row] for row in H.tolist()],
                              'matrix_imag':[[int(sp.im(z)) for z in row] for row in H.tolist()]})
    expected=(x+2)**5*(x+3)**3*(x+4)*(x+5)**5*(x+6)**6*(x+7)**5*(x+8)*(x+14)*(x**3+25*x**2+176*x+248)**3
    assert polys[0]==sp.Poly(expected,x)
    exact_gcd=sp.gcd(*polys);assert exact_gcd==sp.Poly(1,x)
    prime=1009;iroot=469;assert sp.isprime(prime) and iroot**2%prime==prime-1
    modular=[]
    for H,poly in zip(matrices,polys):
        Hmod=matmod(H,prime,iroot);coeff=modular_charpoly(Hmod,prime)
        assert coeff==[int(v)%prime for v in poly.all_coeffs()]
        # 37 distinct exact determinant values certify each degree-36 polynomial.
        determinants=[]
        for lam in range(37):
            D=(lam*np.eye(36,dtype=np.int64)-Hmod)%prime
            value=detmod(D,prime);assert value==polynomial_value(coeff,lam,prime)
            determinants.append(value)
        modular.append({'coefficients':coeff,'determinants_at_0_through_36':determinants})
    f,g=[sp.Poly.from_list(row['coefficients'],x,modulus=prime) for row in modular]
    s,t,h=sp.gcdex(f,g);assert h.as_expr()==1 and s*f+t*g==sp.Poly(1,x,modulus=prime)
    candidates=(-2,-3,-4,-5,-6,-7,-8,-14)
    evaluations={str(a):int(g.eval(a))%prime for a in candidates};assert all(evaluations.values())
    cubic=sp.Poly(x**3+25*x**2+176*x+248,x,modulus=prime)
    cubic_rem=g.rem(cubic);assert sp.gcd(cubic,g).degree()==0
    # The zero-fiber uniform vector is not an eigenstate after localizing flux.
    output=defaultdict(Fraction)
    for (out,q,shift),amp in paths.items():output[(out,shift)]+=Fraction(amp,6)
    mean=sum(Fraction(1,6)*amp for (out,shift),amp in output.items() if shift==ZERO)
    norm_sq=sum(amp*amp for amp in output.values());variance=norm_sq-mean*mean
    assert variance>0
    assert matrices[0]*sp.ones(36,1)==-14*sp.ones(36,1)
    return {
      'scope':'P-space six-record total-charge-four unit-rotor cube; physical point spectrum only',
      'environment':{'python':platform.python_version(),'sympy':sp.__version__,'numpy':np.__version__},
      'edges':EDGES,'tree':sorted(TREE),'chords':CHORDS,
      'basis_P':P,'basis_Pi1':Q,'basis_counts':list(map(len,bases)),
      'tree_minor_determinant':int(tree_minor.det()),'cycle_basis_rows':cycles.tolist(),
      'exact_gauss_first_hop_checks':count,'exact_gauss_second_hop_checks':full_shift_path_checks,
      'ordered_two_hop_paths':ordered_paths,'distinct_laurent_terms':len(paths),
      'zero_phase_absolute_row_sum':14,'diagonal':-6,
      'fibers':fiber_results,'exact_rational_charpoly_gcd':str(exact_gcd.as_expr()),
      'modular_certificate':{'prime':prime,'imaginary_unit_residue':iroot,'fibers':modular,
         'bezout_s_coefficients':[int(v)%prime for v in s.all_coeffs()],
         'bezout_t_coefficients':[int(v)%prime for v in t.all_coeffs()],
         'bezout_identity':'s f_0 + t f_i = 1 modulo 1009',
         'second_polynomial_at_zero_fiber_integer_roots':evaluations,
         'second_polynomial_remainder_mod_zero_fiber_cubic':str(cubic_rem.as_expr()),
         'cubic_gcd_degree':sp.gcd(cubic,g).degree()},
      'normalizable_localized_flux_countercontrol':{'state':'36-word uniform matter vector tensor flux delta_0',
         'norm_squared':'1','mean_H2':str(mean),'mean_H2_squared':str(norm_sq),'variance_H2':str(variance),
         'zero_fiber_eigenvalue':-14,'zero_fiber_vector_is_not_a_normalizable_flux_plane_wave':True},
      'conclusion':'No flat fiber eigenvalue, hence no nonzero normalizable physical H2 eigenvector.',
      'elapsed_seconds':time.perf_counter()-start}

if __name__=='__main__':
    print(json.dumps(main(),indent=2,default=lambda x:int(x) if isinstance(x,sp.Integer) else str(x)))
