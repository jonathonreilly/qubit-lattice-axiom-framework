# THETAW.md — the exponents of 𝔐 and BFT, decoupled (target T55-J)

*Owner: the T55-J worker, session 25. Writes only this file and `checks/tw1_*`. Every change this file
wants in another lane file is in `## FOR OTHER FILES (not edited)` at the end, for the lead to land.*

---

## §T0 PRE-STATED (first edit of this file, 2026-10-28T21:39:13Z; STATEMENTS ONLY)

**This is the first edit of THETAW.md.** It contains statements only: no derivation, no grep, no
classification, no arithmetic and no check of mine precedes it. It cites nothing produced in session 25.

### §T0.1 The object

`REVIEW_S22.md` l.389-432 states the background-field theorem (BFT), clauses 0-5, with the norm 𝔐
defined at l.392-397. The norm's scale weights, and BFT-1's decay rate, are written with the single
letter **θ_w**, quantified once at l.399 as *"there exist … θ_w ∈ (0, 2]"*. `NORMS.md` §N7 (session 24)
records that the composite contraction needs **three** exponents — θ_w^c (curvature), θ_w^r (residual),
θ_A (potential) — with θ_A = min(1, θ_w^c − 1) and A = L^{d − θ_w^r − 2θ_A}; and `PROOF.md` l.30-34
([S24-fix 3]) records that a single common θ_w has no solution in (0, 2]. Separately,
`RTARGET.md` §33 l.587-588, `SF.md` l.680 and `BFT_A.md` l.36 all use the letter **θ** for the *source*
weight ω_l = L^{θ(k−l)}, with their own stated windows.

### §T0.2 Pre-registered targets

- **TW-1 (inventory).** Enumerate every distinct job an exponent does in 𝔐 and in BFT-0…BFT-5, one
  symbol per job, preferring symbols already in use in the lane. State for each clause which jobs it
  inherits.
- **TW-2 (consumed windows).** For each job, derive the window its consumer's **proof** requires, not
  the window its **statement** announces, and record for each whether consumed ⊊ stated, consumed ⊋
  stated, or equal. A window read off a statement is to be recorded as unverified.
- **TW-3 (satisfiability).** Decide whether the decoupled system is satisfiable. If yes, exhibit the
  feasible region explicitly. If no, prove it empty and identify the minimal set of clauses whose
  windows must move, and by how much.
- **TW-4 (restatement).** Write append-ready replacement text for REVIEW_S22 l.389-432's clause
  statement with every exponent decoupled and quantified over its own window, saying what BFT-1's
  existential must become.
- **TW-5 (d = 4).** Determine whether the feasible region is empty only at d = 4 or at every d, and
  say which of the two it is.

### §T0.3 Named failure modes (pre-stated, so a failure is recorded as a failure)

- **TW-F1** The decoupling is vacuous — i.e. the four windows were always windows on the same job, so
  separating the letters changes nothing and the system stays empty. Then TW-3's answer is EMPTY and
  the repair is an estimate, not a restatement.
- **TW-F2** The decoupling *is* real but introduces a coupling I did not find, so a region I report as
  feasible is not. Guard: for every pair of jobs I must state explicitly which lemma couples them, or
  state that I searched and found none.
- **TW-F3** I report a window from a clause's **statement** rather than from its proof, and so inherit
  the very defect the target has. Guard: every window row carries the file:line of the step that
  consumes it.
- **TW-F4** A job exists that I do not enumerate (in particular: a clause of 𝔐 or of BFT-0/2/3/4 that
  carries a scale exponent I have not named), so a "feasible" verdict is feasibility of a sub-system.
  Guard: enumerate from the text of l.392-423 line by line, and from the consumers listed at l.425-431.
- **TW-F5** The symbol θ, or θ_w, means something different in one of the files I combine, and I combine
  two different objects. Guard: quote file:line at every comparison (session-25 brief, defect 1).

### §T0.4 What would count as a FAIL of my own gate

Any numeric gate I run is exact rational arithmetic over the exponent inequalities. It must come with a
designed-FAIL control — an input for which the gate must return INFEASIBLE — and I must report that the
control fired. A gate that returns FEASIBLE for every input it is given is not evidence. Two controls
are pre-registered here, before any script: **(i)** the single-common-θ_w system of PROOF l.30-34 must
come back EMPTY (if it does not, my encoding of NORMS §N7 is wrong and nothing else in this file counts);
**(ii)** the decoupled system must come back EMPTY in some dimension d, since if it is feasible in every
d the exponent count has lost the dimensional content it is supposed to carry.

### §T0.5 Scope limits stated in advance

- I decide **windows and satisfiability**, not the open estimates themselves. Nothing here proves
  (G♯_0-field), (GAP-Z), (CO-fun), (G♯-rough) or (SPD).
- A feasible region is a statement about *parameters*, not about *status*: a clause can have an
  admissible exponent and still be OPEN. I will not let a feasibility verdict read as progress on a
  proof.
- I do not edit `SYMBOLS.md`; where a rename is implied I list it for that file's owner.
