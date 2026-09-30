# Actual source winding after formation

Author derivation under WINDING_CONTRACT2c01efab, independently unchecked. This proof uses the landed local-pair formula and actual original marks directly. It does not use the new phase/slab packet under separate check.

## 1. Exact law and a field-band sign fact

Work on a fixed cubic torus of even side L divisible by4, L>=8, n=L³/2, with the supplied q=0,+1,−1 hard-core matter, integer rotors and div E=q−1_A. All edges are oriented A to B. The W0 rotor target from bare Omega is exactly

 h=K D+delta H4,    H4=−Q,
 Q=2 sum_(unordered a,c at distance2) (F_c F_a P0)* (F_c F_a P0),
 b_mu=j_mu F_a P0,
 R=sum_mu b_mu* b_mu,
 A=−i K D+i delta Q−(kappa/2)R.                         (1)

A is the complete original no-event generator. The original labels are either resolved (edge,sign) or the unnormalized coherent edge sums. The effective density rho_eff(s) uses h and all sqrt(kappa)b_mu jumps, including every later birth. The positive leading source coefficient is

 B_mu^+=−F_a j_mu F_a P0,
 tau_mu(s)=B_mu^+ rho_eff(s) (B_mu^+)*.                  (2)

This source coefficient is not an extra observed event or an independently supplied preparation. No finite-epsilon equality with(2) is asserted here.

In the physical charge/integer-field basis, F_a, j_mu and b_mu have nonnegative real entries, including the complete coherent sums. Therefore Q and R have nonnegative real entries and −B_mu^+ does also. Q has electric l1 displacement at most4, each b_mu at most2 and B_mu^+ at most3. Although b_mu itself contains two shifts, its LOSS has only band2:

 b_mu* b_mu=P0 F_a* (j_mu* j_mu) F_a P0.                (3)

For a resolved mark, j_mu* j_mu is the empty-A/empty-B diagonal projector. For a coherent edge its two output charge signs are orthogonal, so cross terms vanish and the diagonal projector is multiplied by2. Summing the resolved labels gives the same R. Thus(3), not the naive band4 of two unrelated b words, proves band2 and entrywise positivity of the complete original loss. D is diagonal and has band0. All coherent recycling amplitudes remain inside the original b_mu; no sign/path label is observed.

## 2. A legal preparation family at fixed B count

Use coordinates modulo L. Put a0=(0,0,0). The first ordinary mark is the edge a0->(0,1,0), with sign+ in the resolved case or its complete coherent edge label. Select for the existence argument its Fa0 path to b0=(1,0,0). This selected component leaves A charges all+, B charges + at b0 and − at(0,1,0), and fields−1 on(a0,b0), +1 on the marked edge.

Let C be all A centers with y=0 modulo4, x+z even, except a0. There are n/4−1 such centers. Choose any b−1 distinct centers from C, where

 1<=b<=n/4.

At each chosen center a take the actual ordinary mark to a+e_y (sign+ or coherent edge) and select its outward path to a−e_y. These B pairs are disjoint: their y coordinates are1 or3 modulo4 and each pair fixes x,z. None meets the x ring y=z=0. They also do not meet the first B pair, because a0 is excluded. Every selected A center is distinct, and its chosen paths are legal in any fixed ordering. The selected final A charges remain all+; each extra pair consists of one B+ and one B−. All2b selected field edges are distinct and have magnitude1.

Let Phi_b=b_mu_b ... b_mu_1 Omega be the COMPLETE original word for those labels. It is a finite physical vector with nonnegative coefficients and field support ||E||_1<=2b. The selected configuration chi_b occurs with coefficient at least1. The construction does not replace Phi_b by chi_b in the process; chi_b is used to certify one nonzero coefficient of the complete operator product.

### A dark-input variant with the same count and field price

For any4<=b<=n/4, replace the arbitrary preparation subset by the following choice. In addition to the first birth, include the grid centers a_minus=(4,0,0) and a_plus=(4,4,0), with the same old −y/marked +y paths, and add the center a_z=(4,2,L−2), with old destination a_z−e_z and marked destination a_z+e_z, sign+ or coherent edge. Take the remaining b−4 grid centers from C excluding a_minus,a_plus. There are n/4−3 available grid centers, so the requested range has enough choices. The special z pair lies at y=2 and is disjoint from all grid pairs, the first pair and the x ring. All A centers and all selected field edges remain distinct.

At c0=(4,2,0), these three background births occupy precisely its neighbors c0−e_y, c0+e_y and c0−e_z needed below. Its other three neighbors c0+e_x,c0−e_x,c0+e_z remain empty. Thus the later positive source fills the whole six-site star, and its final word satisfies G Xi_(b,r)=0 for every r. This is a DARK actual source component; it does not assert invariant darkness under H2. The same2b field norm, complete-word positivity and ring transport proof apply unchanged.

