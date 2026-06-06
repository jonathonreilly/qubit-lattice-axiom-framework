#!/usr/bin/env python3
"""Class-A verifier: the MAGNITUDE of the interaction asymmetry `delta` (hence of the emergent
C3 coupling |K|) is routed to the framework's MASSLESS-GRAVITY mediator IR scale -- the single open
gravity-scale derivation -- while its FORM is corner-protected and its real single-hop coupling is K-real.

Background (established in companion notes): delta is the two-fermion mutual energy of two hw=1
BZ-corner generations through the retained two-body mediator V(r) = -G (L+mu^2)^-1, with
  delta_ij = ( Vq(0) - Vq(k_i - k_j) ) / N,   Vq(q) = -G/(eps(q)+mu^2),   eps(Delta k)=8.

This runner pins where the *magnitude* lives:

  (1) The framework's gravity is MASSLESS (retained newton_law_derived: 1/r, inverse-square), so
      mu^2 is an IR regulator, not a physical mass. As mu^2 -> 0 the q=0 MONOPOLE -G/mu^2 is
      IR-divergent; the corner (Fock) part -Vq(Delta k) = G/(8+mu^2) -> G/8 is mu^2-INDEPENDENT
      (the IR-SAFE piece). So |delta| is set by the gravity mediator's IR scale (G, mu^2), not a
      localization distance => it routes to the open gravity-scale derivation.

  (2) The corner transfer eps(Delta k)=8 is identical for all three generation pairs at EVERY
      mu^2 => the C3 (J-I) FORM is corner-protected and IR-ROBUST (independent of the magnitude).

  (3) The emergent coupling is K-REAL: the second-order |K| is a real coefficient on
      J-I = C+C^2, i.e. it lies in the einselection sieve's K-real cone span_R{I, C+C^2}
      (retained flavor_einselection_2sector_modulo_kreality) => 2-sector-partition-compatible.
      (Shown for the real single-hop model; the full complex staggered-Dirac hopping is the open
      K-reality predicate. This does NOT deliver the value r=1/2 -- no overreach.)

  (4) The ordering argument is magnitude-insensitive only inside a supplied hierarchy window:
      the predictability sieve selects the pointer basis as the eigenbasis of the DOMINANT of
      {coupling |K|, sector mass M}. The selection flips on the |K|-vs-M ORDERING. The physical
      window remains a separate input surface.

By the scale-reference primitive (one dimensionful ruler, zero dimensionless content), the
physical magnitude of |delta| is exactly the kind of quantity the framework leaves to the open
gravity-scale derivation. This runner does not close that scale or add a flavor value.

No new axiom/import: massless gravity + the two-body mediator + the corner generations + the
einselection cone are cited in their own narrow roles; the IR structure and cone membership are exact arithmetic.
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


G = 50.0
CORNERS = {1: (np.pi, 0.0, 0.0), 2: (0.0, np.pi, 0.0), 3: (0.0, 0.0, np.pi)}
PAIRS = [(1, 2), (1, 3), (2, 3)]


def eps(q):
    return float(sum(2 * (1 - np.cos(qi)) for qi in q))


def Vq(epsq, mu2):
    return -G / (epsq + mu2)


def kron3(o, q):
    I2 = np.eye(2, dtype=complex)
    m = np.array([[1]], dtype=complex)
    for i in range(3):
        m = np.kron(m, o if i == q else I2)
    return m


def emergent_K(delta):
    """second-order C3 coupling on hw=1 sourced by an asymmetry delta (real single-hop model)."""
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    nup = np.array([[0, 0], [0, 1]], dtype=complex)
    hwv = np.array([bin(i).count("1") for i in range(8)])
    P1 = [i for i in range(8) if hwv[i] == 1]
    Vc = sum(kron3(sx, q) for q in range(3))
    nops = [kron3(nup, q) for q in range(3)]
    Hint = delta * sum(nops[i] @ nops[j] for i in range(3) for j in range(i + 1, 3))
    E = {i: hwv[i] * 1.0 + Hint[i, i].real for i in range(8)}
    E1 = E[P1[0]]
    return np.array([[sum(Vc[a, k] * Vc[k, b] / (E1 - E[k])
                          for k in range(8) if hwv[k] != 1 and abs(E1 - E[k]) > 1e-9)
                      for b in P1] for a in P1])


def main() -> int:
    print("=" * 78)
    print("delta MAGNITUDE routes to the massless-gravity IR scale; FORM robust  [class A]")
    print("=" * 78)

    # ---- (1) massless gravity: monopole IR-divergent, corner-Fock mu^2-independent (IR-safe) ----
    print("\n-- (1) massless gravity (mu^2->0): monopole diverges, corner-Fock G/8 is IR-safe --")
    monopole = [abs(Vq(0.0, mu2)) for mu2 in (1e-2, 1e-4, 1e-6)]
    check("the q=0 monopole |Vq(0)| = G/mu^2 DIVERGES as mu^2 -> 0 (massless-gravity IR scale)",
          monopole[2] > monopole[1] > monopole[0],
          detail=f"|Vq(0)|(mu2=1e-2,1e-4,1e-6) = {[f'{m:.1e}' for m in monopole]}")
    fock = [G / (8 + mu2) for mu2 in (1e-2, 1e-4, 1e-6)]
    check("the corner (Fock) part |Vq(Delta k)| = G/(8+mu^2) -> G/8 is mu^2-INDEPENDENT "
          "(the IR-SAFE piece)", np.allclose(fock, G / 8, atol=1e-2),
          detail=f"-> G/8 = {G/8:.4f}")

    # ---- (2) corner transfer eps(Delta k)=8 for all pairs at every mu^2 => J-I IR-robust ----
    print("\n-- (2) the J-I FORM is corner-protected and IR-robust --")
    eps_pairs = [eps(tuple(np.array(CORNERS[i]) - np.array(CORNERS[j]))) for i, j in PAIRS]
    check("eps(Delta k)=8 for all three generation pairs (mu^2-independent) => exact C3 (J-I) "
          "form is corner-protected, independent of the magnitude", np.allclose(eps_pairs, 8.0),
          detail=f"eps(Delta k) = {eps_pairs}")

    # ---- (3) the emergent |K| is K-real => 2-sector-partition-compatible ----
    print("\n-- (3) the emergent coupling is K-real (lies in the sieve's span_R{I, C+C^2}) --")
    C = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=float)
    J = np.ones((3, 3))
    check("the C3-invariant coupling J-I equals the einselection sieve's cone generator C+C^2",
          np.allclose(C + C @ C, J - np.eye(3)))
    for delta in (-0.4, +0.4):
        Hk = emergent_K(delta)
        a, k = Hk[0, 0].real, Hk[0, 1].real
        recon = a * np.eye(3) + k * (J - np.eye(3))
        is_kreal = np.max(np.abs(Hk.imag)) < 1e-12 and np.allclose(Hk.real, recon)
        check(f"delta={delta:+.1f}: the emergent |K| is K-REAL (real coeff on J-I=C+C^2 => "
              f"K-real cone => 2-sector partition)", is_kreal,
              detail=f"max|Im(K)|={np.max(np.abs(Hk.imag)):.0e}")

    # ---- (4) conditional hierarchy window: pointer = eigenbasis of the DOMINANT of {|K|, mass} ----
    print("\n-- (4) conditional hierarchy-window check (sieve selects by |K|-vs-mass order) --")
    def pointer_is_C3(absK, mass):
        # predictability sieve: pointer basis = eigenbasis of the dominant operator
        return absK > mass
    # This is a supplied hierarchy-window example, not a physical-window proof.
    window = [1e-3, 1e-1, 1e1, 1e3]   # |K| values spanning many orders
    m_nu, m_heavy = 1e-6, 1e6
    nu_C3 = all(pointer_is_C3(absK, m_nu) for absK in window)
    heavy_corner = all(not pointer_is_C3(absK, m_heavy) for absK in window)
    check("inside a supplied hierarchy window, the lightest sector is |K|-dominated "
          "and the heaviest is mass-dominated: the ordering argument is insensitive to the "
          "precise magnitude and sign of K in that window", nu_C3 and heavy_corner,
          detail=f"window spans {window[0]:.0e}..{window[-1]:.0e}; only the |K|-vs-mass ORDER matters")

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("VERDICT: delta-magnitude / gravity-scale reduction FAILED.")
        return 1
    print("VERDICT: the magnitude of delta/|K| routes to the framework's MASSLESS-GRAVITY "
          "mediator scale (the monopole is the IR-divergent gravity scale; the corner-Fock G/8 "
          "is IR-safe) = the single open gravity-scale derivation (scale-reference primitive); it "
          "does not close a flavor value. The C3 (J-I) FORM is corner-protected and "
          "IR-robust, the real single-hop emergent |K| is K-real, and a supplied hierarchy "
          "window can make the pointer-ordering argument insensitive to the precise magnitude. "
          "No flavor value (r, Q) is forced.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
