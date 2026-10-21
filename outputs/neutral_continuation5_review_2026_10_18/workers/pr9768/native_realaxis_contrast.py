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
import sys, json, numpy as np, mpmath as mp
ROOT = Path(__file__).resolve().parents[1]
P = ROOT / '.claude/science/physics-loops/neutral-composite-24h-20261018/native'
sys.path.insert(0, str(P))
from neutral_realaxis_model import calc
from neutral_slow_host import host
from scipy.special import ai_zeros
rng = np.random.default_rng(812)
lam = 0.17
F = rng.normal(size=(4, 4))
F = (F + F.T) / 2
S = rng.normal(size=(3, 3))
S = (S + S.T) / 2
T = rng.normal(size=(2, 2))
T = (T + T.T) / 2
V = np.array([[0.0, 0.0], [-1.0, 0.0], [-1.0, -2.0], [0.0, 0.0]])
W = np.zeros((3, 2))
W[0, 0] = -1
Hs = np.block([[S, W], [W.T, T]])
Vbig = np.zeros((4, 5))
Vbig[:, :2] = V
H = np.block([[lam * F, lam ** 2 * Vbig], [lam ** 2 * Vbig.T, lam ** 2 * Hs]])
w = -0.045 + 0.003j
e = w / lam ** 2
z = w / lam
R = np.linalg.inv(z * np.eye(4) - F)
h = np.linalg.inv(e * np.eye(3) - S)[:2, :2]
gs = np.linalg.inv(e * np.eye(2) - T)[0, 0]
hs = h + gs * np.outer(h[:, 0], h[0, :]) / (1 - gs * h[0, 0])
b = V.T @ R[:, 0]
value = 2 * lam * R[0, 0] + 2 * lam ** 2 * b @ np.linalg.solve(np.eye(2) - lam * hs @ V.T @ R @ V, hs @ b)
j = np.zeros(9)
j[0] = -np.sqrt(2) * lam
exact = j @ np.linalg.solve(w * np.eye(9) - H, j)
err = float(abs(value - exact))
_check('P9768:C001', err < 1e-12 and exact.imag < 0)
n = 512
c = np.cos(2 * np.pi * np.arange(n) / n)
E = -2 + 0.2j
free = np.fft.ifft2(1 / (E + 2 * c[:, None] + 2 * c[None, :]))
coords = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1), (2, 0), (-2, 0), (0, 2), (0, -2), (1, 1), (1, -1), (-1, 1), (-1, -1)]
M = np.array([[free[(x - u) % n, (y - v) % n] for u, v in coords] for x, y in coords])
Q = M[5:, 5:] - M[5:, :5] @ np.linalg.solve(M[:5, :5], M[:5, 5:])
U = np.zeros((8, 2))
U[:4, 0] = 0.5
U[4:, 1] = 0.5
brancherr = float(np.max(abs(U.T @ Q @ U - host(E))))
_check('P9768:C002', brancherr < 1e-09)
mp.mp.dps = 40
bs = []
for lam in [0.5, 0.3]:
    f = lam ** 3 / 16
    z = -6 * lam + 0.02j * lam ** 3
    g = 0j
    for n in range(int(16 / f), 0, -1):
        g = 1 / (z - f * (n + 1) - 4 * g)
    bessel = complex(-mp.besselj(2 - z / f, 4 / f) / (2 * mp.besselj(1 - z / f, 4 / f)))
    _check('P9768:C003', abs(g - bessel) < 1e-10 and g.imag < 0)
    bs.append(dict(lam=lam, error=float(abs(g - bessel))))
h = host(-2)
sigma = h[0, 0]
a = sigma / (1 + sigma)
slow = []
for lam in [0.01, 0.001, 0.0001]:
    f = lam ** 2 / 8
    e = -2 + abs(ai_zeros(1)[0][0]) * f ** (2 / 3) + f * (2 + a.real) + 0.1j * lam ** 2
    g = 0j
    for n in range(int(24 * f ** (-1 / 3)), 0, -1):
        g = 1 / (e - f * (n + 2) - g)
    pred = -1 / (1 + sigma) + 1 / (8 * (1 + sigma) ** 2 * (1j * (0.1 - a.imag / 8)))
    slow.append(dict(lam=lam, error=float(abs(g / (1 - g * sigma) - pred))))
_check('P9768:C004', slow[-1]['error'] < 0.0002 and slow[-1]['error'] < slow[0]['error'] / 10)
rows = []
for lam in [0.1, 0.05, 0.025]:
    for beta in [0.03, 0.3]:
        data = [calc(lam, float(x), beta) for x in np.linspace(-0.4, 0.4, 17)]
        _check('P9768:C005', all((d['full'] > 0 and d['base'] > 0 for d in data)))
        _check('P9768:C006', min(data, key=lambda d: abs(d['x']))['contrast'] < 0)
        rows.append(dict(lam=lam, beta=beta, rows=data))
result = dict(status='bounded-support', schur_error=err, upper_branch_error=brancherr, bessel_controls=bs, slow_limit=slow, corrected_model=rows, scope='Specified coefficient models and leading source only; arm deletion is counterfactual; no microscopic signal dominance or observational test')
p = ROOT / 'outputs/native_realaxis_contrast/result.json'
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result))

(Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
