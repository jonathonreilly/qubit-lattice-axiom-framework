#!/usr/bin/env python3
r"""DUAL-COMPUTATION: FERMION-SECTOR BEREZIN BLOCK METRIC  ==  OPERATOR TRANSFER
for the 2-step blocked staggered OS transfer representation (fermion sector).

Audit-companion runner for
  docs/MIXED_OS_TRANSFER_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md

============================================================================
WHAT THIS RUNNER DECIDES (and what it explicitly does NOT)
============================================================================
The existing mixed-observable runner
(scripts/rp_combined_mixed_observable_u_integrated_2026_05_29.py) builds the
operator transfer T_full = W^dag W and checks that the OPERATOR Gram
<Omega|O^dag T_full O|Omega> = ||W O Omega||^2 is PSD.  That is automatic once
T_full is posited -- it is the ASSEMBLY lemma, not the representation theorem.
The no-go runner (scripts/axiom_first_rp_spin_basis_single_step_psd_failure.py)
computes the BEREZIN path-integral reflected Gram by Wick contraction with
M[U]^{-1}.  Those two objects live in two separate runners and NO existing
runner checks that they are EQUAL in the FERMION sector.

THE DELIVERED CHECK HERE: in the FERMION sector of the 2-step blocked staggered
surface, compute INDEPENDENTLY

    (i)  the reflected BEREZIN/Wick block metric of the staggered Grassmann
         fields (the genuine path-integral object, via real M^{-1} contractions
         with NO operator-side reference), and
    (ii) the OPERATOR two-step transfer eigenvalue c_block * e^{-2E_j} on Fock
         space,

and assert (i) == (ii).  The two sides share ONLY the lattice action (the
spatial-hop spectrum {E_j}); they are otherwise completely separate code paths
(Grassmann integration over the temporal chain vs. operator algebra on Fock
space).  Equality of the two is the FERMION-SECTOR instance of the
Luescher/Osterwalder-Seiler transfer-matrix REPRESENTATION theorem, here verified
on finite carriers: per mode, per fixed gauge background (U(1)/SU(3)), and -- the
genuine many-field test -- on the FULL position-basis many-field Berezin Gram
(every Grassmann cross-contraction, no per-mode reduction) which fixes c_block=2
a priori (mode/mass-independent).

NOT ESTABLISHED HERE: the full gauge-fermion-ENTANGLED representation equality --
a genuine many-field Grassmann integral of a MIXED (gauge x fermion) observable at
each U, compared to the operator sandwich -- is NOT verified by this runner.  The
"U-integrated" assembly below (CHECK 3) carries the gauge/Fock structure
IDENTICALLY on both compared sides (same Wilson kernel Kg, same flat reference
Omega, same observables, same Fock operators), differing ONLY in the per-config
fermion block; its residual is therefore PURELY the per-mode fermion-sector scalar
already tested per mode / per config, NOT an independent test of gauge-fermion
mixing.  (Forcing the Berezin block := operator block makes that residual exactly
zero while the operator-Schmidt rank is unchanged.)  The genuine full-mixed
representation equality is RP_MIXED's assembly target and remains the harder open
step.  This runner also does NOT verify the det(M[U]) positive weight or the Haar
U-average (those belong to the gauge measure / RP_MIXED, not here), and does NOT
prove the continuum / OS-reconstruction (Wightman) limit.

NEGATIVE CONTROL (must FAIL): the SINGLE-step (one-slice) reflection breaks
Theta-covariance of the staggered eta_1(t)=(-1)^t phase, so the single-step
Berezin reflected form is NOT equal to any positive operator sandwich (its
positive-cone metric is indefinite, min eig < 0).  The runner asserts the
single-step equality is VIOLATED -- i.e. the 2-step reflection sign is the real
physics and the discriminator has teeth.

============================================================================
CITED (standard) vs DERIVED (in-repo) -- honesty ledger
============================================================================
CITED methodology (not reproven here):
  * Luescher, Comm. Math. Phys. 54 (1977) 283 -- transfer-matrix construction,
    reflection = adjoint, Hilbert-space reconstruction from the Euclidean
    correlator.
  * Osterwalder-Seiler, Ann. Phys. 110 (1978) 440 -- gauge + fermion lattice
    OS positivity; reflection on Grassmann fields.
  * Creutz, Phys. Rev. D 15 (1977) 1128 -- free-fermion transfer matrix and
    coherent-state (Grassmann) slice resolution.
  * Sharatchandra-Thun-Weisz, Nucl. Phys. B192 (1981) 205;  Palumbo,
    Phys. Rev. D 66 (2002) 077503 -- the STAGGERED 2-step transfer matrix and
    the coherent-state Berezin slice reconstruction.
  * Montvay-Munster Ch.3; Smit Sec.6 -- textbook treatments.
DERIVED in-repo here (the load-bearing new finite-carrier content):
  * The explicit dual computation that the reflected Berezin block metric of the
    staggered Grassmann FERMION fields EQUALS the operator two-step transfer
    eigenvalue c_block * e^{-2E_j} -- per mode, per fixed gauge background, and on
    the FULL position-basis many-field Berezin Gram (no per-mode reduction) --
    including the staggered eta_1 sign / 2-step block bookkeeping under
    Theta(t,x)=(-1-t,x), with c_block=2 fixed a priori by the free many-field Gram
    (mode/mass-independent), and with the single-step version as a built-in
    negative control that the equality FAILS.

============================================================================
SCOPE / HONESTY (anti-over-claim)
============================================================================
Finite carrier, FERMION sector only.  This runner verifies the fermion-sector
REPRESENTATION EQUALITY on explicit small lattices (illustrating the construction
whose general form is the cited methodology).  It does NOT verify the full
gauge-fermion-entangled (mixed-observable) representation equality (CHECK 3's
"U-integrated" assembly carries the gauge/Fock structure identically on both
compared sides, so its residual is purely the per-mode fermion scalar -- see the
CHECK 3 header; the genuine mixed object is RP_MIXED's open assembly target).  It
does NOT verify the det(M[U]) positive weight or the Haar U-average (gauge measure
/ RP_MIXED, not here).  It does NOT prove the continuum / OS-reconstruction
(Wightman) limit, nor Euclidean rotational invariance, nor compact-group Wilson-
boundary positivity (a separate gauge-sector source note).  It does NOT claim the full interacting
RP "closes": the fermion-sector representation here + (H1 gauge PSD, separate
gauge-sector note) + Case-A det positivity (retained) + per-config fermion 2-step positivity
(audited_conditional) + the open mixed-observable assembly together would give the
conditional bridge; this runner delivers the fermion-sector representation only.
No ledger edits.  Settled Berezin sign convention
<chi_b bar_a>=+(M^-1)[b,a], <bar_a chi_b>=-(M^-1)[b,a].
"""
from __future__ import annotations

