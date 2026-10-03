"""Coordinator check of A1 D23 (lock-and-move channel), relevant after A20 Theorem N (reversible NN covariant ticks are trivial).
K_v = 3^{-1/2} P_v (x) T_v, v in {+-x,+-y,+-z}: P_v projects the record's qubit onto the Bloch direction v; T_v steps it to x+v.
Checks: (1) completeness sum_v K_v^dag K_v = 1 on the qubit (T_v unitary); (2) soldered covariance: a proper rotation R maps the
Kraus set to itself (P_v -> P_{Rv} via the spin-1/2 lift, T_v -> T_{Rv}); (3) step statistics from content |v>: continue / turn / reverse."""
import numpy as np, itertools
sx = np.array([[0,1],[1,0]],complex); sy = np.array([[0,-1j],[1j,0]]); sz = np.diag([1.,-1.]).astype(complex)
def P(n): return 0.5*(np.eye(2) + n[0]*sx + n[1]*sy + n[2]*sz)
dirs = [np.array(v, float) for v in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]]
S = sum(P(v)/3 for v in dirs)
print("(1) sum_v P_v/3 = identity:", np.allclose(S, np.eye(2)))
# (2) the 24 proper rotations of the cube permute the six directions; spin-1/2 lift u(R) satisfies u P_v u^dag = P_{Rv}
def rot_from_perm(p, s):
    R = np.zeros((3,3)); 
    for i in range(3): R[p[i], i] = s[i]
    return R
rots = [rot_from_perm(p, s) for p in itertools.permutations(range(3)) for s in itertools.product((1,-1), repeat=3) if np.isclose(np.linalg.det(rot_from_perm(p, s)), 1)]
def su2(R):   # spin-1/2 lift via axis-angle
    ang = np.arccos(np.clip((np.trace(R)-1)/2, -1, 1))
    if np.isclose(ang, 0): return np.eye(2, dtype=complex)
    if np.isclose(ang, np.pi):
        w, V = np.linalg.eigh(R); n = V[:, np.argmin(abs(w-1))]
    else:
        n = np.array([R[2,1]-R[1,2], R[0,2]-R[2,0], R[1,0]-R[0,1]]) / (2*np.sin(ang))
    return np.cos(ang/2)*np.eye(2) - 1j*np.sin(ang/2)*(n[0]*sx + n[1]*sy + n[2]*sz)
ok = all(np.allclose(su2(R) @ P(v) @ su2(R).conj().T, P(R @ v)) for R in rots for v in dirs)
print("(2) %d proper rotations; every rotation maps P_v to P_{Rv} (and T_v to T_{Rv}): %s" % (len(rots), ok))
# (3) step statistics from content |v> (the record points where it last stepped)
v = dirs[0]; psi_rho = P(v)
probs = {tuple(w.astype(int)): np.real(np.trace(psi_rho @ P(w)))/3 for w in dirs}
cont = probs[(1,0,0)]; rev = probs[(-1,0,0)]; turn = sum(p for k, p in probs.items() if k not in [(1,0,0),(-1,0,0)])
print("(3) from content +x: continue %.4f, reverse %.4f, turn (4 ways) %.4f  -> a persistent walk that never steps back" % (cont, rev, turn))
