from rest_framework import serializers

from .models import Text


class TextSerializer(serializers.ModelSerializer):
    tid = serializers.SerializerMethodField()
    html_code = serializers.SerializerMethodField()
    create_time = serializers.DateTimeField(format="%Y-%m-%d, %H:%M:%S")

    class Meta:
        model = Text
        fields = (
            'tid', 'text', 'code_lang', 'create_time', 'html_code'
        )

    def get_tid(self, obj):
        return obj.id

    def get_html_code(self, obj):
        html_code = """<pre><code class="language-{}">{}</code></pre>""".format(obj.code_lang, obj.text)
        return html_code
