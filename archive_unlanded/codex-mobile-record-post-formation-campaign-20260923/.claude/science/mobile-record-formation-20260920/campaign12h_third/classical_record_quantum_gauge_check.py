#!/usr/bin/env python3
"""Finite controls for the supplied classical-record/quantum-fiber model.

No native M2 compiler or physical continuum identification is tested here.
"""
from __future__ import annotations

import itertools
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp
from scipy import sparse
from scipy.sparse.linalg import expm_multiply

OUT = Path(__file__).resolve().parent


def charge(a):
    return 0 if a == 0 else (1 if a in (1, 2) else -1)


def content(q, b):
    return (1 if q == 1 else 3) + (b == -1)


def fibers(m, marked):
    alphabet = range(5) if marked else (0, 1, 3)
    configs = [c for c in itertools.product(alphabet, repeat=4)
               if sum(map(charge, c)) == 0]
    fields = list(itertools.product(range(m), repeat=4))
    by_q = {}
    for e in fields:
        q = tuple((e[i]-e[(i-1) % 4]) % m for i in range(4))
        by_q.setdefault(q, []).append(e)
    basis = [by_q[tuple(charge(a) % m for a in c)] for c in configs]
    assert all(len(b) == m for b in basis)
    return configs, basis


def shift_map(source, target, edge, amount, m):
    index = {e: i for i, e in enumerate(target)}
    u = np.zeros((m, m), complex)
    for a, e in enumerate(source):
        out = list(e); out[edge] = (out[edge]+amount) % m
        assert tuple(out) in index, (e, edge, amount, target)
        u[index[tuple(out)], a] = 1
    assert np.array_equal(u.conj().T @ u, np.eye(m))
    return u


def loop(basis, m):
    index = {e: i for i, e in enumerate(basis)}
    w = np.zeros((m, m), complex)
    for a, e in enumerate(basis):
        w[index[tuple((x+1) % m for x in e)], a] = 1
    assert np.array_equal(w.conj().T @ w, np.eye(m))
    return w


def exact_instrument():
    rows = []
    for m in (3, 5, 7):
        w = sp.zeros(m)
        for j in range(m): w[(j+1) % m, j] = 1
        eye = sp.eye(m)
        kraus = {(b, eta): (eye+b*(w if eta == 1 else w.T))/(2*sp.sqrt(2))
                 for b in (1, -1) for eta in (1, -1)}
        loss = sum((k.T*k for k in kraus.values()), sp.zeros(m))
        assert loss == eye
        for b in (1, -1):
            effect = sum((kraus[b, eta].T*kraus[b, eta] for eta in (1, -1)), sp.zeros(m))
            assert effect == (eye+b*(w+w.T)/2)/2
            cp = sum((sp.kronecker_product(kraus[b, eta], kraus[b, eta])
                      for eta in (1, -1)), sp.zeros(m*m))
            reversed_cp = sum((sp.kronecker_product(kraus[b, -eta], kraus[b, -eta])
                               for eta in (1, -1)), sp.zeros(m*m))
            assert cp == reversed_cp
        channel = sum((sp.kronecker_product(k, k) for k in kraus.values()), sp.zeros(m*m))
        assert channel == sp.eye(m*m)/2+(sp.kronecker_product(w, w)+sp.kronecker_product(w.T, w.T))/4
        for power in range(m):
            obs = w**power
            dual = sum((k.T*obs*k for k in kraus.values()), sp.zeros(m))
            assert dual == obs
        # A Wilson eigenstate has a measurable, nontrivial permanent-bit law.
        theta = 2*math.pi/m
        rows.append({'m':m, 'exact_total_effect':'I', 'exact_bit_effect':'(I+b Re W)/2',
                     'orientation_reversal_coarse_map':'equal',
                     'Wilson_powers_preserved':m,
                     'p_plus_W1':1., 'p_plus_W_exp_2pii_over_m':(1+math.cos(theta))/2})
    return rows


