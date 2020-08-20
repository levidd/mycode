#!/usr/bin/env python3

import pytest
import json
import requests


@pytest.fixture(scope="module")
def api_data():
    returning = None
    with open("api_data.json") as data:
        returning = json.load(data)
    return returning


@pytest.fixture(autouse=True)
def disable_network_calls(monkeypatch):
    def stunted_get():
        raise RuntimeError("No Network Calls during tests")

    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: stunted_get())

