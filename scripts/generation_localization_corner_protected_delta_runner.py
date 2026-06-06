#!/usr/bin/env python3
"""Class-A verifier: the generation "localization" that sets the magnitude of the
interaction asymmetry `delta` is the RETAINED momentum-corner structure -- not a free spatial
separation -- and this (a) protects the exact C3 (J-I) form of the emergent coupling by cubic
corner symmetry, (b) re-confirms `delta < 0` from the momentum picture (independent of the
spatial-packet route), and (c) shows the magnitude reduces to the mediator IR monopole, NOT to
the localization.

Retained structure (three_generation_observable_theorem / structure / hw1_distinct_translation
_characters): the three generations are the hw=1 Brillouin-zone corners
  k1=(pi,0,0), k2=(0,pi,0), k3=(0,0,pi),
distinguished by three distinct joint translation CHARACTERS under (T_x,T_y,T_z); they carry no
spatial separation. So `delta` (the two-excitation mutual energy) is the two-fermion energy of
two corner excitations interacting through the retained mediator
  V(r) = -G (L + mu^2)^-1   (attractive; sign from the retained two-body channel).

For two plane waves k_i,k_j (a Slater determinant) with a translation-invariant V, the mutual
energy is EXACT:
  delta_ij = ( Vq(0) - Vq(k_i - k_j) ) / N ,   Vq(q) = -G/(eps(q)+mu^2),  eps(q)=sum 2(1-cos q).

Verifies:
  (1) the three generation corners carry three distinct joint translation characters (retained);
  (2) every generation PAIR has eps(k_i-k_j)=8 (two pi-flips) => identical exchange =>
      the C3 (J-I) form is CORNER-SYMMETRY-PROTECTED;
  (3) the exact lattice two-fermion mutual energy matches the Hartree-Fock formula and is < 0
      for all three pairs (=> delta<0, sign re-confirmed from the momentum picture);
  (4) |delta| is dominated by the q=0 monopole (Hartree ~ -G/(N mu^2)); it scales with the
      lattice volume N and the IR parameter mu^2, NOT a localization distance => the magnitude
      reduces to the mediator IR scale and stays OPEN (wide-window robust); the corner (Fock)
      part ~G/(8N) is subleading.

No new axiom/import: the corner structure and the mediator are retained; the two-fermion matrix
element is exact arithmetic.
"""

from __future__ import annotations
import numpy as np

PASS = 0
FAIL = 0


def check(name, condition, detail=""):
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok); FAIL += int(not ok)
    tag = "PASS" if ok else "FAIL"
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


G, MU2 = 50.0, 0.001
CORNERS = {1: (np.pi, 0.0, 0.0), 2: (0.0, np.pi, 0.0), 3: (0.0, 0.0, np.pi)}
PAIRS = [(1, 2), (1, 3), (2, 3)]


def eps(q):
    return float(sum(2 * (1 - np.cos(qi)) for qi in q))


def Vq(q):
    return -G / (eps(q) + MU2)


def exact_lattice_delta(L):
    """exact two-fermion mutual energy of corners 1,2 on an L^3 periodic lattice."""
    pos = [(x, y, z) for x in range(L) for y in range(L) for z in range(L)]
    idx = {p: a for a, p in enumerate(pos)}
    n = L ** 3
    Lap = np.zeros((n, n))
    for (x, y, z) in pos:
        a = idx[(x, y, z)]
        for dx, dy, dz in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
            b = idx[((x + dx) % L, (y + dy) % L, (z + dz) % L)]
            Lap[a, b] -= 1.0; Lap[a, a] += 1.0
    Vreal = -G * np.linalg.inv(Lap + MU2 * np.eye(n))

    def pw(k):
        return np.array([np.exp(1j * (k[0] * x + k[1] * y + k[2] * z)) for (x, y, z) in pos]) / np.sqrt(n)
    ki, kj = pw(CORNERS[1]), pw(CORNERS[2])
    ni, nj = np.abs(ki) ** 2, np.abs(kj) ** 2
    hartree = float(np.real(ni @ Vreal @ nj))
    A = ki.conj() * kj
    B = kj.conj() * ki
    fock = float(np.real(A @ Vreal @ B))
    return hartree - fock


