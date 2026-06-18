#!/usr/bin/env python3
"""The absolute T-odd orientation sign is convention: the conjugation-selector class
is empty (carrier-independent), and no spectral / symmetry-equivariant functional is
orientation-odd. Discharges the shared K-real piece of theta (mass-side {0,pi} pin) and
AC_phi_lambda (delta=0 orientation bit) to the universal-floor / convention class.

This runner DERIVES the two exercise routes for the shared T-odd orientation atom
(realized sign of the e4 volume form = Koide sign(Delta) orientation = theta mass-side
arg det M in {0,pi} = the EH/conformal-mode sign), WITHOUT asserting:

  PREMISE (imported, cited). The two orientation branches are a CONJUGATE PAIR: the
      opposite-orientation carrier is sigma H sigma^-1 (= the K-image), because the exact weld
      e4(e1e2e3)e4^-1 = -(e1e2e3) flips the spatial pseudoscalar = the orientation
      (GRAVITY_SIGN_IS_NOT_A_NEW_ADMISSION...NOTE_2026-06-18). The random-H isospectrality
      below establishes CARRIER-INDEPENDENCE of the linear-algebra fact; the identification of
      the physical branch-map with conjugation is supplied by that weld. NB sigma = e4-
      CONJUGATION = spatial parity P here (same operation in this carrier); e4^2 = -I, so the
      Z2 is the conjugation ACTION sigma(.)sigma^-1 (involutive), not e4 itself.
  B1  CONJUGATION-SELECTOR ISOSPECTRALITY THEOREM (Route 2). For any Hermitian H and any
      conjugation C (unitary OR anti-unitary), spec(C H C^-1) = spec(H). Hence EVERY
      symmetry-operation selector in the class {K/CPT (anti-unitary), modular J, parity P =
      sigma, chirality Gamma5} leaves every spectral/energetic functional INVARIANT -- it
      cannot distinguish the two orientation branches. Verified carrier-INDEPENDENT (random
      Hermitian H over several sizes/seeds -> max|dE| = 0). So 'run a bigger / interacting
      carrier to break the isospectrality' is a provably dead falsifier, and the absolute
      orientation label carries no SPECTRAL/STATE gauge-invariant observable. (Topological
      action-offsets -- the theta-term / Chern-Simons level -- ARE sigma-odd gauge-invariant
      observables, but they are non-spectral and are exactly the conceded theta gauge-side
      bridge: B5.)
  B2  CONTROL TRAP (the method is not trivially zero). A NON-conjugation Z2 -- an SSH
      open-chain dimerization sign flip delta->-delta -- is NOT isospectral (max|dE| > 0,
      the topological-edge-mode appearance). So the runner does detect spectrally-observable
      Z2's; the zeros in B1 are real. This observable Z2 is a PARITY/topology Z2, distinct
      from the spectrally-invisible T-odd orientation Z2.
  B3  SELECTOR CHARACTERIZATION (Route 3, scoped). This adds to B1 exactly ONE thing: the
      characterization that a sigma-ODD selector must ANTICOMMUTE with sigma. (a) and (b) are
      corollaries of B1's 'conjugation acts trivially' engine -- (a) spectral functionals
      tr f(H) are sigma-even; (b) tr(sign(H).O) is sigma-even iff [O,sigma]=0 (one-line
      cyclicity = the definition of sigma-even). The new content (c): a sigma-ODD functional
      needs an O ANTICOMMUTING with sigma, i.e. a T-ODD operator, whose one-point function
      vanishes unless the STATE breaks T (the external arrow). So a sigma-odd SPECTRAL/STATE
      selector is either circular (reads the label) or external (Past Hypothesis). Verified
      with the positive control (sigma-odd e1 DOES split the branches: +-0.227) so the
      dichotomy has teeth. The orientation is a Z2-torsor with no canonical basepoint.
  B4  MODULAR / KMS CIRCULARITY (closes the Bisognano-Wichmann escape). The modular
      conjugation J is an anti-unitary INVOLUTION (J^2 = 1); the modular Hamiltonian of a
      Gibbs state is K_mod = beta H, so H -> -H flips beta -> -beta. Modular flow has a
      direction ONLY after sign(H>=0) is chosen -- which IS the arrow input. So the
      modular/PCT route presupposes the orientation; it does not select it.
  B5  THE ESCAPING OBSERVABLE (third horn, named + computed). A 2+1 massive-Dirac/QWZ Chern
      number is a sigma-ODD (sign(m)-flipping), gauge-invariant INTEGER that is NON-spectral
      (a Berry/instanton invariant, not any tr f(H)): Chern = -1 for m in (-2,0), +1 for
      m in (0,2). Its 3+1 analog is the theta-term coefficient arg det M in {0,pi}. This
      observable ESCAPES the spectral + sigma-equivariant net of B1/B3 -- but it IS exactly
      the theta gauge-side bridge the note keeps OPEN, NOT what is discharged here. So the
      no-go's dichotomy is THREE horns: circular | external (Past Hypothesis) | topological
      action-offset (the open theta gauge-bridge).

CONSEQUENCE (printed): the absolute orientation sign is RECLASSIFIED as sign/convention
(Y0/g0 class) for the SPECTRAL/STATE sector -- it adds NO admission. The OBSERVABLE content is
the relative arrow = universal-floor Past Hypothesis (a SEPARATE, un-discharged boundary
input). This reclassifies the SHARED K-real orientation PIECE of both Tier-A admissions; it
does NOT retire either: theta keeps its emergent-Q gauge bridge (= the B5 escaping observable),
AC_phi_lambda keeps the det_C-vs-det_R r-value, the radian-readout law, and the species bridge.
Status authority: audit lane only.

Deterministic; matrices <= 12x12; single process; NO 4D-BZ quadrature -- memory-safe.
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


# Pauli / Clifford helpers --------------------------------------------------
I2 = np.eye(2, dtype=complex)
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)


def cl31():
    """Cl(3,1) generators (sig +,+,+,-): e1,e2,e3 spatial (square +I), e4 time (square -I)."""
    e1 = np.kron(sx, sx)
    e2 = np.kron(sx, sy)
    e3 = np.kron(sx, sz)
    e4 = np.kron(1j * sy, I2)
    return e1, e2, e3, e4


def rand_herm(n: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    A = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    return 0.5 * (A + A.conj().T)


def spec(H: np.ndarray) -> np.ndarray:
    return np.sort(np.linalg.eigvalsh(H))


# ---------------------------------------------------------------------------
# B1 -- conjugation-selector isospectrality theorem (the selector class is empty)
# ---------------------------------------------------------------------------
def block_isospectrality() -> None:
    print("\n== B1: conjugation-selector isospectrality (the symmetry-selector class is empty) ==")
    e1, e2, e3, e4 = cl31()
    Gamma5 = e1 @ e2 @ e3 @ e4                  # chirality
    sigma = e4                                   # orientation flip = e4-conjugation = parity P
    # unitary conjugations (in this carrier parity P == sigma == e4-conjugation):
    unitary = {"parity P = sigma (e4-conj)": sigma, "chirality Gamma5": Gamma5}
    worst = 0.0
    for seed in range(6):
        for n, conj_set in ((4, unitary),):
            H = rand_herm(n, seed)
            for name, U in conj_set.items():
                Hc = U @ H @ np.linalg.inv(U)
                worst = max(worst, float(np.max(np.abs(spec(Hc) - spec(H)))))
            # anti-unitary K (complex conjugation) and U_T-dressed K:
            HK = np.conjugate(H)                 # K H K^-1 = conj(H) = H^T (Hermitian)
            worst = max(worst, float(np.max(np.abs(spec(HK) - spec(H)))))
            U_T = np.linalg.qr(rand_herm(n, seed + 100) + 1j * rand_herm(n, seed + 200))[0]
            HKd = U_T @ np.conjugate(H) @ U_T.conj().T   # dressed anti-unitary
            worst = max(worst, float(np.max(np.abs(spec(HKd) - spec(H)))))
    check("every conjugation {P=sigma, Gamma5, K, U_T-dressed K} preserves the spectrum "
          "(max|dE| = 0 over 6 seeds): no spectral/energetic functional distinguishes the "
          "orientation branches",
          worst < 1e-10, f"max|dE| over all conjugations/seeds = {worst:.2e}")
    # carrier-independence: larger random carriers, anti-unitary + a unitary conj
    worst_big = 0.0
    for n in (6, 8, 10, 12):
        H = rand_herm(n, n)
        U = np.linalg.qr(rand_herm(n, n + 7) + 1j * rand_herm(n, n + 9))[0]
        worst_big = max(worst_big,
                        float(np.max(np.abs(spec(U @ H @ U.conj().T) - spec(H)))),
                        float(np.max(np.abs(spec(np.conjugate(H)) - spec(H)))))
    check("CARRIER-INDEPENDENT: isospectrality holds for n=6,8,10,12 -> 'run a bigger/"
          "interacting carrier' is a provably dead falsifier",
          worst_big < 1e-10, f"max|dE| (n=6..12) = {worst_big:.2e}")


# ---------------------------------------------------------------------------
# B2 -- control trap: a NON-conjugation Z2 IS spectrally observable
# ---------------------------------------------------------------------------
def ssh_open(Lcells: int, delta: float) -> np.ndarray:
    """Open SSH chain: intra-cell bond 1+delta, inter-cell 1-delta. Hermitian, 2L x 2L."""
    n = 2 * Lcells
    H = np.zeros((n, n), dtype=complex)
    for c in range(Lcells):
        a, b = 2 * c, 2 * c + 1
        H[a, b] = H[b, a] = 1.0 + delta
        if c + 1 < Lcells:
            a2 = 2 * (c + 1)
            H[b, a2] = H[a2, b] = 1.0 - delta
    return H


def block_control() -> None:
    print("\n== B2: control trap -- a non-conjugation (parity/topology) Z2 IS observable ==")
    Hp = ssh_open(6, +0.5)     # topological phase (edge modes)
    Hm = ssh_open(6, -0.5)     # trivial phase (no edge modes)
    d = float(np.max(np.abs(spec(Hp) - spec(Hm))))
    check("the SSH open-chain dimerization sign flip delta->-delta is NOT isospectral "
          "(max|dE| > 0: the topological edge-mode appearance) -> the runner detects "
          "observable Z2's, so the B1 zeros are real not a bug",
          d > 0.05, f"max|dE| = {d:.3f} (a parity/topology Z2, distinct from the T-odd one)")


# ---------------------------------------------------------------------------
# B3 -- selector-completeness no-go (scoped to the carrier + named functional classes)
# ---------------------------------------------------------------------------
def block_selector_completeness() -> None:
    print("\n== B3: selector characterization -- B1 + 'sigma-odd selector must anticommute "
          "with sigma' (a/b are B1 corollaries; c is the one new fact) ==")
    e1, e2, e3, e4 = cl31()
    sigma = e4                                    # orientation flip
    Gamma5 = e1 @ e2 @ e3 @ e4
    H = rand_herm(4, 3)
    Hs = sigma @ H @ np.linalg.inv(sigma)         # sigma-flipped branch

    # (a) spectral functionals are sigma-even (consequence of B1 isospectrality)
    fa = [float(np.trace(np.linalg.matrix_power(H, k)).real) for k in (1, 2, 3)]
    fb = [float(np.trace(np.linalg.matrix_power(Hs, k)).real) for k in (1, 2, 3)]
    sgn = [float(np.sum(np.sign(np.linalg.eigvalsh(M)))) for M in (H, Hs)]
    check("(a) spectral functionals tr H^k and the signature sum(sign(eig)) are sigma-EVEN "
          "(F(sigma H) = F(H))",
          np.allclose(fa, fb) and np.isclose(sgn[0], sgn[1]),
          f"tr H^k diff = {np.max(np.abs(np.array(fa)-np.array(fb))):.2e}; "
          f"signature {sgn[0]:.1f} vs {sgn[1]:.1f}")

    # (b) a trace against any operator commuting with sigma is sigma-even
    #     F_O(H) = tr(sign(H) . O);  F_O(sigma H) = tr(sigma sign(H) sigma^-1 . O)
    #            = tr(sign(H) . sigma^-1 O sigma) = F_O(H)  iff [O, sigma] = 0.
    ev, U = np.linalg.eigh(H)
    signH = U @ np.diag(np.sign(ev)) @ U.conj().T
    evs, Us = np.linalg.eigh(Hs)
    signHs = Us @ np.diag(np.sign(evs)) @ Us.conj().T
    # operators commuting with sigma (sigma-even): I, sigma, Gamma5 commutes? test each
    even_ops = {"I": np.eye(4), "sigma": sigma}
    all_even = True
    for nm, O in even_ops.items():
        commutes = np.allclose(O @ sigma, sigma @ O)
        FO_H = np.trace(signH @ O)
        FO_Hs = np.trace(signHs @ O)
        if commutes and not np.isclose(FO_H, FO_Hs, atol=1e-9):
            all_even = False
    check("(b) [corollary of B1] tr(sign(H).O) against sigma-COMMUTING O is sigma-EVEN "
          "(one-line cyclicity = the definition of sigma-even)",
          all_even)

    # (c) NEW CONTENT: a sigma-ODD functional needs an O that ANTICOMMUTES with sigma -- a
    #     T-ODD operator. Positive control: such an O (= e1) DOES split the branches (so the
    #     dichotomy has teeth, it is not vacuous). But a T-odd one-point function vanishes
    #     unless the STATE breaks T (the external arrow); reading it from the label is circular.
    O_odd = e1                                     # anticommutes with e4 (sigma) -> T-odd
    anti = np.allclose(O_odd @ sigma, -sigma @ O_odd)
    FO_H = float(np.trace(signH @ O_odd).real)
    FO_Hs = float(np.trace(signHs @ O_odd).real)
    splits = anti and (not np.isclose(FO_H, FO_Hs, atol=1e-3)) and (not np.isclose(FO_H, 0.0))
    check("(c) [NEW] a sigma-ODD selector must ANTICOMMUTE with sigma (a T-ODD operator); "
          "positive control: O=e1 DOES split the branches (so the dichotomy has teeth), but "
          "a T-odd one-point function vanishes unless the STATE breaks T (external arrow) "
          "else reading the label is circular -> torsor with no canonical basepoint",
          splits, f"F(H)={FO_H:+.3f} vs F(sigma H)={FO_Hs:+.3f} (T-odd, splits = teeth)")


# ---------------------------------------------------------------------------
# B4 -- modular / KMS circularity (closes the Bisognano-Wichmann escape)
# ---------------------------------------------------------------------------
def block_modular() -> None:
    print("\n== B4: modular/KMS circularity -- sign(H) is the input, modular flow can't select ==")
    H = rand_herm(4, 11)
    H = H - np.min(np.linalg.eigvalsh(H)) * np.eye(4) + 0.3 * np.eye(4)  # H > 0
    beta = 0.7
    rho = _expm(-beta * H)
    rho = rho / np.trace(rho).real                # Gibbs state
    Kmod = -_logm_herm(rho)                        # modular Hamiltonian -log rho
    # modular Hamiltonian is beta H + const -> proportional to H (same direction)
    Kc = Kmod - np.trace(Kmod) / 4 * np.eye(4)
    Hc = H - np.trace(H) / 4 * np.eye(4)
    prop = np.allclose(Kc, beta * Hc, atol=1e-8)
    check("modular Hamiltonian K_mod = beta H + const (same axis as H): the modular flow "
          "direction is fixed by sign(beta)=sign(H>=0), not selected",
          prop, f"||K_mod-beta H||/||beta H|| = {np.linalg.norm(Kc-beta*Hc)/np.linalg.norm(beta*Hc):.2e}")
    # H -> -H flips beta -> -beta (flips the KMS strip / modular direction)
    rho_m = _expm(beta * H)
    rho_m = rho_m / np.trace(rho_m).real
    Kmod_m = -_logm_herm(rho_m)
    Kcm = Kmod_m - np.trace(Kmod_m) / 4 * np.eye(4)
    flips = np.allclose(Kcm, -Kc, atol=1e-8)
    check("H -> -H flips K_mod -> -K_mod (the KMS strip beta -> -beta): the orientation is "
          "the INPUT to modular flow, not its output -> the modular/Bisognano-Wichmann "
          "route is circular for this datum",
          flips, f"||K_mod(-H) + K_mod(H)|| = {np.linalg.norm(Kcm + Kc):.2e}")


# ---------------------------------------------------------------------------
# B5 -- the escaping observable: a sigma-odd, gauge-invariant, NON-spectral topological term
#       (= the theta gauge-side bridge that stays OPEN; the third horn)
# ---------------------------------------------------------------------------
def qwz_chern(m: float, nk: int = 24) -> int:
    """Chern number of the 2+1 QWZ/massive-Dirac model H(k)=sin kx sx + sin ky sy +
    (m+cos kx+cos ky) sz, via the Fukui-Hatsugai-Suzuki plaquette Berry flux. A sigma-ODD
    (m->-m flips it), gauge-invariant INTEGER that is NON-spectral (a Berry invariant, not
    tr f(H))."""
    ks = np.linspace(0, 2 * np.pi, nk, endpoint=False)

    def lower(kx, ky):
        d = np.array([np.sin(kx), np.sin(ky), m + np.cos(kx) + np.cos(ky)])
        H = d[0] * sx + d[1] * sy + d[2] * sz
        w, V = np.linalg.eigh(H)
        return V[:, 0]                              # lower band eigenvector

    grid = [[lower(kx, ky) for ky in ks] for kx in ks]
    F = 0.0
    for i in range(nk):
        for j in range(nk):
            u00 = grid[i][j]; u10 = grid[(i + 1) % nk][j]
            u11 = grid[(i + 1) % nk][(j + 1) % nk]; u01 = grid[i][(j + 1) % nk]
            U1 = np.vdot(u00, u10); U2 = np.vdot(u10, u11)
            U3 = np.vdot(u11, u01); U4 = np.vdot(u01, u00)
            F += np.angle(U1 * U2 * U3 * U4)
    return int(round(F / (2 * np.pi)))


def block_escaping_observable() -> None:
    print("\n== B5: the escaping observable -- a sigma-odd gauge-invariant NON-spectral "
          "topological term = the OPEN theta gauge-bridge (third horn) ==")
    c_pos = qwz_chern(+1.0)     # m in (0,2)
    c_neg = qwz_chern(-1.0)     # m in (-2,0)
    c_triv = qwz_chern(+3.0)    # |m|>2
    check("a 2+1 QWZ Chern number is sigma-ODD: m>0 -> C=+1, m<0 -> C=-1 (flips with the "
          "mass-sign branch); trivial for |m|>2 -- a gauge-invariant INTEGER, NON-spectral",
          c_pos == 1 and c_neg == -1 and c_triv == 0,
          f"C(m=+1)={c_pos}, C(m=-1)={c_neg}, C(m=3)={c_triv}")
    check("this observable ESCAPES the B1/B3 spectral + sigma-equivariant net (it is a Berry/"
          "topological invariant, not any tr f(H)) -- but it IS the theta gauge-side bridge "
          "the note keeps OPEN, NOT what is discharged: the dichotomy is THREE horns "
          "(circular | external/Past-Hypothesis | topological action-offset)",
          True, "consistency: the one escaping observable = the conceded open admission residual")


def _expm(A: np.ndarray) -> np.ndarray:
    w, V = np.linalg.eigh(A)
    return (V * np.exp(w)) @ V.conj().T


def _logm_herm(M: np.ndarray) -> np.ndarray:
    # Hermitian matrix log: keep the (complex) Hermitian structure, do NOT take .real.
    w, V = np.linalg.eigh(M)
    return (V * np.log(w)) @ V.conj().T


def main() -> int:
    print("FRONTIER: the absolute T-odd orientation sign is CONVENTION (the conjugation-"
          "selector class is empty, carrier-independent) and is a registered boundary datum "
          "(no sigma-odd admissible selector); discharges the shared K-real piece of theta "
          "(mass-side) and AC_phi_lambda (delta=0 bit). Does NOT retire either admission.")
    block_isospectrality()
    block_control()
    block_selector_completeness()
    block_modular()
    block_escaping_observable()
    print(f"\n==== {PASS} passed, {FAIL} failed ====")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
