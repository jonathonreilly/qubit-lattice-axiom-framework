# T34 pre-registration (written before any of the test scripts below was run)

Author: Claude Sonnet 5.5 (same family as supervisor; same-family check, not a referee).
Only run before this file: lane script mh_sens.py (copy) -> m_H = 125.138 GeV at y_t = 0.9176 (re-run of L07-W10's claim; matches).

## Hypothesis H*
T34 is not one independent wall.
 (a) The Higgs DOUBLET is decided upstream, by whether the matter sector contains weak-singlet
     fermion modes (T22/T25). On a Fock space whose fermion modes are all weak doublets, the centre of
     SU(2) acts as (-1)^F, so no bosonic doublet and no fermionic singlet can be made.
     With a weak-singlet sector added, doublet bilinears appear automatically, but several (not one).
 (b) The lane's EWSB test (is G_eff > G_crit?) is scheme-dependent and, whatever it answers, does not
     produce v: a condensate on the lattice sits at O(1/a), so v/M_Pl = 2e-17 is a scale question (T31).

## Test A  (script A_fock_census.py) -- PRIMARY, decides (a)
Model: the 8-state left-handed surface of docs/GAUGE_MATTER_CLOSURE_GATES_2026-04-12.md
(Q_L = (2,3)_{+1/3}, L_L = (2,1)_{-1}, convention Q = T3 + Y/2), 8 fermion modes, Fock dim 256.
Then the supplied right-handed sector (u_R (1,3)_{4/3}, d_R (1,3)_{-2/3}, e_R (1,1)_{-2}, nu_R (1,1)_0),
16 modes, Fock dim 65536.  Operators built by Jordan-Wigner; SU(2), SU(3), Y, F explicit.
PASS readings (all must hold):
  A1  L-only: every one of the 256 states has 2T = F mod 2 (exp(2 pi i T3) = (-1)^F): zero bosonic
      states with half-integer T, zero fermionic states with integer T (weak singlets are all bosons).
  A2  L-only, F=2 sector (28 states): no colour-singlet state with T = 1/2 (no doublet scalar).
  A3  Full L+R space, F=2 sector (120 states): colour-singlet, T=1/2 states number exactly 4 and
      all are L-R bilinears; hypercharges (Y of the state, creating psi_R^dag psi_L-type pairs used as
      operators on the vacuum) come out as two with +1 and two with -1 (up to sign convention),
      i.e. four composite doublets, two Phi-type and two Phi-tilde-type.
  A4  Record-domain check (routes that put the doublet in the site record M_2(C)): under conjugation
      by SU(2) the 4 complex = 8 real dimensions of M_2(C) split as spin content {0, 1}; no spin 1/2.
      Under LEFT multiplication they split as two doublets (so a doublet exists only if left
      multiplication is a symmetry, which is not an automorphism of the algebra).
FAIL readings: any bosonic T=1/2 state in A1/A2; A3 count different from 4; a doublet in A4 under
conjugation.  Fail of A1/A2 would kill H*(a) and mean the L-surface can supply a doublet alone.

## Test B  (script B_condensate_scale.py) -- decides (b)
B1  Reproduce the lane's numbers: u0 = 0.5934^(1/4), G_crit = u0^2/4, G_eff = 1/(2 N_c), ratio 0.866.
B2  Standard strong-coupling leading-order staggered mean field (Kawamoto-Smit): after the Haar
    integral the fermion hopping is gone; F(sigma) = d sigma^2/(4N) - N ln(m + d sigma/(2N)), chiral limit
    m = 0.  Scan N = 2..6, d = 2..4.
    PASS: broken (interior minimum at sigma0^2 = 2 N^2/d) for every (N, d), including N = 3, d = 4,
    i.e. LO strong coupling and the lane's "hybrid" (strong-coupling tree term + weak-coupling hopping
    u0) give OPPOSITE phases for the same N_c, so the lane's 0.866 is not a scheme-independent statement.
    FAIL: KS mean field symmetric for (3,4)  -> the lane's verdict would be the robust one.
B3  Scale.  In the hybrid model sigma_min^2 = 16 (G - G_crit); require sigma_min = v/M_Pl = 2.0e-17
    -> required (G/G_crit - 1).  In KS: sigma0 = O(1) lattice unit.
    PASS: required tuning < 1e-30, and KS scale O(1)  -> either way the condensate is at 1/a unless
    tuned, so W2 is really the hierarchy question.
    FAIL: tuning of order 1e-3 or larger (no fine-tuning needed).

## What each outcome would mean for the verdict
 A1..A4 and B2/B3 pass  -> MISFRAMED: T34 dissolves into T22 (doublet), T31 (scale), plus the
                            already-priced input lambda(M_Pl)=0.
 A1 or A2 fails         -> the doublet has an independent route; outcome would be STANDS with that route.
 B2 fails               -> W2 stays as the lane states; verdict for the breaking part becomes STANDS.

## Addendum 1 (written after Test A and B outputs, before A7 was written or run)
Test A run 1 printed A3 = False because the script compared 8 T3-components with the pre-registered
"4 doublets".  Physics matched the pre-registration (8 components = 4 doublets, Y_op = +1,+1,-1,-1); the
check was fixed to count multiplets (A_output_run1.txt keeps the original output).  Test B: B1, B2, B3 as
pre-registered (B2's minimisation is analytic; the scan only confirms it).

Reading of docs/GAUGE_MATTER_CLOSURE_GATES_2026-04-12.md and scripts/frontier_right_handed_sector.py showed that
the repo's R-sector is a supplied weak-neutral assignment ("singlets by the chirality of weak interactions",
script lines 511-516, 481-484), and that its own script says the KS su(2) generators T1, T3 anticommute with gamma_5.
So Test A7 (script A7_ks_su2_chirality.py) is added, with predictions fixed now:
  A7a  On the repo's 4D staggered C^16 (G0=zzzx, G1=xIII, G2=zxII, G3=zzxI, gamma_5=G0G1G2G3) the KS su(2)
       T_k = sigma_k/2 on factor 1: T1, T3 anticommute with gamma_5, T2 commutes.
  A7b  The Casimir of T on C^16 is uniformly 3/4: 8 doublets, no weak singlet anywhere (so the weak-neutral R
       sector is not produced by this su(2)).
  A7c  The chirality-projected action P_L T_k P_L generates a Lie algebra of dimension 1 (a u(1)), not su(2).
  A7d  The taste commutant (dim 16) commutes with gamma_5 and has equal traces on L and R (so any su(2) taste
       symmetry acts identically on both chiralities: vector-like).
PASS = all four as predicted.  A7 fail (e.g. a chirality-respecting su(2) subalgebra of dimension 3) would mean
the repo's structure DOES supply a chiral weak su(2) and T22-side of the price would be weaker than claimed.
