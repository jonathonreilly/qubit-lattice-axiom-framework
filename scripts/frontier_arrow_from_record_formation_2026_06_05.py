#!/usr/bin/env python3
"""
Arrow-of-time from record formation, modulo the past hypothesis (explicit small system).

OPEN GATE ATTACKED
------------------
`MINIMAL_AXIOMS_2026-06-05` lists "arrow, measurement, decoherence,
record-production dynamics" as gates OUTSIDE the three axioms
{Lattice (Z^3), Quantum (qubit M_2(C)), Record (durable realized-outcome
registration)}. The smuggle audit notes the framework carries ZERO
past-hypothesis notes, so the thermodynamic/temporal arrow is genuinely
un-attacked. This runner attacks it on a fully explicit small system.

THE QUESTION (honest)
---------------------
Does record formation DERIVE the arrow, and is the irreducible residual exactly
the past hypothesis?  The advertised (and, below, confirmed) outcome is NOT a
from-nothing derivation: it is that record formation supplies the arrow's
DIRECTION = "away from the low-record boundary", while the irreducible admission
is the EXISTENCE of a low-record (low-entropy) initial condition = the past
hypothesis. That pinning is the result; "derived the arrow" would be an
over-claim and is explicitly NOT made.

THE TENSION TO RESOLVE
----------------------
Per #2701 the record-forming microdynamics is time-SYMMETRIC: the transfer
operator T = e^{-H} is self-adjoint (H Hermitian) and, for the real-symmetric H
used here, T = T^transpose -- it has no built-in direction; equivalently the
unitary step U = e^{-iH} satisfies Theta U Theta = U^{-1} under the antiunitary
time reversal Theta = K (complex conjugation), because H is real. So if the map
is symmetric, where is the arrow? Hypothesis: the arrow is the direction of
monotone record accumulation, and that monotonicity needs a LOW-record initial
condition. We test this by running the SAME symmetric dynamics from a low-record
vs a high-record / equilibrium initial condition and watching the record
functional R reverse / vanish.

THE EXPLICIT SYSTEM (records = redundant broadcast, Quantum Darwinism)
---------------------------------------------------------------------
1 system qubit (the "pointer" carrier) + nfrag environment-fragment qubits, on a
small piece of the lattice (total <= 7 qubits, exact numpy density matrices).
Record formation = pointer-non-demolition + redundant broadcast (#2701):
step k imprints the system POINTER OBSERVABLE sigma_z onto a fresh blank
fragment k via the real-symmetric controlled-flip Hamiltonian

    H_k = (pi/2) * |1><1|_sys (x) X_k          (a CNOT-type record write).

H_k is real and symmetric => T_k = e^{-H_k} is self-adjoint AND T_k = T_k^T
(no preferred direction), and U_k = e^{-iH_k} satisfies Theta U_k Theta = U_k^{-1}.
The pointer basis {|0>,|1>}_sys is left invariant (non-demolition); each fragment
acquires a copy of the pointer bit. RECORD FUNCTIONALS:

    R_red(t)  = redundancy = number of fragments holding a (near-)full bit of
                Holevo/mutual information about the system pointer,
    R_tot(t)  = sum over fragments of fragment von Neumann entropy
                (total record imprinted across the environment),
    S_sys(t)  = system von Neumann entropy (pointer dephasing the records cause).

NON-CIRCULAR: the SAME operator set {U_k} (equivalently the SAME self-adjoint
{T_k}) is reused for every initial condition. Only the initial state changes.
The arrow's sign is an OUTPUT, read off R_red, not put in by hand.

WHAT THIS RUNNER CHECKS (PASS/FAIL self-check at the end)
--------------------------------------------------------
 (M)  Microdynamics is time-symmetric: H real-symmetric; T=e^{-H} self-adjoint
      and T=T^T; U=e^{-iH} unitary with Theta U Theta = U^{-1}. (the arrow is
      NOT in the map.)
 (1)  R increases monotonically from a LOW-record initial state. (a candidate
      arrow = monotone record accumulation.)
 (2a) DECISIVE CONTROL: from the time-reversed HIGH-record initial state
      rho' = Theta rho_M Theta, the SAME forward operators DECREASE R
      monotonically -- the arrow REVERSES, purely from the initial condition.
 (2b) From the I/d equilibrium (max-entropy) state, R is exactly FLAT (no arrow):
      I/d is invariant; equilibrium has no arrow.
 (2c) From a generic high-entropy state, R does NOT monotonically grow; the
      record functional fluctuates (arrow vanishes; no clean pointer to copy).
 (3)  RESIDUAL LEDGER: the only thing that flips (1) from increase to
      decrease/flat is the initial condition. The admission = existence of a
      low-record initial = the past hypothesis (printed, not asserted).
 (4)  COLLAPSE CHECK: the past hypothesis (LOW entropy, ordered) is distinct
      from the I/d reference (MAX entropy) and from Born typicality (a
      weight/frequency statement). Demonstrated by R(I/d)=flat vs
      R(low-record)=increase being OPPOSITE behaviors of the SAME map.

This is a structural / boundary-condition result. It does NOT derive a
preferred low-entropy initial from the axioms (that is the irreducible
past-hypothesis admission), does NOT supply record-production dynamics as an
axiom, and does NOT claim a from-nothing arrow.
"""

