# Chapter 5

## concurrent_futures_pooling

### Explaination:
This code compares the performance of sequential execution, thread pool execution, and process pool execution using the `concurrent.futures` module. It defines a `count` function, which performs a CPU-intensive operation (an empty loop) for each item in a list, and an `evaluate` function that calls `count` and prints the result. First, the tasks are executed sequentially by iterating through the list. Next, a `ThreadPoolExecutor` is used to run the tasks concurrently in multiple threads, and a `ProcessPoolExecutor` is employed to run them in multiple processes. The execution time for each method is measured and printed, highlighting the speed differences between sequential, threaded, and multiprocessing approaches.

### Output:
![Ergonomic](images/concurrent_futures_pooling.PNG "Ergonomic ")


## coroutine

### Explaination:
This code simulates a Finite State Machine (FSM) using Python's `asyncio` library with coroutines to handle state transitions asynchronously. It defines five asynchronous functions (`start_state`, `state1`, `state2`, `state3`, and `end_state`), where each function represents a state in the FSM. When `start_state` is called, it randomly decides whether to transition to `state1` or `state2`. Each state function generates an output message and randomly decides the next state based on the transition value (0 or 1), eventually leading to the `end_state` where the process halts. The `time.sleep(1)` calls simulate time delays, but they should ideally be replaced with `await asyncio.sleep(1)` to avoid blocking the event loop, allowing other tasks to run concurrently. The `asyncio.get_event_loop()` is used to run the FSM starting from the `start_state` and orchestrates the state transitions.

### Output:
![Ergonomic](images/coroutine.PNG "Ergonomic ")

## dealing

### Explaination:
This script demonstrates using `asyncio` with `Future` objects to run two asynchronous tasks concurrently. The `first_coroutine` computes the sum of the first `num` integers, while the `second_coroutine` calculates the factorial of `num`. The script takes two command-line arguments (`num1` and `num2`) which are passed to the coroutines. Each coroutine uses `await asyncio.sleep()` to simulate a time delay and makes the computation non-blocking. The results of the computations are set into `Future` objects (`future1` and `future2`). After the coroutines are executed, `add_done_callback` is used to invoke `got_result`, which prints the result from the `Future`. The `asyncio.get_event_loop()` manages the event loop, and `loop.run_until_complete()` ensures both tasks run concurrently. The script terminates once both tasks are complete and the results are printed.

### Output:
![Ergonomic](images/dealing.PNG "Ergonomic ")

## event_loops

### Explaination:
This script demonstrates a sequence of asynchronous tasks scheduled using `asyncio`. Three tasks (`task_A`, `task_B`, and `task_C`) are defined, each with varying sleep durations that simulate unpredictable work. The tasks are triggered in a cyclic manner with `loop.call_later()`, meaning that each task schedules the next task to run after a delay of 1 second. The tasks use `time.sleep()` to simulate blocking behavior, but `loop.call_later()` schedules subsequent tasks based on the time available before reaching `end_time`, which is 60 seconds from the current time. If the loop's time exceeds the `end_time`, the loop is stopped. The tasks will continue to cycle through until the time limit is reached. The program runs until the loop is stopped after 60 seconds.

### Output:
![Ergonomic](images/event_loops.PNG "Ergonomic ")

## manipulating_task

### Explaination:
This script uses `asyncio` to run two asynchronous tasks concurrently: `factorial()` and `fibonacci()`. The `factorial()` function computes the factorial of a given number, and `fibonacci()` calculates Fibonacci numbers up to a specified index. Both functions use `await asyncio.sleep(1)` to simulate delays, making them non-blocking and allowing for asynchronous execution. In the main part of the script, the event loop is created using `asyncio.get_event_loop()`, and the tasks are added to the event loop with `loop.create_task()`. `loop.run_until_complete(asyncio.wait(task_list))` is used to run all tasks concurrently. The event loop continues executing until all tasks are complete, and then it is closed.

### Output:
![Ergonomic](images/manipulating_task.PNG "Ergonomic ")
