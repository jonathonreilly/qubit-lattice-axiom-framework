"""New released-source recovery comparator. No imported source code or writes.

Reads only captured evidence and its already observed live originals. The
caller owns new stdout/stderr records. No simulation, subprocess, eval, exec,
author module, old checker, writer, pipeline, network or publication mutation.
"""
from pathlib import Path
from fractions import Fraction
from itertools import product, combinations
from collections import Counter, defaultdict
import ast, hashlib, json, math, re, stat

HERE = Path(__file__).resolve().parent
S = HERE / 'sources'
W = S / 'local-charge-observation-publication'
F = Fraction
def sha(raw): return hashlib.sha256(raw).hexdigest()
def read_json(p): return json.loads(p.read_text())
def freeze(x): return tuple(freeze(y) for y in x) if isinstance(x,list) else x
def leaves(x):
    if isinstance(x,dict): return sum(map(leaves,x.values()))
    if isinstance(x,list): return sum(map(leaves,x))
    return 1
def exact(x,y,path='$'):
    assert type(x) is type(y), (path,type(x),type(y))
    if isinstance(x,dict):
        assert x.keys()==y.keys(),path
        for k in x: exact(x[k],y[k],path+'.'+k)
    elif isinstance(x,list):
        assert len(x)==len(y),path
        for i,(a,b) in enumerate(zip(x,y)):exact(a,b,path+f'[{i}]')
    else: assert x==y,(path,x,y)
def signature(p):
    s=p.stat()
    return dict(sha256=sha(p.read_bytes()),bytes=s.st_size,mode=stat.S_IMODE(s.st_mode),
                mtime_ns=s.st_mtime_ns,ctime_ns=s.st_ctime_ns,inode=s.st_ino)

pins=read_json(HERE/'SOURCE_PINS.json')['members']
for row in pins:
    assert signature(Path(row['original']))=={k:row[k] for k in signature(Path(row['original']))},row['original']
    p=HERE/row['snapshot'];assert sha(p.read_bytes())==row['sha256'] and p.stat().st_size==row['bytes']

m=read_json(S/'LOCAL_CHARGE_OBSERVATION_FROZEN_SOURCES.json')
for rel,digest in m['files_sha256'].items():assert sha((W/rel).read_bytes())==digest,rel
seals=[]
for directory,name in [
 ('native-charge-current-noise-personal','AUTHOR_SEAL.json'),
 ('native-charge-current-noise-qualified','QUALIFICATION_SEAL.json'),
 ('native-charge-current-noise-independent','PRE_SEAL.json'),
 ('native-charge-current-noise-independent','POST_SEAL.json'),
 ('native-charge-finite-time-personal','AUTHOR_SEAL.json'),
 ('native-charge-finite-time-independent','PRE_SEAL.json'),
 ('native-charge-finite-time-independent','POST_SEAL.json')]:
    d=S/directory; seal=read_json(d/name)
    for row in seal['members']:
        p=d/row['path']; assert p.is_relative_to(d),row
        assert sha(p.read_bytes())==row['sha256'],str(p)
        if 'bytes' in row:assert p.stat().st_size==row['bytes']
    seals.append(dict(path=directory+'/'+name,sha256=sha((d/name).read_bytes()),
                      members=len(seal['members'])))

qdir=S/'native-charge-current-noise-qualified'
old46=(S/'native-charge-current-noise-personal/CHARGE_CURRENT_AND_INITIAL_COVARIANCE_ROOT.md').read_text()
qualified=(qdir/'CHARGE_CURRENT_AND_INITIAL_COVARIANCE_QUALIFIED.md').read_text()
old='Only for the separately supplied zero-field\nbasis vector does the expectation of that off-diagonal Hamiltonian current\nvanish.'
new='For the separately supplied zero-field basis vector, the expectation of\nthat off-diagonal Hamiltonian current vanishes; it need not vanish for\narbitrary field input.'
assert old46.count(old)==1 and old46.replace(old,new,1)==qualified
for row in read_json(qdir/'QUALIFICATION_SEAL.json')['sources']:
    rel=Path(row['path']).relative_to(HERE.parent); assert sha((S/rel).read_bytes())==row['sha256']

