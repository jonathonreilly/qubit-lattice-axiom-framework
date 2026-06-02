#!/usr/bin/env python3
"""
Runner: Reality/CPT of the record-writing channel discharges the branch PHASE
but not the SIGN; the terminal T-positivity import shrinks from U(1) to Z_2.

Pairs with KOIDE_RECORDS_REALITY_SHRINKS_IMPORT_TO_SIGN_NARROW_THEOREM_NOTE.

Verifies, on finite carriers (no CAR, no T-positivity, no Hermitian records
ASSUMED in any forcing step):

 1. The prior branch-phase counterexample (complex off-diagonal record
    multiplier z) reproduces: valid CPTP, unital, persists the Z-record, yet
    transfer superoperator T has complex spectrum (not Hermitian, not positive).
 2. Self-duality of the transfer (T Hermitian as a matrix) <=> the record
    Kraus set is closed under dagger <=> reality/CPT of the record-writing
    generator (a REAL interaction Hamiltonian, the records analog of
    cpt_exact's 'D real anti-Hermitian'). Reality kills the U(1) branch phase:
    it forces the off-diagonal multiplier z REAL.
 3. But reality buys only Hermiticity (self-duality), NOT positivity: a real
    record-writing H_int yields a Hermitian transfer with a NEGATIVE eigenvalue
    for generic coupling time. The residual is a Z_2 SIGN, not a U(1) phase.
 4. Positive-Hermitian transfer (=> H=-log T/a real, the spectrum condition,
    OS reflection positivity) requires the strictly stronger Hermitian-Kraus /
    detailed-balance-at-I/2 condition (sufficient; Pauli/sigma_i channels).
 5. Genericity: random unital qubit channels give measure-zero
    Hermitian-Kraus / positive-Hermitian transfer -> a genuine import.
 6. The emergent-time single-clock-Stone construction CONSUMES T-positivity as
    a hypothesis (non-positive T -> no real generator), so it cannot FORCE it
    (using it as a forcing argument is circular).

SCORECARD PASS=k printed at end.
"""
import numpy as np
from scipy.linalg import expm, sqrtm, logm
from scipy.stats import unitary_group

I2 = np.eye(2, dtype=complex)
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
TOL = 1e-9

def superop(Ks):
    """Column-stacking superoperator of E(rho)=sum_r K_r rho K_r^dag."""
    d = Ks[0].shape[0]
    return sum(np.kron(K.conj(), K) for K in Ks)

def dual_superop(Ks):
    """Superoperator of the HS-dual map E*(X)=sum_r K_r^dag X K_r."""
    return sum(np.kron(K.T, K.conj().T) for K in Ks)

def is_herm(M, tol=TOL):
    return np.allclose(M, M.conj().T, atol=tol)

def is_pos_herm(M, tol=1e-8):
    if not is_herm(M, tol):
        return False
    return np.all(np.linalg.eigvalsh((M + M.conj().T) / 2) > -tol)

def cptp(Ks):
    return np.allclose(sum(K.conj().T @ K for K in Ks), I2, atol=TOL)

def unital(Ks):
    return np.allclose(sum(K @ (I2 / 2) @ K.conj().T for K in Ks), I2 / 2, atol=TOL)

def persists_Z(Ks):
    rho = np.array([[0.6, 0.2 + 0.1j], [0.2 - 0.1j, 0.4]], dtype=complex)
    out = sum(K @ rho @ K.conj().T for K in Ks)
    return np.allclose(np.diag(out), np.diag(rho), atol=1e-9)

def vn_record_blocks(Hint, t, d_sys=2):
    """von Neumann premeasurement record (Kraus) blocks with meter init |0>."""
    U = expm(-1j * Hint * t).reshape(d_sys, 2, d_sys, 2)
    return [U[:, m, :, 0] for m in range(2)]

results = []
def check(name, cond):
    results.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}")
    return bool(cond)

