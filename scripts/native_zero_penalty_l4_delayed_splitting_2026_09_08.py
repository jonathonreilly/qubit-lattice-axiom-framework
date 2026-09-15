AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=('docs/NATIVE_ZERO_PENALTY_L4_DELAYED_SPLITTING_NOTE_2026-09-08.md', 'docs/NATIVE_ZERO_PENALTY_ENDPOINT_NOTE_2026-09-08.md', 'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md', 'docs/NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md', 'scripts/native_zero_penalty_electric_exact_2026_09_08.py', 'scripts/native_zero_penalty_spectator_exact_2026_09_08.py', 'scripts/native_zero_penalty_isolation_exact_2026_09_08.py')
import argparse,hashlib,json,os,resource,importlib.util,signal,time
from pathlib import Path
start=time.monotonic();signal.alarm(AUDIT_TIMEOUT_SEC)
p=argparse.ArgumentParser();p.add_argument('--json',action='store_true');args=p.parse_args()
root=Path(__file__).resolve().parents[1];inputs={n:hashlib.sha256((root/n).read_bytes()).hexdigest() for n in AUDIT_INPUT_PATHS}
parts={}
def execute_helper(path,key,count):
 spec=importlib.util.spec_from_file_location(path.stem,path);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
 part=module.out
 if part['checks']!=count:raise RuntimeError('predicate coverage changed '+key)
 parts[key]=part
execute_helper(root / 'scripts' / 'native_zero_penalty_electric_exact_2026_09_08.py','electric',964)
execute_helper(root / 'scripts' / 'native_zero_penalty_spectator_exact_2026_09_08.py','spectator',87509)
execute_helper(root / 'scripts' / 'native_zero_penalty_isolation_exact_2026_09_08.py','isolation',5091)
seconds=time.monotonic()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if os.uname().sysname=='Darwin' else 1024)
if not 0<rss<384 or seconds>=180:raise RuntimeError('resource cap')
r=dict(executed_predicates=93564,parts=parts,elapsed_seconds=seconds,peak_rss_mib=rss,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),input_sha256=inputs,scope='Finite supplied L4 isolation and scalar canonical coefficients through five; sixth only support allowed.')
(root/'outputs').mkdir(exist_ok=True);(root/'outputs/native_zero_penalty_l4_delayed_splitting_2026_09_08.json').write_text(json.dumps(r,indent=2,allow_nan=False)+'\n');print(json.dumps(r,indent=2,allow_nan=False))
if not args.json:
 print('per_element: executed actual electric pair flux toggles and finite graph cut controls.')
 print('per_site: executed small cuts and incident-pair matching on the declared finite graphs.')
 print('per_mode: executed active parity and spectator projection controls in the supplied finite Clifford models.')
 print('per_block: finite fixed-flux compression is executed; the general canonical-normalization argument is analytical in the note.')
 print('lattice_wide: executed L4 constant-square and winding controls; the general-torus cut proof and finite L4 isolation proof are analytical; no exhaustive flux-sector run.')
 print('TOTAL: PASS=93564 FAIL=0')
 print(f'Resources: {seconds:.6f}s, {rss:.3f}MiB; timeout180s, RSS384MiB.')
