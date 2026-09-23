# Post-seal comparison: fast ring spectrum and formation outputs

2026-09-23. This is a bounded scientific source comparison, not formal audit,
publication approval, or a subsequent-formation theorem. No required source
correction or unresolved mathematical defect was found in the stated scope.

The independently reconstructed operator, complete general-L spectral measure,
and L=4 controls in `REPORT.md` were frozen before author access. They remain
byte-identical under PRE seal
`cffc3495e440045bd73077e8be1a5e231ff39a07e53889a22336c204f60f5c37`.
The new work below checks the author's added lowest-band/gap argument and the
complete source/evidence assembly. It does not relabel post-access work as blind.
Prior exposure to the independently checked L=3 example remains disclosed in
the PRE report. The author seal also discloses receiving concise progress before
its freeze; it does not claim isolation from those messages.

## Sources and authentication

The authorized author folder is `../post_birth_ring_spectrum_author/`.

| Item | SHA-256 |
|---|---|
| `AUTHOR_SEAL.json` | `c2e0e2adcff2dee95c682da2789c19f3113445e7f3e53f20d95936ab25ec07b9` |
| `EXACT_FAST_SPECTRUM_AND_FORMATION_OUTPUTS_ON_RINGS.md` | `b9c30d8418cb4d4c577ea193dee8482d2d0c92125823593feb2a7c01b8310bf5` |
| `ring_spectrum_check.py` | `79b9ab1095d58f9e4b56a5ca61f6106cbe65956205ba8ca8bc9e252d0fdbe9cf` |
| `RING_SPECTRUM_RESULTS.json` | `bf7f114668dc5e27dc015f9c3c2af7e48d9925652e890a02431c31f31cde6b77` |
| Checked third-campaign fast-target premise | `002119d5a3f9bec171c3678cb15afdb91f7a763311ca38e6e4458ce10865572e` |
| Independent PRE report | `8bb9e330303d5b66e14c19031716d8fb8e7baa5a49d193759dbabce1f343b7b2` |

`comparison_check.py` authenticated all 11 author artifact bindings plus the
parent-source binding, and all six source plus 29 artifact bindings in PRE.
The complete note, final checker, preserved initial probe, both complete saved
result objects, command receipts and streams were inspected. A combined tool
display truncated a small part of the L=7 results; a targeted complete L=7 read
repaired that display before disposition. The final and exploratory stdout
files are byte-identical to their respective result JSONs, and both stderr files
are empty. Both receipts bind the actual source and successful commands.

The preserved probe-to-final diff adds spectral-measure, zero-angle gap and
crossing checks without altering the physical-hop or factorization builders.
It is recorded in `AUTHOR_PROBE_TO_FINAL.diff`. Authentication of the author
runs is not an independent scientific calculation. Their two runners were not
rerun. The independently executed comparison uses only function definitions
from the already sealed independent `ring_control.py`; no author builder is
imported or executed.

## General-L operator and formation law

Sections 1–3 agree with the PRE reconstruction. The P-space occupation word has
two occupied B positions and one minus among M=L+2 records. Every empty B has
two occupied A neighbors, giving the diagonal -2(L-2). A non-reversing two-hop
return to P moves one occupied B to its vacant neighbor and transports both
unchanged records along that length-two route. Its amplitude is -1. In vacancy
coordinates it is the opposite vacancy move. This accounts for every two-hop
term; there is no additional simultaneous-hole channel at this order.

The cut move applies

    V_theta |r> = exp[i theta(1-2 delta_(r,0))] |r-1>,
    V_theta^M = exp(i L theta) I.

The author's vacancy coordinates and the PRE occupied-pair coordinates have
opposite spatial motion across the same cut, with this same charge-word
unitary. The corresponding plane-wave sign convention can be reversed; the
cosine spectrum and specified overlaps agree. The boundary fermion sign is
essential: the h-vacancy representation uses pi(h-1); the complementary pair
representation uses pi. The PRE wrong-sign control already rejects dropping
this pi. Complementing the two omitted momenta and shifting by pi changes the
integer momentum label by two, which explains the equivalence without adding
an unexplained twist.

