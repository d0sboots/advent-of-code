#!/usr/bin/python3
"""
Generates nasty problem input for 2024's Advent of Code problem 24

Version 0.2
"""

import argparse
import random
import time

parser = argparse.ArgumentParser(
        description="Generates nasty problem input for 2024's AoC problem 24")
parser.add_argument("-s", "--seed", help="Use specified random seed")
parser.add_argument("-e", "--easy", action="store_true",
    help="Use swaps like those found in the contest, instead of mean ones.")
parser.add_argument("-v", "--visible", action="store_true",
    help="Use readable names for intermediate states, instead of random ones")
parser.add_argument("-x", "--scramble", action="store_true",
    help="Scramble the order of the final rules. This does not affect the " +
        "problem difficulty, only the visual presentation. This is on by default " +
        "unless -v is used, but can be enabled in that case for output parity.")

def print_args(args):
    vis = " --visible" if args.visible else ""
    scr = " --scramble" if args.scramble else ""
    ez = " --easy" if args.easy else ""
    print(f'--seed={args.seed}{vis}{scr}{ez} ', end="")

def print_result(answer, size, rules):
    print("answer=" + ",".join(sorted(answer)))
    for x in range(size):
        print(f'x{x:02d}: 0')
    for y in range(size):
        print(f'y{y:02d}: 0')
    print()
    for rule in rules:
        print('{2[0]} {1} {3[0]} -> {0}'.format(*rule))

def make_problem(args):
    rng = random.Random(args.seed)
    size = rng.randrange(43, 52)
    xrefs = []
    yrefs = []
    for x in range(size):
        xrefs.append((f'x{x:02d}',))
    for y in range(size):
        yrefs.append((f'y{y:02d}',))
    rules = []
    rules.append(["z00", "XOR", xrefs[0], yrefs[0]])
    rules.append(["c00", "AND", xrefs[0], yrefs[0]])
    for i in range(1, size):
        rules.append([f'a{i:02d}', "XOR", xrefs[i], yrefs[i]])
        rules.append([f'b{i:02d}', "AND", xrefs[i], yrefs[i]])
        rules.append([f'z{i:02d}', "XOR", rules[-2], rules[-3]])
        rules.append([f'd{i:02d}', "AND", rules[-3], rules[-4]])
        rules.append([f'c{i:02d}', "OR",  rules[-1], rules[-3]])
    rules[-1][0] = f'z{size:02d}'

    if not args.visible or args.scramble:
        for r in rules:
            if rng.randrange(2):
                r[2], r[3] = r[3], r[2]
        rng.shuffle(rules)
    # Rename after shuffling, so that just turning on visible keeps the same order when shuffled
    az_full = "abcdefghijklmnopqrstuvwxyz"
    if not args.visible:
        seen = set()
        for r in rules:
            if r[0][0] == "z":
                continue
            while True:
                pull = rng.choice(az_full[:-3]) + "".join(rng.choices(az_full, k=2))
                if pull not in seen:
                    break
            r[0] = pull
            seen.add(pull)
    return [], size, rules

if __name__ == "__main__":
    args = parser.parse_args()
    if args.seed is None:
        args.seed = str(time.time_ns())
    print_args(args)
    result = make_problem(args)
    print_result(*result)
