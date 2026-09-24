# Airy turning-point current-main source search

base: 0e6ad8285096ed668816f18caaa6fbbfbd9c50e8

## matching document titles

$ git ls-tree -r --name-only origin/main -- docs

exit: 1
```text
(no matches)
```

## focused transfer/turning text search

$ git grep -n -i -E five.site.{0,80}transfer|transfer.{0,80}five.site|moving.cell.{0,80}transfer|turning.point.{0,80}transfer|Airy origin/main -- docs/POSTMARK_ELECTRIC*

exit: 1
```text
(no matches)
```

## Airy/turning-point text search

$ git grep -n -i -E Airy|turning.point origin/main -- docs/POSTMARK_ELECTRIC*

exit: 1
```text
(no matches)
```

## Search-quality note

An earlier broad numeric regex matched `1800` inside an unrelated coefficient. The focused title, Airy/turning, and five-site/moving-cell transfer searches above return no relevant match; that numeric hit is excluded as a false positive.

## Candidate note identity

93b7e366491ea4d92027d683e85e776fd7f0d8b287148ee2000cb6b817bd8799  docs/POSTMARK_ELECTRIC_SIMPLE_TURNING_POINT_AIRY_SCALE_TRANSFER_BOUNDED_THEOREM_NOTE_2026-09-24.md
