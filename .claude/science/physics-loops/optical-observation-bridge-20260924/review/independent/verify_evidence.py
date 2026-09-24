"""Read-only inventory and verification of this independent PRE evidence."""
from pathlib import Path
import datetime, hashlib, json

HERE=Path(__file__).resolve().parent
BASE=HERE.parent

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

parents=[
 ('campaign-working/docs/WEAK_FIELD_WAVE_PACKETS_FROM_MOBILE_RECORD_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md','651fa7cfd816ca5df8c401959458b7590c2f6ec706af437ef3ce31accb7d3ccf','Full weak-field note; fixed-volume preparation, quotient and harmonic normalization. Main revision 0e6ad8285096ed668816f18caaa6fbbfbd9c50e8.'),
 ('photon-observation-publication/docs/PHOTON_DISPERSION_OBSERVATIONAL_CONSTRAINTS_AND_LIVE_FORMATION_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-24.md','acf74cfce461cfbf607f7ba2994ff0a3d5986b9571bf7c5efacecebdf9ab5d7b','Part I and bridge/limitations: supplied timing/SI conversion and exact archival table identities, including the preserved printed-number discrepancy.'),
 ('prepared-observation-publication/docs/ORIGINAL_RECORD_CALIBRATION_AND_PREPARED_MATTER_PROBE_BOUNDED_THEOREM_NOTE_2026-09-24.md','14ed0194fefd18eeee711e733bb76c75ce4a88832b01bc55dc41e6e058ba612b','A.2, B.1-6, C.2 and relevant D: mode normalization, physical initial isometry, exact effect and full count/microscopic limit premises. Earlier unchanged full reading reused.'),
 ('probe-physical-limits-publication/docs/PREPARED_ORIGINAL_RECORD_PROBE_ENERGY_VACUUM_RESPONSE_AND_CLOCK_SCOPE_BOUNDED_THEOREM_NOTE_2026-09-24.md','2dd49ffa004fa09726b2388decb7c4a36dd69f2cdaf5f3bbb8ffe3e829a47c6d','Part C only, fully refreshed; prior checked rate/probability ratio and clock identification. Whole-file snapshot/hash is not A/B science coverage.')]
source_rows=[]
for rel,expected,scope in parents:
    origin=BASE/rel; snapshot=HERE/'sources'/origin.name
    assert sha(origin)==expected==sha(snapshot)
    source_rows.append({'origin':str(origin),'snapshot':str(snapshot.relative_to(HERE)), 'sha256':expected,'bytes':snapshot.stat().st_size,'scientific_read_scope':scope,'premise_status':'Supplied named conditional parent reused; not recertified.'})
instructions=[
 (BASE/'campaign-working/AGENTS.md','9bea097b409610ed70f55f53349ce206b6df7e62c63205d7775bac9b3d10dde6'),
 (BASE/'campaign-working/docs/ai_methodology/SCIENCE_WORKFLOW.md','d74718214335d4feae4b40d75720482ca93bd1560a3c35174e7bf875b5b59cc4'),
 (Path('/Users/jonreilly/.codex/skills/physics-claim-reviewer/SKILL.md'),'9d841edd05b9dc4c5145abcfd5352cd45460a1cc57c23c1eabd131590dbb1455')]
for path,expected in instructions:
    assert sha(path)==expected
archive=HERE/'attempt01_before_empty_band_label_fix'
for row in json.loads((archive/'PRESERVATION.json').read_text())['members']:
    assert sha(archive/row['path'])==row['sha256']
    assert (archive/row['path']).stat().st_size==row['bytes']

