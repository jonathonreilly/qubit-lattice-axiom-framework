#!/usr/bin/env python3
"""Post-seal arithmetic/source comparison. Does not execute author code."""
import argparse
import hashlib
import json
from pathlib import Path
import sympy as s


HERE=Path(__file__).resolve().parent
ROOT=HERE.parent


def identity(path):
    raw=path.read_bytes()
    return {'path':str(path.resolve()),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}


def run():
    pre=json.loads((HERE/'PRE_COMPARISON_SEAL.json').read_text())
    for row in pre['artifacts']:
        assert identity(HERE/row['path'])['sha256']==row['sha256']
    inputs=[]
    for row in pre['sources']:
        actual=identity(Path(row['path']));assert actual['sha256']==row['sha256'];inputs.append(actual)
    checker=ROOT/'prepared_transverse_state_check.py'
    assert identity(checker)['sha256']=='215b7e73909eb016ebf62a09738bf24617ab9a0d5028379eff6714b685eabbb4'
    inputs.append(identity(checker))
    result_path=ROOT/'PREPARED_TRANSVERSE_STATE_RESULTS.json'
    log_path=ROOT/'PREPARED_TRANSVERSE_STATE_RUN.log'
    inputs.extend([identity(result_path),identity(log_path)])
    result=json.loads(result_path.read_text())
    rest=log_path.read_text();log=[];decoder=json.JSONDecoder()
    while rest.strip():
        row,end=decoder.raw_decode(rest.lstrip());log.append(row);rest=rest.lstrip()[end:]
    assert log[:-1]==result['rows'] and log[-1]['groups']==len(result['rows'])==4
    assert log[-1]['sources_sha256']==result['sources_sha256']
    actual_by_name={Path(row['path']).name:row['sha256'] for row in inputs}
    for name,digest in result['sources_sha256'].items():assert actual_by_name[name]==digest
    assert result['all_pass'] and log[-1]['all_pass'] and all(row['pass'] for row in result['rows'])
    rows={r['name']:r for r in result['rows']}
    gaussian=rows['exact_gamma_integrals_for_preparation_and_entropy']['cases']
    for row in gaussian:
        m=row['m'];lam=s.Rational(row['lambda'])
        assert s.Rational(row['Z'])==(1+lam)**(-2*m)
        assert s.Rational(row['mean_Q'])==2*m/(1+lam)
        assert s.simplify(s.sympify(row['entropy'])-2*m*(s.log(1+lam)-lam/(1+lam)))==0
    site=rows['fifteen_label_orthogonality_spectators_and_local_charge']
    expected_eigenvalues={str((17-s.sqrt(145))/72):1,str((17+s.sqrt(145))/72):1,
                         str(s.Rational(2,9)):1,str(s.Rational(2,3)):1,str(s.Rational(1,2)):4}
    # Compare exact values independent of their printed symbolic form.
    actual={s.simplify(s.sympify(k)):v for k,v in site['spectator_covariance_eigenvalues'].items()}
    expected={s.simplify(s.sympify(k)):v for k,v in expected_eigenvalues.items()}
    assert actual==expected and all(bool(x>0) for x in actual)
    assert site['covariance_rank']==14 and site['spectator_rank']==8
    assert site['local_centered_divergence_variances']==site['expected_variances']==['1/6','3/4']
    matrix=rows['exact_wave_spectrum_and_prepared_covariance_invariance']
    assert matrix['wavevectors']==4 and matrix['lambda_values']==3 and matrix['time_differences']==4
    assert matrix['max_exponential_residual']<2e-13
    path=rows['finite_path_density_bound_without_false_stationarity']
    assert path['states']==6 and s.Rational(path['Z'])==s.Rational(2,3)
    assert [s.Rational(x) for x in path['prepared_stationarity_residual']]==[s.Rational(1,4),-s.Rational(1,2),s.Rational(1,4),s.Rational(1,4),-s.Rational(1,2),s.Rational(1,4)]
    for row in path['cases']:
        assert abs(row['upper_bound']-1.5*row['reference_error'])<3e-14
        assert 0<=row['prepared_error']<=row['upper_bound']+1e-13
    return {'inputs':inputs,'preseal_artifacts_unchanged':len(pre['artifacts']),
            'author_sources_and_logs_read_completely':True,'author_checker_executed':False,
            'author_groups_authenticated':4,'Gaussian_cases_compared_exactly':len(gaussian),
            'spectator_spectrum_and_charge_values_compared_exactly':True,
            'toy_path_cases_arithmetic_compared':len(path['cases']),
            'coverage_limit':'The four-site toy tests measure-transfer algebra, not the fifteen-label propagator. That propagator remains an imported pinned hypothesis. Matrix-exponential decimals are authenticated author output, not an independent rerun; signed-generator/covariance identities were checked independently before comparison.',
            'unresolved_finding':'The source finite-N nonstationarity witness over a larger symmetry-closed M needs the first-axis-shell or sufficiently-large-N qualification. The author checker does not test larger harmonic mode sets.',
            'additional_drift_findings':[]}


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,required=True);args=parser.parse_args()
    result=run();args.out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
    print('PASS: source/log authentication and exact/arithmetic comparisons. The narrow finite-volume witness-scope finding remains.')
