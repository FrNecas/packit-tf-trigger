#!/usr/bin/env python3
from specfile import Specfile

spec = Specfile('test.spec')
assert spec.epoch == "2"
