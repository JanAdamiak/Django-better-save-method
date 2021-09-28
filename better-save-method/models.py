from django.db import models

class OverwrittenModel(models.Model):
    """
    An abstract base class model that provides hooks
    in the save method for better organised code.
    """

    def pre_default_methods_funcs_hook(self):
        """
        """
        pass

    def update_object(self):
        """
        """
        pass

    def create_object(self):
        """
        """
        pass

    def post_default_funcs_hook(self):
        """
        """
        pass

    def pre_save_post_funcs_validation(self):
        """
        """
        pass

    def post_save_triggers(self):
        """
        """
        pass

    def save(self, *args, **kwargs):
        """
        """
        self.pre_default_methods_funcs_hook()

        if self.pk:
            self.update_object()
        else:
            self.create_object()

        self.post_default_funcs_hook()
        self.pre_save_post_funcs_validation()
        super().save(*args, **kwargs)
        self.post_save_triggers()