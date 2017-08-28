from os.path import abspath, dirname, basename

PROJECT_ROOT = dirname(dirname(dirname(abspath(__file__))))
DJANGO_ROOT = dirname(dirname(abspath(__file__)))
PROJECT_NAME = basename(DJANGO_ROOT)

###############################################################################
# General configuration
###############################################################################

MIDDLEWARE = [

    # The per-site caching middleware, this middlewares allows django to cache
    # entire pages when are accesed, to use this middleware a cache backend
    # must be configurated first. for more information:
    # https://docs.djangoproject.com/en/1.11/topics/cache/#the-per-site-cache
    # 'django.middleware.cache.UpdateCacheMiddleware',
    # 'django.middleware.common.CommonMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
]

# efault charset to use for all HttpResponse objects, if a MIME type isn’t
# manually specified.
DEFAULT_CHARSET = 'utf-8'
# Default content type to use for all HttpResponse objects, if a MIME type
# isn’t manually specified.
DEFAULT_CONTENT_TYPE = 'text/html'

# Default decimal separator used when formatting decimal numbers
DECIMAL_SEPARATOR = '.'

# If a given URL doens't match any in URLConf it gives the URL some flexibility
# if you add or remove one slash from the end an it matches some URL in URLConf
# it is taken as valid.
APPEND_SLASH = False

# Default exception reporter filter class to be used if none has been assigned
# to the HttpRequest instance yet.
DEFAULT_EXCEPTION_REPORTER_FILTER = \
    'django.views.debug.SafeExceptionReporterFilter'

# Default file storage class to be used for any file-related operations that
# don’t specify a particular storage system.
DEFAULT_FILE_STORAGE = \
    'django.core.files.storage.FileSystemStorage'

# Absolute urls are urls linked to a database Model, it is mostly used
# in the admin of django to access directly to that object and modify it.
ABSOLUTE_URL_OVERRIDES = {
    # example of usage:
    #  relative path of object, o in this is case is the object
    # 'blogs.weblog': lambda o: "/blogs/%s/" % o.slug,
}

###############################################################################
# File uploads configuration
###############################################################################

# The character encoding used to decode any files read from disk. This includes
# template files and initial SQL data files.
FILE_CHARSET = 'utf-8'
# A list of handlers to use for uploading
FILE_UPLOAD_HANDLERS = [
    'django.core.files.uploadhandler.MemoryFileUploadHandler',
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
]

# LAST ONE:
# https://docs.djangoproject.com/en/1.11/ref/settings/#file-upload-max-memory-size


###############################################################################
# Email server configuration
###############################################################################

# The backend to use for sending emails
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#

# Specifies a timeout in seconds for blocking operations like the connection
# attempt.
EMAIL_TIMEOUT = None

# The directory used by the file email backend to store output files.
# EMAIL_FILE_PATH =

# The host to use for sending email.
EMAIL_HOST = 'localhost'
# Port to use for the SMTP server defined in
EMAIL_PORT = 25
# Password and username to use for the SMTP server
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST_USER = ''

# Subject-line prefix for email messages sent with django.core.mail.mail_admins
# or django.core.mail.mail_managers. You’ll probably want to include the
# trailing space.
EMAIL_SUBJECT_PREFIX = '[Django] '

# Whether to send the SMTP Date header of email messages in the local time zone
# (True) or in UTC (False).
EMAIL_USE_LOCALTIME = False

# Whether to use a TLS (secure) connection when talking to the SMTP server.
# This is used for explicit TLS connections, generally on port 587.
EMAIL_USE_TLS = False
# Whether to use an implicit TLS (secure) connection when talking to the SMTP
# server. In most email documentation this type of TLS connection is referred
# to as SSL. It is generally used on port 465.
EMAIL_USE_SSL = False
# If EMAIL_USE_SSL or EMAIL_USE_TLS is True, you can optionally specify the
# path to a PEM-formatted certificate chain file to use for the SSL connection.
EMAIL_SSL_CERTFILE = None
# If EMAIL_USE_SSL or EMAIL_USE_TLS is True, you can optionally specify the
# path to a PEM-formatted private key file to use for the SSL connection.
EMAIL_SSL_KEYFILE = None

# Default email address to use for various automated correspondence from the
# site manager(s). This is the mail used to send simple emails to users.
DEFAULT_FROM_EMAIL = 'webmaster@localhost'

###############################################################################
# Debug configuration
###############################################################################

# People who will receive an email if there's an error or exception raised
# this only works if DEBUG is set to false
ADMINS = [
    # example of usage:
    # ('John', 'john@example.com'),
]

DEBUG = False  # Never deploy a site into production with DEBUG turned on.

# If set to True, Django’s exception handling of view functions (handler500,
# or the debug view if DEBUG is True) and logging of 500 responses
# (django.request) is skipped and exceptions propagate upwards.
DEBUG_PROPAGATE_EXCEPTIONS = False

###############################################################################
# Date formats configuration
###############################################################################

# The default formatting to use for displaying date fields in any part of the
# system.
DATE_FORMAT = 'N j, Y'  # February. 4, 2003

