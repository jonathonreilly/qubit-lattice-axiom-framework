#!/usr/bin/env python3
"""ADVERSARIAL verification of the chirality chain (#3316/#3317/#3320).

Independent re-derivation that tries to REFUTE each claim, separating what is
genuinely verified from what the PR runners OVERSTATE. Finite-dim, memory-safe.

Confirms the sound core (Cl(3,1) gamma_5; CAR positive-energy) and pins three
scope-overstatements in the PR runners + restates the admitted residual.
"""
import numpy as np

PASS = 0; FAIL = 0; FLAG = []
def check(name, ok, detail=""):
    global PASS, FAIL
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
    if ok: PASS += 1
    else: FAIL += 1
def flag(name, detail):
    FLAG.append(name); print(f"FLAG: {name} -- {detail}")

I2 = np.eye(2, dtype=complex); Z = np.zeros((2, 2), complex)
def blk(A,B,C,D): return np.block([[A,B],[C,D]])
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]],complex); sz=np.array([[1,0],[0,-1]],complex)
g0=blk(I2,Z,Z,-I2); g=[blk(Z,si,-si,Z) for si in (sx,sy,sz)]
g5=1j*g0@g[0]@g[1]@g[2]
eta=np.diag([1,-1,-1,-1.0])
gammas=[g0]+g

print("== CORE (confirm #3317A + #3320 MODE): Cl(3,1) chirality is genuine ==")
clifford=all(np.allclose(gammas[a]@gammas[b]+gammas[b]@gammas[a], 2*eta[a,b]*np.eye(4)) for a in range(4) for b in range(4))
check("clifford_3p1_algebra", clifford, "{g^mu,g^nu}=2 eta^{mu nu} -- genuine Cl(3,1)")
check("g5_chirality", np.allclose(g5@g5,np.eye(4)) and abs(np.trace(g5))<1e-12 and all(np.allclose(g5@gm+gm@g5,0) for gm in gammas),
      "g5^2=I, traceless, {g5,g^mu}=0 -- the partner chirality is real")

print("== CORE (confirm #3320 T1): CAR positive-energy vs Bose unbounded -- with the vacuum constant kept ==")
# H_hat = E a^dag a - E b b^dag.  CAR: b b^dag = 1 - b^dag b  => E(na+nb) - E ; Bose: +E => E(na-nb)
E=1.0
car=sorted(E*na+E*nb-E for na in (0,1) for nb in (0,1))     # keep the -E constant the PR dropped
check("CAR_bounded_below", car[0]==-E and car[-1]==E, f"CAR eigs {car} -- BOUNDED below (min=-E, a finite vacuum shift)")
N=12; bose=min(E*na-E*nb for na in range(N+1) for nb in range(N+1))
check("Bose_unbounded_below", bose<=-E*N+1e-9, f"Bose min={bose:.0f} -> -inf -- UNBOUNDED: statistics (sign of the b-reorder) is the engine")
flag("normal_ordering", "PR runner drops the -E vacuum constant (shows {0,E,E,2E}); physically the claim is BOUNDED-below, which holds either way")

print("== REFUTE #3320 BOOST: the runner's check is vacuous; test the REAL boost property ==")
m=0.8
# (a) vacuity: the runner checks S^-1 (m I) S = m I.  m*I is CENTRAL -> true for ANY invertible M.
rng=np.random.default_rng(7); M=rng.standard_normal((4,4))+1j*rng.standard_normal((4,4))
vacuous = np.allclose(np.linalg.inv(M)@(m*np.eye(4))@M, m*np.eye(4))
check("boost_check_is_vacuous", vacuous, "inv(M)(m I)M = m I holds for a RANDOM non-boost M -> the runner's boost check verifies NOTHING")
# (b) the real test: mass term m psi-bar psi = m psi^dag g0 psi is boost-invariant  <=>  S^dag g0 S = g0
eta_b=0.7
Srun=np.array([[np.cosh(eta_b/2),0,np.sinh(eta_b/2),0],[0,np.cosh(eta_b/2),0,np.sinh(eta_b/2)],
               [np.sinh(eta_b/2),0,np.cosh(eta_b/2),0],[0,np.sinh(eta_b/2),0,np.cosh(eta_b/2)]],complex)
