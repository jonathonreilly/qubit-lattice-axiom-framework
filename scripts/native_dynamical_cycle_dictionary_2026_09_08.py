"""Live finite evidence for the full native CAR/Z2 Gauss dictionary."""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md',
    'docs/NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md',
    'docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_PROJECTOR_MAXWELL_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-03.md',
    'docs/THE_FERMIONS_U1_COUPLED_TO_QUANTUM_LINKS_GAUSS_LAW_AS_A_SUPPORT_CONDITION_AMONG_RECORDS_BOUNDED_THEOREM_NOTE_2026-09-03.md',
    'scripts/native_dynamical_cycle_dictionary_author_2026_09_08.py',
    'scripts/native_dynamical_cycle_dictionary_independent_2026_09_08.py',
    'scripts/native_dynamical_cycle_dictionary_exchange_2026_09_08.py',
)
from pathlib import Path
import os,time,signal,resource,argparse,importlib.util,contextlib,io,json,hashlib,math
start=time.monotonic();signal.alarm(AUDIT_TIMEOUT_SEC)
for variable in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[variable]='1'
parser=argparse.ArgumentParser();parser.add_argument('--json',action='store_true');args=parser.parse_args()
root=Path(__file__).resolve().parents[1]
inputs={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS}
def load_helper(path):
    # Execute fresh modules with literal paths visible to both packet resolvers.
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module.result

parts = {
    'author': load_helper(root / 'scripts' / 'native_dynamical_cycle_dictionary_author_2026_09_08.py'),
    'independent': load_helper(root / 'scripts' / 'native_dynamical_cycle_dictionary_independent_2026_09_08.py'),
    'exchange': load_helper(root / 'scripts' / 'native_dynamical_cycle_dictionary_exchange_2026_09_08.py'),
}
if parts['author']['checks']!=6712:raise RuntimeError('author coverage changed')
if parts['independent']['exact_matrix_groups']!=15 or parts['independent']['Gauss_dimension']!=64 or parts['independent']['missing_phase_failures']!=6:
    raise RuntimeError('independent dictionary coverage changed')
if parts['exchange']['accepted_star_patterns']!=1188 or parts['exchange']['nonzero_exchange_domains']!=2 or parts['exchange']['unsigned_identity_failures']!=2 or parts['exchange']['nonalternating_face_patterns']!=14:
    raise RuntimeError('independent exchange coverage changed')
def finite(value):
    if isinstance(value,float) and not math.isfinite(value):raise RuntimeError('nonfinite evidence')
    if isinstance(value,dict):
        for item in value.values():finite(item)
    if isinstance(value,(list,tuple)):
        for item in value:finite(item)
finite(parts)
seconds=time.monotonic()-start
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if os.uname().sysname=='Darwin' else 1024)
if not 0<rss<384 or seconds>=180:raise RuntimeError('resource contract')
result={'status':'PASS','classification':'conditional-support','parts':parts,'executed_assertions':6712+15+2+1188+2,'elapsed_seconds':seconds,'peak_rss_mib':rss,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'input_sha256':inputs,'scope':'Exact constrained Z2 dictionary and finite local charged-exchange controls; no U1, phase-of-matter or axiom-selection conclusion.'}
(root/'outputs').mkdir(exist_ok=True)
(root/'outputs/native_dynamical_cycle_dictionary_2026_09_08.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
print(json.dumps(result,indent=2,allow_nan=False))
if not args.json:
    print('per_element: native A, B and physical Z are intertwined with constrained CAR/link operators.')
    print('per_site: mathematical enlarged variables add no physical site role or nearest-neighbor implementation.')
    print('per_mode: m CAR modes obey all m Gauss constraints and even total parity.')
    print('per_block: five author graph fixtures, independent pentagon/chord and local exchange controls.')
    print('lattice_wide: checked and not executed — finite-graph theorem proved analytically; no lattice-wide numerical execution, large-volume phase, formation law or selected Hamiltonian.')
    print(f"TOTAL: PASS={result['executed_assertions']} FAIL=0")
    print(f'Resources: {seconds:.6f}s, {rss:.3f}MiB; timeout180s, RSS384MiB.')
