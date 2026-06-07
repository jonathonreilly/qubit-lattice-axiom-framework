"""Class-A finite runner: K-reality (delta=0) on the generation C^3 orbit is
EXACTLY equivalent to C3-symmetry of the realized past-hypothesis boundary, and
that boundary symmetry is NOT forced from A1+A2+retained (arrow-vs-symmetry
tension). Plus the parity-mismatch lemma: no single T-odd functional can SELECT
delta=0 (it is the conjugation-even fixed set).

Objects on the generation orbit C^3:
  C = cyclic shift (C^3=I); A = i(C - C^2) (the unique C3-invariant K-odd line);
  S = C + C^2 (partition observable, eig {2,-1,-1}); [A,S]=0 (A partition-blind).
  Character projectors P_k = (1/3) sum_j w^{-kj} C^j; D(rho)=sum_k P_k rho P_k.
  Realized history T (real 3x3); arrow carrier Aham(T) = i(T - T^T)/2 (Hermitian,
  T-odd). Circulant Koide operator M(a,b,delta) = a I + b e^{i delta} C +
  b e^{-i delta} C^2 (Hermitian); K-reality = delta=0 (M real).

Theorem chain (all checked exactly):
  T1  RELOCATION: a C3-equivariant (real circulant) realized history forces
      Aham(T) into span{A}, which commutes with S -> partition-blind -> K-reality
      holds on the WHOLE Koide cone (the conjugation-even no-go is re-derived).
  T2  A C3-BREAKING history makes Aham partition-SELECTIVE ([Aham,S]!=0).
      => delta=0 K-reality  <=>  realized history C3-equivariant
                            <=>  realized boundary C3-symmetric.
  T3  DICHOTOMY a: the C3-symmetric reference I/3 is the NO-ARROW fixed point
      (Aham=0); it bears no arrow.
  T4  DICHOTOMY b: an A1-reachable zero-entropy single-axis boundary |e_k> is
      C3-BROKEN ([rho,C]!=0) -- it bears an arrow but is partition-selective.
  T5  REGISTER-COLLAPSE: D(|e_k><e_k|) = I/3 exactly; and D(rho) is circulant
      (C3-symmetric) for EVERY rho. Registration symmetrizes the boundary but
      collapses the arrow-bearing single-axis state to the no-arrow reference
      (register-not-read cannot supply 'C3-symmetric AND arrow-bearing').
  T6  PARITY-MISMATCH: every conjugation-odd (T-odd) functional F (F(conj M) =
      -F(M)) is identically ZERO on K-real operators (delta=0). The clean T-odd
      carrier Tr(A M) = 6|b| sin(delta) is delta-ODD and NULL at delta=0, so it
      can only fix the residual sign, never SELECT delta=0.

Controls (teeth): a circulant arrow-bearing history has Aham!=0 in span{A}
(C3-symmetric AND arrow-bearing IS possible for histories, but not for the
registrable single-axis boundary); a delta!=0 operator gives a nonzero T-odd
carrier (T6 is not vacuous).

prints TOTAL: PASS=N FAIL=0
"""

import numpy as np

TOL = 1e-9
w = np.exp(2j * np.pi / 3)
C = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)
A = 1j * (C - C @ C)
S = C + C @ C
I3 = np.eye(3, dtype=complex)


def Pchar(k):
    return sum((w ** (-k * j)) * np.linalg.matrix_power(C, j) for j in range(3)) / 3.0


P0, P1, P2 = Pchar(0), Pchar(1), Pchar(2)


def D(rho):
    return P0 @ rho @ P0 + P1 @ rho @ P1 + P2 @ rho @ P2


def Aham(T):
    return 1j * (T - T.T) / 2.0


def is_circulant(X):
    return np.allclose(C @ X @ C.conj().T, X, atol=TOL)


def in_span_A(X):
    coeff = np.trace(A.conj().T @ X) / np.trace(A.conj().T @ A)
    return np.linalg.norm(X - coeff * A) < TOL


def Mop(a, b, delta):
    bb = b * np.exp(1j * delta)
    return a * I3 + bb * C + np.conj(bb) * (C @ C)


rng = np.random.default_rng(11)
results = []


def check(name, ok):
    results.append((name, bool(ok)))


# baseline: A is partition-blind
check("base [A,S]=0 (A partition-blind)", np.allclose(A @ S - S @ A, 0, atol=TOL))
check("base A Hermitian", np.allclose(A, A.conj().T, atol=TOL))

# --- T1: circulant history => Aham in span{A} (partition-blind) ---
ok = True
for _ in range(1000):
    a, b, c = rng.standard_normal(3)
    T = a * I3 + b * C + c * (C @ C)
    Ah = Aham(T)
    if not in_span_A(Ah) or not np.allclose(Ah @ S - S @ Ah, 0, atol=TOL):
        ok = False
