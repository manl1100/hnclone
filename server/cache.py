from functools import wraps
import hashlib
import json

from redis import RedisError, StrictRedis

redis = StrictRedis(
    host="redis",
    db=0,
    socket_connect_timeout=2,
    socket_timeout=2
)


def memoize(ttl=5):
    def memoize_decorator(func):
        @wraps(func)
        async def func_wrapper(*args, **kwargs):
            key = 'HACKERNEWS_{}'.format(hashlib.md5(b'stories').hexdigest())
            result = redis.get(key)
            if result:
                return json.loads(result)
            else:
                result = await func(*args, **kwargs)
                redis.setex(key, ttl, json.dumps(result))
                return result
        return func_wrapper
    return memoize_decorator
