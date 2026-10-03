"""A34 c3: is a blind swap energy-neutral 'in calm surroundings' (A31 D11, K1(b), K3(c))?

Compressed Heisenberg change H_R = Q (J sum_<ij> s_i.s_j) Q. Calm snapshot: unrecorded sites in |n>,
records with content +n or -n. For such product snapshots <s_i.s_j> = n_i.n_j exactly, so
<H_R> = J * (#bonds - 2 * #(record(-n)--unrecorded contacts) - 2 * #(record(-n)--record(+n) contacts)).
(1) exact statevector check of that formula on an 8-site ring (compression done with matrices);
(2) 3D: energy change of ONE blind swap that moves a -n record (a) in empty calm space, (b) off a flat
    face of a 3x3x3 jam of -n records, (c) the same with +n contents. Units: J.
"""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[v] = "1"
import signal
import numpy as np
signal.alarm(28)
J = 1.0
I2 = np.eye(2, dtype=complex); X = np.array([[0, 1], [1, 0]], complex); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1, -1]).astype(complex)

# (1) exact ring check
Lr = 8
def op1(o, i):
    out = np.array([[1.0]], complex)
    for j in range(Lr):
        out = np.kron(out, o if j == i else I2)
    return out
S = [[op1(p, i) for p in (X, Y, Z)] for i in range(Lr)]
H = sum(J * sum(S[i][c] @ S[(i + 1) % Lr][c] for c in range(3)) for i in range(Lr))
up = np.array([1, 0], complex); dn = np.array([0, 1], complex)
def ring_energy(rec):     # rec: dict site -> content vector; others |n> = up
    Q = np.eye(2 ** Lr, dtype=complex)
    psi = np.array([1.0], complex)
    for j in range(Lr):
        v = rec.get(j, up)
        psi = np.kron(psi, v)
        if j in rec:
            Q = Q @ op1(np.outer(v, v.conj()), j)
    HR = Q @ H @ Q
    return np.vdot(psi, HR @ psi).real
before = ring_energy({2: dn, 3: dn})            # two adjacent -n records
after = ring_energy({2: dn, 4: dn})             # blind swap: record at 3 trades places with empty site 4
alone_b = ring_energy({3: dn}); alone_a = ring_energy({4: dn})
print(f"(1) 8-ring exact: adjacent -n pair -> separated: <H_R> {before:.6f} -> {after:.6f} (change {after-before:+.6f} J)")
print(f"    lone -n record stepping: {alone_b:.6f} -> {alone_a:.6f} (change {alone_a-alone_b:+.6f} J)")
plus_b = ring_energy({2: up, 3: up}); plus_a = ring_energy({2: up, 4: up})
print(f"    adjacent +n pair -> separated: change {plus_a-plus_b:+.6f} J")

# (2) 3D product-state energies on an L^3 torus
L = 9
def energy(content):      # content[x,y,z] = +1 (n, unrecorded or +n record) or -1 (-n record)
    e = 0.0
    for ax in range(3):
        e += J * np.sum(content * np.roll(content, -1, axis=ax))
    return e
c = np.ones((L, L, L))
c[3:6, 3:6, 3:6] = -1                           # 3x3x3 jam of -n records
e0 = energy(c)
c2 = c.copy(); c2[5, 4, 4] = 1; c2[6, 4, 4] = -1  # face-centre record at x=5 trades places with calm site x=6
print(f"(2b) 3D jam, one blind step off a flat face (-n contents): energy change {energy(c2)-e0:+.1f} J")
c3 = np.ones((L, L, L)); c3[4, 4, 4] = -1
c4 = np.ones((L, L, L)); c4[5, 4, 4] = -1
print(f"(2a) 3D lone -n record, one blind step: energy change {energy(c4)-energy(c3):+.1f} J")
print("(2c) +n contents: every product snapshot has the same energy (all n_i.n_j = 1): change 0 J")
# full dissolution of the 27-record jam into isolated records (no record-record contacts):
print(f"     27-record -n jam: energy as a block {e0:.0f} J vs fully dispersed "
      f"{J*(3*L**3) - 2*J*27*6:.0f} J -> change {J*(3*L**3) - 2*J*27*6 - e0:+.0f} J "
      f"(= -2J x gained record-calm contacts)")
