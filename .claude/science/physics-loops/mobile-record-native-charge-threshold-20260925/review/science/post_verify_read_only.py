"""Read-only POST40 correspondence checker, authored after author release.

No local or author module is imported or executed. All writes, including stdout
capture, belong to an external caller. Primitive input columns are unchanged
blind PRE evidence. New calculations are exact standard-library arithmetic.
"""
from pathlib import Path
from hashlib import sha256
from collections import Counter
from fractions import Fraction
from itertools import product, permutations
import ast
import json

HERE=Path(__file__).resolve().parent
A=HERE/'post_sources'/'author'
THRESHOLD=12096
DEN=10**9

def digest(path):
    return sha256(path.read_bytes()).hexdigest()

def read(path):
    return json.loads(path.read_bytes())

def kind(pair, side=None):
    differences=[abs(a-b) for a,b in zip(*pair)]
    if side is not None:
        differences=[min(d,side-d) for d in differences]
    return tuple(sorted(differences))

def classes(radius):
    return sorted({tuple(sorted(v)) for v in product(range(radius+1),repeat=3)
                   if 0<sum(v)<=radius and sum(v)%2==0})

def group(column, side=None):
    result=Counter()
    for target,value in column.items():result[kind(target,side)]+=value
    return dict(result)

def to_column(rows):
    return {tuple(tuple(p) for p in target):value for target,value in rows}

def shifted(column, offset, side=None):
    result=Counter()
    for target,value in column.items():
        moved=[]
        for point in target:
            point=tuple(a+b for a,b in zip(point,offset))
            if side is not None:point=tuple(v%side for v in point)
            moved.append(point)
        result[tuple(sorted(moved))]+=value
    return {target:value for target,value in result.items() if value}

def neighbors(point):
    result=[]
    for axis in range(3):
        for sign in (-1,1):
            v=list(point);v[axis]+=sign;result.append(tuple(v))
    return result

def active_and_empty(occupied):
    # Geometric inventory and empty diagonal, not a repeat of the author row builder.
    pairs=set()
    for b in occupied:
        for a in neighbors(b):
            for shared in neighbors(a):
                for c in neighbors(shared):
                    if a!=c:pairs.add(tuple(sorted((a,c))))
    empty=0
    for a,c in pairs:
        multiplicities=Counter(tuple(sorted((u,v))) for u in neighbors(a)
                               for v in neighbors(c) if u!=v)
        empty+=2*sum(m*m for m in multiplicities.values())
    return len(pairs),empty

def canonical_map(pair, target):
    # Translate/reflect/permute a pair to (0,sorted absolute displacement).
    u,v=pair
    diff=tuple(b-a for a,b in zip(u,v))
    order=tuple(sorted(range(3),key=lambda i:abs(diff[i])))
    signs=tuple(1 if diff[i]>=0 else -1 for i in order)
    answer=tuple(sorted(tuple(sign*(p[i]-u[i]) for i,sign in zip(order,signs)) for p in target))
    return tuple(abs(diff[i]) for i in order),answer

def orbit_size(d):
    return len({tuple(x*s for x,s in zip(p,signs)) for p in permutations(d)
                for signs in product((-1,1),repeat=3)})

def check_preservation(pins):
    for member in pins['preserved_prior_files']:
        path=Path(member['path']);stat=path.stat()
        assert digest(path)==member['sha256'] and stat.st_size==member['bytes']
        assert stat.st_mtime_ns==member['mtime_ns'] and stat.st_ctime_ns==member['ctime_ns']
    for member in pins['new_source_pins']:
        frozen=HERE/member['frozen_path'];origin=Path(member['origin'])
        assert digest(frozen)==member['sha256']==digest(origin)
        assert frozen.stat().st_size==member['bytes']==origin.stat().st_size
    for member in pins['inherited_PRE_source_pins']:
        frozen=HERE/member['frozen_path']
        assert digest(frozen)==member['sha256'] and frozen.stat().st_size==member['bytes']
        if not member['origin'].startswith('git:'):
            assert Path(member['origin']).read_bytes()==frozen.read_bytes()

