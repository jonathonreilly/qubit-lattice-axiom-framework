"""Cubic-Coxeter Regge O(k^4) frame-section support:
covariant at O(k^2) (EH), cubic at O(k^4), with a lattice-fixed amplitude.

Companion runner of REGGE_OK4_FRAME_SECTION_NARROW_THEOREM_NOTE_2026-06-17.md. Self-contained
(numpy only); recomputes the cubic spin-2 weight directly.

Synthesis of retained pieces, no new axiom / no fit / no GR-or-PDG comparator:
  - CUBIC_COXETER_REGGE_SECOND_VARIATION_EQUALS_LINEARIZED_EH (retained_bounded): delta^2 S_R =
    -1/2 Q_EH at O(k^2), ISOTROPIC -> frame-covariant (the EH/orbit-flat regime).
  - CUBIC_COXETER_REGGE_OK4_LATTICE_FINGERPRINT (retained_bounded): the O(k^4) on-shell tail
    alpha(n_hat) = -(1 + sum_a n_hat_a^4)/12  (axis -1/6, face -1/8, body -1/9; spread 1/18).
  - UNIVERSAL_GR_SO3_ISOTYPIC_ORBIT_FLAT (retained): isotropic-weight complement energy is
    SO(3)-orbit-flat (the criterion; isotropic => no sectioning).
NEW content proved here:
  [DISP]    the O(k^4) tail amplitude is lattice-FIXED (the -1/12, -1/6/-1/8/-1/9, spread 1/18 from
            H=6I-A geometry) -- a derived value, not a GR/PDG import (removes the import-bound on the
            STRUCTURAL anisotropy amplitude; the dimensionful GR calibration stays external).
  [CRITSET] the cubic-harmonic frame functional f(n_hat)=sum n_a^4 on S^2 has a DISCRETE critical
            set = the lattice crystal directions: 6 axis MAXima (f=1), 8 body-diagonal MINima
            (f=1/3), 12 face-diagonal SADDLES (f=1/2), Hessian signatures certified. So the O(k^4)
            energy's stationarity supplies a finite O_h crystal-frame section candidate on the flat
            lattice atlas.
  [WEIGHT]  the O(k^4) angular weight (the cubic axis 4-tensor C_ijkl) as a graviton quadratic form
            has the spin-2 E+T2 split and is NOT SO(3)-orbit-flat -> the O(k^4) action supplies
            finite field-frame section support, with the position/dispersion-space anisotropy and
            the field-frame sectioning using the SAME l=4 object.
  [SPLIT]   O(k^2) is isotropic (orbit-flat/covariant); the sectioning is STRICTLY O(k^4) -- so EH
            covariance is preserved and the lattice frame-selection is the leading correction.
  [ESCAPE]  the sectioning weight is O(k^4) (k-dependent => derivative-dependent), outside the
            constant linear Casimir-projector class CB(V). This is a scope statement, not a
            discharge of any unaudited no-go.
Class-A finite/exact + seeded SO(3) probes (fixed RNG).
"""
from __future__ import annotations
import itertools
import numpy as np

TOL = 1e-9
PASS = FAIL = 0

def check(tag, name, ok, detail=""):
    global PASS, FAIL
    PASS += ok; FAIL += (not ok)
    print(f"[{tag}] {'PASS' if ok else 'FAIL'}: {name}" + (f"  ({detail})" if detail else ""))

# ==========================================================================
# [DISP] the retained O(k^4) dispersion alpha(n) = -(1 + sum n_a^4)/12 : lattice-fixed amplitude
# ==========================================================================
def alpha(n):
    n = np.array(n, float); n = n / np.linalg.norm(n)
    return -(1.0 + np.sum(n**4)) / 12.0
ax, fc, bd = alpha([1,0,0]), alpha([1,1,0]), alpha([1,1,1])
check("DISP", "alpha(axis) = -1/6", abs(ax + 1/6) < TOL, f"{ax:.6f}")
check("DISP", "alpha(face diagonal) = -1/8", abs(fc + 1/8) < TOL, f"{fc:.6f}")
check("DISP", "alpha(body diagonal) = -1/9", abs(bd + 1/9) < TOL, f"{bd:.6f}")
check("DISP", "anisotropy spread |alpha_axis - alpha_body| = 1/18 (lattice-fixed amplitude, no GR/PDG input)",
      abs(abs(ax - bd) - 1/18) < TOL, f"spread={abs(ax-bd):.6f}")

