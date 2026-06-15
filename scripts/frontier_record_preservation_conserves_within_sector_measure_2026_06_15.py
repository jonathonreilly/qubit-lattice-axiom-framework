"""Class-A finite-dim exact checks: record-preservation CONSERVES the within-sector
measure, so the generation breaking (r, delta) is not a relaxation outcome of the
record-preserving dynamics -- it is registered/coupling data.

Chain: Stage 1 -> the forced record-preserving generation form is the circulant
H = a I + b C + conj(b) C^T with [H, C] = 0, hence [H, S] = 0 for the einselected
pointer S = C + C^2 (spectrum {2, -1, -1}). Block-diagonality in singlet (+) doublet
then CONSERVES the realized state's block weight under H-evolution. The einselected
2-sector record D_S (dephasing onto {P_singlet, P_doublet}) does NOT resolve the
2-dim doublet, so it PRESERVES the within-doublet structure (it does not erase the
doublet-internal phase); only a finer character-basis record would touch it.

(Corrected per an independent verification pass: the claim is conservation +
preservation by the coarse 2-sector record, NOT erasure; the erasure only holds
for the finer character-basis record. Tautological 'spectrum invariant' / 'r>0'
gates removed.)
"""
import numpy as np
from scipy.linalg import expm

PASS = 0
FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS  {name}" + (f"  -- {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL  {name}" + (f"  -- {detail}" if detail else ""))


C = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)
I3 = np.eye(3, dtype=complex)
S = C + C @ C

evals, evecs = np.linalg.eigh(S)
P_singlet = np.outer(evecs[:, 2], evecs[:, 2].conj())   # +2 eigenvalue
P_doublet = I3 - P_singlet                              # the two -1 eigenvalues
doublet_basis = evecs[:, :2]                            # orthonormal doublet basis


def circ(a, babs, delta):
    b = babs * np.exp(1j * delta)
    return a * I3 + b * C + np.conj(b) * C.T


def doublet_coherence(rho):
    m = doublet_basis.conj().T @ rho @ doublet_basis
    return abs(m[0, 1])


def record_2sector(rho):
    """The einselected 2-sector record: dephasing onto {P_singlet, P_doublet}."""
    return P_singlet @ rho @ P_singlet + P_doublet @ rho @ P_doublet


F = np.array([[1, 1, 1],
              [1, np.exp(2j * np.pi / 3), np.exp(4j * np.pi / 3)],
              [1, np.exp(4j * np.pi / 3), np.exp(8j * np.pi / 3)]], complex) / np.sqrt(3)


def record_character(rho):
    """A FINER character-basis record (not the einselected 2-sector one)."""
    r = F.conj().T @ rho @ F
    return F @ np.diag(np.diag(r)) @ F.conj().T


check("S=C+C^2 spectrum == {-1,-1,2} (the einselected 2-sector record)", np.allclose(np.sort(evals.real), [-1, -1, 2]))

H = circ(1.0, np.sqrt(0.5), 2.0 / 9.0)  # an r=1/2-class coupling set (r=|b|^2/a^2=0.5), inserted by hand (free label)
check("forced form [H,S]=0 (block-diagonal in singlet+doublet)", np.allclose(H @ S, S @ H))

# (i) CONSERVATION of the realized state's block weight under H-evolution (the genuine result)
rng = np.random.default_rng(20260615)
conserve_ok = True
spreads = []
for _ in range(8):
    psi = rng.normal(size=3) + 1j * rng.normal(size=3); psi /= np.linalg.norm(psi)
    rho0 = np.outer(psi, psi.conj())
    ws = [np.real(np.trace(P_doublet @ (expm(-1j * H * t) @ rho0 @ expm(-1j * H * t).conj().T)))
          for t in np.linspace(0.0, 25.0, 30)]
    spreads.append(max(ws) - min(ws))
    conserve_ok &= (max(ws) - min(ws)) < 1e-9
check("realized-state doublet block weight tr(P_doublet rho) CONSERVED under H-evolution (<1e-9)",
      conserve_ok, detail=f"max spread over 8 states = {max(spreads):.2e}")

# Discriminating control: a non-block-diagonal generator changes the block weight
Hbad = np.zeros((3, 3), complex); Hbad[0, 1] = Hbad[1, 0] = 1.0
check("control: Hbad has [Hbad,S]!=0 (not record-preserving)", not np.allclose(Hbad @ S, S @ Hbad))
psi = rng.normal(size=3) + 1j * rng.normal(size=3); psi /= np.linalg.norm(psi); rho0 = np.outer(psi, psi.conj())
wb = [np.real(np.trace(P_doublet @ (expm(-1j * Hbad * t) @ rho0 @ expm(-1j * Hbad * t).conj().T)))
      for t in np.linspace(0, 5, 20)]
check("control: NON-record-preserving Hbad CHANGES the block weight (spread>1e-3) -> conservation is special",
      (max(wb) - min(wb)) > 1e-3, detail=f"spread={max(wb)-min(wb):.3e}")

# (ii) The einselected 2-sector record PRESERVES the within-doublet phase (does NOT erase delta)
preserve_ok = True
finer_erases = True
raw_vals, ds_vals, dchi_vals = [], [], []
for _ in range(8):
    psi = rng.normal(size=3) + 1j * rng.normal(size=3); psi /= np.linalg.norm(psi)
    rho0 = np.outer(psi, psi.conj())
    raw, ds, dchi = doublet_coherence(rho0), doublet_coherence(record_2sector(rho0)), doublet_coherence(record_character(rho0))
    raw_vals.append(raw); ds_vals.append(ds); dchi_vals.append(dchi)
    preserve_ok &= abs(ds - raw) < 1e-12 and raw > 1e-3            # 2-sector record leaves doublet coherence unchanged
    finer_erases &= dchi < raw - 1e-6                              # finer character record DOES reduce it
check("einselected 2-sector record D_S PRESERVES within-doublet coherence (does NOT erase delta)",
      preserve_ok, detail=f"max |D_S - raw| = {max(abs(d-r) for d,r in zip(ds_vals,raw_vals)):.2e}")
check("contrast: a FINER character-basis record reduces the doublet coherence (the distinction is real)",
      finer_erases, detail=f"raw~{np.mean(raw_vals):.3f} vs finer~{np.mean(dchi_vals):.3f}")

# D_S is a valid record map: trace-preserving and idempotent
tp_ok = idem_ok = True
for _ in range(6):
    psi = rng.normal(size=3) + 1j * rng.normal(size=3); psi /= np.linalg.norm(psi); rho0 = np.outer(psi, psi.conj())
    tp_ok &= abs(np.trace(record_2sector(rho0)) - 1.0) < 1e-12
    idem_ok &= np.allclose(record_2sector(record_2sector(rho0)), record_2sector(rho0))
check("the 2-sector record D_S is trace-preserving (registered diagonal content preserved)", tp_ok)
check("the 2-sector record D_S is idempotent (a genuine record/dephasing map)", idem_ok)

print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
