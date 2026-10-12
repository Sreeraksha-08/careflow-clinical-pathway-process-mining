import pandas as pd


def test_waiting_time_calculation():
    """Check time intervals between consecutive clinical events."""

    data = {
        "case_id": ["C001", "C001", "C001"],
        "activity_name": [
            "Registration",
            "Initial Assessment",
            "Doctor Consultation",
        ],
        "timestamp": [
            "2026-10-01 09:00:00",
            "2026-10-01 09:20:00",
            "2026-10-01 10:00:00",
        ],
    }

    df = pd.DataFrame(data)
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    df["waiting_minutes"] = (
        df.groupby("case_id")["timestamp"]
        .diff()
        .dt.total_seconds()
        .div(60)
    )

    assert pd.isna(df.loc[0, "waiting_minutes"])
    assert df.loc[1, "waiting_minutes"] == 20
    assert df.loc[2, "waiting_minutes"] == 40

    print("Waiting-time calculation test passed!")


if __name__ == "__main__":
    test_waiting_time_calculation()