"""One-time root receipt for fully read final released-source comparisons."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,subprocess,time

E=Path(__file__).resolve().parent
D=E/'local-charge-publication-recovery-independent'
F=E/'native-charge-finite-time-independent/publication_comparison_46_47'
h=lambda p:sha256(p.read_bytes()).hexdigest()
def identity(p):
 s=p.stat();return(h(p),s.st_size,s.st_mode,s.st_mtime_ns,s.st_ctime_ns,s.st_ino,s.st_dev,s.st_nlink)
assert h(D/'SEAL.json')=='5bc0355fa7d14e120687927cf014d3adcccc0595328f5617df8b4e80d08aac2d'
assert h(F/'PUBLICATION_COMPARISON_SEAL.json')=='5846abbbf9931aea9abe51949e9074cfa9fd47e17eade05f063d4d770cd035a8'
counts={}
for directory,seal in [(D,'SEAL.json'),(F,'PUBLICATION_COMPARISON_SEAL.json')]:
 rows=json.loads((directory/seal).read_text())['members'];counts[str(directory)]=len(rows)
 for row in rows:
  p=directory/row['path'];assert h(p)==row['sha256'] and p.stat().st_size==row['bytes']
prior=json.loads((E/'LOCAL_CHARGE_OBSERVATION_FINAL47_ROOT_REVIEW.json').read_text())
assert prior['output_byte_exact'] and prior['byte_and_stat_unchanged'] and prior['required_repairs']==[]
assert prior['seal_sha256']==h(F/'PUBLICATION_COMPARISON_SEAL.json')
observed={p for p in D.rglob('*') if p.is_file()}
for row in json.loads((D/'SOURCE_PINS.json').read_text())['members']:observed.add(Path(row['original']))
before={p:identity(p) for p in observed}
program=D/'compare_read_only.py'
assert h(program)=='387d3c4bde61db0a6d791b4a23620d4a8757a4ee5ad339a993d85a9ebcfa1918'
start=datetime.now(timezone.utc).isoformat();tick=time.monotonic()
run=subprocess.run(['python3','-B',str(program)],cwd=D,capture_output=True)
elapsed=time.monotonic()-tick
for p,row in before.items():assert identity(p)==row,str(p)
for suffix,raw in [('stdout.json',run.stdout),('stderr.txt',run.stderr)]:
 with (E/('LOCAL_CHARGE_OBSERVATION_RECOVERY_ROOT_READONLY.'+suffix)).open('xb') as f:f.write(raw)
assert run.returncode==0 and not run.stderr,run.stderr.decode()
assert run.stdout==(D/'COMPARISON02.stdout.json').read_bytes()
data=json.loads(run.stdout)
assert data['original_bytes_unchanged']==332 and data['previously_partial47_chmod_changes']==57
assert [r['non_timing_scalar_leaves'] for r in data['complete_fresh_publication_vs_author_outputs']]==[177399,249500]
report=dict(started_utc=start,elapsed_seconds=elapsed,exit_code=0,
 observed_files=len(before),all_observed_bytes_and_stats_unchanged_during_root_replay=True,
 recovery_comparison_stdout_byte_exact=True,program_sha256=h(program),
 prior_recovery_metadata_exception='57 captured partial47 files were sealed concurrently: only mode0644->0444 and ctime changed. Initial stopped attempt and exact exception preserved; no source bytes changed.',
 sealed_member_counts=counts,complete_reports_new_code_compact_results_and_failed_attempt_diff_read=True,
 original47_final_scope='Part II and branch-compression joins; both complete payloads mechanically compared.',
 recovery_final_scope='Full released-source publication and joins; distinct from interrupted original Part I final approval.',
 new_blind_derivation=False,required_repairs=[],
 final_comparisons=[dict(directory=str(F),seal='PUBLICATION_COMPARISON_SEAL.json',publication_subdirectory='final47',report='PUBLICATION_COMPARISON.md',report_sha256=h(F/'PUBLICATION_COMPARISON.md'),seal_sha256=h(F/'PUBLICATION_COMPARISON_SEAL.json')),
                    dict(directory=str(D),seal='SEAL.json',publication_subdirectory='final_recovery',report='REPORT.md',report_sha256=h(D/'REPORT.md'),seal_sha256=h(D/'SEAL.json'))],
 limitations=['No empirical charge/preparation/detector/scale identification.',
 'K-independent fixed-local-support finite-time bound is not a uniform Fourier-volume or infinite-volume dynamics result.',
 'PRE colored-series formation-factor and Pearson results remain separately attributed.',
 'Original46 interrupted partial final comparison remains preserved and unsealed.'])
with (E/'LOCAL_CHARGE_OBSERVATION_FINAL_ROOT_VERIFICATION.json').open('x') as f:json.dump(report,f,indent=2);f.write('\n')
print(json.dumps(report,indent=2))
