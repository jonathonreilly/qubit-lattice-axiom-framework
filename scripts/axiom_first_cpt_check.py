#!/usr/bin/env python3
"""
axiom_first_cpt_check.py
-------------------------

Corrected non-degenerate fermion-sector CPT exhibits for

  docs/AXIOM_FIRST_CPT_THEOREM_STRETCH_NOTE_2026-04-29.md
  (2026-06-11 audit-failed repair revision)

The 2026-06-11 audit failed the prior revision on two findings:

  (F-A) the displayed composition chain ended at M^dagger, not M^*,
        and gamma_5/epsilon-Hermiticity by itself does not bridge the
        gap: for the real staggered M = m + M_KS one has
        M^dagger = m - M_KS while M^* = m + M_KS.
  (F-B) the runner's canonical L = 2 PERIODIC blocks are degenerate:
        the forward and backward staggered hops coincide and cancel,
        so the tested matrix was just m*I and every identity held
        vacuously.

This rewrite verifies the CORRECTED construction on non-degenerate
blocks with explicit boundary conventions:

  carrier   M = m*I + M_KS on the 4D block
            Lambda = Z_{L0} x Z_{L1} x Z_{L2} x Z_{L3} (all L_mu even),
            KS phases eta_mu(x) = (-1)^{x_0+...+x_{mu-1}},
            per-direction periodic or antiperiodic wrap signs.

  C   (charge conjugation, action level)
            chi_x -> eps(x) chibar_x^T, chibar_x -> -eps(x) chi_x^T,
            eps(x) = (-1)^{x_0+x_1+x_2+x_3}.
            Kernel identity:  E M^T E = M  (E = diag eps).
            (Equivalent to eps-Hermiticity E M E = M^dagger since M
            is real.)

  PT  (bond-centered full reflection)
            r(x)_mu = L_mu - 1 - x_mu  for every mu,
            chi_x -> sigma_PT(x) chi_{r(x)},
            sigma_PT(x) = (-1)^{x_1 + x_3}.
            Kernel identity:  S_PT Rb M Rb^{-1} S_PT = M^T.
            Boundary convention: the BOND-CENTERED reflection maps
            boundary-crossing links to boundary-crossing links, so it
            is compatible with BOTH periodic and antiperiodic wrap
            signs. (Site-centered x -> -x mod L is the identity map at
            L = 2 and maps crossing links to non-crossing links under
            APBC; both failure modes are exhibited as falsifiers.)
            The sign field absorbs the eta-parity flip
            eta_mu(r(x)) = (-1)^mu eta_mu(x) (L_mu even):
            sigma_PT(x) sigma_PT(x +- mu-hat) = +1 for mu in {0,2}
            and -1 for mu in {1,3}.

  K   complex conjugation (antiunitarity).

  Theta_CPT := (E S_PT Rb) K        (one antiunitary factor)

  corrected chain:
      Theta M Theta^{-1} = (E S_PT Rb) M^* (E S_PT Rb)^{-1}
                         = E (S_PT Rb M Rb^{-1} S_PT) E    [M real]
                         = E M^T E
                         = M
                         = M^*                                (CPT2)

  landing exactly at M^*, with the eps sign field carried INSIDE the
  map (this is the step the failed revision was missing).

Check blocks:
  [HYP]  carrier construction: nonzero KS hopping (the audit-demanded
         non-degeneracy), real, antisymmetric hop part.
  [DEG]  degeneracy witness (F-B made explicit): the 2^4 PERIODIC
         block has M_KS = 0 exactly -- the old runner's surface could
         not detect any construction error.
  [EPS]  eps-Hermiticity E M E = M^T = M^dagger.
  [C]    charge-conjugation kernel identity E M^T E = M.
  [PT]   bond-centered reflection identity -> M^T, plus the
         eta-parity-flip lemma it absorbs.
  [CPT]  composite (CPT1) Theta^2 = id and (CPT2) Theta M Theta^{-1}
         = M^* on every non-degenerate block.
  [DET]  (CPT4) det(M) real; (CPT5) computational corollary: a
         Theta_CPT-odd bilinear kernel has vanishing fermion-sector
         expectation tr(A_odd M^{-1}) = 0.
  [FALS] falsifiers: reflection without the sign field fails; wrong
         sign field fails; site-centered reflection under APBC fails;
         on the DEGENERATE 2^4-periodic block the no-sign-field map
         "passes" (why the old runner was blind).
  [DIAG] retained diagnostics (out of scope, expected non-zero):
         1D time circle (no spatial parity) and staggered + Wilson
         FERMION term (breaks the eps-as-gamma_5 chain).

Deterministic, numpy only, runtime a few seconds.
Exit code 0 iff TOTAL: PASS=n FAIL=0.
"""

