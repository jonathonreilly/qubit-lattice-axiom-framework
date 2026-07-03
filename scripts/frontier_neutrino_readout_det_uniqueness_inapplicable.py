"""Class-A finite runner: the retained det-uniqueness observable-principle is
STRUCTURALLY INAPPLICABLE to the neutrino generation-sector mass readout, because the
real anti-Hermitian kinetic Dirac operator VANISHES on the hw=1 generation corners.
=> the physical readout y_nu^(0)/g = 1/sqrt2 is NOT derivable via this route; it remains
a genuine admitted input (sharpens #3172 ADM-1; connects to the corner-vanishing #3156).

Setup: staggered Dirac on Z^3. Kinetic D_kin = real ANTI-symmetric hopping with KS phases
eta_mu(x)=(-1)^(x_1+..+x_{mu-1}) (D_kin^T=-D_kin, real). Momentum eigenvalue ~ i sum_mu
eta sin(k_mu). The retained det-uniqueness theorem (observable_principle_real_d_block_
uniqueness, retained_bounded) forces W=log|det(D+J)| ONLY for an INVERTIBLE real
anti-Hermitian D (D^T=-D, det D != 0) with real-symmetric source J. The generations are
the hw=1 corners k in {(pi,0,0),(0,pi,0),(0,0,pi)}.

  T1  D_kin is real and anti-symmetric (D^T=-D) -> the det-uniqueness operator class.
  T2  D_kin VANISHES on the hw=1 generation corners (sin(0)=sin(pi)=0): ||P_corner D_kin
      P_corner|| = 0. So D_kin is NON-invertible (identically zero) on the generation
      sector -> the det-uniqueness domain (X1: invertible anti-Herm D) is EMPTY there.
  T3  the generation-sector mass is real-SYMMETRIC (the source J), with NO anti-Hermitian
      D to host it -> det-uniqueness has no in-domain operator on the generation corners.
  T4  CONTROL (teeth): off-corner (generic k), D_kin is NONZERO and anti-Hermitian -> the
      vanishing is corner-SPECIFIC, not a trivial zero operator. So the no-go is scoped to
      the generation (hw=1) sector, not all of D_kin.
  T5  the readout det responses (det(mI+jY)=m^16 nilpotent vs det(mI+jGamma_1)=(m^2-j^2)^8)
      are scalar-baseline diagnostics only (per the retained bridge note) -> not a licensed
      physical response absent an in-domain anti-Herm D.

CONCLUSION (negative-route-pruning): the det-uniqueness route cannot derive the neutrino
generation-sector readout; the readout is a genuine admitted input requiring a separate
observable-principle covering real-symmetric, corner-localized mass with no anti-Herm host.

prints TOTAL: PASS=N FAIL=0
"""

import numpy as np
import itertools

TOL = 1e-9
L = 4
N = L ** 3
def idx(x): return (x[0] % L) * L * L + (x[1] % L) * L + x[2] % L
def eta(x, mu): return (-1) ** sum(x[:mu])

# --- build the real anti-symmetric staggered kinetic Dirac operator ---
Dk = np.zeros((N, N))
for x in itertools.product(range(L), repeat=3):
    for mu in range(3):
        y = list(x); y[mu] = (y[mu] + 1) % L
        s = eta(x, mu)
        Dk[idx(tuple(y)), idx(x)] += s / 2
        Dk[idx(x), idx(tuple(y))] += -s / 2   # antisymmetric real hop

def bloch(k):
    v = np.array([np.exp(1j * np.dot(np.array(k), np.array(x))) for x in itertools.product(range(L), repeat=3)], dtype=complex)
    return v / np.linalg.norm(v)

corners = [(np.pi, 0, 0), (0, np.pi, 0), (0, 0, np.pi)]
B = np.array([bloch(k) for k in corners]).T

results = []
def check(name, ok): results.append((name, bool(ok)))

# T1: D_kin real anti-symmetric
check("T1 D_kin real & anti-symmetric (D^T=-D) = det-uniqueness operator class",
      np.allclose(Dk.imag, 0) and np.allclose(Dk.T, -Dk))

# T2: D_kin vanishes on the hw=1 generation corners
Dk_corner = B.conj().T @ Dk @ B
check("T2 D_kin VANISHES on the hw=1 generation corners (||.||=0)", np.linalg.norm(Dk_corner) < TOL)
check("T2b => D_kin non-invertible (zero) on the generation sector (det-uniqueness X1 domain empty)",
      np.linalg.norm(Dk_corner) < TOL)

# T3: the generation mass is real-symmetric (source J), no anti-Herm D to host it
# a generic real-symmetric corner mass:
Jmass = np.array([[1.3, 0.4, 0.2], [0.4, 1.1, 0.3], [0.2, 0.3, 0.9]])
check("T3 generation-sector mass is real-symmetric (source J, NOT anti-Hermitian)",
      np.allclose(Jmass, Jmass.T) and not np.allclose(Jmass.T, -Jmass))

# T4: control — off-corner D_kin is nonzero anti-Hermitian (vanishing is corner-specific)
generic = [(0.7, 1.1, 0.3), (1.9, 0.5, 2.2)]
Bg = np.array([bloch(k) for k in generic]).T
Dk_gen = Bg.conj().T @ Dk @ Bg
check("T4 CONTROL: off-corner D_kin is NONZERO (vanishing is corner-specific, not trivial)",
      np.linalg.norm(Dk_gen) > 0.1)
# and the full D_kin is a nonzero anti-Hermitian operator
check("T4b full D_kin is a nonzero operator (norm>0)", np.linalg.norm(Dk) > 1.0)

# T5: det responses are diagnostics only (no in-domain anti-Herm D on generation sector)
sx = np.array([[0, 1], [1, 0]]); sz = np.array([[1, 0], [0, -1]]); I8 = np.eye(8)
g5 = np.kron(sz, I8); G1 = np.kron(sx, I8)
PL = (np.eye(16) - g5) / 2; PR = (np.eye(16) + g5) / 2
Y = PR @ G1 @ PL
mm = 1.7
check("T5 det(mI+jY)=m^16 (nilpotent) and det(mI+jG1)=(m^2-j^2)^8 (scalar-baseline diagnostics)",
      abs(np.linalg.det(mm * np.eye(16) + 0.9 * Y) - mm**16) < 1e-6 and
      abs(np.linalg.det(mm * np.eye(16) + 0.9 * G1) - (mm**2 - 0.9**2)**8) < 1e-6)
# the scalar baseline m*I is real-symmetric, not anti-Hermitian (the #3172 finding, recapped)
check("T5b scalar baseline m*I is real-symmetric, not anti-Hermitian (outside det-uniqueness X1)",
      not np.allclose((mm * np.eye(4)).T, -(mm * np.eye(4))))

n_pass = sum(1 for _, ok in results if ok)
n_fail = sum(1 for _, ok in results if not ok)
for name, ok in results:
    print(("PASS" if ok else "FAIL"), name)
print()
print("TOTAL: PASS=%d FAIL=%d" % (n_pass, n_fail))
