# Archery cookie
Cookies from Archery person.

## Environment

Before using the module, it is necessary to create the following environment variables:

* ARCHERY_PERSON_SECRET - This key must be 32 url-safe base64-encoded bytes.
* ARCHERY_PERSON_SESSION_DB - Database name.
* ARCHERY_PERSON_SESSION_TIME - Cookie expiration, in seconds.
* ARCHERY_PERSON_REDIS_HOST - Host URL.
* ARCHERY_PERSON_REDIS_PORT - Host port.

These variables can be stored within an .env file.

## How to use
```python
>>> from archery_cookie import Cookie, CookieNotFound
>>>
>>>
>>> cookie = Cookie()
>>> data = {'id': 123, 'path': '/home'}
>>> # New cookie
>>> new_cookie = cookie.new(data)
>>> new_cookie
'it2HNyyStj_gMmIodh7-omFMwFQELd64qFeKbD2hAXI='
>>> # Show cookie data
>>> cookie_get(new_cookie)
{'id': 123, 'path': '/home'}
>>> # Renew cookie
>>> renew = cookie.renew(new_cookie)
>>> renew
'ecBgREMrLYs2rZ2cTRUfsZxzUCo3iq1J0UimWsQecxo='
>>> cookie_get(renew)
{'id': 123, 'path': '/home'}
>>> # Trying to reuse cookie
>>> try:
...     cookie.renew(new_cookie)
... except CookieNotFound:
...     print('Cookie not found.')
Cookie not found.
```
