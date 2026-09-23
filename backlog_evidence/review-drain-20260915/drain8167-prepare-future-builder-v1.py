from pathlib import Path
import json,hashlib,ast
R=Path('/private/tmp/review-drain-20260915');W=R/'review-meta-slot';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();ref=lambda p:dict(path=str(p),sha256=sha(p))
review=json.loads((R/'drain8167-original-review.json').read_text())
refs=[ref(R/x) for x in ['drain8167-original-review.json','drain8167-original-review.md','drain8167-author-prepared-v1.json','drain8167-prepared-v1-source-freeze.json','drain8167-author-preservation-v1.json','drain8167-author-full-mapping-v1.json','drain8167-author-input-resource-plan-v1.json','drain8167-author-correction-v1.diff','drain8167-author-discovery-v1.json','drain8167-capture-plan-v1.json',*review['bound_artifacts']]]
authority=['docs/MINIMAL_AXIOMS_2026-06-29.md','docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md','docs/audit/data/axiom_premise_nodes.json','docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md','docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md','docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md']
p=R/'drain8167-future-authority-bindings-v1.json';assert not p.exists();p.write_text(json.dumps([dict(path=x,sha256=sha(W/x)) for x in authority],indent=2)+'\n');refs.append(ref(p))
s=(R/'drain8165-build-staged-draft-v1.py').read_text().replace('PR8165','PR8167').replace('drain8165','drain8167').replace("W=R/'author-draft-slot'","W=R/'review-meta-slot'").replace("R/'author-draft-slot.json'","R/'review-meta-slot.json'")
start=s.index('IMMUTABLE_REFS = ');end=s.index('\nfailure=',start);s=s[:start]+'IMMUTABLE_REFS = '+repr(refs)+s[end:]
s=s.replace("ap.add_argument('--version',required=True);args=ap.parse_args()","ap.add_argument('--version',required=True);ap.add_argument('--confirmation',required=True);ap.add_argument('--confirmation-sha256',required=True);args=ap.parse_args()")
s=s.replace('assert len(frozen)==74','assert len(frozen)==68').replace("confirmation=R/'drain8167-early-affected-review-v1.json'",'''confirmation=Path(args.confirmation)
    assert confirmation.is_relative_to(R) and not confirmation.is_relative_to(W) and not confirmation.is_symlink()
    assert re.fullmatch('[0-9a-f]{64}',args.confirmation_sha256) and sha(confirmation)==args.confirmation_sha256
    confirmation_data=json.loads(confirmation.read_text())
    assert confirmation_data.get('reviewer_session')=='/root/review_8167'
    assert 'b1249f0427dc7e1a8523775fd6341a2a7bbb7b007b373f19af7296d63b8aa597' in json.dumps(confirmation_data), 'Report does not bind frozen prepared-v1'
    assert str(confirmation_data.get('verdict','')).startswith('PASS'), 'Clean affected-source confirmation required'
    assert not confirmation_data.get('findings'), 'Unresolved findings require new preparation, never edit frozen-v1'
''')
s=s.replace("original['original_inventory']","original['original_dispositions']").replace('==len(mapped)==88','==len(mapped)==116').replace("deps=paths[:i]","deps=[]").replace("assert {p for p in cites if p.startswith('docs/COMPACT_ROTOR_')}==set(deps)","assert cites==['docs/work_history/repo/review_feedback/pr8167-evidence/README.md']")
s=s.replace("dependency_rationale='Self-contained supplied compact rotor model and complete sampled-event proof; no current-main scientific parent.' if i==0 else 'Complete linked in-unit mathematical parents, including full compact path specification for the coarse-current result. PR8164 is context only, not a dependency.'","dependency_rationale='Complete self-contained positive proof for the supplied rotor/source/state. No external current-main science parent or unlanded PR8165/8166 theorem is imported. Historical recovery is context only.'")
s=s.replace("assert len({n['primary_runner'] for n in notes})==3","assert len({n['primary_runner'] for n in notes})==2")
s=s.replace("ast.literal_eval(declarations['AUDIT_MEMORY_MB'])==512","ast.literal_eval(declarations['AUDIT_MEMORY_MB'])==768")
a=s.index('    claims=[dict(');b=s.index("    refs=IMMUTABLE_REFS+",a)
s=s[:a]+'''    claims=d['claim_dispositions']
    assert len(claims)==5 and claims[-1]['disposition'].startswith('Deferred')
'''+s[b:]
s=s.replace("refs=IMMUTABLE_REFS+[ref(outputs['cache-api'])]","refs=IMMUTABLE_REFS+[ref(confirmation),ref(outputs['cache-api'])]")
s=s.replace("mathematical_closure='Four complete in-unit claims, acyclic sampled -> excursion -> path law -> coarse currents. No external current-main science parent. Framework authorities are context only; supplied model not inferred from them.'","mathematical_closure='Two full self-contained positive arguments: exact compact-cover/source identities, and compact sine MGF/static exact-curl conditional Gaussian proof. Sparse-law construction and universal negative implication deferred in exact historical recovery. No false sibling theorem dependency. Framework authorities are context only.'")
s=s.replace("runtime_scope='Three unique programs, one shared primary; own source and literal proof input reads distinguished from mathematical dependency edges.'","runtime_scope='Two unique programs, no helper/sibling invocation; own source and own-note reads distinguished from mathematical closure. Sparse-law runner remains historical only.'")
s=s.replace("session='/root/review_8165;", "session='/root/review_8167;")
s=s.replace("rationale='Exact historical original/provisional proof, scope or review record. All current scientific proof bodies are preserved completely in four canonical claims; no autonomous historical claim/status adopted.'","rationale='Exact historical proof or review record. Two current positive arguments are complete in canonical claims. The entire sparse construction and its negative implication are deferred scientific recovery, not a live claim, not discarded, and not mathematically refuted; preserve original branch.'")
s=s.replace("No science, gates, registry mutations, commits or pushes.","No science, gates, registry mutations, commits or pushes. Requires separately supplied clean original-reviewer affected report pinned by SHA; corrections invalidate this v1 builder.")
assert '8165' not in s.replace('PR8165/8166','')
builder=R/'drain8167-build-staged-draft-v1.py';assert not builder.exists();compile(s,str(builder),'exec');builder.write_text(s)
print(json.dumps(dict(builder=ref(builder),capture_plan=ref(R/'drain8167-capture-plan-v1.json'),status='SYNTAX CHECKED ONLY; BUILDER NOT EXECUTED',requires='--expected-base current-main --stage-authorized --version fresh-vN --confirmation absolute-clean-original-reviewer-report --confirmation-sha256 exact-report-hash'),indent=2))
