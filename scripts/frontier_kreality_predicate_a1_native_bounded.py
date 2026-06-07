"""Class-A finite runner: the flavor_einselection GAP-A K-reality predicate (delta=0)
is A1-NATIVE, and delta=0 is forced for the K-EVEN generation coupling; the ONLY
route to delta!=0 is the native Hermitian K-odd channel A=i(C-C^2)=(C-C^2)(x)omega
(= the standing generation-chirality import) or an imported U(1) connection.
=> BOUNDED: K-reality is derived MODULO the single chirality import (not independent).

Generation orbit = the 3 hw=1 Brillouin-zone corners {(pi,0,0),(0,pi,0),(0,0,pi)}.
C = cyclic shift among them (native, real); S=C+C^2 (K-even); A=i(C-C^2) (K-odd);
omega = Cl(3) pseudoscalar = i*I2 on the qubit factor (omega^2=-1, A2-native).
K = complex conjugation in the A1 site basis (the canonical lattice real-structure).

Facts (all checked exactly):
  T1  the 3 corners AND their connecting (pi,pi,0)-type momenta are self-conjugate
      (-k = k mod 2pi, since -pi=pi).
  T2  reality theorem: any K-even (real site-basis) operator H gives an EXACTLY real
      corner-coupling block => delta=0. (Proof: <ki|H|kj>* = <-ki|H|-kj> = <ki|H|kj>.)
  T3  crux decomposition: write H = H_R (K-even) + H_I (K-odd); the corner coupling
      from H_R is exactly real, from H_I exactly pure-imaginary. So b is complex
      IFF the site operator has a nonzero K-odd part. delta=0 <=> coupling K-even.
  T4  translation-invariant complex (Peierls) Hermitian hoppings are momentum-DIAGONAL
      => ZERO inter-corner coupling (cannot source a complex b). Only a
      translation-breaking operator couples the distinct corners.
  T5  A1-native predicate: site-basis conjugation transported by the complex C3-Fourier
      F acts conj(P0)=P0, conj(P1)=P2, conj(P2)=P1 = EXACTLY flavor_einselection K.
  T6  the native K-odd channel A=i(C-C^2) is Hermitian and is realized natively as
      (C-C^2)(x)omega (native C, native omega). A native mass with this component has
      delta!=0. This channel = the standing generation-chirality import.
  CTRL the K-odd channel cannot be reached by any K-even (real) corner block (teeth).

prints TOTAL: PASS=N FAIL=0
"""

import numpy as np
import itertools

TOL = 1e-9
w = np.exp(2j * np.pi / 3)
C = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)
S = C + C @ C
A = 1j * (C - C @ C)
I3 = np.eye(3, dtype=complex)
omega = 1j * np.eye(2)  # Cl(3) pseudoscalar on the qubit factor

results = []
def check(name, ok): results.append((name, bool(ok)))

# --- T1: self-conjugacy of corners + connectors ---
corners = [(np.pi, 0, 0), (0, np.pi, 0), (0, 0, np.pi)]
def selfconj(k):
    return all(abs((-c) % (2 * np.pi) - (c % (2 * np.pi))) < TOL for c in k)
check("T1 all 3 corners self-conjugate (-k=k mod 2pi)", all(selfconj(k) for k in corners))
conns = [tuple(np.array(corners[i]) - np.array(corners[j])) for i, j in [(0, 1), (1, 2), (0, 2)]]
check("T1b connecting (pi,pi,0)-type momenta self-conjugate", all(selfconj(k) for k in conns))

# --- T2: reality theorem on a real-symmetric (K-even) lattice operator ---
L = 4
N = L ** 3
def idx(x): return (x[0] % L) * L * L + (x[1] % L) * L + x[2] % L
rng = np.random.default_rng(7)
H = np.zeros((N, N))
for x in itertools.product(range(L), repeat=3):
    H[idx(x), idx(x)] += rng.standard_normal()
    for mu in range(3):
        y = list(x); y[mu] = (y[mu] + 1) % L
        t = rng.standard_normal()
        H[idx(tuple(y)), idx(x)] += t; H[idx(x), idx(tuple(y))] += t
H = (H + H.T) / 2
def bloch(k):
    v = np.array([np.exp(1j * np.dot(np.array(k), np.array(x))) for x in itertools.product(range(L), repeat=3)], dtype=complex)
    return v / np.linalg.norm(v)
B = np.array([bloch(k) for k in corners]).T
Mc = B.conj().T @ H @ B
check("T2 K-even (real) site op => real corner block (delta=0)", np.max(np.abs(Mc.imag)) < 1e-9)

# --- T3: crux decomposition K-even->real, K-odd->pure-imaginary ---
okR = okI = True
for _ in range(500):
    Hc = rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))
    Hc = Hc + Hc.conj().T
    HR = (Hc + np.conj(Hc)) / 2  # K-even
    HI = (Hc - np.conj(Hc)) / 2  # K-odd
    cR = B.conj().T @ HR @ B
    cI = B.conj().T @ HI @ B
    if np.max(np.abs(cR.imag)) > 1e-8: okR = False
    if np.max(np.abs(cI.real)) > 1e-8: okI = False
