#!/usr/bin/env python3
"""The orientation label on the minimal e_4 carrier is net-zero / isospectral /
NON-SELECTING: an injected arrow does not produce a gauge-invariant sign -- concretely
exhibiting why the gravity sign is not derived (it is unobservable in the spectrum).

Loop iteration 2 (the sharpest next artifact from the orientation-reduction
adjudication): does append-only record accumulation orient the e_4 volume form, forcing
one element of the derived [+1,-1] pair? Tested on the minimal native carrier -- a 1D
Dirac/SSH boundary ring in the e_4 (time/append) direction -- via the standard
Jackiw-Rebbi/SSH soliton, with chirality extracted by projecting Gamma5 onto the
near-zero subspace (required: a naive per-eigenvector read returns a hybridized ~0 under
the zero-mode degeneracy). The honest finding is a NON-selection:

  N0  PURE STAGGERED (parity-odd, no defect): Gamma5 H Gamma5 = -H => +/- symmetric
      spectrum => spectral asymmetry eta = 0. The label is undefined -- reproducing the
      landed KODD_PFAFFIAN_LINE_BUNDLE trivial +1 / empty crossing set.
  A1  DEFECT (dimerization kink-antikink, "arrow" s = delta -> -delta): a domain wall
      binds a Jackiw-Rebbi chiral zero mode; the kink and antikink carry OPPOSITE Gamma5
      chirality (+/-1); the gauge-invariant NET near-zero chirality is identically 0 for
      BOTH arrow values. The "arrow" s = delta->-delta is exactly the SSH kink<->antikink
      swap, so injecting s merely RELABELS which defect is the kink -- the local chirality
      at a fixed position flips with s, but the SAME flip is produced at fixed s by reading
      the other defect. s selects no gauge-invariant observable.
  D1  DISCRIMINATOR: a uniformly dimerized ring (parity-odd, gapped, NO domain wall) binds
      NO mid-gap mode. So a domain WALL is required to bind a chiral mode -- the standard
      Jackiw-Rebbi dichotomy. (This isolates "you need a wall," not "orientation selects a
      branch": both arrows are net-zero and isospectral.)
  R1  NON-SELECTION: the two arrow directions are ISOSPECTRAL and net-zero -- nothing in
      the spectrum/energetics selects s. The arrow direction is the append-only /
      low-record-boundary existence input (the Past-Hypothesis residual / directionless
      Stone clock), so the gravity sign REDUCES to the arrow; it is NOT derived.

This is a CONSISTENCY picture for the reduction, not an independent proof of it: the
gravity<->orientation weld itself rests on the exact Cl(3,1) e_4 identity in the companion
runner (frontier_gravity_sign_reduces_to_shared_orientation_datum). Here we only exhibit,
on the minimal carrier, that the orientation label carries no gauge-invariant sign -- so
the selection must be an external admitted datum. The absolute chirality sign is itself
convention-dependent (A/B sublattice + kink-sign labeling); only the relative flip and the
net-zero / isospectral non-selection are convention-free. Deterministic, exact
diagonalization of small (<= 200x200) Hermitian rings -- memory-safe, no MC.
"""

from __future__ import annotations

import numpy as np

PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if cond else "FAIL"
    if cond:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{tag}] {name}" + (f" :: {detail}" if detail else ""))


# ---------------------------------------------------------------------------
# 1D Dirac/SSH boundary RING (periodic) in the e_4 (time/append) direction.
# Gamma5 = diag(+1,-1) sublattice grading. All hoppings off-diagonal => H anticommutes
# with Gamma5 (parity-odd) for ANY dimerization. The "mass" is the dimerization; an
# orientation reversal (kink) is the Jackiw-Rebbi/SSH soliton.
# ---------------------------------------------------------------------------
def gamma5(L: int) -> np.ndarray:
    g = np.zeros((2 * L, 2 * L))
    for n in range(L):
        g[2 * n, 2 * n] = +1.0
        g[2 * n + 1, 2 * n + 1] = -1.0
    return g


def site_positions(L: int) -> np.ndarray:
    return np.array([n for n in range(L) for _ in range(2)], dtype=float)


