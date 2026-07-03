"""Class-A finite runner: the RECORD registration map RE-INSTANTIATES the
Koide chirality no-go on the generation C^3 orbit, rather than dissolving it.

Decisive facts (all checked exactly on the 3x3 generation orbit):

  G := Gamma_chi = (2/3) J - I   (J = all-ones 3x3), the Z_3 chiral grading of
  the retained koide_anticommuting_operator_derivation_theorem. eig(G)={+1,-1,-1}.

  The C_3-character central-sector projectors P_k = (1/3) sum_j w^{-kj} C^j
  (C = cyclic shift, w = e^{2pi i/3}) are exactly the G-eigenspaces:
  P_0 in the +1 eigenspace, P_1,P_2 in the -1 eigenspace.

  Registration map D(M) = sum_k P_k M P_k. Because the partition blocks are
  G-eigenspaces, D commutes with conjugation by G, hence D ANNIHILATES every
  G-anticommuting Hermitian operator: {M,G}=0 => D(M)=0. This holds for BOTH
  the 3-block character partition and the 2-block singlet|doublet partition.

  The Q=2/3 mass carrier anticommutes with G (retained theorem), so D never
  registers it; D registers only the C_3-equivariant (circulant) family, whose
  Koide value is Q=1. Register-not-read therefore re-instantiates the no-go.

Control checks give the runner teeth: D registers circulant operators
(non-trivially), and a partition whose blocks STRADDLE the G-eigenspaces would
register the carrier -- but that partition is not the C_3 central-sector / K-real
decomposition (the forbidden A3 over-reach that got the #2972 route rejected).

prints TOTAL: PASS=N FAIL=0
"""

import numpy as np

TOL = 1e-9
w = np.exp(2j * np.pi / 3)
C = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)  # cyclic shift, C^3=I
J = np.ones((3, 3), dtype=complex)
I3 = np.eye(3, dtype=complex)
G = (2.0 / 3.0) * J - I3  # Gamma_chi


def Pchar(k):
    return sum((w ** (-k * j)) * np.linalg.matrix_power(C, j) for j in range(3)) / 3.0


P0, P1, P2 = Pchar(0), Pchar(1), Pchar(2)
Pd = P1 + P2  # doublet projector


def herm(rng):
    A = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))
    return A + A.conj().T


def anticommuting_part(M):
    # (M - G M G)/2 anticommutes with G for any M
    return (M - G @ M @ G) / 2.0


def commuting_part(M):
    return (M + G @ M @ G) / 2.0


def D3(M):
    return P0 @ M @ P0 + P1 @ M @ P1 + P2 @ M @ P2


def D2(M):
    return P0 @ M @ P0 + Pd @ M @ Pd


def is_circulant(M):
    return np.allclose(C @ M @ C.conj().T, M, atol=TOL)


results = []


def check(name, ok):
    results.append((name, bool(ok)))


# --- T1: Gamma_chi eigenvalues are {+1,-1,-1} ---
ev = np.sort(np.linalg.eigvalsh(G))
check("T1 Gamma_chi eig = {-1,-1,+1}", np.allclose(ev, [-1, -1, 1], atol=TOL))
check("T1b Gamma_chi^2 = I", np.allclose(G @ G, I3, atol=TOL))

# --- T2: character projectors are a resolution of identity, orthogonal ---
check("T2 sum P_k = I", np.allclose(P0 + P1 + P2, I3, atol=TOL))
check("T2b P_k orthogonal idempotent",
      all(np.allclose(Pa @ Pb, (Pa if i == j else 0 * I3), atol=TOL)
          for i, Pa in enumerate([P0, P1, P2]) for j, Pb in enumerate([P0, P1, P2])))

# --- T3: the character partition blocks ARE Gamma_chi-eigenspaces ---
check("T3 G P0 = +P0  (singlet in +1 eigenspace)", np.allclose(G @ P0, +P0, atol=TOL))
check("T3 G P1 = -P1  (doublet char in -1 eigenspace)", np.allclose(G @ P1, -P1, atol=TOL))
check("T3 G P2 = -P2  (doublet char in -1 eigenspace)", np.allclose(G @ P2, -P2, atol=TOL))
check("T3b G Pd = -Pd  (doublet block in -1 eigenspace)", np.allclose(G @ Pd, -Pd, atol=TOL))

# --- T4: D commutes with conjugation by G (both partitions) ---
rng = np.random.default_rng(7)
ok3 = ok2 = True
for _ in range(2000):
    M = herm(rng)
    if not np.allclose(D3(G @ M @ G), G @ D3(M) @ G, atol=TOL):
        ok3 = False
    if not np.allclose(D2(G @ M @ G), G @ D2(M) @ G, atol=TOL):
        ok2 = False