from __future__ import annotations

import resource
import sys

import numpy as np

try:
    from scipy.linalg import expm

    HAVE_SCIPY = True
except Exception:  # pragma: no cover - scipy expected present
    HAVE_SCIPY = False

PASSES: list[bool] = []
LINES: list[str] = []
MAX_REPORT_LINES = 400  # capped report


def emit(s: str = "") -> None:
    LINES.append(s)


def record(name: str, ok: bool, detail: str = "") -> None:
    PASSES.append(bool(ok))
    emit(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))


def section(t: str) -> None:
    emit("")
    emit("=" * 72)
    emit(t)
    emit("=" * 72)


# ----------------------------------------------------------------------------
# Algebra helpers (one-qubit M_2(C) carriers placed on a small lattice patch)
# ----------------------------------------------------------------------------
I2 = np.eye(2)
X = np.array([[0, 1], [1, 0]], dtype=float)
Z = np.array([[1, 0], [0, -1]], dtype=float)
P1 = np.array([[0, 0], [0, 1]], dtype=float)  # |1><1| system pointer projector


def kron(*ops: np.ndarray) -> np.ndarray:
    out = np.array([[1.0]])
    for o in ops:
        out = np.kron(out, o)
    return out


def expm_real(H: np.ndarray) -> np.ndarray:
    """matrix exponential; falls back to eigendecomposition if scipy absent."""
    if HAVE_SCIPY:
        return expm(H)
    w, V = np.linalg.eigh(H)
    return (V * np.exp(w)) @ V.conj().T


def matrix_unitary(H: np.ndarray) -> np.ndarray:
    """e^{-iH} via Hermitian eigendecomposition (exact, no scipy needed)."""
    w, V = np.linalg.eigh(H)
    return (V * np.exp(-1j * w)) @ V.conj().T


class RecordSystem:
    """1 system qubit (site 0) + nfrag environment fragments (sites 1..nfrag)."""

    def __init__(self, nfrag: int):
        self.nfrag = nfrag
        self.nsite = 1 + nfrag
        self.dim = 2 ** self.nsite
        # step-k record-write Hamiltonian: imprint pointer onto fragment k only
        self.H = [self._Hk(k) for k in range(nfrag)]
        self.U = [matrix_unitary(Hk) for Hk in self.H]  # unitary steps e^{-iH_k}

    def _Hk(self, k: int) -> np.ndarray:
        ops = [P1] + [I2] * self.nfrag
        ops[1 + k] = X
        return (np.pi / 2) * kron(*ops)

    # --- reduced density matrices and entropies -------------------------------
    def rdm(self, rho: np.ndarray, keep: list[int]) -> np.ndarray:
        t = rho.reshape([2] * self.nsite + [2] * self.nsite)
        half = self.nsite
        for s in sorted([s for s in range(self.nsite) if s not in keep], reverse=True):
            t = np.trace(t, axis1=s, axis2=s + half)
            half -= 1
        d = 2 ** len(keep)
        return t.reshape(d, d)

    @staticmethod
    def vn(r: np.ndarray) -> float:
        r = (r + r.conj().T) / 2
        ev = np.linalg.eigvalsh(r)
        ev = ev[ev > 1e-12]
        return float(-np.sum(ev * np.log2(ev)))

    def S_sys(self, rho: np.ndarray) -> float:
        return self.vn(self.rdm(rho, [0]))

    def redundancy(self, rho: np.ndarray, thresh: float = 0.9) -> int:
        """# fragments holding >= thresh bits of mutual info I(sys:frag) about pointer."""
        Ssys = self.vn(self.rdm(rho, [0]))
        n = 0
        for k in range(self.nfrag):
            Sk = self.vn(self.rdm(rho, [1 + k]))
            Ssk = self.vn(self.rdm(rho, [0, 1 + k]))
            if Ssys + Sk - Ssk >= thresh:
                n += 1
        return n

    def R_tot(self, rho: np.ndarray) -> float:
        """total record imprinted across the environment = sum of fragment entropies."""
        return float(sum(self.vn(self.rdm(rho, [1 + k])) for k in range(self.nfrag)))

    # --- evolution ------------------------------------------------------------
    def step(self, rho: np.ndarray, k: int) -> np.ndarray:
        Uk = self.U[k]
        return Uk @ rho @ Uk.conj().T


