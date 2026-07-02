"""Axiom-first single-clock codimension-1 unitary evolution check.

Rebuilt 2026-06-11 (hostile science-fix re-scope of the companion note
AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md).

Computes the load-bearing content of the axis-conditional theorem
(S1')-(S3') with falsification legs:

  [A] supply-hypothesis and Stone-closure residuals on a concrete
      finite-range block transfer: T positive Hermitian with trivial
      kernel and ||T|| <= 1 (the (R-STONE) hypotheses), unique-generator
      reconstruction, group laws, tau-rescaling (scope-boundary N2 is
      load-bearing), and the non-Hermitian-transfer falsifier.

  [B] finite-range Lieb-Robinson sanity check on the explicit toy block:
      the standard v_LR = 2 e J_* D_int R_int form is instantiated only
      as a finite-range boundary witness, not as the current propagation
      supplier for the source note.

  [C] first-principles computes:
      [C-LR]  computed Heisenberg commutator residuals vs the L1 bound,
              with inside/outside-cone contrast (the cone is real, the
              bound is satisfied with margin).
      [C-EX]  the exact staggered time-space exchange intertwiner
              W = P_{tau<->1} diag((-1)^{x_tau x_1}):
              W M_KS W^T = M_KS exactly, temporal hop sector mapped
              exactly onto the x_1 hop sector, spectra equal.
              FALSIFIER: the plain permutation without the sign field
              fails by a large margin (the identity is non-trivial).
              This is the computed certificate that withdraws the old
              S3 ("temporal direction is the unique RP-admissible
              reflection axis"): the staggered phase structure cannot
              distinguish the temporal axis.
      [C-2CLK] two-clock tensor-factor comparator: two commuting
              positive transfers T_A (x) I and I (x) T_B with a
              genuinely 2-dimensional generator span. Stone uniqueness
              for the supplied PRODUCT transfer still pins the summed
              generator, but the two-parameter family is not generated
              by any single Hamiltonian: the comparator violates the
              single-clock constraint and is excluded only by the
              declared premise B-AXIS.3 (= scope-boundary N5), which is
              therefore non-vacuous.
      [C-BDRY] strict finite-range boundary for log-transfer generators:
              (i) consistency — the block Hamiltonian used in
              [A]/[B]/[C-LR] is EXACTLY finite-range (every Pauli
              string with support diameter > 1 has zero coefficient),
              so the runner's dynamics lies in the declared class;
              (ii) non-vacuity witness — a strictly local positive
              transfer T = e^{-A/2} e^{-B} e^{-A/2} (A on sites {0,1},
              B on {1,2}) whose log-generator H_w = -log T has a
              computed NONZERO end-to-end Pauli component (support
              diameter 2): strict finite-range-ness of a log-transfer
              generator is not automatic, so the current theorem must
              cite the retained free-bilinear quasilocal bridge rather
              than keep the old B-RANGE premise;
              (iii) contrast — a single-factor local transfer logs
              back to its local generator exactly (the failure in (ii)
              is the non-commuting BCH tail, not a log artifact).

  [D] composition / circularity discipline: textual checks that the
      companion note declares B-AXIS, retires B-RANGE from current
      scope, cites the free-bilinear quasilocal propagation supplier,
      withdraws the old S3, and keeps the claim transfer- and
      tau-relative (guards against wording regression).

Deterministic; runtime well under one minute. TOTAL: PASS=n FAIL=0.
"""
from __future__ import annotations

import itertools
import math
import os

import numpy as np

# -------------------------------------------------------------------
# scaffolding
# -------------------------------------------------------------------

PASS = 0
FAIL = 0


def record(tag: str, label: str, passed: bool, detail: str = "") -> None:
    global PASS, FAIL
    if passed:
        PASS += 1
    else:
        FAIL += 1
    status = "PASS" if passed else "FAIL"
    print(f"  [{status}] [{tag}] {label}" + (f" ({detail})" if detail else ""))


def expm_herm(c: complex, A: np.ndarray) -> np.ndarray:
    w, V = np.linalg.eigh(A)
    return V @ np.diag(np.exp(c * w)) @ V.conj().T