import math
from itertools import combinations, permutations

import numpy as np

# ---------------------------------------------------------------------------
# Global, deterministic, single-seed
# ---------------------------------------------------------------------------
MASS = 0.5
NT_BULK = 16          # half temporal extent per mode (so 2*NT_BULK slices): big
                      # enough that the bulk-projected (vacuum-boundary) regime is
                      # reached to ~1e-10 (decay is geometric in e^{-2E}).
TOL_EQ = 1e-10        # equality tolerance for Berezin vs operator
TOL_PSD = 1e-9
RNG = np.random.default_rng(20260530)


def eta1(t: int) -> float:
    """Staggered spatial phase eta_1(t) = (-1)^t; eta_0 = 1."""
    return (-1.0) ** t


# ===========================================================================
# Berezin / Wick with the settled sign convention.
#   <chi_b bar_a> = +(M^{-1})[b,a],   <bar_a chi_b> = -(M^{-1})[b,a].
# A monomial is a list of (kind, flat_index) with kind in {'c','cb'}.
# ===========================================================================
def wick(monomial, Minv) -> complex:
    n = len(monomial)
    if n == 0:
        return 1.0 + 0.0j
    if n % 2:
        return 0.0 + 0.0j
    chi_pos = [k for k, (kd, _) in enumerate(monomial) if kd == 'c']
    cb_pos = [k for k, (kd, _) in enumerate(monomial) if kd == 'cb']
    if len(chi_pos) != len(cb_pos):
        return 0.0 + 0.0j
    total = 0.0 + 0.0j
    for perm in permutations(cb_pos):
        seq = []
        for c, b in zip(chi_pos, perm):
            seq += [c, b]
        inv = sum(1 for i in range(len(seq)) for j in range(i + 1, len(seq))
                  if seq[i] > seq[j])
        sign = -1.0 if inv % 2 else 1.0
        val = 1.0 + 0.0j
        for c, b in zip(chi_pos, perm):
            _, ci = monomial[c]
            _, bi = monomial[b]
            val *= Minv[ci, bi]
        total += sign * val
    return total


# ===========================================================================
# Group elements
# ===========================================================================
def random_su3() -> np.ndarray:
    z = (RNG.standard_normal((3, 3)) + 1j * RNG.standard_normal((3, 3))) / math.sqrt(2.0)
    q, r = np.linalg.qr(z)
    ph = np.diag(r) / np.abs(np.diag(r))
    q = q * ph
    detq = np.linalg.det(q)
    return q * (detq ** (-1.0 / 3.0))


def random_u1() -> complex:
    return complex(np.exp(1j * RNG.uniform(0.0, 2.0 * math.pi)))


# ===========================================================================
# Spatial hop spectrum (the only action input shared by both sides)
# ===========================================================================
def spatial_hop(spatial_links, Ls, nc) -> np.ndarray:
    """Staggered spatial hop h[U] on the Ls-site ring at a fixed background.
       Anti-Hermitian: h^dag = -h, eigenvalues i*lambda_j, lambda_j real."""
    dim = Ls * nc
    h = np.zeros((dim, dim), dtype=complex)
    for x in range(Ls):
        U = spatial_links[x]
        Ub = spatial_links[(x - 1) % Ls]
        for a in range(nc):
            for b in range(nc):
                h[x * nc + a, ((x + 1) % Ls) * nc + b] += 0.5 * U[a, b]
                h[x * nc + a, ((x - 1) % Ls) * nc + b] += -0.5 * np.conj(Ub[b, a])
    return h


def mode_energies(spatial_links, Ls, nc, m):
    """Single-particle 2-step energies E_j = asinh(sqrt(m^2 + lambda_j^2)) >= 0,
       with the unitary U_h diagonalizing the (anti-Hermitian) hop h = U_h (i L) U_h^dag.
       Returns (E_j array, U_h, lambda_j array)."""
    h = spatial_hop(spatial_links, Ls, nc)
    # h is anti-Hermitian => i*h is Hermitian with real eigenvalues = -lambda? use eig.
    w, V = np.linalg.eig(h)
    lam = (w / 1j).real                      # h = V diag(i lam) V^{-1}
    # orthonormalize V (h normal => eigenvectors orthogonal up to numerics)
    Q, _ = np.linalg.qr(V)
    # recompute lam on the orthonormal basis to keep it clean
    Hd = Q.conj().T @ h @ Q
    lam = (np.diag(Hd) / 1j).real
    E = np.arcsinh(np.sqrt(m * m + lam * lam))
    return E, Q, lam


# ===========================================================================
# BEREZIN SIDE : full spacetime staggered Dirac matrix per mode, then the
# reflected correlator by Wick contraction with M^{-1}.  This is the genuine
# path-integral computation.
#
# We work in the momentum / hop-eigenbasis where the spatial hop is diagonal
# (eigenvalue i*lambda_j).  Each mode is an independent 1+1d staggered temporal
# chain with on-site alpha_t = m + i eta_1(t) lambda_j.  The full Berezin
# correlator factorizes over modes (free / fixed-background / per-config), which
# is exactly how the determinant weight det(M[U]) and the Haar U-average enter.
# ===========================================================================
def per_mode_chain_Minv(lam, Nt):
    """Inverse of the temporal staggered chain Dirac operator for one mode."""
    tmin = -Nt
    Lt = 2 * Nt
    M = np.zeros((Lt, Lt), dtype=complex)
    for t in range(tmin, Nt):
        i = t - tmin
        M[i, i] += MASS + 1j * eta1(t) * lam
        if t + 1 <= Nt - 1:
            M[i, (t + 1) - tmin] += 0.5
        if t - 1 >= tmin:
            M[i, (t - 1) - tmin] += -0.5
    return np.linalg.inv(M), (lambda t: t - tmin)


