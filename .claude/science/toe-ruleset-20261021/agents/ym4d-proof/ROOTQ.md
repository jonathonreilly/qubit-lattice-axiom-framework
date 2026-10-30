# ROOTQ — the level-k root charges (target T55-T)

Owner: worker T55-T. Writes only this file and `checks/rq1_*`.

---

## §0. PRE-STATED (first edit; statements only)

**This is the first edit to this file.** UTC time of writing: **2026-10-28T22:04:45Z**.

Nothing below in this section cites any derivation produced in session 25. It states the targets only.
Where a session-25 file is named it is named as a *claim to be tested*, never as an input.

### §0.1 What I am going to pin

**(P1) The object.** State precisely, from `BFT_A.md` / `BFT_B.md` only:
  - what the **level-k roots** `c_X` are (the set, its index `X`, its cardinality as a function of
    k, L, and the torus side T);
  - what **`D`** is (the operator whose value at the roots is being charged) and what **`S`** is;
  - what the **root charges** `Q_X := D(S)(c_X)` are — scalar, Lie-algebra-valued, or vector-valued —
    and what structure (gauge covariance, lattice symmetry, reality) they carry;
  - the **exact form** of (TENT-Q) / (ROOT-sup), with quantifiers, as the consumer states it.

**(P2) The weak form.** State the **dipole-neutrality-against-a-(1+R)^{−2}-profile** claim precisely
as an inequality/identity in the `Q_X`, and then **verify against BFT_A/BFT_B that this is what the
consumer actually consumes.** The claim that it is, is `GESIGN.md`'s (R4), made today and unreviewed;
I treat it as a hypothesis to be confirmed or refuted at the consumer site, not as given.

**(P3) (FP♯′).** Determine whether the "one scalar per level-k box, already of total zero" item is
itself a neutrality statement, implies one, or is a different object. Decide by file:line.

**(P4) The standing caution — the decisive item.** Session 24 recorded **(NEUT-box) as REFUTED,
"false by a clean power."** Locate that refutation and read it before investing in any neutrality
argument. Then decide, and state as the headline:

  > **Does the session-24 (NEUT-box) refutation reach the weaker dipole form, or does the weaker
  > form survive it?**

  If it survives: name **exactly which power the refutation turns on** and **why the dipole form
  escapes that power**. If it does not survive: **(R4) is dead**, and say so without hedging.

**(P5) The strong form.** `n³ · max_X |D(S)(c_X)| ≤ C(class norms)`, k-, T-, basepoint-uniform.
True or false. Includes: are the two routes to the blow-up (`L^{3k−3}` coarse-size route vs the
sharper `L^{2k−3}` route) two routes or one route in disguise?

**(P6) The double count.** Check whether `BFT_A §38.6` and `BFT_B §35.7` quantify over different
source classes, and whether any live figure in this neighbourhood combines them. If one does, name it.

### §0.2 Pre-registered failure modes (named before any work)

- **RQ-F1.** The level-k root charges are **not** finite-dimensional in the sense assumed — e.g. the
  index set X grows with T as well as k, or `Q_X` is a field on the box rather than one number per
  box. Then "exhaustive enumeration at small k settles it" is false and the framing collapses.
- **RQ-F2.** The consumer does **not** consume dipole neutrality. It consumes the sup bound, or a
  weighted sum with a profile other than `(1+R)^{−2}`, or neutrality against a class of profiles.
  Then (R4) is a statement about the wrong pairing.
- **RQ-F3.** The session-24 (NEUT-box) refutation's power is **in the profile-weighted sum too** —
  i.e. the counterexample that kills monopole neutrality also kills the dipole form. **(R4) dead.**
- **RQ-F4.** (FP♯′)'s "total zero" is zero of a **different** sum (e.g. over a single level-k block,
  or of a gauge-fixing multiplier) and has no edge to `Q_X`.
- **RQ-F5.** The two blow-up routes are the same route; the apparent independence is a double count
  of the kind flagged at `BFT_A §38.6` / `BFT_B §35.7`, so "two independent routes" is one route and
  the exponent figure quoted for it is wrong.
- **RQ-F6.** `Q_X`, `D`, `S`, `c_X`, `n` are each more than one object in this lane (the session-25
  symbol-collision defect). Any comparison I make across files is then void unless pinned by
  file:line. I will pin every one of them.

### §0.3 Pre-registered standard of proof

- **PROVEN** only if the complete argument is written out in this file from hypotheses stated here.
- Any numeric gate gets a **designed-FAIL control**, pre-registered in `checks/rq1_*_criteria.md`
  before the script exists, and the control's firing is **reported**.
- The object is finite-dimensional, so **exhaustive enumeration at small k is admissible as proof of
  a universally quantified statement only over the enumerated range**; any extrapolation is ARGUED
  and labelled, and I will say what it does and does not generalise.

### §0.4 What I expect to be wrong

Session 25 has refuted two of its own headlines inside a day. The prior most likely to break here is
**(P2)**: that the consumer consumes dipole neutrality. It is the newest claim, it is the one that
makes the target cheap, and nobody has read it but its author.

---


---
**[LEAD, 2026-10-28T22:11:08Z] ABANDONED DRAFT.** This worker was stopped mid-run. Nothing in this file is a result.