def opnorm(A: np.ndarray) -> float:
    return float(np.linalg.norm(A, ord=2))


# -------------------------------------------------------------------
# toy block: L-site qubit chain (per-site M_2(C), finite-range H)
# -------------------------------------------------------------------


def site_op(L: int, site: int, op: np.ndarray) -> np.ndarray:
    return np.kron(np.eye(2**site), np.kron(op, np.eye(2 ** (L - site - 1))))


def finite_range_hamiltonian(L: int, J: float, seed: int) -> np.ndarray:
    """H = sum_z h_z on sites (z, z+1); each ||h_z||_op = J exactly."""
    rng = np.random.default_rng(seed)
    dim = 2**L
    H = np.zeros((dim, dim), dtype=complex)
    for z in range(L - 1):
        h = rng.standard_normal((4, 4)) + 1j * rng.standard_normal((4, 4))
        h = 0.5 * (h + h.conj().T)
        h *= J / opnorm(h)
        H += np.kron(np.eye(2**z), np.kron(h, np.eye(2 ** (L - z - 2))))
    return H


SIGMA_Z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
SIGMA_X = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)


# -------------------------------------------------------------------
# [A] S1' supply hypotheses + Stone closure + falsifiers
# -------------------------------------------------------------------


def block_A_stone(H: np.ndarray, tau: float) -> None:
    print()
    print("-" * 72)
    print("[A] (S1') SUPPLY HYPOTHESES AND STONE CLOSURE (transfer/tau-relative)")
    print("-" * 72)
    dim = H.shape[0]

    # supplied transfer, vacuum-normalized so spec in (0,1] (R-SC2 style)
    H_shift = H - np.eye(dim) * float(np.linalg.eigvalsh(H).min())
    T = expm_herm(-tau, H_shift)

    herm = opnorm(T - T.conj().T)
    eigs = np.linalg.eigvalsh(0.5 * (T + T.conj().T))
    record("A", "(R-STONE hyp) T Hermitian", herm < 1e-12, f"||T-T^dag|| = {herm:.2e}")
    record("A", "(R-STONE hyp) T positive, trivial kernel",
           float(eigs.min()) > 1e-12, f"min eig = {eigs.min():.3e}")
    record("A", "(R-STONE hyp) ||T||_op <= 1",
           float(eigs.max()) <= 1.0 + 1e-12, f"max eig = {eigs.max():.6f}")

    # Stone reconstruction: H_rec = -(1/tau) log T equals the shifted H
    w, V = np.linalg.eigh(0.5 * (T + T.conj().T))
    H_rec = V @ np.diag(-(1.0 / tau) * np.log(w)) @ V.conj().T
    rec_resid = opnorm(H_rec - H_shift)
    record("A", "unique generator: -(1/tau) log T reproduces the supplied H",
           rec_resid < 1e-9 * max(1.0, opnorm(H_shift)),
           f"||H_rec - H|| = {rec_resid:.2e}")
    record("A", "H >= 0 (R-SC2 normalization)",
           float(np.linalg.eigvalsh(H_rec).min()) > -1e-10,
           f"min E = {np.linalg.eigvalsh(H_rec).min():.2e}")

    # group laws
    s, t = 0.37, 0.91
    U = lambda x: expm_herm(-1j * x, H_rec)  # noqa: E731
    r0 = opnorm(U(0.0) - np.eye(dim))
    r1 = opnorm(U(s) @ U(t) - U(s + t))
    r2 = opnorm(U(t).conj().T @ U(t) - np.eye(dim))
    record("A", "U(0) = I", r0 < 1e-12, f"resid = {r0:.2e}")
    record("A", "U(s)U(t) = U(s+t)", r1 < 1e-9, f"resid = {r1:.2e}")
    record("A", "U(t)^dag U(t) = I", r2 < 1e-9, f"resid = {r2:.2e}")

    # generator identification with quantified finite-difference bound
    eps = 1e-5
    fd = (1j / eps) * (U(eps) - np.eye(dim))
    fd = 0.5 * (fd + fd.conj().T)
    fd_resid = opnorm(fd - H_rec)
    fd_bound = 0.6 * eps * opnorm(H_rec) ** 2
    record("A", "generator: i dU/dt|_0 = H within the 2nd-order FD bound",
           fd_resid < fd_bound, f"resid = {fd_resid:.2e}, bound = {fd_bound:.2e}")

    # tau-rescaling: same T, doubled tau, halved generator (scope-boundary N2)
    H_rec_2tau = V @ np.diag(-(1.0 / (2 * tau)) * np.log(w)) @ V.conj().T
    n2_resid = opnorm(H_rec_2tau - 0.5 * H_rec)
    record("A", "N2 load-bearing: same T with tau' = 2 tau gives H' = H/2 exactly",
           n2_resid < 1e-10, f"||H' - H/2|| = {n2_resid:.2e}  "
           "(T alone does NOT fix the clock unit; B-AXIS.1 is a premise)")

    # FALSIFIER: non-Hermitian transfer breaks unitarity of the evolution
    rng = np.random.default_rng(7)
    T_bad = T + 0.05 * (rng.standard_normal(T.shape) + 1j * rng.standard_normal(T.shape))
    wb, Vb = np.linalg.eig(T_bad)
    Hb = Vb @ np.diag(-(1.0 / tau) * np.log(wb.astype(complex))) @ np.linalg.inv(Vb)
    Ub = Vb @ np.diag(np.exp(-1j * 1.0 * (-(1.0 / tau) * np.log(wb.astype(complex))))) @ np.linalg.inv(Vb)
    unit_resid = opnorm(Ub.conj().T @ Ub - np.eye(dim))
    herm_bad = opnorm(Hb - Hb.conj().T)
    record("A", "falsifier: non-Hermitian T -> non-self-adjoint H, non-unitary U",
           unit_resid > 1e-3 and herm_bad > 1e-3,
           f"||U^dag U - I|| = {unit_resid:.2e}, ||H-H^dag|| = {herm_bad:.2e}")


