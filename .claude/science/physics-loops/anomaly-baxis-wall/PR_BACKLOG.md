# PR_BACKLOG — anomaly-abj-bridge

**Reason PRs not opened live:** GitHub auth unavailable this run (`gh auth status`
fails; `git push` → could not read Username). Per physics-loop SKILL.md this is a
delivery degradation, not a science stop. Work committed to local stacked block
branches; batch-deliver when auth is restored (`gh auth login`). Do NOT merge.

Stacked chain: block01←main? (block01 based on main) then block02←block01,
block03←block02, block04←block03.

```bash
cd "/Users/jonBridger/tp-audit-bridge-20260620"

# block01 (base: main)
git push -u origin physics-loop/anomaly-abj-bridge-block01-20260620
gh pr create --base main --head physics-loop/anomaly-abj-bridge-block01-20260620 \
  --title "[physics-loop] anomaly-abj-bridge block01: per-edge fresh attempts + 3 bankable arithmetic cores (no crack, 222 PASS)" \
  --body "See docs/ANOMALY_FORCES_TIME_ABJ_FRESH_ATTEMPTS_STRETCH_NOTE_2026-06-20.md + commit 19e5288d8."

# block02 (base: block01)
git push -u origin physics-loop/anomaly-abj-bridge-block02-20260620
gh pr create --base physics-loop/anomaly-abj-bridge-block01-20260620 --head physics-loop/anomaly-abj-bridge-block02-20260620 \
  --title "[physics-loop] anomaly-abj-bridge block02: exercise on 3 walls + decisive verification (P-REC partial unlock; P-COMP/P-ABJ sharpened no-gos)" \
  --body "See docs/ANOMALY_FORCES_TIME_ABJ_EXERCISE_VERIFICATION_NOTE_2026-06-20.md + commit 236962136."

# block03 (base: block02)
git push -u origin physics-loop/anomaly-abj-bridge-block03-20260620
gh pr create --base physics-loop/anomaly-abj-bridge-block02-20260620 --head physics-loop/anomaly-abj-bridge-block03-20260620 \
  --title "[physics-loop] anomaly-abj-bridge block03: bank 3 deps-all-retained cores + unified hybrid obstruction note (PASS=94)" \
  --body "Bank notes ABJ_{PHY,PCOMP,PREC}_*_CORE_DEPS_RETAINED_BOUNDED_THEOREM_NOTE_2026-06-20.md + unified note + commit ecf89aa07."

# block04 (base: block03)
git push -u origin physics-loop/anomaly-abj-bridge-block04-20260620
gh pr create --base physics-loop/anomaly-abj-bridge-block03-20260620 --head physics-loop/anomaly-abj-bridge-block04-20260620 \
  --title "[physics-loop] anomaly-abj-bridge block04: owner/audit-lane decision packet (A-I) + campaign handoff" \
  --body-file docs/ANOMALY_FORCES_TIME_ABJ_OWNER_DECISION_PACKET_2026-06-20.md
```
