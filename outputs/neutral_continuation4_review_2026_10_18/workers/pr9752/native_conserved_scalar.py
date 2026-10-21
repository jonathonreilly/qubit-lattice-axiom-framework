import sys as _sys
if _sys.flags.optimize: raise RuntimeError("Optimized Python disables scientific helper assertions")
_sys.stdout.reconfigure(line_buffering=True)
_sys.stderr.reconfigure(line_buffering=True)
_groups=set(); _calls=0
def _check(label, condition):
 global _calls
 _calls+=1
 if not bool(condition):
  print('[FAIL]',label,flush=True)
  print(f'TOTAL: PASS={len(_groups)} FAIL=1',flush=True)
  raise AssertionError(label)
 if label not in _groups:
  _groups.add(label);print('[PASS]',label,flush=True)
"""Native Pauli fluctuation/coupling identities; supplied statistical states."""
from pathlib import Path
import sys, json, numpy as np
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '.claude/science/physics-loops/neutral-composite-24h-20261018/native'))
from neutral_energy_collective import run
from neutral_energy_qnorm import polynomial
from neutral_energy_thermal import run as thermal

def main():
    r = run()
    p = polynomial()
    t = thermal()
    rows = []
    _check('P9752:native_conserved_scalar:C001', p['at_zero'] == 5376 and abs(r['conserved_fraction'] - 4 / 7) < 1e-14)
    for q in [0.1, 0.01, 0.001]:
        h = np.cos(q / 2)
        N = 3072 + 1280 * np.cos(q) + 1024 * h
        g = -(32 / 3) * (2 * h + 1)
        m2 = 64 * (1 - h)
        Omega = 10 * q
        bound = max(0, abs(g) * np.sqrt(3 / N) - np.sqrt(m2 / (3 * Omega ** 2))) ** 2
        _check('P9752:native_conserved_scalar:C002', 0 < bound < 4 / 7)
        rows.append(dict(q=q, window=Omega, rigorous_fraction_lower_bound=float(bound)))
    result = dict(status='PASS', native=r, qnorm=p, thermal_control=t, low_window=rows, scope='Exact fluctuation statements in supplied beta0 state; highT finite-volume Taylor control only. No nonzero beta0 retarded response, vacuum particle, physical detector or cosmological identification.')
    out = ROOT / 'outputs/native_conserved_scalar/result.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
if __name__ == '__main__':
    main()

print('Assertion evaluations:',_calls,'; PASS counts distinct primary assertion groups; helper assertions are additional uncounted checks.',flush=True)
from pathlib import Path as _Path
import json as _json
(_Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(_json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
