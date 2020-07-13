import asyncio, time


tic = time.perf_counter()

#defining a co routine
async def coroutine_1():
    print('Coroutine 1 is active on the Event Loop')

    print('Coroutine 1 yielding control, going to be blocked for 4 seconds')
    await asyncio.sleep(4) #simulating a block, could be an HTTP request, DB query, etc.

    print('Coroutine 1 resumed, exiting now.')


async def coroutine_2():
    print('Coroutine 2 is active on the Event Loop')

    print('Coroutine 2 is yielding control, going to be blocked for 5 seconds.')
    await asyncio.sleep(5)

    print('Coroutine 2 resumed, exiting now.')

#Defining the Event Loop
loop = asyncio.get_event_loop()

#Scheduling both routines to run on the event loop
loop.run_until_complete(asyncio.gather(coroutine_1(), coroutine_2()))

toc = time.perf_counter()

print(f'Total time elapsed is {toc - tic:.04f} seconds')






