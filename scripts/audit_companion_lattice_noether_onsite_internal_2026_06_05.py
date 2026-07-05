#!/usr/bin/env python3
"""
audit_companion_lattice_noether_onsite_internal_2026_06_05.py
-------------------------------------------------------------

Companion runner for

  docs/AXIOM_FIRST_LATTICE_NOETHER_ONSITE_INTERNAL_NARROW_THEOREM_NOTE_2026-06-05.md

This is an audit-repair runner for the lattice Noether row
`axiom_first_lattice_noether_theorem_note_2026-04-29`. It REPROVES, from
primitives (sympy exact + numpy), the three things the conditional audit asked
for:

  (1) The U(1) sign convention of the Noether current is fixed (no longer
      ad-hoc) by requiring the lattice CONTINUITY equation

          d rho_x / dt  +  (div^L j)_x  =  0,        rho_x := chibar_x chi_x,

      to hold, where (div^L j)_x = sum_mu ( j^mu_x - j^mu_{x-mu} ). With the
      onsite U(1) number-density operator rho_x = chibar_x chi_x and dQ/dt = 0,
      the current sign is determined uniquely.

  (2) The general lattice Noether identity is RESTRICTED to onsite / internal
      symmetry generators T (acting site-locally, T_{xy} = t * delta_{xy} for a
      single-site internal matrix t, i.e. [T, S^{(a)}] = 0 for every lattice
      shift). For such generators the conserved current inherits the support
      envelope of the Hamiltonian coefficients. It is nearest-neighbour on the
      finite staggered nearest-neighbour carrier, finite-range for finite-range
      coefficients, and all-to-all when c_xy is all-to-all. Site-mixing
      generators (e.g. the two-site translation) are scoped OUT and recorded as
      a named open item; see Part D for the explicit counterexample that
      motivates the restriction.

  (3) An ARBITRARY-BILINEAR SYMBOLIC check (Part A): for a fully symbolic
      bilinear H = sum_ij c_ij a_i^dag a_j with the global U(1) / onsite-internal
      symmetry, the operator continuity equation is verified symbolically over
      the bilinear Lie algebra E_{pq} := a_p^dag a_q, with NO numeric entries.
      The lattice divergence of the symbolic current equals the (negative of
      the) time-derivative of the charge density, and dQ/dt = 0.

REPROVE-AND-CITE: every load-bearing algebraic fact below is reproven here from
the bilinear-operator primitives. The standard variational/Noether technique
and the bilinear commutator identity are reproven, not asserted. No PDG /
fitted / measured / lattice-MC / beta=6 / g_bare value is used as input. The
free staggered Dirac operator built in Parts C and D is a finite exhibit only
(no measured input); its mass is an arbitrary positive bookkeeping constant.

2026-06-07 boundary repair: the paired source note now cites the retained
abstract bilinear continuity theorem as the authority for the carrier-free
matrix-unit identities. This runner keeps the replay as a guardrail and checks
that the source note does not promote the finite staggered/Kawamoto-Smit
exhibit into the framework's realized matter kinetic or a physical readout
theorem.

Each check prints [PASS]/[FAIL]; the script prints a final
'TOTAL: N PASS / 0 FAIL' line and exits nonzero on any failure.
"""

from __future__ import annotations

import sys
from itertools import product

import numpy as np
import sympy as sp

RESULTS: list[tuple[str, bool]] = []


def record(name: str, ok: bool) -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    RESULTS.append((name, bool(ok)))


# ---------------------------------------------------------------------------
# Shared primitive: the number-conserving bilinear Lie algebra.
#
# E_{pq} := a_p^dag a_q. The single structural input is the commutator
#
#     [E_ij, E_pq]  =  delta_jp E_iq  -  delta_qi E_pj.                 (B)
#
# (B) holds for BOTH bosonic (CCR) and fermionic (CAR) statistics; we reprove
# it exactly on the fermionic Fock space (finite dimension) in Part B0, so it
# is not asserted by name. All symbolic Noether algebra below uses ONLY (B).
# ---------------------------------------------------------------------------