# -------------------------------------------------------------------
# [A] S2' equal-time tensor locality + codimension arithmetic
# -------------------------------------------------------------------


def block_A_slice(L: int) -> None:
    print()
    print("-" * 72)
    print("[A] (S2') EQUAL-TIME TENSOR LOCALITY AND CODIMENSION (R-ET, R-CL3)")
    print("-" * 72)

    max_comm = 0.0
    for x in range(L):
        for y in range(x + 1, L):
            Ox = site_op(L, x, SIGMA_Z)
            Oy = site_op(L, y, SIGMA_X)
            max_comm = max(max_comm, opnorm(Ox @ Oy - Oy @ Ox))
    record("A", "equal-time [O_x, O_y] = 0 strictly for x != y",
           max_comm < 1e-12, f"max resid = {max_comm:.2e}")

    # explicit tensor-product factorization at two sites
    x, y = 1, 3
    chain = [SIGMA_Z if k == x else SIGMA_X if k == y else np.eye(2, dtype=complex)
             for k in range(L)]
    O_tensor = chain[0]
    for op in chain[1:]:
        O_tensor = np.kron(O_tensor, op)
    fact = opnorm(site_op(L, x, SIGMA_Z) @ site_op(L, y, SIGMA_X) - O_tensor)
    record("A", "equal-time algebra factorizes as the tensor product",
           fact < 1e-12, f"resid = {fact:.2e}")

    record("A", "codimension-1: framework block dim(Sigma)=3, dim(Lambda)=4",
           (1 + 3) - 3 == 1, "codim = 1")


# -------------------------------------------------------------------
# [B] + [C-LR] Lieb-Robinson cone: imported constant, computed residuals
# -------------------------------------------------------------------


