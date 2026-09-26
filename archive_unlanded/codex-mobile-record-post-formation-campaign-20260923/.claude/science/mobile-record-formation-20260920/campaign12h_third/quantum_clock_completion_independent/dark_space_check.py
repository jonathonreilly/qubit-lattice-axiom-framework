#!/usr/bin/env python3
"""Exact small-cycle dark-space and physical T-sector controls over Q(i)."""
from __future__ import annotations

import itertools
import json
from pathlib import Path

import sympy as sp

OUT=Path(__file__).resolve().parent


def hole_hamiltonian(k,h,links,potential=None):
    states=list(itertools.combinations(range(k),h));ix={c:i for i,c in enumerate(states)}
    mat=sp.SparseMatrix(len(states),len(states),{})
    for j,c in enumerate(states):
        mat[j,j]=0 if potential is None else potential(c)
        for x in c:
            for y,amp in [((x+1)%k,links[x]),((x-1)%k,sp.conjugate(links[(x-1)%k]))]:
                if y not in c:mat[ix[tuple(sorted((set(c)-{x})|{y}))],j]+=amp
    assert mat==mat.adjoint()
    contact=[i for i,c in enumerate(states) if any((x+1)%k in c for x in c)]
    free=[i for i in range(len(states)) if i not in contact]
    return states,mat,contact,free


def row_basis(mat,n):
    if mat.rows==0:return sp.zeros(0,n)
    reduced,pivots=mat.rref()
    return reduced[:len(pivots),:]


def exact_dark_dimension(k,h,links,potential=None,monitor=None):
    states,ham,contact,free=hole_hamiltonian(k,h,links,potential)
    n=len(free)
    if n==0:return {'dimension':len(states),'contact_free_dimension':0,'dark_dimension':0,'rank_iterations':[]}
    compression=ham.extract(free,free)
    boundary=ham.extract(contact,free)
    operators=[compression]
    if monitor is not None:operators.append(sp.diag(*[int(monitor in states[i]) for i in free]))
    rows=row_basis(boundary,n);history=[rows.rows]
    while True:
        joined=sp.Matrix.vstack(rows,*[rows*a for a in operators])
        more=row_basis(joined,n);history.append(more.rows)
        if more.rows==rows.rows:break
        rows=more
    return {'dimension':len(states),'contact_free_dimension':n,'dark_dimension':n-more.rows,
            'rank_iterations':history,'field':'exact rational complex Q(i), not modular rank'}