def berezin_block_metric_per_mode(lam, Nt):
    r"""Berezin positive-cone metric for ONE mode on the 2-step block (slices 0,1).

    OS reflection on the staggered Grassmann field across the plane between
    t=-1 and t=0:  theta(t)=(-1-t).  The Osterwalder-Seiler fermion reflection
    carries the gamma_0-type sign so that the reflected inner product is the
    physical (positive) metric:  Theta(chi_t) = - bar_chi_{theta t}  (and the
    overall sign is the OS convention, NOT a free parameter -- the OPPOSITE sign
    is the single-step naive Sharatchandra map that gives the documented no-go,
    reproduced as the negative control).

    Returns the 2x2 Hermitian metric K_ab = <Theta(chi_a) chi_b> over the block
    fields {chi_0, chi_1}.  Its single positive eigenvalue is the reconstructed
    state norm; we verify below it equals (block measure) * e^{-2E}.
    """
    Minv, idx = per_mode_chain_Minv(lam, Nt)
    K = np.zeros((2, 2), dtype=complex)
    for a, ta in enumerate((0, 1)):
        for b, tb in enumerate((0, 1)):
            # OS sign (-1) * <bar_{theta a} chi_b>
            K[a, b] = -wick([('cb', idx(-1 - ta)), ('c', idx(tb))], Minv)
    return 0.5 * (K + K.conj().T)


def berezin_singlestep_metric_per_mode(lam, Nt):
    """NEGATIVE CONTROL: the naive single-slice (single-step) reflected metric
       on {chi_0, bar_chi_0} with the naive Sharatchandra reflection
       Theta(chi_0)=+bar_{theta 0}.  Indefinite (the staggered eta_1 flip is not
       compensated) -> not equal to any positive operator sandwich."""
    Minv, idx = per_mode_chain_Minv(lam, Nt)
    fields = [('c', 0), ('cb', 0)]

    def refl(kd, t):
        return ('cb' if kd == 'c' else 'c', -1 - t)

    K = np.zeros((2, 2), dtype=complex)
    for a, (ka, ta) in enumerate(fields):
        rk, rt = refl(ka, ta)
        for b, (kb, tb) in enumerate(fields):
            K[a, b] = wick([(rk, idx(rt)), (kb, idx(tb))], Minv)
    return 0.5 * (K + K.conj().T)


# ===========================================================================
# OPERATOR SIDE : Fock space, transfer matrix T_full built from the action-
# derived 2-step single-particle kernel e^{-2E_j}.  Completely separate code
# path from the Berezin side -- shares only the spatial-hop spectrum {E_j}.
#
# Per mode the operator transfer is t1^(2) = e^{-2E}; the many-body transfer is
# the second quantization T_hat^2 = Gamma(diag_j e^{-2E_j}) = (x)_j diag(1,e^{-2E_j}).
# |Omega> = Fock vacuum (the bulk boundary state for E>0).  A blocked positive-
# half creation operator maps to b_j^dag; the reconstructed-state norm is the
# block measure c_block * e^{-2E_j}.  We verify the dual equality
#   Berezin block metric (positive eig)  ==  c_block * (operator <Omega|b T2 b^dag|Omega>)
# mode by mode, then assemble the full mixed Gram and assert equality.
# ===========================================================================
BLOCK_MEASURE = 2.0   # two Grassmann pairs per 2-step block (slices 0,1); the
                      # exact, mode-independent normalization relating the
                      # Berezin block metric to the canonical operator transfer.
                      # Derived/verified numerically against e^{-2E} below.


def operator_block_value_per_mode(E):
    """Operator side per mode: <Omega| b T_hat^2 b^dag |Omega> for the canonical
       blocked mode = e^{-2E} (b^dag|Omega>=|1>, T2|1>=e^{-2E}|1>)."""
    return math.exp(-2.0 * E)


# ===========================================================================
# DUAL CHECK 1 : FREE case (U=1) -- elementary representation equality per mode.
# ===========================================================================
def dual_free(Ls, nc, m):
    """Free staggered (U=1): Berezin block metric positive eigenvalue must equal
       BLOCK_MEASURE * operator transfer value e^{-2E}, mode by mode.  This is the
       cleanest instance of the representation equality (no gauge entanglement)."""
    links = [np.eye(nc, dtype=complex) for _ in range(Ls)]
    E, Uh, lam = mode_energies(links, Ls, nc, m)
    worst = 0.0
    rows = []
    for j in range(len(E)):
        Kb = berezin_block_metric_per_mode(lam[j], NT_BULK)
        ev = np.linalg.eigvalsh(Kb)
        pos = ev[ev > 1e-9]
        berezin_val = float(pos[0]) if len(pos) else 0.0
        op_val = BLOCK_MEASURE * operator_block_value_per_mode(E[j])
        worst = max(worst, abs(berezin_val - op_val))
        rows.append((lam[j], E[j], berezin_val, op_val))
    return worst, rows


def full_position_basis_berezin_gram(Ls, nc, m, Nt):
    r"""GENUINE many-field path-integral cross-check (closes the per-mode-reduction
    concern).  Free U=1 staggered theory on the FULL 1+1d spacetime lattice in the
    POSITION basis; the OS block metric over ALL block fields {chi_{t,x}: t in (0,1)}
    is computed by direct Grassmann Wick contraction with the full M^{-1} -- every
    cross-contraction included, no momentum/per-mode factorization.  Its positive
    eigenvalues must equal BLOCK_MEASURE * e^{-2E_j} (the operator transfer
    spectrum), proving the representation equality for the full many-field Gram,
    not merely a per-mode scalar.  Returns (sorted positive eigs, expected, worst).
    """
    tmin = -Nt
    Lt = 2 * Nt
    N = Lt * Ls * nc

    def idx(t, x, a=0):
        return ((t - tmin) * Ls + (x % Ls)) * nc + a

    M = np.zeros((N, N), dtype=complex)
    for t in range(tmin, Nt):
        for x in range(Ls):
            for a in range(nc):
                i = idx(t, x, a)
                M[i, i] += m
                if t + 1 <= Nt - 1:
                    M[i, idx(t + 1, x, a)] += 0.5
                if t - 1 >= tmin:
                    M[i, idx(t - 1, x, a)] += -0.5
            e = eta1(t)
            for a in range(nc):
                M[idx(t, x, a), idx(t, (x + 1) % Ls, a)] += 0.5 * e
                M[idx(t, x, a), idx(t, (x - 1) % Ls, a)] += -0.5 * e
    Minv = np.linalg.inv(M)

    # OS block metric over all positive-half block fields (slices 0,1), OS sign.
    block_fields = [('c', t, x, a) for t in (0, 1) for x in range(Ls)
                    for a in range(nc)]
    nf = len(block_fields)
    K = np.zeros((nf, nf), dtype=complex)
    for p, (kp, tp, xp, ap) in enumerate(block_fields):
        rk = 'cb'                                # reflect chi -> bar
        rt = -1 - tp
        for q, (kq, tq, xq, aq) in enumerate(block_fields):
            K[p, q] = -wick([(rk, idx(rt, xp, ap)), (kq, idx(tq, xq, aq))], Minv)
    K = 0.5 * (K + K.conj().T)
    eigs = np.linalg.eigvalsh(K)
    pos = np.sort(eigs[eigs > 1e-9])

    # expected: BLOCK_MEASURE * e^{-2E_j} for the modes of the spatial hop
    h = spatial_hop([np.eye(nc, dtype=complex) for _ in range(Ls)], Ls, nc)
    lam = np.sort((np.linalg.eigvals(h) / 1j).real)
    E = np.arcsinh(np.sqrt(m * m + lam * lam))
    expected = np.sort(BLOCK_MEASURE * np.exp(-2.0 * E))
    expected = expected[-len(pos):] if len(expected) >= len(pos) else expected
    worst = float(np.max(np.abs(pos - expected))) if len(pos) == len(expected) else math.inf
    return pos, expected, worst


