from django.db import models


class Poll(models.Model):
    title = models.CharField(max_length=500, unique=True, null=False)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField(null=False)

    def __str__(self):
        return self.title


class Question(models.Model):
    ANSWER_TEXT = 'text'
    ANSWER_SINGLE = 'single'
    ANSWER_MULTIPLE = 'multiple'
    QUESTION_TYPES = (
        (ANSWER_TEXT, 'Text answer'),
        (ANSWER_SINGLE, 'Single choice'),
        (ANSWER_MULTIPLE, 'Multiple choices'),
    )
    poll = models.ForeignKey('Poll', related_name='questions', on_delete=models.CASCADE)
    text = models.TextField(null=False)
    question_type = models.CharField(max_length=15, choices=QUESTION_TYPES)

    def __str__(self):
        return self.text


class AnswerVariant(models.Model):
    question = models.ForeignKey('Question', related_name='variants', on_delete=models.CASCADE)
    text = models.TextField(null=False)

    def __str__(self):
        return self.text


class PollParticipation(models.Model):
    poll = models.ForeignKey('Poll', on_delete=models.CASCADE)
    participant_id = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)


class ParticipantAnswer(models.Model):
    poll_participation = models.ForeignKey('PollParticipation', related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    text = models.TextField(null=True)


class ChosenVariant(models.Model):
    answer = models.ForeignKey('ParticipantAnswer', related_name='variants', on_delete=models.CASCADE)
    variant = models.ForeignKey('AnswerVariant', on_delete=models.PROTECT)
