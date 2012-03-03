# Volt default configurations file fixture

from os.path import join

from volt.config.base import Config


VOLT = Config(
    USER_CONF = 'voltconf.py',
    CONTENT_DIR = 'content',
    TEMPLATE_DIR = 'templates',
    SITE_DIR = 'site',
    IGNORE_PATTERN = '_*.html',
)

SITE = Config(
    TITLE = 'Title in default',
    DESC = 'Desc in default', 
    ENGINES = (),
    PLUGINS = (('',[]),),
)

BLOG = Config(
    URL = 'blog',
    PERMALINK = '{time:%Y/%m/%d}/{slug}',
    CONTENT_DATETIME_FORMAT = '%Y/%m/%d %H:%M',
    DISPLAY_DATETIME_FORMAT = '%A, %d %B %Y',
    GLOBAL_FIELDS = {'author': ''},
    POSTS_PER_PAGE = 10,
    CONTENT_DIR = join(VOLT.CONTENT_DIR, 'blog'),
    UNIT_TEMPLATE_FILE = join(VOLT.TEMPLATE_DIR, '_post.html'),
    PACK_TEMPLATE_FILE = join(VOLT.TEMPLATE_DIR, '_pagination.html'),
    SORT = '-time',
    PROTECTED = ('id', 'content', ),
    REQUIRED = ('title', 'time', ),
    FIELDS_AS_DATETIME = ('time', ),
    FIELDS_AS_LIST = ('tags', 'categories', ),
    LIST_SEP = ', '
)

PLAIN = Config(
    URL = '/',
    PERMALINK = '{slug}',
    CONTENT_DATETIME_FORMAT = '%Y/%m/%d %H:%M',
    DISPLAY_DATETIME_FORMAT = '%A, %d %B %Y',
    CONTENT_DIR = join(VOLT.CONTENT_DIR, 'plain'),
    UNIT_TEMPLATE_FILE = join(VOLT.TEMPLATE_DIR, '_plain.html'),
    REQUIRED = ('title', ),
    GLOBAL_FIELDS = {},
    PROTECTED = ('id', 'content', 'parent', ),
    FIELDS_AS_DATETIME = ('time', ),
    FIELDS_AS_LIST = ('tags', 'categories', ),
    LIST_SEP = ', '
)

PLUGINS = Config()

JINJA2 = Config(
    TESTS = dict(),
    FILTERS = dict(),
)
