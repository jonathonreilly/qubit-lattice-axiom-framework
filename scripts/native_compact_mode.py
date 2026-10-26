"""Fresh finite-sector spectrum and bond covariance; no retained or size-selection verdict."""
from pathlib import Path
import sys,json
AUDIT_TIMEOUT_SEC = 1800
AUDIT_INPUT_PATHS = ('docs/NATIVE_MODE_CORRELATIONS_OPEN_GATE_NOTE_2026-10-21.md', 'scripts/native_mode_compass_sector_basis.py', 'scripts/native_mode_compass_sector_solve.py', 'scripts/native_mode_exact_cube_poles.py', 'scripts/native_mode_correlations.py', 'scripts/native_mode_independent_control.py', 'scripts/native_mode_diagnostic_controls.py', 'scripts/native_longitudinal_mode.py', 'scripts/native_mode_longitudinal.py')
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
# Companion source is imported for complete packet discovery; its guarded main is not run here.
import native_longitudinal_mode
def main():
 import native_mode_independent_control,native_mode_diagnostic_controls,native_mode_exact_cube_poles
 native_mode_independent_control.main();native_mode_diagnostic_controls.main();native_mode_exact_cube_poles.main()
 data=json.loads((ROOT/'outputs/native_mode_correlations_20261019/exact_cube_poles.json').read_text())
 assert max(data['eigen_residuals'])<1e-7
 assert data['ground_residual']<1e-8
 assert any(max(row[j] for row in data['normalized_probe_weights'])>1e-8 for j in range(1,len(data['lowest_energies'])))
 print('Finite selected-sector spectral and covariance computations completed; finite internal size remains an open research target.')
if __name__=='__main__':main()
