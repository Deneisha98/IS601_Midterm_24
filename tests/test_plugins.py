import pytest
import calculator.plugins.sqrt as sqrt_plugin
import calculator.plugins.power as power_plugin
import calculator.plugins.log as log_plugin

def test_sqrt():
    assert sqrt_plugin.run(16) == 4

def test_power():
    assert power_plugin.run(2, 3) == 8

def test_log():
    assert log_plugin.run(100, 10) == 2