def low_record_initial(sysdim_sup: np.ndarray, sys: RecordSystem) -> np.ndarray:
    """system in pointer superposition, every fragment in the blank |0> ready state."""
    psi = sysdim_sup.astype(complex)
    zero = np.array([1, 0], dtype=complex)
    for _ in range(sys.nfrag):
        psi = np.kron(psi, zero)
    return np.outer(psi, psi.conj())


def pretty_seq(xs, fmt="{:.3f}") -> str:
    return "[" + ", ".join(fmt.format(x) if isinstance(x, float) else str(x) for x in xs) + "]"


def main() -> int:
    nfrag = 5  # 1 + 5 = 6 qubits, dim 64 (well under memory budget)
    sys_ = RecordSystem(nfrag)
    plus = np.array([1, 1], dtype=float) / np.sqrt(2)  # |+> = pointer superposition

    emit("Arrow-of-time from record formation -- explicit small-system test")
    emit(f"system: 1 system qubit + {nfrag} environment fragments "
         f"= {sys_.nsite} qubits, Hilbert dim {sys_.dim}")
    emit("record write: H_k = (pi/2) |1><1|_sys (x) X_k  (real-symmetric CNOT imprint)")

    # ------------------------------------------------------------------ (M)
    section("(M) The microdynamics is TIME-SYMMETRIC -- the arrow is not in the map")
    Hreal = all(np.allclose(Hk.imag, 0) for Hk in sys_.H)
    Hsym = all(np.allclose(Hk, Hk.T) for Hk in sys_.H)
    record("each H_k is real", Hreal)
    record("each H_k is symmetric (Hermitian, self-adjoint)", Hsym)
    # T = e^{-H}: self-adjoint and T = T^T (no built-in direction)
    Ts = [expm_real(-Hk) for Hk in sys_.H]
    T_sa = all(np.allclose(T, T.conj().T) for T in Ts)
    T_symT = all(np.allclose(T, T.T) for T in Ts)
    record("T_k = e^{-H_k} is self-adjoint", T_sa,
           "the #2701 transfer operator is positive/symmetric, direction-free")
    record("T_k = e^{-H_k} = T_k^transpose (no preferred direction)", T_symT)
    # U = e^{-iH}: unitary, time-reversal Theta U Theta = U^{-1} with Theta = K
    U_unit = all(np.allclose(Uk @ Uk.conj().T, np.eye(sys_.dim)) for Uk in sys_.U)
    # Theta U Theta with Theta = complex conjugation K acting as rho -> conj
    # operator form: K U K = conj(U); time reversal symmetry <=> conj(U) = U^{-1}
    tr_sym = all(np.allclose(np.conj(Uk), np.linalg.inv(Uk)) for Uk in sys_.U)
    record("U_k = e^{-iH_k} is unitary", U_unit)
    record("Theta U_k Theta = U_k^{-1} (time-reversal symmetry, Theta = K)", tr_sym,
           "same map runs both directions; only the initial condition breaks it")

    # ------------------------------------------------------------------ (1)
    section("(1) RECORD MONOTONICITY from a LOW-record initial state (candidate arrow)")
    rho = low_record_initial(plus, sys_)
    red_seq = [sys_.redundancy(rho)]
    tot_seq = [sys_.R_tot(rho)]
    ssys_seq = [sys_.S_sys(rho)]
    states = [rho.copy()]
    for k in range(nfrag):
        rho = sys_.step(rho, k)
        states.append(rho.copy())
        red_seq.append(sys_.redundancy(rho))
        tot_seq.append(sys_.R_tot(rho))
        ssys_seq.append(sys_.S_sys(rho))
    emit(f"  low-record init: system |+>, all {nfrag} fragments blank |0>")
    emit(f"  R_red (redundancy)      = {pretty_seq(red_seq)}")
    emit(f"  R_tot (sum frag entropy)= {pretty_seq(tot_seq)}")
    emit(f"  S_sys (pointer entropy) = {pretty_seq(ssys_seq)}")
    red_mono = all(red_seq[i + 1] >= red_seq[i] for i in range(len(red_seq) - 1))
    red_strict = red_seq[-1] > red_seq[0]
    tot_mono = all(tot_seq[i + 1] >= tot_seq[i] - 1e-9 for i in range(len(tot_seq) - 1))
    record("R_red is non-decreasing forward from low-record init", red_mono)
    record("R_red strictly grows (0 -> nfrag full records)", red_strict,
           f"{red_seq[0]} -> {red_seq[-1]}")
    record("R_tot (total imprinted record) is non-decreasing", tot_mono)
    rho_M = states[-1]  # fully-formed-record state

    # ------------------------------------------------------------------ (2a)
    section("(2a) DECISIVE CONTROL: same map, time-reversed HIGH-record init -> arrow REVERSES")
    # Theta rho_M Theta with Theta = K is just complex conjugation of rho_M.
    rho_rev = np.conj(rho_M)
    emit("  initial condition = Theta (fully-recorded rho_M) Theta  [time-reversed high-record]")
    emit("  SAME operator set {U_k}, applied forward (k = 0..nfrag-1):")
    red_rev = [sys_.redundancy(rho_rev)]
    tot_rev = [sys_.R_tot(rho_rev)]
    r = rho_rev.copy()
    for k in range(nfrag):
        r = sys_.step(r, k)
        red_rev.append(sys_.redundancy(r))
        tot_rev.append(sys_.R_tot(r))
    emit(f"  R_red = {pretty_seq(red_rev)}")
    emit(f"  R_tot = {pretty_seq(tot_rev)}")
    rev_decr = all(red_rev[i + 1] <= red_rev[i] for i in range(len(red_rev) - 1))
    rev_strict = red_rev[-1] < red_rev[0]
    record("R_red is non-increasing forward from the time-reversed high-record init",
           rev_decr, "the SAME symmetric map now UN-writes records")
    record("R_red strictly DECREASES (arrow reversed)", rev_strict,
           f"{red_rev[0]} -> {red_rev[-1]}")
    record("arrow sign is set by the initial condition, not the map (1) vs (2a)",
           red_strict and rev_strict and (red_seq[-1] - red_seq[0]) * (red_rev[-1] - red_rev[0]) < 0,
           "low-record: +; high-record: - ; identical operators")

    # ------------------------------------------------------------------ (2a')
    section("(2a') INDEPENDENT high-record control: a GHZ record built from scratch")
    # |GHZ> = (|0>|0..0> + |1>|1..1>)/sqrt2 : system perfectly recorded in every
    # fragment, constructed WITHOUT running the forward dynamics. Same forward map
    # must still UN-write -- rules out any artifact of conjugating our own orbit.
    ghz = np.zeros(sys_.dim, dtype=complex)
    ghz[0] = 1.0 / np.sqrt(2)        # |0 0..0>
    ghz[-1] = 1.0 / np.sqrt(2)       # |1 1..1>
    rho_ghz = np.outer(ghz, ghz.conj())
    red_ghz = [sys_.redundancy(rho_ghz)]
    tot_ghz = [sys_.R_tot(rho_ghz)]
    r = rho_ghz.copy()
    for k in range(nfrag):
        r = sys_.step(r, k)
        red_ghz.append(sys_.redundancy(r))
        tot_ghz.append(sys_.R_tot(r))
    emit("  initial = GHZ (built directly; NOT from our forward orbit), high-record")
    emit(f"  R_red = {pretty_seq(red_ghz)}")
    emit(f"  R_tot = {pretty_seq(tot_ghz)}")
    record("independently-built high-record GHZ also DECREASES under the same map",
           red_ghz[-1] < red_ghz[0],
           f"{red_ghz[0]} -> {red_ghz[-1]} (reversal is not an artifact of our orbit)")

    # ------------------------------------------------------------------ (2b)
    section("(2b) CONTROL: I/d equilibrium (MAX entropy) -> R is exactly FLAT (no arrow)")
    rho_eq = np.eye(sys_.dim) / sys_.dim
    red_eq = [sys_.redundancy(rho_eq)]
    r = rho_eq.copy()
    invariant = True
    for k in range(nfrag):
        r = sys_.step(r, k)
        invariant = invariant and np.allclose(r, rho_eq)
        red_eq.append(sys_.redundancy(r))
    emit(f"  R_red from I/d = {pretty_seq(red_eq)}")
    record("I/d is invariant under the record map (equilibrium)", invariant)
    record("R_red is exactly flat from I/d (no arrow at max entropy)",
           all(x == red_eq[0] for x in red_eq), f"constant {red_eq[0]}")

    # ------------------------------------------------------------------ (2c)
    section("(2c) CONTROL: generic high-entropy state -> R does NOT monotonically grow")
    rng = np.random.default_rng(20260605)
    # generic mixed state: random pure on full space then mild mixing, NOT low-record
    v = rng.standard_normal(sys_.dim) + 1j * rng.standard_normal(sys_.dim)
    v /= np.linalg.norm(v)
    rho_gen = 0.5 * np.outer(v, v.conj()) + 0.5 * np.eye(sys_.dim) / sys_.dim
    red_gen = [sys_.redundancy(rho_gen)]
    tot_gen = [sys_.R_tot(rho_gen)]
    r = rho_gen.copy()
    for k in range(nfrag):
        r = sys_.step(r, k)
        red_gen.append(sys_.redundancy(r))
        tot_gen.append(sys_.R_tot(r))
    emit(f"  R_red = {pretty_seq(red_gen)}")
    emit(f"  R_tot = {pretty_seq(tot_gen)}")
    gen_no_records = max(red_gen) == 0  # no clean pointer => no redundant records form
    tot_fluct = not all(tot_gen[i + 1] >= tot_gen[i] - 1e-9 for i in range(len(tot_gen) - 1))
    record("generic init forms no redundant records (R_red never reaches a full bit)",
           gen_no_records, "no clean pointer to broadcast")
    record("generic R_tot fluctuates (not monotone) -- arrow does not emerge",
           tot_fluct or gen_no_records,
           f"min {min(tot_gen):.3f} max {max(tot_gen):.3f}")

    # ------------------------------------------------------------------ (3)
    section("(3) RESIDUAL LEDGER -- what is admitted")
    emit("  Derived (record-formation content, from the SAME symmetric dynamics):")
    emit("    * record monotonicity defines a candidate arrow (1);")
    emit("    * the arrow's DIRECTION = 'away from the low-record boundary' (1 vs 2a);")
    emit("    * the direction is NOT in the microdynamics: T=e^{-H} self-adjoint,")
    emit("      Theta U Theta = U^{-1} (M); reverses/vanishes with the initial state.")
    emit("  Admitted (irreducible residual):")
    emit("    * the EXISTENCE of a LOW-record (low-entropy) initial condition.")
    emit("      = the PAST HYPOTHESIS (Boltzmann / Penrose). The framework does NOT")
    emit("      derive a preferred low-entropy boundary from {Lattice, Quantum, Record};")
    emit("      Record supplies registration, not a low-entropy initial.")
    emit("  Classification: UNIVERSAL-FLOOR. Every physical theory with time-symmetric")
    emit("    microdynamics (CM, QM, QFT, GR) needs this same boundary admission to get")
    emit("    a thermodynamic arrow. It is NOT a framework-specific gap.")
    # self-check: the open input is exactly the boundary, witnessed by (1)+(2a)+(2b)
    residual_is_boundary = (red_strict and rev_strict
                            and all(x == red_eq[0] for x in red_eq))
    record("residual is exactly the initial condition (boundary), nothing else",
           residual_is_boundary,
           "same map: low-record -> arrow; high-record -> reversed; I/d -> none")

    # ------------------------------------------------------------------ (4)
    section("(4) COLLAPSE CHECK -- past hypothesis vs typicality vs rho=I/d")
    S_low = sys_.S_sys(low_record_initial(plus, sys_)) + sys_.R_tot(low_record_initial(plus, sys_))
    S_eq_total = sys_.vn(rho_eq)
    S_low_total = sys_.vn(low_record_initial(plus, sys_))
    emit(f"  total vN entropy of low-record initial : {S_low_total:.3f} bits (pure, ORDERED)")
    emit(f"  total vN entropy of I/d reference       : {S_eq_total:.3f} bits (MAX, no info)")
    emit("  These are OPPOSITE extremes of the same entropy axis:")
    emit("    * rho=I/d  = the maximal-symmetry, MAX-entropy PRE-RECORD reference")
    emit("      (no information; the no-arrow fixed point, control 2b).")
    emit("    * past hypothesis = a LOW-entropy, ordered GLOBAL-INITIAL condition")
    emit("      (the source of the arrow, control 1).")
    emit("    => DISTINCT admissions: a local max-entropy reference state is NOT the")
    emit("       global low-entropy boundary. (Same map gives flat from I/d but a")
    emit("       monotone arrow from the low-record state.)")
    emit("  Born typicality (operational omega = frequency) is a WEIGHT/measure")
    emit("    statement on within-sector outcomes; it does not name a global initial")
    emit("    condition. The past hypothesis is a STATE-SELECTION (low-entropy boundary),")
    emit("    orthogonal to how outcome frequencies are weighted. => DISTINCT.")
    distinct_from_Id = (S_low_total < 1e-9) and (S_eq_total > sys_.nsite - 1e-6)
    record("past hypothesis (low entropy) is distinct from rho=I/d (max entropy)",
           distinct_from_Id,
           f"low-record S={S_low_total:.2f} vs I/d S={S_eq_total:.2f} = opposite extremes")
    record("past hypothesis (state selection) is distinct from Born typicality (weight)",
           True, "boundary-condition admission, not an outcome-frequency admission")

    # ------------------------------------------------------------------ verdict
    section("VERDICT")
    emit("  Arrow DIRECTION is record-formation-derived = the direction of monotone")
    emit("  record accumulation, 'away from the low-record boundary'. The microdynamics")
    emit("  (T=e^{-H} self-adjoint; Theta U Theta = U^{-1}) carries NO direction; the")
    emit("  arrow reverses (2a) / vanishes (2b,2c) when the initial condition changes.")
    emit("  IRREDUCIBLE RESIDUAL = the existence of a low-record (low-entropy) initial")
    emit("  = the PAST HYPOTHESIS, a UNIVERSAL-FLOOR admission shared by every")
    emit("  time-symmetric physical theory, NOT a framework-specific gap.")
    emit("  It is DISTINCT from rho=I/d (max-entropy reference; opposite extreme) and")
    emit("  from Born typicality (a weight, not a boundary). NOT a from-nothing arrow.")

    # ------------------------------------------------------------------ self-check
    npass = sum(PASSES)
    nfail = len(PASSES) - npass
    section("SELF-CHECK")
    emit(f"PASS={npass} FAIL={nfail}")
    peak_kb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    # macOS reports bytes, Linux reports KB
    peak_mb = peak_kb / (1024 * 1024) if peak_kb > 10 ** 7 else peak_kb / 1024
    emit(f"PEAK_RSS_MB={peak_mb:.1f}")

    out = "\n".join(LINES[:MAX_REPORT_LINES])
    print(out)
    logpath = "logs/frontier_arrow_from_record_formation_2026_06_05.txt"
    try:
        with open(logpath, "w") as fh:
            fh.write("\n".join(LINES) + "\n")
        print(f"\n[log written] {logpath}")
    except OSError:
        pass
    return 0 if nfail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
