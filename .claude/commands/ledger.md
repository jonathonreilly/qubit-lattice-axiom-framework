# /ledger — Claim Status Lookup

Verify a claim's audit-ratified status before citing it, building on it, or
listing it as a dependency. In-file `Status:` headers, note prose, and session
memory all go stale; `docs/audit/data/audit_ledger.json` on `origin/main` is
the authoritative surface.

## Invocation

```text
/ledger <claim-id | note filename | keyword>
```

## Procedure

1. Best-effort freshness: `git fetch origin main`, then read the ledger from
   `origin/main` rather than the local checkout (a science branch may carry a
   stale ledger):

   ```bash
   git show origin/main:docs/audit/data/audit_ledger.json > /tmp/ledger-main.json
   ```

   Fall back to the local file if offline, and say so.

2. Match rows by claim id or note path:

   ```bash
   python3 - "<query>" <<'PY'
   import json, sys
   q = sys.argv[1].lower()
   rows = json.load(open("/tmp/ledger-main.json"))["rows"]
   hits = {cid: r for cid, r in rows.items()
           if q in cid.lower() or q in (r.get("note_path") or "").lower()}
   for cid, r in sorted(hits.items()):
       print(f"{cid}")
       print(f"  note: {r.get('note_path')}")
       print(f"  claim_type={r.get('claim_type')}  audit_status={r.get('audit_status')}  effective_status={r.get('effective_status')}")
       for d in r.get("deps") or []:
           ds = rows.get(d, {}).get("effective_status", "NOT IN LEDGER")
           print(f"  dep {d}: {ds}")
   PY
   ```

3. Report for each match: `claim_type`, `audit_status`, `effective_status`,
   and every dependency with its `effective_status`. Flag any dependency that
   is not retained-grade.

## Interpretation Rules

- Retained-grade means `effective_status` in
  `{retained, retained_bounded, retained_no_go}`. Nothing else is.
- `unaudited`, `audit_in_progress`, `retained_pending_chain`, `open_gate`,
  and all `audited_*` non-clean statuses are NOT retained-grade and block
  retained-grade claims that depend on them.
- `audited_conditional` with `dependency_not_retained` is normal dependency
  bookkeeping (the downstream landed before its upstream was ratified), not
  a defect in the downstream proof.
- Approved axiom/primitive premise nodes (`minimal_axioms`,
  `scale_reference_primitive`, `kinetic_isotropy_primitive`,
  `realized_state_primitive` per
  `docs/audit/data/axiom_premise_nodes.json`) chain-satisfy dependencies
  without bounding downstream rows. Do not report them as imports or walls.
- A claim absent from the ledger has never been seeded: treat it as a
  proposal at most, regardless of what its note says.

## Rules

- Read-only. Never edit the ledger, queue, or effective-status surfaces — the
  audit lane on `main` is their sole authority.
- Authoring sessions may read `verdict_rationale` to target repairs (the
  physics-loop V1 gate requires quoting it). If you are operating as the
  independent auditor mid-claim, do not use this skill — the audit lane has
  its own clean-context guards.
- When a memory, note header, or PR body disagrees with the ledger, the
  ledger wins. Say so explicitly in your report.
