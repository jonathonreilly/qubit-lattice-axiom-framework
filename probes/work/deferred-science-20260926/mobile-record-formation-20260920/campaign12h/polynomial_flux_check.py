#!/usr/bin/env python3
"""Primary exact controls for polynomial realization and four-site scope."""
from pathlib import Path
from itertools import product, permutations, combinations
from fractions import Fraction as R
from math import comb
import hashlib
import json
import numpy as np
import sympy as sp

HERE=Path(__file__).resolve().parent
V=np.array([[0,0,0],[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]],dtype=np.int64)
n=np.array([0]+[1]*6,dtype=np.int64)
CHECKS=[]


def check(name,okay,details=None):
    if not okay: raise AssertionError((name,details))
    CHECKS.append({'name':name,'passed':True,'details':details})
    print(json.dumps(CHECKS[-1]),flush=True)


def rank_mod(matrix,prime=1000003):
    a=np.array(matrix,dtype=np.int64,copy=True)%prime
    row=0
    for col in range(a.shape[1]):
        nz=np.flatnonzero(a[row:,col])
        if len(nz)==0: continue
        pivot=row+int(nz[0]);a[[row,pivot]]=a[[pivot,row]]
        a[row,col:]=a[row,col:]*pow(int(a[row,col]),-1,prime)%prime
        factors=a[row+1:,col].copy()
        a[row+1:,col:]=(a[row+1:,col:]-factors[:,None]*a[row,col:])%prime
        row+=1
        if row==len(a): break
    return row


def zero(matrix): return all(sp.expand(x)==0 for x in matrix)


def cubic_tables():
    tables=np.zeros((3,7,7,7),dtype=np.int64)
    for axis in range(3):
        f=V[:,axis];s=2*n-3*f*f
        for labels in product(range(7),repeat=3):
            value=sum(int(n[labels[j[0]]]*s[labels[j[1]]]*f[labels[j[2]]]) for j in permutations(range(3)))
            value+=18*int(np.prod(f[list(labels)]))
            tables[(axis,)+labels]=value
    return tables


def h6(table,states):
    l2,l1,a,b,r1,r2=states.T
    return (table[l2,l1,a]-table[l2,l1,b]+table[l1,a,r1]-table[l1,b,r1]
            +table[a,r1,r2]-table[b,r1,r2])


def check_realization():
    tables=cubic_tables();states=np.indices((7,)*6).reshape(6,-1).T
    check('sharp_cubic_tensor_norm',np.max(abs(tables))==20,{'max_abs_S':'10/3'})
    triples=np.indices((7,)*3).reshape(3,-1).T
    lookup={tuple(v):a for a,v in enumerate(V)}
    count=0
    for perm in permutations(range(3)):
        for signs in product([-1,1],repeat=3):
            matrix=np.zeros((3,3),dtype=int)
            for old in range(3): matrix[perm[old],old]=signs[old]
            labels=np.array([lookup[tuple(matrix@v)] for v in V])
            for old in range(3):
                transformed=labels[triples]
                assert np.array_equal(tables[perm[old]][tuple(transformed.T)], signs[old]*tables[old][tuple(triples.T)])
                count+=len(triples)
    check('cubic_tensor_all_signed_coordinate_transformations',True,{'local_cases':count})
    ranges=[]
    for axis in range(3):
        h=h6(tables[axis],states)
        assert np.array_equal(h6(tables[axis],states[:,[0,1,3,2,4,5]]),-h)
        total=np.zeros(len(states),dtype=np.int64)
        for x in range(6):total+=h6(tables[axis],states[:,[(x+j)%6 for j in [-2,-1,0,1,2,3]]])
        assert not np.any(total)
        ranges.append([int(h.min()),int(h.max())])
    check('six_site_endpoint_antisymmetry_and_six_cycle_balance',True,
          {'configurations_per_axis':len(states),'axes':3,'h_numerator_over_6_ranges':ranges})
    rng=np.random.default_rng(2026092190)
    for length in [7,8,11,17]:
        sample=rng.integers(0,7,size=(10000,length))
        for axis in range(3):
            total=sum((h6(tables[axis],sample[:,[(x+j)%length for j in [-2,-1,0,1,2,3]]]) for x in range(length)),np.zeros(len(sample),dtype=np.int64))
            assert not np.any(total)
    check('longer_periodic_balance_exact_integer_controls',True,{'lengths':[7,8,11,17],'strings_each':10000})
    cases=[[18]+[1]*6,[6]+[1]*6,[2]+[1]*6,[5,1,2,3,4,5,6]]
    tested=0
    for numerators in cases:
        denominator=sum(numerators);p=[R(x,denominator) for x in numerators]
        weights=np.prod(np.array(numerators,dtype=np.int64)[states],axis=1)
        assert int(weights.sum())==denominator**6
        rho=1-p[0]
        for axis in range(3):
            f=V[:,axis];q=f*f
            g=sum(p[a]*int(f[a]) for a in range(7));qi=sum(p[a]*int(q[a]) for a in range(7))
            psi=rho*(2*rho-3*qi)*g+3*g**3
            target=[p[a]*((int(n[a])*(4*rho-3*qi)-3*rho*int(q[a]))*g
                     +(rho*(2*rho-3*qi)+9*g*g)*int(f[a])-3*psi) for a in range(7)]
            tensor_mean=sum(p[a]*p[b]*p[c]*R(int(tables[axis,a,b,c]),6) for a,b,c in product(range(7),repeat=3))
            assert tensor_mean==psi
            h=h6(tables[axis],states)
            for name,rates60 in [('minimal',3+10*np.maximum(h,0)),('constant_K11',660+5*h)]:
                assert rates60.min()>0
                flow=weights*rates60
                current=np.zeros(7,dtype=np.int64)
                np.add.at(current,states[:,2],flow);np.add.at(current,states[:,3],-flow)
                got=[R(int(x),60*denominator**6) for x in current]
                assert got==target,(numerators,axis,name,got,target)
                tested+=1
    check('direct_six_site_product_currents_both_rates',True,{'product_axis_rate_cases':tested,'species_each':7})


