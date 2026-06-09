"""Block 06 runner - the color-einselection pointer-frame multiplicity fork
resolves into a unistochastic-irreducibility criterion.

Setting (predictability sieve on the C^3 color carrier). One NAMED record frame
B = {|e_i>} (the block-02 frame-naming instrument I-A; an admission on the
record-formation boundary) acts as the complete projective dephasing
channel D_B(X) = sum_i P_i X P_i (P_i = |e_i><e_i|, rank one). Between record
steps the coherent matter color dynamics acts as a unitary kick Ad_U(rho)
= U rho U^dag. One emergent-time step of the einselection layer is the composite
predictability-sieve channel

        Phi(rho) = D_B( U rho U^dag ).

This runner establishes, by exact finite-dimensional channel / Markov-chain
algebra (no Monte-Carlo fit in the derivation path; random states are only
witnesses for already-proven identities):

  C1  Phi maps every state into the B-diagonal subalgebra in ONE step.
  C2  On the B-diagonal subalgebra Phi acts as the classical Markov channel of
      the unistochastic transition matrix T_U[i,j] = |<e_i|U|e_j>|^2:
      Phi(diag p) = diag(T_U p).
  C3  T_U is doubly stochastic (row and column sums = 1) for every unitary U.
  C4  Fixed points of Phi = B-diagonal states whose vector is T_U-stationary; the
      maximally mixed I3/3 is ALWAYS a fixed point (T_U doubly stochastic).
  C5  COMMUTING LIMIT [U,B]=0 (U diagonal in B): T_U = identity, the ENTIRE
      B-diagonal 2-simplex is fixed -> frame B is einselected, NO depolarization
      (recovers the block-05 single-frame polarized boundary as the [U,B]=0 case).
  C6  REDUCIBLE T_U (U block-diagonal): >=2 ergodic classes -> multiple pointer
      states, color information survives, NO depolarization.
  C7  IRREDUCIBLE-but-PERIODIC T_U (a cyclic permutation U): UNIQUE T_U-stationary
      (uniform) so the fixed point is unique, but Phi^n oscillates (no pointwise
      relaxation); the Cesaro average is I3/3.
  C8  PERRON-PRIMITIVE T_U (irreducible + aperiodic; sufficient: U has no zero
      amplitude in B): the UNIQUE pointer state is I3/3 and Phi^n(rho) -> I3/3
      with the SINGLE record frame B. The complementary mixing is supplied by
      the matter unitary U, not a second instrument.
  C9  Order parameter P(rho) = Tr(rho^2) - 1/3 (= ||traceless(rho)||_F^2, the
      same order parameter as adjacent depolarization work) decreases
      monotonically in strictly positive transition witnesses.
  C10 GUARD (SU(3)-covariance != contraction): the identity channel (U=I,
      D_B trivial direction) is SU(3)-covariant yet inert; covariance never
      implies depolarization. Consistent with block-05 I-B (color-blind = inert).
  C11 RELOCATION gate: depolarization under a single record frame holds iff T_U is
      Perron primitive, which requires the matter unitary to mix the frame; Record
      supplies neither the frame (named admission) nor U's alignment (open input).
      No hat discharged.

All matrices are 3x3 (color C^3); a 2x2 sanity case is included. Memory-safe.
"""

import numpy as np

PASS = 0
FAIL = 0


def check(name, ok):
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"[PASS] {name}")
    else:
        FAIL += 1
        print(f"[FAIL] {name}")


rng = np.random.default_rng(20260609)


def haar_unitary(d):
    z = (rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))) / np.sqrt(2)
    q, r = np.linalg.qr(z)
    ph = np.diag(r) / np.abs(np.diag(r))
    return q * ph


def rand_rho(d):
    a = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
    m = a @ a.conj().T
    return m / np.trace(m)


def dephase(rho):
    """Complete projective dephasing in the computational frame B (rank-1 P_i)."""
    return np.diag(np.diag(rho))