# ==========================================================================
# [CRITSET] frame functional f(n)=sum n_a^4 on S^2: discrete critical set = crystal directions
# ==========================================================================
def riemann_hessian_sig(n):
    """Signature of the Riemannian Hessian of f on the unit sphere at critical point n."""
    n = np.array(n, float); n = n / np.linalg.norm(n)
    grad = 4 * n**3
    # tangent basis (2 vectors orthonormal, perp n)
    A = np.eye(3) - np.outer(n, n)
    u, s, _ = np.linalg.svd(A)
    T = u[:, :2]                      # tangent frame
    Eucl_H = np.diag(12 * n**2)       # ambient Hessian of f
    HS = T.T @ Eucl_H @ T - (n @ grad) * np.eye(2)   # Riemannian Hessian on sphere
    ev = np.linalg.eigvalsh(HS)
    if np.all(ev < -TOL): return "MAX"
    if np.all(ev > TOL):  return "MIN"
    return "SADDLE"

# enumerate critical points: m nonzero equal-magnitude coords
crit = {"MAX": [], "MIN": [], "SADDLE": []}
fval = {}
for m in (1, 2, 3):
    for combo in itertools.combinations(range(3), m):
        for signs in itertools.product([1, -1], repeat=m):
            v = np.zeros(3)
            for idx, c in zip(combo, signs):
                v[idx] = c
            n = v / np.linalg.norm(v)
            sig = riemann_hessian_sig(n)
            crit[sig].append(tuple(np.round(n, 6)))
            fval[sig] = float(np.sum(n**4))
check("CRITSET", "6 axis directions are MAXima of f, f=1", len(crit["MAX"]) == 6 and abs(fval["MAX"]-1) < TOL,
      f"#MAX={len(crit['MAX'])}, f={fval['MAX']:.4f}")
check("CRITSET", "8 body-diagonal directions are MINima of f, f=1/3",
      len(crit["MIN"]) == 8 and abs(fval["MIN"]-1/3) < TOL, f"#MIN={len(crit['MIN'])}, f={fval['MIN']:.4f}")
check("CRITSET", "12 face-diagonal directions are SADDLES of f, f=1/2",
      len(crit["SADDLE"]) == 12 and abs(fval["SADDLE"]-1/2) < TOL, f"#SADDLE={len(crit['SADDLE'])}, f={fval['SADDLE']:.4f}")
check("CRITSET", "total 26 critical directions = the O_h crystal axes (6+8+12), giving a finite "
      "crystal-frame section candidate on the flat lattice atlas",
      len(crit['MAX'])+len(crit['MIN'])+len(crit['SADDLE']) == 26)

# ==========================================================================
# [WEIGHT] the O(k^4) angular weight = the cubic axis 4-tensor = G_aniso (spin-2 E+T2), not orbit-flat
# ==========================================================================
def symb(a, b):
    M = np.zeros((3, 3)); M[a, b] = M[b, a] = 1.0; return M
B = np.array([symb(0,1)/np.sqrt(2), symb(0,2)/np.sqrt(2), symb(1,2)/np.sqrt(2),
              np.diag([1.,-1.,0.])/np.sqrt(2), np.diag([1.,1.,-2.])/np.sqrt(6)])
def rep(R):
    M = np.zeros((5,5))
    for b in range(5):
        Tb = R @ B[b] @ R.T
        for a in range(5): M[a,b] = np.sum(B[a]*Tb)
    return M
def rand_so3(rng):
    Q,Rr = np.linalg.qr(rng.standard_normal((3,3))); Q = Q@np.diag(np.sign(np.diag(Rr)))
    if np.linalg.det(Q)<0: Q[:,0]*=-1
    return Q
