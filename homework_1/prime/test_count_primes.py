from homework_1.prime.count_primes import count_primes


def test_count_primes():
    assert count_primes(0) == 0
    assert count_primes(1) == 0
    assert count_primes(2) == 0
    assert count_primes(3) == 1
    assert count_primes(4) == 2
    assert count_primes(5) == 2
    assert count_primes(6) == 3
    assert count_primes(100) == 25
    assert count_primes(1_000_000) == 78498