def check_symbolic_currents():
    p=sp.Matrix(sp.symbols('p1:7'));rho=sum(p);alpha=sp.symbols('alpha',real=True)
    C=sp.diag(*p)-p*p.T
    r=sp.symbols('rho',positive=True);g=sp.symbols('gx gy gz',real=True)
    on_manifold={p[2*i]:r/6+g[i]/2 for i in range(3)}
    on_manifold.update({p[2*i+1]:r/6-g[i]/2 for i in range(3)})
    at_balance={x:r/6 for x in p}
    field=sp.Matrix([[1]*6,[1,-1,0,0,0,0],[0,0,1,-1,0,0],[0,0,0,0,1,-1],
                     [1,1,-1,-1,0,0],[1,1,1,1,-2,-2]])
    ks=sp.symbols('kx ky kz',real=True);combined=sp.zeros(6)
    for axis in range(3):
        f=sp.Matrix(V[1:,axis].tolist());q=f.applyfunc(lambda x:x*x)
        gi=(p.T*f)[0];qi=(p.T*q)[0]
        psi=alpha*(rho*(2*rho-3*qi)*gi+3*gi**3)
        J=C*sp.Matrix([sp.diff(psi,x) for x in p])
        jac=J.jacobian(p)
        check(f'cubic_entropy_symmetry_axis_{axis}',zero(jac*C-(jac*C).T))
        Jr=sp.expand(sum(J).subs(on_manifold))
        assert sp.expand(Jr-3*alpha*(1-r)*(r*r*g[axis]+3*g[axis]**3))==0
        for j in range(3):
            fj=sp.Matrix(V[1:,j].tolist());qj=fj.applyfunc(lambda x:x*x)
            Jg=sp.expand((fj.T*J)[0].subs(on_manifold))
            Jq=sp.expand((qj.T*J)[0].subs(on_manifold))
            expected_g=alpha*(int(axis==j)*r**3/3+3*r*(1-r)*g[axis]*g[j]-9*g[axis]**3*g[j])
            expected_traceless=9*alpha*g[axis]**3*(int(axis==j)-sp.Rational(1,3))
            assert sp.expand(Jg-expected_g)==0
            assert sp.expand(Jq-Jr/3-expected_traceless)==0
        combined+=ks[axis]*field*jac.subs(at_balance)*field.inv()
    check('exact_density_vector_and_quadrupole_currents_on_axis_isotropic_slice',True)
    ac=3*alpha*r*r*(1-r);bc=alpha*r*r;x,y,z=ks
    expected=sp.Matrix([[0,ac*x,ac*y,ac*z,0,0],[bc*x,0,0,0,0,0],
                       [bc*y,0,0,0,0,0],[bc*z,0,0,0,0,0],[0]*6,[0]*6])
    check('cubic_potential_all_density_linear_matrix',zero(combined-expected))
    zz=sp.symbols('z',real=True)
    rotation=sp.Matrix([[1,-1,0],[1,1,0],[0,0,sp.sqrt(2)]])/sp.sqrt(2)
    gv=sp.Matrix([zz,0,0]);rot=rotation*gv
    def P2(v):return alpha*(r*r/3*sp.eye(3)+2*(1-r)*v*v.T-3*sp.diag(*[x*x for x in v]))
    def P3(v):return alpha*(r**3/3*sp.eye(3)+3*r*(1-r)*v*v.T-9*sp.Matrix([x**3 for x in v])*v.T)
    residual2=sp.simplify(P2(rot)-rotation*P2(gv)*rotation.T)
    residual3=sp.simplify(P3(rot)-rotation*P3(gv)*rotation.T)
    check('quadratic_rule_nonzero_rotation_residual',residual2[0,1]==3*alpha*zz**2/2)
    check('cubic_rule_quadratic_defect_removed_quartic_retained',residual3==9*alpha*zz**4/4*sp.Matrix([[1,1,0],[1,1,0],[0,0,0]]))


