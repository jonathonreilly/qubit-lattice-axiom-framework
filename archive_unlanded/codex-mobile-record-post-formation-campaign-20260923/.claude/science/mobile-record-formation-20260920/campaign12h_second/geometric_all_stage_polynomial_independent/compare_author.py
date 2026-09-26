#!/usr/bin/env python3
"""Post-seal source authentication and selective independent comparison."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import datetime,hashlib,json,math,sys
sys.dont_write_bytecode=True
import independent_check as own

OUT=Path(__file__).resolve().parent;RAW=OUT.parent

def bind(p):
    b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())

def reconstruct_graph(row):
    K=row['K'];possible=list(product(range(K),range(K,2*K)))
    if 'graph_mask' in row:return [e for i,e in enumerate(possible) if row['graph_mask']>>i&1]
    kind=row['graph_kind']
    return [(a,b) for a,b in possible if kind=='complete' or b-K==a or b-K==a-1 or (kind=='cycle' and a==0 and b-K==K-1)]

def connected(K,E):
    seen={0}
    while True:
        updated=seen|{b for a,b in E if a in seen}|{a for a,b in E if b in seen}
        if updated==seen:return len(seen)==2*K
        seen=updated

def exact_mean_and_pivots(row):
    n=row['n'];kind=row['kind'];beta=F(row['beta']);h=row['hazards'];m=max(h);p=F(sum(h),n)
    A=[[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if kind=='complete' or j==i+1 or (kind=='cycle' and i==0 and j==n-1):
                A[i][i]+=1;A[j][j]+=1;A[i][j]-=1;A[j][i]-=1
    for i in range(n):A[i][i]+=beta*h[i]
    factor=2/(beta*p)+(1+2*m/p)/row['known_gap'];assert factor==F(row['inverse_eigenvalue_bound'])
    T=[[factor*A[i][j]-(i==j) for j in range(n)] for i in range(n)]
    pivots=[]
    for i in range(n):
        pivot=T[i][i];assert pivot>0;pivots.append(pivot)
        for j in range(i+1,n):
            for k in range(i+1,n):T[j][k]-=T[j][i]*T[i][k]/pivot
    assert pivots==list(map(F,row['exact_LDL_pivots']))
    augmented=[line+[F(1)] for line in A]
    for i in range(n):
        pivot=augmented[i][i];assert pivot>0
        augmented[i]=[x/pivot for x in augmented[i]]
        for j in range(n):
            if j==i:continue
            amount=augmented[j][i]
            augmented[j]=[a-amount*b for a,b in zip(augmented[j],augmented[i])]
    mean=[line[-1] for line in augmented];assert mean==list(map(F,row['exact_mean_by_start']))
    bound=(1+.5*math.log(n))*float(factor)
    assert abs(bound-row['uniform_logarithmic_bound'])<=1e-12*max(1,bound)
    return dict(n=n,kind=kind,hazards=h,beta=str(beta),exact_pivots=True,exact_mean=True)

def main():
    pre=json.loads((OUT/'PRE_COMPARISON_SEAL.json').read_text())
    for r in pre['artifacts']+pre['source_bindings']:assert bind(Path(r['path']))==r,r['path']
    results=json.loads((RAW/'geometric_all_stage_polynomial_checks/RESULTS.json').read_text())
    for name,digest in results['sources_sha256'].items():assert bind(RAW/name)['sha256']==digest
    for group in results['groups']:
        assert group['passed'] is True
        actual=json.loads((RAW/'geometric_all_stage_polynomial_checks'/f"{group['group']}.json").read_text())
        assert actual==group['detail']
    assert (RAW/'GEOMETRIC_ALL_STAGE_POLYNOMIAL_RUN.log').read_text()==''.join(g['group']+' PASS\n' for g in results['groups'])
    assert (RAW/'GEOMETRIC_ALL_STAGE_POLYNOMIAL_RUN.stderr').read_bytes()==b''
    pad=results['groups'][0]['detail'];inventory=[]
    for r in pad['inventory']:
        K=r['K'];possible=list(product(range(K),range(K,2*K)));masks=[]
        for mask in range(1<<len(possible)):
            E=[e for i,e in enumerate(possible) if mask>>i&1]
            if connected(K,E) and own.enumerate_rank(list(range(K)),list(range(K,2*K)),E,K):masks.append(mask)
        assert len(masks)==r['eligible_connected_graphs_with_perfect_matching']
        selected={x['graph_mask'] for x in pad['rows'] if x['K']==K}
        assert selected<=set(masks) and len(selected)==r['selected_graphs']
        inventory.append(dict(K=K,eligible=len(masks),selected=len(selected)))
    rowschecked=0;selected=[];shared=[]
    prior=json.loads((OUT/'INDEPENDENT_RESULTS.json').read_text())['padded_cases']
    for row in pad['rows']:
        K,j=row['K'],row['j'];k=j+1;h=K-k;f0=math.factorial(h)**2;E=reconstruct_graph(row)
        layers=[own.enumerate_rank(list(range(K)),list(range(K,2*K)),E,r) for r in range(K+1)]
        a=list(map(len,layers));assert row['m']==len(E)
        expected={'perfect':a[k]*f0,'two_original':a[j]*(h+1)**2*f0,'mixed':a[k]*2*h*f0,
                  'two_dummy':(a[k+1] if k<K else 0)*f0}
        assert all(row['fiber_counts'].get(key,0)==value for key,value in expected.items())
        nh=sum(expected.values());mh=len(E)+2*h*K
        assert row['augmented_states']==nh and row['augmented_edges']==mh
        assert row['augmented_vertices']==2*(K+h) and row['original_two_level_states']==a[j]+a[k]
        assert F(row['exact_R_hat'])==F(nh-expected['perfect'],expected['perfect'])
        assert F(row['proved_upper_R_hat'])==(h+1)*F(a[K-1],a[K])+2*h+F(len(E),k+1)
        assert row['maximum_good_projected_edge_multiplicity']<=(h+1)**2*f0*mh
        assert row['maximum_bad_parent_multiplicity']==(2*f0 if h else 0)
        assert row['exact_good_minimum_fiber']==(2*h+1)*f0
        assert row['energy_PSD_scaled_minimum']>=-1e-12
        rowschecked+=1
        if K==4 and row.get('graph_kind')=='complete':
            ours=next(x for x in prior if x['graph']=='complete_bipartite4' and x['rank']==j)
            shared.append(dict(K=K,j=j,source='sealed independent dense fixture'))
        elif (K==2 and row.get('graph_mask')==13) or (K==3 and row.get('graph_mask') in [87,511]) or (K==4 and row.get('graph_kind')=='path' and j in [1,2]):
            ours=own.padded_case('selected_author_fixture',K,E,j,layers)
            selected.append(ours)
        else:continue
        assert ours['augmented_undirected_transitions']==row['augmented_transition_edges']
        assert ours['full_states']+ours['near_states']==nh
        assert ours['bad_states']==expected['two_dummy']
        if 'numeric_gap_comparison' in row:
            assert abs(ours['numerical_auxiliary_gap']-row['numeric_gap_comparison']['two_level'])<2e-12
            if ours['numerical_padded_gap'] is not None:assert abs(ours['numerical_padded_gap']-row['numeric_gap_comparison']['augmented'])<2e-12
    killed=[exact_mean_and_pivots(r) for r in results['groups'][1]['detail']]
    cubic=results['groups'][2]['detail'];cubic_count=0
    for row in cubic:
        K=row['K'];m=6*K
        for stage in row['stages']:
            j=stage['j'];k=j+1;h=K-k;mh=m+2*h*K;U=(h+1)*F(K*K,6)+2*h+F(m,k+1)
            C=1+(2*K-2)*(m+m*m)*(k-1)*(k+1+2*m)
            assert stage['mhat']==mh and F(stage['R_upper'])==U and stage['corridor_C']==C
            ratio=256*mh*mh*(h+2)*U**4*C/F(2**23*K**22)
            assert ratio==F(stage['ratio_to_coarse_gap_denominator'])<=1;cubic_count+=1
        assert F(row['selection_delta_bound'])==F(3,32*K**3)
        assert F(row['sequence_TV_bound'])==F(3,16*K**2)
        assert F(row['relative_clock_mean_bound'])==F(3,13*K**3)
    author=[RAW/'geometric_all_stage_polynomial_check.py',RAW/'GEOMETRIC_ALL_STAGE_POLYNOMIAL_GAP_AND_FILLING.md',
        RAW/'EMPTY_START_DETERMINISTIC_WAVE_PREPARATION.md',RAW/'GEOMETRIC_ALL_STAGE_FORMATION_CLOCK.md',
        RAW/'GEOMETRIC_POLYNOMIAL_RELAXATION_AND_FORMATION.md',
        *sorted((RAW/'geometric_all_stage_polynomial_checks').iterdir()),
        RAW/'GEOMETRIC_ALL_STAGE_POLYNOMIAL_RUN.log',RAW/'GEOMETRIC_ALL_STAGE_POLYNOMIAL_RUN.stderr']
    payload=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='pass',
        preseal_artifacts_authenticated=len(pre['artifacts']),preseal_sources_authenticated=len(pre['source_bindings']),
        original_graph_inventory=inventory,all_fiber_rows_independently_counted=rowschecked,
        shared_presealed_transition_fixtures=shared,fresh_selected_full_transition_comparisons=selected,
        independent_fraction_LDL_and_mean_rows=killed,exact_cubic_rows=cubic_count,
        sources=[bind(p) for p in author],
        scope='Complete author source read; complete JSON groups/logs parsed and authenticated. Selected complete augmented graphs independently rebuilt. No author code imported or run. The deterministic-window note has no new checker; its conditional-law and coupling steps were reconstructed before comparison.')
    (OUT/'AUTHOR_COMPARISON.json').write_text(json.dumps(payload,indent=2)+'\n')
    print(json.dumps({'status':'pass','fiber_rows':rowschecked,'fresh_transition_fixtures':len(selected),'reused_presealed_fixtures':len(shared),'exact_killing_rows':len(killed),'exact_cubic_rows':cubic_count,'author_files':len(author)},indent=2))

if __name__=='__main__':main()
