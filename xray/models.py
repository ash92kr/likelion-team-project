from django.db import models
from django.conf import settings
from django.urls import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


def post_image_path(instance, filename):
    return 'image/{}/{}'.format(instance.pk, filename)

class Xray(models.Model):
    image = ProcessedImageField(
                upload_to=post_image_path,
                processors=[ResizeToFill(300,300)],
                format='JPEG',
                options={'quality':90},
                )
#models.ImageField()
    def get_absolute_url(self):
         return reverse('xray:detail', kwargs={'pk': self.pk})


    