def Phi(rho, U):
    return dephase(U @ rho @ U.conj().T)


def unistochastic(U):
    return np.abs(U) ** 2


def purity_above_floor(rho):
    d = rho.shape[0]
    return np.real(np.trace(rho @ rho)) - 1.0 / d


def traceless(rho):
    d = rho.shape[0]
    return rho - np.trace(rho) / d * np.eye(d)


d = 3
I3 = np.eye(d) / d

print("=== C1: Phi maps every state into the B-diagonal subalgebra in one step ===")
ok = True
for _ in range(40):
    U = haar_unitary(d)
    rho = rand_rho(d)
    out = Phi(rho, U)
    off = out - np.diag(np.diag(out))
    if np.linalg.norm(off) > 1e-12:
        ok = False
check("C1 Phi(rho) is exactly B-diagonal for all states", ok)
# and it is a valid state (PSD, trace 1)
ok = True
for _ in range(20):
    U = haar_unitary(d)
    rho = rand_rho(d)
    out = Phi(rho, U)
    if abs(np.trace(out) - 1) > 1e-12 or np.min(np.linalg.eigvalsh(out)) < -1e-12:
        ok = False
check("C1 Phi is trace-preserving and PSD-preserving (CPTP)", ok)

print("\n=== C2: on the diagonal, Phi = Markov channel of T_U (unistochastic) ===")
ok = True
for _ in range(40):
    U = haar_unitary(d)
    p = rng.random(d)
    p /= p.sum()
    T = unistochastic(U)
    lhs = np.diag(Phi(np.diag(p), U)).real
    rhs = T @ p
    if np.linalg.norm(lhs - rhs) > 1e-12:
        ok = False
check("C2 Phi(diag p) = diag(T_U p) exactly", ok)

print("\n=== C3: T_U = |U_ij|^2 is doubly stochastic for every unitary ===")
ok = True
for _ in range(40):
    U = haar_unitary(d)
    T = unistochastic(U)
    if np.linalg.norm(T.sum(1) - 1) > 1e-12 or np.linalg.norm(T.sum(0) - 1) > 1e-12:
        ok = False
check("C3 row sums = col sums = 1", ok)
# also for 2x2 sanity
ok = True
for _ in range(10):
    U2 = haar_unitary(2)
    T = unistochastic(U2)
    if np.linalg.norm(T.sum(1) - 1) > 1e-12 or np.linalg.norm(T.sum(0) - 1) > 1e-12:
        ok = False
check("C3 doubly stochastic also for d=2 (sanity)", ok)

print("\n=== C4: I3/3 is always a fixed point of Phi ===")
ok = True
for _ in range(40):
    U = haar_unitary(d)
    if np.linalg.norm(Phi(I3, U) - I3) > 1e-12:
        ok = False
check("C4 Phi(I3/3) = I3/3 for all U", ok)

print("\n=== C5: commuting limit [U,B]=0 -> T_U=I -> whole simplex fixed, NO depolarization ===")
U = np.diag(np.exp(1j * rng.standard_normal(d)))
T = unistochastic(U)
check("C5 [U,B]=0 gives T_U = identity", np.linalg.norm(T - np.eye(d)) < 1e-12)
ok = True
for _ in range(20):
    p = rng.random(d)
    p /= p.sum()
    rho = np.diag(p)
    rinf = rho.copy()
    for _ in range(300):
        rinf = Phi(rinf, U)
    if np.linalg.norm(rinf - rho) > 1e-10:
        ok = False
check("C5 every B-diagonal state is fixed (pointer frame B einselected)", ok)
# a generic state stays polarized: relaxes to its own diagonal, not to I3/3
rho = rand_rho(d)
rinf = rho.copy()
for _ in range(300):
    rinf = Phi(rinf, U)
check("C5 generic state stays POLARIZED (P>0, not depolarized)",
      purity_above_floor(rinf) > 1e-3 and np.linalg.norm(rinf - I3) > 1e-2)
