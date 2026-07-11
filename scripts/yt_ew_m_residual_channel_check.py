"""yt_ew M-residual repair: Fierz channels and the propagator-scaling bridge.

The exact lemma is that both degree-2 Fierz channels scale by |lambda|²
whenever the propagator is multiplied by any complex scalar lambda.  This
runner then separates the link-to-propagator question by mass sector: for a
massless one-link, link-linear hopping matrix it derives
G[u_0 V] = u_0^{-1} G[V], while at nonzero mass it computes a rejector for
overall scalar action.  Thus the massive conclusion requires the named
premise (P-G); the old imposed G_full = u_0 G_V relation is retained only as
conditional bookkeeping context.

Tests 1-4 and 6-7 retain the original channel checks.  Test 5 is split into
the general scalar blindness lemma (5a), massless derivation (5b), and
massive rejector (5c).  Test 8 pins the repaired note surface and date.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np


def gell_mann_su2() -> list[np.ndarray]:
    """Pauli matrices / 2 for SU(2)."""
    s1 = np.array([[0, 1], [1, 0]], dtype=complex) / 2
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex) / 2
    s3 = np.array([[1, 0], [0, -1]], dtype=complex) / 2
    return [s1, s2, s3]


def gell_mann_su3() -> list[np.ndarray]:
    """Gell-Mann matrices / 2 for SU(3)."""
    L1 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex)
    L2 = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex)
    L3 = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex)
    L4 = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex)
    L5 = np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex)
    L6 = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
    L7 = np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex)
    L8 = (1 / np.sqrt(3)) * np.array(
        [[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex
    )
    return [L / 2 for L in [L1, L2, L3, L4, L5, L6, L7, L8]]


def random_traceless_hermitian(N: int, rng: np.random.Generator) -> list[np.ndarray]:
    """Build orthonormal traceless Hermitian basis (random SU(N) generator basis)."""
    if N == 2:
        return gell_mann_su2()
    if N == 3:
        return gell_mann_su3()
    # General N: not implemented for this stretch attempt
    raise NotImplementedError(f"SU({N}) generator basis not supported in this stretch attempt")


def random_su_n(N: int, rng: np.random.Generator) -> np.ndarray:
    """Sample a Haar-distributed SU(N) matrix by QR with determinant repair."""

    z = rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))
    q, r = np.linalg.qr(z)
    diag = np.diag(r)
    phases = np.where(np.abs(diag) > 0, diag / np.abs(diag), 1.0)
    q = q * phases.conj()

    # Multiplying one column by det(q)^* preserves unitarity and fixes det=1.
    q[:, 0] *= np.linalg.det(q).conjugate()
    return q


def channel_values(G: np.ndarray, generators: list[np.ndarray]) -> tuple[float, float]:
    """Return the singlet and adjoint degree-2 Fierz channels for G."""

    N = G.shape[0]
    singlet = float((1 / N) * abs(np.trace(G)) ** 2)
    adjoint = float(2 * sum(abs(np.trace(G @ t)) ** 2 for t in generators))
    return singlet, adjoint


def one_link_ring_hopping(links: list[np.ndarray]) -> np.ndarray:
    """Forward-minus-backward antihermitian hopping on a periodic 1D ring."""

    L = len(links)
    N = links[0].shape[0]
    H = np.zeros((L * N, L * N), dtype=complex)
    for x, link in enumerate(links):
        y = (x + 1) % L
        xs = slice(x * N, (x + 1) * N)
        ys = slice(y * N, (y + 1) * N)
        H[xs, ys] += link
        H[ys, xs] -= link.conj().T
    return H


def main() -> None:
    print("=" * 72)
    print("yt_ew M-RESIDUAL STRETCH ATTEMPT: FIERZ CHANNEL BOOKKEEPING UNDER CMT")
    print("=" * 72)
    print()

    rng = np.random.default_rng(42)

    # ----- Test 1: Fierz identity on random complex matrices for SU(2), SU(3) -----
    print("-" * 72)
    print("TEST 1: Fierz identity Tr[M† M] = (1/N) |Tr M|² + 2 Σ_A |Tr[M t^A]|²")
    print("-" * 72)
    max_fierz_dev = 0.0
    for N in [2, 3]:
        T = random_traceless_hermitian(N, rng)
        for trial in range(5):
            # Random complex matrix M
            M = rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))
            lhs = np.trace(M.conj().T @ M).real
            singlet = (1 / N) * abs(np.trace(M)) ** 2
            adjoint = 2 * sum(abs(np.trace(M @ t)) ** 2 for t in T)
            rhs = singlet + adjoint
            dev = abs(lhs - rhs)
            max_fierz_dev = max(max_fierz_dev, dev)
        print(f"  N={N}: max Fierz residual = {max_fierz_dev:.3e}")
    t1_ok = max_fierz_dev < 1e-10
    print(f"  STATUS: {'PASS' if t1_ok else 'FAIL'}")
    print()

    # ----- Test 2: Adjoint channel fraction exactly (N²-1)/N² -----
    print("-" * 72)
    print("TEST 2: dim(adj)/dim(N⊗N̄) = (N²-1)/N² (channel fraction)")
    print("-" * 72)
    for N in [2, 3, 4, 5]:
        adj_dim = N ** 2 - 1
        total_dim = N ** 2
        frac = adj_dim / total_dim
        print(f"  N={N}: dim(adj)={adj_dim}, dim(total)={total_dim}, fraction={frac:.4f}")
    expected_at_3 = 8 / 9
    actual_at_3 = (3 ** 2 - 1) / 3 ** 2
    t2_ok = abs(actual_at_3 - expected_at_3) < 1e-15
    print(f"  At N=3: 8/9 = {expected_at_3:.6f}, computed = {actual_at_3:.6f}")
    print(f"  STATUS: {'PASS' if t2_ok else 'FAIL'}")
    print()

    # ----- Test 3: Channel decomposition on random SU(N) propagator-like matrices -----
    print("-" * 72)
    print("TEST 3: Tr_color[G G^†] = S(G) + C(G) on random non-trivial G")
    print("-" * 72)
    max_decomp_dev = 0.0
    for N in [2, 3]:
        T = random_traceless_hermitian(N, rng)
        for trial in range(10):
            G = rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))
            lhs = np.trace(G.conj().T @ G).real
            S = (1 / N) * abs(np.trace(G)) ** 2
            C = 2 * sum(abs(np.trace(G @ t)) ** 2 for t in T)
            d = abs(lhs - (S + C))
            max_decomp_dev = max(max_decomp_dev, d)
        print(f"  N={N}: 10 trials, max ||Tr[G†G] - (S+C)|| = {max_decomp_dev:.3e}")
    t3_ok = max_decomp_dev < 1e-10
    print(f"  STATUS: {'PASS' if t3_ok else 'FAIL'}")
    print()

    # ----- Test 4: Singlet on identity background (color-diagonal G) -----
    print("-" * 72)
    print("TEST 4: Color-diagonal G = g · I_N has S = N · g², C = 0")
    print("        (static-CMT limit: all singlet, no adjoint)")
    print("-" * 72)
    max_diag_dev = 0.0
    for N in [2, 3]:
        T = random_traceless_hermitian(N, rng)
        for g_val in [1.0, 0.5, 2.0, -1.5]:
            G_diag = g_val * np.eye(N, dtype=complex)
            S = (1 / N) * abs(np.trace(G_diag)) ** 2
            S_expected = N * g_val ** 2
            C = 2 * sum(abs(np.trace(G_diag @ t)) ** 2 for t in T)
            d_S = abs(S - S_expected)
            d_C = abs(C - 0)
            max_diag_dev = max(max_diag_dev, d_S, d_C)
        print(f"  N={N}: S_diag exact, C_diag = 0 (max dev = {max_diag_dev:.3e})")
    t4_ok = max_diag_dev < 1e-10
    print(f"  STATUS: {'PASS' if t4_ok else 'FAIL'}")
    print(f"  ⇒ Color-diagonal (static) G has ONLY singlet content; adjoint requires V fluctuations.")
    print()

    # ----- Test 5a: exact channel blindness for every overall scalar action -----
    print("-" * 72)
    print("TEST 5a: S(lambda G) and C(lambda G) scale by |lambda|²")
    print("         for general complex scalar action on G")
    print("-" * 72)
    max_scalar_dev = 0.0
    scalar_samples = [
        -1.25 + 0.0j,
        0.70 + 0.40j,
        0.85 + 0.0j,
        complex(*rng.standard_normal(2)),
        complex(*rng.standard_normal(2)),
    ]
    for N in [2, 3]:
        T = random_traceless_hermitian(N, rng)
        for scalar in scalar_samples:
            G = rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))
            S, C = channel_values(G, T)
            S_scaled, C_scaled = channel_values(scalar * G, T)
            factor = abs(scalar) ** 2
            max_scalar_dev = max(
                max_scalar_dev,
                abs(S_scaled - factor * S),
                abs(C_scaled - factor * C),
            )
        print(f"  N={N}: negative-real, genuinely-complex, and random lambda samples checked")
    print("  (P-G)-conditional bookkeeping, previously Test 5: lambda = u_0")
    print(f"  max scalar-channel deviation = {max_scalar_dev:.3e}")
    t5a_ok = max_scalar_dev < 1e-10
    print(f"  STATUS: {'PASS' if t5a_ok else 'FAIL'}")
    print()

    # ----- Test 5b: derive scalar action for massless link-linear hopping -----
    print("-" * 72)
    print("TEST 5b: Massless derivation on a one-link L=7 SU(3) ring")
    print("-" * 72)
    L = 7
    N = 3
    dim = L * N
    u_0 = 0.85
    cond_H = np.inf
    for reroll in range(100):
        links_V = [random_su_n(N, rng) for _ in range(L)]
        H_V = one_link_ring_hopping(links_V)
        cond_H = np.linalg.cond(H_V)
        if cond_H <= 1e8:
            break
    else:
        raise RuntimeError("could not sample an invertible, well-conditioned massless hopping")

    H_full = one_link_ring_hopping([u_0 * V for V in links_V])
    linear_dev = np.linalg.norm(H_full - u_0 * H_V)
    G_V = np.linalg.inv(H_V)
    G_full = np.linalg.inv(H_full)
    inverse_rel_dev = np.linalg.norm(G_full - (u_0 ** -1) * G_V) / np.linalg.norm(G_full)

    T = gell_mann_su3()
    factor = u_0 ** -2
    channel_abs_dev = 0.0
    channel_scale = 1.0
    for x in range(L):
        for y in range(L):
            xs = slice(x * N, (x + 1) * N)
            ys = slice(y * N, (y + 1) * N)
            S_V, C_V = channel_values(G_V[xs, ys], T)
            S_full, C_full = channel_values(G_full[xs, ys], T)
            channel_abs_dev = max(
                channel_abs_dev,
                abs(S_full - factor * S_V),
                abs(C_full - factor * C_V),
            )
            channel_scale = max(channel_scale, factor * S_V, factor * C_V)
    channel_rel_dev = channel_abs_dev / channel_scale
    t5b_ok = linear_dev < 1e-13 and inverse_rel_dev < 1e-12 and channel_rel_dev < 1e-12
    print(f"  accepted hopping after {reroll} reroll(s), cond(H[V]) = {cond_H:.3e}")
    print(f"  H[u_0 V] == u_0 H[V]: max deviation = {linear_dev:.3e}")
    print(f"  G_full == u_0^-1 G_V: relative deviation = {inverse_rel_dev:.3e}")
    print(f"  all {L * L} site-pair color blocks: S,C scale by u_0^-2")
    print(f"  max relative channel deviation = {channel_rel_dev:.3e}")
    print(f"  STATUS: {'PASS' if t5b_ok else 'FAIL'}")
    print()

    # ----- Test 5c: massive inverse rejects overall scalar action -----
    print("-" * 72)
    print("TEST 5c: Massive rejector for scalar propagator action at m = 1/2")
    print("-" * 72)
    mass = 0.5
    identity = np.eye(dim, dtype=complex)
    G_m_V = np.linalg.inv(mass * identity + H_V)
    G_m_full = np.linalg.inv(mass * identity + u_0 * H_V)
    ratio = G_m_full @ np.linalg.inv(G_m_V)
    ratio_scalar = np.trace(ratio) / dim
    massive_relative_deviation = np.linalg.norm(ratio - ratio_scalar * identity) / np.linalg.norm(ratio)
    t5c_ok = massive_relative_deviation > 1e-2
    print("  R = G_m[u_0 V] @ inv(G_m[V])")
    print(f"  relative deviation from (tr R / dim) I = {massive_relative_deviation:.6e}")
    print("  decisive threshold: deviation > 1e-2")
    print(f"  STATUS: {'PASS' if t5c_ok else 'FAIL'}")
    print()

    # ----- Test 6: Haar SU(N) V-fluctuation generates adjoint content -----
    print("-" * 72)
    print("TEST 6: Haar SU(N) link V generates non-trivial adjoint content")
    print("        with unitarity and determinant-one residuals checked explicitly")
    print("-" * 72)
    print()
    print("  N | mean(C/(S+C)) over 5000 Haar-SU(N) trials | expected (N²-1)/N²")
    print("  ---|----------------------------------------|------------------")
    t6_ok = True
    for N in [2, 3]:
        T = random_traceless_hermitian(N, rng)
        ratios = []
        max_unitarity_dev = 0.0
        max_det_dev = 0.0
        for trial in range(5000):
            V = random_su_n(N, rng)
            max_unitarity_dev = max(max_unitarity_dev, np.linalg.norm(V.conj().T @ V - np.eye(N)))
            max_det_dev = max(max_det_dev, abs(np.linalg.det(V) - 1))
            S = (1 / N) * abs(np.trace(V)) ** 2
            C = 2 * sum(abs(np.trace(V @ t)) ** 2 for t in T)
            if S + C > 0:
                ratios.append(C / (S + C))
        mean_ratio = np.mean(ratios)
        expected = (N ** 2 - 1) / N ** 2
        print(f"  {N} | {mean_ratio:.4f}                                 | {expected:.4f}")
        print(f"      max ||V†V-I||={max_unitarity_dev:.2e}, max |det(V)-1|={max_det_dev:.2e}")
        if abs(mean_ratio - expected) > 0.02:
            t6_ok = False
    print(f"  STATUS: {'PASS' if t6_ok else 'FAIL'}")
    print(f"  ⇒ Haar SU(N) links statistically realize the (N²-1)/N² adjoint fraction.")
    print()

    # ----- Test 7: Numerical at N=3 — adjoint dominates at expected fraction -----
    print("-" * 72)
    print("TEST 7: At N=3 (framework's N_c), adjoint fraction = 8/9 ≈ 0.8889")
    print("-" * 72)
    print()
    T = gell_mann_su3()
    n_trials = 5000
    ratios = []
    max_unitarity_dev = 0.0
    max_det_dev = 0.0
    for trial in range(n_trials):
        V = random_su_n(3, rng)
        max_unitarity_dev = max(max_unitarity_dev, np.linalg.norm(V.conj().T @ V - np.eye(3)))
        max_det_dev = max(max_det_dev, abs(np.linalg.det(V) - 1))
        S = (1 / 3) * abs(np.trace(V)) ** 2
        C = 2 * sum(abs(np.trace(V @ t)) ** 2 for t in T)
        if S + C > 0:
            ratios.append(C / (S + C))
    mean_ratio = np.mean(ratios)
    std_ratio = np.std(ratios) / np.sqrt(n_trials)
    expected = 8 / 9
    print(f"  N=3 with {n_trials} Haar-SU(3) link trials:")
    print(f"    mean(C/(S+C)) = {mean_ratio:.4f} ± {std_ratio:.4f}")
    print(f"    expected (N²-1)/N² = 8/9 = {expected:.4f}")
    print(f"    deviation = {abs(mean_ratio - expected):.4f}")
    print(f"    max ||V†V-I||={max_unitarity_dev:.2e}, max |det(V)-1|={max_det_dev:.2e}")
    t7_ok = abs(mean_ratio - expected) < 0.01 and max_unitarity_dev < 1e-12 and max_det_dev < 1e-12
    print(f"  STATUS: {'PASS' if t7_ok else 'FAIL'}")
    print()

    # ----- Test 8: repaired note-surface pins -----
    print("-" * 72)
    print("TEST 8: Repaired note-surface pins")
    print("-" * 72)
    note_path = Path(__file__).resolve().parents[1] / "docs" / "YT_EW_M_RESIDUAL_NOTE_2026-05-02.md"
    note_text = note_path.read_text(encoding="utf-8")
    claim_scope_block = note_text.split("**Claim scope:**", 1)[1].split("**Status authority:**", 1)[0]
    key_finding_block = note_text.split("## Key finding", 1)[1].split("## Where the actual selection", 1)[0]
    yaml_block = note_text.split("```yaml", 1)[1].split("```", 1)[0]
    repair_block = note_text.split("## Repair Note", 1)[1].split("## Background", 1)[0]
    old_unconditional_scope = (
        "The runner verifies that under U → u_0 V factorization, both S and C inherit "
        "the same u_0² factor uniformly"
    )
    note_pins = {
        "(P-G) in claim scope": "(P-G)" in claim_scope_block,
        "(P-G) in key finding": "(P-G)" in key_finding_block,
        "(P-G) in yaml": "(P-G)" in yaml_block,
        '"Massless derivation" present': "Massless derivation" in note_text,
        "2026-07-11 Repair Note present": "2026-07-11" in repair_block,
        "old unconditional claim-scope sentence absent": old_unconditional_scope not in " ".join(
            claim_scope_block.replace("**", "").split()
        ),
    }
    for label, passed in note_pins.items():
        print(f"  {label}: {'PASS' if passed else 'FAIL'}")
    t8_ok = all(note_pins.values())
    print(f"  STATUS: {'PASS' if t8_ok else 'FAIL'}")
    print()

    print("=" * 72)
    print(f"  Test 1 (Fierz identity exact):                          {'PASS' if t1_ok else 'FAIL'}")
    print(f"  Test 2 (channel fraction (N²-1)/N²):                    {'PASS' if t2_ok else 'FAIL'}")
    print(f"  Test 3 (channel decomposition on random G):             {'PASS' if t3_ok else 'FAIL'}")
    print(f"  Test 4 (color-diagonal G has only singlet, no adjoint): {'PASS' if t4_ok else 'FAIL'}")
    print(f"  Test 5a (scalar-action blindness lemma):                {'PASS' if t5a_ok else 'FAIL'}")
    print(f"  Test 5b (massless link-to-propagator derivation):        {'PASS' if t5b_ok else 'FAIL'}")
    print(f"  Test 5c (massive scalar-action rejector):                {'PASS' if t5c_ok else 'FAIL'}")
    print(f"  Test 6 (Haar SU(N) V-fluctuation generates adjoint):   {'PASS' if t6_ok else 'FAIL'}")
    print(f"  Test 7 (N=3 adjoint fraction = 8/9):                    {'PASS' if t7_ok else 'FAIL'}")
    print(f"  Test 8 (repaired note-surface pins):                     {'PASS' if t8_ok else 'FAIL'}")
    results = [t1_ok, t2_ok, t3_ok, t4_ok, t5a_ok, t5b_ok, t5c_ok, t6_ok, t7_ok, t8_ok]
    pass_count = sum(results)
    fail_count = len(results) - pass_count
    all_ok = all(results)
    print(f"  TOTAL: PASS={pass_count} FAIL={fail_count}")
    print(f"  OVERALL: {'PASS' if all_ok else 'FAIL'}")
    print()
    print("RESIDUAL (sharpened obstruction):")
    print("  The scalar-action lemma and massless link-to-propagator bridge are exact")
    print("  at machine precision. What remains for full closure of (M):")
    print()
    print("  (i)  Define the framework's lattice EW current as a Wilson-line bilinear")
    print("       (currently implicit; needs explicit formula in framework primitives).")
    print("  (ii) Show: physical (CMT-improved) EW vacuum polarization corresponds to")
    print("       the adjoint channel C, while the singlet channel S is absorbed into")
    print("       the link improvement u_0^n_link. Scalar action is channel-blind:")
    print("       it is derived with u_0^-2 channel scaling at m=0, and is conditional")
    print("       on (P-G) at m!=0, where Test 5c rejects automatic scalar action.")
    print()
    print("  Until (ii) is closed, (M) remains a structural input. This stretch")
    print("  attempt sharpens (M) to a single named question: which channel survives")
    print("  CMT improvement in the framework's specific EW current construction?")
    if not all_ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
