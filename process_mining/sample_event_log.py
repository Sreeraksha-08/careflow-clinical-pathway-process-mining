import pandas as pd

# Simulated hospital activity data
events = [
    {
        "case_id": "C001",
        "activity_name": "Registration",
        "timestamp": "2026-10-10 09:00:00",
        "resource": "Reception Staff",
        "department": "Reception",
        "age_group": "Adult",
    },
    {
        "case_id": "C001",
        "activity_name": "Initial Assessment",
        "timestamp": "2026-10-10 09:20:00",
        "resource": "Triage Nurse",
        "department": "Triage",
        "age_group": "Adult",
    },
    {
        "case_id": "C001",
        "activity_name": "Doctor Consultation",
        "timestamp": "2026-10-10 10:00:00",
        "resource": "Doctor",
        "department": "Emergency",
        "age_group": "Adult",
    },
    {
        "case_id": "C002",
        "activity_name": "Registration",
        "timestamp": "2026-10-10 09:10:00",
        "resource": "Reception Staff",
        "department": "Reception",
        "age_group": "Child",
    },
    {
        "case_id": "C002",
        "activity_name": "Initial Assessment",
        "timestamp": "2026-10-10 09:35:00",
        "resource": "Triage Nurse",
        "department": "Triage",
        "age_group": "Child",
    },
]

df = pd.DataFrame(events)
df["timestamp"] = pd.to_datetime(df["timestamp"])

print("CareFlow sample event log")
print(df.to_string(index=False))
print("\nTotal events:", len(df))
print("Unique cases:", df["case_id"].nunique())