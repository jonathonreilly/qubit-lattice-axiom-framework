# Renormalized energy form, its unconfined directions, and the actual ledger

Author analytic exploration, awaiting focused check. The law and quantifiers are CONTRACT1460f698. This companion does not assert a quadratic moment theorem. It tests the proposed coercive-energy route against the actual gates, and keeps the original H energy in every accounting statement. Older main weak-energy and number-offset results are prior scope restrictions, not new conclusions here.

## 1. What the exact normal-form energy does control

Let N=|A|, Cspin=S(S+1), D_full=sum_a D_el,a and D_g=sum_a D_el,a Q_gate,a. Both are nonnegative diagonal forms on the full physical spin carrier, including A holes. Define

  E_rest=H'-delta epsilon^-4 W,
  H'=Y H Y*=delta epsilon^-4 W+delta epsilon^-2 D2+V_rem,
  ||V_rem||<=c delta N,

for the fixed exact order-six local circuit and small epsilon. The bound follows from the bounded-incidence D4,D6 and exact R_H; it is not a global bound on ||Y-I||.

The actual expansion is

  D2=D_g/Cspin+H_h,
  H_h=sum_a F_a F_a*+sum_a F_a*F_a(Q_gate,a-1)
                             +sum_(a!=c)[F_a,F_c*].         (E1)

The diagonal electric correction is removed explicitly. The complete hard-core row classification gives at most756 two-hop paths per input A hole, including the returning paths. The three counts are36 same-hole,648 absent-gate,72 cross-hole paths. Every normalized spin path has modulus at most one. H_h is Hermitian, and its absolute row sum is at most756 W(input). Therefore

  -756 W<=H_h<=756 W.                                      (E2)

For each a, 0<=D_el,a<=6 Cspin n_a and

  1-Q_gate,a <=sum_(c!=a,distance(c,a)<=2) w_c.

There are eighteen such A neighbors. Summing the nonnegative diagonal products gives

  0<=D_full-D_g<=108 Cspin W.                              (E3)

Using delta epsilon^-2/Cspin=K in(E1)-(E3),

  K D_full-864 delta epsilon^-2 W-c delta N
       <=E_rest
       <=K D_full+756 delta epsilon^-2 W+c delta N.         (E4)

Thus the checked actual rotated hole estimate gives

  |<E_rest>_sigma(t)-K<D_full>_sigma(t)|<=C_T N.             (E5)

This prices the local A-occupancy gate losses using finite-spin capacity. It proves that a uniform upper bound on the renormalized mean would control the actual VACANT-B electric form D_full in this frame. It does not prove that upper bound and it does not control every link's E².

More explicitly, with Q2_active=sum_(a,b) n_a(1-n_b)E_ab², integer fields give

  (1/2)Q2_active-3N <=D_full <=(3/2)Q2_active+3N.             (E6)

Missing A factors in the vacant-B square cost at most6 S² W, whose actual expectation is O_T(N) under the coupled scaling. The remaining difference from the full Q2 is the occupied-B field square sum sum_(a,b)n_b E_ab². It cannot be paid by W or the gate-error bound(E3).

The initial E_rest mean is O(N): the local commutator ||[E_e,Y]||<=c epsilon gives <Q2>_sigma(0)<=c epsilon²N; D_full<=2Q2 on integer fields and the actual <W>_sigma(0)<=c epsilon²N, together with(E4), suffice. This is consistent with the divergent full physical initial energy described below.

## 2. Exact physical noncoercivity witness

Fix L=8. Every A site has q=+1 and every B site will be occupied. For each (y,z) row, pair consecutive B sites along x, choosing signs plus then minus. Join each pair through its intermediate A. Put E=-1 on that A-to-plus-B edge, +1 on its A-to-minus-B edge, and zero on all other edges. Then div E=q-1_A at every vertex. All A divergences vanish, while the B divergences equal their signed charges.

Add m units of a divergence-free elementary square circulation. Every physical word remains Gauss compatible. Choose m=S-1, with the circulation sign and square in the control below; every field stays in the spin box. Because EVERY site is occupied,

  F_a psi=F_a* psi=j_mu psi=0, D_el,a psi=0, W psi=0.

Consequently H psi=0 for every epsilon,S and fixed positive couplings, for both original instruments. Each local normal-form generator built from W,T,C and their commutators vanishes on this entire filled subspace, so Y psi=psi and E_rest psi=0 as well. Yet Q2 grows quadratically with m at this fixed volume. Thus no all-state inequality of the form

  K Q2 <=a E_rest+b epsilon^-2 W+c N I

with constants independent of S can hold, even on the actual physical Gauss carrier. The same obstruction defeats an all-state control by the full H. This is a missing-gate obstruction, not a statement that the actual Omega ensemble reaches such fields with appreciable probability.

There is an exact legal primitive word connecting Omega to the witness. On the square a=(0,0,0),b=(1,0,0),c=(1,1,0),d=(0,1,0), use hops a->b,c->d,b->c,d->a, repeated m times. They restore the original matter and add a circulation. Then for every paired B pair, hop its intermediate A charge to the first B and perform the original plus birth on the second B edge, restoring that A. All selected spin coefficients are positive for m=S-1. This establishes algebraic source accessibility by actual primitive words only. The exact unconditioned history contains coherent sums over Hamiltonian paths; this word does not bound its amplitude after those sums, its probability, or its contribution to Omega's moment. No actual-state counterexample is claimed.

For the specified square and pairing, N=256 and direct independent edge counting gives

  Q2=256+4m²+2m,      min selected spin coefficient squared=2/(S+1).

Exactly one of the four circulation links overlaps the paired reference flow, with the same sign; this fixes the linear term2m. The four-spins control checks all intermediate Gauss identities and retains the full final field lists. It tests this scoped witness, not an energy-growth simulation.

