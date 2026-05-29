# Assumptions Audit: Koide Q=2/3 hardening (self-adversarial)

## Date
2026-05-28

## Object under audit
The hardened derivation
`koide-q23-extremal-from-a1a2-2026-05-28.md` (Step-3 hardening), runner
`scripts/koide_q23_central_trace_hardening_2026_05_28.py`.

This is an adversarial pass on my OWN result: every load-bearing claim
is listed, classified EXACT / ASSUMPTION / KILLED, and stress-tested.

## Claims classified

### EXACT (proven, no hidden assumption)
1. **Q = purity of the sqrt-mass distribution.** `Q = sum p_k^2`,
   `p_k = sqrt(m_k)/sum sqrt(m_j)`. Algebraic identity. VERIFIED.
2. **Q = 1/(d cos^2 theta); Q=2/3 <=> cos^2 theta=1/2 <=>
   |s_par|^2=|s_perp|^2.** Geometry. VERIFIED (theta=44.9997 deg).
3. **Generation space = Cl(3) grade-1 = regular rep of the color-Z_3
   automorphism.** The cyclic permutation of (sigma_1,sigma_2,sigma_3)
   has eigenvalues {1, w, w^2}; the eigenvalue-1 eigenvector is the body
   diagonal (1,1,1)/sqrt3. So the democratic direction is FORCED as the
   unique Z_3-fixed axis -- it is not an external choice. VERIFIED.
4. **Frobenius-Schur: R[Z_3] = R (+) C.** Fluctuation isotypic is ONE
   2-real-dim block carrying a complex structure J with J^2=-I; J is the
   Cl(3) grade-2 bivector dual to the body diagonal (rotation generator
   about (1,1,1)). VERIFIED (Kahler (1,1), 1 complex dof).
5. **Three canonical isotypic weightings map to the three special Koide
   values.** (p_triv,p_fluct) = (1,0)/(1/2,1/2)/(1/3,2/3) give Q =
   1/3 / 2/3 / 1 = (Q_min, midpoint, Q_max). VERIFIED.
6. **B(d)=2 (FS real-block count) only for d in {2,3}.** VERIFIED.
7. **d=3 double-characterization is transversal.** Delta(d)=Q_mid-Q_equi
   = (d-3)/(2d), simple zero at d=3, slope 1/6. VERIFIED.

### KILLED (claims I made earlier that FAILED audit)
K1. **"Equipartition = the canonical / Plancherel central tracial
    state."** FALSE. The canonical group-algebra trace weights blocks by
    dim^2/|G| = (1/3, 2/3), giving Q = 1, not 2/3. The Lane-4 lit lead
    ("missing primitive = Frobenius-Schur central tracial state"), read
    literally as the canonical trace, does NOT close the gap -- it lands
    on Q_max. Recorded as a no-go for that specific route.
K2. **"A pure qubit (|n|=1) forces equipartition" (original Step 3).**
    FALSE as stated. In the Bloch-trine embedding, purity gives a^2+b^2=1
    but leaves the ratio b^2/a^2 free; equipartition additionally needs
    b^2=2a^2. Purity is at most a consistency condition, not the forcing.
K3. **"Equipartition ties to rho_ref = (x) I/2."** FALSE. rho_ref
    restricted to generations is the maximally mixed (uniform) packet =
    democratic = Q=1/3 (Q_min), the opposite extreme from 2/3.

### ASSUMPTION (residual, load-bearing, NOT yet derived)
A1*. **The physical packet sits at EQUAL-BLOCK weight (1/2,1/2) =
     maximum entropy over the B=2 Frobenius-Schur block label.**
     - This is strictly weaker and sharper than the original Step 3.
     - It is tied to A1: the qubit is a 1-bit (2-valued) primitive; the
       FS decomposition yields a 2-valued block label exactly for
       d in {2,3}; max-entropy over a 1-bit label is (1/2,1/2).
     - But it is NOT derived: WHY maximum entropy is taken over the
       BLOCK label (giving 2/3) rather than over the GENERATION/state
       label (giving uniform p, Q=1/3) or via the canonical
       dimension-weighted trace (Q=1) is the open step.
     - The three options are mutually exclusive and give the three
       special values; nothing yet proven forces the middle one beyond
       the (independent, exact) range-midpoint coincidence at d=3.

## Adversarial probes run
- **Probe: does the canonical trace give 2/3?** No -> Q=1. (kills K1)
- **Probe: does purity alone give 2/3?** No, 1-param family. (kills K2)
- **Probe: does rho_ref give 2/3?** No -> Q=1/3. (kills K3)
- **Probe: is d=3 a degenerate/accidental coincidence?** No -> transversal
  simple zero, slope 1/6; isolated.
- **Probe: is the democratic direction an input?** No -> forced as the
  unique Z_3-fixed eigenvector of the color automorphism.

## Net assessment
The hardening is a genuine advance even though it does NOT fully close
the gap:
- It converts 3 previously-vague steps into EXACT statements (the map,
  the Kahler structure, the three-weighting/three-value correspondence,
  the B(d) count, transversality).
- It KILLS two attractive-but-wrong routes (canonical central trace;
  pure-state forcing), preventing false closure.
- It localizes the entire residual content to ONE crisp question:
  *why equal weight over the FS block label?* with two independent
  exact anchors (equipartition value 2/d AND range-midpoint
  (1+d)/2d) that coincide only and transversally at d=3.

Honest status: **bounded** -- the forcing principle A1* is named, not
derived. No claim of full closure.

## Status
AUDITED -- one residual assumption (A1*), two routes killed, remainder
exact.
