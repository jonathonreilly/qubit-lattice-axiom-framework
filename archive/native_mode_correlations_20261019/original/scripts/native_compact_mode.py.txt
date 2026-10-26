"""Fresh finite-sector spectrum and bond covariance; no retained or size-selection verdict."""
from pathlib import Path
import sys,json
AUDIT_TIMEOUT_SEC = 1800
AUDIT_INPUT_PATHS = ('.claude/science/physics-loops/native-mode-correlations-20261019/compass_sector_basis.py', '.claude/science/physics-loops/native-mode-correlations-20261019/compass_sector_solve.py', '.claude/science/physics-loops/native-mode-correlations-20261019/exact_cube_poles.py', '.claude/science/physics-loops/native-mode-correlations-20261019/correlations.py', '.claude/science/physics-loops/native-mode-correlations-20261019/independent_control.py', '.claude/science/physics-loops/native-mode-correlations-20261019/diagnostic_controls.py')
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/".claude/science/physics-loops/native-mode-correlations-20261019"))
def main():
 import independent_control,diagnostic_controls,exact_cube_poles
 independent_control.main();diagnostic_controls.main();exact_cube_poles.main()
 data=json.loads((ROOT/'outputs/native_mode_correlations_20261019/exact_cube_poles.json').read_text())
 assert max(data['eigen_residuals'])<1e-7
 assert data['ground_residual']<1e-8
 assert any(max(row[j] for row in data['normalized_probe_weights'])>1e-8 for j in range(1,len(data['lowest_energies'])))
 print('Finite selected-sector spectral and covariance computations completed; finite internal size remains an open research target.')
if __name__=='__main__':main()
