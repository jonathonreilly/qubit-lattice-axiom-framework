from pathlib import Path
import sys,json
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native';sys.path.insert(0,str(P))
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/LARGE_FEATURE_MOBILITY_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_mobility_control.py','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_mobility_finite_graph.py','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_threshold_highprecision.py','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_transverse_bound_model.py']
from neutral_mobility_control import run_checks
from neutral_mobility_finite_graph import run_checks as finite_checks
rows=run_checks();finite=finite_checks()
assert rows[0]['curvature_y']<0 and rows[-1]['curvature_y']>0
assert all(r['curvature_z']>0 and r['source_weight_over_lambda2']>0 for r in rows)
out=dict(status='bounded-support',cavity_controls=rows,finite_graph_control=finite,scope='Native K1 curvature and leading source coefficient, not full-H dispersion or empirical scalar test')
p=ROOT/'outputs/native_large_feature_mobility/result.json';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
