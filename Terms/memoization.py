import time

start_time = time.time()

func_cache = {}

def expensive_func(num):
    if num in func_cache: #O(1) lookup if input has been calculated before
        return func_cache[num]
    print('Computing {}...'.format(num))
    time.sleep(1) #artificial computing time
    result = num * num
    func_cache[num] = result #add result to cache so we get O(1) complexity if we see this input again
    return result


print(expensive_func(4))

print(expensive_func(10))

print(expensive_func(4))

print(expensive_func(10))

print('--- {:.02f} seconds ---'.format(time.time() - start_time))

#testing commit