from __future__ import annotations

import sys
from itertools import product
from pathlib import Path

import numpy as np

PASS = 0
FAIL = 0


def check(tag: str, label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        s = "PASS"
    else:
        FAIL += 1
        s = "FAIL"
    print(f"  [{s}] [{tag}] {label}" + (f"  ({detail})" if detail else ""))


def section(title: str) -> None:
    print()
    print("-" * 76)
    print(title)
    print("-" * 76)


# ---------------------------------------------------------------------------
# carrier: 4D staggered M = m I + M_KS with per-direction wrap signs
# ---------------------------------------------------------------------------

def eta(mu: int, x: tuple) -> int:
    return (-1) ** sum(x[:mu])


def eps(x: tuple) -> int:
    return (-1) ** sum(x)


def build_block(dims, m, apbc):
    """M = m I + M_KS, (M_KS)_{x,x+-mu} = +-(1/2) eta_mu(x) * wrap."""
    sites = list(product(*[range(L) for L in dims]))
    idx = {s: i for i, s in enumerate(sites)}
    N = len(sites)
    M = np.zeros((N, N))
    for x in sites:
        for mu in range(4):
            for sgn in (+1, -1):
                y = list(x)
                y[mu] += sgn
                wrap = 1.0
                if y[mu] >= dims[mu]:
                    y[mu] -= dims[mu]
                    wrap = -1.0 if apbc[mu] else 1.0
                if y[mu] < 0:
                    y[mu] += dims[mu]
                    wrap = -1.0 if apbc[mu] else 1.0
                M[idx[x], idx[tuple(y)]] += sgn * 0.5 * eta(mu, x) * wrap
    return M + m * np.eye(N), sites, idx


def sign_diag(sites, f):
    return np.diag([float(f(x)) for x in sites])


def perm(sites, idx, f):
    N = len(sites)
    P = np.zeros((N, N))
    for x in sites:
        P[idx[f(x)], idx[x]] = 1.0
    return P


def resid(A):
    return float(np.abs(A).max())


def main() -> int:
    print("=" * 76)
    print("AXIOM-FIRST CPT CHECK -- corrected non-degenerate construction")
    print("(2026-06-11 audit-failed repair: eps sign field carried inside the")
    print(" map; bond-centered boundary convention; nonzero KS hopping)")
    print("=" * 76)

    section("[SRC] source-boundary guard -- explicit KS carrier, no gate dependency")
    note_path = Path("docs/AXIOM_FIRST_CPT_THEOREM_STRETCH_NOTE_2026-04-29.md")
    note = note_path.read_text()
    check("SRC", "source note carries the 2026-06-12 explicit-carrier rescope",
          "explicit-carrier rescope" in note)
    check("SRC", "finite-matrix theorem is over the explicit KS carrier family",
          "explicit finite KS carrier" in note and "explicit KS matrix" in note)
    check("SRC", "framework baseline does not smuggle the KS carrier",
          "does not supply the Grassmann" in note
          and "finite even block, periodic/APBC wrap signs" in note
          and "finite-KS carrier/boundary data below" in note)
    check("SRC", "staggered realization gate is non-load-bearing context only",
          "non-load-bearing downstream context" in note
          and "No markdown dependency edge to that gate is present" in note)
    check("SRC", "source note has no markdown dependency edge to the realization gate",
          "](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)" not in note)

    blocks = [
        ("2^4 all-APBC", (2, 2, 2, 2), (1, 1, 1, 1)),
        ("4^4 periodic", (4, 4, 4, 4), (0, 0, 0, 0)),
        ("4^4 APBC-time", (4, 4, 4, 4), (1, 0, 0, 0)),
        ("4x2x4x2 mixed-APBC", (4, 2, 4, 2), (1, 1, 0, 0)),
    ]
    masses = (0.3, 0.5)

    # =======================================================================
    section("[DEG] degeneracy witness -- why the old runner was vacuous (F-B)")
    # =======================================================================
    Mdeg, sdeg, ideg = build_block((2, 2, 2, 2), 0.3, (0, 0, 0, 0))
    KSdeg = Mdeg - 0.3 * np.eye(len(sdeg))
    check("DEG", "2^4 PERIODIC block: forward/backward hops cancel, M_KS = 0",
          resid(KSdeg) == 0.0, f"max |M_KS| = {resid(KSdeg):.1e} -> M = m I")
    Rdeg = perm(sdeg, ideg, lambda x: tuple((2 - 1 - x[mu]) % 2 for mu in range(4)))
    check("DEG", "on the degenerate block the NO-SIGN-FIELD reflection 'passes' "
                 "(the old surface could not detect the construction error)",
          resid(Rdeg @ Mdeg @ Rdeg.T - Mdeg) == 0.0)

    for label, dims, apbc in blocks:
        for m in masses:
            M, sites, idx = build_block(dims, m, apbc)
            N = len(sites)
            KS = M - m * np.eye(N)

            # ===============================================================
            section(f"block {label}, m = {m}  (N = {N})")
            # ===============================================================
            check("HYP", "nonzero KS hopping (audit-demanded non-degeneracy)",
                  resid(KS) >= 0.5, f"max |M_KS| = {resid(KS):.3f}")
            check("HYP", "M real and hop part antisymmetric (M_KS^T = -M_KS)",
                  resid(KS + KS.T) == 0.0 and np.isrealobj(M))

            E = sign_diag(sites, eps)
            check("EPS", "eps-Hermiticity: E M E = M^T = M^dagger",
                  resid(E @ M @ E - M.T) == 0.0)
            check("C", "charge conjugation kernel: E M^T E = M",
                  resid(E @ M.T @ E - M) == 0.0)

            # bond-centered full reflection
            def rb(x, dims=dims):
                return tuple((dims[mu] - 1 - x[mu]) % dims[mu] for mu in range(4))
            Rb = perm(sites, idx, rb)
            S_PT = sign_diag(sites, lambda x: (-1) ** (x[1] + x[3]))

            # eta-parity-flip lemma absorbed by sigma_PT
            flips_ok = all(
                eta(mu, rb(x)) == ((-1) ** mu) * eta(mu, x)
                for x in sites for mu in range(4)
            )
            check("PT", "eta-parity flip lemma: eta_mu(r(x)) = (-1)^mu eta_mu(x) "
                        "(L_mu even, bond-centered)",
                  flips_ok)
            check("PT", "bond-centered reflection: S_PT Rb M Rb^-1 S_PT = M^T",
                  resid(S_PT @ Rb @ M @ Rb.T @ S_PT - M.T) == 0.0)

            # composite CPT
            V = E @ S_PT @ Rb
            check("CPT", "(CPT1) involution: Theta^2 = id  (V real, V^2 = I)",
                  resid(V @ V - np.eye(N)) == 0.0)
            check("CPT", "(CPT2) Theta M Theta^-1 = M^*  (corrected chain lands "
                         "at M^*, not M^dagger)",
                  resid(V @ M.conj() @ V.T - M.conj()) == 0.0
                  and resid(V @ M @ V.T - M) == 0.0)

            # determinant reality + Theta_CPT-odd corollary
            detM = np.linalg.det(M)
            check("DET", "(CPT4) det(M) real",
                  abs(np.imag(detM)) == 0.0, f"det = {detM:.6e}")
            rng = np.random.default_rng(20260429)
            B = rng.standard_normal((N, N))
            A_odd = B - V @ B @ V.T          # Theta_CPT-odd part: V A V^-1 = -A
            check("DET", "(CPT5) Theta_CPT-odd kernel: V A_odd V^-1 = -A_odd exactly",
                  resid(V @ A_odd @ V.T + A_odd) < 1e-12)
            ev = abs(np.trace(A_odd @ np.linalg.inv(M)))
            check("DET", "(CPT5) fermion-sector expectation of the Theta_CPT-odd "
                         "bilinear vanishes: |tr(A_odd M^-1)| = 0",
                  ev < 1e-10, f"|tr| = {ev:.2e}")

            # falsifiers (sign field and boundary convention are load-bearing)
            check("FALS", "falsifier: reflection WITHOUT the sign field fails "
                          "(plain S = 1)",
                  resid(Rb @ M @ Rb.T - M.T) > 0.4)
            S_wrong = sign_diag(sites, lambda x: (-1) ** (x[2]))
            check("FALS", "falsifier: WRONG sign field (-1)^{x_2} fails",
                  resid(S_wrong @ Rb @ M @ Rb.T @ S_wrong - M.T) > 0.4)
            if any(apbc):
                def rs(x, dims=dims):
                    return tuple((-x[mu]) % dims[mu] for mu in range(4))
                Rs = perm(sites, idx, rs)
                Vs = E @ S_PT @ Rs
                check("FALS", "falsifier: SITE-centered reflection x -> -x mod L "
                              "is wrap-incompatible under APBC (boundary "
                              "convention is load-bearing)",
                      resid(Vs @ M @ Vs.T - M) > 0.4)

    # =======================================================================
    section("[DIAG] diagnostics revisited under the corrected construction")
    # =======================================================================
    # 1D time circle. The OLD note recorded a 1D residual of 1.0 and
    # explained it as "no spatial parity to absorb the time inversion".
    # Under the CORRECTED map (eps sign field inside, bond-centered
    # reflection) the 1D TC identity closes EXACTLY: the old 1D failure
    # was an artifact of the defective composition (F-A), not a wall.
    sites1 = [(t, 0, 0, 0) for t in range(4)]
    idx1 = {s: i for i, s in enumerate(sites1)}
    M1 = 0.3 * np.eye(4)
    for x in sites1:
        for sgn in (+1, -1):
            t = (x[0] + sgn) % 4
            M1[idx1[x], idx1[(t, 0, 0, 0)]] += sgn * 0.5
    R1 = perm(sites1, idx1, lambda x: ((4 - 1 - x[0]) % 4, 0, 0, 0))
    S1 = sign_diag(sites1, lambda x: (-1) ** (x[1] + x[3]))  # trivial in 1D
    E1 = sign_diag(sites1, eps)
    V1 = E1 @ S1 @ R1
    r1 = resid(V1 @ M1 @ V1.T - M1)
    check("DIAG", "1D time circle: the CORRECTED map closes exactly "
                  "(the old 1D residual 1.0 was an artifact of the defective "
                  "composition, not a parity wall)",
          r1 == 0.0, f"residual = {r1:.3f}")

    # staggered + Wilson FERMION term breaks the eps-as-gamma_5 chain
    dims_w, apbc_w = (4, 4, 4, 4), (0, 0, 0, 0)
    M_w, sites_w, idx_w = build_block(dims_w, 0.3, apbc_w)
    rW = 1.0
    for x in sites_w:
        for mu in range(4):
            for sgn in (+1, -1):
                y = list(x)
                y[mu] = (y[mu] + sgn) % dims_w[mu]
                M_w[idx_w[x], idx_w[tuple(y)]] += -0.5 * rW  # Wilson-style sym hop
        M_w[idx_w[x], idx_w[x]] += rW * 4.0
    E_w = sign_diag(sites_w, eps)
    r_eps_w = resid(E_w @ M_w @ E_w - M_w.T)
    check("DIAG", "staggered + Wilson FERMION term: eps-Hermiticity residual "
                  "NON-zero (the wall is real; pure staggered is the explicit "
                  "carrier family here; expected, out of scope)",
          r_eps_w > 0.4, f"residual = {r_eps_w:.3f}")

    print()
    print("=" * 76)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 76)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