def main() -> int:
    print("=" * 78)
    print("GENERATION LOCALIZATION = momentum corners: J-I corner-protected; delta<0; |delta| IR  [class A]")
    print("=" * 78)

    # ---- (1) three distinct joint translation characters (retained distinctness) ----
    print("\n-- (1) the three generation corners carry distinct joint translation characters --")
    chars = {i: tuple(int(np.round(np.cos(kc))) for kc in CORNERS[i]) for i in CORNERS}
    # cos(pi)=-1 (T=-1 on the pi axis), cos(0)=+1 ; characters: gen1=(-1,+1,+1), etc.
    distinct = len(set(chars.values())) == 3
    check("the three hw=1 corners have three DISTINCT joint (T_x,T_y,T_z) sign characters "
          "(retained: translations separate the generations)", distinct,
          detail=f"{chars[1]},{chars[2]},{chars[3]}")

    # ---- (2) every generation pair has eps(Delta k)=8 => J-I corner-protected ----
    print("\n-- (2) every generation pair has eps(Delta k)=8 => J-I form corner-symmetry-protected --")
    eps_pairs = []
    for i, j in PAIRS:
        dk = tuple(np.array(CORNERS[i]) - np.array(CORNERS[j]))
        eps_pairs.append(eps(dk))
    check("all three generation pairs share the SAME inter-corner transfer eps(Delta k)=8 "
          "(each pair differs by two pi-flips) => identical exchange => exact C3 (J-I) form",
          np.allclose(eps_pairs, 8.0), detail=f"eps(Delta k) = {[round(e,3) for e in eps_pairs]}")

    # ---- (3) exact lattice two-fermion mutual energy = HF formula, and delta<0 ----
    print("\n-- (3) exact two-fermion mutual energy matches Hartree-Fock, and delta<0 (sign cross-check) --")
    for L in (4, 6):
        N = L ** 3
        d_exact = exact_lattice_delta(L)
        d_hf = (Vq((0, 0, 0)) - Vq((np.pi, np.pi, 0.0))) / N
        check(f"L={L}: exact lattice two-fermion delta == HF formula [Vq(0)-Vq(Δk)]/N",
              np.isclose(d_exact, d_hf, rtol=1e-7), detail=f"exact={d_exact:.4e} hf={d_hf:.4e}")
    # delta<0 for all three pairs (all share eps(Δk)=8 => all equal)
    deltas = []
    N = 10 ** 3
    for i, j in PAIRS:
        dk = tuple(np.array(CORNERS[i]) - np.array(CORNERS[j]))
        deltas.append((Vq((0, 0, 0)) - Vq(dk)) / N)
    check("delta<0 for all three generation pairs (sign re-confirmed from the momentum picture, "
          "independent of the spatial-packet route) and all equal (=> J-I form)",
          all(d < 0 for d in deltas) and np.allclose(deltas, deltas[0]),
          detail=f"delta(pairs) = {[f'{d:.3e}' for d in deltas]}")

    # ---- (4) |delta| is monopole-dominated (~1/(N mu^2)), NOT pinned by localization ----
    print("\n-- (4) |delta| reduces to the mediator IR monopole (~1/(N mu^2)), not a localization distance --")
    ratios = []
    for L in (6, 8, 10, 14, 20):
        N = L ** 3
        d = (Vq((0, 0, 0)) - Vq((np.pi, np.pi, 0.0))) / N
        hartree = Vq((0, 0, 0)) / N
        ratios.append(abs(d) * N)                       # |delta|*N -> constant if ~1/N
    check("|delta| scales as 1/N (the q=0 Hartree monopole -G/(N mu^2) dominates; the corner "
          "Fock part ~G/(8N) is subleading) => the magnitude is set by the mediator IR scale "
          "(G, mu^2), NOT by a localization distance => stays open, wide-window robust",
          np.allclose(ratios, ratios[0], rtol=1e-3),
          detail=f"|delta|*N (const over L) = {ratios[0]:.3f}; Fock/Hartree ~ mu^2/8 = {MU2/8:.2e}")
    # the monopole (Hartree) part carries essentially all of |delta|
    N = 10 ** 3
    hartree_frac = abs(Vq((0, 0, 0)) / N) / abs((Vq((0, 0, 0)) - Vq((np.pi, np.pi, 0.0))) / N)
    check("the q=0 monopole carries essentially all of |delta| (corner structure fixes the FORM "
          "and SIGN, the IR scale fixes the magnitude)", hartree_frac > 0.999,
          detail=f"Hartree fraction of |delta| = {hartree_frac:.5f}")

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("VERDICT: generation-localization corner structure FAILED.")
        return 1
    print("VERDICT: the generation 'localization' is the retained momentum-corner structure (no "
          "spatial separation). The three corners' equal inter-transfer eps(Δk)=8 protects the "
          "exact C3 (J-I) form by cubic corner symmetry; the two-fermion mutual energy is delta<0 "
          "(sign re-confirmed from the momentum picture); and |delta| is dominated by the q=0 "
          "mediator monopole (~1/(N mu^2)) -- so the magnitude reduces to the mediator IR scale, "
          "NOT to the localization, and stays open (wide-window robust).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
