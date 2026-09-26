#!/usr/bin/env python3
"""Bounded post-seal verification, without importing or rerunning author code."""
from pathlib import Path
from itertools import product,combinations
import hashlib
import json
import sys
import time
sys.dont_write_bytecode=True
import sympy as s
from z2_completion_check import model,occupation
from link_witness_check import DATA,hamiltonian_channels,record_cycle,field_loop,INDEX

HERE=Path(__file__).resolve().parent
AUTHOR=HERE.parent


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def authenticate():
    pre=HERE/'PRE_COMPARISON_SEAL.json'
    assert sha(pre)=='bb7539d6463e71fe402ee5738a40ecff09ba52ec4fc0879f2f271fbce981553e'
    old=json.loads(pre.read_text())
    for row in old['sources']+old['artifacts']:
        p=Path(row['path']);assert p.stat().st_size==row['bytes'] and sha(p)==row['sha256']
    seal=AUTHOR/'GAUGE_RECORD_AUTHOR_PRECOMPARISON_SEAL.json'
    assert sha(seal)=='41c3ccff2f341887b71c1ef5ab7d3055f6288eaea97095c89e577273ec4bc9bc'
    source=json.loads(seal.read_text())
    for row in source['artifacts']:
        p=Path(row['path']);assert p.stat().st_size==row['bytes'] and sha(p)==row['sha256']
    stems=[('GAUGE_RECORD_LOCAL_ALGEBRA','gauge_record_local_algebra_check.py'),
           ('GAUGE_RECORD_EXTREME_FLUX','gauge_record_extreme_flux_check.py'),
           ('GAUGE_COLLECTIVE_RECORD_CYCLE','gauge_collective_record_cycle_check.py')]
    for stem,script in stems:
        result=json.loads((AUTHOR/(stem+'_RESULTS.json')).read_text())
        receipt=json.loads((AUTHOR/(stem+'_RUN_RECEIPT.json')).read_text())
        assert result['script_sha256']==receipt['script_sha256']==sha(AUTHOR/script)
        assert receipt['returncode']==0
        assert (AUTHOR/(stem+'_RUN.stderr')).read_bytes()==b''
        if stem=='GAUGE_RECORD_EXTREME_FLUX':
            expected=dict(result)
            expected['cases']=[{k:v for k,v in row.items() if k not in {'final_charge','birth_history','final_negative_flux_edge_indices'}} for row in result['cases']]
            assert json.loads((AUTHOR/(stem+'_RUN.log')).read_text())==expected
        else:
            assert (AUTHOR/(stem+'_RUN.log')).read_bytes()==(AUTHOR/(stem+'_RESULTS.json')).read_bytes()
    return {'earlier_source_and_artifact_bindings_unchanged':len(old['sources'])+len(old['artifacts']),
            'author_artifact_bindings_authenticated':len(source['artifacts']),
            'all_three_success_receipts_and_stdout_relationships_authenticated':True}


def modular_rank_and_determinant(matrix,prime,iroot):
    assert (iroot*iroot+1)%prime==0
    def rational_mod(x):
        a,b=s.fraction(x)
        assert a.is_Integer and b.is_Integer and int(b)%prime!=0
        return int(a)*pow(int(b),-1,prime)%prime
    def field(x):
        re,im=x.as_real_imag()
        return (rational_mod(re)+iroot*rational_mod(im))%prime
    A=[[field(matrix[i,j]) for j in range(matrix.cols)] for i in range(matrix.rows)]
    rank=0;det=1
    for col in range(matrix.cols):
        pivot=next((i for i in range(rank,len(A)) if A[i][col]),None)
        if pivot is None:continue
        if pivot!=rank:A[pivot],A[rank]=A[rank],A[pivot];det=-det
        value=A[rank][col];det=det*value%prime
        inv=pow(value,-1,prime)
        A[rank]=[(x*inv)%prime for x in A[rank]]
        for i in range(rank+1,len(A)):
            a=A[i][col]
            if a:
                A[i]=[(x-a*y)%prime for x,y in zip(A[i],A[rank])]
        rank+=1
    return rank,det%prime


def nonzero_H0_control():
    _,L,_=model(range(4))
    ring=s.zeros(16)
    for z in range(16):ring[z^15,z]=1
    electric=s.diag(*[4-2*z.bit_count() for z in range(16)])
    H0=s.Rational(2,3)*ring+s.Rational(1,7)*electric
    for x in range(4):
        nx=s.diag(*[occupation(z)[x] for z in range(16)])
        assert H0*nx==nx*H0
    L-=s.I*(s.kronecker_product(s.eye(16),H0)-s.kronecker_product(H0.T,s.eye(16)))
    assert s.eye(16).vec().T*L==s.zeros(1,256)
    transient=[z for z in range(16) if not all(occupation(z))]
    inds=[r+16*c for c in transient for r in transient]
    K=L.extract(inds,inds)
    rank,det=modular_rank_and_determinant(K,65537,256)
    assert K.shape==(196,196) and rank==196 and det!=0
    # A nonzero determinant under a denominator-valid ring homomorphism from
    # Gaussian rationals proves the original Gaussian-rational determinant is
    # nonzero. This independently corroborates the author's exact rank.
    assert H0.extract([5,10],[5,10])==s.Matrix([[0,s.Rational(2,3)],[s.Rational(2,3),0]])
    return {'transient_dimension':196,'prime':65537,'image_of_i':256,
            'rank_mod_prime':rank,'determinant_mod_prime':det,
            'consequence':'Full rank 196 over Gaussian rationals; no stationary transient operator.',
            'H0_commutes_with_every_occupation_projector':True,
            'full_sector_H0':'(2/3) sigma_x; full occupation does not mean a stationary gauge density.'}


