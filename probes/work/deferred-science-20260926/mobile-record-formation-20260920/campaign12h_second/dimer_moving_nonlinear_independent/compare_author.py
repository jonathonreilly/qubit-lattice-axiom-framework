#!/usr/bin/env python3
"""Selective post-seal comparison; no author module imported or suite executed."""
from pathlib import Path
from fractions import Fraction as F
import datetime, hashlib, itertools, json, math
import numpy as np
from scipy.sparse import csr_matrix
import independent_check as own

HERE=Path(__file__).resolve().parent
RAW=HERE.parent

def row(path):
    data=path.read_bytes()
    return {'path':str(path),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}

def authenticate():
    seals=[]
    for filename in ['PRE_COMPARISON_SEAL.json','ADDENDUM_PRE_COMPARISON_SEAL.json']:
        seal=json.loads((HERE/filename).read_text())
        for r in seal['sources']+seal['artifacts']:
            assert row(Path(r['path']))==r,r['path']
        seals.append({'seal':row(HERE/filename),'authenticated_rows':len(seal['sources'])+len(seal['artifacts'])})
    receipt=json.loads((HERE/'AUTHOR_SOURCE_RECEIPT.json').read_text())
    for r in receipt['sources']:assert row(Path(r['path']))==r,r['path']
    result=json.loads((RAW/'dimer_moving_nonlinear_checks/RESULTS.json').read_text())
    for r in result['sources']:assert row(Path(r['path']))==r,r['path']
    assert row(RAW/'dimer_moving_nonlinear_check.py')['sha256']=='2000fcf382ab9eeb833d8d67d608776017a37c9848c29263dee32c06f5038052'
    assert row(RAW/'dimer_moving_nonlinear_checks/RESULTS.json')['sha256']=='9248bcdc11b78f955d90ea0710bc228ce37b4d1ab38eb6037024d0301ef30cc0'
    finalrun=json.loads((RAW/'DIMER_MOVING_NONLINEAR_RUN_RECEIPT.json').read_text())
    assert finalrun['returncode']==0 and finalrun['script_sha256']==row(RAW/'dimer_moving_nonlinear_check.py')['sha256']
    assert (RAW/'DIMER_MOVING_NONLINEAR_RUN.stderr').read_bytes()==b''
    assert (RAW/'DIMER_MOVING_NONLINEAR_RUN.log').read_text()=='three_moving_nonlinear_control_groups_complete\n'
    return result,{'pre_seals':seals,'author_files_authenticated':len(receipt['sources']),'embedded_author_bindings':len(result['sources'])}