note=(W/m['note']).read_text();body_checks=[]
for source,changes in zip(m['source_notes'],m['presentation_replacements']):
    p=S/Path(source).relative_to(HERE.parent);body=p.read_text()
    for change in changes:
        assert body.count(change['old'])==1
        body=body.replace(change['old'],change['new'],1)
    body=re.sub(r'^(#{1,6}) ',lambda z:'#'*(len(z[1])+2)+' ',body,flags=re.M)
    assert note.count(body)==1
    body_checks.append(dict(source=str(p.relative_to(S)),source_sha256=sha(p.read_bytes()),
                           embedded_sha256=sha(body.encode()),replacements=len(changes),
                           first_line=note[:note.index(body)].count('\n')+1,
                           embedded_lines=len(body.splitlines())))

tree=ast.parse((W/m['runner']).read_text())
decl={n.targets[0].id:ast.literal_eval(n.value) for n in tree.body
      if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name)
      and n.targets[0].id in {'AUDIT_INPUT_PATHS','AUDIT_TIMEOUT_SEC','OUTPUT_DIRECTORY','RUNTIMES'}}
assert decl['AUDIT_INPUT_PATHS']==tuple([m['note'],*m['parent_paths'],*m['runtime']])
assert decl['RUNTIMES']==tuple(m['runtime']) and decl['AUDIT_TIMEOUT_SEC']==120
assert decl['OUTPUT_DIRECTORY']==m['output_directory']
comparisons=[]
for label,directory,program,rel in zip(('current','finite_time'),
 ('native-charge-current-noise-personal','native-charge-finite-time-personal'),
 ('current_noise_controls.py','local_support_controls.py'),m['runtime']):
    raw=(W/rel).read_bytes()
    assert raw==(S/directory/program).read_bytes()==(S/directory/'attempt01/source.py').read_bytes()
    old_data=read_json(S/directory/'attempt01/stdout.json')
    new_data=read_json(W/m['output_directory']/(label+'.stdout.json'))
    old_time=old_data.pop('elapsed_seconds');new_time=new_data.pop('elapsed_seconds')
    exact(old_data,new_data)
    assert (W/m['output_directory']/(label+'.stderr.txt')).read_bytes()==b''
    comparisons.append(dict(label=label,non_timing_scalar_leaves=leaves(new_data),
                            old_elapsed_seconds=old_time,new_elapsed_seconds=new_time,
                            strict_complete_non_timing_equality=True,
                            runtime_sha256=sha(raw)))

result_text=(W/m['result']).read_text();result=json.loads(result_text)
execution=read_json(S/'LOCAL_CHARGE_OBSERVATION_PRIMARY_EXECUTION.json')['execution']
assert execution['exit_code']==0 and execution['status']=='ok' and execution['stderr']==''
assert execution['stdout']==result_text+'TOTAL_PASS: 1\n'
assert result['source_sha256']==sha((W/m['runner']).read_bytes()) and result['all_assertions_passed'] is True
for rel in m['runtime']:assert result['runtime_sha256'][rel]==sha((W/rel).read_bytes())
for row in result['artifacts']:
    p=W/row['path'];assert sha(p.read_bytes())==row['sha256'] and p.stat().st_size==row['bytes']
    assert row['exit_code']==row['stderr_bytes']==0
    assert row['runtime_source_sha256']==comparisons[0 if row['label']=='current' else 1]['runtime_sha256']
fingerprint=hashlib.sha256(b'runner-cache-input-fingerprint-v1\0')
for rel in decl['AUDIT_INPUT_PATHS']:
    body=(W/rel).read_bytes();rb=rel.encode()
    fingerprint.update(len(rb).to_bytes(8,'big'));fingerprint.update(rb)
    fingerprint.update(len(body).to_bytes(8,'big'));fingerprint.update(body)
