"""A27 extra check: does a record sitting in a quiet aligned emptiness |n...n> disturb it?
Supplied 1D toy, sites 0..4, record at 2 with content r; emptiness |n> elsewhere.
 (a) compressed Heisenberg change for time tau: neighbours feel the field J|r><r|.
 (b) one tick of three swap-relocation (SW) variants, 1D weight c/2 per direction:
     SW-content : W_y = beta + (alpha-beta)|r><r|_y
     SW-blind   : W_y = 1
     SW-activity: W_y = singlet projector on (y, y's other neighbour)  [annihilates aligned states]
Measured: total weight off the emptiness on the unrecorded sites, sum_s (1 - <n|rho_s|n>),
summed over outcome branches (record position tracked).
"""
import signal
import numpy as np
from scipy.linalg import expm
signal.alarm(55)
rng = np.random.default_rng(9)
N = 5; D = 2**N; x0 = 2
I2 = np.eye(2)

def op_on(ops):
    out = np.array([[1.0+0j]])
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

def sqrtm_psd(A):
    w, V = np.linalg.eigh(A)
    return (V*np.sqrt(np.clip(w, 0, None))) @ V.conj().T

def red1(rho, keep):
    t = rho.reshape([2]*(2*N)); idx = list(range(2*N))
    for i in range(N):
        if i != keep:
            idx[i+N] = idx[i]
    return np.einsum(t, idx, [keep, keep+N])

def unit(v):
    return v/np.linalg.norm(v)

S = {(i, j): swap(i, j) for i in range(N) for j in range(N) if i != j}
sw2 = np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1.0]])
Ps2 = (np.eye(4) - sw2)/2

def pair_op(i, j, M):  # M on (i, j) with i < j adjacent
    assert j == i+1
    return np.kron(np.kron(np.eye(2**i), M), np.eye(2**(N-j-1)))

def off_emptiness(branches, n):
    Pn = np.outer(n, n.conj())
    tot = 0
    for pos, rho in branches:
        for s in range(N):
            if s != pos:
                tot += np.real(np.trace(rho)) - np.real(np.trace(Pn @ red1(rho, s)))
    return tot

r = unit(rng.normal(size=2) + 1j*rng.normal(size=2))
rperp = np.array([-r[1].conjugate(), r[0].conjugate()])
cases = {"n generic": unit(rng.normal(size=2) + 1j*rng.normal(size=2)), "n = r_perp": rperp, "n = r": r}
H = sum(S[(i, i+1)] for i in range(N-1))
alpha, beta, c, tau = 0.15, 0.85, 0.6, 0.3
for name, n in cases.items():
    st = [n]*N; st[x0] = r
    psi = st[0]
    for s in st[1:]:
        psi = np.kron(psi, s)
    rho = np.outer(psi, psi.conj())
    Q = op_on({x0: np.outer(r, r.conj())})
    U = expm(-1j*tau*(Q @ H @ Q))
    rho_t = U @ rho @ U.conj().T
    field = off_emptiness([(x0, rho_t)], n)
    out = {}
    for var in ["content", "blind", "activity"]:
        W = {}
        for y, z in [(1, 0), (3, 4)]:
            if var == "content":
                W[y] = op_on({y: beta*I2 + (alpha-beta)*np.outer(r, r.conj())})
            elif var == "blind":
                W[y] = np.eye(D)
            else:
                W[y] = pair_op(min(y, z), max(y, z), Ps2)
        Ks = sqrtm_psd(np.eye(D) - (c/2)*(W[1] + W[3]))
        br = [(x0, Ks @ rho @ Ks.conj().T)]
        for y in (1, 3):
            K = np.sqrt(c/2)*S[(x0, y)] @ sqrtm_psd(W[y])
            br.append((y, K @ rho @ K.conj().T))
        out[var] = off_emptiness(br, n)
    print(f"{name:11s}: |<r|n>|^2={abs(np.vdot(r, n))**2:.3f}  field from compressed change (tau={tau}) {field:.2e}; "
          f"SW-content {out['content']:.2e}, SW-blind {out['blind']:.2e}, SW-activity {out['activity']:.2e}")
