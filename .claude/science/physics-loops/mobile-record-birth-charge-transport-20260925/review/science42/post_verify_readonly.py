#!/usr/bin/env python3
"""POST42 read-only source and complete stored-data comparison.
No author/PRE scientific program is imported or executed. No filesystem writes.
"""
from collections import Counter, defaultdict
from datetime import datetime, timezone
from fractions import Fraction as Q
from itertools import combinations, product
from pathlib import Path
import hashlib
import json

BASE=Path(__file__).resolve().parent


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def read_json(p):
    return json.loads(p.read_text())


def stats(values):
    mean=Q(sum(values),len(values))
    return mean,Q(sum(x*x for x in values),len(values))-mean*mean


def coordinates_and_edges(L):
    vertices=tuple(product(range(L),repeat=3))
    A={i for i,x in enumerate(vertices) if sum(x)%2==0}
    # Independent unordered-pair distance construction. No author geometry call.
    edges=[]
    for u,v in combinations(range(len(vertices)),2):
        distance=sum(min(abs(x-y),L-abs(x-y)) for x,y in zip(vertices[u],vertices[v]))
        if distance==1:
            edges.append((u,v) if u in A else (v,u))
    edges=tuple(sorted(edges))
    neighbors={a:tuple(b for aa,b in edges if aa==a) for a in sorted(A)}
    return vertices,A,edges,neighbors