In the occupied-pair representation the complete eigenbasis is the product of
the charge-word eigenvectors and normalized two-coordinate Slater determinants.
For phi_s=(L theta+2 pi s)/M, its energies are

    -2(L-2)-2 cos[(2 pi m+pi+phi_s)/L]
             -2 cos[(2 pi n+pi+phi_s)/L],  m<n.

These have M binomial(L,2) labels, the full fiber dimension. The one-dimensional
wedge construction is a spectral representation, not a claim of new record
statistics. No theorem from the contextual Hubbard references is needed here;
their literature content was not independently reviewed for this comparison.

For the named first mark, the only prior destination is B_(L-1). The old plus
crosses the flux cut once, and both newborn orientations share the same flux
translation. The normalized resolved charge word is r=1; the coherent channel
is (|r=0>+|r=1>)/sqrt(2). Their relative sign is positive. The common flux phase
does not change fiber probabilities. Taking the adjacent-coordinate Slater
minor gives exactly

    p_res(s,m,n) = 4 sin^2[pi(m-n)/L]/(M L^2),
    p_coh(s,m,n) = p_res(s,m,n) [1+cos(theta-phi_s)].

Both sum to one, with equal energies grouped at degeneracies. The formulas
match the complete PRE eigenvector-residual and physical-field moment checks,
not merely equality of sorted eigenvalues. The centered variance is 2, and the
mean is -2(L-2), for both instruments and every angle. Two distinct coherent
charge words have no common one-step neighbor and no path of length at most
two between them with the original B pair restored. The interference thus
does not change either of these moments. It does change higher moments for
certain coherent normalizable field inputs, as retained in PRE.

## Lowest-band ordering, gap and exceptional angles

The added claims in Section 4 follow from the complete spectrum. A useful
independent organization is to collect all adjacent momentum pairs from all
word branches. Their energies are, with multiplicity,

    -2(L-2)-4 cos(pi/L) cos[(L theta+2 pi k)/(L M)],
    k modulo L M.

The nearest center to zero selects phi_* with |phi_*|<=pi/M. For L>=4 a
nonadjacent pair has absolute separation factor at most cos(2 pi/L), whereas

    cos(pi/L) cos[pi/(L M)] > cos(2 pi/L).

For L=3 all pairs are adjacent. Thus this nearest-center branch really is the
global fiber minimum, not just a minimum within a guessed subfamily. At theta=0
the nearest center is unique. The next two are at +/-2 pi/(L M). They also beat
all nonadjacent pairs, since

    cos(pi/L) cos[2 pi/(L M)] >= cos^2(pi/L) > cos(2 pi/L)

for L>=4. Hence the claimed gap and curvature are correct:

    gap_L(0)=4 cos(pi/L) {1-cos[2 pi/(L(L+2))]},
    e_0''(0)=4 cos(pi/L)/(L+2)^2.

Their asymptotics are 8 pi^2/L^4 and 4/L^2, respectively. At
theta=(2j+1)pi/L modulo 2pi, the two nearest centers tie. There are exactly two
lowest eigenvectors, and their probabilities must be summed. This validates
the note's explicit exceptional-angle treatment. Neither the zero-angle gap
nor its curvature is a uniform gap over rotor angles or a three-dimensional
propagation claim.

The independent new controls rebuilt the full legal-hop matrices for
L=3,4,6,9 at seven angles each: zero, negative crossing, positive crossing,
both nearby sides, another crossing, and a generic angle. They checked the
minimum, multiplicity, zero-angle gap, twofold first excitation and the entire
lowest-eigenspace weight for both marks. All passed. The largest minimum-energy
formula error was below 8e-15. In particular L=4, theta=pi/4 has resolved
lowest-eigenspace weight 1/24, not the generic 1/48. The note correctly limits
its constant rank-one expression to almost every angle.

For normalizable rotor states, the Fourier spectral measure is absolutely
continuous with respect to circle measure. For a density operator this follows
by a positive trace-class eigenvector expansion: its angle density is the
summable nonnegative sum of the squared Fourier wavefunctions. The finite
crossing set consequently has zero probability. Therefore the generic
resolved weight

    w_L=4 sin^2(pi/L)/(L^2(L+2))

