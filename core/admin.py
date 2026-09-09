from django.contrib import admin
from django.utils.html import format_html

from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    def changelist_view(self, request, extra_context=None):
        new_messages = ContactMessage.objects.filter(
            is_read=False
        ).count()

        extra_context = extra_context or {}

        extra_context["new_messages_count"] = new_messages

        return super().changelist_view(
            request,
            extra_context=extra_context
        )

    list_display = (
        "name",
        "email",
        "subject",
        "message_preview",
        "status_display",
        "created_at",
    )

    list_filter = (
        "is_read",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "subject",
        "message",
    )

    ordering = ("-created_at",)

    readonly_fields = ("created_at",)

    actions = (
        "mark_as_read",
        "mark_as_unread",
    )

    fieldsets = (
        (
            "Contact Information",
            {
                "fields": (
                    "name",
                    "email",
                    "subject",
                )
            },
        ),
        (
            "Message",
            {
                "fields": (
                    "message",
                )
            },
        ),
        (
            "Message Status",
            {
                "fields": (
                    "is_read",
                    "created_at",
                )
            },
        ),
    )

    @admin.display(description="Message")
    def message_preview(self, obj):
        if not obj.message:
            return "-"

        preview = obj.message.replace("\n", " ").strip()

        if len(preview) > 60:
            preview = preview[:60] + "..."

        return preview

    @admin.display(description="Status", ordering="is_read")
    def status_display(self, obj):
        if obj.is_read:
            return format_html(
                "<strong style='color: green'>{}</strong>",
                "✓ READ",
            )

        return format_html(
            "<strong style='color: red'>{}</strong>",
            "● NEW",
        )

    @admin.action(description="Mark selected messages as read")
    def mark_as_read(self, request, queryset):
        updated = queryset.update(is_read=True)

        self.message_user(
            request,
            f"{updated} message(s) marked as read."
        )

    @admin.action(description="Mark selected messages as unread")
    def mark_as_unread(self, request, queryset):
        updated = queryset.update(is_read=False)

        self.message_user(
            request,
            f"{updated} message(s) marked as unread."
        )