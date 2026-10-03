# A39 c2: loophole (b). The entangled (antiferromagnetic) stationary vacuum of the plain
# rule J sigma.sigma with J>0 (C57's light-like comparator) next to a record:
# is the unrecorded part of an edge star full rank? Versus the aligned (J<0) vacuum.
# Record content |0> (Z=+1) at one site; compression turns its bonds into a field J*Z on
# its neighbours (wall strength lam multiplies it). Plus finite-size gap scaling (z) and
# the static structure factor S(k) of the conserved density (Feynman ratio input).
import signal, numpy as np, scipy.sparse as sp
from scipy.sparse.linalg import eigsh
signal.alarm(55)
X = sp.csr_matrix([[0, 1], [1, 0]], dtype=complex); Y = sp.csr_matrix([[0, -1j], [1j, 0]]); Z = sp.csr_matrix([[1, 0], [0, -1]], dtype=complex)
I2 = sp.identity(2, format="csr", dtype=complex)
def op(o, i, n):
    m = sp.identity(1, format="csr", dtype=complex)
    for k in range(n):
        m = sp.kron(m, o if k == i else I2, format="csr")
    return m
def heis(bonds, n, J):
    H = sp.csr_matrix((1 << n, 1 << n), dtype=complex)
    for (i, j) in bonds:
        for o in (X, Y, Z):
            H = H + J*(op(o, i, n) @ op(o, j, n))
    return H
def gs(H, k=1):
    w, v = eigsh(H, k=k, which="SA", tol=1e-12)
    o = np.argsort(w); return w[o], v[:, o]
def marg(psi, keep, n):
    t = psi.reshape([2]*n)
    rest = [a for a in range(n) if a not in keep]
    t = np.transpose(t, list(keep) + rest).reshape(1 << len(keep), -1)
    return t @ t.conj().T
def mineig(r): return np.linalg.eigvalsh(r).min()

print("== 1D ring of 13, site 0 recorded (content Z=+1); unrecorded sites 1..12 -> qubits 0..11 ==")
n = 12
bonds = [(i, i+1) for i in range(n-1)]          # 1-2, ..., 11-12 among unrecorded
for J, lab in ((1.0, "J>0 antiferromagnetic"), (-1.0, "J<0 aligned")):
    for lam in ((1.0, 3.0, 10.0, 30.0) if J > 0 else (1.0,)):
        H = heis(bonds, n, J) + lam*J*(op(Z, 0, n) + op(Z, n-1, n))
        w, v = gs(H, 2); psi = v[:, 0]
        e_star = mineig(marg(psi, [0, 1], n))     # star of site 1 = {0(rec),1,2}: U = {1,2}
        b_star = mineig(marg(psi, [4, 5, 6], n))  # a bulk star {5,6,7}
        print(f"  {lab:24s} wall x{lam:<4}: GS gap to next {w[1]-w[0]:.3e}; edge-star U={{1,2}} min eig {e_star:.3e}; bulk star min eig {b_star:.3e}")

print("== 2D 4x3 torus, site (0,0) recorded (content Z=+1); 11 unrecorded qubits ==")
Lx, Ly = 4, 3
sites = [(x, y) for y in range(Ly) for x in range(Lx)]
rec = (0, 0); free = [s for s in sites if s != rec]; q = {s: k for k, s in enumerate(free)}
n2 = len(free)
bset = set()
for (x, y) in sites:
    for (a, b) in (((x+1) % Lx, y), (x, (y+1) % Ly)):
        bset.add(tuple(sorted([(x, y), (a, b)])))
fb = [(q[a], q[b]) for (a, b) in bset if rec not in (a, b)]
nb = [q[b] if a == rec else q[a] for (a, b) in bset if rec in (a, b)]
for J, lab in ((1.0, "J>0 antiferromagnetic"), (-1.0, "J<0 aligned")):
    H = heis(fb, n2, J) + J*sum(op(Z, k, n2) for k in nb)
    w, v = gs(H, 2); psi = v[:, 0]
    x0 = (1, 0)
    star = [((x0[0]+dx) % Lx, (x0[1]+dy) % Ly) for (dx, dy) in ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1))]
    U = [q[s] for s in star if s != rec]
    print(f"  {lab:24s}: GS gap to next {w[1]-w[0]:.3e}; edge star U ({len(U)} sites) min eig {mineig(marg(psi, U, n2)):.3e}")

print("== finite-size gaps on rings (z check), H = J sum sigma.sigma ==")
for N in (6, 8, 10, 12):
    rb = [(i, (i+1) % N) for i in range(N)]
    wa, _ = gs(heis(rb, N, 1.0), 2)
    da = wa[1]-wa[0]
    df = 4*(1-np.cos(2*np.pi/N))        # aligned: one flip at k=2pi/N, exact 4|J|(1-cos k)
    wf, vf = gs(heis(rb, N, -1.0), N+2)
    gaps = np.unique(np.round(wf - wf[0], 9)); dfn = gaps[gaps > 1e-7][0]
    print(f"  N={N:2d}: antiferromagnetic gap {da:.4f} (gap*N {da*N:.3f});  aligned gap {dfn:.4f} (gap*N^2 {dfn*N*N:.3f}; formula 4(1-cos 2pi/N) = {df:.4f})")

print("== static structure factor of the conserved density, N=12 ring ==")
N = 12; rb = [(i, (i+1) % N) for i in range(N)]
_, va = gs(heis(rb, N, 1.0), 1); psi = va[:, 0]
Zs = [op(Z, i, N) for i in range(N)]
for m in range(1, 4):
    kk = 2*np.pi*m/N
    A = sum(np.exp(1j*kk*i)*Zs[i] for i in range(N))
    S = np.vdot(A @ psi, A @ psi).real/N
    print(f"  antiferromagnetic: k={kk:.3f}  S(k)={S:.4f}  S(k)/k={S/kk:.4f}")
print("  aligned vacuum: S(k) of the flip operator = 1 for all k (product state, EXACT)")
