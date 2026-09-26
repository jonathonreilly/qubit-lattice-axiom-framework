# Fixed-rate formation: larger-volume follow-up declared before runs

2026-09-21. This follows the 144-run exploratory screen and the exact cube
calculation. It does not test a new generator. Use the unchanged, source-bound
geometry-only Gillespie executable, with kappa=1, nu=0, and initially empty
even periodic cubic tori. Bloch marks remain integrated out. Every reported
field is the geometric staggered matching field, not electromagnetism.

The exact slow-birth theorem concerns beta->0 at fixed finite graph. This
experiment instead holds beta fixed while increasing N. Its main question is
whether the observed low-wavevector power remains of order one, or drifts
toward the suppressed spectrum of a gas of bounded independent local curls.
Agreement with Coulomb-like finite-size diagnostics is not a phase theorem,
a proof of Gaussianity, or a proof that the full law is uniform.

Declared grid: N=16,32,64, with 256 independent seeds per beta=0.1,1,10;
N=128, with 64 independent seeds per beta. Total2496 runs. Assign globally
distinct seeds by 210000000+10000*N+1000*beta_index+replicate, with beta_index
0,1,2 in the listed order and replicate starting at1. These seeds do not
reuse the exploratory sample. Use two concurrent processes. The accepted
event cap is10^9 per run. Stop scheduling at the fixed campaign deadline;
retain unfinished/capped outcomes as such and do not relabel them as jamming.

The two primary summaries are (i) first-axis-shell transverse power per
polarization, and (ii) winding power per component, sum_i Phi_i^2/(3N).
Secondary diagnostics: the second/first axis-shell power ratio; the two
diagonal shells; the per-mode fourth-power ratio; total formation time/V;
accepted slides/site; cumulative site reuse. Average modes within each
formation realization before computing between-realization uncertainty.
Do not treat different modes in one realization as independent samples.

Use mean, standard error across runs, and independently seeded bootstrap
intervals over whole realizations for the primary means and shell-power
ratios. Comparisons across rates and sizes are descriptive and declared;
no post hoc removal of inconvenient seeds, phase classification or fitted
critical exponent is permitted. Any subsequent fit must be labeled
exploratory and preserve its complete candidate-size/rate set.

For every completed case, a separate NumPy reconstruction checks the final
record-ID permutation, antipodal-key proxy pairing, nearest-neighbor partner
reciprocity, birth budget, geometric Gauss identity, and equality of winding
flux across all parallel planes. An independent FFT implementation recomputes
all16 saved modes and compares with the C++ direct sums. This is author
verification by another implementation, not independent scientific review.
Capped states retain their complete outputs but are excluded from full-state
spectral summaries with an explicit count.

Keep source, binary, wrapper, protocol and analysis identities; every command,
process return code, stdout/stderr, trajectory and final summary; and a
lossless compact final state. After the full ASCII state is parsed and checked,
save partner and record IDs as signed32-bit arrays and site birth counts as
unsigned16-bit arrays in a compressed NumPy archive. Reopen and compare all
arrays before removing only that newly generated redundant ASCII file. The
site indices are exactly0..N^3-1 and the two ASCII header lines are retained
in metadata, so the original text representation is reconstructible; preserve
its original SHA-256 as well. Large state archives stay in the external
campaign evidence directory and are not staged or included in a review PR.

The production executable may take longer on rare histories; preserve failure
and truncation receipts. If the existing direct-sum Fourier tolerance fails,
retain the state and diagnose roundoff against the independent FFT before
changing any tolerance or rerunning. This protocol itself does not authorize
new physical primitives or a main-branch merge.
