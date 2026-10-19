# careflow-clinical-pathway-process-mining
CareFlow: Clinical Pathway Process Mining
# Bottleneck Analysis

CareFlow analyzes simulated clinical event logs to identify activities associated with longer intervals between consecutive events.

# Objectives

- Calculate time intervals between consecutive clinical events.
- Summarize intervals by activity.
- Identify activities with the longest observed intervals.
- Support investigation of potential workflow bottlenecks.

# Current Status

The process-mining module includes process discovery, waiting-time analysis, and a test for interval calculations.

# Limitations

The current dataset is simulated and small. These intervals represent time differences between consecutive recorded events and should not be interpreted as verified patient waiting times or real hospital performance.