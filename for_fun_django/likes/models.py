from django.db import models

class Like(models.Model):
  slug = models.CharField()
  tracking_id = models.IntegerField()
  url = models.CharField()
  embed_url = models.CharField()
  embed_html = models.CharField()
  title = models.CharField()
  game = models.CharField()
  thumbnail = models.CharField()
  duration = models.IntegerField()

  def __str__(self):
    return self.slug
