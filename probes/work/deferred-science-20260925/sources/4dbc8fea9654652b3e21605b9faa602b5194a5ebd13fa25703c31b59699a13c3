"""Released-source bindings and PRE-formula comparison of stored author data.

No author source is imported or executed; no Fock or Fourier control rerun.
The Decimal comparison uses equations (20)--(21) already in sealed PRE.md.
It is a POST consistency check, not another blind reconstruction or interval
certificate of either the floating inputs or the full dynamical process.
"""
from pathlib import Path
from datetime import datetime, timezone
from decimal import Decimal as D, localcontext
import hashlib
import json


HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def decimal(value):
    return D(str(value))


def stable_pre(v1, v2, c, a, b, cross, g):
    """PRE equations 20 and 21, without author characteristic-function code."""
    g2 = g*g
    e1 = (-g2*v1/2).exp()
    e2 = (-g2*v2/2).exp()
    base1, base2 = 1-e1, 1-e2
    z = g2*c
    positive, negative = z.exp(), (-z).exp()
    cosine_minus_one = (positive+negative)/2-1
    sine = (positive-negative)/2
    joint0 = base1*base2+e1*e2*cosine_minus_one
    joint1 = joint0+g2*(e1*a+e2*b-e1*e2*(a+b)*(1+cosine_minus_one)+2*e1*e2*cross*sine)
    raw = joint1/((base1+g2*e1*a)*(base2+g2*e2*b))
    subtracted = (((1-g2*(a+b))*cosine_minus_one+2*g2*cross*sine)/(g2*g2*a*b)) if a*b else None
    return joint1/(g2*g2), raw, subtracted


