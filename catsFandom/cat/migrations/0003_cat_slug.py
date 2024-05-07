from django.db import migrations, models

def populate_slug(apps, schema_editor):
    Cat = apps.get_model('cat', 'Cat')
    for cat in Cat.objects.all():
        cat.slug = cat.id
        cat.save()

class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0002_cat_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='slug',
            field=models.SlugField(default='', editable=False),
            preserve_default=False,
        ),
        migrations.RunPython(populate_slug),
    ]