expected_cache=('===== runner cache v1 =====\nrunner: '+m['runner']+'\nrunner_sha256: '+result['source_sha256']+
 '\ninput_fingerprint_sha256: '+fingerprint.hexdigest()+
 f"\ntimeout_sec: {execution['timeout_sec']}\nexit_code: {execution['exit_code']}\nelapsed_sec: {execution['elapsed_sec']:.2f}\nstatus: {execution['status']}\n----- stdout -----\n"+
 execution['stdout']+'\n----- stderr -----\n'+execution['stderr']+'\n')
assert (W/m['cache']).read_text()==expected_cache

old_graph=read_json(HERE/'BASE_GRAPH.json');new_graph=read_json(W/'docs/audit/data/citation_graph_manifest.json')
cid=Path(m['note']).stem.lower()
parents=re.search(r'upstream_dependencies:\n(.*?)runner:',note,re.S)[1]
dependencies=re.findall(r'^  - (.+)$',parents,re.M)
assert dependencies==[Path(p).stem.lower() for p in m['parent_paths']]
assert set(new_graph['nodes'])-set(old_graph['nodes'])=={cid}
assert not set(old_graph['nodes'])-set(new_graph['nodes'])
assert all(new_graph['nodes'][k]==v for k,v in old_graph['nodes'].items())
assert new_graph['nodes'][cid]==dict(out_degree=3,deps_hash=sha('\n'.join(sorted(dependencies)).encode())[:12])
assert new_graph['node_count']==old_graph['node_count']+1==len(new_graph['nodes'])
assert new_graph['edge_count']==old_graph['edge_count']+3==sum(n['out_degree'] for n in new_graph['nodes'].values())
assert {k:v for k,v in old_graph.items() if k not in {'nodes','node_count','edge_count'}}=={k:v for k,v in new_graph.items() if k not in {'nodes','node_count','edge_count'}}
failure=read_json(S/'local-charge-observation-publication-history/PREMATURE_GRAPH_DEPENDENCY_FAILURE.json')
assert failure['source_sha256']==sha((S/'local-charge-observation-publication-history/verify_publication_attempt01.py').read_bytes())
assert failure['exit_code']==1 and failure['failed_before_science_or_manifest_mutation'] is True

