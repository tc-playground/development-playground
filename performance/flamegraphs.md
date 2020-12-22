# Flame graphs


## Flame Graphs

__A hierarchical visualisation of a running process and it's sub-routines.__

* Profile by `pid`.

* __Interpretation__

    * The `x-axis` shows the stack profile population, sorted alphabetically (it is not the passage of time).

    * The he `y-axis` shows stack depth, counting from zero at the bottom.

    * Each rectangle represents a `stack frame`. The wider a frame is is, the more often it was present in the stacks. Percentage of time executing.

    * The top edge shows what is on-CPU, and beneath it is its ancestry.
    * The colors are usually not significant, picked randomly to differentiate frames.

* __Functions that are both deeply-nested (high on the y-axis) and time-intensive (wide on the x-axis); are the indicator that a function is improperly using CPU resources and can benefit from optimization.__

* __In a `flame graph`, it is a function’s `total time` that is communicated by that function’s `width`.__

---

## Other Charts

* `Treemap Charts` - __In a `treemap chart`, it is a function’s `self time` that is communicated by that function’s `area`.__

* `Sunburst Charts`

---

## Resources

* [Flame Graphs](http://www.brendangregg.com/flamegraphs.html) - Brendan Gregg

    * [Github](https://github.com/brendangregg/FlameGraph)

    * [Understanding CPU Flame-graphs](https://nodesource.com/blog/understanding-cpu-flame-graphs/).
