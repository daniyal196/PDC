# Chapter 4

## alltoall
### Explaination:
In this code the mpi4py library is used to demonstrate Alltoall communication in MPI. Each process creates a senddata array where elements are scaled by (rank+1) and allocates an empty recvdata array to receive data from other processes. The Alltoall method allows each process to send its data to every other process and receive corresponding data from them. After the communication, each process prints its rank, the data it sent, and the data it received. This pattern ensures every process exchanges data with all others.

### output:
![Ergonomic](images/alltoall.PNG "iamge")


## broadcast
### Explaination:
In this code, the `mpi4py` library is used to demonstrate broadcasting data from one process to all other processes using the `bcast` method. The communicator `comm` is initialized, and each process retrieves its unique rank. Process 0 initializes a variable `variable_to_share` with the value `100`, while all other processes set this variable to `None`. The `comm.bcast` method is then used to broadcast the value of `variable_to_share` from the root process (rank 0) to all processes in the communicator. After broadcasting, every process receives the same value of `variable_to_share` and prints its rank along with the shared variable value.

### output:
![Ergonomic](images/broadcast.PNG "iamge")


## deadLockProblems
### Explaination:
In this code, the `mpi4py` library is used to demonstrate point-to-point communication between two processes using the `send` and `recv` methods. Each process retrieves its unique rank using `comm.Get_rank()` and prints it. If the rank is `1`, the process sends the string `"a"` to process `5` and receives data from process `5`. If the rank is `5`, the process receives data from process `1` and then sends the string `"b"` back to process `1`. Each send and receive operation is accompanied by a print statement indicating the action taken, the data involved, and the source or destination process. This creates a two-way communication exchange between processes `1` and `5`.

### output:
![Ergonomic](images/deadLockProblems.PNG "iamge")


## gather
### Explaination:
In this code, the `mpi4py` library is used to demonstrate the `gather` operation in MPI, where data from all processes is collected at a root process. Each process retrieves its rank and the total number of processes. If the rank is not `0`, the process computes its data as the square of `(rank + 1)` and prepares it for sending. The `comm.gather` method is then called, where all processes send their data to the root process (`rank 0`). On the root process, the gathered data is stored in the `data` array. The root process iterates through the received data and prints messages indicating the data received from each process.

### output:
![Ergonomic](images/gather.PNG "iamge")


## point_to_point_comm
### Explaination:
In this code, the `mpi4py` library is used to demonstrate point-to-point communication with additional checks to ensure ranks involved in sending and receiving operations are valid. Each process retrieves its rank and total number of processes. 

- **Rank 0** initializes a `data` value of `1000` and sends it to process `1` if the destination rank (`1`) exists within the total number of processes (`size`). If not, it prints a message indicating the invalid destination.

- **Rank 1** receives data from process `0`, printing the received value if the source rank (`0`) is valid. It then sends the string `"hello"` to process `2` if the destination rank exists, otherwise printing an error message.

- **Rank 2** waits to receive data from process `1`, printing the data received if the source rank is valid, or reporting an error if the source does not exist.

- **Rank 8** contains a placeholder block to illustrate invalid rank handling, but it does not execute unless `rank 8` exists in the communicator.

This structure ensures all send and receive operations are executed only when valid ranks exist, avoiding errors during execution in smaller communicator sizes.

### output:
![Ergonomic](images/point_to_point_comm.PNG "iamge")


## reduction
### Explaination:
In this code, the `mpi4py` library is used to demonstrate the `Reduce` collective operation, which combines data from all processes into a single result at the root process using a specified operation. Each process calculates its `senddata` array as a sequence of integers scaled by `(rank + 1)`. The `recvdata` array is initialized to zeros on all processes to store the reduced result. 

The `comm.Reduce` function is called with `MPI.SUM` as the reduction operation, which sums the `senddata` arrays from all processes. Only the root process (rank `0`) receives and stores the reduced result in its `recvdata` array, while other processes do not see the reduced data. After the reduction, each process prints its rank and the corresponding output. Rank `0` displays the combined result stored in `recvdata`, while other processes indicate they did not receive the reduced data.

### output:
![Ergonomic](images/reduction.PNG "iamge")


## scatter
### Explaination:
In this code, the `mpi4py` library is used to demonstrate the `scatter` operation, where data from the root process (rank `0`) is distributed among all processes in the communicator. 

- **Rank 0** initializes an `array_to_share` with a size matching the total number of processes (`size`), such that each process can receive one element. The root process prints this array before scattering it.
- **Non-root processes** set `array_to_share` to `None` since they do not need access to the full array.
- The `comm.scatter` function is called, distributing one element of `array_to_share` to each process. Each process receives its part of the data in the `recvbuf` variable.
- After scattering, each process prints its rank and the value it received.

This operation ensures that the array is divided among processes, with each process working only on its designated element.

### output:
![Ergonomic](images/scatter.PNG "iamge")


## virtualTopology
### Explaination:
This code demonstrates the creation of a 2D grid topology using `mpi4py`'s Cartesian communicator. A grid of processes is arranged in rows and columns, with each process having potential neighbors in the directions UP, DOWN, LEFT, and RIGHT. 

The communicator (`comm`) determines the total number of processes (`size`) and assigns a unique rank to each process. The dimensions of the grid are calculated as `grid_rows` and `grid_columns`, ensuring that the product of these dimensions equals the total number of processes. If this condition isn't met, the program exits with an error message from rank `0`.

The Cartesian topology is created using `comm.Create_cart`, enabling processes to organize themselves in a grid with specified dimensions and no periodic boundaries. Each process then determines its position (`my_mpi_row`, `my_mpi_col`) in the grid and identifies its neighbors in all four directions (`UP`, `DOWN`, `LEFT`, `RIGHT`) using `cartesian_communicator.Shift`.

Finally, each process prints its rank, grid coordinates, and the ranks of its neighbors, providing a clear overview of the grid topology and neighbor relationships. This is useful for applications that require structured communication patterns, such as finite-difference simulations or stencil computations.

### output:
![Ergonomic](images/virtualTopology.PNG "iamge")