# Reconstruct every current-control row from the stated finite geometries.
# These are released-source consistency checks, not a new blinded derivation.
current=read_json(W/m['output_directory']/'current.stdout.json')
pre46=read_json(S/'native-charge-current-noise-independent/primitive_attempt01/stdout.json')
star_pre={g['degree']:{(r['mark'],r['hop'],r['sign_at_A']):r for r in g['branches']} for g in pre46['star_initial']}
by_graph=defaultdict(list)
for row in current['primitive_rows']:by_graph[row['graph']].append(row)
current_groups=[]
for g in current['graph_summaries']:
    name=g['graph'];L=int(name[5:]) if name.startswith('torus') else None
    if L:
        xyz=list(product(range(L),repeat=3));A={i for i,p in enumerate(xyz) if sum(p)%2==0}
        edges=[(a,b) for a in sorted(A) for b in range(len(xyz)) if b not in A and
               sum(min(abs(x-y),L-abs(x-y)) for x,y in zip(xyz[a],xyz[b]))==1]
    else:
        xyz=[(i,0,0) for i in range(7 if name=='path7' else 5)]
        A={0,2,4,6} if name=='path7' else {0,1}
        edges=[(a,b) for a in sorted(A) for b in range(len(xyz)) if b not in A and (abs(a-b)==1 if name=='path7' else True)]
    n=len(xyz);near={a:[b for u,b in edges if u==a] for a in A};ei={e:i for i,e in enumerate(edges)}
    assert g['edges']==[list(e) for e in edges] and g['vertices']==n and g['A']==len(A)
    tests=[[1]*n,[int(i==0) for i in range(n)],[x-2*y+3*z for x,y,z in xyz],[1 if i in A else -1 for i in range(n)]]
    if L==4:tests.extend([[(1,0,-1,0)[x] for x,y,z in xyz],[(0,-1,0,1)[x] for x,y,z in xyz]])
    elif L==6:tests.extend([[(-1)**x for x,y,z in xyz],[0]*n])
    else:tests.extend([[i%3 for i in range(n)],[i%5 for i in range(n)]])
    coverage={(a,b,c,s) for a in A for b in near[a] for c in near[a] if c!=b for s in (-1,1)}
    seen=set();mean=[0]*6;cov=[[0]*6 for _ in range(6)];drift=[0]*n;edrift=[0]*len(edges)
    matter_by_edge=defaultdict(set)
    for r in by_graph[name]:
        a,b,c,s=r['a'],r['b'],r['c'],r['sigma'];key=(a,b,c,s)
        assert key in coverage and key not in seen;seen.add(key)
        dq={a:s-1,b:-s,c:1};dq={i:v for i,v in dq.items() if v}
        de={ei[a,b]:s,ei[a,c]:-1}
        assert r['delta_q']==[[i,v] for i,v in sorted(dq.items())]
        assert r['delta_E']==[[i,v] for i,v in sorted(de.items())]
        divergence=[0]*n
        for e,v in de.items():u,w=edges[e];divergence[u]+=v;divergence[w]-=v;edrift[e]+=v
        assert divergence==[dq.get(i,0) for i in range(n)] and sum(divergence)==0
        q=tuple(int(i in A)+dq.get(i,0) for i in range(n))
        assert all(v in (-1,0,1) for v in q) and all(q[i]!=0 for i in A)
        assert sum(abs(v) for v in q)==len(A)+2 and sum(q)==len(A)
        assert q not in matter_by_edge[a,b];matter_by_edge[a,b].add(q)
        local=star_pre[len(near[a])][near[a].index(b)+1,near[a].index(c)+1,s]
        assert local['charge_change']==[dq.get(i,0) for i in [a,*near[a]]]
        assert local['electric_shift']==[de.get(ei[a,v],0) for v in near[a]]
        values=[sum(f[i]*v for i,v in dq.items()) for f in tests];assert values==r['charge_tests']
        for i in range(n):drift[i]+=dq.get(i,0)
        for i in range(6):
            mean[i]+=values[i]
            for j in range(6):cov[i][j]+=values[i]*values[j]
    assert seen==coverage
    expected_mean=[2*sum((len(near[a])-1)*(f[b]-f[a]) for a,b in edges) for f in tests]
    expected_cov=[[4*sum((len(near[a])-1)*(f[b]-f[a])*(h[b]-h[a]) for a,b in edges) for h in tests] for f in tests]
    assert mean==expected_mean==g['initial_mean_slope_in_kappa']
    assert cov==expected_cov==g['initial_covariance_slope_in_kappa']
    assert [-x for x in edrift]==g['formation_current_in_kappa']==[2*(len(near[a])-1) for a,b in edges]
    assert drift==g['initial_charge_drift_in_kappa']
    assert g['mark_squared_norms']==[[a,b,len(matter_by_edge[a,b]),len(near[a])-1,2*(len(near[a])-1)] for a,b in edges]
    assert g['primitive_rows']==len(coverage)==g['total_first_event_rate_in_kappa']
    fourier=g['Fourier']
    if fourier:
        full=cov[4][4]+cov[5][5]
        assert full==fourier['full_initial_second_moment_slope_in_kappa']
        assert full/n==fourier['site_normalized_slope_in_kappa']==40*(1 if L==4 else 2)
    current_groups.append(dict(graph=name,vertices=n,edges=len(edges),branches=len(coverage),
                               means=mean,covariance=cov,Fourier=fourier))
assert sum(g['branches'] for g in current_groups)==current['primitive_count']==8480
assert len(current_groups)*36==current['real_polarized_covariance_entries']==180

