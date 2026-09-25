# Native one-pair spectrum — released-source POST

The released author claim is supported within its stated fixed-graph,
small-\(g\), fixed incoming electric-basis-state scope. I found no mathematical
correction necessary for that claim. The new row polynomial and its
\(L\ge10\) local counting argument agree with a separate POST reconstruction
and bounded exact checks. The author's finite matrices agree exactly with
the unchanged blind PRE after their factor-of-two and symmetry-quotient
conventions are reconciled.

This is a selective scientific comparison, not an audit verdict, publication
approval, physical-vacuum selection or a finite-spin energy theorem. No author
program was executed or imported. The complete report and evidence of the
blind PRE remain unchanged.

## 1. Exact sources and chronology

The released primary is NATIVE_ONE_PAIR_SPECTRAL_EDGE_ROOT.md, SHA256
e177784652f4c6fafb344ddc72ac20144ebabb9b063e009a1a8618529f8ef922.
Its AUTHOR_SEAL.json has SHA256
69a754ada477506f4437705dbb49e8ebe93b3c230185b7376b3b8d6bfb18dc6d.
All 21 author members and that seal are frozen under post_sources/author.
I read the complete primary argument, historical working derivation, all
three scientific control sources, the author's evidence-verifier source,
all logs, source metadata and review receipts. Large stored integer payloads
were consumed completely and checked by the new comparison program below.

The independent PRE seal is
bed28ea9c81afb7822d0ddeeb552260e3e0547b6f387c9edb8dbd6aec83ee25b.
All its 42 members were reverified before this comparison. PRE.md remains
0a3cbf8eaf157866d0c496ff6fb35f2e0fda5f4ba19767db37aa8a82cc4cf8a9.
Its two scientific parents remain the exact bytes pinned at
60c5f194d940a7bbaf1cdd545296e31d74a02f1a.

The root's THIRTY_THIRD_PRE_ROOT_VERIFICATION.json, SHA256
fe54a392a2dc48669da07e302ab561d3e9d8d91e8be5515f23ad36ff684ca234,
is frozen as process evidence. Its report of root reading/reverification is
not used as scientific authority. Links in author metadata to other work
were not followed.

POST_SOURCE_PINS.json records every source, frozen path, byte count and hash.
The physics-claim-reviewer procedure and necessary instruction references
were read and pinned consistently at the same repository revision. Its
proof and artifact checks were applied within the owner's bounded request:
unchanged model/effort, no delegation, no other active packet, no audit
mutation and no publication edits.

## 2. Conventions and full-sector reconstruction

Let \(Q_{\rm I},q_{\rm I},\Lambda_{\rm I}\) denote the independent PRE
occupation matrix, initial-sector scalar and Perron value. Let \(Q_{\rm A}\)
and \(q_{\rm A}\) denote the author's corresponding objects. Then

\[
Q_{\rm A}=2Q_{\rm I},\qquad q_{\rm A}=2q_{\rm I},\qquad
\rho(Q_{\rm A})=2\Lambda_{\rm I}.
\]

Consequently

\[
\Delta_L=-\frac{\rho(Q_{\rm A})-q_{\rm A}}4
        =-\frac{\Lambda_{\rm I}-q_{\rm I}}2.
\]

There is no energy discrepancy. For \(L\ge6\), \(q_{\rm A}=321L^3\) and
\(q_{\rm I}=321|B|\). For \(L=4\), they are \(270L^3\) and \(270|B|\).
For the simple degree-three cube they are 108 and 54.

The author's Sections 2–3 preserve the same physical Gauss space as PRE.
All two-occupied-B words have one minus among the \(n+2\) occupied sites.
The exact path permutations between these color spaces have operator norm
one. The norm-vector inequality gives the upper bound by \(Q_{\rm A}\), and
the normalized uniform-minus embedding gives the reverse bound. This is a
valid alternative to the PRE's equitable-row/Perron lifting proof. It does
not equate the complete colored spectrum to the occupancy spectrum.

The Gauss Fourier representation includes every integer cycle, including
harmonic cycles. The entrywise phase bound identifies the flat magnetic
infimum, and the physical smooth bump gives the variational upper bound.
The electric operator is the actual occupied-B-gated, nonnegative diagonal
\(D\), not \(\sum E^2\) in the postbirth sector. Smoothness supplies all
electric moments and the required form/operator domains; no false assertion
that arbitrary shifts preserve a degenerate \(D(D)\) is used.

