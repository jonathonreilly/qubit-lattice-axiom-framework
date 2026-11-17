# Council brief: where the 4D SU(2) mass-gap proof is stuck (rows 1128-1134)

Written by the lead (Claude Opus 5.5) on 2026-11-17, owner request: "Pull together a council of agents (max best
Astra and fable) with different diverse backgrounds in physics and math, show them where we are stuck, ask them how
to attack it." Sources are named for each statement. A statement marked PROVED is proved in this lane and checked
once, unless the line says otherwise. Nothing here is a mass-gap claim.

## 1. The target

Jaffe-Witten, for the gauge group SU(2): construct a quantum Yang-Mills theory on R^4 that satisfies the
Osterwalder-Schrader axioms, with a mass gap: the spectrum of the Hamiltonian is {0} together with a set contained
in [Delta, infinity) for some Delta > 0.

The lattice form used here. Wilson SU(2) on periodic 4D tori: action A(U) = sum over plaquettes p of
(1 - (1/2) tr U_p), weight exp(-beta A(U)) with Haar measure on the links. The couplings beta_j follow an
asymptotically free trajectory with spacings a_j tending to 0. Ultraviolet control comes from Balaban's
renormalization group, as written up in full by Sussman and Alpoge (here: "the account"). Credit Balaban for every
use of it. The account controls the small scales. It does not give a gap: it stops at the scale where the
effective coupling becomes of order one ("first passage").

## 2. What is proved (the consumer side is done)

- Transfer operators (TM), (TM-c): for every box there is a positive trace-class transfer operator T, and the
  centre flips split the space of a periodic cube into eight flux sectors (`library/gap-crux-restate.md` Section 1).
- Theorem S and Theorem SH (rows 697-699, 705; `library/gap-crux-restate.md` 3.4): one seed at one box size gives a
  uniform gap on all dyadic boxes above it. The key fact is Lemma K: the ground-state deficit is non-negative,
  convex and non-increasing in the size.
- Theorem ZD-c (row 720, `library/gap-phys-seed.md` L311-336): along the trajectory, the seed at one physical size
  (PHYS-SEED) is equivalent to two statements with no small number in them:
  - (BDD-Delta): the excess (Casimir) free energy D of the symmetric torus stays bounded at large physical sizes;
  - (Z-UNB): z^-(L), the lowest gap of the periodic cube of physical side L in units of 1/L, flux sectors
    included, is unbounded along the dyadic sizes.
- Hence the wall (W): there are L_0, D_0 with D^+(L) at most D_0 for every dyadic L at least L_0, and one size
  L at least 4 L_0 with z^-(L) larger than 256 D_0 + 30. An equivalent one-size form is (Z-SEED):
  L m(L^3) larger than 2 Phi_4(L/4) + 30, where Phi_4(n) = 16 F(n^4) - F((2n)^4) is the doubling defect and
  F = log Z. GUIDE (numerics, not proof): (Z-SEED) holds from about 40 correlation lengths.
- (W) also follows from (CAS): the doubling defect contracts by a factor theta below 1 per doubling over a bounded
  range of sizes, from an extensive base (row 708).
- Everything downstream of a seed is done: the gap at all larger sizes, the carry to finer cutoffs, and the
  clustering at a physical rate.

## 3. Where it is stuck

In plain words (row 998 9.1): on each doubling of the box, between the last small box (first passage, where the
account stops) and the first good box (the seed size), one free energy must shrink by a fixed factor. In a model
with a massless particle it never gets small.

So the missing piece is one **selective** inequality at order-one effective coupling, at every scale between first
passage and the seed size. "Selective" means: it must be false for every model in Section 4. The Wilson window
where the effective coupling is of order one is about beta 2.3 to 2.6.

The two kinds of input that could supply it (row 998 6b):

- (K-one): a property of the measure at one scale in the band, with a number in it.
- (K-flow): a statement that starts from the account's first-passage data and is carried through the band by a
  step that fails for U(1), for frozen groups and for products with a massless factor.

Every known tool works only at very strong coupling or at very weak coupling:

- Strong coupling, by hand: 4D SU(2) gap and clustering for beta_W below about 1/3 (Bhattacharjee et al. v6; to
  0.351 only with interval arithmetic, which is not allowed here); slab area laws for beta below 1/24
  (Cao-Nissim-Sheffield) or 1/48 (Shen-Zhu-Zhu); a uniform Langevin gap for beta below 2/9 (lane row 815,
  normalization to be compared). The families of majorants behind such bounds stop at the ceilings
  1/3, 2/3, 0.775 and 1.0109 (checks 840, 841, 849, 857).
- Weak coupling: the account (Balaban's RG), up to first passage only.
- The band between them (Wilson beta from about 1/3 to about 2.3, effective coupling of order one) holds the
  whole difficulty.

## 4. The comparison models (a valid attack must fail at a named line for each)

- Compact U(1) at weak coupling: massless photon, (Z-UNB) fails, (BDD-Delta) holds. Theorem-grade at large beta
  (Guth; Frohlich-Spencer; Villain in the lane at beta at least 2^14, row 786).
- The free photon: the periodic-box quantity has a massless floor (17.04, row 988).
- A product of SU(2) with a massless factor (row 708): any step that reads only one factor of the state space fails.
- Frozen finite subgroups: Z_2 above beta 2.191 (Peierls); Q_8 near beta 1.15 and the binary tetrahedral group near
  2.15 (transition couplings are numerics, GUIDE). So a tool at the crossover must see SU(2) representations of
  spin 2 or 3, not only the low ones (row 838).
- Positive-character weights at their first-order coupling (van Enter-Shlosman; lane Proposition V): a pure
  one-scale number without first-passage data is refuted there.

## 5. What has failed, by kind (do not propose these again without a changed mechanism)

Details: `parts/gap.md` (route registry, test table, "Methods set aside" 1-34) and the FINISH RESULT lines.

- One-scale numbers with no consumer (route RC, row 996); suprema over tilts (Theorem D2, row 977); hypotheses
  uniform over plaquette coupling fields (Lemma SHEET, row 996).
- Contraction or sign statements proved by class-wide tools (routes RA, RB): their terminal obligation is the target.
- Functional inequalities (log-Sobolev, curvature, Polchinski flow, Piazza-Shen) from small-field convexity (route
  RF, rows 957-988): stronger than the target, no supplier in the band.
- Hierarchical (Migdal-Kadanoff type) comparison: group-blind (route RG, retired).
- Gauge-invariant block criteria (Knabe, Gosset-Mozgunov, Martinelli-Olivieri type): fail at the block corners for
  every product-box cover at beta from 1/16 to 64 (rows 763, 769, 777).
- Criteria in the law of the model for pinned cells: one-sample means need a uniqueness clause; two-sample means
  with a small constant are one-scale mixing in disguise; independent-replica swaps are false at the window (rows
  845, 852, 895, 896, 1115-1123).
- An anisotropic bridge from the beta_L = infinity face to the isotropic window (BR-2): blocked at (SING) (row 1115).
- Ten ideas from probability, optimal transport and entropy (row 1031): all fail the kill tests.

## 6. The nearest working example

In two dimensions the analogue of the stuck step has posted, unrefereed proofs (lane rows 1006-1010; reading only):

- OpenAI (github.com/openai/math, 2026-10): the 2D O(3) and O(4) models have a mass gap at every coupling. A mixing
  bound at one fixed bare coupling comes from a pinned-cell stiffness iteration, uniform over all boundary pins and
  strengths. Its gain is the commutator ("bracket") term of the target group, which is zero for the abelian model.
  The RG only carries the bound across cutoffs. No first-passage data are used.
- Ding-Huang-Yang (arXiv:2611.04908): the 2D O(N) gap for N at least 3, with a loop-soup argument.

The lane's attempt to port the pinned-cell step to 4D (row 1018, form (T-pin)) stopped at clause (L3): the step
from a response bound in the law of the model to mixing of all observables. (L3) is OPEN for Wilson SU(2) (check
1123). No gauge-theory stiffness or Schrodinger-functional bound at order-one coupling exists in the literature
(row 1012).

## 7. Rules for every council member

- No computer-assisted step in a proof: every step must be checkable by hand and formalizable in Lean. A numeric run
  may guide or refute, never prove. Stop any run above 2 GB of memory.
- Build on published work; credit the authors. A citation is not a proof step until its hypotheses are checked.
- Mark every statement PROVED, ARGUED, GUIDE or OPEN.
- Do not claim a mass gap.
