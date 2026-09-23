"""Post-PRE energy-filter comparison using only the frozen independent rules.

All new author controls are reconstructed at their parameters; neither the
author runner nor its inherited builders are imported or executed.
"""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction
from collections import defaultdict
import hashlib,json,math,difflib
import numpy as np
import scipy.linalg as la
import scipy.sparse as sparse
from scipy.sparse.linalg import spsolve,expm_multiply
import sympy as sy
from filter_controls import pb,fp,first_outputs,flat_hamiltonian,lift,HERE

AUTHOR=HERE.parent/'energy_selected_formation_author'
PRE_HASH='78c272d1e51b182c4bdd7f98072f7fafa9cad83e6280d7092df5f4449d5f3e65'
AUTHOR_HASH='e41fcf88533b5f708b83e9265e6c1ed218547bfce44e7226a550d90f9d1a8bde'
READS={}


def identity(path):
    path=Path(path).resolve();data=path.read_bytes()
    row={'path':str(path),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
    READS[str(path)]=row;return row


def authenticate(row):
    got=identity(row['path'])
    assert all(got[k]==row[k] for k in ('path','bytes','sha256')),row['path']


def json_objects(path):
    stream=Path(path).read_text();answer=[];decoder=json.JSONDecoder()
    while stream.strip():
        obj,end=decoder.raw_decode(stream.lstrip());answer.append(obj);stream=stream.lstrip()[end:]
    return answer


def sources():
    assert identity(HERE/'PRE_COMPARISON_SEAL.json')['sha256']==PRE_HASH
    pre=json.loads((HERE/'PRE_COMPARISON_SEAL.json').read_text())
    for row in pre['science_sources']+pre['instruction_snapshots']+pre['independent_artifacts']:authenticate(row)
    assert identity(AUTHOR/'AUTHOR_SEAL.json')['sha256']==AUTHOR_HASH
    author=json.loads((AUTHOR/'AUTHOR_SEAL.json').read_text())
    for row in author['sources']+author['artifacts']:authenticate(row)
    draft=json.loads((AUTHOR/'ANALYTIC_DRAFT_SEAL.json').read_text())
    # Author draft paths are repository-relative, and must retain their exact binding.
    raw=HERE.parent.parents[3]
    for row in [draft['artifact']]+draft['sources']:
        binding=dict(row);binding['path']=str(raw/row['path']);authenticate(binding)
    results={}
    streams={}
    for label,folder in [('current',AUTHOR),('preserved_first',AUTHOR/'first_control_run')]:
        result=json.loads((folder/'ENERGY_FILTER_RESULTS.json').read_text())
        receipt=json.loads((folder/'FILTER_CONTROL_RUN_RECEIPT.json').read_text())
        assert receipt['exit_code']==0
        assert receipt['runner_sha256']==result['source_sha256']==identity(folder/'energy_filter_check.py')['sha256']
        assert (folder/'FILTER_CONTROL.stderr.log').read_bytes()==b''
        objects=json_objects(folder/'FILTER_CONTROL.stdout.log')
        assert len(objects)==5 and objects[-1]==result
        assert objects[:-1]==result['numerical']['rows']
        results[label]=result;streams[label]={'objects_matched':5,'exit_code':0,'stderr_empty':True}
    before=results['preserved_first'];after=results['current']
    assert before['exact']==after['exact']
    for old,new in zip(before['numerical']['rows'],after['numerical']['rows']):
        assert {k:v for k,v in old.items() if k!='elapsed_seconds'}=={k:v for k,v in new.items() if k!='elapsed_seconds'}
    code_diff=''.join(difflib.unified_diff((AUTHOR/'first_control_run/energy_filter_check.py').read_text().splitlines(True),
                 (AUTHOR/'energy_filter_check.py').read_text().splitlines(True),
                 fromfile='preserved_first_run',tofile='current_author_runner'))
    (HERE/'AUTHOR_CONTROL_REPAIR_DIFF.txt').write_text(code_diff)
    return after,{'PRE_created_utc':pre['created_utc'],'author_analytic_draft_utc':draft['utc'],
                  'author_final_seal_utc':author['created_utc'],
                  'pre_unique_source_instruction_artifact_rows':54,'author_source_rows':8,'author_artifact_rows':14,
                  'author_streams':streams,'old_and_current_numerical_rows_identical_except_timing':True}


def laurent_cross(v,w):
    out=defaultdict(lambda:sy.Integer(0))
    for (q,f),a in v.items():
        for (r,g),b in w.items():
            if q==r:out[f-g]+=sy.conjugate(sy.sympify(a))*sy.sympify(b)
    return {f:sy.simplify(a) for f,a in out.items() if sy.simplify(a)!=0}


def exact_grams(expected):
    resolved=first_outputs(0);rows=[]
    for e in range(8):
        pair={sign:{state:sy.Rational(amp) for state,amp in resolved[e,sign].items()} for sign in (-1,1)}
        both=defaultdict(lambda:sy.Integer(0),pair[-1])
        for state,amp in pair[1].items():both[state]+=amp
        pair[None]=dict(both)
        projected={sign:fp.project(v) for sign,v in pair.items()}
        for sign in (-1,1,None):
            n=2 if sign is None else 1
            assert laurent_cross(pair[sign],pair[sign])=={0:n}
            assert laurent_cross(projected[sign],projected[sign])=={0:sy.Rational(n,2)}
            assert fp.project(projected[sign])==projected[sign]
            rows.append({'edge':e,'sign':sign,'unfiltered_Gram':n,'filtered_Gram':str(sy.Rational(n,2)),
                         'projected_output_terms':len(projected[sign])})
        assert laurent_cross(pair[1],projected[-1])=={}
    assert rows==expected['exact_Laurent_Grams_all_24_marks']
    return {'all_24_Laurent_Gram_rows_equal':True,'opposite_sign_cross_Grams_exactly_zero':True,
            'resolved_total':8,'coherent_total':8}


def physical_array(vector,basis):return np.array([complex(vector.get(state,0)) for state in basis])


def squared_distance(actual,basis,reference):
    overlap=np.vdot(actual,physical_array(reference,basis))
    return max(0.,float(np.vdot(actual,actual).real+sum(abs(v)**2 for v in reference.values())-2*overlap.real))


def reference_and_tails(expected):
    cut=24;K=.4;delta=.7;a=16.
    basis,H=flat_hamiltonian(cut,K,delta)
    seed=np.zeros(len(basis));seed[basis.index((1,1,1))]=1/np.sqrt(2)
    # Our b frame is minus the author's b frame. Their -b_(1,1) seed is ours +b_(1,1).
    source=first_outputs(0)[0,1]
    projected={s:complex(v) for s,v in fp.project(source).items()}
    assert all(abs(lift(seed,basis).get(s,0)-v)<1e-14 for s,v in projected.items())
    rm=spsolve(H-1j*a*sparse.eye(len(basis)),seed)
    rp=spsolve(H+1j*a*sparse.eye(len(basis)),seed)
    gvec=a*(rm-rp)/(2j);gphysical=lift(gvec,basis)
    interior=[float(np.linalg.norm((H-1j*a*sparse.eye(len(basis)))@rm-seed)),
              float(np.linalg.norm((H+1j*a*sparse.eye(len(basis)))@rp-seed))]
    larger,HL=flat_hamiltonian(cut+1,K,delta);li={s:i for i,s in enumerate(larger)}
    boundary=[]
    for sign,vec in [(1,rm),(-1,rp)]:
        extended=np.zeros(len(larger),complex)
        for s,v in zip(basis,vec):extended[li[s]]=v
        residual=(HL-sign*1j*a*sparse.eye(len(larger)))@extended
        inds=[i for i,s in enumerate(larger) if abs(s[2])>cut]
        boundary.append(float(np.linalg.norm(residual[inds])))
    maxshift=0;offrow=sy.Integer(0)
    for kind in (0,1):
        for r in range(6):
            row=fp.compress(fp.h4_apply(fp.flat_mode(kind,r)))
            offrow=max(offrow,sum(abs(c) for state,c in row.items() if state!=(kind,r,0)))
            maxshift=max(maxshift,max(abs(state[2]) for state in row))
    assert offrow==4 and maxshift==1
    normB=Fraction(7,10)*int(offrow);ratio=normB/Fraction(16)
    n0=cut-max(abs(basis[i][2]) for i,v in enumerate(seed) if v)+1
    assert ratio==Fraction(7,40) and n0==24
    resolvent_tail=2*ratio**n0/(1-ratio)
    assert Fraction.from_float(expected['flat_reference_filter_error_norm_bound'])>=resolvent_tail
    assert expected['flat_reference_filter_error_norm_bound']==math.nextafter(float(resolvent_tail),math.inf)
    x=Fraction(2)
    assert x>=normB*Fraction(2,5)
    motion_tail=2*x**n0*Fraction(n0+1,math.factorial(n0)*(n0+1-x))
    assert Fraction.from_float(expected['flat_reference_motion_Dyson_tail_norm_bound'])>=motion_tail
    assert expected['flat_reference_motion_Dyson_tail_norm_bound']==math.nextafter(float(motion_tail),math.inf)
    ref_times={}
    for t in (-.4,0.,.4):
        v=expm_multiply((-1j*t)*H,seed*np.sqrt(2),traceA=(-1j*t)*H.diagonal().sum())
        ref_times[t]=lift(v,basis)
    return projected,gphysical,ref_times,{
        'independent_flat_frame_b_is_minus_author_b':True,'source_compact_coordinate':[1,1,1],
        'reference_cut':cut,'max_field_shift_per_offdiagonal_step':maxshift,
        'offdiagonal_norm_bound_exact':str(normB),'Neumann_ratio_exact':str(ratio),'first_possible_exit_order':n0,
        'exact_resolvent_truncation_bound':str(resolvent_tail),'reported_resolvent_bound':float(resolvent_tail),
        'exact_Dyson_truncation_bound':str(motion_tail),'reported_motion_bound':float(motion_tail),
        'independent_interior_floating_residual_norms':interior,
        'independent_omitted_boundary_floating_residual_norms':boundary,
        'rounding_and_scope':'Reported author bounds are upward-rounded images of the exact rational truncation bounds. They exclude solve and floating-point roundoff error; numerical residuals are separate and not interval certified.'}


def numerical(expected):
    projected,gphysical,ref_times,tail=reference_and_tails(expected)
    source=first_outputs(0)[0,1];rows=[]
    K,delta=.4,.7
    for old in expected['rows']:
        S=old['S'];p,n8,H2,H4,B,R=pb.finite_operators(S)
        eta=K*S*(S+1);H=eta*(H2+4*sparse.eye(len(p)))+delta*H4
        psi=physical_array(source,p);flat=physical_array(projected,p);bright=psi-flat
        width=2*np.sqrt(eta)
        ev,V=la.eigh(H.toarray(),subset_by_value=(-width,width),driver='evr')
        selected=V@(V.conj().T@psi)
        selectedflat=V@(V.conj().T@flat);selectedbright=V@(V.conj().T@bright)
        resid=float(np.linalg.norm(H@V-V*ev,'fro'));assert resid<1e-8
        gm=spsolve(H-16j*sparse.eye(len(p)),psi);gp=spsolve(H+16j*sparse.eye(len(p)),psi)
        gv=16*(gm-gp)/(2j)
        measured={'accepted_norm_squared':float(np.vdot(selected,selected).real),
                  'selected_vector_error_to_F_first_output':float(np.linalg.norm(selected-flat)),
                  'selected_bright_norm_squared':float(np.vdot(selectedbright,selectedbright).real),
                  'flat_rejection_norm_squared':float(np.linalg.norm(selectedflat-flat)**2),
                  'smooth_filter_vector_error_to_reference':float(np.sqrt(squared_distance(gv,p,gphysical)))}
        assert len(p)==old['physical_dimension'] and len(ev)==old['selected_eigenvalue_count']
        diffs={k:abs(v-old[k]) for k,v in measured.items()};assert max(diffs.values())<2e-10
        motions=[]
        for saved in old['pure_Hamiltonian_motion']:
            t=saved['t'];actual=expm_multiply((-1j*t)*H,flat*np.sqrt(2),traceA=(-1j*t)*H.diagonal().sum())
            err=float(np.sqrt(squared_distance(actual,p,ref_times[t])))
            norm=float(np.vdot(actual,actual).real)
            # Difference-of-norms distances have cancellation at t=0.
            tolerance=1e-7 if t==0 else 2e-9
            assert abs(err-saved['state_norm_error'])<tolerance
            assert abs(norm-saved['finite_norm_squared'])<1e-10
            motions.append({'t':t,'state_norm_error':err,'finite_norm_squared':norm,
                            'error_discrepancy':abs(err-saved['state_norm_error'])})
        row={'S':S,'physical_dimension':len(p),'selected_eigenvalue_count':len(ev),
             'independent_eigen_residual_Frobenius':resid,'measured_filter_fields':measured,
             'filter_discrepancies':diffs,'pure_Hamiltonian_motion':motions}
        rows.append(row);print(json.dumps(row),flush=True)
    return rows,tail


def main():
    assert not (HERE/'COMPARISON_RESULTS.json').exists()
    author,auth=sources();exact=exact_grams(author['exact']);numeric,tails=numerical(author['numerical'])
    result={'source_sha256':identity(Path(__file__))['sha256'],'authentication':auth,
            'exact_Laurent_controls':exact,'reference_tail_check':tails,'reconstructed_numeric_controls':numeric,
            'read_identities':sorted(READS.values(),key=lambda row:row['path']),
            'scope':'New author filter/unitary diagnostics rebuilt from frozen independent rules. No author runner or inherited author builder executed; no cube or full finite-spin filtered count simulation; analytic theorem comparison recorded separately.'}
    (HERE/'COMPARISON_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
