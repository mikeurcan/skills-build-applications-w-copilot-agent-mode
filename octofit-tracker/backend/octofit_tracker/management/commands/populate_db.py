from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel', description='Marvel Team')
        dc = Team.objects.create(name='dc', description='DC Team')

        # Create users
        users = [
            User.objects.create(email='ironman@marvel.com', name='Tony Stark', team='marvel'),
            User.objects.create(email='captain@marvel.com', name='Steve Rogers', team='marvel'),
            User.objects.create(email='batman@dc.com', name='Bruce Wayne', team='dc'),
            User.objects.create(email='wonderwoman@dc.com', name='Diana Prince', team='dc'),
        ]


        # Create activities (denormalized user fields)
        Activity.objects.create(user_email=users[0].email, user_name=users[0].name, user_team=users[0].team, type='run', duration=30, date=timezone.now().date())
        Activity.objects.create(user_email=users[1].email, user_name=users[1].name, user_team=users[1].team, type='cycle', duration=45, date=timezone.now().date())
        Activity.objects.create(user_email=users[2].email, user_name=users[2].name, user_team=users[2].team, type='swim', duration=25, date=timezone.now().date())
        Activity.objects.create(user_email=users[3].email, user_name=users[3].name, user_team=users[3].team, type='yoga', duration=60, date=timezone.now().date())

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='easy')
        Workout.objects.create(name='Squats', description='Do 30 squats', difficulty='medium')
        Workout.objects.create(name='Plank', description='Hold plank for 1 min', difficulty='hard')

        # Create leaderboard (denormalized team fields)
        Leaderboard.objects.create(team_name=marvel.name, team_description=marvel.description, points=150)
        Leaderboard.objects.create(team_name=dc.name, team_description=dc.description, points=120)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
