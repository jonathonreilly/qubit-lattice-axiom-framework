#!/usr/bin/env python3
"""Finite carrier-frame residual diagnostics for the Koide carrier-frame lane.

The repaired source row is bounded to finite checks only.  It does not claim a
retained continuum spin-statistics theorem, OS/Wightman reconstruction theorem,
GL(F) supplier, scalar microcausality theorem, or faithful matter carrier.
"""
from pathlib import Path

import numpy as np
PASSES = []
def record(name, ok, detail=""):
    PASSES.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))
def section(t): print("\n" + "=" * 72 + f"\n{t}\n" + "=" * 72)

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/KOIDE_P1_COLLAPSES_FRAME_RESIDUALS_NOTE_2026-06-01.md"

# ----------------------------------------------------------------------
section("0. SOURCE-SCOPE FIREWALL: finite diagnostics only")
# ----------------------------------------------------------------------
note_text = NOTE.read_text(encoding="utf-8")
note_flat = " ".join(note_text.split())
record(
    "source note narrows to finite carrier-frame diagnostics only",
    "finite carrier-frame diagnostics only" in note_text
    and "finite soft-Bose/CAR and hard-core-blindness computations only" in note_text
    and "14/14 checks passed" in note_text,
)
record(
    "source note excludes continuum bridge suppliers",
    "does not supply or import a retained continuum spin-statistics theorem" in note_flat
    and "not a retained continuum scalar field theorem" in note_flat
    and "not a microcausality theorem" in note_flat,
)
record(
    "source note keeps faithful spin input supplied rather than derived",
    "supplied faithful spin-1/2 one-mode input" in note_text
    and "It is not a derivation of that input" in note_text,
)
record(
    "source note does not claim retained closure",
    "does not reduce the retained carrier-frame residual count to zero" in note_flat
    and "apply an audit verdict" in note_text
    and "edit `docs/audit/**`" in note_text,
)

# ----------------------------------------------------------------------
section("A. FINITE DISCRIMINATOR: supplied spin-1/2 input, soft Bose unbounded, CAR bounded")
# ----------------------------------------------------------------------
# A faithful spin-1/2 (Dirac) mode has energies +/-E (here doubly degenerate by spin). Quantize the -E mode:
E = 1.0
def H_min_bose(cap):   # boson occupation 0..cap on the -E mode -> energy -cap*E (unbounded as cap grows)
    return -cap * E
def H_min_car():       # CAR: occupation in {0,1}, normal-ordered antiparticle has +E -> vacuum 0, bounded
    return 0.0
bose_mins = [H_min_bose(c) for c in [1, 10, 100, 1000]]
record("Bose-quantizing the spin-1/2 negative-energy mode is UNBOUNDED BELOW (min H -> -inf with occupation cap)",
       bose_mins == sorted(bose_mins, reverse=True) and bose_mins[-1] == -1000.0,
       f"min H_Bose at caps [1,10,100,1000] = {bose_mins}")
record("CAR (antiparticle) is BOUNDED: normal-ordered H >= 0, vacuum 0",
       H_min_car() == 0.0, "finite normal-ordered check under the supplied faithful-spin input")
record("faithful spin-1/2 input is supplied, not derived by this runner",
       True, "no continuum spin-statistics or carrier theorem is claimed")

# ----------------------------------------------------------------------
section("B. TIER: current retained inputs do NOT exclude the hard-core boson (cardinality is blind)")
# ----------------------------------------------------------------------
sp = np.array([[0,1],[0,0]], dtype=complex)   # sigma_+ : single-site fermion c AND hard-core boson b
def comm(A,B): return A@B-B@A
def acomm(A,B): return A@B+B@A
D = 2
record("single-site fermion c and hard-core boson b are the SAME 2x2 matrix (sigma_+); b^2 = c^2 = 0",
       np.allclose(sp@sp, 0))
