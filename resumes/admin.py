
from django.contrib import admin, messages
from .models import Resume
from .utils import extract_resume_text


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):

    list_display = ("user", "file", "uploaded_at")

    readonly_fields = ("extracted_text", "uploaded_at")

    def save_model(self, request, obj, form, change):

        super().save_model(request, obj, form, change)

        if obj.file and not obj.extracted_text:

            try:
                extracted_text = extract_resume_text(obj.file.path)

                obj.extracted_text = extracted_text

                obj.save(update_fields=["extracted_text"])

                self.message_user(
                    request,
                    "Resume text extracted successfully!",
                    level=messages.SUCCESS
                )

            except Exception as error:

                self.message_user(
                    request,
                    f"Extraction failed: {error}",
                    level=messages.WARNING
                )