Thus the author's \(O_L(1/\tau)\) variational remainder and the PRE
\(O_L(1)\) remainder agree at fixed \(\tau\). Neither proof requires
compact resolvent or a normalizable ground eigenvector.

## 3. New POST reconstruction of the row polynomial

Here I use the author's factor-two convention. For one pair of overlapping
degree-\(z\) A stars let their B neighbor sets be \(A_*,C_*\), with overlap
\(r\). Let \(X\) be the existing two-B occupancy and put

\[
s_a=|A_*\cap X|,\quad s_c=|C_*\cap X|,\quad
t=|A_*\cap C_*\cap X|,
\quad n_a=z-s_a,\quad n_c=z-s_c,\quad n_i=r-t.
\]

Choose an ordered outward assignment
\(u\in A_*\setminus X,\ v\in C_*\setminus X,\ u\ne v\).
Write \(x=1_{u\in C_*}\), \(y=1_{v\in A_*}\).
For the intermediate occupied set \(Y=X\cup\{u,v\}\), the number of ordered
allowed returns is exactly

\[
|Y\cap A_*|\,|Y\cap C_*|-|Y\cap A_*\cap C_*|
=(s_a+1)(s_c+1)-t+s_ax+s_cy+xy.
\]

Over all allowed outward assignments the sums of \(1,x,y,xy\) are

\[
n_an_c-n_i,\qquad n_i(n_c-1),\qquad
n_i(n_a-1),\qquad n_i(n_i-1).
\]

Subtract twice the vacuum Gram count
\(z^2+r^2-2r\). This reproduces the author's equation (10), including both
mixed terms and their coefficients. In particular, the polynomial counts
returns of old occupied B records as well as reversals of the two outward
hops. Excluding those returns would change the matrix and the sign analysis.

The author's synthetic test has 180 actual input pairs: 21 and 15 for
\((z,r)=(3,1),(3,2)\), and 78 and 66 for \((6,1),(6,2)\).
The new POST program independently enumerates the intermediate-set Gram
sum for every one of these cases and checks all 36 distinct parameter rows.
This is a check against direct counts, not a polynomial tested against itself.

For one occupied B site, count the active A pairs geometrically. Each of
its six A neighbors has six axial and twelve diagonal second neighbors.
The opposite pairs among those six A neighbors are counted twice in the
axial family, and the twelve nonopposite pairs twice in the diagonal
family. Therefore the singly incident counts are
\(6\cdot6-2\cdot3=30\) and \(6\cdot12-2\cdot12=48\), while the doubly
incident counts are 3 and 12. The resulting four contributions are

\[
30(56)+3(80)+48(64)+12(88)=6048.
\]

The new code reconstructs these four counts from coordinates and direct
Gram sums. This matters for provenance: the author's polynomial runner
lines 61–63 supplies the four multiplicities as literal annotations. Its
scalar assertion alone does not verify those multiplicities. The note's
geometric argument supplies their proof, its separate local path runner
checks the complete resulting rows, and this POST explicitly checks the
inventory. No repair is needed, but the literal inventory should not be
advertised as an independently computed table from that particular runner.

For two B sites the correction to twice 6048 is restricted to A pairs whose
two-star union contains both sites. The reconstructed complete correction
inventories agree with every recorded author entry. Their sums are:

| Sorted absolute displacement | Oriented displacements | Common A pairs | Correction | Full row sum |
|---|---:|---:|---:|---:|
| (0,0,2) | 6 | 22 | -196 | 11900 |
| (0,1,1) | 12 | 37 | -584 | 11512 |
| (0,0,4) | 6 | 1 | 26 | 12122 |
| (0,1,3) | 24 | 3 | 72 | 12168 |
| (0,2,2) | 12 | 4 | 92 | 12188 |
| (1,1,2) | 24 | 7 | 152 | 12248 |

All 84 nearby displacements, all six constituent correction tables, and
all four stored far controls were recomputed, including their diagonal
coefficients, target counts, active-pair counts and maximum local radius.
Far-separated inputs have row sum 12096.