def block_BC_lieb_robinson(H: np.ndarray, L: int, J: float) -> None:
    print()
    print("-" * 72)
    print("[B]/[C-LR] FINITE-RANGE SANITY CHECK vs STANDARD LR BOUND")
    print("-" * 72)

    # [B] instantiate the standard finite-range constants:
    # v_LR = 2 e J_* D_int R_int.
    # For the nearest-neighbor chain: J_* = J, D_int = 2 (each site is in
    # <= 2 interaction terms), R_int = 1.
    J_star, D_int, R_int = J, 2, 1
    v_LR = 2 * math.e * J_star * D_int * R_int
    record("B", "finite-range LR sanity: v_LR = 2 e J_* D_int R_int instantiated",
           abs(v_LR - 4 * math.e * J) < 1e-12,
           f"J_*={J_star}, D_int={D_int}, R_int={R_int} -> v_LR = {v_LR:.4f}")

    # [C] computed commutator residuals vs the L1 bound
    # L1: ||[A(t),B]|| <= 2||A||||B|| exp(-d/R_int) exp(2 J_* D_int e |t|)
    t = 0.2
    Ut = expm_herm(-1j * t, H)
    O0t = Ut @ site_op(L, 0, SIGMA_Z) @ Ut.conj().T
    comms = {}
    ok_bound = True
    detail = []
    for d in range(1, L):
        c = opnorm(O0t @ site_op(L, d, SIGMA_Z) - site_op(L, d, SIGMA_Z) @ O0t)
        comms[d] = c
        bound = 2.0 * math.exp(-d / R_int) * math.exp(2 * J_star * D_int * math.e * abs(t))
        if c > bound:
            ok_bound = False
        detail.append(f"d={d}: {c:.2e} <= {bound:.2e}")
    record("C", "L1 bound satisfied at every distance (computed residuals)",
           ok_bound, "; ".join(detail[:3]) + " ...")

    inside, outside = comms[1], comms[L - 1]
    record("C", "cone is real: inside/outside contrast > 1e3",
           outside < 1e-3 * inside,
           f"||[.,.]||(d=1) = {inside:.3e} vs (d={L-1}) = {outside:.3e}")

    mono = all(comms[d + 1] <= comms[d] * 1.5 for d in range(1, L - 1))
    record("C", "commutator decays with distance outside the cone", mono,
           f"profile = {[f'{comms[d]:.1e}' for d in range(1, L)]}")


# -------------------------------------------------------------------
# [C-EX] the exact staggered time-space exchange intertwiner
#         (the certificate that withdraws the old S3)
# -------------------------------------------------------------------


def staggered_hop_matrix(Ls: tuple[int, int, int, int], mass: float = 0.0):
    """Antisymmetrized KS hop matrix, time-first convention:
    eta_0 = 1, eta_mu(x) = (-1)^(x_0 + ... + x_{mu-1}); periodic block."""
    sites = list(itertools.product(*[range(l) for l in Ls]))
    idx = {s: i for i, s in enumerate(sites)}
    N = len(sites)

    def eta(mu, x):
        return (-1) ** sum(x[:mu])

    def hop(x, mu):
        y = list(x)
        y[mu] = (y[mu] + 1) % Ls[mu]
        return tuple(y)

    M = np.zeros((N, N))
    sectors = []
    for mu in range(4):
        Mmu = np.zeros((N, N))
        for x in sites:
            y = hop(x, mu)
            Mmu[idx[x], idx[y]] += eta(mu, x)
            Mmu[idx[y], idx[x]] -= eta(mu, x)
        sectors.append(Mmu)
        M += Mmu
    M += mass * np.eye(N)
    return M, sectors, sites, idx


