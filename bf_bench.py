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


if __name__ == '__main__':
    interpreter = "/home/wilfred/projects/brainfrack/c/brainfrack"

    print("Program: hello_world.bf")
    print("Interpreter: ")
    print(timed_run("{} < hello_world.bf".format(interpreter)))

    print("Compiled: ")
    print(timed_run("/home/wilfred/projects/bfc/hello_world"))
    print()

    print("Program: bottles.bf")
    print("Interpreter: ")
    print(timed_run("{} < bottles.bf".format(interpreter)))

    print("Compiled: ")
    print(timed_run("/home/wilfred/projects/bfc/bottles"))
    print()
    
    print("Program: squares.bf")
    print("Interpreter: ")
    print(timed_run("{} < squares.bf".format(interpreter)))

    print("Compiled: ")
    print(timed_run("/home/wilfred/projects/bfc/squares"))
    print()
    
    print("Program: fibs.bf")
    print("Interpreter: ")
    print(timed_run("{} < fibs.bf".format(interpreter)))

    print("Compiled: ")
    print(timed_run("/home/wilfred/projects/bfc/fibs"))
    print()
    