def entropy_recompute(expected):
    q=14;d=q*q;nu=1/3
    a,b=np.divmod(np.arange(d),q);permutation=q*b+a
    rr=[];cc=[];vv=[]
    for M in range(2):
        for x in range(d):
            for y in [x,int(permutation[x])]:rr.append(M*d+x);cc.append((1-M)*d+y);vv.append(nu)
            rr.append(M*d+x);cc.append(M*d+x);vv.append(-2*nu)
    Q=csr_matrix((vv,(rr,cc)),shape=(2*d,2*d))
    weights=np.array([[1+int((aa+3*bb)**2%29) for aa,bb in zip(a,b)],
                      [2+int((5*aa+bb)**2%31) for aa,bb in zip(a,b)]],float)
    conditional=weights/weights.sum(axis=1)[:,None];rho=np.array([.9,.1])
    mu=(rho[:,None]*conditional).ravel();dm=Q.T@mu;dr=dm.reshape(2,d).sum(axis=1)
    reference=np.repeat(rho/d,d)
    derivative=float(dm@np.log(mu/reference)-np.sum(mu*np.repeat(dr/rho,d)))
    joint=float(dm@np.log(mu*2*d));marginal=float(dr@np.log(rho*2))
    def H(state):
        prob=state.reshape(2,d);r=prob.sum(axis=1)
        return float(np.sum(prob*np.log(prob/(r[:,None]/d))))
    vals={'conditional_entropy_derivative':derivative,'joint_uniform_entropy_derivative':joint,
          'geometry_uniform_entropy_derivative':marginal,'before':H(mu),'after_Euler_channel':H(mu+.001*dm)}
    errors={k:abs(v-expected[k]) for k,v in vals.items()}
    assert max(errors.values())<3e-15
    assert abs(derivative-(joint-marginal))<3e-15
    reference_error=float(np.max(abs(Q.T@reference-np.repeat(dr/d,d))))
    assert reference_error<2e-17
    rate=nu*(1+(a==0).astype(int)+(b==0).astype(int))
    # Independently create the color-dependent row generator by source rates.
    bad=Q.multiply(np.tile(rate/nu,2)[:,None]).tocsr()
    dep_dm=bad.T@reference;dep_dr=dep_dm.reshape(2,d).sum(axis=1)
    residual=float(np.max(abs(dep_dm-np.repeat(dep_dr/d,d))))
    dependentH=H(reference+.001*dep_dm)
    assert abs(residual-expected['color_dependent_countercontrol']['reference_derivative_residual'])<2e-17
    assert abs(dependentH-expected['color_dependent_countercontrol']['conditional_entropy_after'])<3e-15
    return {'states':2*d,'recomputed':vals,'maximum_saved_value_error':max(errors.values()),
            'reference_equation_residual':reference_error,'autonomy_countercontrol_residual':residual,
            'autonomy_countercontrol_conditional_entropy':dependentH}