does give the physical band probability for every allowed initial field
density. For a coherent mark it must instead be integrated against
1+cos(theta-phi_*(theta)). A sharp integer flux has uniform angle density;
grouping the integrand in L equally spaced angles cancels its cosine correction
because phi_* is 2pi/L periodic. Additional controls checked that cancellation
at independently selected angles for L=3,4,6,9,20. A sharp angle remains
nonnormalizable. The theta=0 coherent value 2w_L is an angle-local limit, not
the value for a sharp flux or all normalizable inputs. The source states this
distinction correctly. The asymptotic w_L~4 pi^2/L^5 follows directly.

## Compact-fast-time transfer

Section 6 uses only the already checked fixed-graph, uniform-spin approximation
with P-supported initial density. Rechecking its exact hypotheses confirms that
the fast-target theorem is for any fixed finite bipartite graph; the separate
cubic restrictions of its first-event field corollary are not needed here.

On tau=epsilon^2 u/delta, the target generator is

    -i[H2, .] + epsilon^2 (-i[H4, .] + (kappa/delta) sum D[B_j]).

At fixed L its bounded remainder has norm O(epsilon^2), uniformly in integer
spin. Trace-norm contraction and Duhamel give the stated compact-u error. The
inherited microscopic error remains O(epsilon). Normalized spin shifts and
their adjoints converge strongly to rotor shifts under the usual embeddings;
bounded products defining H2 then converge strongly with a common fixed-graph
bound. Polynomial approximation of the exponential and finite-rank
approximation of trace-class inputs give uniform compact-u convergence for
convergent normalizable initial densities. This argument supports arbitrary
joint epsilon->0, S->infinity sequences at fixed L. It requires no uniform
fiber spectral gap and does not exchange a long-time average with those limits.

The source correctly treats specified mark outputs as effective initial states.
The bound for deterministic P-supported initial densities does not by itself
prove convergence of microscopic histories conditioned at a random first
event, or a uniform normalized conditional error for a rare selected outcome.
The source expressly excludes that inference. Likewise the bounded effective
intensity gives an O(epsilon^2) probability of another effective formation on
the compact-fast-time interval, not its ordinary-time waiting distribution.
No second-event source was read or used. PRE's L=4 initial next-channel norm
control remains only an operator control, not that missing dynamics.

## Evidence and remaining boundaries

The full author checker implements exactly the described direct two-hop
Laurent dictionary, an independently coded vacancy/word dictionary, and the
same resolved/coherent output normalization. Integer dictionary equality is
an exact finite check. Dense eigenvalues, characteristic functions and overlap
comparisons are floating controls, correctly labeled as such. The declared
L=3 through 8 grid and printed error maxima agree with all saved rows. At
crossings the author's checker tests the two lowest eigenvalues; the new
independent controls additionally test both full-ground-space probabilities.
No consequential prose/code drift was found.

New executable evidence is `comparison_check.py`, `COMPARISON_RESULTS.json`,
`comparison_run.stdout`, `comparison_run.stderr`, and
`comparison_run_RECEIPT.json`. The actual command was

    /opt/homebrew/opt/python@3.13/bin/python3.13 run_control.py comparison_check.py comparison_run

It completed in about 1.35 seconds with exit code zero and empty stderr.
The comparison added no failed scientific assertion. The earlier preserved
SymPy symbol-assumption helper failure and repaired original control remain
unchanged in PRE; they have not been removed from the final evidence.

No source correction is requested. The confirmed claims concern the supplied
unit-rotor ring operator, specified effective first-mark outputs, exact
general-L fiber formulas, normalizable band probabilities, and the stated
fixed-graph compact-fast-time transfer. This report does not extend them to
ordinary-time repeated formation, prepared lowest-band occurrence, increasing
volume, a photon phase, native quantum dynamics, or a formal retained status.
Those limits are not unresolved steps in the formulas checked here; they are
separate claims absent from this bounded result.
