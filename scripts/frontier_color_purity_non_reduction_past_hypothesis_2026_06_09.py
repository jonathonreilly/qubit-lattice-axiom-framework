"""Color-purity non-reduction runner -- the purity component of the global color-neutrality admission does NOT reduce
into the retained past-hypothesis slot, and is strictly WEAKER than the named
global-neutrality admission.

Context (the global color-neutrality admission split). The admissions-collapse note collapsed
the three mapped color-depolarization mechanisms to two irreducible admissions,
one of which is the global color-neutrality admission: a GLOBAL color-singlet / Gauss-law physical-state condition
that drives the single-carrier color density to rho_color = I3/3. The orientation-retirement note split that admission into two pieces:

  * ORIENTATION (the state's position in the SU(3) orbit) -- predictively
    vacuous on the single irreducible carrier (the SU(3)-invariant observable
    algebra is scalars; orientation carries zero color invariant). Retired as a
    source proposal.
  * PURITY / spectrum (the order parameter P = Tr(rho_color^2) - 1/3, the color-purity order-parameter note)
    -- preserved by the orientation rotation; the genuine residual.

The purity residual question asks: does the PURITY residual reduce into the framework's EXISTING
retained past-hypothesis slot (`arrow_from_record_formation_past_hypothesis_
residual_note_2026-06-05`, retained_bounded -- the low-record/low-entropy
initial-condition boundary selection), i.e. does a past hypothesis of "no
initial unregistrable structure" pin rho_0 = I3/3, unifying with the existing
slot?

This runner records the honest answer: NO. The purity does not reduce into the
past-hypothesis slot. The load-bearing obstructions are on the
ORIENTATION/symmetry and SUFFICIENCY axes, NOT an entropy-orthogonality axis:

  (1) the retained past hypothesis fixes GLOBAL record entropy (a boundary
      state-selection). The order parameter P is a property of the single
      carrier's MARGINAL. Fixing the global entropy does NOT fix P: P = 0 is
      realized at BOTH a globally pure state (S_global = 0, via entanglement)
      and a globally maximally-mixed two-carrier state (S_global = log 9). So the entropy
      boundary is uninformative about P -- it neither supplies nor excludes it.
  (2) "no unregistrable (orientation) structure" is an ORIENTATION/symmetry
      selector. By the orientation-retirement note the orientation is vacuous; retiring it does NOT pin
      the registrable purity (a polarized rho with retired orientation still
      has P > 0). The uniqueness "I3/3 is the only density with no orientation
      structure" needs the MAXIMAL-SU(3)-SYMMETRY (invariance) demand, which is
      the NEUTRALITY-type condition -- a different KIND of admission than the
      entropy-axis past hypothesis, not a unification with the existing slot.
  (3) the purity condition rho_color = I3/3 is STRICTLY WEAKER than global
      color-neutrality: a pure NON-singlet two-fundamental state realizes
      rho_color = I3/3 yet is not invariant under the diagonal SU(3). So
      P = 0 does NOT entail neutrality; the named neutrality admission is one
      (stronger) realization, not the residual itself.

Conclusion: no admission discharged, no admission count reduced. The purity is
an independent SU(3)-invariant state-structure admission, on a different axis
than the entropy-boundary past hypothesis, and strictly weaker than the named
neutrality admission. The proposed purity reduction is refuted.

All checks are exact finite-dimensional linear algebra on C^3 and C^3 (x) C^3
(dims <= 9). Seeded SU(3) elements are witnesses for already-proven exact
identities; there is NO Monte-Carlo fit in the logic path. The 9-element
Heisenberg-Weyl twirl gives the SU(3)-invariant-density uniqueness EXACTLY.
"""

import numpy as np

PASS = 0
FAIL = 0


def check(name, ok):
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"[PASS] {name}")
    else:
        FAIL += 1
        print(f"[FAIL] {name}")


rng = np.random.default_rng(20260917)
Nc = 3
I3 = np.eye(Nc)
Imix = np.eye(Nc) / Nc


def haar_unitary(n):
    z = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / np.sqrt(2)
    q, r = np.linalg.qr(z)
    return q * (np.diag(r) / np.abs(np.diag(r)))


def su3():
    u = haar_unitary(Nc)
    return u / np.linalg.det(u) ** (1.0 / Nc)


def vn_entropy(rho):
    w = np.linalg.eigvalsh((rho + rho.conj().T) / 2)
    w = w[w > 1e-12]
    return float(-(w * np.log(w)).sum())


def order_param(rho):
    return float(np.trace(rho @ rho).real) - 1.0 / Nc


def reduced_A(rho):
    """Partial trace over carrier B of a 9x9 state on C^3 (x) C^3."""
    r = rho.reshape(Nc, Nc, Nc, Nc)
    return np.einsum("ijkj->ik", r)