def certificates():
    data=json.loads((AUTHOR/'GAUGE_RECORD_EXTREME_FLUX_RESULTS.json').read_text())
    out=[]
    for row in data['cases']:
        N=row['N'];xyz=list(product(range(N),repeat=3));where={x:i for i,x in enumerate(xyz)}
        def shift(x,k,sign=1):
            y=list(x);y[k]=(y[k]+sign)%N;return tuple(y)
        edges=[(a,where[shift(x,k)]) for a,x in enumerate(xyz) for k in range(3)]
        lookup={e:(j,1) for j,e in enumerate(edges)}
        lookup.update({(y,x):(j,-1) for j,(x,y) in enumerate(edges)})
        negative=set(row['final_negative_flux_edge_indices'])
        assert len(negative)==row['negative_flux_count']==(N**3-2)//2
        q=[0]*(N**3);seen=set();history=[]
        for e in row['final_negative_flux_edge_indices']:
            x,y=edges[e];assert x not in seen and y not in seen
            assert q[x]==q[y]==0
            q[x]=-1;q[y]=1;seen.update((x,y));history.append([e,x,y])
        assert history==row['birth_history'] and q==row['final_charge']
        holes={i for i,a in enumerate(q) if not a}
        assert {xyz[i] for i in holes}=={(0,0,0),(1,1,1)}
        for h in holes:
            for axis in range(3):
                assert q[where[shift(xyz[h],axis)]]==1
                assert q[where[shift(xyz[h],axis,-1)]]==-1
        legal_hops=[];legal_births=[]
        for e,(x,y) in enumerate(edges):
            E2=1-2*int(e in negative)
            if not q[x] and not q[y]:legal_births.append(e)
            for src,dst,sign in [(x,y,1),(y,x,-1)]:
                if q[src] and not q[dst] and E2==sign*q[src]:legal_hops.append((e,src,dst))
        assert not legal_hops and not legal_births
        faces=0;enabled=0
        for x in xyz:
            for i,j in combinations(range(3),2):
                verts=[where[v] for v in (x,shift(x,i),shift(shift(x,i),j),shift(x,j))]
                channels=[lookup[(verts[k],verts[(k+1)%4])] for k in range(4)]
                for orientation in (-1,1):
                    if all(1-2*int(e in negative)==-orientation*sgn for e,sgn in channels):enabled+=1
                faces+=1
        assert faces==3*N**3 and enabled==0
        out.append({'N':N,'birth_history_entries_verified':len(history),
                    'matter_charge_entries_verified':len(q),'faces_checked':faces,
                    'hops':0,'births':0,'field_plaquette_channels':0})
    first=data['cases'][0]
    assert first['final_negative_flux_edge_indices']==DATA['negative_flux_edge_indices']
    assert first['final_charge']==DATA['matter_charges']
    assert sha(AUTHOR/'GAUGE_RECORD_EXTREME_FLUX_RESULTS.json')==DATA['source_identity_sha256']
    return out


def cycle_count_and_nonannihilation_control():
    state=(tuple(DATA['matter_charges']),sum(1<<e for e in DATA['negative_flux_edge_indices']))
    channels=hamiltonian_channels(state)
    cycles=[row for row in channels if row[1]['kind']=='record_cycle']
    assert len(cycles)==68
    assert all(row[1]['kind']=='record_cycle' for row in channels)
    control=json.loads((HERE/'LINK_WITNESS_RESULTS.json').read_text())
    example=control['one_enabled_hexagon_example']
    verts=tuple(INDEX[tuple(x)] for x in example['cycle'])
    output=field_loop(state,verts,example['orientation'])
    assert output is not None and output!=state and output[0]==state[0]
    assert output[1].bit_count()==state[1].bit_count()
    return {'enabled_oriented_record_cycle_channels':len(cycles),
            'independent_H3_coefficient_reused':control['coherent_matrix_elements_at_unit_coefficients'],
            'F1_nonannihilation_witness':example,
            'contractible_loop_output_differs_from_initial':True,
            'fixed_charge_and_F_preserved':True,
            'finding':'The earlier generator preserves the trapped subspace, but a general allowed diagonal energy or longer contractible loop need not annihilate the individual vector.'}


if __name__=='__main__':
    started=time.monotonic()
    result={'boundary':'Post-seal author comparison; no author code imported or rerun.',
            'authentication':authenticate(),'nonzero_H0':nonzero_H0_control(),
            'all_three_certificate_reconstructions':certificates(),
            'cycle_and_scope_control':cycle_count_and_nonannihilation_control(),
            'runtime_seconds':time.monotonic()-started}
    (HERE/'COMPARISON_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
