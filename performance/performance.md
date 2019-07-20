# Performance

## Introduction

* [Brendan Greg](http://www.brendangregg.com/books.html)

---

## Types of Profiling

* `CPU` 

* `Memory`

* `Disk`

* `Network`

---

### Performance Tools

* `perf`

* [`ptrace`](http://man7.org/linux/man-pages/man2/ptrace.2.html)

    * Can do many complex things and is used, for example, by debuggers like `gdb` to look into a running process.

* [`strace`](https://strace.io/) - 'System Call Tracer`

    * Shows you the `syscalls` that `processes` make as well as their `arguments` and return `values`.

    * `strace` uses `ptrace` to instrument a target process and “listen” to that process’s `system calls`.

    * `ptrace` makes it possible for `strace` to interrupt the traced process every time a system call is invoked, capture the call, decode it, and then resume the execution of the traced process.

        > NB The info is fed back from `kernel space` to `user space` which causes multiple `context switches` and add expensive overhead.

* [`dtrace`](http://dtrace.org/blogs/about/) 

    * Solaris / BSD / Mac OSX only.

    * A `kernel` facility allow the user to create `probes` for kernel functionality.

    * DTrace takes scripts written in a domain-specific language called `D`, converts them into `bytecode`, and then `injects the bytecode into specific places` in the `kernel`. 
    
    * The `bytecode` can be executed when specific `events` happen, for example when a `system call` is `invoked`. The scripts are run in-line with no context switch.

    * The `output` can be collected through `libdtrace` by user level consumers, who print it on the screen or save it to disk.

    > NB: More efficient than `ptrace`+`strace` (no context switch), but, more complicated.

* [`sysdig`](https://sysdig.com/blog/sysdig-vs-dtrace-vs-strace-a-technical-discussion/)

    * Has an architecture similar to `libpcap`/`tcpdump`/`wireshark`.

    1. `events` are captured in the kernel by a small `driver`, called `sysdig-probe`, which leverages a kernel facility called `tracepoints`.

        * `tracepoints` make it possible to install a “handler” that is called from specific functions in the kernel.

        * Currently, `sysdig` registers `tracepoints` for `system calls` on `enter` and `exit`, and for `process scheduling events`.

        * `sysdig` copies the `event details` into a `shared buffer` (between `kernel` and `userspace`), encoded for later consumption.
    
    2. The `event buffer` is `memory-mapped` into `user space` so that it can be accessed without any copy, minimizing CPU usage and cache misses.

        * `libscap` and `libsinsp`, then offer support for reading, decoding, and parsing events.

            * `libscap` offers trace file management functionality.

            * `libsinsp` includes sophisticated `state tracking` functionality (e.g. you can use a file name instead of an FD number) and also `filtering`, `event decoding`, a `Lua JIT compiler` to run `chisels`, and much more.
    
    3. If the `event buffer` fills up, and sysdig-probe starts dropping the `incoming events`. So it does not slow down anything.

    > __NB__: The `sysdig` tracing overhead is predictable, and it means `sysdig` is suitable for running in production environments.


* Other Tracers

    * [eBPF](https://lwn.net/Articles/740157/) - A more powerful tracer builtin, `eBPF`. Is this the standard?
    
    * [SystemTap](https://sourceware.org/systemtap/)

    * [LTTng](https://lttng.org/)

    * [ftrace](https://elinux.org/Ftrace) - Function Tracer (does other stuff as well).

    * [ltrace](https://ltrace.org/) - ltrace intercepts and records dynamic library calls.

---

## Hardware Interrupts

* `Hardware Interrupts`

* `Software Interrupts`

* `Process Context Switch`

* `Linux System Calls`

---

## Articles

* [Playing with `ptrace`](https://www.linuxjournal.com/article/6100)

* [DTrace on Linux](https://www.phoronix.com/scan.php?page=news_item&px=DTrace-For-Linux-2018)














