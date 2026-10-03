"""A30 q2_seal: is a jam sealed against quiet emptiness under Option R? (supplied toy)

Chain: sites 0..2 recorded (the jam), content r; sites 3..12 unrecorded (10 qubits), start
in the aligned emptiness |n>^(x) with n = |0>.  Between ticks: compressed Heisenberg change
H_R = Q (J sum SWAP) Q, i.e. J sum_{bonds in 3..12} SWAP + J |r><r|_3 (+ const).
Per-tick odds (A27 SW and A9 formation, all linear in the possibilities):
  step (SW-content, beta = 0):  (c/z) alpha <r|rho_3|r>
  step (SW-blind):              c/z
  step (SW-activity):           (c/z) <P_singlet(3,4)>     (the other neighbour of 3 is 4)
  formation (quiet weight that locks 'occupied' = -n):  f <1|rho_3|1>
Reported: max over the run of each odds/(prefactor), and how far the emptiness moved.
Contents tested: r = -n (|1>), r = n (|0>), r off-axis at angle theta.
Plus the 2D notch case for the activity weight, by hand-built compression.
"""
import signal
import numpy as np
from scipy.sparse.linalg import expm_multiply
import scipy.sparse as sp

signal.alarm(55)
J = 1.0
L = 10                       # unrecorded sites 3..12 -> qubits 0..9 here
dim = 2 ** L


def op_site(o, i):
    mats = [sp.identity(2, format='csr')] * L
    mats[i] = sp.csr_matrix(o)
    out = mats[0]
    for m in mats[1:]:
        out = sp.kron(out, m, format='csr')
    return out


X = np.array([[0, 1], [1, 0]], dtype=complex)
Yp = np.array([[0, -1j], [1j, 0]])
Z = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2)
SW = 0.5 * (np.kron(I2, I2) + np.kron(X, X) + np.kron(Yp, Yp) + np.kron(Z, Z)).real


def swap_bond(i):
    # SWAP on qubits i, i+1 (adjacent)
    left = sp.identity(2 ** i, format='csr')
    right = sp.identity(2 ** (L - i - 2), format='csr')
    return sp.kron(sp.kron(left, sp.csr_matrix(SW)), right, format='csr')


Hbulk = sum(J * swap_bond(i) for i in range(L - 1))
Ps = 0.5 * (np.eye(4) - SW)                       # singlet projector on two qubits


def run(r, T=12.0, nt=48):
    rr = np.outer(r, r.conj())
    H = Hbulk + J * op_site(rr, 0)
    psi = np.zeros(dim, dtype=complex); psi[0] = 1.0         # |0...0> = aligned emptiness
    psi0 = psi.copy()
    ts = np.linspace(0, T, nt + 1)
    out = expm_multiply(-1j * H, psi, start=0, stop=T, num=nt + 1, endpoint=True)
    worst = dict(content=0.0, activity=0.0, formation=0.0, moved=0.0)
    for ps in out:
        M = ps.reshape([2] * L)
        rho3 = np.tensordot(M, M.conj(), axes=(list(range(1, L)), list(range(1, L))))
        rho34 = np.tensordot(M, M.conj(), axes=(list(range(2, L)), list(range(2, L)))).reshape(4, 4)
        worst['content'] = max(worst['content'], np.real(r.conj() @ rho3 @ r))
        worst['activity'] = max(worst['activity'], np.real(np.trace(Ps @ rho34)))
        worst['formation'] = max(worst['formation'], np.real(rho3[1, 1]))
        worst['moved'] = max(worst['moved'], 1 - abs(np.vdot(psi0, ps)) ** 2)
    return worst


print("max over t in [0,12] (49 times); odds shown divided by their prefactors")
for name, th in [("r = -n (|1>)", np.pi), ("r = +n (|0>)", 0.0), ("r off-axis th=pi/2", np.pi / 2),
                 ("r off-axis th=0.9pi", 0.9 * np.pi), ("r off-axis th=0.99pi", 0.99 * np.pi)]:
    r = np.array([np.cos(th / 2), np.sin(th / 2)], dtype=complex)
    w = run(r)
    print(f"{name:22s}: content<r|rho|r> {w['content']:.3e}  activity<Ps> {w['activity']:.3e}  "
          f"formation<1|rho|1> {w['formation']:.3e}  1-|<psi0|psi_t>|^2 {w['moved']:.3e}")

print("\n2D notch (empty y touching two jam records x and z, other neighbours quiet |n>):")
print(" compressed activity weight W_y = (1/3)[<r|Ps(y,z)|r>_z + sum_quiet Ps] -> on y=|n>:")
for name, th in [("r=-n", np.pi), ("r=+n", 0.0), ("r off-axis pi/2", np.pi / 2)]:
    r = np.array([np.cos(th / 2), np.sin(th / 2)], dtype=complex)
    n = np.array([1, 0], dtype=complex)
    # <r|_z Ps(y,z) |r>_z as an operator on y
    Ps4 = Ps.reshape(2, 2, 2, 2)                     # indices (y,z,y',z')
    Wy_from_z = np.einsum('b,abcd,d->ac', r.conj(), Ps4, r)
    val_z = np.real(n.conj() @ Wy_from_z @ n)
    val_quiet = np.real(np.kron(n, n).conj() @ Ps @ np.kron(n, n))
    print(f"  {name:16s}: from recorded z: {val_z:.4f}   from each quiet neighbour: {val_quiet:.1e}"
          f"   -> W_y on |n> = {(val_z + 2 * val_quiet) / 3:.4f}  (sealed iff 0)")
