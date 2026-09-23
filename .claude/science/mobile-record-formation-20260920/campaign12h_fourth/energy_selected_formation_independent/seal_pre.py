"""Freeze the independent energy-filter reconstruction before author access."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
HERE=Path(__file__).resolve().parent


def identity(path):
    path=Path(path).resolve();data=path.read_bytes()
    return {'path':str(path),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}


def authenticate(row):
    assert all(identity(row['path'])[k]==row[k] for k in ('path','bytes','sha256')),row['path']


sources=json.loads((HERE/'SOURCE_IDENTITIES.json').read_text())
for row in sources['science_sources']+sources['instruction_snapshots']:authenticate(row)
validation=json.loads((HERE/'VALIDATION_RESULTS.json').read_text())
receipt=json.loads((HERE/'VALIDATION_RECEIPT.json').read_text())
assert receipt['exit_code']==0
assert receipt['script_sha256']==identity(HERE/'validate.py')['sha256']==validation['source_sha256']
assert receipt['stdout_sha256']==identity(HERE/'VALIDATION.stdout')['sha256']
assert receipt['stderr_sha256']==identity(HERE/'VALIDATION.stderr')['sha256']
assert json.loads((HERE/'VALIDATION.stdout').read_text())==validation
assert (HERE/'VALIDATION.stderr').read_bytes()==b''
artifacts=[identity(p) for p in sorted(HERE.rglob('*'))
           if p.is_file() and p.name!='PRE_COMPARISON_SEAL.json']
result={
    'phase':'PRE_COMPARISON',
    'created_utc':datetime.now(timezone.utc).isoformat(),
    'status':'Bounded independent reconstruction complete under the explicitly reused checked premises; not a formal audit, retention or no-go packet verdict.',
    'scope':'Original deterministic H6,S=eta H2,S+delta H4,S, eta=K S(S+1), fixed ring/cube graphs; statewise output-energy filters and explicitly changed first-instrument target evolution from fixed normalizable original N4 field densities with convergent physical spin embeddings.',
    'candidate_exposure':'No energy_selected_formation_author source, runner, result, new root scientific message outside the assignment, compensation/proposal/general-checker packet, campaign plan/registry/checkpoint or Git surface opened before PRE. Root stated its analytic draft was already frozen; no author identity or formula was supplied.',
    'result':'Moving o(eta) windows vanish on continuous-spectral inputs uniformly in centers and on compact input families. Ring C0(H6,S+4eta) functional calculus converges to the prepared flat calculus; centered expanding sublinear windows converge strongly to P0. Changed first jumps with their changed losses yield a full trace-norm ring target limit with rates8 kappa then4 kappa and probabilities exp(-8kt),2(exp(-4kt)-exp(-8kt)),(1-exp(-4kt))^2. Cube sublinear windows suppress formation and yield unitary N4 target evolution.',
    'load_bearing_new_bridges':[
        'Weak spectral measures plus a compact-center contradiction prove uniform moving-window nonconcentration, without absolute continuity or rates.',
        'Bounded-loss Dyson restoration converts the checked prepared no-event theorem into a purely Hamiltonian group theorem on the flat space, including negative times and domain checks.',
        'C0 functional calculus and spectral tightness give strong convergence of expanding sharp windows to P0.',
        'Projected first-channel Grams fix the changed first loss; compact source-family semigroup composition gives full target density convergence.'
    ],
    'counterexamples_preserved':[
        'Shrinking-cell normalized inputs disprove uniformity over the entire unit ball despite a continuous-spectrum limit.',
        'Order-eta windows can retain continuous-spectral weight.',
        'Alternating ring centers give different limits on flat inputs.',
        'Exact rational finite-spin smooth-filter coherent/resolved loss difference implies existence of a centered sharp-window difference; a separate complete-spin floating control gives a concrete radius.',
        'Retaining the original ring first rate16 contradicts the independently derived selected rate8.'
    ],
    'instrument_resolution':'Unfiltered finite-S losses agree, but output energy filters can break newborn-pattern orthogonality. The expanding centered ring filter has common limiting loss8 kappa for both stipulated resolutions by a separate exact P0 Gram argument; recycling densities need not agree.',
    'source_premise_reuse':'Prior prepared and physical ring/cube spectral/first-sector results reused at exact seals; no new independent cube spectral proof or microscopic theorem is claimed. New controls import only frozen independent ring rules/frame helpers.',
    'science_sources':sources['science_sources'],
    'instruction_snapshots':sources['instruction_snapshots'],
    'independent_artifacts':artifacts,
    'actual_execution_receipts':[identity(HERE/(stem+'_RECEIPT.json')) for stem in
                                ('FILTER','EXACT_INSTRUMENT','EXACT_FIXED','EXACT_CROSS','SOURCE','VALIDATION')],
    'execution_summary':'Five successful commands and one preserved failed metadata-serialization command. Full source versions, stdout/stderr, timings, exit codes and stream/source hashes are bound. Complete successful stdout JSON objects were parsed and matched to saved results. No finite-spin time-evolution simulation or numerical convergence rate is claimed.',
    'failed_route':'An exploratory spin-one characteristic-factor calculation did not produce a simple rational sharp-projector witness. Its results remain preserved; the exact rational smooth-filter witness and positive integral over centered sharp projections supplied the needed counterexample instead. The initial SymPy metadata JSON failure is separately preserved without altering a mathematical assertion.',
    'limits':'No derived reservoir, microscopic filter transfer, native selection, local implementation, volume limit, operator-norm filter convergence, arbitrary noncompact spin-dependent input uniformity, or unchanged-instrument density conclusion. Fixed smooth filters have their own generally non-scalar limiting first loss, not the universal expanding-window clock.',
    'attribution':'New reconstruction completed before candidate access. Mathematical progress findings were sent to root during the work. Root stated its own draft preceded this assignment; reciprocal independence beyond that timeline is not asserted.',
    'readiness':'Stop before source comparison. Preserve every PRE-bound byte; any later comparison or correction must be a separate artifact.',
    'authority_boundary':'Writes confined to energy_selected_formation_independent. No Git, checkpoint edit, publication, audit, external messaging or onward delegation.'
}
destination=HERE/'PRE_COMPARISON_SEAL.json';assert not destination.exists()
destination.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'pre_seal':identity(destination),'science_sources':len(result['science_sources']),
                  'instruction_snapshots':len(result['instruction_snapshots']),
                  'independent_artifacts':len(artifacts)},indent=2))