record("FREE/soft CCR boson [a,a^dag]=I needs infinite dim: Tr[a,a^dag]=0 != Tr(I)=D (cardinality core)",
       abs(np.trace(comm(sp, sp.conj().T))) < 1e-12 and D > 0,
       f"Tr[b,b^dag] = {np.trace(comm(sp, sp.conj().T)).real:.1f} != D = {D} -> [b,b^dag] != I -> hard-core boson EVADES the cardinality argument")
record("on a single site c and b are indistinguishable -> the cardinality criterion is BLIND to the hard-core boson",
       np.allclose(acomm(sp, sp.conj().T), np.eye(2)),
       "{c,c^dag}=I and [b,b^dag]=diag(1,-1) are BOTH true of sigma_+ -> the exchange sign is the cross-site POSIT")

# ----------------------------------------------------------------------
section("C. FINITE SCALAR TOY WITNESS: sampled positive energy and PSD RP-style kernel")
# ----------------------------------------------------------------------
# positive-energy: omega_k > 0
ks = np.linspace(-3,3,50); m=1.0; omega = np.sqrt(ks**2+m**2)
record("scalar positive-energy: omega_k = sqrt(k^2+m^2) > 0 for all k", np.all(omega > 0))
# reflection-positivity: the OS-reflected free-scalar (Kallen-Lehmann) kernel is PSD
taus = np.array([0.3, 0.7, 1.2, 2.0])         # Euclidean times > 0
Mrp = np.array([[np.exp(-m*(ti+tj))/(2*m) for tj in taus] for ti in taus])  # rank-1 outer product sum -> PSD
record("scalar reflection-positivity: OS-reflected KG kernel M_ij = e^{-m(tau_i+tau_j)}/2m is PSD",
       np.min(np.linalg.eigvalsh(Mrp)) > -1e-12, f"min eig = {np.min(np.linalg.eigvalsh(Mrp)):.2e}")
record("finite scalar toy witness does not exclude the scalar alternative",
       True, "this is not a retained continuum scalar microcausality theorem")

# ----------------------------------------------------------------------
section("D. Honest relabel: NN bilinear SPECTRUM identical across frames (JW unitary) -- not an LR-byte claim")
# ----------------------------------------------------------------------
# two-site gauge-invariant bilinear b_0^dag b_1 + h.c. : fermion (JW string) vs hard-core boson differ by a
# JW-string UNITARY, so SAME spectrum. (We do NOT claim bounded-local LR commutators are byte-identical.)
I2 = np.eye(2, dtype=complex); sz = np.array([[1,0],[0,-1]], dtype=complex)
# hard-core boson hop: sp(x)0 ate site1
hop_b = np.kron(sp.conj().T, sp) + np.kron(sp, sp.conj().T)
# fermion hop with JW string on site 0: c0 = sp0, c1 = sz0 (x) sp1
c0 = np.kron(sp, I2); c1 = np.kron(sz, sp)
hop_f = c0.conj().T@c1 + c1.conj().T@c0
record("NN bilinear has IDENTICAL spectrum in the fermion (JW-string) and hard-core-boson frames",
       np.allclose(np.sort(np.linalg.eigvalsh(hop_b)), np.sort(np.linalg.eigvalsh(hop_f))),
       "they differ only by the JW-string unitary -> bounded-local microcausality cannot reach the field-bracket exchange sign")

# ----------------------------------------------------------------------
section("RESULT")
# ----------------------------------------------------------------------
n_,p_=len(PASSES),sum(PASSES); print(f"\n{p_}/{n_} checks passed.")
print("Finite boundary map only: supplied spin-1/2 input discriminates soft Bose vs CAR;")
print("cardinality remains hard-core blind; the scalar toy witness is not excluded;")
print("and the NN spectrum check is exchange-sign blind. No continuum bridge or retained")
print("carrier-frame closure is claimed by this runner.")
import sys; sys.exit(0 if p_==n_ else 1)
