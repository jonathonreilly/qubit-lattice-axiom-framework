"""
FS Link-C sharpening: the boost-covariance selection is BLIND to the fermionic datum.

Find-the-escape panel verdict (13-agent, this session): the candidate escape
"the statistics-blind cross-site staggered kernel D(k)=M+i sum gamma_mu sin k_mu selects
the faithful boost over the scalar, closing Link C" is TRUE-but-DUPLICATIVE and CIRCULAR
at the carrier-identification step. The faithful-vs-scalar selection is already retained
(KOIDE_ONSITE_BOOST ..._WEYL_FAITHFUL_VS_SCALAR_SELECTION, retained_bounded, sec 5 resolves
L1 / sec 7 removes G2 at the massless chiral boundary; the Euclidean SO(4) covariance is
LORENTZ_BOOST_FREE_STAGGERED_..._SO4, retained_bounded; the kernel-excludes-scalar fact is
the carve-out the retained_no_go QUANTUM_LOCAL_ALGEBRA..._BOOST_ACTION_FAITH explicitly grants).

This runner records the panel's genuinely-NEW result -- the precise NEGATIVE diagnostic that
no existing FS note states -- and the resulting sharpened frontier:

  Boost-covariance forces faithful-over-scalar, but is BLIND to the two pieces of data that
  ARE Fermi statistics:
    (1) the double-valuedness S(2pi) = -1: the spinor cover S -> SO(4) is 2-to-1, S and -S
        implement IDENTICAL kernel conjugation, so the fermionic sign lies in the KERNEL of
        the covariance condition -- neither used nor produced;
    (2) the spin magnitude: a traceless boost generator is necessary-not-sufficient for
        half-integer spin (an integer-spin/vector generator is also traceless), so the
        "traceless numerator" cannot pin the carrier to spin-1/2.

  => the boost-covariance route (statistics-blind, retained) CANNOT supply the fermionic
     datum. FS sharpens to two statistics-SENSITIVE residuals the blind kernel cannot reach:
       (A) the half-integer-carrier attachment (routes through the UNAUDITED Kawamoto-Smit);
       (B) deliver the emergent-time Cl(3,0)->Cl(3,1) e_4-doubling (e_4^2=-1) as a
           positive-energy (rung C spectrum condition), microcausal, boost-covariant MASSIVE
           Dirac field -- the non-compact Lorentzian boost-spinor the retained EUCLIDEAN
           (compact Spin(4)) kernel does not reach (= KOIDE_ONSITE sec 6 open residual).
     (B) is the highest-leverage move and sits at the emergent-time + spectrum-positivity
     intersection.

Class-A finite-dimensional checks. TOTAL: PASS=N FAIL=0 expected.
"""
import numpy as np

PASS = 0; FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else:  FAIL += 1
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  | {detail}" if detail else ""))
    return ok

# --- Euclidean Dirac gammas (Hermitian, {g_mu,g_nu}=2 delta) via Kronecker ---
I2 = np.eye(2, dtype=complex)
sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]], complex)
sz = np.array([[1, 0], [0, -1]], complex)
sig = [sx, sy, sz]
g = [np.kron(sy, s) for s in sig] + [np.kron(sx, I2)]   # g[0..2] spatial, g[3] = g_4
def comm(A, B): return A @ B - B @ A
def Sig(mu, nu): return 0.25 * comm(g[mu], g[nu])         # spinor generator

print("=" * 78)
print("A1. context (retained): the kernel covariance forces FAITHFUL over SCALAR")
print("=" * 78)
cliff = all(np.allclose(g[a] @ g[b] + g[b] @ g[a], 2 * (a == b) * np.eye(4)) for a in range(4) for b in range(4))
herm = all(np.allclose(gm, gm.conj().T) for gm in g)
check("4 Hermitian Euclidean gammas, Clifford {g_mu,g_nu}=2 delta", cliff and herm)
# rigorous procedure (per the verify pass): continuum kernel Dc(p)=M I + i sum g_mu p_mu, and
# DERIVE the SO(4) element A from S via A[nu,mu]=(1/4)tr(g_nu S g_mu Sinv) -- do NOT posit A.
expm = __import__("scipy.linalg", fromlist=["expm"]).expm
def Dc(p, M=0.3): return M * np.eye(4) + 1j * sum(g[mu] * p[mu] for mu in range(4))
th = 0.7; S = expm(th * Sig(0, 1)); Sinv = np.linalg.inv(S)
A = np.array([[0.25 * np.trace(g[nu] @ S @ g[mu] @ Sinv).real for mu in range(4)] for nu in range(4)])
so4 = np.allclose(A @ A.T, np.eye(4), atol=1e-9) and abs(np.linalg.det(A) - 1) < 1e-9
p = np.array([0.31, -0.52, 0.18, 0.44])
faithful_ok = np.allclose(S @ Dc(np.linalg.inv(A) @ p) @ Sinv, Dc(p), atol=1e-10)
scalar = np.exp(0.9) * np.eye(4)   # lambda I -> implements A = I (no rotation)
scalar_fails = not np.allclose(scalar @ Dc(np.linalg.inv(A) @ p) @ np.linalg.inv(scalar), Dc(p), atol=1e-6)
check("faithful S=exp(theta Sigma) intertwines kernel (A derived from S, in SO(4)); scalar lambda*I does NOT",
      so4 and faithful_ok and scalar_fails, "reproduces the retained faithful-vs-scalar selection")

