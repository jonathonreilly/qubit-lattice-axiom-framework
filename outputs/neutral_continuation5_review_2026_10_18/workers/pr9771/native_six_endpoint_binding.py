import sys as _sys
if _sys.flags.optimize: raise RuntimeError('Optimized Python disables scientific helper assertions')
_sys.stdout.reconfigure(line_buffering=True)
_sys.stderr.reconfigure(line_buffering=True)
_groups=set();_calls=0
def _check(label,condition):
 global _calls
 _calls+=1
 if not bool(condition):
  print('[FAIL]',label,flush=True)
  raise AssertionError(label)
 if label not in _groups:
  _groups.add(label);print('[PASS]',label,flush=True)
from pathlib import Path
import sys, json
ROOT = Path(__file__).resolve().parents[1]
P = ROOT / '.claude/science/physics-loops/neutral-composite-24h-20261018/native'
sys.path.insert(0, str(P))
from neutral_four_interval_certificate import run_all
from neutral_endpoint_cluster_model import run
rows = run_all()
_check('P9771:C001', len(rows) == 15)
D = json.loads((P / 'six_endpoint_integer_trial.json').read_text())
H, states = run(2, 3, 6)
_check('P9771:C002', [list(s) for s in states] == D['states'])
_check('P9771:C003', len(states) == 1459 and H.shape == (1459, 1459))
q = D['integer_trial']
_check('P9771:C004', len(q) == len(states))
_check('P9771:C005', all((type(x) is int for x in q)))
norm = sum((x * x for x in q))
coo = H.tocoo()
num = 0
for i, j, a in zip(coo.row, coo.col, coo.data):
    _check('P9771:C006', int(a) == a)
    num += q[int(i)] * int(a) * q[int(j)]
cert = 10 * num + 71 * norm
_check('P9771:C007', norm == D['norm'] == 9999999925139683)
_check('P9771:C008', num == D['energy_numerator'] == -71308060208219532)
_check('P9771:C009', cert == D['certificate_10H_plus71N'] == -3080607397277827 < 0)
_check('P9771:C010', all((all((s.count(h) % 2 == 0 for h in set(s))) for s in states)))
out = dict(status='bounded-support', four_cluster_interval_certificates=rows, grid_points_per_shape=257, dimension=len(states), norm=norm, energy_numerator=num, exact_certificate=cert, essential_lower_bound=-7, trial_upper_bound=-7.1, scope='Specified native K1 boundary sector only; proof plus interval/integer certificates; not full-H particle or empirical validation')
p = ROOT / 'outputs/native_six_endpoint_binding/result.json'
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out))

(Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
