# checks/tw1 — criteria, pre-registered BEFORE the script exists

Written 2026-10-28T21:41:30Z by the T55-J worker, before `tw1_feas.py` is written.
Exact rational arithmetic (`fractions.Fraction`) in plain python. No BLAS, no numerics lock needed
(session-25 brief rule 6). **No constant below is derived in session 25**: every number and every
inequality is quoted from a pre-session-25 file, with its file:line.

## What tw1 computes

The feasibility of a finite system of **linear inequalities in exponents**. The variables are the
scale-weight exponents of 𝔐 and of BFT-1; the inequalities are the ones the consumers' proofs
impose. The script enumerates the system exactly over Fractions, with no floating point anywhere, and
returns FEASIBLE (with a witness and the region) or EMPTY (with the pair of inequalities that clash).

## Inputs, all pre-session-25, quoted

- **(I-N7a)** `NORMS.md` l.650: the level-0 Wilson vertex contributes exponent (d − θ_w^c − 2θ_A)·k;
  k-uniform **iff θ_w^c + 2θ_A ≥ d**.
- **(I-N7b)** `NORMS.md` l.651: the level-j soft vertex contributes (d − θ_w^r − 2θ_A)·n + θ_w^r;
  k-uniform **iff θ_w^r + 2θ_A > d**.
- **(I-N7c)** `NORMS.md` l.654: **A = L^{d − θ_w^r − 2θ_A}**, and A < 1 ⟺ θ_w^r + 2θ_A > d.
- **(I-N7d)** `NORMS.md` l.656-657: **θ_A = min(1, θ_w^c − 1)** (Lemma N1-5 floor, Lemma N1-6 cap).
- **(I-N7e)** `NORMS.md` l.660: θ_w^c = 2 is the maximum available (K_p^♯ ≥ 1/L², REVIEW_S21 P).
- **(I-A1)** `BFT_A.md` l.834: constraints actually proven on the source weight θ:
  **θ > 0** (Theorem 6.8), **θ < 1** (BL-6 (a), BA-6), **α ≤ θ** (BL-5 (c)).
- **(I-A2)** `BFT_A.md` l.36: α ∈ (0, 1), θ ∈ [0, 1), ω_l = L^{θ(k−l)}.
- **(I-A3)** `BFT_A.md` l.396-397: the claimed window **α ≤ θ ≤ 1 − α (so α ≤ ½)**.
- **(I-A4)** `BFT_A.md` l.538-543 (BL-6 (b)): the F3 slot admits no k-uniform **linear** bound for
  θ ≤ 1 − α; the F3 **remainder** rows are unbounded in it for θ > 1 − α.
- **(I-SF)** `SF.md` l.680: (a5-G♯) states θ ∈ (0, 1].
- **(I-T)** `REVIEW_S22.md` l.399: the BFT target's existential θ_w ∈ (0, 2].
- **(I-d)** d = 4, L = 3 (the lane's standing setting; `NORMS.md` l.509).

## Pre-registered verdicts

**tw1-A — reproduction gate (MUST reproduce a session-24 result).**
System: the single common exponent, θ_w^c = θ_w^r = θ_w, with (I-N7a), (I-N7b), (I-N7d), and
θ_w ∈ (0, 2] from (I-T), at d = 4.
- **PASS** iff the system is **EMPTY**.
- **FAIL** if it is feasible. A FAIL here means my encoding of NORMS §N7 is wrong and every other
  verdict in this file is void. This gate exists to be able to fail.

**tw1-B — the decoupled system at d = 4.**
System: θ_w^c, θ_w^r, θ_A, θ, α as five independent variables, subject to (I-N7a), (I-N7b), (I-N7d),
(I-N7e as a ceiling θ_w^c ≤ 2), (I-A1), and α < θ (strict, since α = θ is recorded OPEN).
- The verdict is **reported either way**; both FEASIBLE and EMPTY are results, not failures.
- If FEASIBLE the script must print the region as explicit inequalities plus one exact rational witness.
- If EMPTY the script must print the minimal clashing subset.

**tw1-C — designed-FAIL control 1 (θ = 0).**
The decoupled system of tw1-B with the source weight pinned to **θ = 0**.
- **CONTROL FIRES** iff the result is **EMPTY**. (I-A1)'s θ > 0 is a strict floor consumed by
  Ω ≤ 1 + 1/(L^θ − 1) (`RTARGET.md` l.588) and by C_P = L/(e(1 − θ)ln L) (`BFT_A.md` l.534); a gate
  that called θ = 0 feasible would be blind to the floor and could not decide anything.
- If this control returns FEASIBLE, tw1-B's verdict is **withdrawn**.

**tw1-D — designed-FAIL control 2 (d = 5).**
The decoupled system of tw1-B at **d = 5**, same inputs.
- **CONTROL FIRES** iff the result is **EMPTY**. The exponent count is supposed to carry the
  dimensional content of the cubic vertex; if it is feasible in d = 5 as well, it carries none and
  tw1-B's FEASIBLE verdict means nothing.
- If this control returns FEASIBLE, tw1-B's verdict is **withdrawn**.

**tw1-E — the d-sweep (reporting, not a gate).**
Report, for d = 2, 3, 4, 5, 6, whether the decoupled system is feasible and with how much slack in each
of (I-N7a), (I-N7b). No PASS/FAIL attaches; this is the output TW-5 asks for.

## What is NOT success

- A verdict obtained by choosing θ_A freely: (I-N7d) **binds** θ_A to θ_w^c and must be imposed.
- A feasible region quoted without saying which of its defining inequalities are PROVEN and which are
  ARGUED or OPEN.
- Floating point anywhere in the script.
- Any claim that feasibility of the exponent system is progress on (G♯_0-field), (SPD) or (G♯-rough).
