from django.db import models

from .validators import validate_annotation_type, validate_iri


class Annotation(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    context = models.CharField(max_length=255, default="http://www.w3.org/ns/anno.jsonld", validators=[validate_iri])
    type = models.CharField(max_length=255, default="Annotation", validators=[validate_annotation_type])
    body = models.JSONField(max_length=255)
    target = models.JSONField(max_length=255)
    creation_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["creation_datetime"]
        verbose_name = "annotation"
        verbose_name_plural = "annotations"
