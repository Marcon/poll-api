from django.utils import timezone
from rest_framework.serializers import ValidationError


class ActivePollValidator:

    def __call__(self, value):
        now = timezone.now()
        if value['poll'].start_date >= now or value['poll'].end_date <= now:
            raise ValidationError('Poll "%s" is inactive' % value['poll'])