check("C5 recovers block-05 single-frame boundary: rinf = diag(rho0)",
      np.linalg.norm(rinf - np.diag(np.diag(rho))) < 1e-9)

print("\n=== C6: reducible T_U (U block-diagonal) -> multiple pointer states, NO depolarization ===")
U2 = haar_unitary(2)
U = np.eye(3, dtype=complex)
U[:2, :2] = U2          # mixes {e0,e1}, decouples e2
T = unistochastic(U)
nunit = int(np.sum(np.abs(np.linalg.eigvals(T) - 1) < 1e-9))
check("C6 reducible T_U has >=2 unit eigenvalues (>=2 ergodic classes)", nunit >= 2)
rho = rand_rho(3)
rinf = rho.copy()
for _ in range(400):
    rinf = Phi(rinf, U)
check("C6 generic state does NOT reach I3/3 (e2 sector survives)",
      np.linalg.norm(rinf - I3) > 1e-3)

print("\n=== C7: irreducible-but-periodic T_U (cyclic permutation U) -> unique fixed pt, oscillation ===")
# cyclic shift e0->e1->e2->e0
U = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)
T = unistochastic(U)
# stationary distribution(s)
w, V = np.linalg.eig(T.T)
nstat = int(np.sum(np.abs(w - 1) < 1e-9))
check("C7 cyclic-permutation T_U is irreducible: unique stationary distribution", nstat == 1)
# but multiple unit-MODULUS eigenvalues (period 3) -> no pointwise convergence
nperiph = int(np.sum(np.abs(np.abs(w) - 1) < 1e-9))
check("C7 periodic: >1 unit-modulus eigenvalue (period 3)", nperiph == 3)
p0 = np.array([0.6, 0.3, 0.1])
traj = []
p = p0.copy()
for _ in range(9):
    p = T @ p
    traj.append(p.copy())
osc = np.linalg.norm(traj[2] - traj[5]) < 1e-12 and np.linalg.norm(traj[0] - np.ones(3) / 3) > 1e-2
check("C7 Phi^n oscillates with period 3 (no pointwise relaxation)", osc)
cesaro = np.mean(np.array(traj[:9]).reshape(3, 3, 3).mean(axis=1), axis=0)  # avg over 9 steps == 3 full periods
check("C7 Cesaro (period) average IS I3/3", np.linalg.norm(np.mean(traj[:3], axis=0) - np.ones(3) / 3) < 1e-9)

print("\n=== C8: Perron-primitive T_U (no zero amplitude in B) -> UNIQUE pointer state I3/3, relaxation ===")
ok_unique = True
ok_relax = True
ok_strictpos = True
for _ in range(40):
    U = haar_unitary(d)
    T = unistochastic(U)
    if np.min(T) <= 0:
        ok_strictpos = False  # Haar U a.s. has strictly positive T_U
    w = np.linalg.eigvals(T)
    nperiph = int(np.sum(np.abs(np.abs(w) - 1) < 1e-9))
    if nperiph != 1:
        ok_unique = False     # primitive: 1 is the only unit-modulus eigenvalue
    rho = rand_rho(d)
    rinf = rho.copy()
    for _ in range(300):
        rinf = Phi(rinf, U)
    if np.linalg.norm(rinf - I3) > 1e-9:
        ok_relax = False
check("C8 Haar U gives strictly positive T_U (Perron-primitive sufficient condition)", ok_strictpos)
check("C8 Perron-primitive T_U: 1 is the unique unit-modulus eigenvalue", ok_unique)
check("C8 Phi^n(rho) -> I3/3 for every state (depolarization, single frame)", ok_relax)
# explicit sufficient condition: strictly positive T_U => Perron primitive => unique uniform stationary
U = haar_unitary(d)
T = unistochastic(U)
w, V = np.linalg.eig(T.T)
idx = np.argmin(np.abs(w - 1))
p = np.real(V[:, idx])
p = p / p.sum()
check("C8 strictly positive T_U has uniform stationary distribution", np.linalg.norm(p - np.ones(d) / d) < 1e-9)

