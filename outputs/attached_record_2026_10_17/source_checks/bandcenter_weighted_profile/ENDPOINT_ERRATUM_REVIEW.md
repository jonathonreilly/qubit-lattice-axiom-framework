# Endpoint strictness erratum to the frozen weighted-profile source

The reported defect is real. In equation(4) of frozen PROPOSAL.md SHA256ab3b7cbfb3ff8159541564ca088b23072f42c075149225b34318d11d581a9ed0, the displayed scalar comparison

    rho(x)+6x+rho(x)/(1-rho(x))+delta_c < 9x+delta_c

is false at x=0: rho(0)=0, so both expressions equal delta_c=1e-86. The precise correction is ≤ on the entire closed interval, with strict inequality only for x>0. This erratum records that correction without altering the historical source bytes.

The ACTUAL scattering norm still satisfies the strict ceiling <9x+delta_c on the entire interval, including x=0. The distinction must be made explicitly instead of attributing strictness to the equal scalar ceilings. No downstream constant needs to change.

## Direct reconstruction

To avoid ambiguity, define epsilon_closed(q)=||S_loaded(q)-S_old(q)|| and define the fixed ceiling Delta_c=1e-86. The checked full feedback estimate is epsilon_closed(q)<Delta_c. This is not an assertion that the actual feedback vanishes at the center.

Write Z=z^(2F). The exact loaded open matrix S_loaded is unitary on the real band, and

    S_new=r_n I+t_c² Z S_loaded (I-r_o Z S_loaded)^-1.

Subtracting its target -Z S_old, with the inverse correction separated before changing S_loaded to S_old, gives the norm ceiling

    ||S_new+Z S_old||
      <=rho+rho/(1-rho)+|t_c²+1|+epsilon_closed(q)
      <=rho+rho/(1-rho)+6x+epsilon_closed(q)
      <rho+rho/(1-rho)+6x+Delta_c
      <=9x+Delta_c.

The last comparison is non-strict at x=0; the preceding comparison is strict there and elsewhere because the full physical feedback is strictly below its fixed ceiling. For x>0, rho≤1.22x and the established small return margin give an additional strict margin below9x. At x=0 one can check directly: r_o=r_n=0 and t_c=i, hence S_new=-Z S_loaded, and the actual norm equals epsilon_closed(0)<Delta_c. Thus the exact source formulas, rather than a favorable review label, establish the strict norm claim.

Even if one retained only the non-strict norm ceiling, the next rounded bounds still have positive slack. Reflection combines the old ceiling5e-21+12*.24x with9x+Delta_c. Its constant is strictly below1e-20 and its slope11.88 is below12. Transmission similarly has constant d0+5e-21+Delta_c<d0+1e-20 and slope180.36<181. Therefore both strict r(x),t(x) bounds survive at zero and away from zero independently of the erroneous strict scalar comparison. The downstream full Schur/profile estimates use these rounded positive-floor bounds; no central calibration or closed correction is erased.

## Wider-band source and downstream status

Inspected the affected full paragraph in final ../bandcenter_bandwidth_extension/PROPOSAL.md and verified SHA256d79a1e9abbf0508a05169d4588539063854f0604ba8db933cf878496aa7328a2. Its displayed scalar comparison already uses ≤, explicitly says equality is allowed at x=0, and separately justifies strictness of the ACTUAL error by the strict closed-feedback estimate. This is mathematically the corrected chain above. For future prose use, writing epsilon_closed<Delta_c=1e-86 avoids its shorthand that calls delta_c both a correction and a ceiling; the required inequality is supplied by the original full feedback proof.

On the wider interval x≤4e-6, the same algebra applies using rho(h)<4.88e-6. The enlarged-domain margin gives rho+6x+rho/(1-rho)≤9x, with equality at0 and strict inequality at positive x. Neither the pointwise floors/slopes nor the wider profile a=1.8e-13,b=220 changes. Consequently this erratum introduces no change to the previously reviewed weighted finite-band mass, normalization or initial-comparison constants, on either width. This is a narrow implication check of the endpoint correction, not a fresh certification of every wider-band premise or a temporal result.

## Review accountability, sources and limits

Inspected the exact frozen equation(4), its adjoining definitions and equation(5), the wider-band affected argument, and my prior bandcenter_weighted_profile_check/REVIEW.md at verified SHA256d2ac8183a6531cce4ed96da1b841b99d31e1340de4b9422507b82f5da7bb9071. That prior review correctly reconstructed the open cost as zero at x=0 and correctly retained the strict physical closed-feedback bound, but it failed to flag the remaining false strict comparison BETWEEN THE TWO DISPLAYED SCALAR CEILINGS. Its statement that there were no outstanding requested fixes was therefore too broad at the source-text level. This erratum corrects that omission. It does not retrospectively claim that the earlier reviewer caught it.

I authored that prior review and the initial wider-band proposal. This is an exposed author/reviewer correction of a directly exhibited algebraic endpoint defect, not a new independent review of my own ancestry. The parent conveyed the publication author's finding before this check. Necessary exact multiple-return and full-feedback premises were read completely in the coherent earlier tasks and are conditionally reused here; no unrelated source theorem is revalidated.

Required repair for publication: reproduce the corrected non-strict scalar chain plus separate strict actual-feedback statement, and preserve/link this erratum when the historical ab3b7cb source is cited. Do not rewrite the historical frozen file or silently describe its displayed inequality as valid. The final wider-band source already contains the required endpoint correction and needs no numerical or theorem-constant repair from this issue. Publication's own final argument still requires its ordinary integration check.

Only this deliverable was written. No frozen source, W/Git/model/prompt/checkpoint or other file was changed; no scientific execution, solver, delegation, audit or publication occurred. Deterministic source reading/hashing and direct algebra only. An initially combined read was marginally truncated; the necessary prior-review argument was reread in a separate complete output and no truncated content is counted as checked.
