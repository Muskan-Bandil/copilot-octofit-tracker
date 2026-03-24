from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        if connection.connection is None:
            connection.ensure_connection()
        db = connection.connection.client['octofit_db']
        # Clear collections
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Teams
        marvel_team = {'name': 'Team Marvel', 'description': 'Marvel superheroes'}
        dc_team = {'name': 'Team DC', 'description': 'DC superheroes'}
        marvel_team_id = db.teams.insert_one(marvel_team).inserted_id
        dc_team_id = db.teams.insert_one(dc_team).inserted_id

        # Users
        users = [
            {'username': 'Muskan-Bandil', 'email': 'muskanbandil@gmail.com', 'team_id': marvel_team_id},
            {'username': 'Spider-Man', 'email': 'spiderman@marvel.com', 'team_id': marvel_team_id},
            {'username': 'Iron Man', 'email': 'ironman@marvel.com', 'team_id': marvel_team_id},
            {'username': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team_id': dc_team_id},
            {'username': 'Batman', 'email': 'batman@dc.com', 'team_id': dc_team_id},
        ]
        db.users.insert_many(users)
        db.users.create_index('email', unique=True)

        # Activities
        activities = [
            {'user': 'spiderman@marvel.com', 'type': 'run', 'distance': 5},
            {'user': 'ironman@marvel.com', 'type': 'cycle', 'distance': 20},
            {'user': 'wonderwoman@dc.com', 'type': 'swim', 'distance': 2},
            {'user': 'batman@dc.com', 'type': 'walk', 'distance': 3},
        ]
        db.activities.insert_many(activities)

        # Workouts
        workouts = [
            {'user': 'spiderman@marvel.com', 'workout': 'pushups', 'count': 50},
            {'user': 'ironman@marvel.com', 'workout': 'situps', 'count': 40},
            {'user': 'wonderwoman@dc.com', 'workout': 'squats', 'count': 60},
            {'user': 'batman@dc.com', 'workout': 'pullups', 'count': 30},
        ]
        db.workouts.insert_many(workouts)

        # Leaderboard
        leaderboard = [
            {'user': 'spiderman@marvel.com', 'points': 100},
            {'user': 'ironman@marvel.com', 'points': 90},
            {'user': 'wonderwoman@dc.com', 'points': 110},
            {'user': 'batman@dc.com', 'points': 80},
        ]
        db.leaderboard.insert_many(leaderboard)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
