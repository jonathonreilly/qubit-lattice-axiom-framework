#!/usr/bin/env python3
"""Exact-symbolic + numerical audit-companion runner for
`LSP_PROJECTIVE_CANONICAL_KP_EQUALS_P_NARROW_THEOREM_NOTE_2026-06-05.md`.

Reproves, from primitives (no imported measurement axiom), the canonical
projective-measurement Kraus selection `K_P = P` under the RESTRICTED
Step-3 scope requested by the audit repair note

    "scope_too_broad: restrict Step 3 to V_A=I, outcome-label
     phase/permutation apparatus unitaries, or an explicit rotated
     readout-frame convention, then re-audit the canonical K_P=P theorem."

and shows EXPLICITLY that a general (outcome-label-mixing) apparatus
unitary V_A breaks K_P = P (so the restriction is necessary).

What is reproven (every load-bearing fact, sympy exact / numpy machine):

  Part A  projective primitives: P_r P_{r'} = d_{rr'} P_r, P_r^dag = P_r,
          sum_r P_r = I, for several projector families.
  Part B  canonical dilation V|psi> = sum_r (P_r|psi>) tensor |r> is an
          isometry: V^dag V = I_sys  (the (iso) computation).
  Part C  canonical Kraus extraction K_r = <r|_A V = P_r exactly (KP), and
          sequential composition K_r^dag E K_r = P_r E P_r (PEP); plus the
          completion-independence check (a sign/phase-perturbed unitary
          completion leaves K_r unchanged).
  Part D  sufficiency of the restriction: V_A = I (K_r = P_r); outcome-label
          phase V_A (K_r = e^{i phi_r} P_r, K_r^dag K_r = P_r); outcome-label
          permutation V_A (K_r^dag K_r = P_{pi^{-1}(r)}).
  Part E  necessity: a general label-mixing V_A gives
          K_r^dag K_r = sum_s |<r|V_A|s>|^2 P_s != P_r on nonzero outcome
          sectors (the auditor's formula), with weights forming a doubly
          stochastic |V_A|^2. A zero-projector edge-case check demonstrates why
          the nonzero-outcome convention is required.
  Part F  source-note boundary string checks.

Literature (Naimark 1940; Stinespring 1955; Holevo; Watrous; Lueders 1951)
is comparator only; the projective construction is built inline.

Companion role: source-side construction with explicit verification. This
runner is NOT a status promotion; the independent audit lane owns the verdict.
"""

from pathlib import Path
import sys

try:
    import sympy as sp
    from sympy import (
        Rational, Symbol, symbols, sqrt, simplify, Matrix, eye, zeros, I,
        cos, sin, exp, conjugate, Abs,
    )
except ImportError:  # pragma: no cover
    print("FAIL: sympy required for exact algebra")
    sys.exit(1)

try:
    import numpy as np
except ImportError:  # pragma: no cover
    print("FAIL: numpy required for numerical checks")
    sys.exit(1)


PASS = 0
FAIL = 0


