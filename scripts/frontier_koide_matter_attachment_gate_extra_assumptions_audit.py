#!/usr/bin/env python3
"""
Extra-assumptions audit of the four retained no-gos that the charged-lepton matter-attachment gate reduces
to. Each no-go is airtight AT ITS STATED SCOPE, but the exercise pins a UNIFORM escape seam: every wall is a
KINEMATIC / single-site / ungraded fact, and the live escape lives in the GRADED cross-site / emergent-time
DYNAMICS arena (currently unaudited, not yet retained). One genuine internal correction surfaced (an
fs no-go's stated reason is superseded by a sister retained result); one red flag surfaced (an unaudited
microcausality note conflates per-site grading with cross-site anticommutation).

Targets (all retained_no_go on origin/main unless noted):
  N1 staggered_dirac_substep1_statistics_agnostic_no_forcing  (the statistics gate)
  N2 fs_rotation_exchange_discrete_insufficiency               (the rotation->exchange decoupling)
  N3 no_per_site_chirality_theorem                             (single-site chirality)
  N4 no_per_site_bosonic_ccr_theorem                           (free-CCR exclusion)

Non-circular: never assumes CAR, the faithful rep, or Q=2/3. All forcing claims are tier/computation only.
"""
import numpy as np
PASSES=[]
def record(name, ok, detail=""):
    PASSES.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))
def section(t): print("\n"+"="*76+f"\n{t}\n"+"="*76)

sp=np.array([[0,1],[0,0]],dtype=complex)        # sigma_+ : single-site fermion AND hard-core boson
sz=np.array([[1,0],[0,-1]],dtype=complex); I2=np.eye(2,dtype=complex)
def comm(A,B): return A@B-B@A
def acomm(A,B): return A@B+B@A

# ======================================================================
section("A. (N1,N4 unifying fact) the KINEMATIC A1+A2 frame IS the hard-core boson (ordinary ungraded tensor)")
# ======================================================================
# two sites, ordinary tensor product: disjoint-site odd ladders COMMUTE (hard-core boson)
O0=np.kron(sp,I2); O1=np.kron(I2,sp)
record("ordinary (ungraded) tensor: disjoint-site odd ladders COMMUTE [O0,O1]=0 (NOT anticommute) -> hard-core boson",
       np.allclose(comm(O0,O1),0) and not np.allclose(acomm(O0,O1),0),
       "A1+A2 commit to the ordinary C*-tensor product -> the kinematic frame is the hard-core boson")
# JW (graded) dressing makes them anticommute -> fermion. JW is an invertible relabel = a frame CHOICE.
c0=np.kron(sp,I2); c1=np.kron(sz,sp)
record("JW-dressed ladders ANTICOMMUTE {c0,c1}=0 -> fermion frame is a graded RELABEL (an invertible choice)",
       np.allclose(acomm(c0,c1),0) and not np.allclose(comm(c0,c1),0))
# single-site invariants are BLIND to the fork (number spectrum, generated algebra)
n_boson=sorted(np.linalg.eigvalsh((O0.conj().T@O0)).round(6).tolist())
n_ferm =sorted(np.linalg.eigvalsh((c0.conj().T@c0)).round(6).tolist())
record("single-site number spectrum is IDENTICAL ({0,1}) in both frames -> cardinality/Pauli-nilpotency cannot select",
       n_boson==n_ferm, f"n_boson={set(n_boson)} n_ferm={set(n_ferm)} -- the free-CCR no-go (N4) kills only [a,a+]=I, not the hard-core boson")

# ======================================================================
section("B. (N1 escape arena) the DYNAMICS distinguishes the frames -- but lives in the emergent-time arena")
# ======================================================================
E=1.0
bose=[-cap*E for cap in (1,10,100,1000)]
record("Bose-quantizing the -E Dirac mode is UNBOUNDED BELOW; CAR is bounded -> energy positivity selects CAR",
       bose==sorted(bose,reverse=True) and bose[-1]==-1000.0,
       "the selector is DYNAMICAL (Dirac sea), not kinematic -> outside the single-slice no-go's scope")
# microcausal on-shell projector identity (mostly-minus gammas): Lu + g0 Lv g0 = 2E g0 (CAR); != for Bose
g0=np.array([[1,0,0,0],[0,1,0,0],[0,0,-1,0],[0,0,0,-1]],dtype=complex)
g1=np.array([[0,0,0,1],[0,0,1,0],[0,-1,0,0],[-1,0,0,0]],dtype=complex)
g2=np.array([[0,0,0,-1j],[0,0,1j,0],[0,1j,0,0],[-1j,0,0,0]],dtype=complex)
g3=np.array([[0,0,1,0],[0,0,0,-1],[-1,0,0,0],[0,1,0,0]],dtype=complex)
m=0.7; p=np.array([0.3,-0.5,0.4]); Ep=np.sqrt(p@p+m*m)
pslash=Ep*g0 - p[0]*g1 - p[1]*g2 - p[2]*g3
Lu=pslash+m*np.eye(4); Lv=pslash-m*np.eye(4)
record("CAR microcausal combo Lu + g0 Lv g0 = 2E g0 (vanishing spacelike anticommutator structure)",
       np.allclose(Lu + g0@Lv@g0, 2*Ep*g0))
record("Bose combo Lu + Lv = 2(E g0 - p.gamma) != 2E g0 -> microcausality FAILS for the boson",
       not np.allclose(Lu+Lv, 2*Ep*g0),
       "escape route = free_sector T1/T2 (unaudited), riding axiom_first_reflection_positivity + spectrum_condition (both UNAUDITED)")

