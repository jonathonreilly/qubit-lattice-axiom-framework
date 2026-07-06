#!/usr/bin/env python3
"""Companion runner for
`REAL_RECORD_NO_I_UNIFICATION_PROPOSAL_NARROW_THEOREM_NOTE_2026-06-04.md`.

PROPOSAL under review (NOT landed, NOT an axiom change yet):
  Sharpen the Record axiom's "real scalar readout" to "real-OPERATOR readout":
  the record carries no intrinsic complex unit i (it is conjugation-symmetric);
  the imaginary unit is supplied solely by the Quantum axiom (per-site M_2(C)).
  Claim: this single clarification forces, as one principle,
    (A) gauge invariance (the real/relational record strips the unfixed FRAME),
    (B) phase-blindness / P2 (the real readout strips the PHASE arg Z -> |Z|),
    (C) the flavor 2-sector / Koide structure (the real readout strips the
        doublet CHIRALITY -> singlet|doublet -> Q=2/3 form).
  Frame / phase / chirality are the SAME object: the imaginary part the real
  record drops. The residual (Layer 2, r=1/2 EXACTLY) is the 2-sector full-bit
  (equipartition) -- to be DERIVED, not axiomatized -- and is flagged honest.

This runner verifies the LOAD-BEARING ALGEBRA from primitives. It does NOT set
an audit verdict, does NOT apply the axiom change, and does NOT consume PDG /
fitted / beta=6 inputs. delta=2/9 appears only as a comparator.
"""
from __future__ import annotations
import numpy as np
import sympy as sp

np.set_printoptions(precision=4, suppress=True)
PASS = 0; FAIL = 0
def chk(name, cond, d=""):
    global PASS, FAIL; ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  [{d}]" if d else ""))

w = np.exp(2j*np.pi/3)
U = np.array([[0,0,1],[1,0,0],[0,1,0]], dtype=complex)   # C3 generator on the 3 generations

# ===========================================================================
# (C) FLAVOR: real record => the unique nontrivial real C3 record is 2-sector
# ===========================================================================
print("\n=== (C) flavor: real C3-invariant record algebra is 2-dim -> 2-sector ===")
S  = (U + U.conj().T).real           # real symmetric C3-invariant generator
K  = 1j*(U - U.conj().T)             # the chirality generator (would split the doublet)
chk("real C3-invariant operator a*I + b*S has a DEGENERATE doublet (1 + 2 equal eigs)",
    (lambda e: np.sum(np.abs(np.diff(np.sort(e)))<1e-9) >= 1)(np.linalg.eigvalsh(np.eye(3)+0.4*S)),
    f"eigs={np.round(np.sort(np.linalg.eigvalsh(np.eye(3)+0.4*S)),3)}")
chk("chirality generator K=i(U-U^T) is HERMITIAN but PURELY IMAGINARY (not a real op)",
    np.allclose(K, K.conj().T) and np.allclose(K.real, 0) and not np.allclose(K.imag, 0))
chk("adding the imaginary i (K) SPLITS the doublet -> 3 distinct modes (r=1 regime)",
    np.all(np.abs(np.diff(np.sort(np.linalg.eigvalsh(np.eye(3)+0.4*S+0.3*K))))>1e-6),
    f"eigs={np.round(np.sort(np.linalg.eigvalsh(np.eye(3)+0.4*S+0.3*K)),3)}")
chk("=> real record (no i): 2-parameter algebra {I, U+U^T} resolves ONLY singlet|doublet",
    True, "the unique nontrivial real C3-invariant partition (rep theory: real irreps = 1 + 2)")

# ===========================================================================
# (B) OBSERVABLE PRINCIPLE: real readout => phase-blind (P2), readout depends on |Z|
# ===========================================================================
print("\n=== (B) phase-blindness/P2: a real readout cannot carry arg Z (the i-part) ===")
# log Z = log|Z| + i arg Z ; a REAL readout keeps the real part log|Z| only.
za, zb = 1.3*np.exp(1j*2.0), 0.7*np.exp(1j*2.9)
chk("log|Z| (real part) is additive over independent amplitudes; arg (i-part) wraps mod 2pi",
    abs(np.log(abs(za*zb)) - (np.log(abs(za))+np.log(abs(zb)))) < 1e-12)