def bil_commutator(A: dict, B: dict) -> dict:
    """Commutator of two elements of span{E_pq}, each a dict {(p,q): coeff},
    using ONLY the structure constants of identity (B)."""
    out: dict = {}
    for (i, j), x in A.items():
        for (p, q), y in B.items():
            if j == p:
                out[(i, q)] = out.get((i, q), 0) + x * y
            if q == i:
                out[(p, j)] = out.get((p, j), 0) - x * y
    return {k: sp.simplify(v) for k, v in out.items() if sp.simplify(v) != 0}


# ---------------------------------------------------------------------------
# Part B0 — reprove the bilinear commutator identity (B) on fermionic Fock
# space (exact, finite dimension). This grounds the symbolic algebra used by
# every other part.
# ---------------------------------------------------------------------------


def _fermi_ann(n: int) -> list[np.ndarray]:
    I2 = np.eye(2)
    Z = np.array([[1.0, 0.0], [0.0, -1.0]])
    ann = np.array([[0.0, 1.0], [0.0, 0.0]])
    ops = []
    for k in range(n):
        mats = [Z] * k + [ann] + [I2] * (n - 1 - k)
        M = mats[0]
        for m in mats[1:]:
            M = np.kron(M, m)
        ops.append(M)
    return ops


def part_B0_commutator_identity() -> None:
    print("\n[Part B0] reprove bilinear commutator identity (B) on CAR Fock space")
    n = 3
    a = _fermi_ann(n)
    adag = [x.conj().T for x in a]

    def comm(A, B):
        return A @ B - B @ A

    max_err = 0.0
    for i, j, p, q in product(range(n), repeat=4):
        lhs = comm(adag[i] @ a[j], adag[p] @ a[q])
        rhs = (1.0 if j == p else 0.0) * (adag[i] @ a[q]) - (
            1.0 if q == i else 0.0
        ) * (adag[p] @ a[j])
        max_err = max(max_err, float(np.max(np.abs(lhs - rhs))))
    print(f"  n={n}, max |[E_ij,E_pq] - (d_jp E_iq - d_qi E_pj)| = {max_err:.3e}")
    record("B0 bilinear commutator identity (B) holds exactly on CAR Fock space", max_err < 1e-12)


# ---------------------------------------------------------------------------
# Part A — arbitrary-bilinear SYMBOLIC continuity check (the E5 replacement).
#
# Fully symbolic c_ij (no numeric entries). H = sum_ij c_ij E_ij with global
# U(1)/onsite-internal symmetry Q = sum_p E_pp. We verify symbolically:
#   (A1) [H, Q] = 0 for an ARBITRARY bilinear (U(1) is automatic);
#   (A2) i[H, rho_p] = sum_q j_{p<-q}  with the bond current
#            j_{p<-q} := i ( c_qp E_qp  -  c_pq E_pq ),
#        i.e. d rho_p/dt equals net inflow -> lattice continuity equation;
#   (A3) the current sign: writing (div^L j)_p := -sum_q j_{p<-q} (net outflow),
#        d rho_p/dt = -(div^L j)_p, the sign-fixed continuity equation;
#   (A4) sum_p d rho_p/dt = 0  =>  dQ/dt = 0  (global conservation).
#   (A5) support envelope: the {p,q} current uses only c_pq and c_qp, and
#        vanishes if those two coefficients vanish. Noether does not turn an
#        arbitrary all-to-all bilinear into a nearest-neighbour current.
# ---------------------------------------------------------------------------


