from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=60)
    username = models.CharField(max_length=32, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=60)
    profile_picture = models.CharField(max_length=60, default="sample_profile_picture.png")

    def __str__(self):
        return f"({self.name}, {self.username}, {self.email}, {self.password}, {self.profile_picture})"

class Admin(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.person.__str__()

class Sponsor(models.Model):
    company_name = models.CharField(max_length=60)
    industry = models.CharField(max_length=60)
    budget = models.IntegerField(default=0)
    person = models.OneToOneField(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.person.__str__()[:-1]}, {self.company_name}, {self.industry}, {self.budget})"

class Influencer(models.Model):
    category = models.CharField(max_length=60)
    niche = models.CharField(max_length=60)
    reach = models.IntegerField(default=0)
    person = models.OneToOneField(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.person.__str__()[:-1]}, {self.category}, {self.niche}, {self.reach})"

class Campaign(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=360)
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.IntegerField(default=0)
    goals = models.CharField(max_length=250)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    influencers = models.ManyToManyField(Influencer)

    def __str__(self):
        return f"({self.name}, {self.description}, {self.start_date}, {self.end_date}, {self.budget}, {self.goals}, {self.sponsor.id}, {[influencer.id for influencer in self.influencers]})"

class Message(models.Model):
    message = models.CharField(max_length=240)
    sponsor = models.ForeignKey(Sponsor, null=True, on_delete=models.CASCADE)
    influencer = models.ForeignKey(Influencer, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"({self.message}, {self.sponsor.id}, {self.influencer.id})"


class ADRequest(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    influencer = models.ForeignKey(Influencer, on_delete=models.CASCADE)
    requirements = models.CharField(max_length=240)
    payment_amount = models.IntegerField(default=0)
    status = models.CharField(max_length=8, choices=[("status", "status"), ("accepted", "accepted"), ("rejected", "rejected")])
    messages = models.ManyToManyField(Message)

    def __str__(self):
        return f"({self.campaign.id}, {self.influencer.id}, {self.requirements}, {self.payment_amount}, {self.status}, {[message.id for message in self.messages]})"