def fixture(N,seed,attempts,winding=False):
    M=own.Matching(N)
    if winding:
        for u in itertools.product(range(N),repeat=3):
            if sum(u)%2:continue
            v=M.canon(np.array(u)+[1,0,0]);M.changed[u]=v;M.changed[v]=u
    rng=np.random.default_rng(seed)
    for _ in range(attempts):
        flat=int(rng.integers(N**3));x=(flat//(N*N),(flat//N)%N,flat%N)
        i,j=rng.choice(3,size=2,replace=False);M.flip(x,int(i),int(j))
    for u in itertools.product(range(N),repeat=3):
        assert M.partner(M.partner(u))==u and np.sum(abs(M.disp(M.partner(u),u)))==1
    return M

def blocks_recompute(rows):
    output=[]
    for expected,seed,attempts in zip(rows,[11,37,53],[0,12**3*8,16**3*8]):
        N,L=expected['N'],expected['L'];M=fixture(N,seed,attempts,winding=not attempts)
        assert M.flips==expected['accepted_geometry_flips']
        assert expected['all_origins']==N**3
        assert expected['exact_anchor_coverage']==L**3+L**2
        assert expected['exact_physical_edge_coverage']==L**3-L**2
        selected=[]
        for saved in expected['selected']:
            z=saved['origin'];origin=(z//(N*N),(z//N)%N,z%N)
            sites,B=own.block(M,origin,L);m=len(B);T2=np.zeros((3,3),dtype=int);boundary=[]
            graph={u:set() for u in B}
            for delta0 in own.DELTAS:
                delta=np.array(delta0);image={M.q(u,delta) for u in B};boundary.append(len(image^B))
                for u in B:T2+=np.outer(M.disp(M.q(u,delta),u),delta)
            for r in itertools.product(range(L),repeat=3):
                u=np.array(origin)+r
                for axis in range(3):
                    if r[axis]==L-1:continue
                    v=u+np.eye(3,dtype=int)[axis];x,y=M.owner(u),M.owner(v)
                    if x!=y:graph[x].add(y);graph[y].add(x)
            seen={next(iter(B))};todo=list(seen)
            while todo:
                for u in graph[todo.pop()]:
                    if u not in seen:seen.add(u);todo.append(u)
            assert seen==B
            residual=(T2-2*m*np.eye(3,dtype=int)).tolist()
            assert m==saved['block_count'] and residual==saved['twice_tensor_residual']
            assert boundary==saved['six_image_boundary_counts'] and saved['connected']
            selected.append({'origin':z,'block_count':m,'twice_tensor_residual':residual,'six_image_boundary_counts':boundary})
        output.append({'N':N,'L':L,'accepted_fixture_flips':M.flips,'selected':selected})
    return output

def failed_fixture_and_constants(expected):
    olddir=RAW/'dimer_moving_nonlinear_development/frozen_winding_fixture'
    old=(olddir/'dimer_moving_nonlinear_check.py').read_text();new=(RAW/'dimer_moving_nonlinear_check.py').read_text()
    removed=' partner=np.empty(V,dtype=int);partner[black]=nn[black,0];partner[partner[black]]=black\n'
    inserted=' partner=np.empty(V,dtype=int)\n if attempts:\n  evenx=np.flatnonzero(coords[:,0]%2==0);partner[evenx]=nn[evenx,0];partner[partner[evenx]]=evenx\n else:\n  partner[black]=nn[black,0];partner[partner[black]]=black\n'
    assert old.count(removed)==1
    reconstructed=old.replace(removed,inserted).replace('  flips+=1\n','  flips+=1\n assert (not attempts or flips>0)\n')
    assert reconstructed==new
    diagnosis=json.loads((olddir/'DIAGNOSIS.json').read_text())
    assert diagnosis['old_sha256']==row(olddir/'dimer_moving_nonlinear_check.py')['sha256']
    assert diagnosis['new_sha256']==row(RAW/'dimer_moving_nonlinear_check.py')['sha256']
    run=json.loads((olddir/'DIMER_MOVING_NONLINEAR_RUN_RECEIPT.json').read_text())
    assert run['returncode']==1 and run['script_sha256']==diagnosis['old_sha256']
    assert 'AssertionError: rough matching must exhibit a nonzero finite-block tensor boundary term' in (olddir/'DIMER_MOVING_NONLINEAR_RUN.stderr').read_text()
    frozen=fixture(12,37,12**3*8,winding=True);assert frozen.flips==0
    # No mathematical assertion, tested size, seed, or threshold changed.
    constant_rows=[];alpha=F(1,1792)
    assert expected['alpha']==str(alpha)
    for r in expected['rows']:
        L=r['L'];chi=32*L**3;m=F(L**3,2)
        assert r['overlap_colors']==chi and r['overlap_degree_plus_one_bound']==(2*L+3)**3
        assert r['minimum_count']==str(m) and r['twice_alpha_chi']==str(2*alpha*chi)
        assert 2*alpha*chi==m/14 and r['maximum_omega']==str(F(L**3,L**3+L**2))
        constant_rows.append({'L':L,'alpha':str(alpha),'chi':chi,'largest_centered_exponent':str(2*alpha*chi)})
    return {'only_changes':'Attempted-flip fixture starts columnar instead of frozen winding; add accepted-flip assertion. All other bytes unchanged.',
            'preserved_failed_run_returncode':run['returncode'],'independently_replayed_old_fixture_accepted_flips':frozen.flips,
            'scope':'Old full suite not repeated; the failed route and exact source delta were checked.', 'exponential_constant_rows':constant_rows}

def main():
    saved,auth=authenticate();result={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'authentication':auth,
      'boundary':'Post-seal selective comparison. Independent proof/control packets preserved. No author module import, full suite, trajectory or PDE simulation.',
      'author_entropy':entropy_recompute(saved['geometry_entropy']),
      'author_selected_blocks':blocks_recompute(saved['owner_blocks']),
      'preserved_fixture_and_constants':failed_fixture_and_constants(saved['exponential_constants']),
      'unrepeated':'Full all-origin extrema/coverage author loops authenticated by source/results; selected block rows recomputed. General identities proved independently. No separate quantitative author checker exists.',
      'checker_sha256':row(Path(__file__))['sha256']}
    with (HERE/'COMPARISON_RESULTS.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    print('all bounded comparison groups complete',flush=True)

if __name__=='__main__':main()