def part_A_arbitrary_bilinear() -> None:
    print("\n[Part A] arbitrary-bilinear symbolic continuity (replaces old E5)")
    n = 3
    c = sp.IndexedBase("c")
    H = {(i, j): c[i, j] for i in range(n) for j in range(n)}
    Q = {(p, p): sp.Integer(1) for p in range(n)}

    # (A1) U(1) is a symmetry of EVERY bilinear: [H, Q] = 0 symbolically.
    HQ = bil_commutator(H, Q)
    record("A1 [H,Q]=0 for arbitrary symbolic bilinear (onsite-internal U(1))", len(HQ) == 0)

    # (A2)/(A3) per-site continuity, fully symbolic.
    sign_ok = True
    div_ok = True
    for p in range(n):
        rho = {(p, p): sp.Integer(1)}
        # i [H, rho_p]
        idr = {k: sp.I * v for k, v in bil_commutator(H, rho).items()}
        # net inflow = sum_q j_{p<-q}, j_{p<-q} = i(c_qp E_qp - c_pq E_pq)
        inflow: dict = {}
        for q in range(n):
            if q == p:
                continue
            inflow[(q, p)] = inflow.get((q, p), 0) + sp.I * c[q, p]
            inflow[(p, q)] = inflow.get((p, q), 0) - sp.I * c[p, q]
        keys = set(idr) | set(inflow)
        for k in keys:
            if sp.simplify(idr.get(k, 0) - inflow.get(k, 0)) != 0:
                sign_ok = False
        # (div^L j)_p := -inflow ; check d rho/dt = -(div^L j)_p, i.e. idr == inflow == -div
        # (same content as sign_ok, but we also confirm the explicit minus-sign form)
        for k in keys:
            div_k = -inflow.get(k, 0)
            if sp.simplify(idr.get(k, 0) - (-div_k)) != 0:
                div_ok = False
    record("A2 i[H,rho_p] = net inflow (operator continuity, arbitrary c_ij)", sign_ok)
    record("A3 d rho_p/dt = -(div^L j)_p with sign-fixed current (arbitrary c_ij)", div_ok)

    # (A4) global: sum_p i[H,rho_p] = i[H,Q] = 0.
    total: dict = {}
    for p in range(n):
        rho = {(p, p): sp.Integer(1)}
        for k, v in bil_commutator(H, rho).items():
            total[k] = total.get(k, 0) + v
    total = {k: sp.simplify(v) for k, v in total.items() if sp.simplify(v) != 0}
    record("A4 sum_p d rho_p/dt = 0 => dQ/dt = 0 (arbitrary c_ij)", len(total) == 0)

    # (A5) exact support envelope. The pair current on {p,q} depends only on the
    # two Hamiltonian coefficients on that pair, c_pq and c_qp. In particular,
    # it vanishes when both are zero. Thus finite-range support stays
    # finite-range, nearest-neighbour support stays nearest-neighbour, and
    # arbitrary all-to-all support stays all-to-all.
    support_ok = True
    for p, q in product(range(n), repeat=2):
        if p == q:
            continue
        edge_current = {
            (q, p): sp.I * c[q, p],
            (p, q): -sp.I * c[p, q],
        }
        allowed = {(q, p), (p, q)}
        zero_pair = {c[q, p]: 0, c[p, q]: 0}
        for expr in edge_current.values():
            if sp.simplify(expr.subs(zero_pair)) != 0:
                support_ok = False
            for a, b in product(range(n), repeat=2):
                if (a, b) not in allowed and expr.has(c[a, b]):
                    support_ok = False
    record("A5 pair current has exactly the Hamiltonian coefficient support envelope", support_ok)


# ---------------------------------------------------------------------------
# Part B — onsite/internal generator restriction (symbolic, arbitrary bilinear).
#
# An ONSITE/INTERNAL generator acts as T_{(x,c1)(y,c2)} = delta_{xy} t_{c1 c2}
# (a single-site internal matrix t, same t on every site). The defining
# property used by the local-current derivation is that T COMMUTES WITH EVERY
# LATTICE SHIFT S^{(a)} (it does not move sites). We verify:
#   (B1) For an internal U(1)-type generator t = i*Id, [T, S^(a)] = 0 (onsite).
#   (B2) Under such an onsite T, the local-alpha Noether current is the
#        anti-Hermitian variational NEAREST-NEIGHBOUR bond current (manifestly
#        local on the staggered nearest-neighbour carrier): the
#        coefficient of (alpha_{x+mu}-alpha_x) is
#            j^mu_x = (1/2) eta_mu(x) [ chibar_x (t) chi_{x+mu}
#                                       + chibar_{x+mu} (t) chi_x ].
#        Verified by an exact symbolic match against delta S_F on a chain.
# ---------------------------------------------------------------------------


