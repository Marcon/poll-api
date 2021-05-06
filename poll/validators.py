from django.utils import timezone
from rest_framework.serializers import ValidationError


class ActivePollValidator:

    def __call__(self, value):
        now = timezone.now()
        if value['poll'].start_date >= now or value['poll'].end_date <= now:
            raise ValidationError('Poll "%s" is inactive' % value['poll'])


class AnswerVariantValidator:

    def __call__(self, value):
        question = value['question']
        if question.question_type == 'text':
            if 'text' not in value or len(value['text']) == 0:
                raise ValidationError('question "%s" should have text answer' % question)
            if 'variants' in value and len(value['variants']) > 0:
                raise ValidationError('question "%s" should not have variant choices' % question)
        elif question.question_type == 'single':
            if 'variants' not in value or len(value['variants']) != 1:
                raise ValidationError('question "%s" should have exactly one variant chosen' % question)
            if 'text' in value and len(value['text']) > 0:
                raise ValidationError('question "%s" should not have text answer' % question)
        elif question.question_type == 'multiple':
            if 'variants' not in value or len(value['variants']) == 0:
                raise ValidationError('question "%s" should have at least one variant chosen' % question)
            if 'text' in value and len(value['text']) > 0:
                raise ValidationError('question "%s" should not have text answer' % question)