print("=" * 74)
print("1. Prior branch-phase counterexample reproduces (complex z).")
print("=" * 74)
# z = 0.5*1 + 0.5*e^{i pi/2} = 0.5 + 0.5 i  -> prior note spec {1,1,0.5+-0.5i}
K0 = np.sqrt(0.5) * np.diag([1.0, 1.0])
K1 = np.sqrt(0.5) * np.diag([np.exp(1j * np.pi / 2), 1.0])
CE = [K0, K1]
check("counterexample is CPTP", cptp(CE))
check("counterexample is unital (fixes I/2)", unital(CE))
check("counterexample persists the Z-record", persists_Z(CE))
T_ce = superop(CE)
check("counterexample transfer NOT positive-Hermitian", not is_pos_herm(T_ce))
check("counterexample transfer has complex spectrum (branch phase)",
      np.max(np.abs(np.linalg.eigvals(T_ce).imag)) > 1e-6)

print("=" * 74)
print("2. Reality/CPT (self-dual / real H_int) FORCES the off-diagonal record")
print("   multiplier z REAL -> kills the U(1) branch phase -> Hermitian transfer.")
print("=" * 74)
# pointer-basis reality E(rho*)=E(rho)*  <=>  z real  <=>  T self-dual (Hermitian)
def chan(rho, Ks):
    return sum(K @ rho @ K.conj().T for K in Ks)
rho = np.array([[0.6, 0.2 + 0.1j], [0.2 - 0.1j, 0.4]], dtype=complex)
reality_even_CE = np.allclose(chan(rho.conj(), CE), chan(rho, CE).conj())
check("complex-z counterexample is NOT pointer-reality-even (excluded by reality)",
      not reality_even_CE)
# symmetric +/- a relative phase -> z = cos a real -> reality-even, Hermitian T
oks = []
for a in [0.3, 0.9, 1.7, 2.6]:
    Ka = np.sqrt(0.5) * np.diag([np.exp(1j * a), 1.0])
    Kb = np.sqrt(0.5) * np.diag([np.exp(-1j * a), 1.0])
    Ks = [Ka, Kb]
    reality_even = np.allclose(chan(rho.conj(), Ks), chan(rho, Ks).conj())
    Th = superop(Ks)
    oks.append(reality_even and is_herm(Th))
check("reality-even (z real) ALWAYS gives Hermitian transfer (phase killed)",
      all(oks))

print("=" * 74)
print("3. Reality buys only HERMITICITY, not POSITIVITY: a REAL record-writing")
print("   H_int (records analog of cpt_exact 'D real') gives Hermitian transfer")
print("   with a NEGATIVE eigenvalue for generic coupling. Residual = Z_2 SIGN.")
print("=" * 74)
Hint_real = np.kron(sz, sx)          # real symmetric (sz, sx real) => reality
check("record-writing H_int is real symmetric (reality condition holds)",
      np.allclose(Hint_real, Hint_real.conj()) and np.allclose(Hint_real, Hint_real.T))
herm_all, pos_some_neg = True, False
for t in [0.6, 0.9, 1.2, np.pi / 2]:
    Ks = vn_record_blocks(Hint_real, t)
    T = superop(Ks)
    if not is_herm(T):
        herm_all = False
    if not is_pos_herm(T):
        pos_some_neg = True
check("real H_int always gives a Hermitian (self-dual) transfer", herm_all)
check("real H_int gives a NON-positive transfer for some coupling time",
      pos_some_neg)
# the Kraus blocks themselves are NOT Hermitian even though H_int is real
Ks12 = vn_record_blocks(Hint_real, 1.2)
check("real H_int record blocks are NOT individually Hermitian (sign survives)",
      not all(is_herm(K) for K in Ks12))