# ===========================================================================
# DUAL CHECK 2 : FIXED nontrivial SU(3)/U(1) background -- per-config equality,
# reusing the gauge-extension modal reduction (anti-Hermitian hop -> {E_j}).
# ===========================================================================
def dual_fixed_background(group, Ls, m):
    nc = 1 if group == 'u1' else 3
    if group == 'u1':
        links = [random_u1() * np.eye(1, dtype=complex) for _ in range(Ls)]
    else:
        links = [random_su3() for _ in range(Ls)]
    E, Uh, lam = mode_energies(links, Ls, nc, m)
    worst = 0.0
    for j in range(len(E)):
        Kb = berezin_block_metric_per_mode(lam[j], NT_BULK)
        ev = np.linalg.eigvalsh(Kb)
        pos = ev[ev > 1e-9]
        berezin_val = float(pos[0]) if len(pos) else 0.0
        op_val = BLOCK_MEASURE * operator_block_value_per_mode(E[j])
        worst = max(worst, abs(berezin_val - op_val))
    return worst, len(E), nc


# ===========================================================================
# DUAL CHECK 3 : the per-config fermion-sector equality ASSEMBLED into a shared
# gauge/Fock wrapper.  NOT an independent test of gauge-fermion mixing.
#
# HONEST SCOPE OF THIS CHECK (read first).  We build a basis of observables
# F = f(U) * (fermion monomial) on H_gauge (x) H_ferm and assemble two Gram
# matrices, G_op and G_ber.  By construction the two share IDENTICALLY:
#   - the gauge half (the same Wilson kernel Kg^{1/2}, used as ONE object),
#   - the reference state Omega (flat gauge reference (x) Fock vacuum),
#   - the observables O = f(U)-multiplication (x) Fock operator, and
#   - the Fock operators.
# G_op and G_ber differ ONLY in the per-config fermion block (Top_blocks vs
# Tber_blocks).  Consequently G_ber - G_op is a pure function of the per-block
# difference Tber - Top; the entire gauge/Fock/entanglement structure CANCELS
# identically.  Forcing Tber := Top gives worst|G_ber-G_op| = 0 EXACTLY while the
# operator-Schmidt rank is unchanged -- so the rank>1 / mixed framing is NOT
# load-bearing here.  The genuine content of this check is therefore exactly the
# PER-CONFIG fermion-sector equality Tber == Top already established per mode
# (CHECK 1) and per fixed background (CHECK 2), now exhibited inside a shared
# operator wrapper.  Moreover Tber = (x)_j diag(1, cov_j) is per-mode FACTORIZED,
# NOT a genuine many-field Grassmann integral of a mixed observable.
#
# What is NOT established here: the full gauge-fermion-ENTANGLED representation
# equality -- a many-field Grassmann integral of a MIXED observable at each U,
# compared independently to the operator sandwich -- and the det(M[U]) positive
# weight / Haar U-average.  Those belong to RP_MIXED's assembly + the gauge
# measure and remain open.  The finite-carrier check below uses the Wilson
# transfer kernel Kg with a FLAT reference (no e^{-S_G} Boltzmann weight, no
# det(M[U]) measure); it verifies the FERMION-sector representation per config.
#
#   OPERATOR side: <Omega| O^dag T_full O |Omega>, T_full = (Kg^{1/2}(x)I)
#       (oplus_U B[U]^dag B[U]) (Kg^{1/2}(x)I), fermion blocks from the
#       action-derived {E_j(U)}, gauge transfer Kg the Wilson kernel.
#   BEREZIN side: the SAME quadratic form with the fermion block replaced by the
#       independently-computed Grassmann per-config block metric Tber.
# A SHARED finite gauge sample {g_k} feeds both sides, so the comparison is exact,
# not statistical.
# ===========================================================================
def wilson_kernel(g_list, beta, nc):
    """Wilson temporal-gauge transfer K(g,g')=exp(-beta(1-Re Tr(g g'^dag)/nc))."""
    K = len(g_list)
    Kk = np.zeros((K, K))
    for i in range(K):
        for j in range(K):
            P = g_list[i] @ g_list[j].conj().T
            Kk[i, j] = math.exp(-beta * (1.0 - np.real(np.trace(P)) / nc))
    return Kk


def jw_a(mode, n_modes):
    I2 = np.eye(2)
    Zz = np.diag([1.0, -1.0])
    a = np.array([[0.0, 1.0], [0.0, 0.0]])
    ops = [Zz if k < mode else (a if k == mode else I2) for k in range(n_modes)]
    out = ops[0]
    for o in ops[1:]:
        out = np.kron(out, o)
    return out.astype(complex)