def dimerized_ring(L: int, delta: np.ndarray) -> np.ndarray:
    """Periodic SSH ring: intra-cell bond A_n-B_n = 1+delta_n, inter-cell B_n-A_{n+1 mod L}
    = 1-delta_n. Purely off-diagonal => {Gamma5, H} = 0 (parity-odd) for any delta."""
    H = np.zeros((2 * L, 2 * L), dtype=float)
    for n in range(L):
        a, b = 2 * n, 2 * n + 1
        H[a, b] = H[b, a] = 1.0 + delta[n]
        a2 = 2 * ((n + 1) % L)
        H[b, a2] = H[a2, b] = 1.0 - delta[n]
    return H


def uniform_ring(L: int, delta0: float = 0.0) -> np.ndarray:
    return dimerized_ring(L, np.full(L, delta0))


def kink_antikink_delta(L: int, d0: float, s: int, width: float = 3.0) -> np.ndarray:
    """Dimerization = +d0 on one arc, -d0 on the other, with a kink at L/4 and an antikink
    at 3L/4 (a ring carries walls in pairs). The "arrow" s = +/-1 sets delta -> s*delta,
    i.e. it is the SSH kink<->antikink swap (chiral/sublattice conjugation)."""
    q1, q3 = L / 4.0, 3.0 * L / 4.0
    delta = np.array([s * d0 * (np.tanh((n - q1) / width)
                                - np.tanh((n - q3) / width) - 1.0)
                      for n in range(L)])
    return dimerized_ring(L, delta)


def spectral_asymmetry(H: np.ndarray, tol: float = 1e-9) -> float:
    ev = np.linalg.eigvalsh(H)
    return float(np.sum(np.sign(ev[np.abs(ev) > tol])))


def near_zero_chiralities(H: np.ndarray, G: np.ndarray, L: int, gap: float = 0.25):
    """Diagonalize Gamma5 on the near-zero subspace (robust to degeneracy). Returns a
    list of (chirality, center_of_mass) for the chirality eigenstates."""
    ev, evec = np.linalg.eigh(H)
    idx = [k for k in range(len(ev)) if abs(ev[k]) < gap]
    if not idx:
        return []
    V = evec[:, idx]
    g_sub = V.conj().T @ G @ V
    cvals, cvec = np.linalg.eigh(g_sub)
    states = V @ cvec
    pos = site_positions(L)
    out = []
    for j in range(states.shape[1]):
        psi = states[:, j]
        prob = np.abs(psi) ** 2
        com = float(np.sum(prob * pos) / np.sum(prob))
        out.append((float(cvals[j]), com))
    return out


def chirality_at(H: np.ndarray, G: np.ndarray, L: int, q: float,
                 gap: float = 0.25) -> float:
    chir = near_zero_chiralities(H, G, L, gap)
    if not chir:
        return 0.0
    chir.sort(key=lambda cz: abs(cz[1] - q))
    return chir[0][0]


def block_null_no_arrow() -> None:
    print("\n== N0: pure staggered ring (no defect) => eta = 0 (the landed null label) ==")
    L = 40
    H = uniform_ring(L, 0.0)
    G = gamma5(L)
    parity_odd = np.allclose(G @ H @ G, -H)
    ev = np.linalg.eigvalsh(H)
    sym = np.allclose(np.sort(ev), -np.sort(ev)[::-1])
    eta = spectral_asymmetry(H)
    check("Gamma5 H Gamma5 = -H (uniform staggered ring is parity-odd)", parity_odd)
    check("=> +/- symmetric spectrum => eta = 0 (matches KODD trivial +1 / empty crossing)",
          sym and np.isclose(eta, 0.0), f"eta = {eta:.1f}")


