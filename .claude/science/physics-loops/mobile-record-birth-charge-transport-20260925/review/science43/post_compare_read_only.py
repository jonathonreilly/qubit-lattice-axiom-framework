"""POST43: new, genuinely read-only released-evidence comparator.

No local scientific module is imported or executed.  Charge deviations from
the all-A-plus background and coordinate-indexed sparse fields reconstruct the
175 retained target rows.  Complete author rows are compared, not sampled.
Existing independent PRE vectors provide a separate stored-data comparison.
"""
from pathlib import Path
from hashlib import sha256
from itertools import product, combinations
from collections import Counter
from fractions import Fraction
import ast
import json

HERE = Path(__file__).resolve().parent
AUTHOR = HERE / 'post_sources' / 'author'


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def observed(path):
    st=path.stat()
    raw=path.read_bytes()
    return dict(path=str(path),sha256=sha256(raw).hexdigest(),bytes=len(raw),
                dev=st.st_dev,ino=st.st_ino,mode=st.st_mode,
                mtime_ns=st.st_mtime_ns,ctime_ns=st.st_ctime_ns,nlink=st.st_nlink)


def background(vertex):
    return int(sum(vertex)%2==0)


def neighbors(vertex,L):
    ans=set()
    for axis in range(3):
        for step in (-1,1):
            w=list(vertex);w[axis]=(w[axis]+step)%L;ans.add(tuple(w))
    return sorted(ans)


def freeze(q,e):
    return tuple(sorted((x,v) for x,v in q.items() if v)),tuple(sorted((x,v) for x,v in e.items() if v))


def hop(state,A,B,outward):
    q,e=map(dict,state)
    source,destination=(A,B) if outward else (B,A)
    charge=background(source)+q.get(source,0)
    if not charge or background(destination)+q.get(destination,0):return None
    q[source]=q.get(source,0)-charge
    q[destination]=q.get(destination,0)+charge
    e[A,B]=e.get((A,B),0)+(-charge if outward else charge)
    return freeze(q,e)


def initial(a,b,c,sigma):
    return freeze({a:sigma-1,b:-sigma,c:1},{(a,b):sigma,(a,c):-1})


def sparse(state):
    q,e=state
    return dict(delta_q=[[list(x),v] for x,v in q],
                electric=[[list(x),list(y),v] for (x,y),v in e])


def check_gauss(state):
    q,e=state;div=Counter()
    for (a,b),v in e:div[a]+=v;div[b]-=v
    assert {x:v for x,v in div.items() if v}==dict(q)
    assert all(background(x)+v in (-1,0,1) for x,v in q)


def from_author(row,V,edges):
    assert len(row['q'])==len(V) and len(row['E'])==len(edges)
    assert all(type(v) is int and v in (-1,0,1) for v in row['q'])
    assert all(type(v) is int for v in row['E'])
    state=freeze({x:v-background(x) for x,v in zip(V,row['q'])},
                 {edge:v for edge,v in zip(edges,row['E'])})
    check_gauss(state)
    return state


def from_pre(row):
    q={tuple(x):1 for x in row['occupied_B']}
    for x in row['vacant_A']:q[tuple(x)]=-1
    for x in row['minus_locations']:q[tuple(x)]=-1-background(x)
    return freeze(q,{(tuple(x),tuple(y)):v for x,y,v in row['electric']})


def all_pair_paths(source,x,y,near,target):
    counts=Counter();matches=[]
    # A frontier of distinct primitive paths retains multiplicities and full
    # field words.  Equal intermediate states are never prematurely merged.
    frontier=[(source,[],[source])]
    for stage,(star,outward) in enumerate(((x,True),(y,True),(y,False),(x,False))):
        next_frontier=[]
        for state,moves,states in frontier:
            for B in near[star]:
                reached=hop(state,star,B,outward)
                if reached is None:continue
                counts[stage]+=1
                next_frontier.append((reached,moves+[(star,B,outward)],states+[reached]))
        frontier=next_frontier
    for reached,moves,states in frontier:
        if reached==target:matches.append((moves,states))
    return [counts[i] for i in range(4)],matches


