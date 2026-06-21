# Opportunity Queue

1. Continue with unaudited rows that name one dedicated verifier but have
   `runner_path: null`.
2. Prefer rows where the existing verifier has a decisive pass/fail summary
   or can be safely upgraded.
3. Avoid multi-runner status pages unless a primary runner is unambiguous.
4. Do not refresh older PR branches onto fast-moving `main`; reviewer lane
   owns updates and cherry-picks.