## 3. An actual four-hop pair word carries a record around the torus

On the x ring, chi_b has just one occupied B site, b0, with charge+. Every ring A has charge+. If that B record is at x=4j+1, put

 a=(4j+2,0,0), c=(4j+4,0,0),
 d=(4j+3,0,0), e=(4j+5,0,0).

The centers a,c have distance2 and share d. In the actual Q term2(F_c F_a)*F_c F_a choose, in application order,

 a -> d,   c -> e,   d -> c,   (4j+1,0,0) -> a.          (4)

The first two are outward hops and the last two are the required inward adjoints, in the exact order F_a,F_c,F_c*,F_a*. All donor charges are+, both outward destinations are empty, and every intermediate step preserves Gauss. Equation(4) moves the B+ four sites forward, restores both A+ records and has coefficient2 in Q. Off-ring occupied B sites do not block any chosen path.

After L/4 such Q factors the B+ returns to b0 and every matter charge is restored. The field increment is the divergence-free unit circulation C_x on that x ring:

 (C_x)_(a,a+e_x)=−1,  (C_x)_(a,a−e_x)=+1

for every ring A a. Repeating r>=1 times uses

 m=rL/4                                                   (5)

Q factors and adds r C_x. Their complete Q^m coefficient is at least2^m, since every other path coefficient is nonnegative. The initial birth field on(a0,b0) has the SAME sign as C_x. This sign is essential to the saturation argument below.

## 4. Append the actual positive source and isolate the first Taylor order

Choose source center c0=(4,2,0), the mark to c0+e_z (resolved sign+ or coherent edge), and select the first outward source path to c0+e_x and the last to c0−e_x. These three B sites have y=2, are distinct and empty in chi_b, and are disjoint from all preparation B sites and the ring, including the special z pair in the dark-input variant. The source is legal. Let Xi_(b,r) be the resulting final physical basis word after preparation, r circulations and this source.

Its A hole is c0, its B count is k=2b+3, its minus-charge count b+1, and its total charge n. Thus it belongs to the actual physical W1 sector. Its electric field is exactly

 E_(b,r)=E_prep+r C_x+E_source,
 ||E_(b,r)||_1=2b+3+rL=2b+3+4m.                       (6)

All field supports are disjoint except the first birth edge and C_x, where they add with the same sign. At the periodic x cut between L−1 and0, the preparation and source have zero crossing field. The signed electric flux of E_(b,r) there is r in the direction of C_x. This is a noncontractible electric circulation relative to one FIXED final matter configuration, not a charge/Gauss violation.

For ordered original birth times0<t1<...<tb<s, write g0=t1, gi=t_(i+1)−ti and gb=s−tb. The COMPLETE source-history amplitude is

 f(g)=<Xi_(b,r), B_mu^+ e^(gb A) b_mu_b ... b_mu_1 e^(g0 A) Omega>, (7)

with the intervening exponentials at every gap understood. Consider the total-degree Taylor expansion at all gaps zero. A product with j generator factors can move field l1 by at most4j+2b+3. Hence every coefficient of degree j<m vanishes against(6). At degree m, every generator factor must come from i delta Q: even one R factor loses at least two units from that maximal band, and any D or other zero-band term loses four. This argument includes the entire exact loss R, not a jump-only approximation.

Consequently the leading homogeneous term is

 f(g)=−(i delta)^m P_m(g)+O(s^(m+1)),
 P_m(g)>=0 for g_i>=0,
 P_m(g)>=2^m gb^m/m!.                                  (8)

P_m has nonnegative real coefficients because the COMPLETE Q, b_mu and −B_mu^+ products do. The selected path(4) placed entirely in the last gap proves the last inequality. This retains every coherent same-label path; it does not infer a full amplitude from a lone path in a sum of unknown signs. The unique common complex phase at the first possible degree is precisely what precludes cancellation.

## 5. Unbounded-domain justification and an explicit, deliberately costly time

Set V=1+sum_e|E_e| on the finite graph. D is diagonal, commutes with V, and0<=D<=2V². For a bounded operator O with V bandwidth at mostd, phase averaging against V gives2d+1 bands, each of norm<=||O||. Since V>=1,

 ||V^p O V^(−p)|| <= (2d+1)(1+d)^p ||O||.               (9)

The main pair theorem gives M_Q=38880n as a safe bound for||Q||. The resolved b has norm<=5 and there are12n resolved labels, so M_R=300n bounds||R|| for BOTH original instruments by(3). Use common bounds||b_mu||<=10 and||B_mu^+||<=72. Define

 V_p=9*5^p delta M_Q+(5/2)*3^p kappa M_R,
 a_p=2K+V_p,  J_p=50*3^p,  I_p=504*4^p.                (10)