## 4. Why the local calculation applies to every \(L\ge10\)

The author's Section 4 argument is valid, but it is useful to make the
local-lifting step precise. Any A pair active at a B site has one A center
one step from that site and its other center at most three steps away.
Every B neighbor used in its outward/return count is within four steps.
Its two-star union has graph diameter at most four.

For \(L>8\), reduction modulo \(L\) is injective on the integer radius-four
ball around a chosen lift. All paths needed for one active A pair lift
there without ambiguity. If the second occupied site belongs to that same
two-star union, its lifted displacement has length at most four. There
cannot be a second such lift because two radius-four lifts differ by length
at most eight, less than any nonzero period. Thus common-pair inventories
are precisely the unwrapped ones in the table.

If the torus distance between the two B sites is greater than four, no
active A pair can contain both and the two single-site contributions add.
If it is at most four, there are exactly the six even-parity types above.
The union of two radius-four balls need not itself be injective; the proof
does not require that stronger assertion. Possible identifications of
final targets between different local terms simply add nonnegative path
coefficients and leave the row sum unchanged.

This proves, on every even \(L\ge10\),

\[
q_{\rm A}+11512\le\rho(Q_{\rm A})\le q_{\rm A}+12248,
\qquad -3062\le\Delta_L\le-2878.
\]

The finite nonnegative-matrix row bound is applicable to \(Q_{\rm A}\),
not to an assumed nonnegative unshifted \(R=Q_{\rm A}-q_{\rm A}I\).
The proof correctly adds the vacuum scalar.

As a boundary control, my POST program also checks all 499 nonzero
even-parity B displacements at \(L=10\). It uses the already checked
indicator polynomial on the actual periodic active A pairs and compares
each row sum to the applicable unwrapped class or far value. Every row
agrees. This finite check supports the local-lifting argument; it is not
an extrapolation from a finite list of tori.

The blind PRE already proves the sign for every degree-six even torus,
including \(L=4,6,8\), by a different uniform-vector Rayleigh calculation.
For \(L\ge6\) its consequence is
\(\Delta_L\le-3024+387/(n-1)\). That tighter upper bound retains PRE
provenance. Combining it with this checked author lower bound, for
\(L\ge10\), is a straightforward mixed-provenance consequence rather than
an original claim of either sealed document. The author's displayed looser
interval is correct as written.

## 5. Actual cyclic support and the unbounded electric term

The author's occupancy connectivity argument realizes legal four-hop
exclusion moves with a spare empty B destination. It gives a strictly
positive occupancy Perron vector and then a strictly positive full
one-minus vector. A resolved birth of a fixed electric-basis input has
positive nonzero Laurent components at zero cycle angle, so the overlap
is positive. The continuous functional-calculus argument then supplies
positive magnetic spectral weight in every fixed neighborhood of the edge.
It retains Haar integration over the complete cycle torus.

The argument also applies to the fixed incoming basis state in the unique
\(N_0\) matter component: its Fourier amplitude is a phase and is nonzero
at zero. This confirms the initial cyclic-edge statement in the author's
equation (4). That explicit incoming-edge comparison is assessed here in
POST; the PRE's principal stated cyclic theorem concerned the birth output.

The author's moment route in Section 5 correctly keeps \(D\):

\[
A_s=H_4+sD,\qquad s=2g^4,\qquad A_s=4\tau g^2h_g.
\]

A fixed finite-electric vector and all its images under a fixed finite
number of \(D,H_4\) factors have finite support. For every fixed moment
order, its \(A_s\) moment is therefore a polynomial in \(s\). This is a
valid domain argument even though general shifts need not preserve the
full domain of degenerate \(D\).

Uniform second moments make the measures tight. Higher even moments give
uniform integrability of every lower moment, so a weak subsequential
limit has the moments of the bounded \(H_4\) measure. If it placed positive
mass beyond any radius larger than \(\|H_4\|\), its high even moments
would violate their bounds. It therefore has compact support and is
uniquely determined by those moments. All subsequences have the same
limit. The author's weak convergence argument is thus complete for this
fixed finite-support input class.

