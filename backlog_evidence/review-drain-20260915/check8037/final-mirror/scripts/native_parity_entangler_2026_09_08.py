"""Live finite operator evidence for the conditional native parity entangler."""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    'docs/NATIVE_PARITY_ENTANGLER_AND_CHSH_NOTE_2026-09-08.md',
    'docs/NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md',
    'scripts/native_parity_entangler_numeric_2026_09_08.py',
    'scripts/native_parity_entangler_exact_2026_09_08.py',
)
from pathlib import Path
import os,time,signal,resource,contextlib,io,importlib.util,json,hashlib,argparse
start=time.monotonic();signal.alarm(AUDIT_TIMEOUT_SEC)
for variable in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[variable]='1'
parser=argparse.ArgumentParser();parser.add_argument('--json',action='store_true');args=parser.parse_args()
root=Path(__file__).resolve().parents[1];(root/'outputs').mkdir(exist_ok=True)
def load_helper(path):
    # Fresh module execution with a static path visible to both packet resolvers.
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module.result

parts = {
    'numeric': load_helper(root / 'scripts' / 'native_parity_entangler_numeric_2026_09_08.py'),
    'exact': load_helper(root / 'scripts' / 'native_parity_entangler_exact_2026_09_08.py'),
}
for name, data in parts.items():
    if data['status']!='PASS' or not data['checks'] or any(type(v) is not bool or not v for v in data['checks'].values()):
        raise RuntimeError('incomplete live evidence')
seconds=time.monotonic()-start
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if os.uname().sysname=='Darwin' else 1024)
if not 0<rss<384 or seconds>=AUDIT_TIMEOUT_SEC:raise RuntimeError('resource contract')
result={'status':'PASS','classification':'conditional-support','parts':parts,'executed_assertions':sum(len(v['checks']) for v in parts.values()),'elapsed_seconds':seconds,'peak_rss_mib':rss,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Finite native physical matrix construction; preparation, signed hopping controls, Born Record schedule and CHSH settings supplied. Nonbridge lemma is analytic.'}
(root/'outputs/native_parity_entangler_2026_09_08.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
print(json.dumps(result,indent=2,allow_nan=False))
if not args.json:
    print('per_element: executed full complex success and failure columns on all four input basis states; both middle Z outcomes retained.')
    print('per_site: executed the eight-dimensional carrier of three physical edge qubits; midpoint placement and control admissibility supplied.')
    print('per_mode: executed four even-parity modes, crossed input rails, regrouped output rails and the complete prepared Bell vector.')
    print('per_block: executed numeric and independent exact full instrument, witness spectrum and all four CHSH correlations on the finite three-qubit block.')
    print('lattice_wide: checked and not executed — nonbridge scope is analytic; no spatial scaling, occurrence dynamics or arbitrary protocol simulation.')
    print(f"TOTAL: PASS={result['executed_assertions']} FAIL=0")
    print(f'Resources: {seconds:.6f}s, {rss:.3f}MiB; timeout180s, RSS384MiB.')
