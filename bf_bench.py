#!/usr/bin/env python

from time import time
import os


def timed_run(command, program="hello_world.bf", runs=10):
    """Run BF implementation command with program specified, and return a
    list of timings.

    """
    timings = []
    for _ in range(runs):
        start_time = time()
        os.system("{} < {}".format(command, program))
        elapsed = time() - start_time
        timings.append(elapsed)

    return timings


INTERPRETER = "/home/wilfred/projects/brainfrack/c/brainfrack"


if __name__ == '__main__':
    print(timed_run(INTERPRETER))
