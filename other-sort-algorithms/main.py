
from random_generator import RandomGenerator # pylint: disable=import-error
from quick_sort import QuickSort # pylint: disable=import-error
from insertion_sort import InsertionSort # pylint: disable=import-error
from heapsort import HeapSort # pylint: disable=import-error


if __name__ == '__main__':

    gen = RandomGenerator(count=1000, lower=0, upper=10000)
    gen.generate('other-sort-algorithms/output/numbers.txt')

    nums = gen.read_numbers('other-sort-algorithms/output/numbers.txt')

    qs = QuickSort()
    sorted_qs, time_qs, steps_qs = qs.measure(nums)
    gen.write_numbers('other-sort-algorithms/output/quicksort_output.txt', sorted_qs)
    print(f"QuickSort: time={time_qs:.6f}s, steps={steps_qs}")

    ins = InsertionSort()
    sorted_ins, time_ins, steps_ins = ins.measure(nums)
    gen.write_numbers('other-sort-algorithms/output/insertion_output.txt', sorted_ins)
    print(f"InsertionSort: time={time_ins:.6f}s, steps={steps_ins}")

    hs = HeapSort()
    sorted_hs, time_hs, steps_hs = hs.measure(nums)
    gen.write_numbers('other-sort-algorithms/output/heapsort_output.txt', sorted_hs)
    print(f"HeapSort: time={time_hs:.6f}s, steps={steps_hs}")