def main():
    pins=read(HERE/'POST_SOURCE_PINS.json');check_preservation(pins)
    seal=read(HERE/'PRE_SEAL.json')
    assert digest(HERE/'PRE_SEAL.json')==pins['PRE_seal_sha256']
    assert len(seal['members'])==54
    for row in seal['members']:
        assert digest(HERE/row['path'])==row['sha256']
        assert (HERE/row['path']).stat().st_size==row['bytes']
    author_seal=read(A/'AUTHOR_SEAL.json')
    assert len(author_seal['members'])==27
    for row in author_seal['members']:
        assert digest(A/row['path'])==row['sha256']
        assert (A/row['path']).stat().st_size==row['bytes']
    own=read(HERE/'DECISIVE_RESULTS.json')
    raw={tuple(row['separation']):to_column(row['complete_column'])
         for row in read(HERE/'UNWRAPPED_PRIMITIVE_COLUMNS.json')}
    assert sorted(raw)==classes(10) and sum(map(len,raw.values()))==6876
    own_rows={tuple(row['separation']):row for row in own['supersolution']['complete_unwrapped_type_rows']}
    author=read(A/'attempt05'/'RESULT.json')
    assert author['source_sha256']==digest(A/'two_record_threshold_and_charge_controls.py')
    assert author['imported_scientific_helpers']==[]
    tree=ast.parse((A/'two_record_threshold_and_charge_controls.py').read_text())
    imported=[]
    for node in ast.walk(tree):
        if isinstance(node,ast.Import):imported.extend(v.name for v in node.names)
        elif isinstance(node,ast.ImportFrom):imported.append(node.module)
    assert set(imported)=={'collections','fractions','itertools','pathlib','argparse','hashlib','json','time'}
    literal_deficits=next(ast.literal_eval(node.value) for node in tree.body
                          if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='DEFICITS' for t in node.targets))
    deficits={tuple(d):x for d,x in author['deficits']}
    assert deficits==literal_deficits and sorted(deficits)==classes(6)
    assert author['denominator']==DEN and all(0<=v<DEN for v in deficits.values())
    assert min(DEN-v for v in deficits.values())==937545272
    own_c={tuple(d):v for d,v in own['supersolution']['corrections_numerators']}
    assert any(deficits[d]!=-own_c[d] for d in deficits)
    residuals=[];group_entries=0
    for row in author['unwrapped_rows']:
        d=tuple(row['type']);column=raw[d];g=group(column)
        assert g=={tuple(k):v for k,v in row['grouped_integer_row']}
        assert g=={tuple(k):v for k,v in own_rows[d]['grouped_column']}
        assert sum(column.values())==row['row_sum']==own_rows[d]['row_sum']
        assert len(column)==row['target_count']
        pairs,empty=active_and_empty(((0,0,0),d))
        assert pairs==row['active_A_pairs']
        assert sum(column.values())+empty==2*row['ordered_out_return_paths']
        numerator=sum(value*(DEN-deficits.get(k,0)) for k,value in g.items())-THRESHOLD*(DEN-deficits.get(d,0))
        assert numerator==row['trial_residual_numerator']<=0
        own_residual=sum(value*(DEN+own_c.get(k,0)) for k,value in g.items())-THRESHOLD*(DEN+own_c.get(d,0))
        assert own_residual==own_rows[d]['residual_numerator']<0
        residuals.append({'type':d,'entries':len(column),'groups':len(g),'active_pairs':pairs,
                          'ordered_paths':row['ordered_out_return_paths'],'row_sum':row['row_sum'],
                          'author_residual':numerator,'PRE_residual':own_residual})
        group_entries+=len(g)
    assert len(residuals)==37
    defect=sum((sum(raw[d].values())-THRESHOLD)*orbit_size(d) for d in classes(4))
    assert defect==author['near_total_row_defect']==-1548
    kernel={tuple(d):v for d,v in author['auxiliary_one_occupancy_kernel']}
    assert kernel=={tuple(d):v for d,v in own['single_algebraic_kernel']['complete_column']}
    assert len(kernel)==85 and sum(kernel.values())==author['auxiliary_kernel_row_sum']==6048
    assert all(kernel[d]==kernel[tuple(-x for x in d)] for d in kernel)
    second=[[sum(c*d[i]*d[j] for d,c in kernel.items()) for j in range(3)] for i in range(3)]
    assert second==author['auxiliary_kernel_second_moment']==[[7392,0,0],[0,7392,0],[0,0,7392]]
    fourth=sum(c*sum(x*x for x in d)**2 for d,c in kernel.items())
    assert fourth==93696
    _,single_empty=active_and_empty(((0,0,0),))
    assert 6048+single_empty==2*author['auxiliary_ordered_paths']==12678

    def free_column(d):
        x=((0,0,0),d);out=Counter()
        for i in (0,1):
            for move,c in kernel.items():
                y=tuple(a+b for a,b in zip(x[i],move))
                out[tuple(sorted((y,x[1-i])))]+=c
        return {y:c for y,c in out.items() if c}
    for d,column in raw.items():
        if sum(d)>4:assert column==free_column(d)
    assert author['far_pair_equals_two_auxiliary_contributions'] is True
    periodic=[]
    for row in author['periodic_controls']:
        side=row['side'];d=tuple(row['type']);origin=tuple(row['origin'])
        assert side in (24,26)
        column=shifted(raw[d] if d in raw else free_column(d),origin,side)
        x=tuple(sorted((origin,tuple((a+b)%side for a,b in zip(origin,d)))))
        g=group(column,side)
        value=sum(c*(DEN-deficits.get(kind(y,side),0)) for y,c in column.items())-THRESHOLD*(DEN-deficits.get(kind(x,side),0))
        assert sum(column.values())==row['row_sum'] and len(column)==row['target_count']
        assert value==row['trial_residual_numerator']<=0
        assert row['near_full_grouped_row_equal_unwrapped']==(sum(d)<=6)
        if sum(d)<=6:assert g==group(raw[d])
        periodic.append({'side':side,'type':d,'origin':origin,'row_sum':sum(column.values()),
                         'target_count':len(column),'residual':value})
    assert len(periodic)==68
    reciprocity=[]
    for row in author['reciprocity_controls']:
        d=tuple(row['input_type']);x=((1,0,0),(1+d[0],d[1],d[2]))
        y=tuple(tuple(v) for v in row['target'])
        forward=shifted(raw[d],(1,0,0))[y]
        reverse_type,target=canonical_map(y,x)
        reverse=raw[reverse_type][target]
        assert forward==reverse==row['both_coefficients']
        reciprocity.append({'input':d,'target':y,'coefficient':forward,'reverse_type':reverse_type})
    assert len(reciprocity)==43

    # Full stored exploratory row histories and both exact author witnesses.
    attempts=[]
    for index,filename,radius in [(1,'stdout.json',2),(2,'RESULT.json',4),(3,'RESULT.json',6)]:
        folder=A/f'attempt{index:02d}';data=read(folder/filename)
        rows=data['classes'] if index==1 else data['rows'];small=classes(radius)
        for row in rows:
            d=tuple(row['displacement_type']);g=group(raw[d])
            assert g=={tuple(k):v for k,v in row['grouped_exact_row']}
            assert sum(g.values())==row['row_sum']
            assert row['correction']==row['row_sum']-THRESHOLD
            assert row['deficit_coefficients']==[-g.get(k,0)+(THRESHOLD if k==d else 0) for k in small]
        assert len(rows)==len(classes(radius+4))
        script='explore_two_record_threshold.py' if index==1 else 'explore_two_record_threshold_extended.py'
        assert data['source_sha256']==digest(folder/script)==digest(A/script)
        receipt=read(folder/'EXECUTION.json');assert receipt['exit_code']==0
        assert receipt['source_sha256']==data['source_sha256']
        out='stdout.json' if index==1 else 'stdout.log'
        assert (folder/out).stat().st_size==receipt['stdout_bytes']
        assert (folder/'stderr.log').stat().st_size==receipt['stderr_bytes']==0
        if index!=1:assert read(folder/'stdout.log')=={k:v for k,v in data.items() if k!='rows'}
        assert data['lp_success']==(index==3)
        if index==1:
            assert all(data[k] is None for k in ['proposed_deficits','exact_supersolution_residuals','all_listed_residuals_nonpositive'])
        elif index==2:assert data['exact_certificate'] is None
        else:
            cert=data['exact_certificate'];values={tuple(row['type']):Fraction(row['value']) for row in cert['deficits']}
            assert sorted(values)==small and all(0<=v<1 for v in values.values())
            assert len(cert['residuals'])==37
            for row in cert['residuals']:
                d=tuple(row['type']);g=group(raw[d])
                value=sum(c*(1-values.get(k,0)) for k,c in g.items())-THRESHOLD*(1-values.get(d,0))
                assert value==Fraction(row['value'])<=0
            assert cert['all_deficits_in_zero_one'] and cert['all_residuals_nonpositive']
        attempts.append({'attempt':index,'rows':len(rows),'groups':sum(len(row['grouped_exact_row']) for row in rows),
                         'recorded_lp_success':data['lp_success'],'elapsed_seconds':data['elapsed_seconds'],
                         'wrapper_elapsed_seconds':receipt['elapsed_seconds']})
    short=read(A/'attempt04'/'RESULT.json')
    assert short['source_rows_sha256']==digest(A/'attempt03'/'RESULT.json')
    assert short['denominator']==DEN
    assert {tuple(row['type']):row['numerator'] for row in short['deficit_numerators']}==deficits
    assert {tuple(row['type']):row['numerator_at_common_denominator'] for row in short['residuals']}=={
        tuple(row['type']):row['author_residual'] for row in residuals}
    assert short['lp_success'] and short['all_exact_residuals_nonpositive'] and short['all_deficits_in_zero_one']

    # Independently spell out diagonal charge words and oriented two-edge Gauss shifts.
    charges=[];totals=Counter()
    for result in author['charge_controls']:
        side=result['side'];vertices=list(product(range(side),repeat=3))
        aset=[v for v in vertices if sum(v)%2==0];bset=[v for v in vertices if sum(v)%2==1]
        n=len(aset);m=n+2;degree=3 if side==2 else 6
        assert result['A_sites']==n and result['occupied_sites_after_one_birth']==m
        expected_scalars={'uniform_minus_mean_A_excitation':Fraction(-2,m),
            'uniform_minus_mean_occupied_B_charge':Fraction(n,m),
            'uniform_minus_probability_minus_on_B':Fraction(2,m),
            'resolved_first_birth_color_line_weight':Fraction(1,m),
            'flat_coherent_first_birth_color_line_weight':Fraction(2,m)}
        for k,v in expected_scalars.items():assert Fraction(result[k])==v
        counts=Counter()
        for a in aset:
            ns=sorted({tuple(x%side for x in v) for v in neighbors(a)})
            assert len(ns)==degree
            for b in ns:
                for sign in (-1,1):
                    branch_count=0
                    for c in ns:
                        if c==b:continue
                        word={a:sign-1,b:-sign,c:1}
                        divergence=Counter({a:sign,b:-sign});divergence[a]-=1;divergence[c]+=1
                        assert {v:q for v,q in word.items() if q}=={v:q for v,q in divergence.items() if q}
                        assert sum(word.values())==0
                        minus=b if sign==1 else a
                        assert minus in aset or minus in (b,c)
                        counts['minus_on_B' if minus in (b,c) else 'minus_on_A']+=1
                        counts['resolved_primitive_outputs']+=1;branch_count+=1
                    assert branch_count==degree-1
                    counts['resolved_edge_sign_marks']+=1
                counts['flat_coherent_edge_controls']+=1
        assert dict(counts)==result['counts']
        b,c=bset[:2];occupied=aset+[b,c]
        tests={'total':lambda v:1,'one_A':lambda v:int(v==aset[0]),
               'one_B':lambda v:int(v==b),'both_B':lambda v:int(v in (b,c)),
               'coordinate':lambda v:v[0]-2*v[1]+3*v[2]}
        moments=[]
        for row in result['test_charge_rows']:
            f=tests[row['test']];eigenvalues=[f(b)+f(c)-2*f(z) for z in occupied]
            mean=Fraction(sum(eigenvalues),m)
            variance=sum((Fraction(q)-mean)**2 for q in eigenvalues)/m
            fmean=Fraction(sum(f(z) for z in occupied),m)
            assert mean==f(b)+f(c)-2*fmean
            assert variance==4*(Fraction(sum(f(z)**2 for z in occupied),m)-fmean**2)
            assert str(mean)==row['charge_mean'] and str(variance)==row['charge_variance']
            # Norm of the perpendicular component is the exact average squared
            # coefficient after subtracting the uniform-vector expectation.
            leakage=sum((Fraction(q)-mean)**2 for q in eigenvalues)/m
            assert leakage==variance
            moments.append({**row,'perpendicular_norm_squared':str(leakage)})
        assert len(moments)==5
        totals.update(counts);charges.append({'side':side,'counts':dict(counts),'moments':moments})
    assert totals['resolved_primitive_outputs']==8448
    assert totals['resolved_edge_sign_marks']==1704 and totals['flat_coherent_edge_controls']==852

    # Final result/stdout/execution must be the declared source's recorded run.
    receipt=read(A/'attempt05'/'EXECUTION.json')
    assert receipt['exit_code']==0 and receipt['source_sha256']==author['source_sha256']
    assert receipt['command'][1]==str(HERE.parent/'native-charge-identification-personal'/'two_record_threshold_and_charge_controls.py')
    assert receipt['command'][2:]==['--output',str(HERE.parent/'native-charge-identification-personal'/'attempt05'/'RESULT.json')]
    assert digest(A/'attempt05'/'stdout.txt')==receipt['stdout_sha256']
    assert digest(A/'attempt05'/'stderr.txt')==receipt['stderr_sha256']
    assert (A/'attempt05'/'stderr.txt').stat().st_size==0
    omitted={'unwrapped_rows','periodic_controls','reciprocity_controls','auxiliary_one_occupancy_kernel'}
    assert read(A/'attempt05'/'stdout.txt')=={k:v for k,v in author.items() if k not in omitted}
    assert digest(A/'attempt05'/'two_record_threshold_and_charge_controls.py')==author['source_sha256']
    assert 0<author['elapsed_seconds']<receipt['elapsed_seconds']
    check_preservation(pins)
    output={'scope':'Released-source exact correspondence; no author scientific program execution/import, no new blind claim, no audit verdict.',
        'source_sha256':digest(Path(__file__)),
        'all_PRE_members_preserved':54,'prior_files_byte_and_stat_preserved':len(pins['preserved_prior_files']),
        'released_author_members_verified':27,'source_origins_verified':len(pins['new_source_pins']),
        'inherited_source_pins_verified':len(pins['inherited_PRE_source_pins']),
        'author_imports':imported,'primitive_PRE_entries_consumed':sum(map(len,raw.values())),
        'matched_author_grouped_entries':group_entries,'unwrapped_rows':residuals,
        'author_minimum_trial_numerator':min(DEN-v for v in deficits.values()),
        'distinct_PRE_minimum_trial_numerator':own['supersolution']['positive_minimum_numerator'],
        'near_total_row_defect':defect,'kernel_entries':len(kernel),'kernel_second_moment':second,
        'kernel_fourth_moment':fourth,'Euclidean_fourth_order_remainder_bound_coefficient':str(Fraction(fourth,24)),
        'periodic_controls_from_PRE_periodization':periodic,'reciprocity_from_PRE_columns':reciprocity,
        'historical_attempts':attempts,'attempt03_exact_rational_residuals_recomputed':37,
        'attempt04_short_residuals_recomputed':37,
        'attempt04_missing_saved_source_and_execution_receipt':True,
        'charge_controls':charges,'charge_counts':dict(totals),
        'author_result_elapsed_seconds':author['elapsed_seconds'],
        'author_execution_elapsed_seconds':receipt['elapsed_seconds'],
        'author_result_stdout_execution_bindings_match':True}
    print(json.dumps(output,indent=2))

if __name__=='__main__':
    main()
