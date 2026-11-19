lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-20T09:12Z

# gap-mini-free-fable: (W) by a free method, starting from the Jaffe-Witten target

Row 1181 of `FINISH.md`. Started 2026-11-19T21:12Z at commit 6a3a26b93. Research-stage working
state. It grants no status. Nothing here is a public claim. Every statement below carries one
of the labels PROVED, ARGUED, GUIDE, OPEN.

## Plan (written before any lane file was opened)

1. Read the statement of (W) only (row 720) and the Jaffe-Witten target as `GOAL.md` states
   it. Keep the lane files (`library/gap-solve*`, the council files, `parts/gap.md`) closed.
2. Write the target from the Jaffe-Witten side: what a mass gap is, which equivalent forms
   exist, and which inputs are specific to four dimensions and to a nonabelian group.
3. Choose routes that do not pass through the lane's reformulations. Attack one route per
   step. Each step ends with: statement, argument, the first step that fails, what is left.
4. Open the lane files and compare: `library/gap-council-synthesis.md`, `parts/gap.md`
   (methods 1-36 and the route registry), RESULT lines of rows 1143-1177. Mark each of my
   statements as new, known, or refuted there. Before attacking any open lemma, grep
   `library/open-core.md` and the FINISH rows for it.
5. Close: a proof, a disproof, or one precise obstruction statement per route tried. End
   with one RESULT line.

Rules in force: no computer-assisted step in a proof; a numeric run may only guide or refute;
credit Balaban, Sussman and Alpoge, Chatterjee and every other source by name; no
home-directory path in this file.

## Log

(steps are appended below, one per response)

### Step 1 (21:12Z to 21:40Z). The statement, and the target seen from the Jaffe-Witten side

**Read so far (statements only).** `GOAL.md`; `FINISH.md` L1-84, L299-356, rows 720 and
1174-1181; `parts/gap.md` L1-60 (the wording of (W)); `library/gap-phys-seed.md` L270-338
(definitions of S, D, Phi, z^-, D^+, Theorem ZD-c). No `gap-solve*` file, no council file and
no method list is open yet.

**(W), as on record (`parts/gap.md` L21-23).** Wilson SU(2) on four-dimensional tori, along
the trajectory (a_j, beta_j) of the account of Sussman and Alpoge after Balaban. P is a
dyadic set of physical sizes. D^+(L) is the upper limit of the Casimir free energy of the
symmetric torus of side L. z^-(L) is the lower limit of (side) x (gap of the transfer
operator of the periodic cube of side L). (W): there are (L_0, D_0) with D^+ <= D_0 from L_0
on, and one L >= 4 L_0 in P with z^-(L) > 256 D_0 + 30. By Theorem ZD-c of row 720, (W) is
equivalent to (PHYS-SEED), and Theorem S carries a seed to a gap on every larger cube.

**The Jaffe-Witten target.** A quantum Yang-Mills theory on R^4 for SU(2) with a Hamiltonian
H >= 0, a unique vacuum, and spectrum of H in {0} united with [Delta, infinity), Delta > 0.
In Euclidean form: exponential clustering of gauge-invariant local fields at a rate that is
positive in physical units. (W) is this statement at one finite physical volume of about 40
correlation lengths (GUIDE in row 720), together with flux energies that are not of order
1/L. So (W) is not a weak-coupling statement, and no small-volume expansion reaches it.

**What a proof must use (my own list, before any lane file).**

- U(1) in four dimensions at weak coupling has a massless photon (Guth; Froehlich and
  Spencer). A proof of (W) must use an input that is false for U(1).
- I know four inputs of this kind. (i) Asymptotic freedom: the sign of the one-loop
  coefficient, proportional to the adjoint Casimir. (ii) The Ricci curvature of the group
  manifold: positive for SU(2), zero for U(1); this is the same number as (i) in another
  role (Friedan's flow for sigma models; Singer's remarks on the orbit space). (iii) Twist
  eaters: SU(2) has flat connections with non-trivial 't Hooft flux (holonomies i sigma_1,
  i sigma_2), so a centre twist has zero classical cost; a U(1) flux has classical cost
  beta (2 pi)^2 / 2 times an aspect ratio. (iv) The dimension count N > 2 of the new
  two-dimensional proofs (below): SU(2) = S^3 has N = 4.

**Published work fetched (public, into a scratch folder; credited).** Jian Ding, Fenglin
Huang and Peng Yang, "Exponential decay for the two-dimensional Heisenberg model",
arXiv:2611.04908v1 (3 Nov 2026), 74 pages: exponential decay for the O(N) spin model on Z^2
for every real N > 2 and every beta. Their Remark 1.5 and Section 1 describe two mechanisms:
theirs (loop soup of intensity N/2 with fixed local time, Lupu's isomorphism, projection to
an XY model with random couplings, a Gaussian tail for the number of macroscopic loops, an
improved spin-wave argument on a "defective" region, then a coarse-graining step), and
OpenAI's of 6 Oct 2026 (non-commutativity of rotations of S^2 and a constructed family of
spin waves on S^2). Both are unchecked here. Both reach a finite-size criterion at a scale
exp(C beta) by a multi-scale argument that starts at the lattice scale and needs no control
of effective actions. That is the shape (W) needs, with one difference that matters:

**Remark 1.1 (ARGUED; rate versus trajectory).** A lattice result "gap at every fixed beta
with correlation length at most exp(C beta)" gives (W) only if C equals the exact exponent
1/(2 b_0) of the trajectory, with the right power of beta in front, or if it is applied to
the effective theory at the first-passage scale, uniformly over the effective actions that
the account produces there. With a constant C that is not sharp, the gap in physical units
tends to zero along the trajectory. So a port of a two-dimensional mechanism has two parts:
the mechanism at one cutoff, and its robustness under the block maps of the account.

**Routes I consider outside the reformulations (to be tested against the lane's list at the
compare step).**

- F1. Curvature route in Hamiltonian form: the Kogut-Susskind operator as a Dirichlet form
  on a product of 3-spheres, Bakry-Emery with Ric > 0, and what replaces log-concavity of
  the ground state.
- F2. Conditional sigma-model structure (Durhuus and Froehlich 1980): given the spatial
  links, the temporal links of one layer are an O(4) model in three dimensions in an SO(4)
  background. Random-walk form with holonomy weights (Kassel and Levy, covariant Symanzik
  identities). Question: does a mechanism of the Ding-Huang-Yang type survive holonomy
  signs?
- F3. Non-abelian spin waves for the twist: field-dependent, measure-preserving colour
  rotations, with the cost governed by a stiffness that non-commutativity reduces.

Nothing is proved in this step.
