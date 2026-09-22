"""Authenticate the bounded independent reconstruction and preserve its boundary."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json
import sys
import platform
import numpy
import scipy
import sympy

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
PRIOR = BASE/'hardcore_live_density_independent'


def row(path):
    path = Path(path).resolve(); data = path.read_bytes()
    return {'path':str(path), 'bytes':len(data), 'sha256':sha256(data).hexdigest()}


def write(name, obj):
    (HERE/name).write_text(json.dumps(obj,indent=2)+'\n')


def main():
    expected = {
        PRIOR/'REPORT.md':'4956231c27a2724f52d2a859dfe06807320d86da033e738ccb1bb142f0bd5ded',
        PRIOR/'PRE_COMPARISON_SEAL.json':'caf8a8632b62fa99bcd9fad95f33aa27be44ed0ecd1b511e09827a825b04a703',
        PRIOR/'COMPARISON.md':'e671afbbc8c42a8dbd6e2922af644c073ac54f6508ceca575cd42fff7766fbb3',
        PRIOR/'FINAL_SEAL.json':'656e03ef2bc63bb3aafa27741bd0f2db9cb7df0f292eb84359f9b6a478df26b0',
        PRIOR/'finite_sector_check.py':'c1e6142e632ae77c14fee1b76079c8cba0f2e9c73cf1fed2e40f84f0a3893122',
        PRIOR/'FOURTH_ORDER_RESULTS.json':'e0b8287324cbcdc9712c6b43b468c77d25de556db846cc1c176a94b7e2408047',
        BASE/'HARDCORE_RECORD_MOTION_GENERATES_GAUGE_RINGS.md':'a527532324a5ed75e660b19c131f759fa0b38be4cdcf855f3a4f59c205cbc99e',
        BASE/'UNIFORM_RECORD_DENSITY_WITH_LIVE_FORMATION.md':'b900352f9e1d33c249f5ff155602feb6345c680d09ea192eedbc65d51ee670a4',
        BASE/'HOMOGENEOUS_FIELD_STAR_PENALTY_FOR_MOBILE_RECORDS.md':'860e8d364e50f8cddcbb6c534d69ca4ce822020ea80deab6c22361eeda0d361c',
        HERE/'literature/Nachtergaele_Sims_0506030v3.pdf':'c6af8d70ba5081a5d5bf000881d47fca6bfd19eb9a9bc74ff40939e48079c498',
        HERE/'literature/Bravyi_DiVincenzo_Loss_1105.0675v1.html':'a1616b2bf968d4c1067a076336c1606006be6fddbfa4b8cbca1f07e8fb19b825',
    }
    dependencies = []
    for path, digest in expected.items():
        item = row(path); assert item['sha256'] == digest; dependencies.append(item)
    previous = json.loads((PRIOR/'FINAL_SEAL.json').read_text())
    inherited = previous['reviewed_author_packet_and_reused_dependency']+previous['preserved_pre_comparison']+previous['comparison_artifacts']
    assert len(inherited) == 75
    for item in inherited:
        assert row(item['path']) == item
    result = json.loads((HERE/'NORMAL_FORM_RESULTS.json').read_text())
    receipt = json.loads((HERE/'NORMAL_FORM_CHECK_RECEIPT.json').read_text())
    assert receipt['returncode'] == 0
    assert receipt['script_sha256'] == row(HERE/'normal_form_check.py')['sha256']
    assert result['script'] == row(HERE/'normal_form_check.py')
    assert (HERE/'NORMAL_FORM_CHECK.stdout').read_bytes() == (HERE/'NORMAL_FORM_RESULTS.json').read_bytes()
    assert (HERE/'NORMAL_FORM_CHECK.stderr').read_bytes() == b''
    assert receipt['stdout_sha256'] == row(HERE/'NORMAL_FORM_CHECK.stdout')['sha256']
    assert receipt['stderr_sha256'] == row(HERE/'NORMAL_FORM_CHECK.stderr')['sha256']
    assert result['square']['physical_dimension'] == 9
    assert len(result['square']['finite_open_controls']) == 18
    for name, data in result['square']['exact_series'].items():
        assert len(data['order_checks']) == 10
        assert all(x['commutes_penalty_exactly'] for x in data['order_checks'])
        assert data['low_coefficients']['4'] == [['2','-2'],['-2','2']]
    for r in result['square']['finite_open_controls']:
        assert r['trace_error'] < 1e-8
    write('RUNTIME.json', {'python':sys.version,'executable':sys.executable,'platform':platform.platform(),
                          'numpy':numpy.__version__,'scipy':scipy.__version__,'sympy':sympy.__version__})
    write('LITERATURE_READ_RECEIPT.json', {
        'read_before_precomparison':True,
        'import':{'source':row(HERE/'literature/Nachtergaele_Sims_0506030v3.pdf'),
                  'version':'arXiv math-ph/0506030v3, 2 September 2005',
                  'coverage':'Definitions and interaction norm on PDF page 2; Theorem 1 and local-observable corollaries on page 3; complete Section 3.1 proof on pages 5-6. Clustering theorem not imported.',
                  'hypotheses_checked':'Finite cell dimension, arbitrary finite metric graph, bounded finite-range interaction norm proportional to the stated strength. Applied to finite-range F_r and each preparation generator, not directly to a constrained tensor factorization or a growing onsite penalty.',
                  'own_steps':'Homological recursion, finite local integral remainder, clipped-cone spatial sum, open-system Duhamel and scaling are reconstructed in REPORT.'},
        'context_only':{'source':row(HERE/'literature/Bravyi_DiVincenzo_Loss_1105.0675v1.html'),
                        'coverage':'Complete Section 4.4 through Lemma 4.2 proof, including the local recursion, interaction-strength estimate and stated ground-energy theorem. Adjacent Section 4.5 opening viewed. No ground-energy theorem imported as dynamical control.'},
        'failed_lookup':'Nonexistent 1810.02428v4 HTML returned 404; later abstract/version history only, no theorem used. See download receipt.',
        'limits':'No claim that all of either paper was read or independently reproved.'})
    write('SOURCE_READ_BOUNDARY.json', {
        'created_utc':datetime.now(timezone.utc).isoformat(),
        'neutral_task':row(HERE/'INPUT_SPEC.md'),
        'source_status':'Independent reconstruction before any newer author-source comparison.',
        'prior_comparison_bindings_reauthenticated':len(inherited),
        'new_author_sources_opened':[],
        'unopened':['newer one-dimensional transport','ramp','uniform-local normal form','their author scripts/results','campaign checkpoint','campaign registry'],
        'read_and_executed':'Only own sealed sector builder imported. New independent exact checker read fully; all result fields read in two nontruncated portions.',
        'changes':'Only this new independent directory was written. Earlier completed comparison and all prior packets unchanged.',
        'controls':'Exact order-ten nine-state algebra, local gap and inverse checks, finite cone sums, and 18 numerical full-Lindblad observations.',
        'failures':'No scientific execution failed. Preserve external 404 and rejected report-patch syntax receipt; pre-seal preparation Hamiltonian sign wording clarified to -iS_n, consistent with unchanged checker.'})
    artifacts = []
    exclude = {'PRE_COMPARISON_SEAL.json','CHECKPOINT.md'}
    sourcepaths = {str(Path(x['path'])) for x in dependencies}
    for path in sorted(HERE.rglob('*')):
        if path.is_file() and path.name not in exclude and '__pycache__' not in path.parts and str(path.resolve()) not in sourcepaths:
            artifacts.append(row(path))
    seal = {'created_utc':datetime.now(timezone.utc).isoformat(),
            'status':'Independent local-dynamics reconstruction complete; no new author sources accessed before seal.',
            'sources':dependencies,'artifacts':artifacts,
            'counts':{'sources':len(dependencies),'artifacts':len(artifacts),'total':len(dependencies)+len(artifacts)},
            'result':'For both supplied penalties, fixed J and a tenth-order number/gauge-preserving local preparation, beta<=beta0 epsilon^7 gives O(epsilon) local-field expectation error on fixed time intervals uniformly over even cubic tori of side>=6.',
            'general_sufficient_scaling':'Order r=2d+4 and beta=o(epsilon^(2d)); beta=O(epsilon^(2d+1)) gives O(epsilon).',
            'limits':['Prepared initial family; bare uniform-volume theorem unproved here.',
                      'Positive finite-parameter births decrease to zero; no fixed-beta result.',
                      'No time-window growth, thermodynamic phase, native compiler, or formal audit status.',
                      'Finite controls support algebra; the local remainder and locality proof supply the uniform statement.',
                      'Sufficient exponents, not optimized. Constants may be large.']}
    write('PRE_COMPARISON_SEAL.json',seal)
    for item in dependencies+artifacts:
        assert row(item['path']) == item
    print(json.dumps({'report':row(HERE/'REPORT.md'),'seal':row(HERE/'PRE_COMPARISON_SEAL.json'),
                      'counts':seal['counts'],'all_bindings_verify':True},indent=2))


if __name__ == '__main__':
    main()
