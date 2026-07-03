#!/usr/bin/env python3
"""Companion runner: Kraus<->Choi correspondence with a single, self-consistent
Choi-Jamiolkowski normalization, reproven from primitives on the qubit (M_2) and
two-qubit (M_2 (x) M_2) algebras.

This runner exists to repair the Choi-normalization inconsistency in
docs/KRAUS_CHOI_REPRESENTATION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md,
whose statement mixed the NORMALIZED maximally-entangled vector
|Omega> = (1/sqrt d) sum_i |i>|i> with the inverse formula and Kraus-extraction
factors that belong to the UNNORMALIZED vector |Omega> = sum_i |i>|i>.

It pins ONE convention (UNNORMALIZED) and verifies every link of the
correspondence end to end, with all d-factors made explicit and consistent:

  Convention (used throughout, no mixing):
    |Omega>      = sum_i |i>|i>            (norm^2 = d, UNNORMALIZED)
    C_Phi        = (id (x) Phi)(|Omega><Omega|)
                 = sum_{i,j} |i><j| (x) Phi(|i><j|)          (NO 1/d prefactor)
    inverse      Phi(rho) = Tr_1[(rho^T (x) I) C_Phi]        (NO d-factor)
    Kraus        C_Phi = sum_a lambda_a |v_a><v_a|  (eigh, lambda_a >= 0)
                 K_a   = sqrt(lambda_a) * reshape(v_a, (d,d))^T   (eigenvalue
                         absorbed; NO extra sqrt(d) factor)
    CP           <=> C_Phi >= 0 (PSD)
    TP           <=> Tr_2 C_Phi = I_d  (partial trace over the OUTPUT system)
                 <=> sum_a K_a^dagger K_a = I_d

The reshape uses the transpose because (I (x) K)|Omega> = sum_{i,m} K_{m,i} |i>|m>,
so the bipartite eigenvector component at (i, m) equals K_{m, i}; hence
K = reshape(v, (d,d))^T.

Everything is reproven from primitives (numpy random CPTP via Stinespring
isometries, plus an exact sympy check on M_2). No literature value is imported;
Choi 1975 and Nielsen-Chuang Ch.8 are comparators only, cited in the note.

Per-check [PASS]/[FAIL] lines, then 'TOTAL: N PASS / M FAIL'.
"""

from __future__ import annotations

import numpy as np
import sympy as sp

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"{tag} {label}" + (f"  ::  {detail}" if detail else ""))


# --------------------------------------------------------------------------- #
# Primitive building blocks (numpy)                                           #
# --------------------------------------------------------------------------- #
def apply_kraus(kraus_ops, x):
    out = np.zeros_like(x, dtype=complex)
    for k in kraus_ops:
        out = out + k @ x @ k.conj().T
    return out


def kraus_tp_defect(kraus_ops, d):
    s = np.zeros((d, d), dtype=complex)
    for k in kraus_ops:
        s = s + k.conj().T @ k
    return np.linalg.norm(s - np.eye(d))


def choi_unnormalized(map_fn, d):
    """C_Phi = sum_{i,j} |i><j| (x) Phi(|i><j|) with UNNORMALIZED |Omega>.

    No 1/d prefactor: this is the convention paired with the no-d inverse
    formula and the no-extra-sqrt(d) Kraus extraction below.
    """
    c = np.zeros((d * d, d * d), dtype=complex)
    for i in range(d):
        for j in range(d):
            eij = np.zeros((d, d), dtype=complex)
            eij[i, j] = 1.0
            c = c + np.kron(eij, map_fn(eij))
    return c


def map_from_choi(choi, d):
    """Inverse Choi-Jamiolkowski map: Phi(rho) = Tr_1[(rho^T (x) I) C_Phi].

    UNNORMALIZED convention: NO d-factor. (With normalized |Omega> this formula
    would require an extra factor d -- the omission of which is the bug being
    repaired.)
    """

    def phi(rho):
        op = np.kron(rho.T, np.eye(d)) @ choi
        op4 = op.reshape(d, d, d, d)  # (sys1_row, sys2_row, sys1_col, sys2_col)
        return np.einsum("ikil->kl", op4)  # trace over system 1

    return phi


