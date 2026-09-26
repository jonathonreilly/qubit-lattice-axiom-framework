#!/usr/bin/env python3
"""Independently assembled two-hole mean operators and singular-limit controls."""
from __future__ import annotations

import itertools
import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp
from scipy.linalg import solve_continuous_lyapunov

OUT=Path(__file__).resolve().parent


def geometry(k):
    states=list(itertools.combinations(range(k),2));index={c:i for i,c in enumerate(states)}
    neighbors=[];contact=[]
    for c in states:
        contact.append(any((x+1)%k in c for x in c))
        row=[]
        for x in c:
            for step in [-1,1]:
                y=(x+step)%k
                if y not in c:
                    row.append(index[tuple(sorted((set(c)-{x})|{y}))])
        assert len(row)==len(set(row))
        neighbors.append(row)
    return states,index,neighbors,np.array(contact,dtype=int)


def exact_four_cycle():
    kappa,beta,d=sp.symbols('kappa beta d',nonzero=True,real=True)
    states,index,neighbors,contact=geometry(4);dim=len(states)
    h=sp.zeros(dim)
    for i,row in enumerate(neighbors):
        for j in row:h[i,j]=kappa
    a=sp.Rational(3,2)/beta
    bb=a+1/(beta+d)+1/(2*(beta+2*d))+1/(2*d)+(d+beta/2)/(8*kappa**2)
    m=sp.zeros(dim)
    for i,c in enumerate(states):
        for j,e in enumerate(states):
            if i==j:m[i,j]=a if contact[i] else bb
            elif contact[i] and contact[j]:m[i,j]=1/(2*(beta+d*(2-len(set(c)&set(e)))))
            elif not contact[i] and not contact[j]:m[i,j]=-1/(2*d)
            else:m[i,j]=(sp.I if contact[i] else -sp.I)/(8*kappa)
    dual=sp.I*(h*m-m*h)
    for i,c in enumerate(states):
        for j,e in enumerate(states):
            dual[i,j]-=(d*(2-len(set(c)&set(e)))+beta*sp.Rational(int(contact[i]+contact[j]),2))*m[i,j]
    assert (dual+sp.eye(dim)).applyfunc(sp.factor)==sp.zeros(dim)
    expected=sp.Rational(3,2)/beta+1/(3*(beta+d))+1/(6*(beta+2*d))+1/(6*d)+d/(24*kappa**2)+beta/(48*kappa**2)
    assert sp.factor(sp.trace(m)/dim-expected)==0
    dark=sp.zeros(dim,1);dark[index[(0,2)]]=1;dark[index[(1,3)]]=-1
    pd=dark*dark.T/2
    assert h*pd==sp.zeros(dim)
    assert (d*m).applyfunc(lambda x:sp.limit(x,d,0))==pd
    strong=(m/d).applyfunc(lambda x:sp.limit(x,d,sp.oo))
    assert strong==sp.diag(*[0 if c else 1/(8*kappa**2) for c in contact])
    return {'states':states,'adjacent_mean':str(a),'uniform_mean':str(expected),
            'opposite_diagonal_mean':str(bb),'dark_pure_mean':str(sp.factor((dark.T*m*dark)[0]/2)),
            'full_exact_Poisson_residual':'zero','small_d_operator_limit':'d M -> P_dark',
            'large_d_operator_limit':'M/d -> diag(0 on contact,1/(8 kappa^2) on opposite)'}


