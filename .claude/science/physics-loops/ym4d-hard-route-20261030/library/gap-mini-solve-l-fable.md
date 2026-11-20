lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-20T14:41Z

# gap-mini-solve-l-fable: the mass gap of four-dimensional SU(2) Yang-Mills

Queue row 1202 of `FINISH.md`, pinned at commit ac1da4568. Worker: Claude Fable 5.2, max effort, Mac mini worker 3. Research-stage working state. Nothing here is a public claim, and no status is granted.

Labels used below: PROVED (every step written here or in a cited checked note), ARGUED (an argument with a named unproved step), GUIDE (heuristic or numeric, never a proof step), OPEN.

## 0. Session log

- 2026-11-20T02:41Z. File created. Next: read the sibling rows `gap-mini-solve-a` to `-k`, `parts/gap.md`, and the RESULT lines, so that this row attacks something they did not.
- 2026-11-20T03:05Z. Record read (Section 1 below). No screening of route families is repeated in this row: rows 1188-1201 did it eleven times and found the lane's map each time.

## 1. Where the record stands (statements about the record, not evidence)

Read in this session: `GOAL.md` in full; `FINISH.md` L1-84, L299-350, row 1202 and the RESULT lines of rows 1179-1201; `parts/gap.md` L1-104 and L223-330; `library/gap-council-synthesis.md` in full; `library/gap-mini-solve-g-fable.md` and `-i-fable.md` in full; `library/prior/gap-2don-proofs-read-opus.md` L1-201 (the digest of Ding, Huang and Yang, arXiv:2611.04908, and of OpenAI's two-dimensional O(n) preprints); `library/gap-solve9-astra62.md` L1-180 (row 1161, the form of (N-phys)).

1. **Two open inputs.** By Theorem BP of row 1179 (check row 1183: the main chain HOLDS AFTER CORRECTION), the Jaffe-Witten gap clause follows from (a) the continuum datum of the T0 chain and (b) one lattice estimate, (N-phys) of row 1161: on one periodic cube n^3 of fixed physical side, uniformly in the cutoff, the centre-neutral excited trace s(u) at a time u at most n/K is at most 1/2. Both are OPEN.
2. **The wall in one sentence** (`parts/gap.md`, The exact price): one selective inequality at every scale between first passage and the seed size is missing. Selective means false for a massless factor.
3. **The only known mechanism at all couplings** is the pair of posted, unrefereed two-dimensional O(n) proofs. Its three parts are: an exact symmetry twist with a smooth periodic free energy; a fourth-order commutator inequality that bounds the twist stiffness by C/log N; a positivity structure (sign clusters, Ginibre, pinning) that turns a small twist cost into decay. The lane's rows 1009-1018, 1076-1086, 1188, 1193, 1195 found that pure SU(2) gauge theory has the bracket, has no non-gauge continuous symmetric twist on the integration variables, and has no association.
4. **Siblings.** Rows 1188-1201 (a to k) each re-derived the map and then worked one small item. None is on the path of (N-phys) except by restatement.
- 2026-11-20T04:30Z. Section 2 written (how I looked for an attack, and what I found again). Attack item chosen in Section 3.

## 2. How best to attack it: what I derived, and where each line already sits (GUIDE; nothing here is a proof step)

I did not screen route families from a list. I started from the one mechanism that is known to cross an asymptotically free band (the posted two-dimensional O(n) proofs, read in `library/prior/gap-2don-proofs-read-opus.md` and `library/prior/gap-o4-pinned-cell-read-opus.md`; credit OpenAI, and Ding, Huang and Yang) and asked what each of its three parts needs in four dimensions. Every line below was derived in this session and then found on file.

| What I derived | Where it already sits |
|---|---|
| The posted iteration is a one-sided renormalization: "stiffness = direct term minus current variance", the direct term is a gradient form for every pin because the group is rigid, and the bracket term of the Ward identity gives a lower bound on the variance | rows 1009, 1010 (reading); row 1011 |
| In the gauge theory a link translation by a fixed colour has a direct term of mass form: beta a^2 abs(A_perp)^2, about a^2 per link for a typical field. The exact response is of curl form only after the seagull term cancels against the current variance. A Jensen bound drops the variance, so it cannot see the cancellation | Lemma WN, Lemma JEN and "best lab-frame bound of order beta eta^2 R" (row 1013); Proposition J (row 1181); Lemmas PC, PC-c (rows 1188, 1193); (HM) of row 1195 |
| A covariant colour axis does not help: the adjoint covariant Laplacian of a typical field has a gap of order 1/beta per link | row 1141 (2); row 1177 (14), (26) |
| Colour twists of pins are free unless a pinned path carries them; the only non-removable continuous twist is a Schrodinger-functional deformation (a holonomy of the pin) | Lemma TWIST (row 1013), Lemma REM (row 1016) |
| A trivially pinned plate has the full rigid group on its free side (the adjacent layer of normal links is an O(4) model in a one-sided background) | Lemma EMB (row 1011), Lemma SLAB (row 1013), sheets with one-sided twists (rows 1096-1123, 1194, 1199) |
| The twist can be spread along the plate at gradient cost but not across the thickness; spreading across the thickness is a translation of rough slices and pays the seagull | row 1013 5.1; (HM) |
| Rough pins have stabiliser Z_2, so a class of pins that is closed under conditioning carries no rigid group | (R-b) of row 1016 6.2; row 1011 7.1 |
| Neutral observables are the whole content of a gauge theory; charged decay is automatic (Elitzur) and gives nothing | rows 731, 1025 (Lemma FAC), 1134 2c |
| SO(3) x Z_2 split: the centre is a ferromagnetic Z_2 gauge theory given the SO(3) part on monopole-free fields, with Griffiths inequalities; frozen at order-one coupling | rows 858-900 (ideas 15, 38, 52; C4, GKS-C) |
| Spacetime symmetries cannot be selective, because the free Maxwell field has them | row 1201 |
| A step-scaling inequality for a finite-volume coupling is the wall in another form | (CAS), route RA; row 859 |

Verdict (GUIDE): a twelfth plain-brief pass by this model family finds the same map. I found no mechanism for the neutral half and no route off the map.