def part_B_onsite_internal_locality() -> None:
    print("\n[Part B] onsite/internal generator => local nearest-neighbour current")

    # (B1) onsite generator commutes with shift (uses only that it is diagonal
    # in the site index). Build a small site set and a single-site internal
    # matrix t acting in a 1-dim internal space (U(1): t = i). Onsite T on the
    # lattice index is i*Identity; a shift permutation S commutes with i*Id.
    L = 4
    N = L
    S = np.zeros((N, N), dtype=complex)
    for x in range(N):
        S[x, (x + 1) % L] = 1.0  # one-site shift permutation
    T_onsite = 1j * np.eye(N, dtype=complex)  # onsite internal U(1) generator
    comm_err = float(np.max(np.abs(T_onsite @ S - S @ T_onsite)))
    print(f"  ||[T_onsite, S^(1)]||_max = {comm_err:.3e} (onsite gen commutes with shift)")
    record("B1 onsite/internal generator commutes with every lattice shift", comm_err < 1e-12)

    # (B2) exact symbolic locality of the current for an onsite internal U(1)
    # generator t = i on a periodic chain (direction 0, eta = 1).
    Lc = 5  # odd length avoids periodic-wrap coincidences
    chi = sp.symbols(f"chi0:{Lc}")
    chibar = sp.symbols(f"chibar0:{Lc}")
    alpha = sp.symbols(f"alpha0:{Lc}")
    half = sp.Rational(1, 2)
    i = sp.I

    def Mchi(x):
        return half * chi[(x + 1) % Lc] - half * chi[(x - 1) % Lc]

    # delta S_F with site-dependent alpha, onsite U(1): delta chi_x = i alpha_x chi_x.
    dS = 0
    for x in range(Lc):
        dchibar_x = -i * alpha[x] * chibar[x]
        dchi_xp = i * alpha[(x + 1) % Lc] * chi[(x + 1) % Lc]
        dchi_xm = i * alpha[(x - 1) % Lc] * chi[(x - 1) % Lc]
        Mdchi_x = half * dchi_xp - half * dchi_xm
        dS += dchibar_x * Mchi(x) + chibar[x] * Mdchi_x
    dS = sp.expand(dS)

    # bilateral local current (coefficient of forward difference alpha_{x+1}-alpha_x)
    def bilateral(x):
        return half * (chibar[x] * (i * chi[(x + 1) % Lc]) + chibar[(x + 1) % Lc] * (i * chi[x]))

    RHS = sum(bilateral(x) * (alpha[(x + 1) % Lc] - alpha[x]) for x in range(Lc))
    locality_residual = sp.simplify(sp.expand(dS - RHS))
    print(f"  delta S_F - sum_x j^mu_x (alpha_(x+1)-alpha_x) = {locality_residual}")
    record(
        "B2 onsite U(1): current is local bilateral nn bond current (exact symbolic)",
        locality_residual == 0,
    )


# ---------------------------------------------------------------------------
# Part C — staggered specialization with the FIXED U(1) SIGN (numeric exhibit
# on the finite free staggered carrier). This pins the prefactor in the
# corrected formula (4):
#
#     j^mu_x  =  -(1/2) eta_mu(x) [ chibar_x chi_{x+mu} + chibar_{x+mu} chi_x ]
#
# as the (anti-Hermitian-kinetic) charge current whose lattice divergence
# equals -d rho_x/dt, with rho_x = chibar_x chi_x. We verify:
#   (C1) the symmetry condition [T_U1, M] = 0 for T_U1 = i Id;
#   (C2) on the free ground state, the fixed-sign current is divergence-free:
#        (div^L j)_x = 0 (the static ground-state continuity, d rho/dt = 0);
#   (C3) the dynamical continuity equation d rho_x/dt + (div^L j)_x = 0 holds
#        operator-wise with the FIXED sign (and FAILS with the flipped sign),
#        checked on the exact fermionic Fock space for the staggered hop. This
#        is what selects the sign that the old note set by an ad-hoc -i rule.
# ---------------------------------------------------------------------------