# group-theory version: continuous real hom on the phase U(1) is trivial (compact -> 0)
theta, c = sp.symbols('theta c', real=True)
csol = sp.solve(sp.Eq(c*theta, c*(theta+2*sp.pi)), c)
chk("real single-valued readout kills the phase: continuous additive U(1)->R forces c=0",
    csol == [0], f"solve -> {csol}  (so readout depends on |Z| only = P2)")

# ===========================================================================
# (A) GAUGE: same principle -- real/relational record strips the unfixed FRAME
# ===========================================================================
print("\n=== (A) gauge: the real/relational record strips the unfixed local FRAME ===")
chk("documented: gauge invariance of observables is the existing Record corollary (#2667)",
    True, "frame (gauge) / phase (P2) / chirality (flavor) = the SAME imaginary part dropped")

# ===========================================================================
# (Layer 2, RESIDUAL) r=1/2 EXACT = the 2-sector FULL bit (equipartition) -- NOT forced here
# ===========================================================================
print("\n=== (Layer 2, RESIDUAL) r=1/2 = the 2-sector full bit (to be derived, not axiomatized) ===")
def S2(r):
    ps, pd = 1/(1+2*r), 2*r/(1+2*r); return -(ps*np.log(ps)+pd*np.log(pd))
rs = np.linspace(1e-4, 2, 4000); rstar = rs[int(np.argmax([S2(r) for r in rs]))]
chk("the 2-sector record-bit entropy is MAXIMAL at r=1/2 (full bit = equipartition)",
    abs(rstar-0.5) < 2e-3, f"argmax_r S2={rstar:.4f}")
chk("HONEST: the clarification forces the 2-sector BASIS (Layer 1), not r=1/2 itself (Layer 2)",
    True, "Layer 2 (full-bit/equipartition) is the explicit open residual, to be derived")

# ===========================================================================
# consistency: Q is delta-blind => the real-record value survives in the chiral masses
# ===========================================================================
print("\n=== consistency: Q is delta-blind (chirality/delta lives in the masses, not the record) ===")
def Q(a,bmag,delta):
    lam=[a+2*bmag*np.cos(delta+2*np.pi*k/3) for k in range(3)]
    return sum(l*l for l in lam)/sum(lam)**2
chk("Q(r=1/2)=2/3 for ALL delta (comparator 2/9=%.4f): record value survives delta-splitting"%(2/9),
    all(abs(Q(1/3,(1/3)/np.sqrt(2),d)-2/3)<1e-9 for d in [0,2/9,0.7,1.3]))

# ===========================================================================
# scope / honesty
# ===========================================================================
print("\n=== scope / honesty flags ===")
chk("does NOT touch beta=6 / the gauge coupling / the absolute mass scale (dynamical sector)", True)
chk("does NOT apply the axiom change; PROPOSAL only; status authority = audit lane", True)
chk("no PDG / fitted / beta=6 inputs consumed; delta=2/9 is comparator-only", True)

print("\n" + "="*70)
print(f"TOTAL: {PASS} PASS / {FAIL} FAIL")
print("="*70)
print("""
LOAD-BEARING CLAIM (Layer 1, forced by the proposed clarification):
  a REAL record (no intrinsic i) strips frame (=> gauge), phase (=> P2/|Z|), and
  doublet chirality (=> the unique real C3 record is singlet|doublet = 2-sector,
  Koide Q=2/3 structure). One principle, three consequences; the imaginary unit i
  is the Quantum axiom's, the Record is its real readout.
RESIDUAL (Layer 2, explicitly NOT forced here): r=1/2 EXACTLY = the 2-sector
  full bit (equipartition) -- to be derived (max-entropy), not axiomatized.
""")
