import heapq

class Job:
    def __init__(self, job_Number, job_name, submitter_name, submission_date, priority):
        self.job_Number = job_Number
        self.job_name = job_name
        self.submitter_name = submitter_name
        self.submission_date = submission_date
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

class PRIORITYQUEUE:
    def __init__(self):
        self.wait_queue = []
        self.ready_queue = []

    def insert_job(self, job):
        heapq.heappush(self.wait_queue, job)

    def update_priority(self, job_Number, new_priority):
        pass

    def delete_job(self, job_Number):
        pass

    def move_highest_priority_to_ready_queue(self):
        pass

    def display_wait_queue(self):
        pass

    def display_ready_queue(self):
        pass

Priority_Queue = PRIORITYQUEUE()

job01 = Job(1, "Job1", "Submitter1", "Date1", 10)
Priority_Queue.insert_job(job01)

Priority_Queue.display_wait_queue()

heapq.heapify(Priority_Queue.wait_queue)

for _ in range(5):
    Priority_Queue.move_highest_priority_to_ready_queue()

Priority_Queue.display_wait_queue()
Priority_Queue.display_ready_queue()

Priority_Queue.delete_job(job_Number)

Priority_Queue.display_ready_queue()

job02 = Job(2, "Job2", "Submitter2", "Date2", 15)
Priority_Queue.insert_job(job02)

for _ in range(4):
    Priority_Queue.move_highest_priority_to_ready_queue()

Priority_Queue.delete_job(job_Number)

Priority_Queue.display_wait_queue()
Priority_Queue.display_ready_queue()

Priority_Queue.update_priority(job_Number, new_priority)

while Priority_Queue.wait_queue:
    Priority_Queue.move_highest_priority_to_ready_queue()
while Priority_Queue.ready_queue:
    Priority_Queue.delete_job(job_Number)
