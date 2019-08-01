from django.db import models

class Like(models.Model):
  slug = models.CharField(max_length=100)
  tracking_id = models.IntegerField()
  url = models.CharField(max_length=500)
  embed_url = models.CharField(max_length=500)
  embed_html = models.CharField(max_length=500)
  title = models.CharField(max_length=500)
  game = models.CharField(max_length=500)
  thumbnail = models.CharField(max_length=500)
  duration = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.slug
