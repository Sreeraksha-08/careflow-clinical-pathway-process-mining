import pandas as pd
import pm4py

# Load our simulated hospital events
from sample_event_log import events

df = pd.DataFrame(events)
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Tell PM4Py which columns represent the event log
event_log = pm4py.format_dataframe(
    df,
    case_id="case_id",
    activity_key="activity_name",
    timestamp_key="timestamp",
)

# Discover a process model using the Inductive Miner
process_tree = pm4py.discover_process_tree_inductive(event_log)

print("CareFlow process discovery successful!")
print("\nDiscovered process model:")
print(str(process_tree))
print("\nProcess tree type:", type(process_tree))
print("\nProcess discovery completed successfully!")
print("Process tree:")
print(process_tree)