"""Fresh 18/24-qubit fixed-width longitudinal diagnostics; no bulk extrapolation."""
from pathlib import Path
import sys
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/NATIVE_MODE_CORRELATIONS_OPEN_GATE_NOTE_2026-10-21.md', 'scripts/native_mode_compass_sector_basis.py', 'scripts/native_mode_compass_sector_solve.py', 'scripts/native_mode_longitudinal.py')
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
if __name__=='__main__':
 from native_mode_longitudinal import main
 main()