# A list of formats on  Python’s datetime module syntax that will be accepted
# when inputting data on a date field. Formats will be tried in order, using
# the first valid one.
DATE_INPUT_FORMATS = [
    '%Y-%m-%d', '%m/%d/%Y',   # '2006-10-25', '10/25/2006',
    '%m/%d/%y', '%b %d %Y',   # '10/25/06', 'Oct 25 2006',
    '%b %d, %Y', '%d %b %Y',  # 'Oct 25, 2006', '25 Oct 2006',
    '%d %b, %Y', '%B %d %Y',  # '25 Oct, 2006', 'October 25 2006',
    '%B %d, %Y', '%d %B %Y',  # 'October 25, 2006', 25 October 2006',
    '%d %B, %Y',              # '25 October, 2006'
]

# The default formatting to use for displaying datetime fields in any part of
# the system
DATETIME_FORMAT = 'N j, Y, P'

# Same as DATE's list of formtas but for DATETIME
DATETIME_INPUT_FORMATS = [
    '%Y-%m-%d %H:%M:%S',     # '2006-10-25 14:30:59'
    '%Y-%m-%d %H:%M:%S.%f',  # '2006-10-25 14:30:59.000200'
    '%Y-%m-%d %H:%M',        # '2006-10-25 14:30'
    '%Y-%m-%d',              # '2006-10-25'
    '%m/%d/%Y %H:%M:%S',     # '10/25/2006 14:30:59'
    '%m/%d/%Y %H:%M:%S.%f',  # '10/25/2006 14:30:59.000200'
    '%m/%d/%Y %H:%M',        # '10/25/2006 14:30'
    '%m/%d/%Y',              # '10/25/2006'
    '%m/%d/%y %H:%M:%S',     # '10/25/06 14:30:59'
    '%m/%d/%y %H:%M:%S.%f',  # '10/25/06 14:30:59.000200'
    '%m/%d/%y %H:%M',        # '10/25/06 14:30'
    '%m/%d/%y',              # '10/25/06'
]

###############################################################################
# DATABASE configuration
###############################################################################

DATABASES = {
    'default': {
        # The build-in django's engines are:
        # 'django.db.backends.postgresql'
        # 'django.db.backends.mysql'
        # 'django.db.backends.sqlite3'
        # 'django.db.backends.oracle'
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_project',
        'USER': 'user',
        'PASSWORD': 'password123',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        # A string to set explicitly a timezone for datetimes stored in this
        # database, use it if not using UTC, it has specific uses.
        'TIME_ZONE':  None,
        # Lifetime of a database connection, set 0 to close connection at the
        # end of each request, None for unlimited persistent connections.
        'CONN_MAX_AGE': 0,
        # To access a database's data, lets say modify or retrieve, the
        # database manager needs to start a 'transaction', when changes are
        # commited the transaction finishes automatically or is finished by
        # the user or manager of the database.
        # Atomic requests are means that django uses to manage this
        # transactions, when set to True django wraps every View on the project
        # with a function that starts a transaction before the view is executed
        # and finishes it right after the view is executed. It is a simple way
        # to handle transactions but it is not the one that django uses by
        # default, in anyway it as any automatic behavior it is rather
        # inefficient.
        # for more information:
        # https://docs.djangoproject.com/en/1.11/topics/db/transactions/
        'ATOMIC_REQUESTS': False,
        # By default django uses AutoCommit, when a query to the database is
        # made, django wraps that query in its own transaction. If set False
        # and ATOMIC_REQUESTS is also False, you will have to control
        # transactions explicitly.
        'AUTOCOMMIT': True,
        # When making tests with django's tools, django creates a database only
        # for testing, with empty values. These are the settings that database
        # will take.
        'TEST': {
            'NAME': 'test_django_project',
            # When there are several databases you can set this variable to
            # create another one first at testing creation of databases.
            'DEPENDENCIES': [''],
            # When setting a database here the connection with mirror database
            # is linked with this one too, so every change made to that
            # database is goign to be made in both mirror and this one too.
        },
        # Extra options this vary depending of the engine, for more
        # information: https://docs.djangoproject.com/en/1.11/ref/databases/
        'OPTIONS': {},
    },
    'development': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'django_project',
    },
}

# For multiple databases the list of routers that will be used to determine
# which database to use when performing a database query.
DATABASE_ROUTERS = []

# Default tablespace to use for indexes on fields that don’t specify one,
# if the backend supports it.
DEFAULT_INDEX_TABLESPACE = ''
# Default tablespace to use for models that don’t specify one, if the backend
# supports it.
DEFAULT_TABLESPACE = ''

###############################################################################
# CSRF configuration
###############################################################################