In the KD interaction picture, (9) gives

 ||V^p e^(tA) V^(−p)||<=exp(V_p t),
 ||V^p A V^(−p−2)||<=a_p.                              (11)

These are graph-norm statements; no norm continuity of the unbounded electric generator is assumed. Finite physical words lie in every V-power domain. Bounded finite-band b_mu and B_mu^+ preserve these domains, and the interaction-picture Dyson construction proves strong propagation and differentiation on them. This also justifies every fixed-order joint Taylor coefficient in(8).

More explicitly put p=2(m+1), u_i=g_i/s, sum u_i=1, and differentiate f(su) m+1 times. Each generator lowers the available V weight by2; each ordinary mark costs at most J_p, and the source at most I_p. All intermediate p'<=p are dominated by(10), all evolution durations sum to s, and the multinomial factors sum to(sum u_i)^(m+1)=1. Thus, uniformly on the simplex and for s<=min(1,1/V_p),

 |d^(m+1) f(su)/ds^(m+1)|
       <= e I_p J_p^b a_p^(m+1) =: C_(L,b,m).          (12)

Taylor's integral remainder is therefore at most C s^(m+1)/(m+1)!. A valid explicit positive source-time scale is

 s_* = min(1, 1/V_p, (m+1)delta^m/(2 C_(L,b,m))).        (13)

The dependence on L,b,r,K,delta,kappa is fully retained and can be enormous. No uniform lower time or useful numerical probability is asserted. On the history region tb<=s/2, equations(8),(12),(13) give, for0<s<=s_*,

 |f(g)| >= delta^m s^m/(2 m!).                          (14)

## 6. Genuine positive weight in the actual continuously generated source

The original quantum-jump expansion of rho_eff(s) is positive and includes the chosen b-label history with weight kappa^b times its ordered time simplex. Restricting that positive integral to0<t1<...<tb<s/2 has volume(s/2)^b/b!. Keeping only this contribution and using(14) proves

 <Xi_(b,r), tau_mu(s) Xi_(b,r)>
  >= kappa^b delta^(2m) s^(2m+b)
                   /[2^(b+2) b! (m!)²]  >0,
            0<s<=s_*,  m=rL/4.                        (15)

Summing source marks only increases the left side. No actual ordinary mark, waiting factor, coherent sum, loss or later-birth channel was deleted from the dynamics; a positive history contribution supplies a lower bound. The source coefficient is still the original derived B_mu^+, not a proxy observed process.

At fixed b (hence fixed k) and every r>=1, there is therefore an actual source word with arbitrarily large noncontractible electric circulation and the same final matter configuration. The interval s_*(r) depends on r; this does NOT establish unbounded support at one common positive time by itself. It DOES rule out a proposed exact finite winding cutoff or zero-winding invariant of the actual source for all small times after formation. It remains valid for b up to n/4, so it is not a fixed-small-global-B construction.

For the dark-input preparation with4<=b<=n/4, every Xi_(b,r) in(15) obeys G Xi_(b,r)=0. Consequently the same lower bound applies to the diagonal component of the ACTUAL dark-compressed source D_dark tau_mu(s) D_dark, D_dark=1_(G=0). It does not establish survival for any positive fast duration.

There is also a precise infinite-dimensional cyclic-span statement. Let v_j=B_mu^+ A^j Phi_b. Each v_j is a finite-field vector. It belongs to the closed linear span of actual source-history vectors: zero preliminary waiting gaps are strong limits of positive gaps, and the jth derivative at the last gap zero is a finite-difference limit in that closed span. For m_r=rL/4, equation(6) gives <Xi_(b,r),v_(m_j)>=0 when j<r, while the diagonal j=r is nonzero by the same all-Q sign argument. Hence {v_(m_r):r>=1} is linearly independent. In the dark variant the same proof applies after D_dark compression, because D_dark Xi=Xi. This is not fiber faithfulness: nonzero populations or an infinite-dimensional global span do not imply overlap with an arbitrary coherent invariant dark module. No such inference is made.

## 7. What remains open

The initial W0 no-birth sector indeed has only plaquette magnetic motion and zero winding from Omega. Equations(4)-(15) show exactly why extending that invariant through actual formation is false. They provide a source-sensitive obstruction to one full-module shortcut, with its actual history/time price. They do not decide full generic observability, provide a sourced invariant dark vector, or prove source cyclicity in every charge/mask phase fiber.

Nor do they give a long-age rate, finite-spin survival transfer, a common epsilon-dependent source bound, mean-residence/energy UI, autonomous work or physical-law selection. The finite-spin boundary weights are not substituted for rotor unit weights. Only the fixed-graph leading rotor source is addressed. A control of the selected words can corroborate geometry/Gauss/circulation; it cannot replace the complete-operator sign, band and unbounded-domain argument above.