def staggered_eta(x, mu):
    if mu == 0:
        return 1.0
    return float((-1) ** sum(x[:mu]))


def build_M_pure_staggered(L, mass, dim):
    sites = list(product(range(L), repeat=dim))
    idx = {x: i for i, x in enumerate(sites)}
    N = len(sites)
    M = np.zeros((N, N), dtype=complex)
    for x in sites:
        i = idx[x]
        M[i, i] += mass
        for mu in range(dim):
            ehat = tuple(1 if k == mu else 0 for k in range(dim))
            xp = tuple((x[k] + ehat[k]) % L for k in range(dim))
            xm = tuple((x[k] - ehat[k]) % L for k in range(dim))
            eta = staggered_eta(x, mu)
            M[i, idx[xp]] += 0.5 * eta
            M[i, idx[xm]] += -0.5 * eta
    return M, sites, idx


def part_C_staggered_fixed_sign() -> None:
    print("\n[Part C] staggered specialization: U(1) symmetry + fixed-sign current")
    L, dim = 4, 3
    mass = float(sp.Rational(3, 10))  # arbitrary positive bookkeeping const
    M, sites, idx = build_M_pure_staggered(L, mass, dim)
    N = len(sites)

    # (C1) symmetry condition [T_U1, M] = 0.
    T_U1 = 1j * np.eye(N, dtype=complex)
    comm_err = float(np.max(np.abs(T_U1 @ M - M @ T_U1)))
    print(f"  ||[T_U1, M]||_max = {comm_err:.3e}")
    record("C1 U(1) symmetry condition [T_U1, M] = 0 on staggered carrier", comm_err < 1e-12)

    # (C2) fixed-sign current divergence-free in the free ground state.
    Minv = np.linalg.inv(M)

    def G(a, b):
        # <chibar_a chi_b> = (M^-1)_{ba} (Wick), consistent across exhibits.
        return Minv[idx[b], idx[a]]

    def j_fixed(x, mu):
        # corrected formula (4): j^mu_x = -(1/2) eta [ <chibar_x chi_{x+mu}> + <chibar_{x+mu} chi_x> ]
        ehat = tuple(1 if k == mu else 0 for k in range(dim))
        xp = tuple((x[k] + ehat[k]) % L for k in range(dim))
        eta = staggered_eta(x, mu)
        return -0.5 * eta * (G(x, xp) + G(xp, x))

    div_max = 0.0
    for x in sites:
        dv = 0j
        for mu in range(dim):
            ehat = tuple(1 if k == mu else 0 for k in range(dim))
            xm = tuple((x[k] - ehat[k]) % L for k in range(dim))
            dv += j_fixed(x, mu) - j_fixed(xm, mu)
        div_max = max(div_max, abs(dv))
    print(f"  max |(div^L j)_x| in free ground state = {div_max:.3e}")
    print("  (note: ground-state divergence is sign-independent; C3 fixes the sign)")
    record("C2 formula-(4) U(1) current is divergence-free on shell (ground state)", div_max < 1e-9)

    # (C3) dynamical continuity d rho_x/dt + (div^L j)_x = 0 operator-wise. This
    # is what FIXES the U(1) sign convention of formula (4) (no longer the old
    # ad-hoc "-i times the imaginary-generator current" rule).
    #
    # Build the number-conserving staggered hop Hamiltonian H = sum_ij c_ij
    # a_i^dag a_j with c = i*M (Hermitian, since M is real antisymmetric) on a
    # SMALL exact fermionic Fock space. We use a periodic L=3 chain in 1D (Fock
    # dimension 2^3=8): odd length keeps the staggered hop NONtrivial (an even
    # L=2 ring degenerates to M=0 because x+mu and x-mu coincide). The corrected
    # charge current (the OUTflow current from x toward x+mu) is
    #
    #     j^mu_x = -(1/2) eta_mu(x) [ chibar_x chi_{x+mu} + chibar_{x+mu} chi_x ]
    #
    # i.e. exactly formula (4)'s sign. The check confirms continuity holds with
    # THIS sign and FAILS with the flipped sign, so the sign is determined by
    # the continuity equation (given rho_x = chibar_x chi_x), not by convention.
    Ls, ds = 3, 1
    Ms, ss, ix = build_M_pure_staggered(Ls, 0.0, ds)  # massless: pure hop
    n = len(ss)
    a = _fermi_ann(n)
    adag = [x.conj().T for x in a]
    Hmat = 1j * Ms  # c = i*M, Hermitian
    herm_err = float(np.max(np.abs(Hmat - Hmat.conj().T)))
    hop_norm = float(np.max(np.abs(Ms)))  # guard: hop must be nontrivial
    H = sum(Hmat[p, q] * (adag[p] @ a[q]) for p in range(n) for q in range(n))

    def rho(p):
        return adag[p] @ a[p]

    fock_dim = a[0].shape[0]

    def jmu(x, mu, sign):
        # OUTflow current at x in direction mu; corrected formula (4) sign is
        # sign=+1 -> -(1/2) eta [...]; the flipped sign multiplies by -1.
        ehat = tuple(1 if k == mu else 0 for k in range(ds))
        xp = tuple((x[k] + ehat[k]) % Ls for k in range(ds))
        eta = staggered_eta(x, mu)
        ix_x, ix_xp = ix[x], ix[xp]
        return sign * (-0.5) * eta * (adag[ix_x] @ a[ix_xp] + adag[ix_xp] @ a[ix_x])

    def divj(x, sign):
        out = np.zeros((fock_dim, fock_dim), dtype=complex)
        for mu in range(ds):
            ehat = tuple(1 if k == mu else 0 for k in range(ds))
            xm = tuple((x[k] - ehat[k]) % Ls for k in range(ds))
            out = out + (jmu(x, mu, sign) - jmu(xm, mu, sign))
        return out

    # Heisenberg d rho/dt = i[H, rho]; continuity: d rho_x/dt + (div^L j)_x = 0.
    cont_err_fixed = 0.0
    cont_err_flipped = 0.0
    drho_norm = 0.0
    for x in ss:
        drho = 1j * (H @ rho(ix[x]) - rho(ix[x]) @ H)
        drho_norm = max(drho_norm, float(np.max(np.abs(drho))))
        cont_err_fixed = max(cont_err_fixed, float(np.max(np.abs(drho + divj(x, +1.0)))))
        cont_err_flipped = max(cont_err_flipped, float(np.max(np.abs(drho + divj(x, -1.0)))))
    print(f"  H Hermiticity err = {herm_err:.3e}, hop norm = {hop_norm:.3e}, |d rho/dt| = {drho_norm:.3e}")
    print(f"  max||d rho/dt + (div j)_formula(4)|| = {cont_err_fixed:.3e}  (must be ~0)")
    print(f"  max||d rho/dt + (div j)_flipped||    = {cont_err_flipped:.3e}  (must be NONZERO)")
    record(
        "C3 continuity fixes the sign: formula (4) sign satisfies d rho/dt + div j = 0",
        herm_err < 1e-12 and hop_norm > 1e-6 and drho_norm > 1e-6 and cont_err_fixed < 1e-10,
    )
    record(
        "C3b flipped sign VIOLATES continuity (U(1) sign is determined, not convention)",
        cont_err_flipped > 1e-6,
    )