# Lifespan of the CSRF session cookie, is approximatelly one year in seconds
# long to have a persistent cookie on the user's browser. set to none to use
# session-based CSRF cookies.
CSRF_COOKIE_AGE = 31449600
# Custom domain used in csrf cookies
CSRF_COOKIE_DOMAIN = None
# Set to use HttpOnly flag on the CSRF cookie. If this is set to True,
# client-side JavaScript will not to be able to access the CSRF cookie.
CSRF_COOKIE_HTTPONLY = False
# Custom name for the cookie used to send a CSRF authentication token
CSRF_COOKIE_NAME = 'csrftoken'
# The path set on the CSRF cookie
CSRF_COOKIE_PATH = '/'
# Whether to use a secure cookie for the CSRF cookie. If this is set to True,
# the cookie will be marked as “secure,” which means browsers may ensure that
# the cookie is only sent with an HTTPS connection.
CSRF_COOKIE_SECURE = False
# Whether to store the CSRF token in the user’s session instead of in a cookie.
CSRF_USE_SESSIONS = False
# A dotted path to the view function to be used when an incoming request is
# rejected by the CSRF protection.
# If want to customize a function should have the next structure:
# def csrf_failure(request, reason=""):
#     ...
# for more information:
# https://docs.djangoproject.com/en/1.11/ref/settings/#csrf-failure-view
CSRF_FAILURE_VIEW = 'django.views.csrf.csrf_failure'
# The name of the request header used for CSRF authentication
CSRF_HEADER_NAME = 'HTTP_X_CSRFTOKEN'
# When using HTTPS this is a list of hosts which are trusted origins for unsafe
# requests. That can make a post request from a domain that is not the where
# the CSRF token was created.
CSRF_TRUSTED_ORIGINS = []
# To use with  CommonMiddleware, ist of compiled regular expression objects
# representing User-Agent strings that are not allowed to visit any page,
# systemwide. Use this for bad robots/crawlers.
DISALLOWED_USER_AGENTS = []

###############################################################################
# Cache Memory configuration
###############################################################################

# Some times when django process a queryset it saves the queryset result on a
# cache database in case is needed in the future.
# You can set multiple cache databases but some extra configurations must be
# done to do such thing.
# BACKEND: the cache backend to use, django options are:
# 'django.core.cache.backends.db.DatabaseCache'
# 'django.core.cache.backends.dummy.DummyCache'
# 'django.core.cache.backends.filebased.FileBasedCache'
# 'django.core.cache.backends.locmem.LocMemCache'
# 'django.core.cache.backends.memcached.MemcachedCache'
# 'django.core.cache.backends.memcached.PyLibMCCache'
# you can set you own custom cache backend for more information:
# https://docs.djangoproject.com/en/1.11/topics/cache/
# LOCATION:
# The location of the cache to use. This might be the directory for
# a file system cache, a host and port for a memcache server, or simply an
# identifying name for a local memory cache.
# KEY_PREFIX:
# When accessing a cache database, data is stored and accesed by using a
# (key,value) method, this key prefix allows to avoid collision when several
# servers are accesing the sabe cache database or if development and production
# user the same database.


# django has by default a function like this that generates the keys to access
# a cache database. That function can be configured here to have an specific
# behavior if is necesary.
def make_key(key, key_prefix, version):
    return ':'.join([key_prefix, str(version), key])

CACHES = {
    'default': {
        'BACKEND': '',
        'LOCATION': '',
        'KEY_PREFIX': '',
        'VERSION': 1,
        'TIMEOUT': 300,  # Keys lifespan on cache
        'KEY_FUNCTION': make_key,
        'OPTIONS': {  # This options vary depending of the backend
            'MAX_ENTRIES': 300  # Maximum number of entries allowed
        }
    }
}


# If your are using per-site caching you will need to configure this settings.
CACHE_MIDDLEWARE_ALIAS = ''  # Name of the cache database for the middleware
# This is a prefix that will be used by the middleware to discern from pages
# cached and other values cached so it will use toghether with the backend
# cache 'KEY_PREFIX' configuration.
CACHE_MIDDLEWARE_KEY_PREFIX = ''
CACHE_MIDDLEWARE_SECONDS = 600  # The default number of seconds to cache a page

###############################################################################
# Security configuration
###############################################################################

# The maximum size in bytes that a request body may be before a
# SuspiciousOperation (RequestDataTooBig) is raised. Set to None to disable the
# check but is not recomended.
DATA_UPLOAD_MAX_MEMORY_SIZE = 2621440  # bytes 2.5 MB approximatelly
# The maximum number of parameters that may be received via GET or POST before
# a SuspiciousOperation (TooManyFields) is raised. Set to None to disable the
# check but is not recomended.
DATA_UPLOAD_MAX_NUMBER_FIELDS = 1000

# This is a list of all available host name for this django application
# It exist due to security reasons, Django uses the host name to populate
# some URLs some times if the app has many hosts example.com happy.com
# it needs someway to know from wich one a request should go, if an user
# is already using lets say example.com, the user will send in a header in
# the request this domain, and django will redirect the user using this value
# in the header only if this value is in this list, allowed_hosts.
# If your are running django on DEBUG=True this list will be ignores and the
# only allowed host will be, localhost or '127.0.0.1'.
# https://docs.djangoproject.com/en/1.11/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    # examples of usage:
    # for a domain
    # 'www.example.com',
    # for a subdomain
    # 'example.com',
    # '*' caracter will match anything, should be used with care
    # 'www.example-*.com'
]