def dark_projection(k,states,index):
    columns=[]
    for distance in range(2,k//2+1):
        if 2*distance==k:
            if distance%2:continue
            period=k//2
        else:period=k
        col=np.zeros(len(states))
        for x in range(period):col[index[tuple(sorted((x,(x+distance)%k)))]]=(-1)**x/math.sqrt(period)
        columns.append(col)
    q=np.column_stack(columns)
    assert np.linalg.norm(q.T@q-np.eye(q.shape[1]))<1e-13
    return q@q.T


def invariant_orbits(k,states,index):
    dim=len(states);perms=[]
    for sign in [-1,1]:
        for shift in range(k):
            perms.append([index[tuple(sorted(((sign*x+shift)%k for x in c)))] for c in states])
    mapping={};representatives=[]
    for i in range(dim):
        for j in range(dim):
            if (i,j) in mapping:continue
            label=len(representatives);representatives.append((i,j))
            for perm in perms:mapping[(perm[i],perm[j])]=label
    return mapping,representatives


def mean_operator(k,kappa,beta,d,states,neighbors,contact,mapping,reps):
    size=len(reps);a=np.zeros((size,size),complex);rhs=np.zeros(size,complex)
    for row,(i,j) in enumerate(reps):
        for z in neighbors[i]:a[row,mapping[(z,j)]]+=1j*kappa
        for z in neighbors[j]:a[row,mapping[(i,z)]]-=1j*kappa
        a[row,row]-=d*(2-len(set(states[i])&set(states[j])))+beta*(contact[i]+contact[j])/2
        rhs[row]=-int(i==j)
    values=np.linalg.solve(a,rhs)
    m=np.array([[values[mapping[(i,j)]] for j in range(len(states))] for i in range(len(states))])
    precision='float64'
    preliminary_hermiticity=float(np.linalg.norm(m-m.conj().T))
    if preliminary_hermiticity>=1e-8:
        # Preserve the original parameters and all verification thresholds.
        # Reassemble coefficients, rather than importing a rounded solve,
        # when the near-dark singular limit loses absolute Hermiticity digits.
        mp.mp.dps=70
        aa=mp.matrix(size);rr=mp.matrix(size,1)
        kk=mp.mpf(str(kappa));bb=mp.mpf(str(beta));dd=mp.mpf(str(d))
        for row,(i,j) in enumerate(reps):
            for z in neighbors[i]:aa[row,mapping[(z,j)]]+=mp.j*kk
            for z in neighbors[j]:aa[row,mapping[(i,z)]]-=mp.j*kk
            aa[row,row]-=dd*(2-len(set(states[i])&set(states[j])))+bb*int(contact[i]+contact[j])/2
            rr[row]=-int(i==j)
        values=[complex(x) for x in mp.lu_solve(aa,rr)]
        m=np.array([[values[mapping[(i,j)]] for j in range(len(states))] for i in range(len(states))])
        precision='70 decimal digits, independently reassembled coefficients'
    h=np.zeros_like(m)
    for i,ngh in enumerate(neighbors):h[i,ngh]=kappa
    residual=1j*(h@m-m@h)+np.eye(len(states))
    for i,c in enumerate(states):
        for j,e in enumerate(states):
            residual[i,j]-=(d*(2-len(set(c)&set(e)))+beta*(contact[i]+contact[j])/2)*m[i,j]
    assert np.max(abs(residual))<2e-7,(k,d,np.max(abs(residual)))
    assert np.linalg.norm(m-m.conj().T)<2e-7
    assert np.linalg.eigvalsh((m+m.conj().T)/2).min()>-1e-7
    return m,h,float(np.max(abs(residual))),precision,preliminary_hermiticity


def numerical_families():
    rows=[];kappa=4/3;beta=7/5
    for k in [4,6,8,10,12]:
        states,index,neighbors,contact=geometry(k);dim=len(states)
        mapping,reps=invariant_orbits(k,states,index)
        pd=dark_projection(k,states,index);rank=round(np.trace(pd));assert rank==2*(k//4)-1
        expected_weak=rank/((k-1)*(k-2))
        expected_strong=(k-2)*(k-3)/(48*kappa*kappa)
        tests=[]
        for d in [1e-5,1e-3,.4,10.,1e3,1e5]:
            m,h,res,precision,preliminary_hermiticity=mean_operator(k,kappa,beta,d,states,neighbors,contact,mapping,reps)
            adjacent=np.diag(m)[contact.astype(bool)].real
            mix=float(np.trace(m).real/dim)
            exact_adj=(k-1)/(2*beta)
            assert np.max(abs(adjacent-exact_adj))<2e-6,(k,d,adjacent)
            assert mix>exact_adj
            gamma=beta*np.diag(contact)
            energy=float(np.trace(gamma@m@m).real)
            for x in range(k):
                occ=np.diag([int(x not in c) for c in states])
                comm=occ@m-m@occ
                energy+=d*np.linalg.norm(comm)**2/2
            assert abs(energy-np.trace(m).real)/max(1,np.trace(m).real)<2e-6
            assert np.linalg.norm(h@pd)<1e-12 and np.linalg.norm(gamma@pd)<1e-12
            for x in range(k):
                hole=np.diag([int(x in c) for c in states])
                assert np.linalg.norm(pd@hole@pd-2*pd/k)<1e-12
            tests.append({'d':d,'adjacent_mean':float(adjacent.mean()),'uniform_mean':mix,
                          'd_times_uniform':d*mix,'uniform_over_d':mix/d,
                          'Poisson_max_residual':res,'Dirichlet_sum_relative_residual':abs(energy-np.trace(m).real)/max(1,np.trace(m).real),
                          'solve_precision':precision,'preliminary_float64_Hermiticity_residual':preliminary_hermiticity})
        assert abs(tests[0]['d_times_uniform']/expected_weak-1)<.003
        assert abs(tests[-1]['uniform_over_d']/expected_strong-1)<.003
        # The d=0 bright corner has no loss-free eigenstate. Solve its smaller
        # ordinary Lyapunov equation; dark inputs instead have infinite mean.
        eigenvalues,eigenvectors=np.linalg.eigh(pd)
        qb=eigenvectors[:,eigenvalues<.5]
        hb=qb.conj().T@h@qb;gb=qb.conj().T@(beta*np.diag(contact))@qb
        drift=-1j*hb-gb/2
        mb=solve_continuous_lyapunov(drift.conj().T,-np.eye(qb.shape[1]))
        mzero=qb@mb@qb.conj().T
        adjzero=np.diag(mzero)[contact.astype(bool)].real
        expected_zero=(dim-rank)/(beta*k)
        assert np.max(abs(adjzero-expected_zero))<2e-10
        rows.append({'K':k,'dimension':dim,'invariant_matrix_orbits':len(reps),'dark_dimension':rank,
                     'kappa':kappa,'beta':beta,'small_d_uniform_coefficient':expected_weak,
                     'large_d_uniform_coefficient':expected_strong,'d_positive_adjacent_mean':(k-1)/(2*beta),
                     'd_zero_bright_adjacent_mean':expected_zero,'d_zero_Lyapunov_max_error':float(np.max(abs(adjzero-expected_zero))),
                     'tests':tests})
    return rows


def main():
    result={'status':'PASS','four_cycle_exact':exact_four_cycle(),'fixed_K_numeric_controls':numerical_families(),
            'proof_boundary':'All-size identities and singular limits are established separately in REPORT.md; finite floating-point checks are not proofs of rates or limits.',
            'failed_attempts':[{'path':'failed_attempts/clock/DIAGNOSIS.json',
                                'issue':'Initial float64 solve at K=10,d=1e-5 failed the absolute Hermiticity threshold.',
                                'repair':'Reassemble flagged solves at70decimal digits; physical parameters and all thresholds unchanged.'}]}
    (OUT/'CLOCK_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))


if __name__=='__main__':main()
