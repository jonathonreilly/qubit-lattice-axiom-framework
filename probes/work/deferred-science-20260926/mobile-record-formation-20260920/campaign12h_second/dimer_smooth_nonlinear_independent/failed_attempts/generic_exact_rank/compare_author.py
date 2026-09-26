#!/usr/bin/env python3
"""Post-seal source authentication and selected independent author-row reconstruction."""
from pathlib import Path
from fractions import Fraction
import datetime,hashlib,itertools,json,math
import numpy as np
import sympy as s
import independent_check as own

HERE=Path(__file__).resolve().parent;RAW=HERE.parent
def identity(p):
    b=p.read_bytes();return {'path':str(p.resolve()),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}

def main():
    pre=json.loads((HERE/'PRE_COMPARISON_SEAL.json').read_text())
    for row in pre['sources']+pre['artifacts']:assert identity(Path(row['path']))==row,row['path']
    expected={'dimer_smooth_nonlinear_check.py':'d97be26aa22fad562ac9419566bcb09c4c97db01dcbd598bca0d601f968f7eb8',
              'dimer_smooth_nonlinear_checks/RESULTS.json':'7eab8d3d38a557a89baae56552c87930d568d4a395e04651974eabff262166be'}
    for name,sha in expected.items():assert identity(RAW/name)['sha256']==sha
    author=json.loads((RAW/'dimer_smooth_nonlinear_checks/RESULTS.json').read_text())
    for row in author['sources']:assert identity(Path(row['path']))==row
    receipt=json.loads((RAW/'DIMER_SMOOTH_NONLINEAR_RUN_RECEIPT.json').read_text())
    assert receipt['script_sha256']==expected['dimer_smooth_nonlinear_check.py'] and receipt['returncode']==0
    assert (RAW/'DIMER_SMOOTH_NONLINEAR_RUN.stderr').read_bytes()==b''
    assert (RAW/'DIMER_SMOOTH_NONLINEAR_RUN.log').read_text().strip()=='three_control_groups_complete'
    for row in author['blocks']:
        ell,N=row['ell'],row['N'];assert N>8*ell and N%2==0
        assert row['block_sites']==ell**3 and row['actual_difference_count']==(2*ell-1)**3
        assert row['overlap_colors_bound']==8*ell**3 and row['bare_internal_edges']==3*(ell-1)*ell**2
        assert row['five_internal_stencil_counts']==[max(ell-3,0)*ell**2]*3+[max(ell-3,0)**2*ell]*2
    # Selected two-color cube sectors, built as bitmasks and single-bit hypercube edges.
    sectors=[]
    for k in (2,4):
        masks=[sum(1<<v for v in pos) for pos in itertools.combinations(range(8),k)]
        index={v:i for i,v in enumerate(masks)};dim=len(masks);L=np.zeros((dim,dim),dtype=np.int64)
        edges=[(v,v^step) for v in range(8) for step in (1,2,4) if v<(v^step)]
        for row,mask in enumerate(masks):
            for a,b in edges:
                if ((mask>>a)&1)!=((mask>>b)&1):
                    col=index[mask^(1<<a)^(1<<b)];L[row,col]-=1;L[row,row]+=1
        assert np.array_equal(L,L.T)
        assert s.Matrix(L).rank()==dim-1
        gap=float(np.linalg.eigvalsh(L)[1])
        c=np.array([1+i%7 for i in range(dim)],dtype=np.int64);den=int(c@c)
        variance=1-Fraction(int(c.sum())**2,dim*den);D=Fraction(int(c@L@c),den)
        observable=np.array([((mask>>0)&1)*((mask>>3)&1) for mask in masks],dtype=np.int64)
        mean=Fraction(int(observable.sum()),dim)
        pairing=sum(Fraction(int(c[i])**2,den)*(int(observable[i])-mean) for i in range(dim))
        f=dim*c.astype(float)**2/den;hdot=float(np.dot(-L@f,np.log(f))/dim)
        saved=next(row for row in author['fixed_sector'] if row['particle_count']==k)
        assert str(variance)==saved['exact_variance'] and str(D)==saved['exact_Dirichlet']
        assert str(pairing)==saved['centered_pairing'] and saved['exact_connected_rank']==dim-1
        assert abs(gap-saved['numerical_gap'])<1e-12 and abs(hdot-saved['entropy_derivative'])<1e-12
        sectors.append({'particle_count':k,'dimension':dim,'exact_variance':str(variance),'exact_Dirichlet':str(D),
                        'exact_pairing':str(pairing),'gap_difference':abs(gap-saved['numerical_gap']),
                        'entropy_derivative_difference':abs(hdot-saved['entropy_derivative'])})
    tangent=[]
    T=s.Matrix.vstack(s.eye(13),-s.ones(1,13))
    for row in author['entropy_algebra']['tangent_cancellations']:
        seed=row['seed'];weights=[2+(i+3*seed)**2%13 for i in range(14)]
        p=s.Matrix([s.Rational(w,sum(weights)) for w in weights]);H=s.diag(*[1/x for x in p])
        derivatives=[T*s.Matrix([s.Rational((i+seed+j)%5-2,101) for i in range(13)]) for j in range(3)]
        As=[own.jac(p,s.eye(3)[:,j],1) for j in range(3)]
        pt=-sum((A*z for A,z in zip(As,derivatives)),s.zeros(14,1))
        coeff=H*pt+sum((A.T*H*z for A,z in zip(As,derivatives)),s.zeros(14,1))
        assert len(set(coeff))==1 and str(coeff[0])==row['ambient_constant']
        tangent.append(str(coeff[0]))
    for row in author['entropy_algebra']['without_replacement_coupling']:
        m=row['m'];failure=1-Fraction(math.prod(range(m-3,m+1)),m**4)
        assert str(failure)==row['exact_index_coupling_failure'] and str(Fraction(6,m))==row['four_draw_bound']
    assert author['entropy_algebra']['holder_alpha']=='1/224'
    assert author['entropy_algebra']['integrated_Hoeffding_exponential_bound']==29
    maximum=0.
    for row in author['entropy_algebra']['Bernoulli_checks']:
        p,t=row['p'],row['t'];value=math.log((1-p)*math.exp(-t*p)+p*math.exp(t*(1-p)))
        maximum=max(maximum,abs(value-row['log_centered_MGF']))
        assert abs(value-row['log_centered_MGF'])<3e-15 and row['bound']==t*t/8
    sources={row['path']:row for row in pre['sources']+author['sources']}
    for name in [*expected,'DIMER_SMOOTH_NONLINEAR_RUN_RECEIPT.json','DIMER_SMOOTH_NONLINEAR_RUN.log','DIMER_SMOOTH_NONLINEAR_RUN.stderr']:
        row=identity(RAW/name);sources[row['path']]=row
    result={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'disposition':'no actionable source or numerical discrepancy',
       'sources':list(sources.values()),'author_checker_executed':False,'precomparison_authentication':{'sources':len(pre['sources']),'artifacts':len(pre['artifacts'])},
       'coverage':{'complete_source_read':True,'complete_author_checker_result_read':True,'block_arithmetic_rows':5,
                   'selected_cube_sectors':sectors,'exact_tangent_coefficients':tangent,'exact_coupling_rows':8,
                   'Bernoulli_rows':30,'maximum_Bernoulli_difference':maximum},
       'limits':'Author finite controls support selected identities; they do not establish all-volume convergence by enumeration. General proof assessed independently in the pre-seal derivation. No author suite execution or trajectory simulation.'}
    with (HERE/'AUTHOR_COMPARISON.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({'disposition':result['disposition'],'sources':len(sources),'coverage':result['coverage']}))

if __name__=='__main__':main()
