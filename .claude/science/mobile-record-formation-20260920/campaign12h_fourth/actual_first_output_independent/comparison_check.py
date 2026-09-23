"""Post-PRE comparison using the independently sealed physical builder/frame.

No author implementation is imported or executed. Only exact bound candidate
files and stored corroborative vectors are read; the S=64 evolution is rerun
from the independent physical local rules.
"""
import sys
sys.dont_write_bytecode=True
from consequence_check import *
import sympy as sp

AUTHOR=HERE.parent/'actual_first_output_author'
SUPPORT=HERE.parent/'finite_spin_unprepared_followup'

def ident(p):
    b=p.read_bytes()
    return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}

def authenticate():
    pre=HERE/'PRE_COMPARISON_SEAL.json'
    assert ident(pre)['sha256']=='ba8907a8da440ad8832f86ff42b33b7c90d99082d181d215af43a8b89c11f37c'
    predata=json.loads(pre.read_text())
    for item in predata['science_sources']+predata['independent_artifacts']:
        assert ident(Path(item['path']))==item
    seal=AUTHOR/'AUTHOR_SEAL.json'
    assert ident(seal)['sha256']=='e8a1ea634f3355f883da749124af2ab5f5fbaba3ea7270d972dd279d3ded6046'
    data=json.loads(seal.read_text());opened=[ident(seal)]
    support_names={'unprepared_decomposition_check.py','DECOMPOSITION_RESULTS.json','CHECK_RUN_RECEIPT.json'}
    support_names.update('PROPAGATED_S'+str(s)+'.npz' for s in (64,96,128,192))
    permitted=data['artifacts']+data['sources'][:3]+[x for x in data['sources'][3:] if Path(x['path']).name in support_names]
    for item in permitted:
        got=ident(Path(item['path']));assert got==item;opened.append(got)
    prepared=HERE.parent/'finite_spin_post_birth_author/finite_spin_dynamics_check.py'
    pp=ident(prepared)
    assert pp['sha256']=='5030a960accba4a654b27de92fcc7bdd074f179b207930ae0aa1b97af20ca3df'
    # Its exact identity is also bound by the previously checked prepared seal.
    ps=json.loads((prepared.parent/'AUTHOR_SEAL.json').read_text())
    assert any(x['path']==str(prepared) and x['sha256']==pp['sha256'] for x in ps['artifacts'])
    opened.append(pp)
    record={'opened_and_authenticated':opened,
            'support_scope':'The bound decomposition runner/results/receipt and four bound stored vectors were read solely to check the candidate numerical diagnostics. No broader unprepared research, tail packet, plan or checkpoint was read.',
            'unopened_candidate_support_entries':[x for x in data['sources'][3:] if Path(x['path']).name not in support_names],
            'author_code_execution':'None; all numerical reconstructions use the independent PRE helpers.',
            'pre_bytes_unchanged':True}
    (HERE/'COMPARISON_SOURCES.json').write_text(json.dumps(record,indent=2)+'\n')
    return record

def exact_comparison(candidate):
    own=json.loads((HERE/'CONSEQUENCE_RESULTS.json').read_text())
    for a in candidate['first_sector_exact_weight_controls']:
        b=next(x for x in own['first_clock']['finite_spin_rows'] if x['S']==a['S'])
        assert a['H2']==b['H2_zero_field']==-8 and a['H4']==b['H4_zero_field']==24
        assert sum(sum(m['resolved_grams']) for m in a['first_marks'])==b['total_loss_without_kappa']==16
        assert all(m['resolved_grams']==[1,1] and m['coherent_gram']==2 for m in a['first_marks'])
    for a in candidate['complete_finite_spin_loss_controls']:
        b=next(x for x in own['finite_spin_loss_bounds'] if x['S']==a['S'])
        assert a['P_dimension']==b['P_dimension']
        assert a['minimum_loss_without_kappa']==b['loss_diagonal_min']==0
        assert a['maximum_loss_without_kappa']==b['loss_diagonal_max']==4
        assert a['off_diagonal_nonzero_entries']==b['off_diagonal_nonzero_entries']==0
    k,t,s=sp.symbols('k t s',positive=True)
    a=sp.exp(-16*k*t);g=sp.Rational(4,3)*(sp.exp(-4*k*t)-a);h=1-a-g
    bound=sp.Rational(1,2)-sp.Rational(2,3)*sp.exp(-4*k*t)+sp.Rational(1,6)*a
    assert sp.simplify(h/2-bound)==0
    convolution=sp.integrate(16*k*sp.exp(-16*k*s)*(1-sp.exp(-4*k*(t-s)))/2,(s,0,t))
    assert sp.simplify(convolution-bound)==0
    return {'clock_and_loss_rows_equal':True,'symbolic_B_equals_independent_h_over_two':True,'symbolic_first_clock_convolution_equal':True}

def flat_coefficients(words,vectors):
    """Map full physical columns to complete compact-frame coefficients."""
    ret={}
    for i,(q,z) in enumerate(words):
        fc,sign=flat_coord(q,z)
        if fc is not None:
            if fc not in ret:ret[fc]=np.zeros(vectors.shape[1],complex)
            ret[fc]+=sign*vectors[i]/np.sqrt(2)
    return ret

