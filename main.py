import random, time
import tabulate

def ssort(L):
    ### selection sort
    if (len(L) == 1):
        return(L)
    else:
        m = L.index(min(L))
        print('selecting minimum %s' % L[m])       
        L[0], L[m] = L[m], L[0]
        print('recursively sorting L=%s\n' % L[1:])
        return [L[0]] + selection_sort(L[1:])
        
def qsort(a, pivot_fn):
   if len(a) <= 1:
        return a
    pivot = pivot_fn(a)
    less = [x for x in a if x < pivot]
    equal = [x for x in a if x == pivot]
    greater = [x for x in a if x > pivot]
    return qsort(less, pivot_fn) + equal + qsort(greater, pivot_fn)
    
def time_search(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds. 
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key 

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000
    ###

def compare_sort(sizes=[100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]):
    """
    Compare the running time of different sorting algorithms.

    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """
    ### TODO - sorting algorithms for comparison
    results = []
    for size in sizes:
        mylist = list(range(size))
        random.shuffle(mylist)

        fixed_pivot_time = time_search(lambda lst: qsort(lst, lambda lst: lst[0]), mylist.copy())
        random_pivot_time = time_search(lambda lst: qsort(lst, lambda lst: random.choice(lst)), mylist.copy())
        tim_sort_time = time_search(sorted, mylist.copy())

        results.append([
            size,
            fixed_pivot_time,
            random_pivot_time,
            tim_sort_time,
        ])
    return results
    ###

def print_results(results):
    """ change as needed for comparisons """
    print(tabulate.tabulate(results,
                            headers=['n', 'qsort-fixed-pivot', 'qsort-random-pivot'],
                            floatfmt=".3f",
                            tablefmt="github"))

def test_print():
    print_results(compare_sort())

random.seed()
test_print()
