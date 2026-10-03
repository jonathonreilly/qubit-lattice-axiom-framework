"""A27 check 1b: re-cutting the record's own site every tick converges (fine-tick limit) to the
compressed generator QHQ: the recorded site is frozen and acts on its neighbours as a one-site
field.  Supplied toy: open Heisenberg chain H = J sum SWAP_{i,i+1}, N = 7 qubits, record at site 3
locking |r> (random pure state), random possibilities on the other sites.

Also: (i) the identity <r|_3 SWAP_{3,4} |r>_3 = |r><r|_4 (compression = one-site field);
(ii) the compressed generator still moves unrecorded content (magnon group speed);
(iii) per-tick 'stay' weight 1 - ||Q U psi||^2 = tau^2 Var_Q(H) + O(tau^3).
"""
import signal
import numpy as np
from scipy.linalg import expm

signal.alarm(55)
rng = np.random.default_rng(27)
N, site, J = 7, 3, 1.0
I2 = np.eye(2)

def op_on(ops):
    out = np.array([[1.0+0j]])
    for k in range(N):
        out = np.kron(out, ops.get(k, I2))
    return out

def swap(i, j):
    d = 2**N
    S = np.zeros((d, d))
    for b in range(d):
        bits = [(b >> (N-1-k)) & 1 for k in range(N)]
        bits[i], bits[j] = bits[j], bits[i]
        b2 = sum(bit << (N-1-k) for k, bit in enumerate(bits))
        S[b2, b] = 1
    return S

H = sum(J*swap(i, i+1) for i in range(N-1))
r = rng.normal(size=2) + 1j*rng.normal(size=2); r /= np.linalg.norm(r)
Pr = np.outer(r, r.conj())
Q = op_on({site: Pr})

# (i) compression identity, checked on the full space
lhs = Q @ H @ Q
field = op_on({site-1: Pr}) + op_on({site+1: Pr})
rest = sum(J*swap(i, i+1) for i in range(N-1) if site not in (i, i+1))
rhs = Q @ (rest + J*field) @ Q
print("compression identity  ||QHQ - Q(H_rest + J*field)Q|| =", f"{np.linalg.norm(lhs-rhs):.2e}")

# initial state: |r> at the record site, random elsewhere
psi_rest = rng.normal(size=2**(N-1)) + 1j*rng.normal(size=2**(N-1)); psi_rest /= np.linalg.norm(psi_rest)
psi0 = np.zeros(2**N, complex)
for b in range(2**(N-1)):
    hi, lo = b >> (N-1-site), b & ((1 << (N-1-site)) - 1)
    for s in range(2):
        b2 = (hi << (N-site)) | (s << (N-1-site)) | lo
        psi0[b2] += r[s]*psi_rest[b]

t = 1.0
Hc = lhs
psi_c = expm(-1j*Hc*t) @ psi0
print(f"\nfine-tick limit at fixed change-time t = {t}: projected (re-cut every tick) vs compressed")
for n in [10, 100, 1000, 10000]:
    tau = t/n
    U = expm(-1j*H*tau)
    psi = psi0.copy()
    for _ in range(n):
        psi = Q @ (U @ psi)
    surv = np.vdot(psi, psi).real
    dist = np.linalg.norm(psi/np.sqrt(surv) - psi_c)
    print(f"  ticks {n:6d}: survival (record content stayed every tick) {surv:.6f}; "
          f"1-survival {1-surv:.3e}; ||psi_n/|psi_n| - psi_compressed|| {dist:.3e}")

# (iii) per-tick leak vs tau^2 Var
varQ = np.vdot(psi0, H @ H @ psi0).real - np.vdot(psi0, H @ Q @ H @ psi0).real
for tau in [0.1, 0.01]:
    U = expm(-1j*H*tau)
    leak = 1 - np.linalg.norm(Q @ U @ psi0)**2
    print(f"  tau={tau}: one-tick leak {leak:.4e}  vs tau^2 <H(1-Q)H> = {tau*tau*varQ:.4e}")

# (ii) compressed dynamics still moves unrecorded content: magnon (flipped vs aligned emptiness)
# in the sites right of the record; aligned emptiness = |r_perp>, magnon = |r> at site 5.
rp = np.array([-r[1].conjugate(), r[0].conjugate()])
def prod_state(states):
    v = np.array([1.0+0j])
    for s in states:
        v = np.kron(v, s)
    return v
st = [rp]*N; st[site] = r; st[5] = r
phi0 = prod_state(st)
nr = [op_on({k: Pr}) for k in range(N)]
for tt in [0.0, 0.5, 1.0, 1.5]:
    phi = expm(-1j*Hc*tt) @ phi0
    occ = [np.vdot(phi, nr[k] @ phi).real for k in range(N)]
    print(f"  compressed dynamics t={tt}: weight of |r> per site", np.round(occ, 3))
