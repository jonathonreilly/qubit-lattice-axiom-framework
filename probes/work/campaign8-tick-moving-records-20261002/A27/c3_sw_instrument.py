"""A27 checks 1-2: the swap-relocation (SW) move instrument on a 3D star (7 qubits).

Record at the centre (site 0) locking |r>; six empty neighbours 1..6 = +x,-x,+y,-y,+z,-z.
  G(r) = beta*1 + (alpha-beta)|r><r|            (neighbour weight, built from the record's content)
  K_y  = sqrt(c/6) SWAP_{0y} sqrt(G(r))_y         (record steps to y; y's cut possibility moves to 0)
  K_0  = sqrt(1 - (c/6) sum_y G(r)_y)             (record stays)
Checks: completeness; covariance under the 24 soldered rotations; 'unglued' tests (spatial rotation
alone, internal rotation alone); odds = (c/6) tr(G rho_y); back-action (coherence of a neighbour's
possibility, tracked wherever it ends) = 1 - (c/12)(sqrt(alpha)-sqrt(beta))^2 + O(c^2).
Contrast: A1 D23 lock-and-move K_v = 3^{-1/2} SWAP_{0,y(v)} (P_v)_0 (glued).
"""
import signal, itertools
import numpy as np

signal.alarm(55)
rng = np.random.default_rng(2727)
N = 7
D = 2**N
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1.0+0j, -1])
I2 = np.eye(2)
dirs = [np.array(v) for v in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]]

def op_on(ops):
    out = np.array([[1.0+0j]])
    for k in range(N):
        out = np.kron(out, ops.get(k, I2))
    return out

def perm_op(pi):  # pi: dict site->site (qubit at site i moves to site pi[i])
    P = np.zeros((D, D))
    for b in range(D):
        bits = [(b >> (N-1-k)) & 1 for k in range(N)]
        nb = [0]*N
        for i in range(N):
            nb[pi[i]] = bits[i]
        P[sum(bit << (N-1-k) for k, bit in enumerate(nb)), b] = 1
    return P

SW = {y: perm_op({**{i: i for i in range(N)}, 0: y, y: 0}) for y in range(1, 7)}

def su2_from_R(R):
    # find U with U (n.sigma) U^dag = (R n).sigma via quaternion (Shepperd)
    t = np.trace(R)
    if t > 0:
        s = np.sqrt(t+1)*2; w = s/4; x = (R[2,1]-R[1,2])/s; y = (R[0,2]-R[2,0])/s; z = (R[1,0]-R[0,1])/s
    elif R[0,0] > R[1,1] and R[0,0] > R[2,2]:
        s = np.sqrt(1+R[0,0]-R[1,1]-R[2,2])*2; w = (R[2,1]-R[1,2])/s; x = s/4; y = (R[0,1]+R[1,0])/s; z = (R[0,2]+R[2,0])/s
    elif R[1,1] > R[2,2]:
        s = np.sqrt(1+R[1,1]-R[0,0]-R[2,2])*2; w = (R[0,2]-R[2,0])/s; x = (R[0,1]+R[1,0])/s; y = s/4; z = (R[1,2]+R[2,1])/s
    else:
        s = np.sqrt(1+R[2,2]-R[0,0]-R[1,1])*2; w = (R[1,0]-R[0,1])/s; x = (R[0,2]+R[2,0])/s; y = (R[1,2]+R[2,1])/s; z = s/4
    return w*I2 - 1j*(x*sx + y*sy + z*sz)

rots = []
for p in itertools.permutations(range(3)):
    for sg in itertools.product([1, -1], repeat=3):
        R = np.zeros((3, 3))
        for i in range(3):
            R[p[i], i] = sg[i]
        if np.linalg.det(R) > 0:
            rots.append(R)
assert len(rots) == 24
pauli = [sx, sy, sz]
maxlift = 0
for R in rots:
    U = su2_from_R(R)
    for a in range(3):
        rhs = sum(R[b, a]*pauli[b] for b in range(3))
        maxlift = max(maxlift, np.abs(U @ pauli[a] @ U.conj().T - rhs).max())
print(f"24 rotations, SU(2) lift error {maxlift:.1e}")

def bloch(v):
    return np.real([np.vdot(v, s @ v) for s in pauli])

def proj(v):
    return np.outer(v, v.conj())

def sqrtm_psd(A):
    w, V = np.linalg.eigh(A)
    return (V*np.sqrt(np.clip(w, 0, None))) @ V.conj().T

def sw_kraus(r, alpha, beta, c):
    G = beta*I2 + (alpha-beta)*proj(r)
    sG = sqrtm_psd(G)
    K = {y: np.sqrt(c/6)*SW[y] @ op_on({y: sG}) for y in range(1, 7)}
    K[0] = sqrtm_psd(np.eye(D) - (c/6)*sum(op_on({y: G}) for y in range(1, 7)))
    return K

def d23_kraus():
    K = {}
    for y in range(1, 7):
        v = dirs[y-1]
        Pv = 0.5*(I2 + sum(v[a]*pauli[a] for a in range(3)))
        K[y] = SW[y] @ op_on({0: Pv})/np.sqrt(3)
    return K

def site_perm_of(R):
    pi = {0: 0}
    for i, v in enumerate(dirs):
        w = R @ v
        j = [k for k, u in enumerate(dirs) if np.allclose(u, w)][0]
        pi[i+1] = j+1
    return pi