def kraus_from_choi(choi, d, tol=1e-12):
    """K_a = sqrt(lambda_a) * reshape(v_a, (d,d))^T (eigenvalue absorbed).

    NO extra sqrt(d): the eigenvalue alone carries the normalization in the
    UNNORMALIZED convention. (The source note's K_r = sqrt(d) * vec^{-1}(v_r)
    is the NORMALIZED-convention factor; pairing it with an unnormalized Choi
    overcounts by sqrt(d).)
    """
    herm = (choi + choi.conj().T) / 2
    w, v = np.linalg.eigh(herm)
    kraus = []
    for a in range(len(w)):
        if w[a] > tol:
            mat = v[:, a].reshape(d, d).T
            kraus.append(np.sqrt(w[a]) * mat)
    return kraus


def partial_trace_output(choi, d):
    """Tr_2 C_Phi: partial trace over the OUTPUT (second) factor."""
    c4 = choi.reshape(d, d, d, d)
    return np.einsum("ikjk->ij", c4)


def partial_trace_input(choi, d):
    """Tr_1 C_Phi: partial trace over the INPUT (first) factor; equals Phi(I)."""
    c4 = choi.reshape(d, d, d, d)
    return np.einsum("kikj->ij", c4)


def random_cptp(d, n_kraus, rng):
    """Random CPTP map via Stinespring: K_a = <a| V, V: C^d -> C^d (x) C^{n}.

    V is an isometry (orthonormal columns), so sum_a K_a^dagger K_a = I exactly:
    a primitive-level CPTP generator, no fitted/measured input.
    """
    m = rng.normal(size=(d * n_kraus, d)) + 1j * rng.normal(size=(d * n_kraus, d))
    q, _ = np.linalg.qr(m)  # (d*n_kraus, d), orthonormal columns => isometry
    return [q[a * d : (a + 1) * d, :].copy() for a in range(n_kraus)]


def random_density(d, rng):
    a = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    rho = a @ a.conj().T
    return rho / np.trace(rho).real


def min_herm_eig(a):
    herm = (a + a.conj().T) / 2
    return float(np.linalg.eigvalsh(herm).min().real)


# --------------------------------------------------------------------------- #
# Part A -- exact sympy check on the qubit (d = 2): inverse formula has NO     #
#           d-factor in the unnormalized convention.                          #
# --------------------------------------------------------------------------- #
def part_a_sympy_qubit():
    print("-" * 72)
    print("Part A -- exact (sympy) qubit check: unnormalized inverse formula")
    print("-" * 72)
    d = 2

    def skron(a, b):
        return sp.Matrix(
            sp.BlockMatrix(
                [[a[i, j] * b for j in range(a.cols)] for i in range(a.rows)]
            )
        )

    # General single-Kraus CP map Phi(x) = K x K^dagger with symbolic K.
    a, b, c, e = sp.symbols("a b c e")
    kk = sp.Matrix([[a, b], [c, e]])

    def phi(x):
        return kk * x * kk.conjugate().T

    # Unnormalized Choi C = sum_ij |i><j| (x) Phi(|i><j|).
    choi = sp.zeros(d * d, d * d)
    for i in range(d):
        for j in range(d):
            eij = sp.zeros(d, d)
            eij[i, j] = 1
            choi += skron(eij, phi(eij))

    # Inverse formula Phi(rho) = Tr_1[(rho^T (x) I) C], NO d-factor.
    r0, r1, r2, r3 = sp.symbols("r0 r1 r2 r3")
    rho = sp.Matrix([[r0, r1], [r2, r3]])
    op = skron(rho.T, sp.eye(d)) * choi
    tr1 = sp.zeros(d, d)
    for k in range(d):
        tr1 += op[k * d : (k + 1) * d, k * d : (k + 1) * d]
    diff = sp.simplify(tr1 - phi(rho))
    check(
        "A1 exact inverse round-trip on M_2 (no d-factor)",
        diff == sp.zeros(d, d),
        "Tr_1[(rho^T (x) I) C] - Phi(rho) == 0 symbolically",
    )

    # If one (wrongly) inserted the normalized Choi (1/d) but kept the no-d
    # inverse, the round-trip would be off by exactly 1/d -- the mixed-convention
    # bug. Show that the WRONG combination does NOT reduce to Phi(rho).
    choi_norm = choi / d
    op_w = skron(rho.T, sp.eye(d)) * choi_norm
    tr1_w = sp.zeros(d, d)
    for k in range(d):
        tr1_w += op_w[k * d : (k + 1) * d, k * d : (k + 1) * d]
    diff_w = sp.simplify(tr1_w - phi(rho))
    check(
        "A2 mixed convention (normalized Choi + no-d inverse) is OFF by 1/d",
        diff_w != sp.zeros(d, d) and sp.simplify(tr1_w - phi(rho) / d) == sp.zeros(d, d),
        "documents the repaired inconsistency: result = Phi(rho)/d, not Phi(rho)",
    )