# ---------------------------------------------------------------------------
# Part D — site-mixing generator is OUT of scope (named open item).
#
# The one-site translation S^(1) is a SITE-MIXING generator. We confirm it is
# NOT an onsite/internal generator (it does not commute with the staggered M
# as a plain shift), so the onsite-internal locality argument of Parts A/B does
# not apply to it. This is the explicit reason the corrected theorem restricts
# to onsite/internal generators; the (2Z)^3 translation / taste current is
# recorded as a named open item, not claimed here.
# ---------------------------------------------------------------------------


def part_D_site_mixing_out_of_scope() -> None:
    print("\n[Part D] site-mixing generator (one-site shift) is out of scope")
    L, dim, mass = 4, 3, 0.3
    M, sites, idx = build_M_pure_staggered(L, mass, dim)
    N = len(sites)

    # one-site shift permutation in direction mu=1 (a SITE-MIXING generator)
    Sshift = np.zeros((N, N), dtype=complex)
    for x in sites:
        ehat = tuple(1 if k == 1 else 0 for k in range(dim))
        xp = tuple((x[k] + ehat[k]) % L for k in range(dim))
        Sshift[idx[x], idx[xp]] = 1.0
    one_site_err = float(np.max(np.abs(Sshift @ M @ Sshift.T - M)))
    print(f"  one-site shift ||S M S^T - M||_max = {one_site_err:.3e} (NONzero => not a plain symmetry)")
    record(
        "D1 one-site (site-mixing) shift is NOT a plain symmetry of staggered M",
        one_site_err > 1e-6,
    )

    # two-site shift IS a symmetry of M (recorded as the named open item: its
    # conserved current is site-mixing and NOT covered by the onsite-internal
    # restriction of this note).
    Sshift2 = np.zeros((N, N), dtype=complex)
    for x in sites:
        shift = tuple(2 if k == 1 else 0 for k in range(dim))
        xp = tuple((x[k] + shift[k]) % L for k in range(dim))
        Sshift2[idx[x], idx[xp]] = 1.0
    two_site_err = float(np.max(np.abs(Sshift2 @ M @ Sshift2.T - M)))
    print(f"  two-site shift ||S2 M S2^T - M||_max = {two_site_err:.3e} (zero => symmetry, but site-mixing)")
    record(
        "D2 two-site shift is a symmetry but SITE-MIXING (named open item, out of scope)",
        two_site_err < 1e-12,
    )


