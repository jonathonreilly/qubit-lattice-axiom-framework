# Supplement reproduction

The unchanged author additions and all their runtime dependencies are retained in integration_snapshot. These scientific programs are portable with the complete evidence directory:

    PYTHONDONTWRITEBYTECODE=1 python3 -B supplement_controls_v1.py
    PYTHONDONTWRITEBYTECODE=1 python3 -B integration_snapshot/check_mode_trace_root_v1.py
    PYTHONDONTWRITEBYTECODE=1 python3 -B integration_snapshot/check_mode_joint_gain_v1.py

Use a fresh 120-second external timeout for each. The original bounded execution, full stdout/stderr and source bindings are retained in supplement_attempt01.run.json and the two author replay records. The one-shot capture/replay script run_integration_replays_v1.py requires the original campaign pack and refuses to overwrite integration_snapshot; it is not needed for the portable scientific replays.

REPRODUCE_v1.md covers the earlier six programs. Existing result files are evidence and should not be overwritten.