real_ok = np.allclose(Srun.conj().T@g0@Srun, g0)
# the canonical Dirac z-boost for comparison: exp(eta/2 g0 g3)
Sdir=__import__('scipy.linalg',fromlist=['expm']).expm(eta_b/2*g0@g[2]) if False else None
G0G3=g0@g[2]; Sdir=np.cosh(eta_b/2)*np.eye(4)+np.sinh(eta_b/2)*G0G3
dir_ok=np.allclose(Sdir.conj().T@g0@Sdir,g0)
check("real_boost_test_on_canonical_S", dir_ok, "the canonical Dirac boost exp(eta/2 g0 g3) DOES satisfy S^dag g0 S=g0 (mass bilinear invariant)")
if real_ok:
    flag("boost_overstated", "runner's S happens to pass the real test too, but the check it RAN (m I central) was vacuous -- boost-covariance is true yet UN-verified by the runner")
else:
    flag("boost_S_not_a_boost", "runner's S FAILS the real test S^dag g0 S=g0 -- it is not a Dirac boost; the vacuous m I check masked this")

print("== REFUTE #3320 CAUS: completeness is the EQUAL-TIME precursor, not spacelike microcausality ==")
us=np.linalg.eigh(sum([0.4,-0.6,0.3][i]*(g0@g[i]) for i in range(3))+m*g0)[1][:, np.linalg.eigh(sum([0.4,-0.6,0.3][i]*(g0@g[i]) for i in range(3))+m*g0)[0]>0]
vs=np.linalg.eigh(sum([0.4,-0.6,0.3][i]*(g0@g[i]) for i in range(3))+m*g0)[1][:, np.linalg.eigh(sum([0.4,-0.6,0.3][i]*(g0@g[i]) for i in range(3))+m*g0)[0]<0]
check("completeness_equal_time_CAR", np.allclose(us@us.conj().T+vs@vs.conj().T, np.eye(4)),
      "sum(uu^dag+vv^dag)=I -> canonical EQUAL-TIME {psi,psi^dag}=delta (a NECESSARY precursor)")
flag("microcausality_overstated", "equal-time CAR != microcausality. The spacelike statement {psi(x),psi-bar(y)}=0 for (x-y) spacelike "
     "needs the Pauli-Jordan mode integral over the mass shell (a field construction) -- NOT verified by the finite-dim single-momentum runner")

print("== REFUTE #3317 CONT: the decoupling's load-bearing premise is HARDCODED ==")
flag("decoupling_premise_assumed", "the runner sets has_k4_corner=False by hand. The Clifford-vs-corner DISTINCTION is sound, but 'continuous "
     "emergent time => no k_4 doubler' is the ASSUMED premise (emergent-time continuity), not a derived result")

print("== #3316 Koide overreach (already bounded by PR #3333) ==")
flag("koide_overreach", "Dirac g5=I_3(x)sigma_3 is generation-blind ([g5, Gamma_chi(x)I]=0) -> cannot supply the Koide Q=2/3 generation "
     "chirality; #3316's 'one keystone' collapse holds only for the spin-statistics (Dirac) half (see #3333)")

print()
print(f"TOTAL: PASS={PASS} FAIL={FAIL}  FLAGS={len(FLAG)}")
print("VERDICT: the chain's ALGEBRA is sound and confirmed -- Cl(3,1) supplies a genuine gamma_5 chirality, and CAR "
      "uniquely gives a bounded-below H (Bose is unbounded). But the PR runners OVERSTATE three checks: (1) BOOST "
      "covariance is verified by a vacuous identity (m I is central; true for any matrix); (2) MICROCAUSALITY is only "
      "the equal-time CAR precursor, not the spacelike Pauli-Jordan vanishing; (3) the #3317 DECOUPLING rests on the "
      "ASSUMED premise that emergent time is continuous (no k_4 corner). Plus #3316 overreaches on Koide (bounded by "
      "#3333). NET: positive-energy + the chiral algebra are solid; microcausality/boost/decoupling are "
      "PARTIALLY-supported-pending the admitted residual -- the OS->Wightman field construction on the emergent-time "
      "Hilbert space, which is exactly where the spacelike-causality and genuine-boost-covariance checks live.")
raise SystemExit(0 if FAIL==0 else 1)
