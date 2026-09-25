#!/usr/bin/env python3
"""Fresh exact author controls for conditional input energy and original mark power."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/ACTUAL_INPUT_ENERGY_AND_ORIGINAL_MARK_POWER_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'docs/LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/WEAK_FIELD_WAVE_PACKETS_FROM_MOBILE_RECORD_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/ORIGINAL_RECORD_CALIBRATION_AND_PREPARED_MATTER_PROBE_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/PREPARED_ORIGINAL_RECORD_PROBE_ENERGY_VACUUM_RESPONSE_AND_CLOCK_SCOPE_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/PHOTON_DISPERSION_OBSERVATIONAL_CONSTRAINTS_AND_LIVE_FORMATION_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/OPTICAL_REFERENCE_ENERGY_LIMITS_FOR_ORIGINAL_RECORD_COUNTS_BOUNDED_THEOREM_NOTE_2026-09-24.md', '.claude/science/physics-loops/mobile-record-input-energy-power-20260925/runtime/energy/prepared_energy_polynomial.py', '.claude/science/physics-loops/mobile-record-input-energy-power-20260925/runtime/energy/energy_spectral_controls.py', '.claude/science/physics-loops/mobile-record-input-energy-power-20260925/runtime/power/selected_power_polynomial.py', '.claude/science/physics-loops/mobile-record-input-energy-power-20260925/runtime/power/power_spectral_controls.py', '.claude/science/physics-loops/mobile-record-input-energy-power-20260925/runtime/power/power_positive_certificate.py')
RESULT_PATH = 'outputs/input_energy_power_20260925/ENERGY_POWER_RESULTS.json'
RUNTIME = ['.claude/science/physics-loops/mobile-record-input-energy-power-20260925/runtime/energy/prepared_energy_polynomial.py', '.claude/science/physics-loops/mobile-record-input-energy-power-20260925/runtime/energy/energy_spectral_controls.py', '.claude/science/physics-loops/mobile-record-input-energy-power-20260925/runtime/power/selected_power_polynomial.py', '.claude/science/physics-loops/mobile-record-input-energy-power-20260925/runtime/power/power_spectral_controls.py', '.claude/science/physics-loops/mobile-record-input-energy-power-20260925/runtime/power/power_positive_certificate.py']

from pathlib import Path
import contextlib,hashlib,json,os,shutil,subprocess,sys,tempfile,time

def main():
    started=time.perf_counter(); root=Path(__file__).resolve().parents[1]
    stages=[]; payload={}
    with tempfile.TemporaryDirectory(prefix='original-energy-power-') as directory:
        tmp=Path(directory)
        for rel in RUNTIME:
            source=root/rel; label=source.parent.name
            target=tmp/label/source.name; target.parent.mkdir(parents=True,exist_ok=True)
            target.write_bytes(source.read_bytes())
        specs=[('energy','prepared_energy_polynomial.py','ENERGY_POLYNOMIAL_RESULTS.json'),
               ('energy','energy_spectral_controls.py','ENERGY_SPECTRAL_RESULTS.json'),
               ('power','selected_power_polynomial.py','POWER_POLYNOMIAL_RESULTS.json'),
               ('power','power_spectral_controls.py','POWER_SPECTRAL_RESULTS.json'),
               ('power','power_positive_certificate.py','POWER_POSITIVE_CERTIFICATE.json')]
        env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
        for label,name,resultname in specs:
            script=tmp/label/name; tic=time.perf_counter()
            process=subprocess.run([sys.executable,str(script)],cwd=script.parent,
                                   capture_output=True,env=env,check=False)
            elapsed=time.perf_counter()-tic
            if process.returncode or process.stderr:
                raise RuntimeError(f'{name}: exit {process.returncode}; '+process.stderr.decode())
            value=json.loads(process.stdout); (script.parent/resultname).write_bytes(process.stdout)
            payload[resultname]=value
            stages.append({'program':name,'code_sha256':hashlib.sha256(script.read_bytes()).hexdigest(),
                           'result':resultname,'stdout_sha256':hashlib.sha256(process.stdout).hexdigest(),
                           'stdout_bytes':len(process.stdout),'stderr_bytes':len(process.stderr),
                           'exit_code':process.returncode,'elapsed_seconds':elapsed})
    result={'scope':'Exact source-reused root controls, independently checked separately; no full dynamics, finite lab error or fit.',
            'payload':payload,'stages':stages,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'elapsed_seconds':time.perf_counter()-started,'all_assertions_passed':True}
    target=root/RESULT_PATH; target.parent.mkdir(parents=True,exist_ok=True)
    data=json.dumps(result,indent=2,allow_nan=False)+'\n';target.write_text(data);print(data,end='')
    print('TOTAL_PASS: 5')

if __name__=='__main__':main()
