#!/usr/bin/env python3
"""Supplied SU(3) on a three-dimensional symmetric carrier: invariant
singlet tests, not reconstruction of a physical gauge group from projectors.
The inherited diagonal SU(2) action on Sym^2(C^2) is spin one; SU(3) is an
additional chosen action. All matrix constructions are supplied. Symbolic
checks and floating-point SVD/singlet residual checks are distinguished.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120

import sys
from itertools import permutations, product

import numpy as np

try:
    import sympy as sp
    from sympy import I as sym_I
    from sympy import Matrix, Rational, eye, simplify, sqrt as sym_sqrt, zeros
except ImportError:  # pragma: no cover
    print("FAIL: sympy required")
    sys.exit(1)


# ----------------------------------------------------------------------------
# bookkeeping + capped output to file
# ----------------------------------------------------------------------------
PASS = 0
FAIL = 0
EPS = 1e-12
_LINES: list[str] = []
_MAX_LINES = 600  # capped report


def emit(s: str = "") -> None:
    _LINES.append(s)
    if len(_LINES) <= _MAX_LINES:
        print(s)
    elif len(_LINES) == _MAX_LINES + 1:
        print("... (further lines truncated in stdout; full log in cache file) ...")


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  ({detail})" if detail else ""
    emit(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    emit()
    emit("-" * 84)
    emit(title)
    emit("-" * 84)


def rss_mb() -> float:
    """Best-effort RSS sampler (no hard dep on psutil)."""
    try:
        import resource

        ru = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        # macOS reports bytes; Linux reports kilobytes.
        if sys.platform == "darwin":
            return ru / (1024 * 1024)
        return ru / 1024
    except Exception:
        return float("nan")


def kron(*mats):
    r = mats[0]
    for m in mats[1:]:
        r = np.kron(r, m)
    return r


def sym_eq(A: Matrix, B: Matrix) -> bool:
    if A.shape != B.shape:
        return False
    d = A - B
    for i in range(d.rows):
        for j in range(d.cols):
            if simplify(d[i, j]) != 0:
                return False
    return True


# ----------------------------------------------------------------------------
# shared algebra: Pauli, Gell-Mann, U_base, the embedded generators
# (construction matches CL3_SU3_SYMMETRIC_BASE_COMMUTANT note)
# ----------------------------------------------------------------------------
def pauli():
    s1 = Matrix([[0, 1], [1, 0]])
    s2 = Matrix([[0, -sym_I], [sym_I, 0]])
    s3 = Matrix([[1, 0], [0, -1]])
    return [s1, s2, s3]


def gell_mann():
    lam = [
        Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
        Matrix([[0, -sym_I, 0], [sym_I, 0, 0], [0, 0, 0]]),
        Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]]),
        Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
        Matrix([[0, 0, -sym_I], [0, 0, 0], [sym_I, 0, 0]]),
        Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
        Matrix([[0, 0, 0], [0, 0, -sym_I], [0, sym_I, 0]]),
        Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -2]]) / sym_sqrt(3),
    ]
    return lam


def u_base():
    s2 = sym_sqrt(2)
    # rows = new basis (sym0, sym1, sym2, antisym) in terms of (00,01,10,11)
    return Matrix(
        [
            [1, 0, 0, 0],
            [0, 0, 0, 1],
            [0, Rational(1) / s2, Rational(1) / s2, 0],
            [0, Rational(1) / s2, -Rational(1) / s2, 0],
        ]
    )


def embed_M4(X3: Matrix, U: Matrix) -> Matrix:
    """diag(X3 on 3D sym block, 0 on 1D antisym block), rotated to (00..11)."""
    blk = zeros(4, 4)
    for i in range(3):
        for j in range(3):
            blk[i, j] = X3[i, j]
    return U.H * blk * U


# ----------------------------------------------------------------------------
# numpy bridges of the symbolic objects (for sweeps)
# ----------------------------------------------------------------------------
def to_np(M: Matrix) -> np.ndarray:
    return np.array(M.evalf(), dtype=complex)


def main() -> int:
    emit("=" * 84)
    emit("FINITE MODEL: supplied symmetric-base SU(3) and fiber SU(2)")
    emit("Invariant tensor/projector checks; physical color assignment remains open.")
    emit("Carrier: C^8 = C^4_base (x) C^2_fiber. Symbolic and floating-point checks.")
    emit("=" * 84)

    sigmas = pauli()
    lam = gell_mann()
    U = u_base()
    I2 = eye(2)
    I4 = eye(4)

    # embedded base-SU(3) generators T^a_8D = M_{3,sym}(lam^a/2) (x) I_2
    # built exactly via explicit tensor (sympy has no kron helper here)
    T8 = []
    for a in range(8):
        M4 = embed_M4(lam[a] / 2, U)
        T = zeros(8, 8)
        for i in range(4):
            for j in range(4):
                for k in range(2):
                    T[2 * i + k, 2 * j + k] = M4[i, j]
        T8.append(T)

    # fiber SU(2) generators Jf_i = I_4 (x) sigma_i/2
    Jf = []
    for i in range(3):
        J = zeros(8, 8)
        si = sigmas[i] / 2
        for p in range(4):
            for r in range(2):
                for c in range(2):
                    J[2 * p + r, 2 * p + c] = si[r, c]
        Jf.append(J)

    # ========================================================================
    section("PART 1: two candidate local symmetries -> two DISTINCT record algebras")
    # ========================================================================
    emit("(i)  base SU(3): T^a_8D on the 3D symmetric base block (color).")
    emit("(ii) fiber SU(2): Jf_i = I_4 (x) sigma_i/2 (weak isospin).")
    emit("")

    # sanity: base SU(3) closes, fiber SU(2) closes, and the two commute.
    # base SU(3) Lie closure (sample a few brackets to confirm su(3), cheap)
    f123 = simplify((-sym_I) * ((T8[0] * T8[1] - T8[1] * T8[0]) - sym_I * T8[2]).norm())
    check("base SU(3): [T^1,T^2] = i T^3 (f^123=1)", f123 == 0)
    # fiber SU(2) closure
    su2_ok = sym_eq(Jf[0] * Jf[1] - Jf[1] * Jf[0], sym_I * Jf[2])
    check("fiber SU(2): [J^1,J^2] = i J^3", su2_ok)
    # the two symmetries commute (tensor-product factors)
    comm_all = all(sym_eq(T8[a] * Jf[i], Jf[i] * T8[a]) for a in range(8) for i in range(3))
    check("[base SU(3), fiber SU(2)] = 0 (different tensor factors)", comm_all)

    # --- invariants (commutants) inside End(C^8) ---------------------------
    # commutant of a set of (numpy) generators = nullspace of the stacked
    # [G, .] superoperators. We compute dimensions exactly via sympy rank on
    # the real-rational super-operator where possible, else numpy SVD rank.
    def commutant_dim_np(gens_np):
        n = gens_np[0].shape[0]
        d = n * n
        rows = []
        I = np.eye(n)
        for G in gens_np:
            # vec(GX - XG) = (I (x) G - G^T (x) I) vec(X)
            S = np.kron(I, G) - np.kron(G.T, I)
            rows.append(S)
        A = np.vstack(rows)
        # rank via SVD
        s = np.linalg.svd(A, compute_uv=False)
        tol = max(A.shape) * np.finfo(float).eps * (s[0] if s.size else 1.0)
        rank = int((s > tol).sum())
        return d - rank

    T8_np = [to_np(T) for T in T8]
    Jf_np = [to_np(J) for J in Jf]

    dim_comm_su3 = commutant_dim_np(T8_np)
    dim_comm_su2 = commutant_dim_np(Jf_np)
    emit(f"  dim commutant(base SU(3)) in End(C^8) = {dim_comm_su3}")
    emit(f"  dim commutant(fiber SU(2)) in End(C^8) = {dim_comm_su2}")
    # The base SU(3) acts on the 3D sym block; its commutant within the 8D
    # algebra = (scalars on the 3D block) (+) End(1D antisym block), each (x)
    # End(C^2_fiber). dim = (1 + 1)*4 = ... compute structurally and compare.
    # We just assert they DIFFER, the load-bearing PART-1 point.
    check(
        "commutant(base SU(3)) != commutant(fiber SU(2)) (distinct record algebras)",
        dim_comm_su3 != dim_comm_su2,
        f"{dim_comm_su3} vs {dim_comm_su2}",
    )
    # fiber-SU(2) commutant should be End(C^4_base) (x) I_2 = 16-dim.
    check("commutant(fiber SU(2)) = End(C^4_base)(x)I_2 = 16", dim_comm_su2 == 16)

    # --- the explicit color singlets (records of base SU(3)) ---------------
    section("PART 1b: explicit base-SU(3) color singlets (eps_qqq, qqbar) -- the records")
    # work in the abstract color C^3 (the 3D sym base block), N_c = 3.
    Nc = 3
    lam_np = [to_np(L) for L in lam]
    Ta = [L / 2 for L in lam_np]  # fundamental generators on C^3

    # meson q-qbar singlet on C^3 (x) C^3 (qbar = conjugate rep):
    # generators act as Ta (x) I - I (x) Ta^* (conjugate on the qbar factor).
    qqbar_gens = [np.kron(Ta[a], np.eye(3)) - np.kron(np.eye(3), Ta[a].conj()) for a in range(8)]
    singlet_meson = (1 / np.sqrt(3)) * sum(
        np.kron(np.eye(3)[:, i], np.eye(3)[:, i]) for i in range(3)
    )
    inv_meson = all(np.linalg.norm(G @ singlet_meson) < 1e-10 for G in qqbar_gens)
    check("meson q-qbar singlet (1/sqrt3) sum|i ibar> is base-SU(3) invariant", inv_meson)
    # uniqueness: kernel of all qqbar gens is 1-dimensional (3 (x) 3bar = 1 + 8)
    Mstack = np.vstack(qqbar_gens)
    s = np.linalg.svd(Mstack, compute_uv=False)
    tol = max(Mstack.shape) * np.finfo(float).eps * s[0]
    null_meson = 9 - int((s > tol).sum())
    check("meson singlet multiplicity = 1 (3(x)3bar = 1+8)", null_meson == 1, f"dim={null_meson}")

    # baryon qqq singlet on C^3^(x)3: eps_{abc} q^a q^b q^c
    qqq_gens = [
        np.kron(np.kron(Ta[a], np.eye(3)), np.eye(3))
        + np.kron(np.kron(np.eye(3), Ta[a]), np.eye(3))
        + np.kron(np.kron(np.eye(3), np.eye(3)), Ta[a])
        for a in range(8)
    ]
    eps = np.zeros(27, dtype=complex)
    for p in permutations(range(3)):
        # sign of permutation
        sgn = 1
        pl = list(p)
        for i in range(3):
            for j in range(i + 1, 3):
                if pl[i] > pl[j]:
                    sgn = -sgn
        idx = 9 * p[0] + 3 * p[1] + p[2]
        eps[idx] = sgn
    eps = eps / np.linalg.norm(eps)
    inv_baryon = all(np.linalg.norm(G @ eps) < 1e-10 for G in qqq_gens)
    check("baryon eps_{abc} q^a q^b q^c is base-SU(3) invariant", inv_baryon)
    Bstack = np.vstack(qqq_gens)
    s = np.linalg.svd(Bstack, compute_uv=False)
    tol = max(Bstack.shape) * np.finfo(float).eps * s[0]
    null_baryon = 27 - int((s > tol).sum())
    check("baryon singlet multiplicity = 1 (3(x)3(x)3 = 1+8+8+10)", null_baryon == 1)

    # --- the fiber SU(2) singlets are DIFFERENT records --------------------
    # On C^2 (x) C^2, SU(2) singlet = (|01>-|10>)/sqrt2 (the antisym doublet).
    su2gen2 = [np.kron(to_np(sigmas[i] / 2), np.eye(2)) + np.kron(np.eye(2), to_np(sigmas[i] / 2)) for i in range(3)]
    su2_singlet = (np.kron(np.eye(2)[:, 0], np.eye(2)[:, 1]) - np.kron(np.eye(2)[:, 1], np.eye(2)[:, 0])) / np.sqrt(2)
    inv_su2 = all(np.linalg.norm(G @ su2_singlet) < 1e-10 for G in su2gen2)
    check("fiber SU(2) singlet = antisym doublet (|01>-|10>)/sqrt2 (a DIFFERENT record)", inv_su2)
    emit("  => the SU(3) color-singlet record algebra (eps_qqq, qqbar->1) is")
    emit("     STRUCTURALLY DISTINCT from the SU(2) weak-singlet record algebra.")

    # ========================================================================
    section("PART 2: invariant projectors do not uniquely reconstruct SU(3)")
    # ========================================================================
    emit("We test the invariant projectors of two supplied group actions;")
    emit("the singlets sit in the commutant on their tensor representations,")
    emit("commutant of the base-SU(3) generators (=their invariant algebra),")
    emit("without asserting that these projectors reconstruct a unique group.")
    emit("")
    # The color-singlet PROJECTORS are SU(3)-invariant operators on the matter,
    # i.e. they live in the commutant of the (diagonal) SU(3) action. Verify
    # P_meson = |singlet><singlet| commutes with every qqbar generator.
    P_meson = np.outer(singlet_meson, singlet_meson.conj())
    meson_in_commutant = all(np.linalg.norm(P_meson @ G - G @ P_meson) < 1e-10 for G in qqbar_gens)
    check("color-singlet projector P_meson IN commutant of base-SU(3) action", meson_in_commutant)
    P_baryon = np.outer(eps, eps.conj())
    baryon_in_commutant = all(np.linalg.norm(P_baryon @ G - G @ P_baryon) < 1e-10 for G in qqq_gens)
    check("color-singlet projector P_baryon IN commutant of base-SU(3) action", baryon_in_commutant)

    # Projector invariance is insufficient to reconstruct SU(3).
    # A scalar U(3) phase fixes the meson vector and multiplies the baryon
    # vector by a phase, leaving both rank-one projectors unchanged.
    phase = np.exp(0.17j)
    scalar3 = phase * np.eye(3)
    transformed_baryon = kron(scalar3, scalar3, scalar3) @ eps
    check("U(3) phase counterexample: baryon projector invariant",
          np.linalg.norm(np.outer(transformed_baryon, transformed_baryon.conj())-P_baryon)<EPS)
    check("same phase does not fix baryon vector",
          np.linalg.norm(transformed_baryon-eps)>0.1)
    emit("Projector invariance proves inclusion only, not unique group reconstruction.")
    emit("Fixing the alternating tensor itself within a supplied U(3) action adds det=1.")

    # ========================================================================
    section("PART 3: two supplied finite link models")
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    I2n = np.eye(2)

    def op4(op, slot):
        mats = [I2n, I2n, I2n, I2n]
        mats[slot] = op
        return kron(*mats)

    # endpoints A (slot0), link-end a (slot1), link-end b (slot2), endpoint B (slot3)
    # SU(2) Gauss generators at each endpoint (matter + adjacent link-end)
    SA = [(op4(s, 0) + op4(s, 1)) / 2 for s in (sx, sy, sz)]
    SB = [(op4(s, 2) + op4(s, 3)) / 2 for s in (sx, sy, sz)]

    def endpoint_invariance(O, gens):
        return all(np.linalg.norm(O @ G - G @ O) < 1e-9 for G in gens)

    # bare link-end transport (slot1<->slot2 raising), fully dressed Wilson line
    bare = op4(sx, 1)  # acts only on a link-end -> variant at A, invariant at B
    invA = endpoint_invariance(bare, SA)
    invB = endpoint_invariance(bare, SB)
    check("SU(2): bare link-end transport variant at A", not invA)
    check("SU(2): bare link-end transport invariant at B", invB)

    # This is a fiber-SU(2) Gauss law. Now build an SU(3) Gauss law on the SAME
    # kind of link by giving each endpoint a color triplet (C^3, = the Sym^2(C^2)
    # symmetric base block) and a link-end color (anti)triplet.
    # Carrier: endpoint(C^3) (x) link-end(C^3) at each end. (We use an abstract
    # C^3 here for the singlet algebra; the framework's C^3 is Sym^2(C^2) -- see
    # the SHARPENING below for that distinction.)
    def op_cc(op3, slot, nslots=2):
        mats = [np.eye(3)] * nslots
        mats[slot] = op3
        return kron(*mats)

    # single endpoint color Gauss law on (matter C^3, fundamental 3) (x)
    # (link-end C^3, CONJUGATE 3bar). This mirrors the U(1) Gauss law
    # G = sigma_z(A) + sigma_z(a): the link end carries the OPPOSITE
    # ("anti") charge so a matched matter+link-end pair can be a singlet.
    # SU(3) version: G^a = T^a(matter) + (-T^a*)(link-end).
    GA_color = [op_cc(Ta[a], 0) - op_cc(Ta[a].conj(), 1) for a in range(8)]
    # bare color link-end transport: a raising operator on the link-end only
    Elink = np.zeros((3, 3), dtype=complex)
    Elink[0, 1] = 1.0  # a non-symmetric link-end operator
    bare_color = op_cc(Elink, 1)
    color_invA = endpoint_invariance(bare_color, GA_color)
    check("SU(3): bare color link-end transport variant at endpoint A", not color_invA)

    # dressed color Wilson singlet: the matter-3 / link-end-3bar singlet
    # projector P_meson on (matter (x) link-end) is invariant under the
    # endpoint color Gauss law (the matched 3 (x) 3bar -> 1 contraction).
    s_3_3bar = (1 / np.sqrt(3)) * sum(np.kron(np.eye(3)[:, i], np.eye(3)[:, i]) for i in range(3))
    P_link_singlet = np.outer(s_3_3bar, s_3_3bar.conj())
    color_dressed_inv = endpoint_invariance(P_link_singlet, GA_color)
    check("SU(3): dressed color singlet invariant at endpoint A (Wilson-type)", color_dressed_inv)

    emit("")
    emit("Two chosen carriers admit the tested endpoint-invariance profiles.")
    # The discriminator (which generator sits on the link) is an INPUT.
    both_have_profile = (not invA) and invB and (not color_invA) and color_dressed_inv
    check(
        "two supplied carriers admit the tested variant/invariant profile",
        both_have_profile,
        "each symmetry admits the tested variant/invariant structure on its own link carrier",
    )

    section("SCOPE")
    emit("Supplied base SU(3) and fiber SU(2) have different commutants.")
    emit("Meson and baryon projectors are invariant under the supplied color action.")
    emit("These projectors also admit scalar U(3) phases: no unique gauge-group converse.")
    emit("Sym^2(C^2) is a vector-space carrier; its inherited SU(2) action is spin one.")
    emit("An additional SU(3) action and its physical color interpretation remain choices.")
    emit("Link tests concern two chosen models, not all theories satisfying axioms.")

    # ------------------------------------------------------------------------
    section("SELF-CHECK SUMMARY")
    peak = rss_mb()
    emit(f"  peak RSS (best-effort): {peak:.1f} MB  (cap 2048 MB)")
    rss_ok = (peak < 2048) or (peak != peak)  # nan tolerated
    if not rss_ok:
        emit("  [FAIL] RSS exceeded cap")
        globals()["FAIL"] += 1
    emit(f"  SUMMARY: PASS={PASS} FAIL={FAIL}")

    # The canonical SHA-pinned runner cache (logs/runner-cache/<stem>.txt) is
    # produced by scripts/precompute_audit_runners.py through the runner_cache
    # wrapper, which captures this stdout under the `===== runner cache v1 =====`
    # envelope. Do not hand-write the cache path here: a raw self-write clobbers
    # the v1 header (source hash, exit code, stdout/stderr sections) and the
    # cache parser then classifies the artifact as corrupt.

    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