current=json.loads((HERE/'CONTROL_RESULTS.json').read_text())
first=json.loads((archive/'CONTROL_RESULTS.json').read_text())
for directory in [archive,HERE]:
    receipt=json.loads((directory/'CONTROL_EXECUTION.json').read_text())
    result=json.loads((directory/'CONTROL_RESULTS.json').read_text())
    assert sha(directory/'optical_band_controls.py')==receipt['source_sha256']==result['source_sha256']
    assert sha(directory/'CONTROL_STDOUT.log')==receipt['stdout_sha256']
    assert (directory/'CONTROL_STDOUT.log').read_bytes()==(directory/'CONTROL_RESULTS.json').read_bytes()
    assert receipt['exit_code']==0 and receipt['stderr_bytes']==0
    assert (directory/'CONTROL_STDERR.log').read_bytes()==b''
    assert sha(directory/'CONTROL_STDERR.log')==receipt['stderr_sha256']
assert current['source_sha256']=='56a189c0d7463c5cf6ae90a72209a0881e8a14d1a3b0100abe5b37f48b34cfb8'
assert sha(HERE/'CONTROL_RESULTS.json')=='740c8d9cd1e04e58d097d3718ba657cd2768ea6499c97313fdc30bcb23234c57'
for result in [first,current]:
    for key in ['elapsed_seconds','completed_utc','source_sha256']:
        result.pop(key)
for row in current['hard_band_rows']:
    feasible=row.pop('normalized_one_particle_state_feasible')
    assert feasible != row['band_empty']
    if not feasible:
        assert row['eta_max'] is None and row['limiting_ratio_max'] is None
        row['eta_max']=0.0;row['limiting_ratio_max']=1.0
assert current==first
result=json.loads((HERE/'CONTROL_RESULTS.json').read_text())
groups=['spectral_rows','hard_band_rows','finite_volume_enclosure_rows','exact_mean_constraint_rows','mean_tail_counterexamples_to_band_substitution','SI_rows','small_graph_reference_gap_rows']
row_counts={key:len(result[key]) for key in groups}
assert row_counts==dict(zip(groups,[7,56,17,9,3,6,4]))

pins={'captured_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(), 'phase':'blind independent PRE', 'sources':source_rows,
 'instructions_reused':[{'path':str(path),'sha256':expected,'status':'Previously fully read for this coherent campaign; unchanged hash reverified.'} for path,expected in instructions],
 'author_or_other_active_packets_read':False,'current_checkpoint_read':False,'new_primary_retrievals':0,
 'transitive_parents_recertified':False,'whole_file_snapshot_does_not_expand_scientific_scope':True}
report={'verified_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_origins_and_snapshots_verified':4,
 'own_control_runs':2,'parent_or_author_runners_executed':0,'both_runs_exit_zero_empty_stderr':True,
 'complete_stdout_equals_results_for_both_runs':True,'preserved_first_run_members':5,
 'empty_band_label_correction':{'rows':10,'meaning':'No normalized one-particle state exists below the reference gap; optimum and ratio are null.','other_scientific_values_exact_between_runs':True},
 'complete_scientific_rows_read':row_counts,'group_row_total':sum(row_counts.values()),
 'direct_real_curl_record_read':True,'direct_real_vs_Fourier_optimizer_comparisons':3,
 'max_squared_frequency_error':result['direct_real_curl']['max_squared_frequency_error'],
 'max_real_vs_Fourier_eta_difference':max(x['difference'] for x in result['direct_real_curl']['mean_optimization_comparisons']),
 'volume_scope':'Static spectral bounds proved uniformly; full count errors remain fixed-graph with ordered limits.',
 'mean_vs_hard_band_distinction':'Exact mean optimizer and explicit high-energy-tail states preserve the failure of a fourth-power mean-only inference.',
 'numerical_scope':'Finite floating corroboration and rounded SI arithmetic, not interval certification or a full-process simulation.',
 'author_or_other_active_packets_read':False,'delegation':False,'publication_audit_or_existing_packet_mutation':False}
for name,value in [('SOURCE_PINS.json',pins),('VERIFICATION_REPORT.json',report)]:
    path=HERE/name;assert not path.exists();path.write_text(json.dumps(value,indent=2)+'\n')
print(json.dumps(report,indent=2))