# Check complete PRE47 initial matrices, and exact row correspondence on L4/L6.
pre47=read_json(S/'native-charge-finite-time-independent/PRIMITIVE_RESULTS.json')
pre_comparisons=[]
for g in pre47['tori']:
    n=len(g['sites']);edge_set={tuple(e) for e in g['edges_oriented_A_to_B']}
    lap=[[0]*n for _ in range(n)];means=[0]*n
    for a,b in edge_set:
        lap[a][a]+=20;lap[b][b]+=20;lap[a][b]-=20;lap[b][a]-=20
        means[a]-=10;means[b]+=10
    for instrument in ('resolved','coherent'):
        r=g['instruments'][instrument]
        assert r['covariance_slope_in_kappa']==lap and r['mean_slope_in_kappa']==means
        assert r['initial_gain_norm']==2*len(edge_set)*5
    assert g['instruments']['plus_only_mutant']['covariance_slope_in_kappa']!=lap
    rows={(r['a'],r['b'],r['c'],r['sigma']):r for r in by_graph['torus'+str(g['L'])]}
    assert len(rows)==len(g['primitive_rows'])
    for r in g['primitive_rows']:
        q=rows[r['a'],r['b'],r['c'],r['sign']]
        assert q['delta_q']==r['delta_q'] and q['delta_E']==r['field']
    pre_comparisons.append(dict(L=g['L'],branches=len(rows),full_covariance_entries_each=n*n,instruments=2,plus_only_rejected=True))
coherence=pre46['coherent_field_magnetic_current']
assert any(x!=[0,0] for x in coherence['mean_current_numerator_over_delta'])

# Rebuild every global support from common-B incidence, not the primary's
# local-center search. Compare entire saved lists, then exact rational bounds.
finite=read_json(W/m['output_directory']/'finite_time.stdout.json');geometry_rows=[]
total_atoms=0;total_groups=0
for g in finite['graphs']:
    L=g['L'];sites=list(product(range(L),repeat=3));A=[x for x in sites if sum(x)%2==0]
    def nbr(x):
        return sorted({tuple((x[j]+d)%L if j==i else x[j] for j in range(3)) for i in range(3) for d in (-1,1)})
    stars={a:frozenset([('s',*a),*[('s',*b) for b in nbr(a)],*[('e',*a,*b) for b in nbr(a)]]) for a in A}
    supports={('f',a):st for a,st in stars.items()}
    pairs={tuple(sorted((a,c))) for b in sites if sum(b)%2 for a,c in combinations(nbr(b),2)}
    for a,c in pairs:supports['h',a,c]=stars[a]|stars[c]
    touching=defaultdict(set)
    for group,support in supports.items():
        for atom in support:touching[atom].add(group)
    electric=defaultdict(set)
    for a in A:
        for b in nbr(a):
            triple={('s',*a),('s',*b),('e',*a,*b)}
            for atom in triple:electric[atom].update(triple)
    counts={};strength={};halo_strength={};out={}
    for label,r in g['sets'].items():
        X={freeze(v) for v in r['S']}
        G=set().union(*(touching[v] for v in X));X1=X|set().union(*(supports[v] for v in G))
        X2=X1|set().union(*(electric[v] for v in X1));G2=set().union(*(touching[v] for v in X2))
        for key,expected in [('X1',X1),('X2',X2),('groups',G),('halo_groups',G2)]:
            stored=[freeze(v) for v in r[key]]
            assert stored==sorted(expected),(L,label,key)
        def count(gs):return dict(formation=sum(x[0]=='f' for x in gs),magnetic=sum(x[0]=='h' for x in gs))
        c=count(G);h=count(G2);assert c==r['counts'] and h==r['halo_counts']
        counts[label]=(c,h);strength[label]=(5184*c['magnetic'],600*c['formation'])
        halo_strength[label]=(5184*h['magnetic'],600*h['formation'])
        assert list(strength[label])==r['J_coefficients'] and list(halo_strength[label])==r['J_halo_coefficients']
        total_atoms+=len(X)+len(X1)+len(X2);total_groups+=len(G)+len(G2)
        out[label]=dict(counts=c,halo_counts=h,X1=len(X1),X2=len(X2))
    def mul(p,q):return [F(p[0]*q[0]),F(p[0]*q[1]+p[1]*q[0]),F(p[1]*q[1])]
    M={}
    for key,l,r,scale in [('AA','A','A',4),('BB','B','B',1),('AB','A','B',2)]:
        support=l if l==r else 'AB'
        term1=mul(strength[support],halo_strength[support]);term2=mul(strength[l],strength[r])
        M[key]=[scale*(a/2+b) for a,b in zip(term1,term2)]
        assert [str(x) for x in M[key]]==g['M'][key]
    assert g['means_in_kappa']==['-60','60'] and g['covariance_in_kappa']==[['120','-20'],['-20','120']]
    mab=sum(M['AB']);mbb=sum(M['BB']);t=min(F(120)/(60*mab+11*mbb),F(60)/mbb)
    denom=120-t*mbb;error=t*(mab+mbb/6)/denom;illustration=g['illustrative_delta_kappa_equal_one']
    assert str(t)==illustration['max_time_for_bound_one_over_sixty']
    assert str(denom)==illustration['denominator'] and denom>0
    assert str(error)==illustration['ratio_error_bound'] and error<=F(1,60)
    assert float(t)==illustration['decimal_time']
    geometry_rows.append(dict(L=L,global_formation_groups=len(A),global_magnetic_pairs=len(pairs),
                              local_sets=out,M={k:[str(x) for x in v] for k,v in M.items()},
                              rational_time=str(t),positive_denominator=str(denom),error=str(error)))