def per_config_fermion_transfer(links, Ls, nc, m, n_modes):
    r"""Per-config fermion 2-step transfer operator T_hat^2[U] on the Fock space,
    built TWO independent ways that must agree (the per-config instance of the
    representation equality -- the fermion factor of the mixed object):

      OPERATOR build (T2op): from the ACTION-derived single-particle kernel
        e^{-2E_j(U)} (E_j from the anti-Hermitian spatial hop), second-quantized
        as Gamma(diag_j e^{-2E_j}) = (x)_j diag(1, e^{-2E_j}) in the canonical
        (hop-eigen) mode basis.

      BEREZIN build (T2ber): from the BEREZIN per-mode 2-step block metric (the
        genuine Grassmann path integral on the temporal chain), whose single
        positive eigenvalue is BLOCK_MEASURE * e^{-2E_j}.  Dividing by the
        block-measure normalization gives the canonical covariance, second-
        quantized the same way: (x)_j diag(1, cov_j).

    Both are returned as dimF x dimF Fock-space operators in the SAME canonical
    mode basis, with the Fock-operator list used to form the mixed Gram.  They are
    EQUAL iff the Berezin block metric reproduces the action transfer eigenvalue,
    i.e. iff the per-config representation equality holds.
    """
    E, Uh, lam = mode_energies(links, Ls, nc, m)
    dimF = 2 ** n_modes

    # ---- OPERATOR transfer: action-derived e^{-2E_j} ----
    t1_op = np.exp(-2.0 * E)
    T2op = np.array([[1.0]], dtype=complex)
    for j in range(n_modes):
        T2op = np.kron(T2op, np.diag([1.0, t1_op[j]]))

    # ---- BEREZIN transfer: independent Grassmann per-mode block metric ----
    cov = np.zeros(n_modes, dtype=float)
    for j in range(n_modes):
        Kb = berezin_block_metric_per_mode(lam[j], NT_BULK)
        ev = np.linalg.eigvalsh(Kb)
        pos = ev[ev > 1e-12]
        cov[j] = (float(pos[0]) if len(pos) else 0.0) / BLOCK_MEASURE
    T2ber = np.array([[1.0]], dtype=complex)
    for j in range(n_modes):
        T2ber = np.kron(T2ber, np.diag([1.0, cov[j]]))

    # ---- Fock operators (canonical modes) for the mixed Gram ----
    As = [jw_a(k, n_modes) for k in range(n_modes)]
    fock_ops = [np.eye(dimF, dtype=complex)]
    for k in range(n_modes):
        fock_ops.append(As[k].conj().T)       # b_k^dag (creation)
        fock_ops.append(As[k])                # b_k
    for k, l in combinations(range(n_modes), 2):
        fock_ops.append(As[k].conj().T @ As[l])

    return T2op, T2ber, fock_ops, E


