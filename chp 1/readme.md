# Chapter 1

## fibonacci

### Explaination:
This Python script demonstrates parallel computation of Fibonacci numbers using multiple threads. The `calc_fibonacci(n)` function calculates the Fibonacci number for a given `n` recursively, where the base cases are when `n` equals 0 or 1. The `timed_fibonacci(n, thread_num)` function wraps the Fibonacci calculation to measure and print the time taken for each thread to compute the result. In the main part of the script, a list of threads is created, and nine threads are started to calculate the Fibonacci of 10 concurrently. After launching all threads, the program waits for their completion using `t.join()`. The execution time for each thread is printed, and at the end, the total time for all threads to finish is shown. This approach demonstrates how threading can be used for parallel computation to improve performance when dealing with independent tasks like Fibonacci calculations.
### Output:
![image](images/fibonacci.PNG "image")


## IPC

### Explaination:
This script demonstrates inter-process communication using the `Queue` class from Python's `multiprocessing` module. The `producer` function puts five items (numbers 0-4) into the queue, printing each item as it is produced, and measures its execution time. The `consumer` function retrieves and processes the items from the queue, consuming them one by one, also printing the consumed item and measuring its execution time. In the main section, two separate processes are created: one for producing items (`p1`) and one for consuming them (`p2`). Both processes are started and then joined to ensure that the main program waits for their completion. Execution times for both the producer and consumer are printed after they finish their respective tasks. This script shows how the producer-consumer pattern can be implemented in Python with multiprocessing, helping to understand the coordination of parallel processes using a shared queue.
![image](images/IPC.PNG "image")

## Mpi

### Explaination:
This script demonstrates basic message passing between processes using the `mpi4py` library. It sets up a simple MPI environment where two processes (rank 0 and rank 1) communicate by sending and receiving data. The program begins by checking if the number of processes (`size`) is at least 2, as communication between processes is required. If there are sufficient processes, it records the start time. Process 0 creates a dictionary `data` and sends it to process 1 using the `comm.send()` method. Process 1 then receives the data with `comm.recv()` and prints the received content. Any processes with ranks greater than 1 are idle and print a corresponding message. Finally, the end time is recorded for each process, and the total execution time is printed to show how long the operations took. This example illustrates the use of MPI for communication between processes in a parallel computing environment.
### Output:
![image](images/Mpi.PNG "image")

## Multi_process

### Explaination:
This Python script compares the performance of multiprocessing and multithreading for a task that involves generating random numbers and appending them to a list. The function `do_something` runs a loop, appending random values to `out_list`. The script first uses the `multiprocessing` module to create multiple processes (10 processes, in this case), each executing the `do_something` function. Each process runs in its own memory space, which can lead to performance gains in CPU-bound tasks because each process runs independently on separate CPU cores. After all processes finish, the time taken is printed.

Next, the script resets the job list and switches to using the `threading` module, where it creates 10 threads to perform the same task. Unlike processes, threads share the same memory space, so this method is typically more efficient for I/O-bound tasks but may not perform as well for CPU-bound tasks due to the Global Interpreter Lock (GIL) in Python.

The script compares the execution time for both approaches. Since the task is CPU-bound (involving random number generation), multiprocessing is likely to show better performance than multithreading. The execution time for both methods is measured and printed after all tasks are completed.
### Output:
![image](images/Multi_process.PNG "image")

## Parallelism

### Explaination:
This Python script demonstrates a simple data parallel computation using NumPy for vector addition. The vectors `a` and `b` are randomly initialized with `N` elements (1 million in this case). The computation `c = a + b` performs element-wise addition of the two vectors.

NumPy, which is highly optimized and often leverages parallelism internally (using libraries like BLAS and optimized hardware-specific routines), handles the vector addition. This means you don’t have to manually manage parallelism. The script starts by recording the time before the operation and then stops the timer after the addition. The time taken for the computation is printed, and it also displays the first 10 elements of the resulting vector `c`.

