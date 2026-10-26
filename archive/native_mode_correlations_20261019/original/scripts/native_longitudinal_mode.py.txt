"""Fresh 18/24-qubit fixed-width longitudinal diagnostics; no bulk extrapolation."""
from pathlib import Path
import sys
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('.claude/science/physics-loops/native-mode-correlations-20261019/compass_sector_basis.py', '.claude/science/physics-loops/native-mode-correlations-20261019/compass_sector_solve.py', '.claude/science/physics-loops/native-mode-correlations-20261019/longitudinal.py')
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/".claude/science/physics-loops/native-mode-correlations-20261019"))
if __name__=='__main__':
 from longitudinal import main
 main()
