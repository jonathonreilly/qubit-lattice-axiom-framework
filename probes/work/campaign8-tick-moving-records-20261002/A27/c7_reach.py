"""A27 check 4a: a smooth covariant change is not nearest-neighbour per tick (so Theorem N's
hypothesis fails), yet it moves content.  Supplied toy: Heisenberg chain H = J sum SWAP, N = 9, open.
Weight of the Heisenberg-picture operator e^{iH tau} sz_4 e^{-iH tau} outside the window {3,4,5}
(Hilbert-Schmidt fraction).  Expect ~ C tau^4 for small tau (second-order commutator reaches
distance 2), nonzero for every tau > 0 tested.
"""
import signal
import numpy as np
from scipy.linalg import expm
signal.alarm(55)
N, c0 = 9, 4
D = 2**N
I2 = np.eye(2); sz = np.diag([1.0, -1.0])

def op_on(ops):
    out = np.array([[1.0]])
    for k in range(N):
        out = np.kron(out, ops.get(k, I2))
    return out

def swap(i, j):
    S = np.zeros((D, D))
    for b in range(D):
        bits = [(b >> (N-1-k)) & 1 for k in range(N)]
        bits[i], bits[j] = bits[j], bits[i]
        S[sum(bit << (N-1-k) for k, bit in enumerate(bits)), b] = 1
    return S

H = sum(swap(i, i+1) for i in range(N-1))
w, V = np.linalg.eigh(H)
O0 = op_on({c0: sz})
win = [c0-1, c0, c0+1]

def outside_weight(O):
    # HS projection onto (window algebra) x 1: partial trace over the complement, re-tensor with 1/2^k
    t = O.reshape([2]*(2*N))
    rest = [i for i in range(N) if i not in win]
    in_idx = list(range(2*N))
    for i in rest:
        in_idx[i+N] = in_idx[i]
    out_idx = [i for i in win] + [i+N for i in win]
    red = np.einsum(t, in_idx, out_idx).reshape(8, 8)/2**len(rest)
    # embed back: window qubits are contiguous (3,4,5)
    P = np.kron(np.kron(np.eye(2**win[0]), red), np.eye(2**(N-1-win[-1])))
    return np.linalg.norm(O-P)**2/np.linalg.norm(O)**2

print("tau    outside-window weight    weight/tau^4")
for tau in [0.02, 0.05, 0.1, 0.2, 0.5, 1.0]:
    U = (V*np.exp(-1j*w*tau)) @ V.T
    O = U.conj().T @ O0 @ U
    ow = outside_weight(O)
    print(f"{tau:5.2f}   {ow:.4e}               {ow/tau**4:.4f}")
