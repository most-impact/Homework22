from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="price_purchase",
            new_name="price",
        ),
    ]
    