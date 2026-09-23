"""Freeze the bounded completed comparison, keeping every PRE byte intact."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
HERE=Path(__file__).resolve().parent
AUTHOR=HERE.parent/'energy_selected_formation_author'


def identity(path):
    path=Path(path).resolve();data=path.read_bytes()
    return {'path':str(path),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}


def authenticate(row):
    current=identity(row['path'])
    assert all(current[k]==row[k] for k in ('path','bytes','sha256')),row['path']


pre_row=identity(HERE/'PRE_COMPARISON_SEAL.json')
assert pre_row['sha256']=='78c272d1e51b182c4bdd7f98072f7fafa9cad83e6280d7092df5f4449d5f3e65'
pre=json.loads((HERE/'PRE_COMPARISON_SEAL.json').read_text())
for row in pre['science_sources']+pre['instruction_snapshots']+pre['independent_artifacts']:authenticate(row)
author_row=identity(AUTHOR/'AUTHOR_SEAL.json')
assert author_row['sha256']=='e41fcf88533b5f708b83e9265e6c1ed218547bfce44e7226a550d90f9d1a8bde'
author=json.loads((AUTHOR/'AUTHOR_SEAL.json').read_text())
for row in author['sources']+author['artifacts']:authenticate(row)
comp=json.loads((HERE/'COMPARISON_RESULTS.json').read_text())
for row in comp['read_identities']:authenticate(row)
assert comp['source_sha256']==identity(HERE/'comparison_check.py')['sha256']
receipt=json.loads((HERE/'COMPARISON_RECEIPT.json').read_text())
assert receipt['exit_code']==0 and receipt['script_sha256']==comp['source_sha256']
assert receipt['stdout_sha256']==identity(HERE/'COMPARISON.stdout')['sha256']
assert receipt['stderr_sha256']==identity(HERE/'COMPARISON.stderr')['sha256']
assert (HERE/'COMPARISON.stderr').read_bytes()==b''
stream=(HERE/'COMPARISON.stdout').read_text();objects=[];decoder=json.JSONDecoder()
while stream.strip():
    obj,end=decoder.raw_decode(stream.lstrip());objects.append(obj);stream=stream.lstrip()[end:]
assert len(objects)==5 and objects[-1]==comp
assert objects[:-1]==comp['reconstructed_numeric_controls']
sources=[identity(row['path']) for row in comp['read_identities']
         if not Path(row['path']).is_relative_to(HERE)]
sources=sorted({row['path']:row for row in sources}.values(),key=lambda r:r['path'])
artifacts=[identity(path) for path in sorted(HERE.rglob('*'))
           if path.is_file() and path.name!='FINAL_SEAL.json']
result={
    'created_utc':datetime.now(timezone.utc).isoformat(),
    'status':'Completed bounded mathematical source comparison; no required correction. Not a formal audit, retention or publication verdict.',
    'original_pre_seal':pre_row,
    'authorized_author_seal':author_row,
    'scope':pre['scope'],
    'sources':sources,
    'artifacts':artifacts,
    'required_corrections':[],
    'mathematical_disposition':'The moving-center spectral lemma, compact-family uniformity, purely Hamiltonian flat functional calculus, expanding centered ring projectors, and explicitly changed-instrument ring/cube full target density/count limits agree with the preserved independent derivation. No microscopic filter or native selection conclusion follows.',
    'domain_and_embedding_check':'Complete physical spin boxes in the common rotor space; bounded strong scaled Hamiltonian limit; atomless measures only where required; flat h selfadjoint on D(f^2), cube first h on D(sum E^2); finite-support cores plus unitary/contraction extension handle arbitrary normalizable fixed fields. No gap, uniform moment, full unit-ball uniformity or full-space Hamiltonian limit is assumed.',
    'pure_Hamiltonian_routes':'Author validly repeats the prepared weighted/crossing proof at kappa0 and both time signs; the independent PRE separately restores bounded loss by Dyson expansion. The two routes remain distinct in attribution.',
    'finite_vs_limit_instruments':'Both limiting flat-projected first losses are8 kappa I, and original second flat loss is4 kappa I. Finite-spin energy-filtered coherent/resolved losses can differ; the exact independent counterexample and the root control interpretation explicitly preserve that distinction. Recycling densities are not identified from equal limiting counts.',
    'author_control_repair':'The archived first run succeeded but its omitted-boundary-only residual was insufficient as a total reference error bound. The current source supplies exact rational truncation tails and separately labelled floating interior/boundary residuals. The reconstruction verifies the Neumann ratio7/40, first possible boundary exit order24, filter truncation2(7/40)^24/(1-7/40), and Dyson truncation8/136092312239308425, including upward rounding. These bounds exclude numerical solve/roundoff error and apply to the declared reference seed.',
    'actual_read_coverage':'Complete author analytic draft, interpretation, current control runner, result fields, both actual receipts and old qualification; full source diff covers the archived runner with the unchanged body read in the current version. All10 author stdout JSON objects parsed/matched. All8 author source and14 artifact bindings authenticated. Inherited author builders and unrelated inherited proofs were hash-reused, not re-reviewed or executed.',
    'actual_execution_scope':'One new comparison run imported only the frozen independent rules/frame. It rebuilt all24 exact Laurent Gram rows, complete physical S4/8/16/32 ring filter diagnostics, both signs of the unitary control, and the analytic reference-tail arithmetic. No author runner, inherited author builder, cube propagation, full finite-spin filtered count simulation or new spectral proof was executed.',
    'numerical_agreement':'Physical dimensions and selected counts match exactly; maximum filter-readout discrepancy approximately3.28e-15 and maximum unitary state-error discrepancy approximately7.41e-14. Numerical values corroborate the analytic proof and are not interval-certified error guarantees or a measured convergence rate.',
    'comparison_execution_receipt':identity(HERE/'COMPARISON_RECEIPT.json'),
    'comparison_stdout_objects_verified':len(objects),
    'preservation':'All54 distinct PRE source/instruction/artifact bindings remain unchanged. The old independent SymPy metadata failure and its original source/logs are preserved; the author archived successful but inadequately qualified run is unchanged. No comparison execution failed.',
    'attribution_and_timeline':{'analytic_draft_utc':comp['authentication']['author_analytic_draft_utc'],
       'author_packet_utc':comp['authentication']['author_final_seal_utc'],
       'independent_pre_utc':comp['authentication']['PRE_created_utc'],
       'record':'Root states analytic draft froze before independent dispatch. The later control interpretation finite-spin caution was added after the independent progress finding and is feedback-informed, not an independent root discovery. Candidate access began only after independent PRE authorization.'},
    'independent_additions_preserved':'Bounded-loss Dyson Hamiltonian extension; explicit noncompact-family, order-eta-width and alternating-center counterexamples; exact finite-spin filtered-instrument counterexample; fixed-C0 changed-target formulation with generally nonscalar first loss.',
    'authority_and_exclusions':'No Git/checkpoint/publication edit, compensation or volume-frontier access, unrelated source opening, delegation or formal audit. All writes confined to energy_selected_formation_independent.',
    'limits':'Deterministic supplied target with an explicitly changed first instrument, fixed graphs and fixed normalizable initial N4 field densities. No derived reservoir, microscopic filter transfer, native selection, local implementation, growing-volume limit or formal retained/no-go status.'
}
destination=HERE/'FINAL_SEAL.json';assert not destination.exists()
destination.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'final_seal':identity(destination),'source_bindings':len(sources),
                  'artifact_bindings':len(artifacts),'pre_unchanged':True,
                  'comparison_exit_code':receipt['exit_code']},indent=2))
