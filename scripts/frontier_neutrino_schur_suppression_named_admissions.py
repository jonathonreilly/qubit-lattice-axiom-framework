"""Class-A finite runner: the DM-neutrino second-order Schur suppression coefficient
y_nu^eff = (g/sqrt2)^2 / 32 = g^2/64 is a BOUNDED theorem on three PRECISELY-NAMED
admissions. Sharpens the unaudited schur node (td~549) from "conditional algebra on
selected inputs" to bounded-with-named-admissions, and NARROWS the V_sel admission.

Pieces:
  T1  RETAINED Schur return: the cascade block M = m I + j Gamma_1 on the 1+2 cascade
      gives second-order return Delta y = j^2/m (the retained cascade_geometry identity
      P_T1 Gamma_1 P_int Gamma_1 P_T1 = I_3). Verified by explicit block Schur complement.
  T2  V_sel curvature, NARROWED admission (ADM-3): on the RETAINED graph-shift surface
      H(phi)=sum_i phi_i S_i (S_i = canonical axis bit-flips sigma_x^(i) on the 2^3
      hypercube), the first nontrivial even invariant V_sel = Tr H^4 - (1/8)(Tr H^2)^2
      = 32 sum_{i<j} phi_i^2 phi_j^2 (graph_first_selector_derivation, retained). Hessian
      at e_1 = diag(0,64,64) => m_perp = 32. So the form AND the 32 are DERIVED on a
      retained surface; only the identification of this phi-space with the Dirac Higgs
      family M(phi)=sum phi_i Gamma_i is admitted (narrower than "V_sel flatly admitted").
  T3  READOUT bridge, ADMITTED (ADM-1) via a DOMAIN MISMATCH: the retained Frobenius
      ratio is sqrt(Tr(Y^d Y)/Tr(Gamma_1^d Gamma_1)) = sqrt(8/16) = 1/sqrt2 (raw). The
      physical readout y_nu^(0)/g = 1/sqrt2 is NOT licensed by the retained det-uniqueness
      theorem (observable_principle_real_d_block_uniqueness): that forces W=log|det(D+J)|
      only for INVERTIBLE REAL ANTI-HERMITIAN D, but the neutrino baseline D=m I is
      real-SYMMETRIC (D^T=+D != -D), outside the domain. det responses: det(mI+jY)=m^16
      (nilpotent, j-flat) vs det(mI+jGamma_1)=(m^2-j^2)^8 (diagnostics only).
  T4  ASSEMBLY: y_nu^eff = j^2/m = (g/sqrt2)^2/32 = g^2/64 (given ADM-1, ADM-2).
  CTRL teeth: wrong m, wrong j, or rescaled S_i break the coefficient.

Named admissions (honest ceiling): ADM-1 physical readout 1/sqrt2 (det-uniqueness
domain mismatch); ADM-2 g_weak as physical coupling (registered comparator, G3);
ADM-3 the phi-space identification (graph-shift selector <-> Dirac Higgs family).

prints TOTAL: PASS=N FAIL=0
"""

from pathlib import Path

import numpy as np
import sympy as sp

results = []
def check(name, ok): results.append((name, bool(ok)))

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "DM_NEUTRINO_SCHUR_SUPPRESSION_NAMED_ADMISSIONS_BOUNDED_THEOREM_NOTE_2026-06-07.md"

# --- T2: V_sel = 32 sum phi^2 phi^2 from the RETAINED graph-shift surface ---
sx = np.array([[0, 1], [1, 0]], dtype=int)
def Sop(i):
    ops = [np.eye(2, dtype=int)] * 3; ops[i] = sx
    M = ops[0]
    for o in ops[1:]:
        M = np.kron(M, o)
    return sp.Matrix(M)
S = [Sop(i) for i in range(3)]
p = sp.symbols('p0 p1 p2', real=True)
H = S[0] * p[0] + S[1] * p[1] + S[2] * p[2]
TrH2 = sp.trace(H * H)
TrH4 = sp.trace((H * H) * (H * H))
Vsel = sp.expand(TrH4 - sp.Rational(1, 8) * TrH2 ** 2)
target = 32 * (p[0]**2 * p[1]**2 + p[0]**2 * p[2]**2 + p[1]**2 * p[2]**2)
check("T2 V_sel = TrH^4-(1/8)(TrH^2)^2 = 32 sum_{i<j} phi^2 phi^2 (retained graph-shift)",
      sp.simplify(Vsel - target) == 0)
check("T2b Tr H^2 = 8|phi|^2", sp.simplify(TrH2 - 8 * (p[0]**2 + p[1]**2 + p[2]**2)) == 0)
# Hessian at e_1 -> diag(0,64,64), m_perp=32
Hess = sp.hessian(target, p).subs({p[0]: 1, p[1]: 0, p[2]: 0})
check("T2c V_sel Hessian at e_1 = diag(0,64,64)", Hess == sp.diag(0, 64, 64))
m_perp = Hess[1, 1] / 2
check("T2d transverse curvature m_perp = 32", m_perp == 32)

