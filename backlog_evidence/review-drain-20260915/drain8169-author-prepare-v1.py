from pathlib import Path
import ast,copy,difflib,hashlib,json,subprocess,shutil
R=Path('/private/tmp/review-drain-20260915');W=R/'author-draft-slot';P=R/'drain8169-originals/head';sha=lambda b:hashlib.sha256(b).hexdigest();pin=lambda p:dict(path=p,sha256=sha((W/p).read_bytes()))
assert json.loads((R/'author-draft-slot.json').read_text())['owner']=='PR8169-author'
assert subprocess.check_output(['git','-C',str(W),'rev-parse','HEAD'],text=True).strip()=='ed129b572ea8364ed8d2792a0860b07ab94056a5'
inv=json.loads((R/'drain8169-inventory.json').read_text());assert len(inv['files'])==8
archive=W/'docs/work_history/repo/review_feedback/pr8169-evidence';archive.mkdir(parents=True);kept=archive/'kept';kept.mkdir();entries=[]
for e in inv['files']:
 raw=(P/e['path']).read_bytes();assert sha(raw)==e['head_sha256'];mode,_,blob=e['head'].split('\t')[0].split();assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==blob
 target=kept/(Path(e['path']).stem+'-'+blob[:16]+Path(e['path']).suffix);target.write_bytes(raw);target.chmod(0o755 if mode=='100755' else 0o644)
 entries.append(dict(original_path=e['path'],original_mode=mode,git_blob=blob,raw_sha256=sha(raw),encoding='identity',stored_path=str(target.relative_to(archive)),stored_sha256=sha(raw)))