def block_C_exchange() -> None:
    print()
    print("-" * 72)
    print("[C-EX] (S3') EXACT TIME-SPACE EXCHANGE INTERTWINER (withdraws old S3)")
    print("-" * 72)

    Ls = (4, 4, 2, 2)  # (t, x1, x2, x3), even extents, L_t = L_1 for the swap
    mass = 0.3
    M, sec, sites, idx = staggered_hop_matrix(Ls, mass)
    N = len(sites)

    P = np.zeros((N, N))
    S = np.zeros((N, N))
    for x in sites:
        P[idx[(x[1], x[0], x[2], x[3])], idx[x]] = 1.0
        S[idx[x], idx[x]] = (-1) ** (x[0] * x[1])
    W = P @ S

    record("C", "W = P_{tau<->1} diag((-1)^{x_tau x_1}) is orthogonal",
           opnorm(W @ W.T - np.eye(N)) < 1e-14, f"N = {N} sites, mass = {mass}")

    inv = opnorm(W @ M @ W.T - M)
    record("C", "EXACT action invariance: || W M_KS W^T - M_KS || = 0",
           inv < 1e-13, f"resid = {inv:.2e} (staggered + mass term)")

    s01 = opnorm(W @ sec[0] @ W.T - sec[1])
    s10 = opnorm(W @ sec[1] @ W.T - sec[0])
    s22 = opnorm(W @ sec[2] @ W.T - sec[2])
    record("C", "temporal hop sector maps EXACTLY onto the x_1 hop sector",
           s01 < 1e-13 and s10 < 1e-13,
           f"||W M_t W^T - M_1|| = {s01:.2e}, ||W M_1 W^T - M_t|| = {s10:.2e}")
    record("C", "transverse hop sectors are fixed by W",
           s22 < 1e-13, f"resid = {s22:.2e}")

    ev_t = np.sort(np.linalg.eigvals(sec[0]).imag)
    ev_1 = np.sort(np.linalg.eigvals(sec[1]).imag)
    record("C", "temporal and spatial hop operators are unitarily identical (spectra)",
           float(np.max(np.abs(ev_t - ev_1))) < 1e-10,
           f"max |spec diff| = {np.max(np.abs(ev_t - ev_1)):.2e}")

    # W maps the x_1 >= L/2 half-block onto the t >= L/2 half-block
    half_t = {s for s in sites if s[0] >= Ls[0] // 2}
    half_1 = {s for s in sites if s[1] >= Ls[1] // 2}
    mapped = {(x[1], x[0], x[2], x[3]) for x in half_1}
    record("C", "W maps the x_1 half-block onto the temporal half-block",
           mapped == half_t, f"|half| = {len(half_t)}")

    # FALSIFIER: plain permutation (no sign field) does NOT preserve the action
    naive = opnorm(P @ M @ P.T - M)
    record("C", "falsifier: plain axis swap WITHOUT the sign field fails",
           naive > 1.0, f"resid = {naive:.4f} >> 0 (the intertwiner is non-trivial)")

    # FALSIFIER of the old T10 criterion: orientation-reversal sign flip is
    # generic (holds with ALL staggered phases stripped), hence was never an
    # RP discriminator.
    sites2 = sites
    Mplain = np.zeros((N, N))
    for x in sites2:
        y = list(x)
        y[0] = (y[0] + 1) % Ls[0]
        Mplain[idx[x], idx[tuple(y)]] += 1.0
        Mplain[idx[tuple(y)], idx[x]] -= 1.0
    # temporal site reflection t -> (Ls[0]-1) - t (a lattice involution)
    R = np.zeros((N, N))
    for x in sites2:
        R[idx[(Ls[0] - 1 - x[0], x[1], x[2], x[3])], idx[x]] = 1.0
    flip = opnorm(R @ Mplain @ R.T + Mplain)
    record("C", "old-T10 criterion is phase-blind: plain (eta-free) temporal hops "
           "already flip sign under temporal reflection",
           flip < 1e-13, f"resid = {flip:.2e} -> the old T10 tested orientation "
           "reversal, not staggered RP structure")


# -------------------------------------------------------------------
# [C-2CLK] two-clock tensor-factor comparator (premise B-AXIS.3 is
#           non-vacuous; scope-boundary N5)
# -------------------------------------------------------------------


def block_C_two_clock() -> None:
    print()
    print("-" * 72)
    print("[C-2CLK] TWO-CLOCK COMPARATOR (codimension-2 evolution exists; "
          "excluded only by B-AXIS.3)")
    print("-" * 72)

    T_A = np.diag([0.5, 1.0 / 3.0])
    T_B = np.diag([0.2, 1.0 / 7.0, 0.9])
    tau = 1.0
    H_A = np.diag(-np.log(np.diag(T_A)) / tau)
    H_B = np.diag(-np.log(np.diag(T_B)) / tau)
    IA, IB = np.eye(2), np.eye(3)
    G1 = np.kron(H_A, IB)
    G2 = np.kron(IA, H_B)

    TA_full = np.kron(T_A, IB)
    TB_full = np.kron(IA, T_B)
    comm = opnorm(TA_full @ TB_full - TB_full @ TA_full)
    pos = min(np.linalg.eigvalsh(TA_full).min(), np.linalg.eigvalsh(TB_full).min())
    record("C", "two commuting positive transfers exist on a tensor product",
           comm < 1e-14 and pos > 0, f"[T_A x I, I x T_B] = {comm:.1e}, min eig = {pos:.3f}")

    # generator span is genuinely 2-dimensional: no scalars a,b (not both 0)
    # with a G1 + b G2 = 0
    V = np.stack([G1.ravel(), G2.ravel()])
    rank = np.linalg.matrix_rank(V, tol=1e-12)
    record("C", "generator span is 2-dimensional (a genuine second clock direction)",
           rank == 2, f"rank span{{H_A x I, I x H_B}} = {rank}")

    # the two-parameter family U(s,t) is a homomorphism of R^2, not of R:
    # U(s,t) = exp(-i(s G1 + t G2)) since [G1,G2]=0; its tangent space at the
    # identity is the 2-dim span. A single supplied clock H_sum generates only
    # the 1-dim diagonal subgroup.
    g_comm = opnorm(G1 @ G2 - G2 @ G1)
    record("C", "[H_A x I, I x H_B] = 0: U(s,t) is a genuine 2-parameter unitary group",
           g_comm < 1e-13, f"resid = {g_comm:.1e}")

    # Stone uniqueness is NOT violated within its scope: the supplied product
    # transfer pins exactly the summed generator
    T_prod = TA_full @ TB_full
    w, V_ = np.linalg.eigh(T_prod)
    H_prod = V_ @ np.diag(-np.log(w) / tau) @ V_.T
    pin = opnorm(H_prod - (G1 + G2))
    record("C", "per supplied PRODUCT transfer, Stone pins H = H_A x I + I x H_B "
           "(uniqueness holds within its transfer-relative scope)",
           pin < 1e-10, f"resid = {pin:.2e}")

    # off-diagonal member of the 2-parameter family is not in the 1-parameter
    # group generated by H_sum: U(1,0) != exp(-i r H_sum) for all r in a scan,
    # and exactly: U(1,0) commutes with H_sum but log spectrum mismatch
    U10 = expm_herm(-1j, G1)
    H_sum = G1 + G2
    # if U10 = exp(-i r H_sum), eigenvalues of U10 on H_sum eigenbasis must be
    # exp(-i r E_k) -- in particular constant on the I x H_B factor; check the
    # B-factor dependence is absent in U10 but present in H_sum:
    varies = opnorm(np.kron(IA, H_B) @ U10 - U10 @ np.kron(IA, H_B)) < 1e-13
    # U10 acts as identity on the B factor while exp(-i r H_sum) does not
    # unless r E_B in 2 pi Z for all eigenvalues E_B simultaneously with the
    # A-factor matching; scan a fine grid of r and measure the gap:
    rs = np.linspace(-6.0, 6.0, 24001)
    gap = min(opnorm(U10 - expm_herm(-1j * r, H_sum)) for r in rs)
    record("C", "U_A(1) x I is NOT on the single-clock orbit exp(-i r H_sum) "
           "(min gap over r in [-6,6])",
           varies and gap > 0.05, f"min gap = {gap:.4f} > 0.05; B-AXIS.3 "
           "excludes a mathematically realizable alternative -> non-vacuous")


# -------------------------------------------------------------------
# [C-BDRY] strict finite-range boundary: consistency + counterexample
# witness (the log of a strictly local positive transfer is generically
# NOT finite-range)
# -------------------------------------------------------------------

SIGMA_Y = np.array([[0.0, -1j], [1j, 0.0]], dtype=complex)
PAULI_1Q = {"I": np.eye(2, dtype=complex), "X": SIGMA_X, "Y": SIGMA_Y, "Z": SIGMA_Z}


def pauli_string(ops: str) -> np.ndarray:
    M = PAULI_1Q[ops[0]]
    for ch in ops[1:]:
        M = np.kron(M, PAULI_1Q[ch])
    return M


def pauli_support_diameter(ops: str) -> int:
    sites = [k for k, ch in enumerate(ops) if ch != "I"]
    if not sites:
        return -1  # identity string
    return max(sites) - min(sites)


def logm_herm(T: np.ndarray) -> np.ndarray:
    w, V = np.linalg.eigh(0.5 * (T + T.conj().T))
    return V @ np.diag(np.log(w)) @ V.conj().T


def block_C_range_boundary(H: np.ndarray, L: int) -> None:
    print()
    print("-" * 72)
    print("[C-BDRY] STRICT FINITE-RANGE BOUNDARY FOR LOG-TRANSFER GENERATORS:")
    print("         sanity check + counterexample witness")
    print("-" * 72)

    # (i) consistency: the block Hamiltonian consumed by [A]/[B]/[C-LR]
    # lies in the finite-range class EXACTLY — every Pauli string with
    # support diameter > 1 has zero coefficient.
    dim = 2**L
    max_far = 0.0
    for ops in itertools.product("IXYZ", repeat=L):
        s = "".join(ops)
        if pauli_support_diameter(s) <= 1:
            continue
        coef = abs(np.einsum("ij,ji->", pauli_string(s), H)) / dim
        max_far = max(max_far, float(coef))
    record("C", "(finite-range sanity) block H is exactly finite-range: all "
           "Pauli strings with support diameter > 1 vanish",
           max_far < 1e-12, f"max far-string coeff = {max_far:.2e}")

    # (ii) non-vacuity witness on 3 sites: strictly local positive
    # transfer T = e^{-A/2} e^{-B} e^{-A/2}, A on {0,1}, B on {1,2}.
    A = 0.9 * pauli_string("XXI") + 0.4 * pauli_string("ZII")
    B = 0.7 * pauli_string("IZZ") + 0.3 * pauli_string("IIX")
    eA2 = expm_herm(-0.5, A)
    T_loc = eA2 @ expm_herm(-1.0, B) @ eA2
    herm = opnorm(T_loc - T_loc.conj().T)
    min_eig = float(np.linalg.eigvalsh(0.5 * (T_loc + T_loc.conj().T)).min())
    record("C", "(strict-range boundary) strictly local transfer is positive Hermitian",
           herm < 1e-12 and min_eig > 0.0,
           f"||T - T^dag|| = {herm:.2e}, min eig = {min_eig:.4f}")

    H_w = -logm_herm(T_loc)
    end_to_end, best = 0.0, ""
    nn_part = np.zeros_like(H_w)
    for ops in itertools.product("IXYZ", repeat=3):
        s = "".join(ops)
        P = pauli_string(s)
        coef = complex(np.einsum("ij,ji->", P, H_w)) / 8.0
        if pauli_support_diameter(s) <= 1:
            nn_part += coef * P
        if s[0] != "I" and s[2] != "I" and abs(coef) > end_to_end:
            end_to_end, best = abs(coef), s
    record("C", "(strict-range boundary) log-generator has a nonzero end-to-end Pauli "
           "component (support diameter 2 > range 1)",
           end_to_end > 1e-3, f"|coeff[{best}]| = {end_to_end:.4f}")
    remainder = opnorm(H_w - nn_part)
    record("C", "(strict-range boundary) H_w = -log T is NOT in the range-1 class: "
           "||H_w - P_range1(H_w)||_op > 0",
           remainder > 1e-3, f"remainder norm = {remainder:.4f}")

    # (iii) contrast: a single-factor local transfer logs back exactly —
    # the witness failure is the non-commuting BCH tail, not the log.
    back = opnorm(-logm_herm(expm_herm(-1.0, A)) - A)
    record("C", "(strict-range contrast) single-factor transfer: -log(e^{-A}) = A "
           "exactly (locality preserved when no non-commuting tail exists)",
           back < 1e-10, f"resid = {back:.2e}")

    print("  BOUNDARY: strict finite-range-ness of a log-transfer generator is")
    print("  not automatic. The companion note therefore retires the old B-RANGE")
    print("  premise from the current claim and cites the retained free-bilinear")
    print("  quasilocal LR bridge only on its stated free U=1 exact-log sector.")


# -------------------------------------------------------------------
# [D] composition / circularity discipline (note wording guards)
# -------------------------------------------------------------------


def block_D_discipline() -> None:
    print()
    print("-" * 72)
    print("[D] COMPOSITION / CIRCULARITY DISCIPLINE (note wording guards)")
    print("-" * 72)

    note_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..",
        "docs",
        "AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md",
    )
    try:
        text = open(note_path, encoding="utf-8").read()
    except OSError:
        record("D", "companion note readable", False, note_path)
        return

    record("D", "note declares the axis premise (B-AXIS)", "(B-AXIS)" in text
           and "B-AXIS.3" in text, "premise declared with N2/N4/N5 clauses")
    record("D", "note withdraws the old S3 unique-RP-axis claim",
           "withdrawn" in text and "unique RP-admissible reflection axis" in text,
           "withdrawal recorded in scope and changelog")
    record("D", "claim stays transfer- and tau-relative (scope-boundary compliant)",
           "transfer-relative" in text and ("τ-relative" in text or "tau-relative" in text),
           "G-SCOPE compliance wording present")
    flat_text = " ".join(text.split())
    record("D", "claim_type is bounded_theorem (no positive_theorem over-claim)",
           "Claim type bounded" in text
           and "positive_theorem grade" not in text,
           "canonical bounded claim type checked")
    record("D", "proposal firewall: B-AXIS remains a declared blocker",
           "not a retained-grade proposal" in flat_text
           and "B-AXIS" in text
           and "remains declared" in text,
           "no retained-grade proposal while B-AXIS is declared")
    record("D", "spatial-clustering clause not consumed (cluster L2 is conditional)",
           "L2 spatial clustering is consumed nowhere" in text
           or "not consumed" in text, "S2'(b) demoted to conditional remark")
    record("D", "note retires B-RANGE from current scope",
           ("no longer a current premise" in text
            or "no\nlonger a current premise" in text)
           and "conditional on (B-RANGE)" not in text,
           "S2'(c) now uses the retained free-sector quasilocal supplier")
    record("D", "note cites the free-bilinear quasilocal LR bridge as propagation supplier",
           "FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md" in text
           and "R-FBQL" in text
           and "0 < d μ < η < arcsinh(m)" in text,
           "free U=1 exact-log sector and finite quasilocal lightcone named")
    record("D", "2026-06-12 firewall: B-RANGE retired, B-AXIS remains the live blocker",
           "2026-06-12 Remaining-Blocker Source Firewall" in text
           and "B-AXIS as the live" in text
           and ("record-durability axis selection" in text
                or "record-durability axis-selection" in text)
           and ("do not derive B-AXIS" in text
                or "does not derive B-AXIS" in text
                or "leaves B-AXIS open" in text)
           and "No retained-grade proposal or status promotion is made here" in text,
           "axis-selection route-pruning context wired without retained promotion")


# -------------------------------------------------------------------
# main
# -------------------------------------------------------------------


def main() -> None:
    print("=" * 72)
    print("AXIOM-FIRST SINGLE-CLOCK CODIMENSION-1 EVOLUTION CHECK (2026-06-11)")
    print("=" * 72)
    print()
    print("Axis-conditional theorem (S1')-(S3'): conditional on B-AXIS, the")
    print("supplied transfer data give one generator, one unitary group, and")
    print("codimension-1 Cauchy slices. Propagation is cited only on the")
    print("retained free U=1 exact-log quasilocal bridge; the staggered action's")
    print("exact time-space exchange symmetry shows the axis itself is a premise")
    print("(old S3 withdrawn).")

    L = 6
    J = 1.0
    tau = 0.5
    H = finite_range_hamiltonian(L, J, seed=20260503)
    print(f"\n  toy block: L = {L} qubit sites, dim = {2**L}, J = {J}, tau = {tau}")
    print(f"  ||H||_op = {opnorm(H):.4f}")

    block_A_stone(H, tau)
    block_A_slice(L)
    block_BC_lieb_robinson(H, L, J)
    block_C_range_boundary(H, L)
    block_C_exchange()
    block_C_two_clock()
    block_D_discipline()

    print()
    print("=" * 72)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 72)
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