def build(m, marked):
    configs, bases = fibers(m, marked)
    ci = {c:i for i,c in enumerate(configs)}
    patterns = sorted({tuple(int(x != 0) for x in c) for c in configs})
    pi = {p:i for i,p in enumerate(patterns)}
    width=m*m; blocks=len(configs)
    eye=np.eye(m); ie=sparse.eye(m, format='csr')
    rows=[]; cols=[]; vals=[]
    def add_block(dst, src, a):
        a=sparse.coo_matrix(a)
        rows.extend((dst*width+a.row).tolist())
        cols.extend((src*width+a.col).tolist())
        vals.extend(a.data.tolist())
    def jump(dst, src, a):
        add_block(dst,src,sparse.kron(a.conjugate(),a,format='csr'))
        aa=a.conj().T@a
        add_block(src,src,-.5*(sparse.kron(ie,aa)+sparse.kron(aa.T,ie)))
    wilson=[loop(b,m) for b in bases]
    classical=np.zeros((len(patterns),len(patterns)))
    rate_lists={}
    hops=births=0
    max_intertwining=0.
    for src,(c,basis,w) in enumerate(zip(configs,bases,wilson)):
        centered=lambda e: e if e <= m//2 else e-m
        h=np.diag([.04*sum((i+1)*centered(e[i])**2 for i in range(4)) for e in basis])
        h=h+.13*(w+w.conj().T)+.07j*(w-w.conj().T)
        assert np.linalg.norm(h-h.conj().T)<1e-14
        add_block(src,src,-1j*(sparse.kron(ie,h)-sparse.kron(h.T,ie)))
        occ=tuple(int(x != 0) for x in c)
        transitions={}
        for edge in range(4):
            x=edge; y=(edge+1)%4
            krate=.3+.11*edge
            beta=.5+.13*edge
            if bool(c[x]) != bool(c[y]):
                tail_to_head=bool(c[x]); start=x if tail_to_head else y
                d=list(c); d[x],d[y]=d[y],d[x]; d=tuple(d); dst=ci[d]
                q=charge(c[start]); exponent=-q if tail_to_head else q
                u=shift_map(basis,bases[dst],edge,exponent,m)
                max_intertwining=max(max_intertwining,float(np.linalg.norm(wilson[dst]@u-u@w)))
                jump(dst,src,np.sqrt(krate)*u); hops+=1
                destocc=tuple(int(a != 0) for a in d)
                transitions[destocc]=transitions.get(destocc,0)+krate
            if c[x] == c[y] == 0:
                local_loss=np.zeros((m,m),complex)
                for q in (1,-1):
                    for b in ((1,-1) if marked else (1,)):
                        d=list(c); d[x]=content(q,b); d[y]=content(-q,b); d=tuple(d); dst=ci[d]
                        u=shift_map(basis,bases[dst],edge,q,m)
                        max_intertwining=max(max_intertwining,float(np.linalg.norm(wilson[dst]@u-u@w)))
                        for eta in ((1,-1) if marked else (1,)):
                            k=(eye+b*(w if eta==1 else w.conj().T))/(2*np.sqrt(2)) if marked else eye
                            a=np.sqrt(beta/2)*u@k
                            jump(dst,src,a); local_loss+=a.conj().T@a; births+=1
                assert np.linalg.norm(local_loss-beta*eye)<2e-14
                destocc=list(occ); destocc[x]=destocc[y]=1; destocc=tuple(destocc)
                transitions[destocc]=transitions.get(destocc,0)+beta
        if occ in rate_lists:
            assert transitions == rate_lists[occ]
        else:
            rate_lists[occ]=transitions
            for dest, rate in transitions.items(): classical[pi[dest],pi[occ]]+=rate
            classical[pi[occ],pi[occ]]-=sum(transitions.values())
    gen=sparse.coo_matrix((vals,(rows,cols)),shape=(blocks*width,blocks*width)).tocsr()
    tr_r=[];tr_c=[]
    for src,c in enumerate(configs):
        p=pi[tuple(int(x!=0) for x in c)]
        for j in range(m):tr_r.append(p);tr_c.append(src*width+j*(m+1))
    trace=sparse.coo_matrix((np.ones(len(tr_r)),(tr_r,tr_c)),shape=(len(patterns),blocks*width)).tocsr()
    residual=trace@gen-sparse.csr_matrix(classical)@trace
    closure=float(abs(residual.data).max()) if residual.nnz else 0.
    assert closure<3e-14
    assert max_intertwining == 0.
    return gen,trace,classical,configs,bases,patterns,{
        'm':m,'readout_bits':marked,'record_configurations':blocks,
        'gauge_fiber_dimension':m,'CQ_Liouville_dimension':blocks*width,
        'occupation_patterns':len(patterns),'directed_hop_jumps':hops,'birth_Kraus_jumps':births,
        'Gauss_maps':'every enumerated unit shift is a whole-fiber permutation',
        'Wilson_intertwining_residual':max_intertwining,'occupation_closure_residual':closure}


def evolution(m,marked):
    gen,tr,q,configs,bases,patterns,row=build(m,marked)
    origin=configs.index((0,0,0,0)); op=patterns.index((0,0,0,0))
    full=patterns.index((1,1,1,1))
    times=(.1,.8,2.,20.)
    matrices=[]
    # Different pure and mixed gauge inputs, identical definite empty records.
    psi=np.ones(m,complex)/np.sqrt(m)
    phi=np.exp(2j*np.pi*np.arange(m)/m)/np.sqrt(m)
    local=np.zeros(m); local[0]=1
    for vec in (psi,phi,local): matrices.append(np.outer(vec,vec.conj()))
    matrices.append(np.eye(m)/m)
    tests=[]
    classical_initial=np.zeros(len(patterns));classical_initial[op]=1
    for t in times:
        prediction=expm_multiply(t*sparse.csr_matrix(q),classical_initial)
        errors=[]; minima=[]
        for rho in matrices:
            initial=np.zeros(gen.shape[0],complex)
            initial[origin*m*m:(origin+1)*m*m]=rho.reshape(-1,order='F')
            evolved=expm_multiply(t*gen,initial)
            errors.append(float(np.linalg.norm(tr@evolved-prediction)))
            for block in range(len(configs)):
                a=evolved[block*m*m:(block+1)*m*m].reshape(m,m,order='F')
                minima.append(float(np.linalg.eigvalsh((a+a.conj().T)/2).min()))
        assert max(errors)<4e-12 and min(minima)>-4e-12
        tests.append({'time':t,'classical_full_probability':float(prediction[full]),
                      'four_field_input_occupation_errors':errors,'minimum_block_eigenvalue':min(minima)})
    row['evolution_checks']=tests
    return row


def main():
    result={'status':'PASS','exact_Wilson_instrument':exact_instrument(),
            'physical_CQ_controls':[evolution(m,marked) for m,marked in ((3,False),(5,False),(3,True),(5,True))],
            'failed_attempts':[],
            'limits':'Finite C4 controls support the general direct proofs; no native lattice compilation, full-trajectory retention, rotor limit or physical phase is established.'}
    (OUT/'CLASSICAL_RECORD_QUANTUM_GAUGE_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