def diagnostics(candidate):
    data=json.loads((SUPPORT/'DECOMPOSITION_RESULTS.json').read_text())
    K,delta,kappa=.4,.7,.3;times=np.linspace(0,1.2,4)
    basis,H=flat_matrix(32,K,delta);ix={s:i for i,s in enumerate(basis)}
    comparisons=[];maxima=defaultdict(float);references=None;seed=None
    saved64=None
    for row in data['rows']:
        S=row['S'];p=SUPPORT/row['vector_file']
        assert ident(p)['sha256']==row['vector_sha256']
        z=np.load(p,allow_pickle=False)
        words=[(tuple(map(int,q)),int(f)) for q,f in zip(z['charges'],z['circulations'])]
        assert np.array_equal(z['times'],times)
        initial=z['vectors'][0].sum(axis=1)
        physical={s:complex(a) for s,a in zip(words,initial) if a}
        matching=[str(ch) for ch,v in first_jumps().items() if v==physical]
        assert len(matching)==1
        if seed is None:
            seed=physical
            fv,fc=flat_projection(seed)
            v=np.zeros(len(basis),complex)
            for s,a in fc.items():v[ix[s]]=a
            generator=-1j*H-2*kappa*sps.eye(len(basis))
            references=expm_multiply(generator,v,start=0,stop=1.2,num=4,traceA=generator.diagonal().sum())
        else:assert seed==physical
        fv,fc=flat_projection(seed)
        assert np.linalg.norm(z['vectors'][0,:,0]-np.array([fv.get(s,0) for s in words]))<1e-14
        if S==64:saved64=(words,z['vectors'].copy())
        for ti,t in enumerate(times):
            coefficients=flat_coefficients(words,z['vectors'][ti])
            for N in (1,2,8):
                labels=[b for b in basis if abs(b[2])<=N]
                got=np.array([sum(coefficients.get(b,[0,0])) for b in labels])
                bright=np.array([coefficients.get(b,[0,0])[1] for b in labels])
                expected=np.array([references[ti,ix[b]] for b in labels])
                density=np.outer(got,got.conj())-np.outer(expected,expected.conj())
                # Direct Hermitian diagonalization checks the author's rank-two formula.
                err=float(np.sum(abs(np.linalg.eigvalsh(density))))
                own={'actual_window_weight':float(np.vdot(got,got).real),
                     'limiting_window_weight':float(np.vdot(expected,expected).real),
                     'density_trace_norm_error':err,
                     'complementary_window_weight':float(np.vdot(bright,bright).real)}
                a=next(x for x in candidate['finite_window_controls'] if x['S']==S and x['N']==N and abs(x['t']-t)<1e-12)
                for key,val in own.items():
                    diff=abs(a[key]-val);maxima[key]=max(maxima[key],diff)
                    assert diff<2e-11,(S,N,t,key,val,a[key])
                comparisons.append({'S':S,'N':N,'t':float(t),**own})
            if ti==3:
                total_flat=sum(abs(v[1])**2 for v in coefficients.values())
                high_flat=sum(abs(v[1])**2 for (a,r,f),v in coefficients.items() if abs(f)>=S/4)
                comparisons.append({'S':S,'t':float(t),'post_PRE_bounded_check_of_candidate_high_field_sentence':True,
                                    'complement_rotor_flat_mass':float(total_flat),
                                    'complement_rotor_flat_mass_at_label_abs_f_at_least_S_over_four':float(high_flat)})
    # Independent complete S=64 propagation, with the same physical initial seed.
    words,stored=saved64
    p,n8,H2,H4,B,R=finite_operators(64,False);pix={s:i for i,s in enumerate(p)}
    perm=np.array([pix[s] for s in words]);assert len(perm)==len(p)
    fv,fc=flat_projection(seed)
    v=np.array([seed.get(s,0) for s in p]);flat=np.array([fv.get(s,0) for s in p])
    generator=-1j*(K*64*65*(H2+4*sps.eye(len(p)))+delta*H4)-kappa*R/2
    evolved=expm_multiply(generator,np.column_stack([flat,v-flat]),start=0,stop=1.2,num=4,traceA=generator.diagonal().sum())
    errors=[float(np.linalg.norm(evolved[i,perm,:]-stored[i])) for i in range(4)]
    assert max(errors)<2e-10
    # A conservative independent interaction-picture cutoff tail estimate.
    cut=32;initial_f=max(abs(s[2]) for s in fc);n0=cut-initial_f+1;x_upper=4
    tail=Fraction(2*x_upper**n0*(n0+1),math.factorial(n0)*(n0+1-x_upper))
    return {'saved_vector_window_diagnostics':comparisons,'maximum_author_diagnostic_differences':dict(maxima),
            'independent_S64_complete_propagation_vector_errors':errors,
            'independent_flat_reference_flux_cutoff':cut,'independent_flat_reference_Dyson_tail_bound':float(tail),
            'first_mark_seed':{'matching_channel':matching[0],'states':[{'q':list(q),'f':f,'coefficient_real':a.real,'coefficient_imag':a.imag} for (q,f),a in seed.items()]},
            'scope':'Saved higher-spin vectors are authenticated and reprocessed, not regenerated. S=64 complete propagation is independently regenerated. Diagnostics are finite-spin corroboration and do not prove a complementary limit.'}

def main():
    sources=authenticate()
    candidate=json.loads((AUTHOR/'ACTUAL_OUTPUT_CONTROLS.json').read_text())
    result={'exact_comparison':exact_comparison(candidate),'diagnostics':diagnostics(candidate),
            'source_entries_authenticated':len(sources['opened_and_authenticated']),
            'material_candidate_discrepancies_identified':[],
            'proof_scope':'Shared candidate claims agree with the frozen independent PRE. Broader full-window time-smearing, first-age-convolved local state limit, and trace-norm obstruction remain explicitly independent provisional additions.'}
    (HERE/'COMPARISON_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
