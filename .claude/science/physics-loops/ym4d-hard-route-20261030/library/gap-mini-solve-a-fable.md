lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-20T10:59Z

# gap-mini-solve-a-fable (queue row 1188): the mass gap of 4D SU(2) Yang-Mills, attack on the crux

Pinned at commit f7e5907e5 of `claude/ym4d-hard-route`. Worker: Claude Fable 5.2 (max), Mac mini worker 1.
Started 2026-11-19T22:59Z (`date -u`). Research-stage working state; nothing here grants status.

Labels: PROVED (every step written here, not yet checked by another model), ARGUED (argument with a named
gap), GUIDE (numeric or heuristic, never a proof step), OPEN.

## 0. Status log (one line per step, newest last)

- 22:59Z file created; reading FINISH.md rule sections, GOAL.md, `parts/gap.md` and the latest RESULT lines.
- (time typed by hand, not from `date -u`; the true time was about 23:03Z) read FINISH rule sections (L52-73, L299-350), GOAL.md, `parts/gap.md` L1-104, `library/gap-council-synthesis.md`, the RESULT lines of rows 1178-1187. Next: RESULT lines of rows 1135-1177, then the attack plan (Section 1).
- 23:28Z (`date -u`) read: RESULT lines of rows 1135-1177; `prior/gap-2don-proofs-read-opus.md` L44-170 (the two posted 2D proofs); `gap-crux-restate.md` L20-60; `gap-solve9-astra62.md` L95-150 (the neutral bound and its consumer). Section 1 written below. No attack chosen yet.

## 1. How best to attack it (analysis before any attack)

### 1.1 The target as the lane holds it (cited, not re-proved)

- The lane reduces the Jaffe-Witten gap clause to one lattice estimate plus the continuum datum. The lattice
  estimate is the one-cube physical neutral bound (N-phys): on the periodic spatial cube n_j^3 of one admissible
  physical side, the vacuum-normalized neutral excited trace s_j(floor(n_j/K); n_j) is at most 1/2, uniformly in the
  cutoff j (`gap-solve9-astra62.md`, "One finite aspect" and "consumer", L146-148; row 1161, checked in row 1162).
  The consumer is Theorem BP of row 1179 (`gap-mini-branch-fable.md`), which HOLDS AFTER CORRECTION in the
  cross-provider check 1183 (`gap-neutral-chain-check-astra.md`).
- The continuum datum ((P1)-(P4), (H2), (TOT) on the intended Hilbert space) is the T0 chain. FINISH "Where it
  stands" records: existence is not proved. I do not touch it in this row.
- The Wilson branch selection (BS) is on the path of (W) (confinement on tori), not of the gap clause (row 1179).
- (N-phys) is the glue half (GLUE-FP) of rows 895 and 920 with other constants (row 1184). In one sentence: a gap
  and a level count for centre-neutral states at one physical box, at arbitrarily weak bare coupling.
- The fixed-coupling form: the seed Phi(n) = 16 F(n^4) - F((2n)^4) <= 1.9e-4 at some n (`gap-crux-restate.md`
  L57-60, Theorems D and S). GUIDE (my arithmetic from Teper's table quoted in my memory of row 974: a m = 1.216,
  a^2 sigma = 0.136 at beta 2.3): the flux term 6 n^2 exp(-sigma n^2) passes 1e-5 at n = 12 and the glue term
  n^3 exp(-m n) at n about 18. So the seed at beta 2.3 is a statement about log Z on 18^4 and 36^4 to an absolute
  accuracy of 1e-4. No convergent expansion with absolute weights reaches beta 2.3 (method 35).

### 1.2 What a proof has to contain

ARGUED (nothing here is new; each line names its place on file).

1. The band has no small parameter. Between the last scale where the effective coupling is small and the first
   scale where the seed holds, no expansion converges, and the owner rule excludes a computed finite-box criterion.
   So the crossing must be a structural inequality that holds at every coupling. (`parts/gap.md` L41-50.)
2. Symmetry does not force disorder in four dimensions. A continuous one-form symmetry can break in d = 4 (the
   Coulomb phase of compact U(1)), and SU(2) has only the Z_2 centre as a one-form symmetry. So there is no
   Mermin-Wagner argument; the gap is dynamical. The comparison cases of lead rule W2 say the same.
3. The only band-crossing mechanism on record is the pair of posted 2D O(N) proofs (rows 1006-1011). My reading of
   the OpenAI skeleton (from `prior/gap-2don-proofs-read-opus.md` B(2), not from the paper): the twist between two
   pinned layers is produced by commutators of single-axis spin waves at each of log N scales. The amplitudes add,
   lambda about log N. The costs add as squares of Dirichlet energies, also about log N, by orthogonality. So the
   stiffness is at most K/log N. Two facts make it work: (a) a response functional W with exact invariance under a
   non-abelian group of changes of variables; (b) Ward bounds for that group whose cost form is scale invariant.
