"""R15-3 s4: the two non-local six-pair symbols, counted under the strict (N1) partner definition.
X1: H = 1/2 E:E + 1/2 h:[L(k) P_TT(k)]:h            (R14-4's 'symbol that works', C^1 not C^2 at k=0; continuous)
X2: H = 1/2 E:E + 1/2 h:[L(k) + m^2 (1 - P_TT(k))]:h  (O(1) direction-dependent mass; DIScontinuous at k=0)
L(k) = sum_i 2(1-cos k_i). Gapless = frequency -> 0 as |k| -> 0 (flat zero modes included)."""
import numpy as np
from common import tt_projector
def freqs(H):
    n = H.shape[0] // 2
    J = np.block([[np.zeros((n, n)), np.eye(n)], [-np.eye(n), np.zeros((n, n))]])
    om = (1j * np.linalg.eigvals(J @ H)).real
    return np.sort(om[om > -1e-9])
rng = np.random.default_rng(0)
dirs = [np.array([0, 0, 1.]), np.array([1, 1, 1.]) / np.sqrt(3), np.array([1, 1, 0.]) / np.sqrt(2)] + [d / np.linalg.norm(d) for d in rng.normal(size=(3, 3))]
for name in ["X1", "X2"]:
    print(f"== {name} ==")
    for d in dirs:
        row = []
        for t in (1e-3, 2e-3):
            k = t * d; L = np.sum(2 * (1 - np.cos(k))); PT = tt_projector(d)
            V = L * PT if name == "X1" else L * np.eye(6) + 1.0 * (np.eye(6) - PT)
            H = np.block([[V, np.zeros((6, 6))], [np.zeros((6, 6)), np.eye(6)]])
            om = freqs(H)
            row.append(om)
        om1, om2 = row
        gl = om1[om1 < 0.05]
        nz = int(np.sum(gl < 1e-7)); nlin = int(np.sum(gl > 1e-7))
        print(f"  dir {np.round(d,3)}: gapless branches {nlin + nz//2} = {nlin} linear + {nz//2} flat (free-particle Jordan pairs: {nz} zero eigenvalues of JH); omega/|k| of linear ones {np.round(gl[gl>1e-7]/1e-3,5)}; lowest gapped {np.round(om1[len(gl)],4) if len(gl) < len(om1) else None}")
# discontinuity of X2 at k=0: compare the symbol along two directions at |k| = 1e-8
a = 1.0 * (np.eye(6) - tt_projector([0, 0, 1])); b = 1.0 * (np.eye(6) - tt_projector([1, 0, 0]))
print("X2: ||H(1e-8 z) - H(1e-8 x)|| =", np.round(np.linalg.norm(a - b), 4), "(does not vanish as |k| -> 0: discontinuous)")
