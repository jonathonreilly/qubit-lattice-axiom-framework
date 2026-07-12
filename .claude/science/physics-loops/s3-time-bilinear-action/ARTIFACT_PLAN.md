# Artifact plan

1. Rewrite the target note as a self-contained `no_go` source note.
2. Replace the old finiteness/semigroup witness with a runner that checks the
   actual variational mismatch and a generator-bearing control.
3. Record the exact first variation as the independent math check.
4. Run the source runner, syntax checks, vocabulary lint, audit-pipeline
   validation, strict audit lint, and `git diff --check`.
5. Run local review-loop passes and fix only scoped findings.
6. Commit, push the dedicated physics-loop branch, and open one review PR.
