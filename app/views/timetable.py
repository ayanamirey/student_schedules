from rest_framework import generics, permissions
from rest_framework.response import Response
from app.serializers.timetable import PairSerializer, PairCreateSerializer, MyUserUpdateSerializer
from app.models.timetable import Pair
from authorization.models.users import MyUser


class TimeTableAPIList(generics.ListAPIView):
    queryset = Pair.objects.all()
    serializer_class = PairSerializer
    permission_classes = (permissions.IsAuthenticated,)


class TimeTableAPICreate(generics.CreateAPIView):
    queryset = Pair.objects.all()
    serializer_class = PairCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)


class TimeTableAPIUpdate(generics.UpdateAPIView):
    queryset = Pair.objects.all()
    serializer_class = PairCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)


class TimeTableAPIRetrieveDestroy(generics.RetrieveDestroyAPIView):
    queryset = Pair.objects.all()
    serializer_class = PairSerializer
    permission_classes = (permissions.IsAuthenticated,)


class GroupAPIList(generics.ListAPIView):
    """Фильтрация по группам"""

    def list(self, request, *args, **kwargs):
        user_group = MyUser.objects.get(username=request.user)
        queryset = Pair.objects.all().filter().filter(group=user_group.group_id)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    serializer_class = PairSerializer
    permission_classes = (permissions.IsAuthenticated,)


class DayAPIList(generics.ListAPIView):
    """Фильтрация по дням недели"""

    def list(self, request, pk, *args, **kwargs):
        queryset = Pair.objects.all().filter(day=pk)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    serializer_class = PairSerializer
    permission_classes = (permissions.IsAuthenticated,)


class TeacherAPIList(generics.ListAPIView):
    """Фильтрация учителей по id"""

    def list(self, request, pk, *args, **kwargs):
        queryset = Pair.objects.all().filter(lessons__teacher=pk)
        print(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    serializer_class = PairSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserGroupUpdate(generics.UpdateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserUpdateSerializer