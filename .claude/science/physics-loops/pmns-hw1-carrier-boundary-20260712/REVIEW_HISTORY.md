# Review History

## Pre-review state

- Base: `origin/main` at `5ad790c3e`.
- Initial worktree: clean.
- Shared automation lock: unavailable because the script hardcodes another
  user's home directory.
- Fallback lock: acquired at
  `/private/tmp/pmns_hw1_source_transfer_boundary.physics-lock.json` with
  holder `pmns-hw1-872bcebf`.
- Review-loop disposition: pending.

## Promotion value gate

Draft answers are recorded in `OPPORTUNITY_QUEUE.md`; final answers will be
written after the decisive artifact exists and before PR creation.

## Independent math check

An implementation-independent SymPy check was run after the first passing
runner execution. It solved the entrywise commutator equations directly (no
Kronecker/SVD path) and returned
`X=diag(x8,x8,x8)`. It also simplified

```text
R_act = 1/[1-lambda_act(alpha-1)] I_3,
R_pass = 1/[1-lambda_pass beta] I_3
```

and both reconstructed-block residuals to the exact zero matrix. Command:

```bash
python3 - <<'PY'
import sympy as s
x=s.symbols('x0:9'); X=s.Matrix(3,3,x)
Tx=s.diag(-1,1,1); Ty=s.diag(1,-1,1); Tz=s.diag(1,1,-1)
C=s.Matrix([[0,1,0],[0,0,1],[1,0,0]])
eqs=[]
for A in (Tx,Ty,Tz,C): eqs.extend(list(X*A-A*X))
print(s.linsolve(eqs,x))
a,b,la,lp=s.symbols('a b la lp', nonzero=True)
Ra=(s.eye(3)-la*(a*s.eye(3)-s.eye(3))).inv()
Rp=(s.eye(3)-lp*b*s.eye(3)).inv()
print(s.simplify(s.eye(3)+(s.eye(3)-Ra.inv())/la-a*s.eye(3)))
print(s.simplify((s.eye(3)-Rp.inv())/lp-b*s.eye(3)))
PY
```

Observed result: scalar joint commutant and two exact zero reconstruction
matrices.

## Review Results (Iteration 1)

### Code / Runner: FAIL
### Physics Claim Boundary: BOUNDED / FIX
### Imports / Support: DISCLOSED / FIX
### Nature Retention: BOUNDED
### No-Go Discipline: PASS with documentation fixes
### Labeling Convention: PASS
### Repo Governance: FIX
### Audit Compatibility: FIX pending validation pipeline
### Methodology Skill: SKIPPED

Findings and fixes:

1. `SEMANTIC_BRIDGE`: opening language blurred the explicit invariance
   hypothesis with axiom output. Fixed by making the question/answer
   conditional and deleting the unproved maximality sentence.
2. `MISSING_ARTIFACT`: finite admissibility samples did not constitute a full
   four-axiom model. Fixed by removing that claim and using the exact formal
   language-extension argument; the runner now verifies only source-signature
   absence and the two explicit carrier assignments.
3. `IMPORTED_VALUE` / interface disclosure: local support classifier was
   implicit. Fixed by adding a separate defined support-interface premise.
4. `BUG`: the first local classifier missed permutation-conjugate active masks
   and admitted non-cyclic passive permutations. Fixed by implementing the
   six-permutation active orbit and the three cyclic monomial masks, with
   positive/negative controls.
5. `OVERCLAIM`: universal/independent runner labels described a 16-point grid.
   Fixed by narrowing runner labels; the universal statement is carried by the
   displayed analytic proof and the independent SymPy check above.
6. `NO_GO_OVERCLAIM`: N2 collapsed separable carrier, normalization, and
   sector-relation walls. Fixed by a three-wall pairwise independence table.
7. `API/CLAIM FIREWALL`: legacy consumers require the historical function
   name. Added `conditional_unit_hw1_source_transfer_pack`, retained the old
   name as an alias, and added machine-visible `normalization_status` metadata.
8. `REPO_GOVERNANCE`: added portable locators/status evidence to N1/N4/N8;
   final loop-state refresh remains pending review-loop disposition.

Iteration-1 fix checks: paired runner `PASS=31 FAIL=0`, Python compilation
passes, compatibility alias/metadata smoke test passes.

## Review Results (Iteration 2)

### Code / Runner: RISK — one stale docstring
### Physics Claim Boundary: BOUNDED / FIX — two stale evidence rows
### Imports / Support: DISCLOSED / FIX
### Nature Retention: BOUNDED
### No-Go Discipline: FAIL — N2 wall-independence wording
### Labeling Convention: PASS
### Repo Governance: FIX
### Audit Compatibility: FIX pending the mandatory N2 correction
### Methodology Skill: SKIPPED

Fixes applied:

- replaced the stale explicit-reduct docstring with formal same-premise
  expansion wording;
- replaced stale Admissibility/Record executable-witness claims with the
  conservative-signature argument;
- corrected N2 to the independent set `{W_C,W_A,W_P}` and recorded
  sector-exchange as an alternative retirement route;
- added the exact N4 blocker locator;
- refreshed import-ledger roles/dispositions and artifact-plan wording.

## Review Results (Iteration 3)

### Code / Runner: PASS
### Physics Claim Boundary: BOUNDED — PASS
### Imports / Support: DISCLOSED — PASS
### Nature Retention: BOUNDED
### No-Go Discipline: PASS
### Labeling Convention: PASS
### Repo Governance: PASS
### Audit Compatibility: PASS at pre-pipeline gate
### Methodology Skill: SKIPPED

No findings remained in the iteration-3 targeted file set.

## Audit-pipeline compatibility validation

Commands:

```bash
bash docs/audit/scripts/run_pipeline.sh
python3 docs/audit/scripts/audit_lint.py --strict
git diff --check
```

Validation result:

- target `claim_type`: `bounded_theorem`;
- target dependency set: `[minimal_axioms]`;
- helper runner set: empty;
- target runner: revised paired runner;
- target queue state: `ready: true`, `criticality: critical`;
- strict lint: no errors (repository-wide legacy warnings/notices remain);
- every regenerated audit/effective-status/front-door output was restored from
  `origin/main`; the untracked pipeline certificate was removed.

## Additional compatibility checks

- paired runner: `PASS=31 FAIL=0`;
- direct SymPy solve/reconstruction: exact scalar commutant and zero residuals;
- support-interface cross-check against `pmns_lower_level_utils`: all six
  active permutation conjugates and all six monomial permutations agree;
- compatibility alias/metadata smoke check: pass;
- five direct downstream consumers execute through the wrapper; four pass and
  one reproduces an unrelated pre-existing source-manifold text-needle failure;
- minimal-axiom companion: `68/68`;
- generation carrier boundary: `4/4`;
- independent Burnside companion: `50/50`;
- vocabulary lint and portable-link gates: clean.

## Review PR disposition

- opened: 2026-07-12T18:47:32-04:00;
- PR: [#5300](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/5300);
- base/head: `main` / `physics-loop/pmns-hw1-source-transfer-block01-20260712`;
- initial GitHub disposition: open, non-draft, mergeable;
- audit-authority diff gate: clean;
- merge action: intentionally not performed.
