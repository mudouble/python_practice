from django.core.cache import cache

class CacheLock(object):
    def __init__(self, expires, wait_timeout=0):
        self.cache = cache
        self.expires = expires
        self.wait_timeout = wait_timeout

    def get_lock(self, lock_key):
        wait_timeout = self.wait_timeout
        identifier = uuid.uuid4()
        while wait_timeout>=0:
            if self.cache.add(lock_key, identifier, self.expires):
                return identifier
            wait_timeout-=1
            time.sleep(1)
        raise LockTimeout({'msg':'当前有其他用户正在编辑该采集配置，请稍后重试'})

    def release_lock(self, lock_key, identifier):
        lock_value = self.cache.get(lock_key)
        if lock_value==identifier:
            self.cache.delete(lock_key)

def redis_lock(cache_lock):
    def my_decorator(func):
        def warapper(*args, **kwargs):
            lock_key = ''
            identifier = cache_lock.get_lock(lock_key)
            try:
                return func(*args, **kwargs)
            finally:
                cache_lock.release_lock(lock_key, identifier)
        return warapper
    return my_decorator