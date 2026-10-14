"""Comparator: 'gravity in a solid' relation m_g^2 ~ 16 pi G mu_shear (Dubovsky-type, RECALLED, O(1) convention).
Effective shear stiffness to TT metric strain implied by F1's uncancelled Earth number, vs real rock; and the
Planckian 'deformation potential' implied by the root's Hessian."""
import numpy as np
G=6.674e-11; c=2.998e8; hbar=1.0546e-34; eV=1.602e-19
mg_eV=3.6e-9; w=mg_eV*eV/hbar
mu_eff=w**2*c**2/(16*np.pi*G)
print(f"F1 Earth |m_g|=3.6e-9 eV -> m_g c^2/hbar = {w:.2e} 1/s -> mu_eff = m_g^2 c^2/(16 pi G) = {mu_eff:.1e} Pa")
mu_rock=7e10
print(f"real rock shear modulus ~{mu_rock:.0e} Pa (RECALLED) -> ratio {mu_eff/mu_rock:.1e}; GR-solid m_g from real rock = {np.sqrt(16*np.pi*G*mu_rock)/c*hbar/eV:.1e} eV")
lP=1.616255e-35; EP_eV=1.221e28
e2=4*np.pi/137.036
print(f"deformation potential (rest-mass curvature) per unit strain^2: Hess*e2/a = {2.42401e-2*e2*EP_eV:.1e} eV  (semiconductors: ~1-10 eV, RECALLED)")
