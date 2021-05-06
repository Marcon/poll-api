from django.utils import timezone
from rest_framework import generics

from poll.models import Poll, Question, AnswerVariant, PollParticipation
from poll.serializers import PollSerializer, PollUpdateSerializer, QuestionSerializer, AnswerVariantSerializer, PollParticipationSerializer
from poll.permissions import AdminOrReadOnly


class PollListView(generics.ListCreateAPIView):
    queryset = Poll.objects.filter(start_date__lte=timezone.now(), end_date__gte=timezone.now())
    serializer_class = PollSerializer
    permission_classes = [AdminOrReadOnly, ]


class PolDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.filter(start_date__lte=timezone.now(), end_date__gte=timezone.now())
    permission_classes = [AdminOrReadOnly, ]

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return PollUpdateSerializer
        return PollSerializer


class QuestionListView(generics.ListCreateAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [AdminOrReadOnly, ]

    def get_queryset(self):
        if 'poll_id' in self.request.query_params:
            return Question.objects.filter(poll_id=self.request.query_params['poll_id'])
        return Question.objects.all()


class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [AdminOrReadOnly, ]


class AnswerVariantListView(generics.ListCreateAPIView):
    serializer_class = AnswerVariantSerializer
    permission_classes = [AdminOrReadOnly, ]

    def get_queryset(self):
        if 'question_id' in self.request.query_params:
            return AnswerVariant.objects.filter(question_id=self.request.query_params['question_id'])
        return AnswerVariant.objects.all()


class AnswerVariantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnswerVariant.objects.all()
    serializer_class = AnswerVariantSerializer
    permission_classes = [AdminOrReadOnly, ]


class PollParticipationView(generics.CreateAPIView):
    queryset = PollParticipation.objects.all()
    serializer_class = PollParticipationSerializer


class PollParticipationDetailsView(generics.RetrieveAPIView):
    queryset = PollParticipation.objects.all()
    serializer_class = PollParticipationSerializer
    lookup_field = 'participant_id'
