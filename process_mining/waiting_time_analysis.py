import pandas as pd

# Load the simulated event log
from sample_event_log import events

df = pd.DataFrame(events)
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Sort activities in the order they occurred
df = df.sort_values(["case_id", "timestamp"])

# Find the previous activity time for each case
df["previous_timestamp"] = df.groupby("case_id")["timestamp"].shift(1)

# Calculate time between consecutive activities
df["waiting_minutes"] = (
	df["timestamp"] - df["previous_timestamp"]
).dt.total_seconds() / 60

print("CareFlow Waiting Time Analysis")
print(
	df[
		[
			"case_id",
			"activity_name",
			"previous_timestamp",
			"timestamp",
			"waiting_minutes",
		]
	].to_string(index=False)
)

print("\nAverage time between consecutive activities:")
print(df.groupby("activity_name")["waiting_minutes"].mean())
# Save the analysis results
df.to_csv("process_mining/waiting_time_results.csv", index=False)
print("\nWaiting-time results saved successfully!")