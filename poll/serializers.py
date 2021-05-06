from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Poll, Question, AnswerVariant, PollParticipation, ParticipantAnswer, ChosenVariant


class PollSerializer(ModelSerializer):
    class Meta:
        model = Poll
        fields = ['id', 'title', 'start_date', 'end_date']


class AnswerVariantSerializer(ModelSerializer):
    question = serializers.PrimaryKeyRelatedField(many=False, queryset=Question.objects.all())

    class Meta:
        model = AnswerVariant
        fields = ['id', 'question', 'text']


class QuestionSerializer(ModelSerializer):

    variants = AnswerVariantSerializer(many=True, read_only=True, required=False)
    poll = serializers.PrimaryKeyRelatedField(many=False, queryset=Poll.objects.all())

    class Meta:
        model = Question
        fields = ['id', 'poll', 'text', 'question_type', 'variants']


class ChosenVariantSerializer(ModelSerializer):
    class Meta:
        model = ChosenVariant
        fields = ['id', 'answer', 'variant']


class ParticipantAnswerSerializer(ModelSerializer):
    variants = serializers.PrimaryKeyRelatedField(many=True, required=False, queryset=AnswerVariant.objects.all())

    class Meta:
        model = ParticipantAnswer
        fields = ['id', 'question', 'text', 'variants']


class PollParticipationSerializer(ModelSerializer):
    answers = ParticipantAnswerSerializer(many=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        participation = PollParticipation(poll=validated_data['poll'], participant_id=validated_data['participant_id'])
        participation.save()
        for ans in validated_data['answers']:
            answer = ParticipantAnswer(poll_participation=participation, question=ans['question'])
            if 'text' in ans:
                answer.text = ans['text']
            answer.save()
            if 'variants' in ans:
                for var in ans['variants']:
                    ChosenVariant(answer=answer, variant=var).save()
        return participation

    class Meta:
        model = PollParticipation
        fields = ['id', 'poll', 'participant_id', 'date', 'answers']
