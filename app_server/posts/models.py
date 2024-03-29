from collections import Counter

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager

User = get_user_model()


class Post(models.Model):
    # STATUS_CHOICES = (
    #     ('draft', 'Draft'),
    #     ('published', 'Published'),
    # )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    link = models.URLField(max_length=200, blank=True, unique=False)
    tags = TaggableManager(blank=True)
    tag_descriptions = models.ManyToManyField("TagDescription", blank=True)
    labels = models.CharField(max_length=200, blank=True)
    text = models.CharField(max_length=20000, blank=True)
    upload = models.FileField(upload_to="uploads/", null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    likes = models.ManyToManyField(User, blank=True, related_name="liked_posts")
    title_tag = models.CharField(max_length=200, null=True, blank=True, unique=False)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    spaces = models.ManyToManyField("spaces.Space", related_name="posts", blank=True)
    # status = models.CharField(max_length=10,
    #                           choices=STATUS_CHOICES,
    #                           default='draft')

    def total_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ("-published_date",)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", args=[self.id])

    # add tags counter for recommendations
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        for space in self.spaces.all():
            space.update_tags_counter()

    # update tags counter for recommendations
    def update_tags_counter(self):
        tags = self.tags.all()
        self.spaces.annotate(tags_counter=Counter(tags))

        # Update the tags_counter field in Space model
        for space in self.spaces.all():
            space.tags_counter = Counter(tags)
            space.save()

    def get_labels_list(self):
        return self.labels.split(",") if self.labels else []


class TagDescription(models.Model):
    tag = models.ForeignKey("taggit.Tag", on_delete=models.CASCADE, related_name="tag_description")
    description = models.CharField(max_length=200, blank=True, unique=False)

    def __str__(self):
        return f"{self.tag.name}: {self.description}"


class Comment(models.Model):
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    class Meta:
        ordering = ("created_date",)
        indexes = [
            models.Index(fields=["created_date"]),
        ]

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