def finite_cases():
    cases=[]
    def add(name,k,h,links,expected,potential=None,monitor=None):
        result=exact_dark_dimension(k,h,links,potential,monitor)
        assert result['dark_dimension']==expected,(name,result,expected)
        cases.append({'name':name,'K':k,'h':h,'links':[str(x) for x in links],
                      'diagonal_potential':potential is not None,'monitored_site':monitor,**result})
    for k in [4,6,8,10]:
        add('uniform_flux_zero',k,2,[1]*k,2*(k//4)-1)
        expected=k//2-2+int((k//2)%2==1)
        add('uniform_magnitude_flux_pi',k,2,[1]*(k-1)+[-1],expected)
        add('nonexceptional_flux_pi_over_two',k,2,[1]*(k-1)+[sp.I],0)
        add('one_monitored_site_at_exceptional_flux',k,2,[1]*k,0,monitor=0)
    add('paired_opposite_magnitudes',4,2,[1,2,1,2],1)
    add('unpaired_magnitudes_remove_dark',4,2,[1,1,1,2],0)
    add('diagonal_detuning_removes_dark',4,2,[1]*4,0,potential=lambda c:int(c==(0,2)))
    add('nonuniform_diagonal_and_complex_hops',6,2,[1,sp.I,2,-1,1,sp.I],0,
        potential=lambda c:sum(3**x for x in c),monitor=2)
    for k,h in [(6,3),(7,3),(8,3),(10,3),(8,4),(10,4)]:
        links=[(1,sp.I,2,-1)[i%4] for i in range(k)]
        add('three_or_more_holes_with_arbitrary_potential',k,h,links,0,
            potential=lambda c:sum((x+1)**2 for x in c))
    # Odd cycles provide an independent check of (-1)^K exp(2iPhi)=1.
    for k in [5,7]:
        add('odd_cycle_nonexceptional_zero_flux',k,2,[1]*k,0)
        add('odd_cycle_exceptional_pi_over_two',k,2,[1]*(k-1)+[sp.I],(k-3)//2)
    add('one_hole_cannot_form_a_pair_even_with_monitoring',6,1,[1]*6,6,monitor=0)
    return cases


def physical_sector_checks():
    rows=[]
    for k in [4,6,8]:
        dim=1<<k;mask=dim-1
        bit=lambda b,i:(b>>(i%k))&1
        occupations=lambda b:tuple(bit(b,i)^bit(b,i-1) for i in range(k))
        ham=sp.SparseMatrix(dim,dim,{})
        number=[]
        for b in range(dim):
            number.append(sum(occupations(b)))
            for i in range(k):
                if bit(b,i-1)!=bit(b,i+1):ham[b^(1<<i),b]=1
        t=sp.SparseMatrix(dim,dim,{(b^mask,b):1 for b in range(dim)})
        assert ham*t==t*ham
        for h in range(0,k+1,2):
            states=list(itertools.combinations(range(k),h));ix={c:i for i,c in enumerate(states)}
            representatives={}
            for b in range(dim):
                if bit(b,k-1)==0 and number[b]==k-h:
                    holes=tuple(i for i,n in enumerate(occupations(b)) if not n)
                    representatives[holes]=b
            assert set(representatives)==set(states)
            for tau in [-1,1]:
                lift=sp.SparseMatrix(dim,len(states),{})
                for c,b in representatives.items():lift[b,ix[c]]=1;lift[b^mask,ix[c]]=tau
                assert lift.T*lift==2*sp.eye(len(states))
                assert t*lift==tau*lift
                reduced=lift.T*ham*lift/2
                _,expected,contact,free=hole_hamiltonian(k,h,[1]*(k-1)+[tau])
                assert reduced==expected,(k,h,tau)
                occupation_zero=sp.diag(*[occupations(b)[0] for b in range(dim)])
                assert lift.T*occupation_zero*lift/2==sp.diag(*[int(0 not in c) for c in states])
                loss=[sum((i+1)%k in c for i in c) for c in states]
                assert [i for i,x in enumerate(loss) if x>0]==contact
                rows.append({'K':k,'h':h,'T_sector':tau,'sector_dimension':len(states),
                             'boundary_hopping_sign':tau,'exact_reduction':'verified',
                             'one_occupation_monitor_and_contact_kernel':'verified'})
    return rows


def countercontrols():
    # Positive diagonal entries alone do not mean positive definite contact loss.
    sx=sp.Matrix([[0,1],[1,0]]);gamma=sp.eye(2)+sx;v=sp.Matrix([1,-1])
    assert all(gamma[i,i]>0 for i in range(2)) and gamma*v==sp.zeros(2,1)
    assert sx*v==-v
    # C4 empty-start births enter only contact states, which are orthogonal to
    # its T=+ two-hole dark vector. Existence is not empty-start reachability.
    states,ham,contact,free=hole_hamiltonian(4,2,[1]*4)
    dark=sp.zeros(len(states),1);dark[states.index((0,2))]=1;dark[states.index((1,3))]=-1
    assert ham*dark==sp.zeros(len(states),1)
    assert all(dark[i]==0 for i in contact)
    return {'basiswise_loss_positivity_is_insufficient':{'Gamma':'I+sigma_x','H':'sigma_x',
                                                       'dark_vector':'(1,-1)','Gamma_kernel_nonzero':True},
            'C4_empty_start_boundary':'First birth from four vacancies leaves an adjacent two-hole configuration. Its entire range is orthogonal to the dark space; the H/loss evolution cannot populate that invariant dark space. The other T sector has no two-hole dark state. Thus a two-hole dark vector is not proof of empty-start trapping.'}


def main():
    result={'status':'PASS','exact_dark_space_cases':finite_cases(),'physical_gauge_sector_reductions':physical_sector_checks(),
            'countercontrols':countercontrols(),'failed_attempts':[],
            'proof_boundary':'Finite exact Q(i) ranks and matrix reductions corroborate, rather than establish, the all-size minimal-gap and single-monitor arguments.'}
    (OUT/'DARK_SPACE_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))


if __name__=='__main__':main()
