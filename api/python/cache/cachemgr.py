#coding: utf-8
'''
Created on 2015年12月11日

@author: AilenZou
'''

class CacheMgr(object):
    def _do_get_from_cache(self, key):
        """
            Get value from cache.
            @param key: String, the key.
            @return: value of the key; None if missing.
        """
        raise
    
    def _do_save_cache(self, key, value):
        """
            Save new value of the key.
            @param key: String.
            @param value: object value to save.
        """
        raise
    
    def _do_delete_cache(self, key):
        """
            Delete key from the cache.
            @param key: String.
        """
        raise
    
    def get(self, key, fetcher=None, *args, **kwargs):
        """
            Get value of the @key, if there is no value, @fetcher will be called
            with @args and @kwargs for fetching the value. If no value fetched, 
            None will be returned.
            @param key: String.
            @param fetcher: Function, the method to fetch value if missing.
            @return: 
                Value of the key; None if missing.
        """
        value = self._do_get_from_cache(key)
        if value is None and not fetcher is None:
            value = fetcher(*args, **kwargs)
            if value is None:
                return None
            self._do_save_cache(key, value)
        return value
            
    def set(self, key, value):
        """
            Set value of key.
            @param key: String.
            @param value: object.
        """
        self._do_save_cache(key, value)
        
    def delete(self, key):
        """
            Delete key from the cache.
            @param key: String.
        """
        self._do_delete_cache(key)