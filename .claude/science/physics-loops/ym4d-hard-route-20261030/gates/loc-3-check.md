# loc-3-check — queue row 224
Provenance: Codex / GPT-6 (serving variant and configured effort not exposed; queue requests xhigh); checkout `6d367c519f0d145221b3786676c6c50a7354169f`; Sussman–Alpoge commit `31a47c543775`; research check, not an audit; grants no status.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the cited outline and YM3 methods. Checks below are by hand; no computation discharges a step.

## 1. Lemma S — ADVANCE

Checked line by line by Codex, first failing step none. The outer-cube argument proves (F). A boundary limit of interior seam points then puts points from both sides of the seam in one layer. This is impossible.

## 2. Corollary S2 — ADVANCE

Checked line by line by Codex, first failing step none for the stated geometric conclusion. The distance assumption puts \(x_b\) inside \(W\); Lemma S includes its entire seam component. This constrains the localisation domain. It supplies no lower bound on dependence on distant data.

## 3. Proposition O — ADVANCE for (a), (b), and (3.1); WRONG as a no-go for (N2′)

Checked line by line by Codex. First failing step none in the geometric proposition or its telescoping consequence. The first unsupported step in the proposed history application is L97: openness of individual failures does not establish a nonempty joint history with all the requested passes.

Even granting that family, L105's “no such nest can carry (N2′)” does not follow. Theorem 6(c) supplies an upper bound, not a positive lower bound. An error can obey both that bound and (3.1), including by being zero. L103 correctly admits that no response lower bound is proved. The geometry exposes a missing estimate; it does not refute (N2′) or justify abandoning every nest.

## 4. Lemma C — ADVANCE, conditional

Checked line by line by Codex against YM3_I I-91-59, first failing step none under the stated carrier and fixed-point hypotheses. Surviving hulls lie inside one wall-component. The margin keeps each constraint row's double block there. Thus both R9 equations split on every row read by an operator; unread rows cannot feed back. The small-solution bounds and uniqueness identify the component solutions. Zero datum gives the zero solution.

This includes the extra assumptions on \(\mathsf W_s\) and the separately specified current construction at L159. It does not establish either assumption for the actual moves.

## 5. Lemma M — WRONG as stated for carried partial maps

Checked line by line by Codex. First failing step: defining \(\varphi(\mathcal K)\) at L125 without admitting every shifted argument into \(F\)'s domain. (D1), (D1c), (D2) supply no such inclusion. SA L5813–5824 requires it for **every** use of (R10), not just the bound (iv), as L145 suggests.

The admission issue is substantive: the small holomorphic interpolation \(a(s_1,s_2)=\epsilon(s_1-s_2)\) has zero endpoint values but \(a(1,0)=\epsilon\). A local function defined on \(|a|<\epsilon/2\) admits both endpoints and rejects that bracket corner. This illustrates the missing premise; it is not a counterexample to the actual R9 response.

With all evaluations admitted, (i)–(iv) are **CORRECT-NO-ADVANCE**: Boolean inversion, component cancellation, and the Cauchy kernel \(1/[z(z-1)]\) give exactly the stated conclusions. The bound is weaker than SA's excess bound; it carries no \(\varrho_F^{-1}\) gain. No algebraic failure remains.

## 6. Theorem W — WRONG from the listed inputs alone

Checked line by line by Codex. First failing step: L169, “re-express each carried piece by Lemma M.” Response existence does not admit a previously formed partial map at every decoupled corner. (D3) concerns new terms; (SUP) concerns histories. Neither supplies this missing premise. SA L17908–17912 explicitly uses hereditary-domain estimates here.

The later equality-preservation steps are valid once the common local families and their evaluations exist. They cannot establish that missing admission. Thus this proof does not yet give later-step or stage (LOC), \(V_{\mathfrak X}(Y)\) locality, or (Act) from (D1)–(D3), (SUP). Repair needed: retain and verify domain inclusion for each carried composition; complex room is also needed for the bounds. No conclusion about failure of the actual Yang–Mills construction follows.

All line numbers above refer to `library/loc-3.md` unless marked SA. Only this report was edited. No audit or status change was performed.