def main():
    before=json.loads((HERE/'POST_PRESERVATION_BEFORE.json').read_text())
    for row in before['files']:assert observed(Path(row['path']))==row
    pins=json.loads((HERE/'POST_SOURCE_PINS.json').read_text())
    for row in pins['author_sources']:
        path=HERE/row['frozen_path']
        assert digest(path)==row['sha256'] and path.stat().st_size==row['bytes']
        assert observed(Path(row['origin']))==row['observed_origin']
    result_path=AUTHOR/'attempt01/RESULT.json'
    assert result_path.read_bytes()==(AUTHOR/'attempt01/stdout.log').read_bytes()
    assert (AUTHOR/'attempt01/stderr.log').read_bytes()==b''
    source=AUTHOR/'cluster_escape_controls.py'
    helper=AUTHOR/'birth_geometry.py'
    assert source.read_bytes()==(AUTHOR/'attempt01/cluster_escape_controls.py').read_bytes()
    data=json.loads(result_path.read_text())
    receipt=json.loads((AUTHOR/'attempt01/EXECUTION.json').read_text())
    root_read=json.loads((AUTHOR/'ROOT_READ_RECEIPT.json').read_text())
    assert data['source_sha256']==receipt['source_sha256']==digest(source)
    assert data['personal42_helper_sha256']==digest(helper)
    assert receipt['exit_code']==0 and receipt['stderr_bytes']==0
    assert root_read['primary_result_sha256']==digest(result_path)
    assert root_read['primary_external_seconds']==receipt['elapsed_seconds']==0.1268903750460595
    assert data['elapsed_seconds']==0.08149287500418723
    ast_bindings=[]
    for p in (source,helper,AUTHOR/'attempt01/cluster_escape_controls.py'):
        tree=ast.parse(p.read_text())
        ast_bindings.append(dict(path=str(p.relative_to(HERE)),sha256=digest(p),
            functions=[n.name for n in tree.body if isinstance(n,ast.FunctionDef)],
            imports=[ast.unparse(n) for n in tree.body if isinstance(n,(ast.Import,ast.ImportFrom))]))

    payloads=[];row_count=0;path_count=0;gauss_states=0;pre_lookup_counts=[]
    for data_row in data['results']:
        L=data_row['L'];assert L in (4,6)
        V=list(product(range(L),repeat=3));index={x:i for i,x in enumerate(V)}
        A=[x for x in V if background(x)];near={x:neighbors(x,L) for x in A}
        edges=[(x,y) for x in A for y in near[x]]
        assert data_row['vertices']==[list(x) for x in V]
        assert data_row['A_sites']==[index[x] for x in A]
        assert data_row['oriented_edges']==[[index[x],index[y]] for x,y in edges]
        a,b,c,d,u,v=(0,0,0),(L-1,0,0),(0,L-1,0),(1,1,0),(1,0,0),(0,1,0)
        assert data_row['named_sites']==dict(zip(('a','b','c','d','u','v'),map(index.get,(a,b,c,d,u,v))))
        source_minus=initial(a,b,c,-1)
        assert from_author(data_row['actual_selected_birth_source'],V,edges)==source_minus
        target=source_minus
        for x,y,outward in ((a,u,True),(d,v,True),(d,u,False),(a,v,False)):
            target=hop(target,x,y,outward);assert target is not None;check_gauss(target)
        assert from_author(data_row['target'],V,edges)==target
        target_delta=dict(target[0]);assert target_delta=={d:-2,b:1,c:1}
        distances=[sum(min((p-q)%L,(q-p)%L) for p,q in zip(d,B)) for B in (b,c)]
        assert distances==data_row['target_distances_to_positive_B']==[3,3]
        allpairs=[(x,y) for x,y in combinations(A,2) if set(near[x])&set(near[y])]
        stored={}
        for row in data_row['all_relevant_pair_rows']:
            key=(row['sigma'],V[row['birth_outward']],tuple(V[i] for i in row['pair']))
            assert key not in stored;stored[key]=row
        expected_keys=set();render_rows=[];matches=[];H=Counter();Gamma=Counter();inputs=[]
        for sign in (-1,1):
            for outgoing in near[a]:
                if outgoing==b:continue
                initial_state=initial(a,b,outgoing,sign);check_gauss(initial_state);inputs.append(initial_state)
                changed={x for x in A if dict(initial_state[0]).get(x,0)!=target_delta.get(x,0)}
                candidates=[p for p in allpairs if changed<=set(p)]
                for x,y in candidates:
                    key=(sign,outgoing,(x,y));expected_keys.add(key)
                    row=stored[key]
                    counts,found=all_pair_paths(initial_state,x,y,near,target)
                    labels=('first_outward','second_outward','first_return','second_return')
                    assert row['legal_path_counts']==dict(zip(labels,counts))
                    assert row['target_Gram_coefficient']==len(found)
                    H[sign]-=2*len(found)
                    render_rows.append([sign,list(outgoing),[list(x),list(y)],*counts,len(found)])
                    for moves,states in found:
                        for state in states:check_gauss(state)
                        matches.append(dict(sigma=sign,birth_outward=index[outgoing],
                            outward=[index[z] for z in (moves[0][0],moves[0][1],moves[1][0],moves[1][1])],
                            **{'return':[index[z] for z in (moves[2][0],moves[2][1],moves[3][0],moves[3][1])]},
                            states=states))
                # Independent original-loss contraction: post-outward empty
                # B neighbors give G_x; each sign contributes one Kraus norm.
                for star in A:
                    if not changed<={star}:continue
                    for B in near[star]:
                        middle=hop(initial_state,star,B,True)
                        if middle is None:continue
                        vacancies=sum(background(z)+dict(middle[0]).get(z,0)==0 for z in near[star])
                        for returning in near[star]:
                            if hop(middle,star,returning,False)==target:Gamma[sign]+=2*vacancies
        assert set(stored)==expected_keys
        assert len(inputs)==len(set(inputs))==10
        assert data_row['birth_squared_norms']==dict(resolved_minus=5,resolved_plus=5,coherent=10)
        assert {str(s):H[s] for s in (-1,1)}==data_row['H4_target_numerators_before_birth_normalization']=={'-1':-4,'1':0}
        assert {str(s):Gamma[s] for s in (-1,1)}==data_row['Gamma_target_numerators_in_kappa']=={'-1':0,'1':0}
        coefficients=dict(resolved_minus=str(Fraction(H[-1]**2,5)),resolved_plus=str(Fraction(H[1]**2,5)),
                          coherent=str(Fraction((H[-1]+H[1])**2,10)))
        assert coefficients==data_row['exact_initial_target_probability_coefficients_in_delta_squared']
        assert data_row['all_integer_Gauss_and_coefficient_assertions'] is True
        assert len(matches)==len(data_row['all_matching_primitive_paths'])==2
        sparse_matches=[]
        for calculated,saved in zip(matches,data_row['all_matching_primitive_paths']):
            assert {k:v for k,v in calculated.items() if k!='states'}=={k:v for k,v in saved.items() if k!='states'}
            decoded=[from_author(s,V,edges) for s in saved['states']]
            assert decoded==calculated['states']
            assert decoded[0]==source_minus and decoded[-1]==target
            gauss_states+=len(decoded)
            sparse_matches.append(dict(sigma=saved['sigma'],birth_outward=V[saved['birth_outward']],
                outward=[V[i] for i in saved['outward']],**{'return':[V[i] for i in saved['return']]},
                states=[sparse(s) for s in decoded]))
        pre=json.loads((HERE/('L'+str(L)+'_RESULTS.json')).read_text())
        assert pre['source_sha256']==digest(HERE/'primitive_transport.py')
        def coefficient(rows):
            lookup=[r['coefficient'] for r in rows if from_pre(r)==target]
            assert len(lookup)<=1
            return sum(lookup)
        lookups=[]
        for r in pre['resolved']:
            h=coefficient(r['QH4_rows']);loss=coefficient(r['loss_rows'])
            assert h==H[r['initial_sign']] and loss==Gamma[r['initial_sign']]
            lookups.append(dict(sign=r['initial_sign'],QH4=h,loss_over_kappa=loss))
        assert coefficient(pre['coherent']['QH4_rows'])==H[-1]+H[1]
        checked_rows=sum(len(r['QH4_rows'])+len(r['loss_rows']) for r in pre['resolved'])+len(pre['coherent']['QH4_rows'])
        pre_lookup_counts.append(dict(L=L,stored_PRE_rows_consumed_for_target_lookup=checked_rows,
                                     resolved=lookups,coherent_QH4=-4))
        payloads.append(dict(L=L,vertices=len(V),oriented_edges=len(edges),retained_pair_rows=len(render_rows),
            row_columns=['sign','outgoing_B','A_pair','first_out','second_out','first_return','second_return','target_Gram'],
            complete_pair_rows=render_rows,complete_matched_paths=sparse_matches,
            source=sparse(source_minus),target=sparse(target),coefficients=coefficients,
            original_loss_target_numerators={str(s):Gamma[s] for s in (-1,1)},
            target_distances=distances))
        row_count+=len(render_rows);path_count+=len(matches)
    assert row_count==175 and path_count==4 and gauss_states==20
    assert root_read['counts']==[dict(L=4,complete_relevant_rows=80,complete_matched_paths=2),
                                 dict(L=6,complete_relevant_rows=95,complete_matched_paths=2)]
    for row in before['files']:assert observed(Path(row['path']))==row
    for row in pins['author_sources']:assert observed(Path(row['origin']))==row['observed_origin']
    return dict(scope='Released-source POST43, no author import/execution; coordinate-sparse target reconstruction and prior sealed-data correspondence.',
        source_sha256=digest(Path(__file__)),author_source_AST_inventory=ast_bindings,
        complete_author_pair_rows_checked=row_count,complete_author_matching_paths_checked=path_count,
        full_matched_dense_Gauss_states_checked=gauss_states,
        prior_PRE_target_lookups=pre_lookup_counts,preserved_PRIOR_files=len(before['files']),
        author_source_result_execution_bindings=True,author_stdout_exact_result_bytes=True,
        author_unchanged=True,old_sealed_writers_executed=False,author_scientific_programs_imported_or_executed=False,
        author_reported_external_elapsed=receipt['elapsed_seconds'],author_reported_internal_elapsed=data['elapsed_seconds'],
        rows_and_paths=payloads)


if __name__=='__main__':
    print(json.dumps(main(),separators=(',',':')))