# The tree evidence is retained PRE data, not a new numerical evolution.
t=read_json(S/'native-charge-finite-time-independent/TREE_RESULTS.json')
assert t['A']==[0,1] and t['edges_A_to_B']==[[0,2],[0,3],[0,4],[1,4],[1,5]]
assert len(t['full_charge_words'])==90 and len(t['P_charge_words'])==40 and set(t['number'])=={2,4,6}
assert t['P_charge_words'][t['initial_P_index']]==[1,1,0,0,0,0]
assert len(t['finite_time_rows'])==24
for r in t['finite_time_rows']:
    assert r['number_probabilities']['6']>0
    assert abs(sum(r['number_probabilities'].values())-1)<1e-12
    assert abs(r['covariance'][0][2]/math.sqrt(r['covariance'][0][0]*r['covariance'][2][2])-r['pearson_0_2'])<1e-12
tree_summary=dict(A=2,B=4,full_dimension=90,P_dimension=40,number_sectors=[2,4,6],
                  finite_time_rows=24,minimum_N6_probability=min(r['number_probabilities']['6'] for r in t['finite_time_rows']),
                  numerical_evolution_rerun=False,historical_A3_B3_capacity_floor=(6-3)//2,
                  ratio_definitions_distinct=True)
for row in pins:
    assert signature(Path(row['original']))=={k:row[k] for k in signature(Path(row['original']))},row['original']

report=dict(scope='NEW released-source recovery comparison; not original-reviewer final approval, not a blinded derivation, and not an audit.',
 sealed_records=seals,source_files_matched=len(m['files_sha256']),original_files_unchanged=len(pins),
 qualified46_exact_single_prose_repair=True,canonical_embedded_bodies=body_checks,
 complete_fresh_publication_vs_author_outputs=comparisons,
 cache=dict(identity='fresh',input_fingerprint_sha256=fingerprint.hexdigest(),entire_cache_and_execution_result_equal=True),
 graph=dict(old_nodes=old_graph['node_count'],new_nodes=new_graph['node_count'],old_edges=old_graph['edge_count'],
            new_edges=new_graph['edge_count'],unchanged_old_nodes=len(old_graph['nodes']),new_node=cid,dependencies=dependencies),
 prior_failed_graph_write=dict(record_sha256=sha((S/'local-charge-observation-publication-history/PREMATURE_GRAPH_DEPENDENCY_FAILURE.json').read_bytes()),
                              failed_verifier_hash_bound=True,execution_repeated=False),
 current_controls=current_groups,PRE47_correspondence=pre_comparisons,
 PRE46_nonzero_coherent_field_current=coherence,finite_time_geometry=geometry_rows,
 stored_atom_occurrences_compared=total_atoms,stored_group_occurrences_compared=total_groups,
 PRE47_tree_scope=tree_summary,
 incomplete_publication_reviews_used_as_completed_evidence=False,
 limitations='Proof and premise assessment is in REPORT.md. Large raw arrays are mechanically checked, not all manually read. No author code, old writer, numerical propagator, or pipeline was executed.')
print(json.dumps(report,indent=2,sort_keys=True,allow_nan=False))
