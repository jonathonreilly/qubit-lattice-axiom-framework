#!/usr/bin/env zsh
set -u

ROOT="/private/tmp/yt-primitive-physical-source-theorem-20260526"
LOOP="$ROOT/.claude/science/physics-loops/yt-positive-closure-12h-20260527"
PROMPT="$LOOP/RUN_PROMPT.md"
LOG="$LOOP/supervisor.log"
LAST="$LOOP/last-message.md"
POSITIVE="$LOOP/POSITIVE_CLOSURE"
START_EPOCH="$(date +%s)"
END_EPOCH="$(( START_EPOCH + 43200 ))"
CYCLE=1

mkdir -p "$LOOP"
echo "supervisor_start=$(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$LOG"

while [ "$(date +%s)" -lt "$END_EPOCH" ]; do
  if [ -f "$POSITIVE" ]; then
    echo "positive_closure_marker_seen=$(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$LOG"
    exit 0
  fi

  echo "" >> "$LOG"
  echo "cycle=$CYCLE start=$(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$LOG"
  REMAINING="$(( END_EPOCH - $(date +%s) ))"

  (
    cd "$ROOT"
    "$HOME/.local/bin/codex" exec \
      --cd "$ROOT" \
      --dangerously-bypass-approvals-and-sandbox \
      --output-last-message "$LAST" \
      - <<EOF
$(cat "$PROMPT")

Supervisor cycle: $CYCLE
Approximate remaining campaign seconds: $REMAINING

Continue from current branch state. If the prior cycle left a handoff, read it
and keep going. Do not stop the whole campaign after a no-go; commit/push the
science block and pivot to the next ranked route unless positive closure is
actually achieved.
EOF
  ) >> "$LOG" 2>&1
  STATUS="$?"
  echo "cycle=$CYCLE exit_status=$STATUS end=$(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$LOG"

  if [ -f "$POSITIVE" ]; then
    echo "positive_closure_marker_seen=$(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$LOG"
    exit 0
  fi

  CYCLE="$(( CYCLE + 1 ))"
  sleep 30
done

echo "supervisor_end=time_budget_exhausted $(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$LOG"
exit 0