def short_displacement(vertices,a,b,L):
    raw=[y-x for x,y in zip(vertices[a],vertices[b])]
    if L>=4:
        raw=[v-L if v>L//2 else v+L if v<-L//2 else v for v in raw]
    assert sum(abs(v) for v in raw)==1
    return tuple(raw)


def sparse(items):
    return tuple(sorted((key,value) for key,value in items if value))


def main():
    preseal=read_json(BASE/'PRE_SEAL.json')
    assert sha(BASE/'PRE_SEAL.json')=='61b5a0edaffee445ba80cfd7eb7e25cb60dea3e6aede4b449df2fc2e3dbc7cca'
    for row in preseal['members']:
        assert sha(BASE/row['path'])==row['sha256']
    assert len(preseal['members'])==33
    pins=read_json(BASE/'POST_SOURCE_PINS.json')
    for row in pins['sources']:
        assert sha(Path(row['origin']))==row['sha256']
        assert sha(BASE/row['snapshot'])==row['sha256']
        assert (BASE/row['snapshot']).stat().st_size==row['bytes']
    assert len(pins['sources'])==11
    root=BASE/'post_sources'
    seal=read_json(root/'AUTHOR_SEAL.json')
    assert len(seal['members'])==10
    for row in seal['members']:
        assert sha(root/row['path'])==row['sha256']
    author_sources=read_json(root/'SOURCE_PINS.json')
    pre_sources={row['origin']:row for row in read_json(BASE/'SOURCE_PINS.json')['sources']}
    for row in author_sources['sources']:
        assert row['sha256']==pre_sources[row['origin']]['sha256']
        assert sha(Path(row['origin']))==row['sha256']
    assert len(author_sources['sources'])==3
    assert author_sources['independent_40_41_PRE_read'] is False
    assert sha(root/'charge_cluster_controls.py')==sha(root/'attempt01/charge_cluster_controls.py')
    assert sha(root/'attempt01/RESULT.json')==sha(root/'attempt01/stdout.log')
    assert (root/'attempt01/stderr.log').read_bytes()==b''
    result=read_json(root/'attempt01/RESULT.json')
    execution=read_json(root/'attempt01/EXECUTION.json')
    root_receipt=read_json(root/'ROOT_READ_RECEIPT.json')
    assert execution['exit_code']==0 and execution['stderr_bytes']==0
    assert result['source_sha256']==execution['source_sha256']==sha(root/'charge_cluster_controls.py')
    assert root_receipt['result_sha256']==sha(root/'attempt01/RESULT.json')
    assert root_receipt['all_raw_rows_manually_read'] is False
    assert 'end time' in root_receipt['receipt_timestamp_qualification']
    assert result['all_assertions_passed'] is True
    assert result['primitive_columns']==['L','a','b','c','sigma','delta_q_sparse','delta_E_sparse']
    assert result['row_columns']==['L','a','b','test','mean','variance','outgoing_mean','outgoing_variance','internal_dipole','charge_distribution_multiplicities']
    geometries={L:coordinates_and_edges(L) for L in (2,4,6)}
    edge_lookup={L:{edge:i for i,edge in enumerate(g[2])} for L,g in geometries.items()}
    branches=defaultdict(list)
    all_branches={}
    expected_keys=set()
    for L,(vertices,A,edges,neighbors) in geometries.items():
        for a,b in edges:
            for c in neighbors[a]:
                if c!=b:
                    for sigma in (-1,1):
                        expected_keys.add((L,a,b,c,sigma))
    for row in result['primitive_rows']:
        L,a,b,c,sigma,dq_raw,dE_raw=row
        key=(L,a,b,c,sigma)
        assert key in expected_keys and key not in all_branches
        vertices,A,edges,neighbors=geometries[L]
        dq=tuple(map(tuple,dq_raw)); dE=tuple(map(tuple,dE_raw))
        assert dq==sparse(((a,sigma-1),(b,-sigma),(c,1)))
        assert dE==sparse(((edge_lookup[L][(a,b)],sigma),(edge_lookup[L][(a,c)],-1)))
        div=Counter()
        for ei,value in dE:
            x,y=edges[ei]
            div[x]+=value; div[y]-=value
        assert sparse(div.items())==dq
        charges=dict(dq)
        assert charges.get(a,0)+charges.get(b,0)==-1
        assert sum(charges.get(x,0) for x in neighbors[a] if x!=b)==1
        assert sum(charges.values())==0
        final=[int(x in A)+charges.get(x,0) for x in range(len(vertices))]
        assert all(v in (-1,0,1) for v in final)
        assert sum(abs(v) for v in final)==len(A)+2
        all_branches[key]=(dq,dE)
        branches[(L,a,b)].append((sigma,c,charges))
    assert set(all_branches)==expected_keys
    swaps=0
    for (L,a,b,c,sigma),out in all_branches.items():
        if sigma==-1:
            assert out==all_branches[(L,a,c,b,-1)]
            swaps+=1
    assert len(all_branches)==8448 and swaps==4224 and len(branches)==852
    for (L,a,b),rows in branches.items():
        assert len(rows)==2*(len(geometries[L][3][a])-1)
        assert len({tuple(sorted(dq.items())) for _,_,dq in rows})==len(rows)
    tests={}
    for L,(vertices,A,edges,neighbors) in geometries.items():
        phase=tuple(((1,0),(0,-1),(-1,0),(0,1))[(sum(x) if L==4 else 2*x[0])%4] for x in vertices)
        tests[L]={
            'constant':tuple(1 for x in vertices),
            'x':tuple(x[0] for x in vertices),
            'polynomial':tuple(x[0]**2+2*x[1]-x[2] for x in vertices),
            'Fourier_real':tuple(x[0] for x in phase),
            'Fourier_imag':tuple(x[1] for x in phase)}
    groups=defaultdict(list)
    row_map={}
    negative_operator_checks=0
    resolved_moment_checks=0
    for row in result['rows']:
        L,a,b,name,mu,var,muout,varout,dip,law=row
        key=(L,a,b,name)
        assert key not in row_map
        f=tests[L][name]
        branch=branches[(L,a,b)]
        values=[sum(f[x]*v for x,v in dq.items()) for _,_,dq in branch]
        actual=stats(values)
        assert actual==(Q(mu),Q(var))
        assert sorted(Counter(values).items())==[tuple(x) for x in law]
        neighbors=geometries[L][3]
        outgoing=[f[c] for c in neighbors[a] if c!=b]
        outmean,outvar=stats(outgoing)
        assert (outmean,outvar)==(Q(muout),Q(varout))
        assert dip==f[a]-f[b]
        assert actual==(outmean-f[a],outvar+dip*dip)
        assert sum(multiplicity for _,multiplicity in law)==len(branch)
        for sigma in (-1,1):
            vals=[sum(f[x]*v for x,v in dq.items()) for s,_,dq in branch if s==sigma]
            assert stats(vals)==(outmean-f[a]+sigma*dip,outvar)
            resolved_moment_checks+=1
        for sigma,c,dq in branch:
            negative=f[a]*dq.get(a,0)+f[b]*dq.get(b,0)
            assert negative==-f[a]+sigma*dip
            assert (negative+f[a])**2==dip*dip
            negative_operator_checks+=1
        assert sum(s*f[c] for s,c,dq in branch)==0
        row_map[key]=row
        groups[(L,name)].append(row)
    expected_moment_keys={(L,a,b,name) for L,a,b in branches for name in tests[L]}
    assert set(row_map)==expected_moment_keys and len(row_map)==4260
    grouped=[]
    for (L,name),rows in sorted(groups.items()):
        means=[Q(row[4]) for row in rows]
        variances=[Q(row[5]) for row in rows]
        grouped.append(dict(L=L,test=name,rows=len(rows),
                            mean_range=[str(min(means)),str(max(means))],
                            variance_range=[str(min(variances)),str(max(variances))],
                            distribution_support_sizes=sorted({len(row[9]) for row in rows})))
    root_groups={(row['L'],row['test']):row for row in root_receipt['grouped_summaries']}
    assert len(root_groups)==15
    for row in grouped:
        assert row==root_groups[(row['L'],row['test'])]
    geometry_reports=[]
    structure_reports=[]
    for L,(vertices,A,edges,neighbors) in geometries.items():
        second_values=[]
        tensor=[[0]*3 for _ in range(3)]
        fixed_orientation=defaultdict(list)
        for a,b in edges:
            real=row_map[(L,a,b,'Fourier_real')]
            imag=row_map[(L,a,b,'Fourier_imag')]
            S=Q(real[5])+Q(real[4])**2+Q(imag[5])+Q(imag[4])**2
            fR,fI=tests[L]['Fourier_real'],tests[L]['Fourier_imag']
            direct=Q(sum((fR[c]-fR[a])**2+(fI[c]-fI[a])**2 for c in neighbors[a] if c!=b),len(neighbors[a])-1)
            direct+=(fR[a]-fR[b])**2+(fI[a]-fI[b])**2
            assert S==direct
            second_values.append(S)
            d=short_displacement(vertices,a,b,L)
            if L>=4:
                expected=Q(4) if L==4 else Q(4)-Q(4,5)-Q(8,5)*(1-2*d[0]**2)
                assert S==expected
                fixed_orientation[d].append(S)
                for sigma,c,dq in branches[(L,a,b)]:
                    r=short_displacement(vertices,a,c,L)
                    dipole=tuple(r[i]-sigma*d[i] for i in range(3))
                    for i in range(3):
                        for j in range(3):
                            tensor[i][j]+=dipole[i]*dipole[j]
        denominator=2*len(edges)*(len(neighbors[next(iter(A))])-1)
        average=sum(second_values,Q(0))/len(edges)
        tensor_output=None if L==2 else [[str(Q(x,denominator)) for x in line] for line in tensor]
        if L>=4:
            assert tensor_output==[['2/3' if i==j else '0' for j in range(3)] for i in range(3)]
        expected_summary=dict(L=L,n_A=len(A),degree=len(neighbors[next(iter(A))]),edge_marks=len(edges),
                              resolved_rate_per_edge_sign_in_kappa=len(neighbors[next(iter(A))])-1,
                              coherent_rate_per_edge_in_kappa=2*(len(neighbors[next(iter(A))])-1),
                              total_first_birth_rate_in_kappa=denominator,
                              orientation_averaged_dipole_second_moment=tensor_output,
                              selected_wavevector_structure_factor=str(average))
        assert expected_summary==next(row for row in result['summaries'] if row['L']==L)
        geometry_reports.append(expected_summary)
        for d,values in sorted(fixed_orientation.items()):
            assert min(values)==max(values)
            structure_reports.append(dict(L=L,d=d,edge_count=len(values),exact_second_moment=str(values[0])))
    expected_counts=dict(primitive_paths=8448,negative_mark_ambiguity_controls=4224,edge_marks=852,
                         charge_moment_controls=4260,complex_structure_factor_controls=852)
    assert result['counts']==expected_counts
    assert root_receipt['all_primitive_rows_rechecked']==8448
    assert root_receipt['all_charge_distribution_rows_rechecked']==4260
    pre=read_json(BASE/'primitive_attempt01/stdout.json')
    pregraph={row['graph']:row for row in pre['graphs']}
    prewave={tuple(row['mode']):row for row in pre['fourier']}
    comparisons=[]
    for L,key in ((2,'cubic_L2'),(4,'cubic_L4')):
        author=next(row for row in geometry_reports if row['L']==L)
        independent=pregraph[key]
        assert author['total_first_birth_rate_in_kappa']==independent['actual_loss_over_kappa']
        comparisons.append(dict(quantity='total_loss_over_kappa',L=L,value=author['total_first_birth_rate_in_kappa'],PRE_match=True))
    for L,mode in ((4,(1,1,1)),(6,(2,0,0))):
        author=next(row for row in geometry_reports if row['L']==L)
        # L6 comparison is the same dimensionless wavevector in the PRE L4
        # dataset; it is a statistic/formula correspondence, not an L6 PRE run.
        value=prewave[mode]['statistics']['0']['second']
        assert Q(author['selected_wavevector_structure_factor'])==Q(value)
        comparisons.append(dict(quantity='orientation_averaged_structure_factor',author_L=L,
                                PRE_L=4,PRE_mode=mode,value=value,PRE_match=True))
    chronology=dict(author_seal_utc=seal['at'],root_read_utc=root_receipt['at'],
                    original_receipt_field=execution['started_before_utc'],
                    original_receipt_field_means='after process return; not start',
                    author_elapsed_external_seconds=execution['elapsed_seconds'],
                    author_elapsed_internal_seconds=result['elapsed_seconds'],
                    PRE_sealed_utc=preseal['sealed_utc'])
    assert seal['at']<preseal['sealed_utc']
    print(json.dumps(dict(status='all released-source stored-data correspondence checks passed',
                          checked_utc=datetime.now(timezone.utc).isoformat(),
                          mode='genuinely read only; no author/control imports or execution',
                          PRE_members_unchanged=33,released_origins_verified=11,
                          unchanged_scientific_parent_origins=3,
                          counts=expected_counts,all_raw_primitive_and_moment_rows_mechanically_checked=True,
                          raw_rows_claimed_manually_read=False,negative_operator_checks=negative_operator_checks,
                          resolved_sign_moment_comparisons=resolved_moment_checks,
                          graph_summaries=geometry_reports,grouped_moment_rows=grouped,
                          fixed_mark_structure_factor_groups=structure_reports,
                          PRE_comparisons=comparisons,chronology=chronology),indent=2,sort_keys=True))


if __name__=='__main__':
    main()