## 3. The full physical energy ledger cannot be dropped

At every finite spin and volume the actual identity is

  <H>_rho(t)=<E_rest>_sigma(t)+delta epsilon^-4<W>_sigma(t),  (E7)

and the exact first-law expression supplied by the GKSL model is

  Delta<H>=kappa epsilon^-2 integral_0^t sum_mu
       <J_mu* H' J_mu-{J_mu*J_mu,H'}/2>_sigma ds.            (E8)

The Hamiltonian contributes zero to its own mean derivative. Equivalently substitute(E7) on both endpoints of(E8). No gap term is silently erased. E_rest is a circuit-dependent accounting diagnostic, not a different adopted physical Hamiltonian. The microscopic model contains no reservoir specification making(E8) heat or work. Any implementation must still include its apparatus/controller/interaction endpoint and external-work terms; none is constructed here.

For the actual bare Omega, the six outward returns per A site give

  <H>_Omega=6 delta epsilon^-2 N.

This divergent initial full energy is consistent with the rotated gap population6 epsilon²N plus higher orders. It is one reason that the fixed-graph main theorem for uniformly full-energy-capped inputs cannot simply be applied to Omega. The already-main finite-window energy note also gives an exact actual-graph weak-law/moment counterexample. Neither prior is being republished as a new conclusion.

## 4. A useful correction of the off-grade bookkeeping, not of the remaining loss

Let P denote W-grade averaging, H_d=P H', V=H_d-delta epsilon^-4 W, and R=(1-P)H'. Thus E_rest=V+R, ||R||_local=O(epsilon³), V is neutral with local strength O(epsilon^-2), and [H_d,V]=0. Write L'^*=A+B, A=i delta epsilon^-4 ad_W, and B=epsilon^-2 B2+O_local-action(epsilon^-1).

Set R_V=(1-P)L'^*V. Its leading local strength is O(epsilon^-3), since the off-grade jump cross map has strength epsilon^-1 and V has strength epsilon^-2. The leading epsilon^-2 map preserves grades. Define

  C1=(i epsilon^4/delta) I R_V,
  C2=(i epsilon^4/delta) I(1-P)B C1.

Then C1,C2 have bounded local strengths O(epsilon),O(epsilon³), and

  L'^*(V+C1+C2)=P L'^*V+P B C1+B C2.

The apparent P epsilon^-2 B2 C1 vanishes exactly. The remaining right corrections have strength O(1),O(epsilon). Since [H_d,V]=0,

  P L'^*V=kappa epsilon^-2 sum_(mu,r) D[J_(mu,r)]^* V.

Consequently the actual signed balance obeys

  Delta<E_rest>=kappa epsilon^-2 integral_0^t
          sum_(mu,r)<D[J_(mu,r)]^*V> ds+Err,
  |Err|<=C N(T+epsilon),       0<=t<=T.                     (E9)

This algebra controls the full off-grade cross contribution at bounded integrated density. The diagonal-grade expression is an identity for a corrected TEST in the original state. It does not replace the original observed instrument or evolve a secular density.

Equation(E9) does not close(E5). The dangerous same-negative-grade LOSS remains. For a given jump, cancel all disjoint energy terms first and let V_mu be the remaining neutral bounded local energy sum, of norm O(epsilon^-2). Its negative-grade gain can be bounded by this norm times the exact negative activity, so D10 prices the sum of those gains by O_T(N). A negative-grade J_r V_mu annihilates the filled local input, but its norm bound alone gives

  |<J_r*J_r V_mu>|
       <=C epsilon^-2 sqrt(<J_r*J_r>) sqrt(<Q_U>).

After the jump prefactor kappa epsilon^-2 and time Cauchy, the available integrated activity O(epsilon^4) and hole occupation O(epsilon²) give O(epsilon^-1), per bounded local incidence. This is not finite. The negative-grade cross-loss needs an additional actual-state cancellation/passivity or holding estimate. The already-checked arbitrary-state dark-current example makes an automatic loss-domination replacement especially unjustified.

Positive-grade terms have jump coefficients O(epsilon²), so their local V drift has O(1) norm after all prefactors. Neutral-grade terms retain the full source's gated-electric gain/loss and can depend on occupied-background coherences; no ordinary-field argument here prices their entire gated-energy drift. The occupied-B electric omission in(E6) would remain even if these drifts were controlled. Thus this energy route has TWO separately stated obstacles: a genuine drift estimate, and the absent occupied-link coercivity. The companion direct Q2 calculation avoids the latter by keeping the actual ungated field observable; it leaves a precise fast Hamiltonian current instead.

## 5. Evidence and unresolved target

The companion QUADRATIC_BALANCE proof is analytic. The fresh control tests four exact Gauss words,60 original single-edge increments and the declared source-word counts. Its first version reached the 5CPU-second hard cap with empty scientific output. The cause was repeated linear-list membership in every Gauss check. The exact failed script/captures/receipt are preserved in history_cpu_cap; the only repair replaces that membership by a set, with no physical assertion or expected-value change. The rerun completed in2.314567 child CPU seconds,2.386513 external wall seconds and25,542,656 bytes child peak RSS, under the same5CPU/30wall/100MiB price. It made1072 intermediate Gauss checks; internal science time and RSS are separately recorded. The RSS ceiling was checked at return, not asserted as an operating-system hard memory cap. No other new computation was run.

No new uniform quadratic moment, quadratic-tail bound, actual energy convergence, energy/W1 convergence, unique effective process, selected physical energy, or native-axiom result is claimed. A uniform quadratic moment would still not imply quadratic uniform integrability. The explicit current/first-field-residence consumer in the companion is the next actual-state target; the frozen proofs require focused independent reconstruction before substantial reuse.