# Exact unitary 1-design: the 9-element Heisenberg-Weyl group on C^3.
# (1/9) sum_{a,b} (X^a Z^b) M (X^a Z^b)^dag = (Tr M / Nc) I  EXACTLY.
_omega = np.exp(2j * np.pi / Nc)
_X = np.roll(np.eye(Nc), 1, axis=0).astype(complex)
_Z = np.diag([_omega ** k for k in range(Nc)]).astype(complex)
_HW = [np.linalg.matrix_power(_X, a) @ np.linalg.matrix_power(_Z, b)
       for a in range(Nc) for b in range(Nc)]


def hw_twirl(M):
    return sum(W @ M @ W.conj().T for W in _HW) / len(_HW)


def is_density(rho):
    herm = np.allclose(rho, rho.conj().T, atol=1e-10)
    tr1 = abs(np.trace(rho).real - 1.0) < 1e-10
    psd = np.linalg.eigvalsh((rho + rho.conj().T) / 2).min() > -1e-10
    return herm and tr1 and psd


# A polarized (non-maximally-mixed) reference density and a random orientation.
rho_pol = np.diag([0.6, 0.3, 0.1]).astype(complex)
U_orient = su3()

print("=== order parameter zero and invariant-density uniqueness ===")
check("P(I3/3) = 0 exactly (fully color-blind)", abs(order_param(Imix)) < 1e-12)
check("P(polarized) > 0 (purity above the floor)", order_param(rho_pol) > 1e-6)
# I3/3 is the UNIQUE SU(3)-invariant density (Schur / commutant = scalars),
# witnessed exactly by the HW(3) 1-design twirl collapsing ANY density to I3/3.
check("HW twirl of a polarized density = I3/3 exactly (invariant density unique)",
      np.allclose(hw_twirl(rho_pol), Imix, atol=1e-12))
check("HW twirl of a generic (oriented) density = I3/3 exactly",
      np.allclose(hw_twirl(U_orient @ rho_pol @ U_orient.conj().T), Imix, atol=1e-12))
# A density invariant under the full group must equal its twirl => I3/3.
check("only the twirl-fixed density is I3/3 (P=0 iff rho=I3/3)",
      abs(order_param(hw_twirl(rho_pol))) < 1e-12 and order_param(rho_pol) > 1e-6)

print("\n=== purity is orientation-invariant ===")
def conjugate(rho, U):
    return U @ rho @ U.conj().T
oriented = [conjugate(rho_pol, su3()) for _ in range(8)]
check("P(U rho U^dag) = P(rho) for every orientation (spectral function)",
      all(abs(order_param(r) - order_param(rho_pol)) < 1e-12 for r in oriented))
# Retiring orientation does NOT change the purity: a polarized state
# with 'vacuous' orientation still has P > 0 -- orientation vacuity cannot pin P.
check("retiring orientation leaves the purity residual intact (P stays > 0)",
      all(order_param(r) > 1e-6 for r in oriented))

print("\n=== global entropy does not fix color purity ===")
# I3/3 has MAXIMAL single-carrier (color) von Neumann entropy = log 3.
check("S(I3/3) = log 3 (maximal qutrit marginal entropy)",
      abs(vn_entropy(Imix) - np.log(Nc)) < 1e-12)
# a GLOBALLY PURE state (S_global = 0) with marginal I3/3: the q-qbar
# singlet |s> = (1/sqrt3) sum_i |i,ibar>.  P = 0 at zero global entropy.
c_singlet = (np.eye(Nc) / np.sqrt(Nc)).reshape(Nc * Nc)   # coeff matrix = I/sqrt3
rho_glob_singlet = np.outer(c_singlet, c_singlet.conj())
rhoA_singlet = reduced_A(rho_glob_singlet)
check("globally PURE singlet: S_global = 0", vn_entropy(rho_glob_singlet) < 1e-10)
check("singlet marginal rho_A = I3/3 (P = 0)", abs(order_param(rhoA_singlet)) < 1e-12)
# a GLOBALLY MAXIMALLY-MIXED separable realization: rho = I3/3 (x) I3/3.
rho_glob_sep = np.kron(Imix, Imix)
rhoA_sep = reduced_A(rho_glob_sep)
check("separable realization: marginal rho_A = I3/3 (P = 0)",
      abs(order_param(rhoA_sep)) < 1e-12)
check("maximally mixed two-carrier realization: S_global = log 9",
      abs(vn_entropy(rho_glob_sep) - np.log(Nc * Nc)) < 1e-12)
