from pathlib import Path
import hashlib,json,datetime
P=Path(__file__).resolve().parent;R=P.parent
def row(f):
 b=f.read_bytes();return dict(path=str(f),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
pre=json.loads((P/'PRE_COMPARISON_SEAL.json').read_text())
for z in pre['sources']+pre['artifacts']:assert row(Path(z['path']))==z
expected={'dimer_two_pair_faithful_encoding_check.py':'07e9dbd7aea660c5cf4bcd36da7dc448e02e479dea99d43c31140d056f5a5c0b','DIMER_TWO_PAIR_FAITHFUL_ENCODING_RESULTS.json':'c2f750b6d59179f8024f509d89350f6c468ff11ee0fbc23691c460799a362fb9','DIMER_TWO_PAIR_FAITHFUL_ENCODING_RUN.log':'a3a672548cca9901b8d4e07860c46e9c7ac91378462a72a35b55cee1d88e8c58','DIMER_TWO_PAIR_FAITHFUL_ENCODING_RUN.stderr':'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855','DIMER_TWO_PAIR_FAITHFUL_ENCODING_RUN_RECEIPT.json':'8b5bfd41ef5b3d139e3680f46d4c854fbb0330b45fcf836e22c1a147129cf1d8'}
sources=[]
for f,h in expected.items():
 z=row(R/f);assert z['sha256']==h;sources.append(z)
(P/'AUTHOR_SOURCES.json').write_text(json.dumps(dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),boundary='After independent seal; complete author code/result/streams/receipt read.',sources=sources),indent=2)+'\n')
a=json.loads((R/'DIMER_TWO_PAIR_FAITHFUL_ENCODING_RESULTS.json').read_text());o=json.loads((P/'INDEPENDENT_RESULTS.json').read_text())
for z in a['sources']:assert row(Path(z['path']))==z
assert json.loads((R/'DIMER_TWO_PAIR_FAITHFUL_ENCODING_RUN.log').read_text())==a
run=json.loads((R/'DIMER_TWO_PAIR_FAITHFUL_ENCODING_RUN_RECEIPT.json').read_text());assert run['returncode']==0 and run['script_sha256']==expected['dimer_two_pair_faithful_encoding_check.py']
assert (R/'DIMER_TWO_PAIR_FAITHFUL_ENCODING_RUN.stderr').read_bytes()==b''
pairs=[('stabilizers','stabilizer_sizes'),('trace_denominators','traces'),('rational_state_column_rank','modular_column_rank'),('affine_probability_rank','affine_rank_mod_prime'),('operator_alternating_multiplicity','alternating_operator_multiplicity'),('hilbert_alternating_multiplicity','alternating_hilbert_multiplicity'),('minimum_eigenvalue_lower_bounds','strict_eigenvalue_lower_bounds'),('cubic_operator_frobenius_square','cubic_density_Frobenius_squared'),('covariance_equalities','exact_covariance_relations')]
for x,y in pairs:assert a[x]==o[y]
assert a['seed_vectors']==[o['integer_seed_A'],o['integer_seed_B']]
assert a['cubic_operator_nonzero'] and o['cubic_operator_nonzero_entries']>0
out=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),author_files_authenticated=5,embedded_sources_authenticated=2,pre_seal_rows_authenticated=8,all_reported_mathematical_values_agree=True,rank_certificate='Independent integer minor determinant 22325 mod65537 certifies the same rational rank14; normalized differences give affine13.',scope='Complete author source/evidence read. No author execution or new rational-rank rerun. Exact saved outputs compared against the independently sealed modular and integer construction. No source correction or unresolved finite-construction claim.')
(P/'COMPARISON_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
