from django.db import models

class TaskList(models.Model):
    name = models.CharField(max_length=255, verbose_name="목록 이름")

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name="제목")
    description = models.TextField(verbose_name="설명", blank=True, null=True)
    urgency = models.IntegerField(choices=[(1, '긴급'), (2, '긴급하지 않음')], verbose_name="긴급도")
    importance = models.IntegerField(choices=[(1, '중요'), (2, '중요하지 않음')], verbose_name="중요도")
    category = models.IntegerField(choices=[
        (1, '중요하고 긴급함'),
        (2, '중요하지만 긴급하지 않음'),
        (3, '긴급하지만 중요하지 않음'),
        (4, '중요하지도 긴급하지 않음')
    ], default=4, verbose_name="카테고리")
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name="tasks", verbose_name="할일 목록")

    def save(self, *args, **kwargs):
        if self.urgency == 1 and self.importance == 1:
            self.category = 1
        elif self.urgency == 2 and self.importance == 1:
            self.category = 2
        elif self.urgency == 1 and self.importance == 2:
            self.category = 3
        else:
            self.category = 4
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
