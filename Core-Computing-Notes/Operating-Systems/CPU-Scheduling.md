# CPU Scheduling

## 1. Purpose
CPU scheduling selects a ready process/thread to execute. Goals may include high throughput, low waiting/turnaround/response time, and fairness.

## 2. Metrics
- Turnaround time = completion time − arrival time.
- Waiting time = turnaround time − CPU burst time for a simple single-burst model.
- Response time = first CPU start − arrival time.

## 3. Algorithms
- FCFS: first come, first served; simple but may cause convoy effect.
- SJF: shortest job first; optimal average waiting time under ideal assumptions when burst lengths are known.
- SRTF: preemptive shortest remaining time.
- Priority: highest-priority ready job; starvation may occur.
- Round Robin: each ready process receives a time quantum.

## 4. Preemption
A preemptive scheduler may interrupt a running process. A non-preemptive scheduler lets it continue until it blocks or finishes.

## 5. Exercises
For a given arrival/burst table, draw Gantt charts for FCFS and Round Robin, then calculate waiting and turnaround times. State tie-breaking assumptions.