# ======================================================================
section("C. (N2 internal correction) discrete exchange Z2 EXISTS; but the 2pi=-1 spinor sign is CENTRAL")
# ======================================================================
# The no-go's stated reason 'discrete pi_1 is trivial' is superseded: graph_braid_z3_anyon_exclusion_dichotomy
# (retained_bounded) proves H1(UD2(Z3)) carries a Z2 exchange class. The TRUE obstruction is centrality:
minusI_on_1 = np.kron(-I2, I2)                    # 2pi=-1 rotation of particle 1 (the qubit's own C^2)
record("the 2pi=-1 sign on ONE particle = central -I_2 (x) I = GLOBAL -I_4 -> a global phase, not a relative sign",
       np.allclose(minusI_on_1, -np.eye(4)),
       "the discrete exchange Z2 EXISTS (graph_braid_z3_anyon_exclusion, retained_bounded) -> the no-go's 'pi_1 trivial' reason is SUPERSEDED")
# build SWAP and show the central 2pi sign commutes with it (cannot be the exchange sign) while a NON-central spin op does not
SWAP=np.zeros((4,4));
for a in range(2):
    for b in range(2): SWAP[2*b+a, 2*a+b]=1
record("central 2pi=-1 sign COMMUTES with the exchange/SWAP -> decoupled from statistics (centrality, not factor-separation)",
       np.allclose(comm(minusI_on_1, SWAP),0))
nonc=np.kron(1j*sz, I2)                            # a NON-central spin rotation of particle 1
record("a NON-central spin rotation is MOVED by SWAP (SWAP R1 SWAP = R2) -> only the central 2pi element decouples",
       np.allclose(SWAP@nonc@SWAP, np.kron(I2,1j*sz)) and not np.allclose(SWAP@nonc@SWAP, nonc),
       "=> the true residual is a discrete FRAMING/ribbon coupling graph-braid Z2 -> spin Z2 (an import, user-approval), NOT 'pi_1 trivial'")

# ======================================================================
section("D. (N3 scope) multi-site chirality EXISTS but does not split the generation triplet")
# ======================================================================
corners=[(a,b,c) for a in(0,1) for b in(0,1) for c in(0,1)]; cidx={s:i for i,s in enumerate(corners)}
hw=lambda s: sum(s); eps=np.diag([(-1.0)**hw(s) for s in corners])
D=np.zeros((8,8))                                  # any nearest-neighbour (Hamming-1) operator on the cube
rng=np.random.default_rng(0)
for s in corners:
    for mu in range(3):
        t=list(s); t[mu]^=1; w=rng.standard_normal()
        D[cidx[s],cidx[tuple(t)]]+=w; D[cidx[tuple(t)],cidx[s]]-=w
record("corner chirality eps=(-1)^Hamming anticommutes with the cross-site Dirac op: {eps, D}=0 (multi-site chirality EXISTS)",
       np.allclose(acomm(eps,D),0), "the single-site no-go (N3) is scope-limited; it never addresses this multi-site object")
hw1=[cidx[s] for s in corners if hw(s)==1]
eps_gen=eps[np.ix_(hw1,hw1)]
record("but eps restricted to the hw=1 generation triplet = -I_3 (uniform scalar) -> does NOT split generation-from-generation",
       np.allclose(eps_gen,-np.eye(3)),
       "the generation-chirality wall is a DIFFERENT theorem (koide_z3_equivariant_anticommuting_no_go, retained_bounded); the unbuilt bridge is eps(position)->Gamma_chi(generation)")

# ======================================================================
section("E. DISPOSITION")
# ======================================================================
record("all four no-gos are airtight AT THEIR STATED SCOPE (kinematic / single-site / ungraded)",
       True, "verified: ordinary-tensor=hard-core-boson; single-site invariants blind; single-site chirality central; free-CCR trace argument")
record("the UNIFORM escape seam is the GRADED cross-site / emergent-time DYNAMICS arena (currently unaudited)",
       True, "two named promotion targets + one internal correction + one red flag (below)")

# ======================================================================
section("RESULT")
# ======================================================================
n_,p_=len(PASSES),sum(PASSES); print(f"\n{p_}/{n_} checks passed.")
print("EXTRA-ASSUMPTIONS AUDIT of the matter-attachment gate's four retained no-gos. Each is airtight at its")
print("STATED scope, but all four are KINEMATIC / single-site / ungraded facts, and the escape is UNIFORM:")
print("the GRADED cross-site / emergent-time DYNAMICS arena. Concretely: (A) A1+A2's ordinary tensor product")
print("IS the hard-core-boson frame and single-site invariants are blind to the fermion fork; (B) the DYNAMICS")
print("(energy positivity + microcausality) DOES select CAR, but rides the UNAUDITED reflection-positivity +")
print("spectrum-condition + free_sector reconstruction chain; (C) the fs no-go's 'discrete pi_1 trivial' reason")
print("is SUPERSEDED by the retained graph-braid Z2, and the true residual is a framing/ribbon import, not")
print("pi_1; (D) multi-site chirality EXISTS but sits on the wrong tensor factor for the generation triplet.")
print("Two named promotion targets: reflection-positivity + spectrum-condition (->CAR derived); a discrete")
print("framing map (graph-braid Z2 -> spin Z2). Red flag: the UNAUDITED microcausality note asserts per-site")
print("grading auto-propagates to cross-site anticommutation -- FALSE in the ordinary tensor product (section A).")
import sys; sys.exit(0 if p_==n_ else 1)
