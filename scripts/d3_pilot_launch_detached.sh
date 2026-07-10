#!/bin/zsh
# Detached launcher for the d3 registration pilot full run.
# Survives SSH disconnect, terminal/agent exit, and idle sleep:
#   - nohup + orphaning (parent exits immediately -> child re-parents
#     to launchd, immune to SIGHUP)
#   - caffeinate -is holds off idle/system sleep while the run lives
#   - the runner checkpoints every 10 steps and auto-resumes from the
#     newest checkpoint, so even a hard interruption only pauses it;
#     rerunning this script continues where it stopped.
# Logs/checkpoints: logs/runner-cache/d3_pilot_checkpoints/
set -u
REPO="/Users/jonBridger/tp-matter-mass-wep"
LOGDIR="$REPO/logs/runner-cache/d3_pilot_checkpoints"
mkdir -p "$LOGDIR"
nohup sh -c "cd '$REPO' && exec caffeinate -is python3 scripts/d3_registration_onset_pilot_2026_07_09.py --full >> '$LOGDIR/full_run_stdout.log' 2>> '$LOGDIR/full_run_progress.log'" >/dev/null 2>&1 &
LAUNCHED=$!
disown $LAUNCHED 2>/dev/null || true
echo "detached pilot run launched (initial pid $LAUNCHED; child re-parents to launchd)"
echo "progress: tail -f $LOGDIR/full_run_progress.log"
