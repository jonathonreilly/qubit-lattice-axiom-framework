#!/usr/bin/env python3
"""
Phase-dof resolution: does the doublet phase theta=Im(b) count as a measure dof?
The C3-symmetric Hermitian mass operator's doublet subspace is 2-real-dim:
  {J-I = C+C^2 (symmetric, Re b, NATIVE cube double-shift, move 1),
   i(C-C^2)    (antisymmetric, Im b, the CHIRAL IMPORT, move 1)}.
Q = 1/3 + (2/3)|b|^2/a^2, |b|^2 = (Re b)^2 + (Im b)^2.

RESOLUTION (verified): the PHYSICAL 3-distinct spectrum (e!=mu!=tau) REQUIRES the
antisymmetric/imported dof (Im b != 0); the native-symmetric-only operator (Im b=0)
gives at most 2 DISTINCT masses. So the physical operator's |b|^2 carries BOTH dof
-> covariant-measure median Q = 1.34 (the retraction of the 'native 2/3 lean'
STANDS). The native-symmetric-only operator has median 2/3 but is NOT the physical
(3-distinct) spectrum. So under the measure interpretation the physical operator ->
Q=1; EXACT 2/3 comes from the chiral CONSTRAINT {M,Gamma_chi}=0, not any measure.
The phase theta IS the chiral import.
"""
import numpy as np
C = np.array([[0,1,0],[0,0,1],[1,0,0]], complex)
def specQ(a, bre, bim):
    b = bre + 1j*bim; Y = a*np.eye(3) + b*C + np.conj(b)*C.conj().T
    ev = np.linalg.eigvalsh(Y)
    return (ev**2).sum()/ev.sum()**2, np.sort(ev), len(set(np.round(ev,4)))
print("native-symmetric (Im b=0): at most 2 distinct masses:")
for bre in [0.3,0.5]:
    q,ev,n = specQ(1.0,bre,0.0); print(f"  Re b={bre}: sqrt-masses {np.round(ev,3)} -> {n} distinct, Q={q:.4f}")
print("full operator (Im b!=0 = chiral import): 3 distinct (physical):")
for bim in [0.2,0.4]:
    q,ev,n = specQ(1.0,0.3,bim); print(f"  Im b={bim}: sqrt-masses {np.round(ev,3)} -> {n} distinct, Q={q:.4f}")
rng=np.random.RandomState(5); N=1_000_000
a=rng.randn(N)/np.sqrt(3); bre=rng.randn(N)/np.sqrt(6); bim=rng.randn(N)/np.sqrt(6)
print(f"\nmeasure-median Q: native-symmetric-only={np.median(1/3+2/3*bre**2/a**2):.3f}; full physical={np.median(1/3+2/3*(bre**2+bim**2)/a**2):.3f}")
print("=> physical 3-distinct needs the import -> median Q=1 (retraction stands); exact 2/3 = chiral constraint.")