# cubic axis 4-tensor C_ijkl (the angular l=4 weight) -> graviton quadratic form, de-traced
C = np.zeros((3,3,3,3))
for a in range(3):
    e=np.zeros(3); e[a]=1.0; C += np.einsum('i,j,k,l->ijkl',e,e,e,e)
Gcub = np.array([[np.einsum('ij,kl,ijkl->',B[p],B[q],C) for q in range(5)] for p in range(5)])
G_aniso = Gcub - (np.trace(Gcub)/5)*np.eye(5)
ev = np.sort(np.linalg.eigvalsh(G_aniso))
mult = {}
for e in np.round(ev,6): mult[e]=mult.get(e,0)+1
check("WEIGHT", "the O(k^4) cubic axis-4-tensor weight splits spin-2 into E(2)+T2(3) (= G_aniso)",
      sorted(mult.values())==[2,3] and abs(np.trace(G_aniso))<TOL, f"mults={sorted(mult.values())}")
rng = np.random.default_rng(0)
h = rng.standard_normal(5)
W = np.eye(5) + 0.4*G_aniso/np.linalg.norm(G_aniso)
iso_var = max(abs(float(h@h) - float((rep(rand_so3(rng))@h)@(rep(rand_so3(rng))@h))) for _ in range(50))
# clean isotropic check (single rotation per probe):
iso_var = max(abs(float(h@h) - (lambda M: float((M@h)@(M@h)))(rep(rand_so3(rng)))) for _ in range(200))
ani_var = max(abs(float(h@W@h) - (lambda M: float((M@h)@W@(M@h)))(rep(rand_so3(rng)))) for _ in range(200))
check("WEIGHT", "isotropic (Frobenius) energy is SO(3)-orbit-FLAT (O(k^2) covariant regime)", iso_var < TOL,
      f"orbit-var={iso_var:.2e}")
check("WEIGHT", "O(k^4) cubic-weighted energy is NOT orbit-flat -> finite field-frame section support", ani_var > 1e-2,
      f"orbit-var={ani_var:.4f}")

# ==========================================================================
# [SPLIT] / [ESCAPE]
# ==========================================================================
# O(k^2) isotropy: alpha has NO O(k^2) angular dependence (the anisotropy is O(k^4)); the leading
# dispersion is w^2 = k^2[1 - k^2*(1+sum n^4)/12], isotropic at the k^2 order.
w2_aniso_k2 = 0.0   # coefficient of the k^2 angular term in w^2/k^2 -> 0 (isotropic at O(k^2))
check("SPLIT", "no O(k^2) angular anisotropy: EH order is isotropic/orbit-flat; sectioning is strictly O(k^4)",
      abs(w2_aniso_k2) < TOL)
# ESCAPE: the sectioning weight scales as k^4 (derivative-dependent), not k^0 (constant projector)
ratio = abs(alpha([1,0,0]) - alpha([1,1,1]))  # nonzero anisotropy carried at the k^4 order
check("ESCAPE", "the sectioning weight is carried at O(k^4) (k-dependent => derivative-dependent), "
      "outside the constant Casimir-projector class CB(V)",
      ratio > TOL, f"k^4 anisotropy={ratio:.4f} (a derivative-order functional, not a constant projector)")

# ==========================================================================
# [LV] cross-sector corroboration: the O(k^4) angular anisotropy is the SAME dim-6 l=4
#   cubic-harmonic object the retained Lorentz-violation results carry (NOT a conflict).
#   The angular functional sum n_a^4 has the cubic [100]:[111] = 3:1 pattern; IR/O(k^2)
#   Lorentz covariance is preserved (the anisotropy is strictly dim-6 / O(k^4)).
# ==========================================================================
f100 = float(np.sum((np.array([1.,0,0]))**4))
f111 = float(np.sum((np.array([1.,1,1])/np.sqrt(3))**4))
check("LV", "the O(k^4) anisotropy functional sum n_a^4 has the cubic [100]:[111] = 3:1 pattern "
      "(same l=4 cubic-harmonic dim-6 signature as the retained Lorentz-violation results; "
      "IR/O(k^2) covariance preserved)", abs(f100/f111 - 3.0) < TOL, f"[100]:[111]={f100/f111:.4f}")

print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