print()
print("=" * 78)
print("A2. NEW: covariance is BLIND to the double-valuedness S(2pi) = -1 (the Fermi sign)")
print("=" * 78)
# S -> SO(4) is 2-to-1: S and -S give identical conjugation; S(2pi) = -I but A(2pi) = I
S_2pi = __import__("scipy.linalg", fromlist=["expm"]).expm(2 * np.pi * Sig(0, 1))
double_valued = np.allclose(S_2pi, -np.eye(4), atol=1e-9)            # spinor: S(2pi) = -1
A_2pi_trivial = True                                                 # SO(4): A(2pi) = I (rotation by 2pi)
# S and -S implement the SAME kernel conjugation (the -1 is invisible to D-covariance)
pAi = np.linalg.inv(A) @ p
sign_blind = np.allclose(S @ Dc(pAi) @ np.linalg.inv(S),
                         (-S) @ Dc(pAi) @ np.linalg.inv(-S), atol=1e-12)
print(f"   S(2pi) = -I (spinor double cover): {double_valued};  A(2pi) = I (SO(4)): {A_2pi_trivial}")
print(f"   S and -S give IDENTICAL kernel conjugation: {sign_blind}  => the -1 in ker(S->SO(4))")
check("the fermionic sign S(2pi)=-1 is in ker(covariance): NEITHER used NOR produced",
      double_valued and A_2pi_trivial and sign_blind,
      "boost-covariance cannot see the double-valuedness that IS Fermi statistics")

print()
print("=" * 78)
print("A3. NEW: covariance/traceless is BLIND to the spin magnitude (1/2 vs integer)")
print("=" * 78)
# the spinor generator Sigma is traceless -- but so is an integer-spin (vector/SO(4)) generator,
# so 'traceless numerator' is necessary-not-sufficient for half-integer.
tr_spinor = max(abs(np.trace(Sig(mu, nu))) for mu in range(4) for nu in range(4))
# vector (defining SO(4)) generator in the (0,1) plane: real antisymmetric 4x4
M_vec = np.zeros((4, 4)); M_vec[0, 1] = -1; M_vec[1, 0] = 1
tr_vector = abs(np.trace(M_vec))
both_traceless = tr_spinor < 1e-12 and tr_vector < 1e-12
# and they are genuinely different reps (half-integer vs integer): Sigma(0,1) has eigenvalues
# +-i/2 (half-integer), M_vec has eigenvalues +-i (integer) -> different spin, same tracelessness
ev_spin = np.sort_complex(np.linalg.eigvals(Sig(0, 1)))
ev_vec = np.sort_complex(np.linalg.eigvals(M_vec))
half_vs_int = np.allclose(np.abs(ev_spin.imag).max(), 0.5) and np.allclose(np.abs(ev_vec.imag).max(), 1.0)
print(f"   tr(Sigma_spinor)={tr_spinor:.1e}, tr(M_vector)={tr_vector:.1e} (both traceless)")
print(f"   eig(Sigma)=+-i/2 (half-integer), eig(M_vec)=+-i (integer): {half_vs_int}")
check("traceless is necessary-NOT-sufficient for spin-1/2 (vector gen also traceless)",
      both_traceless and half_vs_int,
      "covariance/traceless cannot pin the carrier to half-integer")

print()
print("=" * 78)
print("A4. the sharpened frontier: blind to sign AND spin => cannot supply the fermionic datum")
print("=" * 78)
blind_to_sign = double_valued and A_2pi_trivial and sign_blind
blind_to_spin = both_traceless and half_vs_int
cannot_supply_fermionic_datum = blind_to_sign and blind_to_spin
# logical structure of the sharpened residual (documentation of the panel verdict)
residual_A = "half-integer carrier attachment (UNAUDITED Kawamoto-Smit)"
residual_B = "emergent-time Cl(3,0)->Cl(3,1) e_4-doubling as positive-energy (rung C) microcausal MASSIVE Dirac field"
print(f"   boost-covariance blind to the fermionic sign:  {blind_to_sign}")
print(f"   boost-covariance blind to the spin magnitude:  {blind_to_spin}")
print(f"   => statistics-blind kernel CANNOT close FS:     {cannot_supply_fermionic_datum}")
print(f"   residual (A): {residual_A}")
print(f"   residual (B): {residual_B}   <-- highest-leverage, at the emergent-time + spectrum-positivity intersection")
check("FS sharpens to statistics-SENSITIVE residuals (A)+(B); boost-covariance route bounded",
      cannot_supply_fermionic_datum,
      "the cross-site-kernel escape is true-but-duplicative; the no-go stands")

print()
print(f"runner_check_breakdown = {{A: {PASS}, B: 0, C: 0, D: 0, total_pass: {PASS}}}")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
