from django.db import models


class Region(models.Model):
    title = models.CharField(
        max_length=128,
    )

    def __str__(self) -> str:
        return self.title


class District(models.Model):
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, related_name="districts"
    )
    title = models.CharField(
        max_length=128,
    )

    def __str__(self) -> str:
        return self.title


class School(models.Model):
    title = models.CharField(max_length=128)
    district = models.ForeignKey(
        District, on_delete=models.CASCADE, related_name="schools"
    )

    def __str__(self) -> str:
        return self.title


class Student(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name="students"
    )
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name


class Result(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="results"
    )
    correct_answers = models.IntegerField()
    total_answers = models.IntegerField()

    percentage = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    ball = models.FloatField(default=0)

    def __str__(self) -> str:
        return self.student.first_name + ' ' + str(self.percentage) + '% (' + self.student.school.district.title + ')'

    @property
    def ball_calc(self):
        if self.percentage <= 100 and self.percentage > 80:
            self.ball = 1
            self.save()
        elif self.percentage <= 80 and self.percentage > 50:
            self.ball = 0.5
            self.save()