manifest=dict(schema_version=1,revision=inv['head'],entries=entries);(archive/'archive-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
name='FRAME_ATTACHED_MENU_EXCHANGE_COVARIANT_PROBABILITIES_BOUNDED_THEOREM_NOTE_2026-09-16.md';runner='frame_attached_menu_exchange_probabilities_2026_09_16';parent='POSSIBILITY_COVARIANCE_SOLDERED_VS_UNSOLDERED_CL30_INVARIANT_RULES_AND_HAAR_FAIR_COIN_BOUNDED_THEOREM_NOTE_2026-09-14.md';orderparent='SUPPLIED_RECORD_LAWS_AND_COMMON_ORDER_KERNELS_BOUNDED_THEOREM_NOTE_2026-09-15.md'
note='''---
claim_id: frame_attached_menu_exchange_covariant_probabilities_bounded_theorem_note_2026-09-16
claim_type: bounded_theorem
claim_scope: "Conditional normalized probabilities on a supplied four-point sphere menu, under independent internal rotations and exchangeable cubic slots; exact Gibbs, linear and normalized-overlap identities."
upstream_dependencies: [minimal_axioms, possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14]
runner: scripts/frame_attached_menu_exchange_probabilities_2026_09_16.py
---

# Exchange-covariant probabilities on a frame-attached four-point menu

**Type:** bounded_theorem

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Result and supplied premises

For noncollinear unit vectors q,q' and t=q·q', the allowed menu is
S(q,q')={q,q',-q,-q'}. For a fixed two-slot occupancy stratum, independent
internal SO(3) covariance together with exchange of the two occupied cubic
slots gives masses (α(t),α(t),γ(t),γ(t)), where α,γ≥0 and 2α+2γ=1.
The menu has four points; the probability support has four only if both
α and γ are positive. Boundary choices have two nonzero atoms.

The [current axiom memo](MINIMAL_AXIOMS_2026-06-29.md) supplies the finite
support meaning: nonzero-probability possibilities. It does not select the
sphere, covariance action, menu, weights, formation order or stochastic
product model used here. The [conditional covariance parent](PARENT_NAME)
supplies the direct product of proper cubic slot permutations and independent
internal SO(3), as a mathematical representation. This note works in that
supplied representation, not every interpretation of the full M_2(C) domain.
No registered primitive supplies these probability choices.

## 1. Menu covariance and the one-record boundary

For every rotation R, S(Rq,Rq')=R S(q,q'). The four points are distinct
exactly when |t|<1. If q'=q or q'=-q, the set collapses to {q,-q}; the
four-distinct formulas below are stated only on -1<t<1.

For a single record q, a finite SO(2)-invariant probability support lies
inside {q,-q}. Indeed, rotations fixing q sweep every other sphere point
through an infinite circle. A finite invariant support cannot contain such
an orbit. Conversely a δ_q+(1-a)δ_-q is covariant for every a∈[0,1]. Its
support is a singleton at a=0 or a=1, and the pair only for 0<a<1.
This is a complete finite-support statement; it does not require both
antipodes to have nonzero mass.

## 2. Ordered covariance versus occupied-slot exchange

For an ordered noncollinear pair, the internal SO(3) stabilizer is trivial:
a rotation fixing both vectors fixes their cross product and therefore an
oriented basis. Two ordered pairs with the same t are related by a unique
proper rotation, obtained by matching their oriented orthonormal frames.
Thus internal covariance alone permits any four nonnegative functions
w_1(t),...,w_4(t) summing to one, attached respectively to q,q',-q,-q'.
For example (1/2,1/4,1/8,1/8) defines such an internally covariant law.
It is not symmetric under exchanging the two records.

Now include the two occupied spatial slots in the input. For opposite
slots (+x,-x), rotation by π about y exchanges them. For adjacent slots
(+x,+y), rotation by π about the x+y axis exchanges them. These are proper
cubic rotations; every two-slot pair is cubic-equivalent to one of these
cases. Opposite and adjacent occupancy strata are distinct and may have
different functions α and γ. No equality across these strata is asserted.
There is no external slot label distinguishing the two occupied positions.

The internal bisector rotation B, of angle π about (q+q')/|q+q'|, exchanges
q and q'. It does NOT stabilize the ordered record pair by itself.
Combine it with the independent cubic slot exchange: each original slot
then receives its original record, so the complete input is fixed. The
output transforms by B, forcing the q and q' masses to agree and likewise
the -q and -q' masses. This proves necessity of (α,α,γ,γ).
Conversely, these equalities, dependence only on t within the occupancy
stratum, and normalization give covariance under all the declared actions.
Equivalently this is the internally covariant classification of an unordered
record pair. A π rotation about q at t=0 relates the different inputs
(q,q') and (q,-q'); it does not force α(0)=γ(0).

## 3. Pair-Gibbs and the full valid linear parametrization

For finite real β, the supplied pair-Gibbs formula on S is

    p(s)=exp[β s·(q+q')]/[2exp(β(1+t))+2exp(-β(1+t))],
    α(t)/γ(t)=exp[2β(1+t)].

At t=0 and B=exp(2β)=2, α=1/3 and γ=1/6; B=1 gives α=γ=1/4.
The runner's rational B formula is explicitly restricted to t=0. At finite
β all four masses are positive. At fixed -1<t<1, β→+∞ or -∞ gives the
uniform distribution on the two copy or two flip atoms, respectively.
These are not deterministic single-record choices.

A general member of the exchange family has the equivalent form

    p(s)=[1+λ(t) s·(q+q')]/4,
    α(t)=[1+λ(t)(1+t)]/4, γ(t)=[1-λ(t)(1+t)]/4,
    λ(t)=[4α(t)-1]/(1+t), |λ(t)|(1+t)≤1, -1<t<1.

Antipodal cancellation makes the four weights sum to one. The displayed
inequality is exactly their nonnegativity condition. This is a function
λ(t), potentially different in the two occupancy strata; a fixed constant
λ is only a subfamily on a domain where its bound holds. For a constant
valid on all -1<t<1, |λ|≤1/2 suffices and is necessary. At t=0, λ=0 is
uniform, while λ=±1 gives the two-copy or two-flip boundary law. At t=3/5,
λ=1 would give γ=-3/20 and is excluded. The parameterization retains all
zero-mass boundary cases rather than silently assuming four-point support.

## 4. Raw overlap and normalized menu identities

For any unit reference a, antipodal cancellation gives

    sum_(s in S) (1+s·a)/2=2.

For a=q the raw weights in menu order are

    (1,(1+t)/2,0,(1-t)/2).

They are raw overlap values, not normalized four-menu probabilities. After
dividing by two they define the normalized internally covariant law

    (1/2,(1+t)/4,0,(1-t)/4).

It depends on q' through both its atom locations and t. No violation of the
Admissibility variation sentence follows from the absence of q' as a literal
symbol in the overlap formula. Under the separately imposed occupied-slot
exchange this normalized law generally differs from its swapped-input law;
it is an ordered-reference comparison, not an exchange-family member.
On {q,-q} the original two-outcome law is (1,0).

With a=(q+q')/sqrt(2+2t), the raw four-menu sum is again two. Dividing by
two gives the symmetric linear family with λ(t)=1/sqrt(2+2t), whose bound
is sqrt((1+t)/2)≤1. This is a normalized four-menu comparison, not a
claim that a physical Born rule or a replacement Hamiltonian was selected.

## 5. Scope, preserved process argument and evidence

The complete corrected endpoint-event argument for the supplied three-site
sequential process is preserved readably in
`work_history/repo/review_feedback/pr8169-evidence/DEFERRED_CORRECTED_ENDPOINT_PROOF.md`.
It distinguishes actual joint endpoint laws using |L·R|<1, rather than
conditional menus at an endpoint profile unreachable in chain order. The
argument is preserved as deferred scientific source; no universal negative
process conclusion is asserted as part of this live bounded row. Formal
negative certification is not supplied by changing its label. The exact
original erroneous argument is separately retained, never overwritten.

The current supplied-record/common-kernel note is relevant comparison
context, not a parent of the menu theorem:
`SUPPLIED_RECORD_LAWS_AND_COMMON_ORDER_KERNELS_BOUNDED_THEOREM_NOTE_2026-09-15.md`.
Its common-kernel and all-order hypotheses remain conditional. No conclusion
about physical formation or all framework laws is imported.

Primary runner: `scripts/frame_attached_menu_exchange_probabilities_2026_09_16.py`.
Exact rational finite controls cover the reference pair, all 24 proper cubic
rotations, both occupied-slot exchange strata, support boundaries, parameter
bounds, normalized overlaps and a finite endpoint-event analogue. They are
not numerical execution of Haar almost-sure or infinite-system statements.
TOTAL counts actual check calls, including explicitly identified input checks.
The original 120-second timeout is retained; a 256 MiB external process-tree
cap is proposed for small exact rational arrays and standard-library overhead.
JSON diagnostics go to `logs/runner-cache/`. No capture has yet been made.

[Exact eight-path original recovery](work_history/repo/review_feedback/pr8169-evidence/README.md)
preserves original modes, blobs, hashes, the 21-check historical cache, all
original route text and the topology manifest as history only. The original
branch remains a recovery handle for deferred negative certification.

## No-Go Discipline Gate

N1: The four actual original routes are preserved with corrected dispositions
in the deferred proof. No fifth route or formal negative PASS is invented.
N2: The supplied covariance, finite-support and product-process assumptions
are not declared independent walls; no nonimplication witnesses were proved.
N3: Slot exchange, nonnegative weights, unordered/ordered inputs, fixed
occupancy stratum and independent Haar roots are explicit where used.
N4: The covariance parent supplies an action, not weights or physical
formation. The common-kernel result is context only; no open sibling is an
authority or a required runner string.
N5: Five stdout lines name finite element/site/mode/block checks and the
unexecuted lattice-wide class. A finite six-axis control is labelled as such.
N6: No primitive, reading, menu, weighting, physical order or Gibbs rule is
selected by these conditional identities.
N7: Ordered unequal weights, singleton support and direction-sensitive
process hypotheses are substantive alternative inputs; the argument must
retain its precise exchange and sequential assumptions.
N8: The read covariance parent distinguishes supplied actions from physical
selection; the current common-kernel theorem distinguishes joint equality
from null-profile cancellation. These scope corrections are retained.
'''.replace('PARENT_NAME',parent)
(W/'docs'/name).write_text(note)
deferred='''# Corrected endpoint-event proof — deferred scientific source

This is a newly corrected full argument, not the exact original source.
The exact original note remains byte-for-byte in `kept/`. This proof has not
yet received affected-source confirmation or formal negative certification.
It is preserved for review and recovery, not asserted by the live menu row.

## Supplied process and measurable separator

Take X=S² with Haar probability π, a supplied sequential product of local
records-only conditional kernels on a three-site path L–M–R, and independent
empty-neighbour draws. For every recorded q, the one-neighbour kernel in
any relevant slot is supported on a nonempty subset of {q,-q}. Zero weights
and singleton supports are allowed. The two-neighbour kernel may be any
normalized kernel, including four-menu boundary laws. These are process
premises, not a process or probability supplied by the framework axioms.

In chain order L,M,R, M is ±L almost surely, and R is ±M almost surely.
Therefore R=±L almost surely, even if sign probabilities depend on records
or slots. For the Borel endpoint event E={|L·R|<1}, P_chain(E)=0.

In ends-first order L,R,M, L and R are independent Haar sphere draws. For
each fixed L, the set {L,-L} consists of two points and has Haar area zero.
For example z=L·R has uniform density 1/2 on [-1,1]; the two caps
|z|>1-ε have probability ε, tending to zero. Fubini gives
P_ends-first(E)=1. Integrating the final normalized middle kernel leaves
this endpoint marginal unchanged. Thus these two supplied joint measures
are different. This establishes the conditional process separator without
conditioning on a profile that chain order cannot reach.

The menu comparison remains a separate finite illustration: for L=e_z,
R=e_x, the one-record allowed menu has two points and the two-record menu
has four; for collinear ends the latter collapses to two. These menu counts
are not support counts when weights vanish and are not the joint-law proof.
The same reasoning does not identify a physical formation order, exclude
all stochastic laws or assert a framework-wide impossibility theorem.

## Relation to current common-kernel context

`docs/SUPPLIED_RECORD_LAWS_AND_COMMON_ORDER_KERNELS_BOUNDED_THEOREM_NOTE_2026-09-15.md`
proves, for its supplied standard-Borel common-slot-kernel model, that
all-order equality implies reversibility from two sites and K²=Π from path
endpoint marginals; selfadjointness then gives K=Π almost everywhere. It
never cancels null conditional profiles. The direct sphere-axis proof above
needs no import of that theorem and does not require equality of slot kernels.
The common-kernel hypothesis cannot be discarded in other applications.

## Four original routes and corrected dispositions

1. ATTEMPTED: divide the raw overlap menu by two. This gives a normalized
   internally SO(3)-covariant ordered-reference law, depending on q' through
   atoms and t. It is generally not exchange-symmetric. The original blanket
   variation-clause violation is withdrawn; no replacement negative follows.
2. ATTEMPTED: use the normalized bisector reference. Its raw sum is two;
   after division by two it belongs to the valid symmetric linear family
   with λ(t)=1/sqrt(2+2t). It is a supplied normalized menu comparison.
3. ATTEMPTED: force endpoint collinearity. The menu collapses to two, but
   this changes the independent Haar root premise; it is not the ends-first
   joint law above. No impossible conditioning is canceled.
4. OPEN / OUTSIDE THE DECLARED FINITE-SUPPORT CLASS: replace finite supports
   by continuum kernels. Such a route is not ruled out here. The common-kernel
   context states its separate hypotheses and surviving direction-sensitive
   alternatives. It does not supply a fifth failed route.

Formal negative-packet certification remains deferred: these are four actual
routes, not five, and their assumptions have no proved independence relation.
The procedural limitation does not make the corrected measure argument false.
Keep the complete proof and original branch recoverable for further review.
'''
(archive/'DEFERRED_CORRECTED_ENDPOINT_PROOF.md').write_text(deferred)
oldnote=next(P.glob('docs/ADMISSIBILITY_RULE_FRAME_ATTACHED*'));oldrunner=next(P.glob('scripts/admissibility_rule_frame_attached*.py'));original=oldrunner.read_text();a=ast.parse(original)
keep=['normalize','dot','add','scale','neg','apply_matrix','proper_cubic_rotations','four_point_support','distinct_four','linear_copy_mass']
functions='\n\n'.join(ast.get_source_segment(original,n) for n in a.body if isinstance(n,ast.FunctionDef) and n.name in keep)
inputs=['docs/'+name,'docs/MINIMAL_AXIOMS_2026-06-29.md','docs/'+parent];hashes={p:sha((W/p).read_bytes()) for p in inputs}
source='''#!/usr/bin/env python3
"""Exact finite menu/exchange probability checks; no physical-law selection.
Corrected endpoint controls are finite analogues, not numerical Haar proofs.
"""
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path
import hashlib, json
AUDIT_TIMEOUT_SEC=120
AUDIT_MEMORY_MB=256
AUDIT_INPUT_PATHS=INPUTS
EXPECTED_INPUT_SHA256=HASHES
ROOT=Path(__file__).resolve().parents[1]
'''.replace('INPUTS',repr(inputs)).replace('HASHES',repr(hashes))+'\n\n'+functions+'''


def gibbs_copy_mass_at_orthogonal(B):
    """B=exp(2 beta)>0, t=0 only; no silent discarded t argument."""
    if B <= 0:
        raise ValueError("B must be positive")
    return B/(2*B+2)


def main():
    results=[]
    def check(label, condition, detail):
        ok=bool(condition)
        results.append(dict(label=label,passed=ok,detail=detail))
        print(("PASS" if ok else "FAIL")+": "+label+" "+detail)
    for path in AUDIT_INPUT_PATHS:
        check("input-sha:"+path,hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==EXPECTED_INPUT_SHA256[path],"Actual source/parent bytes")
    q=(Fraction(0),Fraction(0),Fraction(1));qp=(Fraction(1),Fraction(0),Fraction(0))
    rotations=proper_cubic_rotations()
    check("orthogonal-menu",dot(q,qp)==0 and distinct_four(q,qp),"Four allowed points, not assumed positive support")
    swap=lambda v:(v[2],-v[1],v[0])
    check("bisector-swap",swap(q)==qp and swap(qp)==q,"Internal rotation exchanges ordered records")
    flip=lambda v:(-v[0],-v[1],v[2])
    check("different-input",flip(q)==q and flip(qp)==neg(qp),"This relates distinct inputs; no forced alpha=gamma")
    check("cubic-group",len(rotations)==len(set(rotations))==24,"Original full proper cubic group")
    check("menu-covariance",all(set(four_point_support(apply_matrix(M,q),apply_matrix(M,qp)))=={apply_matrix(M,s) for s in four_point_support(q,qp)} for M in rotations),"All 24 finite group controls; general SO(3) proof is analytic")
    slots=((Fraction(1),Fraction(0),Fraction(0)),(Fraction(0),Fraction(1),Fraction(0)))
    for label,b in (("adjacent",slots[1]),("opposite",neg(slots[0]))):
        check("slot-exchange:"+label,any(apply_matrix(M,slots[0])==b and apply_matrix(M,b)==slots[0] for M in rotations),"Proper cubic slot exchange exists in this occupancy stratum")
    weights=(Fraction(1,2),Fraction(1,4),Fraction(1,8),Fraction(1,8))
    law=lambda x,y,w:dict(zip(four_point_support(x,y),w))
    check("ordered-unequal-covariance",all({apply_matrix(M,s):v for s,v in law(q,qp,weights).items()}==law(apply_matrix(M,q),apply_matrix(M,qp),weights) for M in rotations),"Unequal masses retain internal covariance")
    check("ordered-exchange-distinction",law(q,qp,weights)!=law(qp,q,weights),"Exchange is an additional hypothesis")
    samples=((Fraction(1,4),Fraction(1,4)),(Fraction(1,2),Fraction(0)),(Fraction(0),Fraction(1,2)),(Fraction(3,8),Fraction(1,8)))
    check("exchange-family",all(2*a+2*g==1 and a>=0 and g>=0 and law(q,qp,(a,a,g,g))==law(qp,q,(a,a,g,g)) for a,g in samples),"Original four pairs, including zero weights")
    check("invalid-family",2*Fraction(1,3)+2*Fraction(1,3)!=1,"Original normalization countercontrol")
    check("support-not-menu",[sum(v>0 for v in (a,a,g,g)) for a,g in samples]==[4,2,2,4],"Support counts use nonzero masses")
    check("singleton-one-record",len({q:Fraction(1)})==1 and all({apply_matrix(M,q):Fraction(1)}=={apply_matrix(M,q):Fraction(1)} for M in rotations),"delta_q is a normalized covariant singleton; covariance also follows from pushforward")
    check("gibbs-B2",gibbs_copy_mass_at_orthogonal(Fraction(2))==Fraction(1,3),"B=2,t=0: alpha=1/3,gamma=1/6")
    check("gibbs-B1",gibbs_copy_mass_at_orthogonal(Fraction(1))==Fraction(1,4),"B=1 gives uniform masses")
    check("original-linear-fixtures",[linear_copy_mass(l,Fraction(0)) for l in (Fraction(0),Fraction(1),Fraction(-1),Fraction(1,2))]==[Fraction(1,4),Fraction(1,2),Fraction(0),Fraction(3,8)],"Original lambda values at t=0 retained")
    for t in (Fraction(-3,5),Fraction(0),Fraction(3,5)):
        r=(Fraction(4,5),Fraction(0),t) if t else qp
        for lam in (Fraction(0),1/(1+t),-1/(1+t)):
            vals=[(1+lam*dot(s,add(q,r)))/4 for s in four_point_support(q,r)]
            check("linear-bound:"+str((t,lam)),sum(vals)==1 and min(vals)>=0,"Exact valid lambda(t) boundary and interior")
        for alpha in (Fraction(0),Fraction(1,8),Fraction(1,2)):
            lam=(4*alpha-1)/(1+t)
            check("lambda-inverse:"+str((t,alpha)),linear_copy_mass(lam,t)==alpha and abs(lam)*(1+t)<=1,"Function parameterization, not a fixed universal lambda")
        raw=tuple((1+dot(s,q))/2 for s in four_point_support(q,r));norm=tuple(v/2 for v in raw)
        check("overlap-normalization:"+str(t),sum(raw)==2 and sum(norm)==1 and min(norm)>=0,"Raw sum2, normalized ordered-reference law")
    check("excluded-lambda",Fraction(1,2)-linear_copy_mass(Fraction(1),Fraction(3,5))==Fraction(-3,20),"lambda=1 at t=3/5 violates nonnegativity")
    normalized=lambda x,y:law(x,y,tuple((1+dot(s,x))/4 for s in four_point_support(x,y)))
    check("normalized-exchange",normalized(q,qp)!=normalized(qp,q),"Exchange failure, not blanket framework variation failure")
    r=(Fraction(4,5),Fraction(0),Fraction(3,5))
    check("second-record-dependence",normalized(q,qp)!=normalized(q,r),"Moving atoms and t change the normalized law")
    check("collinear-menu",len(set(four_point_support(q,q)))==2,"Original collinear menu control")
    check("chain-endpoint-event",all(abs(dot(q,scale(a*b,q)))==1 for a,b in product((-1,1),repeat=2)),"Every one-record sign path is collinear, including singleton choices")
    axes=tuple(scale(sign,e) for e in (q,qp,(Fraction(0),Fraction(1),Fraction(0))) for sign in (-1,1))
    check("independent-endpoint-analogue",sum(abs(dot(l,r))<1 for l,r in product(axes,repeat=2))==24,"Finite six-axis analogue:24/36; Haar probability1 is analytic, not this finite test")
    failed=sum(not r['passed'] for r in results);passed=len(results)-failed
    output=ROOT/'logs'/'runner-cache'/(Path(__file__).stem+'.json');output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),input_sha256=EXPECTED_INPUT_SHA256,checks=results,passed=passed,failed=failed),indent=2)+"\\n")
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    print("per_element: exact menu atoms, scalar probabilities, support and parameter-bound checks.")
    print("per_site: one-record singleton/pair cases and both adjacent/opposite occupied-slot strata.")
    print("per_mode: checked and not executed — no physical spectrum or dynamical modes are defined.")
    print("per_block: 24 cubic rotations, rational parameter fixtures, four chain sign paths and 36 six-axis endpoint pairs.")
    print("lattice_wide: checked and not executed — Haar measure and general process statements require analytic proofs; no infinite lattice is simulated.")
    return int(failed>0)


if __name__=='__main__':
    raise SystemExit(main())
'''
compile(source,runner,'exec');(W/'scripts'/(runner+'.py')).write_text(source)
# Preserve every unaffected original mathematical helper exactly; report the deliberate repairs.
b=ast.parse(source);newf={n.name:n for n in b.body if isinstance(n,ast.FunctionDef)}
for n in a.body:
 if isinstance(n,ast.FunctionDef) and n.name in keep:assert ast.dump(n,include_attributes=False)==ast.dump(newf[n.name],include_attributes=False)
(archive/'README.md').write_text('# Exact original recovery and corrected deferred proof\n\nAll eight original paths at `7e268bd96edda8819250318a3cbdaa1b20e90f35` are stored byte-for-byte with distinct modes, blobs and SHA-256 hashes in archive-manifest.json. Original note, runner, route records, cache and topology manifest remain readable. The topology/cache are history, not current authority or evidence.\n\nDEFERRED_CORRECTED_ENDPOINT_PROOF.md is a separately authored correction, not the exact original. It preserves the complete valid conditional endpoint-event argument and four actual route dispositions while formal negative certification remains deferred. No fifth route or unsupported independence assertion is manufactured. Preserve the original branch recovery handle while that conclusion is unlanded.\n\nThe live menu theorem retains the complete corrected positive symmetry, normalization, Gibbs/linear and overlap arguments. No erroneous source is silently replaced in historical recovery.\n')
mapping=[]
for e in entries:
 final='docs/'+name if e['original_path']==str(oldnote.relative_to(P)) else ('scripts/'+runner+'.py' if e['original_path']==str(oldrunner.relative_to(P)) else None)
 mapping.append(dict(original_path=e['original_path'],original_mode=e['original_mode'],original_blob=e['git_blob'],original_sha256=e['raw_sha256'],recovery=str((archive/e['stored_path']).relative_to(W)),recovery_encoding='identity',disposition='Corrected complete positive source; original exact recovery and corrected negative proof separately deferred' if final else 'Exact historical provenance; no old cache/status/topology authority imported',final_path=final,final_sha256=sha((W/final).read_bytes()) if final else None))
diff=''.join(difflib.unified_diff(oldnote.read_text().splitlines(True),note.splitlines(True),fromfile=str(oldnote.relative_to(P)),tofile='docs/'+name))+''.join(difflib.unified_diff(original.splitlines(True),source.splitlines(True),fromfile=str(oldrunner.relative_to(P)),tofile='scripts/'+runner+'.py'))
(R/'drain8169-author-correction-v1.diff').write_text(diff)
for key,obj in [('full-mapping',mapping),('preservation',dict(unchanged_original_helper_ASTs=keep,deliberate_math_repairs=['F1 full slot/internal exchange stabilizer','F2 support nonzero subset','F3 lambda(t) domain and explicitly orthogonal Gibbs function','F4 complete joint endpoint-event proof in deferred recovery plus finite analogue','F5 normalized overlap dependence/exchange distinction','F6 four original routes and withdrawn independence assertion','F7 remove stale text checks and false menu cardinality evidence; add decisive controls'],independent_confirmation='Required; original reviewer check8169 controls already inform repairs, no self certification')) ,('input-resource-plan',dict(runner=pin('scripts/'+runner+'.py'),ordered_inputs=[pin(x) for x in inputs],context_only=pin('docs/'+orderparent),timeout_sec=120,proposed_external_process_tree_limit_bytes=256*1024**2,source_basis='24 small 3x3 rational matrices, finite four-atom menus and36endpoint pairs, standard-library JSON/hash overhead; no numerical array package or scaling lattice',json_output='logs/runner-cache/'+runner+'.json',execution='not run',mutation_plan='Original reviewer to prescribe/confirm decisive final-source controls; no mutation or primary executed during preparation'))]:
 (R/('drain8169-author-'+key+'-v1.json')).write_text(json.dumps(obj,indent=2)+'\n')
prepared=dict(status='PROVISIONAL_UNTRACKED_PREPARED_V1_REQUIRES_INDEPENDENT_AFFECTED_REVIEW',owner='PR8169-author',base='ed129b572ea8364ed8d2792a0860b07ab94056a5',original_head=inv['head'],original_merge_base=inv['merge_base'],notes=[pin('docs/'+name)],runners=[pin('scripts/'+runner+'.py')],deferred_corrected_proof=pin(str((archive/'DEFERRED_CORRECTED_ENDPOINT_PROOF.md').relative_to(W))),archive_manifest=pin(str((archive/'archive-manifest.json').relative_to(W))),original_report=dict(path=str(R/'drain8169-review-original.json'),sha256=sha((R/'drain8169-review-original.json').read_bytes())),claim_disposition='Live corrected positive menu classification/identities; full corrected conditional joint-law separator preserved as deferred scientific proof; no formal negative PASS',originals=8,primary_executions=0,staged=False)
(R/'drain8169-author-prepared-v1.json').write_text(json.dumps(prepared,indent=2)+'\n')
print(json.dumps(dict(status=prepared['status'],originals=8)))
