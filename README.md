django-querytagger
==================

django-querytagger allows to correlate SQL query logs in your database with your Django application and logs.

Installation
------------

- Add `django-querytagger` to your dependencies.
- Add `django_querytagger` to `INSTALLED_APPS`
- Add `django_querytagger.middleware.SetTagMiddleware` early in your middleware stack
- Optionally, set `REQUEST_ID_HEADER` to the HTTP header you use for log correlation between webserver and django (make sure that these headers cannot be injected by users!)

Tag output
----------

For Django views, the query will be modified to include the internal name of the resolved URL:

    SELECT /* url=presale:event.index */ …

Or, with a request ID header:

    SELECT /* url=presale:event.index request=15fa49ec-2447-4bed-8785-581f02f2ab65 */ …

For Celery tasks, the query will be modified like this:

    SELECT /* task=pretix.base.services.cart.add_items_to_cart taskid=e7fbba31-5d56-4e67-b0dd-155bcd5733d9 */ …

For management tasks, the query will be modified like this:

    SELECT /* command=shell */ …


Compatibility
-------------

- Django 6.0 tested, but probably any version
- Python versions supported by Django
- SQLite and PostgreSQL, but probably any database

Security
--------

If you discover a security issue, please contact us at security@pretix.eu and see our [Responsible Disclosure Policy](https://docs.pretix.eu/trust/security/disclosure/) further information.

License
-------
The code in this repository is published under the terms of the Apache License.
See the LICENSE file for the complete license text.