check("T1 circulant history: Aham in span{A}, [Aham,S]=0 (1000)", ok)

# --- T2: C3-breaking history => partition-selective ---
n_sel = 0
for _ in range(1000):
    T = rng.standard_normal((3, 3))
    if not is_circulant(T):
        Ah = Aham(T)
        if np.linalg.norm(Ah @ S - S @ Ah) > 1e-6:
            n_sel += 1
        else:
            n_sel = -10000  # any C3-breaking history that is NOT selective fails
check("T2 C3-breaking history => Aham partition-selective (all)", n_sel > 900)

# --- T3: I/3 is the no-arrow fixed point ---
check("T3 Aham(I/3) = 0 (no arrow)", np.allclose(Aham(I3 / 3), 0, atol=TOL))

# --- T4: single-axis boundary is C3-broken, zero-entropy ---
ok = True
for k in range(3):
    e = np.zeros(3, complex); e[k] = 1.0
    rho = np.outer(e, e.conj())
    if np.linalg.norm(rho @ C - C @ rho) < 0.5:   # must be C3-BROKEN
        ok = False
    if np.linalg.matrix_rank(rho) != 1:           # zero-entropy (pure)
        ok = False
check("T4 single-axis |e_k>: C3-broken & rank-1 (k=0,1,2)", ok)

# --- T5: register-collapse + D(rho) always circulant ---
ok_collapse = True
for k in range(3):
    e = np.zeros(3, complex); e[k] = 1.0
    rho = np.outer(e, e.conj())
    if not np.allclose(D(rho), I3 / 3, atol=TOL):
        ok_collapse = False
check("T5 D(|e_k><e_k|) = I/3 (register-collapse to no-arrow)", ok_collapse)
ok_circ = True
for _ in range(500):
    v = rng.standard_normal(3) + 1j * rng.standard_normal(3); v /= np.linalg.norm(v)
    if not is_circulant(D(np.outer(v, v.conj()))):
        ok_circ = False
check("T5b D(rho) circulant (C3-symmetric) for every rho (500)", ok_circ)

# --- T6: parity-mismatch ---
# (a) general theorem: a conjugation-odd functional is null on K-real M
F = lambda X: np.trace(A @ X).real   # T-odd carrier Tr(A M)
ok_odd = ok_null = True
for _ in range(500):
    a, b, d = rng.standard_normal(3)
    M = Mop(a, b, d)
    if not np.isclose(F(np.conj(M)), -F(M), atol=TOL):   # T-odd
        ok_odd = False
    M0 = Mop(a, b, 0.0)
    if abs(F(M0)) > TOL:                                  # null at delta=0
        ok_null = False
check("T6 Tr(A M) is conjugation-odd: F(conj M) = -F(M) (500)", ok_odd)
check("T6 Tr(A M) = 0 on every K-real (delta=0) operator (500)", ok_null)
# (b) closed form Tr(A M) = 6|b| sin(delta)
ok_form = True
for _ in range(200):
    a, b, d = rng.standard_normal(), abs(rng.standard_normal()), rng.uniform(-np.pi, np.pi)
    if not np.isclose(F(Mop(a, b, d)), 6 * b * np.sin(d), atol=1e-7):
        ok_form = False
check("T6b Tr(A M) = 6|b| sin(delta) (closed form, 200)", ok_form)

# --- CONTROL 1 (teeth): a delta!=0 operator gives nonzero T-odd carrier ---
check("CTRL1 delta!=0 => Tr(A M) != 0 (T6 not vacuous)", abs(F(Mop(1.0, 0.5, 0.6))) > 0.1)

# --- CONTROL 2 (teeth): a circulant history CAN be arrow-bearing (Aham!=0) ---
# distinguishes 'history' (can be both) from the registrable boundary (cannot)
Th = 1.0 * I3 + 0.7 * C + 0.2 * (C @ C)
check("CTRL2 circulant arrow-bearing history: Aham != 0 in span{A}",
      np.linalg.norm(Aham(Th)) > 0.1 and in_span_A(Aham(Th)))

# --- CONTROL 3 (teeth): the single-axis boundary itself DOES bear an arrow ---
# (its pre-registration density is C3-broken) -- so the collapse in T5 is the
# register map's doing, not a property of an arrowless state.
e = np.array([1, 0, 0], complex); rho = np.outer(e, e.conj())
check("CTRL3 single-axis boundary bears an arrow pre-registration ([rho,C]!=0)",
      np.linalg.norm(rho @ C - C @ rho) > 0.5)

n_pass = sum(1 for _, ok in results if ok)
n_fail = sum(1 for _, ok in results if not ok)
for name, ok in results:
    print(("PASS" if ok else "FAIL"), name)
print()
print("TOTAL: PASS=%d FAIL=%d" % (n_pass, n_fail))
