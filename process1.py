class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0
        self.response_time = 0

class Scheduler:
    def __init__(self, processes):
        self.processes = processes

    def fcfs_scheduling(self):
        current_time = 0
        for process in self.processes:
            process.waiting_time = max(0, current_time - process.arrival_time)
            process.turnaround_time = process.waiting_time + process.burst_time
            process.response_time = process.waiting_time
            current_time += process.burst_time

    def sjn_scheduling(self):
        processes = sorted(self.processes, key=lambda x: (x.arrival_time, x.burst_time))
        current_time = 0
        ready_queue = []
        while processes or ready_queue:
            while processes and processes[0].arrival_time <= current_time:
                ready_queue.append(processes.pop(0))
            ready_queue.sort(key=lambda x: x.burst_time)
            if ready_queue:
                process = ready_queue.pop(0)
                process.waiting_time = max(0, current_time - process.arrival_time)
                process.turnaround_time = process.waiting_time + process.burst_time
                process.response_time = process.waiting_time
                current_time += process.burst_time
            else:
                current_time += 1

    def round_robin_scheduling(self, time_quantum):
        queue = []
        processes = self.processes.copy()
        current_time = 0
        while processes or queue:
            while processes and processes[0].arrival_time <= current_time:
                queue.append(processes.pop(0))
            if queue:
                process = queue.pop(0)
                if process.burst_time > time_quantum:
                    process.burst_time -= time_quantum
                    current_time += time_quantum
                    queue.append(process)
                else:
                    current_time += process.burst_time
                    process.burst_time = 0
                process.waiting_time = current_time - process.arrival_time - process.burst_time
                process.turnaround_time = current_time - process.arrival_time
                process.response_time = process.waiting_time
            else:
                current_time += 1
# Define processes
processes = [
    Process(1, 0, 8),
    Process(2, 1, 4),
    Process(3, 2, 9),
    Process(4, 3, 5)
]

def print_processes(processes):
    print("PID\tArrival\tBurst\tWaiting\tTurnaround\tResponse")
    for p in processes:
        print(f"{p.pid}\t{p.arrival_time}\t{p.burst_time}\t{p.waiting_time}\t\t{p.turnaround_time}\t\t{p.response_time}")


# Create Scheduler object
scheduler = Scheduler(processes)

# FCFS Scheduling
scheduler.fcfs_scheduling()
print("FCFS Scheduling:")
print_processes(processes)

# SJN Scheduling
scheduler = Scheduler(processes)
scheduler.sjn_scheduling()
print("SJN Scheduling:")
print_processes(processes)

# Round Robin Scheduling
scheduler = Scheduler(processes)
time_quantum = 4
scheduler.round_robin_scheduling(time_quantum)
print("Round Robin Scheduling:")
print_processes(processes)
