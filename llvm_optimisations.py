#!/usr/bin/env python

#!/usr/bin/env python

from time import time
import os


def timed_run(command, runs=10):
    """Run BF implementation command with program specified, and return a
    list of timings.

    """
    timings = []
    for _ in range(runs):
        start_time = time()
        os.system("{} > /dev/null".format(command))
        elapsed = time() - start_time
        timings.append(elapsed)

    return timings


def compile_bf(program, bfc_opt, llvm_opt): 
    """Compare our test programs with and without LLVM optimisations. We
    use peephole optimisation from bfc, but no speculative execution.

    """
    compiler = "/home/wilfred/projects/bfc/target/debug/bfc"
    os.system("{} {} --opt={} --llvm-opt={}".format(compiler, program, bfc_opt, llvm_opt))


def bench_program(program):
    print("Program: {}".format(program))
    
    print("Baseline: ")
    compile_bf("{}.bf".format(program), bfc_opt=0, llvm_opt=0)
    print(min(timed_run("./{}".format(program))))

    print("Peephole only: ")
    compile_bf("{}.bf".format(program), bfc_opt=1, llvm_opt=0)
    print(min(timed_run("./{}".format(program))))

    print("LLVM only: ")
    compile_bf("{}.bf".format(program), bfc_opt=0, llvm_opt=3)
    print(min(timed_run("./{}".format(program))))

    print("Peephole and LLVM: ")
    compile_bf("{}.bf".format(program), bfc_opt=1, llvm_opt=3)
    print(min(timed_run("./{}".format(program))))
    print()

if __name__ == '__main__':
    bench_program("hello_world")
    bench_program("bottles")
    bench_program("squares")
    bench_program("fibs")
