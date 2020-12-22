# System Performance - Methodology

## Terminology

* `IOPS` : Input/output operations per second is a measure of the rate of data transfer operations.

* `Throughput` : The rate of work performed.

* `Response time`: The time for an operation to complete.

* `Latency`: How long an operation spends waiting to be serviced.

* `Utilization` : A measure of how busy a resource is, based on how much time in a given interval it was actively performing work.

    * `Time Based` : `U = B/T` where U = utilization, B = total time the system was busy during T, the observation period.

    * `Capacity Based` : At any level of performance, the system or component is working at some proportion of its capacity.

* `Saturation`: The degree to which a resource has queued work it cannot service.

---

## Models

* `SUT` - System Under Test.

* `Perturbations` - Other factor that may affect measurements: e.g. shared tenancies in cloud environments, scheduled workloads.

* `Queueing Systems` - Many systems are modeled as queueing systems. Quantitative Design and Analysis.

---

## Concepts

* `Latency` - The latency is the time spent waiting before an operation is performed.

    > e.g. `Network Service Request Response Time = Latency + Data Transfer Time`

    * Latency can have many aspects and types: DNS Latency, TCP Handshake Latency, Transfer Time Latency, etc.

    * Predicted speedup can also be calculated, by considering when latency can be reduced or removed.

    * When possible, other metric types can be converted to latency or time so that they can be compared.

* `Trade-offs and Tunable Parameters` e.g.

    * __Filesystem Record Size__ - `Random access` vs `Streaming`.

    * __Network Buffer Size__ - `Small - Scalability` vs `Large - Throughput`.

* `Performance tuning` 

    * Most effective when done closest to where the work is performed.
    
    * For workloads driven by applications, this means within the application itself.

* `Point-in-Time Recommendations`

    * Tunable parameters ay not always be valid or subject to change.

* `Load versus Architecture`

    * The `application workload` may not be appropriate for a `particular architecture`.

    * An application can perform badly due to an issue with the software configuration and hardware on which it is running: its architecture.

    * an application can also perform badly simply due to too much load applied, resulting in queueing and long latencies.

* `Scalability`

    * The `performance` of the system `under increasing load` is its `scalability`.

    * `Throughput` under increased `load` should be linear until the `scalability` limit (`knee point`) is reached.

        > NB: This `saturation` point often exists at points 100% `utilisation` for some resource.
    
    * e.g. For a highly multi-threaded application - As the CPUs approach 100% utilization, performance begins to degrade as CPU scheduler latency increases.

    * `Non-Linear Scalability` - Bad.

    * `Fast vs Slow Scalability Degradation.

* `Known Unknowns`

    * `Known knowns` : These are things you know. __List these__.

    * `Known unknowns` : These are things you know that you do not know. __Have a plan to obtain these__.

    * `Unknown unknowns` : These are things you do not know you do not know. __Learning__.

* `Profiling` - `Sample` the state of the system at timed intervals, and then studying the set of samples.

    * `Observer Effect` : Measuring some metrics e.g. latency, may affect the measurements itself.

* `Caching` : A cache stores results from a slower storage tier in a faster storage tier for reference.

    * `Cache Hit Ratio` : `t ratio = hits / total accesses (hits + misses)`

    * `Cache Miss Rate`

    * `Cache Runtime`

    * `Cache Eviction Algorithms`

        * `MRU` - Most recently used.

        * `LRU` - Least recently used.

        * `MFU`

    * `Cache Warmth` : `Cold` (0%), `Hot` (99%), `Warm`





















