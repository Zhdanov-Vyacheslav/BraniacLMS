# Generated by Django 3.2.13 on 2022-05-29 18:22

from django.db import migrations


def forwards_func(apps, schema_editor):
    # Get model
    Lessons = apps.get_model("mainapp", "Lessons")
    # Create model's objects
    Lessons.objects.create(
        course=1,
        num=1,
        title="Lesson 1",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=1,
        num=2,
        title="Lesson 2",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=1,
        num=3,
        title="Lesson 3",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=1,
        num=4,
        title="Lesson 4",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=1,
        num=5,
        title="Lesson 5",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=1,
        num=6,
        title="Lesson 6",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=1,
        num=7,
        title="Lesson 7",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=1,
        num=8,
        title="Lesson 8",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=2,
        num=1,
        title="Lesson 1",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=2,
        num=2,
        title="Lesson 2",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=2,
        num=3,
        title="Lesson 3",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=2,
        num=4,
        title="Lesson 4",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=2,
        num=5,
        title="Lesson 5",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=2,
        num=6,
        title="Lesson 6",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=2,
        num=7,
        title="Lesson 7",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=2,
        num=8,
        title="Lesson 8",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=3,
        num=1,
        title="Lesson 1",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=3,
        num=2,
        title="Lesson 2",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=3,
        num=3,
        title="Lesson 3",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=3,
        num=4,
        title="Lesson 4",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=3,
        num=5,
        title="Lesson 5",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=3,
        num=6,
        title="Lesson 6",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=3,
        num=7,
        title="Lesson 7",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=3,
        num=8,
        title="Lesson 8",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=4,
        num=1,
        title="Lesson 1",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=4,
        num=2,
        title="Lesson 2",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=4,
        num=3,
        title="Lesson 3",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=4,
        num=4,
        title="Lesson 4",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=4,
        num=5,
        title="Lesson 5",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=4,
        num=6,
        title="Lesson 6",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=4,
        num=7,
        title="Lesson 7",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=4,
        num=8,
        title="Lesson 8",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=5,
        num=1,
        title="Lesson 1",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=5,
        num=2,
        title="Lesson 2",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=5,
        num=3,
        title="Lesson 3",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=5,
        num=4,
        title="Lesson 4",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=5,
        num=5,
        title="Lesson 5",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=5,
        num=6,
        title="Lesson 6",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=5,
        num=7,
        title="Lesson 7",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=5,
        num=8,
        title="Lesson 8",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=6,
        num=1,
        title="Lesson 1",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=6,
        num=2,
        title="Lesson 2",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=6,
        num=3,
        title="Lesson 3",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=6,
        num=4,
        title="Lesson 4",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=6,
        num=5,
        title="Lesson 5",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=6,
        num=6,
        title="Lesson 6",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=6,
        num=7,
        title="Lesson 7",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=6,
        num=8,
        title="Lesson 8",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=7,
        num=1,
        title="Lesson 1",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=7,
        num=2,
        title="Lesson 2",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=7,
        num=3,
        title="Lesson 3",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=7,
        num=4,
        title="Lesson 4",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=7,
        num=5,
        title="Lesson 5",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=7,
        num=6,
        title="Lesson 6",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=7,
        num=7,
        title="Lesson 7",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=7,
        num=8,
        title="Lesson 8",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=8,
        num=1,
        title="Lesson 1",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=8,
        num=2,
        title="Lesson 2",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=8,
        num=3,
        title="Lesson 3",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=8,
        num=4,
        title="Lesson 4",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=8,
        num=5,
        title="Lesson 5",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=8,
        num=6,
        title="Lesson 6",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=8,
        num=7,
        title="Lesson 7",
        description="Описание урока",
    )
    Lessons.objects.create(
        course=8,
        num=8,
        title="Lesson 8",
        description="Описание урока",
    )


def reverse_func(apps, schema_editor):
    # Get model
    Lessons = apps.get_model("mainapp", "Lessons")
    # Delete objects
    Lessons.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