def rand_state1():
    v = rng.normal(size=2) + 1j*rng.normal(size=2)
    return v/np.linalg.norm(v)

alpha, beta, c = 0.15, 0.85, 0.6
dev_comp = dev_cov = dev_sp = dev_int = 0.0
d23_comp = d23_cov = d23_sp = d23_int = 0.0
Kd = d23_kraus()
d23_comp = np.abs(sum(k.conj().T @ k for k in Kd.values()) - np.eye(D)).max()
for trial in range(3):
    r = rand_state1()
    K = sw_kraus(r, alpha, beta, c)
    dev_comp = max(dev_comp, np.abs(sum(k.conj().T @ k for k in K.values()) - np.eye(D)).max())
    for R in rots:
        U = su2_from_R(R)
        pi = site_perm_of(R)
        P = perm_op(pi)
        UN = op_on({k: U for k in range(N)})
        V = P @ UN
        Kr = sw_kraus(U @ r, alpha, beta, c)
        for y in range(7):
            ty = pi[y]
            dev_cov = max(dev_cov, np.abs(V @ K[y] @ V.conj().T - Kr[ty]).max())
            dev_sp = max(dev_sp, np.abs(P @ K[y] @ P.T - K[ty]).max())          # spatial rotation alone
        if trial == 0:
            for y in range(1, 7):
                ty = pi[y]
                d23_cov = max(d23_cov, np.abs(V @ Kd[y] @ V.conj().T - Kd[ty]).max())
                d23_sp = max(d23_sp, np.abs(P @ Kd[y] @ P.T - Kd[ty]).max())
    # internal rotation alone (random SU(2) on every qubit, content rotated, sites fixed)
    for _ in range(5):
        A = rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2))
        Uq, _r = np.linalg.qr(A)
        UN = op_on({k: Uq for k in range(N)})
        Kr = sw_kraus(Uq @ r, alpha, beta, c)
        for y in range(7):
            dev_int = max(dev_int, np.abs(UN @ K[y] @ UN.conj().T - Kr[y]).max())
        if trial == 0:
            for y in range(1, 7):
                d23_int = max(d23_int, np.abs(UN @ Kd[y] @ UN.conj().T - Kd[y]).max())
print(f"SW : completeness {dev_comp:.1e}; 24-rotation covariance {dev_cov:.1e}; "
      f"spatial-alone {dev_sp:.1e}; internal-alone {dev_int:.1e}")
print(f"D23: completeness {d23_comp:.1e}; 24-rotation covariance {d23_cov:.1e}; "
      f"spatial-alone {d23_sp:.2f}; internal-alone {d23_int:.2f}   (nonzero = glued)")

# Odds: SW depends on the neighbours' possibilities; D23 does not.
r = rand_state1()
K = sw_kraus(r, alpha, beta, c)
psi_n = rng.normal(size=2**6) + 1j*rng.normal(size=2**6); psi_n /= np.linalg.norm(psi_n)
psi = np.kron(r, psi_n)
rho = np.outer(psi, psi.conj())
G = beta*I2 + (alpha-beta)*proj(r)
maxdiff = 0
for y in range(1, 7):
    p = np.real(np.trace(K[y] @ rho @ K[y].conj().T))
    pred = (c/6)*np.real(np.trace(op_on({y: G}) @ rho))
    maxdiff = max(maxdiff, abs(p-pred))
print(f"SW odds = (c/6) tr(G rho_y) on a random linked star: max error {maxdiff:.1e}")
pd = [np.real(np.trace(Kd[y] @ rho @ Kd[y].conj().T)) for y in range(1, 7)]
nr = bloch(r)
pred_d = [(1 + nr @ dirs[y-1])/6 for y in range(1, 7)]
print(f"D23 odds = (1 + n_r.v)/6 whatever the neighbours hold: max error {max(abs(a-b) for a, b in zip(pd, pred_d)):.1e}")

# Back-action: neighbour 1 holds a|r> + b|r_perp>, others hold |r_perp> or a random mix.
def coherence_factor(alpha, beta, c, others):
    r = np.array([1.0+0j, 0]); rp = np.array([0, 1.0+0j])
    a, b = np.sqrt(0.3), np.sqrt(0.7)*np.exp(0.4j)
    K = sw_kraus(r, alpha, beta, c)
    st = [r, a*r + b*rp] + others
    psi = st[0]
    for s in st[1:]:
        psi = np.kron(psi, s)
    total = 0
    for y, k in K.items():
        phi = k @ psi
        content_site = 0 if y == 1 else 1        # where neighbour 1's possibility sits afterwards
        t = phi.reshape([2]*N)
        rho1 = np.tensordot(t, t.conj(), axes=([i for i in range(N) if i != content_site],)*2)
        total += rho1[0, 1]
    return abs(total)/abs(a*np.conj(b))

rp = np.array([0, 1.0+0j])
for (al, be) in [(0.15, 0.85), (0.0, 1.0), (0.5, 0.5), (1.0, 1.0)]:
    for cc in [0.6, 0.06]:
        others = [rp]*5
        f = coherence_factor(al, be, cc, others)
        others2 = [rand_state1() for _ in range(5)]
        f2 = coherence_factor(al, be, cc, others2)
        print(f"alpha={al:.2f} beta={be:.2f} c={cc:.2f}: coherence kept {f:.6f} (others empty), "
              f"{f2:.6f} (others random); first-order formula {1-(cc/12)*(np.sqrt(al)-np.sqrt(be))**2:.6f}")
