# ba8 criteria (BFT lane A, session 8). Written before checks/ba8_fun.py existed.

Plan: BFT_A §36.4. Abelian Setting LIN, L = 3, kappa = 1, trivial background, m = 0. Representatives of the plaquette
response Y^p: CG (min-norm CG solution of ba5_y.Chain, orthogonal to the composite gauge directions), C0 (S_C0 of §36.0:
lambda = 0 at the level-k roots, d*Y_0 = 0 at all other level-0 sites), C0# (C0 plus the funnel correction Xi sigma).
**Sign note (found while writing these criteria, before any script):** RF's funnel term in Y_l is -d Phi_l, so the
correction that cancels it is x -> x + Xi sigma(x); the §36.0 definition of Pi^# carries the opposite sign. C0# uses
x + Xi sigma(x). This is recorded later in BFT_A as a dated precision.

E1 (exactness; PASS iff relative error <= 1e-9 for every item; FAIL means BA8-F1/BA8-F5 occur):
 (a) BL-2 (b) one step: Q v = Q_str v - d h(v) for random level-l 1-forms v (h = averaged axial line integral from the
     root, 24 orders, offsets in [-H, H]^4);
 (b) push-down identities used by Lemma DF on random chains (k = 2, T = 2):
     <j, Y_l> = <(Q^(0->l))^T j, Y_0> - sum_{m<l} <(Q^(m+1->l))^T j, r_m(Y)>, and
     <(Q^(0->k))^T b, Y_0> = <b, Y_k> + sum_{i<k} <(Q^(i+1->k))^T b, r_i(Y)>;
 (c) Proposition RF's identity for sp_l(x; Z) at every level-l site Z, 1 <= l <= k - 1, random chains, k = 3, T = 1.

E2 (spikes; trend rules with a-priori thresholds; outcomes decide BA8-F3, BA8-F6):
 setting k = 3, T = 1 (fine side 27), Z = (4,4,4,4) (l(Z) = 2), p = the (0,1)-plaquette at Z + o for
 o in {(0,0,0,0), (1,0,0,0), (-1,0,0,0), (0,0,1,0), (1,1,0,0)}; reference p_ref at (8,8,8,8) (as in REVIEW_BFT_A_S7 D2).
 rho(o) := |sp_2(C0; Z)| L^4 / (|sp_1(C0; Z)| L^2).
 **BA8-F3 occurs iff** for at least one o: rho(o) >= 4 AND |sp_2(C0; Z)| L^4 >= 2 max|Y_2(C0; p_ref)| L^4.
 (A level-independent spike gives rho ~ L^2 = 9; PW's scaling gives rho ~ 1.)
 **BA8-F6 occurs iff** at that o: |sp_2(C0#; Z)| L^4 > 0.5 |sp_2(C0; Z)| L^4.
 Reported for every representative: sp_l(Z) L^{2l}, max|Y_l| L^{2l}, sum|Y_l| / L^{k-3l} (the (PW-i) ratio), l = 0, 1, 2.
 Also k = 2, T = 2 (side 18): Z1 = (7,7,7,7) (l = 1) and the level-2 root (4,4,4,4), p at offset (1,0,0,0): sp_0, sp_1
 in CG and C0 (informational).

E3 (geometry): eps(p, Z) := phi_1(y)(Z) for y the C0 level-0 field, all o of E2. **BA8-F4 occurs iff**
 |eps| <= 1e-10 for every o. Informational: eps of the CG field.

E4 (PW-cc, informational): |<j, Y^p_l>| / (L^{k-3l} max|j|) for 3 random co-closed level-l j (k = 3, T = 1), l = 0, 1, 2.

Run: numeric lock (mkdir; one acquisition; one rmdir), nice 10, OMP/OPENBLAS/MKL/VECLIB threads 1,
PYTHONDONTWRITEBYTECODE=1, python3 without -I, no timeout, no trap, no pkill; abort if load > 8 or free RAM < 25%.
No constant derived in session 8 appears here.
