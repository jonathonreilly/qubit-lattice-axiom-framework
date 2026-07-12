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