4. In 4D gauge theory (a) exists and (b) fails. The exact analogue of W is the Schrodinger functional as a function
   of a pinned boundary field C. It is invariant under the gauge group of the boundary slice, by Haar invariance of
   the time-like links that leave the slice. Its Ward bound is the exact contact identity for smeared Gauss-law
   generators, <X(df a)^2> = <Y> <= beta |df|_2^2. But the gauge functions live on a 3D slice and their Dirichlet
   energy is not scale invariant. Count for a holonomy twist h of size 1/N per link: with plane waves of weight c_p,
   lambda/N = sum c_p^2 k_p and cost = sum c_p^4 k_p^4 N^6, so by Cauchy-Schwarz lambda^2/cost <= N^(-4) sum_k
   k^(-2), which is about 1/N. The fourth-order inequality then gives a bound of order K N, the order of the bound
   with no commutator. This is the lane's slot (ii) and R6 of row 1013 (`gap-invent-selective-max.md` L83, L91) and
   row 1016 (`gap-global-reform-max.md` L359, L429, L545): "scale invariant in two dimensions and not in four".
   My count is a second derivation by the same model family, not a check.
5. The scale-invariant cost form in 4D is the covariant curl form of a one-form. For a move in a fixed colour
   direction it turns into a mass form, because every adjoint direction is rough at the lattice scale (row 1141 (2);
   row 1181 Lemma 5.1a; Proposition J). The exact stiffness is R = <Hess S(a,a)> - Var X(a) for any extension a of
   the boundary twist. Both terms are of order N^2 in lattice units and their difference is of order beta_eff. A
   Jensen bound drops the variance, so it can never see the cancellation (rows 1011, 1016).
6. The other continuous twists in reach are spacetime twists (shifted or rotated identifications). Their Ward
   bounds are stress-tensor contact terms with power divergences. Discrete twists (shifts, the cubic group, the
   centre) isolate every sector except the vacuum sector, and (N-phys) is the statement about the vacuum sector.
7. Thin twisted compactification (Route T, row 842, (AC')), ground-state curvature (rows 957, 968), abelian
   conditional structures (below) and the dichotomy with an emergent massless vector (row 1017, Theorem CR) are on
   file with their first failing steps.

One small item I did not find on file (grep "Hopf", "Ginibre", "abelian projection" in `library/`; hits are about
frames, U(1) and the O(N) proofs). PROVED by direct expansion, unchecked, and negative:

**Lemma HF (the maximal-torus amplitude decomposition is frustrated).** Write a link as U = [[a, b], [-b*, a*]]
with a = cos(phi) e^(i alpha), b = sin(phi) e^(i gamma), phi in [0, pi/2]. For a plaquette U_1 U_2 U_3^* U_4^*,

(1/2) tr = c1 c2 c3 c4 cos(m_0) - s1 s2 c3 c4 cos(m_12) + s1 c2 s3 c4 cos(m_13) + s1 c2 c3 s4 cos(m_14)
 + c1 s2 s3 c4 cos(m_23) + c1 s2 c3 s4 cos(m_24) - c1 c2 s3 s4 cos(m_34) + s1 s2 s3 s4 cos(m_1234),

with c_i = cos(phi_i), s_i = sin(phi_i) and the angle forms m_0 = alpha_1 + alpha_2 - alpha_3 - alpha_4,
m_12 = gamma_1 - gamma_2 - alpha_3 - alpha_4, m_13 = gamma_1 - alpha_2 - gamma_3 - alpha_4,
m_14 = gamma_1 - alpha_2 + alpha_3 - gamma_4, m_23 = alpha_1 + gamma_2 - gamma_3 - alpha_4,
m_24 = alpha_1 + gamma_2 + alpha_3 - gamma_4, m_34 = alpha_1 + alpha_2 + gamma_3 - gamma_4,
m_1234 = gamma_1 - gamma_2 + gamma_3 - gamma_4. Since m_12 = m_0 + m_13 - m_23 as linear forms, and the
coefficients of cos(m_0), cos(m_13), cos(m_23) are non-negative while that of cos(m_12) is non-positive, no shift
of the angles (alpha_l -> alpha_l + eta_l, gamma_l -> gamma_l + delta_l) makes all eight coefficients non-negative
on one plaquette. So, given the amplitudes phi, the abelian model in the angles is not of Ginibre type in any
shifted angle variables, already on a single plaquette.

Proof. The eight terms are the eight even flip patterns of the index path 1 -> . -> . -> . -> 1 through the four
matrices, with entries (U)_11 = a, (U)_12 = b, (U)_21 = -b*, (U)_22 = a* and (U^*)_11 = a*, (U^*)_12 = -b,
(U^*)_21 = b*, (U^*)_22 = a; the path that starts at index 2 gives the complex conjugate. The two minus signs come
from b_1 (-b_2^*) and (-b_3) b_4^*. A shift changes the argument of each cosine by a constant; all coefficients
become non-negative only if the shift is 0 mod 2 pi on m_0, m_13, m_23 and pi on m_12, which contradicts
m_12 = m_0 + m_13 - m_23. QED.

Use: it closes the "amplitude decomposition with abelian conditional systems and association" cell of the reading
table (`prior/gap-2don-proofs-read-opus.md` B(5), marked NONE there) for the Hopf coordinates. It does not exclude
other coordinates. It is consistent with method 35 (the signs are in the model, not in the expansion).

### 1.3 Decision

Every structural route I can name is on the lane's map with a first failing step. I therefore do not open a new
framing. The next sections take one open point and work it to a proof or to a first failing step. The choice and
its reason are in Section 2.
