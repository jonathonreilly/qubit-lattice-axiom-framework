# Independent control limits and preserved correction

Both independent implementations ran once, after their criteria. Their
executed source and complete output remain unchanged. Script 01 returned
30/30, script 02 returned 35/35, and both saved stderr files are empty.

Script 01 contains an **unexecuted comment error** above
`unmatched_two_leg_claim_rejected`: the four-insertion word
`Tr(P0 V G V Delta G V G V)` is stated as `1/(4 lambda(p)^2)`.
For `V=cos(p.x)` and no relevant momentum resonance its correct value is
`1/(8 lambda(p)^2)`. Starting at momentum zero, the only surviving routes
are `0 -> p -> 2p -> p -> 0` and their negatives. Each has four factors
1/2, two uncancelled factors `lambda(p)^-1`, and the middle `Delta G`
equals one at `+/-2p`. Their sum is 2/16. This word also has **four**
external insertions, so it is not evidence for the two-external-leg FC15
claim. No executed predicate or output used that comment or that value.
The actual nonzero determinant-defect evidence is instead the independent
two-vertex covariant-Laplacian calculation with coefficient -1/2.
The incorrect comment is retained to preserve the executed script bytes.

Script 02's predeclared negative root-mean criterion is implemented directly
for Q_per. It does not execute a second separate ghost determinant with the
root-mean term removed. That missing mutation is not counted as numerical
coverage. Its failure is established analytically: if the root-mean row is
deleted, `1_f* F_naive d = -1_c* J* Delta_f`, which is nonzero for the
periodic root set. Hence the prescribed common constant-free left domain is
lost. The author's separate nine-site mutation was read but not replayed or
counted as independent evidence.

The second control uses T=2 and L=3. Its 6^4 fine incidence has no short-edge
collision. The two coarse forward directions along a two-cycle are distinct
oriented bonds in the actual action. This is a valid finite normalization
and local-path test, but the fixed-depth periodization theorem quoted from
Recovery uses T>=3. The script is not presented as testing that theorem's
large-volume assertion. The analytic review supplies the volume passage.

The exact SU(3) control uses polynomial link fields on one local contour
neighborhood; it does not impose periodicity on those polynomial fields.
The second control supplies the complementary fully periodic geometry.
Its stationary-chain solve and Richardson coefficients are numerical, not
interval certificates or a proof of an infinite-volume or depth-uniform
estimate. The exact script's integer matrix operations stay far below the
int64 bound (Green numerator entries at most 416, sparse derivative rows of
bounded degree); rational divisions and SU(3) expansions use exact arithmetic.

Literature retrieval attempts are also preserved: no `pdftotext` executable,
no `requests` module, an urllib certificate-chain failure, and several HTML
responses at purported PDF URLs. System curl successfully obtained six arXiv
PDFs. No HTML access page was treated as a paper or as a theorem read.
