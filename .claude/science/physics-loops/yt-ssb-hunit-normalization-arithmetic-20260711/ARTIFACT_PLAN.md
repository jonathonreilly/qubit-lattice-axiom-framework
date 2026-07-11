# Artifact Plan

1. Edit the target note so normalization begins from `S_D=sum_i E_i`.
2. Derive `||S_D||_HS^2=D`, then `c=1/sqrt(D)` on the positive ray.
3. Evaluate two distinct components separately; remove alias-equality logic.
4. Update the runner to compute the coefficient from the norm and exercise
   rescaling, phase/sign, and nonuniform-weight falsifiers.
5. Refresh the paired log.
6. Run review-loop, the direct runner, an independent symbolic check, Python
   compilation, vocabulary lint, audit-pipeline validation, strict audit lint,
   and `git diff --check`.
7. Drop all pipeline-generated audit/status outputs before commit.
