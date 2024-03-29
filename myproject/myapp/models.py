from django.db import models

# Create your models here.

class FIXTURE(models.Model):
    Round_number=models.CharField(max_length=10)
    Team_1 = models.CharField(max_length=10)
    Team_2=models.CharField(max_length=10)
    Date=models.CharField(max_length=10)
    Location=models.CharField(max_length=20)
    Group=models.CharField(max_length=1)

    def __str__(self):
        return self.Round_number
    
class ICC_RANKING(models.Model):
    Team_name=models.CharField(max_length=10)
    Team_ranking=models.IntegerField()
    Rating=models.IntegerField()

    def __str__(self):
        return self.Team_name
    
class RESULTS(models.Model):
    Date=models.CharField(max_length=10)
    Team_1=models.CharField(max_length=10)
    Team_2=models.CharField(max_length=10)
    Winner=models.CharField(max_length=10)
    Margin=models.CharField(max_length=20)
    Ground=models.CharField(max_length=20)
    
    def __str__(self):
        return self.Date

class LOGIN(models.Model):
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=10)

    def __str__(self):
        return self.Username