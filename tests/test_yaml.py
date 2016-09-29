#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
import pytest
from pytest import approx
from pprint import pprint


def test_load_and_dump():
    with open("test.yml", "rb") as f:
        data = yaml.load(f.read().decode("utf-8"))

    assert data["sec1"]["str"] == "Hello World!"
    assert data["sec1"]["int"] == 100
    assert data["sec1"]["float"] == approx(3.14)
    assert data["sec1"]["bool"] is True
    assert data["sec1"]["path"] == r"C:\Users\admin\config.txt"
    assert data["sec1"]["utf8"] == "不是英文"
    assert data["sec1"]["int_like_str"] == "123"

    assert data["sec2"]["list"] == [1, 2, 3]
    assert data["sec2"]["dict"] == {
        "key1": "value1", "key2": "value2", "key3": "value3"}

    pprint(data)

    with open("test_dump.yml", "wb") as f:
        text = yaml.dump(data, default_flow_style=False)
        print(text)
        f.write(text.encode("utf-8"))


if __name__ == "__main__":
    import os
    pytest.main([os.path.basename(__file__), "--tb=native", "-s", ])
