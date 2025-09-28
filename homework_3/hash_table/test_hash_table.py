from homework_3.hash_table.hash_table import HashTable


def test_hashtable_basic():
    ht = HashTable()

    ht["a"] = 1
    ht["b"] = 2
    assert ht["a"] == 1
    assert ht["b"] == 2

    ht["a"] = 5
    assert ht["a"] == 5

    del ht["a"]
    try:
        _ = ht["a"]
        raise AssertionError("KeyError должен был быть")
    except KeyError:
        pass

    ht["c"] = 10
    assert ht["c"] == 10


def test_hashtable_resize():
    ht = HashTable(size=2, bucket_size=1)
    for i in range(10):
        ht[i] = i * 10
    for i in range(10):
        assert ht[i] == i * 10


def test_hashtable_collisions():
    ht = HashTable(size=1)
    ht["x"] = 100
    ht["y"] = 200
    ht["z"] = 300
    assert ht["x"] == 100
    assert ht["y"] == 200
    assert ht["z"] == 300