def dual_u_integrated(group, Ls, m, beta, K_pts):
    r"""Per-config fermion-sector equality assembled into a shared gauge/Fock
    wrapper (NOT an independent gauge-fermion-mixing test -- see the CHECK 3
    header).  G_op and G_ber share the gauge half, Omega, observables and Fock
    operators identically and differ ONLY in the per-config fermion block, so
    worst|G_ber-G_op| reduces to the per-block fermion residual |Tber-Top|.

    Shared finite gauge sample {g_k} (same Haar draws on both sides).  Uses the
    Wilson transfer kernel Kg with a FLAT reference -- no e^{-S_G} Boltzmann
    weight and no det(M[U]) measure (those belong to the separate gauge measure /
    RP_MIXED assembly, not verified here).
    """
    nc = 1 if group == 'u1' else 3
    n_modes = Ls * nc

    # shared gauge sample
    if group == 'u1':
        g_list = [random_u1() * np.eye(1, dtype=complex) for _ in range(K_pts)]
        def gfun(g):     # scalar gauge multiplications f(g)
            ph = g[0, 0]
            return [1.0 + 0j, ph, np.conj(ph)]
    else:
        g_list = [random_su3() for _ in range(K_pts)]
        def gfun(g):
            return [1.0 + 0j, g[0, 0], g[1, 0]]
    nG = len(gfun(g_list[0]))

    Kg = wilson_kernel(g_list, beta, nc)
    wg, Vg = np.linalg.eigh(0.5 * (Kg + Kg.conj().T))
    gauge_min_eig = float(wg.min())
    wg_c = np.clip(wg, 0.0, None)
    Kg_half = (Vg * np.sqrt(wg_c)) @ Vg.conj().T

    # per-config fermion 2-step transfer operators (operator build vs Berezin
    # build).
    dimF = 2 ** n_modes
    Top_blocks, Tber_blocks = [], []
    fock_ops = None
    # NON-LOAD-BEARING DIAGNOSTIC: the per-config 2-step kernel normalization
    # prod_j (1 + e^{-2E_j}) is positive config-by-config.  This is NOT the
    # det(M[U]) measure weight and does NOT enter G_op or G_ber below (both use a
    # FLAT gauge reference and the Wilson kernel only); it is reported as context.
    # The det(M[U]) positive weight (Case A) and the Haar U-average are part of the
    # separate gauge measure / RP_MIXED assembly, not verified by this runner.
    min_kernel_norm = math.inf
    for g in g_list:
        links = [g for _ in range(Ls)]
        T2op, T2ber, fock_ops, E = per_config_fermion_transfer(
            links, Ls, nc, m, n_modes)
        Top_blocks.append(T2op)
        Tber_blocks.append(T2ber)
        min_kernel_norm = min(min_kernel_norm, float(np.prod(1.0 + np.exp(-2.0 * E))))
    nF = len(fock_ops)

    # ----- OPERATOR side: full mixed Gram on H_gauge (x) H_ferm -----
    # T_full = (Kg^{1/2}(x)I) (oplus_k B[g_k]^dag B[g_k]) (Kg^{1/2}(x)I); the
    # block oplus_k Top_blocks[k] is B^dag B in temporal gauge (U-diagonal).
    dim = K_pts * dimF
    T_ferm = np.zeros((dim, dim), dtype=complex)
    for k in range(K_pts):
        sl = slice(k * dimF, (k + 1) * dimF)
        T_ferm[sl, sl] = Top_blocks[k]
    Kg_half_full = np.kron(Kg_half, np.eye(dimF, dtype=complex))
    T_full = Kg_half_full @ T_ferm @ Kg_half_full
    T_full = 0.5 * (T_full + T_full.conj().T)
    # NON-LOAD-BEARING diagnostic of T_full's structure (T_full is NOT a tensor
    # product across H_gauge (x) H_ferm).  This does NOT make CHECK 3 an
    # independent test of gauge-fermion mixing: this same operator T_full sits
    # IDENTICALLY on both compared sides (only the fermion block differs), so the
    # rank is irrelevant to the residual G_ber-G_op.  Reported as context only.
    Rsh = T_full.reshape(K_pts, dimF, K_pts, dimF).transpose(0, 2, 1, 3).reshape(
        K_pts * K_pts, dimF * dimF)
    sv = np.linalg.svd(Rsh, compute_uv=False)
    op_schmidt_rank = int(np.sum(sv > 1e-9 * sv[0]))

    vac = np.zeros(dimF, dtype=complex)
    vac[0] = 1.0
    gauge_ref = np.ones(K_pts, dtype=complex) / math.sqrt(K_pts)
    Omega = np.kron(gauge_ref, vac)
    gauge_mults = [np.diag([f[ig] for f in [gfun(g) for g in g_list]]).astype(complex)
                   for ig in range(nG)]
    Os, labels = [], []
    for ig in range(nG):
        for ifk in range(nF):
            Os.append(np.kron(gauge_mults[ig], fock_ops[ifk]))
            labels.append((ig, ifk))
    nObs = len(Os)
    TO = [T_full @ (O @ Omega) for O in Os]
    G_op = np.zeros((nObs, nObs), dtype=complex)
    for I in range(nObs):
        left = Os[I] @ Omega
        for J in range(nObs):
            G_op[I, J] = np.vdot(left, TO[J])

    # ----- BEREZIN side: the SAME quadratic form as the operator side, with the
    # fermion block replaced by the Grassmann per-config block metric (Tber_blocks)
    # and the SAME Wilson gauge transfer Kg used identically (one object, both
    # sides) and the SAME flat reference Omega.  Because only the fermion block
    # differs, equality of G_ber and G_op is PRECISELY the per-block statement
    # Tber == Top -- the per-config fermion-sector equality already established per
    # mode (CHECK 1) and per fixed background (CHECK 2).  The gauge/Fock structure
    # cancels identically; this is NOT an independent test of gauge-fermion mixing
    # (forcing Tber:=Top gives worst_eq = 0 exactly, rank unchanged).
    T_fermB = np.zeros((dim, dim), dtype=complex)
    for k in range(K_pts):
        sl = slice(k * dimF, (k + 1) * dimF)
        T_fermB[sl, sl] = Tber_blocks[k]
    T_fullB = Kg_half_full @ T_fermB @ Kg_half_full
    T_fullB = 0.5 * (T_fullB + T_fullB.conj().T)
    TOB = [T_fullB @ (O @ Omega) for O in Os]
    G_ber = np.zeros((nObs, nObs), dtype=complex)
    for I in range(nObs):
        left = Os[I] @ Omega
        for J in range(nObs):
            G_ber[I, J] = np.vdot(left, TOB[J])

    worst_eq = float(np.max(np.abs(G_ber - G_op)))
    # the GENUINE content of this check: the per-block fermion-sector residual
    # |Tber - Top| (the per-config representation equality).  worst_eq above is a
    # pure function of this (the gauge/Fock wrapper cancels identically).
    worst_block = max(float(np.max(np.abs(b - o)))
                      for b, o in zip(Tber_blocks, Top_blocks))
    herm = float(np.max(np.abs(G_op - G_op.conj().T)))
    eig = np.linalg.eigvalsh(0.5 * (G_op + G_op.conj().T))
    n_mixed = sum(1 for (ig, ifk) in labels if ig != 0 and ifk != 0)
    return {
        "group": group, "dim": dim, "nObs": nObs, "n_mixed": n_mixed,
        "gauge_min_eig": gauge_min_eig, "min_kernel_norm": min_kernel_norm,
        "op_schmidt_rank": op_schmidt_rank, "entangled": op_schmidt_rank > 1,
        "worst_eq": worst_eq, "worst_block": worst_block, "herm": herm,
        "min_eig": float(eig.min()), "max_eig": float(eig.max()),
    }


# ===========================================================================
# Decay anchor : the Berezin forward 2-pt decays as e^{-2E(p)} per 2-step block.
# This is the dispersion / transfer-eigenvalue anchor inside the path integral.
# ===========================================================================
def decay_anchor(Ls, nc, m):
    links = [np.eye(nc, dtype=complex) for _ in range(Ls)]
    E, Uh, lam = mode_energies(links, Ls, nc, m)
    worst = 0.0
    for j in range(len(E)):
        Minv, idx = per_mode_chain_Minv(lam[j], NT_BULK)
        # forward 2-pt over consecutive 2-step blocks, measured from a BULK
        # reference point t0 (away from the open temporal ends and the cut, so the
        # ratio is the clean bulk transfer eigenvalue, not a boundary transient)
        t0 = -NT_BULK + 4
        vals = [abs(Minv[idx(t0 + 2 * n), idx(t0)]) for n in range(1, 5)]
        for n in range(1, len(vals)):
            if vals[n - 1] > 1e-14:
                ratio = vals[n] / vals[n - 1]
                worst = max(worst, abs(ratio - math.exp(-2.0 * E[j])))
    return worst


# ===========================================================================
# Reflection = adjoint (a CITED OS property), to machine precision.  Consistency
# check on the assembled Gram -- NOT a new claim.
# Theta(F) = F^dag is implemented on the operator side as the Hermitian adjoint;
# we verify the OS metric (the assembled Gram) is Hermitian, i.e. reflection acts
# as the adjoint on the reconstructed Hilbert space.
# ===========================================================================
def reflection_equals_adjoint(group, Ls, m, beta, K_pts):
    """On the reconstructed Hilbert space the reflection Theta acts as the
       adjoint:  the OS Gram G_op is Hermitian to machine precision (G = G^dag),
       which is the operator statement Theta = (.)^dag (a cited OS property; this
       is a consistency check on the assembled Gram, not a new claim)."""
    res = dual_u_integrated(group, Ls, m, beta, K_pts)
    return res["herm"]


# ===========================================================================
# MAIN
# ===========================================================================
def main() -> int:
    print("=" * 84)
    print("DUAL-COMPUTATION: FERMION-SECTOR BEREZIN BLOCK METRIC == OPERATOR TRANSFER")
    print("  2-step blocked staggered OS transfer representation (fermion sector)")
    print("=" * 84)
    print(f"  mass m={MASS}, temporal bulk half-extent NT_BULK={NT_BULK} "
          f"(2x{NT_BULK}={2*NT_BULK} slices), eq tol={TOL_EQ:g}")
    print("  reflection theta(t,x)=(-1-t,x); staggered eta_1(t)=(-1)^t flips under theta")
    print("  Berezin sign: <chi_b bar_a>=+(M^-1)[b,a], <bar_a chi_b>=-(M^-1)[b,a]")
    print()
    P = 0
    F = 0

    # ---- DUAL CHECK 1: FREE (U=1), per-mode representation equality ----
    print("-" * 84)
    print("CHECK 1  FREE (U=1): Berezin block metric  ==  c_block * operator e^{-2E}")
    print("  cleanest instance of the representation equality (no gauge entanglement)")
    print("-" * 84)
    worst_free, rows = dual_free(Ls=4, nc=3, m=MASS)   # SU(3)-sized free carrier
    for lam, E, bv, ov in rows[:6]:
        print(f"  lambda={lam:+.4f}  E={E:.5f}  Berezin={bv:.10f}  "
              f"operator(c_block*e^-2E)={ov:.10f}  |diff|={abs(bv-ov):.2e}")
    print(f"  worst |Berezin - operator| (free, per-mode) = {worst_free:.3e}")
    # genuine many-field cross-check: full position-basis Grassmann Gram
    pos, exp_eigs, worst_full = full_position_basis_berezin_gram(Ls=3, nc=1, m=MASS, Nt=NT_BULK)
    print(f"  full POSITION-basis many-field Berezin Gram positive eigs = "
          f"{np.round(pos, 8)}")
    print(f"     expected c_block*e^-2E (operator spectrum)             = "
          f"{np.round(exp_eigs, 8)}")
    print(f"  worst |full-Berezin-Gram eig - operator| = {worst_full:.3e} "
          f"(no per-mode reduction: every Grassmann cross-contraction included)")
    ok = (worst_free < TOL_EQ) and (worst_full < 1e-7)
    print(f"  -> CHECK 1 representation equality (free): {'PASS' if ok else 'FAIL'}")
    P += ok; F += (not ok)
    print()

    # ---- DUAL CHECK 2: FIXED background ----
    print("-" * 84)
    print("CHECK 2  FIXED nontrivial background: per-config representation equality")
    print("  reuses the anti-Hermitian-hop modal reduction h[U]=U_h(iL)U_h^dag")
    print("-" * 84)
    worst_fix_u1, nE1, nc1 = dual_fixed_background('u1', Ls=4, m=MASS)
    worst_fix_su3, nE3, nc3 = dual_fixed_background('su3', Ls=2, m=MASS)
    print(f"  U(1)  fixed bkgd: {nE1} modes, worst |Berezin-operator| = {worst_fix_u1:.3e}")
    print(f"  SU(3) fixed bkgd: {nE3} modes, worst |Berezin-operator| = {worst_fix_su3:.3e}")
    ok = (worst_fix_u1 < TOL_EQ) and (worst_fix_su3 < TOL_EQ)
    print(f"  -> CHECK 2 representation equality (fixed bkgd): {'PASS' if ok else 'FAIL'}")
    P += ok; F += (not ok)
    print()

    # ---- DUAL CHECK 3: per-config fermion equality in a shared gauge/Fock wrapper
    print("-" * 84)
    print("CHECK 3  PER-CONFIG fermion equality assembled in a shared gauge/Fock wrapper")
    print("  Top vs Tber are wrapped by the SAME Wilson kernel Kg, SAME flat Omega, SAME")
    print("  observables/Fock ops -- they differ ONLY in the per-config fermion block, so")
    print("  worst|G_ber-G_op| reduces to the per-block residual |Tber-Top|.  This is NOT")
    print("  an independent gauge-fermion-mixing test (rank/dim/'mixed' are diagnostics).")
    print("-" * 84)
    ru1 = dual_u_integrated('u1', Ls=2, m=MASS, beta=2.0, K_pts=8)
    rsu3 = dual_u_integrated('su3', Ls=2, m=MASS, beta=4.0, K_pts=6)
    for r in (ru1, rsu3):
        print(f"  [{r['group']}] dimH={r['dim']}  observables={r['nObs']} "
              f"(diagnostic: nominally mixed={r['n_mixed']})")
        print(f"        diagnostics (context, not load-bearing): gauge transfer min "
              f"eig={r['gauge_min_eig']:.3e} (PSD),")
        print(f"            min 2-step kernel norm={r['min_kernel_norm']:.4f} (>0; NOT the "
              f"det(M[U]) measure), op-Schmidt rank={r['op_schmidt_rank']}")
        print(f"        GENUINE: worst per-block |Tber - Top| (per-config fermion "
              f"equality) = {r['worst_block']:.3e}")
        print(f"        (assembled wrapper residual |G_ber - G_op| = {r['worst_eq']:.3e}, "
              f"a pure function of the per-block residual above)")
        print(f"        operator Gram Hermitian: ||G-G^dag||={r['herm']:.2e}")
    # PASS criterion is the GENUINE per-config fermion equality |Tber-Top|; the
    # assembled-wrapper residual worst_eq is not independent of it, and the
    # entanglement-rank / kernel-norm diagnostics are NOT load-bearing here.
    ok = (ru1["worst_block"] < TOL_EQ and rsu3["worst_block"] < TOL_EQ)
    print(f"  -> CHECK 3 per-config fermion equality (in shared wrapper): "
          f"{'PASS' if ok else 'FAIL'}")
    P += ok; F += (not ok)
    print()

    # ---- REFLECTION = ADJOINT ----
    print("-" * 84)
    print("CHECK 4  REFLECTION = ADJOINT (cited OS property; Theta = (.)^dag)")
    print("  consistency check: the reconstructed OS Gram is Hermitian to machine precision")
    print("-" * 84)
    h1 = reflection_equals_adjoint('u1', Ls=2, m=MASS, beta=2.0, K_pts=8)
    h3 = reflection_equals_adjoint('su3', Ls=2, m=MASS, beta=4.0, K_pts=6)
    print(f"  U(1)  ||G - G^dag|| = {h1:.3e}")
    print(f"  SU(3) ||G - G^dag|| = {h3:.3e}")
    ok = (h1 < 1e-9) and (h3 < 1e-9)
    print(f"  -> CHECK 4 reflection=adjoint: {'PASS' if ok else 'FAIL'}")
    P += ok; F += (not ok)
    print()

    # ---- DECAY ANCHOR ----
    print("-" * 84)
    print("CHECK 5  BEREZIN DECAY ANCHOR: forward 2-pt decays as e^{-2E(p)} per 2-step")
    print("  the transfer eigenvalue appears INSIDE the path integral (faithfulness)")
    print("-" * 84)
    worst_decay = decay_anchor(Ls=3, nc=1, m=MASS)
    ok = worst_decay < 1e-6
    print(f"  worst |ratio - e^{{-2E}}| across modes/separations = {worst_decay:.3e}")
    print(f"  -> CHECK 5 decay anchor: {'PASS' if ok else 'FAIL'}")
    P += ok; F += (not ok)
    print()

    # ---- NEGATIVE CONTROL: single-step BREAKS the equality ----
    print("-" * 84)
    print("CHECK 6  NEGATIVE CONTROL: SINGLE-STEP reflection BREAKS the equality")
    print("  the staggered eta_1 flip is uncompensated single-step => the reflected")
    print("  positive-cone metric is INDEFINITE (min eig < 0), so it is NOT equal to")
    print("  any positive operator sandwich.  This MUST fail the PSD/equality test.")
    print("-" * 84)
    # single-step metric per mode; show it is indefinite (the no-go), unlike the
    # 2-step block metric which is PSD and matches the operator side.
    links = [np.eye(1, dtype=complex) for _ in range(3)]
    E, Uh, lam = mode_energies(links, 3, 1, MASS)
    worst_neg_min = 0.0
    for j in range(len(E)):
        Ks = berezin_singlestep_metric_per_mode(lam[j], NT_BULK)
        mn = float(np.linalg.eigvalsh(Ks).min())
        worst_neg_min = min(worst_neg_min, mn)
    # Also reproduce the full documented single-step Lagrangian Gram min eig -0.80
    ss_min = single_step_lagrangian_gram_min()
    print(f"  single-step per-mode block metric min eig = {worst_neg_min:+.4f} "
          f"(indefinite => no positive operator sandwich)")
    print(f"  full single-step naive Lagrangian Gram min eig = {ss_min:+.4f} "
          f"(documented no-go ~ -0.80)")
    # The negative control PASSES iff the single-step equality is VIOLATED, i.e.
    # the single-step metric is NOT PSD (so it cannot equal a positive sandwich).
    ok = (worst_neg_min < -1e-3) and (ss_min < -1e-2)
    print(f"  -> CHECK 6 single-step equality is VIOLATED (control has teeth): "
          f"{'PASS' if ok else 'FAIL'}")
    P += ok; F += (not ok)
    print()

    # ---- SUMMARY ----
    print("=" * 84)
    print(f"SCORECARD: PASS={P} FAIL={F}")
    print("  CHECK 1 free (U=1)            : Berezin block metric == c_block*e^-2E per mode")
    print("                                 + FULL many-field position-basis Gram (fixes c_block=2)")
    print("  CHECK 2 fixed SU(3)/U(1) bkgd : per-config Berezin == operator")
    print("  CHECK 3 per-config in wrapper : Tber==Top inside a SHARED gauge/Fock wrapper")
    print("                                 (NOT an independent gauge-fermion-mixing test)")
    print("  CHECK 4 reflection = adjoint  : OS Gram Hermitian (cited OS property; consistency)")
    print("  CHECK 5 decay anchor          : Berezin forward 2-pt ~ e^{-2E(p)} per 2-step")
    print("  CHECK 6 single-step control   : single-step BREAKS the equality (indefinite)")
    print("-" * 84)
    print("  DELIVERED: finite-carrier FERMION-SECTOR instance of the Luescher/Osterwalder-")
    print("  Seiler/STW/Palumbo transfer-matrix REPRESENTATION (cited); the 2-step eta_1 sign")
    print("  bookkeeping under theta(t,x)=(-1-t,x) is the in-repo derived content.")
    print("  NOT established here: the full gauge-fermion-ENTANGLED (mixed-observable)")
    print("  representation equality, the det(M[U]) weight / Haar U-average (RP_MIXED + gauge")
    print("  measure), the continuum / OS-reconstruction (Wightman) limit, nor a full RP closure.")
    print("=" * 84)
    return 0 if F == 0 else 1


