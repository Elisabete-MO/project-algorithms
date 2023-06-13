def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    count = 0

    for start_time, end_time in permanence_period:
        if not isinstance(start_time, int) or not isinstance(end_time, int):
            return None

        if start_time <= target_time <= end_time:
            count += 1

    return count

# if __name__ == "__main__":
    # permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
    # print(study_schedule(permanence_period, 5)) #saída: 3
    # print(study_schedule(permanence_period, 4)) #saída: 3
    # print(study_schedule(permanence_period, 3)) #saída: 2
    # print(study_schedule(permanence_period, 2)) #saída: 4
    # print(study_schedule(permanence_period, 1)) #saída: 2