def main():
    pins = read(HERE/'POST_SOURCE_PINS_INITIAL.json')
    for row in pins['sources']:
        assert sha(Path(row['origin'])) == row['sha256']
        if row['snapshot']:
            assert sha(HERE/row['snapshot']) == row['sha256']
    pre_seal = read(HERE/'PRE_SEAL.json')
    assert sha(HERE/'PRE.md') == pre_seal['report_sha256']
    for row in pre_seal['members']:
        path = HERE/row['path']
        assert sha(path) == row['sha256'] and path.stat().st_size == row['bytes']
    prior = read(HERE/'SOURCE_PINS.json')
    for row in prior['sources']+prior['instructions']:
        assert sha(Path(row['origin'])) == row['sha256'] == sha(HERE/row['snapshot'])
    author = HERE/'post_sources/two-detector-coincidence-personal'
    author_seal = read(author/'AUTHOR_SEAL.json')
    for name, row in author_seal['files'].items():
        assert sha(author/name) == row['sha256'] and (author/name).stat().st_size == row['bytes']
    addition = read(author/'AUTHOR_SCOPE_ADDENDUM_SEAL.json')
    assert addition['original_AUTHOR_SEAL_sha256'] == sha(author/'AUTHOR_SEAL.json')
    for name, row in addition['files'].items():
        assert sha(author/name) == row['sha256'] and (author/name).stat().st_size == row['bytes']
    execution = read(author/'EXECUTION.json')
    data = read(author/'COINCIDENCE_RESULTS.json')
    assert execution['exit_code'] == 0 and execution['stderr_bytes'] == 0
    assert (author/'CONTROL.stderr').read_bytes() == b''
    assert sha(author/'coincidence_controls.py') == execution['code_sha256'] == data['source_sha256']
    assert sha(author/'COINCIDENCE_RESULTS.json') == sha(author/'CONTROL.stdout') == execution['stdout_sha256']
    for start in [0, 10, 20]:
        viewed = [json.loads(line) for line in (HERE/f'POST_FOCK_ROWS_{start:02d}_{start+9:02d}.jsonl').read_text().splitlines()]
        assert len(viewed) == 10
        for row in viewed:
            index = row.pop('index')
            assert row == data['fock_rows'][index]
    viewed = [json.loads(line) for line in (HERE/'POST_SPATIAL_ROWS.jsonl').read_text().splitlines()]
    for row in viewed:
        index = row.pop('index')
        assert row == data['spatial_rows'][index]

    moment_rows, finite_rows, spatial_rows = [], [], []
    with localcontext() as context:
        context.prec = 100
        for index, row in enumerate(data['fock_rows']):
            v1,v2,c,a,b,t = [decimal(row[key]) for key in ['v1','v2','c','A1','A2','Re_chi1_star_chi2']]
            m1,m2 = v1+2*a,v2+2*b
            fourth = v1*v2+2*c*c+2*v2*a+2*v1*b+8*c*t
            raw = fourth/(m1*m2)
            sub = (c*c/2+2*c*t)/(a*b) if a*b else None
            expected = {'second1':m1,'second2':m2,'fourth':fourth,'raw_ratio':raw,
                        'rho1':2*a/m1,'rho2':2*b/m2,'background_subtracted_ratio':sub}
            errors = {}
            for key,value in expected.items():
                if value is None:
                    assert row[key] is None
                else:
                    errors[key] = abs(value-decimal(row[key]))
            assert max(errors.values()) < D('2e-13')
            moment_rows.append({'index':index,'packet':row['packet'],'correlation_r':row['correlation_r'],
                                'null_subtraction_denominator':sub is None,
                                'maximum_PRE_formula_vs_stored_float_difference':str(max(errors.values()))})
            for item in row['finite_g_uncut_initial_effect_rows']:
                g = decimal(item['g'])
                values = stable_pre(v1,v2,c,a,b,t,g)
                errors = {}
                for key,value in zip(['joint_effect_over_g4','raw_ratio','background_subtracted_ratio'],values):
                    if value is None:
                        assert item[key] is None
                    else:
                        errors[key] = abs(value-decimal(item[key]))
                assert max(errors.values()) < D('1e-58')
                finite_rows.append({'fock_index':index,'g':str(g),'null_subtraction_denominator':sub is None,
                                    'absolute_decimal_formula_differences':{key:str(value) for key,value in errors.items()}})
        for index,row in enumerate(data['spatial_rows']):
            assert row['L']%2 == 0 and row['separation']%2 == 0
            assert min(row['separation'],row['L']-row['separation']) >= 12
            assert row['packet_available']
            assert row['mean_reference_frequency'] <= row['epsilon']+1e-12
            v,c,vband,cband,a,b,t = [decimal(row[key]) for key in ['v1','c','v_band','band_covariance','A1','A2','Re_chi1_star_chi2']]
            projected = (vband+cband)/2
            coefficient_error = max(abs(a-projected),abs(b-projected),abs(t-projected))
            assert coefficient_error < D('2e-15')
            moment = v*v+2*c*c+2*v*(a+b)+8*c*t
            raw = moment/((v+2*a)*(v+2*b))
            sub = (c*c/2+2*c*t)/(a*b)
            formula_error = max(abs(raw-decimal(row['raw_ratio'])),abs(sub-decimal(row['background_subtracted_ratio'])))
            assert formula_error < D('2e-13')
            spatial_rows.append({'index':index,'L':row['L'],'separation':row['separation'],'epsilon':row['epsilon'],
                                 'even_translation_and_disjoint_separation':True,
                                 'kind':'low-band diagnostic' if row['epsilon']<=2 else 'full-band diagnostic above sqrt(12)',
                                 'projected_amplitude_coefficient_max_difference':str(coefficient_error),
                                 'PRE_ratio_formula_max_difference':str(formula_error)})
        assert D('1')-D('.34')**2 == D('.8844')

    assert len(moment_rows)==30 and len(finite_rows)==120 and len(spatial_rows)==16
    comparison={'scope':'POST arithmetic on stored released data using sealed PRE formulas; no author execution, matrix/Fourier rerun or new blind derivation.',
                'decimal_precision':100,'finite_data_tolerance':'1e-58','float_formula_tolerance':'2e-13',
                'moment_rows':moment_rows,'finite_g_rows':finite_rows,'spatial_rows':spatial_rows}
    text=json.dumps(comparison,indent=2)+'\n'
    (HERE/'POST_DECIMAL_COMPARISON.json').write_text(text)
    summary={'verified_utc':datetime.now(timezone.utc).isoformat(),'verifier_source_sha256':sha(Path(__file__)),
             'own_PRE_members_unchanged':len(pre_seal['members']),
             'released_source_and_PRE_anchor_pins_verified':len(pins['sources']),
             'unchanged_PRIOR_scientific_and_review_origins':len(prior['sources']),
             'unchanged_instruction_origins':len(prior['instructions']),
             'author_members_verified':len(author_seal['files']),
             'author_source_stdout_result_execution_binding':True,
             'author_executions_by_checker':0,'new_Fock_Fourier_simulations':0,
             'author_execution_wall_seconds':execution['elapsed_seconds'],'author_internal_seconds':data['elapsed_seconds'],
             'all_stored_fock_rows':30,'all_stored_finite_g_rows':120,'all_stored_spatial_rows':16,
             'null_subtracted_Fock_rows':sum(row['null_subtraction_denominator'] for row in moment_rows),
             'null_subtracted_finite_rows':sum(row['null_subtraction_denominator'] for row in finite_rows),
             'full_band_spatial_diagnostics':sum(row['epsilon']>2 for row in spatial_rows),
             'author_max_Fock_residual_as_stored':max(row['Fock_moment_max_residual'] for row in data['fock_rows']),
             'maximum_decimal_finite_formula_difference':str(max(D(value) for row in finite_rows for value in row['absolute_decimal_formula_differences'].values())),
             'maximum_float_formula_difference':str(max(D(row['maximum_PRE_formula_vs_stored_float_difference']) for row in moment_rows)),
             'comparison_sha256':sha(HERE/'POST_DECIMAL_COMPARISON.json'),
             'limits':'Bindings and arithmetic correspondence only. Rational L12 covariance certificate and other PRE additions retain PRE provenance. No finite-window simulation, laboratory certificate, audit verdict or author-history completeness claim.'}
    report=json.dumps(summary,indent=2)+'\n'
    (HERE/'POST_VERIFICATION_REPORT.json').write_text(report)
    print(report,end='')


if __name__=='__main__':
    main()
