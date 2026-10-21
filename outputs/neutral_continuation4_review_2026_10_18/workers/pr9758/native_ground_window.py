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
"""Exact finite controls for plaquette ground manifold and plane-invariant response."""
from pathlib import Path
import sys, json
import numpy as np
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '.claude/science/physics-loops/neutral-composite-24h-20261018/native'))
from neutral_energy_collective import comm, mul

def plaquettes():
    L = 4
    states = np.arange(1 << L * L, dtype=np.uint32)
    bad = np.zeros(len(states), int)
    for x in range(L):
        for y in range(L):
            ids = [x * L + y, (x + 1) % L * L + y, x * L + (y + 1) % L, (x + 1) % L * L + (y + 1) % L]
            parity = np.zeros(len(states), dtype=np.uint32)
            for a in ids:
                parity ^= states >> a & 1
            bad += parity
    good = set(map(int, states[bad == 0]))
    generated = set()
    for a in range(1 << L):
        for b in range(1 << L):
            generated.add(sum((((a >> x ^ b >> y) & 1) << x * L + y for x in range(L) for y in range(L))))
    _check('P9758:native_ground_window:C001', good == generated and len(good) == 2 ** (2 * L - 1))
    checks = 0
    for rx in [1, 2, 3]:
        for ry in [1, 2, 3]:
            corners = [0, rx * L, ry, rx * L + ry]
            par = np.zeros(len(states), dtype=np.uint32)
            count = np.zeros(len(states), int)
            for a in corners:
                par ^= states >> a & 1
            prod = np.zeros(len(states), dtype=np.uint32)
            for x in range(rx):
                for y in range(ry):
                    z = (states >> x * L + y ^ states >> (x + 1) * L + y ^ states >> x * L + y + 1 ^ states >> (x + 1) * L + y + 1) & 1
                    prod ^= z
                    count += z
            _check('P9758:native_ground_window:C002', np.array_equal(prod, par) and np.all(par <= count))
            checks += len(states)
    return dict(transverse_shape=[L, L], configurations=len(states), ground_patterns=len(good), predicted_ground_patterns=2 ** (2 * L - 1), minimum_nonzero_bad_plaquettes=int(min(bad[bad > 0])), rectangle_checks=checks)

def native_response():
    nx = ny = 3
    nz = 9
    idx = lambda x, y, z: (x * ny + y) * nz + z
    H = {}
    planes = []
    for x in range(nx):
        bits = sum((1 << idx(x, y, z) for y in range(ny) for z in range(nz)))
        planes.append((bits, 0))
    for y in range(ny):
        bits = sum((1 << idx(x, y, z) for x in range(nx) for z in range(nz)))
        planes.append((bits, bits))
    for x in range(nx):
        for y in range(ny):
            for z in range(nz):
                a = idx(x, y, z)
                for direction, b in [(0, idx((x + 1) % nx, y, z)), (1, idx(x, (y + 1) % ny, z)), (2, idx(x, y, (z + 1) % nz))]:
                    mask = 1 << a | 1 << b
                    p = (mask, 0) if direction == 0 else (mask, mask) if direction == 1 else (0, mask)
                    H[p] = 1 if direction == 1 else -1
    patterns = set()
    for a in range(1 << nx):
        for b in range(1 << ny):
            patterns.add(sum((1 << idx(x, y, z) for x in range(nx) for y in range(ny) for z in range(nz) if (a >> x ^ b >> y) & 1)))
    patterns = sorted(patterns)
    lookup = {s: i for i, s in enumerate(patterns)}
    C = {(0, 1 << idx(0, 0, 0) | 1 << idx(0, 0, 2)): 1}
    Ck = (0, 1 << idx(1, 1, 4) | 1 << idx(1, 1, 6))
    A = C
    rows = []
    for order in range(5):
        for plane in planes:
            _check('P9758:native_ground_window:C003', not comm(A, {plane: 1}))
        O = {}
        for p, v in A.items():
            q, sign = mul(p, Ck)
            O[q] = O.get(q, 0) + v * sign
        M = np.zeros((len(patterns), len(patterns)), complex)
        for col, s in enumerate(patterns):
            for (x, z), v in O.items():
                row = lookup.get(s ^ x)
                if row is not None:
                    M[row, col] += v * (-1 if (z & s).bit_count() % 2 else 1)
        error = float(np.max(abs(M - np.eye(len(M)) * M[0, 0])))
        _check('P9758:native_ground_window:C004', error == 0)
        rows.append(dict(commutator_order=order, pauli_terms=len(A), ground_restriction_scalar_error=error, scalar=[M[0, 0].real, M[0, 0].imag]))
        if order < 4:
            A = comm(H, A)
    return dict(physical_shape=[nx, ny, nz], physical_qubits=nx * ny * nz, ground_pattern_count=len(patterns), rows=rows, scope='Exact low-order Pauli controls of symmetry/local support, not an order40 computation or a finite-time theorem by enumeration.')

def main():
    result = dict(status='PASS', plaquette_manifold=plaquettes(), native_local_response=native_response(), error_exponents=dict(remainder_global=29, dynamics=13, ground_state_replacement=17, source_tail=29, high_sector_filter=8), scope='Finite combinatorial and native Pauli controls supplement the analytical ground-window theorem; no empirical test or numerical weak-coupling threshold.')
    out = ROOT / 'outputs/native_ground_window/result.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
if __name__ == '__main__':
    main()

print('Assertion evaluations:',_calls,'; PASS counts distinct primary assertion groups; helper assertions are additional uncounted checks.',flush=True)
from pathlib import Path as _Path
import json as _json
(_Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(_json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
