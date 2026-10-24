"""Finite supplied-axis symmetry reduction; no lattice/QCA construction."""
import itertools
import numpy as np

AUDIT_INPUT_PATHS = ["docs/FINITE_AXIS_ACTION_PARTICLE_HOLE_COVARIANCE_NOTE_2026-10-23.md"]
TOL = 1e-12
SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]], complex)
SZ = np.array([[1, 0], [0, -1]], complex)
SIG = [SX, SY, SZ]
I2 = np.eye(2)

def build_O():
    import numpy as np
    O = []
    for p in itertools.permutations(range(3)):
        for s in itertools.product((1, -1), repeat=3):
            M = np.zeros((3, 3), int)
            for i in range(3): M[p[i], i] = s[i]
            if round(np.linalg.det(M)) == 1: O.append(M)
    return O

def perm_sign(M):
    import numpy as np
    return int(round(np.linalg.det(np.abs(M))))

def su2_lift(Qm):
    Qm = np.array(Qm, float); tr = np.trace(Qm)
    ang = np.arccos(np.clip((tr - 1) / 2, -1, 1))
    if abs(ang) < 1e-9: return I2.astype(complex)
    if abs(ang - np.pi) < 1e-9:
        Mx = (Qm + np.eye(3)) / 2; k = int(np.argmax(np.diag(Mx))); n = Mx[:, k] / np.sqrt(Mx[k, k])
    else:
        n = np.array([Qm[2, 1] - Qm[1, 2], Qm[0, 2] - Qm[2, 0], Qm[1, 0] - Qm[0, 1]]) / (2 * np.sin(ang))
    return np.cos(ang / 2) * I2 - 1j * np.sin(ang / 2) * sum(n[i] * SIG[i] for i in range(3))


def site_permutation(P):
    """Tensor factor permutation, occupied basis index0, vacant index1."""
    V = len(P)
    result = np.zeros((2**V, 2**V), dtype=int)
    for j in range(2**V):
        bits = np.array([(j >> (V-1-k)) & 1 for k in range(V)])
        moved = P @ bits
        i = sum(int(bit) << (V-1-k) for k, bit in enumerate(moved))
        result[i, j] = 1
    return result


def commutator(A, B):
    return A @ B - B @ A


def main():
    failed = 0
    def check(label, ok, detail=""):
        nonlocal failed
        failed += int(not bool(ok))
        print(f"{'PASS' if ok else 'FAIL'}: {label} {detail}")
    O = build_O()
    key = lambda M: tuple(int(x) for x in M.flat)
    keys = {key(M) for M in O}
    T = [M for M in O if perm_sign(M) == 1]
    odd = [M for M in O if perm_sign(M) == -1]
    check("24 distinct proper rotations; 12+12 parity split", len(keys)==24 and len(T)==len(odd)==12)
    integer_det = lambda M: int(np.dot(M[0], np.cross(M[1], M[2])))
    check("exact integer determinant and orthogonality", all(integer_det(M)==1 and np.array_equal(M.T@M,np.eye(3,dtype=int)) for M in O))
    check("576 group, parity and supplied Q multiplication identities", all(
        key(A@B) in keys and perm_sign(A@B)==perm_sign(A)*perm_sign(B) and
        np.array_equal(perm_sign(A@B)*np.abs(A@B), (perm_sign(A)*np.abs(A))@(perm_sign(B)*np.abs(B)))
        for A in O for B in O))
    check("T and any fixed odd coset representative cover O", {key(M) for M in T}|{key(odd[0]@M) for M in T}==keys)
    nvec=np.ones(3)/np.sqrt(3)
    w,V=np.linalg.eigh(sum(nvec[i]*SIG[i] for i in range(3)))
    Bn=np.column_stack([V[:,1],V[:,0]])
    lifts=[]; pauli_error=pattern_error=unitarity_error=0.0
    for M in O:
        Q=perm_sign(M)*np.abs(M);D=su2_lift(Q);Dn=Bn.conj().T@D@Bn;lifts.append(Dn)
        unitarity_error=max(unitarity_error,float(np.max(np.abs(D.conj().T@D-I2))))
        for a in range(3):
            pauli_error=max(pauli_error,float(np.max(np.abs(D@SIG[a]@D.conj().T-sum(Q[b,a]*SIG[b] for b in range(3))))))
        entries=[Dn[0,1],Dn[1,0]] if perm_sign(M)==1 else [Dn[0,0],Dn[1,1]]
        pattern_error=max(pattern_error,max(abs(z) for z in entries))
    check("all 24 lifts unitary and implement all three Pauli images", max(pauli_error,unitarity_error)<TOL, f"Pauli={pauli_error:.3e}; unitary={unitarity_error:.3e}")
    check("even diagonal / odd antidiagonal in occupation basis", pattern_error<TOL, f"residual={pattern_error:.3e}")
    check("Q(R)n=s(R)n", all(np.array_equal(np.abs(M)@np.ones(3),np.ones(3)) for M in O))
    Pcycle=np.array([[0,0,1],[1,0,0],[0,1,0]],dtype=int)
    cycle=site_permutation(Pcycle)
    counts=np.array([3-i.bit_count() for i in range(8)])
    U=np.zeros((8,8),dtype=int)
    for j,n in enumerate(counts):
        if n==1:U[:,j]=cycle[:,j]
        elif n==2:U[:,j]=cycle.T[:,j]
        else:U[j,j]=1
    C=np.fliplr(np.eye(8,dtype=int));N=np.diag(counts)
    check("finite three-axis witness is an exact number-conserving permutation", np.array_equal(U.T@U,np.eye(8,dtype=int)) and not np.any(commutator(U,N)))
    reduced_ok=True;phase_error=0.0;odd_permutation_failure=False
    for M,Dn in zip(O,lifts):
        P=site_permutation(np.abs(M));H=P if perm_sign(M)==1 else C@P
        reduced_ok &= not np.any(commutator(U,H))
        full=np.kron(np.kron(Dn,Dn),Dn)@P
        phase_error=max(phase_error,float(np.max(np.abs(commutator(U,full)))))
        if perm_sign(M)==-1:odd_permutation_failure |= bool(np.any(commutator(U,P)))
    check("all 24 exact reduced commutators vanish", reduced_ok)
    check("all 24 phase-sensitive full covariances hold", phase_error<TOL, f"residual={phase_error:.3e}")
    check("C alone and odd permutation alone are stronger, violated conditions", bool(np.any(commutator(U,C))) and odd_permutation_failure)
    # At half filling, the odd condition stays inside the same number sector.
    half=np.diag([1,1,-1,1]);C2=np.kron(SX,SX);N2=np.diag([2,1,1,0])
    check("half-filling counterexample: number conserving but violates odd symmetry", not np.any(commutator(half,N2)) and np.max(np.abs(commutator(half,C2)))==2)
    # Single fixed site: reduced actions are I or X. U=X obeys both but not N.
    omitted_error=max(float(np.max(np.abs(commutator(SX,D)))) for D in lifts)
    check("dropping number conservation fails full symmetry despite all reduced conditions", np.max(np.abs(commutator(SX,np.diag([1,0]))))==1 and all(not np.any(commutator(SX,I2 if perm_sign(M)==1 else SX)) for M in O) and omitted_error>1, f"full residual={omitted_error:.3e}")
    print(f"TOTAL FAIL={failed}; finite supplied representation only")
    return int(bool(failed))


if __name__ == "__main__":
    raise SystemExit(main())
