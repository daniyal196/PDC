# Chapter 3

## Communication with pipe
### Explanation:
in this code their are two functions, first function takes a pipe and fills it with 0-9 numbers,second funtion takes two pipes, it takes input from first pipe and squares them and sends it second pipe as output pipe
in last main function 2 pipes and 2 process are made first pipe and process call the first function and second pipe and process call second function and both unused ends of pipes are closed and then pipes the output pipe values are printed

### Output
![Communication with pipe](images/CommunicationWithPipe.PNG "image1")

## Communication with queue
### Explanation:
In this code, there are two classes and a main function. The first class, `producer`, inherits from `multiprocessing.Process`. It takes a queue as input and appends 10 random integers (between 0 and 256) to the queue. Each addition is printed along with the queue size, and it sleeps for 1 second after each operation. 

The second class, `consumer`, also inherits from `multiprocessing.Process`. It takes the same queue as input and continuously removes and prints items from the queue until the queue is empty. It checks if the queue is empty and breaks the loop if true, sleeping for 1 second between operations.

In the main function, a shared multiprocessing queue is created. Two processes, `process_producer` and `process_consumer`, are created from the `producer` and `consumer` classes, respectively. Both processes are started and joined, ensuring they complete their tasks before the program ends.

### Output
![Communication with pipe](images/communicating_with_queue.PNG "image1")

## derom
### Explanation:
In this code there is one function foo and a main function. The foo function is executed by each process and behaves differently based on the process name. The foo function first retrieves the current process name. If the process name is background_process it prints numbers from 0 to 4 with a 1-second delay between prints. If the process name is non_background_process it prints numbers from 5 to 8 with a 1-second delay. The function announces when the process starts and ends. In the main function two processes are created background_process with the name 'background_process' set as a daemon process and non_background_process with the name 'non_background_process' set as a non-daemon process. Both processes are started. The non-background process continues to run independently until completion while the background process runs briefly and terminates when the main program ends due to its daemon nature. A delay time.sleep(2) is added to allow the daemon process to execute briefly before the program exits.
### Output
![Communication with pipe](images/derom.PNG "image1")


## killing_processes
### Explanation:
In this code there is a function foo and a main function. The foo function prints a starting message and then iterates through numbers 0 to 9 printing each number with a 1-second delay between iterations. It ends with a finished message. In the main function a process p is created with the target function foo. The state of the process is printed before starting it. The process is started and its running state is printed. The process is then terminated and its state is printed again. After termination the process is joined and its state is printed once more. Finally the process's exit code is printed to indicate its termination status.
### Output
![Communication with pipe](images/killing_processes.PNG "image1")


## naming_processes
### Explanation:
In this code there is a function myFunc and a main function. The myFunc function retrieves the name of the current process and prints a starting message with the process name. It then sleeps for 3 seconds before printing an exiting message with the process name. In the main function two processes are created. The first process, process_with_name, is explicitly given the name 'myFunc process' and targets the myFunc function. The second process, process_with_default_name, uses the default naming scheme and also targets the myFunc function. Both processes are started, and the program waits for each process to complete using the join method.
### Output
![Communication with pipe](images/naming_processes.PNG "image1")


## process_in_subclass
### Explanation:
In this code there is a class MyProcess and a main function. The MyProcess class inherits from multiprocessing.Process and overrides the run method. The run method prints a message indicating it has been called along with the name of the process. In the main function a loop runs 10 times. In each iteration a new process is created using the MyProcess class. The process is started which triggers the run method and then the program waits for the process to complete using the join method.
### Output
![Communication with pipe](images/process_in_subclass.PNG "image1")


## process_pool
### Explanation:
In this code there is a function function_square and a main function. The function_square function takes a single input value, squares it, and returns the result. In the main function a list of numbers from 0 to 99 is created and a multiprocessing pool with 4 worker processes is initialized. The pool.map method is used to apply the function_square function to each value in the list, distributing the work across the worker processes. After mapping the tasks the pool is closed to prevent new tasks from being submitted and the program waits for all worker processes to complete using the join method. Finally the squared results are printed as a list.
### Output
![Communication with pipe](images/process_pool.PNG "image1")


## processes_barrier
### Explanation:
In this code there are two functions, test_with_barrier and test_without_barrier, along with a main function. The test_with_barrier function takes a Barrier and a Lock as arguments. It retrieves the current process name, waits for all processes sharing the barrier to reach the same point using synchronizer.wait(), and then retrieves the current time. Using the Lock to ensure serialized access, it prints the process name along with the current time. The test_without_barrier function does not use a barrier or lock. It retrieves the current process name and immediately prints the name and the current time.

In the main function, a Barrier is created to synchronize two processes and a Lock is created to ensure serialized access to printing. Four processes are started:

Two processes, p1 - test_with_barrier and p2 - test_with_barrier, run the test_with_barrier function and are synchronized using the barrier.
Two processes, p3 - test_without_barrier and p4 - test_without_barrier, run the test_without_barrier function and execute independently without synchronization.
### Output
![Communication with pipe](images/processes_barrier.PNG "image1")

## run_background_processes_no_daemons
### Explanation:
In this code there is a function foo and a main function. The foo function retrieves the name of the current process and prints a starting message. If the process name is background_process, it prints numbers from 0 to 4 and then sleeps for 1 second. If the process name is NO_background_process, it prints numbers from 5 to 9 and then sleeps for 1 second. Finally, the function prints an exiting message.

In the main function, two processes are created. The first process, background_process, is explicitly given the name 'background_process' and targets the foo function. The second process, NO_background_process, is explicitly given the name 'NO_background_process' and also targets the foo function. Both processes are set as non-daemon processes and are started to execute their respective tasks.
### Output
![Communication with pipe](images/run_background_processes_no_daemons.PNG "image1")


## run_background_processes
### Explanation:
In this code there is a function `foo` and a main function. The `foo` function retrieves the current process name and prints a starting message. If the process name is `background_process`, it prints numbers from 0 to 4 and then sleeps for 1 second. If the process name is `NO_background_process`, it prints numbers from 5 to 9 and then sleeps for 1 second. Finally, the function prints an exiting message.

In the main function, two processes are created. The first process, `background_process`, is explicitly given the name `'background_process'`, targets the `foo` function, and is set as a daemon process. The second process, `NO_background_process`, is explicitly given the name `'NO_background_process'`, targets the `foo` function, and is set as a non-daemon process. Both processes are started. The daemon process runs only while the main program is running and terminates when the main program ends, while the non-daemon process continues until it completes its task.
### Output
![Communication with pipe](images/run_background_processes.PNG "image1")


## spawning_processes_namespace
### Explanation:
In this code the `myFunc` function is imported from another module named `myFunc`. The main function creates and manages processes. A loop runs 6 times, and in each iteration, a new process is created targeting the `myFunc` function and passing the current loop index `i` as an argument. Each process is started, which triggers the execution of `myFunc` with the provided argument, and the program waits for the process to complete using the `join` method before starting the next process.
### Output
![Communication with pipe](images/spawning_processes_namespace.PNG "image1")


## spawning_processes
### Explanation:
In this code there is a function `myFunc` and a main function. The `myFunc` function takes an argument `i`, prints a message indicating the process number, and then runs a loop from 0 to `i-1`, printing each value as the output of `myFunc`. 
In the main function, a loop runs 6 times. In each iteration, a new process is created targeting the `myFunc` function and passing the current loop index `i` as an argument. The process is started, which triggers the execution of `myFunc`, and the program waits for the process to finish using the `join` method before proceeding to the next iteration.
### Output
![Communication with pipe](images/spawning_processes.PNG "image1")

