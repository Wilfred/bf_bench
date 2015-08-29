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


def inter_vs_comp(program):
    compiler = "/home/wilfred/projects/bfc/target/debug/bfc"
    interpreter = "/home/wilfred/projects/brainfrack/c/brainfrack"

    print("Program: {}".format(program))
    print("Interpreter: ")
    print(min(timed_run("{} < {}.bf".format(interpreter, program))))

    os.system("{} {}.bf --opt=0 --llvm-opt=0".format(compiler, program))
    print("Compiled: ")
    print(min(timed_run("./{}".format(program))))
    print()


if __name__ == '__main__':
    inter_vs_comp("hello_world")
    inter_vs_comp("bottles")
    inter_vs_comp("squares")
    inter_vs_comp("fibs")
