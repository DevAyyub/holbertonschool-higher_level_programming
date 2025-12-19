#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Extend tuple with zeros to ensure at least 2 elements, then slice first 2
    t_a = (tuple_a + (0, 0))[:2]
    t_b = (tuple_b + (0, 0))[:2]
    return (t_a[0] + t_b[0], t_a[1] + t_b[1])
