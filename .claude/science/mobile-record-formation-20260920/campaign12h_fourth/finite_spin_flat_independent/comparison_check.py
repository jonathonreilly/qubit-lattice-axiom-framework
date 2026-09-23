"""Post-PRE comparison. Never imports or executes candidate author code."""
import hashlib,json,difflib,math
from pathlib import Path
from fractions import Fraction
import numpy as np
import scipy.sparse as sps
from scipy.sparse.linalg import expm_multiply
from decisive_controls import TABLE,expected_h4,physical_limit
from flat_probe import *

HERE=Path(__file__).resolve().parent
AUTHOR=HERE.parent/'finite_spin_post_birth_author'
PRE_HASH='97aa84106b6ca88adcb4bd4c6286ada6d24087740da767fded03485590df495b'
AUTHOR_HASH='dfc55f6eac748bb11130fe3a8e5544194c6babd810c0c06d45e177c56c72df7e'

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def polynomial(s):
    got=sy.sympify(s)
    return got.subs({z:f for z in got.free_symbols})

def compare_source_bindings():
    pre=HERE/'PRE_COMPARISON_SEAL.json';seal=AUTHOR/'AUTHOR_SEAL.json'
    assert digest(pre)==PRE_HASH
    assert digest(seal)==AUTHOR_HASH
    pdata=json.loads(pre.read_text());adata=json.loads(seal.read_text())
    for item in pdata['artifacts']+pdata['sources']['sources']:
        assert digest(Path(item['path']))==item['sha256'],item['path']
    for item in adata['artifacts']:
        assert Path(item['path']).parent==AUTHOR
        assert digest(Path(item['path']))==item['sha256'],item['path']
    prior_allowed={x['path'] for x in pdata['sources']['sources']}
    checked=[];excluded=[]
    for item in adata['sources']:
        if item['path'] in prior_allowed:
            assert digest(Path(item['path']))==item['sha256'];checked.append(item['path'])
        else:excluded.append(item['path'])
    old1=(AUTHOR/'finite_spin_dynamics_check_before_tail_factor_fix.py').read_text()
    old2=(AUTHOR/'finite_spin_dynamics_check_before_geometric_bound.py').read_text()
    now=(AUTHOR/'finite_spin_dynamics_check.py').read_text()
    diffs=''.join(difflib.unified_diff(old1.splitlines(True),old2.splitlines(True),fromfile='before_tail_factor_fix',tofile='before_geometric_bound'))+'\n'+''.join(difflib.unified_diff(old2.splitlines(True),now.splitlines(True),fromfile='before_geometric_bound',tofile='current'))
    (HERE/'AUTHOR_HISTORY_DIFFS.txt').write_text(diffs)
    streams=[]
    for p in sorted(AUTHOR.glob('*.stderr.log')):
        assert not p.read_bytes();streams.append({'file':p.name,'bytes':0})
    runs=[]
    for p in sorted(AUTHOR.glob('*RUN_RECEIPT.json')):
        data=json.loads(p.read_text());assert data['exit_code']==0;runs.append({'file':p.name,**data})
    probe=json.loads((AUTHOR/'FLAT_BAND_SPIN_CORRECTION_RESULTS.json').read_text())
    comp=json.loads((AUTHOR/'FLAT_COMPRESSED_OPERATORS_RESULTS.json').read_text())
    assert json.loads((AUTHOR/'PROBE.stdout.log').read_text())==probe
    assert json.loads((AUTHOR/'COMPRESSION.stdout.log').read_text())==comp
    dynstreams=[]
    for suffix in ('','_BEFORE_TAIL_FACTOR_FIX','_BEFORE_GEOMETRIC_BOUND'):
        result=json.loads((AUTHOR/f'FINITE_SPIN_DYNAMICS_RESULTS{suffix}.json').read_text())
        stream=(AUTHOR/f'DYNAMICS{suffix}.stdout.log').read_text()
        split=stream.index('{\n')
        preamble=[json.loads(s) for s in stream[:split].splitlines()]
        assert json.loads(stream[split:])==result
        assert len(preamble)==len(result['rows'])==6
        dynstreams.append({'suffix':suffix,'summary_rows':preamble,'tail_bound':result['flat_reference_Dyson_tail_norm_bound']})
    return {'PRE_artifacts':len(pdata['artifacts']),'PRE_sources':len(pdata['sources']['sources']),'author_artifacts':len(adata['artifacts']),'author_permitted_sources':checked,'excluded_source_bindings_not_read_or_hashed':excluded,'runs':runs,'stderr_streams':streams,'dynamic_streams':dynstreams}

