#!/bin/zsh
# Detached launcher for the d3 bar-window full measurement.
# Survives SSH disconnect, terminal/agent exit, and idle sleep:
#   - nohup + orphaning (parent exits immediately -> child re-parents
#     to launchd, immune to SIGHUP)
#   - caffeinate -is holds off idle/system sleep while the run lives
#   - the runner checkpoints every 10 steps and auto-resumes from the
#     newest checkpoint, so a hard interruption only pauses it;
#     rerunning this script continues where it stopped.
#   - the runner's own preflight gate refuses to start (exit 2) if
#     measured gather timings project past 13.5 h or RSS past 8 GiB.
# Logs/checkpoints: logs/runner-cache/d3_bar_window_checkpoints/
set -u
REPO="/Users/jonBridger/tp-matter-mass-wep"
LOGDIR="$REPO/logs/runner-cache/d3_bar_window_checkpoints"
mkdir -p "$LOGDIR"
nohup sh -c "cd '$REPO' && exec caffeinate -is python3 scripts/d3_bar_window_measurement_2026_07_11.py --full >> '$LOGDIR/full_run_stdout.log' 2>> '$LOGDIR/full_run_progress.log'" >/dev/null 2>&1 &
LAUNCHED=$!
disown $LAUNCHED 2>/dev/null || true
echo "detached bar-window run launched (initial pid $LAUNCHED; child re-parents to launchd)"
echo "progress: tail -f $LOGDIR/full_run_progress.log"
