# main.py
def make_set(bucket_count: int):
    """Create a hash set with a given number of buckets."""
    return {"buckets": [[] for _ in range(bucket_count)], "size": 0}


def _bucket_for(s, key):
    """Get the bucket list for a given key."""
    idx = hash(key) % len(s["buckets"])
    return s["buckets"][idx]


def add(s, key: str) -> bool:
    """Add key to the set. Return True if added, False if already present."""
    bucket = _bucket_for(s, key)
    if key in bucket:
        return False
    bucket.append(key)
    s["size"] += 1
    return True


def contains(s, key: str) -> bool:
    """Return True if key is in the set."""
    bucket = _bucket_for(s, key)
    return key in bucket


def remove(s, key: str) -> bool:
    """Remove key from set. Return True if removed, False if not found."""
    bucket = _bucket_for(s, key)
    if key in bucket:
        bucket.remove(key)
        s["size"] -= 1
        return True
    return False


def size(s) -> int:
    """Return number of keys currently in the set."""
    return s["size"]