Since NumPy efficiently handles large-scale array operations, this script is expected to run quickly. The execution time will depend on the system's performance, but for such a task, it should be efficient due to NumPy’s internal optimizations.
### Output:
![image](images/Parallelism.PNG "image")

## PCnM

### Explaination:
In this Python script, two separate processes are created using the `multiprocessing` module to compute the square and cube of a given number (`10` in this case). The functions `print_square` and `print_cube` are defined to calculate and print the square and cube of the number, respectively. Each function also measures the execution time for its calculation using `time.time()` to record the start and end time of the operation, then prints the execution time.

The script creates two processes: one for the `print_square` function and another for the `print_cube` function. The processes are started with the `start()` method, and the `join()` method is used to wait for both processes to finish their execution. Once both processes are complete, a message indicating that both processes have finished is printed.

This approach demonstrates how to use multiprocessing to perform independent calculations concurrently. Since both calculations (square and cube) can be done in parallel, using multiple processes can improve execution efficiency, especially for computationally expensive tasks.
### Output:
![image](images/PCnM.PNG "image")

## pipe

### Explaination:
In this script, a parent process and a child process communicate with each other using a `Pipe` from the `multiprocessing` module. The parent process sends a message ("hello from parent") to the child process, and the child process processes this message by converting it to uppercase before sending it back to the parent.

### Breakdown of the script:
1. **Pipe Creation**: The `Pipe()` function creates a communication channel between two processes. It returns two connection objects: `parent_conn` and `child_conn`. The parent process will use `parent_conn` to send data to the child, while the child will use `child_conn` to receive data and send a response back.

2. **Child Process**:
   - The `child_process` function is designed to be executed by the child process. It receives `child_conn` (the child side of the pipe), waits to receive data from the parent using `child_conn.recv()`, processes the received data (converts it to uppercase), and sends the processed result back to the parent using `child_conn.send()`.

3. **Parent Process**:
   - The parent process sends the message `"hello from parent"` using `parent_conn.send()`. After sending the message, it waits for the child process's response using `parent_conn.recv()`. Once the response is received, it prints it.

4. **Process Management**:
   - The child process is started using `p.start()`, and the parent process waits for the child process to complete using `p.join()`.

The script demonstrates inter-process communication using pipes, allowing two processes to send and receive data asynchronously. This setup can be useful in scenarios where processes need to exchange information or coordinate their actions.
### Output:
![image](images/pipe.PNG "image")

## Shared_mem

### Explaination:
This script demonstrates basic multi-threading in Python where multiple threads interact with a shared resource, `balance`. The operations performed are deposit and withdrawal, both of which modify the balance. To ensure that these operations are thread-safe and don't lead to race conditions, a `Lock` is used to synchronize access to the `balance` variable.

### Breakdown of the script:

1. **Shared Resource (`balance`) and Lock**:
   - The `balance` variable is a global variable initialized to 100. It represents the amount of money in an account.
   - A `Lock` named `lock` is created to prevent multiple threads from accessing the `balance` simultaneously, ensuring that the deposit and withdrawal operations happen sequentially, thus avoiding race conditions.

2. **Deposit Function**:
   - The `deposit` function takes an `amount` as an argument and adds it to the global `balance`. 
   - The `with lock:` statement ensures that only one thread at a time can execute the code within the block, which modifies the shared `balance`.

3. **Withdraw Function**:
   - The `withdraw` function takes an `amount` as an argument and subtracts it from the global `balance`.
   - Like the `deposit` function, this operation is protected by the lock to ensure thread-safety.

4. **Thread Creation and Execution**:
   - Two threads are created: `t1` for the `deposit` function and `t2` for the `withdraw` function. Both threads are started using `start()` and then synchronized using `join()` to ensure that the main thread waits for both to finish before continuing.

5. **Measuring Execution Time**:
   - The execution time for both threads to complete is measured using `time.time()`. The difference between the start and end times is printed as the total execution time for the multi-threading operation.

