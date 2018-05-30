from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'

    def ready(self):
        import blog.signals
        # post_save.connect(create_user_profile, sender=User)
        # post_save.connect(save_user_profile, sender=User)
