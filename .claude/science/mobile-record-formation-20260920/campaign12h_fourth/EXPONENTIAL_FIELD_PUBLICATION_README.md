# Finite-time one-link electric tails — review unit

This unit builds on the compensated target and local volume dynamics in
PRs #8841 and #8852, and on PR #8865's physical path matrix. Read
`local_field_exponential_review/ROOT_REVIEW.md`, the unchanged root theorem,
its separate absolute-field corollary, and the independent PRE/comparison.
The PRE was sealed before the checker read the root candidate. Its distinct
path-factorization proof and exact Gauss counterexample support the safe
pair count; the post-PRE comparison found the root coefficient sound.

The supplied target keeps an initially finite one-link exponential electric
moment finite at every finite time, uniformly in graph volume for fixed
maximum degree. The direct absolute-field corollary gives a prefactor-one
Chernoff tail from initial zero field. This is a finite-time statement about
the **exact compensated target**. It supplies no spin-uniform microscopic
limit, time-uniform field control, energy reservoir, or native TOE result.

Run `verify_exponential_field_publication.py` in this directory to check
every selected artifact and pinned source identity. The root
`shift_and_weight_check.py` uses SymPy; the root finite-matrix check and
independent PRE finite check use NumPy. Root scripts accept
`FIELD_EXPONENTIAL_OUTPUT_DIR` for scratch reruns. The independent PRE script
writes beside itself, so rerun it in a disposable copy. Original root and
independent stdout/stderr, exact results and run receipts/seals are included.
No source landing, merge or formal audit verdict is requested here.