By using a lock, this script ensures that updates to the shared resource (`balance`) are done in a thread-safe manner, preventing the potential problems that could arise from concurrent access.
### Output:
![image](images/Shared_mem.PNG "image")

## Sync

### Explaination:
This script demonstrates the use of a semaphore to control access to a shared resource among multiple threads. A semaphore is a synchronization primitive that limits the number of threads that can access a resource simultaneously. Here, the semaphore is initialized with a value of `2`, meaning that only two threads can access the resource at the same time.

### Breakdown of the script:

1. **Semaphore Initialization**:
   - The semaphore `sem` is created with a value of `2`, indicating that up to two threads can access the shared resource concurrently.

2. **Thread Function (`access_resource`)**:
   - Each thread attempts to acquire the semaphore by calling `sem.acquire()`. If the semaphore's value is greater than 0, the thread proceeds. If it's 0 (i.e., the resource is already being accessed by two threads), the thread will block until the semaphore becomes available.
   - After acquiring the semaphore, the thread simulates accessing the shared resource by printing a message, sleeping for 2 seconds, and then releasing the semaphore using `sem.release()`.
   - The execution time for each thread (time spent accessing the resource) is measured using `time.time()`.

3. **Thread Creation and Execution**:
   - The script creates and starts 5 threads (`Thread-0`, `Thread-1`, etc.). Each thread calls the `access_resource` function, which simulates accessing a shared resource.
   - Since only two threads can access the resource at any given time (due to the semaphore), the remaining threads will have to wait for a slot to become available.

4. **Thread Synchronization (`join`)**:
   - After starting all the threads, the main thread waits for each thread to finish by calling `t.join()` on each one. This ensures that the main thread will only continue after all worker threads have completed their execution.

5. **Execution Time**:
   - The execution time for each thread accessing the resource is printed, showing how long each thread spent while using the semaphore to control its access.

By using the semaphore, the script ensures that no more than two threads can access the shared resource concurrently, providing better control over the resource usage and preventing potential issues from too many threads modifying the resource simultaneously.
### Output:
![image](images/Sync.PNG "image")

## fibonacci

### Explaination:
This Python script demonstrates parallel computation of Fibonacci numbers using multiple threads. The `calc_fibonacci(n)` function calculates the Fibonacci number for a given `n` recursively, where the base cases are when `n` equals 0 or 1. The `timed_fibonacci(n, thread_num)` function wraps the Fibonacci calculation to measure and print the time taken for each thread to compute the result. In the main part of the script, a list of threads is created, and nine threads are started to calculate the Fibonacci of 10 concurrently. After launching all threads, the program waits for their completion using `t.join()`. The execution time for each thread is printed, and at the end, the total time for all threads to finish is shown. This approach demonstrates how threading can be used for parallel computation to improve performance when dealing with independent tasks like Fibonacci calculations.
### Output:
![image](images/fibonacci.PNG "image")

## Task_parallelism

### Explaination:
This script demonstrates the usage of ThreadPoolExecutor from the concurrent.futures module to run tasks concurrently in separate threads, simplifying the process of managing a pool of threads.

Breakdown of the script:
Task Definitions:

Two simple tasks, task_1 and task_2, are defined. Each function prints a message indicating the task has been executed.
Measuring Execution Time:

The script records the start time using time.time() before running the tasks.
Using ThreadPoolExecutor:

A ThreadPoolExecutor is used to manage a pool of threads. The with statement ensures that the executor is properly cleaned up after use.
executor.submit() is used to submit the tasks (task_1 and task_2) to the executor. Each task is scheduled to run in a separate thread. The submit() method returns a Future object that represents the execution of the task.
Execution and Timing:

After the tasks are submitted, the script measures the end time using time.time().
The execution time (from the start to the end of task execution) is printed, showing how long it took to execute both tasks concurrently.
Parallel Execution:

Since ThreadPoolExecutor runs task_1 and task_2 concurrently in separate threads, the execution time is generally shorter than if they were run sequentially (depending on how long the tasks take to execute).
### Output:
![image](images/Task_parallelism.PNG "image")
