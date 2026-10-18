from pathlib import Path
import sys,json
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native';sys.path.insert(0,str(P))
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/MICROSCOPIC_LARGE_FEATURE_WINDOW_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_window_orbit_control.py','.claude/science/physics-loops/neutral-composite-24h-20261018/native/MICROSCOPIC_GROUND_WINDOW_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/LARGE_BOUND_FEATURE_PROOF.md']
from neutral_window_orbit_control import run_checks
out=dict(status='bounded-support',physical_bit_controls=run_checks(),scope='Exact symmetry/orbit controls supporting analytic uniform local bounds and spectral-window inequality; no finite-lambda full-H spectrum or empirical data')
p=ROOT/'outputs/native_large_feature_microscopic_window/result.json';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
