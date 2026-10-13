"""R19-22 s4: observational numbers and the CONDITIONAL price table (no model; scenario arithmetic only).

All observational inputs are RECALLED (not fetched):
  GW170817/GRB170817A: -3e-15 <= dc/c <= +7e-16 (Abbott et al. 2017).
  graviton mass (LVK GWTC-3 propagation test): m_g <= 1.27e-23 eV.
  Planck mass 1.221e28 eV, Planck length 1.616e-35 m, hbar c = 1.9733e-7 eV m.
Lattice: a = l_P, J g = 1 (bare speed c), Planck units hbar = c = 1.
Scenarios (all SUGGESTED, none derived): a gauge-breaking residue eps makes (i) a speed offset dc/c ~ eps
(absorbable by one retuning of J g) or (ii) a TT mass m_g^2 a^2 ~ eps (not absorbable).
"""
import numpy as np
lP = 1.616e-35; c = 2.998e8; MP_eV = 1.221e28; hbarc = 1.9733e-7
print("LIGO-band k a and lattice dispersion (omega = (2/a) sin(k a/2)):")
for f in [10, 100, 1000]:
    ka = 2*np.pi*f/c*lP
    print(f"  f={f:5d} Hz: k a = {ka:.3e};  1 - v_group = 1 - cos(ka/2) ~ (ka)^2/8 = {(ka)**2/8:.3e}")
mg = 1.27e-23; r = mg/MP_eV
print(f"\nm_g/M_P <= {r:.3e};  (m_g a)^2 <= {r**2:.3e};  Compton range hbar/(m_g c) = {hbarc/mg:.3e} m = {hbarc/mg/9.461e15:.2f} ly")
for f in [10, 100]:
    w = 2*np.pi*f*6.582e-16      # eV
    print(f"  massive dispersion at {f} Hz: 1 - v_g ~ m^2/(2 w^2) = {mg**2/(2*w**2):.3e}  (vs GW170817 1e-15: mass bound binds, not speed)")

def qubits(d): return np.log2(d)
print("\nCONDITIONAL price table (one TT-protecting mechanism assumed to exist; per slot, 6 slots per cell):")
rows = []
need_speed = 1e-15; need_mass2 = r**2
for lab, need in [("speed offset dc/c ~ eps  (no retuning)", need_speed), ("mass m_g^2 a^2 ~ eps", need_mass2)]:
    S1 = 1/need; S2 = 1/np.sqrt(need)
    N = 2/np.pi*np.log(1/need)
    print(f"  {lab}: eps <= {need:.2e}")
    print(f"     HP eps ~ 1/S   : S >= {S1:.2e}  qubits/slot = {qubits(2*S1+1):6.1f}  per cell = {6*qubits(2*S1+1):7.1f}")
    print(f"     HP eps ~ 1/S^2 : S >= {S2:.2e}  qubits/slot = {qubits(2*S2+1):6.1f}  per cell = {6*qubits(2*S2+1):7.1f}")
    print(f"     clock eps ~ exp(-pi N/2): N >= {N:.1f}  qubits/slot = {qubits(N):5.2f} (ceil {int(np.ceil(qubits(N)))})  per cell = {6*np.ceil(qubits(N)):.0f}")
    Ns = np.log(1/need)/1.4452
    print(f"     clock with s1's fitted slope 1.4452: N >= {Ns:.1f}  qubits/slot = {qubits(Ns):5.2f}")
# lifetime scenario: junk drift reaches the spin boundary sqrt(S) at t ~ S^alpha t_P
tU = 13.8e9*3.156e7/5.391e-44
print(f"\nAge of universe / t_P = {tU:.2e}. Lifetime scenario t* ~ S^alpha t_P (SUGGESTED, alpha unknown):")
for al in [0.5, 0.75, 1.0]:
    S = tU**(1/al); print(f"  alpha={al}: S >= {S:.2e}, qubits/slot = {qubits(2*S+1):.1f}")
print("\nTrace-collapse depth (proved bound, per cell): HP E_gs <= -(3/4) J S + O(1);  clock (CCR scaling) <= -(3 pi/8) J N + O(1)")
for S in [10, 1e15, 1e51, 1e102]:
    print(f"  S={S:.0e}: collapse depth ~ {0.75*S:.2e} J per cell below the HP graviton sector")
