# Artifact plan

1. Add an explicit load-bearing derivation certificate to the canonical parent
   note.
2. Preserve the paired runner unchanged so its previously audited hash and
   cached `PASS=11 FAIL=0` surface remain comparable.
3. Refresh the existing meta companion's parent-note hash pin and cached log;
   do not change the scientific runner.
4. Run the paired runner, vocabulary lint, diff checks, and repo-native
   review-loop.
5. Do not edit auditor-owned ledger or publication-effective-status files.
