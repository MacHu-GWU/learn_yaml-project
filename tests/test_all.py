#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
this script is the main test file can recursively test everything in this directory.
"""

if __name__ == "__main__":
    import pytest
    pytest.main(["--tb=native", "-s"])