from GuessGameEngine import GuessGameEngine
import random

def test_perfect_guess(monkeypatch):
    engine = GuessGameEngine()
    monkeypatch.setattr(random, "randint", lambda a, b: 7)
    result = engine.magic_number_function(7)
    assert "Perfect guess" in result

def test_too_low(monkeypatch):
    engine = GuessGameEngine()
    monkeypatch.setattr(random, "randint", lambda a, b: 8)
    result = engine.magic_number_function(5)
    assert "too low" in result

def test_too_high(monkeypatch):
    engine = GuessGameEngine()
    monkeypatch.setattr(random, "randint", lambda a, b: 3)
    result = engine.magic_number_function(6)
    assert "too high" in result

