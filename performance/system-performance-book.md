# System Performance

## Introduction

* `System Stack` - Have a diagram of the system stack.
    
    * __Software__ - `Applications`, `databases`, `webservers`, `language libraries`, `OS system libraries`, `system calls`.

    * __Kernel__ - `Thread scheduler`, `file systems`, `network stack`, `virtual memory`, `device drivers`, 

    * __Hardware__ - `Machines`, `processors`, `caches`, `memory`, `disks`, `networks`, `devices`.

* `Workload Analysis` - Uderstanding the `workload` produced by applications in the statck and their requirements.

* `Resource Analysis` - Understanding the `resources` in the stack and their requirements.

* Quantifaction and Metrics - Quantify performance issues and estimate the benefit of fixes.

    * `Latency` -  A measure of time spent waiting. The time it takes for an operation to complete. High latency is a good general indicator for performance quantification.

    * `Utilisation` - A measure of the percentage time a resource is busy.

* `Dynamic Tracing`

    * Allow the `latency` of all system operations to be `instrumented` and `observed`.

    * It is a technique of taking `in-memory CPU instructions` and `dynamically building instrumentation` upon them.

    * `Dtrace` was the first dynamic tracer.

        > NB: Before dyamic tracing, only a small set of kernel instrumentaion points (`static probes`) were available. 
    