print("=" * 74)
print("4. POSITIVE-Hermitian transfer requires the strictly stronger")
print("   HERMITIAN-KRAUS / detailed-balance-at-I/2 condition (sufficient).")
print("=" * 74)
# Pauli channels (Hermitian Kraus sqrt(p_i) sigma_i) -> self-dual AND PSD
paulis = [I2, sx, sy, sz]
all_pos = True
for p in [(0.7, 0.1, 0.1, 0.1), (0.25, 0.25, 0.25, 0.25), (0.4, 0.3, 0.2, 0.1)]:
    Ks = [np.sqrt(pp) * P for pp, P in zip(p, paulis)]
    T = superop(Ks)
    if not (np.allclose(T, dual_superop(Ks)) and is_pos_herm(T)):
        all_pos = False
check("Hermitian-Kraus (sigma_i) channels are self-dual AND positive", all_pos)
# Hermitian POVM sqrt(E_r) also works
E0 = 0.6 * I2 + 0.2 * sz
Ks = [sqrtm(E0), sqrtm(I2 - E0)]
check("Hermitian POVM sqrt(E_r) gives positive-Hermitian transfer",
      all(is_herm(K) for K in Ks) and is_pos_herm(superop(Ks)))

print("=" * 74)
print("5. Genericity: Hermitian-Kraus / positive-Hermitian transfer is")
print("   measure-zero among unital qubit channels -> a genuine import.")
print("=" * 74)
rng = np.random.default_rng(2027)
n_herm_kraus = n_pos = n_self_dual = 0
N = 4000
for _ in range(N):
    U = unitary_group.rvs(4, random_state=rng).reshape(2, 2, 2, 2)
    Ks = [U[:, m, :, 0] for m in range(2)]
    T = superop(Ks)
    if all(is_herm(K, 1e-6) for K in Ks):
        n_herm_kraus += 1
    if is_pos_herm(T):
        n_pos += 1
    if np.allclose(T, dual_superop(Ks), atol=1e-6):
        n_self_dual += 1
print(f"  over {N} random unital qubit channels: Hermitian-Kraus={n_herm_kraus}, "
      f"positive-T={n_pos}, self-dual-T={n_self_dual}")
check("Hermitian-Kraus is measure-zero (genuine import, count==0)",
      n_herm_kraus == 0)
check("positive-Hermitian transfer is measure-zero (count==0)", n_pos == 0)

print("=" * 74)
print("6. The emergent-time single-clock-Stone construction CONSUMES")
print("   T-positivity (cannot force it): non-positive T -> no real generator.")
print("=" * 74)
# positive Hermitian T -> real Hermitian H=-log(T)/a
T_pos = superop([np.sqrt(0.7) * I2, np.sqrt(0.3) * sz])  # Hermitian-Kraus -> PSD
H_real = -logm((T_pos) / np.max(np.abs(np.linalg.eigvals(T_pos))))
check("positive-Hermitian T -> Hermitian generator H=-log(T/||T||)",
      is_herm(H_real, 1e-6))
# non-positive (but Hermitian) T -> generator is NOT real/Hermitian (log of neg)
T_neg = superop(vn_record_blocks(Hint_real, 1.2))   # Hermitian, has neg eigenvalue
w = np.linalg.eigvalsh((T_neg + T_neg.conj().T) / 2)
H_from_neg = logm(T_neg.astype(complex))
check("non-positive transfer has a NEGATIVE eigenvalue (Stone hypothesis fails)",
      w.min() < -1e-6)
check("non-positive transfer -> generator NOT Hermitian (construction can't run)",
      not is_herm(-H_from_neg, 1e-6))
print("  -> single_clock_stone ASSUMES 0 < spec(T) <= ||T|| (its stated")
print("     hypothesis); it derives H from T-positivity, it does not deliver it.")
print("     Using it to 'force' T-positivity is circular.")

n_pass = sum(ok for _, ok in results)
n_tot = len(results)
print()
print("=" * 74)
print(f"SCORECARD PASS={n_pass}/{n_tot}")
print("=" * 74)
if n_pass != n_tot:
    print("FAILURES:")
    for name, ok in results:
        if not ok:
            print(f"  - {name}")