# --------------------------------------------------------------------------- #
# Part B -- numeric end-to-end on M_2 (qubit) and M_2 (x) M_2 (two-qubit).    #
# --------------------------------------------------------------------------- #
def part_b_numeric(d, label, rng):
    print("-" * 72)
    print(f"Part B -- numeric end-to-end on {label} (d = {d})")
    print("-" * 72)
    atol = 1e-10

    for trial in range(40):
        n_kraus = rng.integers(1, d * d + 1)
        kraus = random_cptp(d, int(n_kraus), rng)
        map_fn = lambda x, ks=kraus: apply_kraus(ks, x)

        # 1. generating map is CPTP at the primitive level
        ok_tp_in = kraus_tp_defect(kraus, d) < atol

        # 2. Choi (unnormalized), PSD <=> CP
        choi = choi_unnormalized(map_fn, d)
        ok_psd = min_herm_eig(choi) > -atol

        # 3. TP <=> Tr_2 C = I (output partial trace)
        ok_tr2 = np.linalg.norm(partial_trace_output(choi, d) - np.eye(d)) < atol

        # 4. Tr_1 C = Phi(I) (input partial trace identity)
        ok_tr1 = np.allclose(partial_trace_input(choi, d), map_fn(np.eye(d)), atol=atol)

        # 5. inverse formula round-trips on a random density matrix
        phi_rec = map_from_choi(choi, d)
        rho = random_density(d, rng)
        ok_inv = np.allclose(phi_rec(rho), map_fn(rho), atol=atol)

        # 6. Kraus extracted from Choi reproduce the map exactly
        kraus_rec = kraus_from_choi(choi, d)
        ok_kr_map = np.allclose(apply_kraus(kraus_rec, rho), map_fn(rho), atol=atol)

        # 7. extracted Kraus are themselves trace-preserving
        ok_kr_tp = kraus_tp_defect(kraus_rec, d) < atol

        # 8. extracted Kraus rebuild the SAME Choi (full round trip)
        choi_back = choi_unnormalized(lambda x, ks=kraus_rec: apply_kraus(ks, x), d)
        ok_choi_rt = np.linalg.norm(choi_back - choi) < atol

        if not (ok_tp_in and ok_psd and ok_tr2 and ok_tr1 and ok_inv
                and ok_kr_map and ok_kr_tp and ok_choi_rt):
            check(f"{label} trial {trial} (all 8 links)", False,
                  f"tp_in={ok_tp_in} psd={ok_psd} tr2={ok_tr2} tr1={ok_tr1} "
                  f"inv={ok_inv} kr_map={ok_kr_map} kr_tp={ok_kr_tp} "
                  f"choi_rt={ok_choi_rt}")
            return

    check(f"{label} generator CPTP at primitive level (40 trials)", True,
          "sum_a K_a^dagger K_a = I from Stinespring isometry")
    check(f"{label} C_Phi PSD <=> CP (40 trials)", True, "min eig(C) >= 0")
    check(f"{label} TP <=> Tr_2 C_Phi = I (40 trials)", True,
          "output partial trace = I_d")
    check(f"{label} Tr_1 C_Phi = Phi(I) (40 trials)", True,
          "input partial trace identity")
    check(f"{label} inverse formula round-trips (40 trials)", True,
          "Phi(rho) = Tr_1[(rho^T (x) I) C], no d-factor")
    check(f"{label} extracted Kraus reproduce map (40 trials)", True,
          "K_a = sqrt(lambda_a) reshape(v_a)^T, no extra sqrt(d)")
    check(f"{label} extracted Kraus are trace-preserving (40 trials)", True,
          "sum_a K_a^dagger K_a = I_d")
    check(f"{label} extracted Kraus rebuild same C_Phi (40 trials)", True,
          "full Kraus<->Choi round trip")


