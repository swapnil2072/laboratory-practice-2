class JobScheduling:
    def __init__(self):
        self.jobs = []

    def add_job(self, job_id, deadline, duration):
        self.jobs.append((job_id, deadline, duration))

    def schedule_jobs(self):
        # Sort jobs based on deadlines in ascending order
        sorted_jobs = sorted(self.jobs, key=lambda x: x[1])

        n = len(sorted_jobs)
        scheduled_jobs = []
        time_slots = [False] * n

        for i in range(n):
            for j in range(min(n, sorted_jobs[i][1]) - 1, -1, -1):
                if not time_slots[j]:
                    scheduled_jobs.append(sorted_jobs[i][0])
                    time_slots[j] = True
                    break

        return scheduled_jobs

    def display_schedule(self, scheduled_jobs):
        print("Scheduled Jobs:", scheduled_jobs)


def main():
    job_scheduling = JobScheduling()

    while True:
        print("----------------Job Scheduling----------------------")
        print("1. Add Job.")
        print("2. Schedule Jobs (Earliest Deadline First).")
        print("3. Exit.")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            job_id = input("Enter the job ID: ")
            deadline = int(input("Enter the job deadline: "))
            duration = int(input("Enter the job duration: "))
            job_scheduling.add_job(job_id, deadline, duration)
            print("Job added:", (job_id, deadline, duration))

        elif choice == 2:
            scheduled_jobs = job_scheduling.schedule_jobs()
            job_scheduling.display_schedule(scheduled_jobs)

        elif choice == 3:
            print("End of the program")
            break

        else:
            print("Invalid choice!")

        print()


if __name__ == "__main__":
    main()