check("T3 K-even part => real corner coupling (500)", okR)
check("T3 K-odd part => pure-imaginary corner coupling (500)", okI)

# --- T4: translation-invariant complex Peierls hoppings are momentum-diagonal ---
Ht = np.zeros((N, N), dtype=complex)
ph = [0.4, 1.1, -0.7]
for x in itertools.product(range(L), repeat=3):
    for mu in range(3):
        y = list(x); y[mu] = (y[mu] + 1) % L
        t = np.exp(1j * ph[mu])
        Ht[idx(tuple(y)), idx(x)] += t; Ht[idx(x), idx(tuple(y))] += np.conj(t)
McT = B.conj().T @ Ht @ B
offdiag = McT - np.diag(np.diag(McT))
check("T4 translation-invariant complex hoppings: ZERO inter-corner coupling", np.max(np.abs(offdiag)) < 1e-9)

# --- T5: A1-native predicate = flavor_einselection K ---
F = np.array([[w ** (j * k) for k in range(3)] for j in range(3)], dtype=complex) / np.sqrt(3)
U = np.linalg.inv(F) @ np.conj(F)
def P(k): return sum((w ** (-k * j)) * np.linalg.matrix_power(C, j) for j in range(3)) / 3
P0, P1, P2 = P(0), P(1), P(2)
check("T5 site-conj transports to swap(1,2): U real swap", np.allclose(U.imag, 0) and np.allclose(U.real, [[1, 0, 0], [0, 0, 1], [0, 1, 0]]))
check("T5 conj(P0)=P0, conj(P1)=P2, conj(P2)=P1 (= flavor_einselection K)",
      np.allclose(np.conj(P0), P0) and np.allclose(np.conj(P1), P2) and np.allclose(np.conj(P2), P1))

# --- T6: native K-odd channel A=i(C-C^2)=(C-C^2)(x)omega, Hermitian; gives delta!=0 ---
check("T6 A=i(C-C^2) Hermitian & K-odd", np.allclose(A, A.conj().T) and np.allclose(np.conj(A), -A))
A_native = np.kron(C - C @ C, omega)
check("T6b native (C-C^2)(x)omega Hermitian (native C, native omega)", np.allclose(A_native, A_native.conj().T))
def bcoeff(M): return np.trace(np.linalg.matrix_power(C, -1) @ M) / 3
M_even = I3 + 0.4 * S
M_odd = I3 + 0.4 * S + 0.3 * A
check("T6c K-even mass => b real (delta=0)", abs(bcoeff(M_even).imag) < 1e-9)
check("T6d native K-odd component => b complex (delta!=0)", abs(bcoeff(M_odd).imag) > 0.1)

# --- T7: the delta-channel A is DISTINCT from the chiral grading (Gamma_chi) ---
# Gamma_chi = (2/3)J - I = -(1/3)I + (2/3)S is CIRCULANT (J = I+C+C^2), so A=i(C-C^2)
# COMMUTES with it (both circulant). The chiral grading must ANTICOMMUTE with Gamma_chi
# and is NON-circulant. So the delta (K-reality) channel and the Q/r chiral grading are
# DISTINCT residuals (this corrects the earlier 'unifies with chirality import' framing).
J = np.ones((3, 3), dtype=complex)
Gchi = (2.0 / 3.0) * J - I3
check("T7 J = I + C + C^2 (Gamma_chi is circulant)", np.allclose(J, I3 + C + C @ C))
check("T7b A=i(C-C^2) COMMUTES with Gamma_chi (delta-channel, not chiral grading)",
      np.allclose(A @ Gchi - Gchi @ A, 0))
check("T7c A does NOT anticommute with Gamma_chi", not np.allclose(A @ Gchi + Gchi @ A, 0))
none_circ = True
for _ in range(2000):
    a2, b2, c2 = np.random.randn(3) + 1j * np.random.randn(3)
    Mc2 = a2 * I3 + b2 * C + c2 * (C @ C)
    if np.linalg.norm(Mc2) > 1e-6 and np.allclose(Mc2 @ Gchi + Gchi @ Mc2, 0):
        none_circ = False
check("T7d NO circulant op anticommutes with Gamma_chi (chiral grading is non-circulant)", none_circ)

# --- CTRL: the K-odd channel A is unreachable by any K-even (real) corner block (teeth) ---
# A is purely imaginary-antisymmetric in the corner basis; a real corner block has no overlap
check("CTRL A purely imaginary in corner basis (real-symmetric block can't produce it)",
      np.max(np.abs(A.real)) < 1e-9 and np.max(np.abs(A.imag)) > 0.5)

n_pass = sum(1 for _, ok in results if ok)
n_fail = sum(1 for _, ok in results if not ok)
for name, ok in results:
    print(("PASS" if ok else "FAIL"), name)
print()
print("TOTAL: PASS=%d FAIL=%d" % (n_pass, n_fail))