# --------------------------------------------------------------------------- #
# Part C -- named qubit channels (dephasing, depolarizing, unitary) + a       #
#           non-CP map whose Choi has a negative eigenvalue.                  #
# --------------------------------------------------------------------------- #
def part_c_named_channels():
    print("-" * 72)
    print("Part C -- named qubit channels and the CP boundary (d = 2)")
    print("-" * 72)
    d = 2
    atol = 1e-10
    eye = np.eye(2, dtype=complex)
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)

    p = 0.3
    dephasing = [np.sqrt(1 - p) * eye, np.sqrt(p) * sz]
    q = 0.2
    depolarizing = [
        np.sqrt(1 - 3 * q / 4) * eye,
        np.sqrt(q / 4) * sx,
        np.sqrt(q / 4) * sy,
        np.sqrt(q / 4) * sz,
    ]
    unitary = [(eye + 1j * sx) / np.sqrt(2)]  # exp(i pi/4 sx) up to phase, unitary

    for name, ks in [("dephasing", dephasing),
                     ("depolarizing", depolarizing),
                     ("unitary", unitary)]:
        map_fn = lambda x, kk=ks: apply_kraus(kk, x)
        choi = choi_unnormalized(map_fn, d)
        kraus_rec = kraus_from_choi(choi, d)
        rho = np.array([[0.6, 0.2 + 0.1j], [0.2 - 0.1j, 0.4]], dtype=complex)
        ok = (
            kraus_tp_defect(ks, d) < atol
            and min_herm_eig(choi) > -atol
            and np.linalg.norm(partial_trace_output(choi, d) - eye) < atol
            and np.allclose(map_from_choi(choi, d)(rho), map_fn(rho), atol=atol)
            and np.allclose(apply_kraus(kraus_rec, rho), map_fn(rho), atol=atol)
            and kraus_tp_defect(kraus_rec, d) < atol
        )
        check(f"{name} channel: full reconciled chain holds", ok)

    # Transpose map: positive but NOT completely positive -> Choi has neg eig.
    transpose_choi = choi_unnormalized(lambda x: x.T.copy(), d)
    check("transpose map is non-CP (Choi has a negative eigenvalue)",
          min_herm_eig(transpose_choi) < -1e-6,
          f"min eig = {min_herm_eig(transpose_choi):.4f}")


