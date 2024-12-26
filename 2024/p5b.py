#!/usr/bin/python3

import functools

def valid(update):
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            if not update[j] in table[update[i]]:
                return False
    return True

count = 0
with open("p5.txt") as f:
    words = [x.strip() for x in f.readlines()]
    part = words.index("")
    table = {}
    for x in words[:part]:
        rule = x.split("|")
        st = table.get(rule[0])
        if not st:
            st = set()
            table[rule[0]] = st
        st.add(rule[1])

    keyfunc = functools.cmp_to_key(lambda x,y:-1 if y in table[x] else 1)

    for upd in words[part+1:]:
        update = upd.split(",")
        if not valid(update):
            update.sort(key=keyfunc)
            count += int(update[len(update)//2])
    print(count)