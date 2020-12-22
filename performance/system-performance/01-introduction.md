# System Performance - Introduction

## System Stack

* `System Stack` - Create a diagram of the system stack.
    
    * __Software__ - `Applications`, `databases`, `webserver`, `language libraries`, `OS system libraries`, `system calls`.

    * __Kernel__ - `Thread scheduler`, `file systems`, `network stack`, `virtual memory`, `device drivers`, 

    * __Hardware__ - `Machines`, `processors`, `caches`, `memory`, `disks`, `networks`, `devices`.

---

## Workload vs Resource Analysis

* `Workload Analysis` - Understanding the `workload` produced by applications in the stack and their requirements.

* `Resource Analysis` - Understanding the `resources` in the stack and their requirements.

---

## Quantification

* `Quantification and Metrics` - Quantify performance issues and estimate the benefit of fixes.

    * `Latency` -  A measure of time spent waiting. The time it takes for an operation to complete. High latency is a good general indicator for performance quantification.

    * `Utilisation` - A measure of the percentage time a resource is busy.

    * `Saturation` - A measure of how much work has `built up` / is `queued`.

    * `Errors` - A count of the `errors` and `retried` being exhibited by the system.

* `Predicting Speedup` - Predicted speedup can also be calculated, by considering when latency can be reduced or removed.

---

## Instrumentation and Dynamic Tracing

* `Dynamic Tracing`

    * Allow the `latency` of all system operations to be `instrumented` and `observed`.

    * It is a technique of taking `in-memory CPU instructions` and `dynamically building instrumentation` upon them.

    * `DTrace` was the first dynamic tracer.

        > NB: Before dynamic tracing, only a small set of kernel instrumentation points (`static probes`) were available. 
    


