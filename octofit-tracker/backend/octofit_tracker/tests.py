from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(username='testuser', email='test@example.com', first_name='Test', last_name='User')
        self.assertEqual(user.username, 'testuser')

class TeamModelTest(TestCase):
    def test_create_team(self):
        user = User.objects.create(username='member', email='member@example.com', first_name='Mem', last_name='Ber')
        team = Team.objects.create(name='Test Team')
        team.members.add(user)
        self.assertIn(user, team.members.all())

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(username='active', email='active@example.com', first_name='Ac', last_name='Tive')
        activity = Activity.objects.create(user=user, activity_type='Running', duration=30, calories_burned=300, date=timezone.now().date())
        self.assertEqual(activity.activity_type, 'Running')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Cardio', description='Cardio session', difficulty='Medium', duration=45)
        self.assertEqual(workout.name, 'Cardio')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard_entry(self):
        user = User.objects.create(username='leader', email='leader@example.com', first_name='Lead', last_name='Er')
        entry = Leaderboard.objects.create(user=user, score=1000, rank=1)
        self.assertEqual(entry.rank, 1)