def block_jackiw_rebbi_nonselection() -> None:
    print("\n== A1: domain wall binds a JR chiral mode; kink & antikink carry OPPOSITE "
          "chirality; NET label = 0 (the arrow selects no gauge-invariant observable) ==")
    L = 40
    G = gamma5(L)
    q1, q3 = L / 4.0, 3.0 * L / 4.0
    nets, q1s, q3s = {}, {}, {}
    for s in (+1, -1):
        H = kink_antikink_delta(L, d0=0.5, s=s)
        modes = near_zero_chiralities(H, G, L)
        nets[s] = sum(c for c, _ in modes)
        q1s[s] = chirality_at(H, G, L, q1)
        q3s[s] = chirality_at(H, G, L, q3)
        print(f"   arrow s={s:+d}: near-zero (chir,COM)="
              f"{[(round(c,2),round(x,1)) for c,x in modes]}  NET={nets[s]:+.2f}")
    # Each defect binds a chiral mode of definite +/-1; the two defects are opposite.
    check("a domain wall binds a Jackiw-Rebbi chiral mode (|chirality| = 1 at each defect)",
          all(np.isclose(abs(v), 1.0, atol=1e-3) for v in
              [q1s[+1], q3s[+1], q1s[-1], q3s[-1]]))
    check("kink and antikink carry OPPOSITE chirality (chi(q1) = -chi(q3) at fixed arrow)",
          np.isclose(q1s[+1], -q3s[+1], atol=1e-3))
    # The gauge-invariant net label is 0 for BOTH arrows -> no selection.
    check("the NET near-zero chirality = 0 for BOTH arrow directions (a kink+antikink pair "
          "carries no net orientation) => the arrow selects NO gauge-invariant observable",
          np.isclose(nets[+1], 0.0, atol=1e-6) and np.isclose(nets[-1], 0.0, atol=1e-6),
          f"NET(+)={nets[+1]:+.2f}, NET(-)={nets[-1]:+.2f}")
    # Injecting s flips the LOCAL chirality at a fixed position -- but the SAME flip is
    # produced at FIXED arrow by reading the other defect, so it is a relabeling, not a
    # selection.
    check("injecting s merely RELABELS which defect is the kink: chi(q1) flips with s, and "
          "the identical flip is produced at FIXED s by reading q3 instead of q1",
          np.isclose(q1s[-1], -q1s[+1], atol=1e-3)
          and np.isclose(q1s[-1], q3s[+1], atol=1e-3),
          f"chi_q1(+)={q1s[+1]:+.1f}, chi_q1(-)={q1s[-1]:+.1f}, chi_q3(+)={q3s[+1]:+.1f}")


def block_discriminator() -> None:
    print("\n== D1: uniformly dimerized ring (parity-odd, no wall) binds NO mid-gap mode ==")
    L = 40
    G = gamma5(L)
    H = uniform_ring(L, 0.5)                 # gapped, dimerized, NO orientation reversal
    parity_odd = np.allclose(G @ H @ G, -H)
    chir_modes = near_zero_chiralities(H, G, L)
    gap = float(np.min(np.abs(np.linalg.eigvalsh(H))))
    check("uniformly dimerized ring is parity-odd (Gamma5 H Gamma5 = -H) and gapped",
          parity_odd and gap > 0.2, f"min|E| = {gap:.3f}")
    check("=> NO mid-gap mode: a domain WALL is required to bind a chiral mode (the "
          "standard Jackiw-Rebbi dichotomy; this isolates 'you need a wall', not selection)",
          len(chir_modes) == 0, f"near-zero modes = {len(chir_modes)}")


def block_residual_statement() -> None:
    print("\n== R1: the two arrows are isospectral & net-zero => the arrow is the admitted "
          "residual (not derived) ==")
    L = 40
    Hp = kink_antikink_delta(L, 0.5, +1)
    Hm = kink_antikink_delta(L, 0.5, -1)
    iso = np.allclose(np.sort(np.linalg.eigvalsh(Hp)),
                      np.sort(np.linalg.eigvalsh(Hm)))
    check("the two arrow directions are ISOSPECTRAL (no energetic/spectral datum selects s) "
          "=> the selection IS the admitted arrow / Past-Hypothesis residual, not a derivation",
          iso)


def main() -> int:
    print("FRONTIER iter-2 (consistency picture): on the minimal e_4 carrier the orientation "
          "label is net-zero / isospectral / NON-SELECTING -- exhibiting why the gravity sign "
          "is not derived (no gauge-invariant sign); the weld rests on the companion runner.")
    block_null_no_arrow()
    block_jackiw_rebbi_nonselection()
    block_discriminator()
    block_residual_statement()
    print(f"\n==== {PASS} passed, {FAIL} failed ====")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
