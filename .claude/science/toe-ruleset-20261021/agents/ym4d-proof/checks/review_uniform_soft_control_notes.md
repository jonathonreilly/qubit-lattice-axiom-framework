# Independent control derivations and execution record

The [criteria](review_uniform_soft_criteria.md) predate both programs. The author note and receipt exposed numerical summaries before implementation; author runner source was not read until both independent implementations and successful runs were complete. No mathematical helper was imported. The full [review](../REVIEW_UNIFORM_SOFT_MINIMIZER_ASTRA.md) supplies the all-depth arguments.

## Swept plaquette construction

For a signed edge of an axial root-to-y path P, sweep it through t=0,...,L-1 along the coarse-link direction mu. The signed plaquette boundary equals the edge minus its translated edge plus the difference of straight mu-paths at its endpoints. Summing over P telescopes to

`P - translate_(L e_mu) P + S_mu(y) - S_mu(0)`.

This is the actual rooted contour minus the direct root straight path. Edges parallel to mu give zero. For a centered d=4 block the coefficient norm is at most `L sum_(nu!=mu)|y_nu|<=3L(L-1)/2`; mean subtraction doubles this bound. This is a different construction from the author's adjacent-step-swap algorithm. Program 01 keeps signed integer counters. The 1,944-contour mean for each direction is cleared by that exact integer denominator when checking all 7,776 spreads. Deleting one plaquette or omitting mean subtraction is detected.

## Direct stationary and Schur routes

The one-step KKT solve builds C=d_2, Q_root, Q_str and d from individual links and Bloch phases. Gauge columns are fine gradients with root scalar fixed to zero; the KKT block is `[[C*C+kappa Q_root*Q_root,Gamma],[Gamma*,0]]`. The top zero-momentum harmonic case is checked by its exact constant lift and is not inverted. A separate Fourier Laplacian and co-closed top basis construct B and C for the hard/soft Schur identity. The wrong unprojected root-domain comparison is tested explicitly.

Every nonzero Bloch fibre of top side 3 is solved for all four input orientations, then transformed to the complete periodic kernel. Weighted absolute row and column sums are accumulated independently at m=.003. The F0 output includes all six plaquette orientations and all 3^4 fine offsets. Its column/row ratio is about 100.602; this is not asserted to equal r^4, because maxima also involve orientation and offset dependence. The valid proof uses one common pointwise majorant with its fixed orientation multiplicities and r^4 density.

The depth-two test uses 26,568 unknown link components, kappas .7 and 1.4, actual root maps at both levels, and a stacked root-compatible gauge gradient. Conjugate gradients solve the positive gauge-completed normal system. Independent stationary, residual-transport, and normalized curvature-average equations are evaluated afterward. The derivative has its actual four-link boundary. Wrong sign, wrong kappa ratio and omitted curvature rescaling fail.

## Complex finite characters and images

Program 02 constructs D as a finite character sum; analytic conjugation is D(-z), not conjugation at complex z. It sums complete alias sets at ell=3,9,27. Near-zero complex, boundary-face complex and ordinary complex points check identities and cancellation; face translation tests full alias permutation. These finite points cannot establish the absence of unseen poles.

The sufficient-strip arithmetic repeats the consumed analytic bounds with the repaired fine-curvature condition included. Parameters eta=.005,r0=.57 were visible in the author prose, so this is disclosed arithmetic corroboration. The deliberately invalid eta=.1 case has rho_beta>1; downstream rational values there do not qualify as bounds and are used for no positive assertion. The five-condition certificate is rejected.

The one-dimensional periodic kernel is evaluated by its exact geometric-image expression `(exp(-a*x)+exp(-a*(T-x)))/(1-exp(-a*T))`, with x reduced modulo T. Taking products and summing on the actual fine mesh reproduces coth(a/(2r))^4; a nearest-image-only substitution fails. The general proof follows by unfolding, not these finite values.

## All executions and repairs

1. Program 01 attempt 1 exited 1 at Python parsing: one unmatched parenthesis. Its source, empty stdout and stderr are preserved as `review_uniform_soft_01_attempt01_*`. No scientific computation executed. Removing that extra parenthesis was the sole repair. The corrected source parsed and ran once, exiting zero with 34/34 predicates and empty stderr.
2. Program 02 attempt 1 reached final JSON serialization, then exited 1 because condition flags included a NumPy boolean. The exact source, empty stdout and full error traceback are preserved as `review_uniform_soft_02_attempt01_*`. Casting the five flags to native bool was the sole repair. The corrected program ran once, exiting zero with 84/84 predicates and empty stderr. No mathematical formula or threshold changed.
3. Post-execution review found that several Program 02 identity cutoffs were 1e-9 or 1e-8, looser than the criteria's general 1e-10 identity cutoff. An exhaustive check of every saved identity-error field against 1e-10 passes (largest 8.74087600908654e-11). This is a disclosed later evidence check against the original criterion, not a new threshold or a rewritten run. The mechanical output records it. Floating point errors near the narrowest sample remain diagnostic only.
4. An attempted split of an existing extracted PDF text on form feeds raised IndexError because that text did not contain page separators. No source or evidence file was overwritten. Reading the original PDFs by numbered pages with PyMuPDF succeeded. Exact pages and PDF hashes are in the source manifest. An optional governance-path lookup used the wrong directory for CANONICAL_HARNESS_INDEX, then git tree discovery located docs/CANONICAL_HARNESS_INDEX.md; only its introduction and targeted absence search were read.

All exceptions are recorded in the [failure metadata](review_uniform_soft_failures.json). Deliberate mathematical mutations are successful falsifiers, not erased failures. The two empty attempt stdout files have .json names because they were redirected before the process failed; they are intentionally preserved as empty streams, not valid JSON documents.

## Overlap after author-code inspection

Both author programs, criteria, saved outputs, stderr and retrieval metadata were inspected after independent runs. Shared objects include the exact S4′ contour convention, normalized Hessian, known symbol identities, L=3 test geometry, the prose-exposed weighted norm values and conservative strip pair. The independent implementation choices are signed swept surfaces, direct constrained KKT, gauge-completed sparse depth-two solve, direct finite characters, and closed geometric periodization. No claim of independent discovery or mathematical priority is made.

The author's first 56 path predicates repeat across three modes. Its second integer program uses a separate swap construction; its saved-kernel density mutation is post-selection, explicitly disclosed. This reviewer did not rerun author code. Independent numerical agreement and exact boundary arithmetic strengthen finite implementation confidence; the analytic proof remains responsible for all depth and volume quantifiers.
