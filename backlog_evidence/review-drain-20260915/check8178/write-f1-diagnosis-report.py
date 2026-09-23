from pathlib import Path
import hashlib,json
R=Path('/private/tmp/review-drain-20260915')
def identity(p):
 p=R/p
 return {'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size}
prefix='drain8178-capture-supplied_torus_auxiliary_field_mode_variance_finite_bracket_2026_09_17-v2'
runner='review-draft-slot/scripts/supplied_torus_auxiliary_field_mode_variance_finite_bracket_2026_09_17.py'
control=json.loads((R/'check8178/f1-diagnosis.stdout.json').read_text())
receipt=json.loads((R/'check8178/f1-diagnosis-receipt.json').read_text())
files=[runner,'review-draft-slot/docs/SUPPLIED_TORUS_AUXILIARY_FIELD_MODE_VARIANCE_AND_FINITE_BRACKET_BOUNDED_THEOREM_NOTE_2026-09-17.md']+[prefix+s for s in ['.receipt.json','.raw-result.json','.sidecar.json','.worker.json','.supervisor.txt']]+['check8178/'+s for s in ['f1-diagnosis.py','run-f1-diagnosis.py','f1-diagnosis-plan.json','f1-diagnosis-receipt.json','f1-diagnosis.stdout.json','f1-diagnosis.stderr.txt']]
r={'schema':'pr8178-f1-failure-diagnosis-v1','reviewer':'/root/review_8178','same_session':True,'verdict':'NARROW_EXACT_COMPARISON_REPAIR_REQUIRED','capture_authorized':False,'production_reruns':0,'source_edits':0,'staging_operations':0,'base':'f947216c6ec62d6c663b9c73ef180b1f4f8b622f','reviewed_main':'f947216c6ec62d6c663b9c73ef180b1f4f8b622f','failed_source_tree':'f43989dbe522bf381dc13f6c9225dcfd5bfc2550','cause':{'path':runner,'line':292,'expression':'U*P*U.H == D','classification':'SymPy structural equality false negative on unevaluated Gaussian rational expressions','math_disagreement':False},'failed_baseline':{'passes':15,'failures':1,'failed_check':'F1','exit_code':1,'runner_elapsed_seconds':1.0133697986602783,'sampled_peak_rss_bytes':126894080,'mutations_run':0,'status':'FAILED; preserved and not superseded'},'control_result':control,'control_receipt':receipt,'proof':'For U[k,x]=exp(-ik.x)/L and P f(x)=(f(x)+f(x-e1)+f(x-e2))/3, substituting y=x-ej gives U(Pf)[k]=(1+exp(-ik1)+exp(-ik2))U(f)[k]/3. At L=4 every coefficient is Gaussian rational. Independent Fraction-pair evaluation verifies all 256 entries. Exact expansion of the SymPy residual also gives the zero matrix; no numerical tolerance or approximation is used. Wrong positive-character target yields nonzero residual, including entry (1,1)=-2I/3.','recommended_fix':'Change F1 predicate only to (U*P*U.H-D).applyfunc(sp.expand) == sp.zeros(L*L). Preserve sign mutation, expected D, real-space P, U, and exact arithmetic.','reviewer_accountability':'Earlier affected-source/cold review missed the structural-comparison defect. The actual failed baseline is decisive execution evidence and remains failed. Independent diagnosis establishes a representation issue, not a counterexample to the accepted negative-DFT proof.','must_reconfirm':['Author produces narrow source diff and refreshed source/unit/tree identities; same-session reviewer verifies only intended exact-normalization change.','Keep every failed capture, sidecar, raw output, cache and control artifact; do not overwrite or relabel failure as success.','Any new production attempt requires root authorization, new immutable adapter/output/once-only identities, refreshed cold binding and same bounded resources; this diagnosis does not authorize a retry.','New baseline must actually pass all 16 checks; four pending new mathematical mutation controls must execute, including wrong-sign F1 rejection. Original four reused controls retain only previously accepted scope.','Refresh affected cache/input hash bindings and required mechanical checks after source changes; no scientific promotion from this diagnosis.'],'evidence':[identity(p) for p in files]}
md='''# PR8178 F1 failure diagnosis

**Verdict: narrow exact-comparison repair required. No retry authorized by this report.**

The actual baseline remains failed (15 PASS, 1 FAIL; F1 only). Its raw output, sidecar and failure receipt remain preserved. No production rerun, mutation run, source edit or staging was performed during diagnosis.

## Exact cause and mathematical result

Runner line 292 compares `U*P*U.H == D` using SymPy structural equality. Twelve entries retain unexpanded expressions despite being algebraically equal. For example, the (1,1) product entry is `1/3 - I/6 + I*(-1/12 - I/6) - I*(1/12 + I/6)`; expansion equals the expected `2/3 - I/3` exactly.

For the negative-character transform and shift sampling x-e_j, substitution y=x-e_j gives multiplier `(1+exp(-ik1)+exp(-ik2))/3`. The accepted proof is correct. An isolated control independently reconstructed the L=4 identity without importing the production runner. All 256 residual entries expand to exact zero. Separate Gaussian-rational arithmetic using pairs of Fractions independently verifies all 256 entries. The wrong positive-sign target produces ten nonzero entries, including residual (1,1)=-2I/3. This is an exact discriminating check, not a tolerance adjustment.

The one bounded control completed with exit 0 in 0.306 seconds, sampled peak RSS 80,379,904 bytes, within the predeclared 30-second/192-MiB process-tree limits. Full script, plan, raw output, stderr and receipt are retained under `check8178/f1-diagnosis*` and hash-bound in the JSON report. No scientific baseline was executed by the control.

## Narrow repair and follow-through

Replace only the F1 predicate with `(U*P*U.H-D).applyfunc(sp.expand) == sp.zeros(L*L)`. Keep D, U, P, the wrong-sign mutation, and strict exact arithmetic unchanged. The earlier review missed this symbolic-representation defect; the failed execution exposed it and must not be erased.

After author repair, rebind source hashes and staged tree, review the narrow diff in this same session, and refresh cold/adapter evidence. A separately authorized attempt needs new immutable output names and once-only identities under unchanged resource bounds. The actual 16-check baseline and all four pending new mutation controls still need successful execution, including rejection of the wrong Fourier sign. This report neither authorizes a rerun nor claims those pending results. Original control reuse remains limited to its previously accepted scope.

All source identities, raw failed-capture evidence, full independent control output and required reconfirmations appear in the companion JSON.
'''
for name,data in [('drain8178-f1-failure-diagnosis-v1.json',json.dumps(r,indent=2)+'\n'),('drain8178-f1-failure-diagnosis-v1.md',md)]:
 with (R/name).open('x') as f:f.write(data)
 print(identity(name))
