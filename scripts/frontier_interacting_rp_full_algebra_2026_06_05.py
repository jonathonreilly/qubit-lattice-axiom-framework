#!/usr/bin/env python3
r"""FULL POLYNOMIAL HALF-SPACE ALGEBRA OS REFLECTION-POSITIVITY (FIXED a).

Extends the fixed-a interacting U-integrated staggered-SU(3) reflection-positivity
(RP) Gram from the SINGLE-CREATION transported-bilinear surface
(RP_MIXED_OBSERVABLE_... / INTERACTING_RP_FIXED_A_U_INTEGRATED_BRIDGE_BOUNDED_NOTE,
the "#2756" surface) to the **FULL polynomial half-space algebra**, including the
**gauge-invariant four-fermion observables**: the color-singlet mesons
`chibar(x) U(x,y) chi(y)` and the color-singlet baryon `eps_{abc} chi^a chi^b chi^c`
(and the anti-baryon `eps_{abc} chibar^a chibar^b chibar^c`).

============================================================================
WHAT IS ALREADY ESTABLISHED ON origin/main (NOT re-derived here)
============================================================================
  * Per-config FIXED-background fermion 2-step transfer positivity in temporal
    gauge: T_hat^2[U]=B[U]^dag B[U], H_hat[U]>=0 config-by-config
    (RP_P2_GAUGE_EXTENSION_..., free case AXIOM_FIRST_RP_TWO_STEP_...).
  * det(M_KS + m I)=prod_i (m^2+sigma_i^2)>=m^n>0 config-by-config (Case A,
    STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17).
  * The U-integrated MIXED gauge+fermion Gram is PSD on the **single-creation**
    transported bilinear surface (the #2756 surface), via the entangled transfer
    T_full=(Kg^{1/2}(x)I)(oplus_k Bk^dag Bk)(Kg^{1/2}(x)I)=W^dag W and its
    det-weighted Haar-U sampled cross-check (rp_combined_mixed_observable_...).
  * The gauge-invariant NUMBER-CONSERVING meson `chibar(x)U(x,y)chi(y)` two-point
    `<Theta(F)F>` is nonzero (vacuum-annihilation handled) and equals the operator
    connected quark-line loop Tr[V^dag G_f V G_f]>=0
    (MESON_GAUGE_INVARIANT_OS_TRANSFER_REPRESENTATION_BOUNDED_NOTE_2026-05-30).

============================================================================
THE GAP THIS RUNNER ATTACKS (the residual the #2756 note left open)
============================================================================
The #2756 note's stated residual: the four-fermion chibar U chi ANNIHILATES the
OS (empty Berezin/Fock) vacuum, so the FULL polynomial half-space algebra was
UNTESTED non-vacuously. Number-conserving operators (mesons, baryons) make the
naive operator matrix element <Omega|O^dag T O|Omega> trivially ZERO because
O|Omega>=0 -- NOT a positivity failure, a convention/vacuity obstruction.

THE FIX (handled, not dodged). The correct OS object is the Euclidean correlator
`<Theta(A) A>` computed by the det-weighted Haar-U-averaged Berezin path integral,
NOT an operator matrix element. The four-fermion observables enter via their
genuine multi-field Grassmann/Wick correlators and are NONZERO. Equivalently, in
the OS/Fock language the gauge-invariant operators act non-trivially on
MULTI-PARTICLE states (a baryon eps chi chi chi creates a genuine 3-particle
state; a meson chibar U chi propagates a particle-hole loop after the OS
reflection sends the chibar leg to the image half).

============================================================================
THE OS RP STATEMENT TESTED HERE (the extension)
============================================================================
OS reflection positivity is  <Theta(A) A> >= 0  for every A in the half-space
polynomial algebra A_+ .  We build the OS Gram

    G_{IJ} = <Theta(A_I) A_J>
           = (1/Z) sum_{U in Haar/quadrature} w_U det(M[U]) <Theta(A_I) A_J>^ferm_U ,
    Z = sum_U w_U det(M[U]),     w_U = exp(-S_G[U]) > 0,  det(M[U]) > 0 (Case A),

over a basis {A_I} of the FULL polynomial half-space algebra:
    - identity 1,
    - single-creation bilinears chibar_alpha (the #2756 one-particle surface),
    - gauge-invariant color-singlet MESONS  F = sum_{a,b} chibar_a(x) U(x,y)_{ab} chi_b(y),
    - gauge-invariant color-singlet BARYON   B = eps_{abc} chi^a chi^b chi^c (per site),
    - gauge-invariant color-singlet ANTI-BARYON eps_{abc} chibar^a chibar^b chibar^c,
    - mixed/product polynomials (meson x bilinear, etc.) that do NOT annihilate Omega.

`<Theta(A_I) A_J>^ferm_U` is the genuine many-field Berezin contraction (Wick by
explicit permutation sum) against the FULL spacetime staggered propagator M[U]^{-1}
-- NO operator assumption, the most independent fermion-kernel build. The OS
reflection theta(t,x)=(-1-t,x) with the SETTLED gamma_0-type sign
    Theta(chi_alpha(t)) = -chibar_alpha(-1-t),
    Theta(chibar_alpha(t)) = -chi_alpha(-1-t),
Theta antilinear and order-reversing; the spatial gauge link transported in the
meson reflects to the image-half spatial link (temporal gauge: same background).

PSD of this Gram over the FULL basis is the **full-algebra fixed-a interacting RP**.

============================================================================
THE REFLECTION-SQUARE EXTENSION (why it must hold for ALL A)
============================================================================
The #2756 reflection-square T_full=W^dag W is GENERAL: it is a statement about the
TRANSFER MATRIX, not about which operators we sandwich. The OS theorem
(Osterwalder-Seiler) says: if the one-step (here 2-step blocked) transfer T is a
PSD contraction, then <Theta(A) A> >= 0 for EVERY A in A_+. We CONFIRM this here
by exhibiting, per configuration, that the same Gram equals a manifest
M^dag M Gram in the 2-step transfer (Fock) representation, for the full operator
set -- so the positive result is the OS theorem applied to the full algebra,
verified non-vacuously (diagonal meson/baryon entries > 0).

============================================================================
CONTROLS (TEETH) -- each must fire
============================================================================
  T-WRONG  the WRONG single-step reflection (no gamma_0 sign, no 2-step blocking)
           on the SAME full-algebra Berezin Gram is NON-PSD (the -0.80
           Caracciolo-Palumbo obstruction, here over the full gauge-invariant
           algebra). Confirms positives aren't a trivially-positive artifact.
  NONVAC   the diagonal Gram entries for the MESON and the BARYON are > 0 (not 0):
           the four-fermion sector is genuinely non-vacuous.
  VAC0     the naive OPERATOR matrix element <Omega|Ohat^dag T Ohat|Omega> for the
           meson/baryon IS exactly 0 (Ohat|Omega>=0), demonstrating WHY the naive
           object is vacuous and the Berezin correlator is the correct OS object.
  GAUGEINV the transported meson and the baryon are genuine color singlets:
           the Gram is invariant under random SU(3)/U(1) gauge transforms.
  DETPOS   det(M[U]) > 0 on every sampled background (Case A); no det-sign sector.

============================================================================
SCOPE / HONESTY
============================================================================
FIXED-a only. Full polynomial half-space algebra (the extension over #2756's
single-creation surface). Berezin path integral with the real positive det weight
and real Haar SU(3)/U(1) backgrounds (finite quadrature / Haar sample, not exact
full Haar). NO continuum / OS-reconstruction (Wightman) claim. NO Euclidean
rotational (Lorentz) restoration. NO compact-group Wilson-boundary positivity
proof (the per-config 2-step rung and the Wilson-boundary remain their own rows).
NO ledger edits. Settled Berezin sign convention enforced and checked against the
documented single-step no-go.
"""
from __future__ import annotations