print("\n=== C9: order parameter P = Tr(rho^2)-1/3 contracts in strictly positive witnesses ===")
check("C9 P = ||traceless(rho)||_F^2 (identity), and 0 iff rho=I3/3",
      all(abs(purity_above_floor(r) - np.linalg.norm(traceless(r)) ** 2) < 1e-12
          for r in [rand_rho(d) for _ in range(20)])
      and abs(purity_above_floor(I3)) < 1e-12)
U = haar_unitary(d)
rho = rand_rho(d)
seq = []
r = rho.copy()
for _ in range(40):
    r = Phi(r, U)
    seq.append(purity_above_floor(r))
mono = all(seq[i + 1] <= seq[i] + 1e-12 for i in range(len(seq) - 1))
check("C9 P decreases monotonically to 0 in the strictly positive witness", mono and seq[-1] < 1e-9)

print("\n=== C10: GUARD SU(3)-covariance does NOT imply contraction ===")
# identity channel: covariant under all g, but inert (no depolarization)
def conj(g, rho):
    return g @ rho @ g.conj().T
g = haar_unitary(d)
rho = rand_rho(d)
ident = lambda x: x
check("C10 identity channel is SU(3)-covariant", np.linalg.norm(ident(conj(g, rho)) - conj(g, ident(rho))) < 1e-12)
check("C10 identity channel is inert (no contraction of P)",
      abs(purity_above_floor(ident(rho)) - purity_above_floor(rho)) < 1e-12)
# Phi itself is NOT SU(3)-covariant (the frame B breaks it) -- covariance is instrument-inherited
U = haar_unitary(d)
lhs = Phi(conj(g, rho), U)
rhs = conj(g, Phi(rho, U))
check("C10 Phi is frame-fixed (NOT globally SU(3)-covariant): a named-frame admission",
      np.linalg.norm(lhs - rhs) > 1e-3)

print("\n=== C11: RELOCATION gate -- single-frame depolarization <=> T_U Perron primitive (open input) ===")
# Decision table: depolarization to I3/3 happens exactly in the primitive column.
cases = {
    "commuting [U,B]=0": np.diag(np.exp(1j * rng.standard_normal(d))),
    "block-diagonal": (lambda: (lambda U: U)(np.block([[haar_unitary(2), np.zeros((2, 1))],
                                                       [np.zeros((1, 2)), np.array([[1.0]])]]).astype(complex)))(),
    "cyclic permutation": np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex),
    "Haar (primitive)": haar_unitary(d),
}
def depolarizes(U):
    rho = rand_rho(d)
    r = rho.copy()
    for _ in range(400):
        r = Phi(r, U)
    return np.linalg.norm(r - I3) < 1e-8
results = {k: depolarizes(U) for k, U in cases.items()}
check("C11 only the Perron-primitive (Haar witness) case depolarizes",
      results["Haar (primitive)"] and not results["commuting [U,B]=0"]
      and not results["block-diagonal"] and not results["cyclic permutation"])
# the verdict is a function of T_U = |U_ij|^2 ALONE: U and its diagonal-phase
# dressings share the same T_U and the same depolarization verdict. So the criterion
# is the alignment magnitude of the matter unitary to the record frame B -- not a
# phase convention and not anything Record supplies (neither frame nor alignment).
U = haar_unitary(d)
L = np.diag(np.exp(1j * rng.standard_normal(d)))
R = np.diag(np.exp(1j * rng.standard_normal(d)))
Udress = L @ U @ R
check("C11 T_U is invariant under diagonal-phase dressing of U",
      np.linalg.norm(unistochastic(U) - unistochastic(Udress)) < 1e-12)
check("C11 same T_U => same depolarization verdict (criterion depends on T_U only)",
      depolarizes(U) == depolarizes(Udress))

print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