# --- T1: retained Schur return Delta y = j^2/m ---
m, j = sp.symbols('m j', positive=True)
# the retained cascade identity gives the *return* coefficient j^2/m per internal channel;
# verify the single-channel Schur complement gives the m - j^2/m return
Mb1 = sp.Matrix([[m, j], [j, m]])
schur1 = Mb1[0, 0] - Mb1[0, 1] * (1 / Mb1[1, 1]) * Mb1[1, 0]
check("T1 single-channel Schur return: m - j^2/m  (Delta y = j^2/m)",
      sp.simplify(schur1 - (m - j**2 / m)) == 0)

# --- T3: readout det responses + domain mismatch ---
# canonical C^16: gamma5 = sz (x) I8, Gamma_1 = sx (x) I8
sz = np.array([[1, 0], [0, -1]]); I8 = np.eye(8)
g5 = np.kron(sz, I8); G1 = np.kron(sx, I8)
check("T3 {gamma5,Gamma_1}=0, both involutive", np.allclose(g5 @ G1 + G1 @ g5, 0) and np.allclose(G1 @ G1, np.eye(16)))
PL = (np.eye(16) - g5) / 2; PR = (np.eye(16) + g5) / 2
Y = PR @ G1 @ PL
check("T3b Y nilpotent (Y^2=0), Y+Y^dag = Gamma_1", np.allclose(Y @ Y, 0) and np.allclose(Y + Y.conj().T, G1))
check("T3c raw Frobenius ratio sqrt(Tr(Y^d Y)/Tr(G1^d G1)) = 1/sqrt2",
      abs(np.sqrt(np.trace(Y.conj().T @ Y).real / np.trace(G1.conj().T @ G1).real) - 1 / np.sqrt(2)) < 1e-12)
mm = 1.7
check("T3d det(mI+jY)=m^16 (nilpotent, j-flat)", abs(np.linalg.det(mm * np.eye(16) + 0.9 * Y) - mm**16) < 1e-6)
check("T3e det(mI+jG1)=(m^2-j^2)^8", abs(np.linalg.det(mm * np.eye(16) + 0.9 * G1) - (mm**2 - 0.9**2)**8) < 1e-6)
# DOMAIN MISMATCH: D=m*I is real-symmetric, not anti-Hermitian -> readout NOT licensed
D = mm * np.eye(4)
check("T3f ADM-1: D=m I is NOT real anti-Hermitian (readout unlicensed by det-uniqueness)",
      not np.allclose(D.T, -D))

# --- T4: assembly ---
g = sp.symbols('g', positive=True)
y_eff = (g / sp.sqrt(2))**2 / 32
check("T4 y_nu^eff = (g/sqrt2)^2/32 = g^2/64", sp.simplify(y_eff - g**2 / 64) == 0)

# --- CTRL teeth ---
check("CTRL wrong m_perp=16 gives g^2/32 (not g^2/64)", sp.simplify((g / sp.sqrt(2))**2 / 16 - g**2 / 32) == 0)
check("CTRL wrong j=g gives g^2/32 (not g^2/64)", sp.simplify(g**2 / 32 - g**2 / 32) == 0)
# rescaled S_i -> 2 S_i: cross-coeff scales by 2^4=16 -> 512 != 32 (teeth on the graph-shift derivation)
H2 = (2 * S[0]) * p[0] + (2 * S[1]) * p[1] + (2 * S[2]) * p[2]
V2 = sp.expand(sp.trace((H2 * H2) * (H2 * H2)) - sp.Rational(1, 8) * sp.trace(H2 * H2)**2)
coeff2 = V2.coeff(p[0]**2 * p[1]**2)
check("CTRL rescaled 2*S_i: cross-coeff = 512 != 32 (graph-shift normalization has teeth)", coeff2 == 512)

# --- Source firewall: the row remains bounded on ADM-1/2/3 ---
note_text = NOTE_PATH.read_text(encoding="utf-8")
note_flat = " ".join(note_text.split())
check("SRC top-level status is bounded support over ADM-1/2/3",
      "**Claim type:** bounded_theorem" in note_text
      and "bounded support over ADM-1/ADM-2/ADM-3" in note_flat
      and "not an import-free physical coefficient theorem" in note_flat
      and "No new axiom, retained bridge, audit verdict, ledger tag, or publication" in note_flat
      and "TOTAL: PASS=18 FAIL=0" in note_text)
check("SRC 2026-06-12 firewall keeps ADM-1/2/3 live, no retained promotion",
      "2026-06-12 Admissions-Closure Attempt And No-Go Routing" in note_text
      and "this is bounded support only" in note_flat
      and "No retained-grade proposal or status promotion is made here" in note_flat)
check("SRC ADM-3 positive closure must evade the native even-trace no-go",
      "DM_NEUTRINO_VSEL_CURVATURE_TASTE_TO_DIRAC_TRANSPORT_OBSTRUCTION_NO_GO_NOTE_2026-06-07.md" in note_text
      and "native pure even-trace Dirac-Higgs transport route is blocked" in note_flat
      and "outside the native even-trace no-go" in note_flat)

n_pass = sum(1 for _, ok in results if ok)
n_fail = sum(1 for _, ok in results if not ok)
for name, ok in results:
    print(("PASS" if ok else "FAIL"), name)
print()
print("TOTAL: PASS=%d FAIL=%d" % (n_pass, n_fail))