# --------------------------------------------------------------------------- #
# Part D -- normalization-consistency guards (the actual repair).             #
# --------------------------------------------------------------------------- #
def part_d_normalization_guards(rng):
    print("-" * 72)
    print("Part D -- normalization-consistency guards (the repaired d-factors)")
    print("-" * 72)
    atol = 1e-10
    d = 2
    kraus = random_cptp(d, 3, rng)
    map_fn = lambda x: apply_kraus(kraus, x)
    rho = random_density(d, rng)

    # Unnormalized chain (ours): everything consistent.
    choi_u = choi_unnormalized(map_fn, d)
    ok_u = np.allclose(map_from_choi(choi_u, d)(rho), map_fn(rho), atol=atol)
    check("unnormalized |Omega> + no-d inverse: consistent", ok_u)

    # Wrong mix 1: normalized Choi (1/d) with the no-d inverse -> off by 1/d.
    choi_n = choi_u / d
    res_n = map_from_choi(choi_n, d)(rho)
    ok_mix1 = (not np.allclose(res_n, map_fn(rho), atol=atol)) and np.allclose(
        res_n, map_fn(rho) / d, atol=atol
    )
    check("normalized Choi + no-d inverse is OFF by exactly 1/d (the bug)",
          ok_mix1, "result = Phi(rho)/d")

    # Wrong mix 2: unnormalized Choi but Kraus given the spurious sqrt(d) factor
    # -> map overcounted by d.
    herm = (choi_u + choi_u.conj().T) / 2
    w, v = np.linalg.eigh(herm)
    kraus_spurious = [
        np.sqrt(d) * np.sqrt(w[a]) * v[:, a].reshape(d, d).T
        for a in range(len(w)) if w[a] > 1e-12
    ]
    res_sp = apply_kraus(kraus_spurious, rho)
    ok_mix2 = (not np.allclose(res_sp, map_fn(rho), atol=atol)) and np.allclose(
        res_sp, d * map_fn(rho), atol=atol
    )
    check("unnormalized Choi + spurious sqrt(d) Kraus overcounts by d (the bug)",
          ok_mix2, "result = d * Phi(rho)")

    # The matched normalized convention (1/d Choi AND sqrt(d) Kraus AND d-inverse)
    # is internally consistent too -- demonstrating the fix is 'pick one', not
    # 'one is right'. Here C_n = C/d, eigenvalues lambda^n = lambda/d, and
    # K_a = sqrt(d) * sqrt(lambda^n) * reshape(v_a)^T = sqrt(lambda) reshape(v_a)^T,
    # i.e. the SAME Kraus operators -- so the map is reproduced.
    herm_n = (choi_n + choi_n.conj().T) / 2
    wn, vn = np.linalg.eigh(herm_n)
    kraus_norm_conv = [
        np.sqrt(d) * np.sqrt(wn[a]) * vn[:, a].reshape(d, d).T
        for a in range(len(wn)) if wn[a] > 1e-12
    ]
    ok_norm_conv = np.allclose(apply_kraus(kraus_norm_conv, rho), map_fn(rho), atol=atol)
    # And the matched normalized inverse Phi(rho) = d * Tr_1[(rho^T (x) I) C_n].
    res_norm_inv = d * map_from_choi(choi_n, d)(rho)
    ok_norm_inv = np.allclose(res_norm_inv, map_fn(rho), atol=atol)
    check("matched normalized convention (1/d Choi + sqrt(d) Kraus + d-inverse) is also consistent",
          ok_norm_conv and ok_norm_inv, "confirms fix = pick ONE convention end-to-end")


def main() -> int:
    print("=" * 72)
    print("Kraus<->Choi correspondence with reconciled Choi normalization")
    print("=" * 72)
    print("Convention: UNNORMALIZED |Omega> = sum_i |i>|i>; C = (id (x) Phi)|Omega><Omega|;")
    print("            Phi(rho)=Tr_1[(rho^T (x) I) C]; K_a=sqrt(lambda_a) reshape(v_a)^T.")
    print("Reproven from primitives (numpy Stinespring + exact sympy). Choi 1975 /")
    print("Nielsen-Chuang Ch.8 are comparators only, not derivation inputs.")

    rng = np.random.default_rng(seed=20260605)
    part_a_sympy_qubit()
    part_b_numeric(2, "M_2 (qubit)", rng)
    part_b_numeric(4, "M_2 (x) M_2 (two-qubit)", rng)
    part_c_named_channels()
    part_d_normalization_guards(rng)

    print("=" * 72)
    print(f"TOTAL: {PASS} PASS / {FAIL} FAIL")
    print("=" * 72)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