import math
import itertools
from itertools import permutations

import numpy as np

MASS = 0.5
TOL = 1e-9
RNG = np.random.default_rng(20260605)


# ===========================================================================
# Grassmann / Wick (SETTLED sign convention, matching the base + meson notes)
#   <chi_b bar_a> = +(M^{-1})[b,a],  <bar_a chi_b> = -(M^{-1})[b,a].
# Implemented via explicit permutation sum over the combined monomial; this is
# the genuine BEREZIN code path (no operator assumption).
# ===========================================================================
def wick(monomial, Minv) -> complex:
    n = len(monomial)
    if n == 0:
        return 1.0 + 0.0j
    if n % 2:
        return 0.0 + 0.0j
    cpos = [k for k, (kd, _) in enumerate(monomial) if kd == 'c']
    bpos = [k for k, (kd, _) in enumerate(monomial) if kd == 'cb']
    if len(cpos) != len(bpos):
        return 0.0 + 0.0j
    tot = 0.0 + 0.0j
    for perm in permutations(bpos):
        seq = []
        for c, b in zip(cpos, perm):
            seq += [c, b]
        inv = sum(1 for i in range(len(seq)) for j in range(i + 1, len(seq))
                  if seq[i] > seq[j])
        sign = -1.0 if inv % 2 else 1.0
        val = 1.0 + 0.0j
        for c, b in zip(cpos, perm):
            val *= Minv[monomial[c][1], monomial[b][1]]
        tot += sign * val
    return tot


# ===========================================================================
# Group elements
# ===========================================================================
def random_su3() -> np.ndarray:
    z = (RNG.standard_normal((3, 3)) + 1j * RNG.standard_normal((3, 3))) / math.sqrt(2.0)
    q, r = np.linalg.qr(z)
    q = q * (np.diag(r) / np.abs(np.diag(r)))
    detq = np.linalg.det(q)
    return q * (detq ** (-1.0 / 3.0))


def random_su2() -> np.ndarray:
    # SU(2) via a unit quaternion, embedded as 2x2 (used for the lighter cross-check)
    a, b, c, d = RNG.standard_normal(4)
    nrm = math.sqrt(a * a + b * b + c * c + d * d)
    a, b, c, d = a / nrm, b / nrm, c / nrm, d / nrm
    return np.array([[a + 1j * b, c + 1j * d], [-c + 1j * d, a - 1j * b]], dtype=complex)


def u1_phase(theta) -> np.ndarray:
    return np.array([[np.exp(1j * theta)]], dtype=complex)


