#!/usr/bin/env python3
"""Post-seal authentication and selective comparison; imports only own controls."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from datetime import datetime,timezone
from itertools import permutations,product
import hashlib,json,math
import numpy as np
import sympy as s
import singlet_local_check as independent

OUT=Path(__file__).resolve().parent;RAW=OUT.parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
read=lambda p:json.loads(Path(p).read_text())
pre=read(OUT/'PRE_COMPARISON_SEAL.json')
for row in pre['artifacts']:
    p=OUT/row['path'];assert p.stat().st_size==row['bytes'] and sha(p)==row['sha256']
for row in pre['sources']:
    p=Path(row['path']);assert p.stat().st_size==row['bytes'] and sha(p)==row['sha256']

names=['geometric_singlet_fiber','geometric_klein_parent','geometric_local_quantum_gram_fast','geometric_singlet_channel','dimer_color_operational_moment']
sources={};answers={};bindings=[]
def bind(p):
    p=Path(p).resolve();sources[str(p)]={'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)}
for name in names:
    p=RAW/(name+'_checks')/'RESULTS.json';data=read(p);answers[name]=data;bind(p)
    for source,digest in data.get('sources_sha256',data.get('sources',{})).items():
        q=RAW/source;assert sha(q)==digest;bind(q);bindings.append({'result':str(p),'source':source,'matched_sha256':digest})
    log=RAW/(name.upper()+'_RUN.log');stderr=RAW/(name.upper()+'_RUN.stderr')
    assert not stderr.read_bytes();bind(log);bind(stderr)
    if name in names[:2]:assert read(log)==data
    elif name=='geometric_local_quantum_gram_fast':assert [json.loads(line) for line in log.read_text().splitlines()]==data['rows']
    else:assert log.read_text().splitlines()==[g['group']+' PASS' for g in data['groups']]

own=read(OUT/'SINGLET_LOCAL_RESULTS.json');byshape={tuple(r['shape']):r for r in own['local_graphs']}
comparison=[];built={}
for row in answers['geometric_local_quantum_gram_fast']['rows']:
    shape=tuple(row['shape']);expected=byshape[shape]
    fields={'sites':'vertices','singlet_covers':'covers','magnetization_zero_dimension':'spin_sector_dimension',
        'NN_leakage_rank':'nn_leakage_rank','ring_leakage_rank':'ring_leakage_rank',
        'NN_squared_Frobenius_leakage':'nn_leakage_norm_squared','ring_squared_Frobenius_leakage':'ring_leakage_norm_squared',
        'minimum_squared_Frobenius_leakage':'minimal_combination_leakage_squared'}
    for a,b in fields.items():assert row[a]==expected[b],(shape,a,row[a],expected[b])
    assert row['exact_least_squares_alpha']==(expected['optimal_nn_coefficient'] or 'unrestricted')
    assert row['exact_cover_subspace_closure']==(s.Rational(expected['minimal_combination_leakage_squared'])==0)
    coords,edges,faces,black=independent.geometry(shape);V=len(coords);covers=independent.matchings(V,edges)
    basis,index,D=independent.columns(V,covers,black);G=D.T*D/2**(V//2)
    Wnn=independent.action_on_columns(D,basis,index,[independent.spin_permutation(V,list(e)) for e in edges])
    cycles=[c for face in faces for c in [list(face),list(reversed(face))]]
    Wr=independent.action_on_columns(D,basis,index,[independent.spin_permutation(V,c) for c in cycles])
    maximum=max(abs(x) for A in [D,Wnn,Wr] for x in A);bound=len(basis)*maximum**2
    assert bound==row['integer_dot_product_bound'] and bound<2**63
    comparison.append({'shape':shape,'all_reported_ranks_norms_optimum_and_integer_bound_match':True})
    if shape in [(2,2),(2,3),(2,2,2)]:built[{(2,2):'square',(2,3):'ladder6',(2,2,2):'cube8'}[shape]=(D,G,Wnn,Wr)

for row in answers['geometric_singlet_fiber']['rows']:
    D,G,_,_=built[row['graph']];Gauthor=s.sympify(row['Gram'],locals={'Matrix':s.Matrix})
    assert Gauthor.eigenvals()==G.eigenvals() and sorted(Gauthor)==sorted(G)
    assert row['VB_rank']==D.cols and row['fiber']==2**(int(math.log2((D.T*D)[0,0])))*math.factorial(int(math.log2((D.T*D)[0,0])))
assert answers['geometric_singlet_fiber']['square_readout']=={'RVB_norm_squared':'3','RVB_singlet_projector':'3/4','incoherent_singlet_cover_mixture':'5/8','classical_uniform_geometric_occupation':'1/2'}

parent=answers['geometric_klein_parent'];ours=own['cube_parent']
assert parent['VB_dimension']==ours['exact_cover_span_dimension'] and parent['parent_kernel_dimension']==ours['exact_parent_kernel_dimension']
assert parent['extra_groundspace_dimension']=='10'
for row,expected in zip(parent['magnetization_sectors'],ours['magnetization_sectors']):
    assert row['down_spins']==expected['number_down'] and row['dimension']==expected['dimension'] and row['exact_nullity']==expected['exact_kernel_dimension']
    assert abs(row['smallest_positive_eigenvalue']-expected['finite_numerical_positive_gap'])<2e-13
D,G,NN,RING=built['cube8'];norm=(D.T*D)[0,0]
Gauthor=s.sympify(answers['geometric_singlet_fiber']['rows'][2]['Gram'],locals={'Matrix':s.Matrix})
for row,W,expectednorm in zip(parent['perturbations'],[NN,RING],[5,20]):
    A=(D.T*D).inv(method='DM')*D.T*W
    reported=s.sympify(row['coefficient_matrix'],locals={'Matrix':s.Matrix})
    assert Gauthor*reported==reported.T*Gauthor and reported!=reported.T
    assert reported.charpoly().all_coeffs()==A.charpoly().all_coeffs()
    assert row['squared_Frobenius_leakage']==str(expectednorm)
    assert row['leakage_rank']==row['outside_parent_kernel_rank']==1 and row['extra_parent_groundspace_rank']==0

channel=answers['geometric_singlet_channel'];rows=channel['groups'][0]['detail']
for row in rows:
    _,G,_,_=built[row['graph']]
    Gauthor=s.sympify(row['Gram'],locals={'Matrix':s.Matrix});assert Gauthor.eigenvals()==G.eigenvals()
    rowsums=[sum(G.row(i)) for i in range(G.rows)];bound=max(rowsums)
    assert sorted(map(s.Rational,row['exact_row_sums']))==sorted(rowsums)
    assert s.Rational(row['rational_filter_scale_squared'])==1/bound
    assert s.Rational(row['rational_filter_uniform_success'])==sum(G)/(G.rows*bound)
    spectrum={s.sympify(k):v for k,v in row['exact_filter_defect_eigenvalues'].items()}
    assert spectrum==(s.eye(G.rows)-G/bound).eigenvals()
    top=float(max(G.eigenvals()));assert abs(top-row['numerical_lambda_max'])<2e-13
    assert abs(float(sum(G)/G.rows)/top-row['numerical_optimal_uniform_success'])<2e-13
for row in channel['groups'][1]['detail']['product_Grams']:
    P=row['tiles'];assert s.Rational(row['exact_top_eigenvalue'])==s.Rational(3,2)**P
    assert s.Rational(row['exact_basis_success'])==s.Rational(2,3)**P
    assert row['product_eigenvalues']=={str(s.Rational(3,2)**(P-j)*s.Rational(1,2)**j):math.comb(P,j) for j in range(P+1)}

moment=answers['dimer_color_operational_moment'];controls=moment['groups'][1]['detail']['tilted_moment_controls']
moments=[s.diag(s.Rational(1,2),s.Rational(1,3),s.Rational(1,6)),s.Matrix([[s.Rational(1,3),s.Rational(1,12),0],[s.Rational(1,12),s.Rational(1,3),0],[0,0,s.Rational(1,3)]])]
for offset,M in enumerate(moments):
    for j,row in enumerate(controls[offset*6:(offset+1)*6]):
        axis=row['axis'];tilt=s.Rational(row['tilt']);mu=tilt*M[:,axis]
        rho=s.Matrix.vstack(s.Matrix.hstack(s.ones(1),mu.T),s.Matrix.hstack(mu,M))/2
        minors=[s.Integer(1)]+[rho[:k,:k].det() for k in range(1,5)]
        pivots=[s.factor(minors[k+1]/minors[k]) for k in range(4)]
        assert list(map(str,pivots))==row['exact_positive_LDL_pivots'] and all(x>0 for x in pivots)
assert moment['groups'][2]['detail']['odd_tangent_rank']==7 and moment['groups'][2]['detail']['vector_feature_rank_on_kernel']==6

development=[]
for folder,current,old,new in [
 ('local_quantum_gram_shape_assertion','geometric_local_quantum_gram_fast_check.py',"assert a['shape']==b['shape']","assert tuple(a['shape'])==tuple(b['shape'])"),
 ('singlet_channel_symbolic_equality','geometric_singlet_channel_check.py','assert out==expected and s.trace(out)==1','assert s.simplify(out-expected)==s.zeros(2**n) and s.simplify(s.trace(out))==1')]:
    root=RAW/'dimer_routed_development'/folder;before=root/current
    assert before.read_text().count(old)==1 and before.read_text().replace(old,new)==(RAW/current).read_text()
    for p in root.iterdir():
        if p.is_file():bind(p)
    development.append({'folder':folder,'sole_source_correction':{'before':old,'after':new},'scientific_definitions_unchanged':True})
for folder,current,stem in [('local_quantum_combination_dense_attempt','geometric_local_quantum_combination_check.py','GEOMETRIC_LOCAL_QUANTUM_COMBINATION_RUN'),('local_quantum_gram_rank_attempt','geometric_local_quantum_gram_check.py','GEOMETRIC_LOCAL_QUANTUM_GRAM_RUN')]:
    root=RAW/'dimer_routed_development'/folder
    assert (root/current).read_bytes()==(RAW/current).read_bytes()
    for suffix in ['.log','.stderr']:assert (root/(stem+suffix)).read_bytes()==(RAW/(stem+suffix)).read_bytes();bind(RAW/(stem+suffix))
    for p in root.iterdir():
        if p.is_file():bind(p)
    bind(RAW/current)
    rows=[json.loads(line) for line in (root/(stem+'.log')).read_text().splitlines()];assert len(rows)==4
    for row in rows:
        expected=byshape[tuple(row['shape'])]
        assert row['NN_squared_Frobenius_leakage']==expected['nn_leakage_norm_squared']
        assert row['ring_squared_Frobenius_leakage']==expected['ring_leakage_norm_squared']
    development.append({'folder':folder,'completed_patch_rows':4,'unfinished_12_site_step_not_counted_as_completed':True})

answer={'created_utc':datetime.now(timezone.utc).isoformat(),'precomparison_seal_sha256':sha(OUT/'PRE_COMPARISON_SEAL.json'),
 'unchanged_precomparison_artifacts_authenticated':len(pre['artifacts']),'result_source_bindings_authenticated':bindings,
 'completed_result_packets':5,'independent_local_patch_comparisons':comparison,
 'other_mathematical_comparisons':['Cover Gram spectra/entries and fiber counts; square readouts','Cube full magnetization nullities, gap tolerance, compressed operator characteristic polynomials and Gram self-adjointness','Three channel Grams, exact filter defects/scales, six tiled Gram spectra','Twelve positive moment LDL pivot rows via independent leading-minor ratios'],
 'preserved_author_attempts':development,'no_author_code_executed':True,
 'scope':'Post-seal source/evidence authentication and targeted algebra, not a new blind derivation or an execution of the author suite.'}
(OUT/'AUTHOR_COMPARISON.json').write_text(json.dumps(answer,indent=2)+'\n')
(OUT/'POST_COMPARISON_SOURCES.json').write_text(json.dumps({'created_utc':datetime.now(timezone.utc).isoformat(),'sources':list(sources.values())},indent=2)+'\n')
print(json.dumps({'completed_packets':5,'source_bindings':len(bindings),'sources_and_evidence':len(sources),'local_patches':len(comparison),'precomparison_artifacts_unchanged':len(pre['artifacts']),'status':'all stated comparisons passed'},indent=2))
