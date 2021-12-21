from rest_framework import serializers
from .signals import my_handler
from .models import Student, SubGroup, SuperGroup, Group


class RegisterStudentSerializer(serializers.ModelSerializer):
    my_handler(sender=Student)
    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'email', 'group', 'password')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubGroup
        fields = ('name', 'is_headman')


class StudentsSerializer(serializers.ModelSerializer):

    group = GroupSerializer()

    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'group')


class RegisterSubGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name', 'is_headman', 'super_group')