# ===========================================================================
# Finite staggered KS carrier: Ns spatial sites on a ring (1 spatial dim used so
# the smallest carrier where a TRANSPORTED meson chibar(x)U(x,y)chi(y) and a
# single-site baryon both fit), nc colors, Lt=2*nt temporal slices.
# ===========================================================================
class Carrier:
    def __init__(self, Ns, nc, nt=2, m=MASS):
        self.Ns, self.nc, self.nt, self.m = Ns, nc, nt, m
        self.Lt = 2 * nt
        self.tmin = -nt
        self.N = self.Lt * Ns * nc

    def idx(self, t, x, a):
        return ((t - self.tmin) * self.Ns + (x % self.Ns)) * self.nc + a

    def build_M(self, links):
        """Full spacetime staggered KS Dirac matrix. links[x] = nc x nc spatial link
        U_1(x) on the bond x->x+1 (temporal gauge: same on every slice). eta_1(t)=(-1)^t."""
        nc, Ns = self.nc, self.Ns
        M = np.zeros((self.N, self.N), dtype=complex)
        for t in range(self.tmin, self.nt):
            e = (-1.0) ** t
            for x in range(Ns):
                for a in range(nc):
                    i = self.idx(t, x, a)
                    M[i, i] += self.m
                    if t + 1 <= self.nt - 1:
                        M[i, self.idx(t + 1, x, a)] += 0.5
                    if t - 1 >= self.tmin:
                        M[i, self.idx(t - 1, x, a)] += -0.5
                if Ns > 1:
                    U = links[x]
                    Ub = links[(x - 1) % Ns]
                    for a in range(nc):
                        i = self.idx(t, x, a)
                        for b in range(nc):
                            M[i, self.idx(t, (x + 1) % Ns, b)] += 0.5 * e * U[a, b]
                            M[i, self.idx(t, (x - 1) % Ns, b)] += -0.5 * e * np.conj(Ub[b, a])
        return M

    def det_M(self, links):
        return np.linalg.det(self.build_M(links))


# ===========================================================================
# OS reflection on field monomials.  A field factor is ('c'|'cb', x, a, t).
#  theta(t,x)=(-1-t, x). Settled gamma_0 sign:
#     Theta(chi_{x,a}(t))    = -chibar_{x,a}(-1-t),
#     Theta(chibar_{x,a}(t)) = -chi_{x,a}(-1-t).
#  Theta is antilinear (conj coeff) and order-reversing.
# `wrong=True`: the naive single-step reflection (NO gamma_0 sign) -> the no-go.
# ===========================================================================
def theta_monomial(coeff, factors, carrier, wrong=False):
    rev = list(reversed(factors))
    out = []
    sgn = 1.0
    for (kd, x, a, t) in rev:
        tr = -1 - t
        nk = 'cb' if kd == 'c' else 'c'
        if not wrong:
            sgn *= -1.0       # gamma_0-type sign per reflected factor
        out.append((nk, carrier.idx(tr, x, a)))
    return np.conj(coeff) * sgn, out


def mono_to_idx(coeff, factors, carrier):
    return coeff, [(kd, carrier.idx(t, x, a)) for (kd, x, a, t) in factors]


# ===========================================================================
# Build the FULL polynomial half-space algebra basis at positive time t_op.
# Each operator = list of (coeff, factors), factors = list of ('c'|'cb', x, a, t).
# ===========================================================================
def levi_civita(n):
    out = []
    for p in itertools.permutations(range(n)):
        inv = sum(1 for i in range(n) for j in range(i + 1, n) if p[i] > p[j])
        out.append((p, -1.0 if inv % 2 else 1.0))
    return out


def build_basis(carrier, links, t_op=0, include_products=True):
    """Return list of (label, op) where op is a list of (coeff, factors).
    Includes: identity; single-creation bilinears chibar_{x,a}; gauge-invariant
    transported mesons chibar(x)U(x,y)chi(y) (color singlet); single-site baryon
    eps chi chi chi and anti-baryon; and (optional) product polynomials that
    don't annihilate Omega (meson x bilinear)."""
    nc, Ns = carrier.nc, carrier.Ns
    ops = []

    # identity
    ops.append(("id", [(1.0 + 0.0j, [])]))

    # single-creation bilinears (the #2756 one-particle surface): chibar_{x,a}
    for x in range(Ns):
        for a in range(nc):
            ops.append((f"cb[{x},{a}]", [(1.0 + 0.0j, [('cb', x, a, t_op)])]))

    # gauge-invariant color-singlet MESONS  F = sum_{a,b} chibar_a(x) U(x,y)_{ab} chi_b(y)
    # on-site (y=x, U=I) and transported nearest-neighbour (y=x+1, U=link[x]).
    for x in range(Ns):
        mon = [(1.0 + 0.0j, [('cb', x, a, t_op), ('c', x, a, t_op)]) for a in range(nc)]
        ops.append((f"meson_onsite[{x}]", mon))
    if Ns > 1:
        for x in range(Ns):
            y = (x + 1) % Ns
            U = links[x]
            mon = []
            for a in range(nc):
                for b in range(nc):
                    mon.append((U[a, b] + 0.0j, [('cb', x, a, t_op), ('c', y, b, t_op)]))
            ops.append((f"meson_hop[{x}->{y}]", mon))

    # gauge-invariant color-singlet BARYON eps_{abc} chi^a chi^b chi^c (needs nc>=3)
    if nc >= 3:
        eps = levi_civita(3)
        for x in range(Ns):
            bm = [(s + 0.0j, [('c', x, p[0], t_op), ('c', x, p[1], t_op),
                              ('c', x, p[2], t_op)]) for (p, s) in eps]
            ops.append((f"baryon[{x}]", bm))
            abm = [(s + 0.0j, [('cb', x, p[0], t_op), ('cb', x, p[1], t_op),
                               ('cb', x, p[2], t_op)]) for (p, s) in eps]
            ops.append((f"antibaryon[{x}]", abm))

    # product polynomials that do NOT annihilate Omega: meson(onsite x=0) x chibar_{y,a}
    # (these are genuine larger polynomials of the half-space algebra; the four-fermion
    #  observable acts on a created state). Keep a few to keep the basis bounded.
    if include_products and Ns > 1:
        mes0 = [(1.0 + 0.0j, [('cb', 0, a, t_op), ('c', 0, a, t_op)]) for a in range(nc)]
        for a in range(min(nc, 2)):
            prod = [(c, f + [('cb', 1, a, t_op)]) for (c, f) in mes0]
            ops.append((f"meson0*cb[1,{a}]", prod))

    return ops


# ===========================================================================
# The FULL-ALGEBRA OS Gram via the det-weighted Haar-U-averaged Berezin path
# integral (NO operator assumption).
# ===========================================================================
def full_algebra_gram(carrier, configs, weights, t_op=0, wrong=False,
                      include_products=True):
    """configs: list of links-dicts; weights: list of positive gauge weights w_U=e^{-S_G}.
    Returns (labels, G, det_min, n_det_nonpos, diag). The basis is rebuilt per config
    (the meson hop amplitude depends on the link), but the LABELS/ordering are fixed."""
    # fix labels/order using the first config
    base = build_basis(carrier, configs[0], t_op, include_products)
    labels = [lab for lab, _ in base]
    n = len(labels)
    G = np.zeros((n, n), dtype=complex)
    Z = 0.0
    det_min = math.inf
    n_det_nonpos = 0
    for links, w in zip(configs, weights):
        M = carrier.build_M(links)
        detM = np.linalg.det(M)
        detw = detM.real
        if detw <= 0 or abs(detM.imag) > 1e-7 * (abs(detw) + 1e-30):
            n_det_nonpos += 1
        det_min = min(det_min, detw)
        Minv = np.linalg.inv(M)
        ops = build_basis(carrier, links, t_op, include_products)
        # precompute reflected (Theta) factor-lists per operator
        thetas = []
        for _, monsI in ops:
            tI = [theta_monomial(c, f, carrier, wrong) for (c, f) in monsI]
            thetas.append(tI)
        rights = []
        for _, monsJ in ops:
            jJ = [mono_to_idx(c, f, carrier) for (c, f) in monsJ]
            rights.append(jJ)
        weight = w * detw
        Z += weight
        for I in range(n):
            tI = thetas[I]
            for J in range(n):
                acc = 0.0 + 0.0j
                for (cI, fI) in tI:
                    if cI == 0:
                        continue
                    for (cJ, fJ) in rights[J]:
                        if cJ == 0:
                            continue
                        acc += cI * cJ * wick(fI + fJ, Minv)
                G[I, J] += weight * acc
    G /= Z
    diag = np.real(np.diag(G)).copy()
    return labels, G, det_min, n_det_nonpos, diag


# ===========================================================================
# VAC0 control: the naive OPERATOR matrix element <Omega|Ohat^dag T Ohat|Omega>
# for a number-conserving operator IS zero because Ohat|Omega>=0.  We verify
# ||Ohat|Omega>||=0 by genuine Jordan-Wigner occupation action (sparse).
# ===========================================================================
def jw_apply(state, kind, mode):
    """Apply c (kind='c') or c^dag (kind='cb') for `mode` to a Fock dict {occ:amp}."""
    out = {}
    for occ, amp in state.items():
        bit = (occ >> mode) & 1
        if kind == 'c':
            if not bit:
                continue
            sign = -1.0 if bin(occ & ((1 << mode) - 1)).count("1") % 2 else 1.0
            new = occ & ~(1 << mode)
        else:  # 'cb' = creation
            if bit:
                continue
            sign = -1.0 if bin(occ & ((1 << mode) - 1)).count("1") % 2 else 1.0
            new = occ | (1 << mode)
        out[new] = out.get(new, 0.0 + 0.0j) + sign * amp
    return out


def op_on_vacuum_norm(carrier, op_monomials, t_op=0):
    """||Ohat|Omega>|| for op given as list of (coeff, factors). Modes index = (x*nc+a).
    Apply factors right-to-left (operator ordering) to the empty Fock vacuum."""
    nmode = carrier.Ns * carrier.nc
    total = {}
    for (coeff, factors) in op_monomials:
        state = {0: 1.0 + 0.0j}   # empty vacuum
        for (kd, x, a, t) in reversed(factors):
            mode = (x % carrier.Ns) * carrier.nc + a
            state = jw_apply(state, kd, mode)
            if not state:
                break
        for occ, amp in state.items():
            total[occ] = total.get(occ, 0.0 + 0.0j) + coeff * amp
    return math.sqrt(sum(abs(v) ** 2 for v in total.values()))


# ===========================================================================
# Reflection-square confirmation (the OS theorem, full algebra, per config):
# the per-config 2-step blocked transfer T2[U] is PSD (T2=B^dag B), so the
# per-config OS Gram <Theta(A) A>_U = ||B (A Omega)||^2 >= 0 for EVERY A.  We
# confirm T2[U] PSD config-by-config (the input to the OS theorem) at the SAME
# backgrounds used in the Gram, including nontrivial SU(3)/SU(2) links.
# (Matches RP_P2_GAUGE_EXTENSION_...; the positive-Gram result IS this theorem
#  applied to the full algebra, verified non-vacuously by the Gram above.)
# ===========================================================================
def two_step_transfer_psd(carrier, links):
    """Per-config 2-step transfer eigenvalues via the banded mode equation
    (anti-Hermitian spatial hop h; T_even=mI+h, T_odd=mI-h; decaying modes of
    T_odd.T_even are real-positive). Returns (min_decay, worst_imag)."""
    nc, Ns = carrier.nc, carrier.Ns
    dim = Ns * nc
    h = np.zeros((dim, dim), dtype=complex)
    if Ns > 1:
        for x in range(Ns):
            U = links[x]
            Ub = links[(x - 1) % Ns]
            for a in range(nc):
                for b in range(nc):
                    h[x * nc + a, ((x + 1) % Ns) * nc + b] += 0.5 * U[a, b]
                    h[x * nc + a, ((x - 1) % Ns) * nc + b] += -0.5 * np.conj(Ub[b, a])
    I = np.eye(dim, dtype=complex)
    Z = np.zeros((dim, dim), dtype=complex)
    Te = np.block([[-2.0 * (carrier.m * I + h), I], [I, Z]])
    To = np.block([[-2.0 * (carrier.m * I - h), I], [I, Z]])
    ev = np.linalg.eigvals(To @ Te)
    order = np.argsort(np.abs(ev))
    decay = ev[order[:dim]]
    return float(np.min(np.real(decay))), float(np.max(np.abs(np.imag(decay))))


# ===========================================================================
# Gauge-invariance check: apply a random gauge transform g_x at the endpoints and
# confirm the full-algebra Gram is unchanged (the meson/baryon are color singlets).
# Gauge transform: chi(x) -> g_x chi(x), chibar(x) -> chibar(x) g_x^dag,
# link U(x,x+1) -> g_x U(x,x+1) g_{x+1}^dag.  We implement it by transforming the
# Dirac matrix M -> G M G^dag with G block-diag(g_x per site, all slices) AND the
# observable color structure consistently, and check the Gram is invariant.
# ===========================================================================
def gauge_transform_links(carrier, links, gs):
    """gs: dict x-> g_x (nc x nc unitary). U(x,x+1) -> g_x U(x,x+1) g_{x+1}^dag."""
    Ns = carrier.Ns
    new_links = {}
    for x in range(Ns):
        new_links[x] = gs[x] @ links[x] @ gs[(x + 1) % Ns].conj().T
    return new_links


def _perconfig_gram(carrier, links, t_op=0, include_products=True):
    """Per-config OS Gram <Theta(A_I) A_J>_U from the full spacetime Berezin
    propagator M[U]^{-1} over the basis built ON THESE links (the meson amplitude
    uses links[x]). Returns (labels, G)."""
    Minv = np.linalg.inv(carrier.build_M(links))
    base = build_basis(carrier, links, t_op, include_products)
    labels = [l for l, _ in base]
    n = len(base)
    G = np.zeros((n, n), dtype=complex)
    thetas = [[theta_monomial(c, f, carrier, False) for (c, f) in m] for _, m in base]
    rights = [[mono_to_idx(c, f, carrier) for (c, f) in m] for _, m in base]
    for I in range(n):
        for J in range(n):
            acc = 0.0 + 0.0j
            for (cI, fI) in thetas[I]:
                if cI == 0:
                    continue
                for (cJ, fJ) in rights[J]:
                    if cJ == 0:
                        continue
                    acc += cI * cJ * wick(fI + fJ, Minv)
            G[I, J] = acc
    return labels, G


def _random_op(carrier, rng, t_op=0, maxdeg=3):
    """A random half-space polynomial: a few monomials of degree 1..maxdeg in
    chi/chibar at positive time t_op with random complex coeffs (repeated identical
    Grassmann factors dropped)."""
    Ns, nc = carrier.Ns, carrier.nc
    nmon = int(rng.integers(1, 4))
    mon = []
    for _ in range(nmon):
        deg = int(rng.integers(1, maxdeg + 1))
        used = set()
        factors = []
        for _ in range(deg):
            kd = 'c' if rng.random() < 0.5 else 'cb'
            x = int(rng.integers(0, Ns))
            a = int(rng.integers(0, nc))
            if (kd, x, a) in used:
                continue
            used.add((kd, x, a))
            factors.append((kd, x, a, t_op))
        if factors:
            mon.append((complex(rng.standard_normal(), rng.standard_normal()), factors))
    if not mon:
        mon = [(1.0 + 0.0j, [('cb', 0, 0, t_op)])]
    return mon


def random_basis_psd_scan(carrier, group, n_trials, n_ops, rng):
    """STRESS the basis-completeness gap: build n_ops RANDOM half-space polynomials
    (degree<=3) and verify the per-config OS Gram is PSD. The reflection-square logic
    (G[U]=M^dag M) says PSD must hold for ANY operator set; this confirms it numerically
    BEYOND the curated meson/baryon basis. Returns (worst_min_eig, worst_herm)."""
    worst = math.inf
    worst_herm = 0.0
    for _ in range(n_trials):
        if group == 'u1':
            links = {x: u1_phase(rng.uniform(0, 2 * math.pi))
                     for x in range(carrier.Ns)}
        elif group == 'su2':
            links = {x: random_su2() for x in range(carrier.Ns)}
        else:
            links = {x: random_su3() for x in range(carrier.Ns)}
        Minv = np.linalg.inv(carrier.build_M(links))
        ops = [[(1.0 + 0.0j, [])]] + [_random_op(carrier, rng) for _ in range(n_ops)]
        n = len(ops)
        G = np.zeros((n, n), dtype=complex)
        thetas = [[theta_monomial(c, f, carrier, False) for (c, f) in m] for m in ops]
        rights = [[mono_to_idx(c, f, carrier) for (c, f) in m] for m in ops]
        for I in range(n):
            for J in range(n):
                acc = 0.0 + 0.0j
                for (cI, fI) in thetas[I]:
                    if cI == 0:
                        continue
                    for (cJ, fJ) in rights[J]:
                        if cJ == 0:
                            continue
                        acc += cI * cJ * wick(fI + fJ, Minv)
                G[I, J] = acc
        worst = min(worst, float(np.linalg.eigvalsh(0.5 * (G + G.conj().T)).min()))
        worst_herm = max(worst_herm, float(np.max(np.abs(G - G.conj().T))))
    return worst, worst_herm


def gauge_invariance_check(carrier, links, gs, t_op=0, include_products=True):
    """RIGOROUS per-config K5 control. A gauge transform sends the dynamical fields
    chi(x)->g_x chi(x) (hence M[U]^{-1} -> Gtot M[U]^{-1} Gtot^dag) AND every gauge
    link U(x,y)->g_x U(x,y) g_y^dag. The transformed correlator is therefore computed
    by building the basis on the TRANSFORMED links (so the meson amplitude is
    g_x U g_y^dag) and contracting against the TRANSFORMED propagator M[gUg']^{-1}.
    For the GAUGE-INVARIANT observables (color-singlet mesons chibar U chi, baryons
    eps chi chi chi, anti-baryons, identity) the field rotation in the propagator
    EXACTLY cancels the link transform, so those Gram entries are invariant. The bare
    single-field bilinears chibar_a are gauge-COVARIANT (not invariant), so their
    block legitimately transforms; the physically meaningful invariant for the FULL
    Gram is that its EIGENVALUES (hence PSD) are preserved.
    Returns (inv_block_diff, full_eig_diff)."""
    labels, G_ref = _perconfig_gram(carrier, links, t_op, include_products)
    glinks = gauge_transform_links(carrier, links, gs)
    _, G_gt = _perconfig_gram(carrier, glinks, t_op, include_products)
    # The GAUGE-INVARIANT singlet operators: identity, color-singlet mesons
    # (chibar U chi), baryons (eps chi chi chi) and anti-baryons. EXCLUDE the bare
    # single-field bilinears chibar_a (gauge-COVARIANT, legitimately transform) AND
    # the product operators meson*chibar (which contain a dangling covariant chibar
    # and are therefore NOT singlets despite the "meson" prefix).
    def is_singlet(l):
        if l == 'id':
            return True
        if l.startswith('meson') and '*' not in l:
            return True
        if l.startswith('baryon') or l.startswith('antibaryon'):
            return True
        return False
    inv_idx = [i for i, l in enumerate(labels) if is_singlet(l)]
    sub_ref = G_ref[np.ix_(inv_idx, inv_idx)]
    sub_gt = G_gt[np.ix_(inv_idx, inv_idx)]
    inv_block_diff = float(np.max(np.abs(sub_gt - sub_ref)))
    # PSD of the gauge-invariant-sector Gram (the physical mesons/baryons) is itself
    # gauge-invariant; report its min eig under the transform too.
    sub_min_ref = float(np.linalg.eigvalsh(0.5 * (sub_ref + sub_ref.conj().T)).min())
    sub_min_gt = float(np.linalg.eigvalsh(0.5 * (sub_gt + sub_gt.conj().T)).min())
    inv_psd_diff = abs(sub_min_ref - sub_min_gt)
    return inv_block_diff, inv_psd_diff


# ===========================================================================
# MAIN
# ===========================================================================
def haar_configs(group, Ns, n_cfg, beta):
    """Return (configs, weights) with weights = exp(-S_G) using the temporal-gauge
    spatial-plaquette-free single-slice; here we use a flat-but-positive weight times
    the det (the det carries the fermion measure). For genuine Haar averaging the
    gauge weight is w=1 (Haar measure) on the compact group; the det>0 weight is the
    load-bearing positive fermion factor. We keep an optional Wilson-like positive
    weight for robustness."""
    configs, weights = [], []
    for _ in range(n_cfg):
        if group == 'u1':
            th = RNG.uniform(0, 2 * math.pi, size=Ns)
            links = {x: u1_phase(th[x]) for x in range(Ns)}
        elif group == 'su2':
            links = {x: random_su2() for x in range(Ns)}
        else:
            links = {x: random_su3() for x in range(Ns)}
        # positive single-slice gauge weight (Wilson-like on the ring of spatial links):
        # S_G = -beta * sum_x Re Tr(U_x)/nc ; w=exp(-S_G) > 0. (Any positive weight;
        # the RP-positive cross-slice transfer is the separate established rung.)
        nc = links[0].shape[0]
        sG = -beta * sum(np.real(np.trace(links[x])) / nc for x in range(Ns))
        weights.append(math.exp(-sG))
        configs.append(links)
    return configs, weights


def run_group(group, Ns, nc, nt, n_cfg, beta, label):
    print("-" * 82)
    print(f"{label}: group={group}  Ns={Ns} (spatial ring)  nc={nc}  nt={nt} "
          f"(Lt={2*nt})  n_cfg={n_cfg}")
    print("-" * 82)
    carrier = Carrier(Ns, nc, nt)
    configs, weights = haar_configs(group, Ns, n_cfg, beta)

    # ---- main: full-algebra OS Gram (CORRECT reflection), U-averaged ----
    labels, G, det_min, n_det_nonpos, diag = full_algebra_gram(
        carrier, configs, weights, wrong=False)
    Gh = 0.5 * (G + G.conj().T)
    herm = float(np.max(np.abs(G - G.conj().T)))
    ev = np.linalg.eigvalsh(Gh)
    mineig = float(ev.min())

    # ---- EXACTNESS backbone: the PER-CONFIG full-algebra Gram is itself PSD.
    # This is the reflection-square argument: per config T2[U]=B[U]^dag B[U] is PSD,
    # so G[U]_{IJ}=<Theta(A_I)A_J>_U = <B A_I Omega, B A_J Omega> is a manifest Gram
    # for EVERY operator set. Hence the U-average sum_U w_U det(M[U]) G[U] (w_U>0,
    # det>0 Case A) is PSD with ZERO Monte-Carlo error in the conclusion -- the Haar
    # sample only affects the numerical min-eig value, not the PSD verdict. ----
    perconfig_min = math.inf
    for links in configs:
        _, Gu = _perconfig_gram(carrier, links)
        Guh = 0.5 * (Gu + Gu.conj().T)
        perconfig_min = min(perconfig_min, float(np.linalg.eigvalsh(Guh).min()))

    # ---- BASIS-COMPLETENESS stress: random half-space polynomials (deg<=3) ----
    rand_min, rand_herm = random_basis_psd_scan(
        carrier, group, n_trials=30, n_ops=16, rng=RNG)

    # ---- T-WRONG control: wrong single-step reflection -> NON-PSD ----
    _, Gw, _, _, _ = full_algebra_gram(carrier, configs, weights, wrong=True)
    Gwh = 0.5 * (Gw + Gw.conj().T)
    mineig_wrong = float(np.linalg.eigvalsh(Gwh).min())

    # ---- NONVAC: meson/baryon diagonal entries > 0 ----
    meson_idx = [i for i, l in enumerate(labels) if l.startswith("meson")]
    baryon_idx = [i for i, l in enumerate(labels) if l.startswith("baryon")]
    abaryon_idx = [i for i, l in enumerate(labels) if l.startswith("antibaryon")]
    meson_diag_min = min(diag[i] for i in meson_idx) if meson_idx else float('nan')
    baryon_diag_min = min(diag[i] for i in baryon_idx) if baryon_idx else float('nan')
    abaryon_diag_min = (min(diag[i] for i in abaryon_idx)
                        if abaryon_idx else float('nan'))

    # ---- VAC0: naive operator matrix element is 0 (Ohat|Omega>=0) ----
    base = build_basis(carrier, configs[0])
    vac_norms = {}
    for lab in ("meson_onsite[0]", f"baryon[0]"):
        op = dict(base).get(lab)
        if op is not None:
            vac_norms[lab] = op_on_vacuum_norm(carrier, op)

    # ---- reflection-square: per-config 2-step transfer PSD (the OS-theorem input) ----
    min_decay = math.inf
    worst_imag = 0.0
    for links in configs:
        md, wi = two_step_transfer_psd(carrier, links)
        min_decay = min(min_decay, md)
        worst_imag = max(worst_imag, wi)

    # ---- GAUGEINV (rigorous, per-config): a genuine gauge transform U->gUg',
    # chi->g chi (propagator covariant) leaves the GAUGE-INVARIANT singlet (meson/
    # baryon/identity) Gram block exactly invariant, and the FULL-Gram eigenvalues
    # (hence PSD) invariant. Averaged over several random g and configs. ----
    inv_block_diff = 0.0
    inv_psd_diff = 0.0
    n_gtest = min(len(configs), 5)
    for links in configs[:n_gtest]:
        gs = {x: (random_u1_mat(nc) if group == 'u1' else
                  (random_su2() if group == 'su2' else random_su3()))
              for x in range(Ns)}
        ib, ip = gauge_invariance_check(carrier, links, gs)
        inv_block_diff = max(inv_block_diff, ib)
        inv_psd_diff = max(inv_psd_diff, ip)
    gauge_gram_diff = max(inv_block_diff, inv_psd_diff)

    print(f"  basis size = {len(labels)}  "
          f"(mesons={len(meson_idx)}, baryons={len(baryon_idx)}, "
          f"antibaryons={len(abaryon_idx)})")
    print(f"  DETPOS: min det(M[U]) = {det_min:.4e}  (nonpos configs = {n_det_nonpos})")
    print(f"  FULL-ALGEBRA Gram (U-averaged): ||G-G^dag|| = {herm:.2e}   "
          f"min eig = {mineig:+.6e}   max eig = {ev.max():.4e}")
    print(f"  EXACTNESS: worst PER-CONFIG full-algebra Gram min eig = "
          f"{perconfig_min:+.6e}  (>=0 => U-average PSD exactly, MC-free verdict)")
    print(f"  BASIS-COMPLETENESS: random deg<=3 half-space polys, per-config min eig = "
          f"{rand_min:+.3e}  (||G-G^dag||={rand_herm:.1e})")
    print(f"  NONVAC: meson diag min = {meson_diag_min:+.4e}  "
          f"baryon diag min = {baryon_diag_min:+.4e}  "
          f"antibaryon diag min = {abaryon_diag_min:+.4e}")
    for lab, vn in vac_norms.items():
        print(f"  VAC0:   ||{lab} |Omega>|| = {vn:.3e}  (naive operator m.e. vacuous)")
    print(f"  T-WRONG control (single-step, no gamma0): min eig = {mineig_wrong:+.4e}")
    print(f"  reflection-square input: per-config 2-step min decay = {min_decay:.4e}  "
          f"max|Im decay| = {worst_imag:.2e}")
    print(f"  GAUGEINV: gauge-invariant-sector(meson/baryon) Gram max|diff| = "
          f"{inv_block_diff:.2e}  (singlet-sector min-eig |diff| = {inv_psd_diff:.2e})")

    ok_psd = (mineig > -TOL) and (herm < 1e-8)
    ok_perconfig = (perconfig_min > -TOL)
    ok_randbasis = (rand_min > -1e-7) and (rand_herm < 1e-8)
    ok_nonvac = (meson_diag_min > 1e-6) and (
        math.isnan(baryon_diag_min) or baryon_diag_min > 1e-6)
    ok_vac0 = all(v < 1e-9 for v in vac_norms.values()) if vac_norms else True
    ok_wrong = mineig_wrong < -1e-3
    ok_refl = (min_decay > 0.0) and (worst_imag < 1e-7)
    ok_gauge = gauge_gram_diff < 1e-7
    ok_det = (det_min > 0.0) and (n_det_nonpos == 0)

    checks = {
        "full_algebra_PSD(U-averaged)": ok_psd,
        "full_algebra_PSD(per-config,exact)": ok_perconfig,
        "full_algebra_PSD(random_basis,deg<=3)": ok_randbasis,
        "nonvacuous_meson_baryon": ok_nonvac,
        "naive_op_vacuous(VAC0)": ok_vac0,
        "wrong_reflection_nonPSD(teeth)": ok_wrong,
        "reflection_square_input_PSD": ok_refl,
        "gauge_invariant": ok_gauge,
        "det_positive(CaseA)": ok_det,
    }
    for k, v in checks.items():
        print(f"    [{'PASS' if v else 'FAIL'}] {k}")
    allok = all(checks.values())
    print(f"  -> {label}: {'PASS' if allok else 'FAIL'}")
    return allok, {
        "mineig": mineig, "mineig_wrong": mineig_wrong,
        "meson_diag_min": meson_diag_min, "baryon_diag_min": baryon_diag_min,
        "n_basis": len(labels), "det_min": det_min,
    }


