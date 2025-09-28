from math import log2


class Bucket:
    def __init__(self):
        self.elems = []

    def append(self, key, val):
        self.elems.append((key, val))

    def remove(self, k_v_tuple):
        self.elems.remove(k_v_tuple)

    def search(self, key):
        for k, v in self.elems:
            if k == key:
                return (k, v)
        raise KeyError(f"key {key} not found")

    def delete(self, key):
        for k, v in self.elems:
            if k == key:
                self.elems.remove((k, v))
                return
        raise KeyError(f"key {key} not found")


class HashTable:
    def __init__(self, size=10, bucket_size=None):
        if bucket_size is None:
            bucket_size = int(log2(size))

        self.count = 0
        self.size = size
        self.bucket_size = bucket_size
        self.buckets = [Bucket() for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def _reshape(self, k=1.5):
        old_buckets = self.buckets
        self.size = int(k * self.size)
        self.buckets = [Bucket() for _ in range(self.size)]
        self.count = 0
        for bucket in old_buckets:
            for key, val in bucket.elems:
                idx = self._hash(key)
                self.buckets[idx].append(key, val)

    def __getitem__(self, key):
        idx = self._hash(key)
        _, v = self.buckets[idx].search(key)
        return v

    def __setitem__(self, key, value):
        idx = self._hash(key)
        try:
            k, v = self.buckets[idx].search(key)
            if v != value:
                self.buckets[idx].remove((k, v))
                self.buckets[idx].append(key, value)
        except KeyError:
            self.buckets[idx].append(key, value)
            self.count += 1
            if self.count > self.size * self.bucket_size:
                self._reshape()

    def __delitem__(self, key):
        idx = self._hash(key)
        self.buckets[idx].delete(key)
        self.count -= 1
