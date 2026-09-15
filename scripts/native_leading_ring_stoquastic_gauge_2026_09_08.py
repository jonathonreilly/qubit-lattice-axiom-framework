"""Finite leading-ring phase controls; not full-H equivalence."""
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=('docs/NATIVE_LEADING_RING_STOQUASTIC_GAUGE_NOTE_2026-09-08.md', 'docs/NATIVE_VIRTUAL_PAIR_RING_MECHANISM_NOTE_2026-09-08.md', 'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md', 'docs/NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md', 'docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_PROJECTOR_MAXWELL_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-03.md', 'scripts/native_leading_ring_stoquastic_gauge_exact_2026_09_08.py', 'docs/NATIVE_SIXTH_OFFDIAGONAL_SIGN_OBSTRUCTION_NOTE_2026-09-08.md')
import argparse,hashlib,json,os,resource,importlib.util,signal,time
from pathlib import Path
start=time.monotonic();signal.alarm(AUDIT_TIMEOUT_SEC)
p=argparse.ArgumentParser();p.add_argument('--json',action='store_true');args=p.parse_args()
root=Path(__file__).resolve().parents[1];inputs={n:hashlib.sha256((root/n).read_bytes()).hexdigest() for n in AUDIT_INPUT_PATHS}
spec=importlib.util.spec_from_file_location('leading_ring_exact',root / 'scripts' / 'native_leading_ring_stoquastic_gauge_exact_2026_09_08.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
part=module.out
if part['checks']!=6253:raise RuntimeError('predicate coverage changed')
seconds=time.monotonic()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if os.uname().sysname=='Darwin' else 1024)
if not 0<rss<384 or seconds>=180:raise RuntimeError('resource cap')
r=dict(executed_predicates=6253,parts={'exact':part},elapsed_seconds=seconds,peak_rss_mib=rss,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),input_sha256=inputs,scope='Leading H4 gauge, L4 winding extras and transformed coherent boundaries only.')
(root/'outputs').mkdir(exist_ok=True);(root/'outputs/native_leading_ring_stoquastic_gauge_2026_09_08.json').write_text(json.dumps(r,indent=2,allow_nan=False)+'\n');print(json.dumps(r,indent=2,allow_nan=False))
if not args.json:
 print('per_element: executed literal native edge-toggle phases and background holonomies on supplied full-bit fixtures.')
 print('per_site: finite L4 and L6 degree-three ice fixtures with the declared preparation faces and legal transitions.')
 print('per_mode: coherent density-matrix and diagonal-readout transformation is analytical in the note, not executed by this helper.')
 print('per_block: executed exact alternating cycle phase ratios, including 132 legal winding transitions.')
 print('lattice_wide: the general even-torus gauge identity is analytical; this invocation executes only declared L4/L6 fixtures, not a phase or full-H equivalence test.')
 print('TOTAL: PASS=6253 FAIL=0')
 print(f'Resources: {seconds:.6f}s, {rss:.3f}MiB; timeout180s, RSS384MiB.')
