#!/usr/bin/env python
# SPDX-License-Identifier: CC0-1.0

"""Simple test program to ensure the b64s wheel works and type-checks."""

import enum
import sys

import b64s


@enum.unique
class Status(enum.IntEnum):
    """Exit status for this test script."""
    SUCCESS = 0
    FAILURE = 1


def main() -> Status:
    """Check that the installed wheel seems to be working."""
    plain = 'The Hebrew phrase for “snowboarder” is גולש סנובורד. 🏂'
    coded = b64s.encode(plain)
    print(f'{plain = }')
    print(f'{coded = }')
    roundtrip = b64s.decode(coded)
    print(f'{roundtrip = }')
    roundtrip_ok = roundtrip == plain
    print(f'{roundtrip_ok = }')
    return Status.SUCCESS if roundtrip_ok else Status.FAILURE


if __name__ == '__main__':
    sys.exit(main())