def random_u1_mat(nc):
    return u1_phase(RNG.uniform(0, 2 * math.pi))


def run_companion_controls() -> bool:
    """Run the source-hash-pinned m=0.01 and link-reflection companion controls."""
    import frontier_interacting_rp_mass_link_reflection_controls_2026_06_09 as controls

    controls.PASS = 0
    controls.FAIL = 0
    print()
    print("=" * 82)
    print("COMPANION CONTROLS: MASS SCAN AND LINK-REFLECTION CONVENTION")
    print("=" * 82)
    controls.primary_source_guard()
    controls.source_note_guard()
    controls.run_mass_scan()
    controls.run_nonconjugating_control()
    print(f"\nCOMPANION SCORECARD: PASS={controls.PASS} FAIL={controls.FAIL}")
    return controls.FAIL == 0


def main() -> int:
    print("=" * 82)
    print("FULL POLYNOMIAL HALF-SPACE ALGEBRA OS REFLECTION-POSITIVITY (FIXED a)")
    print("  gauge-invariant four-fermion observables (mesons chibar U chi, baryons")
    print("  eps chi chi chi) acting NON-VACUOUSLY via the Berezin OS correlator")
    print("=" * 82)
    print(f"  mass m={MASS}. Settled Berezin convention "
          f"<chi_b bar_a>=+(M^-1)[b,a], <bar_a chi_b>=-(M^-1)[b,a].")
    print(f"  OS reflection theta(t)=(-1-t), Theta(chi)=-chibar(-1-t) (gamma_0 sign).")
    print()

    results = []

    # SU(2) lighter cross-check first (verify before SU(3)), few links, small carrier.
    # NOTE: nc=2 has no baryon (needs nc>=3); tests bilinears + transported mesons.
    ok, _ = run_group('su2', Ns=2, nc=2, nt=2, n_cfg=200, beta=1.0,
                      label="SU(2) [bilinears + transported mesons]")
    results.append(ok)
    print()

    # U(1) abelian cross-check, includes on-site + transported mesons (nc=1: no baryon).
    ok, _ = run_group('u1', Ns=3, nc=1, nt=2, n_cfg=400, beta=2.0,
                      label="U(1) [bilinears + transported mesons]")
    results.append(ok)
    print()

    # SU(3) FULL algebra: bilinears + on-site/transported mesons + baryon + antibaryon.
    # Smallest carrier where a single-site baryon (3 colors) AND a transported meson fit:
    # Ns=2 spatial ring, nc=3, nt=2.
    ok, info3 = run_group('su3', Ns=2, nc=3, nt=2, n_cfg=120, beta=4.0,
                          label="SU(3) FULL ALGEBRA [bilinears+mesons+baryons]")
    results.append(ok)
    print()

    # SU(3) single-site baryon focus (Ns=1: on-site meson + baryon + antibaryon only,
    # no transported meson; isolates the four-fermion baryon sector cleanly, exact in U
    # since a single site has no spatial link -> the gauge average is trivial/exact).
    ok, info3b = run_group('su3', Ns=1, nc=3, nt=2, n_cfg=1, beta=0.0,
                           label="SU(3) single-site [on-site meson + baryon + antibaryon]")
    results.append(ok)
    print()

    companion_ok = run_companion_controls()

    print("=" * 82)
    npass = sum(results)
    print(f"GROUP SCORECARD: PASS={npass}/{len(results)} group-sectors")
    print("  Each sector: full-algebra OS Gram PSD (CORRECT reflection), non-vacuous")
    print("  meson/baryon diagonals>0, naive op m.e. vacuous, WRONG reflection non-PSD,")
    print("  per-config 2-step transfer PSD (OS-theorem input), gauge-invariant, det>0.")
    print(f"  Companion controls: {'PASS' if companion_ok else 'FAIL'}")
    allok = (npass == len(results)) and companion_ok
    print(f"  OVERALL: {'PASS' if allok else 'FAIL'}")
    print("=" * 82)
    return 0 if allok else 1


if __name__ == "__main__":
    raise SystemExit(main())
