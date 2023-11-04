from django.db import models
from django.db.models.functions import Coalesce, JSONObject
from django.contrib.postgres.expressions import ArraySubquery

from school.models import School, Student, District, Region, Result


def district_ball():
    districts = District.objects.all().annotate(
        district_ball=Coalesce(
            models.Sum(
                models.F('schools__students__results__ball')
            ),
            0,
            output_field=models.FloatField()
        )
    )
    return districts


def school_res():
    school_query = (
        School.objects.filter(district_id=models.OuterRef('id'))
        .annotate(
            school_result=Coalesce(
                models.Avg(
                    models.F('students__results__correct_answers')
                    * 100
                    / models.F('students__results__total_answers')

                ),
                0,
                output_field=models.FloatField()
            )
        )
        .annotate(
            json_object=JSONObject(
                title=models.F('title'), result=models.F('school_result')
            )
        )
        .values_list('json_object', flat=True)
    )
    districts = District.objects.all().annotate(school=ArraySubquery(school_query))
    # for d in districts:
    #     print(d.school)
    return districts