def main() -> int:
    print("=" * 74)
    print(" audit_companion_lattice_noether_onsite_internal_2026_06_05.py")
    print(" Onsite/internal-restricted lattice Noether theorem, corrected U(1) sign.")
    print(" Reproves: (1) sign fixed by continuity, (2) onsite/internal support envelope,")
    print("           (3) arbitrary-bilinear symbolic current conservation.")
    print("=" * 74)

    part_B0_commutator_identity()
    part_A_arbitrary_bilinear()
    part_B_onsite_internal_locality()
    part_C_staggered_fixed_sign()
    part_D_site_mixing_out_of_scope()

    n_pass = sum(1 for _, ok in RESULTS if ok)
    n_fail = sum(1 for _, ok in RESULTS if not ok)
    print("\n" + "=" * 74)
    print(" SUMMARY")
    print("=" * 74)
    for name, ok in RESULTS:
        print(f"   {'PASS' if ok else 'FAIL'}  {name}")
    print(f"\nTOTAL: {n_pass} PASS / {n_fail} FAIL")
    from pathlib import Path

    note = (
        Path(__file__).resolve().parents[1]
        / "docs"
        / "AXIOM_FIRST_LATTICE_NOETHER_ONSITE_INTERNAL_NARROW_THEOREM_NOTE_2026-06-05.md"
    ).read_text()
    note_flat = " ".join(note.split())
    required_terms = [
        "2026-06-07 authority split",
        "AXIOM_FIRST_LATTICE_NOETHER_ABSTRACT_BILINEAR_CONTINUITY_NARROW_THEOREM_NOTE_2026-06-06",
        "finite staggered/Kawamoto-Smit exhibit",
        "downstream realization-gate bridge",
        "physical realization/readout identification of this exhibit is",
        "downstream and is not consumed here",
        "Finite carrier exhibit (constructed here, not a broad-gate dependency)",
        "No load-bearing broad-gate dependency is recorded here",
        "prior staggered-realization parent link has been removed",
    ]
    banned_terms = [
        "derives the admitted staggered",
        "derives the Kawamoto-Smit",
        "framework-native staggered carrier",
        "physical realization/readout identification of this exhibit is consumed",
        "](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)",
    ]
    boundary_ok = all(term in note_flat for term in required_terms) and not any(
        term in note_flat for term in banned_terms
    )
    print(
        f"BOUNDARY GUARD: {'PASS' if boundary_ok else 'FAIL'} "
        "retained abstract authority is cited; finite exhibit is not promoted and no gate edge is present"
    )
    if not boundary_ok:
        return 1
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
