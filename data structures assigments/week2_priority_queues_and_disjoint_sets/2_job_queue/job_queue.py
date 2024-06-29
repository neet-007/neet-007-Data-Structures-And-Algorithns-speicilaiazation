# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

class HeapItem:
    def __init__(self, index, time):
        self.index = index
        self.time = time

class MinHeap():
    def __init__(self, size) -> None:
        self.arr = [HeapItem(index=i, time=0) for i in range(size)]
        self.size = size - 1

    def get_parent(self, i):
        return (i - 1) // 2

    def get_left_child(self, i):
        return (i * 2) + 1

    def get_rigth_child(self, i):
        return (i * 2) + 2

    def shift_up(self, i):
        curr = i
        parent_idx = self.get_parent(curr)
        while curr > 0 and self.arr[curr].time <= self.arr[parent_idx].time:
            if self.arr[curr].time == self.arr[parent_idx]:
                if self.arr[curr].index < self.arr[parent_idx].index:
                    self.arr[parent_idx], self.arr[curr] = self.arr[curr], self.arr[parent_idx]
            else:
                self.arr[curr], self.arr[parent_idx] = self.arr[parent_idx], self.arr[curr]
            curr = parent_idx
            parent_idx = self.get_parent(curr)

        return

    def shift_down(self, i):
        curr = i
        while curr < self.size:
            min_index = curr
            left_child = self.get_left_child(curr)

            if left_child <= self.size and self.arr[left_child].time <= self.arr[min_index].time:
                if self.arr[left_child].time == self.arr[min_index].time:
                    if self.arr[left_child].index < self.arr[min_index].index:
                        min_index = left_child
                else:
                    min_index = left_child

            rigth_child = self.get_rigth_child(curr)

            if rigth_child <= self.size and self.arr[rigth_child].time <= self.arr[min_index].time:
                if self.arr[rigth_child].time == self.arr[min_index].time:
                    if self.arr[rigth_child].index < self.arr[min_index].index:
                        min_index = rigth_child
                else:
                    min_index = rigth_child

            if min_index != curr:
                self.arr[min_index], self.arr[curr] = self.arr[curr], self.arr[min_index]
                curr = min_index
            else:
                break

        return

    def get_min(self, job_time):
        self.arr[0].time += job_time
        return_value = self.arr[0]
        self.shift_down(0)
        return return_value

def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    heap = MinHeap(n_workers)
    results = []
    for job in jobs:
        val = heap.get_min(job)
        results.append(AssignedJob(val.index, val.time - job))
    return results
    """
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result
    """


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