Finite support alone gives that convergence, not a nonzero edge overlap
for every arbitrary superposition. The support statement also uses the
specified basis input and its positive resolved-birth components. The final
finite-support sentence in the author's Section 5 should be read as this
domain restriction, not as an enlargement of the stated input class.

Together with \(A_s\ge\lambda_n\), a positive continuous spectral test near
\(\lambda_n\) proves only the claimed leading cyclic edge. The sealed
PRE's strong-resolvent proof is a shorter sufficient alternative and keeps
its independent provenance; it is not a repair needed to rescue the
author's moment proof.

Both routes leave the following distinctions intact:

- Leading equality does not establish exact cyclic/full-sector bottom
  equality for each fixed \(g>0\).
- The incoming basis vector is fixed as \(g\to0\). A specified positive
  first-event time gives a different \(g\)-dependent input and is not
  covered by substitution or averaging.
- Nonzero support near the edge is not an atom, a lower bound uniform in
  volume on the relevant probability, a typical birth energy or the mean.
- No effective-to-microscopic unbounded-energy or spectral convergence,
  growing-volume exchange of limits, finite-spin conclusion, particle
  mass or empirically identified physical vacuum is supplied.

For a future public synthesis, one explicit sentence excluding exact
finite-\(g\) cyclic/full equality would improve readability. The current
author formulas already claim only limits, so this is optional clarification,
not a missing mathematical premise or required repair.

## 6. Exact matrix and stored-evidence comparison

The author translation quotient is finer than the independent cubic-symmetry
quotient. My new comparison consumes each of its 11,884 integer entries
over 208 rows. For every row, summing its destination entries into the PRE
cubic classes gives exactly twice the corresponding PRE row. Summing the
translation-orbit weights gives exactly the PRE orbit size.

| \(L\) | Author rows | PRE rows | Author integer entries |
|---:|---:|---:|---:|
| 2 | 3 | 1 | 9 |
| 4 | 19 | 5 | 355 |
| 6 | 55 | 9 | 2557 |
| 8 | 131 | 18 | 8963 |

Every weighted symmetry identity and positive rational Collatz inequality
was checked. In these actual stored files the author increment intervals
equal exactly twice the PRE intervals, and the resulting gap intervals
are identical. Their displayed outward decimal summaries are consistent
with the exact fractions. Floating eigenvalues and residuals remain author
diagnostics; no floating eigensolver was rerun.

The author's 36-state colored cube uses a different order of minus locations
within each occupancy. After the explicitly reconstructed basis permutation,
all 1,296 integer entries equal twice the PRE matrix. All 36 occupation
matrix entries also agree. The exact cube gap \(5/2\) and the special
\(L=4\) scalar are preserved.

The code dependencies are internal to the released packet: the local
certificate imports the author's occupancy-row helper, and the polynomial
certificate imports its local-geometry helpers and reads its prior local
result. These are author controls sharing code and geometry, not three
independent scientific reproductions. The POST imports none of them.

The three recorded author executions bind their unchanged source hashes,
complete stdout and empty stderr. The main stdout's four numerical summaries
and final result hash match the full stored result. The local stdout is a
declared projection of its full certificate; the polynomial stdout equals
its complete result bytes. The full integer matrices, local rows and
certificate data were checked beyond those summaries.

Historical wording such as “unsealed” in WORKING_DERIVATION.md and the
initial control result records the state at drafting/execution. It is not
the current seal state and should remain historical if copied. The author
seal and current comparison establish byte identities, not independent
audit status.

## 7. Disposition and preserved boundaries

No required scientific repair was found. The substantive conditional
conclusion is the stated cross-sector energy ordering and leading actual
spectral support. Since the isolated Hamiltonian preserves record number,
the ordering does not itself imply spontaneous unitary decay. The supplied
birth process changes record number, and its physical energy source and
vacuum selection remain separate questions.

The additional local-polynomial and radius-four checks in this POST were
made after author disclosure. They must not be presented as part of the
blind PRE. The original PRE Rayleigh sign proof, symmetry reduction,
primitive charge/Gauss control and strong-resolvent proof retain their
earlier independent provenance.

POST_COMPARISON_RESULTS.json contains the complete new evidence. All runs
and source bindings are preserved in separate POST files. No author source,
PRE member, publication file, audit file or axiom file was changed.
