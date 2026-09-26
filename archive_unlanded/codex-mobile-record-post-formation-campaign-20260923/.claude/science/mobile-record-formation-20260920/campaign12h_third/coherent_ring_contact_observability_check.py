#!/usr/bin/env python3
"""Exact finite-field observability certificates for coherent hole rings.

Full rank mod 65537 with i mapped to 256 certifies full rank over Q(i).
Deficient ranks are only diagnostics unless an exact dark witness is checked.
No author mean-time or gauge-ring helper is imported.
"""
from pathlib import Path
from itertools import combinations
from collections import defaultdict, deque
from datetime import datetime, timezone
import hashlib
import json
import math
import time
import sympy as s

HERE=Path(__file__).resolve().parent
PRIME=65537
IMAG=256
assert IMAG*IMAG % PRIME == PRIME-1
assert all(PRIME % q for q in range(2,math.isqrt(PRIME)+1))


def insert(row,basis):
    row={i:v % PRIME for i,v in row.items() if v % PRIME}
    while row:
        pivot=min(row)
        if pivot not in basis:
            inv=pow(row[pivot],-1,PRIME)
            reduced={i:v*inv % PRIME for i,v in row.items()}
            basis[pivot]=reduced
            return reduced
        factor=row[pivot]
        for i,v in basis[pivot].items():
            value=(row.get(i,0)-factor*v) % PRIME
            if value: row[i]=value
            else: row.pop(i,None)
    return None


def build(K,h,phase='real',open_chain=False,inhomogeneous=False,potential=False):
    states=list(combinations(range(K),h));index={a:i for i,a in enumerate(states)}
    occupied=[set(a) for a in states]
    edges=list(range(K-1 if open_chain else K))
    contact={i for i,a in enumerate(occupied) if any(x in a and (x+1)%K in a for x in edges)}
    rows=[{} for _ in states]
    phase0={'real':1,'minus':PRIME-1,'quarter':IMAG,'minus_quarter':PRIME-IMAG}[phase]
    for col,a in enumerate(occupied):
        if potential:
            rows[col][col]=sum((x+1)**2 for x in a) % PRIME
        for x in edges:
            y=(x+1)%K
            if (x in a)==(y in a):continue
            amplitude=(x+1 if inhomogeneous else 1)
            z=phase0 if x==0 else 1
            if x not in a: z=pow(z,-1,PRIME)
            target=(a-{x,y})|({y} if x in a else {x})
            row=index[tuple(sorted(target))]
            rows[row][col]=(rows[row].get(col,0)+amplitude*z) % PRIME
    return states,rows,contact


def rank_observable(K,h,phase='real',open_chain=False,inhomogeneous=False,potential=False,one_monitor=False):
    states,H,contact=build(K,h,phase,open_chain,inhomogeneous,potential)
    D=len(states);noncontact=sorted(set(range(D))-contact);n=len(noncontact);ix={x:i for i,x in enumerate(noncontact)}
    A=[{ix[j]:v for j,v in H[x].items() if j in ix} for x in noncontact]
    initial=[{ix[j]:v for j,v in H[x].items() if j in ix} for x in contact]
    # Row observability: contact rows, followed by all words in H and n_0.
    # After projecting out contacts, the compressed n_0 is diagonal, so this
    # smaller closure is equivalent to adjoining the full contact basis.
    n0=[int(0 in states[x]) for x in noncontact]
    basis={};queue=deque();longest=0
    for row in initial:
        added=insert(row,basis)
        if added is not None:queue.append((added,1))
    initial_rank=len(basis)
    while queue and len(basis)<n:
        row,depth=queue.popleft();longest=max(longest,depth)
        product=defaultdict(int)
        for j,c in row.items():
            for k,v in A[j].items():product[k]=(product[k]+c*v) % PRIME
        candidates=[dict(product)]
        if one_monitor:candidates.append({j:v*n0[j] for j,v in row.items()})
        for candidate in candidates:
            added=insert(candidate,basis)
            if added is not None:queue.append((added,depth+1))
    rank=len(contact)+len(basis)
    return {'K':K,'holes':h,'phase':phase,'open_chain':open_chain,
            'inhomogeneous_hopping':inhomogeneous,'diagonal_potential':potential,
            'one_occupation_monitor':one_monitor,'dimension':D,'contact_dimension':len(contact),
            'noncontact_dimension':n,'initial_boundary_constraint_rank':initial_rank,
            'observable_rank_mod_prime':rank,'unobserved_dimension_mod_prime':D-rank,
            'maximum_processed_word_length':longest,
            'full_rank_certifies_characteristic_zero_observability':rank==D}


