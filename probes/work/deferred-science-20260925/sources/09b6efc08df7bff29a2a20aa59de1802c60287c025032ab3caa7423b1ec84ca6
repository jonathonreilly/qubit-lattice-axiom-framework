#!/usr/bin/env python3
"""Read-only comparison of released Part I and existing results; no primary run."""
from pathlib import Path
import ast
import hashlib
import json
from datetime import datetime, timezone

HERE = Path(__file__).parent
ROOT = HERE.parent / 'photon-observation-personal'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    pins = {}
    def pin(path, expected=None):
        got = sha(path)
        if expected is not None:
            assert got == expected, (str(path), got, expected)
        pins[str(path)] = got
        return got
    pin(HERE / 'PRE_SEAL.json', 'a83ce23e6d3e27a0a4bccd4ec2170441123e6b49c0cf09b3d2670eea00a1e6e4')
    preseal = json.loads((HERE / 'PRE_SEAL.json').read_text())
    for name,digest in preseal['files'].items():
        pin(HERE/name,digest)
    pin(ROOT/'AUTHOR_CONTROL_SEAL.json', '2ee41b61dd03f9e20eacd257469cd03bb54c9b96951bc06c0d58e535e0394f05')
    authorseal=json.loads((ROOT/'AUTHOR_CONTROL_SEAL.json').read_text())
    for name,digest in authorseal['files'].items():
        pin(ROOT/name,digest)
    source=ROOT/'PHOTON_OBSERVATION_AND_LIVE_BIRTH_ROOT_DERIVATION.md'
    pin(source,'15c48725d54c95abe43de50de23b62fbf9d983029ee2152c125f361a9ca316ba')
    sourcemanifest=json.loads((ROOT/'SOURCE_PINS.json').read_text())
    assert sourcemanifest['main']=='0e6ad8285096ed668816f18caaa6fbbfbd9c50e8'
    matched_parents=[]
    for row in sourcemanifest['sources'][:3]:
        path=Path(row['path'])
        pin(path,row['sha256'])
        assert sha(HERE/'sources'/path.name)==row['sha256']
        matched_parents.append(path.name)
    lines=source.read_text().splitlines(keepends=True)
    assert lines[10].startswith('## I.') and lines[122].startswith('## II.')
    assert lines[251].startswith('## What the actual observational bridge')
    excerpt=('Released source SHA256: '+sha(source)+'\n'
             'Reviewed Part I: original lines 1-122. Shared closure: lines 252-270, only for Part I limitations.\n'
             'Part II body is omitted and not reviewed.\n\n'+''.join(lines[:122])+
             '\n[Part II omitted]\n\n'+''.join(lines[251:]))
    with (HERE/'POST_RELEASED_PART_I.txt').open('x') as f:f.write(excerpt)
    control=ROOT/'photon_birth_controls.py'
    script=control.read_text();tree=ast.parse(script)
    pieces=[]
    for node in tree.body:
        if isinstance(node,(ast.Import,ast.ImportFrom)) or (isinstance(node,ast.FunctionDef) and node.name in ('dispersion_controls','main')):
            pieces.append(ast.get_source_segment(script,node))
    scoped_script='\n\n'.join(pieces)+'\n'
    with (HERE/'POST_SCOPED_CONTROL_SOURCE.txt').open('x') as f:f.write(scoped_script)
    full_result=json.loads((ROOT/'PHOTON_BIRTH_CONTROL_RESULTS.json').read_text())
    dispersion=full_result['dispersion']
    assert full_result['source_sha256']==sha(control)
    assert (ROOT/'PHOTON_BIRTH_CONTROL_RESULTS.json').read_bytes()==(ROOT/'CONTROL.stdout.txt').read_bytes()
    assert not (ROOT/'CONTROL.stderr.txt').read_bytes()
    execution=json.loads((ROOT/'CONTROL_EXECUTION.json').read_text())
    assert execution['exit_code']==0
    with (HERE/'POST_SCOPED_CONTROL_RESULTS.json').open('x') as f:
        json.dump({'root_source_sha256':sha(control),'root_complete_result_sha256':sha(ROOT/'PHOTON_BIRTH_CONTROL_RESULTS.json'),
                   'scope':'Part I dispersion/conversion payload only; graph results not scientifically reviewed.',
                   'dispersion':dispersion},f,indent=2);f.write('\n')
    original=json.loads((HERE/'CONTROL_RESULTS.json').read_text())
    comparison=[]
    for row in dispersion['rows']:
        assert float(row['speed_over_c'])<=1
        assert float(row['radial_remainder_over_x4'])<1/40
        assert float(row['speed_remainder_over_x4'])<1/20
        same=[r for r in original['rows'] if r['direction']==row['direction'] and float(r['x'])==float(row['x'])]
        if same:
            old=same[0]
            assert float(row['A4'])==old['A4']
            assert float(row['radial_remainder_over_x4'])==old['scaled_remainders']['radial']
            assert float(row['speed_remainder_over_x4'])==old['scaled_remainders']['speed']
            comparison.append({'direction':row['direction'],'x':row['x'],'A4_and_remainder_values_equal_at_PRE_output_precision':True})
    assert len(dispersion['rows'])==30 and len(comparison)==8
    assert dispersion['hbar_c_GeV_m']==original['conversions']['hbar_c_GeV_m']
    conversions=[]
    for row in dispersion['conditional_bounds']:
        old=next(r for r in original['conversions']['rows'] if r['E_QG2_GeV']==float(row['E_QG_2_GeV']))
        assert float(row['a_sqrt_A4_upper_m'])==old['a_sqrt_A4_bound_m']
        assert float(row['a_orientation_independent_necessary_upper_m'])==old['unknown_orientation_a_bound_m']
        conversions.append({'root_label':row['published_analysis'],'matching_PRE_label':old['label'],
                            'both_length_conversions_equal_at_PRE_output_precision':True})
    assert authorseal['sealed_at_utc']<preseal['sealed_at_utc']
    for path,digest in pins.items():assert sha(Path(path))==digest,path
    now=datetime.now(timezone.utc).isoformat()
    verification={
        'verified_at_utc':now,'preserved_PRE_members':len(preseal['files']),
        'root_seal_members_hash_verified':len(authorseal['files']),
        'root_seal_hash_verification_is_not_Part_II_scientific_review':True,
        'Part_I_parent_hashes_match_PRE':matched_parents,
        'root_authorship_seal_utc':authorseal['sealed_at_utc'],'independent_PRE_seal_utc':preseal['sealed_at_utc'],
        'root_authorship_seal_precedes_PRE':True,
        'complete_Part_I_and_relevant_shared_closure_read':True,
        'Part_II_body_graph_functions_and_graph_result_rows_reviewed':False,
        'complete_dispersion_function_and_30_rows_read':True,
        'source_hash_in_result_matches_released_script':True,
        'complete_stdout_equals_complete_result_bytes':True,'recorded_control_exit_code':execution['exit_code'],
        'recorded_wrapper_wall_seconds':execution['wall_seconds'],'stderr_bytes':0,
        'overlapping_rows_compared_without_rerun':comparison,
        'hbar_c_70_digit_string_matches_PRE':True,'conditional_conversions':conversions,
        'maximum_recorded_radial_remainder_over_x4':max(float(r['radial_remainder_over_x4']) for r in dispersion['rows']),
        'maximum_recorded_speed_remainder_over_x4':max(float(r['speed_remainder_over_x4']) for r in dispersion['rows']),
        'first_failed_harness_record_preserved_in_root_seal':True,
        'primary_or_control_functions_imported_or_rerun':False,
        'printed_LHAASO_inverse_discrepancy_preserved_from_PRE':True,
        'new_independent_derivation_claim':False,
        'scope':'Mechanical Part I released-source comparison; mathematical findings are in POST.md.'}
    for name,value in [('POST_SOURCE_PINS.json',{'verified_at_utc':now,'reviewed_source_and_evidence_sha256':dict(sorted(pins.items())),
                         'scope':'Shared source/whole-result hashes bind identity only; scientific review excludes Part II and graph payloads.'}),
                       ('POST_VERIFICATION.json',verification)]:
        with (HERE/name).open('x') as f:json.dump(value,f,indent=2);f.write('\n')
    print(json.dumps(verification,indent=2))


if __name__=='__main__':main()
