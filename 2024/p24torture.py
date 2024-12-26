#!/usr/bin/python3
"""
Generates nasty problem input for 2024's Advent of Code problem 24

Version 1.0
"""

import argparse
import random
import time

parser = argparse.ArgumentParser(
        description="Generates nasty problem input for 2024's AoC problem 24")
parser.add_argument("-s", "--seed", help="Use specified random seed")
parser.add_argument("-n", "--size", type=int,
    help="Size of the problem output (default range [43,52))")
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
    size = f" --size={args.size}" if args.size is not None else ""
    print(f'--seed={args.seed}{size}{vis}{scr}{ez} ', end="")


def print_result(answer, size, rules):
    print("answer=" + ",".join(sorted(x[0] for x in answer)))
    for x in range(size):
        print(f'x{x:02d}: 0')
    for y in range(size):
        print(f'y{y:02d}: 0')
    print()
    for rule in rules:
        print('{2[0]} {1} {3[0]} -> {0}'.format(*rule))


def swap(rules, bit0, gate0, bit1, gate1):
    if bit0 == 0 and gate0 >= 2:
        raise ValueError(f"{bit0} {gate0}")
    if bit1 == 0 and gate1 >= 2:
        raise ValueError(f"{bit0} {gate0}")
    if gate0 >= 5 or gate1 >= 5:
        raise ValueError(f"{gate0} {gate1}")
    off0 = bit0*5 + gate0 - (0 if bit0 == 0 else 3)
    off1 = bit1*5 + gate1 - (0 if bit1 == 0 else 3)
    r0 = rules[off0]
    r1 = rules[off1]
    r0[0], r1[0] = r1[0], r0[0]
    # We swapped the (output) labels on the rules, but this will also swap the
    # labels on all gates using these as inputs, which we don't want. So we
    # also swap the input references, in effect double-swapping the input
    # labels so they are correct again.
    for r in rules:
        if r[2] is r0:
            r[2] = r1
        elif r[2] is r1:
            r[2] = r0
        if r[3] is r0:
            r[3] = r1
        elif r[3] is r1:
            r[3] = r0
    return (r0, r1)


def make_problem(args):
    answer = []
    rng = random.Random(args.seed)
    if args.size is None:
        size = rng.randrange(43, 52)
    else:
        size = args.size
    if size < 5:
        raise ValueError(f"--size must be at least 5, got {size}")
    rules = make_rules(size)
    if args.easy:
        choices = rng.sample(range(1, size), k=4)
        # There are exactly four swaps we can make within a single bit,
        # and we make each of them once.
        answer.extend(swap(rules, choices[0], 2, choices[0], 1))
        answer.extend(swap(rules, choices[1], 2, choices[1], 3))
        answer.extend(swap(rules, choices[2], 2, choices[2], 4))
        answer.extend(swap(rules, choices[3], 0, choices[3], 1))
    else:
        pair_chain = size == 5 or rng.randrange(2)
        choices = rng.sample(range(1, size), k=4-pair_chain)
        pair1 = 4 if pair_chain else rng.choice([3, 4])
        pair2 = 3 if pair_chain else rng.choice([3, 4])
        answer.extend(swap(rules, choices[0], pair1, choices[2-pair_chain], pair1))
        answer.extend(swap(rules, choices[1], pair2, choices[3-pair_chain], pair2))
        cluster = choices[1] if pair_chain else rng.choice(choices)
        remain = set(range(size))
        remain.difference_update(choices)
        last_two = rng.sample(sorted(remain), k=2)
        gate_remain = set(range(3))
        zero_map = [-1, 1, 0]
        for n in last_two:
            if n == 0:
                w = rng.choice(sorted(gate_remain.intersection([1,2])))
                answer.extend(swap(rules, n, zero_map[w], cluster, w))
            else:
                w = rng.choice(sorted(gate_remain))
                answer.extend(swap(rules, n, w, cluster, w))
            gate_remain.remove(w)

    do_shuffle(rules, args, rng)
    return answer, size, rules


def make_rules(size):
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
    return rules


def do_shuffle(rules, args, rng):
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


if __name__ == "__main__":
    c_args = parser.parse_args()
    if c_args.seed is None:
        c_args.seed = str(time.time_ns())
    print_args(c_args)
    result = make_problem(c_args)
    print_result(*result)
