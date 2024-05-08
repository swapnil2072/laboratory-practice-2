def printJobScheduling(arr, t):
    n = len(arr)
    arr.sort(key=lambda x: x[2], reverse=True)
    result = [False] * t
    job = ["-1"] * t
    total_profit = 0

    for i in range(n):
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
            if not result[j]:
                result[j] = True
                job[j] = arr[i][0]
                total_profit += arr[i][2]
                break

    print("Scheduled job sequence:", job)
    print("Maximum profit:", total_profit)


if __name__ == "__main__":
    num_jobs = int(input("Enter the number of jobs: "))
    arr = []

    for i in range(num_jobs):
        job_name = input("Enter job name: ")
        deadline = int(input(f"Enter deadline for {job_name}: "))
        profit = int(input(f"Enter profit for {job_name}: "))
        arr.append([job_name, deadline, profit])

    total_slots = int(input("Enter the total number of time slots: "))

    print("Following is the maximum profit sequence of jobs")
    printJobScheduling(arr, total_slots)