def exact_comparison():
    data=json.loads((AUTHOR/'FLAT_COMPRESSED_OPERATORS_RESULTS.json').read_text())
    rows=[]
    for row in data['rows']:
        a,r=row['kind'],row['r'];v=flat_mode(a,r);got=h2_apply(v,True)
        compressed=compress(got);beta,gamma=TABLE[a][r]
        assert sy.expand(polynomial(row['electric_quadratic'])-(4*f*f+beta*f+gamma))==0
        leakage=sy.expand(sum(x*x for x in residual(got).values())/2)
        assert sy.expand(polynomial(row['leading_spin_leakage_norm_squared'])-leakage)==0
        # The author b basis is minus our type-1 basis; both input and output transform.
        author_terms={(x['kind'],x['r'],x['circulation_shift']):int(x['coefficient'])*((-1)**(a+x['kind'])) for x in row['H4_terms']}
        assert author_terms==compress(h4_apply(v))==expected_h4(a,r,0)
        rows.append({'type':a,'r':r,'electric':str(compressed[(a,r,0)]),'squared_leakage':str(leakage),'H4_terms_after_sign_map':str(author_terms)})
    probe=json.loads((AUTHOR/'FLAT_BAND_SPIN_CORRECTION_RESULTS.json').read_text())
    for row in probe['exact_rows']:
        a=0 if row['C']==[0,1] else 1;r=row['minus_word_index'];z=row['initial_circulation']
        v=flat_mode(a,r);d=h2_apply(v,True);ell=residual(d)
        norm=lambda vec:sy.simplify(sum(c.subs(f,z)**2 for c in vec.values())/4)
        assert Fraction(row['flat_vector_norm_squared'])==Fraction(1,2)
        assert sy.Rational(row['D2_norm_squared'])==norm(d)
        assert sy.Rational(row['D2_leakage_norm_squared'])==norm(ell)
        assert sy.Rational(row['flat_compressed_expectation'])==compress(d)[a,r,0].subs(f,z)
    # Independently check the full loss identity quoted from an excluded packet.
    lossrows=[]
    for q in PWORDS:
        C,r=coord(q);adj=C not in ((0,2),(1,3));expected={(q,0):sy.Integer(4)} if adj else {}
        for coherent in (False,True):assert loss_apply({(q,0):sy.Integer(1)},coherent)==expected
        lossrows.append({'word':list(q),'adjacent_B_pair':adj,'loss_diagonal':4 if adj else 0})
    h4spectra=[]
    for theta in (0.,.13,.82,1.7,3.0):
        H=np.zeros((12,12),complex)
        for a in range(2):
            for r in range(6):
                for (b,s,df),v in expected_h4(a,r,0).items():H[6*b+s,6*a+r]+=v*np.exp(1j*df*theta)
        got=np.linalg.eigvalsh(H);expected=np.sort([12+4*np.cos((4*theta+2*np.pi*j)/12) for j in range(12)])
        error=np.max(abs(got-expected));assert error<1e-12
        h4spectra.append({'theta':theta,'maximum_eigenvalue_error':float(error)})
    return {'twelve_exact_compressions':rows,'all_rational_probe_rows_checked':len(probe['exact_rows']),'full_rotor_loss_diagonal':lossrows,'H4_spectrum_controls':h4spectra}

def finite_loss_equality():
    rows=[]
    for S in (1,2,4,8):
        p,n8,H2,H4,B,R=finite_operators(S,False)
        coherent=sps.csc_matrix(R.shape);cross=[]
        for edge in range(8):
            plus=B.get((edge,1),sps.csc_matrix((len(n8),len(p))))
            minus=B.get((edge,-1),sps.csc_matrix((len(n8),len(p))))
            product=plus.T@minus
            assert product.nnz==0
            cross.append({'edge':edge,'cross_Gram_nonzero_entries':int(product.nnz)})
            joined=plus+minus;coherent+=joined.T@joined
        error=sps.linalg.norm(coherent-R)
        assert error<1e-13
        rows.append({'S':S,'P_dimension':len(p),'total_loss_difference_norm':float(error),'cross_Grams':cross})
    return rows

