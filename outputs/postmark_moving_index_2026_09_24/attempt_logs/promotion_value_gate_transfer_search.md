# Transfer milestone source and PR search

**Search revision:** `origin/main` at
`0e6ad8285096ed668816f18caaa6fbbfbd9c50e8` (fetched 2026-09-24).
**Parent review head:** `c734332ca227c4371f3c188f96227c494b43f533`.

## Exact source searches

```bash
git grep -n -i -E 'adiabatic.{0,40}(five.site|Bragg|transfer)|((five.site|Bragg|transfer).{0,40}adiabatic)|simple Bragg crossing|central Bragg contact|moving.frame product|homological change' origin/main -- 'docs/POSTMARK_ELECTRIC*' 'scripts/postmark_electric*'
git grep -n -i -E 'adiabatic.{0,40}(five.site|Bragg|transfer)|((five.site|Bragg|transfer).{0,40}adiabatic)|simple Bragg crossing|central Bragg contact|moving.frame product|homological change' origin/physics-loop/postmark-electric-weighted-phase-20260924 -- 'docs/POSTMARK_ELECTRIC*' 'scripts/postmark_electric*'
```

Both commands returned no matching source lines. The parent branch does have
the five-site frozen-band correction and explicitly leaves global transport
open; that is the closest match, not a transport theorem.

## Pull-request family search

```bash
gh pr list --state all --limit 100 --json number,title,headRefName,baseRefName,url,isDraft | jq '[.[] | select(.headRefName|test("postmark-(electric-)?(phase-correlation|quantization-phase|weighted-phase|moving-index)"))]'
```

The query returns #9091 (`physics-loop/postmark-electric-weighted-phase-20260924`,
non-draft, based on the #9078 branch) and #9078
(`physics-loop/postmark-moving-index-central-match-20260924`, non-draft, based
on `main`). It finds no existing phase-correlation or quantization-phase PR.
Neither existing PR contains the four proposed transfer-product theorems.

This search supports a novelty judgment only; it is not an independent review
or an audit decision.
