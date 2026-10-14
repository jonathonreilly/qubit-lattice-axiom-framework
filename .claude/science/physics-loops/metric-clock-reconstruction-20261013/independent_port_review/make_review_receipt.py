from pathlib import Path
import datetime,hashlib,json,platform
out=Path(__file__).resolve().parent;p=out.parent;w=p.parents[3]
def ident(f):
 b=f.read_bytes()
 return {'path':str(f),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}
frozen=json.loads((out/'REVIEW_INPUT_FREEZE_v1.json').read_text())
for e in frozen['files']:
 assert hashlib.sha256((w/e['path']).read_bytes()).hexdigest()==e['sha256']
original=json.loads((out/'REVIEWER_ORIGINAL_DISPOSITIONS_v1.json').read_text())
for e in original['original_sources']:
 assert hashlib.sha256(Path(e['original_path']).read_bytes()).hexdigest()==e['original_sha256']
res=json.loads((out/'INDEPENDENT_PORT_RESULTS_v1.json').read_text())
assert res['status']=='PASS scoped source port'
counts=res['result_comparison']['scientific_result_leaf_counts']
assert counts['numeric']-counts['booleans_in_numeric_count']==2431
assert counts['other']+counts['booleans_in_numeric_count']==306
note='docs/METRIC_CLOCK_RECONSTRUCTION_BOUNDED_THEOREM_NOTE_2026-10-13.md'
runner='scripts/metric_clock_reconstruction_2026_10_13.py'
cache='logs/runner-cache/metric_clock_reconstruction_2026_10_13.txt'
manifest='docs/audit/data/citation_graph_manifest.json'
receipt={
 'schema':'focused_independent_canonical_port_review/v1',
 'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'reviewer_session':'/root/direct_quantum_visibility_review',
 'source_author':'parent /root',
 'scope':'Complete canonical metric/clock construction, wrapper/controls, initial source preservation and constituent disposition; focused source check only.',
 'disposition':'PASS within stated conditional source/state/readout scope',
 'source_ready':True,'combined_integration_gate_run':False,'landing_authorized':False,
 'formal_audit':False,'retained_status_conferred':False,'new_framework_premise_adopted':False,
 'original_constituent':{'commit':'2f451838e0d58df6b52024dd9db1062f60d8bf2b',
    'tree':'3dde95713fafb4d48c72bcfc673d2d121018cdc5',
    'base':'516cb69d8487ff04f8a48e065d3dcbe71d7dd237','complete_port_path_count':124},
 'canonical_identities':[ident(w/f) for f in [note,runner,cache,manifest]],
 'report':ident(out/'PORT_REVIEW.md'),
 'current_claim_dispositions':ident(out/'CLAIM_DISPOSITIONS_v2.json'),
 'original_constituent_dispositions':ident(out/'REVIEWER_ORIGINAL_DISPOSITIONS_v1.json'),
 'current_port_dispositions':ident(out/'REVIEWER_PORT_DISPOSITIONS_v1.json'),
 'complete_original_file_mapping':{'originals':98,'exact_files':88,'base64_originals':2,
    'local_primary_only':8,'separately_accounted_later_DISPLAY_derivatives':2,
    'all_original_and_initial_port_identities_rechecked_at_completion':True},
 'complete_proof_preservation':{'units':2,'changes':'Markdown heading depth only','full_proof_text_identity_verified':True},
 'runner_transfer':{'original_decorated_functions_identical':17,'canonical_families':14,
    'numeric_leaves_excluding_bool':2431,'other_leaves_including_bool':306,
    'all_original_scientific_result_leaves_unchanged':True,
    'all_canonical_fields_reproduced_in_isolated_CLI':True,
    'false_formula_controls_are_not_source_mutations':True},
 'independent_route':['Exact orbital dyadic Fourier coefficients',
    'Radial inverse-k^4 Green kernel differentiation',
    'Exact rotational polynomial moments',
    'Basis invariant and fixed-G_N algebra',
    'Independent on-shell frequency/angular covariance normalization',
    'Positive integral and exact same-center source cancellation',
    'Reused unchanged prior time-domain clock/phase-space controls',
    'Read full unchanged tensor/scalar report and independent derivation'],
 'CLI_controls':{'default_stdout_repeatable':True,'json_stdout_equals_exclusive_file':True,
    'existing_file_refused_and_unchanged':True,'copied_input_change_changes_current_hash':True,
    'four_successful_executions':True,'one_expected_FileExistsError':True,
    'not_claimed_independent_mathematical_evidence_by_itself':True},
 'source_input_closure':{'runtime_sources':[runner,note],
    'local_helper_runners':[],'repository_theorem_parents':[],
    'external_libraries':['NumPy','SciPy','SymPy','mpmath'],
    'library_versions':json.loads((p/'evidence/CANONICAL_RESULT_v2.json').read_text())['environment'],
    'cache_fingerprint':res['cache']['declared_input_fingerprint']},
 'material_required_author_corrections':[],
 'nonblocking_historical_caveat':'Clock CHECKED_OUTCOME describes reproducing six refinements; underlying immutable review inspected those author refinements rather than independently rerunning them. Canonical note correctly states independent98-channel/32-oscillator reproduction. No additional independent-refinement claim is endorsed.',
 'governance':{'conditional_support':True,'unknown_frontier':True,'five_route_no_go_packet_substantively_triggered':False,
    'reason':'Constructive supplied-action map and scoped algebraic positivity/bounds, no failed-search or route-exhaustion claim.'},
 'failure_history':{'parent_first_JSON_NumPy_bool_failure':'exact failed source and structured record retained; one built-in bool conversion only; first run not pre-frozen',
    'parent_topology_timeout':'120-second timeout preserved; same builder retry successful',
    'independent_scientific_assertion_failures':0,
    'expected_CLI_guard_nonzero_exit':1,
    'reviewer_documentary_issues':['read-only display truncation','incorrect initial cache helper path',
       'initial reviewer claim line ranges corrected in separatev2, original preserved',
       'one no-effect report patch context failure, recorded and corrected']},
 'full_pipeline_run':False,'git_mutations':0,'PR_mutations':0,'merges':0,
 'author_source_edits':0,'subagents_spawned':0,'model_or_settings_changes':0,
 'pending':['same-session final metadata/head/manifest confirmation if changed',
    'parent-owned exact-final-candidate combined mechanical validation'],
 'fixed_deadline_utc':'2026-10-13T16:53:00Z','discovery_cutoff_utc':'2026-10-13T16:38:00Z',
 'reviewer_evidence_inventory_excludes_receipt_itself':True,
 'reviewer_evidence_inventory':[ident(f) for f in sorted(out.rglob('*')) if f.is_file()]
}
target=out/'PORT_REVIEW_RECEIPT_v1.json'
with target.open('x') as f:json.dump(receipt,f,indent=2);f.write('\n')
print(json.dumps({'report':ident(out/'PORT_REVIEW.md'),'receipt':ident(target),
 'reviewer_evidence_files':len(receipt['reviewer_evidence_inventory']),
 'source_readiness':receipt['source_ready'],'combined_gate_run':receipt['combined_integration_gate_run']},indent=2))
