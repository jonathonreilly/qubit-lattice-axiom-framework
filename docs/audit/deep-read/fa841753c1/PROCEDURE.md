# Reading rule

Pin: `fa841753c1a6296e5ad45518375660b0f1004769`

This is the rule for every later note. A reader summary is not a filing. The parent files a row only after the checks below.

The 2026-11-09 non-label re-read missed two repairs. The reader instruction said a printed corrigendum is not a second repair, so a withdrawn sentence that was still on the page was left in place. The same read computed a base ratio from the printed components, saw that it differed from the printed ratio, and waived the gap with a tolerance the note does not print. That instruction is withdrawn.

## File a repair

A row in `FIXES.md` is a printed sentence that is false, or a claim the note overstates.

1. Leftover sentence. If the note has a corrigendum, a withdrawal, or a "what was wrong" block, find the sentence it names. If that sentence is still printed as a current claim, file the leftover sentence. Keep the corrigendum. Do not file the corrigendum's corrected mathematics again. Notes 1634 and 1635 are the examples. The corrigendum is right, and a later section still states the withdrawn claim.

2. Printed join. If the note prints inputs and prints an output as their value, recompute the output from those printed digits. If the printed output is not that value, file the join. Do not add a tolerance, a half-ulp box, or a finer unprinted state unless the note prints that tolerance or says the output comes from a finer state. Do not replace either number unless the note says which one is authoritative. Note 1737 is the example: the printed components do not give the printed base ratios. Note 1711 is the same class. A float the note already calls a numerical illustration is not a repair when the exact value stays inside a bound the note prints. Note 59 is that case.

## Do not file

- A correct no-go, or an identification the note already leaves open.
- A Type-versus-ledger label mismatch, ledger or manifest bookkeeping, or a printed PASS/FAIL.
- A title or filename whose physical reading the body already states and limits. Note 1716 is the example. The body says the proved object is the dimensionless root and does not promote `alpha_s(M_Z)`.
- A conclusion the note already states. Note 1737 already says the shipped fit is outside the small-correction caps. That conclusion is not a repair.

## Who files

The reader writes only the batch file. Any recomputed value that differs from the printed value is reported there, including a gap the reader thinks is rounding. The Result line does not waive that gap.

Before a no-fix row is accepted, the parent does three things:

- Search the note for a corrigendum or withdrawal, and confirm the named sentence is not still printed as a current claim.
- Recompute every joined equality the batch treats as holding, from the printed digits.
- Reject a waiver that depends on a tolerance the note does not print.

Runners are not executed. This log does not rewrite a note, rerun a campaign, or push `main`.