def check_four_site_classification():
    q=7;triples=list(product(range(q),repeat=3));index={t:i for i,t in enumerate(triples)}
    rows=[]
    for l,a,b,r in product(range(q),repeat=4):
        row=np.zeros(q**3,dtype=np.int64)
        for t,c in [((l,a,b),1),((l,b,a),1),((a,b,r),-1),((b,a,r),-1)]:row[index[t]]+=c
        rows.append(row)
    matrix=np.array(rows);basis=[]
    for a,b in combinations(range(q+1),2):
        # This indexes every unordered pair with repetition: (a,b-1).
        b-=1
        S=np.zeros((q,q),dtype=np.int64);S[a,b]=S[b,a]=1
        basis.append([S[l,x]-S[l,y]+S[x,y] for l,x,y in triples])
    for selected in combinations(range(q),3):
        tensor={}
        for perm in permutations(range(3)):
            inversions=sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
            tensor[tuple(selected[j] for j in perm)]=(-1)**inversions
        basis.append([tensor.get(t,0) for t in triples])
    basis=np.array(basis,dtype=np.int64).T
    assert not np.any(matrix@basis)
    lower=rank_mod(matrix);kernel_rank=rank_mod(basis)
    check('exact_four_site_constraint_rank_certificate',lower==280 and kernel_rank==63 and lower+kernel_rank==343,
          {'prime':1000003,'constraint_matrix_shape':list(matrix.shape),'rank_mod_prime':lower,
           'integer_kernel_columns':kernel_rank,'h_dimension_after_constant_gauge':62,
           'interpretation':'Finite-field lower rank plus an exact integer kernel of complementary rank certify the rational rank; the general decomposition proof is in the note.'})
    # Degree <=2 vector polynomials in qx,qy,qz,gx,gy,gz under proper rotations.
    exponents=[(0,)*6]
    for degree in [1,2]:
        exponents.extend(t for t in product(range(degree+1),repeat=6) if sum(t)==degree)
    monindex={t:i for i,t in enumerate(exponents)};size=len(exponents)
    constraints=[]
    for perm in permutations(range(3)):
        inv=sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
        for signs in product([-1,1],repeat=3):
            if (-1)**inv*np.prod(signs)!=1:continue
            rows=np.zeros((3*size,3*size),dtype=np.int64)
            for j in range(3):
                for mi,exp in enumerate(exponents):
                    new=[0]*6;sign=1
                    for a in range(3):
                        new[perm[a]]+=exp[a];new[3+perm[a]]+=exp[3+a]
                        sign*=signs[a]**exp[3+a]
                    ni=monindex[tuple(new)]
                    rows[j*size+ni,j*size+mi]+=sign
                    rows[j*size+mi,perm[j]*size+mi]-=signs[j]
            constraints.append(rows)
    constraints=np.vstack(constraints)
    b=np.zeros((3*size,3),dtype=np.int64)
    for j in range(3):
        exp=[0]*6;exp[3+j]=1;b[j*size+monindex[tuple(exp)],0]=1
        for a in range(3):
            term=exp.copy();term[a]=1;b[j*size+monindex[tuple(term)],1]=1
        term=exp.copy();term[j]=1;b[j*size+monindex[tuple(term)],2]=1
    assert not np.any(constraints@b)
    check('all_cubic_vector_potentials_degree_at_most_two',rank_mod(constraints)==81 and rank_mod(b)==3,
          {'monomials_per_component':size,'proper_rotations':24,'dimension':3,
           'basis':['g_i','rho*g_i','q_i*g_i']})


def main():
    check_realization();check_symbolic_currents();check_four_site_classification()
    result={'status':'all_primary_controls_passed','checks':CHECKS,'count':len(CHECKS),
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'scope':'Exact finite and symbolic controls; general telescoping and classification proofs are in the primary notes. Independent scrutiny is pending.'}
    (HERE/'POLYNOMIAL_FLUX_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':main()
