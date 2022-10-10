def study_schedule(permanence_period, target_time):
    try:
        if target_time is None:
            return None
        return len(
            [
                period
                for period in permanence_period
                if target_time in range(period[0], period[1] + 1)
            ]
        )
    except TypeError:
        return None