def author_reference(R,K,delta,kappa,seed,t):
    basis=[(a,r,z) for a in range(2) for r in range(6) for z in range(-R,R+1)];bi={s:i for i,s in enumerate(basis)}
    rr=[];cc=[];vv=[]
    for j,(a,r,z) in enumerate(basis):
        beta,gamma=TABLE[a][r]
        rr.append(j);cc.append(j);vv.append(K*(4*z*z+beta*z+gamma))
        for s,c in expected_h4(a,r,z).items():
            if s in bi:rr.append(bi[s]);cc.append(j);vv.append(delta*c)
    H=sps.csc_matrix((vv,(rr,cc)),shape=(len(basis),len(basis)))
    initial=np.zeros(len(basis),complex);initial[bi[seed]]=(-1)**seed[0]
    evolved=np.exp(-2*kappa*t)*expm_multiply(-1j*t*H,initial)
    return physical_limit(initial,basis),physical_limit(evolved,basis)

def dynamic_comparison():
    data=json.loads((AUTHOR/'FINITE_SPIN_DYNAMICS_RESULTS.json').read_text());param=data['parameters'];K=param['K'];delta=param['delta'];kappa=param['kappa']
    stored=[]
    for row in data['rows']:
        S=row['S'];C=S*(S+1)
        assert row['physical_P_dimension']==len(p_basis(S))
        assert abs(row['eta']-K*C)<1e-12
        assert abs(row['epsilon']-np.sqrt(delta/(K*C)))<1e-15
        for d in row['controls']:
            expected=np.exp(-4*kappa*d['t'])
            assert abs(d['flat_limit_survival']-expected)<1e-11
            assert abs(d['survival_error']-abs(d['finite_spin_survival']-expected))<1e-14
            assert -1e-13<=d['finite_spin_survival']<=1+1e-12
        stored.append({'S':S,'P_dimension':len(p_basis(S)),'controls':row['controls']})
    comparisons=[]
    for S in (8,32):
        p,n8,H2,H4,B,R=finite_operators(S,False)
        gen=-1j*(K*S*(S+1)*(H2+4*sps.eye(len(p)))+delta*H4)-kappa*R/2
        for seed in ((1,1,1),(0,0,0)):
            t=.6;initial,ref=author_reference(32,K,delta,kappa,seed,t)
            v=np.array([initial.get(s,0) for s in p]);u=expm_multiply(t*gen,v);got=dict(zip(p,u))
            error=np.sqrt(sum(abs(got.get(s,0)-ref.get(s,0))**2 for s in set(got)|set(ref)))
            survival=float(np.vdot(u,u).real)
            author=next(d for row in data['rows'] if row['S']==S for d in row['controls'] if abs(d['t']-t)<1e-10 and d['initial_flat_label']==list(seed))
            assert abs(error-author['state_norm_error'])<1e-9
            assert abs(survival-author['finite_spin_survival'])<1e-10
            comparisons.append({'S':S,'seed':list(seed),'t':t,'independent_state_error':float(error),'author_state_error':author['state_norm_error'],'independent_survival':survival,'author_survival':author['finite_spin_survival']})
    n0=32;x_upper=2
    exact=Fraction(2*x_upper**n0*(n0+1),math.factorial(n0)*(n0+1-x_upper))
    bound=data['flat_reference_Dyson_tail_norm_bound']
    assert Fraction.from_float(bound)>=exact
    return {'all_stored_dynamic_rows':stored,'independent_endpoint_comparisons':comparisons,'Dyson_tail':{'exact_rational_upper_bound':str(exact),'saved_float_bound':bound,'saved_float_is_upper_bound':True},'quantitative_exponents':{'h_exponent':'-2/7','sqrt_h':'-1/7','eta^-1_h^-3':'-1/7','eta^-2_h^-5':'-4/7','endpoint':'-5/7'}}

def main():
    result={'provenance':compare_source_bindings(),'exact':exact_comparison(),'finite_spin_instrument_loss_equality':finite_loss_equality(),'dynamics':dynamic_comparison()}
    (HERE/'COMPARISON_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
