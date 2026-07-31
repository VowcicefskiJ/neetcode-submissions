class HashTable:

    def __init__(self, capacity: int):
        # Set up the boxes: capacity = how many, buckets = the empty boxes,
        # size = running count of keys stored.
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    def _index(self, key: int) -> int:
        # The "mailbox rule": maps any key to a box. Same key → same box.
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        # Go to the key's box. If the key's already there, overwrite it.
        # Otherwise add it, count it, and grow if the boxes are getting full.
        bucket = self.buckets[self._index(key)]
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        bucket.append([key, value])
        self.size += 1
        if self.size / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        # Go to the key's box and search it. Return the value, or -1 if missing.
        bucket = self.buckets[self._index(key)]
        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key: int) -> bool:
        # Go to the key's box and search it. Pull the key out if found
        # (return True), otherwise return False.
        bucket = self.buckets[self._index(key)]
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                bucket.pop(i)
                self.size -= 1
                return True
        return False

    def getSize(self) -> int:
        # Number of keys currently stored.
        return self.size

    def getCapacity(self) -> int:
        # Number of boxes currently available.
        return self.capacity

    def resize(self) -> None:
        # Double the number of boxes. Because the mailbox rule depends on
        # capacity, every existing key has to be re-filed into the new set.
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        for bucket in old_buckets:
            for key, value in bucket:
                idx = key % self.capacity
                self.buckets[idx].append([key, value])