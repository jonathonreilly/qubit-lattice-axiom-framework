#!/usr/bin/env python3
"""Exact finite-field observability certificate with occupation-only monitoring.

Rank is computed over a fixed prime. Full modular rank is a certificate of
full rational rank, since all generating operations use integer matrices.
Deficient modular rank is reported as inconclusive unless independently
verified over characteristic zero. No large-size conclusion is drawn.
"""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter, deque
import hashlib,itertools,json,sys,math
sys.dont_write_bytecode=True
from gauge_configuration_connectivity_screen import inventory

HERE=Path(__file__).resolve().parent
PRIME=1000003
assert PRIME>1 and all(PRIME%a for a in range(2,math.isqrt(PRIME)+1))


def hamiltonian(charge,edges,faces,hops,fields,kappa,field,circulation):
    H={u:Counter({v:kappa for v in hops[u]}) for u in charge}
    for u,qs in charge.items():
        for v in fields[u]: H[u][v]+=field
        for face in faces:
            flip=sum(1<<e for e,_ in face)
            for sense in (1,-1):
                oriented=face if sense==1 else [(e,-s) for e,s in reversed(face)]
                sites=[edges[e][0 if s==1 else 1] for e,s in oriented]
                if not all(qs[a]!=0 for a in sites):continue
                if not all(1-2*((u>>e)&1)==s*qs[a] for (e,s),a in zip(oriented,sites)):continue
                v=u^flip; target=list(qs)
                for i,a in enumerate(sites):target[sites[(i+1)%4]]=qs[a]
                assert charge[v]==tuple(target)
                H[u][v]+=circulation
        H[u]=Counter({v:c for v,c in H[u].items() if c})
    for u,row in H.items():
        for v,c in row.items(): assert H[v][u]==c
    return H


def close_space(charge,births,H,records):
    states=[u for u,q in charge.items() if sum(x!=0 for x in q)==records]
    pattern={u:sum(1<<a for a,q in enumerate(charge[u]) if q==0) for u in states}
    groups={}
    for u in states:groups.setdefault(pattern[u],[]).append(u)
    echelon={g:{} for g in groups}; queue=deque(); ranks=Counter(); attempts=0
    def insert(g,vector):
        nonlocal attempts
        attempts+=1
        v={u:c%PRIME for u,c in vector.items() if c%PRIME}
        while v:
            p=min(v); c=v[p]
            if p not in echelon[g]:
                scale=pow(c,-1,PRIME);v={u:a*scale%PRIME for u,a in v.items()}
                echelon[g][p]=v;queue.append((g,v));ranks[g]+=1
                return True
            row=echelon[g][p]
            for u,a in row.items():
                v[u]=(v.get(u,0)-c*a)%PRIME
                if not v[u]:del v[u]
        return False
    contact_states=[u for u in states if births[u]]
    for u in contact_states:insert(pattern[u],{u:1})
    processed=0
    while queue:
        _,v=queue.popleft(); processed+=1
        projected={}
        for u,c in v.items():
            for w,a in H[u].items():
                g=pattern[w];z=projected.setdefault(g,Counter());z[w]+=c*a
        for g,z in projected.items():insert(g,z)
    total=sum(ranks.values())
    return dict(records=records,sector_dimension=len(states),occupation_blocks=len(groups),
                maximum_occupation_block_dimension=max(map(len,groups.values())),
                initial_contact_rank=len(contact_states),generated_rank_mod_prime=total,
                full_rational_rank_certified=total==len(states),
                unresolved_modular_deficit=len(states)-total,
                insertions_attempted=attempts,independent_vectors_processed=processed,
                block_deficits=[dict(vacancy_mask=g,dimension=len(group),rank=ranks[g])
                                for g,group in groups.items() if ranks[g]<len(group)])


def check(shape):
    vertices,edges,faces,charge,births,hops,fields,_=inventory(shape)
    V=len(vertices);rows=[]
    for name,k,f,g in [('hop_only',1,0,0),('hop_field',1,1,0),
                       ('hop_field_cycle',1,1,1),('hop_field_cycle_unequal',2,3,5)]:
        H=hamiltonian(charge,edges,faces,hops,fields,k,f,g)
        sectors=[close_space(charge,births,H,n) for n in range(0,V,2)]
        rows.append(dict(model=name,coefficients=dict(kappa=k,field=f,cycle=g),sectors=sectors,
                         every_nonfull_sector_observable=all(x['full_rational_rank_certified'] for x in sectors)))
    return dict(shape=shape,physical_basis_size=len(charge),models=rows)


if __name__=='__main__':
    result=dict(created_utc=datetime.now(timezone.utc).isoformat(),
                script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                inventory_script_sha256=hashlib.sha256((HERE/'gauge_configuration_connectivity_screen.py').read_bytes()).hexdigest(),
                prime=PRIME,characteristic_zero_bound='Full rank modulo the prime implies full rational rank; deficits alone do not prove dark states.',
                monitoring='All local occupation projectors only; no electric-field measurement.',
                cases=[check((2,2,2)),check((2,2,3))])
    encoded=json.dumps(result,indent=2)+'\n';(HERE/'GAUGE_OCCUPATION_OBSERVABILITY_RESULTS.json').write_text(encoded);print(encoded,end='')