check("T4 D3 commutes with conj-by-G (2000 trials)", ok3)
check("T4 D2 commutes with conj-by-G (2000 trials)", ok2)

# --- T5: D ANNIHILATES every Gamma_chi-anticommuting Hermitian operator ---
ok3 = ok2 = anti_ok = True
for _ in range(3000):
    M = anticommuting_part(herm(rng))
    if np.linalg.norm(M) < TOL:
        continue
    if not np.allclose(G @ M + M @ G, 0, atol=TOL):
        anti_ok = False
    if not np.allclose(D3(M), 0, atol=TOL):
        ok3 = False
    if not np.allclose(D2(M), 0, atol=TOL):
        ok2 = False
check("T5 carriers genuinely anticommute with G", anti_ok)
check("T5 D3 annihilates ALL anticommuting carriers (3000)", ok3)
check("T5 D2 annihilates ALL anticommuting carriers (3000)", ok2)

# --- T6: the explicit 4 canonical anticommuting carriers also give D=0 ---
# any anticommuting carrier is supported on the off-(+1,-1)-block; build a basis
plus = P0
minus = Pd
basis_carriers = []
# off-diagonal generators between the +1 (1-dim) and -1 (2-dim) eigenspaces
# parametrize by mapping the singlet to each doublet character and h.c.
s = np.array([1, 1, 1], dtype=complex) / np.sqrt(3)
for d in [np.array([2, -1, -1], complex) / np.sqrt(6),
          np.array([0, 1, -1], complex) / np.sqrt(2)]:
    Msd = np.outer(s, d.conj()) + np.outer(d, s.conj())          # real off-block
    Msd_i = 1j * (np.outer(s, d.conj()) - np.outer(d, s.conj()))  # imag off-block
    basis_carriers += [Msd, Msd_i]
ok = True
for M in basis_carriers:
    if not np.allclose(G @ M + M @ G, 0, atol=TOL):
        ok = False
    if not (np.allclose(D3(M), 0, atol=TOL) and np.allclose(D2(M), 0, atol=TOL)):
        ok = False
check("T6 all 4 explicit anticommuting carriers: anticommute & D=0", ok)

# --- CONTROL 1 (teeth): D registers circulant (G-commuting) operators ---
# S = C + C^2 is circulant, commutes with G; D must register it (D(S) != 0)
S = C + C @ C
check("CTRL1 S=C+C^2 is circulant", is_circulant(S))
check("CTRL1 [S,G]=0 (G-commuting)", np.allclose(S @ G - G @ S, 0, atol=TOL))
check("CTRL1 D3(S) = S (registered, NOT annihilated)", np.allclose(D3(S), S, atol=TOL))
check("CTRL1 D registers a nonzero circulant op", np.linalg.norm(D3(S)) > 0.5)

# --- CONTROL 2 (teeth): a STRADDLING partition DOES register a carrier ---
# partition {span(s,u1)} | {span(u2)} straddles the G-eigenspaces; it registers
# the singlet<->u1 carrier. This is the forbidden A3 move (not a C_3 central
# decomposition); it shows the annihilation is partition-specific, not vacuous.
u1 = np.array([2, -1, -1], complex) / np.sqrt(6)
u2 = np.array([0, 1, -1], complex) / np.sqrt(2)
PA = np.outer(s, s.conj()) + np.outer(u1, u1.conj())
PB = np.outer(u2, u2.conj())
carrier = np.outer(s, u1.conj()) + np.outer(u1, s.conj())  # anticommutes with G
check("CTRL2 carrier anticommutes with G", np.allclose(G @ carrier + carrier @ G, 0, atol=TOL))
check("CTRL2 char-partition D3 annihilates it", np.allclose(D3(carrier), 0, atol=TOL))
straddle_D = PA @ carrier @ PA + PB @ carrier @ PB
check("CTRL2 straddling partition REGISTERS it (D!=0)", np.linalg.norm(straddle_D) > 0.5)
check("CTRL2 straddling blocks are NOT C_3-invariant (not a central decomposition)",
      not np.allclose(C @ PA @ C.conj().T, PA, atol=TOL))

# --- T7: the registered family is circulant => Koide value Q=1 (not 2/3) ---
# D3(M) is always circulant (commutes with C); spot-check
ok = all(is_circulant(D3(herm(rng))) for _ in range(500))
check("T7 D3(M) is always circulant (registers only Q=1 family)", ok)

n_pass = sum(1 for _, ok in results if ok)
n_fail = sum(1 for _, ok in results if not ok)
for name, ok in results:
    print(("PASS" if ok else "FAIL"), name)
print()
print("TOTAL: PASS=%d FAIL=%d" % (n_pass, n_fail))
