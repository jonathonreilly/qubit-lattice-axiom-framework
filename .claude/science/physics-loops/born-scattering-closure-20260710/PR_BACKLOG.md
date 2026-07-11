# PR Backlog

## Block 01

Status: open; independent review/audit pending.

PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/5137

Branch: `physics-loop/born-scattering-closure-block01-20260710`

Title: `[physics-loop] born-scattering closure block01: bounded no-go`

Body: [`PR_BODY.md`](PR_BODY.md)

Verified remote state after creation: base `main`, expected head branch,
non-draft, open. The audit-lane check was in progress; no merge was attempted.

Recovery commands if the PR must be recreated:

```bash
git push -u origin physics-loop/born-scattering-closure-block01-20260710
gh pr create --base main \
  --head physics-loop/born-scattering-closure-block01-20260710 \
  --title "[physics-loop] born-scattering closure block01: bounded no-go" \
  --body-file .claude/science/physics-loops/born-scattering-closure-20260710/PR_BODY.md
```
