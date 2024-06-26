from django.db import models
from users.models import User

class Message(models.Model):
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    issue = models.ForeignKey("Issue", on_delete=models.CASCADE)

class Issue(models.Model):
    title = models.CharField(max_length=100)
    status = models.PositiveSmallIntegerField()

    junior = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="junior_issues",
    )

    senior = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="senior_issues",
        null=True,
    )

    def __repr__(self) -> str:
        return f"Issue[{self.pk}{self.title[:10]}]"