def _report(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {label}{(': ' + detail) if detail else ''}")
    if ok:
        PASS += 1
    else:
        FAIL += 1


# --------------------------------------------------------------------------
# sympy helpers
# --------------------------------------------------------------------------

def skron(A: Matrix, B: Matrix) -> Matrix:
    """Kronecker product for sympy Matrices (sites ordered sys (x) apparatus)."""
    ra, ca = A.shape
    rb, cb = B.shape
    out = zeros(ra * rb, ca * cb)
    for i in range(ra):
        for j in range(ca):
            for k in range(rb):
                for l in range(cb):
                    out[i * rb + k, j * cb + l] = A[i, j] * B[k, l]
    return out


def is_zero_matrix(M: Matrix) -> bool:
    M = simplify(M)
    return all(M[i, j] == 0 for i in range(M.rows) for j in range(M.cols))


def basis_vec(dim: int, idx: int) -> Matrix:
    v = zeros(dim, 1)
    v[idx, 0] = 1
    return v


def build_canonical_isometry(projs, dS: int, dA: int) -> Matrix:
    """V : H_sys -> H_sys (x) H_A, V|psi> = sum_r (P_r|psi>) (x) |r>_A.

    Returns the (dS*dA) x dS matrix whose i-th column is V|i>_sys.
    Apparatus |0>_A is the basis vector |0>; outcomes r index basis {|r>_A}.
    """
    full = dS * dA
    V = zeros(full, dS)
    for i in range(dS):
        psi = basis_vec(dS, i)
        col = zeros(full, 1)
        for r, P in enumerate(projs):
            col = col + skron(P * psi, basis_vec(dA, r))
        V[:, i] = col
    return V


def braA(r: int, dS: int, dA: int) -> Matrix:
    """(I_sys (x) <r|_A) as a dS x (dS*dA) contraction matrix."""
    op = zeros(dS, dS * dA)
    for i in range(dS):
        op[i, i * dA + r] = 1
    return op


# --------------------------------------------------------------------------
# Projector families (sympy, exact)
# --------------------------------------------------------------------------

def family_rank1_qubit():
    P0 = Matrix([[1, 0], [0, 0]])
    P1 = Matrix([[0, 0], [0, 1]])
    return "rank-1 single qubit {|0><0|,|1><1|}", [P0, P1], 2


def family_rotated_qubit():
    t = Symbol('t', real=True)
    c, s = cos(t), sin(t)
    ket = Matrix([[c], [s]])
    P = simplify(ket * ket.T)
    Pc = simplify(eye(2) - P)
    return "rotated-basis qubit (symbolic angle t)", [P, Pc], 2


def family_rank2_two_qubit():
    # P projects onto span{|00>,|11>} in a 2-qubit (dim-4) space; complement rank 2
    P = zeros(4, 4)
    P[0, 0] = 1
    P[3, 3] = 1
    Pc = eye(4) - P
    return "rank-2 two-qubit {span(|00>,|11>), complement}", [P, Pc], 4


SYMPY_FAMILIES = [family_rank1_qubit, family_rotated_qubit, family_rank2_two_qubit]


def test_part_A_primitives():
    print("\n[Part A] Projective-measurement primitives")
    for fam in SYMPY_FAMILIES:
        name, projs, dS = fam()
        m = len(projs)
        # idempotent / orthogonal / self-adjoint
        orth_ok = True
        for a in range(m):
            for b in range(m):
                target = projs[a] if a == b else zeros(dS, dS)
                if not is_zero_matrix(projs[a] * projs[b] - target):
                    orth_ok = False
        _report(f"A[{name}]: P_r P_r' = delta_rr' P_r", orth_ok)
        sa_ok = all(is_zero_matrix(P.H - P) for P in projs)
        _report(f"A[{name}]: P_r^dag = P_r", sa_ok)
        completeness = zeros(dS, dS)
        for P in projs:
            completeness = completeness + P
        _report(f"A[{name}]: sum_r P_r = I", is_zero_matrix(completeness - eye(dS)))


def test_part_B_isometry():
    print("\n[Part B] Canonical dilation is an isometry (V^dag V = I_sys)")
    for fam in SYMPY_FAMILIES:
        name, projs, dS = fam()
        dA = len(projs)
        V = build_canonical_isometry(projs, dS, dA)
        gram = simplify(V.H * V)
        _report(f"B[{name}]: V^dag V = I_sys", is_zero_matrix(gram - eye(dS)))


def test_part_C_canonical_kraus():
    print("\n[Part C] Canonical Kraus K_r = P_r (KP) and P E P (PEP)")
    for fam in SYMPY_FAMILIES:
        name, projs, dS = fam()
        dA = len(projs)
        V = build_canonical_isometry(projs, dS, dA)
        all_kp = True
        for r, P in enumerate(projs):
            Kr = simplify(braA(r, dS, dA) * V)
            if not is_zero_matrix(Kr - P):
                all_kp = False
        _report(f"C[{name}]: K_r = <r|_A V = P_r (exact)", all_kp)
        # PEP composition against a few Hermitian effects E
        eff_list = [("I", eye(dS))]
        if dS == 2:
            eff_list += [("sigma_x", Matrix([[0, 1], [1, 0]])),
                         ("sigma_z", Matrix([[1, 0], [0, -1]]))]
        else:
            a, b, c, d, e, f = symbols('a b c d e f', real=True)
            E_sym = Matrix([[a, 0, 0, b], [0, c, 0, 0], [0, 0, d, 0], [b, 0, 0, e]])
            eff_list += [("symbolic Hermitian", E_sym)]
        pep_ok = True
        for ename, E in eff_list:
            for r, P in enumerate(projs):
                Kr = P  # canonical
                M = simplify(Kr.H * E * Kr)
                if not is_zero_matrix(M - simplify(P * E * P)):
                    pep_ok = False
        _report(f"C[{name}]: K_r^dag E K_r = P_r E P_r for all tested E", pep_ok)


def test_part_C_completion_independence():
    """Kraus extraction depends only on the prepared-subspace isometry, so a
    different (sign/phase-perturbed) unitary completion leaves K_r unchanged."""
    print("\n[Part C'] Completion-independence of K_r (numpy)")
    rng = np.random.default_rng(11)
    ket = lambda i, d: np.eye(d, dtype=complex)[:, i:i + 1]
    dS, dA = 2, 2
    P = [ket(0, 2) @ ket(0, 2).conj().T, ket(1, 2) @ ket(1, 2).conj().T]
    full = dS * dA

    def kron(a, b):
        return np.kron(a, b)

    # canonical isometry as map H_sys -> H_full
    V = np.zeros((full, dS), dtype=complex)
    for i in range(dS):
        psi = ket(i, dS)
        col = np.zeros((full, 1), dtype=complex)
        for r in range(dA):
            col = col + kron(P[r] @ psi, ket(r, dA))
        V[:, i:i + 1] = col

    def braA_np(r):
        op = np.zeros((dS, full), dtype=complex)
        for i in range(dS):
            op[i, i * dA + r] = 1
        return op

    # K_r from the bare isometry
    K_from_iso = [braA_np(r) @ V for r in range(dA)]
    base_ok = all(np.allclose(K_from_iso[r], P[r], atol=1e-12) for r in range(dA))
    _report("C'[K_r from isometry] = P_r (numerical)", base_ok)

    # Build TWO different unitary completions and confirm K_r is identical.
    def complete(seed):
        rnd = np.random.default_rng(seed)
        # orthonormal basis for the occupied range = columns of V (already iso)
        Q = V.copy()
        # random complement
        X = rnd.standard_normal((full, full)) + 1j * rnd.standard_normal((full, full))
        proj = X - Q @ (Q.conj().T @ X)
        Qc, _ = np.linalg.qr(proj)
        comp = Qc[:, : full - dS]
        # input columns: occupied inputs |i>(x)|0> at index i*dA+0 -> Q[:,i];
        # remaining standard inputs -> complement columns
        U = np.zeros((full, full), dtype=complex)
        occupied = [i * dA + 0 for i in range(dS)]
        others = [c for c in range(full) if c not in occupied]
        for k, c in enumerate(occupied):
            U[:, c] = Q[:, k]
        for k, c in enumerate(others):
            U[:, c] = comp[:, k]
        return U

    emb = np.zeros((full, dS), dtype=complex)
    for i in range(dS):
        emb[i * dA + 0, i] = 1  # |i>(x)|0>

    U1 = complete(1)
    U2 = complete(99)
    u1_unit = np.allclose(U1.conj().T @ U1, np.eye(full), atol=1e-9)
    u2_unit = np.allclose(U2.conj().T @ U2, np.eye(full), atol=1e-9)
    _report("C'[two completions are unitary]", u1_unit and u2_unit)
    same = True
    for r in range(dA):
        K1 = braA_np(r) @ U1 @ emb
        K2 = braA_np(r) @ U2 @ emb
        if not (np.allclose(K1, P[r], atol=1e-9) and np.allclose(K2, P[r], atol=1e-9)):
            same = False
    _report("C'[K_r identical (=P_r) across two unitary completions]", same)


def test_part_D_sufficiency():
    print("\n[Part D] Sufficiency: V_A = I, outcome-label phase, permutation")
    # Use the rank-1 qubit family symbolically.
    _, projs, dS = family_rank1_qubit()
    dA = len(projs)
    V = build_canonical_isometry(projs, dS, dA)

    # (a) V_A = I, U_sys = I -> K_r = P_r (already in Part C; restate here)
    va_I_ok = True
    for r, P in enumerate(projs):
        Kr = simplify(braA(r, dS, dA) * V)
        if not is_zero_matrix(Kr - P):
            va_I_ok = False
    _report("D(a)[V_A=I]: K_r = P_r", va_I_ok)

    # (b) outcome-label phase V_A = diag(1, e^{i phi})
    phi = Symbol('phi', real=True)
    VA_phase = Matrix([[1, 0], [0, exp(I * phi)]])
    Vtw_phase = skron(eye(dS), VA_phase) * V
    phase_ok = True
    phase_form_ok = True
    for r, P in enumerate(projs):
        Kr = simplify(braA(r, dS, dA) * Vtw_phase)
        KdK = simplify(Kr.H * Kr)
        if not is_zero_matrix(KdK - P):
            phase_ok = False
        # K_r should equal (phase) * P_r
        phase_factor = exp(I * phi) if r == 1 else sp.Integer(1)
        if not is_zero_matrix(simplify(Kr - phase_factor * P)):
            phase_form_ok = False
    _report("D(b)[phase V_A]: K_r^dag K_r = P_r (exact)", phase_ok)
    _report("D(b)[phase V_A]: K_r = e^{i phi_r} P_r (exact)", phase_form_ok)

    # (c) outcome-label permutation V_A = swap |0>_A<->|1>_A
    VA_perm = Matrix([[0, 1], [1, 0]])
    Vtw_perm = skron(eye(dS), VA_perm) * V
    perm_ok = True
    # permutation pi swaps 0,1 so pi^{-1}(r) = 1-r
    for r in range(dA):
        Kr = simplify(braA(r, dS, dA) * Vtw_perm)
        KdK = simplify(Kr.H * Kr)
        if not is_zero_matrix(KdK - projs[1 - r]):
            perm_ok = False
    _report("D(c)[permutation V_A]: K_r^dag K_r = P_{pi^{-1}(r)} (relabel)", perm_ok)


def test_part_E_necessity_symbolic():
    print("\n[Part E] Necessity (symbolic): mixing V_A breaks K_P = P")
    _, projs, dS = family_rank1_qubit()
    dA = len(projs)
    V = build_canonical_isometry(projs, dS, dA)
    # genuine mixing apparatus rotation V_A = [[c,-s],[s,c]], c=cos a, s=sin a
    a = Symbol('a', real=True)
    c, s = cos(a), sin(a)
    VA_mix = Matrix([[c, -s], [s, c]])
    Vtw = skron(eye(dS), VA_mix) * V
    # auditor formula: K_r^dag K_r = sum_s |<r|V_A|s>|^2 P_s
    matches_mixture = True
    breaks_kp = True  # for generic a it should not equal P_r
    for r in range(dA):
        Kr = simplify(braA(r, dS, dA) * Vtw)
        KdK = simplify(Kr.H * Kr)
        mixture = zeros(dS, dS)
        for sidx in range(dA):
            w = simplify(Abs(VA_mix[r, sidx]) ** 2)
            mixture = mixture + w * projs[sidx]
        mixture = simplify(mixture)
        if not is_zero_matrix(KdK - mixture):
            matches_mixture = False
        # at a = pi/4 the mixing is maximal: K_r^dag K_r = (1/2)(P_0+P_1) != P_r
        KdK_quarter = simplify(KdK.subs(a, sp.pi / 4))
        if is_zero_matrix(KdK_quarter - projs[r]):
            breaks_kp = False
    _report("E[symbolic]: K_r^dag K_r = sum_s |<r|V_A|s>|^2 P_s", matches_mixture)
    _report("E[symbolic]: at maximal mixing (a=pi/4) K_r^dag K_r != P_r", breaks_kp)


def _haar_unitary(dim: int, rng) -> "np.ndarray":
    X = rng.standard_normal((dim, dim)) + 1j * rng.standard_normal((dim, dim))
    Q, R = np.linalg.qr(X)
    ph = np.diag(R) / np.abs(np.diag(R))
    return Q @ np.diag(ph)


def test_part_E_necessity_numeric():
    print("\n[Part E'] Necessity (numpy Haar): mixing V_A breaks K_P = P")
    rng = np.random.default_rng(2026)
    ket = lambda i, d: np.eye(d, dtype=complex)[:, i:i + 1]

    def kron(x, y):
        return np.kron(x, y)

    # try a few dims: (dS=2,dA=2), (dS=2,dA=2 rotated isn't needed), (dS=2,dA=2)
    configs = [
        ("qubit dS=2,dA=2", [ket(0, 2) @ ket(0, 2).conj().T,
                             ket(1, 2) @ ket(1, 2).conj().T], 2, 2),
        ("two-qubit rank-2 dS=4,dA=2",
         [np.diag([1, 0, 0, 1]).astype(complex), np.diag([0, 1, 1, 0]).astype(complex)],
         4, 2),
    ]
    mixture_all = True
    breaks_all = True
    dstoch_all = True
    n_samples = 25
    for name, P, dS, dA in configs:
        full = dS * dA
        V = np.zeros((full, dS), dtype=complex)
        for i in range(dS):
            psi = ket(i, dS)
            col = np.zeros((full, 1), dtype=complex)
            for r in range(dA):
                col = col + kron(P[r] @ psi, ket(r, dA))
            V[:, i:i + 1] = col

        def braA_np(r):
            op = np.zeros((dS, full), dtype=complex)
            for i in range(dS):
                op[i, i * dA + r] = 1
            return op

        n_break = 0
        for _ in range(n_samples):
            VA = _haar_unitary(dA, rng)
            Vtw = kron(np.eye(dS), VA) @ V
            W = np.abs(VA) ** 2  # weights w_{rs}
            # doubly stochastic rows/cols sum to 1
            if not (np.allclose(W.sum(axis=1), 1.0, atol=1e-9)
                    and np.allclose(W.sum(axis=0), 1.0, atol=1e-9)):
                dstoch_all = False
            broke_this = False
            for r in range(dA):
                Kr = braA_np(r) @ Vtw
                KdK = Kr.conj().T @ Kr
                mixture = sum(W[r, sidx] * P[sidx] for sidx in range(dA))
                if not np.allclose(KdK, mixture, atol=1e-9):
                    mixture_all = False
                if not np.allclose(KdK, P[r], atol=1e-9):
                    broke_this = True
            if broke_this:
                n_break += 1
        # For Haar-random VA, mixing is generic, so essentially all samples break K_P=P.
        if n_break < n_samples - 1:  # allow at most one accidental near-permutation
            breaks_all = False
        _report(f"E'[{name}]: {n_break}/{n_samples} Haar V_A break K_r^dag K_r = P_r",
                n_break >= n_samples - 1)
    _report("E'[all]: K_r^dag K_r = sum_s |<r|V_A|s>|^2 P_s for every sample", mixture_all)
    _report("E'[all]: weight matrix |V_A|^2 is doubly stochastic", dstoch_all)
    _report("E'[all]: generic mixing V_A breaks K_P = P", breaks_all)


def test_part_E_zero_projector_edge_case():
    print("\n[Part E''] Zero-projector edge-case for the necessity clause")
    ket = lambda i, d: np.eye(d, dtype=complex)[:, i:i + 1]

    def kron(x, y):
        return np.kron(x, y)

    dS, dA = 2, 4
    P0 = ket(0, 2) @ ket(0, 2).conj().T
    P1 = ket(1, 2) @ ket(1, 2).conj().T
    Z = np.zeros((2, 2), dtype=complex)
    P = [P0, P1, Z, Z]

    full = dS * dA
    V = np.zeros((full, dS), dtype=complex)
    for i in range(dS):
        psi = ket(i, dS)
        col = np.zeros((full, 1), dtype=complex)
        for r in range(dA):
            col = col + kron(P[r] @ psi, ket(r, dA))
        V[:, i:i + 1] = col

    def braA_np(r):
        op = np.zeros((dS, full), dtype=complex)
        for i in range(dS):
            op[i, i * dA + r] = 1
        return op

    def rotate_labels(a, b, theta):
        VA = np.eye(dA, dtype=complex)
        c, s = np.cos(theta), np.sin(theta)
        VA[a, a] = c
        VA[a, b] = -s
        VA[b, a] = s
        VA[b, b] = c
        return VA

    def kdks_for(VA):
        Vtw = kron(np.eye(dS), VA) @ V
        return [(braA_np(r) @ Vtw).conj().T @ (braA_np(r) @ Vtw) for r in range(dA)]

    # Old broad wording "any label mixing breaks K_P=P" is false if the mixing is
    # purely among formal zero-effect bookkeeping labels.
    VA_zero_zero = rotate_labels(2, 3, np.pi / 5)
    zero_zero_kdks = kdks_for(VA_zero_zero)
    zero_zero_preserves = all(np.allclose(zero_zero_kdks[r], P[r], atol=1e-12) for r in range(dA))
    _report("E''[zero-zero mixing]: formal zero-label rotation leaves every K_r^dag K_r unchanged",
            zero_zero_preserves)

    # Mixing two nonzero sectors breaks the same-projective-measurement condition.
    VA_nonzero_nonzero = rotate_labels(0, 1, np.pi / 5)
    nz_kdks = kdks_for(VA_nonzero_nonzero)
    nonzero_breaks = (
        not np.allclose(nz_kdks[0], P0, atol=1e-12)
        and not np.allclose(nz_kdks[1], P1, atol=1e-12)
    )
    _report("E''[nonzero-nonzero mixing]: nonzero sector mixing breaks K_r^dag K_r = P_r",
            nonzero_breaks)

    # Leaking a displayed nonzero sector into a zero label also breaks that
    # nonzero sector, because the target coefficient falls below one.
    VA_nonzero_zero = rotate_labels(0, 2, np.pi / 5)
    nz_zero_kdks = kdks_for(VA_nonzero_zero)
    nonzero_zero_breaks = (
        not np.allclose(nz_zero_kdks[0], P0, atol=1e-12)
        and not np.allclose(nz_zero_kdks[2], Z, atol=1e-12)
    )
    _report("E''[nonzero-zero mixing]: leaking a nonzero sector into a zero label still breaks",
            nonzero_zero_breaks)

    # After deleting formal zero labels, the physical outcome list is nonzero
    # and the necessity statement has no zero-label exception.
    nonzero_labels_only = all(np.linalg.norm(Q) > 0 for Q in [P0, P1])
    _report("E''[nonzero convention]: displayed physical labels have P_r != 0",
            nonzero_labels_only)


def test_part_F_boundary_strings():
    print("\n[Part F] Source-note boundary string checks")
    note_path = Path(__file__).resolve().parent.parent / "docs" / (
        "LSP_PROJECTIVE_CANONICAL_KP_EQUALS_P_NARROW_THEOREM_NOTE_2026-06-05.md"
    )
    if not note_path.exists():
        _report("F: source note exists", False, f"not found: {note_path}")
        return
    text = note_path.read_text(encoding="utf-8")
    required = [
        "Status authority:** independent audit lane only",
        "restricted Step-3 scope",
        "K_P = P",
        "P_r ≠ 0",
        "zero-projector edge-case",
        "outcome-label",
        "necessary",
        "What this does NOT claim",
        "audit lane is the only status authority",
    ]
    forbidden = [
        "Status: retained",
        "Status: promoted",
        "**Status:** retained",
        "target_" + "audit_status",
        "audited_" + "clean",
        "effective_" + "status=",
        "audit_" + "status=",
        "uniqueness theorem for all instruments",
    ]
    for s in required:
        _report(f"F.required present: {s!r}", s in text)
    for s in forbidden:
        _report(f"F.forbidden absent: {s!r}", s not in text)


def main() -> int:
    print("=" * 72)
    print("LSP-projective canonical K_P = P (restricted Step-3 scope) runner")
    print("=" * 72)
    print()
    print("Reproves K_r = P_r from the canonical Naimark/Lueders isometry, shows")
    print("the V_A = I / phase / permutation restriction is sufficient, and shows")
    print("a general label-mixing V_A breaks K_P = P (K_r^dag K_r = sum_s")
    print("|<r|V_A|s>|^2 P_s != P_r) on nonzero sectors. Literature is comparator only.")
    print()
    test_part_A_primitives()
    test_part_B_isometry()
    test_part_C_canonical_kraus()
    test_part_C_completion_independence()
    test_part_D_sufficiency()
    test_part_E_necessity_symbolic()
    test_part_E_necessity_numeric()
    test_part_E_zero_projector_edge_case()
    test_part_F_boundary_strings()
    print()
    print("=" * 72)
    print(f"TOTAL: {PASS} PASS / {FAIL} FAIL")
    print("=" * 72)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