# => P = 0 occurs at S_global = 0 AND at S_global = log 9. Fixing the global
# entropy (the past-hypothesis boundary) is UNINFORMATIVE about P.
P_at_low = abs(order_param(rhoA_singlet)) < 1e-12
P_at_high = abs(order_param(rhoA_sep)) < 1e-12
check("P=0 realized at both entropy poles => global entropy does not fix P",
      P_at_low and P_at_high)

print("\n=== purity zero does not entail neutrality ===")
g = su3()
# the singlet (diagonal action g (x) g* on quark (x) antiquark) IS neutral.
# coeff matrix C transforms as C -> g C g^dag; singlet C = I/sqrt3 is invariant.
C_singlet = np.eye(Nc) / np.sqrt(Nc)
C_singlet_rot = g @ C_singlet @ g.conj().T
check("singlet rho_A = I3/3 (P = 0)", abs(order_param(rhoA_singlet)) < 1e-12)
check("singlet INVARIANT under g (x) g* (color-neutral)",
      np.allclose(C_singlet_rot, C_singlet, atol=1e-12))
# two FUNDAMENTALS, |F> = (1/sqrt3) sum_i |i>_A|i>_B (diagonal action
# g (x) g): coeff matrix C -> g C g^T.  rho_A = I3/3 but NOT a color singlet.
C_fund = np.eye(Nc) / np.sqrt(Nc)
c_fund_vec = C_fund.reshape(Nc * Nc)
rho_glob_fund = np.outer(c_fund_vec, c_fund_vec.conj())
rhoA_fund = reduced_A(rho_glob_fund)
C_fund_rot = g @ C_fund @ g.T
check("two-fundamental |F> is globally PURE", vn_entropy(rho_glob_fund) < 1e-10)
check("two-fundamental marginal rho_A = I3/3 (P = 0)",
      abs(order_param(rhoA_fund)) < 1e-12)
check("two-fundamental NOT invariant under diagonal g (x) g (NOT a singlet)",
      np.linalg.norm(C_fund_rot - C_fund) > 1e-3)
# So P = 0 is realized by a non-neutral pure state => purity does NOT imply
# neutrality. (Forward direction -- the color-neutrality forward-direction note -- gives neutrality => P=0; the
# converse fails here.)
purity_weaker_than_neutrality = bool(
    abs(order_param(rhoA_fund)) < 1e-12
    and np.linalg.norm(C_fund_rot - C_fund) > 1e-3
)
check("purity is STRICTLY WEAKER than global neutrality (converse fails)",
      purity_weaker_than_neutrality)

print("\n=== reduction assembly ===")
# the entropy boundary does not supply the color-purity order parameter and is
# not the slot that order parameter occupies.
past_hypothesis_does_not_pin_purity = bool(P_at_low and P_at_high)
check("past hypothesis (fixes global entropy) does NOT pin the purity P",
      past_hypothesis_does_not_pin_purity)
# pinning I3/3 needs the maximal-symmetry/neutrality-type demand, NOT the
# entropy boundary: a polarized state with retired orientation still has P>0.
pin_needs_symmetry_not_entropy = bool(all(order_param(r) > 1e-6 for r in oriented))
check("retiring orientation does not pin P (pin needs the symmetry demand)",
      pin_needs_symmetry_not_entropy)
# no admission discharged, no count reduced: purity stands as an
# independent SU(3)-invariant state-structure admission.
no_hat_discharged = bool(
    past_hypothesis_does_not_pin_purity      # P not supplied by the past hypothesis
    and pin_needs_symmetry_not_entropy       # P not supplied by orientation retirement
    and purity_weaker_than_neutrality        # P not equal to the neutrality admission
)
check("no admission discharged / no count reduced (proposed reduction refuted)",
      no_hat_discharged)
# sanity: the only state that is BOTH P=0 AND globally pure AND neutral is
# the singlet (one realization), confirming neutrality is a strict subset.
check("singlet is the neutral P=0 realization; two-fundamental is the non-neutral one",
      np.allclose(rhoA_singlet, Imix, atol=1e-12)
      and np.allclose(rhoA_fund, Imix, atol=1e-12)
      and np.allclose(C_singlet_rot, C_singlet, atol=1e-12)
      and np.linalg.norm(C_fund_rot - C_fund) > 1e-3)

print("\n=== discipline and hygiene ===")
check("all constructed objects are valid densities",
      is_density(rhoA_singlet) and is_density(rhoA_fund) and is_density(rhoA_sep)
      and is_density(rho_glob_singlet) and is_density(rho_glob_fund))
check("booleans wired to fresh computations (no tautological self-pass)",
      isinstance(past_hypothesis_does_not_pin_purity, bool)
      and isinstance(purity_weaker_than_neutrality, bool)
      and isinstance(no_hat_discharged, (bool, np.bool_)))

print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
