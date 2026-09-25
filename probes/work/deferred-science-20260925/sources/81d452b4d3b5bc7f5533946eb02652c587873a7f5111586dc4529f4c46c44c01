#!/usr/bin/env python3
"""Own released-source comparison; no author Python is imported or executed.

Consumes every author quotient entry, full cube entry and local certificate
row. New local counts use direct set/Gram enumeration; their POST provenance
is distinct from the already sealed blind PRE controls.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations,product
from pathlib import Path
import hashlib,json,time

HERE=Path(__file__).resolve().parent;AUTHOR=HERE/'post_sources/author'
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def read(path):return json.loads(path.read_text())
def rational(x):return Fraction(x['numerator'],x['denominator'])
def fp(x):return dict(numerator=x.numerator,denominator=x.denominator)


def quotient_compare(author,pre,primitive):
    own={r['L']:r for r in pre['rows']};reports=[]
    for row in author['quotients']:
        L=row['side'];prior=own[L]
        labels=list(map(tuple,prior['orbit_labels']))
        coarse_label=lambda d:tuple(sorted(min(x,L-x) for x in d))
        groups=[labels.index(coarse_label(d)) for d in row['canonical_displacements']]
        sizes=[0]*len(labels)
        for i,w in enumerate(row['orbit_weights']):sizes[groups[i]]+=w
        assert sizes==prior['orbit_sizes']
        matrix=[dict(r) for r in row['delta_Q_rows']]
        assert len(matrix)==row['translation_orbits']==len(groups)
        ratios=[];v=row['positive_integer_test_vector'];shift=row['nonnegative_shift']
        assert all(type(x) is int and x>0 for x in v)
        for i,entries in enumerate(matrix):
            assert len(entries)==len(row['delta_Q_rows'][i])
            out=[0]*len(labels)
            for j,coefficient in entries.items():
                assert type(coefficient) is int
                assert i==j or coefficient>=0
                assert row['orbit_weights'][i]*coefficient==row['orbit_weights'][j]*matrix[j].get(i,0)
                out[groups[j]]+=coefficient
            assert out==[2*x for x in prior['orbit_quotient_offset_from_Q0'][groups[i]]]
            assert entries.get(i,0)+shift>=0
            ratios.append(Fraction(sum(a*v[j] for j,a in entries.items()),v[i]))
        low,high=min(ratios),max(ratios)
        assert low==rational(row['exact_delta_Q_Perron_interval']['lower'])
        assert high==rational(row['exact_delta_Q_Perron_interval']['upper'])
        assert -high/4==rational(row['proposed_ground_gap_g2_tau_interval']['lower'])
        assert -low/4==rational(row['proposed_ground_gap_g2_tau_interval']['upper'])
        prelow=Fraction(prior['exact_Perron_increment_lower'])
        prehigh=Fraction(prior['exact_Perron_increment_upper'])
        assert max(low/2,prelow)<=min(high/2,prehigh)
        assert row['vacuum_flat_H4']==-2*prior['magnetic_Q0']
        assert row['full_one_minus_matter_dimension']==prior['physical_one_pair_matter_dimension']
        assert row['occupancy_pair_dimension']==prior['occupation_dimension']
        reports.append(dict(L=L,author_translation_rows=len(matrix),PRE_cubic_rows=len(labels),
            exact_author_entries=sum(map(len,matrix)),all_rows_exactly_coarsen_to_twice_PRE=True,
            author_exact_increment_interval=[str(low),str(high)],
            author_bounds_equal_twice_PRE_bounds=(low==2*prelow and high==2*prehigh),
            gap_interval=[str(-high/4),str(-low/4)],
            row_sum_interval=[min(map(lambda r:sum(r.values()),matrix)),max(map(lambda r:sum(r.values()),matrix))]))
    cube=author['full_colored_cube'];owncube=next(r for r in primitive['rows'] if r['L']==2)
    vertices=list(product(range(2),repeat=3));AA=[v for v in vertices if sum(v)%2==0]
    BB=[v for v in vertices if sum(v)%2==1]
    root_basis=[(J,m) for J in combinations(BB,2) for m in sorted(AA+list(J))]
    independent_basis=[(tuple(map(tuple,r['occupied_B'])),tuple(r['minus'])) for r in owncube['rows']]
    perm=[independent_basis.index(word) for word in root_basis]
    full=cube['full_positive_Q'];prior=owncube['full_colored_matrix']
    assert len(full)==36 and all(len(row)==36 for row in full)
    for i,row in enumerate(full):
        for j,value in enumerate(row):assert value==2*prior[perm[i]][perm[j]]
    # The occupation matrix is compared to independently stored colored-row aggregates.
    Bpairs=list(combinations(BB,2));qocc=cube['occupancy_positive_Q']
    for i,J in enumerate(Bpairs):
        source=next(r for r in owncube['rows'] if tuple(map(tuple,r['occupied_B']))==J)
        expected={tuple(map(tuple,e['occupied_B'])):e['value'] for e in source['complete_occupation_row']}
        assert qocc[i]==[2*expected.get(K,0) for K in Bpairs]
    assert cube['vacuum_flat_H4']==-108 and cube['exact_one_pair_flat_H4_bottom']==-98
    assert cube['exact_flat_H4_ground_difference']==10
    return dict(quotients=reports,full_cube_integer_entries=36*36,
        full_cube_exact_after_basis_permutation_and_factor_two=True,
        cube_occupation_entries=36,exact_cube_gap='5/2')


UNITS=tuple(v for v in product((-1,0,1),repeat=3) if sum(map(abs,v))==1)
TWO=tuple(v for v in product(range(-2,3),repeat=3) if sum(map(abs,v))==2)
def plus(a,b,L=None):
    return tuple((x+y)%L if L else x+y for x,y in zip(a,b))
@lru_cache(None)
def neighbor_set(x,L=None):return frozenset(plus(x,d,L) for d in UNITS)
@lru_cache(None)
def active_pairs(b,L=None):
    # Explicit distance-two offsets, rather than the author's three-hop construction.
    return frozenset(tuple(sorted((a,plus(a,d,L)))) for a in neighbor_set(b,L) for d in TWO)
@lru_cache(None)
def kernel(a,c,L=None):
    aa,cc=neighbor_set(a,L),neighbor_set(c,L)
    return {D:int(D[0] in aa and D[1] in cc)+int(D[1] in aa and D[0] in cc)
            for D in combinations(sorted(aa|cc),2)
            if (D[0] in aa and D[1] in cc) or (D[1] in aa and D[0] in cc)}


def gram_delta(k,X):
    X=frozenset(X);row=Counter({tuple(sorted(X)):-2*sum(m*m for m in k.values())})
    for D,m in k.items():
        if X.intersection(D):continue
        intermediate=X.union(D)
        for remaining in combinations(sorted(intermediate),len(X)):
            returning=tuple(sorted(intermediate.difference(remaining)))
            if returning in k:row[remaining]+=2*m*k[returning]
    return row


def polynomial(z,r,a,c,t):
    # Count ordered outward assignments and their four indicator sums.
    na,nc,ni=z-a,z-c,r-t
    sums=(na*nc-ni,ni*(nc-1),ni*(na-1),ni*(ni-1))
    return 2*(sums[0]*((a+1)*(c+1)-t)+a*sums[1]+c*sums[2]+sums[3]-(z*z+r*r-2*r))


def parameters(a,c,X,L=None):
    aa,cc=neighbor_set(a,L),neighbor_set(c,L);X=set(X)
    return len(aa&cc),len(aa&X),len(cc&X),len(aa&cc&X)


def local_row(displacement):
    origin=(0,0,0);X=(origin,tuple(displacement))
    left,right=active_pairs(X[0]),active_pairs(X[1]);pairs=left|right
    full=Counter()
    for a,c in pairs:
        value=gram_delta(kernel(a,c),X)
        full.update(value)
        r,sa,sc,t=parameters(a,c,X)
        assert sum(value.values())==polynomial(6,r,sa,sc,t)
    full={k:v for k,v in full.items() if v}
    distance=max(min(sum(abs(x-y) for x,y in zip(v,b)) for b in X)
                 for a,c in pairs for v in neighbor_set(a)|neighbor_set(c))
    return dict(displacement=list(displacement),active_pairs=len(pairs),common_active_pairs=len(left&right),
        diagonal=full[tuple(sorted(X))],row_sum=sum(full.values()),nonzero_targets=len(full),
        maximum_active_vertex_distance_from_nearer_input=distance)


def local_compare(local,poly):
    origin=(0,0,0);singles=Counter()
    for a,c in active_pairs(origin):
        r,sa,sc,t=parameters(a,c,(origin,))
        value=sum(gram_delta(kernel(a,c),(origin,)).values())
        assert value==polynomial(6,r,sa,sc,t)
        singles[(r,min(sa,sc),max(sa,sc),t,value)]+=1
    expected=Counter({(r['r'],min(r['sa'],r['sc']),max(r['sa'],r['sc']),r['t'],r['row_contribution']):r['count']
                     for r in poly['single_occupied_B_contributions']})
    assert singles==expected
    single_total=sum(k[-1]*count for k,count in singles.items());assert single_total==6048
    near=[local_row(tuple(r['displacement'])) for r in local['near_rows']]
    far=[local_row(tuple(r['displacement'])) for r in local['far_controls']]
    assert near==local['near_rows'] and far==local['far_controls']
    groups=Counter(tuple(sorted(map(abs,r['displacement']))) for r in near)
    assert sum(groups.values())==84 and len(groups)==6
    interaction_rows=[]
    for r in poly['two_occupied_B_interactions']:
        X=(origin,tuple(r['displacement']));common=active_pairs(X[0])&active_pairs(X[1]);counts=Counter()
        for a,c in common:
            joint=sum(gram_delta(kernel(a,c),X).values())
            single=sum(sum(gram_delta(kernel(a,c),(b,)).values()) for b in X)
            overlap,sa,sc,t=parameters(a,c,X)
            counts[(overlap,min(sa,sc),max(sa,sc),t,joint-single)]+=1
        expected=Counter({(x['r'],x['s_min'],x['s_max'],x['t'],x['interaction_per_pair']):x['pairs']
                         for x in r['interaction_counts']})
        assert counts==expected and len(common)==r['common_active_pairs']
        correction=sum(k[-1]*count for k,count in counts.items())
        assert correction==r['interaction_row_correction']
        assert 2*single_total+correction==r['full_row_sum']
        interaction_rows.append(dict(displacement=r['displacement'],complete_counts=[
            dict(r=k[0],s_min=k[1],s_max=k[2],t=k[3],correction_per_pair=k[4],count=n)
            for k,n in sorted(counts.items())],correction=correction,total=2*single_total+correction))
    synthetic=[]
    for z,r in product((3,6),(1,2)):
        aa=set(range(z));cc=set(range(r))|set(range(z,2*z-r))
        k={D:int(D[0] in aa and D[1] in cc)+int(D[1] in aa and D[0] in cc)
           for D in combinations(sorted(aa|cc),2)
           if (D[0] in aa and D[1] in cc) or (D[1] in aa and D[0] in cc)}
        for X in combinations(sorted(aa|cc|{-1,-2}),2):
            occupied=set(X);a=len(aa&occupied);c=len(cc&occupied);t=len(aa&cc&occupied)
            direct=sum(gram_delta(k,X).values());predicted=polynomial(z,r,a,c,t)
            assert direct==predicted
            synthetic.append(dict(z=z,r=r,occupied=list(X),sa=a,sc=c,t=t,value=direct))
    unique=sorted(set((r['z'],r['r'],r['sa'],r['sc'],r['t'],r['value']) for r in synthetic))
    assert list(map(list,unique))==poly['synthetic']['distinct_parameter_rows']
    assert len(synthetic)==poly['synthetic']['exhaustive_input_pairs']==180
    low=min(r['row_sum'] for r in near+far);high=max(r['row_sum'] for r in near+far)
    assert (low,high)==(local['min_delta_Q_row_sum'],local['max_delta_Q_row_sum'])==(11512,12248)
    # Minimum-period boundary control, all 499 nonzero even-parity B displacements.
    # Only scalar row sums are needed, so the already checked indicator polynomial
    # is used here. The proof of the all-L assertion remains the local lifting proof.
    representatives={tuple(sorted(map(abs,r['displacement']))):r['row_sum'] for r in near}
    periodic=[]
    L=10
    for d in product(range(L),repeat=3):
        if not any(d) or sum(d)%2:continue
        X=(origin,d);pairs=active_pairs(origin,L)|active_pairs(d,L)
        value=sum(polynomial(6,*parameters(a,c,X,L)) for a,c in pairs)
        label=tuple(sorted(min(x,L-x) for x in d))
        expected=representatives[label] if sum(label)<=4 else 2*single_total
        assert value==expected
        periodic.append(dict(displacement=d,cubic_label=label,active_pairs=len(pairs),row_sum=value))
    assert len(periodic)==499
    return dict(single_site_exact_inventory=[dict(r=k[0],sa=k[1],sc=k[2],t=k[3],value=k[4],count=n)
        for k,n in sorted(singles.items())],single_site_total=single_total,
        complete_near_rows=near,complete_far_rows=far,complete_interaction_rows=interaction_rows,
        complete_synthetic_cases=synthetic,L10_all_displacements=periodic,
        exact_row_sum_interval=[low,high],static_gap_interval=[str(Fraction(-high,4)),str(Fraction(-low,4))],
        provenance='New after-release POST control; not part of blind PRE')


def bindings():
    pins=read(HERE/'POST_SOURCE_PINS.json');checked=[]
    for source in pins['sources']:
        p=HERE/source['frozen_path'];assert sha(p)==source['sha256']
        if source.get('role')!='Procedure only':assert sha(Path(source['origin']))==source['sha256']
        checked.append(dict(path=source['frozen_path'],sha256=sha(p)))
    for row in read(HERE/'PRE_SEAL.json')['members']:
        assert sha(HERE/row['path'])==row['sha256']
    executions=[]
    for prefix,receipt,script in [('CONTROL','EXECUTION.json','native_pair_controls.py'),
        ('LOCAL','LOCAL_EXECUTION.json','native_pair_local_row_certificate.py'),
        ('POLYNOMIAL','POLYNOMIAL_EXECUTION.json','native_pair_row_polynomial_certificate.py')]:
        d=read(AUTHOR/receipt)
        assert d['exit_code']==0 and d['code_sha256']==sha(AUTHOR/script)
        assert d['stdout_sha256']==sha(AUTHOR/(prefix+'.stdout'))
        assert (AUTHOR/(prefix+'.stderr')).stat().st_size==d['stderr_bytes']==0
        executions.append(d)
    author=read(AUTHOR/'NATIVE_PAIR_RESULTS.json');local=read(AUTHOR/'LOCAL_ROW_CERTIFICATE.json')
    poly=read(AUTHOR/'ROW_POLYNOMIAL_CERTIFICATE.json')
    assert author['source_sha256']==sha(AUTHOR/'native_pair_controls.py')
    assert local['source_sha256']==sha(AUTHOR/'native_pair_local_row_certificate.py')
    assert local['helper_sha256']==author['source_sha256']
    assert poly['source_sha256']==sha(AUTHOR/'native_pair_row_polynomial_certificate.py')
    assert poly['topology_helper_sha256']==local['source_sha256']
    assert poly['prior_row_certificate_sha256']==sha(AUTHOR/'LOCAL_ROW_CERTIFICATE.json')
    stdout=[json.loads(line) for line in (AUTHOR/'CONTROL.stdout').read_text().splitlines()]
    assert len(stdout)==5
    for out,row in zip(stdout[:-1],author['quotients']):
        assert out=={k:row[k] for k in out}
    assert stdout[-1]['sha256']==sha(AUTHOR/'NATIVE_PAIR_RESULTS.json')
    assert stdout[-1]['elapsed_seconds']==author['elapsed_seconds']
    expected={k:local[k] for k in read(AUTHOR/'LOCAL.stdout')}
    assert expected==read(AUTHOR/'LOCAL.stdout')
    assert (AUTHOR/'POLYNOMIAL.stdout').read_bytes()==(AUTHOR/'ROW_POLYNOMIAL_CERTIFICATE.json').read_bytes()
    return checked,executions,author,local,poly


if __name__=='__main__':
    tic=time.perf_counter();checked,executions,author,local,poly=bindings()
    result=dict(scope=__doc__,source_sha256=sha(Path(__file__)),source_bindings=checked,
        author_execution_bindings=executions,
        comparison=quotient_compare(author,read(HERE/'OCCUPATION_SPECTRUM_RESULTS.json'),read(HERE/'PRIMITIVE_COLORED_RESULTS.json')),
        local_counts=local_compare(local,poly),elapsed_seconds=time.perf_counter()-tic,
        no_author_program_execution_or_import=True,all_checks_satisfied=True)
    with (HERE/'POST_COMPARISON_RESULTS.json').open('x') as out:json.dump(result,out,indent=2);out.write('\n')
    summary={**result,'local_counts':{k:v for k,v in result['local_counts'].items()
        if k not in ('complete_near_rows','complete_far_rows','complete_synthetic_cases','L10_all_displacements')}}
    summary['local_row_counts']={k:len(result['local_counts'][k]) for k in
        ('complete_near_rows','complete_far_rows','complete_synthetic_cases','L10_all_displacements')}
    print(json.dumps(summary,indent=2))
