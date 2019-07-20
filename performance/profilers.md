# Profiling

## CPU Profiling

* [CPU Analysis Types](http://www.brendangregg.com/offcpuanalysis.html)

    * `On-CPU` - Where `threads` are spending time running on-CPU.

    * `Off-CPU` - Where time is spent `waiting while blocked` on I/O, locks, timers, paging/swapping, etc.

---

## [Profilers](https://hackernoon.com/how-profilers-work-1826163e1bbc)

* __To accurately and successfully isolate bottlenecks in your code, you must use a combination of profilers.__

* __Deterministic / Instrumenting Profilers__ - Always add special code at the _start_ and _end_ of each `routine`.

    * __Source Code__ - Add special code to the _source_. Bad. Only executable once the function stack has been set-up.

    * __Binary/Hierarchical__ - Add special code to the binary. Can be added at runtime. Can execute before the function is setup on the stack.

        * __Calibration__ - The profiler codes adds time to execution. The overhead for running the instrumentation can be accounted for.

        * __CPU Optimization (e.g. branch prediction)__ - Inserting profiling operations in highly used small operations can effect the program and cause poor results.
    
    > __Good__ : Fast/Easy and produces good results quickly. Gives a full stack trace.

    > __Bad__ : Hard to profile small frequently used operations. Especially those that interfere with CPI optimizations.


* __Statistical / Sampling Profilers__ - Nothing is added to the code. all profiling work is done outside the application.

    1. The operating system interrupts the CPU at regular intervals (time slices) to execute process switches.

    2. At that point, a sampling profiler will record the currently-executed instruction (the execution point) for the application it is profiling.

        * This is as short an operation as can possibly be implemented: the contents of one CPU register are copied to memory.

    3. Using debug information linked into the application's executable, the profiler later correlates the recorded execution points with the routine and source code line they belong to.
    
    4. What the profiling finally yields is the _frequency with which a given routine or source line was executing at a given period in the application's run_.

    * The designs of a sampling profiler are very easy to explain but are unfortunately very tedious and complex to implement because it is mostly non portable code because of its dependencies on the `ABI`, compiled binary format, debug information amongst other things. 

> __Good__ : Easy to profile small frequently used operations.

> __Bad__ : Statistical, may need to run a few times. Get only the routine being executed, not, it's full trace.


---

## [Mozilla Statistical Profiler](https://benoitgirard.wordpress.com/2012/03/30/writing-a-profiler/)

1. First thing you want is a watchdog that will be ready to collect and store samples (backtraces amongst other thing) at a fixed interval. This is implemented as a simple thread that sleeps.

2. Now you want a way to stop a thread to give you a chance to get a snapshot of what it was doing. On windows and mac we use a platform specific thread pause API and on linux and android we use a signal.

3. Now that the thread is paused you need a way to collect data. Our profiler deviates from typical profilera and will record if the process has been responding to its event queue. For unwinding we’ve been extending nsStackWalk.h except on Android where we are working towards using libunwind under fennec profiling builds.
Now you can resume the thread you so rudely interrupted and let it do some more work before the next sample/audit.

4. After you’ve collected a good number of samples you want to dump this data somewhere. In our case we pass the data to JS where we can let fancy extensions and web apps with all the html5 features and buzzwords do their magic. Note that when saving you also want to note what libraries are loaded and where they live in memory for the next step.

5. Now that you’ve collected thousand of backtraces you need to convert these address into something that can be traced back to the source code. Roughtly speaking of course, all source code is converted into binary code into libraries. To make maters more complicated libraries can be loaded just about anywhere in memory.

    * __Symbolicating__ - To translate a raw address you take this process backwards, you start with 0x8106, you know that address falls inside the range of libBAR.so/dll which is loaded at offset 0x8000, thus you’re dealing with address 0x106 in that library,

6. Now that you’ve collected the data you can now present it in some useful way. This is typically some weighted call graph presentation.

---

## References

* [How profilers work](https://hackernoon.com/how-profilers-work-1826163e1bbc).

* [Fundamental of Performance Profiling](https://smartbear.com/learn/code-profiling/fundamentals-of-performance-profiling/)

* [Mozilla Profiler](https://benoitgirard.wordpress.com/2012/03/30/writing-a-profiler/).

* [Application Binary Interface](https://en.wikipedia.org/wiki/Application_binary_interface) - Wikipedia.
