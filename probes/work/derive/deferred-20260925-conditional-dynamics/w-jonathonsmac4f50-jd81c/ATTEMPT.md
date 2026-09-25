# Deferred science, unit 18 (PR #9041): an autonomous history that fixes the isolated site's λ by formation time — attempt a1

Worker `w-jonathonsmac4f50-jd81c`, model `claude-opus-5-5`. PR #9041 (dynamics clause h2) and PR #9142 were written by Claude sessions, the same model family. The referee should be of another family.

**Inspection before work.**
- `origin/main` is `25b8c1874f2ea657653dbb298bf383c18d81e0b5`.
- PR #9041's three bundled sources verify against their SHA256. Its accepted paths on main match.
- The landed note `docs/DYNAMICS_CLAUSE_RECORDS_ACT_AS_FIELDS_..._2026-09-24.md` gives:
  - T1: records act as fields;
  - T2: an isolated site is a qubit in `h(N) = Σ M_f q_f`;
  - T3: *if* the odds depend on the records alone, they are read from a stationary state on the line `(1 + λ ĥ·s)/2`, with `λ` "the relaxation profile", not derived.
- The landed PR #9142 note (`RECORD_FORMATION_CLOCK_IN_THE_CLAUSE_...`) states: "Clock independence still depends on the supplied initial component `r_0·ĥ`. It does not show that neighbour records alone determine the odds. A separate preparation rule would be required."
- No attempt exists on `deferred-20260925-conditional-dynamics`. `deferred-20260924-formation` (w-macbookpro9927a) treats block 34's memory residual: no overlap.

## 1. Statement attempted: one finite autonomous preparation question

**Premises.** PR #9041's supplied clauses, nothing more:
- (D-dyn) Heisenberg bond `J σ_x·σ_y` (Pauli coefficient; PR #9142 writes `J σ·σ/4`);
- (D-perm) records as compressions onto `P_q = (1 + q·σ)/2`;
- (D-tr) the trace rule;
- a **supplied** formation time `τ` for one record, with its trace-rule weight and Lüders update.

**Question.** Is the isolated-site law's `λ` a function of the final records when the site's state at isolation is produced by the supplied finite dynamics itself, rather than supplied from outside?

**Answer: no.** An exact finite construction:
- **The sites.** Two neighbouring sites `x` and `y`. Each has its five other neighbours recorded with contents that cancel: three at 120° in a plane plus an antipodal pair. So neither feels a field from them.
- **Start and formation.** `x` starts along `+z` and `y` along `+x`, and `y`'s record forms at time `τ` with content `+z`.
- **After formation.** `x` is isolated in the field `J ẑ`, and its time-averaged odds on `{p, −p}` are `(1 + λ(τ) p_z)/2`, with
  `λ(τ) = cos²(2Jτ)/(1 + sin²(2Jτ))`.
  - The same final records give `λ = 1`, `1/3` or `0` for `τ = 0`, `π/(8J)` or `π/(4J)`.
- **Averaging over a clock does not help.** A constant formation hazard `f` for `y`'s record gives `λ̄ = (8J² + f² )/(24J² + f²)`, which depends on the supplied clock rate: it is `1` for fast clocks and `1/3` for slow ones.

So a records-only isolated-site law needs a preparation (or relaxation) clause that the finite autonomous dynamics does not supply. **No clock and no Born law are derived.**

## 2. Steps

1. **CHECKED (C1) — the landed T1, re-checked.** `P_q σ_a P_q = q_a P_q` for every unit `q`.
2. **CHECKED (C2) — cancelling records.** Five unit vectors summing to zero:
   `(1, 0, 0)`, `(−½, √3/2, 0)`, `(−½, −√3/2, 0)`, `(0, 0, 1)`, `(0, 0, −1)`.
   Under the Heisenberg bond (`M_f = J I`), a site whose five other neighbours carry these records feels no field from them.
   `x`'s and `y`'s other neighbours are distinct sites of `Z³`.
3. **PROVED and CHECKED (C3) — the pre-formation dynamics.**
   - `σ·σ = 2 SWAP − 1`, so `U(τ) = e^{iJτ}(cos 2Jτ − i sin 2Jτ SWAP)`.
   - It satisfies `i dU/dτ = J σ·σ U` with `U(0) = 1`.
4. **CHECKED (C4) — `y`'s record.**
   - From `|↑⟩_x|→⟩_y`, the trace-rule weight of `y`'s record `+z` at `τ` is `(1 + sin² 2Jτ)/2`.
   - `x`'s conditional Bloch vector has `z`-component `cos² 2Jτ/(1 + sin² 2Jτ)`.
5. **PROVED and CHECKED (C5) — isolation.**
   - After the record, `x` is isolated in `h = J ẑ`: the five cancelling records contribute nothing and `y`'s record contributes `J ẑ` (landed T1–T2).
   - Its Bloch vector precesses about `ẑ` at `2J`, and the time average over a period is `(0, 0, r_z)`.
   - So the time-averaged odds are `(1 + λ p·ĥ)/2`, with `λ = r·ĥ` at isolation.
   - This is the landed stationary line, with `λ` fixed by the state at isolation.
6. **CHECKED (C6) — same records, different odds.** `λ(0) = 1`, `λ(π/(8J)) = 1/3`, `λ(π/(4J)) = 0`.
7. **CHECKED (C7) — the other outcome.** If `y`'s record is `−z` instead (weight `cos²(2Jτ)/2`), `x` stays at `+z` for every `τ`, in the field `−J ẑ`: `λ = −1` along `ĥ`.
8. **CHECKED (C8) — a supplied clock.**
   - For a constant hazard `f`, conditioned on the record `+z` and weighted by its trace-rule weight: `λ̄ = (8J² + f²)/(24J² + f²)`.
   - This depends on `f/J`, so no choice of a constant supplied clock makes the law records-only in this history.

## 3. First failing step

None for the stated countermodel. What it shows fails is the **antecedent** of the landed T3 ("the odds depend on the neighbour records alone") for autonomously prepared isolated sites. The landed note and #9142 leave that antecedent as a supplied preparation, and this construction confirms that it is not automatic.

## 4. Next obligations

- **A preparation clause that is history-independent.** For example: relaxation of the isolated site by coupling to a bath that the axioms would have to supply.
- **Whether any finite autonomous history makes `λ` records-only.** It holds when `x`'s state at isolation is already along `ĥ`, as in C7. The question is whether that can happen for all formation times.
- **The occurrence question.** A formation time not supplied from outside. The dependence on `τ` shown here means any derived clock would enter the isolated-site law.