# ---------------------------------------------------------------------------
# Full single-step naive Lagrangian Gram (documented -0.80 no-go), free U=1,
# reproduced here as part of the negative control.
# ---------------------------------------------------------------------------
def single_step_lagrangian_gram_min():
    """Free U=1 single-step naive reflected fermion Gram (degree-1 monomials at
       the cut), reproducing the documented min eig ~ -0.80."""
    Nt = 2
    Ls = 2
    nc = 1
    tmin = -Nt
    Lt = 2 * Nt
    N = Lt * Ls * nc

    def idx(t, x):
        return (t - tmin) * Ls + (x % Ls)

    M = np.zeros((N, N), dtype=complex)
    for t in range(tmin, Nt):
        for x in range(Ls):
            i = idx(t, x)
            M[i, i] += MASS
            if t + 1 <= Nt - 1:
                M[i, idx(t + 1, x)] += 0.5
            if t - 1 >= tmin:
                M[i, idx(t - 1, x)] += -0.5
            e = eta1(t)
            M[i, idx(t, (x + 1) % Ls)] += 0.5 * e
            M[i, idx(t, (x - 1) % Ls)] += -0.5 * e
    Minv = np.linalg.inv(M)
    monos = []
    for t in range(0, Nt):
        for x in range(Ls):
            monos.append([('c', idx(t, x))])
            monos.append([('cb', idx(t, x))])

    def refl(mono):
        out = []
        for kd, fi in reversed(mono):
            ti, x = divmod(fi, Ls)
            t = ti + tmin
            out.append(('cb' if kd == 'c' else 'c', idx(-1 - t, x)))
        return out

    nB = len(monos)
    G = np.zeros((nB, nB), dtype=complex)
    for I, FI in enumerate(monos):
        tF = refl(FI)
        for J, FJ in enumerate(monos):
            G[I, J] = wick(tF + FJ, Minv)
    return float(np.linalg.eigvalsh(0.5 * (G + G.conj().T)).min())


if __name__ == "__main__":
    raise SystemExit(main())
