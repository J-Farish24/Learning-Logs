import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_log.settings')

import django
django.setup()

from MainApp.models import Topic, Entry

topics = Topic.objects.all()

for topic in topics:
    print(topic.id, topic)

t = Topic.objects.get(id=1)

print(t.text)
print(t.data_added)

entries = t.entry_set.all()

for entry in entries:
    print(entry)