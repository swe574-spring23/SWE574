from django.db.models.signals import post_save
from django.dispatch import receiver

from posts.models import Comment, Post
from spaces.models import Space

from .models import *


@receiver(post_save, sender=Comment)
def award_comment_badge(sender, instance, created, **kwargs):
    if created:
        user = instance.author
        comments_count = Comment.objects.filter(author=user).count()

        if comments_count >= 1:
            badge = Badge.objects.get(name="Commentator")
            user_badge, created = UserBadge.objects.get_or_create(user=user, badge=badge)
            if created:
                "send notification to user"
                user_badge.save()
                pass
        if comments_count >= 2:
            badge = Badge.objects.get(name="Chatty Cathy")
            user_badge, created = UserBadge.objects.get_or_create(user=user, badge=badge)
            if created:
                "send notification to user"
                user_badge.save()
                pass

        if comments_count >= 3:
            badge = Badge.objects.get(name="Comment King")
            user_badge, created = UserBadge.objects.get_or_create(user=user, badge=badge)
            if created:
                "send notification to user"
                user_badge.save()
                pass


@receiver(post_save, sender=Space)
def award_space_badge(sender, instance, created, **kwargs):
    if created:
        user = instance.owner
        space_count = Space.objects.filter(owner=user).count()

        if space_count >= 1:
            badge = Badge.objects.get(name="Explorer")
            user_badge, created = UserBadge.objects.get_or_create(user=user, badge=badge)
            if created:
                "send notification to user"
                user_badge.save()
                pass
        if space_count >= 2:
            badge = Badge.objects.get(name="Organizer")
            user_badge, created = UserBadge.objects.get_or_create(user=user, badge=badge)
            if created:
                "send notification to user"
                user_badge.save()
                pass

        if space_count >= 3:
            badge = Badge.objects.get(name="Space Star")
            user_badge, created = UserBadge.objects.get_or_create(user=user, badge=badge)
            if created:
                "send notification to user"
                user_badge.save()
                pass


@receiver(post_save, sender=Post)
def award_post_badge(sender, instance, created, **kwargs):
    if created:
        user = instance.author
        post_count = Post.objects.filter(author=user).count()

        if post_count >= 1:
            badge = Badge.objects.get(name="Post Duck")
            user_badge, created = UserBadge.objects.get_or_create(user=user, badge=badge)
            if created:
                "send notification to user"
                user_badge.save()
                pass
        if post_count >= 2:
            badge = Badge.objects.get(name="Prolific Poster")
            user_badge, created = UserBadge.objects.get_or_create(user=user, badge=badge)
            if created:
                "send notification to user"
                user_badge.save()
                pass

        if post_count >= 3:
            badge = Badge.objects.get(name="Post King")
            user_badge, created = UserBadge.objects.get_or_create(user=user, badge=badge)
            if created:
                "send notification to user"
                user_badge.save()
                pass