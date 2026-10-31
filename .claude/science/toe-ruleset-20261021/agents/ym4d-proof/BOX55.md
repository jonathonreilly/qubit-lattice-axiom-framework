Reviewer model: claude-opus-5-5

# BOX55 — BFT on boxes: the linear package with a boundary (ASSEMBLY ML11 leaf (BOX))

Worker: Opus 5.5 (claude-opus-5-5). Started 2026-10-29T06:41:29Z (UTC). Append-only.

## 0. PRE-STATED (written before any derivation)

Targets (from the brief, queue/box.md):
- T1. Fix ONE boundary convention: the one N5-sf0 (PROOF.md, located by string) actually uses — frozen
  exterior field; Dirichlet vs free for the fluctuation; how the soft kernel and the S4' averaging are
  truncated at the box boundary. State it once, with file + locating string for every ingredient.
- T2. Prove the box analogue of the trivial-background linear estimate (LINEAR_PACKAGE Thm 4.2 / GF-E /
  CC-INV) in that convention, with constants uniform in box size L_box, box position, scale k and T;
  route: banked torus estimates + boundary parametrix with exponentially decaying error (soft-constraint
  mass), or directly. Exact rational arithmetic for any constant.
- T3. Lift: BFT-0/1/2 on boxes as implications with every input named (interior by locality from the
  torus results; boundary layer from T2).

What would count as a refutation / negative result (each is a first-class outcome):
- R1. A boundary mode the convention cannot control: a family of admissible boxes / fluctuations on which
  the box quadratic form's lowest eigenvalue (in the gauge-fixed or soft-constrained sector the consumer
  uses) tends to 0 (or becomes negative) as L_box or k grows — i.e. no box-uniform coercivity.
- R2. A parametrix whose boundary error does NOT decay exponentially in distance (e.g. a massless/zero-
  mode sector of the soft kernel at the boundary, a gauge direction not damped by the soft constraint
  once truncated), making the constant non-uniform in L_box.
- R3. The N5-sf0 convention turns out not to be well-defined (e.g. the S4' average or the soft kernel
  cannot be truncated without breaking a symmetry the consumer uses), or different consumers need
  incompatible conventions — then T1 reports the incompatibility instead of choosing.
- R4. Any numeric constant I quote failing its pre-registered exact check.
Discipline: every consumer statement and every banked input is cited by file + locating string; symbol
collisions (C_1, c_1, epsilon_1, kappa, theta_0, M, ...) are resolved by file:line before any comparison.
