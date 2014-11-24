from django.utils.html import format_html
from django.conf import settings
from wagtail.wagtailcore import hooks

@hooks.register('insert_editor_js')
def enable_justify():
    return format_html(
        """
        <script>
            registerHalloPlugin('hallojustify');
        </script>
        """
    )
