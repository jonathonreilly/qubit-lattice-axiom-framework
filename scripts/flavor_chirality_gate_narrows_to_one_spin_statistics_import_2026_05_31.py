#!/usr/bin/env python3
"""Finite algebraic scope for the flavor chirality gate repair.

The runner checks only bounded linear-algebra facts:

* the native two-qubit ladder product is ungraded while Jordan-Wigner dressed
  ladders anticommute;
* both sets generate the same ungraded M_4(C) algebra;
* the second Jordan-Wigner dressed ladder is not local to the second native
  qubit factor;
* a supplied first-order Pauli/Clifford symbol squares to the scalar hopping
  Laplacian symbol;
* bipartite parity anticommutes with supplied nearest-neighbor hopping;
* the graph Laplacian is A2-local but not a chiral first-order operator.

The script deliberately does not claim Dirac-Kahler/staggered equivalence,
hw=1/count-three, carrier/generation identification, Koide Q=2/3, or a
spin-statistics derivation of the fermionic frame.
"""

import functools
import itertools

import numpy as np

I2 = np.eye(2)
SP = np.array([[0, 1], [0, 0]], dtype=complex)
S3 = np.diag([1.0, -1.0]).astype(complex)
SM = SP.conj().T
PAULI = [
    np.array([[0, 1], [1, 0]], dtype=complex),
    np.array([[0, -1j], [1j, 0]], dtype=complex),
    np.diag([1.0, -1.0]).astype(complex),
]


def kron(*a):
    return functools.reduce(np.kron, a)


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def alg_rank(gens, dim):
    """Rank of the operator algebra spanned by short products of generators."""
    allm = [np.eye(dim, dtype=complex)]
    cur = [np.eye(dim, dtype=complex)]
    for _ in range(4):
        nxt = [m @ g for m in cur for g in gens]
        allm += nxt
        cur = nxt
    return np.linalg.matrix_rank(np.array([m.flatten() for m in allm]), tol=1e-9)


def second_site_lift(op):
    """Best I tensor B reconstruction for a two-qubit operator."""
    blocks = [[op[2 * a:2 * (a + 1), 2 * b:2 * (b + 1)] for b in range(2)] for a in range(2)]
    b = (blocks[0][0] + blocks[1][1]) / 2.0
    return kron(I2, b)


def periodic_l1(a, b, size):
    return sum(min((x - y) % size, (y - x) % size) for x, y in zip(a, b))


def a2_local_matrix(mat, sites, size, tol=1e-9):
    for i, si in enumerate(sites):
        for j, sj in enumerate(sites):
            if abs(mat[i, j]) > tol and i != j and periodic_l1(si, sj, size) != 1:
                return False
    return True


def main():
    passed = []

    # P1: finite cross-site statistics checks on two native qubits.
    passed.append(check(
        "P1a on-site creator is nilpotent (sigma_+^2 = 0) -- shared by qubit, hard-core boson, fermion mode",
        np.allclose(SP @ SP, 0),
        "dim-2 site excludes only the free boson; nilpotency is statistics-blind",
    ))

    spx, spy = kron(SP, I2), kron(I2, SP)
    c1, c2 = kron(SM, I2), kron(S3, SM)
    passed.append(check(
        "P1b bare qubit ladders commute across sites; JW-dressed fermions anticommute",
        np.allclose(spx @ spy - spy @ spx, 0) and np.allclose(c1 @ c2 + c2 @ c1, 0),
        "[sp_x,sp_y]=0 in the native product; {c1,c2}=0 after the JW dressing",
    ))

    qubit_gens = [spx, spx.conj().T, spy, spy.conj().T, kron(S3, I2), kron(I2, S3)]
    jw_gens = [c1, c1.conj().T, c2, c2.conj().T]
    rq, rj = alg_rank(qubit_gens, 4), alg_rank(jw_gens, 4)
    passed.append(check(
        "P1c qubit-ladder algebra and JW-fermion algebra span the same ungraded algebra M_4(C)",
        rq == 16 and rj == 16,
        f"qubit-ladder rank={rq}, JW-fermion rank={rj}",
    ))

    native_second_is_local = np.allclose(second_site_lift(spy), spy)
    jw_second_is_native_second_site_local = np.allclose(second_site_lift(c2), c2)
    passed.append(check(
        "P1d second JW ladder is not local to the second native qubit factor (no c2 = I tensor B)",
        native_second_is_local and not jw_second_is_native_second_site_local,
        "native sp_y reconstructs as I tensor sigma_+; JW c2=Z tensor sigma_- carries prior-site support",
    ))

    # P2: supplied first-order symbol and supplied bipartite hopping checks.
    for k in [(0.3, 1.1, 2.0), (0.7, 0.7, 0.7), (1.9, 0.2, 2.7)]:
        iD = -sum(PAULI[m] * np.sin(k[m]) for m in range(3))
        lap = sum(np.sin(x) ** 2 for x in k)
        ok = np.allclose(iD @ iD, lap * I2)
        passed.append(check(
            f"P2a supplied Clifford-Dirac symbol at k={k}: (iD)^2 = (sum sin^2 k) I",
            ok,
            f"(iD)^2 == {lap:.4f} * I",
        ))
        break

    size = 2
    sites = list(itertools.product(range(size), repeat=3))
    idx = {s: i for i, s in enumerate(sites)}
    n = len(sites)
    eps = np.diag([(-1) ** sum(s) for s in sites]).astype(float)
    hop = np.zeros((n, n))
    for s in sites:
        for mu in range(3):
            t = list(s)
            t[mu] = (t[mu] + 1) % size
            t = tuple(t)
            hop[idx[s], idx[t]] += 1
            hop[idx[t], idx[s]] += 1
    passed.append(check(
        "P2b epsilon=(-1)^(x+y+z) is the Z^3 bipartite parity and anticommutes with nearest-neighbor hopping",
        np.allclose(eps @ hop + hop @ eps, 0),
        "finite supplied nearest-neighbor hop is parity-reversing on the bipartite lattice",
    ))

    lap_op = np.diag(hop.sum(axis=1)) - hop
    comm_norm = np.linalg.norm(eps @ lap_op - lap_op @ eps)
    anti_norm = np.linalg.norm(eps @ lap_op + lap_op @ eps)
    passed.append(check(
        "P2c graph Laplacian is A2-local and symmetric, but neither epsilon-commuting nor epsilon-anticommuting",
        (
            np.allclose(lap_op, lap_op.T)
            and a2_local_matrix(lap_op, sites, size)
            and not np.allclose(eps @ lap_op + lap_op @ eps, 0)
            and not np.allclose(eps @ lap_op - lap_op @ eps, 0)
        ),
        f"||[epsilon,L]||={comm_norm:.4f}, ||{{epsilon,L}}||={anti_norm:.4f}; this is A2-local non-chiral support",
    ))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("VERDICT: BOUNDED-SUPPORT finite algebra only. The native ungraded two-qubit tensor product does not")
    print("select the cross-site CAR/Jordan-Wigner frame, and the supplied first-order parity-reversing operator")
    print("has the checked Clifford square. The graph Laplacian supplies an A2-local non-chiral alternative.")
    print("No downstream Dirac-Kahler, hw=1/count-three, carrier/generation, Koide-Q, or spin-statistics bridge")
    print("is claimed by this runner.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