def gauge_sector_control(K,h):
    mask=(1<<K)-1
    bit=lambda b,i:(b>>(i%K))&1
    holes=lambda b:tuple(i for i in range(K) if bit(b,i)==bit(b,i-1))
    representatives={holes(b):b for b in range(1<<K) if bit(b,0)==0 and len(holes(b))==h}
    states,Hplus,_=build(K,h,'quarter');_,Hminus,_=build(K,h,'minus_quarter')
    assert set(representatives)==set(states)
    index={a:i for i,a in enumerate(states)}
    rows={1:[{} for _ in states],-1:[{} for _ in states]}
    for col,a in enumerate(states):
        b=representatives[a]
        for edge in range(K):
            target=b^(1<<edge)
            if len(holes(target))!=h:continue
            out=holes(target)
            assert len(set(a)-set(out))==1 and len(set(out)-set(a))==1
            forward=edge in a
            phase=IMAG if edge==0 else 1
            if not forward:phase=pow(phase,-1,PRIME)
            row=index[out]
            for eigenvalue in (1,-1):
                factor=eigenvalue if bit(target,0)==1 else 1
                rows[eigenvalue][row][col]=phase*factor % PRIME
    assert rows[1]==Hplus and rows[-1]==Hminus
    return {'K':K,'holes':h,'fiber_dimension':2,'each_T_sector_dimension':len(states),
            'T_plus_flux_quarter_T_minus_flux_three_quarters_exactly_identified':True}


def exact_real_dark(K):
    pairs=list(combinations(range(K),2));ix={a:i for i,a in enumerate(pairs)};D=len(pairs)
    H=s.zeros(D);S=s.zeros(D);contact=[]
    for col,a in enumerate(pairs):
        contact.append(int((a[1]-a[0]) in (1,K-1)))
        S[ix[tuple(sorted((x+1)%K for x in a))],col]=1
        for x in a:
            for step in (-1,1):
                y=(x+step)%K
                if y not in a:
                    b=tuple(sorted((set(a)-{x})|{y}));H[ix[b],col]+=1
    P=s.zeros(D);power=s.eye(D)
    for j in range(K):P+=(-1)**j*power/K;power=S*power
    G=s.diag(*contact);P=P*(s.eye(D)-G)
    assert P==P.T and P*P==P and H*P==s.zeros(D) and G*P==s.zeros(D)
    rank=K//2-2+int(K%4==0);assert s.trace(P)==rank
    return {'K':K,'exact_dark_projection_rank':rank,'annihilation_and_projector_identities':True}


if __name__=='__main__':
    started=time.monotonic();cases=[]
    for K in (4,6,8,10,12,14):
        for h in range(2,K+1,2):
            for phase in ('real','quarter','minus_quarter'):
                row=rank_observable(K,h,phase)
                if phase!='real' or h>=4:assert row['observable_rank_mod_prime']==row['dimension']
                else:assert row['unobserved_dimension_mod_prime']==K//2-2+int(K%4==0)
                cases.append(row)
        # Real phases, unequal edge magnitudes and a diagonal potential;
        # one measured site's occupation should suffice. Open chains need
        # no occupation monitor in this finite test family.
        for h in (2,4):
            for one_monitor,open_chain in ((True,False),(False,True)):
                row=rank_observable(K,h,'real',open_chain,True,True,one_monitor)
                assert row['observable_rank_mod_prime']==row['dimension'];cases.append(row)
        # The generic-flux argument also permits those inhomogeneities.
        row=rank_observable(K,2,'quarter',False,True,True,False)
        assert row['observable_rank_mod_prime']==row['dimension'];cases.append(row)
        print(json.dumps({'K':K,'completed_cases':len(cases)}),flush=True)
    output={'created_utc':datetime.now(timezone.utc).isoformat(),
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'prime':PRIME,'imaginary_unit_embedding':IMAG,
            'scope':'Full modular ranks are exact characteristic-zero certificates. General all-size claims require the separately written amplitude induction. Deficient rows are supported only where exact dark projectors are also constructed.',
            'cases':cases,
            'gauge_sector_controls':[gauge_sector_control(K,h) for K in (4,6,8) for h in range(2,K+1,2)],
            'exact_dark_controls':[exact_real_dark(K) for K in (4,6,8,10,12,14)],
            'runtime_seconds':time.monotonic()-started}
    (HERE/'COHERENT_RING_CONTACT_OBSERVABILITY_RESULTS.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({'finished':True,'cases':len(cases),'runtime_seconds':output['runtime_seconds']}),flush=True)
